---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 7b73150fe0335ed5
inputs:
  - .claude/skills/end/SKILL.md
  - scripts/forge-status.py
---

# End a session

`/end` is the command that closes a working session by telling you what a shutdown would lose. It is for the principal (the person whose thinking is being forged) at the moment before he closes the command line. It checks three places where work can hide, and it ends with one sentence.

## When to use it

Use it when you are about to stop working and want to know that nothing is lost. Terms of the forge are explained in the [Glossary](../reference/glossary.md). Work lives in files, never in the conversation, and the reason is given in [Documents and records](../about/documents-and-records.md).

## The command

```
/end
```

The command takes no argument.

## What happens

`/end` writes nothing. It runs nothing but its scripts: the status script and the script that makes the ledger. Every remedy is an offer, which you accept or leave.

1. Claude says what lives only in this conversation. That is a round of work not yet written to a file, verdicts carried toward a write at the end of a round, and anything promised and not done. It offers the write.
   You should now see a plain list of what is held only in the conversation, or a statement that there is nothing.
2. Claude runs the status script without the remote, so the script touches no network. It names every repository with unsaved changes (the engine and each project) and offers `/save`, which is described in [Save your work](save-your-work.md).
   You should now see each repository named with its unsaved changes, or reported as clean.
3. Claude remakes the project's ledger (the file that holds the state of the project) with its script. It then names any stale renders as a fact, read from the ledger's Renders table. It makes no offer here, because renders are the business of the release.
   You should now see the stale renders named, or no mention of any.
4. Claude closes with one sentence. Either nothing lives only in this conversation and shutting the command line loses nothing, or the sentence is the list of what it would lose.
   You should now see that one closing sentence.

## What you have afterwards

You have a statement of what a shutdown would lose, and offers to remedy each loss. Nothing is changed by the command itself. The ledger is remade by the step above, and that is the only file the command touches.

## If something goes wrong

The inputs record no stop conditions for `/end`. The status script reports a repository that is not under version control as "not under git", and that is a state, not a failure. The status script also reports whether the settings the forge needs on your machine are registered, and tells you to run `/setup` when they are missing.

## A worked example

A generic closing, after a round that was written and saved:

```
Nothing lives only in this conversation, and shutting the command
line loses nothing.
```

A generic closing when work would be lost:

```
Shutting the command line would lose: the round on the open threads
(answers carried, not written), and the unsaved changes in the
project `my-project`.
```

In the second case you accept the offered write and the offered `/save` first, and run `/end` again.

## See also

- [Save your work](save-your-work.md): the save it offers.
- [Documents and records](../about/documents-and-records.md): why state lives in files and never in the conversation.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
