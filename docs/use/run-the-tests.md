---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: c17940fcbbd9b40e
inputs:
  - .claude/skills/test/SKILL.md
  - .claude/skills/release/SKILL.md
  - .claude/skills/save/SKILL.md
  - pytest.ini
  - .github/workflows/tests.yml
---

# Run the tests

This page shows how to run the engine's tests with `/test` and what you see when a test is red. It is for the extender who changes a script and for the user who wants to know the engine still works.

## When to use it

Use it after you change a script, to see that nothing broke. Use it also when you want to run one part of the suite, such as a single file or the tests that carry a word in their name.

The tests belong to the engine and sit beside the scripts they test. A project has none, so the command takes no slug. For what is tested and why, see [The tests](../about/the-tests.md).

## The command

```
/test
```

Whatever you give after the command goes to pytest as it stands. These forms work:

- `/test`: the whole suite.
- `/test -k conflict`: the tests whose name carries the word `conflict`.
- `/test tests/test_git_scripts.py`: one file.
- `/test -x`: the whole suite, stopping at the first red test.

## What happens

1. Claude runs `python -m pytest -q` from the engine root, with your arguments added. The file `pytest.ini` sets `tests/` as the path and puts `scripts/` on the import path.

   You should now see pytest's progress line, one dot for each test that passed.

2. The tests run on copies of the fixture `tests/fixture`, made in a temporary directory. They touch no repository of the forge.

   You should now see no change in the engine or in any project.

3. Claude reports the sum as pytest prints it.

   You should now see a line of the shape `N passed in M s`.

## What you have afterwards

You have the sum of the run and nothing else. Nothing of the engine or of a project has changed.

A red test is reported word for word as pytest printed it, the failing assertion included. Nothing is fixed on this command's word. The fix is a round of its own, in which the script is changed together with its test. For how a script is changed, see [Add a script](../extend/add-a-script.md).

## If something goes wrong

- pytest is not installed. The output says `No module named pytest`, and Claude says that the tests did not run. Install the one thing a contributor needs beyond `python`:

  ```
  python -m pip install pytest
  ```

  Then run `/test` again.

- A test is red. Read the failing assertion in the output. Fix the script and its test in a round of their own, then run `/test` again.

## Where else the tests run

The same suite runs in continuous integration at every push and every pull request. It runs on Linux and on Windows, with Python 3.8 and with the newest Python.

A release of the engine runs the tests before anything else, and a red test stops the release. See [Release a version](release-a-version.md).

A save never runs them. See [Save your work](save-your-work.md).

## A worked example

A run of the whole suite, with a placeholder sum:

```
/test
```

```
N passed in M s
```

A run with one red test has the shape pytest prints, here with placeholder names:

```
FAILED tests/test_<file>.py::test_<name> - assert <actual> == <expected>
1 failed, N passed in M s
```

Above the last lines pytest prints the test, the failing assertion and the values that differed. Claude reports all of it as it stands.

## See also

- [The tests](../about/the-tests.md): what is tested, what the fixture is and why the tests are in proportion.
- [Release a version](release-a-version.md): the release that runs the tests first.
- [Save your work](save-your-work.md): the save, which never runs them.
- [Add a script](../extend/add-a-script.md): changing a script with its test.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
