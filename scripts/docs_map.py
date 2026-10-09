"""
docs_map.py - the one reader of the documentation map, shared by the
docs-* scripts (docs-state, docs-index, docs-check). Not a command.

The map's shape is the skeleton `templates/docs-map.md`: a
front-matter (`generated`, `target`, `owner`, `previous`) and one
entry per page:

    ### docs/<section>/<page>.md
    - <field>: <value>
      <continuation lines, indented>

`parse(text)` returns `(front, entries)`; an entry is a dict with
`path`, `section`, `name`, `fields` (field -> joined value) and
`lines` (the entry's lines, verbatim, heading included).

`target_root(map_path, front)` is the directory every input path of
the map is relative to: the engine root when `target: engine`
(the map lies in `projects/forge`), else the owning project's
directory, where the map lies.
"""

import re
from pathlib import Path

ORDER = ["start", "use", "about", "extend", "reference"]
ENTRY_RE = re.compile(r"^### (docs/([a-z]+)/(.+?)\.md)\s*$")
FIELD_RE = re.compile(r"^- (\w[\w-]*):\s*(.*)$")


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


def target_root(map_path, front):
    map_path = Path(map_path).resolve()
    if front.get("target", "").strip() == "engine":
        return map_path.parent.parent.parent
    return map_path.parent


def input_paths(entry):
    """The entry's inputs as a list of relative paths (the `inputs` field,
    one path per line in the map, joined by parse into one string)."""
    raw = entry["fields"].get("inputs", "")
    paths = []
    for tok in raw.split():
        tok = tok.strip().strip("`").rstrip(",")
        if tok and tok != "-" and not tok.endswith(":"):
            paths.append(tok)
    return paths


def linked_paths(entry):
    """The paths of the pages the entry links to, in order, without the
    entry's own path."""
    body = "\n".join(l for l in entry["lines"] if not l.startswith("### "))
    found = re.findall(r"`(docs/[a-z]+/[^`]+\.md)`", body)
    return [p for p in dict.fromkeys(found) if p != entry["path"]]
