"""
forge-ledger.py - make the ledger of a project at read time from its
documents (SOL.0680 of the forge solution design; POS.1600 to
POS.1640): the tables of templates/ledger.md, the Waiting rule, the
reports of what the merged files cannot say, the archive for what has
no record of the new shape.

SYNOPSIS
    python scripts/forge-ledger.py <slug> [--out PATH]

WHAT IT DOES
    Reads eleven kinds of document and builds `ledger.md` in the shape
    of templates/ledger.md, the template's own comments kept:
    the project file (the header; a project of the shape before the
    migration, templates/project.md, gives its hand-kept ledger's
    header instead), the
    artefacts' headers (Briefs, Documents), the histories (the date of
    a document, the mining of a brief, the state of a work product,
    the `closed` record of a finding or a challenge), the decisions
    (the Verdict lines), the resource indexes (Sources, Research), the
    reviews and the challenges (Findings, Challenges), the provenance
    of the renders and of the documentation index (Renders), the
    published companions (Published, the state current or stale
    against the render's generated date), the work specifications
    (Work), the threads (Waiting) and `ledger.archive.md`, read for
    every item without a record of the new shape, a newer record
    overriding it; a project not yet migrated is read whole from its
    hand-kept ledger as the archive. Dependencies are the citations of
    `projects/lib-*/` anywhere in the project.

    Waiting on principal and the Reports section follow the rule and
    the list of templates/ledger.md, where each is defined; a closed
    thread's later commit is found through forge_repos. An
    unparsable file is a line `unparsed: <file>:<line>` in the
    header, never a crash; the exit code is 0 (POS.1600).

    Writes `ledger.md` only where it is out of git's index; where it
    is tracked, the script refuses to write and prints to stdout or
    to --out PATH, the dry run of a real project going to tmp/. The
    slug `forge` is the engine's own project.

WHAT IT NEEDS
    Python 3.8 or newer; git on PATH. forge_docs.py, forge_repos.py
    and forge_tools.py beside it; templates/ledger.md.

EXAMPLES
    python scripts/forge-ledger.py fixture                     # the fixture's ledger, written
    python scripts/forge-ledger.py flow-ba --out tmp/flow-ba-ledger.md   # a dry run
    python scripts/forge-ledger.py forge                       # the engine's own project
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import forge_docs as fd  # noqa: E402
import forge_repos as fr  # noqa: E402
import forge_tools as ft  # noqa: E402

TEMPLATE = fr.ENGINE_ROOT / "templates" / "ledger.md"
TODAY = datetime.date.today().isoformat()
LIBRARY_DROPS = ("Briefs", "Documents", "Published", "Work", "Challenges")
FND_CHECK_RE = re.compile(r"^### (FND\.\d{4,5}) — (\w+) [—-] (.*)$")
FND_CRIT_RE = re.compile(r"^### (FND\.\d{4,5}) \[(\w+)\](?: \[([^\]]+)\])? [—-] (.*)$")
CHL_RE = re.compile(r"^### (CHL\.\d{4,5}) — (.*)$")
VERDICT_RE = re.compile(r"\*\*Verdict:\*\*\s*([A-Z]{3}\.\d{4,5})\s+(rejected|parked(?: until .*?)?|obsolete)\s*$")
DEF_RE = re.compile(r"^- \*\*([A-Z]{3}\.\d{4,5})\*\*")


class Project:
    def __init__(self, slug):
        self.slug = slug
        self.repo = fr.ENGINE_ROOT if slug == "forge" else fr.project_path(slug)
        self.proj = fr.ENGINE_ROOT / "projects" / "forge" if slug == "forge" else fr.project_path(slug)
        if not self.proj.is_dir():
            fr.fail(f"Project '{slug}' not found ({self.proj} does not exist).")
        self.root = fr.ENGINE_ROOT if slug == "forge" else self.proj  # where the root renders lie
        self.reports = []
        info = fr.project_file(self.proj)  # the one reader of the project file (SOL.0670)
        self.old_shape = info["shape"] != "current"
        self.kind, self.language = info["kind"], info["language"]
        archive = self.proj / "ledger.md" if self.old_shape else self.proj / "ledger.archive.md"
        self.archive = fd.tables(fd.read(archive)) if archive.exists() else {}
        afront, _ = fd.split_front(fd.read(archive)) if archive.exists() else (None, "")
        self.archive_date = fd.front_value(afront, "updated") or "0000-00-00"
        self.histories = {p: fd.records(p) for p in sorted(self.proj.rglob("*.history.md"))}

    def rel(self, path):
        return Path(path).resolve().relative_to(self.proj.resolve()).as_posix() \
            if str(Path(path).resolve()).startswith(str(self.proj.resolve())) else Path(path).name

    def archive_rows(self, section, key):
        return {r.get(key, ""): r for r in self.archive.get(section, [])}

    # -- records across the project
    def closed_records(self):
        """{ID: (date, doc stem, version, reason)} of the newest `closed` record per ID."""
        out = {}
        for p, recs in self.histories.items():
            for r in recs:
                if r["kind"] != "closed":
                    continue
                for id_ in fd.subject_ids(r["subject"]):
                    if not fd.ID_RE.fullmatch(id_):
                        continue
                    if id_ not in out or out[id_][0] <= r["date"]:
                        stem = p.name.replace(".history.md", "")
                        out[id_] = (r["date"], stem, r["version"], r["reason"])
        return out

    def verdicts(self):
        """{ID: (date, DEC, verdict)} from the Verdict lines of decisions.md."""
        out, dec, date, pending = {}, None, None, []
        p = self.proj / "decisions.md"
        if not p.exists():
            return out
        for line in fd.read(p).split("\n"):
            m = re.match(r"^## (DEC\.\d{4,5})", line)
            if m:
                for id_, v in pending:
                    out[id_] = (date or "", dec, v)
                dec, date, pending = m.group(1), None, []
                continue
            m = VERDICT_RE.search(line)
            if m and dec:
                pending.append((m.group(1), m.group(2)))
            m = re.match(r"^- \*\*Date:\*\*\s*(\d{4}-\d{2}-\d{2})", line)
            if m:
                date = m.group(1)
        for id_, v in pending:
            out[id_] = (date or "", dec, v)
        return out

    def version_of(self, path):
        front, _ = fd.front_of(path)
        return fd.front_value(front, "version"), fd.front_value(front, "status"), front

    def newest_record(self, path):
        recs = self.histories.get(path.with_name(path.name.replace(".md", ".history.md")), [])
        return recs[-1] if recs else None


# ------------------------------------------------------------- tables

def briefs(p):
    rows, arch = [], p.archive_rows("Briefs", "File")
    mined = {}
    for r in p.histories.get(p.proj / "10-intent.history.md", []):
        if r["reason"].startswith("mined:"):
            for s in fd.subject_ids(r["subject"]):
                mined[s] = r
    for f in sorted(p.proj.glob("00-brief*.md"), key=lambda q: (q.name != "00-brief.md", q.name)):
        if ".history." in f.name:
            continue
        version, status, _ = p.version_of(f)
        a = arch.get(f.name, {})
        if f.name in mined:
            m = re.match(r"mined:\s*(\w+),?\s*(.*)$", mined[f.name]["reason"])
            state, note = (m.group(1), m.group(2)) if m else ("pending", mined[f.name]["reason"])
        else:
            state, note = a.get("Mined", "pending"), a.get("Note", "—")
        rows.append([f.name, version or a.get("Version", "—"), status or a.get("Status", "—"), state, note or "—"])
    return rows


def documents(p):
    rows, arch = [], p.archive_rows("Documents", "File")
    for f in sorted(p.proj.glob("[0-9][0-9]-*.md")):
        if f.name.startswith("00-brief") or ".history." in f.name or ".threads." in f.name:
            continue
        version, status, front = p.version_of(f)
        # the date of the newest content record: a state record (a mining, a
        # work state, a closing) carries the version without raising it (POS.1630)
        recs = [r for r in p.histories.get(f.with_name(f.name.replace(".md", ".history.md")), [])
                if r["kind"] != "closed" and not re.match(r"^(mined|state):", r["reason"])]
        date = recs[-1]["date"] if recs else (fd.front_value(front, "date") or arch.get(f.name, {}).get("Date", "—"))
        rows.append([f.name, version or "—", status or "—", date])
    return rows


def renders(p):
    rows, candidates = [], []
    for name in ("README.md", "RELEASE-NOTES.md", "CONTRIBUTING.md"):
        f = p.root / name
        if f.exists():
            candidates.append((f, f"{name} (repo root)" if p.slug == "forge" else name))
    candidates += [(f, "renders/" + f.name) for f in sorted(p.proj.glob("renders/*.md"))]
    for f, label in candidates:
        front, _ = fd.front_of(f)
        if front is None or fd.front_value(front, "render") is None:
            continue
        recipe = fd.front_value(front, "recipe") or "—"
        audience = "—"
        m = re.match(r"(recipes/\S+\.md)", recipe)
        if m and (p.proj / m.group(1)).exists():
            rf, _ = fd.front_of(p.proj / m.group(1))
            audience = fd.front_value(rf, "audience") or "—"
        plain = [q.name for q in f.parent.glob(f.stem + ".*") if q.suffix in (".pptx", ".docx", ".mp4")]
        if plain:
            label += " (with " + ", ".join("renders/" + q for q in plain) + ", plain)"
        rows.append([label, audience, recipe, ", ".join(fd.front_list(front, "inputs")) or "—",
                     fd.front_value(front, "generated") or "—"])
    idx = p.root / "docs" / "README.md"
    if idx.exists():
        front, _ = fd.front_of(idx)
        if front is not None and fd.front_value(front, "made") == "derived":
            rows.append(["docs/README.md (the documentation index, kind page)", "the three readers of the documentation",
                         "none: derived by scripts/docs-index.py (SOL.0460)",
                         ", ".join(fd.front_list(front, "inputs")) + f", 10-intent.md v{fd.front_value(front, 'version')}",
                         fd.front_value(front, "generated") or "—"])
    return rows


def published(p):
    rows = []
    for c in sorted(p.proj.glob("published/*.md")):
        front, _ = fd.front_of(c)
        file = fd.front_value(front, "file") or c.stem
        render_prov = fd.front_value(front, "render") or "—"
        m = re.search(r"generated (\d{4}-\d{2}-\d{2})", render_prov)
        state = "stale"
        rf = p.proj / "renders" / (c.stem + ".md")
        if m and rf.exists():
            rfront, _ = fd.front_of(rf)
            state = "current" if fd.front_value(rfront, "generated") == m.group(1) else "stale"
        rows.append([f"published/{file}", fd.front_value(front, "recipe") or "—", render_prov,
                     fd.front_value(front, "model") or "—", fd.front_value(front, "published") or "—", state])
    seen = {r[0] for r in rows}
    for a in p.archive.get("Published", []):  # a published file without a companion yet
        if a.get("File") and a["File"] not in seen:
            rows.append([a["File"], a.get("Recipe", "—"), a.get("From render", "—"), a.get("Model", "—"),
                         a.get("Published", "—"), a.get("State", "stale")])
    return rows


def work(p):
    rows, arch = [], p.archive_rows("Work", "File")
    for s in sorted(p.proj.glob("work/*.spec.md")):
        version, _, front = p.version_of(s)
        file = fd.front_value(front, "file") or ("work/" + s.name.replace(".spec.md", ".md"))
        made, inputs, state = "—", "—", "stale"
        recs = [r for r in p.histories.get(s.with_name(s.name.replace(".spec.md", ".spec.history.md")), [])
                if r["reason"].startswith("state:")]
        if recs:
            m = re.match(r"state:\s*([^;]+?)(?:;\s*made\s+(\S+)\s+from\s+(.*))?$", recs[-1]["reason"])
            if m:
                state, made, inputs = m.group(1).strip(), m.group(2) or recs[-1]["date"], m.group(3) or "—"
        elif file in arch:
            a = arch[file]
            made, inputs, state = a.get("Made", "—"), a.get("Inputs", "—"), a.get("State", "stale")
        rows.append([file, f"work/{s.name} v{version or '—'}", inputs, made, state])
    return rows


def sources(p):
    rows = []
    arch = {r.get("File", "").split()[0] if r.get("File") else "": r for r in p.archive.get("Sources", [])}
    for e in fd.index_entries(p.proj / "sources" / "00-INDEX.md"):
        if e["name"].startswith("projects/lib-"):
            continue  # a pointer to a library's document: a dependency, not a source
        f = e["fields"]
        date, origin, form = "—", "—", f.get("Form", "—")
        if "Date" in f:
            d = f["Date"]
            m = re.match(r"^(.*?),\s*from the (.*)$", d)
            date, origin = (m.group(1), m.group(2)) if m else (d, "—")
        else:
            a = arch.get(e["name"]) or arch.get("sources/" + e["name"]) or {}
            date, origin, form = a.get("Date", "—"), a.get("Date origin", "—"), a.get("Form", form)
        rows.append([e["heading"], date, origin, form])
    return rows


def dependencies(p):
    """Citations of a library's documents in the chain, the indexes,
    the recipes, the work and the research, grouped by the cited
    directory (a bundle, sources/ or research/); the reports, the
    sources and the archive are not read, since they quote."""
    found, arch = {}, {r.get("Path", "").split()[0]: r for r in p.archive.get("Dependencies", []) if r.get("Path")}
    for f in sorted(p.proj.rglob("*.md")):
        top = p.rel(f).split("/")[0]
        if f.name in ("ledger.md", "ledger.archive.md") or top in ("reviews", "challenges", "sources", "published", "renders", "docs"):
            continue
        for m in re.finditer(r"projects/(lib-[\w-]+)/((?:sources|research)/(?:[\w.-]+/)?)?", fd.read(f)):
            if m.group(1) == p.slug:
                continue  # a library citing itself
            path = "projects/" + m.group(1) + "/" + (m.group(2) or "")
            found.setdefault(path, (m.group(1), set()))[1].add(p.rel(f))
    return [[path, lib, ", ".join(sorted(users)), arch.get(path, {}).get("Note", "—")]
            for path, (lib, users) in sorted(found.items())]


def research(p):
    rows = []
    for f in sorted(p.proj.glob("research/*.md")):
        if f.name == "00-INDEX.md":
            continue
        front, _ = fd.front_of(f)
        rows.append([f.name, fd.front_value(front, "date") or f.name[:10], fd.front_value(front, "derived_from") or "—"])
    return rows


def _state(id_, closed, verdicts, arch, accepted_word):
    """(state, resolution) of a finding or a challenge."""
    cands = []
    if id_ in closed:
        d, stem, v, reason = closed[id_]
        cands.append((d, accepted_word, reason or f"{stem} {v}"))
    if id_ in verdicts:
        d, dec, v = verdicts[id_]
        cands.append((d, v.split()[0], dec + (" (" + v[len("parked "):] + ")" if v.startswith("parked until") else "")))
    if cands:
        cands.sort()
        return cands[-1][1], cands[-1][2]
    if id_ in arch:
        a = arch[id_]
        state = a.get("State", "open")
        return ("rejected" if state == "overruled" else state), a.get("Resolution", "—")
    return "open", "—"


def findings(p, closed, verdicts):
    items, arch, reopened = {}, p.archive_rows("Findings", "ID"), {}
    for f in sorted(p.proj.glob("reviews/*.md")):
        lines = fd.read(f).split("\n")
        front, _ = fd.split_front("\n".join(lines))
        date = fd.front_value(front, "date") or f.name[:10]
        for n, line in enumerate(lines):
            m = FND_CHECK_RE.match(line)
            item = [m.group(1), m.group(2), "conformance", m.group(3)] if m else None
            if item is None:
                m = FND_CRIT_RE.match(line)
                item = [m.group(1), m.group(2), m.group(3) or "—", m.group(4)] if m else None
            if item is None:
                continue
            id_, sev, cat, head = item
            # the first report that names the finding is its source; a later
            # one that names it as reopened opens it again from that date
            items.setdefault(id_, [sev, cat, f.name, head])
            known = next((k for k in lines[n + 1:n + 8] if k.startswith("- **Known as:**")), "")
            if "reopened" in known:
                reopened[id_] = (date, f.name)
    for id_, a in arch.items():
        if id_ and id_ not in items:
            items[id_] = [a.get("Severity", "—"), a.get("Category", "—"), a.get("Source review", "—"), ""]
    rows = []
    for id_ in sorted(items, key=lambda i: int(i.split(".")[1])):
        sev, cat, src, _ = items[id_]
        state, res = _state(id_, closed, verdicts, arch, "resolved")
        # a reopening counts when its report is younger than the record or
        # the verdict that settled the finding and than the archive, which
        # already reflects every report before the migration
        if id_ in reopened:
            rdate = reopened[id_][0]
            settled = max([closed.get(id_, ("",))[0], verdicts.get(id_, ("",))[0]])
            if rdate > settled and (id_ not in arch or rdate >= p.archive_date):
                state, res = "open", f"reopened by {reopened[id_][1]}"
        rows.append([id_, sev, cat, state, src, res])
    return rows, items


def challenges(p, closed, verdicts):
    items, arch = {}, p.archive_rows("Challenges", "ID")
    for f in sorted(p.proj.glob("challenges/*.md")):
        lines = fd.read(f).split("\n")
        for n, line in enumerate(lines):
            m = CHL_RE.match(line)
            if m:
                sev = ""
                for look in lines[n + 1:n + 6]:
                    s = re.match(r"^- \*\*Severity:\*\*\s*(\w+)", look)
                    if s:
                        sev = s.group(1)
                        break
                items[m.group(1)] = [m.group(2) + (f" ({sev})" if sev else ""), f.name]
    for id_, a in arch.items():
        if id_ and id_ not in items:
            items[id_] = [a.get("Headline", "—"), a.get("Source review", "—")]
    rows = []
    for id_ in sorted(items, key=lambda i: int(i.split(".")[1])):
        head, src = items[id_]
        state, res = _state(id_, closed, verdicts, arch, "accepted")
        rows.append([id_, state, head, src, res])
    return rows, items


def threads_of(p):
    """(open threads as (id, text), closed thread files)."""
    if p.old_shape:
        for name in ("threads.md", "10-intent.threads.md"):
            if (p.proj / name).exists():
                blocks, _ = fd.thread_blocks(p.proj / name)
                return [(b["id"], b["text"]) for b in blocks], []
        return [], []
    files = fd.thread_files(p.proj)
    return [(t["id"], t["text"]) for t in files if t["status"] == "open"], [t for t in files if t["status"] != "open"]


def waiting(p, open_threads, fnd_rows, fnd_items, chl_rows, chl_items):
    lines, parked = [], []
    for id_, text in open_threads:
        first, last = fd.first_sentence(text), fd.last_dated_paragraph(text)
        line = f"- {id_} — {first}"
        if last and not last.startswith(first):
            line += f" {last}"
        lines.append(line)
    for f in sorted(list(p.proj.glob("[0-9][0-9]-*.md")) + list(p.proj.glob("work/*.spec.md"))):
        if ".history." in f.name or ".threads." in f.name:
            continue
        flines = fd.read(f).split("\n")
        for n, line in enumerate(flines):
            m = re.match(r"^- \*\*(TBC\.\d{4,5})\*\*\s*\(owner:\s*principal\)\s*(.*)$", line)
            if m:
                text = [m.group(2)]
                for cont in flines[n + 1:]:
                    if cont.startswith("  ") and cont.strip():
                        text.append(cont.strip())
                    else:
                        break
                lines.append(f"- {m.group(1)} of {p.rel(f)} — {fd.first_sentence(' '.join(text))}")
    for id_, sev, cat, state, src, res in fnd_rows:
        head = fnd_items[id_][3] if id_ in fnd_items else ""
        if state == "open" and "critique" in src:
            lines.append(f"- {id_} — {head or 'open finding of a critic'} ({src})")
        elif state == "parked":
            parked.append(f"- {id_} — {head or 'finding'} — {res}")
    for id_, state, head, src, res in chl_rows:
        if state == "open":
            lines.append(f"- {id_} — {head}")
        elif state == "parked":
            parked.append(f"- {id_} — {head} — {res}")
    if parked:
        lines.append("")
        lines.append("### Parked, with their decision")
        lines.extend(parked)
    return lines


def reports(p, open_threads, closed_threads):
    out = []
    # an ID defined twice
    seen = {}
    files = [f for f in list(p.proj.glob("[0-9][0-9]-*.md")) + list(p.proj.glob("work/*.spec.md"))
             + list(p.proj.glob("00-brief*.md")) if ".history." not in f.name and ".threads." not in f.name]
    for f in files:
        for line in fd.read(f).split("\n"):
            m = DEF_RE.match(line)
            if m:
                seen.setdefault(m.group(1), []).append(p.rel(f))
    for id_, _ in open_threads:
        seen.setdefault(id_, []).append("threads/")
    for t in closed_threads:
        seen.setdefault(t["id"], []).append("threads/")
    for id_, places in sorted(seen.items()):
        if len(places) > 1:
            out.append(f"- {id_} defined twice: {', '.join(places)}")
    # a closed thread touched later
    for t in closed_threads:
        rel = Path(t["path"]).resolve().relative_to(p.repo.resolve()).as_posix()
        closing = fr.git_out(["log", "--format=%H", "--diff-filter=AM", "-S", "status: closed", "--", rel], p.repo)
        last = fr.git_out(["log", "-1", "--format=%H", "--", rel], p.repo)
        if closing and last and closing.split("\n")[-1] != last:
            out.append(f"- {t['id']} closed and touched by a later commit {last[:7]}: a closed thread is immutable")
    # a THR cited with neither a file nor a closed record
    known = {id_ for id_, _ in open_threads} | {t["id"] for t in closed_threads}
    for recs in p.histories.values():
        for r in recs:
            if r["kind"] == "closed":
                known |= {s for s in fd.subject_ids(r["subject"]) if s.startswith("THR.")}
    for f in p.proj.rglob("*.history.archive.md"):
        known |= set(re.findall(r"THR\.\d{4,5}", fd.read(f)))
    cited = {}
    for f in sorted(p.proj.rglob("*.md")):
        top = p.rel(f).split("/")[0]
        # the chain, the decisions, the work and the indexes cite the project's own threads;
        # a render, a recipe or a page may cite another project's, and is not read
        if ".history." in f.name or f.name in ("ledger.md", "ledger.archive.md") or top in (
                "threads", "sources", "renders", "recipes", "docs", "published", "reviews", "challenges"):
            continue
        for id_ in set(re.findall(r"THR\.\d{4,5}", fd.read(f))):
            cited.setdefault(id_, set()).add(p.rel(f))
    for id_ in sorted(set(cited) - known, key=lambda i: int(i.split(".")[1])):
        out.append(f"- {id_} cited in {', '.join(sorted(cited[id_]))} with neither a thread file nor a closed record")
    return out


# ------------------------------------------------------------ compose

def compose(p):
    closed, verdicts = p.closed_records(), p.verdicts()
    open_threads, closed_threads = threads_of(p)
    fnd_rows, fnd_items = findings(p, closed, verdicts)
    chl_rows, chl_items = challenges(p, closed, verdicts)
    data = {
        "Briefs": briefs(p), "Documents": documents(p), "Renders": renders(p), "Published": published(p),
        "Work": work(p), "Sources": sources(p), "Dependencies": dependencies(p), "Research": research(p),
        "Findings": fnd_rows, "Challenges": chl_rows,
    }
    waiting_lines = waiting(p, open_threads, fnd_rows, fnd_items, chl_rows, chl_items)
    report_lines = reports(p, open_threads, closed_threads) + [f"- {r}" for r in p.reports]
    drops = set(LIBRARY_DROPS) if p.kind == "library" else set()
    if p.kind == "library" and not fnd_rows:
        drops.add("Findings")

    template = fd.read(TEMPLATE)
    tfront, tbody = fd.split_front(template)
    front = [f"project: {p.slug}", f"updated: {TODAY}",
             f"kind: {p.kind}             # read from project.md (templates/project.md)",
             f"language: {p.language}         # read from project.md"]
    if p.old_shape:
        front.append("shape: before the migration (templates/project.md) - read from the hand-kept ledger as the archive")
    for path, line, what in fd.problems:
        front.append(f"unparsed: {Path(path).name}:{line} ({what})")
    out = ["---", *front, "---"]
    section = None
    for line in tbody.split("\n"):
        if line.startswith("## "):
            section = line[3:].strip()
            if section in drops:
                continue
            out.append(line)
            continue
        if section in drops:
            continue
        if section is None:
            out.append(line.replace("<Project>", p.slug))
            continue
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                out.append(line)
                for row in data.get(section, []):
                    out.append("| " + " | ".join(str(c).replace("|", "/") for c in row) + " |")
            elif cells and cells[0] in ("File", "Render", "Path", "ID"):
                out.append(line)
            continue  # the template's sample rows are dropped
        if section == "Waiting on principal" and line.strip() == "- …":
            out.extend(waiting_lines or ["- nothing: no open thread, no TBC of the principal, no open finding of a critic, no open challenge"])
            continue
        if section == "Reports":
            if line.strip() == "- …":
                if report_lines:
                    out.extend(report_lines)
                else:
                    # nothing to report: the heading and its comment go too
                    while out and out[-1] != "## Reports":
                        out.pop()
                    out.pop()
                    section = "dropped"
            else:
                out.append(line)
            continue
        out.append(line)
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


def main(argv):
    ft.utf8_console()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1].strip())
    ap.add_argument("slug", help="the project ('forge' = the engine's own project)")
    ap.add_argument("--out", help="write here instead of the project's ledger.md (the dry run)")
    a = ap.parse_args(argv)
    fr.need_git()
    p = Project(a.slug)
    text = compose(p)
    target = p.proj / "ledger.md"
    rel = target.resolve().relative_to(p.repo.resolve()).as_posix()
    tracked = (p.repo / ".git").exists() and fr.git(["ls-files", "--error-unmatch", rel], p.repo).returncode == 0
    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(text, encoding="utf-8")
        fr.say(f"{a.slug}: ledger written to {a.out}" + (" (ledger.md is tracked; not touched)" if tracked else ""), "green")
    elif tracked:
        sys.stdout.write(text)
        fr.say(f"{a.slug}: ledger.md is tracked by git - not written; the shape before the migration, run /migrate", "yellow")
    else:
        target.write_text(text, encoding="utf-8")
        fr.say(f"{a.slug}: ledger.md made ({len(text.splitlines())} lines)", "green")
    if fd.problems:
        fr.say(f"{len(fd.problems)} file(s) not parsed, named in the header", "yellow")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
