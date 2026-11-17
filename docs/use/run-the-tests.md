---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 57699a60800729eb
inputs:
  - .claude/skills/test/SKILL.md
  - .claude/skills/release/SKILL.md
  - .claude/skills/save/SKILL.md
  - pytest.ini
  - .github/workflows/tests.yml
---

# Run the tests

`/test` runs the engine's tests and reports the result as pytest prints
it. This page is for an extender who has changed a script and for a
user who wants to know the engine still works.

## When to use it

Use it after you change a script, and before you hand the change on. A
release of the engine runs the tests for you; a save never does.

## The command

```
/test
```

Whatever you give after `/test` goes to pytest as it stands:

- `/test` runs the whole suite.
- `/test -k conflict` runs the tests whose name carries the word.
- `/test tests/test_git_scripts.py` runs one file.
- `/test -x` stops at the first red test.

The command takes no project slug. The tests belong to the engine and
lie beside the scripts they test, in `tests/`; a project has none.

## What happens

1. Claude runs `python -m pytest -q` from the engine root, with your
   arguments added. pytest reads `pytest.ini`, which points it at
   `tests/` and puts `scripts/` on the import path.
   You should now see pytest's progress lines.
2. The tests run on copies of the fixture `tests/fixture` in a
   temporary directory. They touch no repository of the forge, so
   nothing of the engine or of a project changes.
   You should now see no change in `git status`.
3. Claude reports the sum as pytest prints it, a line of the shape
   "N passed in M s".
   You should now see that line.

## What you have afterwards

The sum, and nothing else. No file is written and nothing is fixed.

A red test is reported word for word as pytest printed it, the failing
assertion included. Nothing is fixed on the word of this command. The
fix is a round of its own, in which the script is changed together
with its test.

## If something goes wrong

- pytest is not installed. The output says `No module named pytest`,
  and Claude says that the tests did not run. A contributor needs one
  thing beyond `python`: `python -m pip install pytest`.
- A test is red. See the worked example below.

## Where else the tests run

- CI runs the same suite at every push and pull request, on Linux and
  Windows, with Python 3.8 and the newest Python.
- A release of the engine runs the tests before any check or agent, and
  a red test stops the release. A release of a project runs none. See
  [Release a version](release-a-version.md).
- A save never runs them. See [Save your work](save-your-work.md).

What is tested and how the fixture is made is explained in
[The tests](../about/the-tests.md). Changing a script together with its
test is described in [Add a script](../extend/add-a-script.md). Terms of
the forge are in the [Glossary](../reference/glossary.md).

## A worked example

A green run:

```
/test
```

```
NNN passed in M.Ms
```

A red test, in the shape pytest prints it (the names are placeholders):

```
/test -x
```

```
FAILED tests/test_<script>.py::test_<name> - assert <actual> == <expected>
1 failed, N passed in M.Ms
```

Above the `FAILED` line pytest prints the test's source and the failing
assertion; Claude reports all of it unchanged. You then fix the script
and its test in a round of their own and run `/test` again.

## See also

- [The tests](../about/the-tests.md): what is tested, what the fixture is and why the tests are in proportion.
- [Release a version](release-a-version.md): the release that runs the tests first.
- [Save your work](save-your-work.md): the save, which never runs them.
- [Add a script](../extend/add-a-script.md): changing a script with its test.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
