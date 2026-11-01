---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 4f7d872d7d0a0dcc
inputs:
  - .claude/skills/pull/SKILL.md
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/recipes/release-notes.md#Instructions
---

# Upgrade the engine

Upgrading the engine means taking its new version from the remote
and then bringing your projects to its conventions, one project at a
time. This page is for anyone who keeps an instance of the engine
(one installation of it) with projects of their own. It covers what
you do after the pull: read what the release asks of you, check each
project and, where the release changed the shape of files, migrate
it.

## When to use it

Use it after `/pull` has moved the engine forward. The pull itself
is described in [Pull from the remote](pull-from-the-remote.md).

A project records no engine version. The pull of the engine does
not touch your projects. Each project is measured against the
current conventions only when you check it. Why it is so is
explained in [Upgrades and migration](../about/upgrades-and-migration.md).

## The command

After the pull, for each project you keep, with `my-project` as a
placeholder slug:

```
/check light my-project
```

and then:

```
/check project my-project
```

Where the release changed the shape of files:

```
/migrate my-project
```

## What happens

1. **You read the Action required lines.** After a pull of the
   engine, `/pull` reads the release notes and shows the Action
   required lines of every release the pull crossed. In the release
   notes, Action required stands first in every section of a
   release. It carries word for word what a change asks you to do.
   You should now see the lines that say what each release asks of
   you, or no such lines where nothing is asked.
2. **Claude offers the checks.** `/pull` offers `/check light <slug>`
   and `/check project <slug>` on each project you keep. It runs
   them only on your word. The checks measure the project against
   the current conventions and say what the conventions changed.
   Running a check and settling its findings is described in
   [Check conformance](check-conformance.md). You should now see
   the report of each check, with its findings (the results of a
   check), or no findings where the project already conforms.
3. **You walk the findings.** The findings are worked one at a time,
   and on each you give your word. Claude brings the project current
   on your word, never on its own judgement. You should now see each
   finding settled, and the project changed only where you agreed.
4. **Where the release changed the shape of files, you migrate.** An
   Action required line says so when a release changed the shape of
   files. Then `/pull` offers `/migrate <slug>` for each project you
   keep that is still of the old shape. Each such project is
   migrated once, with `/migrate <slug>`, on one clone. The
   migration is described in [Migrate a project](migrate-a-project.md).
   You should now see the project in the new shape of files.
5. **You save, and pull on the other clones.** Save the migrated
   project. On another clone of the same project, pull it rather
   than migrate it again. You should now see the project in the new
   shape on every clone.

## What you have afterwards

The engine is at its new version. Each project you checked conforms
to the current conventions as far as you agreed. Each project of an
old shape that you migrated is in the new shape, and the engine can
write into it again.

A project you leave as it is stays valid under the conventions it
was written to. A difference from the current conventions in a
finished or dormant project is a fact to report, never a defect to
chase. Bringing a project to newer conventions is your decision, per
project.

## If something goes wrong

- **The engine will not write into a project.** After a release that
  changed the shape of files, a project of the old shape is read and
  not written until you migrate it. The engine cannot write two
  shapes. Migrate the project with `/migrate <slug>`.
- **The pull stopped.** A repository with unsaved changes or with a
  diverged history is not pulled. The offer is `/save` first, or a
  merge by hand or by `/save`. See
  [Pull from the remote](pull-from-the-remote.md).

## A worked example

You keep one project, `my-project`, and run `/pull`. The engine
moves forward across two releases. Claude shows their Action
required lines: one asks you to look at a field of your project
file, the other says the release changed the shape of files and
asks for a migration.

Claude offers `/check light my-project` and
`/check project my-project`. You say yes. The checks report a few
findings. You walk them one at a time, and Claude fixes each one you
accept.

Claude then offers `/migrate my-project`, since the project is of
the old shape. You give your word. The project is migrated on this
clone, and you save it. On your other machine you pull the project
instead of migrating it a second time.

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

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
