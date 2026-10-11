---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 6efce649f3935b1e
inputs:
  - .claude/skills/end/SKILL.md
  - scripts/forge-status.py
---

# End a session

`/end` is the command that closes a working session so that you know nothing is lost. It is for the principal (the person whose thinking is being forged) who is about to shut the command line. It writes nothing and runs nothing but the status script, and every remedy it finds is an offer.

## When to use it

Use it before you close the command line, or whenever you want to know what a shutdown would lose.

## The command

```
/end
```

## What happens

1. Claude says what lives only in this conversation. That is a round not yet written, verdicts carried but not written, and anything it promised and has not done. It offers the write.

   You should now see a list of what exists only in the conversation, with an offer to write it, or a statement that there is none.

2. Claude runs the status script without the remote, so the script touches no network. It names every repository with unsaved changes (the engine and each project) and offers `/save` for each.

   You should now see each repository with unsaved changes named, or the report "clean - nothing to save".

3. Claude names the stale renders as a fact, from the Renders table of the ledger (the file that holds the state of a project). It makes no offer, because renewing the renders belongs to the release.

   You should now see the stale renders listed as they stand, with nothing proposed.

4. Claude closes with one sentence. Either nothing lives only in this conversation and shutting the command line loses nothing, or the sentence is the list of what it would lose.

   You should now see that one closing sentence.

## What you have afterwards

You know what a shutdown would lose, and you have the offers to remove the loss: the write of the round, and the save of each repository with unsaved changes. Nothing has been written or saved yet. Each remedy runs only when you say so.

## A worked example of the closing

When everything is written and saved, the closing reads:

> Nothing lives only in this conversation, and shutting the command line loses nothing.

When something is open, the closing is the list:

> Shutting the command line would lose: the verdicts of the walkthrough on the findings of the `<slug>` project, not yet written; the unsaved changes in `<slug>`.

Each item on such a list comes with its offer, the write or `/save`.

## If something goes wrong

A directory under the projects that is not under version control is reported by the status script as "not under git". That is a property of the project, not a failure, and nothing is offered for it.

## See also

- [Save your work](save-your-work.md): the save it offers.
- [Documents and records](../about/documents-and-records.md): why state lives in files and never in the conversation.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
