---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/save/SKILL.md
  - scripts/forge-save.ps1
  - scripts/forge-status.ps1
  - CLAUDE.md
---

# Save your work

This page is for the person who works in the forge and wants to put
the state of the engine and of his projects safely into git. It says
what `/save` does, in the order it does it, and what you are asked.

The command is:

```
/save [slug] [-m "message"] [-Tag name]
```

The engine and every project are repositories of their own. `/save`
works on whatever branch is checked out in each, runs the light check,
commits and pushes. It makes no render. The other door, with the
renders, is `/release`.

## What happens

1. **The scope is read.** The status script reports the engine and
   each project separately, with the branch each is on, whether it has
   unsaved changes, its last commit and its origin. Without a slug,
   every repository with changes is in scope; with a slug, that one
   only (`forge` means the engine). A project that is not under git is
   named in the report and left alone; that is a property of the
   project, not a defect.
2. **The light check runs** on every repository in scope, and its
   report is settled through `/check`. A save never waits on a finding
   you have not asked to fix.
3. **A commit message is proposed.** Unless you gave `-m`, a one-line
   English message is drafted from the records the round appended to
   the histories of the documents it touched. You confirm it or adjust
   the wording, and the commit uses what you confirmed. When several
   repositories have changes, there is one message for each, or you run
   the save once per slug. The script's own generated file list is used
   only if you say so.
4. **A tag is set only on your word**, either `-Tag name` or asked for
   in words. A tag needs one repository, so a slug must be given. If
   you ask for a tag without naming it, one is proposed from the
   version of that repository's intent, and you take it or give any
   name git accepts.
5. **The save runs.** Per repository the script stages everything,
   commits, and, where an origin is configured, integrates remote
   changes by rebase and pushes. Without an origin the commit is kept
   locally and reported. A tag is pushed with the commit; with nothing
   to commit, the tag marks the current state. A tag name that already
   exists is refused. The script prints the commit's file summary and
   the tag, and that is the outcome you are shown.

## What you see

The report names each repository and its branch, the outcome of the
light check, the message committed and the file summary the script
prints. Projects not under git appear with a note.

## Identity

The forge sets no commit identity. It is git's, resolved on each host
from your own configuration. On a host where none resolves, nothing is
committed and the save fails aloud instead of taking a default.

## See also

- [Release a version](release-a-version.md): the other door, from
  `main`, with the renders.
- [About persistence in git](../about/persistence-in-git.md): why
  there are two doors and two speeds.
