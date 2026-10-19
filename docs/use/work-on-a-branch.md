---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 9795f30121a49ec6
inputs:
  - scripts/forge-branch.py
  - .claude/skills/release/SKILL.md
---

# Work on a branch

This page shows how you switch a repository to a branch, or back to `main`, with one script and without typing git. It is for anyone who wants to keep a stretch of work apart from `main`. Branches are voluntary: whoever does not want one works on `main` and never meets the script.

## When to use it

Use it when you want a branch of your own for a stretch of work, or when you want to know which branch a repository is on. The script does these two things and nothing else.

## The command

```
python scripts/forge-branch.py <slug> <branch>
```

The slug names the repository. The slug `forge` means the engine. There is no form without a slug, because switching every repository at once is never wanted.

With the slug alone, the script reports the branch the repository is on and lists the branches it has:

```
python scripts/forge-branch.py forge
```

To go back to the released line:

```
python scripts/forge-branch.py <slug> main
```

## What happens

1. The script finds the repository and reads the branch it is on.
   You should now see nothing yet; a missing project or a directory that is not a repository stops here with a message saying so.
2. With no branch name, it prints the branch and, when there are several, the list.
   You should now see a line "on branch" followed by the branch name.
3. With the name of the branch you are already on, it changes nothing.
   You should now see "already on" and the name.
4. With another name, it first checks for unsaved changes. Any unsaved change stops the switch, so that nothing is carried across or lost.
5. If the branch exists, the script switches to it.
   You should now see "switched to" and the branch name.
6. If the branch does not exist, the script creates it from the current state and switches to it.
   You should now see "created" with the branch you came from, "and switched to it", and a second line saying the branch reaches the remote with the first save made on it.

## What you have afterwards

The repository is on the branch you named. A new branch exists only on your machine until you save on it: the first save made on the branch carries it to the remote (the copy of the repository kept on a server). How to save is on [Save your work](save-your-work.md).

Merging a branch into `main`, deleting a branch and pushing a branch stay with git: a merge is done by hand or by merge request. The reason merging is left to git is on [Persistence in git](../about/persistence-in-git.md). A release is made from `main` only. On any other branch it stops and tells you which branch the repository is on and how to get back; save first, then switch to `main`.

Terms of the forge are explained one line each in the [Glossary](../reference/glossary.md).

## If something goes wrong

- "has unsaved changes": the repository has changes that are not saved. Save first, then switch again.
- "not found": the slug names no project. Check the slug; `forge` is the engine.
- "is not a repository": the project is not under git, so there is nothing to switch.
- "Cannot read the current branch": the script could not read the branch of the repository.
- "Could not switch" or "Could not create branch": git refused the switch or the creation. The message names the branch and the repository.

## A worked example

You want to try a change in the engine without touching `main`.

1. Save what is open, as described in [Save your work](save-your-work.md).
2. Create the branch and switch to it:

   ```
   python scripts/forge-branch.py forge <branch>
   ```

   You should now see that the branch was created from `main` and switched to.
3. Work and save as usual. The first save carries the branch to the remote.
4. Look at where you are:

   ```
   python scripts/forge-branch.py forge
   ```

   You should now see "on branch" with your branch name, and the list of branches.
5. Go back when you are done:

   ```
   python scripts/forge-branch.py forge main
   ```

   You should now see "switched to main".

## See also

- [Save your work](save-your-work.md): the save that carries a branch to the remote.
- [Persistence in git](../about/persistence-in-git.md): why merging is left to git.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
