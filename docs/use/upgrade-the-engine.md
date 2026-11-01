---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 21b9805b97ab4d71
inputs:
  - .claude/skills/pull/SKILL.md
  - .claude/skills/migrate/SKILL.md
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/recipes/release-notes.md#Instructions
  - CLAUDE.md#Persistence (git)
---

# Upgrade the engine

An upgrade of the engine is a pull of its `main`, followed by the
work of bringing the projects you keep to the conventions the new
releases brought. This page is for you, the user who runs the forge
and keeps one or more projects under it. It takes you from the moment
`/pull` has moved the engine to the moment every project you keep is
either current again or deliberately left as it is. The pull itself
is the job of [Pull from the remote](pull-from-the-remote.md); this
page begins where that one ends.

## When to use it

Use this job after `/pull` has pulled the engine and reported the
commits it crossed. The upgrade of the engine is that pull: a
fast-forward of `main`. What follows it is the subject of this page.

Nothing of this job is needed after a pull of a project alone. A
project records no engine version. The pull of the engine does not
touch the projects.

Not every project needs to be brought current. A project stays valid
under the conventions it was written to. Nonconformance of a finished
or dormant project is a fact to report, never a defect to chase.
Bringing a project to newer conventions is your explicit decision,
made per project and never assumed. One case is different: where a
release changed the shape of files, a project of the old shape is
read and not written until you migrate it.

## What you do

The commands of the job, in the order they are used:

```
/pull
/migrate my-project
/check light my-project
/check project my-project
```

`my-project` is a placeholder for the slug of one of your projects.
`light` and `project` are the two checks the job uses, named as the
check roster names them. `/migrate` is used only where an Action
required line names a migration; the other lines are run for every
project you keep.

## What happens

1. **Claude shows the Action required lines.** After the pull of
   the engine, Claude reads `RELEASE-NOTES.md` and shows the Action
   required lines of every release the pull crossed, that is, every
   release whose commit the pull script listed. In the release notes
   the Action required group stands first in every release's
   section, before everything else of that release. Each of its
   lines carries, word for word, the `Action` of a record of the
   engine's history: what you must do or know after that change.
   You should now see one list of Action required lines, by
   release, before anything has been run on any project.

2. **Where a line names a migration, each project of the old shape
   is migrated once.** A release that changes the shape of files
   says so in its Action required line and comes with a migration.
   Claude offers `/migrate <slug>` for each project you keep that is
   of the shape before the migration; the mark of the shape is
   `templates/project.md`. This step comes before the checks for
   such a project. Until a project is migrated, nothing writes into
   it: the state map, the checks and every writing command say what
   `templates/project.md` says and stop. The migration runs once per
   project, on one clone, on `main`, under git or not; everyone else
   pulls. It runs in this order:
   - A dry run, `python scripts/forge-migrate.py <slug>`, whose
     print Claude shows as it came: the marks of the shape, the
     steps that would run and what each would change. A project
     already in shape ends here.
   - On your word, and only then, the run with `--apply`. The
     script commits nothing.
   - Claude's judgement of what the script printed: the origins it
     guessed for the threads it cut (the open matters of the intent,
     now one file each under `threads/`), the text after the last
     thread that was not a thread, and the Waiting lines without an
     ID. The origins are worked as a walkthrough, that is, one item
     per message with your verdict on each, Claude's judgement in
     one table and your corrections written into the thread files at
     the round's end. What is not a thread goes where it belongs,
     usually a record of the intent's history.
   - The ledger remade, `python scripts/forge-ledger.py <slug>`
     (the ledger is the project's state, built from its documents
     at read time), and the proposal of `/save <slug>`. The
     migrated shape reaches the remote by that save.
   The whole of this step is the job of
   [Migrate a project](migrate-a-project.md). You should now see the
   proposal `/save <slug>` and, once you have said yes, the migrated
   project on its remote, ready for every other clone to pull.

3. **The two checks measure each project against the current
   conventions.** Claude offers `/check light <slug>` and
   `/check project <slug>` on each project you keep, and runs them
   only on your word. The checks say what the conventions changed
   for that project. Running a check and what its report looks like
   is the job of [Check conformance](check-conformance.md). You
   should now see, for each project you ran them on, what each check
   found or that it found nothing.

4. **The findings are settled one at a time.** The findings are
   walked as a walkthrough, one finding per message, with your
   verdict on each. The Action required lines of the release notes
   say what to do. Claude brings the project current on your word,
   for an upgrade of a few lines. A finding you decline stays a fact
   reported, not a defect chased. You should now see each change
   proposed as one step and written on your yes, and no change made
   without it.

## What you have afterwards

- The engine on the new `main`.
- Each project you keep in one of two states: current under the
  conventions of the new releases, or left as it is by your
  decision and still valid under the conventions it was written to.
- Where a release changed the shape of files: each project of the
  old shape migrated once, its migrated shape on its remote, its
  ledger remade, and every other clone of it brought current by a
  pull, not by a second migration.
- The Action required lines of the releases crossed read, and each
  either done or deliberately left.

## If something goes wrong

- **The engine was not pulled.** A repository with unsaved changes
  or with a diverged history stops at the pull, with one offer:
  `/save` first, or a merge by hand or by `/save`. Nothing is pulled
  from it, and the job of this page has not begun. See
  [Pull from the remote](pull-from-the-remote.md).
- **`/migrate` refuses.** It runs on `main` only. It refuses a
  repository behind or diverged from its origin and offers `/pull`.
- **The dry run says the project is already in shape.** There is
  nothing to migrate. The migration ends there.
- **A check or a command on a project of the old shape stops.** It
  says what `templates/project.md` says and does nothing. Migrate
  the project first, then run the checks.
- **A project was already migrated on another clone.** Do not
  migrate it again. The migration runs once per project, on one
  clone, and everyone else pulls. The script refuses a second
  migration; its refusals are said in its help header.
- **The migration went wrong.** The way back is the script's and is
  said in its help header. A tag before the migration can be taken
  through `/save <slug> --tag <name>`, before `--apply`, so that the
  state before the migration has a name.
- **The project is outside git.** It is migrated the same way; the
  migration runs under git or not. The forge runs no git on such a
  project, so there is nothing for it to save or to pull.

## A worked example

You run `/pull` with nothing else. Claude reports the engine behind
its origin and clean, pulls it, and lists the commits between the
old and the new `main`. Two of them are releases. Claude reads
`RELEASE-NOTES.md` and shows the Action required lines of both:

- The newer release: a renamed front-matter key in the recipes; the
  line says which key and what to rename it to.
- The older release: a changed shape of files; the line says that
  each project of the old shape is migrated with `/migrate <slug>`.

You keep one project, `my-project`, on this clone and on a second
machine. Claude offers `/migrate my-project`, because the project is
of the old shape. You accept. The dry run prints the marks of the
shape, the three steps that would run and what each would change.
You say `write`, Claude runs the migration with `--apply`, and the
script prints what it cut and what it guessed. Claude lays out the
origins of the threads it cut as one table; you correct one of them,
and the thread files are written at the end of the round. Claude
remakes the ledger and proposes `/save my-project`. You accept, and
the migrated shape reaches the remote.

Claude then offers `/check light my-project` and
`/check project my-project`. You accept both. The light check finds
nothing. The project check finds the renamed key in two recipes, as
the newer release's Action required line said it would. Claude walks
the two findings one at a time; you accept each; Claude renames the
key in both recipes on your word.

On the second machine you run `/pull`. The engine and `my-project`
are both behind and clean. Both are pulled. Claude shows the same two
Action required lines. The dry run of `/migrate my-project` says the
project is already in shape, and the migration ends there. Nothing
else is to be done on that machine.

## See also

- [Pull from the remote](pull-from-the-remote.md): the pull itself.
- [Check conformance](check-conformance.md): running a check and
  settling its findings.
- [Migrate a project](migrate-a-project.md): the migration of a
  project to a new shape of files.
- [Upgrades and migration](../about/upgrades-and-migration.md): why a
  project records no engine version and when a migration comes with
  a release.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
