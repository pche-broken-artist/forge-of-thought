---
generated: 2026-10-10
made: mirrored
inputs-hash: 7b9fb754cda01e37
inputs:
  - scripts/forge-branch.py
  - CLAUDE.md
---

# Work on a branch

This page is for a user who wants to work on a branch instead of on
`main`: it says how to switch to one, how to create one, how to come
back and what stays with git. Branches are voluntary. Whoever does not
want them works on `main` and never meets this.

## Switch to a branch or create it

Run the script with the repository's slug and the branch name:

```
python scripts/forge-branch.py <slug> <branch>
```

`forge` as the slug means the engine itself; any other slug is a
project. The script does one of two things:

- If the branch exists, it switches the repository to it and says it
  switched.
- If the branch does not exist, it creates it from the current state,
  switches to it and says so. It adds that the branch reaches the
  remote with the first save made on it.

If the repository is already on that branch, the script says so and
changes nothing.

To come back, name `main` as the branch:

```
python scripts/forge-branch.py <slug> main
```

There is no form without a slug: the script never switches every
repository at once.

## See where you are

Give the slug alone:

```
python scripts/forge-branch.py <slug>
```

It reports the branch the repository is on and, when there is more than
one, lists the branches the repository has.

## Unsaved changes stop a switch

If the repository has unsaved changes, the script refuses to switch and
tells you how many files are affected. Save first, then switch, so that
nothing is carried across or lost.

## What stays with git

The script switches and creates, nothing else. Merging, deleting and
pushing branches stay with git, by hand or by merge request:

- A new branch reaches the remote by the first save made on it.
- A merge into `main` is done by hand or by merge request.
- A release is made from `main` only.

## See also

- [Save your work](save-your-work.md): the save that carries a branch to the remote.
- [About persistence in git](../about/persistence-in-git.md): why merging is left to git.
