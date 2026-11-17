---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 8899e7db94d1e6cc
inputs:
  - scripts/forge-branch.py
  - .claude/skills/release/SKILL.md
  - projects/forge/40-solution-design.md#SOL.0510
---

# Work on a branch

This page shows how you switch a repository to a branch, or back to
`main`, without typing git. It is for anyone who wants a branch of
their own. Branches are voluntary: whoever does not want one works on
`main` and never meets this page.

## When to use it

- You want your work on a branch of its own and not on `main`.
- You want to go back to `main` from a branch.
- You want to know which branch a repository is on, and which branches
  it has.

## The command

```
python scripts/forge-branch.py <slug> <branch>
```

The slug names the repository. The word `forge` is a slug too: it
means the engine and the forge's own project cloned beside it, which
are switched together. There is no form without a slug, because
switching every repository at once is never what anyone wants.

With the slug alone, the script reports instead of switching:

```
python scripts/forge-branch.py forge
```

To go back to `main`:

```
python scripts/forge-branch.py <slug> main
```

## What happens

1. The script reads the branch each repository is on.
   You should now see nothing yet if you gave a branch; with the slug
   alone you should now see one line per repository, `on branch ...`,
   and under it the list of branches when there is more than one.
2. Every repository is checked for unsaved changes before any is
   switched. For `forge` this means the engine and the project beside
   it are both checked first, so they are switched together or not at
   all.
   You should now see no message, and the switch goes on.
3. Each repository is switched. When the branch exists, the script
   switches to it. When it does not exist, the script creates it from
   the repository's current state and switches to it.
   You should now see `switched to <branch>`, or `created <branch>
   from <current branch> and switched to it`, once per repository.
   A repository that is already on the branch says `already on
   <branch>`.

## What you have afterwards

- The repository, or both repositories for `forge`, stand on the
  branch.
- A branch created now exists on your machine only. It reaches the
  remote with the first save you make on it (see
  [Save your work](save-your-work.md)). The script says so after it
  creates a branch.

Merging, deleting and pushing branches are not done by this script.
They stay with git. Why merging is left to git is explained in
[Persistence in git](../about/persistence-in-git.md), and how a
contributor's branch reaches the integrator in
[Working together on one project](../about/working-together.md).

A release, a documentation run and a publish are made from `main`
only. On another branch a release stops and reports the branch the
repository is on and how to get back, which is the command above with
`main`, after saving.

## If something goes wrong

- `<name> has unsaved changes (N file(s)). Save first (forge-save
  <slug>), then switch.` Unsaved changes stop a switch, so that
  nothing is carried across or lost. Save, then run the command again.
  For `forge` nothing is switched when any one of the two repositories
  has unsaved changes.
- `Project '<slug>' not found (...)`. The slug names no project. Check
  the spelling.
- `'<slug>' is not a repository - nothing to switch.` The project is
  not a repository of its own, so there is no branch to switch.
- `Could not switch <name> to '<branch>'.` and `Could not create
  branch '<branch>' in <name>.` The switch itself failed. The script
  gives no further reason.
- `Cannot read the current branch of <name>.` The script could not
  tell which branch the repository is on.

## A worked example

You want to try a change on a branch in the project `<slug>`, and
come back afterwards.

1. Save what you have, so that nothing is unsaved.
2. Switch, creating the branch:

   ```
   python scripts/forge-branch.py <slug> <branch>
   ```

   You should now see `created <branch> from main and switched to it`,
   and below it the line that the branch reaches the remote with the
   first save made on it.
3. Work and save as always. The first save carries the branch to the
   remote.
4. Check where you are:

   ```
   python scripts/forge-branch.py <slug>
   ```

   You should now see `on branch <branch>` and the list of branches.
5. Save again, then go back:

   ```
   python scripts/forge-branch.py <slug> main
   ```

   You should now see `switched to main`.

## See also

- [Save your work](save-your-work.md): the save that carries a branch
  to the remote.
- [Persistence in git](../about/persistence-in-git.md): why merging is
  left to git.
- [Working together on one project](../about/working-together.md): how
  a contributor's branch reaches the integrator.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
