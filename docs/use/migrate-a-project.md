---
generated: 2026-10-23
version: 5.33
made: mirrored
inputs-hash: a8138475f5854194
inputs:
  - .claude/skills/migrate/SKILL.md
  - scripts/forge-migrate.py
  - templates/project.md
---

# Migrate a project

This page shows how you bring a project to the shape of files a new release expects, with `/migrate`. It is for the principal (the person whose thinking is forged) who has [upgraded the engine](upgrade-the-engine.md) and finds that a release changed the shape of files.

## When to use it

Use it when a release has changed the shape of files and a project is still in the old shape. A project without its project file is in the old shape, and the commands and checks say so and name `/migrate` as the one remedy.

A migration runs once per project, on one clone, on `main`. Everyone else who works on the project pulls the migrated project and does not migrate it again. The slug `forge` is the engine's own project.

The reasons a shape change comes with a migration, and why it runs once, are on [Upgrades and migration](../about/upgrades-and-migration.md).

## The command

```
/migrate my-idea
```

Without a slug, Claude infers the project from context and asks if that is ambiguous. Claude is the model that works with you. The script behind the command is `scripts/forge-migrate.py`; its forms and what it needs are on [Scripts](../reference/scripts.md).

## What happens

1. Claude runs the dry run, `python scripts/forge-migrate.py my-idea`, and shows its print as it came. The print holds the marks of the shape, the steps that would run and what each would change.
   You should now see the marks, and for every step still missing, what it would change. A project already in shape ends here, with nothing to do.

2. On your word, and only then, Claude runs `python scripts/forge-migrate.py my-idea --apply`. The steps run in this order:
   - The fields that change with a round leave the headers of the artefacts, the work specifications, the recipes, the indexes and the documentation map.
   - The project file is written from its template, with the project's slug, its kind and its language.
   - What only the ledger knew becomes records and index fields. The hand-kept ledger is kept as an immutable archive, and the ledger leaves git.
   - The threads file is cut into one file per thread.
   - The `.gitattributes` is written.

   A library takes fewer steps: the headers, the project file, the ledger and the attributes, but no threads.
   The script commits nothing.
   You should now see the script report each step it ran, and the project's files changed in the working tree.

3. Claude walks through what the script printed, for your judgement. Above all this is the origin the script guessed for each thread. Claude lays the origins out as a walkthrough (one item at a time, each closed with your verdict), as [Walk through a list](walk-through-a-list.md) describes. What you correct is written into the thread files at the round's end. Text the script found that was not a thread goes where it belongs, usually a record of the intent's history. Waiting lines without an ID are printed too, because they have no home in the records.
   You should now see each thread's origin confirmed or corrected, and no text left without a place.

4. Claude makes the ledger and proposes `/save my-idea`. The migrated shape reaches the remote by that save, as [Save your work](save-your-work.md) describes.
   You should now see the ledger rebuilt and the save proposed.

## What you have afterwards

The project has a project file, headers without the fields that change with a round, one file per thread, a `.gitattributes`, and its records and index fields filled from what only the ledger knew. The old hand-kept ledger is an immutable archive, and the ledger is made at read time and is no longer in git. Nothing is committed until you save.

## The way back

Before the save, the way back is `python scripts/forge-migrate.py my-idea --undo`. After the save, the way back is the tag taken before the migration.

A project outside git is migrated the same way, with none of git's refusals. The dry run tells you to take a backup before `--apply`, and that backup is its way back. `--undo` refuses there. A run that stops midway is finished by running it again.

## If something goes wrong

The script stops before it changes anything, and prints that nothing was changed, when one of these holds for a project that is a repository of its own:

- The working tree has unsaved changes to tracked files.
- The branch is behind its origin or has diverged from it.
- The branch is not `main`.

For every project, the script refuses when the instance file has no `Author` line. It prints: "No Author in CLAUDE.local.md - run /setup; the records need the handle." Run `/setup`, then migrate again.

If the project is not found, the script says the directory does not exist. Check the slug.

`--undo` prints "No manifest ... nothing to undo." when no migration has been applied, and, outside git, "not under git - nothing to restore from; the way back is the backup taken before --apply."

## A worked example

You have pulled a release that changed the shape of files, and `my-idea` is still in the old shape.

1. You type `/migrate my-idea`. Claude runs the dry run and shows you the marks: the project file missing, headers with fields to remove, a threads file to cut. You see the steps that would run.
2. You say to go ahead. Claude runs the script with `--apply`. It reports each step and commits nothing.
3. Claude shows a table of the threads with the origin guessed for each. You correct two. Claude writes the corrections into the thread files at the end of the round, and places the one stray paragraph in the intent's history.
4. Claude makes the ledger and proposes `/save my-idea`. You agree, and the migrated project reaches the remote.

## See also

- [Upgrade the engine](upgrade-the-engine.md): the upgrade a migration belongs to.
- [Upgrades and migration](../about/upgrades-and-migration.md): why a shape change comes with a migration and why it runs once.
- [Save your work](save-your-work.md): the save that carries the migrated shape to the remote.
- [Walk through a list](walk-through-a-list.md): how the guessed thread origins are judged.
- [Scripts](../reference/scripts.md): `forge-migrate.py`, its forms and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.33 from the files the front-matter names; never edited by hand.
