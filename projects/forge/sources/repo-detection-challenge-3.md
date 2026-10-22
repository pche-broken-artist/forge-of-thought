origin: pasted into the conversation by the principal on 2026-10-22; written in Czech by Gemini in a session outside the forge, in a conversation the principal ran on his tasks, as a challenge of the operating layer Claude proposed for THR.0730 on 2026-10-22 (the scripts, shown as a block before it was applied); translated into English at registration on the principal's word, the wording kept as close as the translation allows, the code kept as it was
date: 2026-10-22

# Challenge of the operating layer for a project inside a larger repository

The proposal of the operating layer is excellently conceived and
holds the agreed architecture exactly. In analysing the code,
however, I came across one critical error in `docs-state.py` that
needs fixing before the application, so that the script does not take
every project outside git for a part of the engine's repository.

## 1. A critical error in `docs-state.py`

Problem: the proposal says for `docs-state.py`:

```python
proj = map_path.parent
repo = proj if fr.own_repo(proj) else fr.ENGINE_ROOT if fr.ENGINE_ROOT in map_path.parents else None
```

Since in the forge's architecture every project lies physically in
the directory `projects/<slug>` inside the engine's directory, the
path to the map of a project outside git (e.g.
`projects/fixture-nogit/docs-state.md`) has `ENGINE_ROOT` among its
parents (`map_path.parents`).

The condition `fr.ENGINE_ROOT in map_path.parents` evaluates to True
for absolutely every project in `projects/`. The result would be that
the project `fixture-nogit`, outside git, would get `repo =
fr.ENGINE_ROOT` (instead of None), and `docs-state.py` would try to
run `git log` over it in the engine's repository.

Fix: the rule of the fall-back to `ENGINE_ROOT` must hold only for
the documentation of the engine itself or of its own project
`projects/forge`. For any other project without a repository of its
own it must return None.

Corrected code for `docs-state.py`:

```python
proj = map_path.parent
is_engine = (proj.resolve() == fr.ENGINE_ROOT.resolve() or
             proj.resolve() == (fr.ENGINE_ROOT / "projects" / "forge").resolve())

if fr.own_repo(proj):
    repo = proj
elif is_engine and fr.own_repo(fr.ENGINE_ROOT):
    repo = fr.ENGINE_ROOT
else:
    print("none")
    return 0
```

## 2. A small note on `forge_repos.py` (`own_repo`)

In the helper `own_repo`:

```python
top = git_out(["rev-parse", "--show-toplevel"], path)
return bool(top) and Path(top.strip()).resolve() == Path(path).resolve()
```

I recommend adding `.strip()` to the output of `git_out`, so that a
clean string is passed on without the trailing newline that git
returns in its output.

## 3. A check of the other scripts

- `forge-status.py` and `forge-branch.py`: the exchange of
  `(path / ".git").exists()` for `fr.own_repo(path)` is readable and
  exact.
- `forge-migrate.py`: the handling of `under_git`, the omission of the
  git refusals, the change of step B (skipping `git rm --cached`) and
  the warning in the CLI correspond exactly to the specification
  SOL.0800 and POS.1740.
- `forge-ledger.py`: switching off the check of closed threads in the
  git log and setting `tracked = False` for projects outside git works
  without fault.

## 4. An assessment of the test procedure

The test scenario is complete and covers the whole range:

1. `forge-status.py` on the repositories of their own and on the
   engine.
2. The dry run of the migration and of the ledger on the engine.
3. `docs-state` on the engine's map.
4. The test on `fixture-nogit` (dry run, then `--apply`, then
   `ledger`, then the refusal of `--undo`, then a repeated `--apply`
   with "nothing to do").

A note on the test: after the test on `projects/fixture-nogit` is
finished, delete or tidy the directory away, so that it does not stay
in the engine's working tree.

## Verdict

With the fix in `docs-state.py` above and the small `.strip()` in
`own_repo`, the operating layer is ready for application. You have my
word for making the changes and running the tests!
