"""
forge_repos.py - what the forge-* git scripts share: the engine root,
the git check, the list of repositories to visit, running git, the
state of a repository against its origin (`remote_state`: up to date,
behind, ahead, diverged, no origin; POS.1490), the files of the
global git configuration as git reads them (`global_config_files`),
the registration of the merge drivers on the machine
(`registration_state`; SOL.0740) and coloured output. Not a command.

The engine root is the parent of the directory this file lies in
(`scripts/`). A project is `projects/<slug>`; it is a repository of
its own when git names its directory as the top of a repository
(`own_repo`), never by a `.git` looked for; anything else is a project
outside git, on which the forge runs no git (CLAUDE.md, Persistence;
POS.0550). The scripts carry no URL and no identity.
"""

import os
import re
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
    if not own_repo(ENGINE_ROOT):
        fail("The engine is not the top of a git repository (clone it, do not copy it).")


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


def own_repo(path):
    """True when `path` is itself the top of a git repository: git's
    `rev-parse --show-toplevel` run inside it names `path`, resolved
    paths compared, a worktree and a linked directory alike. A
    directory inside another repository, the engine's included, or
    under no git at all is not a repository of its own, and the forge
    runs no git on it (CLAUDE.md, Persistence; POS.0550, SOL.0510)."""
    top = git_out(["rev-parse", "--show-toplevel"], path)
    return bool(top) and Path(top).resolve() == Path(path).resolve()


def git_out(args, cwd):
    """Stdout of a git command, stripped; empty when it failed."""
    r = subprocess.run(["git", *args], cwd=str(cwd), text=True, encoding="utf-8",
                       errors="replace", stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    return r.stdout.strip() if r.returncode == 0 else ""


def in_progress(path):
    """'rebase' or 'merge' when `path` has one standing, else None: a
    conflict forge-save left for the step of a conflict (the cutover
    plan, R6.02), or one the user began by hand. Read from git's own
    marks (rebase-merge, rebase-apply, MERGE_HEAD), nothing of the
    forge's."""
    for mark in ("rebase-merge", "rebase-apply"):
        p = git_out(["rev-parse", "--git-path", mark], path)
        if p and (Path(path) / p).exists():
            return "rebase"
    if git(["rev-parse", "--verify", "--quiet", "MERGE_HEAD"], path).returncode == 0:
        return "merge"
    return None


def conflicted(path):
    """The files in conflict, as git lists them."""
    out = git_out(["diff", "--name-only", "--diff-filter=U"], path)
    return out.splitlines() if out else []


def remote_state(path):
    """The branch of `path` against its origin after a fetch: one of
    'up to date', 'behind N', 'ahead N', 'diverged (ahead N, behind M)',
    'no origin', 'no upstream'. The fetch changes nothing in the
    working tree. Shared by forge-status (--remote) and forge-pull."""
    if not git_out(["remote", "get-url", "origin"], path):
        return "no origin"
    branch = git_out(["rev-parse", "--abbrev-ref", "HEAD"], path)
    if not branch or branch == "HEAD":
        return "no upstream"
    git(["fetch", "origin", branch], path)
    counts = git_out(["rev-list", "--left-right", "--count", f"HEAD...origin/{branch}"], path)
    if not counts:
        return "no upstream"
    ahead, behind = (int(x) for x in counts.split())
    if ahead and behind:
        return f"diverged (ahead {ahead}, behind {behind})"
    if behind:
        return f"behind {behind}"
    if ahead:
        return f"ahead {ahead}"
    return "up to date"


# The registration /setup makes in the global git configuration, once
# per machine (SOL.0740): the keys with the values they must carry.
# `rerere.enabled` is a convenience and is never reported missing. The
# driver's own key, `merge.forge-records.driver`, is checked only when
# it is set, for a path that leads nowhere; it arrives with the driver.
REGISTRATION = (
    ("merge.ours.driver", "true"),
    ("rebase.backend", "merge"),
    ("merge.renormalize", "true"),
)
DRIVER_KEY = "merge.forge-records.driver"


def _unquote(path):
    """A path as git prints it in --show-origin: C-quoted when it holds
    a backslash, a quote or a byte beyond ASCII ("C:\\\\Users\\\\..."),
    plain otherwise."""
    if not (len(path) >= 2 and path[0] == path[-1] == '"'):
        return path
    body, out, i = path[1:-1], bytearray(), 0
    while i < len(body):
        if body[i] == "\\" and i + 1 < len(body):
            if re.match(r"[0-7]{3}", body[i + 1:i + 4]):
                out.append(int(body[i + 1:i + 4], 8))
                i += 4
                continue
            out += {"n": b"\n", "t": b"\t"}.get(body[i + 1], body[i + 1].encode())
            i += 2
            continue
        out += body[i].encode()
        i += 1
    return out.decode("utf-8", "replace")


def global_config_files():
    """The files of the global git configuration as git itself reads
    them, the global file first and then every file it includes; empty
    when there is none yet. The forge never names the file by a path of
    its own: git decides where it lies (HOME, HOMEDRIVE and HOMEPATH,
    GIT_CONFIG_GLOBAL), and it may differ from place to place."""
    listing = git_out(["config", "--global", "--list", "--show-origin"], ENGINE_ROOT)
    files = []
    for line in listing.splitlines():
        m = re.match(r"^file:(.+?)\t", line)
        if m:
            f = _unquote(m.group(1))
            if f not in files:
                files.append(f)
    return files


def registration_state():
    """The registration of the merge drivers in the global git
    configuration: (missing, broken) - the keys of REGISTRATION that
    are absent or carry another value, and the registered command of
    the forge-records driver when its script does not exist (None
    otherwise). An unregistered clone silently falls back to a
    conflict, so forge-status reports both (SOL.0740)."""
    missing = [key for key, value in REGISTRATION
               if git_out(["config", "--global", "--get", key], ENGINE_ROOT) != value]
    driver = git_out(["config", "--global", "--get", DRIVER_KEY], ENGINE_ROOT)
    broken = None
    if driver:
        script = next((t.strip("'\"") for t in driver.split() if t.endswith(".py")), None)
        if script is None or not Path(script).is_file():
            broken = driver
    return missing, broken


def project_path(slug):
    return ENGINE_ROOT / "projects" / slug


def project_file(path):
    """The project file of the project at `path` (SOL.0670, POS.1590):
    a dict with project, kind, language, fixture and shape. `shape` is
    'current' when project.md exists, 'before the migration' when
    only a hand-kept ledger.md carries the header (its kind and
    language are read then, one release back tolerated), 'none' when
    the directory has neither. Kind defaults to thought, language to
    en (POS.0960, POS.0060). The one reader of the file."""
    path = Path(path)
    info = {"project": path.name, "kind": "thought", "language": "en", "fixture": False, "shape": "none"}
    src = None
    if (path / "project.md").exists():
        src, info["shape"] = path / "project.md", "current"
    elif (path / "ledger.md").exists():
        src, info["shape"] = path / "ledger.md", "before the migration"
    if src is None:
        return info
    text = src.read_text(encoding="utf-8", errors="replace")
    front = text.split("\n---", 2)[0] if text.startswith("---") else ""
    for key in ("project", "kind", "language", "fixture"):
        m = re.search(r"^" + key + r":\s*([^#\n]*)", front, re.M)
        if m and m.group(1).strip():
            value = m.group(1).strip().strip('"').strip("'")
            info[key] = (value.lower() == "true") if key == "fixture" else value
    return info


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
        if not own_repo(path):
            fail((strict_message or "Project '{slug}' is not a repository.").format(slug=slug))
        repos.append((slug, path))
        return repos
    repos.append(("forge (engine)", ENGINE_ROOT))
    if not slug:
        projects = ENGINE_ROOT / "projects"
        if projects.is_dir():
            for d in sorted(p for p in projects.iterdir() if p.is_dir() and p.name != "forge"):
                if own_repo(d):
                    repos.append((d.name, d))
                else:
                    say(f"{d.name:<20} not under git - skipped", "grey")
    return repos


def label(name, text):
    return f"{name:<20} {text}"
