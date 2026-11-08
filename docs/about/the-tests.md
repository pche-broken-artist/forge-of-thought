---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 973c753fd9336d8a
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

The tests are the engine's own proof that its scripts still do what
they say after a change. This page is for the extender who changes a
script and for the evaluator who wants to know what the suite covers
and what it leaves alone: what the tests are, what fixture they run
on, how they reach it, where they run, and why they are kept in
proportion rather than made complete.

## What it is

The engine's scripts have tests. They live in `tests/` at the engine
root, beside the `scripts/` directory they test, and pytest runs them
from the engine root. `/test` is the one door to them; the command it
runs is `python -m pytest`, with whatever arguments are given passed
through. The running of them is described on
[Run the tests](../use/run-the-tests.md).

pytest is the one thing a contributor installs beyond `python`. A
user of the engine never runs the tests and installs nothing for
them.

The suite is in proportion. It is enough to catch what a change of a
script breaks. It is never a suite for its own sake, and no coverage
figure is a target. The rule behind this is the forge's "kind, not
count": a rule says what kind of content belongs, never a number.

A script is changed with its test, and a pull request on a script
carries it. How that is done is on
[Add a script](../extend/add-a-script.md).

## How it works

### What is tested

The tests were built in a fixed order, and the suite keeps it: the
deterministic cores first, then the scripts that write git, then the
conversions.

The deterministic cores are the parts of the scripts that read and
compute without touching git or an external tool:

- the front-matter of a document;
- the records of a history companion;
- the reader of the documentation map (the file the documentation
  pages are made from);
- the git hook's judgement over a command, that is, whether a command
  reads git or writes it;
- the ledger (the project's state, made at read time from its
  documents) built from the fixture, every table of it, the states
  taken from records and verdicts, and the write to its default
  place;
- the light check as a program: the fixture conforming, and planted
  defects found.

The git hook once carried its own built-in cases behind a flag. Those
cases became the first test file, and the flag went. The reason is
one place for tests.

Then the git scripts, on a copy of the fixture made into a
repository: status, save, branch and pull; the step of a conflict
left standing and then finished; a standing rebase refused; the
derived file taken as ours where the merge driver is registered and
left in conflict where it is not; a merge made by hand pushed as it
stands, from the integrator's side and from the contributor's. One
further file covers what the word `forge` names in the commands of
git: the engine and the forge's own project beside it, before the
cut of that project out of the engine and after it, run on a
throwaway engine that the test builds for itself. It covers the save
of two commits with the tag on the engine alone, the status of both,
the branch switched together or not at all, and the root render
found through its recipe.

What calls pandoc, markitdown or the model is tested for its failure
alone: each conversion script is run with an empty PATH and must
fail naming the tool it misses. What those tools return is not
tested.

Not tested, by design: the skills, the agents, the text of the core
instruction file, and the run of the screenplay script. A live
repository is never used.

### The fixture

The fixture is `tests/fixture`: a synthetic thought project of the
current shape with a made-up subject. It holds one of each kind of
document the scripts read: a project file, the attributes and the
ignore file from the templates, a brief and an intent with their
history companions, a thread open and one closed, a decisions file
with one verdict, a critique and a challenge, a source with its
index, an empty research index, a readme recipe with its companion
and the README as its render with provenance. The histories and the
indexes carry the skeletons' comments as they stand, so that the
light check finds nothing on it. It has no ledger: a test makes one.
Its own README says that it is a test fixture and what it is for.

The project file of the fixture carries `fixture: true`. The project
file skeleton, `templates/project.md`, names that flag as the mark
of a fixture project.

The fixture is never a copy of a real project, and it never lies
under `projects/`. A test never changes it: a test works on a copy
in pytest's temporary directory. Where the test needs git, the copy
is made a repository on `main` with a local identity, one commit and
a bare origin beside it; where two people are needed, a second clone
stands for the other person.

The fixture conforms to the light check. The cost of a synthetic
fixture is that it is kept by hand to the templates, and the light
check's test on it is what enforces that. So a template the fixture
no longer follows turns a test red, and that red test is the signal
wanted.

### What the tests share

What every test needs lives in one file beside them,
`tests/conftest.py`:

- a script loaded as a module without running its main, so that a
  script with a hyphen in its name can be tested from inside;
- a script run as the forge runs it, `python scripts/<name>.py …`
  from the engine root, with an environment;
- the copy of the fixture;
- git with an empty global configuration and no system one, and no
  terminal prompt;
- the copy as a repository with a bare origin, and a second clone;
- a throwaway engine as a repository with a bare origin, with the
  forge's own project inside it as the engine tracked it before the
  cut, and the cut run on it, the scripts pointed at it through the
  shared module's engine root.

`pytest.ini` at the engine root sets `tests` as the test path and
puts `scripts/` on the import path, so that the shared modules
import by name.

The scripts run as subprocesses, not by importing their main. So
what is tested is the command as the forge calls it. Each test gets
its own copy of the fixture rather than one shared repository; this
buys correctness at the price of a slower full run.

### How a test reaches its copy

A script takes a project by its slug or by the path of its
directory. A bare word is a slug and means `projects/<slug>`.
Anything with a separator in it, or an absolute path, is the
directory itself, taken as given. The project's name is the
`project` field of its project file, or the directory's name where
there is none. `forge` stays the engine's own project by that name.
One resolver in the shared module does this, and every script goes
through it. The commands of the forge call by slug as before.

So a copy in a temporary directory is reached by its path, and by
nothing else.

### Where they run

The same suite runs in CI at every push and every pull request of
the engine, through the workflow in `.github/workflows/tests.yml`:
on Linux and on Windows, on Python 3.8 and on the newest stable
release, resolved at each run. The workflow installs pytest and runs
`python -m pytest`, the same command a contributor types. The run's
token can read the repository and nothing more. macOS is not in the
matrix until someone asks for it.

The git tests run git with an empty global configuration and no
system one. The identity is set in the throwaway repository alone.
So the user's guard, his stanzas and his registration of the merge
driver change nothing, and CI without any of them sees the same. The
registration itself is tested both by its presence and by its
absence. The portability rule these tests turn into a run is on
[Persistence in git](../about/persistence-in-git.md).

A release of the engine runs the tests before anything else, and a
red test stops it; the release is on
[Release a version](../use/release-a-version.md). A save never runs
them. Every push runs them in CI.

## Why

A tree of scripts without one test is the first thing a contributor
looks for and the first thing a change breaks. That is why the
scripts have tests at all.

The suite is kept in proportion because the forge's rules say what
kind of content belongs, never a count. A coverage figure as a
target would be a count standing in for a judgement.

The fixture is synthetic because real content does not belong in
the public engine. It lies in the engine's tree because `projects/`
is gitignored, so a fixture there would reach neither a contributor
nor CI. A copy of a real project was weighed and dropped for the
same two reasons, and for a third: the git tests change what they
run on, so a copy in a temporary directory is needed wherever the
fixture lies. A bare remote in the engine's working folder was
weighed too, and dropped because it would be per machine.

A script takes a path because a copy in a temporary directory is
reached by a path and by nothing else, and a path is an argument
like any other, visible in the command. Two alternatives were
weighed and dropped. An environment variable naming the projects'
root would be a setting hidden from the command, where a path is an
argument everyone sees. A branch in the scripts for a test project
lying in `tests/` would be production code with a path only the
tests take; and because the copy the tests work on lies in a
temporary directory, not in `tests/`, the branch would be the
variable in another coat.

The tests run in CI so that the portability rule of the scripts
becomes a run instead of a writing rule. They read nothing of the
machine because a test that depends on the machine it runs on tests
the machine.

pytest was chosen over unittest because it is the convention of the
language and the one install. The scripts are run as subprocesses
so that what is tested is the command as the forge calls it.

A script is changed with its test, and a pull request carries both.
That is possible in one repository only, and CI runs where the code
is.

## A worked example

A test of the save script, in words. The test asks for the copy of
the fixture as a repository: pytest copies `tests/fixture` into its
temporary directory, makes the copy a repository on `main` with a
local identity and one commit, and puts a bare origin beside it. The
test then changes one file of the copy and runs the save script as
the forge runs it, `python scripts/forge-save.py` with the path of
the copy as its argument, under an environment in which git has an
empty global configuration and no system one. The test reads the
copy's log and the bare origin and finds the new commit in both. The
fixture in `tests/` is as it was before the test began, and nothing
of the machine the test ran on entered the result.

## See also

- [Run the tests](../use/run-the-tests.md): running `/test`.
- [Add a script](../extend/add-a-script.md): changing a script with
  its test.
- [Persistence in git](../about/persistence-in-git.md): the
  portability rule the tests make a run.
- [Release a version](../use/release-a-version.md): the release that
  runs the tests first.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
