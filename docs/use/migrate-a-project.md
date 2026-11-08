---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 082a4d0171ad19bc
inputs:
  - .claude/skills/migrate/SKILL.md
  - scripts/forge-migrate.py
  - templates/project.md
---

# Migrate a project

`/migrate [slug]` brings a project to the shape of files a new release expects. It is for you, the principal (the person whose thinking is forged), when a release has changed the shape of files and a project still has the old one.

## When to use it

Use it when a release has changed the shape of files and your project is not yet in the new shape. Until it is, Claude's commands and checks say so as a fact and write nothing into the project.

A migration runs once per project, on one clone, on `main`. Everyone else who works on the project pulls the migrated project and does not migrate. The upgrade this belongs to is described in [Upgrade the engine](upgrade-the-engine.md), and the reason a shape change comes with a migration is in [Upgrades and migration](../about/upgrades-and-migration.md).

## The command

```
/migrate my-idea
```

The slug is optional where Claude can infer the project from context. The slug `forge` is the engine's own project.

## What happens

1. Claude runs the dry run, `python scripts/forge-migrate.py <slug>`, and shows its print as it came. The print lists the marks of the shape, the steps that would run and what each would change. A project that is already in shape ends here.

   You should now see the marks, each ticked or not, and for each missing step what it would change.

2. Before the migration you take a tag, `/save <slug> --tag <name>`. The tag is the way back once the migrated project is saved. See [Save your work](save-your-work.md).

   You should now see the save report with the tag named.

3. On your word, and only then, Claude runs the script with `--apply`. The script commits nothing. It performs these steps:
   - The fields that change with a round leave the headers.
   - The project file is written.
   - What only the ledger knew becomes records and index fields.
   - The hand-kept ledger is kept as an immutable archive, and the ledger leaves git.
   - The threads file is cut into one file per thread.
   - The `.gitattributes` file is written.

   A library takes fewer steps: it has no threads to cut.

   You should now see a line starting `migrated:` and every mark ticked.

4. Claude walks through what the script printed, for your judgement. The main item is the origin the script guessed for each thread. This is a walkthrough (see [Walk through a list](walk-through-a-list.md)): one table of Claude's judgement from the texts, you correct what is wrong, and the result is written into the thread files at the round's end. Text that was not a thread goes where it belongs.

   You should now see each thread file with the origin you judged.

5. Claude makes the ledger and proposes `/save <slug>`. The migrated shape reaches the remote by that save.

   You should now see the save report for the migrated project.

## What you have afterwards

- A project file, and headers without the fields that change with a round.
- Records and index fields where the ledger alone held state.
- The old hand-kept ledger as an immutable archive, with the ledger out of git.
- One file per thread, each with its origin judged.
- The attributes file for the project's repository.

## The way back

Before the save, run `python scripts/forge-migrate.py <slug> --undo`. After the save, the way back is the tag taken before.

## A project outside git

A project outside git is migrated the same way, with none of git's refusals. You take a backup before `--apply`, as the dry run tells you. That backup is the way back, because `--undo` refuses there. A run that stops midway is finished by running it again.

## If something goes wrong

For a project that is a repository of its own, `--apply` refuses and changes nothing when:

- the working tree has unsaved changes to tracked files
- the branch is behind or diverged from its origin
- the branch is any but `main`

For every project, the script refuses when the instance file has no `Author` line: it prints "No Author in CLAUDE.local.md - run /setup; the records need the handle." Run `/setup`, then try again.

If the steps ran but a mark still fails, the script says "steps ran but these marks still fail" and names them, and offers `--undo`. `--undo` also refuses when there is nothing to undo.

## A worked example

1. You say `/migrate my-idea`. Claude shows the dry run: some marks are unticked, and it lists the steps that would run.
2. You answer yes to the tag. Claude runs `/save my-idea --tag before-migration`.
3. You give your word. Claude runs `python scripts/forge-migrate.py my-idea --apply` and the script prints `migrated:`.
4. Claude shows a table of the thread origins it guessed. You correct two. Claude writes them into the thread files.
5. Claude makes the ledger and proposes `/save my-idea`. You accept, and the migrated shape reaches the remote.

## See also

- [Upgrade the engine](upgrade-the-engine.md): the upgrade a migration belongs to.
- [Upgrades and migration](../about/upgrades-and-migration.md): why a shape change comes with a migration and why it runs once.
- [Save your work](save-your-work.md): the save that takes the tag before and carries the migrated shape to the remote after.
- [Walk through a list](walk-through-a-list.md): how the guessed thread origins are judged.
- [Scripts](../reference/scripts.md): `forge-migrate.py`, its forms and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
