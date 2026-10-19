"""
docs_map.py - the one reader of the documentation map, shared by the
docs-* scripts (docs-state, docs-index, docs-check). Not a command.

The map's shape is the skeleton `templates/docs-map.md`: a
front-matter (`target`, `owner`; the previous map comes from git,
docs-state --previous), a
`## Paths` section with one line per reader, and one entry per page:

    ### docs/<section>/<page>.md
    - <field>: <value>
      <continuation lines, indented>

`parse(text)` returns `(front, entries)`; an entry is a dict with
`path`, `section`, `name`, `fields` (field -> joined value) and
`lines` (the entry's lines, verbatim, heading included).
`reader_paths(text)` returns the Paths section as a list of
`(reader, [page path, ...])` in the order written.

`target_root(map_path, front)` is the directory every input path of
the map is relative to: the engine root when `target: engine`
(the map lies in `projects/forge`), else the owning project's
directory, where the map lies.

An input is a file, or a part of one named after `#`: a section by
its heading (`CLAUDE.md#Isolated reviewers`: the heading line to the
next heading of the same or a higher level), an item by its ID
(`10-intent.md#POS.1450`: the line that carries `**POS.1450**` to
the next line that opens an item at the same indent, or a heading)
or a block by its bold label (`brief.md#Inputs`: the paragraph
opening with `**Inputs.**` to the next label or heading, where no
heading of that name exists).
`input_parts(entry)` returns `[(path, part or None), ...]`;
`part_text(root, path, part)` returns the text of that part, or
None when the file or the part is not found (POS.1450: an input
hashed as the part, so that a change elsewhere in the file leaves
the page as it is).
"""

import re
from pathlib import Path

ORDER = ["start", "use", "about", "extend", "reference"]
ENTRY_RE = re.compile(r"^### (docs/([a-z]+)/(.+?)\.md)\s*$")
FIELD_RE = re.compile(r"^- (\w[\w-]*):\s*(.*)$")
PATHS_LINE_RE = re.compile(r"^- (\w+):\s*(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
ID_RE = re.compile(r"^[A-Z]{3}\.\d{4,5}$")  # four digits, a fifth beyond 9999 (POS.0220)


def parse(text):
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
                       "name": m.group(3), "fields": {}, "lines": [line]}
            entries.append(current)
            field = None
            continue
        if line.startswith("## "):
            current = None
            field = None
            continue
        if current is None:
            continue
        current["lines"].append(line)
        fm = FIELD_RE.match(line)
        if fm:
            field = fm.group(1)
            current["fields"][field] = fm.group(2).strip()
            continue
        if field and line.startswith("  "):
            current["fields"][field] = (current["fields"][field] + " " + line.strip()).strip()
    for e in entries:
        while e["lines"] and not e["lines"][-1].strip():
            e["lines"].pop()
    return front, entries


def reader_paths(text):
    """The `## Paths` section: [(reader, [page path, ...]), ...]."""
    out = []
    inside = False
    for line in text.splitlines():
        if line.startswith("## "):
            inside = line.strip().lower() == "## paths"
            continue
        if not inside:
            continue
        m = PATHS_LINE_RE.match(line)
        if m:
            pages = [p.strip().strip("`") for p in m.group(2).split(",")]
            out.append((m.group(1), [p for p in pages if p]))
    return out


def target_root(map_path, front):
    map_path = Path(map_path).resolve()
    if front.get("target", "").strip() == "engine":
        return map_path.parent.parent.parent
    return map_path.parent


def _input_tokens(entry):
    raw = entry["fields"].get("inputs", "")
    toks = []
    for tok in raw.split():
        tok = tok.strip().strip("`").rstrip(",")
        if tok and tok != "-" and not tok.endswith(":"):
            toks.append(tok)
    return toks


def input_parts(entry):
    """The entry's inputs as [(path, part or None), ...]. A part follows
    `#`; a heading with spaces is written with the spaces, so tokens
    after a `#` token that carry no `/` and no `.` are joined to it."""
    out = []
    for tok in _input_tokens(entry):
        if "#" in tok:
            path, _, part = tok.partition("#")
            out.append([path, part])
        elif out and out[-1][1] is not None and not ID_RE.match(out[-1][1]) \
                and "/" not in tok and not tok.endswith(".md") and not tok.endswith(".py") \
                and not tok.endswith(".json"):
            out[-1][1] = out[-1][1] + " " + tok
        else:
            out.append([tok, None])
    return [(p, q) for p, q in out]


def input_paths(entry):
    """The entry's input files, without the parts, each once."""
    return list(dict.fromkeys(p for p, _ in input_parts(entry)))


def part_text(root, rel, part):
    """The text of the part of a file, or None when not found."""
    p = Path(root) / rel
    if not p.is_file():
        return None
    text = p.read_text(encoding="utf-8", errors="replace")
    if part is None:
        return text
    lines = text.splitlines()
    if ID_RE.match(part):
        marker = re.compile(r"\*\*" + re.escape(part) + r"(\*\*|\s)")
        start = None
        for i, line in enumerate(lines):
            if line.lstrip().startswith(("- ", "* ")) and marker.search(line):
                start = i
                break
        if start is None:
            return None
        indent = len(lines[start]) - len(lines[start].lstrip())
        end = len(lines)
        for j in range(start + 1, len(lines)):
            l = lines[j]
            if HEADING_RE.match(l):
                end = j
                break
            if (len(l) - len(l.lstrip())) == indent and l.lstrip().startswith(("- ", "* ")):
                end = j
                break
        return "\n".join(lines[start:end]).rstrip() + "\n"
    want = part.strip().lower()
    start = None
    level = 0
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line)
        if m and m.group(2).strip().lower() == want:
            start, level = i, len(m.group(1))
            break
    if start is None:
        # a block by its bold label: `**Inputs.**` opening a paragraph
        label = re.compile(r"\*\*" + re.escape(part.strip()) + r"\.?\*\*", re.IGNORECASE)
        any_label = re.compile(r"\*\*[^*]+\*\*")
        for i, line in enumerate(lines):
            if label.match(line.lstrip()):
                start = i
                break
        if start is None:
            return None
        end = len(lines)
        for j in range(start + 1, len(lines)):
            l = lines[j]
            if HEADING_RE.match(l) or any_label.match(l.lstrip()):
                end = j
                break
        return "\n".join(lines[start:end]).rstrip() + "\n"
    end = len(lines)
    for j in range(start + 1, len(lines)):
        m = HEADING_RE.match(lines[j])
        if m and len(m.group(1)) <= level:
            end = j
            break
    return "\n".join(lines[start:end]).rstrip() + "\n"


def linked_paths(entry):
    """The paths of the pages the entry links to, in order, without the
    entry's own path."""
    body = "\n".join(l for l in entry["lines"] if not l.startswith("### "))
    found = re.findall(r"`(docs/[a-z]+/[^`]+\.md)`", body)
    return [p for p in dict.fromkeys(found) if p != entry["path"]]


def intent_version(map_path):
    """The version of the owning project's intent beside the map, or None."""
    intent = Path(map_path).parent / "10-intent.md"
    if not intent.exists():
        return None
    for line in intent.read_text(encoding="utf-8").splitlines()[:12]:
        if line.startswith("version:"):
            return line.split(":", 1)[1].strip()
    return None
