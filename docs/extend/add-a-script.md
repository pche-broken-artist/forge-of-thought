---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 0134e6a01e2328f1
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

A script of the forge is a Python program in `scripts/`, run as
`python scripts/<name>.py`, that does one mechanical job for the
engine or for a project: the scripts are the one way a write of git
happens, and they make the ledger (the project's state, built from
its documents at read time), the reports, the conversions and the
documentation's state. This page is for the extender who wants to
add one. It says how a new script is written so that it runs on
every platform the forge runs on, carries its own help in its
docstring, is tested with its change and is the one owner of the
facts about itself.

## Before you start

A new script is a change of the forge like any other: it is proved,
recorded and released as [Make a change to the
forge](how-a-change-is-made.md) says. Read that page first; this one
adds only what is particular to a script.

Know the scripts that exist before you add one. They are listed on
[Scripts](../reference/scripts.md), each with the job it does. Why the
scripts, and only the scripts, write into git is said on [Persistence
in git](../about/persistence-in-git.md). Not every addition needs a
script: a new engine for the research, for instance, is a row of the
engine script and nothing of its own, as [Add an
engine](add-an-engine.md) shows. The words of the forge used here are
in the [Glossary](../reference/glossary.md).

## The files

- `scripts/<name>.py`: the script. A script that is run carries a
  hyphen in its name, as `forge-status.py` does. A module that other
  scripts import carries an underscore, as `forge_repos.py` does. A
  hyphen is not a name Python imports, so a script is loaded in a
  test through the shared `load_script` and a module by its name.
- `scripts/<module>.py`: the shared module, where the new script
  shares something with others. What several scripts share lives in
  one module beside them, imported by path, and never twice. There
  are five today:
  - `forge_repos.py`: the engine root, the check that git is there,
    the list of repositories a bare or a slug form visits, running
    git, the state of a repository against its origin, and the one
    resolver of a project by its slug or its path; for the git
    scripts, and for every script that takes a project.
  - `forge_tools.py`: a tool on PATH, resolving paths, the headless
    Claude Code run; for the conversions.
  - `forge_docs.py`: the front-matter, the records, the ledger
    tables, the index entries and the threads as the scripts read
    them; for `forge-ledger`, `forge-migrate` and `forge-history`.
  - `docs_map.py`: the reader of the documentation map; for the
    documentation scripts.
  - `forge_check.py`: a finding and its report, the keys and
    comments a template owns; for `forge-check`.
- `tests/test_<concern>.py`: the test of the script, one file per
  concern. The tests are run from the engine root by `/test`; what
  they are and what the fixture is stands on [The
  tests](../about/the-tests.md).
- `tests/conftest.py`: what the tests share. A new test uses it; it
  does not restate it.
- `CLAUDE.md`, the section Repository layout: the comment on the
  `scripts/` line names every script with one clause on what it does.
  The new script gets its clause there.
- `pytest.ini`: nothing to change. It already names `tests/` as the
  test path and puts `scripts/` on the import path, so the shared
  modules import by name in a test.

## Steps

1. Write the script for Python 3.8 or newer, to be run as
   `python scripts/<name>.py`. `python` on PATH is the one
   prerequisite of the scripts; a system that has only `python3`
   gives it that name.

2. Use nothing Windows-only. The rules:
   - paths are composed with `pathlib`, never as strings;
   - processes run through `subprocess` with an argument list, never
     through a shell;
   - an external tool (`git`, `markitdown`, `pandoc`, `claude`, `gh`)
     is resolved from PATH and never installed by the script;
   - colour is printed only on a terminal, and not where `NO_COLOR`
     is set; the shared module's `say` does this for you;
   - the examples in the help are free of platform-specific paths
     and invocations;
   - the script carries no URL and no identity: git configuration is
     the user's, and the forge sets none.

   The scripts are written to run unchanged on Linux and macOS. The
   tests run in CI on Linux and Windows at every push. Nothing has
   run on macOS, so for macOS the writing rule is all there is, and a
   new script is written to it. The conversions are tested for their
   failure without the tool alone, and the per-prompt hook is a
   writing rule until a run says otherwise.

3. Write the help in the module docstring, at the top of the file.
   The docstring has four parts, in this order:
   - a synopsis: the command line, with every argument and option;
   - what it does: what the script reads, what it writes, what it
     prints and what it refuses;
   - what it needs: the Python, the tools on PATH, the modules
     beside it;
   - examples: lines that can be typed as they stand.

   The docstring is the one owner of these facts. A command, a skill
   or a page that needs them cites the header and does not restate
   it; `CLAUDE.md` says of the scripts that each is described in
   full by its own help header. `scripts/forge-status.py` is the
   smallest model to copy from.

4. Where the script takes a project, take it by its slug or by the
   path of its directory, through the one resolver,
   `forge_repos.project_path`. A bare word is a slug and means
   `projects/<slug>`. Anything with a separator, or an absolute path,
   is the directory itself, taken as given. The project's name is the
   `project` field of its project file, read through
   `forge_repos.project_file`, and the directory's name where there
   is none. The word `forge` stays the forge's own project by the
   name. How a report or a message names the target is
   `forge_repos.project_label`. Every script goes through this
   resolver and none has one of its own. The reason: a copy of the
   fixture in a temporary directory is reached by a path and by
   nothing else, and a path is an argument like any other, visible
   in the command.

5. Put what the script shares with others in the module beside it,
   never in two scripts. Where the shared thing fits one of the five
   modules above, it goes there. Where it fits none, a new module is
   a change of the layout comment too.

6. Send the script's working files to the engine's working folder,
   `tmp/`, never to the system's temporary directory. The folder is
   in git with its own README and `.gitignore`, so that it exists on
   every clone; its contents never are. Nothing in `tmp/` is a source
   of truth: no check, no ledger and no history reads from it. A run
   is kept for inspection and deleted by hand, never by a script. The
   reason for one folder in the engine over the system's temporary
   directory: a run is traceable on the machine, and a profile's deny
   rules have one path to name. The price is a folder to empty by
   hand.

7. Write the test with the script, in `tests/test_<concern>.py`, one
   file per concern. A script is changed with its test, and a pull
   request on a script carries it. The tests use what
   `tests/conftest.py` shares:
   - `load_script`: a script with a hyphen in its name loaded as a
     module without running its main;
   - `run_script`: a script run as the forge runs it,
     `python scripts/<name>.py …` from the engine root, with an
     environment;
   - `project`: a copy of the fixture in a temporary directory;
   - `git_env`: git with an empty global configuration and no system
     one, so that nothing of the machine the test runs on changes
     the result;
   - `repo` and `other_clone`: the copy as a repository with a bare
     origin beside it, and a second clone.

   A script that calls an external tool is tested for its failure
   without the tool: the test runs it on an empty PATH and expects
   the message that names the tool and how it is installed. A test
   never runs on a live repository: a copy of the fixture, as a
   throwaway repository where the test needs git, and nothing else.
   Enough to catch what a change of the script breaks, never a suite
   for its own sake.

8. Name the script in the layout comment of `CLAUDE.md`, on the
   `scripts/` line of Repository layout, with one clause on what it
   does, in the place its kind has there.

## Prove it

Run the tests from the engine root:

```
/test
```

The sum comes back as pytest prints it. A red test is reported word
for word, the failing assertion included, and nothing is fixed on
that command's word: the fix is a round of its own, the script changed
with its test. `/test -k <word>` runs the tests whose name carries the
word, `/test tests/test_<concern>.py` one file and `/test -x` stops
at the first red test. Where pytest is not installed, the command
says so and names the one install a contributor needs beyond
`python`: `python -m pip install pytest`. How the command runs in
full is on [Run the tests](../use/run-the-tests.md).

Then run the check of the engine:

```
/check engine
```

Among what it verifies: every file in `scripts/` is described in the
layout comment of `CLAUDE.md`, and nothing described there is missing
on disk. A script without its clause, or a clause without its script,
is a finding.

## Record and release

Record the change and release it as [Make a change to the
forge](how-a-change-is-made.md) says. A release of the engine runs
`/test` as its first step, before any check, and a red test stops
it. `/save` never runs the tests. The same suite runs in CI at every
push and pull request, on Linux and Windows, on Python 3.8 and the
newest.

## A worked example

You add `scripts/forge-example.py`, a script that reads one project
and prints one line about it. Its docstring, at the top of the file,
has the four parts:

```
forge-example.py - one line on the state of a project.

SYNOPSIS
    python scripts/forge-example.py <slug | path>

WHAT IT DOES
    Read-only, changes nothing. Reads the project file of the project
    named and prints its name, its kind and its language on one line.
    Refuses a directory that is not a project and says so.

WHAT IT NEEDS
    Python 3.8 or newer. `forge_repos.py` beside it.

EXAMPLES
    python scripts/forge-example.py my-project        # a project by its slug
    python scripts/forge-example.py ../fixture-copy   # a project by its path
```

The script takes the project through `forge_repos.project_path`, so
that `my-project` means `projects/my-project` and `../fixture-copy`
means that directory as given. It writes no file; if it did, the
file would go to `tmp/`.

Its test is `tests/test_forge_example.py`, one file for the one
concern. In words: the test takes `project`, a copy of the fixture in
a temporary directory, and runs the script on it through
`run_script`, passing the copy by its path, as the forge would run
it from the engine root. It asserts that the line printed carries the
name, the kind and the language the fixture's project file gives. A
second case runs the script on a directory that is no project and
asserts the refusal. Had the script called an external tool, a third
case would run it on an empty PATH and assert the failure that names
the tool and how it is installed. No case touches a repository of the
forge or a project under `projects/`.

The last change is one clause on the `scripts/` line of the layout
comment in `CLAUDE.md`: `forge-example (one line on a project)`.
Then `/test` and `/check engine`, and the change is recorded and
released as any other.

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

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
