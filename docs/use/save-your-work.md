---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 5829a71dc0eb063f
inputs:
  - .claude/skills/save/SKILL.md
  - scripts/forge-save.py
  - scripts/forge-status.py
  - projects/forge/40-solution-design.md#SOL.0530
  - .claude/skills/test/SKILL.md
---

# Save your work

`/save` commits what has changed in the engine and in your projects and pushes it, on whatever branch is checked out, after a light check. This page is for you when a round of work is done and you want it kept in git. A project is a git repository of its own, so a save is made per repository.

## When to use it

Use `/save` at the end of a round of work, or at any point where you want what exists to be safe. It makes no renders and runs no checks beyond the light one. To make a release from `main`, with the renders, use [Release a version](release-a-version.md). Why there are two doors and two speeds is explained in [Persistence in git](../about/persistence-in-git.md).

## The command

```
/save [slug] [-m "message"] [--tag name] [--quick]
```

For example, to save one project with your own message:

```
/save <slug> -m "Tighten the scope of the assignment"
```

- `slug`: the one repository to save. Without it, every repository with changes is saved, so with two windows open the slug narrows the save to the one you work in. `forge` saves the whole: the engine and, where it is cloned beside it, the forge's own project, each as its own commit prefixed `forge:`.
- `-m "message"`: the commit message. Without it Claude drafts one and asks you.
- `--tag name`: a tag on the commit. It needs one repository, so a slug.
- `--quick`: leaves the check out and nothing else.

## What happens

1. Claude reads the scope from the status script. It reports the engine and each project separately, with the branch each is on. A project that is not under git and has changes is named in the report and otherwise left alone.

   You should now see the repositories in scope, each with its branch.

2. Unless you gave `--quick`, Claude runs the `light` check on every repository in scope and settles its report through `/check` (see the [Glossary](../reference/glossary.md) for the terms). A save never waits on a finding you have not asked to fix. Where the ledger script cannot build the ledger or names files it could not read, the check reads the ledger as it lies, the save goes on, and Claude says so aloud. The reason given is that a save is what does not lose work.

   You should now see the check's result, or, with `--quick`, no check at all.

3. Unless you gave `-m`, Claude drafts a one-line English commit message. It draws the message from the records the round appended to the histories of the touched documents. It proposes the message to you and commits with the wording you confirm or adjust. Where several repositories have changes, one message is drafted for each, or you run the save per slug. The script's own file-list message is used only if you say so.

   You should now see a one-line message that you have confirmed.

4. A tag is set only on your word: `--tag name` given, or asked for in plain words. Any name git accepts will do. If you ask for a tag without naming it, Claude proposes `v` followed by the intent's version of that repository, and takes your word or your own name. With `forge` the tag goes on the engine alone, never on the project beside it. A name that already exists is refused and nothing is changed.

   You should now see the tag named in the report, or no tag if you asked for none.

5. Claude runs the save script, which commits and pushes. It prints the commit's file summary and the tag.
   - Where the remote's branch has moved on as well, so that the histories diverged, the script first integrates the remote changes by rebasing your commits onto them.
   - A branch that is merely ahead of its origin is pushed as it stands. A merge you made by hand among its commits therefore keeps its merge commit; why is explained in [Working together on one project](../about/working-together.md).
   - A clean repository that is ahead of its origin is pushed too, a branch with no upstream yet included.
   - Without an origin the commit stays local, and the script says so.

   You should now see "saved and pushed" for each repository, in green.

## What you have afterwards

- One commit per repository that had changes, with the message you confirmed.
- The commits on the remote, where an origin is configured.
- The tag on the commit and on the remote, if you asked for one.
- No renders made and no tests run. A save never runs the engine's tests.

## If something goes wrong

- **A rebase conflicts.** The script leaves the rebase standing. The commit is made and nothing is lost. It prints the files in conflict and the step that follows. The session goes on with the step of a conflict and then saves again; see [Settle a conflict](settle-a-conflict.md).
- **A rebase or a merge is already in progress.** The script refuses before anything is staged, so that conflict markers are never committed. The refusal names the step to finish first; then save again.
- **Git resolves no identity.** The script commits nothing and says so. The message points you to `/setup` for the per-host identity.
- **The tag already exists.** Nothing is changed; choose another name.
- **A tag without a slug.** The script refuses and asks for one repository.
- **No origin.** The commit, and the tag if any, stay local. This is a note, not a failure.
- **A project has no repository.** Named with a slug, it is refused with the one step that makes it a repository; bare, it is skipped with a note.
- **The pull, the commit or the push fails.** The script reports it. After a failed pull that left no rebase, the commit is made and nothing is lost; check the network or the remote access and save again.
- **Nothing to save.** The script says "nothing to save" for that repository.

To see what is still unsaved before you stop, see [End a session](end-a-session.md).

## A worked example

You have finished a round on a project and want it saved with a tag.

```
/save <slug> --tag <name>
```

1. Claude names the project and its branch from the status script.
2. The `light` check runs and reports no finding. You see the result and nothing waits.
3. Claude proposes the message "Add the success criteria to the assignment", drawn from the round's history records. You accept it.
4. Because you gave `--tag`, the tag `<name>` is set on the new commit.
5. The script commits, pushes the branch and the tag, and prints "saved and pushed (with tag <name>)".

Afterwards the project's repository holds one new commit with its tag, on the branch you were on, and the remote has both.

## See also

- [Release a version](release-a-version.md): the other door, from `main`, with the renders.
- [Settle a conflict](settle-a-conflict.md): what to do when the save stops on a conflict.
- [End a session](end-a-session.md): the end of a session, which names what is unsaved.
- [Persistence in git](../about/persistence-in-git.md): why there are two doors and two speeds.
- [Working together on one project](../about/working-together.md): why a merge made by hand is pushed as it stands.
- [Projects and the engine](../about/projects-and-the-engine.md): why `forge` names the engine and the forge's own project beside it.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
