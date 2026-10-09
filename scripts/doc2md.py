#!/usr/bin/env python3
"""
doc2md.py - convert documents (Word / PowerPoint / PDF / Excel) to
Markdown using markitdown.

SYNOPSIS
    python scripts/doc2md.py <input> [<input> ...] [-o <dir>] [--suffix <text>]
        [--recurse] [--force] [--as-list] [--markitdown-path <exe>]
        [--dry-run] [--list-tools]

WHAT IT DOES
    Accepts three input notations, which can be mixed and repeated:
      1) a single file name   doc2md.py report.docx
      2) glob / star notation doc2md.py "*.pdf" "docs/**/*.pptx"
      3) a list file          doc2md.py files.txt
         (plain text, one path or glob per line; '#' or ';' starts a
          comment; relative paths are resolved against the list
          file's own directory)
      +) a directory          doc2md.py docs --recurse

    Each document becomes <name>.md next to it, or in the directory
    -o names; an existing .md is skipped unless --force; --suffix
    inserts text before the .md extension (--suffix .text gives
    report.text.md); a name collision within one run gets _1, _2 ...
    --dry-run lists what would be converted and writes nothing;
    --list-tools checks that markitdown is reachable and exits.

    Handled extensions: .pdf .docx .docm .pptx .pptm .xlsx .xlsm .xls
    .epub .html .htm .csv .json .xml .msg. Legacy binary .doc .ppt
    .rtf .odt .odp .ods are reported as unsupported - resave them as
    .docx/.pptx/.xlsx first.

WHAT IT NEEDS
    Python 3.8 or newer. Conversion is done exclusively by markitdown
    (MIT, Microsoft): https://github.com/microsoft/markitdown, resolved
    from PATH or named by --markitdown-path. This script never installs
    anything. Install the engine yourself with:
        pip install "markitdown[docx,pptx,pdf,xlsx,xls]"

EXAMPLES
    python scripts/doc2md.py presentation.pptx
    python scripts/doc2md.py report.pdf --suffix .text
    python scripts/doc2md.py "*.pdf" "*.docx" -o md
    python scripts/doc2md.py files.txt -o md --force
    python scripts/doc2md.py docs --recurse --dry-run
"""

import argparse
import glob
import shutil
import subprocess
import sys
from pathlib import Path

DOC_EXT = {".pdf", ".docx", ".docm", ".pptx", ".pptm", ".xlsx", ".xlsm", ".xls",
           ".epub", ".html", ".htm", ".csv", ".json", ".xml", ".msg"}
LIST_EXT = {".txt", ".lst", ".list", ".files", ".filelist"}
UNSUPPORTED_EXT = {".doc", ".ppt", ".odt", ".odp", ".ods", ".rtf", ".pages", ".key"}


def warn(text):
    print(f"WARNING: {text}", file=sys.stderr)


def resolve_inputs(token, base, recurse, as_list, depth=0):
    """Expand one input token into document paths."""
    tok = token.strip().strip("\"'")
    if not tok:
        return []
    if depth > 5:
        warn(f"List nesting too deep at '{tok}' - skipped.")
        return []
    candidate = Path(tok) if Path(tok).is_absolute() else base / tok
    if "*" in tok or "?" in tok:
        deep = recurse or "**" in tok
        hits = [Path(h) for h in glob.glob(str(candidate), recursive=True)]
        if deep and "**" not in tok:
            hits += [Path(h) for h in glob.glob(str(candidate.parent / "**" / candidate.name), recursive=True)]
        hits = [h for h in dict.fromkeys(hits) if h.is_file() and h.suffix.lower() in DOC_EXT]
        if not hits:
            warn(f"Pattern '{tok}' matched nothing.")
        return hits
    if not candidate.exists():
        warn(f"Not found: '{tok}'")
        return []
    if candidate.is_dir():
        it = candidate.rglob("*") if recurse else candidate.glob("*")
        return [p for p in it if p.is_file() and p.suffix.lower() in DOC_EXT]
    ext = candidate.suffix.lower()
    if as_list or ext in LIST_EXT:
        out = []
        for line in candidate.read_text(encoding="utf-8", errors="replace").splitlines():
            l = line.strip()
            if not l or l.startswith("#") or l.startswith(";"):
                continue
            out += resolve_inputs(l, candidate.parent, recurse, False, depth + 1)
        return out
    if ext in DOC_EXT:
        return [candidate]
    if ext in UNSUPPORTED_EXT:
        warn(f"markitdown cannot read legacy format '{ext}' - resave as .docx/.pptx/.xlsx: {candidate}")
    else:
        warn(f"Unsupported extension '{ext}': {candidate}")
    return []


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1].strip())
    ap.add_argument("inputs", nargs="*", help="files, globs, list files or directories")
    ap.add_argument("-o", "--out-dir", help="where to write the .md files (default: next to each source)")
    ap.add_argument("--suffix", default="", help="text inserted before the .md extension")
    ap.add_argument("--markitdown-path", help="explicit path to the markitdown executable")
    ap.add_argument("--recurse", action="store_true", help="descend into directories and globs without **")
    ap.add_argument("--force", action="store_true", help="overwrite existing .md files")
    ap.add_argument("--as-list", action="store_true", help="treat every input as a list file")
    ap.add_argument("--dry-run", action="store_true", help="show what would be converted, write nothing")
    ap.add_argument("--list-tools", action="store_true", help="check that markitdown is available and exit")
    a = ap.parse_args(argv)

    exe = a.markitdown_path or shutil.which("markitdown")
    if a.markitdown_path and not Path(a.markitdown_path).exists():
        print(f"ERROR: markitdown not found at '{a.markitdown_path}'.", file=sys.stderr)
        return 1
    if a.list_tools:
        if exe:
            print(f"markitdown  OK   {exe}")
        else:
            print("markitdown  --   not found on PATH\n\nInstall it with:\n"
                  '  pip install "markitdown[docx,pptx,pdf,xlsx,xls]"\n'
                  "Then reopen the shell, or pass --markitdown-path <exe>.")
        return 0
    if not a.inputs:
        ap.print_help()
        return 0
    if not exe and not a.dry_run:
        print('ERROR: markitdown not found. Install it with: pip install "markitdown[docx,pptx,pdf,xlsx,xls]" '
              "(or pass --markitdown-path).", file=sys.stderr)
        return 1

    base = Path.cwd()
    files = []
    for t in a.inputs:
        files += resolve_inputs(t, base, a.recurse, a.as_list)
    files = sorted({f.resolve() for f in files})
    if not files:
        warn("No supported documents found.")
        return 0

    out_dir = Path(a.out_dir).resolve() if a.out_dir else None
    if out_dir and not out_dir.exists():
        if a.dry_run:
            print(f"Dry run: would create output directory '{out_dir}'.")
        else:
            out_dir.mkdir(parents=True)

    written = set()
    ok = skipped = failed = 0
    for i, f in enumerate(files, 1):
        d = out_dir or f.parent
        target = d / f"{f.stem}{a.suffix}.md"
        if str(target).lower() in written:
            n = 1
            while str(target).lower() in written:
                target = d / f"{f.stem}{a.suffix}_{n}.md"
                n += 1
        elif target.exists() and not a.force:
            print(f"SKIP  {f.name}  -> already exists (use --force)")
            skipped += 1
            continue
        if a.dry_run:
            print(f"[{i}/{len(files)}] would convert {f} -> {target}")
            continue
        r = subprocess.run([exe, str(f), "-o", str(target)], text=True, encoding="utf-8",
                           errors="replace", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if r.returncode != 0 or not target.exists():
            failed += 1
            msg = " ".join((r.stdout or "").split())
            print(f"FAIL  {f.name:<45} -> markitdown exited with code {r.returncode}"
                  + (f": {msg}" if msg else "") if r.returncode else
                  f"FAIL  {f.name:<45} -> markitdown produced no output file.")
            continue
        written.add(str(target).lower())
        ok += 1
        print(f"OK    {f.name:<45} -> {target.name} ({round(target.stat().st_size / 1024, 1)} kB)")

    print()
    print(f"Done: {ok} converted, {skipped} skipped, {failed} failed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
