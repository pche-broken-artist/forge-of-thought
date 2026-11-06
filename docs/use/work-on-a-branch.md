---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 5845b2242e092e48
inputs:
  - scripts/forge-branch.py
  - .claude/skills/release/SKILL.md
---

# Work on a branch

This page shows how you switch a repository to a branch, or back to `main`, without typing git. It is for anyone who wants a branch of their own. Branches are voluntary: whoever does not want one works on `main` and never meets the script.

## When to use it

Use it when you want to work apart from `main` and come back later. Use it also to see which branch a repository is on.

A repository is named by its slug. The slug `forge` means the engine, the repository that holds the forge itself.

## The command

Switch to a branch, creating it when it does not exist:

```
python scripts/forge-branch.py <slug> <branch>
```

Switch back to `main`:

```
python scripts/forge-branch.py <slug> main
```

Report the branch and list the branches of the engine:

```
python scripts/forge-branch.py forge
```

The slug is required. There is no form that switches every repository at once.

## What happens

1. The script finds the repository for the slug. You should now see no error that the project is missing or is not a repository.
2. With no branch name, it prints the branch the repository is on, and the list of branches when there is more than one. You should now see a line "on branch ..." and, if there are several, a line "branches: ...".
3. With a branch name equal to the current branch, it changes nothing. You should now see "already on ...".
4. Otherwise it checks for unsaved changes. If there are any, it stops. You should now see no message about unsaved changes.
5. If the branch exists, it switches to it. You should now see "switched to ...".
6. If the branch does not exist, it creates it from the current state and switches to it. You should now see "created ... from ... and switched to it", with a note that the branch reaches the remote with the first save made on it.

## What you have afterwards

The repository stands on the branch you named. A new branch exists only on your machine until you save on it: the first save made on it carries it to the remote. A save is described in [Save your work](save-your-work.md).

## What stays with git

The script does two things only: it switches and it reports. Merging, deleting and pushing branches stay with git:

- A merge into `main` is done by hand or by merge request. Why it is left to git is told in [Persistence in git](../about/persistence-in-git.md), and how a contributor's branch reaches the integrator in [Working together on one project](../about/working-together.md).
- A release is made from `main` only. So are a documentation run and a publish.

On any other branch a release stops and reports the branch the repository is on. To go back, save, then switch to `main` with the command above.

## If something goes wrong

- "has unsaved changes": the switch stops, so that nothing is carried across or lost. Save first, then switch again.
- "Project ... not found": the slug names no project. Check the slug.
- "is not a repository - nothing to switch": the project is not under git of its own, so there is no branch to switch.
- "Could not switch" or "Could not create branch": git refused the switch or the new branch. The repository stays on the branch it was on.
- "Cannot read the current branch": the script cannot tell which branch the repository is on, and stops.

## A worked example

You want to try a change apart from `main` in the project `<slug>`, on a branch `<branch>`.

1. Look where the repository stands: `python scripts/forge-branch.py <slug>`. You should now see that it is on `main`.
2. Switch and create: `python scripts/forge-branch.py <slug> <branch>`. You should now see that `<branch>` was created from `main` and switched to.
3. Work, then save as usual. You should now see the first save carry `<branch>` to the remote.
4. When you want `main` again, save, then run `python scripts/forge-branch.py <slug> main`. You should now see "switched to main".

## See also

- [Save your work](save-your-work.md): the save that carries a branch to the remote.
- [Persistence in git](../about/persistence-in-git.md): why merging is left to git.
- [Working together on one project](../about/working-together.md): how a contributor's branch reaches the integrator.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
