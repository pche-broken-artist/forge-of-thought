---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 4ca4dbb9bda19f90
inputs:
  - .claude/skills/test/SKILL.md
  - pytest.ini
  - .github/workflows/tests.yml
---

# Run the tests

`/test` is the command that runs the engine's tests and shows you the
result. It is for a contributor who has changed a script and for
anyone who wants to know whether the engine's tests pass on their
machine. Terms of the forge are explained in the
[Glossary](../reference/glossary.md).

## When to use it

Run it after you change a script, and before you hand the change on.
The tests are the engine's, kept in `tests/` beside the scripts they
test. A project has no tests of its own, so the command takes no
slug.

For what the tests cover, what the fixture is and why the suite is
kept in proportion, see [The tests](../about/the-tests.md).

## The command

```
/test
```

Whatever you add is passed to pytest (the Python test runner) as it
stands:

```
/test -k conflict
/test tests/test_git_scripts.py
/test -x
```

- `/test`: the whole suite.
- `/test -k conflict`: the tests whose name carries the word
  "conflict".
- `/test tests/test_git_scripts.py`: that one file.
- `/test -x`: the whole suite, stopping at the first red test.

## What happens

1. Claude runs `python -m pytest -q` from the engine root, with your
   arguments added. The file `pytest.ini` tells pytest to look in
   `tests/` and to put `scripts/` on the import path.

   You should now see pytest's own output scrolling by, in its quiet
   form.

2. Each test runs on a copy of the fixture `tests/fixture` (a small
   synthetic project) in a temporary directory. No repository of the
   forge is touched.

   You should now see no change in the engine or in any project.

3. Claude reports the sum as pytest prints it.

   You should now see a line of the shape `N passed in M s`.

## What you have afterwards

The sum, and nothing else changed: nothing of the engine or of a
project is written by this command.

## If something goes wrong

- A test is red. Claude reports it word for word as pytest printed
  it, the failing assertion included. It fixes nothing on the word of
  this command. The fix is a round of its own: the script is changed
  together with its test. See [Add a script](../extend/add-a-script.md).
- pytest is not installed. The output says `No module named pytest`,
  and Claude says that the tests did not run. The one thing a
  contributor installs beyond `python` is pytest:

  ```
  python -m pip install pytest
  ```

## Where else the tests run

- The same suite runs in CI (the automatic runs on the hosting
  service) at every push and every pull request, on Linux and
  Windows, with Python 3.8 and the newest Python.
- A release of the engine runs the tests before anything else, and a
  red test stops it. See [Release a version](release-a-version.md).
- A save never runs them. See [Save your work](save-your-work.md).

## A worked example

A run of the whole suite that passes:

```
/test
```

```
NNN passed in MM.MMs
```

A run in which one test is red ends with pytest's own report of it,
of this shape (the names here are placeholders):

```
================ FAILURES ================
______________ test_some_behaviour ______________

    def test_some_behaviour():
>       assert result == expected
E       AssertionError: assert 'got' == 'wanted'

tests/test_some_script.py:NN: AssertionError
======== 1 failed, NNN passed in MM.MMs ========
```

Claude shows this as it stands and stops there. The next step is a
change of the script and its test, as its own round.

## See also

- [The tests](../about/the-tests.md): what is tested, what the
  fixture is and why the tests are in proportion.
- [Release a version](release-a-version.md): the release that runs
  the tests first.
- [Save your work](save-your-work.md): the save, which never runs
  them.
- [Add a script](../extend/add-a-script.md): changing a script with
  its test.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
