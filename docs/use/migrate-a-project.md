---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 49b9c1f98e2e35d0
inputs:
  - .claude/skills/migrate/SKILL.md
  - scripts/forge-migrate.py
  - templates/project.md
---

# Migrate a project

This page shows how you bring a project to the shape of files a new release expects, with `/migrate`. It is for the principal (the person whose thinking is forged) who has upgraded the engine and finds that a project still has the older shape. For the upgrade itself see [Upgrade the engine](upgrade-the-engine.md).

## When to use it

Use it when a release has changed the shape of files and your project is still in the old one. A command that finds the project in the old shape says so and stops. The project file (`project.md`) is missing, and `/migrate` is the one remedy.

A migration runs once per project, on one clone, on the `main` branch. Everyone else who works on the project pulls the migrated project and does not migrate it again. Why a shape change comes with a migration, and why it runs once, is explained in [Upgrades and migration](../about/upgrades-and-migration.md).

## The command

```
/migrate my-idea
```

The slug is optional where Claude can tell the project from the context. The slug `forge` is the engine's own project.

## What happens

1. Claude runs the dry run, `python scripts/forge-migrate.py <slug>`, and shows you what it printed as it came. The print lists the marks of the shape (one mark per step, each saying whether the project already has that part of the new shape), the steps that would run and what each would change. The dry run changes nothing.

   You should now see the marks and, for every step still missing, a line saying what it would change. A project already in shape ends here.

2. On your word, and only then, Claude runs `python scripts/forge-migrate.py <slug> --apply`. The script does these steps, in this order:

   - The fields that change with a round (such as dates and last-change notes) leave the headers of the artefacts, specifications, recipes, indexes and the documentation map.
   - The project file is written, with the project's slug, kind and language.
   - What only the ledger knew becomes records and index fields. The ledger is the state report that Claude makes from the documents. The hand-kept ledger is kept as an immutable archive, and the ledger leaves git.
   - The threads file is cut into one file per thread. Each thread file gets the bracketed topic of the old entry as the artefact it concerns, a guessed origin, and the status open.
   - The `.gitattributes` file is written.

   A library takes fewer steps: the headers, the project file, the ledger and the attributes, but no threads.

   The script commits nothing. You should now see each step report that its own mark is met.

3. Claude walks you through what the script printed, for your judgement. Above all this is the origin the script guessed for each thread. Claude lays them out as one walkthrough (a list worked one item at a time, with your verdict on each), as [Walk through a list](walk-through-a-list.md) describes. Your corrections are written into the thread files at the end of the round. The text after the last thread that was not a thread goes where it belongs, usually a record in the history of the intent. A line of the old Waiting list that carried no ID has no home in the records, so Claude raises it for you to decide.

   You should now see the thread files with origins you have confirmed or corrected.

4. Claude makes the ledger and proposes `/save <slug>`. The migrated shape reaches the remote by that save. See [Save your work](save-your-work.md).

   You should now see the save proposed with the project's changes in it.

## The way back

Before the save, `python scripts/forge-migrate.py <slug> --undo` takes back the last `--apply`. After the save, the way back is the tag taken before the migration.

## A project outside git

A project that is not a repository of its own is migrated the same way, but none of git's refusals apply to it. You take a backup before `--apply`, as the dry run tells you. That backup is the way back, because `--undo` refuses there. A run that stops midway is finished by running it again.

## What you have afterwards

- A project file and headers without the fields that change with a round.
- Records and index fields in place of what only the ledger knew.
- The old hand-kept ledger as an immutable archive, and the ledger out of git.
- One file per thread, with origins you have judged.
- The `.gitattributes` file.
- All of it uncommitted until you save.

## If something goes wrong

For a project that is a repository of its own, `--apply` refuses in these cases:

- There are unsaved changes to tracked files. An untracked file is no risk. Save or set aside the changes first.
- The branch is behind or has diverged from its origin. Pull first.
- The branch is not `main`.

For every project, `--apply` refuses when the instance file (`CLAUDE.local.md`) has no `Author` line. The script writes records in that author's name, so add the line and run again.

If the print differs from what you expect, or the migrated project looks wrong before the save, take it back with `--undo`. For the script's forms and what it needs, see [Scripts](../reference/scripts.md).

## A worked example

You have upgraded the engine and your project `my-idea` still has the old shape.

1. You type `/migrate my-idea`. Claude runs the dry run and shows its print: the marks, with the project file, the thread files and the attributes missing, and the steps that would create them.
2. You say to go ahead. Claude runs the script with `--apply`, and the marks are all met.
3. Claude shows a table of the threads the script cut, each with the origin it guessed. You correct two of them. Claude writes the corrected origins into the thread files when the round ends.
4. Claude makes the ledger and proposes `/save my-idea`. You accept, and the migrated project reaches the remote.

## See also

- [Upgrade the engine](upgrade-the-engine.md): the upgrade a migration belongs to.
- [Upgrades and migration](../about/upgrades-and-migration.md): why a shape change comes with a migration and why it runs once.
- [Save your work](save-your-work.md): the save that carries the migrated shape to the remote.
- [Walk through a list](walk-through-a-list.md): how the guessed thread origins are judged.
- [Scripts](../reference/scripts.md): `forge-migrate.py`, its forms and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
