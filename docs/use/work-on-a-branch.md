---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 1b5c3002db06ede2
inputs:
  - scripts/forge-branch.py
---

# Work on a branch

This page shows how you switch a repository to a branch, or back to `main`, with one script and without typing git. It is for anyone who wants a branch. Branches are voluntary: whoever does not want one works on `main` and never meets the script.

## When to use it

- You want to work on a change apart from `main`.
- You want to know which branch a repository is on.
- You want to go back to `main`.

## The command

```
python scripts/forge-branch.py <slug> <branch>
```

The slug names the repository. The slug `forge` means the engine. There is no form without a slug, because switching every repository at once is never what anyone wants.

With the slug alone, the script reports where the repository stands:

```
python scripts/forge-branch.py <slug>
```

## What happens

1. The script finds the repository named by the slug. You should now see no error. If the slug is not a repository, the script stops and says so.
2. Without a branch name, it prints the branch the repository is on. You should now see a line "on branch" followed by the name. When the repository has more than one branch, a second line lists them after "branches:".
3. With a branch name that is the current branch, it changes nothing. You should now see "already on" and the name.
4. With another name, it first checks for unsaved changes. If there are any, it stops (see below). You should now see no stop message.
5. If the branch exists, it switches to it. You should now see "switched to" and the name.
6. If the branch does not exist, it creates the branch from the current state and switches to it. You should now see "created" the branch "from" the previous one "and switched to it", then a second line saying that the branch reaches the remote with the first save made on it.

Use `main` as the branch name to switch back.

## What you have afterwards

The repository is on the branch you named, and nothing else has changed. The script does two things only: it switches, and it reports.

What stays with git, outside the script:

- Merging a branch into `main` is done by hand or by merge request. The reason is on [Persistence in git](../about/persistence-in-git.md).
- Deleting a branch.
- Pushing a branch.

A new branch reaches the remote by the first save made on it. How a save is made is on [Save your work](save-your-work.md).

A release is made from `main` only. Switch back to `main` before you release.

## If something goes wrong

- Unsaved changes: the script stops with "has unsaved changes", the number of files, and the instruction to save first. Save the repository, then switch again. Nothing is carried across the switch and nothing is lost.
- The project does not exist: the script stops with "Project ... not found", naming the path it looked at.
- The slug is not a repository: the script stops with "is not a repository - nothing to switch".
- The current branch cannot be read: the script stops with "Cannot read the current branch".
- The switch or the creation fails: the script stops with "Could not switch" or "Could not create branch", naming the branch.

## A worked example

You want to try a change in a project without touching `main`.

1. Look at where the project stands:

   ```
   python scripts/forge-branch.py <slug>
   ```

   You should now see that it is on `main`.

2. Create the branch and switch to it:

   ```
   python scripts/forge-branch.py <slug> <branch>
   ```

   You should now see that `<branch>` was created from `main` and switched to.

3. Work, then save on the branch. The first save pushes the new branch to the remote.

4. When you want to leave the branch, save first, then switch back:

   ```
   python scripts/forge-branch.py <slug> main
   ```

   You should now see that the repository switched to `main`.

## See also

- [Save your work](save-your-work.md): the save that carries a branch to the remote.
- [Persistence in git](../about/persistence-in-git.md): why merging is left to git.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
