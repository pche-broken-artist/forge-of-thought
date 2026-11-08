---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: ce5fce2a8ced6fb0
inputs:
  - .claude/skills/save/SKILL.md
  - scripts/forge-save.py
  - scripts/forge-status.py
  - projects/forge/40-solution-design.md#SOL.0530
  - .claude/skills/test/SKILL.md
---

# Save your work

`/save` commits your work to git and pushes it, after a light check and on whatever branch is checked out. It is for the principal (the person whose thinking is being forged) who wants a round kept safe without making a release.

## When to use it

Use it at the end of a round, or whenever work should not be lost. It makes no render. The other door, which runs from `main` and renders the README and the release notes, is [Release a version](release-a-version.md). The reason for two doors and two speeds is in [Persistence in git](../about/persistence-in-git.md).

## The command

```
/save [slug] [-m "message"] [--tag name] [--quick]
```

- `slug` narrows the save to one repository. `forge` means the engine.
- `-m "message"` gives the commit message, so that Claude drafts none.
- `--tag name` tags the commit. It needs a slug.
- `--quick` leaves the light check out and nothing else.

A bare `/save` commits every repository that has changes. With two windows open, give the slug so that the save touches only the one you work in.

A typed line that stands as it is:

```
/save <slug> -m "tighten the scope of the intent"
```

## What happens

1. Claude reads the scope from the status script. It reports the engine and each project separately, each with the branch it is on. A project that is not under git is named if it has changes and is otherwise left alone.
   You should now see each repository listed with its branch.
2. Claude runs the `light` check on every repository in scope and settles its report through `/check`. This step is skipped with `--quick`. A save never waits on a finding you have not asked to fix. Where the ledger script cannot read a file, the check reads the ledger as it lies, the save goes on and Claude says so aloud. The ledger is the state of a project, made from its documents at the moment it is read. The save goes on because it is what does not lose work.
   You should now see the check's result, or a statement that the check was left out.
3. Claude drafts a one-line English commit message from the records the round added to the histories of the touched documents. It proposes the message and you confirm or adjust it. With `-m` it drafts nothing. When more than one repository has changes, it drafts one message per repository, or you run the save per slug.
   You should now see the message you confirmed.
4. A tag is set only on your word: `--tag` given, or asked for in words. If you ask for a tag without a name, Claude proposes `v<intent version>` of that repository's intent, and you may take it or give your own. Any name git accepts will do.
   You should now see the tag name agreed, or no tag at all.
5. Claude runs the save script. It stages everything, commits and pushes. It prints the commit's file summary and the tag. It runs no render.
   You should now see a line saying the repository was saved and pushed.

### When the remote has moved on

The script looks at the remote's branch before it pushes.

- Where the remote's branch has moved on as well, the histories have diverged. The script then integrates the remote changes first, by rebasing your commits onto them.
- A branch that is merely ahead of the remote is pushed as it stands. A merge you made by hand among its commits therefore keeps its merge commit. The reason is in [Working together on one project](../about/working-together.md).
- A clean repository that is ahead of its origin is pushed in the same way, for example after a rebase finished by hand or a push that failed.
- A branch with no upstream yet reaches the remote with its first commit.
- When there is nothing to commit and a tag is given, the current state is tagged.

## What you have afterwards

- One commit per repository with changes, with the confirmed message.
- The commit pushed to the origin, on the branch that was checked out.
- The tag, if you asked for one, pushed with the commit.

No render is made and no other check than `light` has run. A save never runs the engine's tests.

## If something goes wrong

- **A rebase conflicts.** The rebase is left standing. The commit is made and nothing is lost. The script prints the files in conflict and the step that follows. Claude goes on with the step of a conflict and you save again afterwards. See [Settle a conflict](settle-a-conflict.md).
- **A rebase or a merge is already in progress.** The script refuses before anything is staged, so that conflict markers are never committed. The refusal names the step to finish first.
- **There is no origin.** The commit stays local, and the script says it was not pushed.
- **Git resolves no identity.** The script commits nothing and says so.
- **The tag exists already.** The script refuses and changes nothing.
- **The push fails.** The script reports it; check the network and the remote access, then save again.
- **The repository is not under git.** The save skips it with a note, or refuses it when you named its slug.

If you are unsure what is still unsaved when you stop, see [End a session](end-a-session.md).

## A worked example

You have worked one round in a project and want it kept. You type:

```
/save <slug>
```

Claude lists the project with its branch and runs the `light` check. The check finds nothing to fix. Claude proposes `intent: narrow the scope to the first release` from the round's history records, and you accept it. The script prints the file summary and then a line that the project was saved and pushed to its origin. Nothing more has been done: no render ran and no tag was set.

## See also

- [Release a version](release-a-version.md): the other door, from `main`, with the renders.
- [Settle a conflict](settle-a-conflict.md): what to do when the save stops on a conflict.
- [End a session](end-a-session.md): the end of a session, which names what is unsaved.
- [Persistence in git](../about/persistence-in-git.md): why there are two doors and two speeds.
- [Working together on one project](../about/working-together.md): why a merge made by hand is pushed as it stands.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
