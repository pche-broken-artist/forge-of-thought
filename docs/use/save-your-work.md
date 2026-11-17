---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 7ad429bd8d81a5e8
inputs:
  - .claude/skills/save/SKILL.md
  - scripts/forge-save.py
  - scripts/forge-status.py
  - projects/forge/40-solution-design.md#SOL.0530
  - .claude/skills/test/SKILL.md
---

# Save your work

`/save` is the command that checks your work lightly, commits it and
pushes it to git, on whatever branch is checked out. It is for you,
the principal (the person whose thinking is being forged), whenever a
round of work should be kept safe. It makes no renders; the other
door, from `main` and with the renders, is
[Release a version](release-a-version.md).

## When to use it

Use it at the end of a round, or any time you want what you have
written to be committed and on the remote. Two doors and two speeds
exist for a reason that
[Persistence in git](../about/persistence-in-git.md) gives. A term you
do not know is one line in the [Glossary](../reference/glossary.md).

## The command

```
/save [slug] [-m "message"] [--tag name] [--quick]
```

All four arguments are optional.

- `slug` narrows the save to one repository. A bare save commits
  every repository with changes, so with two windows open the slug
  keeps the save to the one you work in.
- `-m "message"` gives the commit message, so that Claude does not
  draft one.
- `--tag name` sets a tag. It needs one repository, so a slug goes
  with it.
- `--quick` leaves the check out and nothing else.

`/save forge` saves the whole: the engine and, where it is cloned
beside it, the forge's own project. Each is its own commit, prefixed
`forge:`, and a tag goes on the engine alone.
[Projects and the engine](../about/projects-and-the-engine.md) says
why `forge` names both.

## What happens

1. Claude reads the scope from the status script. It reports the
   engine and each project separately, with the branch each is on. A
   project that is not under git and has changes is named in the
   report and otherwise left alone.

   You should now see each repository in scope with its branch.

2. Unless you gave `--quick`, Claude runs the `light` check on every
   repository in scope and settles its report through `/check`. A
   save never waits on a finding you have not asked to fix. Where the
   ledger script (the script that builds the project's single record
   of state) fails or cannot read a file, the check reads the ledger
   as it lies, the save goes on and says so aloud, because a save is
   what does not lose work.

   You should now see the check's report, or the statement that it
   was left out.

3. Unless you gave `-m`, Claude drafts a one-line commit message from
   the records that the round appended to the histories of the
   documents it touched, and proposes it to you. It commits with the
   wording you confirm or adjust. Where more than one repository has
   changes, it drafts one message per repository, or you save per
   slug. With `forge`, the one message serves both commits and
   carries the prefix `forge:` itself, because the script adds no
   prefix to a message it is given. The script's own generated file
   list is used only if you say so.

   You should now see the message you confirmed.

4. A tag is set only on your word: `--tag name` given, or asked for in
   words. Any name git accepts will do. If you ask for a tag without
   naming it, Claude proposes `v` followed by the version of that
   repository's intent, and takes your word or your own name.

   You should now see the tag named, or none.

5. Claude runs the save script. It stages everything, commits and,
   where an origin is configured, pushes. It does not render. The
   script prints the commit's file summary and the tag.

   You should now see a line per repository that ends "saved and
   pushed", or says why not.

How the script treats the remote:

- Where the remote's branch has moved on as well, so that the
  histories diverged, the script first integrates the remote changes
  by rebasing your commits onto them.
- A branch that is merely ahead is pushed as it stands. A merge you
  made by hand among its commits therefore keeps its merge commit.
  [Working together on one project](../about/working-together.md)
  says why.
- A clean repository that is ahead of its origin is pushed too, a
  branch with no upstream yet included.
- Without an origin the commit stays local, and the script says so.

## What you have afterwards

- One commit per repository that had changes, pushed to its origin.
- The tag, if you asked for one, on the commit and pushed with it.
  Where there was nothing to commit, the tag marks the current state.
- No renders, and no run of the engine's tests. A save never runs
  them.

## If something goes wrong

- **A rebase conflicts.** The script leaves the rebase standing. The
  commit is made and nothing is lost. It prints the files in conflict
  and the step that follows. Claude goes on with the step of a
  conflict and saves again; the way is
  [Settle a conflict](settle-a-conflict.md).
- **A rebase or a merge is already in progress.** The script refuses
  before it stages anything, so that conflict markers are never
  committed. The refusal names the step to finish first. Finish it,
  then save again.
- **The pull with rebase fails and leaves no rebase to finish.** The
  commit is made and nothing is lost. Check the network and the access
  to the remote, then save again.
- **The push fails.** Check the network and the access to the remote,
  then save again.
- **The tag exists already.** The script refuses it and changes
  nothing. Choose another name.
- **A tag is asked for without a slug.** The script says that a tag
  needs one repository and names the slug to give.
- **Git resolves no identity for the repository.** The script commits
  nothing and says how to set one: run `/setup` for the per-host
  identity, or set a local one.
- **A project has no repository.** Its changes are noted and the
  save goes on; named by slug, it is refused with the line that makes
  it one.
- **Nothing to save.** The script says so and does nothing.

If the session ended with unsaved work, [End a session](end-a-session.md)
names what is unsaved.

## A worked example

You have finished a round in the project `<slug>`, and another
window works on a second project. You type:

```
/save <slug>
```

Claude reads the status of the repository and the branch it is on,
runs the `light` check and settles its report. It proposes the
message "<slug>: the round's changes in one line", drafted from the
histories. You confirm it. The script commits, finds the remote's
branch unchanged, pushes and prints:

```
saved and pushed to <the origin>
```

The second window's project is left untouched, because the slug
narrowed the save. For a save that skips the check, add `--quick`.

## See also

- [Release a version](release-a-version.md): the other door, from
  `main`, with the renders.
- [Settle a conflict](settle-a-conflict.md): what to do when the save
  stops on a conflict.
- [End a session](end-a-session.md): the end of a session, which
  names what is unsaved.
- [Persistence in git](../about/persistence-in-git.md): why there are
  two doors and two speeds.
- [Working together on one project](../about/working-together.md):
  why a merge made by hand is pushed as it stands.
- [Projects and the engine](../about/projects-and-the-engine.md): why
  `forge` names the engine and the forge's own project beside it.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
