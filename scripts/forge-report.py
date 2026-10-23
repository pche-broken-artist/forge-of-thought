#!/usr/bin/env python3
"""
forge-report.py - the unique name of a reviewer's report: the time to
the minute and four hex characters of a content hash appended to the
name a report was filed under, in place.

SYNOPSIS
    python scripts/forge-report.py <path>

WHAT IT DOES
    No model involved, no git. The command that files a report
    (`/critique`, `/challenge`, `/check`) writes it into the project's
    `reviews/` or `challenges/` under its date, kind and name,
    `YYYY-MM-DD-<kind>-<name>.md`, and then calls this script with the
    file's path. The script reads the file, takes the local time to the
    minute and the first four hex characters of the SHA-256 of its
    bytes, renames the file in place to
    `YYYY-MM-DD-<kind>-<name>-HHMM-<hash>.md` and prints the new path,
    which the command then cites in the ledger. Nothing else is read or
    written. The rule is POS.1720 of the forge intent, realised by
    SOL.0810: two branches must not make the same name, and the first
    report of a day on two branches would; the names given before the
    rule stay as they are.

    It refuses, exit 1, with the reason printed: a path that is not a
    file; a name that already carries the tail `-HHMM-<hash>`; a name
    that ends in a run number (`-2.md`), since the tail alone tells two
    runs apart; a target
    name that exists. It changes no name but the one it was given.

EXAMPLES
    python scripts/forge-report.py projects/forge/reviews/2026-10-18-critique-clarity.md
    -> projects/forge/reviews/2026-10-18-critique-clarity-1732-8a3f.md
"""

import hashlib
import re
import sys
from datetime import datetime
from pathlib import Path

TAIL = re.compile(r"-\d{4}-[0-9a-f]{4}\.md$")
RUN = re.compile(r"-\d{1,2}\.md$")


def main(argv):
    if len(argv) != 2 or argv[1] in ("-h", "--help"):
        print(__doc__.strip())
        return 0 if len(argv) == 2 else 2
    path = Path(argv[1])
    if not path.is_file():
        print(f"forge-report: not a file: {path}")
        return 1
    if TAIL.search(path.name):
        print(f"forge-report: already named with time and hash: {path.name}")
        return 1
    if RUN.search(path.name):
        print(f"forge-report: a run number before the tail: {path.name};"
              " file it under its plain name, the time and the hash tell"
              " two runs of a day apart (POS.1720)")
        return 1
    if path.suffix != ".md":
        print(f"forge-report: not a Markdown file: {path.name}")
        return 1
    digest = hashlib.sha256(path.read_bytes()).hexdigest()[:4]
    stamp = datetime.now().strftime("%H%M")
    target = path.with_name(f"{path.stem}-{stamp}-{digest}.md")
    if target.exists():
        print(f"forge-report: target exists: {target}")
        return 1
    path.rename(target)
    print(target.as_posix())
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
