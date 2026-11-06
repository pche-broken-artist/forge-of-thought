---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 864d0f6591897f4d
inputs:
  - .claude/skills/end/SKILL.md
  - scripts/forge-status.py
---

# End a session

`/end` is the command that tells you what a shutdown of the command line would lose, so that you close a working session knowing nothing is lost. It is for the principal (whoever's thinking is being forged) at the end of a working session. It writes nothing and runs nothing but its scripts. Every remedy it finds is an offer that you accept or leave.

## When to use it

Use it before you close the command line, or before you leave a conversation you will not return to. Claude is the assistant that runs the forge in that command line. What lives only in a conversation is gone when the conversation is closed, because the forge keeps its state in files. The reason is given on [Documents and records](../about/documents-and-records.md).

## The command

```
/end
```

The command takes no argument.

## What happens

1. Claude says what lives only in this conversation. That is a round of work not yet written, verdicts carried but not written (a verdict is your answer to one item of a walkthrough, the one-item-at-a-time way of settling a list), and anything Claude promised and has not done. It offers the write.

   You should now see a plain statement of what is carried in the conversation only, or a statement that nothing is.

2. Claude runs the status script without the remote, so no network is touched. It names every repository with unsaved changes and offers `/save`, the command described on [Save your work](save-your-work.md). The script lists the engine and each project in turn. For each it shows its unsaved changes or the line "clean - nothing to save", the branch, the last commit and the origin. It also says when a conflict is standing in a repository, and when a project is not under git.

   You should now see each repository with changes named, and an offer to save it.

3. Claude makes the ledger of the project, the file that holds its state and is made at read time from the documents. It names the stale renders as a fact, read from the ledger's Renders table. A render is an output generated from the documents of the chain. It makes no offer for them, because renders belong to the release.

   You should now see the stale renders named, or no mention of any.

4. Claude closes with one sentence. Either nothing lives only in this conversation and shutting the command line loses nothing, or it gives the list of what a shutdown would lose.

   You should now see that one sentence.

## What you have afterwards

You have a statement of what a shutdown would lose, and offers for what can be saved. Nothing has been written, committed or changed by `/end` itself. If you accept an offer, the write or the save is a step of its own.

## If something goes wrong

The inputs record no stop condition of `/end`. The status script reports a repository that is not under git as "not under git". It reports a conflict in progress with the number of files in conflict, and says the conflict is settled first, then saved.

## A worked example

This is the closing of two runs, generic and taken from no real session.

When nothing is at risk:

> Nothing lives only in this conversation, and shutting the command line loses nothing.

When something is:

> Shutting the command line now would lose: the round on the open items of `my-project`, carried as verdicts and not yet written; unsaved changes in `my-project`.

## See also

- [Save your work](save-your-work.md): the save it offers.
- [Documents and records](../about/documents-and-records.md): why state lives in files and never in the conversation.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
