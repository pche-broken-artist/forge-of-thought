"""
forge-migrate.py - bring one project to the shape of the first release
of the brief `collaboration` (SOL.0800 of the forge solution design):
the project file, headers without changing fields, the state in
records, threads as files, the attributes, the ledger out of git.

SYNOPSIS
    python scripts/forge-migrate.py <slug>            # dry run
    python scripts/forge-migrate.py <slug> --apply    # perform
    python scripts/forge-migrate.py <slug> --undo     # take back

WHAT IT DOES
    The shape of a project is a set of marks, one per step, never an
    engine version in the project: the project file exists (B0), no
    header of an artefact, a specification, a recipe, an index or the
    map carries a field that changes with a round (A), `threads/`
    exists or the project has no threads file (C1), `.gitattributes`
    exists (D), `ledger.md` is out of git's index (B). The dry run,
    the default, prints the marks and, for every step still missing,
    what it would change; `--apply` runs the missing steps, each
    verifying its own mark afterwards; the order of one run is A, B0,
    B, C1, D. A library takes A, B0, B and D.

    A   The fields `date` and `last_change` leave the headers of the
        artefacts (NN-*.md, 00-brief*.md) and the work specifications,
        `updated` and `last_change` the recipes', `updated` the
        indexes', `generated` and `previous` the map's (POS.1570).
    B0  `project.md` from templates/project.md: `project` the slug
        (the directory's name), `kind` and `language` from the
        hand-kept ledger's header (`thought`, `en` when absent),
        `fixture: true` for a slug that starts with `fixture`.
    B   What only the ledger knew becomes records (POS.1610): the
        mining of a brief as a record in the intent's history with the
        brief as its subject, its version the one the Note names
        ("mined into intent X.Y") or the intent's current one; the
        state of a work product as a record in its specification's
        history; a source's date, its origin and its form as the
        fields `Date` and `Form` of its entry in sources/00-INDEX.md;
        a published file's provenance as the companion
        published/<recipe>.md; then the hand-kept ledger copied as it
        stands to `ledger.archive.md`, immutable, `ledger.md` taken out
        of the index (`git rm --cached`, nothing deleted) and put into
        the project's .gitignore. A Waiting line without an ID is
        printed for the principal; it has no home in records.
    C1  threads.md (in older projects 10-intent.threads.md) cut by
        `- **THR.NNNN**` into threads/THR.NNNN.md from
        templates/thread.md: `concerns` from the bracket (`intent` when
        there is none), `origin` guessed from the first sentence and
        printed for the principal's judgement, `status: open`; the text
        kept; what follows the last thread and is not a thread is
        printed; the old file deleted from the tree.
    D   `.gitattributes` from templates/gitattributes; the engine
        carries a list of its own, which the step only verifies.

    The author of every record it writes is the handle of the instance
    file (CLAUDE.local.md, `Author:`); without it the script refuses.
    `--apply` refuses a project that is not a repository, a working
    tree that is not clean, a branch behind or diverged from its
    origin and any branch but main: the migration is one large change,
    run once, on one clone; everyone else pulls. It commits nothing;
    `/save` follows. `--undo` takes back the last `--apply` from the
    script's own manifest (tmp/forge-migrate-<slug>.json at the engine
    root): changed and deleted tracked files restored from the index,
    created files removed, the ledger put back into the index, the
    .gitignore line taken out. The slug `forge` is the engine's own
    project, whose repository is the engine.

WHAT IT NEEDS
    Python 3.8 or newer; git on PATH. forge_repos.py and forge_tools.py
    beside it; the templates project.md, thread.md and gitattributes.

EXAMPLES
    python scripts/forge-migrate.py fixture            # what would change
    python scripts/forge-migrate.py fixture --apply    # migrate the fixture
    python scripts/forge-migrate.py fixture --undo     # and take it back
    python scripts/forge-migrate.py forge              # the engine's own project, dry
"""

import argparse
import datetime
import json
import os
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import forge_docs as fd  # noqa: E402
import forge_repos as fr  # noqa: E402
import forge_tools as ft  # noqa: E402

TEMPLATES = fr.ENGINE_ROOT / "templates"
ID_RE = fd.ID_RE
TODAY = datetime.date.today().isoformat()
read, split_front, front_value, tables, waiting_lines = fd.read, fd.split_front, fd.front_value, fd.tables, fd.waiting_lines

LEAVING = {
    "artefact": ("date", "last_change"),
    "recipe": ("updated", "last_change"),
    "index": ("updated",),
    "map": ("generated", "previous"),
}


# ---------------------------------------------------------------- files

def header_files(proj):
    """(path, kind) of every file whose header step A touches."""
    out = []
    for p in sorted(proj.glob("[0-9][0-9]-*.md")):
        if ".history." in p.name or ".threads." in p.name:
            continue
        out.append((p, "artefact"))
    for p in sorted(proj.glob("work/*.spec.md")):
        out.append((p, "artefact"))
    for p in sorted(proj.glob("recipes/*.md")):
        if ".history." in p.name:
            continue
        out.append((p, "recipe"))
    for name in ("sources/00-INDEX.md", "research/00-INDEX.md"):
        if (proj / name).exists():
            out.append((proj / name, "index"))
    if (proj / "docs-map.md").exists():
        out.append((proj / "docs-map.md", "map"))
    return out


def leaving_fields(path, kind):
    front, _ = split_front(read(path))
    if front is None:
        return []
    return [k for k in LEAVING[kind] if front_value(front, k) is not None
            or any(l.startswith(k + ":") for l in front)]


# ------------------------------------------------------------ the target

class Target:
    def __init__(self, slug):
        self.slug = slug
        if slug == "forge":
            self.repo = fr.ENGINE_ROOT
            self.proj = fr.ENGINE_ROOT / "projects" / "forge"
        else:
            self.repo = self.proj = fr.project_path(slug)
        if not self.proj.is_dir():
            fr.fail(f"Project '{slug}' not found ({self.proj} does not exist).")
        self.manifest_path = fr.ENGINE_ROOT / "tmp" / f"forge-migrate-{slug}.json"
        self.manifest = {"slug": slug, "date": TODAY, "changed": [], "created": [],
                         "deleted": [], "unindexed": [], "gitignore": None}
        self.ledger = self.proj / "ledger.md"
        info = fr.project_file(self.proj)  # the one reader of the project file (SOL.0670)
        self.kind, self.language = info["kind"], info["language"]

    def rel(self, path):
        return Path(os.path.relpath(path, self.repo)).as_posix()

    def tracked(self, path):
        return fr.git(["ls-files", "--error-unmatch", self.rel(path)], self.repo).returncode == 0

    # -- marks
    def marks(self):
        threads_old = [p for p in (self.proj / "threads.md", self.proj / "10-intent.threads.md") if p.exists()]
        attributes = (self.repo / ".gitattributes").exists() if self.slug == "forge" \
            else (self.proj / ".gitattributes").exists()
        return {
            "A  headers without changing fields": not any(leaving_fields(p, k) for p, k in header_files(self.proj)),
            "B0 project file": (self.proj / "project.md").exists(),
            "B  ledger out of the index": not (self.ledger.exists() and self.tracked(self.ledger)),
            "C1 threads as files": (self.proj / "threads").is_dir() or not threads_old,
            "D  attributes": attributes,
        }

    # -- bookkeeping
    def note_change(self, path):
        r = self.rel(path)
        if path.exists() and self.tracked(path):
            if r not in self.manifest["changed"]:
                self.manifest["changed"].append(r)
        elif r not in self.manifest["created"]:
            self.manifest["created"].append(r)

    def write(self, path, text, apply):
        if apply:
            self.note_change(path)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")

    def append(self, path, lines, apply):
        if not apply:
            return
        self.note_change(path)
        text = read(path) if path.exists() else ""
        if text and not text.endswith("\n"):
            text += "\n"
        path.write_text(text + "\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- steps

def step_a(t, apply, out):
    files = [(p, k, leaving_fields(p, k)) for p, k in header_files(t.proj)]
    files = [(p, k, f) for p, k, f in files if f]
    for p, k, fields in files:
        out.append(f"A   {t.rel(p)}: drop {', '.join(fields)}")
        if apply:
            text = read(p)
            front, body = split_front(text)
            kept = [l for l in front if not any(l.startswith(f + ":") for f in fields)]
            t.write(p, "---\n" + "\n".join(kept) + "\n---" + ("\n" + body if body else ""), apply)
    return bool(files)


def step_b0(t, apply, out):
    target = t.proj / "project.md"
    if target.exists():
        return False
    template = read(TEMPLATES / "project.md")
    front, body = split_front(template)
    lines = []
    for l in front:
        if l.startswith("project:"):
            lines.append(f"project: {t.slug}")
        elif l.startswith("kind:"):
            lines.append(f"kind: {t.kind}" + l[len("kind: thought"):] if t.kind == "thought" else f"kind: {t.kind}")
        elif l.startswith("language:") or l.startswith(" "):
            lines.append(l.replace("language: en", f"language: {t.language}") if l.startswith("language:") else l)
        else:
            lines.append(l)
    if t.slug.startswith("fixture"):
        lines.append("fixture: true")
    text = "---\n" + "\n".join(lines) + "\n---\n" + (("\n" + body.lstrip("\n")) if body.strip() else "")
    note = ""
    ledger_slug = None
    if t.ledger.exists():
        f, _ = split_front(read(t.ledger))
        ledger_slug = front_value(f, "project")
    if ledger_slug and ledger_slug != t.slug:
        note = f" (the ledger's header says project: {ledger_slug}; the directory's name wins)"
    out.append(f"B0  create project.md: project {t.slug}, kind {t.kind}, language {t.language}"
               + (", fixture: true" if t.slug.startswith("fixture") else "") + note)
    t.write(target, text, apply)
    return True


def _version_of(path):
    if not path.exists():
        return None
    front, _ = split_front(read(path))
    return front_value(front, "version") if front else None


def step_b(t, apply, out, author):
    if not t.ledger.exists():
        out.append("B   no ledger.md: nothing to move, nothing to archive")
        return False
    if not t.tracked(t.ledger):
        return False
    text = read(t.ledger)
    tb = tables(text)
    # mining records
    intent_hist = t.proj / "10-intent.history.md"
    intent_version = _version_of(t.proj / "10-intent.md")
    records = []
    for row in tb.get("Briefs", []):
        mined, note, file = row.get("Mined", ""), row.get("Note", ""), row.get("File", "")
        if not file or mined in ("", "—", "-"):
            out.append(f"B   Briefs row {file or '?'}: no mining state, no record written")
            continue
        m = re.search(r"mined into intent (\d+\.\d+)", note)
        version = m.group(1) if m else intent_version
        if not intent_hist.exists() or version is None:
            out.append(f"B   Briefs row {file}: no intent history to record the mining in, printed only: mined: {mined}, {note}")
            continue
        records.append(f"- {TODAY} | {version} | {author} | {file} | changed | mined: {mined}, {note}")
    if records:
        out.append(f"B   {t.rel(intent_hist)}: {len(records)} mining record(s)")
        t.append(intent_hist, records, apply)
    # work states
    for row in tb.get("Work", []):
        spec = row.get("Specification", "")
        m = re.match(r"(work/\S+\.spec\.md)\s*v?(\d+\.\d+)", spec)
        if not m:
            out.append(f"B   Work row {row.get('File', '?')}: specification not readable ({spec}), printed only")
            continue
        hist = t.proj / m.group(1).replace(".spec.md", ".spec.history.md")
        made = row.get("Made", "")
        date = made if re.match(r"^\d{4}-\d{2}-\d{2}$", made) else TODAY
        rec = (f"- {date} | {m.group(2)} | {author} | {row.get('File', '')} | changed | "
               f"state: {row.get('State', '')}; made {made} from {row.get('Inputs', '')}")
        out.append(f"B   {t.rel(hist)}: the work state as a record")
        t.append(hist, [rec], apply)
    # index fields
    index = t.proj / "sources" / "00-INDEX.md"
    if tb.get("Sources"):
        if index.exists():
            itext = read(index)
            for row in tb["Sources"]:
                name = row.get("File", "").split()[0] if row.get("File") else ""
                name = re.sub(r"^sources/", "", name)
                itext, done = _index_fields(itext, name, row.get("Date", ""), row.get("Date origin", ""), row.get("Form", ""))
                out.append(f"B   {t.rel(index)}: {name}: " + ("Date and Form added" if done == "added" else done))
            t.write(index, itext, apply)
        else:
            out.append("B   Sources rows but no sources/00-INDEX.md: the fields have no home, printed only")
    # published companions
    for row in tb.get("Published", []):
        file = row.get("File", "")
        base = Path(file).name
        recipe = re.sub(r"\.[a-z]+$", "", base)
        companion = t.proj / "published" / f"{recipe}.md"
        if companion.exists():
            continue
        body = (f"---\nproject: {t.slug}\nfile: {base}\nrecipe: {row.get('Recipe', '')}\n"
                f"render: {row.get('From render', '')}\nmodel: {row.get('Model', '')}\n"
                f"published: {row.get('Published', '')}\n---\n")
        out.append(f"B   create {t.rel(companion)}: the provenance of {base}")
        t.write(companion, body, apply)
    # waiting lines without an ID
    for line in waiting_lines(text):
        if not ID_RE.search(line):
            out.append(f"B   Waiting line without an ID, for the principal: {line[:120]}")
    # archive and out of the index
    archive = t.proj / "ledger.archive.md"
    if not archive.exists():
        out.append(f"B   copy ledger.md to {t.rel(archive)} as it stands, immutable")
        t.write(archive, text, apply)
    out.append("B   git rm --cached ledger.md; ledger.md into .gitignore")
    if apply:
        fr.git(["rm", "--cached", "-q", t.rel(t.ledger)], t.repo, check=True)
        t.manifest["unindexed"].append(t.rel(t.ledger))
        gi = t.repo / ".gitignore" if t.slug == "forge" else t.proj / ".gitignore"
        line = "projects/forge/ledger.md" if t.slug == "forge" else "ledger.md"
        existing = read(gi) if gi.exists() else ""
        if line not in existing.split("\n"):
            t.note_change(gi)
            gi.write_text(existing + ("" if not existing or existing.endswith("\n") else "\n")
                          + "# The ledger is made at read time, never in git (SOL.0680)\n" + line + "\n",
                          encoding="utf-8")
            t.manifest["gitignore"] = line
    return True


def _index_fields(itext, name, date, origin, form):
    lines = itext.split("\n")
    start = None
    for i, l in enumerate(lines):
        m = re.match(r"^### `([^`]+)`", l)
        if m and (m.group(1) == name or (name.endswith("/") and m.group(1).rstrip("/") == name.rstrip("/"))):
            start = i
            break
    if start is None:
        return itext, "no index entry found, the fields printed only: Date %s (%s), Form %s" % (date, origin, form)
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("### ") or lines[j].startswith("## "):
            end = j
            break
    block = lines[start:end]
    if any(l.startswith("- **Date:**") for l in block):
        return itext, "already carries Date"
    o = origin.lower()
    if o.startswith("content"):
        how = "from the content" + origin[len("content"):]
    elif o.startswith("file"):
        how = "from the file" + origin[len("file"):]
    elif o.startswith("ingest"):
        how = "from the ingest" + origin[len("ingested"):] if o.startswith("ingested") else "from the ingest"
    else:
        how = origin
    new = [f"- **Date:** {date}, {how}".rstrip(", "), f"- **Form:** {form}"]
    # after the Origin field (with its continuation lines), else after the heading
    at = None
    for k in range(start + 1, end):
        if lines[k].startswith("- **Origin:**"):
            at = k + 1
            while at < end and lines[at].startswith("  "):
                at += 1
            break
    if at is None:
        at = start + 1
    lines[at:at] = new
    return "\n".join(lines), "added"


def step_c1(t, apply, out):
    old = next((p for p in (t.proj / "threads.md", t.proj / "10-intent.threads.md") if p.exists()), None)
    if old is None or (t.proj / "threads").is_dir():
        return False
    _, body = split_front(read(old))
    blocks, trailing, current = [], [], None
    for line in body.split("\n"):
        m = fd.THREAD_BLOCK_RE.match(line)
        if m:
            current = {"id": m.group(1), "concerns": (m.group(2) or "intent").strip(), "lines": [m.group(3)]}
            blocks.append(current)
            continue
        if current is None:
            continue  # the heading and the comment before the first thread
        if line.startswith("  ") or not line.strip():
            if trailing:
                trailing.append(line)
            else:
                current["lines"].append(line[2:] if line.startswith("  ") else line)
        else:
            trailing.append(line)
    template = read(TEMPLATES / "thread.md")
    tfront, tbody = split_front(template)
    comment = tbody[tbody.find("<!--"):] if "<!--" in tbody else ""
    for b in blocks:
        text = "\n".join(b["lines"]).strip("\n")
        origin = _guess_origin(text)
        b["origin"] = origin
        target = t.proj / "threads" / f"{b['id']}.md"
        front = [f"id: {b['id']}", f"concerns: {b['concerns']}", f"origin: {origin}", "status: open"]
        t.write(target, "---\n" + "\n".join(front) + "\n---\n\n" + text + "\n\n" + comment.rstrip("\n") + "\n", apply)
    out.append(f"C1  {t.rel(old)}: {len(blocks)} thread(s) cut into threads/; the origins guessed, for the principal:")
    for b in blocks:
        out.append(f"      {b['id']} [{b['concerns']}] origin: {b['origin']}")
    tail = "\n".join(trailing).strip()
    if tail:
        out.append("C1  text after the last thread, not a thread, for the principal:")
        for l in tail.split("\n"):
            out.append("      " + l)
    out.append(f"C1  delete {t.rel(old)} from the tree")
    if apply:
        t.manifest["deleted"].append(t.rel(old))
        old.unlink()
    return True


def _guess_origin(text):
    first = re.split(r"(?<=[.!?])\s", text.strip(), maxsplit=1)[0]
    low = text.lower()
    if "synthesis" in low[:400] or "claude's" in first.lower():
        return "Claude's synthesis"
    m = re.search(r"`?((?:sources|research|work|recipes)/[^\s`,;:)]+|00-brief[^\s`,;:)]*\.md)`?", first)
    if m:
        return m.group(1)
    return "the principal"


def step_d(t, apply, out):
    if t.slug == "forge":
        if (t.repo / ".gitattributes").exists():
            return False
        out.append("D   the engine's own .gitattributes is missing: its list is SOL.0730's, not the template's; write it by hand")
        return True
    target = t.proj / ".gitattributes"
    if target.exists():
        return False
    out.append("D   create .gitattributes from templates/gitattributes")
    t.write(target, read(TEMPLATES / "gitattributes"), apply)
    return True


# ------------------------------------------------------------------ runs

def author_handle():
    local = fr.ENGINE_ROOT / "CLAUDE.local.md"
    if local.exists():
        m = re.search(r"\*\*Author:\*\*\s*(\S+)", read(local))
        if m:
            return m.group(1)
    return None


def refusals(t):
    reasons = []
    if not (t.repo / ".git").exists():
        reasons.append("not a repository")
        return reasons
    if fr.git_out(["status", "--porcelain"], t.repo):
        reasons.append("the working tree is not clean: save first")
    branch = fr.git_out(["rev-parse", "--abbrev-ref", "HEAD"], t.repo)
    if branch != "main":
        reasons.append(f"on branch {branch}, not main")
    state = fr.remote_state(t.repo)
    if state.startswith("behind") or state.startswith("diverged"):
        reasons.append(f"{state} against the origin: /pull first")
    return reasons


def run(t, apply, author):
    marks = t.marks()
    print(f"{t.slug}: kind {t.kind}, language {t.language}, repository {t.repo}")
    for name, ok in marks.items():
        print(f"  [{'x' if ok else ' '}] {name}")
    if all(marks.values()):
        fr.say("already in the shape of the first release - nothing to do", "green")
        return
    out, ran = [], []
    if step_a(t, apply, out):
        ran.append("A")
    if step_b0(t, apply, out):
        ran.append("B0")
    if step_b(t, apply, out, author):
        ran.append("B")
    if t.kind != "library" and step_c1(t, apply, out):
        ran.append("C1")
    if step_d(t, apply, out):
        ran.append("D")
    print("\n".join(out))
    if not apply:
        fr.say(f"dry run: steps {', '.join(ran) or 'none'} would run; nothing changed", "grey")
        return
    t.manifest_path.parent.mkdir(exist_ok=True)
    t.manifest_path.write_text(json.dumps(t.manifest, indent=2), encoding="utf-8")
    after = t.marks()
    failed = [n for n, ok in after.items() if not ok]
    if failed:
        fr.say("steps ran but these marks still fail: " + "; ".join(failed), "red")
        fr.say(f"undo with: python scripts/forge-migrate.py {t.slug} --undo", "yellow")
        sys.exit(1)
    fr.say(f"migrated: steps {', '.join(ran)}; manifest {t.manifest_path}; nothing committed - /save follows", "green")


def undo(t):
    if not t.manifest_path.exists():
        fr.fail(f"No manifest at {t.manifest_path} - nothing to undo.")
    m = json.loads(read(t.manifest_path))
    for r in m["unindexed"]:
        fr.git(["reset", "-q", "--", r], t.repo, check=True)
    for r in m["changed"] + m["deleted"]:
        fr.git(["checkout", "--", r], t.repo, check=True)
    for r in m["created"]:
        p = t.repo / r
        if p.exists():
            p.unlink()
    for d in (t.proj / "threads", t.proj / "published"):
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()
    t.manifest_path.unlink()
    fr.say(f"undone: {len(m['changed'])} restored, {len(m['created'])} removed, "
           f"{len(m['deleted'])} brought back, {len(m['unindexed'])} back in the index", "green")


def main(argv):
    ft.utf8_console()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1].strip())
    ap.add_argument("slug", help="the project ('forge' = the engine's own project)")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--apply", action="store_true", help="perform the missing steps")
    g.add_argument("--undo", action="store_true", help="take back the last --apply from the manifest")
    a = ap.parse_args(argv)
    fr.need_git()
    fr.need_engine_repo()
    t = Target(a.slug)
    if a.undo:
        undo(t)
        return 0
    author = author_handle()
    if author is None:
        fr.fail("No Author in CLAUDE.local.md - run /setup; the records need the handle.")
    if a.apply:
        reasons = refusals(t)
        if reasons:
            fr.fail(f"{a.slug}: " + "; ".join(reasons) + " - nothing was changed.")
    else:
        reasons = refusals(t) if (t.repo / ".git").exists() else ["not a repository"]
        if reasons:
            fr.say(f"{a.slug}: --apply would refuse: " + "; ".join(reasons), "yellow")
    run(t, a.apply, author)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
