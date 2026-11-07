"""
forge_repos.py - what the forge-* git scripts share: the engine root,
the git check, the list of repositories to visit, running git, the
state of a repository against its origin (`remote_state`: up to date,
behind, ahead, diverged, no origin; POS.1490), what waits on GitHub
outside git (`github_waiting`: the open pull requests and the
unanswered discussions through gh, or the one line saying why it
could not read; POS.1970), the files of the
global git configuration as git reads them (`global_config_files`),
the registration of the merge driver ours on the machine
(`registration_state`; SOL.0740) and coloured output. Not a command.

The engine root is the parent of the directory this file lies in
(`scripts/`). A project is `projects/<slug>`, or the directory a path
names (`project_path`: a bare word is a slug, anything with a
separator or absolute is a path, as the forge's tests pass their
copy of the fixture in a temporary directory); its name is the
`project` field of its project file (`project_file`). It is a
repository of its own when git names its directory as the top of a repository
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


_GITHUB_QUERY = """
query($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    owner { login }
    pullRequests(states: OPEN, first: 20, orderBy: {field: CREATED_AT, direction: DESC}) {
      nodes { number title createdAt changedFiles author { login } }
    }
    discussions(first: 50, orderBy: {field: UPDATED_AT, direction: DESC}) {
      nodes { number title createdAt author { login }
        comments(first: 50) { nodes { author { login }
          replies(first: 50) { nodes { author { login } } } } } }
    }
  }
}
"""


def github_waiting(path):
    """What waits on GitHub outside git for the repository at `path`
    (POS.1970): a list of lines, the first the counts, then one line
    per open pull request and per unanswered discussion - a discussion
    opened by someone other than the repository's owner that carries
    no comment or reply by the owner. Read through gh in one GraphQL
    query. Whatever keeps it from reading - no gh on PATH, an origin
    that is not GitHub, no login, no network - gives one line saying
    so, in gh's own words where it has them; the caller goes on
    (SOL.0910)."""
    import json
    gh = shutil.which("gh")
    if not gh:
        return ["could not read: gh not on PATH"]
    origin = git_out(["remote", "get-url", "origin"], path)
    m = re.search(r"github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?/?$", origin)
    if not m:
        return [f"could not read: the origin is not on GitHub ({origin or 'no origin'})"]
    owner, name = m.group(1), m.group(2)
    r = subprocess.run([gh, "api", "graphql", "-f", f"query={_GITHUB_QUERY}",
                        "-F", f"owner={owner}", "-F", f"name={name}"],
                       cwd=str(path), text=True, encoding="utf-8", errors="replace",
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if r.returncode != 0:
        first = next((l.strip() for l in r.stdout.splitlines() if l.strip()), "gh failed")
        return [f"could not read: {first}"]
    try:
        repo = json.loads(r.stdout)["data"]["repository"]
    except (ValueError, KeyError, TypeError):
        return ["could not read: gh answered with something that is not the repository"]
    if repo is None:
        return [f"could not read: gh sees no repository {owner}/{name}"]
    login = (repo.get("owner") or {}).get("login")
    prs = repo["pullRequests"]["nodes"]
    unanswered = []
    for d in repo["discussions"]["nodes"]:
        if (d.get("author") or {}).get("login") == login:
            continue
        answered = any((c.get("author") or {}).get("login") == login
                       or any((x.get("author") or {}).get("login") == login
                              for x in c["replies"]["nodes"])
                       for c in d["comments"]["nodes"])
        if not answered:
            unanswered.append(d)
    lines = [f"{len(prs)} pull request(s) open, {len(unanswered)} discussion(s) unanswered"]
    for x in prs:
        lines.append(f"#{x['number']} pull request \"{x['title']}\" by {(x.get('author') or {}).get('login', '?')}, "
                     f"{x['createdAt'][:10]}, {x['changedFiles']} file(s)")
    for x in unanswered:
        lines.append(f"#{x['number']} discussion \"{x['title']}\" by {(x.get('author') or {}).get('login', '?')}, "
                     f"{x['createdAt'][:10]}")
    return lines


# The registration /setup makes in the global git configuration, once
# per machine (SOL.0740): the keys with the values they must carry.
# `rerere.enabled` is a convenience and is never reported missing.
REGISTRATION = (
    ("merge.ours.driver", "true"),
    ("rebase.backend", "merge"),
    ("merge.renormalize", "true"),
)


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
    """The registration of the merge driver `ours` and the settings it
    needs in the global git configuration: the keys of REGISTRATION
    that are absent or carry another value. An unregistered clone
    silently falls back to a conflict on the derived files, so
    forge-status reports it (SOL.0740)."""
    return [key for key, value in REGISTRATION
            if git_out(["config", "--global", "--get", key], ENGINE_ROOT) != value]


def project_path(project):
    """The directory of a project: `projects/<slug>` for a bare word,
    the directory itself for a path (one with a separator, or an
    absolute one), taken as given. 'forge' is the engine's own
    project; the callers that treat it apart do so by the name."""
    if is_path(project):
        # abspath first: on Python 3.8 for Windows, resolve() leaves a
        # relative path of a directory that does not exist relative
        return Path(os.path.abspath(project)).resolve()
    return ENGINE_ROOT / "projects" / project


def is_path(project):
    """Whether `project` names a directory rather than a slug: it is
    absolute or carries a separator (`./x` counts, as written)."""
    return Path(project).is_absolute() or "/" in str(project) or "\\" in str(project)


def project_label(project):
    """How a report or a message names the target: `projects/<slug>`
    for a slug, the path as it was given for a path."""
    return str(project) if is_path(project) else f"projects/{project}"


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
    (name, path) pairs, the engine first. With a slug or a path other
    than 'forge' the one project, which must exist and be a repository
    (the message for the second case is strict_message, with {slug}
    inside), named as its project file names it; bare, the engine and
    every project that is a repository, the others reported and
    skipped."""
    repos = []
    if slug and slug != "forge":
        path = project_path(slug)
        if not path.exists():
            fail(f"Project '{slug}' not found ({path} does not exist).")
        if not own_repo(path):
            fail((strict_message or "Project '{slug}' is not a repository.").format(slug=slug))
        repos.append((project_file(path)["project"], path))
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
