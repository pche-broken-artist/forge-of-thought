#!/usr/bin/env python3
"""
forge-status.py - report the git state of the Forge: the engine and
every project.

SYNOPSIS
    python scripts/forge-status.py

WHAT IT DOES
    Read-only, changes nothing. First the global configuration file
    git actually reads, which /setup needs to know. Then, for the
    engine and each projects/<slug>: unsaved changes (or "clean"), the
    branch it is on, the last commit, and the origin - or "no origin" /
    "not under git". Exists so that even reading git state goes through
    the scripts (CLAUDE.md, Persistence).

WHAT IT NEEDS
    Python 3.8 or newer; git on PATH. `forge_repos.py` beside it.

EXAMPLES
    python scripts/forge-status.py
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import forge_repos as fr  # noqa: E402


def show_repo(name, path):
    fr.say(f"== {name}", "cyan")
    if not (path / ".git").exists():
        print("   not under git")
        print()
        return
    changes = fr.git_out(["status", "--short"], path)
    if changes:
        for line in changes.splitlines():
            print(f"   {line}")
    else:
        fr.say("   clean - nothing to save", "green")
    branch = fr.git_out(["rev-parse", "--abbrev-ref", "HEAD"], path)
    print("   branch:      " + (branch or "none yet"))
    last = fr.git_out(["log", "-1", "--format=%h %s"], path)
    print("   last commit: " + (last or "none yet"))
    origin = fr.git_out(["remote", "get-url", "origin"], path)
    print("   origin:      " + (origin or "no origin"))
    print()


def main():
    fr.need_git()
    fr.need_engine_repo()
    # The global configuration file git actually reads, named here so
    # that /setup never has to ask git directly (CLAUDE.md,
    # Persistence). With includes in play git names every file it read;
    # the first is the global file itself.
    listing = fr.git_out(["config", "--global", "--list", "--show-origin"], fr.ENGINE_ROOT)
    files = []
    for line in listing.splitlines():
        m = re.match(r"^file:(.+?)\t", line)
        if m and m.group(1) not in files:
            files.append(m.group(1))
    print("global git config: " + (", ".join(files) if files
                                   else "none yet - git creates ~/.gitconfig at its first write"))
    print()
    show_repo("forge (engine)", fr.ENGINE_ROOT)
    projects = fr.ENGINE_ROOT / "projects"
    if projects.is_dir():
        for d in sorted(p for p in projects.iterdir() if p.is_dir() and p.name != "forge"):
            show_repo(d.name, d)
    return 0


if __name__ == "__main__":
    sys.exit(main())
