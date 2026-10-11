---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: f383b1e926aff1c3
inputs:
  - scripts/forge-branch.py
---

# Work on a branch

This page shows how to switch a repository to a branch, or to report
which branch it is on, without typing git. It is for the principal
(the person whose thinking is forged) who wants a branch. Branches
are voluntary: whoever does not want one works on `main` and never
meets this page.

## When to use it

- You want to work apart from `main` and come back to it later.
- You want to know which branch a repository is on and which
  branches it has.

## The command

```
python scripts/forge-branch.py <slug> <branch>
```

The slug names the repository. The word `forge` means the engine.
There is no form without a slug, because switching every repository
at once is never what anyone wants.

Two other forms exist:

- `python scripts/forge-branch.py <slug>` reports the branch the
  repository is on and lists its branches.
- `python scripts/forge-branch.py <slug> main` switches back to
  `main`.

## What happens

1. You name the repository, and a branch if you want to switch. The
   script reads the branch the repository is on.
   You should now see the repository's name and "on branch" with the
   branch, when you gave no branch name. A second line lists the
   branches when the repository has more than one.
2. When you named the branch the repository is already on, nothing
   changes.
   You should now see "already on" with that branch.
3. When you named another branch, the script first looks for unsaved
   changes. Unsaved changes stop the switch, so that nothing is
   carried across or lost.
   You should now see either the stop message or the next step.
4. When the branch exists, the script switches to it.
   You should now see "switched to" with the branch.
5. When the branch does not exist, the script creates it from the
   current state and switches to it.
   You should now see "created" with the branch, "from" with the
   branch you left, and a second line saying the branch reaches the
   remote with the first save made on it.

## What you have afterwards

The repository is on the branch you named. Your next save is made on
that branch. A new branch reaches the remote by the first save made
on it, as [Save your work](save-your-work.md) describes. Merging,
deleting and pushing branches stay with git, and a release is made
from `main` only. [Persistence in git](../about/persistence-in-git.md)
says why merging is left to git.

## If something goes wrong

- The repository has unsaved changes: the script stops and prints
  that the repository has unsaved changes, with the number of files,
  and asks you to save first. Save, then switch again.
- The project does not exist: the script prints that the project was
  not found. Check the slug.
- The folder is not a repository: the script prints that there is
  nothing to switch.
- The current branch cannot be read, or the switch or the creation
  fails: the script prints that it could not read, switch or create.
  Nothing else is said.

## A worked example

You want to work apart from `main` in the repository `<slug>`.

```
python scripts/forge-branch.py <slug>
```

You should now see that the repository is on branch `main`.

```
python scripts/forge-branch.py <slug> <branch>
```

You should now see that `<branch>` was created from `main` and the
repository switched to it. Work and save as usual. When you want to
return:

```
python scripts/forge-branch.py <slug> main
```

You should now see that the repository switched to `main`.

## See also

- [Save your work](save-your-work.md): the save that carries a
  branch to the remote.
- [Persistence in git](../about/persistence-in-git.md): why merging
  is left to git.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
