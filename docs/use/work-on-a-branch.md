---
generated: 2026-10-23
version: 5.33
made: mirrored
inputs-hash: dc0f46e9d05b99c1
inputs:
  - scripts/forge-branch.py
  - .claude/skills/release/SKILL.md
---

# Work on a branch

This page shows how to switch a repository to a branch, or back to `main`, without typing git. It is for anyone who wants a branch of their own. The principal (the person whose thinking is forged) and any contributor can use it. Branches are voluntary: whoever does not want one works on `main` and never meets this script.

For the terms of the forge, see the [Glossary](../reference/glossary.md).

## When to use it

- You want to work on a change apart from `main`, and keep `main` as it is until the change is ready.
- You are a contributor, and your branch is how your work reaches the integrator (see [Working together on one project](../about/working-together.md)).
- You want to know which branch a repository is on.

## The command

```
python scripts/forge-branch.py <slug> <branch>
```

The slug names the repository. The slug `forge` means the engine itself. There is no form without a slug, because switching every repository at once is never wanted.

Three forms of the same command:

- `python scripts/forge-branch.py <slug> <branch>` switches to the branch, and creates it when it does not exist.
- `python scripts/forge-branch.py <slug> main` switches back to `main`.
- `python scripts/forge-branch.py <slug>` reports the branch the repository is on and lists the branches it has.

A real line that can be typed as it stands, to ask which branch the engine is on:

```
python scripts/forge-branch.py forge
```

## What happens

1. The script finds the repository. If the slug names no project, or the project is not a repository, the script stops and says so.
   You should now see the repository's name and its current branch, if you gave no branch name.
2. If you named the branch the repository is already on, nothing changes.
   You should now see "already on" and the branch name.
3. If the repository has unsaved changes, the script stops. Save first, then switch, so that nothing is carried across or lost.
   You should now see a message that the repository has unsaved changes, with the count of files and the save command to use.
4. If the branch exists, the script switches to it.
   You should now see "switched to" and the branch name.
5. If the branch does not exist, the script creates it from the current state and switches to it.
   You should now see "created" and the branch name, and a line saying the branch reaches the remote with the first save made on it.

## What you have afterwards

- The repository stands on the branch you named. Your work from now on is saved on that branch.
- A new branch exists only on your machine until you save on it. The first save made on it carries it to the remote. How a save works is on [Save your work](save-your-work.md).

## What stays with git

The script does two things only: it switches, and it reports. It does not do the rest.

- Merging a branch into `main` is done by hand or by merge request. The reason is on [Persistence in git](../about/persistence-in-git.md).
- Deleting a branch stays with git.
- Pushing a branch is done by the first save made on it, not by this script.
- A release is made from `main` only. On any other branch it stops and tells you which branch the repository is on and how to get back: save, then switch to `main` with the command above.

## If something goes wrong

- "has unsaved changes": save the repository, then run the command again.
- "is not a repository": the slug names a project that is not under git, so there is nothing to switch.
- "Project ... not found": the slug names no project. Check it.
- "Could not switch" or "Could not create branch": git refused the switch or the creation. The script gives no further reason.

## A worked example

You want a branch for a change in the repository `<slug>`, and then to return to `main`.

```
python scripts/forge-branch.py <slug>
python scripts/forge-branch.py <slug> <branch>
python scripts/forge-branch.py <slug> main
```

1. The first line reports `main` as the current branch.
2. The second line creates `<branch>` from `main` and switches to it. You work and save there. The first save carries `<branch>` to the remote.
3. The third line switches back to `main`. If you had unsaved changes, it would have stopped, and you would save first.

## See also

- [Save your work](save-your-work.md): the save that carries a branch to the remote.
- [Persistence in git](../about/persistence-in-git.md): why merging is left to git.
- [Working together on one project](../about/working-together.md): how a contributor's branch reaches the integrator.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.33 from the files the front-matter names; never edited by hand.
