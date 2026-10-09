#!/usr/bin/env python3
"""
forge-pull.py - pull the latest Forge from its remotes - the engine
(its upgrade channel) and every project that has an origin.

SYNOPSIS
    python scripts/forge-pull.py [slug]

WHAT IT DOES
    Fast-forward only. Without arguments pulls the engine, then every
    projects/<slug>/.git with an origin configured; with a slug pulls
    that one repository ('forge' means the engine). A repository with
    unsaved changes is not touched: reported and skipped (bare) or
    refused (slug) - run forge-save.py first, so a pull can never
    create a conflict in half-finished work. Projects without a
    repository or without an origin are reported and skipped.

WHAT IT NEEDS
    Python 3.8 or newer; git on PATH. `forge_repos.py` beside it.

EXAMPLES
    python scripts/forge-pull.py            # engine + every project with an origin
    python scripts/forge-pull.py forge      # the engine only (upgrade)
    python scripts/forge-pull.py platform-strategy   # one project: projects/platform-strategy
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import forge_repos as fr  # noqa: E402


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1].strip())
    ap.add_argument("slug", nargs="?", help="one repository ('forge' = the engine); bare = every one with an origin")
    a = ap.parse_args(argv)
    fr.need_git()
    fr.need_engine_repo()
    strict = bool(a.slug)
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
        branch = fr.git_out(["rev-parse", "--abbrev-ref", "HEAD"], path)
        if fr.git(["pull", "--ff-only", "origin", branch], path, capture=False).returncode != 0:
            fr.fail(f"Pull failed in {name} - local and remote history diverged. "
                    "Run scripts/forge-save.py (it reconciles both), or ask Claude.")
        fr.say(fr.label(name, "up to date"), "green")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
