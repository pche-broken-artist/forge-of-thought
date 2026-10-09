#!/usr/bin/env python3
"""
forge-save.py - save the Forge to git: commit and push - the engine
and every project that is a repository of its own.

SYNOPSIS
    python scripts/forge-save.py [slug] [-m MESSAGE] [--tag NAME]

WHAT IT DOES
    The engine (this repository) and the projects under projects/ are
    separate git repositories; the engine does not track projects/
    (only its own project, projects/forge). Without arguments the
    script visits the engine and every projects/<slug>/.git and gives
    each one with changes its own commit. With a slug it saves that one
    repository only ('forge' means the engine). A project directory
    without a repository is skipped with a note (bare) or refused
    (slug).

    Per repository: stage everything, commit (message from -m, or a
    generated one), then - when an origin is configured - integrate
    remote changes by rebase and push. Without an origin the commit is
    kept locally and reported. With --tag <name> (one repository, so a
    slug is required) the commit is tagged and the tag pushed with it;
    when there is nothing to commit, the current HEAD is tagged, so a
    tag can mark a state before a large change. An existing tag is
    refused. The script never sets an identity, a remote or
    initialises a repository (CLAUDE.md, Persistence). It never uses
    git add -f and never git clean.

WHAT IT NEEDS
    Python 3.8 or newer; git on PATH. `forge_repos.py` beside it.

EXAMPLES
    python scripts/forge-save.py                   # every repository with changes
    python scripts/forge-save.py platform-strategy   # one thought project: projects/platform-strategy
    python scripts/forge-save.py forge             # only the engine
    python scripts/forge-save.py -m "my message"   # custom commit message
    python scripts/forge-save.py forge --tag v3.33 # save the engine and tag the commit
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import forge_repos as fr  # noqa: E402


def save_repo(name, path, message, tag):
    if not fr.git_out(["config", "user.email"], path):
        fr.say(fr.label(name, "no commit identity - git resolves none for this host: run /setup "
                              f"for the per-host identity, or set a local one: git -C '{path}' "
                              "config user.name/user.email"), "yellow")
        return
    if tag and fr.git(["rev-parse", "--verify", "--quiet", f"refs/tags/{tag}"], path).returncode == 0:
        fr.fail(f"Tag '{tag}' already exists in {name} - nothing was changed.")

    fr.git(["add", "-A"], path, check=True)
    nothing_to_commit = fr.git(["diff", "--cached", "--quiet"], path).returncode == 0
    if nothing_to_commit and not tag:
        fr.say(fr.label(name, "nothing to save"), "grey")
        return

    msg = message
    if not msg and not nothing_to_commit:
        files = fr.git_out(["diff", "--cached", "--name-only"], path).splitlines()
        scope = "forge" if name.startswith("forge") else name
        shown = ", ".join(files[:5])
        more = f", +{len(files) - 5} more" if len(files) > 5 else ""
        msg = f"{scope}: {len(files)} file(s) - {shown}{more}"

    if nothing_to_commit:
        fr.say(fr.label(name, "nothing to commit - tagging the current state"), "grey")
    else:
        r = fr.git(["commit", "-m", msg], path)
        if r.returncode != 0:
            fr.fail(f"Commit failed in {name}.\n{r.stdout.strip()}")
        print(fr.label(name, f"committed: {msg}"))
        print(fr.git_out(["diff-tree", "--no-commit-id", "--stat", "-r", "HEAD"], path))

    if tag:
        if fr.git(["tag", tag], path).returncode != 0:
            fr.fail(f"Tag '{tag}' could not be created in {name}.")
        print(fr.label(name, f"tagged: {tag}"))

    origin = fr.git_out(["remote", "get-url", "origin"], path)
    if not origin:
        kept = "commit and tag kept locally" if tag else "commit kept locally"
        fr.say(fr.label(name, f"not pushed - no origin configured ({kept})"), "yellow")
        return

    branch = fr.git_out(["rev-parse", "--abbrev-ref", "HEAD"], path)
    if fr.git(["ls-remote", "--exit-code", "--heads", "origin", branch], path).returncode == 0:
        if fr.git(["pull", "--rebase", "origin", branch], path, capture=False).returncode != 0:
            fr.git(["rebase", "--abort"], path)
            fr.fail(f"Remote changes in {name} conflict with yours. Nothing was lost - "
                    "ask Claude for help before doing anything else.")
    if fr.git(["push", "-u", "origin", branch], path, capture=False).returncode != 0:
        fr.fail(f"Push failed in {name}. Check network / remote access and try again.")
    if tag and fr.git(["push", "origin", tag], path, capture=False).returncode != 0:
        fr.fail(f"Tag '{tag}' was created but could not be pushed from {name}. "
                f"Push it later: git -C '{path}' push origin {tag}")
    what = f"saved and pushed (with tag {tag}) to {origin}" if tag else f"saved and pushed to {origin}"
    fr.say(fr.label(name, what), "green")


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1].strip())
    ap.add_argument("slug", nargs="?", help="one repository ('forge' = the engine); bare = every one with changes")
    ap.add_argument("-m", "--message", help="commit message (default: generated from the files)")
    ap.add_argument("--tag", help="tag the commit (needs a slug)")
    a = ap.parse_args(argv)
    fr.need_git()
    fr.need_engine_repo()
    if a.tag and not a.slug:
        fr.fail("--tag needs one repository: name the slug ('forge' for the engine).")
    repos = fr.repos_to_visit(
        a.slug, "Project '{slug}' is not a repository - run 'git -C projects/{slug} init -b main' once, then save.")
    for name, path in repos:
        save_repo(name, path, a.message, a.tag)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
