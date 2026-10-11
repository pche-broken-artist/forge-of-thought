---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 5bb5e4e8ce318ce4
inputs:
  - .claude/skills/save/SKILL.md
  - scripts/forge-save.py
  - scripts/forge-status.py
---

# Save your work

`/save` is the command that puts your work into git: it runs the light check, drafts a commit message with you, then commits and pushes. This page is for the principal (the person whose thinking is forged) who wants to keep a round of work safe without releasing a version.

## When to use it

Use it at the end of a round of work, or at any point where you want what is written to be kept and shared. It runs on whatever branch is checked out and renders nothing. To release a version from `main`, with the renders regenerated, use the other door, [Release a version](release-a-version.md). The reason for two doors is in [Persistence in git](../about/persistence-in-git.md).

## The command

```
/save [slug] [-m "message"] [--tag name]
```

- `slug` names one repository. `forge` means the engine. Without it, every repository with changes is saved.
- `-m "message"` gives the commit message yourself. Without it, Claude drafts one and asks you.
- `--tag name` tags the commit. It needs a slug.

For example, to save one project under the placeholder slug:

```
/save <slug>
```

## What happens

1. Claude finds the scope. It runs the status script, which reports the engine and each project as a separate repository, each with the branch it is on. A project that is not under git is named in the report and left alone.

   You should now see each repository listed with its unsaved changes, or "clean - nothing to save", and its branch.

2. Claude runs the `light` check on every repository in scope and settles its report through `/check`. The `light` check is the one check a save runs. The other checks belong to a release. A save never waits on a finding you have not asked to fix.

   You should now see the check's report, with nothing held back for a finding you left alone.

3. Claude drafts a one-line commit message in English. It draws the message from the records the round added to the histories of the documents it touched. It proposes the message and commits with the wording you confirm or adjust. With `-m`, this step is skipped. When more than one repository has changes, Claude drafts one message per repository, or the save is run once per slug. The file list that the script generates is used only if you say so.

   You should now see a proposed message, or your own `-m` wording taken as given.

4. A tag is set only on your word: either `--tag name` is given, or you ask for one in words. A tag marks one repository, so it needs a slug. If you ask for a tag without naming it, Claude proposes `v` followed by the version of that repository's intent. You may take it or give any name git accepts.

   You should now see the tag named, or no tag at all if you did not ask for one.

5. Claude runs the save script. For each repository it stages everything, commits, puts your commits on top of what the remote already has, and pushes. If the script finds that git resolves no identity for the host, it commits nothing in that repository and says so.

   You should now see the commit's file summary and a line such as "saved and pushed to" the remote, in green.

## What you have afterwards

- One commit per repository that had changes, with the message you confirmed.
- The commit pushed to the remote on the branch that was checked out.
- A tag on the commit, only if you asked for one. It is pushed with the commit.
- Nothing rendered. The README and release notes are left as they were.

## If something goes wrong

- **No identity.** The script says that git resolves no commit identity for this host and commits nothing there. Run `/setup` for the per-host identity, or set a local one, then save again.
- **Nothing to save.** The repository has no changes, and the script says so. With a tag requested, the script tags the current state instead.
- **No remote.** The commit is kept locally and the script says it was not pushed. A tag is kept locally too.
- **Remote changes conflict with yours.** The script stops and says nothing was lost. Ask Claude for help before doing anything else.
- **The push fails.** The script tells you to check the network and the access to the remote and try again.
- **The tag exists already.** The script refuses it and changes nothing in that repository.
- **A tag without a slug.** The script refuses and asks you to name one repository.
- **A project without a repository.** Named with a slug, it is refused. Bare, it is skipped with a note. Initialise its repository once, then save.

## A worked example

You have finished a round on a project and want it kept. You type:

```
/save <slug>
```

Claude reports the status of that repository: three files changed, branch `main`. It runs the `light` check and finds nothing. It proposes the message `<slug>: <what the round changed>`, drawn from the round's history records. You confirm. Claude runs the save script, and you see the commit's file summary and the line "saved and pushed to" the remote.

If you had also wanted a tag, you would have said so before the script ran, and Claude would have proposed a name for you to confirm or replace.

## See also

- [Release a version](release-a-version.md): the other door, from `main`, with the renders.
- [End a session](end-a-session.md): the end of a session, which names what is unsaved and offers the save.
- [Persistence in git](../about/persistence-in-git.md): why there are two doors and two speeds.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
