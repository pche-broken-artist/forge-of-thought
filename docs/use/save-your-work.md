---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 5bf2c09e077175d2
inputs:
  - .claude/skills/save/SKILL.md
  - scripts/forge-save.py
  - scripts/forge-status.py
  - projects/forge/40-solution-design.md#SOL.0530
---

# Save your work

`/save` puts the work of a session into git: it runs a light check, commits what changed and pushes it, on whatever branch is checked out. It is for you, the principal (the person whose thinking is forged), at the end of a round of work or whenever you want the work safe. It makes no renders; that belongs to the other door, [Release a version](release-a-version.md).

## When to use it

Use it whenever work should not live only on your machine: after a round is written, before you close the window, before you switch to other work. A save does not publish a version. A version goes out through [Release a version](release-a-version.md), from `main`. Why there are two doors and two speeds is explained in [Persistence in git](../about/persistence-in-git.md).

## The command

```
/save [slug] [-m "message"] [--tag name] [--quick]
```

- `slug` narrows the save to one repository. `forge` means the engine itself. Every project under `projects/` is a repository of its own.
- `-m "message"` gives the commit message, so Claude does not draft one.
- `--tag name` tags the commit. It needs a slug, because a tag belongs to one repository.
- `--quick` leaves the check out and nothing else.

A bare `/save` commits every repository that has changes. With two windows open on two projects, give the slug so that the save reaches only the one you work in.

## What happens

1. Claude finds the scope by running the status script. It reports the engine and each project separately, each with the branch it is on. A project that is not under git is named in the report and otherwise left alone.

   You should now see each repository in scope with its branch.

2. Unless you gave `--quick`, Claude runs the `light` check on every repository in scope and settles its report as `/check` does. A save never waits on a finding you have not asked to fix. Where the ledger (the state of the project, built from its documents when it is read) cannot be built, or names a file it could not read, the check reads the ledger as it lies. The save goes on and says so aloud. The reason: the save is what does not lose work.

   You should now see the check's result, and any findings left standing until you ask for them to be fixed.

3. Unless you gave `-m`, Claude drafts a one-line commit message in English. It draws the line from the history records that the round appended to the documents it touched. It proposes the line to you, and the commit uses the wording you confirm or adjust. With more than one repository changed, it drafts one message per repository, or you run the save once per slug. The script's own generated message, a list of files, is used only if you say so.

   You should now see a proposed message waiting for your word.

4. A tag is set only on your word: either `--tag name` or a request in words. Any name git accepts will do. If you ask for a tag without naming it, Claude proposes the version of that repository's intent as the name, and you may take it or give your own.

   You should now see the tag name confirmed, or no tag at all.

5. Claude runs the save script. For each repository it commits the changes, rebases your commits onto the remote and pushes. It does this on whatever branch is checked out, with no render. The script prints the commit's file summary and the tag.

   You should now see a line per repository saying it was saved and pushed.

The script also covers cases where nothing new is committed:

- A clean repository that is ahead of its origin is pushed all the same. A branch with no upstream yet is included; its first push creates it on the remote.
- With a tag and nothing to commit, the tag marks the current state of the repository.
- A repository with nothing to save is reported as such.

## What you have afterwards

Your changes are committed and, where an origin exists, pushed. If you asked for a tag, it sits on the commit and was pushed with it. No render was made and no version was released.

## If something goes wrong

- **A rebase conflicts.** The remote changed the same text as you. The script leaves the rebase standing, the commit is made and nothing is lost. It prints the files in conflict and the step that follows. Claude then goes on with the step of a conflict and, when it is settled, you save again. The steps are in [Settle a conflict](settle-a-conflict.md).
- **A rebase or a merge is already in progress.** The script refuses before anything is staged, so that conflict markers are never committed. The refusal names the step to finish first, and then you save again.
- **There is no origin.** The commit stays local, and the script says so. A project without a repository is a property of the project, not a defect, and the report relays the script's note.
- **Git resolves no identity.** Nothing is committed. The script says that no commit identity is known for this host and points to `/setup`, which offers the per-host identity.
- **The tag already exists.** The script refuses and changes nothing. Choose another name.
- **The pull with rebase fails and leaves no rebase.** The commit is made and nothing is lost. Check network and remote access and save again.
- **The push fails.** The script stops and asks you to check network and remote access, then save again.
- **The tag was created but could not be pushed.** The script says so and names the push to run later.

To see the state of every repository before you save, or what remains unsaved when you stop, see [End a session](end-a-session.md).

## A worked example

You have worked a round on a project and its documents have changed. You are in one window, so you narrow the save to it.

```
/save <slug>
```

Claude reports that `<slug>` is on `main` with changes, runs the `light` check and finds nothing to settle. It proposes the message "Record the round's changes to the intent" drawn from the history records. You adjust one word and confirm. The script commits, rebases onto the remote, which has nothing new, pushes, and prints that `<slug>` was saved and pushed. You did not ask for a tag, so none was set.

## See also

- [Release a version](release-a-version.md): the other door, from `main`, with the renders.
- [Settle a conflict](settle-a-conflict.md): what to do when the save stops on a conflict.
- [End a session](end-a-session.md): the end of a session, which names what is unsaved.
- [Persistence in git](../about/persistence-in-git.md): why there are two doors and two speeds.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
