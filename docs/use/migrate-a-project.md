---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: e457b1a5f47418be
inputs:
  - .claude/skills/migrate/SKILL.md
  - scripts/forge-migrate.py
  - templates/project.md
---

# Migrate a project

This page shows how you bring a project to the shape of files a new release expects, with `/migrate`. It is for the principal (whoever's thinking is forged, and so the one who owns the project) who has upgraded the engine and finds that a release changed the shape of files.

## When to use it

Use it when a release changed the shape of files and your project is still in the old shape. A project without a project file is in the old shape, and `/migrate` is the one remedy.

A migration runs once per project, on one clone, on `main`. Everyone else who works on the project pulls the migrated project instead of migrating it again. The upgrade that comes before it is described in [Upgrade the engine](upgrade-the-engine.md).

## The command

```
/migrate my-idea
```

The slug is optional where Claude can tell the project from the context. The slug `forge` is the engine's own project.

## What happens

1. Claude runs the dry run, `python scripts/forge-migrate.py <slug>`, and shows you its print as it came: the marks of the shape, the steps that would run and what each would change. The dry run changes nothing.

   You should now see a list of marks, each ticked or not, and a closing line that names the steps that would run. A project already in shape ends here, with the line "already in the shape of the first release - nothing to do".

2. Before the migration you take a tag, `/save <slug> --tag <name>`. The tag is the way back once the migrated project is saved. See [Save your work](save-your-work.md).

   You should now see the save report and the tag named in it.

3. On your word, and only then, Claude runs `python scripts/forge-migrate.py <slug> --apply`. The script does these steps:
   - The fields that change with a round leave the headers.
   - The project file is written.
   - What only the ledger knew becomes records and index fields.
   - The hand-kept ledger is kept as an immutable archive, and the ledger leaves git.
   - The threads file is cut into one file per thread.
   - The `.gitattributes` file is written.

   A library takes fewer steps: it has no threads file to cut. The script commits nothing.

   You should now see the line "migrated:" with the steps that ran and the words "nothing committed - /save follows".

4. Claude goes through what the script printed, for your judgement. Above all this is the origin the script guessed for each thread. It is a walkthrough (one item at a time, each closed with your verdict, as in [Walk through a list](walk-through-a-list.md)), and the corrections are written into the thread files at the round's end. Text after the last thread that was not a thread goes where it belongs.

   You should now see each guessed origin put to you, and after the round the thread files carrying the origins you confirmed or corrected.

5. Claude makes the ledger and proposes `/save <slug>`. The migrated shape reaches the remote by that save.

   You should now see the ledger made and the save proposed.

## What you have afterwards

- A project in the new shape, with a project file, headers free of the fields that change with a round, one file per thread, and the ledger out of git.
- The hand-kept ledger kept as an archive that is never edited.
- A migrated project that is saved and on the remote once you have run the save.

## The way back

- Before the save: `python scripts/forge-migrate.py <slug> --undo`.
- After the save: the tag you took before the migration.

## A project outside git

A project outside git is migrated the same way, with none of git's refusals. Take a backup before `--apply`, as the dry run tells you. That backup is its way back, because `--undo` refuses there. A run that stops midway is finished by running it again.

## If something goes wrong

The script refuses `--apply`, and changes nothing, in these cases. The first three apply to a project that is a repository of its own:

- The working tree has unsaved changes to tracked files. Save first.
- The branch is behind or diverged from its origin. Pull first.
- The branch is any but `main`.

For every project one more refusal holds:

- The instance file has no `Author` line. Run `/setup`, because the records need the handle.

If the steps ran but a mark still fails, the script says which and names `--undo`.

## A worked example

You have upgraded the engine and your project `my-idea` is in the old shape.

1. You type `/migrate my-idea`. Claude prints the dry run: the marks, with the project file and the thread files not yet in place, and the steps that would run.
2. You take the tag: `/save my-idea --tag before-migration`.
3. You say yes. Claude runs `python scripts/forge-migrate.py my-idea --apply`, and the script reports the steps that ran and that nothing is committed.
4. Claude shows you the origin guessed for each thread, one at a time. You correct two, and at the end of the round they are written into the thread files.
5. Claude makes the ledger and proposes `/save my-idea`. You accept, and the migrated project reaches the remote.

## See also

- [Upgrade the engine](upgrade-the-engine.md): the upgrade a migration belongs to.
- [Upgrades and migration](../about/upgrades-and-migration.md): why a shape change comes with a migration and why it runs once.
- [Save your work](save-your-work.md): the save that takes the tag before and carries the migrated shape to the remote after.
- [Walk through a list](walk-through-a-list.md): how the guessed thread origins are judged.
- [Scripts](../reference/scripts.md): `forge-migrate.py`, its forms and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
