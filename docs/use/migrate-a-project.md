---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: b5128254f3490622
inputs:
  - .claude/skills/migrate/SKILL.md
  - scripts/forge-migrate.py
  - templates/project.md
---

# Migrate a project

This page is for the user who has upgraded the engine and now has to bring a project to the shape of files the new release expects. `/migrate` does that: it runs a script that changes the files, and Claude then helps the principal (the person whose thinking is being forged) judge what the script guessed. The upgrade it belongs to is described in [Upgrade the engine](upgrade-the-engine.md).

## When to use it

Use it when a release has changed the shape of files and a command tells you that your project is of the older shape. A project without a project file is of the older shape. The one remedy is `/migrate`.

A migration runs once per project, on one clone, on `main`. Everyone else who works on the project pulls the migrated project and does not migrate it again. Why a shape change comes with a migration, and why it runs once, is explained in [Upgrades and migration](../about/upgrades-and-migration.md).

## The command

```
/migrate my-idea
```

The slug is optional. Without it, Claude infers the project from context and asks if that is ambiguous. The slug `forge` is the engine's own project.

## What happens

1. Claude runs the dry run, `python scripts/forge-migrate.py <slug>`, and shows its print as it came. The print has the marks of the shape, the steps that would run and what each would change. You should now see, for every mark, whether it holds, and for every missing one the change it would make. A project that is already in shape ends here.

2. On your word, and only then, Claude runs `python scripts/forge-migrate.py <slug> --apply`. The script does these steps, in this order, and skips those whose mark already holds:
   - The fields that change with a round leave the headers of the artefacts, work specifications, recipes, indexes and the documentation map.
   - The project file is written, with the project's slug, its kind and its language.
   - What only the hand-kept ledger knew becomes records and index fields.
   - The hand-kept ledger is kept as an immutable archive, and the ledger leaves git.
   - The threads file is cut into one file per thread.
   - The `.gitattributes` file is written.

   A library takes fewer steps: the headers, the project file, the records and the ledger, and the attributes. The script commits nothing. You should now see the script's print of what it did, each step confirming its own mark.

3. Claude walks through what the script printed, for your judgement. Above all this is the origin the script guessed for each thread it cut. Claude lays the guesses out as one table of its own judgement from the thread texts, and you correct what is wrong. This is a walkthrough (a list worked with the principal's verdicts, described in [Walk through a list](walk-through-a-list.md)), and the corrections are written into the thread files at the round's end. Text that was not a thread goes where it belongs, usually a record of the intent's history. Waiting lines without an ID, which have no home in the records, are raised too. You should now see each thread with the origin you confirmed.

4. Claude makes the ledger, a state report built from the documents, and proposes `/save <slug>`. The migrated shape reaches the remote by that save, described in [Save your work](save-your-work.md). You should now see the save proposed with the migrated files in it.

## What you have afterwards

- A project file, one file per thread, the attributes file and headers without the fields that change with a round.
- The old hand-kept ledger as an archive that is never edited, and the ledger out of git.
- Records and index fields holding what only the ledger knew.
- Uncommitted changes, until the save. The script itself commits nothing.

## The way back

Before the save, run `python scripts/forge-migrate.py <slug> --undo`. It takes back the last `--apply`.

After the save, the way back is the tag taken before the migration.

## A project outside git

A project that is not a repository of its own is migrated the same way, with none of git's refusals below. Because nothing is recorded in git, the way back is a backup that you take before `--apply`; the dry run tells you to take it. `--undo` refuses on such a project. A run that stops midway is finished by running it again, because the marks of the shape are the memory.

## If something goes wrong

`--apply` refuses in these cases, for a project that is a repository of its own:

- There are unsaved changes to tracked files. Save or set them aside first. An untracked file is no risk.
- The branch is behind or diverged from its origin. Pull first.
- The branch is not `main`. The migration is one large change, run once, on one clone.

For every project, `--apply` also refuses when the instance file has no `Author` line, because the author of every record the script writes is that handle. Add the line to the instance file and run again.

If the result is wrong before the save, use `--undo`. The forms of the script and what it needs are listed in [Scripts](../reference/scripts.md).

## A worked example

You have upgraded the engine and a command says that `my-idea` is of the older shape.

1. You type `/migrate my-idea`. Claude runs `python scripts/forge-migrate.py my-idea` and shows the marks. The project file is missing, the headers still carry fields that leave, the threads are in one file, and the ledger is in git.
2. You say to go ahead. Claude runs `python scripts/forge-migrate.py my-idea --apply`. The print lists each step and confirms each mark.
3. Claude shows a table of the threads with the origin it guessed for each. You correct two of them. Claude writes the corrections into the thread files at the end of the round and puts a stray paragraph that was not a thread into the intent's history.
4. Claude makes the ledger and proposes `/save my-idea`. You accept, and the migrated shape reaches the remote.

Terms such as ledger, thread and record are defined in the [Glossary](../reference/glossary.md).

## See also

- [Upgrade the engine](upgrade-the-engine.md): the upgrade a migration belongs to.
- [Upgrades and migration](../about/upgrades-and-migration.md): why a shape change comes with a migration and why it runs once.
- [Save your work](save-your-work.md): the save that carries the migrated shape to the remote.
- [Walk through a list](walk-through-a-list.md): how the guessed thread origins are judged.
- [Scripts](../reference/scripts.md): `forge-migrate.py`, its forms and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
