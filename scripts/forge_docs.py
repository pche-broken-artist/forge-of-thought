"""
forge_docs.py - what the scripts that read the documents of a project
share: the front-matter of a file, the records of a history companion
(templates/history.md), the tables of a hand-kept ledger or of its
archive (templates/ledger.md), the entries of a resource index
(templates/index.md) and the threads, as files (templates/thread.md)
or in the one file of the shape before the migration. Used by
forge-ledger, forge-migrate and forge-history. Not a command.

A reader here never raises on a malformed file: it returns what it
could read and lists what it could not in `problems`, (path, line,
what) triples, so that a script degrades aloud (POS.1600).
"""

import re
from pathlib import Path

ID_RE = re.compile(r"\b[A-Z]{3}\.\d{4,5}\b")  # four digits, a fifth beyond 9999 (POS.0220)
RECORD_RE = re.compile(
    r"^- (\d{4}-\d{2}-\d{2}) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?)(?: \| (.*))?$")
THREAD_BLOCK_RE = re.compile(r"^- \*\*(THR\.\d{4,5})\*\*\s*(?:\[([^\]]*)\])?\s*(.*)$")
DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")

problems = []


def read(path):
    return Path(path).read_text(encoding="utf-8")


def split_front(text):
    """(front lines without the dashes, body) or (None, text) when the
    file has no front-matter."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[1:i], "\n".join(lines[i + 1:])
    return None, text


def front_value(front, key):
    """The value of `key` in front lines, a trailing `# comment` and
    quotes stripped; None when absent."""
    for line in front or []:
        m = re.match(r"^" + re.escape(key) + r":\s*(.*)$", line)
        if m:
            value = re.sub(r"\s+#.*$", "", m.group(1)).strip()
            return value.strip('"').strip("'")
    return None


def front_list(front, key):
    """A YAML list under `key` (`- item` lines), or the inline value as
    a one-item list."""
    out, inside = [], False
    for line in front or []:
        if inside:
            m = re.match(r"^\s+-\s+(.*)$", line)
            if m:
                out.append(m.group(1).strip())
                continue
            break
        if re.match(r"^" + re.escape(key) + r":\s*$", line):
            inside = True
        else:
            v = front_value([line], key)
            if v is not None:
                return [v]
    return out


def front_of(path):
    """(front lines, body) of a file, the problem noted when the file
    has no front-matter."""
    try:
        front, body = split_front(read(path))
    except (OSError, UnicodeDecodeError) as e:
        problems.append((str(path), 0, f"unreadable: {e}"))
        return None, ""
    if front is None:
        problems.append((str(path), 1, "no front-matter"))
    return front, body


def split_tail(tail):
    """The optional tail of a record: (reason, action, was)."""
    reason, action, was = tail or "", None, None
    if " | Was: " in reason or reason.startswith("Was: "):
        head, _, w = reason.partition("Was: ")
        reason, was = head.rstrip(" |"), w.strip()
    if " | Action: " in reason or reason.startswith("Action: "):
        head, _, a = reason.partition("Action: ")
        reason, action = head.rstrip(" |"), a.strip()
    return reason.strip(), action, was


def records(path):
    """The records of a history companion, oldest first: dicts with
    date, version, author, subject, kind, reason, action, was, line.
    A `- ` line after the first record that is not a record is a
    problem."""
    out = []
    p = Path(path)
    if not p.exists():
        return out
    for n, line in enumerate(read(p).split("\n"), 1):
        m = RECORD_RE.match(line)
        if m:
            reason, action, was = split_tail(m.group(6))
            out.append({"date": m.group(1), "version": m.group(2).strip(), "author": m.group(3).strip(),
                        "subject": m.group(4).strip(), "kind": m.group(5).strip(), "reason": reason,
                        "action": action, "was": was, "line": n})
        elif out and line.startswith("- ") and " | " in line:
            problems.append((str(p), n, "record not in the shape of templates/history.md"))
    return out


def subject_ids(subject):
    return [s.strip() for s in re.split(r",\s*", subject) if s.strip()]


def tables(text):
    """The tables of a ledger or an archive: {section: [row dict]},
    the rows keyed by the table's header cells."""
    out, section, header = {}, None, None
    for line in text.split("\n"):
        if line.startswith("## "):
            section, header = line[3:].strip(), None
            out.setdefault(section, [])
            continue
        if section is None or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            header = cells
            continue
        if all(set(c) <= set("-: ") for c in cells):
            continue
        out[section].append(dict(zip(header, cells)))
    return out


def waiting_lines(text):
    """The `- ` lines under Waiting on principal of a hand-kept ledger,
    a wrapped line joined."""
    lines, inside, current = [], False, None
    for line in text.split("\n"):
        if line.startswith("## "):
            if current:
                lines.append(current)
                current = None
            inside = line.startswith("## Waiting")
            continue
        if not inside:
            continue
        if line.startswith("- "):
            if current:
                lines.append(current)
            current = line[2:].strip()
        elif current and line.startswith("  "):
            current += " " + line.strip()
    if current:
        lines.append(current)
    return lines


def index_entries(path):
    """The entries of a resource index: dicts with name (the heading's
    backticked text), heading (the whole heading text) and fields
    ({field: value}, a wrapped value joined)."""
    out = []
    p = Path(path)
    if not p.exists():
        return out
    _, body = split_front(read(p))
    entry, field = None, None
    for line in body.split("\n"):
        m = re.match(r"^### `([^`]+)`(.*)$", line)
        if m:
            entry = {"name": m.group(1), "heading": (m.group(1) + m.group(2)).strip(), "fields": {}}
            out.append(entry)
            field = None
            continue
        if entry is None:
            continue
        m = re.match(r"^- \*\*([^*]+):\*\*\s*(.*)$", line)
        if m:
            field = m.group(1).strip()
            entry["fields"][field] = m.group(2).strip()
        elif field and line.startswith("  ") and line.strip():
            entry["fields"][field] += " " + line.strip()
        elif not line.strip():
            field = None
    return out


def thread_files(project):
    """The threads of a project as files: dicts with id, concerns,
    origin, status, text, path; the status of a file without a
    header is a problem."""
    out = []
    d = Path(project) / "threads"
    if not d.is_dir():
        return out
    for p in sorted(d.glob("THR.*.md")):
        front, body = front_of(p)
        text = re.sub(r"<!--.*?-->", "", body, flags=re.S).strip()
        out.append({"id": front_value(front, "id") or p.stem, "concerns": front_value(front, "concerns") or "intent",
                    "origin": front_value(front, "origin") or "the principal",
                    "status": front_value(front, "status") or "open", "text": text, "path": p})
    return out


def thread_blocks(path):
    """The threads of the one file of the shape before the migration
    (threads.md, 10-intent.threads.md): dicts with id, concerns, text;
    and the text after the last thread that is not a thread."""
    out, trailing, current = [], [], None
    p = Path(path)
    if not p.exists():
        return out, ""
    _, body = split_front(read(p))
    for line in body.split("\n"):
        m = THREAD_BLOCK_RE.match(line)
        if m:
            current = {"id": m.group(1), "concerns": (m.group(2) or "intent").strip(), "lines": [m.group(3)]}
            out.append(current)
            continue
        if current is None:
            continue
        if line.startswith("  ") or not line.strip():
            (trailing if trailing else current["lines"]).append(line[2:] if line.startswith("  ") else line)
        else:
            trailing.append(line)
    for b in out:
        b["text"] = "\n".join(b.pop("lines")).strip("\n")
    return out, "\n".join(trailing).strip()


def first_sentence(text):
    text = " ".join(text.split())
    m = re.match(r"^(.+?[.!?])(\s|$)", text)
    return m.group(1) if m else text


def last_dated_paragraph(text):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    for p in reversed(paras):
        if DATE_RE.search(p):
            return " ".join(p.split())
    return ""
