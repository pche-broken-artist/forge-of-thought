---
generated: 2026-10-09
made: mirrored
inputs-hash: 031f777672c1d23e
inputs:
  - scripts/forge-branch.py
  - CLAUDE.md
---

# Work on a branch

This page is for anyone who wants to work on a branch instead of on `main`. Branches are voluntary: whoever does not want them works on `main` and never meets this page.

## Switch to a branch

Run the script with the repository's slug and the branch you want:

```
python scripts/forge-branch.py <slug> <branch>
```

`forge` as the slug means the engine itself. There is no form without a slug, because switching every repository at once is never what anyone wants.

- If the branch exists, the repository switches to it and the script says so.
- If it does not exist, the script creates it from the current state and switches to it. It tells you the branch reaches the remote with the first save made on it.
- If you are already on that branch, the script says so and changes nothing.
- To go back, give `main` as the branch: `python scripts/forge-branch.py <slug> main`.

## See where you are

Give the slug alone:

```
python scripts/forge-branch.py <slug>
```

The script reports the branch the repository is on and, when there is more than one, lists the branches the repository has.

## Unsaved changes stop a switch

If the repository has unsaved changes, the script refuses to switch and tells you how many files are affected. Save first, then switch. Nothing is then carried across or lost.

## What stays with git

The script switches and creates, and does nothing else. The rest is git's, done by hand or by merge request:

- Merging a branch into `main`.
- Deleting a branch.
- Pushing a branch: a new branch reaches the remote by the first save made on it.

A release is made from `main` only, so switch back to `main` before releasing.

## See also

- [Save your work](save-your-work.md): the save that carries a branch to the remote.
- [About persistence in git](../about/persistence-in-git.md): why merging is left to git.
