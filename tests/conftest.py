"""
Shared fixtures of the forge's tests (projects/forge/00-brief-tests.md).

The scripts in scripts/ carry hyphens in their names (hook-git.py,
forge-ledger.py), so Python's import statement cannot reach them;
load_script loads one by path as a module, without running its main.
The shared modules (forge_docs, forge_repos, ...) import directly:
pytest.ini puts scripts/ on the import path.

The fixture project, tests/fixture, is a synthetic thought project of
the current shape (project.md with `fixture: true`), never a copy of
a real one; a test works on a copy of it in a temporary directory
(`project`) and reaches the scripts by that path, as the scripts
take a slug or a path (forge_repos.project_path). The original is
never touched and nothing lands in projects/ (DEC.0240).
"""
import importlib.util
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ENGINE = Path(__file__).resolve().parent.parent
SCRIPTS = ENGINE / "scripts"
FIXTURE = ENGINE / "tests" / "fixture"


@pytest.fixture(scope="session")
def engine_root():
    """The engine's root directory."""
    return ENGINE


@pytest.fixture(scope="session")
def load_script():
    """Load scripts/<name>.py as a module and return it; cached per session."""
    loaded = {}

    def load(name):
        if name not in loaded:
            path = SCRIPTS / f"{name}.py"
            spec = importlib.util.spec_from_file_location(name.replace("-", "_"), path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = module
            spec.loader.exec_module(module)
            loaded[name] = module
        return loaded[name]

    return load


@pytest.fixture
def project(tmp_path):
    """A fresh copy of tests/fixture in a temporary directory, not
    under git; its path."""
    target = tmp_path / "fixture"
    shutil.copytree(FIXTURE, target)
    return target


@pytest.fixture(scope="session")
def run_script():
    """Run scripts/<name>.py as the forge runs it, `python scripts/<name>.py
    <args>`, from the engine root; the CompletedProcess with its text."""

    def run(name, *args, cwd=ENGINE, env=None):
        return subprocess.run([sys.executable, str(SCRIPTS / f"{name}.py"), *map(str, args)],
                              cwd=str(cwd), capture_output=True, text=True, encoding="utf-8",
                              env={**os.environ, **(env or {})})

    return run


@pytest.fixture
def git_env(tmp_path):
    """An environment in which git reads no global and no system
    configuration (an empty file stands for the global one), so that a
    test runs the same on every machine and in CI: no identity, no
    registration of the merge driver, nothing of the user's."""
    empty = tmp_path / "gitconfig-empty"
    empty.write_text("", encoding="utf-8")
    return {"GIT_CONFIG_GLOBAL": str(empty), "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_TERMINAL_PROMPT": "0"}


def git(args, cwd, env):
    """git as the tests run it on their own repositories: checked,
    the output as text."""
    r = subprocess.run(["git", *map(str, args)], cwd=str(cwd), capture_output=True, text=True,
                       encoding="utf-8", env={**os.environ, **env})
    assert r.returncode == 0, f"git {' '.join(map(str, args))} in {cwd}:\n{r.stdout}{r.stderr}"
    return r.stdout.strip()


def identity(path, env):
    """A commit identity set in the repository itself, as a user would
    for a throwaway clone; the forge never sets one."""
    git(["config", "user.name", "tester"], path, env)
    git(["config", "user.email", "tester@example.invalid"], path, env)


@pytest.fixture
def repo(project, git_env):
    """The copy of the fixture as a repository of its own: on main, a
    local identity, one commit, and a bare `origin.git` beside it that
    has that commit. Returns the path; `repo.parent / "origin.git"` is
    the origin."""
    git(["init", "-q", "-b", "main"], project, git_env)
    identity(project, git_env)
    git(["add", "-A"], project, git_env)
    git(["commit", "-q", "-m", "fixture: born"], project, git_env)
    origin = project.parent / "origin.git"
    git(["init", "-q", "--bare", "-b", "main", origin], project.parent, git_env)
    git(["remote", "add", "origin", str(origin)], project, git_env)
    git(["push", "-q", "-u", "origin", "main"], project, git_env)
    return project


@pytest.fixture
def other_clone(repo, git_env):
    """A second clone of the origin, as another person's, with its own
    local identity: what makes the first repository behind or diverged."""
    other = repo.parent / "other"
    git(["clone", "-q", repo.parent / "origin.git", other], repo.parent, git_env)
    identity(other, git_env)
    return other
