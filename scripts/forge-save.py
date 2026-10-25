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
    remote changes by rebase and push. A clean repository that is
    ahead of its upstream - a rebase finished by hand, a push that
    failed - is pushed the same way, so that the push has a door
    (SOL.0780 of the forge solution design); a branch with no upstream
    yet reaches the remote with its first commit. A rebase that
    conflicts is left standing, the commit made and nothing lost: the
    script prints the files in conflict and the step that follows,
    the step of a conflict, as CLAUDE.md, Persistence, has it, then
    this script again, which pushes the clean repository that is ahead. A
    repository with a rebase or a merge already in progress is
    refused before anything is staged, so that conflict markers are
    never committed. Without an origin the commit is
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
import forge_tools as ft  # noqa: E402


def save_repo(name, path, message, tag):
    if not fr.git_out(["config", "user.email"], path):
        fr.say(fr.label(name, "no commit identity - git resolves none for this host: run /setup "
                              f"for the per-host identity, or set a local one: git -C '{path}' "
                              "config user.name/user.email"), "yellow")
        return
    if tag and fr.git(["rev-parse", "--verify", "--quiet", f"refs/tags/{tag}"], path).returncode == 0:
        fr.fail(f"Tag '{tag}' already exists in {name} - nothing was changed.")
    standing = fr.in_progress(path)
    if standing:
        files = fr.conflicted(path)
        shown = "\n".join(f"  {f}" for f in files) or "  (none left in conflict)"
        fr.fail(f"A {standing} is in progress in {name} - nothing was staged or committed. "
                f"Finish the step of a conflict first, then save again:\n{shown}\n"
                f"  settle each file, then: git -C '{path}' add <file>\n"
                f"  git -C '{path}' {standing} --continue   (or --abort to give it up)")

    fr.git(["add", "-A"], path, check=True)
    nothing_to_commit = fr.git(["diff", "--cached", "--quiet"], path).returncode == 0
    ahead = 0
    if nothing_to_commit and not tag:
        counts = fr.git_out(["rev-list", "--count", "@{u}..HEAD"], path)
        if not counts and fr.git_out(["remote", "get-url", "origin"], path):
            # no upstream yet (a branch made locally, a clone switched by
            # forge-branch): count against the remote's branch of the same
            # name after a fetch, or push a branch the remote does not have
            branch = fr.git_out(["rev-parse", "--abbrev-ref", "HEAD"], path)
            fr.git(["fetch", "origin", branch], path)
            if fr.git(["rev-parse", "--verify", "--quiet", f"refs/remotes/origin/{branch}"], path).returncode == 0:
                counts = fr.git_out(["rev-list", "--count", f"origin/{branch}..HEAD"], path)
            else:
                counts = fr.git_out(["rev-list", "--count", "HEAD"], path)
        ahead = int(counts) if counts else 0
        if not ahead:
            fr.say(fr.label(name, "nothing to save"), "grey")
            return

    msg = message
    if not msg and not nothing_to_commit:
        files = fr.git_out(["diff", "--cached", "--name-only"], path).splitlines()
        scope = "forge" if name.startswith("forge") else name
        shown = ", ".join(files[:5])
        more = f", +{len(files) - 5} more" if len(files) > 5 else ""
        msg = f"{scope}: {len(files)} file(s) - {shown}{more}"

    if nothing_to_commit and tag:
        fr.say(fr.label(name, "nothing to commit - tagging the current state"), "grey")
    elif nothing_to_commit:
        fr.say(fr.label(name, f"nothing to commit - {ahead} commit(s) ahead of origin, pushing"), "grey")
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
            slug = "forge" if name.startswith("forge") else name
            if fr.in_progress(path) != "rebase":
                fr.fail(f"The pull with rebase failed in {name} and left no rebase to finish; "
                        "the commit is made and nothing was lost. Check network / remote access and save again.")
            files = fr.conflicted(path)
            shown = "\n".join(f"  {f}" for f in files) or "  (none left in conflict)"
            fr.fail(f"Remote changes in {name} conflict with yours. The rebase stands where it stopped, "
                    "the commit is made and nothing was lost. The step of a conflict follows, one file at a time:\n"
                    f"{shown}\n"
                    f"  settle each file (both sides laid out, the principal deciding), then: git -C '{path}' add <file>\n"
                    f"  git -C '{path}' rebase --continue   (again after each conflict, until it ends; --abort gives it up)\n"
                    f"  python scripts/forge-save.py {slug}   (pushes the clean repository that is ahead)")
    if fr.git(["push", "-u", "origin", branch], path, capture=False).returncode != 0:
        fr.fail(f"Push failed in {name}. Check network / remote access and try again.")
    if tag and fr.git(["push", "origin", tag], path, capture=False).returncode != 0:
        fr.fail(f"Tag '{tag}' was created but could not be pushed from {name}. "
                f"Push it later: git -C '{path}' push origin {tag}")
    what = f"saved and pushed (with tag {tag}) to {origin}" if tag else f"saved and pushed to {origin}"
    fr.say(fr.label(name, what), "green")


def main(argv):
    ft.utf8_console()
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
