"""
forge_repos.py - what the forge-* git scripts share: the engine root,
the git check, the list of repositories to visit, running git, and
coloured output. Not a command.

The engine root is the parent of the directory this file lies in
(`scripts/`). A project is `projects/<slug>`; it is a repository when
`projects/<slug>/.git` exists (CLAUDE.md, Persistence). The scripts
carry no URL and no identity.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

ENGINE_ROOT = Path(__file__).resolve().parent.parent

_COLOURS = {"red": "31", "green": "32", "yellow": "33", "cyan": "36", "grey": "90"}


def say(text, colour=None):
    if colour and sys.stdout.isatty() and os.environ.get("NO_COLOR") is None:
        print(f"\033[{_COLOURS[colour]}m{text}\033[0m")
    else:
        print(text)


def fail(text):
    say(f"ERROR: {text}", "red")
    sys.exit(1)


def need_git():
    if shutil.which("git") is None:
        fail("git is not installed.")


def need_engine_repo():
    if not (ENGINE_ROOT / ".git").exists():
        fail("The engine is not a git repository (clone it, do not copy it).")


def git(args, cwd, check=False, capture=True):
    """Run git with `args` in `cwd`. Returns CompletedProcess; output is
    captured as text unless capture=False (then it streams to the
    terminal)."""
    r = subprocess.run(["git", *args], cwd=str(cwd), text=True, encoding="utf-8",
                       errors="replace",
                       stdout=subprocess.PIPE if capture else None,
                       stderr=subprocess.STDOUT if capture else None)
    if check and r.returncode != 0:
        fail(f"git {' '.join(args)} failed in {cwd}:\n{(r.stdout or '').strip()}")
    return r


def git_out(args, cwd):
    """Stdout of a git command, stripped; empty when it failed."""
    r = subprocess.run(["git", *args], cwd=str(cwd), text=True, encoding="utf-8",
                       errors="replace", stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    return r.stdout.strip() if r.returncode == 0 else ""


def project_path(slug):
    return ENGINE_ROOT / "projects" / slug


def repos_to_visit(slug, strict_message=None):
    """The repositories a bare or a slug-form command visits, as
    (name, path) pairs, the engine first. With a slug other than
    'forge' the one project, which must exist and be a repository
    (the message for the second case is strict_message, with {slug}
    inside); bare, the engine and every project that is a repository,
    the others reported and skipped."""
    repos = []
    if slug and slug != "forge":
        path = project_path(slug)
        if not path.exists():
            fail(f"Project '{slug}' not found ({path} does not exist).")
        if not (path / ".git").exists():
            fail((strict_message or "Project '{slug}' is not a repository.").format(slug=slug))
        repos.append((slug, path))
        return repos
    repos.append(("forge (engine)", ENGINE_ROOT))
    if not slug:
        projects = ENGINE_ROOT / "projects"
        if projects.is_dir():
            for d in sorted(p for p in projects.iterdir() if p.is_dir() and p.name != "forge"):
                if (d / ".git").exists():
                    repos.append((d.name, d))
                else:
                    say(f"{d.name:<20} not under git - skipped", "grey")
    return repos


def label(name, text):
    return f"{name:<20} {text}"
