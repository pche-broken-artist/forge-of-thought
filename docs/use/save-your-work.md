---
generated: 2026-10-23
version: 5.34
made: mirrored
inputs-hash: 16f274bd12eb306c
inputs:
  - .claude/skills/save/SKILL.md
  - scripts/forge-save.py
  - scripts/forge-status.py
  - projects/forge/40-solution-design.md#SOL.0530
---

# Save your work

`/save` is the command that checks your work, commits it to git and pushes it, on whatever branch is checked out. It is for the principal (the person whose thinking is forged) at the end of a round of work, and it makes no render.

## When to use it

Use it whenever a round of work is done and you want it kept and shared. It is the quick door. The other door is [Release a version](release-a-version.md), which runs from `main` and makes the renders as well. The [Glossary](../reference/glossary.md) gives every term of the forge in one line.

## The command

```
/save [slug] [-m "message"] [--tag name] [--quick]
```

For example, to save one project with a message of your own:

```
/save <slug> -m "tighten the second objective"
```

The arguments:

- `slug`: the one repository to save, where `forge` means the engine itself. Without it, every repository with changes is saved.
- `-m "message"`: the commit message. Without it, Claude drafts one and asks you.
- `--tag name`: a tag on the commit. A tag needs one repository, so it needs a slug.
- `--quick`: leaves the check out and nothing else.

With two windows open, name the slug. A bare save commits every repository that has changes, including the one the other window is working in.

## What happens

1. Claude reads the scope from the status script. It lists the engine and each project, each with the branch it is on. A project that is not under git is named and left alone.
   You should now see each repository with its changes and its branch.
2. Unless you gave `--quick`, Claude runs the `light` check on every repository in scope and settles its report through `/check`. A save never waits on a finding you have not asked to fix. Where the ledger script (the one that builds the ledger, the single record of state, at read time) fails or cannot read a file, the check reads the ledger as it lies, the save goes on and Claude says so aloud.
   You should now see the check's report, and any finding left as it is unless you asked for a fix.
3. Unless you gave `-m`, Claude drafts a one-line commit message from the records the round added to the histories of the documents it touched, and proposes it. It commits with the wording you confirm or adjust. With more than one repository, it drafts one message for each, or you save one slug at a time. The script's own message, a list of files, is used only if you say so.
   You should now see a one-line message that you can confirm.
4. A tag is set only on your word: `--tag` given, or asked for in words. Any name git accepts will do. If you ask for a tag without naming it, Claude proposes `v` followed by the version of that project's intent, and takes your word or your own name.
   You should now see the tag named before anything is committed.
5. Claude runs the save script. For each repository it commits, rebases your commits onto the remote and pushes. It does this on whatever branch is checked out and makes no render.
   You should now see the commit's file summary, the tag if there is one, and a line saying the repository was saved and pushed.

The script also pushes in two other cases. A clean repository that is ahead of its origin is pushed, for example after a push that failed earlier. A branch with no upstream yet reaches the remote with its first commit. With a tag and nothing to commit, the current state is tagged. A tag that already exists is refused.

## What you have afterwards

Your changes are committed on the current branch and pushed to its origin. If you asked for a tag, it is on the commit and pushed with it. No render has been made.

## If something goes wrong

- A rebase or a merge is already in progress in the repository. The save refuses before anything is staged, so conflict markers are never committed. The refusal lists the files in conflict and names the step. Finish that step, then save again.
- The remote's changes conflict with yours. The rebase is left standing, your commit is made and nothing is lost. The script prints the files in conflict and the step that follows. The session (one run of Claude with you) goes on with the step of a conflict, then you save again. See [Settle a conflict](settle-a-conflict.md).
- There is no origin. The commit stays local and the script says it was not pushed.
- Git resolves no identity for the host. Nothing is committed. The script says so and points to `/setup` for the per-host identity.
- The tag already exists. The script refuses and changes nothing.
- The pull or the push fails for another reason, such as network or access. The commit is made. Check the connection and save again.
- A project without a repository is a property, not a defect. Claude relays the script's note.

## A worked example

You have finished a round on the project `<slug>` and want it kept, with a tag before a large change.

1. You type `/save <slug> --tag <tag-name>`.
2. Claude reads the status. It shows `<slug>` with changes, on branch `main`.
3. It runs the `light` check. One finding comes back. You do not ask to fix it, so the save goes on.
4. Claude proposes the message "Reworked the objective and recorded why". You confirm it.
5. The script commits, rebases onto the remote, tags the commit and pushes both. The last line says the repository was saved and pushed with the tag.

## See also

- [Release a version](release-a-version.md): the other door, from `main`, with the renders.
- [Settle a conflict](settle-a-conflict.md): what to do when the save stops on a conflict.
- [End a session](end-a-session.md): the end of a session, which names what is unsaved.
- [Persistence in git](../about/persistence-in-git.md): why there are two doors and two speeds.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.34 from the files the front-matter names; never edited by hand.
