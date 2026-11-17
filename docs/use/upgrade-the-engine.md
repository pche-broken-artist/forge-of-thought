---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 019a8ff5a0330574
inputs:
  - .claude/skills/pull/SKILL.md
  - .claude/skills/migrate/SKILL.md
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/recipes/release-notes.md#Instructions
---

# Upgrade the engine

Upgrading the engine is the job that follows a
[pull](pull-from-the-remote.md) of a new version of the
[engine](../reference/glossary.md) (the forge itself, as distinct
from your projects). You read what the new releases ask of you. Then
you bring your projects, one at a time, to the current
[conventions](../reference/glossary.md). This page is for whoever
works with the forge and keeps projects in it.

## When to use it

Use it after a pull of the engine has crossed one or more releases.

The engine does not know your projects. A project records no engine
version, and the pull of the engine does not touch it. Bringing a
project to the newer conventions is your decision, made for each
project on its own and never assumed. A project you leave as it is
stays valid under the conventions it was written to. Why this is so
is explained in
[Upgrades and migration](../about/upgrades-and-migration.md).

## What you do

For each project you want to bring current, type the two checks, with
the project's slug in place of `my-project`:

```
/check light my-project
/check project my-project
```

`light` and `project` are the names of two
[checks](check-conformance.md). Each measures the project against the
current conventions.

Where an Action required line of the release notes names a
[migration](migrate-a-project.md), type this as well, for each
project of the old shape:

```
/migrate my-project
```

Claude offers these commands after the pull. Each runs only on your
word.

## What happens

Steps 3 and 4 are taken project by project.

1. **Claude shows the Action required lines.** After the pull of the
   engine, it reads the [release notes](../reference/glossary.md)
   (`RELEASE-NOTES.md`) and shows the Action required lines of every
   release the pull crossed. These lines stand first in every section
   of the release notes. Each carries, word for word, the action
   recorded with a change. They say what to do.

   You should now see the Action required lines of the releases
   between the engine you had and the engine you have.

2. **Claude offers the checks and the migration.** It offers
   `/check light <slug>` and `/check project <slug>` on each project
   you keep. Where an Action required line names a migration, it
   also offers `/migrate <slug>` for each project you keep that is of
   the shape before the migration. It runs none of them unasked.

   You should now see the offers, named for each project you keep.

3. **Where a release changed the shape of files, you migrate each
   project of the old shape.** The Action required line of that
   release says that it did. A migration runs once for each project,
   on one clone of it, on `main`. Until a project of the old shape is
   migrated, it is read and not written.

   `/migrate my-project` first shows a dry run (a run that changes
   nothing):

   - the marks of the project's shape
   - the steps that would run
   - what each step would change

   On your word, and only then, the migration is applied. It commits
   nothing. Claude judges with you what the migration printed and
   proposes to [save](../reference/glossary.md) the project with
   `/save my-project`. The migrated shape reaches the remote (the
   repository the project is pulled from) by that save. Everyone else
   who works on the project pulls the migrated project.

   You should now see the dry run and, once the migration is applied,
   the proposal to save the project.

4. **You run the two checks on the project.**
   `/check light my-project` and `/check project my-project` measure
   the project against the current conventions and say what the
   conventions changed. The Action required lines say what to do
   about it. The findings (the results a check returns) are settled
   with you as [Check conformance](check-conformance.md) describes.
   Where the upgrade is a matter of a few lines, Claude brings the
   project current on your word.

   You should now see what each check found in the project.

## What you have afterwards

- The engine in its new version.
- Every project you brought current: at the current conventions, each
  change made on your word.
- Every project you migrated: in the new shape of files and saved,
  the migrated shape on the remote for everyone else to pull.
- Every project you left as it is: unchanged, and valid under the
  conventions it was written to.

What a check finds in a finished or dormant project is a fact to
report. It is not a defect that has to be removed.

Where a release changed the shape of files, a project left in the old
shape is read and not written until you migrate it.

## If something goes wrong

- **The engine was not pulled.** A repository with unsaved changes or
  with a diverged history is not pulled. Claude stops there with one
  offer: `/save` first, or a merge by hand or by `/save`, which
  rebases your commits onto the remote. The pull itself is described
  in [Pull from the remote](pull-from-the-remote.md).
- **The dry run says the project is already in shape.** `/migrate`
  ends there. Nothing is to migrate.
- **Someone else has already migrated the project.** A migration runs
  once for each project, on one clone. Do not migrate the project
  again. Pull it with `/pull my-project`.
- **`/migrate` refuses to run.** A migration runs on `main` and on
  one clone. The refusals come from the script the command runs
  (`scripts/forge-migrate.py`), and its help header describes the
  script in full. The command is described in
  [Migrate a project](migrate-a-project.md).
- **Something is wrong after a migration.** The way back is described
  in the help header of `scripts/forge-migrate.py`. The tag before
  the migration is taken through `/save my-project --tag <name>`,
  before the migration is applied.
- **Nothing can be written into a project.** After a release that
  changed the shape of files, a project of the old shape is read and
  not written until it is migrated. Migrate it, or leave it as it is.

## A worked example

You have pulled the engine, and the pull crossed one release that
changed the shape of files. You keep three projects, all of the old
shape:

- `my-project`: in work, and to be brought current.
- `shared-project`: worked on by you and a colleague.
- `old-project`: finished.

1. Claude shows the Action required lines of the release. One of them
   says that the release changed the shape of files and names the
   migration. Claude offers `/check light` and `/check project` on
   each of the three projects, and `/migrate` for each.
2. You type `/migrate my-project`. Claude shows the dry run. You give
   your word, and the migration is applied. Claude judges with you
   what the migration printed and proposes `/save my-project`. You
   accept, and the migrated shape reaches the remote.
3. You type `/check light my-project` and `/check project my-project`.
   The checks say where the project differs from the current
   conventions. The findings are settled, and Claude brings the
   project current on your word.
4. You and your colleague agree that the colleague migrates
   `shared-project`. The colleague runs the migration on one clone
   and saves the project. You then type `/pull shared-project` and
   have the migrated project. You do not migrate it again.
5. You decline every offer for `old-project`. It stays as it is,
   valid under the conventions it was written to. You can read it.
   Nothing is written into it until you migrate it.

## See also

- [Pull from the remote](pull-from-the-remote.md): the pull itself.
- [Check conformance](check-conformance.md): running a check and
  settling its findings.
- [Migrate a project](migrate-a-project.md): the migration of a
  project to a new shape of files.
- [Upgrades and migration](../about/upgrades-and-migration.md): why a
  project records no engine version and when a migration comes with a
  release.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
