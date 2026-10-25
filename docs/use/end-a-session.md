---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: b4b2806dee9599df
inputs:
  - .claude/skills/end/SKILL.md
  - scripts/forge-status.py
---

# End a session

`/end` closes a working session by telling you what a shutdown would lose. It is for the principal (the person whose thinking is being forged) who is about to close the command line and wants to know that nothing is lost.

## When to use it

Use it at the end of a working session, before you close the command line. It changes nothing. Every remedy it finds is an offer that you accept or leave.

## The command

```
/end
```

## What happens

1. Claude says what lives only in this conversation. That is a round not yet written, verdicts carried but not written, and anything it promised and has not done. It offers to write what is agreed so far.

   You should now see a list of what exists only in the conversation, or a statement that there is none.

2. Claude runs the status script, without the remote, so it touches no network. It names every repository with unsaved changes and offers [`/save`](save-your-work.md) for them.

   You should now see each repository with unsaved changes named, or no repository named.

3. Claude makes the ledger of the project again with its script. The ledger is the single record of state, made at read time. Claude names the renders it marks stale as a fact. It makes no offer, because renders belong to the release.

   You should now see the stale renders named, or none.

4. Claude closes with one sentence. Either nothing lives only in this conversation and shutting the command line loses nothing, or the sentence is the list of what it would lose.

   You should now see that one closing sentence.

## What you have afterwards

You have a plain answer to the question of whether you can close. `/end` writes nothing and runs nothing but its scripts, so the state of your files is the same as before. If it listed something, you decide whether to accept the write or the save it offered.

## If something goes wrong

The inputs record no stop conditions and no messages of `/end` itself. If it lists something it would lose, that is not a fault. Accept the offered write or save, or leave the matter and close knowing the loss. State lives in files and never in the conversation; the reason is given in [Documents and records](../about/documents-and-records.md).

## A worked example of the closing

Suppose one round was agreed but not written, and one project has unsaved changes. The closing sentence is the list:

```
Shutting the command line now would lose: the round on the open
matters of project <slug>, agreed and not yet written; and the
unsaved changes in project <slug>. Shall I write the round?
```

Suppose everything is written and saved. The closing sentence is:

```
Nothing lives only in this conversation, and shutting the command
line loses nothing.
```

## See also

- [Save your work](save-your-work.md): the save it offers.
- [Documents and records](../about/documents-and-records.md): why state lives in files and never in the conversation.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
