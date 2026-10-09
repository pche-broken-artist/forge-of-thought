#!/usr/bin/env python3
"""
docs-index.py - derive the documentation index from the documentation map.

SYNOPSIS
    python scripts/docs-index.py <map> <docs-dir> [--date YYYY-MM-DD]

WHAT IT DOES
    Reads the documentation map a `docs-planner` run wrote (one entry
    per page: `### docs/<section>/<page>.md` followed by `- title:`,
    `- kind:`, `- reader:`, `- says:` and more) and writes
    `<docs-dir>/README.md`: one line per page, grouped by section in
    the order of the outline (start, use, about, extend, reference),
    each line the page's title linked to its relative path and the
    first sentence of its `says`. Deterministic: the same map gives
    the same index. No model is involved.

    The index is a derivation of the map and never edited by hand:
    change the map (through the planner) and run this script again.

WHAT IT NEEDS
    Python 3.8 or newer. Nothing else.

NOTES
    The front-matter of the index names the map as its one input and
    carries the version of the owning project's intent (`10-intent.md`
    beside the map), which for the engine is its version; the opening
    says the same in words.
    The opening paragraph and the three reading paths are fixed text
    of this script, the one place that owns them (brief
    `documentation`, THR.0340).

EXAMPLES
    python scripts/docs-index.py projects/forge/docs-map.md docs
    python scripts/docs-index.py projects/<slug>/docs-map.md projects/<slug>/docs
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

ORDER = ["start", "use", "about", "extend", "reference"]
HEADINGS = {
    "start": "Start",
    "use": "Use",
    "about": "About",
    "extend": "Extend",
    "reference": "Reference",
}
PATHS = [
    ("the user", "start/", "then use/ for every job"),
    ("the extender", "extend/", "then reference/ for the shapes"),
    ("the evaluator", "about/", "the concept pages, nothing made for him alone"),
]

ENTRY_RE = re.compile(r"^### (docs/([a-z]+)/(.+?)\.md)\s*$")
FIELD_RE = re.compile(r"^- (\w[\w-]*):\s*(.*)$")


def parse_map(text):
    """Return (front, entries). entries: list of dicts with path, section, fields."""
    entries = []
    current = None
    field = None
    front = {}
    lines = text.splitlines()
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            k, _, v = lines[i].partition(":")
            front[k.strip()] = v.strip()
            i += 1
        i += 1
    for line in lines[i:]:
        m = ENTRY_RE.match(line)
        if m:
            current = {"path": m.group(1), "section": m.group(2),
                       "name": m.group(3), "fields": {}}
            entries.append(current)
            field = None
            continue
        if line.startswith("## "):
            current = None
            field = None
            continue
        if current is None:
            continue
        fm = FIELD_RE.match(line)
        if fm:
            field = fm.group(1)
            current["fields"][field] = fm.group(2).strip()
            continue
        if field and line.startswith("  "):
            current["fields"][field] = (current["fields"][field] + " " + line.strip()).strip()
    return front, entries


def first_sentence(text):
    text = text.strip()
    if not text:
        return ""
    # cut at the first full stop followed by a space or the end, outside backticks
    depth = 0
    for i, ch in enumerate(text):
        if ch == "`":
            depth ^= 1
        elif ch == "." and depth == 0 and (i + 1 == len(text) or text[i + 1] == " "):
            return text[: i + 1]
    return text


def engine_version(map_path):
    """The version of the owning project's intent beside the map, or None."""
    intent = map_path.parent / "10-intent.md"
    if not intent.exists():
        return None
    for line in intent.read_text(encoding="utf-8").splitlines()[:12]:
        if line.startswith("version:"):
            return line.split(":", 1)[1].strip()
    return None


def render(front, entries, map_rel, date, version):
    out = []
    out.append("---")
    out.append(f"generated: {date}")
    if version:
        out.append(f"version: {version}")
    out.append("made: derived")
    out.append("inputs:")
    out.append(f"  - {map_rel}")
    out.append("---")
    out.append("")
    out.append("# Documentation")
    out.append("")
    out.append("This is the documentation of Forge of Thought: pages of one topic")
    out.append("each, generated from the engine as it stands, for three readers.")
    out.append("Every page stands on its own; start where your question is.")
    if version:
        out.append("")
        out.append(f"Generated on {date} for Forge of Thought at version {version}")
        out.append("(the version of the engine's intent; a release carries the same")
        out.append("number).")
    out.append("")
    out.append("## Where to start")
    out.append("")
    for who, where, then in PATHS:
        out.append(f"- **{who}**: `{where}`, {then}.")
    out.append("")
    by_section = {}
    for e in entries:
        by_section.setdefault(e["section"], []).append(e)
    for sec in ORDER + [s for s in by_section if s not in ORDER]:
        if sec not in by_section:
            continue
        out.append(f"## {HEADINGS.get(sec, sec.capitalize())}")
        out.append("")
        for e in by_section[sec]:
            f = e["fields"]
            if f.get("state", "").strip() == "remove":
                continue
            title = f.get("title") or e["name"].replace("-", " ").capitalize()
            rel = e["path"][len("docs/"):]
            says = first_sentence(f.get("says", ""))
            line = f"- [{title}]({rel})"
            if says:
                line += f": {says}"
            out.append(line)
        out.append("")
    out.append("The map these pages are generated from, with every page's inputs,")
    out.append(f"is `{map_rel}`. This index is derived from it by")
    out.append("`scripts/docs-index.py` and never edited by hand.")
    out.append("")
    return "\n".join(out)


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1].strip())
    ap.add_argument("map", help="path of the documentation map")
    ap.add_argument("docs", help="documentation directory; README.md is written into it")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    a = ap.parse_args(argv)
    map_path = Path(a.map)
    text = map_path.read_text(encoding="utf-8")
    front, entries = parse_map(text)
    if not entries:
        print("no entries found in the map", file=sys.stderr)
        return 1
    docs = Path(a.docs)
    docs.mkdir(parents=True, exist_ok=True)
    map_rel = map_path.as_posix()
    out = render(front, entries, map_rel, a.date, engine_version(map_path))
    (docs / "README.md").write_text(out, encoding="utf-8", newline="\n")
    print(f"{len(entries)} entries, index written to {docs / 'README.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
