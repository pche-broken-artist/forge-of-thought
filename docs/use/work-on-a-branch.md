---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: f067258165941239
inputs:
  - scripts/forge-branch.py
  - .claude/skills/release/SKILL.md
---

# Work on a branch

This page shows how you switch a repository to a branch, or back to `main`, with one script and without typing git. It is for anyone who wants a branch of their own; whoever does not works on `main` and never meets the script.

## When to use it

Use it when you want to work apart from `main`, for example on a change you are not ready to release. Branches are voluntary. The script does two things and nothing else: it switches the repository to a branch, and it reports which branch the repository is on.

## The command

```
python scripts/forge-branch.py <slug> <branch>
```

- `<slug>` names the repository. The word `forge` means the engine itself. There is no form without a slug, because switching every repository at once is never what anyone wants.
- `<branch>` is the branch to switch to. If it does not exist, the script creates it from the current state. `main` switches back.

With the slug alone, the script reports the branch the repository is on and lists the branches it has:

```
python scripts/forge-branch.py forge
```

## What happens

1. The script finds the repository. You should now see no error; if the slug is not a project, or the project is not a repository, the script stops and says so.
2. It reads the current branch. If you gave no branch, you should now see "on branch" followed by the current branch, and, when there is more than one, a line "branches:" listing them.
3. If you named the branch you are already on, you should now see "already on" that branch, and nothing changes.
4. If the repository has unsaved changes, the script stops. Save first, then switch, so that nothing is carried across or lost.
5. If the branch exists, the script switches to it. You should now see "switched to" the branch.
6. If the branch does not exist, the script creates it from the branch you were on and switches to it. You should now see "created" the branch "from" the previous one "and switched to it", and a second line saying that the branch reaches the remote with the first save made on it.

## What you have afterwards

The repository stands on the branch you named. Nothing has been sent to the remote. A new branch reaches the remote by the first save you make on it (see the page on saving).

Merging, deleting and pushing branches stay with git. A merge into `main` is done by hand or by merge request. A release, a documentation run and a publish are made from `main` only; on any other branch they stop and tell you which branch the repository is on and how to get back, which is the command above with `main`, after saving.

## If something goes wrong

- "has unsaved changes": the repository has changes that are not saved. Save first with the save command, then switch again.
- "not found": the slug names no project. Check the slug; `forge` is the engine.
- "is not a repository - nothing to switch": the project is not under git, so it has no branches.
- "Cannot read the current branch": the script could not read the branch of the repository.
- "Could not switch" or "Could not create branch": git refused the switch or the new branch. The script gives no further reason.

## A worked example

You want to leave `main` for a branch of your own, work there, and come back.

```
python scripts/forge-branch.py <slug> <branch>
```

You should see that `<branch>` was created from `main` and that you are on it. Work and save as usual. The first save made on the branch sends it to the remote. When you want to return:

```
python scripts/forge-branch.py <slug> main
```

You should see "switched to main". If the script instead says there are unsaved changes, save and run it again.

## See also

- [Save your work](save-your-work.md): the save that carries a branch to the remote.
- [Persistence in git](../about/persistence-in-git.md): why merging is left to git.
- [Working together on one project](../about/working-together.md): how a contributor's branch reaches the integrator.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
