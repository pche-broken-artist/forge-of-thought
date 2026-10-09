---
generated: 2026-10-09
made: mirrored
inputs:
  - scripts/forge-branch.ps1
  - CLAUDE.md
---

# Work on a branch

This page is for a user who wants to work on a branch of a project or
of the engine instead of on `main`: how to switch, how to come back,
and what is left to git. Branches are voluntary. Whoever does not want
them works on `main` and never meets this page.

## Switch to a branch

Run the script with the repository's slug and the branch name:

```
./scripts/forge-branch.ps1 my-project my-draft
```

The repository switches to the branch. When the branch does not exist
yet, it is created from the current state. The slug names the
repository; `forge` means the engine itself. There is no form without
a slug, because switching every repository at once is never what
anyone wants.

## Switch back to main

Give `main` as the branch:

```
./scripts/forge-branch.ps1 my-project main
```

## See which branch you are on

Run the script with the slug alone:

```
./scripts/forge-branch.ps1 my-project
```

It reports the current branch and lists the branches the repository
has.

## Save before you switch

Unsaved changes stop a switch. Save first, then switch, so that
nothing is carried across and nothing is lost.

## What stays with git

The script switches and creates, and reports. It does nothing else.

- Merging a branch into `main` is done with git by hand, or by merge
  request.
- Deleting a branch is done with git.
- Pushing a branch is not a step of its own: a new branch reaches the
  remote by the first save made on it.
- A release is made from `main` only. Switch back to `main` before you
  release.

## See also

- [Save your work](save-your-work.md): the save that carries a branch
  to the remote.
- [About persistence in git](../about/persistence-in-git.md): why
  merging is left to git.
