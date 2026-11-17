---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 90025db078a54169
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

The tests are files of test code in `tests/` at the root of the engine
(the repository that holds the forge's scripts): they run the scripts
on a made-up project and show whether a change broke one of them. This
page explains what the tests cover, what the fixture they run on is,
and why they are kept in proportion and are not complete. It is
written for a reader who extends the engine and for a reader who
evaluates it. Every term of the forge used here has its line in the
[Glossary](../reference/glossary.md).

## What it is

The scripts of the engine have tests. The tests lie in `tests/` at the
engine root, beside the scripts they test. There is one place for
tests: no script carries tests of its own.

pytest runs the tests from the engine root. The file `pytest.ini` at
the root names `tests` as the place of the tests and puts `scripts` on
the import path. The modules that several scripts share are therefore
imported by name.

The command `/test` is the one way to run the tests: the one door to
them. It runs `python -m pytest` and passes its arguments through.
[Run the tests](../use/run-the-tests.md) shows the command in use.

pytest is the one thing a contributor installs beyond `python`. A user
of the engine never runs the tests and installs nothing for them.

The tests are kept in proportion:

- enough to catch what a change of a script breaks
- never a suite for its own sake
- no coverage figure as a target

A script is changed with its test, and a pull request on a script
carries the test with it.
[Add a script](../extend/add-a-script.md) covers that change. No test
runs on a live repository.

## How it works

### What is tested

What is tested is listed here in the order it was built. The
deterministic cores came first:

- the front-matter (the header of a file)
- the records of a history
- the reader of the documentation map
- the git hook's judgement over a command
- the ledger made from the documents (the ledger is the file that
  states the state of a project)
- the light check as a program (the light check reads whether the
  files of a project follow their templates)

The git scripts came next, run on the fixture:

- status, save, branch and pull
- the step of a conflict, while the conflict stands and once it is
  finished
- a standing rebase, which is refused
- the derived file, taken as ours where the merge driver is
  registered and left in conflict where it is not
- a merge made by hand, pushed as it stands
- what the word `forge` names in the commands of git: the engine and
  the forge's own project beside it

The last of these runs on a throwaway engine (an engine made for the
test, as a repository with a bare origin). It covers what `forge`
names before the cut of the forge's own project and after it.

A script that calls an outside tool (pandoc, markitdown or the model)
is tested for one thing alone: its failure without the tool. The
script must fail and name the tool.

Not tested:

- what pandoc, markitdown and the model return
- the skills
- the agents
- the text of `CLAUDE.md`
- the run of the screenplay script (`md2video`)
- the migration of a project of an older shape

For the migration the reason is given: a fixture of the current shape
gives it nothing to migrate. For the rest the reason is not recorded.

The tests are kept as one file per concern.

### The fixture

The fixture is `tests/fixture`: a synthetic thought project (a project
of the kind `thought`) of the current shape, with a made-up subject.
It holds one of each kind of document the scripts read:

- the project file `project.md`, which carries `fixture: true` and by
  that marks the project as a fixture
- the attributes file and the ignore file, taken from the templates
- a brief and an intent, each with its history companion (the intent
  has two versions)
- a thread that is open and one that is closed
- a decisions file with one verdict
- a critique and a challenge
- a source with its index
- an empty research index
- a recipe with its history companion, and the README as its render

The fixture has no ledger: a test makes one. Its files carry the line
that names their template. Its README says that it is a test fixture
and what it is for. The fixture is never a copy of a real project and
never lies under `projects/`.

A test never touches the fixture. It works on a copy:

```
tests/fixture                         never changed by a test
     |
     |  copied, once per test
     v
<temporary directory>/<copy>          reached by the scripts by its path
     |
     |  only where the test needs git
     v
the copy as a repository on main  <-->  a bare origin beside it
     |
     |  only where the test needs a second person
     v
a second clone, as another person's
```

- Each test gets a copy of its own in pytest's temporary directory.
- Where a test needs git, the copy is made a repository on `main`
  with a local identity, one commit and a bare origin beside it (a
  bare repository that plays the remote).
- Where a test needs two people, a second clone stands for another
  person's.
- The scripts reach the copy by its path.

The fixture conforms to the light check. A template that the fixture
no longer follows therefore turns a test red. That is the signal
wanted. The price is a fixture kept by hand to the templates; the test
of the light check on the fixture enforces it.

### What the tests share

What the tests share lives in one file beside them,
`tests/conftest.py`:

- a script with a hyphen in its name, loaded as a module without
  running its main
- a script run as the commands of the forge run it:
  `python scripts/<name>.py` from the engine root, with an environment
- the copy of the fixture
- git with an empty global configuration, no system configuration and
  no terminal prompt
- the copy as a repository with a bare origin, and a second clone
- a throwaway engine as a repository with a bare origin

### A project by its slug or by its path

A script takes a project by its slug (the short name of the project)
or by the path of its directory:

- a bare word is a slug and means `projects/<slug>`
- anything with a separator, or an absolute path, is the directory
  itself, taken as given

```
python scripts/<name>.py <slug>
python scripts/<name>.py <path of the copy>
```

This holds for every script alike. The commands of the forge go on
calling by slug. A test passes the path of its copy, and the copy is
visible in the command.

The name of a project is the `project` field of its project file.
Where a directory has no project file, the name is the name of the
directory. `forge` stays the engine's own project by the name.

### CI and the machine

CI (continuous integration: the suite run on hosted machines) runs the
same suite as `python -m pytest` on a contributor's machine:

- at every push and every pull request of the engine
- on Linux and on Windows
- with Python 3.8 and with the newest stable Python, looked up anew at
  each run
- not on macOS until someone asks for it

Each pair of system and Python is a run of its own, and a failing run
does not stop the others. A run installs pytest and runs
`python -m pytest`. The token of a run may read the contents of the
repository and nothing more. The workflow is
`.github/workflows/tests.yml`.

A test reads nothing of the git configuration of the machine it runs
on. The git tests run with an empty global configuration and no system
one. The identity is set in the throwaway repository alone. The guard,
the stanzas and the registration of the merge driver that a user has
in his own git configuration therefore change nothing. CI has none of
them and sees the same. The registration is tested by its presence and
by its absence.

### Release and save

A release of the engine runs `/test` as its step 1a.
[Release a version](../use/release-a-version.md) describes that
release. A save never runs the tests. Every push runs them in CI.

## Why

**Tests at all.** A tree of scripts without one test is the first
thing a contributor looks for. It is also the first thing a change
breaks.

**In proportion.** The tests are there to catch what a change of a
script breaks. The rule behind the proportion is kind, not count: what
matters is the kind of break a test catches. A coverage figure would
be a count.

**In the engine, in one place.** A script is changed with its test,
and a pull request on a script carries both. That is possible in one
repository only. CI runs where the code is.

**pytest, and scripts run as commands.** pytest was chosen against
unittest: it is the convention of the language and the one install.
The scripts are run as subprocesses, and their main is not imported.
What is tested is then the command as the commands of the forge call
it.

**A synthetic fixture in the engine's tree.** Real content does not
belong in the public engine. The directory `projects/` is gitignored.
A fixture there would reach neither a contributor nor CI.

**A copy for each test.** The git tests change what they run on. A
copy in a temporary directory is needed wherever the fixture lies.
Each test gets a copy of its own and not one shared repository:
correctness is bought with a longer full run.

**A path, not a hidden setting.** A copy in a temporary directory is
reached by a path and by nothing else. A path is an argument like any
other, visible in the command. Two other ways were weighed and
dropped:

- An environment variable that names the root of the projects, read
  by the scripts for the tests. It would be a setting hidden from the
  command, where a path is an argument everyone sees.
- A branch in the scripts for a test project lying in `tests/`. It
  would be production code with a path only the tests take. The copy
  a test works on lies in a temporary directory and not in `tests/`.
  The branch would therefore be the same hidden setting in another
  form.

**CI, and nothing of the machine.** The portability rule (the scripts
are to run on more than one operating system) becomes a run instead of
a writing rule. [Persistence in git](persistence-in-git.md) states the
rule. A test that depends on the machine it runs on tests the machine.

## A worked example

A test of the light check, told in words, shows the parts at work.

1. The test asks for a copy of the fixture. `tests/fixture` is copied
   into pytest's temporary directory, and the test receives the path
   of the copy.
2. The test runs the light check on the copy as the commands of the
   forge run it, with the path of the copy as the argument. The light
   check reports that the copy conforms.
3. The test plants a defect in the copy: it changes one file into
   something the light check is to object to.
4. The test runs the light check again. The light check must now find
   the planted defect. Where it does not, the test is red.
5. `tests/fixture` is as it was. Only the copy was changed, and the
   next test gets a copy of its own.

Step 2 turns red by itself where a template has changed and the
fixture has not followed it. That is the signal the fixture is kept to
give.

## See also

- [Run the tests](../use/run-the-tests.md): running `/test`.
- [Add a script](../extend/add-a-script.md): changing a script with
  its test.
- [Persistence in git](persistence-in-git.md): the portability rule
  the tests make a run.
- [Release a version](../use/release-a-version.md): the release that
  runs the tests first.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
