---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: e1d6fefddcdf08c8
inputs:
  - .claude/skills/save/SKILL.md
  - scripts/forge-save.py
  - scripts/forge-status.py
---

# Save your work

`/save` is the command that puts your work into git: it runs a light check, drafts a commit message for you to confirm, then commits and pushes on whatever branch is checked out. It is for the principal (the person whose thinking is being forged) at any point of a round, when the work should be safe in the repository and nothing needs releasing. It makes no render. Terms of the forge are explained in the [Glossary](../reference/glossary.md).

## When to use it

Use `/save` whenever work should not live only on your disk: at the end of a round, before a risky change, or on the way out of a session. Use `/release` instead when you want a version published from `main` with its renders: see [Release a version](release-a-version.md). The reason for two doors at two speeds is in [Persistence in git](../about/persistence-in-git.md).

## The command

```
/save [slug] [-m "message"] [--tag name] [--quick]
```

All parts are optional.

- `slug`: save that one repository only. `forge` stands for the engine. Without a slug, every repository with changes is saved.
- `-m "message"`: the commit message. Without it, Claude drafts one.
- `--tag name`: tag the commit. It needs a slug.
- `--quick`: leave the check out. It changes nothing else.

A typical line:

```
/save <slug> -m "intent: carry the round's answers"
```

## What happens

1. Claude finds the scope with the status script. It reports the engine and each project separately, with the branch each is on. A project that is not under git and has changes is named in the report and otherwise left alone.

   You should now see each repository with its unsaved changes and its branch.

2. Unless you gave `--quick`, Claude runs the `light` check on every repository in scope. It settles the report through `/check`. A save never waits on a finding you have not asked to fix. Where the ledger script cannot read a file, the check reads the ledger as it lies, the save goes on, and Claude says so aloud, because a save is what does not lose work.

   You should now see the check's result, and the save carrying on.

3. Unless you gave `-m`, Claude drafts a one-line English commit message. It draws on the records the round appended to the histories of the touched documents. It proposes the message to you and commits with the wording you confirm or adjust. When several repositories have changes, one message is drafted per repository, or the save is run per slug. The script's own generated message (a file list) is used only if you say so.

   You should now see a one-line message waiting for your word.

4. A tag is set only on your word: `--tag name`, or asked for in words. It needs one repository, so a slug. Any name git accepts will do. If you ask for a tag without naming it, Claude proposes `v` followed by the intent version of that repository, and takes your word or your own name.

   You should now see the tag name agreed, or no tag at all.

5. Claude runs the save script. For each repository it stages everything, commits, rebases your commits onto the remote and pushes. It saves on whatever branch is checked out. It never forces a file in and never cleans anything.

   You should now see a line per repository such as "saved and pushed to" the origin, with the file summary of the commit and the tag if one was set.

## What you have afterwards

- One commit per repository that had changes, with the message you confirmed.
- The commit pushed to the origin of the branch you are on.
- A tag on the commit, if you asked for one. When there was nothing to commit, the tag marks the current state.
- A clean repository that is ahead of its origin is pushed too, with the line "nothing to commit - N commit(s) ahead of origin, pushing". A branch with no upstream yet reaches the remote with its first commit.

## If something goes wrong

- **The rebase conflicts.** The script aborts the rebase, nothing is lost, and it prints the steps to finish by hand: pull with rebase, resolve each conflicted file, add it, continue the rebase, then run the save again for that slug. It pushes the clean repository that is ahead. Type only what the script prints.
- **There is no origin.** The commit stays local and the script says "not pushed - no origin configured". Adding a remote is your act; the script never does it.
- **Git resolves no identity.** The script commits nothing and says so. Run `/setup` for the per-host identity, or set a local one as the message tells you.
- **The tag exists already.** The script refuses and changes nothing. Choose another name.
- **The push fails.** The script reports the failure and asks you to check the network and the remote access, then try again.
- **A tag cannot be pushed.** The tag is created, and the script prints the command to push it later.
- **The project has no repository.** Bare, it is skipped with a note. With its slug, the script refuses and tells you to initialise a repository once, then save.
- **Nothing to save.** The script says "nothing to save" and does nothing.

## A worked example

You have finished a round in a project called `<slug>` and want it safe.

```
/save <slug>
```

Claude reports the project on branch `main` with its changes, runs the `light` check and finds nothing that stops the save. It proposes a message drafted from the round's history records, for example "intent: sharpen the scope and record the round". You confirm it. The script commits, rebases onto the remote, pushes, and prints "saved and pushed to" the origin. To leave the check out, give `--quick`: `/save <slug> --quick`. Before you close your work for the day, [End a session](end-a-session.md) names what is still unsaved.

## See also

- [Release a version](release-a-version.md): the other door, from `main`, with the renders.
- [End a session](end-a-session.md): the end of a session, which names what is unsaved.
- [Persistence in git](../about/persistence-in-git.md): why there are two doors and two speeds.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
