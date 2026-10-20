#!/usr/bin/env python3
"""
forge-status.py - report the git state of the Forge: the engine and
every project.

SYNOPSIS
    python scripts/forge-status.py [--remote]

WHAT IT DOES
    Read-only, changes nothing. First the global configuration file
    git actually reads, which /setup needs to know, and the
    registration of the merge drivers in it: "ok", or the keys that
    are missing (`merge.ours.driver`, `rebase.backend`,
    `merge.renormalize`, as /setup registers them) and a registered
    forge-records driver whose script does not exist - an unregistered
    clone silently falls back to a conflict (SOL.0740 of the forge
    solution design). Then, for the
    engine and each projects/<slug>: unsaved changes (or "clean"), the
    branch it is on, the last commit, and the origin - or "no origin" /
    "not under git". Exists so that even reading git state goes through
    the scripts (CLAUDE.md, Persistence).

    With --remote it also fetches each repository's origin and reports
    the branch against it: "up to date", "behind N", "ahead N" or
    "diverged (ahead N, behind M)". The fetch changes nothing in the
    working tree; without the flag the script touches no network. The
    forge reports this state and offers; it never pulls or merges on
    its own (POS.1490 of the forge intent).

WHAT IT NEEDS
    Python 3.8 or newer; git on PATH. `forge_repos.py` beside it.

EXAMPLES
    python scripts/forge-status.py             # local state, no network
    python scripts/forge-status.py --remote    # the state against each origin as well
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import forge_repos as fr  # noqa: E402
import forge_tools as ft  # noqa: E402


def show_repo(name, path, remote=False):
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
    if remote and origin:
        state = fr.remote_state(path)
        colour = "green" if state == "up to date" else "yellow"
        fr.say("   remote:      " + state, colour)
    print()


def main(argv):
    ft.utf8_console()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1].strip())
    ap.add_argument("--remote", action="store_true",
                    help="fetch each origin and report the branch against it")
    a = ap.parse_args(argv)
    fr.need_git()
    fr.need_engine_repo()
    # The global configuration file git actually reads (CLAUDE.md,
    # Persistence); the first is the global file itself, the rest the
    # files it includes.
    files = fr.global_config_files()
    print("global git config: " + (", ".join(files) if files
                                   else "none yet - git creates ~/.gitconfig at its first write"))
    missing, broken = fr.registration_state()
    if not missing and not broken:
        fr.say("registration:      ok - the merge drivers and the settings they need", "green")
    if missing:
        fr.say("registration:      missing " + ", ".join(missing) + " - run /setup", "yellow")
    if broken:
        fr.say(f"registration:      the forge-records driver leads nowhere: {broken} - run /setup",
               "yellow")
    print()
    show_repo("forge (engine)", fr.ENGINE_ROOT, a.remote)
    projects = fr.ENGINE_ROOT / "projects"
    if projects.is_dir():
        for d in sorted(p for p in projects.iterdir() if p.is_dir() and p.name != "forge"):
            show_repo(d.name, d, a.remote)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
