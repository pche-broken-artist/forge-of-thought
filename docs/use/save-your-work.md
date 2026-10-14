---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 68424bea8d0d186
inputs:
  - .claude/skills/save/SKILL.md
  - scripts/forge-save.py
  - scripts/forge-status.py
---

# Save your work

`/save` is the command that commits your work and pushes it, after a light check, on whatever branch is checked out. This page is for the principal (the person whose thinking is forged) who wants to keep what the round has produced. Terms of the forge are one line each in the [Glossary](../reference/glossary.md).

## When to use it

Use `/save` at the end of a round of work, or at any moment you want the state kept. It makes no render. When you want the renders regenerated and a release made, use the other door, described in [Release a version](release-a-version.md).

## The command

```
/save [slug] [-m "message"] [--tag name]
```

Without a slug, `/save` visits the engine and every project that is a repository of its own, and saves each one that has changes. With a slug it saves that one repository only; `forge` means the engine. A tag needs one repository, so `--tag` needs a slug.

For example, to save one project with your own message:

```
/save <slug> -m "intent: sharpen the objective"
```

## What happens

1. Claude finds the scope. It runs the status script, which reports the engine and each project separately, with the branch each is on and whether it has unsaved changes.
   You should now see, per repository, its changes or "clean - nothing to save", and its branch.
   A project that is not under git and has changes is named in the report and otherwise left alone.

2. Claude runs the `light` check on every repository in scope and settles its report through `/check`, the command that runs a check and files its result. A save never waits on a finding you have not asked to fix.
   You should now see the report of the check, and the save goes on.

3. Claude proposes a one-line English commit message, unless you gave `-m`. It drafts the line from the records that the round appended to the histories of the documents it touched. You confirm the line or adjust it.
   You should now see one proposed line, and it is the one that will be used once you confirm it.
   When more than one repository has changes, Claude drafts one message per repository, or you run the save once per slug.
   The script's own message, which lists the changed files, is used only if you say so.

4. A tag is set only on your word: either you gave `--tag <name>`, or you asked for one in words. If you ask for a tag without naming it, Claude proposes `v<intent version>` of that repository's intent, and you take it or give any name you like.
   You should now see the tag name agreed, or no tag at all.

5. Claude runs the save script with your arguments. For each repository it stages everything, commits with the confirmed message and, where an origin is configured, rebases your commits onto the remote changes and pushes on the branch that is checked out. With a tag it tags the commit and pushes the tag with it.
   You should now see the commit's file summary, the tag if there is one, and the line "saved and pushed" naming the origin.

## What you have afterwards

- A commit in each repository that had changes, with the message you confirmed.
- The same commit on the remote, where an origin is configured.
- The tag on the commit, if you asked for one. When there was nothing to commit, the tag marks the current state, so a tag can mark a state before a large change.
- No render: the renders and the README stay as they were.

## If something goes wrong

- **"no commit identity":** git resolves no identity for this host, so nothing is committed in that repository. Run `/setup` for the per-host identity, or set a local identity in that repository, and save again.
- **"nothing to save":** the repository has no changes and you asked for no tag. Nothing was done.
- **"not pushed - no origin configured":** the commit is kept locally. A project without a remote is a property, not a defect.
- **A project that is not a repository:** a bare `/save` skips it with a note. A save that names it by slug is refused, with the one-time step that makes it a repository.
- **A tag that already exists:** the save is refused and nothing is changed. Choose another name.
- **A tag without a slug:** the save is refused. Name the repository.
- **Remote changes conflict with yours:** the script stops and nothing is lost. Ask Claude for help before doing anything else.
- **The push fails:** check the network and the access to the remote, and try again.
- **A tag was created but could not be pushed:** the commit is saved. Push the tag later.

## A worked example

You have worked a round on the intent of a project and want it kept, with a tag.

```
/save <slug> --tag v0.4
```

Claude reads the status of `<slug>` and sees the changed files on `main`. It runs the `light` check, and the check reports no finding you must act on. It drafts the line "intent: sharpen the objective and close two open questions" from the history records of the round and asks you to confirm it. You say yes. It runs the save script, which prints the commit's file summary, "tagged: v0.4" and "saved and pushed" with the address of the origin.

## See also

- [Release a version](release-a-version.md): the other door, from `main`, with the renders.
- [End a session](end-a-session.md): the end of a session, which names what is unsaved.
- [Persistence in git](../about/persistence-in-git.md): why there are two doors and two speeds.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
