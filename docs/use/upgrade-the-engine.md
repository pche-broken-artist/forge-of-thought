---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: ad9fcb75599c7a14
inputs:
  - .claude/skills/pull/SKILL.md
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/recipes/release-notes.md#Template
---

# Upgrade the engine

Upgrading the engine means taking its new version from the remote
and then bringing your projects to its conventions, one project at a
time. This page is for you if you run an instance of the forge (one
installation of it) and keep projects in it. It covers the job from
the pull of the engine to the last project brought current.

## When to use it

Use it whenever the engine has moved on at its remote and you want
the new version.
You also use it after a pull you have already made, to bring your
projects to the conventions it brought.

## The command

```
/pull forge
```

`forge` names the engine.
The pull itself is described in
[Pull from the remote](pull-from-the-remote.md).

## What happens

1. **The pull of the engine.** `/pull` says the state of the engine
   against its remote. A clean engine that is behind is pulled, and
   the report says where it moved from and to, with the subjects of
   the commits between.
   You should now see the engine reported as moved, with the list of
   its new commits.

2. **The Action required lines.** After the pull, Claude reads the
   release notes and shows the Action required lines of every
   release the pull crossed. The release notes have one section per
   release, newest first, written for whoever takes upgrades through
   the pull. Action required stands first in every section. Each of
   its lines says what changed and what you are to do in your
   projects after pulling. Read them before anything else.
   You should now see the Action required lines of each release
   crossed, or none where a release asks nothing of you.

3. **The checks, project by project.** Claude offers two checks on
   each project you keep:
   - `/check light <slug>`
   - `/check project <slug>`

   A check is an isolated reviewer that measures a project against
   the current conventions mechanically. Claude runs them only on
   your word. Running a check and settling what it finds is described
   in [Check conformance](check-conformance.md).
   You should now see, for each project checked, either that it
   conforms or a report of findings (a finding is one result of a
   reviewer).

4. **The findings, one at a time.** The findings are worked in a
   walkthrough: one finding per message, each closed with your
   verdict. Claude brings the project current on your word, finding
   by finding. Nothing changes in the project until you say so.
   You should now see each finding settled and the project changed
   only where you accepted it.

5. **A migration, where a release changed the shape of files.**
   Where an Action required line names a migration, Claude offers
   `/migrate <slug>` for each project you keep that is still of the
   old shape. Each project is migrated once, on one clone, and then
   saved with `/save`. On every other clone the project is not
   migrated again: it is pulled with `/pull <slug>`. Every user of
   the engine migrates his own projects, whichever machine or
   instance the clone is on. The migration itself is described in
   [Migrate a project](migrate-a-project.md).
   You should now see the project in the new shape, saved, and on
   any other clone pulled rather than migrated.

## What you have afterwards

You have the engine at its new version.
Each project you chose to bring current conforms to the current
conventions.
A project you left as it is stays valid under the conventions it was
written to. Its nonconformance is a fact the checks report, not a
defect to chase.
One exception holds for the shape of files: a project of the old
shape is read but not written until you migrate it.
Projects record no engine version, and the pull of the engine does
not touch them. Why this is so is explained in
[Upgrades and migration](../about/upgrades-and-migration.md).

## If something goes wrong

- **The engine has unsaved changes.** The pull stops and nothing is
  pulled. The offer is `/save` first, then `/pull forge` again.
- **The engine's history has diverged from its remote.** The pull
  stops and nothing is pulled. The offer is a merge by hand, or
  `/save`, which rebases your commits onto the remote. Then pull
  again.
- **The engine is up to date.** There is nothing to pull and no
  release crossed. Your projects can still be checked at any time.
- **A project was migrated on another clone.** Do not migrate it
  again. Pull it with `/pull <slug>`.

## A worked example

You keep one project, `my-project`, and the engine is behind its
remote.

1. You type `/pull forge`. The engine is clean and behind. It is
   pulled, and the report lists the commits between the old and the
   new version, among them two releases.
2. Claude shows the Action required lines of the two releases. One
   line asks you to run the checks on your projects. The other names
   a migration to a new shape of files.
3. Claude offers `/check light my-project` and
   `/check project my-project`. You say yes. The checks report three
   findings.
4. The three findings are walked one at a time. You accept two and
   reject one. Claude changes `my-project` for the two you accepted.
5. Because `my-project` is of the old shape, Claude offers
   `/migrate my-project`. You run it on this clone, then `/save`.
6. On your second machine you type `/pull forge` and then
   `/pull my-project`. The project arrives there already migrated.

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

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
