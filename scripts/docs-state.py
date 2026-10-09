#!/usr/bin/env python3
"""
docs-state.py - compute the state of every page of the documentation
from the content of its inputs, and prepare the writers' tasks.

SYNOPSIS
    python scripts/docs-state.py <map> <docs-dir> --tasks <tmp-dir> [--date YYYY-MM-DD]

WHAT IT DOES
    Reads the documentation map (`docs_map.py` is its reader) and, for
    every entry, hashes the entry's text (its `state` line excepted)
    together with the content of every input file the entry names.
    The page that exists at the entry's path carries in its
    front-matter the hash it was made from, `inputs-hash`; the two are
    compared and the entry's `state` is set in the map:
        new         no page at the path
        regenerate  a page exists, its hash differs (an input or the
                    entry changed)
        keep        a page exists with the same hash
    A page under <docs-dir> that no entry names is listed as `remove`
    (the index `README.md` excepted). The state is computed, never
    judged: a page whose inputs did not change is not regenerated.

    For every `new` or `regenerate` entry one task file is written to
    <tmp-dir>: the engine root, the page's path, the date, the hash
    the page is to carry, the entry verbatim and the titles of the
    pages it links to. The task is a `docs-writer` agent's whole
    prompt (`.claude/skills/document/SKILL.md`, step 4).

    An input the map names and the disk does not have is reported and
    hashed as missing; the page is regenerated and its writer will
    report the gap.

WHAT IT NEEDS
    Python 3.8 or newer. `docs_map.py` beside it. Nothing else.

NOTES
    The map's `inputs` are relative to the target's root: the engine
    root when `target: engine`, else the owning project's directory.
    The script rewrites only the `- state:` line of each entry and
    leaves the rest of the map byte for byte.

EXAMPLES
    python scripts/docs-state.py projects/forge/docs-map.md docs --tasks tmp/docs-tasks
    python scripts/docs-state.py projects/<slug>/docs-map.md projects/<slug>/docs --tasks tmp/docs-tasks
"""

import argparse
import datetime
import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import docs_map  # noqa: E402

STATE_RE = re.compile(r"^- state:\s*.*$")
HASH_RE = re.compile(r"^inputs-hash:\s*([0-9a-f]+)\s*$", re.M)


def entry_hash(entry, root):
    h = hashlib.sha256()
    for line in entry["lines"]:
        if STATE_RE.match(line):
            continue
        h.update(line.encode("utf-8"))
        h.update(b"\n")
    missing = []
    for rel in docs_map.input_paths(entry):
        p = root / rel
        h.update(f"--- {rel}\n".encode("utf-8"))
        if p.is_file():
            h.update(p.read_bytes())
        else:
            h.update(b"<missing>")
            missing.append(rel)
    return h.hexdigest()[:16], missing


def page_hash(page_path):
    if not page_path.is_file():
        return None
    head = page_path.read_text(encoding="utf-8", errors="replace")[:2000]
    m = HASH_RE.search(head)
    return m.group(1) if m else ""


def set_state(lines, state):
    out, done = [], False
    for line in lines:
        if STATE_RE.match(line):
            out.append(f"- state: {state}")
            done = True
        else:
            out.append(line)
    if not done:
        out.append(f"- state: {state}")
    return out


def task_text(entry, root, docs_dir, date, digest, titles):
    rel = entry["path"][len("docs/"):]
    page = (docs_dir / rel).resolve()
    body = "\n".join(entry["lines"]).rstrip() + "\n"
    linked = docs_map.linked_paths(entry)
    tl = "\n".join(f"- `{p}`: {titles.get(p, '(no title in the map)')}" for p in linked) or "- none"
    return (
        f"Target root (input paths are relative to it): `{root}`.\n"
        f"Page to write: `{page}` (this is `{entry['path']}`; relative links are computed from that place).\n"
        f"Date: {date}.\n"
        f"inputs-hash to carry in the front-matter, exactly: {digest}\n\n"
        f"Your entry from the map, verbatim:\n\n{body}\n"
        f"Titles of the pages your entry links to, to cite them by:\n\n{tl}\n\n"
        f"Write the page, then report in a few lines.\n"
    )


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1].strip())
    ap.add_argument("map")
    ap.add_argument("docs")
    ap.add_argument("--tasks", required=True, help="directory for the writers' task files")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    a = ap.parse_args(argv)
    map_path = Path(a.map)
    text = map_path.read_text(encoding="utf-8")
    front, entries = docs_map.parse(text)
    if not entries:
        print("no entries found in the map", file=sys.stderr)
        return 1
    root = docs_map.target_root(map_path, front)
    docs_dir = Path(a.docs)
    tasks_dir = Path(a.tasks)
    tasks_dir.mkdir(parents=True, exist_ok=True)
    for old in tasks_dir.glob("*.md"):
        old.unlink()
    titles = {e["path"]: e["fields"].get("title", "").strip() for e in entries}

    counts = {"new": 0, "regenerate": 0, "keep": 0}
    all_missing = []
    new_lines = text.splitlines()
    # rebuild the map text entry by entry, replacing only the state line
    for e in entries:
        digest, missing = entry_hash(e, root)
        all_missing += [(e["path"], m) for m in missing]
        rel = e["path"][len("docs/"):]
        have = page_hash(docs_dir / rel)
        state = "new" if have is None else ("keep" if have == digest else "regenerate")
        counts[state] += 1
        if state != "keep":
            name = rel.replace("/", "-").replace(".md", "") + ".md"
            (tasks_dir / name).write_text(task_text(e, root, docs_dir, a.date, digest, titles),
                                          encoding="utf-8", newline="\n")
        # locate the entry's lines in the file and replace the state line
        start = new_lines.index(e["lines"][0])
        end = start + len(e["lines"])
        new_lines[start:end] = set_state(new_lines[start:end], state)
    map_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8", newline="\n")

    mapped = {e["path"] for e in entries}
    remove = sorted(
        (docs_dir / p.relative_to(docs_dir)).as_posix()
        for p in docs_dir.rglob("*.md")
        if p.name != "README.md"
        and ("docs/" + p.relative_to(docs_dir).as_posix()) not in mapped
    )
    print(f"entries {len(entries)}: new {counts['new']}, regenerate {counts['regenerate']}, "
          f"keep {counts['keep']}; remove {len(remove)}; tasks written to {tasks_dir}")
    for r in remove:
        print(f"  remove: {r}")
    for page, m in all_missing:
        print(f"  missing input: {m} (named by {page})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
