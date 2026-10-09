#!/usr/bin/env python3
"""
forge-branch.py - switch one Forge repository to a branch, creating it
if needed - or report which branch it is on.

SYNOPSIS
    python scripts/forge-branch.py <slug> [branch]

WHAT IT DOES
    Branches are voluntary in the Forge: whoever wants one gets it
    through this script and never types git; whoever does not works on
    main and never meets it. The script does two things and nothing
    else: with a branch name it switches the repository to that
    branch, creating it from the current state when it does not exist
    yet ('main' switches back); without a name it reports the current
    branch and lists the branches the repository has.

    The repository is named by its slug ('forge' means the engine);
    there is no bare form, since switching every repository at once
    is never what anyone wants. Unsaved changes stop the switch: save
    first (forge-save), then switch, so nothing is carried across or
    lost. Merging, deleting and pushing branches stay with git: a new
    branch reaches the remote by the first forge-save made on it, a
    merge into main is done by hand or by merge request, and a
    release is made from main only (/release:
    .claude/skills/release/SKILL.md).

WHAT IT NEEDS
    Python 3.8 or newer; git on PATH. `forge_repos.py` beside it.

EXAMPLES
    python scripts/forge-branch.py forge              # which branch is the engine on
    python scripts/forge-branch.py forge work-release # switch the engine to work-release, creating it
    python scripts/forge-branch.py platform-strategy main   # switch that project back to main
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import forge_repos as fr  # noqa: E402


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1].strip())
    ap.add_argument("slug", help="the repository ('forge' = the engine)")
    ap.add_argument("branch", nargs="?", help="the branch to switch to, created when missing")
    a = ap.parse_args(argv)
    fr.need_git()
    if a.slug == "forge":
        name, path = "forge (engine)", fr.ENGINE_ROOT
    else:
        name, path = a.slug, fr.project_path(a.slug)
        if not path.exists():
            fr.fail(f"Project '{a.slug}' not found ({path} does not exist).")
    if not (path / ".git").exists():
        fr.fail(f"'{a.slug}' is not a repository - nothing to switch.")

    current = fr.git_out(["rev-parse", "--abbrev-ref", "HEAD"], path)
    if not current:
        fr.fail(f"Cannot read the current branch of {name}.")

    if not a.branch:
        print(fr.label(name, f"on branch {current}"))
        branches = fr.git_out(["branch", "--format=%(refname:short)"], path).splitlines()
        if len(branches) > 1:
            fr.say(fr.label("", "branches: " + ", ".join(branches)), "grey")
        return 0

    if a.branch == current:
        fr.say(fr.label(name, f"already on {a.branch}"), "grey")
        return 0

    dirty = fr.git_out(["status", "--porcelain"], path).splitlines()
    if dirty:
        fr.fail(f"{name} has unsaved changes ({len(dirty)} file(s)). Save first (forge-save {a.slug}), then switch.")

    if fr.git(["rev-parse", "--verify", "--quiet", f"refs/heads/{a.branch}"], path).returncode == 0:
        if fr.git(["switch", a.branch], path).returncode != 0:
            fr.fail(f"Could not switch {name} to '{a.branch}'.")
        fr.say(fr.label(name, f"switched to {a.branch}"), "green")
    else:
        if fr.git(["switch", "-c", a.branch], path).returncode != 0:
            fr.fail(f"Could not create branch '{a.branch}' in {name}.")
        fr.say(fr.label(name, f"created {a.branch} from {current} and switched to it"), "green")
        fr.say(fr.label("", "the branch reaches the remote with the first forge-save made on it"), "grey")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
