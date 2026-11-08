---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 414699cf3fd12a5c
inputs:
  - scripts/forge-branch.py
  - .claude/skills/release/SKILL.md
---

# Work on a branch

This page shows how to switch a repository to a branch, or back to `main`, with one script and without typing git. It is for anyone who wants a branch of their own; whoever does not works on `main` and never meets the script.

A branch is a line of work kept apart from `main`, the released line. Branches are voluntary. The script does two things and nothing else: it switches a repository to a branch, and it reports which branch the repository is on.

## When to use it

- You want to try a change without touching `main`.
- You work with others and your change should travel as a branch (see [Working together on one project](../about/working-together.md)).
- You are on a branch and want to return to `main`, for instance because a release is made from there.

## The command

```
python scripts/forge-branch.py <slug> <branch>
```

The repository is named by its slug. The slug `forge` means the engine itself. There is no form without a slug, because switching every repository at once is never what anyone wants.

Three variants of the same command:

- `python scripts/forge-branch.py <slug> <branch>` switches to the branch and creates it, from the current state, when it does not exist yet.
- `python scripts/forge-branch.py <slug> main` switches back to `main`.
- `python scripts/forge-branch.py <slug>` reports the branch and lists the branches the repository has.

## What happens

1. The script finds the repository. You should now see no error; if the slug is unknown or names something that is not a repository, the script says so and stops.
2. With a slug alone it prints the branch the repository is on and, when there is more than one branch, the list of them. You should now see a line of the form "on branch ...".
3. With a branch name it first checks for unsaved changes. If there are none it carries on. You should now see no message about unsaved changes.
4. It switches to the branch, or creates it when it does not exist. You should now see "switched to ..." for an existing branch, or "created ... from ... and switched to it" for a new one.
5. For a new branch it adds a note that the branch reaches the remote with the first save made on it. You should now see that note under the line of step 4.

## What you have afterwards

- The repository is on the branch you named, and your next work lands there.
- A new branch exists only on your machine until you save on it. The first save made on the branch carries it to the remote (see [Save your work](save-your-work.md)).

## What stays with git

The script does not merge, delete or push branches. These stay with git: a merge into `main` is made by hand or by merge request, and how a contributor's branch reaches the integrator is described in [Working together on one project](../about/working-together.md). The reason merging is left to git is given in [Persistence in git](../about/persistence-in-git.md).

A release, a documentation run and a publish are made from `main` only. On any other branch a release stops and reports the branch the repository is on and how to get back. Save first, then switch back with the second variant above.

## If something goes wrong

- "has unsaved changes": the switch is refused so that nothing is carried across or lost. Save first (see [Save your work](save-your-work.md)), then run the command again.
- "Project '...' not found": the slug names no project. Check the slug against the projects you have.
- "is not a repository - nothing to switch": the project is not under git, so it has no branch to switch.
- "Cannot read the current branch": the script could not read the branch of the repository.
- "Could not switch ..." or "Could not create branch ...": git refused the switch or the creation, and the script stops.
- "already on ...": you asked for the branch you are on; nothing changes.

Every term of the forge, such as the slug, is explained in one line in the [Glossary](../reference/glossary.md).

## A worked example

You are on `main` in a project with the slug `<slug>` and want to work on a branch.

1. Save what is unsaved, as [Save your work](save-your-work.md) describes.
2. Run `python scripts/forge-branch.py <slug> <branch>`. The script prints that it created `<branch>` from `main` and switched to it.
3. Work and save as usual. The first save on `<branch>` carries it to the remote.
4. Run `python scripts/forge-branch.py <slug> main` after saving. The script prints that it switched to `main`.
5. Run `python scripts/forge-branch.py <slug>` to see the branch you are on and the branches that exist.

## See also

- [Save your work](save-your-work.md): the save that carries a branch to the remote.
- [Persistence in git](../about/persistence-in-git.md): why merging is left to git.
- [Working together on one project](../about/working-together.md): how a contributor's branch reaches the integrator.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
