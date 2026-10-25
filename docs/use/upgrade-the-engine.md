---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: b97d92cae6fa0352
inputs:
  - .claude/skills/pull/SKILL.md
  - projects/forge/10-intent.md#POS.0940
  - projects/forge/10-intent.md#POS.0820
  - projects/forge/recipes/release-notes.md#Instructions
---

# Upgrade the engine

Upgrading the engine means taking its new version from the remote
and then bringing your projects to its conventions, one project at a
time. This page is for anyone who runs an instance of the forge (one
installation of the engine with its projects) and has just pulled,
or is about to pull, a new version of the engine. It covers the job
after the pull. The pull itself is on its own page.

## When to use it

Use it when the engine is behind its remote and you want the new
version. Use it again after the pull, whenever you want a project
you keep to follow the conventions the new version brings.

A project records no engine version. The pull of the engine does not
touch your projects. A project you leave as it is stays valid under
the conventions it was written to. If a release changed the shape of
files, a project of the old shape is still read, but nothing writes
into it until it is migrated. Why it is so is on
[Upgrades and migration](../about/upgrades-and-migration.md).

## The command

```
/pull forge
```

`forge` names the engine. The rest of the job runs through the
commands Claude offers after the pull, each on your word.

## What happens

1. **Pull the engine.** Claude looks at the remote first and says
   whether the engine is up to date, behind, ahead or diverged. Only
   a clean engine that is behind is pulled. The details are on
   [Pull from the remote](pull-from-the-remote.md).
   You should now see where the engine moved from and to, and the
   subjects of the commits in between.

2. **Read the Action required lines.** Claude reads the release
   notes and shows the Action required lines of every release the
   pull crossed. Action required stands first in every section of
   the release notes. It carries, word for word, what a change asks
   you to do.
   You should now see the Action required lines of the releases you
   have just taken, or none where a release asked nothing of you.

3. **Check each project.** Claude offers two checks on each project
   you keep, and runs them only on your word:
   - `/check light <slug>`
   - `/check project <slug>`

   Both measure the project against the current conventions, so
   their findings (the results a check reports) say what the new
   conventions changed for that project. Running a check and
   settling its findings is on
   [Check conformance](check-conformance.md).
   You should now see the findings of each check, or the word that
   it found nothing.

4. **Walk the findings and bring the project current.** The findings
   are worked one at a time in a walkthrough (one item per message,
   each closed with your verdict). Claude brings the project to the
   current conventions on your word, never on its own judgement.
   You should now see the changes you agreed made in the project's
   files.

5. **Migrate, where a release changed the shape of files.** A
   release that changed the shape of files says so in its Action
   required line. Claude then offers `/migrate <slug>` for each
   project you keep that is still of the old shape. Each such
   project is migrated once, on one clone, and then saved. Where the
   project was already migrated on another clone, you pull it
   instead of migrating it again. The migration itself is on
   [Migrate a project](migrate-a-project.md).
   You should now see the project in the new shape, saved.

## What you have afterwards

- The engine at its new version.
- Each project you chose to bring forward following the current
  conventions, its findings settled.
- Each project you left as it is, still valid under the conventions
  it was written to. A project of an old shape stays readable, and
  it is written to again once you migrate it.

## If something goes wrong

- **The engine has unsaved changes.** Nothing is pulled. The offer
  is `/save` first.
- **The engine's history has diverged from the remote.** Nothing is
  pulled. The offer is a merge by your own hand, or `/save`, which
  rebases your commits onto the remote.
- **A check reports findings on a finished or dormant project.**
  That is a fact to report, not a defect to chase. Bringing the
  project forward is your decision, project by project.
- **A command will not write into a project.** The project is of a
  shape a release has changed and is not yet migrated. Run
  `/migrate <slug>` on one clone, or pull the project if it was
  migrated elsewhere.

## A worked example

You keep one project, `my-project`, and the engine is behind its
remote.

1. You type `/pull forge`. Claude says the engine is clean and
   behind, pulls it and lists the commits it crossed.
2. Claude shows the Action required lines of the releases crossed.
   One of them says that the shape of files changed and that each
   project is to be migrated.
3. Claude offers `/check light my-project` and
   `/check project my-project`. You say yes, and both run.
4. Claude offers `/migrate my-project`. You say yes on the one clone
   where you work on the project, and the project is migrated and
   saved.
5. The findings of the checks are walked one at a time. Claude makes
   the changes you accept.
6. On your other machine, you pull `my-project` instead of migrating
   it again.

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

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
