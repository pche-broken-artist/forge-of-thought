---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 9fec8c4c8ecfc6ab
inputs:
  - scripts/forge-branch.py
  - .claude/skills/release/SKILL.md
  - projects/forge/40-solution-design.md#SOL.0510
---

# Work on a branch

This page shows how to switch a repository to a branch, or back to `main`, with one script and without typing git. It is for anyone who wants a branch of their own. Branches are voluntary: whoever does not want one works on `main` and never meets the script.

## When to use it

- You want your changes kept apart from `main` until they are ready.
- You want to know which branch a repository is on and which branches it has.
- You want to go back to `main` after working on a branch.

## The command

```
python scripts/forge-branch.py <slug> <branch>
```

`<slug>` names the repository: a project's slug, or `forge`. `forge` means the engine and the forge's own project cloned beside it, which are switched together. `<branch>` is the branch to switch to. The script creates it when it does not exist, and `main` switches back.

With the slug alone the script reports the branch and lists the branches:

```
python scripts/forge-branch.py forge
```

A bare form without a slug does not exist.

## What happens

1. The script reads the branch each named repository is on.
   You should now see nothing yet, or, when you gave no branch, one line per repository saying which branch it is on, with the list of branches beneath it where there is more than one.
2. Given a branch, the script checks every repository for unsaved changes before it switches any. For `forge` that means both repositories are checked first, so that they are switched together or not at all.
   You should now see no message, if nothing is unsaved.
3. The script switches each repository. Where the branch exists it switches to it. Where it does not, it creates the branch from the current state and switches to it. A repository already on the branch is left alone.
   You should now see `switched to <branch>`, `created <branch> from <current branch> and switched to it`, or `already on <branch>`, one line per repository.

## What you have afterwards

- The repository stands on the branch, and your next save is made there.
- A new branch exists only on your machine. It reaches the remote with the first save made on it, as [Save your work](save-your-work.md) describes.

## What stays with git

The script switches and reports, and does nothing else. Merging a branch, deleting it and pushing it stay with git. A new branch reaches the remote by the first save made on it.

A release, a documentation run and a publish are made from `main` only. On any other branch they stop and say which branch the repository is on. Save, switch back to `main` with this script, and run them there.

[Persistence in git](../about/persistence-in-git.md) says why merging is left to git. [Working together on one project](../about/working-together.md) says how a contributor's branch reaches the integrator. The [Glossary](../reference/glossary.md) gives every term of the forge in one line.

## If something goes wrong

- `<name> has unsaved changes (N file(s)). Save first ..., then switch.`: the repository holds changes that are not saved, and nothing was switched. Save, then run the command again, so that nothing is carried across or lost.
- `Project '<slug>' not found`: the slug names no project. Check it.
- `'<slug>' is not a repository - nothing to switch.`: the project is not under git, and the script runs no git on it.
- `Could not switch ...` or `Could not create branch ...`: git refused the switch. The script stops and names the repository.

## A worked example

You work on a project and want a branch of its own.

```
python scripts/forge-branch.py <slug> <branch>
```

The script prints that it created `<branch>` from `main` and switched to it, and that the branch reaches the remote with the first save made on it. You change documents and save. The first save sends the branch to the remote. When you want to release, you save once more and run:

```
python scripts/forge-branch.py <slug> main
```

You should now see `switched to main`. The release is made from there.

## See also

- [Save your work](save-your-work.md): the save that carries a branch to the remote.
- [Persistence in git](../about/persistence-in-git.md): why merging is left to git.
- [Working together on one project](../about/working-together.md): how a contributor's branch reaches the integrator.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
