---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 160c56c8403dba34
inputs:
  - .claude/skills/end/SKILL.md
  - scripts/forge-status.py
---

# End a session

`/end` closes a working session by telling you what a shutdown would lose. It is for the principal (whoever's thinking is being forged) who is about to close the command line and wants to know that nothing is lost.

## When to use it

Use it before you close the command line. It writes nothing and runs nothing but two of the forge's scripts. Every remedy it finds is an offer, never an action.

## The command

```
/end
```

## What happens

1. Claude says what lives only in this conversation. That means a round not yet written, verdicts carried toward a write, and anything promised and not done. It offers the write.

   You should now see a list of what is held only in the conversation, with an offer to write it, or a statement that there is none.

2. Claude runs the status script without the remote, so no network is touched. It names every repository with unsaved changes and offers `/save` (see [Save your work](save-your-work.md)).

   You should now see each repository with unsaved changes named, or the word "clean" for those with none.

3. Claude makes the project's ledger (the single record of state, made at read time from the documents) and names stale renders as a fact. It makes no offer for them, because the renders belong to the release.

   You should now see the stale renders named, or nothing said of them where none is stale.

4. Claude closes with one sentence. Either nothing lives only in this conversation and shutting the command line loses nothing, or the sentence lists what it would lose.

   You should now see that one closing sentence.

## What you have afterwards

You have a statement of what a shutdown would lose, and offers for the write and the save. Nothing has changed on disk through `/end` itself. State lives in files and never in the conversation: see [Documents and records](../about/documents-and-records.md) for why.

## If something goes wrong

The inputs record no stop condition for `/end`. If a repository shows as not under git, the status script says so and goes on to the next one. For the terms used here, see the [Glossary](../reference/glossary.md).

## A worked example

The closing sentence in the clean case:

> Nothing lives only in this conversation, and shutting the command line loses nothing.

The closing in the other case, with placeholder names:

> Shutting the command line now would lose: the verdicts of the round on `<slug>` that are not yet written, and the changes in `<slug>` that are not yet saved.

## See also

- [Save your work](save-your-work.md): the save it offers.
- [Documents and records](../about/documents-and-records.md): why state lives in files and never in the conversation.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
