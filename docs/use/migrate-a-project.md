---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 6a1753c6b14ed1bb
inputs:
  - .claude/skills/migrate/SKILL.md
  - scripts/forge-migrate.py
  - templates/project.md
---

# Migrate a project

This page shows how you bring a project to the shape of files a new release expects, with `/migrate`. It is for the principal (the person whose thinking is forged) who has upgraded the engine and now finds that a project is still of the older shape.

## When to use it

Use `/migrate` when a release has changed the shape of files and a project does not yet have the new shape. A project without a project file is of the older shape.

A migration runs once per project, on one clone, on `main`. Everyone else who works on the project does not migrate: they pull the migrated project. The upgrade it belongs to is in [Upgrade the engine](upgrade-the-engine.md). Why a shape change comes with a migration, and why it runs only once, is in [Upgrades and migration](../about/upgrades-and-migration.md).

Terms of the forge are in the [Glossary](../reference/glossary.md).

## The command

```
/migrate my-idea
```

The slug is optional when Claude can tell the project from the conversation. The slug `forge` names the engine's own project.

## What happens

1. Claude runs the dry run, `python scripts/forge-migrate.py my-idea`, and shows you its print as it came. The print lists the marks of the shape, the steps that would run and what each would change. The dry run changes nothing.

   You should now see the marks of the shape, each ticked or empty, and the closing line "dry run: steps ... would run; nothing changed". A project already in shape ends here, with the line "already in the shape of the first release - nothing to do".

2. You give your word. Only then does Claude run `python scripts/forge-migrate.py my-idea --apply`. The script commits nothing. It runs the steps still missing, in this order:

   - The fields that change with a round leave the headers of the artefacts, work specifications, recipes, indexes and the documentation map.
   - The project file is written, with the project's slug, its kind and its language.
   - What only the ledger knew becomes records and index fields. The ledger is the table of the project's state. The hand-kept ledger is kept as an immutable archive beside it, and the ledger leaves git.
   - The threads file is cut into one file per thread, in a `threads/` directory.
   - The `.gitattributes` file is written.

   A library takes fewer steps: the header fields, the project file, the ledger and the `.gitattributes`. It has no threads to cut.

   You should now see the line "migrated: steps ...; nothing committed - /save follows". If a mark still fails afterwards, the script says so and names the way back.

3. Claude walks you through what the script printed, for your judgement. This is a walkthrough (a list worked one item at a time, see [Walk through a list](walk-through-a-list.md)).
   - The main item is the origin the script guessed for each thread: your own word, a document named by its path, or Claude's synthesis. The script guesses it from the first sentence of the thread, so it can be wrong.
   - Claude lays out one table of its judgement from the texts, and you correct what is wrong.
   - The corrected origins are written into the thread files at the round's end.
   - Text after the last thread that was not a thread, and ledger lines with no ID, go where they belong. Usually that is a record in the history of the intent.

   You should now see each thread file carrying the origin you confirmed.

4. Claude makes the ledger, `python scripts/forge-ledger.py my-idea`, and proposes `/save my-idea`. The migrated shape reaches the remote by that save, described in [Save your work](save-your-work.md).

   You should now see the ledger made and the save proposed.

## What you have afterwards

- The project has a project file, headers without the fields that change with a round, and its threads as one file each.
- The ledger is no longer in git. The old hand-kept ledger is kept as an archive that is never edited.
- The `.gitattributes` file is in place.
- Nothing is committed until you save.

## If something goes wrong

The script refuses `--apply`, and changes nothing, in these cases. The dry run prints the same refusals as a warning.

- Not a repository: "not a repository".
- A working tree that is not clean: "the working tree is not clean: save first".
- A branch that is behind or diverged from its origin: "... against the origin: /pull first".
- Any branch but `main`: "on branch ..., not main".
- An instance file without the `Author` line: "No Author in CLAUDE.local.md - run /setup; the records need the handle." The instance file is `CLAUDE.local.md` at the engine root.

If you judge after the migration that something is wrong, the way back depends on whether you have saved:

- Before the save, run `python scripts/forge-migrate.py my-idea --undo`. It restores the changed and deleted files, removes the created ones and puts the ledger back into git.
- After the save, return to the tag taken before the migration.

## A worked example

You have upgraded the engine and the project `my-idea` is of the older shape.

1. You type `/migrate my-idea`.
2. Claude shows the dry run. The marks for the project file, the threads and the `.gitattributes` are empty, and the steps list what each would change.
3. You say "go on". Claude runs the script with `--apply`.
4. Claude shows a table of the threads with the origin it guessed for each. You correct two of them. Claude writes the corrections into the thread files.
5. Claude makes the ledger and proposes `/save my-idea`. You agree, and the migrated project reaches the remote.

## See also

- [Upgrade the engine](upgrade-the-engine.md): the upgrade a migration belongs to.
- [Upgrades and migration](../about/upgrades-and-migration.md): why a shape change comes with a migration and why it runs once.
- [Save your work](save-your-work.md): the save that carries the migrated shape to the remote.
- [Walk through a list](walk-through-a-list.md): how the guessed thread origins are judged.
- [Scripts](../reference/scripts.md): `forge-migrate.py`, its forms and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
