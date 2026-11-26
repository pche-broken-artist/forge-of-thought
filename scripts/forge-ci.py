#!/usr/bin/env python3
"""
forge-ci.py - say how what GitHub ran on the head of a repository's
origin ended, waiting for it where asked.

SYNOPSIS
    python scripts/forge-ci.py [slug | path] [--wait] [--limit <minutes>]

WHAT IT DOES
    Read-only, no model: it changes nothing and fetches nothing. For
    the engine and every project that is a repository, or with a slug
    or a path for that one ('forge' means the engine and the forge's
    own project beside it, POS.1980), it takes the commit the origin's
    branch stands at as git last saw it - the upstream of the branch
    checked out, which a push or a fetch has just set - and reads
    through gh how what GitHub ran on it ended (forge_repos.github_ci,
    POS.2070): passing, failing, running or none. A failed job is
    named with its workflow and the step it stopped at, and below it
    stands what says why: what GitHub noted at the job, or the part of
    the job's log that says it, pytest's short summary where the log
    has one. Everything GitHub ran on the commit is read, a deployment
    as much as a test.

    With --wait it asks again every quarter of a minute until no job
    is running and then says how they ended: the reading after a push
    (/save, /release). A repository that carries workflows and shows
    no job yet is waited for as well, for the two minutes GitHub may
    take to start one. After --limit minutes (20 where not given) it
    says that jobs still run and ends; the map says the rest later
    (forge-status --remote).

    A state said is no failure of the report: the script ends green
    whatever the jobs did. Whatever keeps it from reading - no gh, no
    login, no network, an origin that is not on GitHub - is one line
    saying so; a repository without an origin, without an upstream or
    with nothing run on its head is said in a line and passed.

    Not forge-check.py, which runs the mechanical clauses of the
    forge's own checks on a project.

WHAT IT NEEDS
    Python 3.8 or newer; git on PATH; gh on PATH and logged in.
    `forge_repos.py` and `forge_tools.py` beside it.

EXAMPLES
    python scripts/forge-ci.py forge --wait    # after a push of the engine
    python scripts/forge-ci.py flow-ba         # one project, as it stands now
    python scripts/forge-ci.py                 # the engine and every project
"""

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import forge_repos as fr  # noqa: E402
import forge_tools as ft  # noqa: E402

PAUSE = 15       # seconds between two readings
STARTING = 120   # seconds a repository with workflows is given to show its first job

# The clock and the pause under their own names, so that a test puts
# its own in their place and no test waits.
sleep = time.sleep
clock = time.monotonic


def head(path):
    """The commit the origin's branch stands at as git last saw it, as
    (sha, None); or (None, why nothing is read)."""
    if not fr.git_out(["remote", "get-url", "origin"], path):
        return None, "no origin"
    sha = fr.git_out(["rev-parse", "@{u}"], path)
    return (sha, None) if sha else (None, "no upstream - nothing pushed whose runs could be read")


def has_workflows(path):
    """Whether the repository carries a workflow GitHub would run."""
    d = Path(path) / ".github" / "workflows"
    return d.is_dir() and any(f.suffix in (".yml", ".yaml") for f in d.iterdir())


def read(path, sha, wait, limit):
    """(word, lines) of what GitHub ran on `sha` (forge_repos.github_ci),
    read once; with `wait`, read again until no job runs or `limit`
    seconds have passed, a repository with workflows and no job yet
    counted as running for its first STARTING seconds."""
    started = clock()
    while True:
        word, lines = fr.github_ci(path, sha)
        waited = clock() - started
        starting = word == "none" and has_workflows(path) and waited < STARTING
        if not wait or not (word == "running" or starting):
            return word, lines
        if waited >= limit:
            return word, lines + ["jobs still run after the limit; the map says the rest (forge-status --remote)"]
        sleep(PAUSE)


def main(argv=None):
    ft.utf8_console()
    ap = argparse.ArgumentParser(prog="forge-ci.py",
                                 description=" ".join(__doc__.strip().split("\n\n")[0].split()))
    ap.add_argument("slug", nargs="?",
                    help="one repository: a project's slug or the path of its directory ('forge' = the engine "
                         "and the forge's own project beside it); bare = the engine and every project")
    ap.add_argument("--wait", action="store_true", help="ask again until no job is running")
    ap.add_argument("--limit", type=float, default=20, help="the minutes --wait waits at most (default 20)")
    a = ap.parse_args(argv)
    fr.need_git()
    fr.need_engine_repo()
    for name, path in fr.repos_to_visit(a.slug):
        sha, why = head(path)
        if not sha:
            fr.say(fr.label(name, why), "grey")
            continue
        word, lines = read(path, sha, a.wait, a.limit * 60)
        if word == "none":
            fr.say(fr.label(name, f"nothing ran on {sha[:7]}"), "grey")
            continue
        fr.say(fr.label(name, "ci " + lines[0]), {"passing": "green", "failing": "red"}.get(word, "yellow"))
        for line in lines[1:]:
            print(" " * 21 + line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
