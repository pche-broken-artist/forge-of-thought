---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 663f02b6c6674dc6
inputs:
  - CLAUDE.md#Persistence (git)
  - CLAUDE.md#Repository layout
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

A script is a Python program in `scripts/` that does one job of the
forge for the engine or for a project, such as saving a repository,
making the ledger or converting a render. This page is for the
extender who writes a new script, or changes one: it says how the
script is written so that it runs on every platform, how it carries
its own help, how it is tested with its change and where its facts
live so that nothing is said twice. The scripts that exist are
listed in [Scripts](../reference/scripts.md).

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md) first: a
new script is a change of the forge, and it is proved, recorded and
released as any other change. The scripts are the only
platform-bound layer of the forge, and they are the only door to a
write of git; why that is so is [Persistence in
git](../about/persistence-in-git.md). Not everything needs a script:
a new engine for a research run, for example, is a row of the one
engine script and needs no script of its own, as [Add an
engine](add-an-engine.md) says.

## The files

- `scripts/<name>.py`: the script, with its help in its module
  docstring.
- `scripts/forge_repos.py`, `scripts/forge_tools.py`,
  `scripts/forge_docs.py`, `scripts/docs_map.py`,
  `scripts/forge_check.py`: the five modules the scripts share, one
  of which the new script imports where it needs what the module
  holds.
- `tests/test_<concern>.py`: the test of the script, one file per
  concern.
- `tests/conftest.py`: what the tests share; read, not changed, unless
  the new test needs something every test will need.
- `pytest.ini`: how pytest runs the tests; read, not changed.
- `CLAUDE.md`, the layout comment under Repository layout: the one
  line that names the script and says what it does.
- `tmp/`: the engine's working folder, where a script's working files
  go.

## Steps

### 1. Write the script to the portability rule

The script is Python 3.8 or newer and is run as
`python scripts/<name>.py`. `python` on PATH is the one prerequisite
of the scripts. A system that has only `python3` gives it that name.
The scripts carry no URL and no identity: the remote and the commit
identity are the user's own git configuration, and the forge sets
none.

The script uses nothing Windows-only:

- paths are composed with `pathlib`;
- processes run through `subprocess` with an argument list, never a
  shell;
- an external tool (`git`, `markitdown`, `pandoc`, `claude`) is
  resolved from PATH and never installed by the script;
- colour is printed only on a terminal; the `say` function of
  `forge_repos.py` does that for you and honours `NO_COLOR`;
- the usage examples in the help are free of platform-specific paths
  and invocations.

The scripts are written to run unchanged on Linux and macOS. The
tests run in CI on Linux and Windows at every push. Nothing has run
on macOS. So for macOS the rule is a writing rule alone, and a new
script is written to it rather than tried.

Why: the forge runs beyond Windows, and the scripts are the one
layer where a platform could creep in. `python` is the one command
name because Windows has only that one, and a Unix system gives it
by an alias or a package.

### 2. Put the help in the module docstring

Each script carries its help in its module docstring, at the top of
the file. The docstring says:

- the synopsis: the command line as it is typed, with its options;
- what it does, step by step where there are steps, and what each
  option changes;
- what it needs: the Python, the tools on PATH, the shared module
  beside it;
- where its output lands;
- examples: one line per way of calling it, each typed as it stands.

The docstring owns those facts. `CLAUDE.md` says of the scripts that
each is described in full by its own help header, and a command or a
skill that needs the script cites the header instead of repeating
it. So a fact about the script, such as what it needs installed or
where its file lands, is written in the docstring once and nowhere
else. `scripts/forge-status.py` is the smallest model: a synopsis,
what it does, what it needs and examples, in that order.

### 3. Take a project by its slug or by its path

A script that takes a project takes it by its slug or by the path of
its directory, through the one resolver of the shared module,
`project_path` of `forge_repos.py`. A bare word is a slug and means
`projects/<slug>`. Anything with a separator or an absolute path is
the directory itself, taken as given. The project's name is the
`project` field of its project file, read by `project_file` of the
same module; the directory's name stands where the file has none.
`forge` stays the engine's own project, by the name. The commands of
the forge call by slug as before; a report names the target the way
`project_label` gives it, `projects/<slug>` for a slug and the path
as given for a path.

Why: a copy of the fixture in a temporary directory is reached by a
path and by nothing else, and a path is an argument like any other,
visible in the command. Every script goes through the one resolver
so that the rule lives in one place.

### 4. Share through a module, never by copying

What several scripts share lives in one module beside them, imported
by path, and never twice. There are five today:

- `forge_repos.py`: the engine root, the git check, the list of
  repositories a bare or a slug form visits, running git, the state
  against the origin, the resolver of a project; for the git scripts.
- `forge_tools.py`: a tool on PATH, resolving paths, the headless
  Claude Code run; for the conversions.
- `docs_map.py`: the reader of the documentation map; for the three
  documentation scripts.
- `forge_docs.py`: the front-matter, the records, the ledger tables,
  the index entries and the threads as the scripts read them; for
  `forge-ledger`, `forge-migrate` and `forge-history`.
- `forge_check.py`: a finding and its report, the keys and comments a
  template owns; for `forge-check`.

A module is not a command: it has no synopsis and is never run. Its
docstring says what it holds and which scripts it serves;
`scripts/forge_repos.py` is the model. Where the new script needs
what a module already holds, it imports the module. Where it needs
something two scripts will need, that goes into the module that
serves them, not into both scripts.

### 5. Put working files in `tmp/`

A script's working files go to the engine's working folder, `tmp/`
at the engine root, never to the system's temporary directory. The
script makes the subfolder it needs there. The folder is in git with
its own README and `.gitignore`, so that it exists on every clone;
its contents never are. Nothing in it is a source of truth: no
check, no ledger (the project's state report, made at read time) and
no history reads from it. A run is kept for inspection and deleted by
hand, never by a script.

Why: one folder in the engine makes a run traceable on the machine
and gives a profile's deny rules one path to name. The price is a
folder to empty by hand.

### 6. Name the script in the layout comment

Add the script to the layout comment of `CLAUDE.md`, under
Repository layout, in the `scripts/` entry: its name and what it does
in a clause, as the others stand there. A shared module is named in
the same entry among the modules the scripts share. The engine check
verifies that comment against the disk (Prove it, below).

### 7. Write the test with the script

A script is changed with its test, and a new script comes with one.
The tests are the engine's, in `tests/` at the engine root, beside
the scripts they test, run by pytest from the engine root. The test
is in proportion: enough to catch what a change of the script
breaks, never a suite for its own sake, and no coverage figure as a
target.

The test uses what the tests share, the fixtures of
`tests/conftest.py`:

- `load_script`: a script with a hyphen in its name loaded as a
  module without running its main;
- `run_script`: a script run as the forge runs it,
  `python scripts/<name>.py …` from the engine root, with an
  environment;
- `project`: a copy of the fixture project;
- `git_env`: git with an empty global configuration and no system
  one, and no terminal prompt;
- `repo` and `other_clone`: the copy as a repository with a bare
  origin beside it, and a second clone.

`pytest.ini` puts `scripts/` on the import path, so a shared module
imports by its name; a script with a hyphen in its name cannot, and
is loaded through `load_script`. The fixture is a synthetic thought
project under `tests/fixture`, never a copy of a real project; a test
works on a copy of it in a temporary directory and never changes the
fixture itself. What the tests cover and what the fixture is, is [The
tests](../about/the-tests.md).

Two rules hold for every test:

- a script that calls an external tool is tested for its failure
  without the tool, on an empty PATH, and the test checks that the
  script names the tool and how it is installed;
- a test never runs on a live repository, neither the engine's nor a
  project's; where it needs git, it takes `repo`, the throwaway
  repository made from the copy.

Why: a pull request on a script carries its test, which is possible
in one repository only, and CI runs where the code is.

## Prove it

Run the tests from the engine root:

```
/test
```

`/test` runs `python -m pytest -q` over `tests/` and reports the sum
as pytest prints it. A red test is reported word for word, the
failing assertion included; nothing is fixed on its word, and the fix
is a round of its own, the script changed with its test. To run the
one file of the new test:

```
/test tests/test_<concern>.py
```

Where pytest is not installed, `/test` says that the tests did not
run and names the one install a contributor needs beyond `python`:

```
python -m pip install pytest
```

A user of the engine never runs the tests and installs nothing for
them. How the command is used in full is [Run the
tests](../use/run-the-tests.md).

Then run the engine check:

```
/check engine
```

Among what it verifies: every file in `scripts/` is described in the
layout comment of `CLAUDE.md`, and nothing described there is
missing on disk. A script left out of the comment, or a line in the
comment for a script that does not exist, is a finding.

The same suite runs in CI at every push and pull request of the
engine, on Linux and Windows, Python 3.8 and the newest.

## Record and release

The script and its test are recorded and released as any change of
the forge; the way is [Make a change to the
forge](how-a-change-is-made.md). The release of the engine runs the
tests as its first step, before its checks, and `/save` never runs
them.

## A worked example

Suppose a script `forge-example.py` that lists the open threads of a
project.

Its docstring opens with its name and one line of what it does: the
open threads of a project, one line each. The synopsis is
`python scripts/forge-example.py [slug | path]`. "What it does" says
that it reads the project's `threads/` directory and prints each open
thread with its ID and title, and that it changes nothing. "What it
needs" says Python 3.8 or newer and `forge_repos.py` beside it, and
nothing on PATH, since it calls no tool. "Where the output lands"
says the terminal, and nothing is written. The examples are two
lines: the script with a placeholder slug such as `my-project`, and
the script with the path of a project's directory, a relative path
such as `../copies/my-project`, which reads the same on every
platform.

The script resolves its argument through `project_path` of
`forge_repos.py`, names the project through `project_file`, and
prints through `say`, so that colour appears on a terminal only.
It is named in the layout comment of `CLAUDE.md` in one clause:
`forge-example` (the open threads of a project).

Its test is `tests/test_forge_example.py`. It takes the `project`
fixture, a copy of the synthetic project in a temporary directory,
and runs the script through `run_script` with the path of the copy,
which is why the script had to take a path. It checks that the open
thread of the fixture is in the output and the closed one is not.
Nothing of the engine or of a project is touched. Since the script
calls no external tool, no failure-without-the-tool test is needed;
a script that called `pandoc` would have one more test, on an empty
PATH, checking that the message names `pandoc` and how to install
it.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Run the tests](../use/run-the-tests.md): running the tests.
- [The tests](../about/the-tests.md): what the tests cover and what
  the fixture is.
- [Scripts](../reference/scripts.md): the scripts that exist.
- [Persistence in git](../about/persistence-in-git.md): why the
  scripts are the only door.
- [Add an engine](add-an-engine.md): a row of the engine script,
  which needs no script of its own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
