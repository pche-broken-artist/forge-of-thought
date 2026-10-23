---
generated: 2026-10-23
version: 5.33
made: derived
inputs-hash: ab6d0a3e195468ad
inputs:
  - .claude/skills/pull/SKILL.md
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/recipes/release-notes.md#Template
---

# Upgrade the engine

Upgrading the engine means taking its new version from the remote
and then bringing each of your projects to the conventions that
version holds. This page is for you as the one who runs the engine
and keeps projects in it. It covers the job that follows a pull of
the engine: what you read, which checks you run on each project, and
when a project needs a migration.

## When to use it

Use it after `/pull` has fast-forwarded the engine to a newer
version. The pull itself is described in [Pull from the
remote](pull-from-the-remote.md). The pull moves the engine only.
Your projects are not touched by it, and a project records no
version of the engine it was made with.

## The command

After the pull, the job runs project by project. For a project with
the placeholder slug `my-project`, the first command is:

```
/check light my-project
```

The other commands of the job are `/check project my-project` and,
only where a release asks for it, `/migrate my-project`.

## What happens

1. **Read the Action required lines.** After a pull of the engine,
   `/pull` reads the release notes and shows the Action required
   lines of every release the pull crossed. In the release notes,
   Action required stands first in the section of every release. Each
   line says what changed and what you do in your projects after
   pulling.
   You should now see the Action required lines of the crossed
   releases, and an offer of the two checks for each project you
   keep.

2. **Measure each project against the current conventions.** For
   each project, run `/check light <slug>` and `/check project
   <slug>`. A check is an isolated reviewer that tests mechanical
   conformance with the conventions. It runs as a subagent (a
   separate agent that never sees your conversation). Claude runs the
   checks only on your word. Between them they say what the new
   conventions changed for that project. How a check runs is
   described in [Check conformance](check-conformance.md).
   You should now see the findings of each check (a finding is one
   result of a reviewer), or the word that the check found nothing.

3. **Walk the findings and bring the project current.** The findings
   are worked in a walkthrough (a review of a list one item at a
   time, each settled by the principal's verdict). The principal is
   the person whose thinking the project forges: here, you. Claude
   brings the project to the current conventions on your word, as
   the Action required lines say to do.
   You should now see each finding settled and the changes you
   agreed made in the project.

4. **Migrate where a release changed the shape of files.** Where a
   release changed the shape of files, its Action required line says
   so. `/pull` then offers `/migrate <slug>` for each project you keep
   that is still of the shape before the migration. Each such project
   is migrated once, on one clone, and then saved with `/save`. A
   project already migrated on another clone is brought in by `/pull`,
   not migrated again. The migration is described in [Migrate a
   project](migrate-a-project.md).
   You should now see each project of the old shape migrated and
   saved, or pulled where it was migrated elsewhere.

## What you have afterwards

The engine is at its new version. Each project you chose to bring
current conforms to the current conventions. A project you leave as
it is stays valid under the conventions it was written to. Its
nonconformance is a fact the checks report, not a defect to chase.
Bringing a project to newer conventions is your decision, made per
project. A project of the old shape of files is the one exception:
it is read and not written until it is migrated. Why a project
records no engine version, and when a release comes with a
migration, is explained in [Upgrades and
migration](../about/upgrades-and-migration.md).

## If something goes wrong

- **The engine has unsaved changes.** `/pull` stops for it and pulls
  nothing. It offers `/save` first.
- **The engine's history has diverged from the remote.** `/pull`
  stops for it and pulls nothing. It offers a merge by your own hand,
  or `/save`, which rebases your own commits onto the remote.
- **Claude does not write into a project.** The project is still of
  the shape before a migration, and it is read, not written. Migrate
  it with `/migrate <slug>`, or pull it where it was migrated on
  another clone.

## A worked example

You keep two projects, `my-project` and `other-project`.

1. You run `/pull`. The engine moves forward across two releases.
   `/pull` shows their Action required lines. One line says a release
   changed the shape of files.
2. For `my-project` you run `/check light my-project` and `/check
   project my-project`. The checks report a few findings. You walk
   them one at a time, and Claude brings the project current on your
   word.
3. `/pull` offered `/migrate my-project`, because the project is of
   the old shape. You run it on this clone, then `/save`.
4. `other-project` was already migrated and saved on another clone.
   You run `/pull other-project` here instead of migrating it again.

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

Generated on 2026-10-23 for version 5.33 from the files the
front-matter names; never edited by hand.
