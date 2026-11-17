---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 9cad9f139c4a9581
inputs:
  - CLAUDE.md#Portability
  - .claude/reference/repository-layout.md
  - scripts/forge-status.py
  - scripts/forge_repos.py
  - .claude/agents/check-engine.md
  - .claude/skills/test/SKILL.md
  - pytest.ini
  - projects/forge/10-intent.md#POS.0830
  - projects/forge/10-intent.md#POS.1900
  - projects/forge/10-intent.md#POS.1930
  - projects/forge/10-intent.md#POS.1950
  - projects/forge/40-solution-design.md#SOL.0620
  - projects/forge/40-solution-design.md#SOL.0890
  - projects/forge/40-solution-design.md#SOL.0900
---

# Add a script

A script is a Python program in `scripts/` at the root of the
[engine](../reference/glossary.md) (the repository that holds the
forge's rules, commands, scripts and templates), run as
`python scripts/<name>.py`. This page is for whoever extends the forge
by a script. It says how the script is written so that it runs beyond
one platform, where its help stands, how it takes a project, where its
working files go and how it is tested with the change that brings it.

## Before you start

- Read [Make a change to the forge](how-a-change-is-made.md). A new
  script is recorded and released as any change of the forge.
- Look in [Scripts](../reference/scripts.md) for the scripts that
  exist.
- A model of another family needs no script of its own. It is a row
  of the engine script: see [Add an engine](add-an-engine.md).
- Have Python 3.8 or newer, with `python` on PATH. That is the one
  prerequisite of the scripts. A system that has only `python3` gives
  it that name.
- Install the one thing the tests need beyond `python`:
  `python -m pip install pytest`.
- Know what a run has proven. The scripts are written to run
  unchanged on Linux and macOS. The tests run in CI (the workflow
  `.github/workflows/tests.yml`) on Linux and Windows at every push.
  Nothing has run on macOS. A new script is therefore written to the
  rules below, whatever machine it is written on.

## The files

| File | What it is |
|---|---|
| `scripts/<name>.py` | the script, with its help in its module docstring |
| `scripts/<module>.py` | a shared module, only where several scripts share something |
| `.claude/reference/repository-layout.md` | the layout of the engine's root, where every script is named in the comment on `scripts/` |
| `CLAUDE.md` | the script's governing rule, where it has one |
| `tests/test_<concern>.py` | the test, one file per concern |
| `tests/conftest.py` | what the tests share |
| `tests/fixture` | the synthetic fixture project that every test copies |
| `pytest.ini` | how pytest runs the tests: `tests/` as the path, `scripts/` on the import path |
| `tmp/` | the engine's working folder, where a script's working files go |

What several scripts share lives in one module beside them. There are
five such modules today:

| Module | What it holds | The scripts it serves |
|---|---|---|
| `forge_repos.py` | the engine root, the git check, the list of repositories a bare or a slug form visits, running git, the one resolver of a project | the five git scripts (`forge-save`, `forge-pull`, `forge-status`, `forge-clone`, `forge-branch`) |
| `forge_tools.py` | a tool on PATH, resolving paths, the headless Claude Code run | the three conversions |
| `docs_map.py` | the reader of the documentation map | the three documentation scripts (`docs-state`, `docs-index`, `docs-check`) |
| `forge_docs.py` | the front-matter, the records, the ledger tables, the index entries and the threads as the scripts read them | `forge-ledger`, `forge-migrate` and `forge-history` |
| `forge_check.py` | a finding and its report, the keys and comments a template owns | `forge-check` |

The ledger is a project's state in tables, made at read time from its
documents. The other terms of the table are explained in the
[Glossary](../reference/glossary.md).

## Steps

1. **Write the docstring first.** Create `scripts/<name>.py`. Its
   module docstring is its help. Under the line that names the script,
   the docstring has four parts, each under its heading in capitals:

   - `SYNOPSIS`: the line as it is typed, `python scripts/<name>.py`
     with its arguments;
   - `WHAT IT DOES`: what the script reads, what it changes and what
     it reports;
   - `WHAT IT NEEDS`: Python 3.8 or newer, every external tool it
     expects on PATH, the shared module beside it;
   - `EXAMPLES`: lines that can be typed as they stand.

   The docstring is the one owner of these facts. A command that runs
   the script cites the docstring and does not repeat it. The smallest
   model of such a docstring is the one of `scripts/forge-status.py`.

2. **Write the script to the rules of portability.**

   - Nothing in it is Windows-only.
   - Paths are composed with `pathlib`.
   - Processes run through `subprocess` with argument lists, never
     through a shell.
   - External tools (`git`, `markitdown`, `pandoc`, `claude`) are
     resolved from PATH. A script never installs a tool. Where the
     tool is missing, the script fails with a message that names the
     tool and how it is installed.
   - Colour is used only on a terminal.
   - The examples in the help are free of Windows-specific paths and
     invocations.
   - The script carries no URL and no identity: no remote URL, no
     author identity, no first-run initialisation. The git
     configuration belongs to whoever runs the forge.

   The reason for these rules is that the forge runs beyond Windows,
   and `scripts/` is its only platform-bound layer.

3. **Take a project by its slug or by the path of its directory.**
   This step applies to a script that takes a project. A bare word is
   a slug and means `projects/<slug>`. Anything with a separator, or
   an absolute path, is the directory itself, taken as given. Resolve
   the argument through the one resolver, `project_path` of
   `forge_repos.py`, and nowhere else. Three functions stand beside
   it:

   - `is_path`: the rule that tells a path from a slug;
   - `project_label`: how a report or a message names the target;
   - `project_file`: the project's name, which is the `project` field
     of its project file, or the directory's name without one.

   The reason is that a copy of a project in a temporary directory is
   reached by a path and by nothing else. A path is also an argument
   like any other, visible in the command. The commands of the forge
   go on calling by slug.

4. **Put what several scripts share into a module.** What your script
   needs and a module of the table above holds, it takes from that
   module. What it shares anew with another script goes into a module
   beside them, never into both scripts. A module is not a command.
   Its docstring says what it holds, as the one of
   `scripts/forge_repos.py` does.

5. **Send working files to `tmp/`.** `tmp/` at the engine's root is
   the one working folder of the forge. A script that needs a
   subfolder there makes it. A script never writes its working files
   to the system's temporary directory. The folder exists on every
   clone, and its contents never enter git. Nothing in it is a source
   of truth: no check, no ledger and no history reads from it. A run
   is kept for inspection and deleted by hand, never by a script.

   The folder was chosen over the system's temporary directory for two
   reasons. A run stays traceable on the machine. The profile of a run
   on another engine has one path to name in its deny rules. The price
   is a folder that is emptied by hand.

6. **Name the script in the layout.** Add the script to the comment
   on `scripts/` in `.claude/reference/repository-layout.md`, with
   what it is for in a clause, as the scripts there stand:
   `forge-history (the history of one item)`. A shared module is
   named in the same comment, among the modules the scripts share.
   Where the script has a governing rule, the rule stands in
   `CLAUDE.md`. The page
   [Repository layout](../reference/repository-layout.md) shows the
   layout as it reads today.

7. **Write the test with the script.** A script is changed with its
   test, and a pull request on a script carries the test. The tests
   have one place, `tests/` at the engine's root, with one file per
   concern. No script carries tests of its own. `tests/conftest.py`
   holds what the tests share:

   - `load_script`: a script with a hyphen in its name, loaded as a
     module without running its main;
   - `run_script`: a script run as the forge runs it,
     `python scripts/<name>.py …` from the engine root, with an
     environment;
   - `project`: a copy of the fixture (the synthetic project in
     `tests/fixture`);
   - `git_env`: git with an empty global configuration and no system
     one, and no terminal prompt;
   - `repo` and `other_clone`: the copy as a repository with a bare
     origin, and a second clone.

   `pytest.ini` puts `scripts/` on the import path, so a test imports
   a shared module by its name. A script with a hyphen in its name is
   loaded through `load_script`. The tests run a script as a
   subprocess rather than importing its main. What is tested is then
   the command as the forge calls it.

   Three rules hold for the test:

   - It works on a copy of the fixture in a temporary directory. It
     never runs on a live repository, neither the engine nor a
     project.
   - A script that calls an external tool is tested for its failure
     without the tool: the message names the tool and how it is
     installed. For a script that calls pandoc, markitdown or a model
     that is the whole test. What those tools return is not tested.
   - It stays in proportion: enough to catch what a change of the
     script breaks, never a suite for its own sake, and no coverage
     figure as a target.

   What the tests cover and what the fixture is stands in
   [The tests](../about/the-tests.md).

## Prove it

1. Run the tests:

   ```
   /test
   ```

   Claude runs the whole suite from the engine root, as
   `python -m pytest -q`. What you add is passed to pytest as it
   stands:

   - `/test tests/test_<concern>.py` runs one file;
   - `/test -k <word>` runs the tests whose name carries the word;
   - `/test -x` stops at the first red test.

   You should now see the sum as pytest prints it, with every test
   passed. A red test is reported word for word as pytest printed it,
   the failing assertion included. Nothing is fixed on this command's
   word: the fix is a round of its own, the script changed with its
   test. If you see `No module named pytest`, the tests did not run:
   install pytest with `python -m pip install pytest`. The command
   changes nothing of the engine or of a project. More on it:
   [Run the tests](../use/run-the-tests.md).

2. Run the engine check:

   ```
   /check engine
   ```

   The check compares the scripts on disk with the layout of the
   engine's root. It verifies three things:

   - every file in `scripts/` is described in the layout;
   - its governing rule stands in `CLAUDE.md` where it has one;
   - nothing described in the layout is missing on disk.

   A script on disk that the layout does not name is what this check
   is there to catch.

Once the change is pushed, the same suite runs in CI: at every push
and pull request, on Linux and Windows, on Python 3.8 and the newest.
That run is what verifies portability. For macOS there is no run.

## Record and release

The new script is recorded and released as any change of the forge:
[Make a change to the forge](how-a-change-is-made.md) says how. A
release of the engine runs the tests first. A save never runs them.

## A worked example

The script here is made up: `forge-example.py` prints the name of a
project. Its docstring, written before anything else:

```python
"""
forge-example.py - print the name of a project.

SYNOPSIS
    python scripts/forge-example.py <slug | path>

WHAT IT DOES
    Read-only, changes nothing. Prints the name of the project: the
    `project` field of its project file, the directory's name
    without one.

WHAT IT NEEDS
    Python 3.8 or newer. `forge_repos.py` beside it.

EXAMPLES
    python scripts/forge-example.py my-project          # a project by its slug
    python scripts/forge-example.py copies/my-project   # a project by its path
"""
```

The four parts say everything a command needs to cite. The examples
carry a placeholder slug and a relative path, nothing of one platform.
The script takes its project through `project_path` of
`forge_repos.py`, which is why the docstring names that module under
what it needs.

The test that goes with it is one file, `tests/test_forge_example.py`,
for this one concern. In words:

- The test asks `tests/conftest.py` for `project` and for
  `run_script`.
- `project` gives it a copy of the fixture in a temporary directory.
- Through `run_script` it runs the script as the forge runs it, with
  the path of the copy as the argument. The copy is reached by its
  path and by nothing else.
- It expects the script to end without an error and to print the name
  that the copy's project file gives.

The script calls no external tool, so there is no test of a failure
without one. It runs no git, so `git_env`, `repo` and `other_clone`
stay unused. Had the script called pandoc, a second test would run it
without pandoc and expect a message that names pandoc and how it is
installed.

Then `/test tests/test_forge_example.py` runs the one file. The name
`forge-example`, with its clause, goes into the comment on `scripts/`
in the layout, and `/check engine` verifies that the layout and the
disk agree.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Run the tests](../use/run-the-tests.md): running the tests.
- [The tests](../about/the-tests.md): what the tests cover and what
  the fixture is.
- [Scripts](../reference/scripts.md): the scripts that exist.
- [Repository layout](../reference/repository-layout.md): the layout
  of the engine's root, where a script is named.
- [Persistence in git](../about/persistence-in-git.md): why the
  scripts are the only door.
- [Add an engine](add-an-engine.md): a row of the engine script,
  which needs no script of its own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
