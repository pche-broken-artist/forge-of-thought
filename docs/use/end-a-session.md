---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 435c0242a8a4714c
inputs:
  - .claude/skills/end/SKILL.md
  - scripts/forge-status.py
---

# End a session

`/end` is the command that tells you what shutting down would lose. It
is for the principal (whoever's thinking is being forged) at the end of
a working session, a session being one run of Claude in the command
line. It writes nothing and runs nothing but its scripts, so it is safe
to run at any moment.

## When to use it

Use it before you close the command line. It answers one question: does
anything live only in this conversation, or in a repository that has not
been saved?

## The command

```
/end
```

## What happens

1. Claude says what lives only in this conversation. That means a round
   of work not yet written to a file, verdicts carried but not written,
   and anything it promised and has not done. It offers the write.

   You should now see a plain statement of what is carried in the
   conversation only, and an offer to write it, or a statement that
   there is nothing of the kind.

2. Claude runs the status script without the remote, so no network is
   touched. It names every repository with unsaved changes and offers
   `/save` for them. The script reports, for the engine and each
   project, the unsaved changes (or "clean - nothing to save"), the
   branch and the last commit.

   You should now see each repository named with its unsaved files, and
   an offer of `/save`, or every repository reported clean.

3. Claude makes the ledger again. The ledger is the single record of
   the state of a project, built from its documents each time it is
   read. From its table of renders Claude names the stale renders as a
   fact. It makes no offer for them, because renders belong to the
   release.

   You should now see the stale renders named, or none named.

4. Claude closes with one sentence. Either nothing lives only in this
   conversation and shutting the command line loses nothing, or the list
   of what it would lose.

   You should now see that one closing sentence.

## What you have afterwards

You have a statement of what a shutdown would lose, and offers to
remedy it. Nothing has been written: the write and `/save` run only if
you accept them. See [Save your work](save-your-work.md) for the save.
The reason state is kept in files and never in the conversation is
given in [Documents and records](../about/documents-and-records.md).

## If something goes wrong

The inputs record no stop conditions for `/end`. The status script
stops with a message if git is not available or if the engine is not a
git repository. In a repository it reports a merge or similar step in
progress together with the number of files in conflict, and points to
the step of a conflict and then the save.

## A worked example

A closing where all is saved:

> Nothing lives only in this conversation, and shutting the command line
> loses nothing.

A closing where something would be lost:

> Shutting the command line now would lose: the round on the intent,
> carried but not written; the verdicts on three items; and the
> promised check of the recipe, not yet run. The project `my-project`
> also has unsaved changes.

## See also

- [Save your work](save-your-work.md): the save it offers.
- [Documents and records](../about/documents-and-records.md): why state lives in files and never in the conversation.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
