# GitHub issue #3: Repository detection tests for `<path>/.git` instead of asking git — a project inside a larger repository is "not under git"

Source: https://github.com/pche-broken-artist/forge-of-thought/issues/3  
Author: vobornik  
Opened: 2026-10-21  
State at download: open, downloaded 2026-10-21

## Summary

The scripts decide whether a project is a git repository by testing `(path / ".git").exists()` on the project directory, and they assume that the project directory *is* the repository root. Git's own answer is `git rev-parse --show-toplevel`. The hand-rolled test gives wrong results for any layout in which the project directory is not the top of its repository, and those layouts are ordinary.

## Example layout

```
~/work/my-project/               <- git repository (.git here)
├── .git/
├── ...
└── specs/                       <- the forge project
<engine>/projects/my-project -> ~/work/my-project/specs   (symlink)
```

`git -C <engine>/projects/my-project rev-parse --show-toplevel` correctly answers `~/work/my-project`. Every forge script answers "not a repository".

## Observed behaviour

- `forge-status.py`: `my-project  not under git`
- `/save`, `/pull` (`repos_to_visit`): the project is skipped, or with a slug the command fails with "is not a repository"
- `forge-branch.py`: "not a repository - nothing to switch"
- `forge-migrate.py --apply`: refuses with "not a repository"
- `forge-ledger.py`: the `tracked` guard never sees the repository, so a tracked `ledger.md` is written instead of refused

## Where (main at `c0b0f3c`)

| file | line | what |
|---|---|---|
| `scripts/forge_repos.py` | 46 | `need_engine_repo`: `(ENGINE_ROOT / ".git").exists()` |
| `scripts/forge_repos.py` | 206, 215 | `repos_to_visit`, used by `forge-save.py` and `forge-pull.py` |
| `scripts/forge-status.py` | 49 | `show_repo` |
| `scripts/forge-branch.py` | 59 | |
| `scripts/forge-migrate.py` | 147, 472, 562 | `self.repo = self.proj = fr.project_path(slug)`; `refusals` |
| `scripts/forge-ledger.py` | 81, 468, 586–587 | `self.repo = fr.project_path(slug)`; paths relative to `p.repo`; the `tracked` guard |
| `scripts/docs-state.py` | 149–151 | walks parent directories looking for `.git`, a hand-written reimplementation of `rev-parse --show-toplevel` |

## Why this is not only a symlink problem

The test also misses:
- a project that is a subdirectory of a repository, symlinked or not;
- `GIT_DIR` / `GIT_WORK_TREE` setups.

A second assumption sits underneath the first one: **project root == repository root**. Paths passed to git are computed relative to the project directory (`forge-ledger.py` `relative_to(p.repo.resolve())`, `forge-migrate.py` undo via `git checkout -- <rel>`, `.gitignore` and `.gitattributes` written into the project directory). These break as soon as the toplevel sits above the project.

## Expected behaviour

Ask git where the repository is and keep the two notions apart: the project directory and its repository.

## Proposed fix

One helper in `forge_repos.py`, used by every site above:

```python
def repo_root(path):
    """The top of the git repository that holds `path`, or None.
    A project inside the engine's tree with no repository of its own
    resolves to the engine (projects/ is gitignored there), which
    means 'not under git' for a project."""
    top = git_out(["rev-parse", "--show-toplevel"], path)
    if not top:
        return None
    top = Path(top).resolve()
    if top == ENGINE_ROOT.resolve() and Path(path).resolve() != ENGINE_ROOT.resolve():
        return None
    return top
```

Then:
- replace every `(x / ".git").exists()` with `repo_root(x)`;
- give `Target` / `Project` separate `proj` and `repo` attributes everywhere, as `forge-migrate.py` already does for `forge`, and compute git pathspecs relative to `repo`;
- decide where `.gitignore` and `.gitattributes` belong when the toplevel is above the project (the repository root, or the project directory with a relative pattern);
- drop the parent-walk in `docs-state.py` in favour of the helper.

The engine-root exclusion is needed because `projects/` lives inside the engine's working tree. Without it, an un-versioned project would be reported as "under git" (the engine's).

## Environment

Linux, Python 3, project directory reached through a symlink into a subdirectory of another repository.


---

## Comment by pche-broken-artist, 2026-10-21 20:59 UTC

Thank you, the analysis holds: all nine sites you list exist on main, and the second assumption (project root == repository root) is real, in forge-ledger (paths relative to `p.repo`, the `tracked` guard), forge-migrate (`git checkout -- <rel>`, `.gitignore` and `.gitattributes` written into the project directory) and docs-state (the parent walk).

Accepted for work. It is not a script fix alone: the forge's own intent states that every project is a repository of its own and CLAUDE.md (Persistence) says the scripts recognise a project through `projects/<slug>/.git`, so the intent changes first, then the solution design, then the scripts and CLAUDE.md. I will note the thread here when it exists.

One remark on the proposed helper: the engine-root exclusion compares `--show-toplevel` with `ENGINE_ROOT` literally, which holds only while the engine is itself the top of its repository. A copied engine (not cloned) inside a directory that is under another git would make a project with no repository of its own resolve to that outer top, which is not `ENGINE_ROOT`, so the exclusion would not fire and `need_engine_repo` would pass. The fix is one condition: the engine must be exactly the top of its repository, else the script refuses as it does today. Read, not run.

On `.gitignore` and `.gitattributes`: git honours both in a subdirectory for the paths below it, so they can stay in the project directory with patterns relative to it; only the pathspecs (`git rm --cached`, `ls-files`, `log -- <path>`, `checkout --`) need to be relative to the repository root.
