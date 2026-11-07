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

    def run(name, *args, cwd=ENGINE):
        return subprocess.run([sys.executable, str(SCRIPTS / f"{name}.py"), *map(str, args)],
                              cwd=str(cwd), capture_output=True, text=True, encoding="utf-8")

    return run
