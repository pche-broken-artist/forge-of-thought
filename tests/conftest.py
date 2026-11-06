"""
Shared fixtures of the forge's tests (projects/forge/00-brief-tests.md).

The scripts in scripts/ carry hyphens in their names (hook-git.py,
forge-ledger.py), so Python's import statement cannot reach them;
load_script loads one by path as a module, without running its main.
The shared modules (forge_docs, forge_repos, ...) import directly:
pytest.ini puts scripts/ on the import path.
"""
import importlib.util
import sys
from pathlib import Path

import pytest

ENGINE = Path(__file__).resolve().parent.parent
SCRIPTS = ENGINE / "scripts"


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
