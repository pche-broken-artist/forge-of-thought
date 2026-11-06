---
project: forge
title: Tests of the scripts and a CI run
author: PCHe
version: 0.1
status: draft
---

<!-- Only this header is fixed; the text below it is free-form. The
rules: its definition, `.claude/skills/forge/states/brief.md`; the
history companion:
templates/history.md. -->

## What prompted it

The engine carries some 7 000 lines of Python in `scripts/` and not
one test in the tree. The only test there is lives inside the git
hook as a self-test of its own. The fixture project on which the
merge and the migration were tried lies in `tmp/`, outside git. No
CI runs but the Pages build. The reading of the repository from
GitHub named this first among what is at risk (THR.0790).

## What is wanted, and why

Tests, so that a change of a script does not break what worked.
That is the one reason. The scripts change little and the forge is
not a development project, so the tests are to be in proportion:
enough to catch what a change breaks, never a suite for its own
sake.

## Where the tests live

In the engine, beside the scripts they test: a `tests/` directory at
the engine root, the fixture project the tests need inside it, never
in `projects/`. Everyone who clones the engine gets them; a user who
only works with the engine never runs them and installs nothing for
them. The thinking about the tests, this brief and the positions
that come of it, stays in the forge's own project. Test and script
change in one step, and a pull request on a script carries its test;
that is possible in one repository only, and CI runs where the code
is. CONTRIBUTING says both: a script is changed with its test, and
whoever wants to understand why the engine is as it is, or to
propose a change of its intent, clones the forge's own project. The
project is not a condition for running the tests.

## What is tested, in what order

The scripts have two layers. The deterministic cores read files and
call nothing: the front-matter, the records of a history, the
ledger, the judgement of the hook over a command, the documentation
map. The outer layer reaches out: git, pandoc, markitdown, the model
through `claude`.

The cores first: that is where most mistakes of a change arise, a
test of them is cheap and runs anywhere. The mechanics of the suite
are made on them. The git layer second, on the fixture, in a
throwaway repository in a temporary directory. What calls pandoc,
markitdown or the model is not tested; only that the script fails
intelligibly without the tool.

## How the tests run

With pytest, from the engine root: `python -m pytest`. Pytest is the
one thing a contributor installs beyond `python`; the rule that
`python` on PATH is the one prerequisite of the scripts stays
untouched, the tests are not the scripts. The principal runs them
the same way on his machine, with no GitHub in between.

The built-in cases of the git hook, some 150 commands with their
verdict allow, ask or deny, become the first test of the suite: the
test loads the hook's judgement and walks the same cases. The hook
loses its `--test` flag and its cases; one place for tests.

## CI

GitHub Actions over the engine, at every push and pull request, on
Linux and Windows, Python 3.8 and the newest. The portability rule
of CLAUDE.md, Persistence, becomes a run instead of a writing rule.
macOS is not in the matrix until someone asks for it.

## Release and save

A release runs the tests locally; a red test stops it, as a red test
before a release already does for the collaboration (POS.1760).
Where pytest is missing, the release says the tests did not run and
goes on only on the principal's word. A save does not run them: a
save is quick, and every push runs CI anyway.

## What not

No coverage figure as a target: kind, not count. No test of what
pandoc, markitdown or the model return, beyond the failure without
them. No test of the skills, the agents or the text of CLAUDE.md:
those are the checks' and the reviewers'. Never a test on a live
repository: on the fixture or in a temporary directory only
(DEC.0240).

## Order

The brief first, then the build in pieces: the mechanics of the
suite on the hook's cases and a few cores, then CI, then the git
layer on the fixture. The intent and the solution design are mined
from the finished and debugged whole, not written ahead of it
(POS.1780). Nothing of this brief is a position yet.

## Open

- What the fixture project in `tests/` carries: made new and
  minimal, or taken from the fixture in `tmp/`.
- Whether the README shows the CI badge; the README is a render, so
  that is its recipe's.
- The exact place of the sentence on tests in CONTRIBUTING, a render
  of its recipe too.
