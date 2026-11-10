#!/usr/bin/env python3
"""
forge-record.py - append one record to a history companion, or one
decision to a project's decisions.md, at the end of the file and
nowhere else.

SYNOPSIS
    python scripts/forge-record.py history <project> <document>
        --subject <subject> --kind <kind> [--reason <text>]
        [--action <text>] [--was <text>] [--instance <path>] [--dry-run]
    python scripts/forge-record.py decision <project>
        --title <line> --decision <text> --reason <text>
        [--verdict "<ID> rejected"]... [--instance <path>] [--dry-run]

WHAT IT DOES
    No model, no git. The histories and the decisions are append-only
    (CLAUDE.md, Document kinds; templates/history.md,
    templates/decisions.md): a record is one line, or a decision one
    block, added after the last line of the file and nothing else
    changed. This script is the way such a write is made (THR.0880),
    so that the end of the file is found by a program and never by
    an editor that can place a line anywhere.

    The project is a slug or the path of its directory
    (forge_repos.project_path). `history` takes the versioned
    document by its path inside the project, `10-intent.md`,
    `recipes/readme.md`, `work/x.spec.md`, and writes to its companion
    beside it, `<file>.history.md`, which must exist. The record is

        - <date> | <version> | <author> | <subject> | <kind> | <reason> | Action: <action> | Was: <was>

    in the shape templates/history.md owns: the date today; the
    version the document's header carries now, since a record of state
    carries the current version and the version is raised in the
    header first (POS.1630); the author the handle of the instance
    file. `decision` writes the next DEC of the project's sequence,
    ten above the highest, in the shape of templates/decisions.md,
    the Decision and the Reason wrapped at 72 columns.

    The author is read from the instance file, `**Author:**` in
    CLAUDE.local.md at the engine root, or the file `--instance`
    names; where it gives none the script refuses and names /setup:
    the handle is never guessed (POS.1050).

    It refuses, exit 1, the reason printed and the file untouched: a
    project, a document or a companion that does not exist; a kind
    outside created | changed | closed | removed | approved; a record
    other than `created` without a reason; a line break in any field;
    ` | `, `Action: ` or `Was: ` inside the subject, the kind, the
    reason or the action, which would break the record's fields
    (`Was` comes last and may carry them); paragraphs of `Was` are
    divided by `<br>`. The line endings of the file are kept, CRLF or
    LF, and a file that does not end in a line break gets one first.
    After the write the script reads the last record back with
    forge_docs.records and refuses if it is not the one it wrote.

    --dry-run prints what would be written and writes nothing: the
    reflection before a write shows the records as this script will
    write them.

EXAMPLES
    python scripts/forge-record.py history forge 10-intent.md --subject THR.0880 --kind created
    python scripts/forge-record.py history forge 10-intent.md --subject POS.1400 --kind changed --reason "the principal's word" --was "the old wording"
    python scripts/forge-record.py decision forge --title "A decision in one line" --decision "What was decided." --reason "Why." --verdict "FND.4680 rejected"
"""

import argparse
import datetime
import re
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import forge_docs as fd  # noqa: E402
import forge_repos as fr  # noqa: E402
import forge_tools as ft  # noqa: E402

KINDS = ("created", "changed", "closed", "removed", "approved")
BREAKERS = (" | ", "Action: ", "Was: ")
DEC_RE = re.compile(r"^## DEC\.(\d{4,5})\b", re.M)


class Refusal(Exception):
    pass


def companion(document):
    """`10-intent.md` -> `10-intent.history.md`."""
    return document.with_name(document.name[:-len(".md")] + ".history.md")


def eol_of(data):
    return b"\r\n" if b"\r\n" in data else b"\n"


def append(path, text, dry_run):
    """Append `text` (lines joined by \\n) after the last line of the file,
    in the file's own line endings; returns the bytes written."""
    data = path.read_bytes()
    eol = eol_of(data)
    add = b""
    if data and not data.endswith(b"\n"):
        add += eol
    add += text.encode("utf-8").replace(b"\n", eol) + eol
    if not dry_run:
        with open(path, "ab") as f:
            f.write(add)
    return add


def author_of(instance):
    author = fd.instance_author(instance)
    if not author:
        raise Refusal(f"no Author in {instance} - run /setup, which adds the line;"
                      " the handle is never guessed (POS.1050)")
    return author


def check_field(name, value, breakers=BREAKERS):
    if value is None:
        return
    if "\n" in value or "\r" in value:
        raise Refusal(f"a line break in {name}: a record is one line"
                      " (paragraphs of Was divided by <br>)")
    for b in breakers:
        if b in value:
            raise Refusal(f"{b.strip() or '|'!r} inside {name} would break the fields of the record")


def history(args, root):
    document = root / args.document
    if not document.is_file():
        raise Refusal(f"no document {document}")
    target = companion(document)
    if not target.is_file():
        raise Refusal(f"no history companion {target}: it is born with its document"
                      " from templates/history.md")
    front, _ = fd.split_front(fd.read(document))
    version = fd.front_value(front, "version")
    if not version:
        raise Refusal(f"no version in the header of {document}")
    if args.kind not in KINDS:
        raise Refusal(f"kind {args.kind!r}: one of {' | '.join(KINDS)}")
    if not args.subject.strip():
        raise Refusal("an empty subject")
    if args.kind != "created" and not (args.reason or "").strip():
        raise Refusal(f"a {args.kind} record carries its reason")
    for name in ("subject", "reason", "action"):
        check_field(name, getattr(args, name))
    check_field("was", args.was, breakers=())
    author = author_of(args.instance)
    parts = [datetime.date.today().isoformat(), version, author, args.subject.strip(), args.kind]
    if args.reason:
        parts.append(args.reason.strip())
    if args.action:
        parts.append("Action: " + args.action.strip())
    if args.was:
        parts.append("Was: " + args.was.strip())
    line = "- " + " | ".join(parts)
    append(target, line, args.dry_run)
    if not args.dry_run:
        last = fd.records(target)[-1:]
        if not last or last[0]["subject"] != args.subject.strip() or \
                last[0]["line"] != len(target.read_text(encoding="utf-8").rstrip("\r\n").split("\n")):
            raise Refusal(f"the record read back from {target} is not the one written; look at the file")
    return target, line


def wrap(label, text):
    return textwrap.fill(f"- **{label}:** {' '.join(text.split())}", width=72,
                         subsequent_indent="  ", break_long_words=False, break_on_hyphens=False)


def decision(args, root):
    target = root / "decisions.md"
    if not target.is_file():
        raise Refusal(f"no {target}: it is born with the project from templates/decisions.md")
    for name in ("title", "decision", "reason"):
        value = getattr(args, name)
        if not (value or "").strip():
            raise Refusal(f"an empty {name}")
    check_field("title", args.title, breakers=())
    for v in args.verdict:
        check_field("verdict", v, breakers=())
    author_of(args.instance)  # a decision is the principal's: the instance must name him
    numbers = [int(n) for n in DEC_RE.findall(fd.read(target))]
    number = (max(numbers) // 10 + 1) * 10 if numbers else 10
    dec_id = f"DEC.{number:04d}"
    lines = ["", f"## {dec_id} — {args.title.strip()}",
             wrap("Decision", args.decision), wrap("Reason", args.reason)]
    lines += [f"- **Verdict:** {v.strip()}" for v in args.verdict]
    lines.append(f"- **Date:** {datetime.date.today().isoformat()}")
    text = "\n".join(lines)
    append(target, text, args.dry_run)
    return target, text


def main(argv=None):
    ft.utf8_console()
    p = argparse.ArgumentParser(prog="forge-record.py", description=__doc__.strip().split("\n")[0])
    sub = p.add_subparsers(dest="what", required=True)
    h = sub.add_parser("history", help="one record at the end of a history companion")
    h.add_argument("project")
    h.add_argument("document")
    h.add_argument("--subject", required=True)
    h.add_argument("--kind", required=True)
    h.add_argument("--reason")
    h.add_argument("--action")
    h.add_argument("--was")
    d = sub.add_parser("decision", help="one DEC at the end of decisions.md")
    d.add_argument("project")
    d.add_argument("--title", required=True)
    d.add_argument("--decision", required=True)
    d.add_argument("--reason", required=True)
    d.add_argument("--verdict", action="append", default=[])
    for s in (h, d):
        s.add_argument("--instance", type=Path, default=fr.ENGINE_ROOT / "CLAUDE.local.md",
                       help="the instance file the author is read from (default: CLAUDE.local.md at the engine root)")
        s.add_argument("--dry-run", action="store_true", help="print what would be written, write nothing")
    args = p.parse_args(argv)
    root = fr.project_path(args.project)
    try:
        if not root.is_dir():
            raise Refusal(f"no project {fr.project_label(args.project)}")
        target, text = (history if args.what == "history" else decision)(args, root)
    except Refusal as e:
        print(f"forge-record: {e}")
        return 1
    print(("would append to " if args.dry_run else "appended to ") + str(target) + ":")
    print(text.strip("\n"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
