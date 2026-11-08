---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 60f1c167b55e20fb
inputs:
  - projects/forge/10-intent.md#POS.1930
  - projects/forge/10-intent.md#POS.1940
  - projects/forge/10-intent.md#POS.1950
  - projects/forge/10-intent.md#POS.1960
  - projects/forge/10-intent.md#REJ.0510
  - projects/forge/10-intent.md#REJ.0520
  - projects/forge/10-intent.md#REJ.0530
  - projects/forge/40-solution-design.md#SOL.0900
  - projects/forge/40-solution-design.md#SOL.0830
  - pytest.ini
  - .github/workflows/tests.yml
  - templates/project.md
---

# The tests

The tests are the engine's own check that its scripts still do what
they are meant to do after a change. This page is for the extender
who changes a script and for the evaluator who wants to know what is
covered, what the tests run on and why they stop where they stop. It
says what the tests are, how they are built and run, and the reasons
behind their shape; how to run them is the how-to
[Run the tests](../use/run-the-tests.md).

## What it is

The engine's scripts have tests. They live in `tests/` at the engine
root, beside the scripts they test, and pytest runs them from the
engine root. `/test` is the one door to them. The command it runs is
`python -m pytest`, with any arguments passed through.

pytest is the one thing a contributor installs beyond `python`. A
user of the engine never runs the tests and installs nothing for
them.

The tests are in proportion. They are enough to catch what a change
of a script breaks. They are never a suite for its own sake, and no
coverage figure is a target: the rule of the forge is kind, not
count. A script is changed with its test, and a pull request on a
script carries it; how that is done is
[Add a script](../extend/add-a-script.md).

The tests never run on a live repository. What they run on is a
synthetic fixture (below), copied for every test.

## How it works

### What is tested

The tests cover the scripts in the order they were built, the
deterministic cores first, then the scripts that write git:

- the front-matter of a document;
- the records of a history;
- the reader of the documentation map, that is the map of pages
  the documentation is made from;
- the git hook's judgement over a command, whether a command reads
  git or writes it;
- the ledger, the state report made at read time from a project's
  documents, every table of it;
- the light check as a program: the fixture conforming, and planted
  defects found;
- the git scripts on the fixture: status, save, branch and pull;
  the step of a conflict standing and then finished; a standing
  rebase refused; a derived file taken as ours where the merge
  driver is registered, and left in conflict where it is not; a
  merge made by hand pushed as it stands, from the integrator's
  side and from the contributor's.

The git hook's built-in cases became the first test, and the hook's
own test flag went, so that tests live in one place.

What calls pandoc, markitdown or the model is tested for its failure
without the tool alone: the script is run with the tool absent and
must name the tool and how it is installed. What those tools return
is not tested.

Not tested, by choice:

- the skills;
- the agents;
- the text of `CLAUDE.md`, the core of the forge's rules;
- the run of the screenplay script `scripts/md2video.py`.

### The fixture

The fixture, `tests/fixture`, is a synthetic thought project of the
current shape with a made-up subject. It holds one of each kind of
document the scripts read:

- a project file marked `fixture: true`, the flag
  `templates/project.md` reserves for a fixture project;
- the attributes file and the ignore file from the templates;
- a brief and an intent with their history companions, the intent at
  a second version with one earlier wording recorded;
- a thread open and one closed;
- a decisions file with one verdict;
- a critique with findings, one settled by a record and one rejected
  by a verdict;
- a challenge with one open challenge;
- a source with its index, and an empty research index;
- a readme recipe with its companion, and the README as its render
  with provenance.

The histories and the indexes carry the skeletons' comments as they
stand. The fixture has no ledger: a test makes it. Its README says
that it is a test fixture and what it is for. It is never a copy of
a real project, and it never lies under `projects/`.

The fixture conforms to the light check. So a template it no longer
follows turns a test red, and that is the signal wanted: the fixture
is kept in step with the templates, or the suite says so.

A test never touches the fixture. It works on a copy in pytest's
temporary directory. Where the test needs git, the copy is made a
repository on `main` with a local identity, one commit, and a bare
origin beside it; where the test needs a second person, a second
clone of that origin stands for them.

### What the tests share

What the tests share lives in one file beside them,
`tests/conftest.py`:

- a script with a hyphen in its name loaded as a module without
  running its main;
- a script run as the forge runs it, `python scripts/<name>.py …`
  from the engine root, with an environment given;
- the copy of the fixture;
- git with an empty global configuration and no system one, and no
  terminal prompt;
- the copy as a repository with a bare origin, and a second clone.

The tests are one file per concern. `pytest.ini` names `tests/` as
the test path and puts `scripts/` on the import path, so that the
modules the scripts share import by name.

The scripts under test run as subprocesses, not by importing their
main. So what is tested is the command as the forge calls it.

### A script takes a slug or a path

A script takes a project by its slug or by the path of its
directory. A bare word is a slug and means `projects/<slug>`.
Anything with a separator, or an absolute path, is the directory
itself, taken as given. The project's name is the `project` field of
its project file, or the directory's name where the file has none;
`forge` stays the engine's own project by that name. One resolver in
`scripts/forge_repos.py` does this, and every script goes through it.
The commands of the forge call by slug as before.

This is what lets a test reach the copy in a temporary directory: by
its path, as an argument visible in the command, and by nothing
else.

### Continuous integration

The same suite runs in CI at every push and every pull request of
the engine, from `.github/workflows/tests.yml`. The matrix is Linux
and Windows, Python 3.8 and the newest stable release, resolved at
each run. Each job installs pytest and runs `python -m pytest`; one
failing job does not stop the others. The run's token can read the
contents and nothing more. macOS is not in the matrix until someone
asks for it.

The git tests run git with an empty global configuration and no
system one. The identity is set in the throwaway repository alone.
So the user's guard, his stanzas and his registration of the merge
driver change nothing, and CI without any of them sees the same. The
registration is tested by its presence and by its absence.

### When the tests run

A release of the engine runs the tests before anything else, and a
red test stops it; the release is
[Release a version](../use/release-a-version.md). A save never runs
them: every push runs them in CI.

## Why

Thousands of lines of Python and not one test in the tree is the
first thing a contributor looks for, and the first thing a change
breaks. The tests exist so that a change of a script is caught where
it breaks something, and they stay in proportion so that the suite
never becomes work of its own.

The fixture is synthetic because real content does not belong in the
public engine. It lies in `tests/` and not under `projects/` because
`projects/` is gitignored, so a fixture there would reach neither a
contributor nor CI. The git tests change what they run on, so a copy
in a temporary directory is needed wherever the fixture lies; that
is why every test works on a copy and the fixture itself stays as it
is. A copy per test was chosen over one shared repository:
correctness, bought with a longer full run.

A script takes a path because a copy in a temporary directory is
reached by a path and by nothing else, and a path is an argument
like any other, visible in the command. Two alternatives were
weighed and dropped. An environment variable naming the projects'
root would be a setting hidden from the command, where a path is an
argument everyone sees. A branch in the scripts for a test project
would be production code with a path only the tests take; and since
the copy the tests work on lies in a temporary directory, not in
`tests/`, the branch would be the variable in another coat.

The tests run in CI on two systems and two versions of Python so
that the portability rule of the engine, that the scripts run
unchanged on Linux and macOS, becomes a run instead of a writing
rule; the rule is [Persistence in git](persistence-in-git.md). The
git tests read nothing of the machine because a test that depends
on the machine it runs on tests the machine.

pytest was chosen over unittest as the convention of the language
and the one install. The scripts run as subprocesses so that what is
tested is the command as the forge calls it, not a function behind
it. A script is changed with its test because that is possible in
one repository only, and CI runs where the code is.

## A worked example

A test of the save script, in words. The test asks for the copy of
the fixture as a repository: the fixture is copied into a temporary
directory, the copy is made a repository on `main` with a local
identity and one commit, and a bare origin is created beside it. The
test changes one document in the copy. It then runs
`python scripts/forge-save.py <path-of-the-copy>` from the engine
root, as the forge would run it, with git pointed at an empty global
configuration. The test reads what the script printed and what the
bare origin now holds: the commit is there, and the script said what
it saved. The fixture under `tests/` is unchanged, and the temporary
directory goes with the run. The same test gives the same answer on
a contributor's machine, with or without the user's own git
configuration, and in CI on Linux and Windows.

## See also

- [Run the tests](../use/run-the-tests.md): running `/test`.
- [Add a script](../extend/add-a-script.md): changing a script with
  its test.
- [Persistence in git](persistence-in-git.md): the portability rule
  the tests make a run.
- [Release a version](../use/release-a-version.md): the release that
  runs the tests first.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
