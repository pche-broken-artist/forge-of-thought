---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 87e0cc2da9439984
inputs:
  - .claude/skills/migrate/SKILL.md
  - scripts/forge-migrate.py
  - templates/project.md
---

# Migrate a project

This page shows how to bring a project to the shape of files a new release expects, with `/migrate`. It is for you, the principal (the person whose thinking is forged), when a release has changed the shape of files and your project still has the old one.

## When to use it

Use it when a release changed the shape of files and your project is not yet in that shape. The migration runs once per project, on one clone, on `main`. Everyone else who works on the project pulls the migrated project and does not migrate it again. The migration belongs to [Upgrade the engine](upgrade-the-engine.md); why a shape change comes with a migration and why it runs once is told in [Upgrades and migration](../about/upgrades-and-migration.md).

## The command

```
/migrate my-idea
```

The slug is optional where Claude can infer the project from context. `forge` is the forge's own project, a repository of its own beside the engine. A library is migrated the same way and takes fewer steps. The script behind the command is described in [Scripts](../reference/scripts.md).

## What happens

1. Claude runs the dry run, `python scripts/forge-migrate.py my-idea`, and shows its print as it came. The print holds the marks of the shape, the steps that would run and what each would change. A project already in shape ends here. If the real run would be refused, the dry run says so.

   You should now see the marks and, for every missing one, what it would change.

2. Before the migration you take a tag, `/save my-idea --tag <name>`. The tag is the way back once the migrated project is saved. See [Save your work](save-your-work.md).

   You should now see the save report the tag.

3. On your word, and only then, Claude runs `python scripts/forge-migrate.py my-idea --apply`. The steps are these:
   - the fields that change with a round leave the headers
   - the project file is written
   - what only the ledger knew becomes records and index fields
   - the hand-kept ledger is kept as an immutable archive and the ledger leaves git
   - the threads file is cut into one file per thread
   - the `.gitattributes` file is written

   A library takes fewer steps. The script commits nothing.

   You should now see a line that starts with "migrated" and names the steps that ran, ending "nothing committed - /save follows".

4. Claude walks through what the script printed for your judgement. Above all this is the origin it guessed for each thread. The origins are one walkthrough, written into the thread files at the round's end. Text that was not a thread goes where it belongs. How such a list is judged is told in [Walk through a list](walk-through-a-list.md).

   You should now see the guessed origins laid out for you to accept or correct.

5. Claude makes the ledger and proposes `/save my-idea`. The migrated shape reaches the remote by that save.

   You should now see the save commit and push the migrated project.

## What you have afterwards

- The headers carry no field that changes with a round.
- The project has a project file.
- The old ledger is kept as an immutable archive, and the ledger is out of git.
- Each thread is a file of its own, with its origin judged.
- The project has a `.gitattributes` file.
- The migrated shape is on the remote.

## The way back

Before the save, run `python scripts/forge-migrate.py my-idea --undo`. After the save, the way back is the tag taken before the migration.

A project outside git is migrated the same way, with none of git's refusals. You take a backup before `--apply`, as the dry run tells you. That backup is its way back, and `--undo` refuses there. A run that stops midway is finished by running it again.

## If something goes wrong

For a project that is a repository of its own, `--apply` refuses and changes nothing in these cases:

- unsaved changes to tracked files
- a branch behind or diverged from its origin
- any branch but `main`

For every project, the script refuses when your instance file has no `Author` line. It prints "No Author in CLAUDE.local.md - run /setup; the records need the handle." Run `/setup` and try again.

If the steps ran but a mark still fails, the script prints "steps ran but these marks still fail" and names them. It also names the undo command. Run it, and the project is back as it was.

`--undo` also refuses when there is nothing to take back: "No manifest ... - nothing to undo."

## A worked example

You have a project `my-idea` and a new release has changed the shape of files.

1. You type `/migrate my-idea`. Claude prints the dry run: the marks, and the steps that would run. Two marks fail, so two steps are listed.
2. You take the tag with `/save my-idea --tag before-migration`.
3. You say "apply". Claude runs `python scripts/forge-migrate.py my-idea --apply`, and the script prints "migrated" and the steps that ran.
4. Claude lays out the origins it guessed for the threads. You correct one and accept the rest. Claude writes them into the thread files.
5. Claude makes the ledger and proposes `/save my-idea`. You accept, and the migrated project reaches the remote.

## See also

- [Upgrade the engine](upgrade-the-engine.md): the upgrade a migration belongs to.
- [Upgrades and migration](../about/upgrades-and-migration.md): why a shape change comes with a migration and why it runs once.
- [Save your work](save-your-work.md): the save that takes the tag before and carries the migrated shape to the remote after.
- [Walk through a list](walk-through-a-list.md): how the guessed thread origins are judged.
- [Scripts](../reference/scripts.md): `forge-migrate.py`, its forms and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
