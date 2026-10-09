#!/usr/bin/env python3
"""
forge-clone.py - bring an existing project into the Forge - clone its
repository into projects/.

SYNOPSIS
    python scripts/forge-clone.py <url>

WHAT IT DOES
    Clones the repository at the given URL into
    projects/<repository name> - the directory name falls out of the
    URL, and an existing directory is never overwritten. The commit
    identity is git's (CLAUDE.md, Persistence); the script sets none
    and carries no identity and no URL. Afterwards it reports facts:
    the last commit, the origin, the commit identity git resolves for
    the fresh clone, and whether the project carries a ledger with a
    kind: header (its absence: templates/ledger.md, header).

WHAT IT NEEDS
    Python 3.8 or newer; git on PATH. `forge_repos.py` beside it.

EXAMPLES
    python scripts/forge-clone.py https://example.com/team/my-idea.git
    python scripts/forge-clone.py git@example.com:team/my-idea.git
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import forge_repos as fr  # noqa: E402


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1].strip())
    ap.add_argument("url", help="the repository to clone")
    a = ap.parse_args(argv)
    fr.need_git()
    name = re.split(r"[/\\:]", a.url.rstrip("/\\"))[-1]
    name = re.sub(r"\.git$", "", name)
    if not name:
        fr.fail(f"Cannot derive a repository name from '{a.url}'.")
    target = fr.project_path(name)
    if target.exists():
        fr.fail(f"projects/{name} already exists - never overwritten. Rename or remove it first.")
    if fr.git(["clone", a.url, str(target)], fr.ENGINE_ROOT, capture=False).returncode != 0:
        fr.fail(f"Clone of {a.url} failed.")
    origin = fr.git_out(["remote", "get-url", "origin"], target)
    last = fr.git_out(["log", "-1", "--format=%h %ad %s", "--date=short"], target)
    print()
    fr.say(f"Cloned into projects/{name}", "green")
    print(f"  origin:      {origin}")
    print(f"  last commit: {last}")
    id_name = fr.git_out(["config", "user.name"], target)
    id_email = fr.git_out(["config", "user.email"], target)
    if id_name and id_email:
        print(f"  identity:    {id_name} <{id_email}> (from your git configuration)")
    else:
        print("  identity:    none resolved - forge-save will report it and skip the commit")
    ledger = target / "ledger.md"
    if ledger.exists():
        m = re.search(r"^kind:\s*(\S+)", ledger.read_text(encoding="utf-8", errors="replace"), re.M)
        print(f"  ledger:      present, kind: {m.group(1)}" if m else "  ledger:      present, no kind: header")
    else:
        print("  ledger:      none - not scaffolded by the forge (a fact, not a defect)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
