#!/usr/bin/env python3
"""
forge-history.py - the history of one item of a project, by its ID,
gathered from the history logs, their archives and the places that
cite it, printed as one timeline.

SYNOPSIS
    python scripts/forge-history.py <ID> <slug> [--full]

WHAT IT DOES
    Read-only, changes nothing, no model involved. For an item named
    by its ID (`PREFIX.NNNN`, CLAUDE.md, ID scheme; a short form such
    as `pos580` is read as `POS.0580`) in the project `projects/<slug>`
    (`forge` is the engine's own project) it prints:
      1. Today: the file that holds the item and its wording, from the
         line that opens the item to the next item or heading (the
         same reader of a part as the documentation scripts use,
         `docs_map.part_text`);
      2. Timeline: one line per event, oldest first, each with its
         version, date where the log has one, and what happened -
         `born`, `changed`, `closed`, `removed`, `approved` from the
         records of every history log of the project (`*.history.md`,
         the artefacts' and the recipes') whose subject names the ID;
         `mentioned by <ID>` from the records of other items that
         name it in their reason, Action or Was; `archive` from the
         rows of the history archives (`*.history.archive.md`) that
         mention it, the sentence that carries the ID. A record's
         reason follows its line; its Action and its Was follow as
         marked lines, Was shortened to its first sentences unless
         --full is given;
      3. Cited today: every other place in the project that names the
         ID, as file:line and the line, shortened: decisions, threads,
         the ledger, reviews, challenges and the other artefacts.
    Every long text is wrapped at 78 columns with a hanging indent.
    An ID with no item and no record is said so. The history is read
    here and printed for the one item, never loaded whole into the
    conversation (CLAUDE.md, Versioning & status): this script is the
    one way Claude reads an item's history before proposing a change
    to it (`/history`, `.claude/skills/history/SKILL.md`).

WHAT IT NEEDS
    Python 3.8 or newer. `forge_repos.py` and `docs_map.py` beside it.

NOTES
    A record is one line of a history log in the shape
    `templates/history.md` owns: date | version | author | subject |
    kind | reason | Action: ... | Was: ...; the subject may name
    several IDs. Lines of a log that are not records (the heading,
    the comment) are skipped. The pages of `docs/`, the map, the
    renders, the resources and `tmp/` are never searched: they are
    outputs or inputs, not the project's record.

EXAMPLES
    python scripts/forge-history.py POS.0580 forge      # a position of the forge intent
    python scripts/forge-history.py sol460 forge        # the short form of SOL.0460
    python scripts/forge-history.py REQ.0120 <slug> --full   # every Was in full
"""

import re
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import docs_map  # noqa: E402
import forge_repos as fr  # noqa: E402
import forge_tools as ft  # noqa: E402

ID_RE = re.compile(r"^[A-Z]{3}\.\d{4}$")
SHORT_RE = re.compile(r"^([A-Za-z]{3})[.\-_ ]?(\d{1,4})$")
RECORD_RE = re.compile(r"^- (\d{4}-\d{2}-\d{2}) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?)(?: \| (.*))?$")
SKIP_DIRS = {"docs", "renders", "published", "tmp", "sources", "research", ".git"}
SKIP_FILES = {"docs-map.md"}
WIDTH = 78
GUTTER = 19  # version and date column


def normalise(arg):
    if ID_RE.match(arg):
        return arg
    m = SHORT_RE.match(arg.strip())
    if m:
        return f"{m.group(1).upper()}.{int(m.group(2)):04d}"
    return None


def version_key(v):
    out = []
    for tok in re.split(r"[.\-]", v.strip()):
        out.append(int(tok) if tok.isdigit() else 0)
    return tuple(out)


def split_tail(tail):
    reason, action, was = "", "", ""
    if not tail:
        return reason, action, was
    parts = tail.split(" | ")
    i = 0
    if parts and not parts[0].startswith(("Action:", "Was:")):
        reason = parts[0].strip()
        i = 1
    for p in parts[i:]:
        if p.startswith("Action:"):
            action = p[len("Action:"):].strip()
        elif p.startswith("Was:"):
            was = p[len("Was:"):].strip()
        else:
            reason = (reason + " | " + p).strip(" |")
    return reason, action, was


def parse_log(path):
    records = []
    for n, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        m = RECORD_RE.match(line)
        if not m:
            continue
        date, version, author, subject, kind, tail = m.groups()
        reason, action, was = split_tail(tail or "")
        records.append({
            "file": path, "line": n, "date": date, "version": version.strip(),
            "author": author.strip(), "subject": subject.strip(), "kind": kind.strip(),
            "reason": reason, "action": action, "was": was,
        })
    return records


def subject_ids(subject):
    return set(re.findall(r"[A-Z]{3}\.\d{4}", subject))


def sentence_with(text, id_):
    for s in re.split(r"(?<=[.;])\s+", text):
        if id_ in s:
            return s.strip()
    return text.strip()


def first_sentences(text, n=1):
    parts = re.split(r"(?<=[.])\s+", text.replace("<br>", " "))
    out = " ".join(parts[:n]).strip()
    return out + (" ..." if len(parts) > n else "")


def files_to_search(project):
    for p in sorted(project.rglob("*.md")):
        rel = p.relative_to(project)
        if any(part in SKIP_DIRS for part in rel.parts) or p.name in SKIP_FILES:
            continue
        yield p


def block(text, indent, first=None):
    """Wrap text at WIDTH with a hanging indent; `first` is the first
    line's prefix (same length as indent or shorter)."""
    first = indent if first is None else first
    return textwrap.fill(" ".join(text.split()), width=WIDTH,
                         initial_indent=first, subsequent_indent=indent)


def main(argv):
    ft.utf8_console()
    full = "--full" in argv
    argv = [a for a in argv if a != "--full"]
    if len(argv) != 2:
        print(__doc__.strip().splitlines()[0])
        print("usage: python scripts/forge-history.py <ID> <slug> [--full]")
        return 2
    id_ = normalise(argv[0])
    slug = argv[1]
    if id_ is None:
        fr.fail(f"not an ID of the forge: {argv[0]} (the shape is PREFIX.NNNN, or a short form such as pos580)")
    project = fr.project_path(slug)
    if not project.is_dir():
        fr.fail(f"no project at {project}")
    doc_rel = lambda p: p.relative_to(project).as_posix()
    short = lambda p: doc_rel(p).replace(".history.archive.md", "").replace(".history.md", "")

    logs = [p for p in files_to_search(project) if p.name.endswith(".history.md")]
    archives = [p for p in files_to_search(project) if p.name.endswith(".history.archive.md")]
    others = [p for p in files_to_search(project)
              if not p.name.endswith((".history.md", ".history.archive.md"))]

    # today
    home, wording = None, None
    for p in others:
        if p.name in ("ledger.md", "decisions.md") or p.name.startswith("00-INDEX"):
            continue
        text = docs_map.part_text(project, doc_rel(p), id_)
        if text:
            home, wording = p, text
            break

    fr.say(f"{id_}  projects/{slug}" + (f"  {doc_rel(home)}" if home else ""), "bold")
    print("-" * WIDTH)
    fr.say("Today", "cyan")
    if home:
        body = " ".join(wording.split())
        body = re.sub(r"^\s*-\s*\*\*" + re.escape(id_) + r"\s*(.*?)\*\*\s*", r"\1 ", body).strip()
        print(block(body, "  "))
    else:
        print("  no file of the project holds an item with this ID today")

    # events
    events = []  # (sort key, lines)
    for log in logs:
        for r in parse_log(log):
            own = id_ in subject_ids(r["subject"])
            mentioned = not own and (id_ in r["reason"] or id_ in r["action"] or id_ in r["was"])
            if not (own or mentioned):
                continue
            key = (1, version_key(r["version"]), r["date"], r["line"])
            label = f"{r['version']}  {r['date']}"
            if own:
                what = "born" if r["kind"] == "created" else r["kind"]
                if r["subject"] != id_:
                    what += f" (with {r['subject']})"
            else:
                what = f"mentioned by {r['subject']}"
            head = f"  {label:<{GUTTER}}{what}"
            if short(r["file"]) not in ("10-intent",):
                head += f"  [{short(r['file'])}]"
            lines = [head]
            pad = " " * (GUTTER + 2)
            if r["reason"]:
                lines.append(block(r["reason"], pad))
            if r["action"]:
                lines.append(block("Action: " + r["action"], pad))
            if r["was"] and (own or full):
                was = r["was"] if full else first_sentences(r["was"])
                lines.append(block("Was: " + was, pad))
            events.append((key, lines))
    for a in archives:
        for n, line in enumerate(a.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if not line.startswith("|") or id_ not in line:
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not cells or cells[0] in ("Version", "---"):
                continue
            cell = next((c for c in cells if id_ in c), line)
            key = (0, version_key(cells[0]), "", n)
            label = f"{cells[0]}"
            head = f"  {label:<{GUTTER}}archive"
            if short(a) not in ("10-intent",):
                head += f"  [{short(a)}]"
            events.append((key, [head, block(sentence_with(cell, id_), " " * (GUTTER + 2))]))
    events.sort(key=lambda e: e[0])

    print()
    fr.say(f"Timeline ({len(events)} events, oldest first; the intent unless marked)", "cyan")
    if not events:
        print("  no record and no archive row names this ID")
    for _, lines in events:
        for l in lines:
            print(l)

    # cited today
    cites = []
    inside = set()
    if home is not None:
        text = home.read_text(encoding="utf-8", errors="replace").splitlines()
        wl = wording.rstrip("\n").splitlines()
        for i in range(len(text) - len(wl) + 1):
            if text[i:i + len(wl)] == wl:
                inside = set(range(i + 1, i + 1 + len(wl)))
                break
    for p in others:
        for n, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if id_ in line and not (p == home and n in inside):
                cites.append((doc_rel(p), n, " ".join(line.split())))
    print()
    fr.say(f"Cited today ({len(cites)} places)", "cyan")
    for rel, n, line in cites:
        where = f"{rel}:{n}"
        print(block(line, " " * 4, first=f"  {where}  ") if len(where) < 30
              else f"  {where}\n" + block(line, " " * 4))
    if home is None and not events and not cites:
        fr.say(f"\nnothing in projects/{slug} knows {id_}", "yellow")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
