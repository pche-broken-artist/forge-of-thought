#!/usr/bin/env python3
"""
forge-pull.py - pull the latest Forge from its remotes - the engine
(its upgrade channel) and every project that has an origin.

SYNOPSIS
    python scripts/forge-pull.py [slug | path]

WHAT IT DOES
    Fast-forward only. Without arguments pulls the engine, then every
    projects/<slug>/.git with an origin configured; with a slug pulls
    that one repository ('forge' means the engine and the forge's own
    project beside it, POS.1980). A repository with
    unsaved changes is not touched: reported and skipped (bare) or
    refused (slug), so a pull can never
    create a conflict in half-finished work. Projects without a
    repository or without an origin are reported and skipped. A
    repository whose history has diverged from its origin is refused
    and nothing is pulled; what to do then is /pull's to offer. The
    script never merges on its own (POS.1490 of the forge intent).

    It looks before it pulls, by the state forge_repos.remote_state
    gives, and names a failure by what it was. An origin that could not
    be reached is said as "unreachable", with git's own reason, and
    left: the others are pulled as if it were not there, and the run
    ends with an error naming every repository it could not reach. A
    branch the origin does not have ("no upstream") has nothing to
    pull and is no error. "Diverged" is said only of histories that
    diverged.

    After a pull it prints where the repository moved from and to
    (before: <hash> <subject>, after: <hash> <subject>) and the
    subjects of the commits between, so that the releases crossed
    ("release <version>") can be read off and their Action required
    lines looked up in RELEASE-NOTES.md.

WHAT IT NEEDS
    Python 3.8 or newer; git on PATH. `forge_repos.py` beside it.

EXAMPLES
    python scripts/forge-pull.py            # engine + every project with an origin
    python scripts/forge-pull.py forge      # the engine only (upgrade)
    python scripts/forge-pull.py platform-strategy   # one project: projects/platform-strategy
    python scripts/forge-pull.py /tmp/fixture-copy   # a project by its path
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import forge_repos as fr  # noqa: E402
import forge_tools as ft  # noqa: E402


def main(argv):
    ft.utf8_console()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1].strip())
    ap.add_argument("slug", nargs="?", help="one repository: a project's slug or the path of its directory ('forge' = the engine and the forge's own project beside it); bare = every one with an origin")
    a = ap.parse_args(argv)
    fr.need_git()
    fr.need_engine_repo()
    strict = bool(a.slug)
    unreached = []
    for name, path in fr.repos_to_visit(a.slug):
        origin = fr.git_out(["remote", "get-url", "origin"], path)
        if not origin:
            t = fr.label(name, "no origin - skipped")
            if strict:
                fr.fail(t)
            fr.say(t, "grey")
            continue
        if fr.git_out(["status", "--porcelain"], path):
            fr.say(fr.label(name, "has unsaved changes:"), "yellow")
            print(fr.git_out(["status", "--short"], path))
            if strict:
                fr.fail("Run scripts/forge-save.py first, then pull.")
            fr.say(fr.label(name, "skipped"), "yellow")
            continue
        # the look before the pull: a state is said only of an origin
        # that was reached, and a failure is named by what it was
        state = fr.remote_state(path)
        if state.startswith("unreachable"):
            fr.say(fr.label(name, state + " - nothing pulled"), "yellow")
            unreached.append(name)
            continue
        if state == "no upstream":
            fr.say(fr.label(name, "no upstream - the origin has no such branch; nothing to pull"), "grey")
            continue
        if state.startswith("diverged"):
            fr.fail(f"Pull failed in {name} - local and remote history diverged; nothing pulled. "
                    "Merge by hand, or scripts/forge-save.py rebases your commits onto the remote.")
        if not state.startswith("behind"):
            fr.say(fr.label(name, state), "green" if state == "up to date" else "grey")
            continue
        branch = fr.git_out(["rev-parse", "--abbrev-ref", "HEAD"], path)
        before = fr.git_out(["rev-parse", "--short", "HEAD"], path)
        if fr.git(["pull", "--ff-only", "origin", branch], path, capture=False).returncode != 0:
            fr.fail(f"Pull failed in {name}, though its origin was reached and the branch is {state}; "
                    "nothing pulled. git says why above.")
        after = fr.git_out(["rev-parse", "--short", "HEAD"], path)
        if after == before:
            fr.say(fr.label(name, "up to date"), "green")
            continue
        fr.say(fr.label(name, f"pulled {before} -> {after}"), "green")
        print("   before: " + fr.git_out(["log", "-1", "--format=%h %s", before], path))
        print("   after:  " + fr.git_out(["log", "-1", "--format=%h %s", after], path))
        between = fr.git_out(["log", "--reverse", "--format=  %s", f"{before}..{after}"], path)
        if between:
            print("   commits between:")
            for line in between.splitlines():
                print("  " + line)
    if unreached:
        fr.fail("The origin could not be reached for " + ", ".join(unreached) + "; nothing was pulled there. "
                "Mend git's way to the origin (network, proxy, access) and pull again.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
