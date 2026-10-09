---
generated: 2026-10-09
made: derived
inputs:
  - scripts/forge-pull.ps1
  - CLAUDE.md
  - projects/forge/10-intent.md
  - projects/forge/recipes/release-notes.md
---

# Upgrade the engine

This page is for the user who has cloned the engine and wants the
newer version of it, and then wants to know what that means for his
projects. It was put together from the help header of
`scripts/forge-pull.ps1`, the Persistence section of `CLAUDE.md`, the
forge intent and the recipe of the release notes.

## What an upgrade is

The engine is a git repository whose `main` is the released line.
Upgrading is pulling it: `scripts/forge-pull.ps1` fast-forwards from
the remote, and on the engine that pull is the upgrade channel. There
is nothing else to install.

Your projects are not changed by an upgrade. A project records no
engine version: it is measured against the conventions of the engine
you have now, whenever you check it. There is no migration tool;
bringing a project to newer conventions is your decision, made project
by project, and done with Claude in the session.

## Steps

1. **Save first.** The pull is fast-forward only and never touches a
   repository with unsaved changes, so that it can never create a
   conflict in half-finished work. Save what you have before you pull.

2. **Pull.** Run one of these from the engine root:

   ```
   ./scripts/forge-pull.ps1              # the engine and every project with an origin
   ./scripts/forge-pull.ps1 forge        # the engine only (the upgrade)
   ./scripts/forge-pull.ps1 my-project   # one project
   ```

   Without an argument the script pulls the engine, then every project
   that is a repository with an origin. A repository with unsaved
   changes is reported with its changes and skipped; a project that is
   not under git, or has no origin, is reported and skipped too. With a
   slug the same cases are refused instead of skipped, and for unsaved
   changes the script tells you to run `scripts/forge-save.ps1` first.
   If the local and the remote history have diverged, the pull fails
   and says so; the script points you to `scripts/forge-save.ps1`, which
   reconciles both, or to Claude.

3. **Read the release notes.** Open `RELEASE-NOTES.md` in the engine
   root. It has one section per release, newest first, written for the
   user who takes upgrades this way. Every section starts with its
   **Action required** lines: what to do in your projects after
   pulling. Read those first, for every release since your last
   upgrade, then the rest of each section (Added, Changed, Removed,
   Fixed, Rejected) for what it means for you.

4. **Check each project.** Project by project, run

   ```
   /check light my-project
   /check project my-project
   ```

   The two checks measure the project against the current conventions
   and report what no longer conforms.

5. **Settle the findings.** The findings are walked through one at a
   time. For each one you decide; Claude migrates on your word, in the
   session. Nothing is changed without it.

## A project you leave as it is

You do not have to migrate. An artefact stays valid under the
conventions it was written to: what a check reports on a finished or
dormant project is a fact about it, not a defect to chase. Whether a
project is brought to newer conventions is your decision, for each
project, and never assumed.

## See also

- [Check conformance](check-conformance.md): running a check and settling its findings.
- [Save your work](save-your-work.md): saving before a pull.
