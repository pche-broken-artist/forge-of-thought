---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 5b94758277d51665
inputs:
  - scripts/forge-branch.py
  - .claude/skills/release/SKILL.md
---

# Work on a branch

This page shows how to switch a repository to a branch, or back to `main`, without typing git. It is for you if you want a branch of your own. Branches are voluntary: whoever does not want one works on `main` and never meets this script. A repository here is the engine or one project, and each project is a repository of its own.

## When to use it

- You want to work on a branch instead of `main`.
- You want to know which branch a repository is on.
- You want to get back to `main`, for example because a release is made from `main` only.

## The command

Switch to a branch, creating it when it does not exist:

```
python scripts/forge-branch.py <slug> <branch>
```

Switch back to `main`:

```
python scripts/forge-branch.py <slug> main
```

Report the branch and list the branches:

```
python scripts/forge-branch.py <slug>
```

The slug names the repository. The slug `forge` means the engine. There is no form without a slug, because switching every repository at once is never what anyone wants.

## What happens

1. The script finds the repository and reads the branch it is on.

   You should now see, with the slug alone, the line "on branch" and the branch name. When the repository has more than one branch, a second line lists them.

2. If you named the branch you are already on, the script says so and does nothing more.

   You should now see "already on" and the branch name.

3. If the repository has unsaved changes, the script stops. Nothing is carried across and nothing is lost.

   You should now see a message that the repository has unsaved changes, with the number of files.

4. If the branch exists, the script switches to it.

   You should now see "switched to" and the branch name.

5. If the branch does not exist, the script creates it from the current state and switches to it.

   You should now see "created" with the branch name, the branch it was made from, and a note that the branch reaches the remote with the first save made on it.

## What you have afterwards

The repository stands on the branch you named. Every save you make now lands on that branch.

A new branch exists only on your machine at first. It reaches the remote with the first save made on it (see [Save your work](save-your-work.md)).

Some things are made from `main` only:

- a release
- a documentation run
- a publish

On any other branch a release stops and reports the branch the repository is on and how to get back to `main`. Save first, then switch back with the command above.

Merging a branch into `main`, deleting a branch and pushing a branch stay with git. A merge is done by hand or by merge request. The script does none of these. [Persistence in git](../about/persistence-in-git.md) explains why merging is left to git, and [Working together on one project](../about/working-together.md) shows how a contributor's branch reaches the integrator.

## If something goes wrong

- "has unsaved changes": save first, then switch. See [Save your work](save-your-work.md).
- "Project ... not found": the slug names no project. Check it against the folders in `projects/`.
- "is not a repository - nothing to switch": the folder is not a repository of its own, so there is no branch to switch.
- "Could not switch" or "Could not create branch": git refused. The reason is not recorded.
- "Cannot read the current branch": the script could not read the branch of the repository. The reason is not recorded.
- git missing: the script needs Python 3.8 or newer and git on the path.

## A worked example

You want a branch called `<branch>` in the project `<slug>`.

```
python scripts/forge-branch.py <slug>
```

The script reports that the project is on `main`.

```
python scripts/forge-branch.py <slug> <branch>
```

The script creates `<branch>` from `main` and switches to it. You work and save as usual; the first save pushes the branch to the remote. When you are done and the work is merged, you go back:

```
python scripts/forge-branch.py <slug> main
```

The script reports that it switched to `main`. If it reports unsaved changes instead, save first and run the command again.

For the engine itself, use `forge` in place of `<slug>`. The terms of the forge are in the [Glossary](../reference/glossary.md).

## See also

- [Save your work](save-your-work.md): the save that carries a branch to the remote.
- [Persistence in git](../about/persistence-in-git.md): why merging is left to git.
- [Working together on one project](../about/working-together.md): how a contributor's branch reaches the integrator.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
