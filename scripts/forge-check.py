#!/usr/bin/env python3
"""
forge-check.py - the mechanical clauses of a check, run as a program
instead of a model: what the files fully determine, verified by
reading them (THR.0530 of the forge intent; the trial of 2026-10-22).

SYNOPSIS
    python scripts/forge-check.py light <slug> [--out PATH]

WHAT IT DOES
    Runs the clauses of one check's Lens (.claude/agents/check-<name>.md)
    that are a comparison of files, and prints a report in the shape
    of the check contract (.claude/skills/check-contract/SKILL.md,
    Output): the verdict line, the findings ranked by severity, each
    with Where (file:line, relative to the project), the rule with its
    owner and one fix, "immediate fix:" where it is pure bookkeeping.
    No ID is given: the /check procedure numbers and files a report.
    A section "Left to reading" closes the report, naming the clauses
    of the Lens the script does not verify, so that the script and the
    agent can be compared clause by clause.

    light <slug>: the bookkeeping of one project, the rules read from
    CLAUDE.md (Versioning & status) and the templates (history.md,
    thread.md, index.md, index-bundle.md, ledger.md, project.md, the
    skeleton of each versioned document):
      1. front-matter and history: the header keys of every versioned
         document against its skeleton, version and status and their
         agreement, the companion beside it with the skeleton's header
         and comment, every record in the shape of the log, the kinds,
         the state words, the order, `created` without a reason,
         `closed` without a Was, the newest record at the header's
         version, no Version History table left;
      2. the ledger's own reports: the ledger is composed in memory by
         forge-ledger.py (nothing written) and each `unparsed:` line
         and each line of its Reports section is a finding; a project
         of the shape before the migration is one finding and nothing
         else (templates/project.md);
      3. records and companions: the published companions against the
         files of published/ and the keys of /publish step 6; a work
         file citing an item its specification's Inputs do not name
         (POS.1520); every thread file with the header of
         templates/thread.md, its id the file's name, its concerns a
         state of the forge, its origin one the template knows, its
         birth recorded in a history, a closed one with its `closed`
         record; a Verdict word the decisions skeleton does not know;
      4. dependencies: every path of the ledger's Dependencies table on
         disk (POS.1020), a missing one advisory;
      5. resource indexes: sources/00-INDEX.md and research/00-INDEX.md
         with the skeleton's header and comment, every file registered
         and every entry a file, a bundle with its inner index in the
         bundle skeleton's shape and its files catalogued there, the
         Date and Form fields of a sources entry in the skeleton's
         vocabulary, the three fields of a research entry.
    Reads only. Exit code 0 always; the report is the result.

WHAT IT NEEDS
    Python 3.8 or newer; git on PATH (the ledger asks it about a closed
    thread). forge_check.py, forge_docs.py, forge_repos.py,
    forge_tools.py and forge-ledger.py beside it; templates/.

EXAMPLES
    python scripts/forge-check.py light fixture
    python scripts/forge-check.py light forge --out tmp/check-light-forge.md
"""

import argparse
import datetime
import fnmatch
import importlib.util
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import forge_check as fc  # noqa: E402
import forge_docs as fd  # noqa: E402
import forge_repos as fr  # noqa: E402
import forge_tools as ft  # noqa: E402

TODAY = datetime.date.today().isoformat()
RECORD_KINDS = ("created", "changed", "closed", "removed", "approved")
MINED_WORDS = ("pending", "partial", "mined", "dropped")
WORK_STATES = ("current", "stale", "by hand")
VERDICT_WORDS = re.compile(r"^(rejected|parked until .+|obsolete)$")
PUBLISHED_KEYS = ["project", "file", "recipe", "render", "model", "published"]
STATES_DIR = fr.ENGINE_ROOT / ".claude" / "skills" / "forge" / "states"
DATE_ORIGINS = ("the content", "the file", "the ingest")
FORM_RE = re.compile(r"^(text|binary|extract of .+)$")
WORK_CITED = re.compile(r"\b(?:DEC|SOL|POS|TBC|THR)\.\d{4,5}\b")


def entry_names(entry):
    """The file names an index entry names: the backticked name of its
    heading and every further backticked name there; a name that
    begins with `-` is a shorthand for the first name with its tail
    after the last `-` replaced (`a-1.md`, `-2.md`)."""
    rest = entry["heading"][len(entry["name"]):]
    m = re.match(r"^(?:\s*,\s*`[^`]+`)+", rest)  # a comma list of further names, nothing in brackets
    names = [entry["name"]] + (re.findall(r"`([^`]+)`", m.group(0)) if m else [])
    out = []
    for n in names:
        n = n.rstrip("/")
        if n.startswith("-") and out:
            base = out[0]
            n = base[:base.rfind("-")] + n if "-" in base else n
        out.append(n)
    return out


def ignore_patterns(gitignore):
    """The patterns of a .gitignore, without comments and blanks."""
    if not Path(gitignore).exists():
        return []
    return [l.strip().lstrip("/") for l in fd.read(gitignore).split("\n") if l.strip() and not l.startswith(("#", "!"))]


def load_ledger_module():
    spec = importlib.util.spec_from_file_location("forge_ledger", Path(__file__).resolve().parent / "forge-ledger.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Light:
    def __init__(self, slug):
        self.slug = slug
        self.ledger = load_ledger_module()
        fd.problems.clear()
        self.p = self.ledger.Project(slug)  # fails aloud on a missing project
        self.proj = self.p.proj
        self.findings = []
        self.groups = {}
        self.left = []
        self.facts = []

    # -- helpers
    def rel(self, path):
        return fc.rel(self.proj, path)

    def add(self, severity, headline, where, rule, fix, immediate=False):
        self.findings.append(fc.Finding(severity, headline, where, rule, fix, immediate))

    def group(self, key, severity, headline, where, rule, fix, immediate=False):
        """One finding for every place that breaks the same rule the same
        way: `headline` is a function of the count and of the places."""
        g = self.groups.setdefault(key, {"severity": severity, "headline": headline, "where": [],
                                         "rule": rule, "fix": fix, "immediate": immediate})
        g["where"].extend(where if isinstance(where, list) else [where])

    def close_groups(self):
        for g in self.groups.values():
            self.findings.append(fc.Finding(g["severity"], g["headline"](len(g["where"]), g["where"]),
                                            g["where"], g["rule"], g["fix"], g["immediate"]))
        self.groups = {}

    def where(self, path, line=0):
        return f"`{self.rel(path)}:{line}`" if line else f"`{self.rel(path)}`"

    def ignored(self, path):
        """Whether a path relative to sources/ matches sources/.gitignore
        (a binary converted in place is not an unregistered file)."""
        return any(fnmatch.fnmatch(path, pat) or fnmatch.fnmatch(path.split("/")[-1], pat)
                   or path.startswith(pat.rstrip("/") + "/") for pat in getattr(self, "ignore", []))

    # -- 1. front-matter and history
    def front_matter_and_history(self):
        rule_vs = "CLAUDE.md, Versioning & status"
        tcomment = fc.template_comment("history")
        for doc, kind in fc.versioned_documents(self.proj):
            text = fd.read(doc)
            front, _ = fd.split_front(text)
            if front is None:
                self.add("medium", f"`{self.rel(doc)}` has no front-matter", self.where(doc, 1),
                         f"{rule_vs}; `templates/{kind}.md`, the header",
                         f"give it the header of `templates/{kind}.md`: version, status and what does not change with the work")
                continue
            allowed = fc.template_keys(kind)
            keys = fc.front_keys(front)
            version = fd.front_value(front, "version")
            status = fd.front_value(front, "status")
            vt = fc.version_tuple(version) if version else None
            faults, severity, immediate = [], "low", True  # the header's faults, one finding per document
            extra = [k for k in keys if k not in allowed]
            if extra:
                faults.append(f"the field{'s' if len(extra) > 1 else ''} {', '.join('`' + k + '`' for k in extra)} the skeleton does not have")
            if version is None or vt is None:
                faults.append("no well-formed `version`" if version else "no `version`")
                immediate = False
            if kind == "recipe":
                if status is not None:
                    faults.append("a `status`, which a recipe does not carry")
                if vt and vt[0] >= 1:
                    faults.append(f"the version {version}, past the 0.x a recipe stays at")
                    immediate = False
            elif "status" in allowed:
                if status is None:
                    faults.append("no `status`")
                elif status not in fc.STATUSES:
                    faults.append(f"the status `{status}`, a word the skeleton does not know")
                elif vt is not None:
                    if vt[1] == 0 and status != "approved":
                        faults.append(f"the integer version {version} with status `{status}`")
                        severity, immediate = "medium", False
                    if vt[1] != 0 and status == "approved":
                        faults.append(f"the version {version}, not an integer, with status `approved`")
                        severity, immediate = "medium", False
            if faults:
                self.add(severity, f"The header of `{self.rel(doc)}` carries " + "; ".join(faults),
                         self.where(doc, 1),
                         f"{rule_vs} (`version` and `status` and what does not change with the work; status agrees with the number; a recipe carries no status and stays 0.x); `templates/{kind}.md`, the header",
                         "the header of the skeleton: version and status of the house scheme, nothing the history computes", immediate=immediate)
            if re.search(r"^#+ .*Version History|^\| *Version *\|", text, re.M):
                self.add("medium", f"`{self.rel(doc)}` carries a Version History table in its body",
                         self.where(doc, fc.line_of(text, r"^#+ .*Version History|^\| *Version *\|", re.M)),
                         f"{rule_vs} (the history lives in the companion, never in the body; a table moves to `<file>.history.archive.md`)",
                         "move the table to the archive companion, on the principal's word, and let the log begin with the next version")
            # the companion
            comp = fc.companion_of(doc)
            if not comp.exists():
                if version is None:
                    continue  # already a finding: no version, no companion
                self.add("medium", f"`{self.rel(doc)}` has no history companion", self.where(doc),
                         f"{rule_vs} (every versioned document keeps its history in `<file>.history.md` beside it)",
                         f"create `{self.rel(comp)}` from `templates/history.md` with a `created` record at {version}")
                continue
            self.companion(doc, comp, version, vt, tcomment)

    def companion(self, doc, comp, version, vt, tcomment):
        rule_vs = "CLAUDE.md, Versioning & status"
        text = fd.read(comp)
        front, body = fd.split_front(text)
        if front is None:
            self.add("low", f"`{self.rel(comp)}` has no front-matter", self.where(comp, 1),
                     "`templates/history.md`, the header", "the header `project` and `document` of the skeleton", immediate=True)
        else:
            keys = fc.front_keys(front)
            allowed = fc.template_keys("history")
            extra = [k for k in keys if k not in allowed]
            missing = [k for k in allowed if k not in keys]
            if extra or missing:
                self.add("low", f"`{self.rel(comp)}` header differs from the skeleton's" +
                         (f": extra {', '.join(extra)}" if extra else "") + (f": missing {', '.join(missing)}" if missing else ""),
                         self.where(comp, 1), "`templates/history.md`, the header (`project`, `document`)",
                         "the two keys of the skeleton and nothing else", immediate=True)
            document = fd.front_value(front, "document")
            if document and document != self.rel(doc):
                self.add("low", f"`{self.rel(comp)}` says `document: {document}` where it lies beside `{self.rel(doc)}`",
                         self.where(comp, fc.line_of(text, r"^document:", re.M)),
                         "`templates/history.md`, the header (`document`: the versioned document this history belongs to)",
                         f"`document: {self.rel(doc)}`", immediate=True)
            placeholder = [k for k in keys if (fd.front_value(front, k) or "").startswith("<")]
            if placeholder:
                self.add("low", f"`{self.rel(comp)}` carries the skeleton's placeholder in `{placeholder[0]}`",
                         self.where(comp, fc.line_of(text, rf"^{placeholder[0]}:", re.M)),
                         "`templates/history.md`, the header", "the project's slug and the document's path", immediate=True)
        if re.search(r"^# Version History|^\| *Version *\|", text, re.M):
            self.add("medium", f"`{self.rel(comp)}` carries a Version History table",
                     self.where(comp, fc.line_of(text, r"^# Version History|^\| *Version *\|", re.M)),
                     f"{rule_vs} (a companion written before the log moves as it stands to `<file>.history.archive.md`)",
                     "move the table to the archive companion, on the principal's word; the log begins with the next version")
        cs = fc.comments(text)
        if tcomment and cs and cs[0][1] != tcomment:
            self.group("history-comment", "low",
                       lambda n, w: f"{n} history companion{'s carry' if n > 1 else ' carries'} the skeleton's comment as it stood before the current `templates/history.md`",
                       self.where(comp, cs[0][0]), "CLAUDE.md, Templates; `templates/history.md`, the comment",
                       "the template's comment, as it stands on disk, in each", immediate=True)
        elif tcomment and not cs:
            self.add("low", f"`{self.rel(comp)}` carries no comment of the skeleton", self.where(comp, 1),
                     "`templates/history.md`, the comment", "the template's comment, as it stands on disk", immediate=True)
        # the records
        before = len(fd.problems)
        recs = fd.records(comp)
        for path, line, what in fd.problems[before:]:
            self.add("medium", f"`{self.rel(comp)}:{line}` is not a record of the log's shape", self.where(comp, line),
                     f"{rule_vs}; `templates/history.md` (one record per change, `- <date> | <version> | <author> | <subject> | <kind> | <reason> | Action: … | Was: …`)",
                     "bring the line to the record's shape", immediate=True)
        del fd.problems[before:]
        for r in recs:
            w = self.where(comp, r["line"])
            if r["kind"] not in RECORD_KINDS:
                self.add("low", f"A record carries the kind `{r['kind']}`, which the log does not have", w,
                         "`templates/history.md` (Kinds: created | changed | closed | removed | approved)",
                         "one of the five kinds", immediate=True)
            if fc.version_tuple(r["version"]) is None:
                self.add("low", f"A record carries the version `{r['version']}`, not of the house scheme", w,
                         f"{rule_vs}", "a version `N.N`", immediate=True)
            if r["kind"] == "created" and r["reason"]:
                self.add("low", "A `created` record carries a reason", w,
                         "`templates/history.md`, the comment (Reason is left out on `created`)",
                         "strip the reason; where its text is to be kept, carry it as a `changed` record of the same version", immediate=True)
            if r["kind"] == "closed" and r["was"] and any(s.startswith("THR.") for s in fd.subject_ids(r["subject"])):
                self.group(("closed-was", comp), "low",
                           lambda n, w, c=comp: f"{n} `closed` record{'s' if n > 1 else ''} of a thread in `{self.rel(c)}` {'carry' if n > 1 else 'carries'} a `Was`",
                           w, "`templates/history.md`, the comment (a thread that closes gets a `closed` record, no `Was`: the closed file is the archive)",
                           "a record is never rewritten: the principal decides whether these stand as written; the next closing carries no `Was`")
            m = re.match(r"^mined:\s*(\w+)", r["reason"])
            if m and m.group(1) not in MINED_WORDS:
                self.add("low", f"A mining record carries the state `{m.group(1)}`", w,
                         "`templates/history.md`, the records of state (`mined: pending | partial | mined | dropped`)",
                         "one of the four words", immediate=True)
            m = re.match(r"^state:\s*([^;]+?)\s*(?:;|$)", r["reason"])
            if m and m.group(1) not in WORK_STATES:
                self.add("low", f"A state record carries the state `{m.group(1)}`", w,
                         "`templates/history.md`, the records of state (`state: current | stale | by hand`)",
                         "one of the three words", immediate=True)
        if recs and version and recs[-1]["version"] != version:
            self.add("medium", f"`{self.rel(doc)}` stands at {version} while the newest record of its history is at {recs[-1]['version']}",
                     [self.where(doc, 1), self.where(comp, recs[-1]["line"])],
                     f"{rule_vs} (the record is written in the same step as the change)",
                     "a record of the version the header carries, or the header at the version the log reached")

    # -- 2. the ledger's own reports
    def ledger_reports(self):
        text = self.ledger.compose(self.p)
        front, body = fd.split_front(text)
        for line in front or []:
            m = re.match(r"^unparsed:\s*(\S+?):(\d+)\s*\((.*)\)$", line)
            if m:
                self.add("medium", f"The ledger could not parse `{m.group(1)}` at line {m.group(2)}: {m.group(3)}",
                         f"`{m.group(1)}:{m.group(2)}`", "`templates/ledger.md`, the header (`unparsed:`, POS.1600)",
                         "bring the file to the shape its skeleton owns", immediate=True)
        inside = False
        for line in body.split("\n"):
            if line.startswith("## "):
                inside = line.strip() == "## Reports"
                continue
            if inside and line.startswith("- "):
                item = line[2:].strip()
                sev = "medium" if ("defined twice" in item or "touched by a later commit" in item) else "low"
                where = ""
                m = re.search(r"\b(threads/\S+|[\w./-]+\.md)\b", item)
                if "touched by a later commit" in item:
                    m2 = re.match(r"(THR\.\d{4,5})", item)
                    where = f"`threads/{m2.group(1)}.md`" if m2 else "`threads/`"
                elif m:
                    where = f"`{m.group(1)}`"
                self.add(sev, f"The ledger reports: {item}", where or "the ledger's Reports section",
                         "`templates/ledger.md`, the Reports section (what the merged files cannot say, POS.1640)",
                         "settle it as the report says: an ID is defined once, a closed thread is not touched, a cited thread has its file or its closed record")

    # -- 3. records and companions
    def records_and_companions(self):
        pub = self.proj / "published"
        if pub.is_dir():
            files = {f.name for f in pub.iterdir() if f.suffix != ".md"}
            named = set()
            for c in sorted(pub.glob("*.md")):
                text = fd.read(c)
                front, _ = fd.split_front(text)
                keys = fc.front_keys(front)
                extra, missing = [k for k in keys if k not in PUBLISHED_KEYS], [k for k in PUBLISHED_KEYS if k not in keys]
                if extra or missing:
                    self.add("low", f"The published companion `{self.rel(c)}` differs from the shape of /publish step 6" +
                             (f": extra {', '.join(extra)}" if extra else "") + (f": missing {', '.join(missing)}" if missing else ""),
                             self.where(c, 1), "`.claude/skills/publish/SKILL.md`, step 6 (the one owner of the companion's shape; POS.1610)",
                             "the six keys of step 6 and nothing else", immediate=True)
                file = fd.front_value(front, "file") or ""
                named.add(file)
                if file and file not in files:
                    self.add("medium", f"The published companion `{self.rel(c)}` names `{file}`, which is not in `published/`",
                             self.where(c, fc.line_of(text, r"^file:", re.M)),
                             "CLAUDE.md, Repository layout (the companion: the provenance of the published file)",
                             "the file beside its companion, or the companion removed with the file")
            for f in sorted(files - named):
                self.add("medium", f"`published/{f}` has no companion", f"`published/{f}`",
                         "`.claude/skills/publish/SKILL.md`, step 6 (a published file carries its companion `published/<recipe>.md`)",
                         "write the companion from what the file was made from, or re-publish")
        # the work files against their specifications' Inputs (POS.1520)
        for spec in sorted(self.proj.glob("work/*.spec.md")):
            stext = fd.read(spec)
            sfront, sbody = fd.split_front(stext)
            file = fd.front_value(sfront, "file")
            wf = self.proj / file if file else None
            if not wf or not wf.exists():
                continue
            m = re.search(r"^## Inputs\s*\n(.*?)(?=^## |\Z)", sbody, re.S | re.M)
            allowed = fc.expand_ranges(m.group(1)) if m else set()
            allowed |= {x.group(1) for x in re.finditer(r"^- \*\*([A-Z]{3}\.\d{4,5})\*\*", sbody, re.M)}
            wtext = fd.read(wf)
            cited = {}
            for n, line in enumerate(wtext.split("\n"), 1):
                for id_ in WORK_CITED.findall(line):
                    cited.setdefault(id_, n)
            outside = sorted((i for i in cited if i not in allowed), key=lambda i: (i[:3], int(i[4:])))
            if outside:
                self.add("medium", f"The work file `{self.rel(wf)}` cites {', '.join(outside)}, which its specification's Inputs do not name",
                         [self.where(wf, cited[i]) for i in outside[:6]],
                         "POS.1520 of the forge intent (the file has moved past the way and the why); CLAUDE.md, Document kinds (work)",
                         f"name the items among the Inputs of `{self.rel(spec)}` at its next write, or cut the citation from the file")
        # the thread files
        tkeys = fc.template_keys("thread")
        states = {p.stem for p in STATES_DIR.glob("*.md")}
        tcomment = fc.template_comment("thread")
        recorded = {}
        for comp, recs in self.p.histories.items():
            for r in recs:
                for s in fd.subject_ids(r["subject"]):
                    recorded.setdefault(s, set()).add(r["kind"])
        archived = set()
        for f in list(self.proj.rglob("*.history.archive.md")) + [self.proj / "ledger.archive.md"]:
            if f.exists():
                archived |= set(re.findall(r"THR\.\d{4,5}", fd.read(f)))
        tdir = self.proj / "threads"
        for f in sorted(tdir.glob("*.md")) if tdir.is_dir() else []:
            text = fd.read(f)
            front, body = fd.split_front(text)
            if not re.fullmatch(r"THR\.\d{4,5}\.md", f.name):
                self.add("low", f"`{self.rel(f)}` is not named `THR.NNNN.md`", self.where(f),
                         "CLAUDE.md, Repository layout (`threads/THR.NNNN.md`); `templates/thread.md`", "one file per thread, named by its ID")
                continue
            if front is None:
                self.add("medium", f"The thread `{self.rel(f)}` has no header", self.where(f, 1),
                         "`templates/thread.md` (the header is the thread's state)", "the four fields of the skeleton", immediate=True)
                continue
            keys = fc.front_keys(front)
            extra, missing = [k for k in keys if k not in tkeys], [k for k in tkeys if k not in keys]
            if extra or missing:
                self.add("low", f"The thread `{self.rel(f)}` header differs from the skeleton's" +
                         (f": extra {', '.join(extra)}" if extra else "") + (f": missing {', '.join(missing)}" if missing else ""),
                         self.where(f, 1), "`templates/thread.md`, the header (`id`, `concerns`, `origin`, `status`)",
                         "the four fields and nothing else", immediate=True)
            id_ = fd.front_value(front, "id")
            if id_ and id_ != f.stem:
                self.add("medium", f"The thread `{self.rel(f)}` says `id: {id_}`", self.where(f, fc.line_of(text, r"^id:", re.M)),
                         "`templates/thread.md`; CLAUDE.md, ID scheme (IDs are global and stable)", "the id is the file's name", immediate=True)
            status = fd.front_value(front, "status")
            if status not in ("open", "closed"):
                self.add("low", f"The thread `{self.rel(f)}` carries status `{status}`", self.where(f, fc.line_of(text, r"^status:", re.M) or 1),
                         "`templates/thread.md` (`open | closed`)", "one of the two words", immediate=True)
            concerns = [c.strip() for c in (fd.front_value(front, "concerns") or "").split(",") if c.strip()]
            unknown = [c for c in concerns if c not in states]
            if unknown:
                self.add("low", f"The thread `{self.rel(f)}` concerns `{', '.join(unknown)}`, which is no state of the forge",
                         self.where(f, fc.line_of(text, r"^concerns:", re.M)),
                         "`templates/thread.md` (`concerns`: the artefact, as /forge names it); CLAUDE.md, Document chain (the states are the listing of `.claude/skills/forge/states/`)",
                         f"one of: {', '.join(sorted(states))}", immediate=True)
            origin = fd.front_value(front, "origin") or ""
            if origin not in ("the principal", "Claude's synthesis") and not (self.proj / origin).exists() and not (fr.ENGINE_ROOT / origin).exists():
                self.add("low", f"The thread `{self.rel(f)}` carries an origin the skeleton does not know: `{origin}`",
                         self.where(f, fc.line_of(text, r"^origin:", re.M) or 1),
                         "`templates/thread.md` (`origin`: the principal | a document by path | Claude's synthesis)",
                         "one of the three: the principal's word, a path that exists, or Claude's synthesis", immediate=True)
            kinds = recorded.get(f.stem, set())
            if not kinds and f.stem not in archived:
                self.add("low", f"The thread {f.stem} has no record of its birth in any history",
                         [self.where(f, 1), "`10-intent.history.md`"],
                         "`templates/history.md`, the comment (at a birth, one record naming every item born); `.claude/skills/forge/states/intent.md`, Threads and files",
                         f"a `created` record naming {f.stem} in the intent's history, at the version of the round that opened it (a record of state, POS.1630)",
                         immediate=True)
            if status == "closed" and "closed" not in kinds and f.stem not in archived:
                self.add("medium", f"The thread {f.stem} is closed without a `closed` record in any history",
                         [self.where(f, fc.line_of(text, r"^status:", re.M)), "`10-intent.history.md`"],
                         "`.claude/skills/forge/states/intent.md`, Threads and files (closing is `status: closed` and a `closed` record in the intent's history saying when and by what)",
                         f"the `closed` record of {f.stem} in the intent's history")
            cs = fc.comments(body)
            if tcomment and cs and cs[-1][1].startswith("A thread (POS.1680)") and cs[-1][1] != tcomment:
                self.group("thread-comment", "low",
                           lambda n, w: f"{n} thread file{'s carry' if n > 1 else ' carries'} the skeleton's comment as it stood before the current `templates/thread.md`",
                           self.where(f, cs[-1][0] + len(front) + 2), "CLAUDE.md, Templates; `templates/thread.md`, the comment",
                           "the template's comment as it stands on disk, or none, in each", immediate=True)
        # the Verdict words
        dec = self.proj / "decisions.md"
        if dec.exists():
            for n, line in enumerate(fd.read(dec).split("\n"), 1):
                m = re.match(r"^- \*\*Verdict:\*\*\s*([A-Z]{3}\.\d{4,5})\s+(.*?)\s*$", line)
                if m and not VERDICT_WORDS.match(m.group(2)):
                    self.add("low", f"A Verdict on {m.group(1)} carries a word the skeleton does not know: `{m.group(2)}`",
                             self.where(dec, n), "`templates/decisions.md` (`rejected | parked until <what> | obsolete`); `templates/ledger.md`, Findings",
                             "a decision record keeps the word it was written with; a new record with the skeleton's word supersedes it")

    # -- 4. dependencies
    def dependencies(self):
        for path, lib, used, _ in self.ledger.dependencies(self.p):
            if not (fr.ENGINE_ROOT / path).exists():
                self.add("low", f"library `{lib}` not cloned alongside — `/import-project <its remote>`",
                         [f"`{path}` (cited by {used})"], "CLAUDE.md, Ledger; POS.1020 (a dependency is a citation of another project's documents)",
                         "advisory: bring the project in with `/import-project`, or leave it until it is needed")

    # -- 5. resource indexes
    def resource_indexes(self):
        icomment = fc.template_comment("index")
        ikeys = fc.template_keys("index")
        for which in ("sources", "research"):
            d = self.proj / which
            idx = d / "00-INDEX.md"
            if not d.is_dir():
                continue
            if not idx.exists():
                self.add("medium", f"`{which}/` has no `00-INDEX.md`", f"`{which}/`",
                         "CLAUDE.md, Document chain, External inputs (every `sources/` and `research/` directory carries a `00-INDEX.md`)",
                         "create it from `templates/index.md` and register every file", immediate=True)
                continue
            text = fd.read(idx)
            front, body = fd.split_front(text)
            keys = fc.front_keys(front)
            if front is None or [k for k in keys if k not in ikeys] or [k for k in ikeys if k not in keys]:
                self.add("low", f"`{which}/00-INDEX.md` header differs from the skeleton's", self.where(idx, 1),
                         "`templates/index.md`, the header (`project`, `directory`)", "the two keys and nothing else", immediate=True)
            elif fd.front_value(front, "directory") != which:
                self.add("low", f"`{which}/00-INDEX.md` says `directory: {fd.front_value(front, 'directory')}`",
                         self.where(idx, fc.line_of(text, r"^directory:", re.M)), "`templates/index.md`, the header", f"`directory: {which}`", immediate=True)
            cs = fc.comments(body)
            if icomment and (not cs or cs[0][1] != icomment):
                self.group("index-comment", "low",
                           lambda n, w: f"{n} resource index{'es carry' if n > 1 else ' carries'} a comment that is not the skeleton's as it stands",
                           self.where(idx, (cs[0][0] + len(front) + 2) if cs and front else 1),
                           "CLAUDE.md, Templates; `templates/index.md`, the comment", "the template's comment, as it stands on disk, in each", immediate=True)
            entries = fd.index_entries(idx)
            names = {}
            for e in entries:
                if e["name"].startswith("projects/"):
                    continue  # a citation of another project's documents (POS.1020), not a file here
                for name in entry_names(e):
                    names[name] = e
            self.ignore = ignore_patterns(d / ".gitignore")
            on_disk = {f.name for f in d.iterdir() if f.name != "00-INDEX.md" and not f.name.startswith(".")}
            for name in sorted(n for n in on_disk - set(names) if not self.ignored(n)):
                self.group(("unregistered", which), "low",
                           lambda n, w, d=which: f"{n} file{'s' if n > 1 else ''} of `{d}/` {'are' if n > 1 else 'is'} on disk and registered nowhere",
                           f"`{which}/{name}`",
                           "CLAUDE.md, Document chain, External inputs (`/ingest` stores, registers and catalogues; `/check` verifies index against directory)",
                           f"register each with `/ingest`" if which == "sources" else "an entry for each in `research/00-INDEX.md`", immediate=True)
            for name in sorted(n for n in set(names) - on_disk if not self.ignored(n)):
                self.group(("entry-no-file", idx), "low",
                           lambda n, w, d=which: f"{n} entr{'ies' if n > 1 else 'y'} of `{d}/00-INDEX.md` name{'' if n > 1 else 's'} a file that is not on disk",
                           self.where(idx, fc.line_of(text, r"^### `" + re.escape(names[name]['name']) + "`", re.M)) + f" (`{name}`)",
                           "CLAUDE.md, Document chain, External inputs (the index agrees with its directory)",
                           "drop the entry, or bring the file back", immediate=True)
            for name, e in sorted(names.items()):
                hline = fc.line_of(text, r"^### `" + re.escape(e["name"]) + "`", re.M)
                f = e["fields"]
                if which == "sources":
                    for field in ("Date", "Form"):
                        if field not in f:
                            self.add("low", f"The sources entry `{name}` has no `{field}` field", self.where(idx, hline),
                                     "`templates/index.md`, the sources entry; CLAUDE.md, Document chain, External inputs (date, origin and form are fields of the entry)",
                                     f"add the `{field}` line in the skeleton's form", immediate=True)
                    if "Date" in f:
                        m = re.match(r"^(\d{4}-\d{2}-\d{2})(?:,\s*from (.+?))?\s*$", f["Date"])
                        if not m or (m.group(2) and m.group(2) not in DATE_ORIGINS):
                            self.group("date-form", "low",
                                       lambda n, w: f"{n} Date field{'s' if n > 1 else ''} of `sources/00-INDEX.md` {'are' if n > 1 else 'is'} not in the skeleton's form",
                                       self.where(idx, hline) + f" (`{name}`: `{f['Date']}`)",
                                       "`templates/index.md`, the sources entry (`YYYY-MM-DD, from the content | the file | the ingest`); CLAUDE.md, Document chain, External inputs (the fixed free-text fields the skeleton shows)",
                                       "one date and one of the three origins in each; what else the field said belongs in What or Origin", immediate=True)
                    if "Form" in f and not FORM_RE.match(f["Form"]):
                        self.group("form-form", "low",
                                   lambda n, w: f"{n} Form field{'s' if n > 1 else ''} of `sources/00-INDEX.md` {'are' if n > 1 else 'is'} not in the skeleton's vocabulary",
                                   self.where(idx, hline) + f" (`{name}`: `{f['Form']}`)",
                                   "`templates/index.md`, the sources entry (`text | extract of <original> | binary`, POS.1040)",
                                   "one of the three forms in each; what else the field said belongs in What", immediate=True)
                    if (d / name).is_dir():
                        self.bundle(d / name)
                else:
                    missing = [x for x in ("Question", "Answer in short", "Consult when") if x not in f]
                    if missing:
                        self.add("low", f"The research entry `{name}` lacks {', '.join('`' + x + '`' for x in missing)}", self.where(idx, hline),
                                 "`templates/index.md`, the research entry", "the three fields of the skeleton", immediate=True)

    def bundle(self, bdir):
        idx = bdir / "00-INDEX.md"
        if not idx.exists():
            self.add("low", f"The bundle `{self.rel(bdir)}/` has no `00-INDEX.md` of its own", f"`{self.rel(bdir)}/`",
                     "CLAUDE.md, Document chain, External inputs (every bundle carries its own `00-INDEX.md`, skeleton `templates/index-bundle.md`)",
                     "create it from `templates/index-bundle.md` and catalogue every file", immediate=True)
            return
        text = fd.read(idx)
        front, body = fd.split_front(text)
        bkeys = fc.template_keys("index-bundle")
        keys = fc.front_keys(front)
        if front is None or [k for k in keys if k not in bkeys] or [k for k in bkeys if k not in keys]:
            self.add("low", f"`{self.rel(idx)}` header differs from the bundle skeleton's", self.where(idx, 1),
                     "`templates/index-bundle.md`, the header (`bundle`, `project`, `date`, `origin`)", "the four keys and nothing else", immediate=True)
        bcomment = fc.template_comment("index-bundle")
        cs = fc.comments(body)
        if bcomment and (not cs or cs[0][1] != bcomment):
            self.group("bundle-comment", "low",
                       lambda n, w: f"{n} bundle index{'es carry' if n > 1 else ' carries'} a comment that is not the bundle skeleton's as it stands",
                       self.where(idx, (cs[0][0] + len(front) + 2) if cs and front else 1),
                       "`templates/index-bundle.md`, the comment (the one owner of the bundle index, POS.1070)", "the template's comment, as it stands on disk, in each", immediate=True)
        names = set()
        for e in fd.index_entries(idx):
            names |= set(entry_names(e))
        on_disk = {f.relative_to(bdir).as_posix() for f in bdir.rglob("*")
                   if f.is_file() and f.name != "00-INDEX.md" and not f.name.startswith(".")
                   and not self.ignored(bdir.name + "/" + f.relative_to(bdir).as_posix())}
        for name in sorted(on_disk - names):
            self.add("low", f"`{self.rel(bdir / name)}` is in the bundle and not in its index", f"`{self.rel(bdir / name)}`",
                     "CLAUDE.md, Document chain, External inputs (a bundle's `00-INDEX.md` catalogues its files)", "an entry in the bundle's index", immediate=True)
        for name in sorted(n for n in names - on_disk if not self.ignored(bdir.name + "/" + n)):
            self.group(("entry-no-file", idx), "low",
                       lambda n, w, i=idx: f"{n} entr{'ies' if n > 1 else 'y'} of `{self.rel(i)}` name{'' if n > 1 else 's'} a file that is not in the bundle",
                       self.where(idx, fc.line_of(text, r"^### `" + re.escape(name), re.M)) + f" (`{name}`)",
                       "CLAUDE.md, Document chain, External inputs (the index agrees with its directory)", "drop the entry, or bring the file back", immediate=True)

    # -- run
    def run(self):
        if self.p.old_shape:
            self.add("medium", "The project is of the shape before the migration", "`project.md` (absent)",
                     "`templates/project.md`, the comment (a project without the project file is of the shape before the migration; a check reports it as one finding and raises nothing else)",
                     "`/migrate` (scripts/forge-migrate.py), on the principal's word")
            return
        self.front_matter_and_history()
        self.ledger_reports()
        self.records_and_companions()
        self.dependencies()
        self.resource_indexes()
        self.close_groups()
        self.left = [
            "Known findings and decided-once (the contract): a finding already filed is not named by its ID here, and a finding a DEC rejected is not held back; the comparison at the walkthrough does that until the script carries the key of a finding.",
            "What the entries of an index say, and whether a text belongs in a document or its history (the `history` check): never this script's.",
        ]


def main(argv):
    ft.utf8_console()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1].strip())
    ap.add_argument("check", choices=["light"], help="the check to run")
    ap.add_argument("slug", help="the project ('forge' = the engine's own project)")
    ap.add_argument("--out", help="write the report here instead of stdout")
    a = ap.parse_args(argv)
    fr.need_git()
    c = Light(a.slug)
    c.run()
    text = fc.report(a.check, f"projects/{a.slug}", TODAY, c.findings, c.left, c.facts)
    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(text, encoding="utf-8")
        fr.say(f"{a.slug}: check {a.check} written to {a.out} ({len(c.findings)} findings)", "green")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
