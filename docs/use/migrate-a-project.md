---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 97aecf6236fa63ad
inputs:
  - .claude/skills/migrate/SKILL.md
  - scripts/forge-migrate.py
  - templates/project.md
---

# Migrate a project

This page is for you when a release has changed the shape of the files
of a project and you must bring the project to the new shape with
`/migrate`. A migration is part of an upgrade, which is described in
[Upgrade the engine](upgrade-the-engine.md). The principal is whoever's
thinking is forged in the project, and so the one who gives the word
for each step below. A ledger is the state of a project made from its
documents when it is read. A walkthrough is the way of working in which
Claude puts one item at a time to the principal for a verdict. The
[Glossary](../reference/glossary.md) has every other term of the forge
in one line.

## When to use it

Run `/migrate` when a release changed the shape of files and a project
does not yet have it.

- A migration runs once per project.
- It runs on one clone, on `main`.
- Everyone else pulls the migrated project.

The slug `forge` is the forge's own project, a repository of its own
beside the engine. A project that is already in shape needs nothing.
The reason a shape change comes with a migration, and why it runs once,
is given in [Upgrades and migration](../about/upgrades-and-migration.md).

## The command

```
/migrate my-idea
```

Replace `my-idea` with the slug of your project. Without a slug Claude
infers the project from the conversation and asks if it is ambiguous.

## What happens

1. Claude runs the dry run, `python scripts/forge-migrate.py my-idea`,
   and shows its print as it came. The print holds the marks of the
   shape, the steps that would run and what each would change. Nothing
   is changed by it.

   You should now see a list of marks, each ticked or not, and one line
   saying that nothing changed. A project already in shape ends here
   with the line that there is nothing to do.

2. Before the migration a tag is taken, with
   `/save my-idea --tag <name>`. The tag is the way back once the
   migrated project is saved. How a save works is told in
   [Save your work](save-your-work.md).

   You should now see the tag named in the save's answer.

3. On your word, and only then, Claude runs
   `python scripts/forge-migrate.py my-idea --apply`. The script does
   these things:
   - The fields that change with a round leave the headers.
   - The project file is written.
   - What only the ledger knew becomes records and index fields.
   - The hand-kept ledger is kept as an immutable archive, and the
     ledger leaves git.
   - The threads file is cut into one file per thread.
   - The `.gitattributes` file is written.

   A library takes fewer steps. The script commits nothing.

   You should now see a last line that begins with "migrated" and says
   that nothing is committed and `/save` follows.

4. Claude walks through what the script printed, for your judgement.
   Above all it judges the origin the script guessed for each thread.
   This is a walkthrough, written into the thread files at the round's
   end; how it runs is told in
   [Walk through a list](walk-through-a-list.md). Text that was not a
   thread goes where it belongs.

   You should now see the origins confirmed or corrected, and the
   thread files written.

5. Claude makes the ledger and proposes `/save my-idea`. The migrated
   shape reaches the remote by that save.

   You should now see the save's report with the migrated files in it.

## The comments of the templates

`/migrate my-idea --comments` is a step of its own. You run it on your
word, and it is never a condition of a write. In every file made from a
template that is not immutable, the template's comment is replaced by
the one line that names the template. Closed threads, archives,
research and sources are left as they are. The templates themselves,
and the one line a file keeps, are listed in
[Templates](../reference/templates.md).

The course is the same as above:

1. Claude shows the dry run as it came.
2. On your word, Claude runs `--comments --apply`.
3. Claude judges with you what the script printed. A recipe whose
   genre the file does not tell is printed and left. A comment of a
   file's own is left and counted.
4. Claude makes the ledger and proposes `/save my-idea`.

## What you have afterwards

- The project carries its project file and one file per thread.
- The headers of its documents hold no field that changes with a round.
- The hand-kept ledger lies as an archive, and the ledger is out of git.
- The migrated shape is on the remote once you have saved.

## If something goes wrong

The script refuses `--apply` and changes nothing in these cases. For a
project that is a repository of its own:

- "the working tree has unsaved changes to tracked files: save first".
- "behind" or "diverged" against the origin: "/pull first".
- "on branch <name>, not main".

For every project:

- "No Author in CLAUDE.local.md - run /setup; the records need the
  handle." The instance file must carry the `Author` line.

The dry run prints a refusal as "--apply would refuse" with its reasons,
so you see it before you give the word.

The way back:

- Before the save: `python scripts/forge-migrate.py my-idea --undo`.
  It takes back the last `--apply`.
- After the save: the tag taken before the migration.

If the steps ran but a mark still fails, the script says so and names
the undo command.

A project outside git is migrated the same way, with none of git's
refusals. The dry run tells you to take a backup before `--apply`. That
backup is the way back, because `--undo` refuses there with "not under
git". A run that stops midway is finished by running it again.

## A worked example

You have upgraded the engine, and the project `my-idea` is still of the
old shape.

1. You type `/migrate my-idea`.
2. Claude runs the dry run and shows it. The marks for the project file
   and the threads are not ticked, and the dry run lists what each step
   would change.
3. Claude takes the tag with `/save my-idea --tag before-migration` and
   asks for your word.
4. You say yes. Claude runs
   `python scripts/forge-migrate.py my-idea --apply`, and the script
   ends with "migrated".
5. Claude lays the guessed origin of each thread before you, one by one.
   You accept most and correct one. Claude writes the thread files.
6. Claude makes the ledger and proposes `/save my-idea`. You accept,
   and the migrated project reaches the remote.

## See also

- [Upgrade the engine](upgrade-the-engine.md): the upgrade a migration
  belongs to.
- [Upgrades and migration](../about/upgrades-and-migration.md): why a
  shape change comes with a migration and why it runs once.
- [Save your work](save-your-work.md): the save that takes the tag
  before and carries the migrated shape to the remote after.
- [Walk through a list](walk-through-a-list.md): how the guessed
  thread origins are judged.
- [Templates](../reference/templates.md): the templates, and the one
  line a file made from a template keeps of its comments.
- [Scripts](../reference/scripts.md): `forge-migrate.py`, its forms and
  what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
