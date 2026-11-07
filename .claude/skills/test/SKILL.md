---
description: Run the engine's tests — pytest over tests/, the sum back, a red test as pytest printed it; nothing fixed, nothing written
argument-hint: "[pytest arguments]"
---

Run the engine's tests (projects/forge/00-brief-tests.md): from the
engine root, `python -m pytest -q $ARGUMENTS`. The tests are the
engine's, beside the scripts they test, in `tests/`; a project has
none, so this command takes no slug. What is given is passed to
pytest as it stands: `/test` runs the whole suite, `/test -k
conflict` the tests whose name carries the word, `/test
tests/test_git_scripts.py` one file, `/test -x` stops at the first
red test.

Report the sum as pytest prints it (`221 passed in 31s`). A red test
is reported word for word as pytest printed it, the failing
assertion included, and nothing is fixed on this command's word: the
fix is a round of its own, the script changed with its test. The
tests run on copies of the fixture `tests/fixture` in a temporary
directory and on no repository of the forge (DEC.0240); nothing of
the engine or of a project changes.

Where pytest is not installed (`No module named pytest`), say that
the tests did not run and how to install the one thing a contributor
needs beyond `python`: `python -m pip install pytest`. The same
suite runs in CI at every push (`.github/workflows/tests.yml`), on
Linux and Windows, Python 3.8 and the newest; what `/release` does
with a red test is its own (`.claude/skills/release/SKILL.md`), and
`/save` never runs them (`.claude/skills/save/SKILL.md`).
