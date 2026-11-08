---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: b1919b641c68bcd0
inputs:
  - .claude/skills/pull/SKILL.md
  - .claude/skills/migrate/SKILL.md
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/recipes/release-notes.md#Instructions
  - CLAUDE.md#Persistence (git)
---

# Upgrade the engine

An upgrade of the engine is a pull of its `main` branch followed by
the work that brings your projects to the conventions the new
release holds. This page is for you, the user who keeps the engine
and one or more projects under it, and it walks the whole job from
the pull to the last save: what `/pull` shows you, what the two
checks measure, and what to do when a release changed the shape of
files. Each step has its own page; this one joins them into one
job.

## When to use it

Use it whenever the engine has moved on the remote and you want to
take the new release. The engine is one git repository, and its
`main` branch is the released line. The upgrade channel is a
fast-forward of that branch, done by `/pull`. Your projects are
repositories of their own, each outside the engine's repository.
A project records no engine version. The pull of the engine does
not touch any project.

A project left as it is stays valid under the conventions it was
written to. Its nonconformance with the current conventions is a
fact to report, never a defect to chase. Bringing a project to the
newer conventions is your explicit decision, made project by
project and never assumed. One case is narrower: where a release
changed the shape of files, a project of the old shape is read and
not written until you migrate it. Why that is so is said on
[Upgrades and migration](../about/upgrades-and-migration.md).

## The command

The job starts with one command and continues with three more,
each run on your word:

```
/pull
```

Bare, `/pull` looks at the engine and at every project with an
origin. `/pull forge` takes the engine alone. Then, for each project
you keep, with a placeholder slug in place of yours:

```
/check light my-project
/check project my-project
```

And, where a release changed the shape of files, once per project:

```
/migrate my-project
```

## What happens

1. **`/pull` reports the state of every repository in scope.** It
   says, as a fact, whether each one is up to date, behind, ahead,
   diverged, without an origin or not under git. The same run says
   what waits on GitHub outside git, the open pull requests and the
   unanswered discussions, or that it could not read them and why.
   Nothing of that is pulled, merged or answered. The pull itself
   is on [Pull from the remote](pull-from-the-remote.md).
   You should now see one line per repository with its state.

2. **`/pull` fast-forwards what is clean and behind.** Claude (the
   machine, your cognitive extension in the forge) pulls only a
   clean repository that is behind. It merges nothing and runs no
   check unasked. It relays where each repository moved from and
   to, and the subjects of the commits between.
   You should now see the engine's `main` at the new release, with
   the commits it crossed listed by subject.

3. **Claude shows the Action required lines of the releases
   crossed.** After a pull of the engine it reads `RELEASE-NOTES.md`
   and shows the Action required lines of every release whose
   commit the pull listed. Action required stands first in every
   section of the release notes. Each of its lines carries, word for
   word, the Action a change was recorded with: what you must do
   after that change.
   You should now see the Action required lines, or none where a
   release asked nothing of you.

4. **Claude offers the two checks on each project you keep.** It
   offers `/check light <slug>` and `/check project <slug>` and runs
   them only on your word. Where an Action required line names a
   migration, it also offers `/migrate <slug>` for each project of
   the shape before the migration.
   You should now see the offers, one per project, waiting for your
   word.

5. **The checks measure each project against the current
   conventions.** A check is a mechanical measure of conformance,
   never of substance or quality. `/check light <slug>` and
   `/check project <slug>` say what the conventions changed for that
   project. Their findings are walked one at a time, as a
   walkthrough, that is one item per message, each settled by your
   decision before the next. For an upgrade of a few lines Claude
   brings the project current on your word, finding by finding.
   Running a check and settling its findings is on
   [Check conformance](check-conformance.md).
   You should now see each finding in turn, and the project current
   for every one you accepted.

6. **Where a release changed the shape of files, each project of
   the old shape is migrated once.** `/migrate <slug>` runs a dry
   run first and shows the marks of the shape, the steps that would
   run and what each would change. A project already in shape ends
   there. On your word, and only then, it applies the migration.
   The migration commits nothing by itself. A migration runs once
   per project, on one clone, on `main`, under git or not. It is
   never run on Claude's own judgement. What needs your judgement
   afterwards, and the way back should anything be wrong, is on
   [Migrate a project](migrate-a-project.md).
   You should now see the dry run, then the print of the applied
   migration.

7. **The migrated project is saved.** Claude makes the ledger (the
   project's state report, built from its documents at read time and
   never in git) and proposes `/save <slug>`. The migrated shape
   reaches the remote by that save.
   You should now see the save proposed, and after your word the
   push reported.

8. **Everyone else pulls the migrated project.** A second clone of
   the same project does not migrate again: it pulls, with
   `/pull <slug>`, and takes the migrated shape from the remote.
   You should now see, on that clone, the report of the pull.

## What you have afterwards

- The engine's `main` at the new release.
- The Action required lines of the releases crossed, read and
  acted on.
- Each project you chose to bring current measured by the two
  checks, its findings settled one by one.
- Each project of the old shape migrated once, saved, and on the
  remote in its new shape.
- Any project you left as it is, unchanged and still valid under
  the conventions it was written to.

## If something goes wrong

- **A repository has unsaved changes or a diverged history.** `/pull`
  stops there with one offer: `/save` first, or a merge by hand or
  by `/save`, which rebases your commits onto the remote. Nothing is
  pulled from that repository.
- **The state of GitHub could not be read.** `/pull` says so and
  why. It pulls what git knows as usual.
- **The merge driver is not registered on this machine.** The
  status run says so. An unregistered clone falls back to a conflict
  in silence, so register it through `/setup` before you pull.
- **`/migrate` is run off `main`, or on a repository behind or
  diverged from its origin.** It refuses and offers `/pull`. The
  same holds for every command that makes a derived file.
- **A project is already in shape.** The dry run of `/migrate` ends
  there. Nothing is applied.
- **A project of the old shape is not yet migrated.** Nothing
  writes into it: the state map, the checks and every writing
  command say what `templates/project.md` says and stop. The
  project is read, not written, until you migrate it.
- **Something is wrong after the migration.** The way back belongs
  to the script, `scripts/forge-migrate.py`, as its help header
  says. A tag before the migration is taken through
  `/save <slug> --tag <name>`, before the migration is applied.

## A worked example

You keep the engine and one project, `my-project`, both under git
with an origin. The engine has moved on the remote.

```
/pull
```

Claude reports the state: the engine is behind, `my-project` is up
to date. Nothing waits on GitHub. It pulls the engine and lists the
commits crossed by subject, one of them a release. It reads
`RELEASE-NOTES.md` and shows the Action required lines of that
release. One of them says that the release changed the shape of
files and names `/migrate`. Claude offers `/check light my-project`,
`/check project my-project` and `/migrate my-project`.

```
/check light my-project
```

The check files its findings. Claude walks them one at a time. You
accept the two that the conventions changed, and Claude brings the
project current on your word.

```
/check project my-project
```

The check finds nothing more.

```
/migrate my-project
```

The dry run shows the marks of the old shape, the steps that would
run and what each would change. You give the word, and Claude
applies the migration. It shows you what needs your judgement, you
settle it, and Claude makes the ledger.

```
/save my-project
```

The migrated shape reaches the remote. On your second machine,
`/pull my-project` takes it from there. No migration runs twice.

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

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
