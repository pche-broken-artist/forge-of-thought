---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 3b898300dc27a89e
inputs:
  - .claude/skills/save/SKILL.md
  - scripts/forge-save.py
  - scripts/forge-status.py
  - projects/forge/40-solution-design.md#SOL.0530
---

# Save your work

`/save` is the command that commits your work to git and pushes it, after a light check. It is for you, the principal (the person whose thinking is being forged), whenever a round of work should be kept. It works on whatever branch is checked out and makes no render.

## When to use it

Use it at the end of a round, or whenever you want what you have written kept in git and on the remote. A save keeps work and loses none. For a release from `main`, which also regenerates the renders, use the other door: [Release a version](release-a-version.md).

## The command

```
/save [slug] [-m "message"] [--tag name] [--quick]
```

- `slug`: the one repository to save (`forge` stands for the engine, any other slug for the project of that name). Without it, every repository with changes is saved.
- `-m "message"`: the commit message, so that Claude does not draft one.
- `--tag name`: a tag on the commit. It needs a slug.
- `--quick`: leaves the check out and nothing else.

A typed line looks like this:

```
/save <slug> -m "<one line saying what the round changed>"
```

## What happens

1. Claude finds the scope. It reads the state of the engine and of each project through the status script, which reports every repository with the branch it is on. A project that is not under git and has changes is named in the report and otherwise left alone. You should now see each repository with its changes and its branch.
2. Claude runs the `light` check on every repository in scope, unless you gave `--quick`. It settles the report through `/check`. A save never waits on a finding you have not asked to fix. Where the ledger script (the one that builds the ledger, the file that holds the state of a project) fails or names files it could not read, the check reads the ledger as it lies, the save goes on and says so aloud. You should now see the check's result, or the remark that the save went on without a readable ledger.
3. Claude proposes the commit message, unless you gave `-m`. It drafts one English line from the records that the round appended to the histories of the documents it touched, and you confirm or adjust the wording. When more than one repository has changes, it drafts one message per repository, or you run the save once per slug. The script's own generated message, a list of files, is used only if you say so. You should now see a one-line message waiting for your word.
4. A tag is set only on your word. Give `--tag name`, or ask for one in words. Any name git accepts will do. If you ask for a tag without naming it, Claude proposes a name from the intent version of that repository, and takes yours if you give one. You should now see the tag named, or no tag at all.
5. Claude runs the save script. For each repository it stages everything, commits, rebases your commit onto the remote's changes and pushes. You should now see the commit's file summary, the tag if there is one, and a line saying the repository was saved and pushed.

## What the save does in special cases

- A clean repository that is ahead of its origin is pushed. A branch with no upstream yet reaches the remote with its first commit.
- A rebase that conflicts is left standing. The commit is made and nothing is lost. The script prints the files in conflict and the step that follows. The session (the running conversation with Claude) goes on with the step of a conflict, as [Settle a conflict](settle-a-conflict.md) describes, and then you save again.
- A repository with a rebase or a merge already in progress is refused before anything is staged. The refusal names the step to finish first, so that conflict markers are never committed.
- Without an origin the commit stays local, and the script says so.
- Where git resolves no identity for the repository, nothing is committed. The script says what to set up.
- With a tag and nothing to commit, the tag marks the current state. A tag that already exists is refused and nothing is changed.

## What you have afterwards

Your work is committed on the branch that was checked out, pushed to its origin if it has one, and tagged if you asked. Nothing was rendered. A bare save visits every repository with changes, so when you have two windows open, give the slug of the one you work in and the other is left alone.

## If something goes wrong

- "no commit identity": git resolves no name or e-mail for this host. Run `/setup` for the per-host identity. Nothing was committed.
- "Tag ... already exists": choose another name. Nothing was changed.
- "A rebase is in progress" (or a merge): finish the step of a conflict first, then save again. Nothing was staged.
- "Remote changes ... conflict with yours": the rebase stands where it stopped and the commit is made. Settle the conflict as [Settle a conflict](settle-a-conflict.md) says, then save again.
- "The pull with rebase failed ... left no rebase to finish": the commit is made. Check the network and the remote access, then save again.
- "Push failed": the commit is made. Check the network and the remote access, then save again.
- "Tag ... could not be pushed": the tag was created locally. The script prints the way to push it later.
- "not pushed - no origin configured": the commit is kept locally. This is a property of the repository, not a defect.
- "Project ... is not a repository": a project without its own repository cannot be saved by slug. The script says how to start one.

## A worked example

You have finished a round on a project and want it kept.

```
/save <slug>
```

Claude reads the status and sees the project with its changes on `main`. It runs the `light` check and finds nothing to fix. It reads the round's history records and proposes one line:

```
<what the round changed, in one English line>
```

You confirm it. Claude runs the save script. The script commits, rebases onto the remote and pushes, and prints the file summary and a line saying the project was saved and pushed.

## See also

- [Release a version](release-a-version.md): the other door, from `main`, with the renders.
- [Settle a conflict](settle-a-conflict.md): what to do when the save stops on a conflict.
- [End a session](end-a-session.md): the end of a session, which names what is unsaved.
- [Persistence in git](../about/persistence-in-git.md): why there are two doors and two speeds.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
