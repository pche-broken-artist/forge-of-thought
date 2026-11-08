---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: ecd6548426013080
inputs:
  - .claude/skills/end/SKILL.md
  - scripts/forge-status.py
---

# End a session

`/end` is the command that tells you, before you close the command line, what a shutdown would lose. It is for you, the principal (the person whose thinking is being forged), at the end of a working session (one run of Claude with you, from its start to the moment you close it).

## When to use it

Use it when you are about to stop working and want to know that nothing is lost.

## The command

```
/end
```

## What happens

`/end` writes nothing. It runs nothing but its scripts. Every remedy it finds is an offer, never an action.

1. Claude says what lives only in this conversation. That means a round of work not yet written, verdicts carried but not written, and anything promised and not done. It offers the write.

   You should now see a list of what is held only in the conversation, with the offer to write it, or a statement that there is nothing of the kind.

2. Claude runs the status script without the remote, so nothing touches the network. It names every repository with unsaved changes and offers `/save` for them.

   You should now see each repository named with its unsaved changes, or told that it is clean.

3. Claude makes the ledger (the file that holds the state of the project, made when it is read) with its script. It names the stale renders as a fact from the ledger's Renders table. It makes no offer, because renders belong to the release.

   You should now see the stale renders named, or none named.

4. Claude closes with one sentence. Either nothing lives only in this conversation and shutting the command line loses nothing, or the list of what it would lose.

   You should now see that one closing sentence.

## What you have afterwards

You have a plain statement of what a shutdown would lose. Nothing has been written, saved or changed by `/end` itself. What you decide to keep is written through the offers it made: the write of your round, and [Save your work](save-your-work.md).

## If something goes wrong

The inputs record no stop condition for `/end`. If the status script prints a repository as "not under git", that repository has no unsaved changes to name, because the forge does not track it with git.

## A worked example

The closing, when everything is kept in files (the project slug is a placeholder):

```
Nothing lives only in this conversation, every repository is clean,
and no render of my-project is stale: shutting the command line
loses nothing.
```

The closing, when something would be lost:

```
A shutdown would lose:
- the verdicts of this round, carried but not written (I offer the write)
- unsaved changes in my-project (I offer /save)
```

## See also

- [Save your work](save-your-work.md): the save it offers.
- [Documents and records](../about/documents-and-records.md): why state lives in files and never in the conversation.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
