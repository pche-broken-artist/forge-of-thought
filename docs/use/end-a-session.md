---
generated: 2026-10-23
version: 5.34
made: mirrored
inputs-hash: 811f2e955ed8e541
inputs:
  - .claude/skills/end/SKILL.md
  - scripts/forge-status.py
---

# End a session

`/end` is the command that tells you, before you close the command line, whether closing it would lose anything. It is for the principal (the person whose thinking is being forged) at the end of a working session, and it answers with a list or with one sentence of reassurance.

## When to use it

Use it when you are about to stop working and shut the command line. A session is one running conversation with Claude. Whatever is only in that conversation, and not in a file, is gone when it closes, because state lives in files (see [Documents and records](../about/documents-and-records.md)).

## The command

```
/end
```

The command takes no argument.

## What happens

1. Claude says what lives only in this conversation. That means a round of work not yet written, verdicts carried but not written, and anything Claude promised and has not done. It offers the write for what is agreed.

   You should now see a plain statement of what is only in the conversation, or that nothing is.

2. Claude runs the status script without the remote, so it touches no network. The script reports each repository, the engine and every project, with its unsaved changes or "clean - nothing to save", its branch, its last commit and its origin. It also says whether the global git registration is in place and names the missing keys, with the advice to run `/setup`. Claude names every repository with unsaved changes and offers `/save` for it (see [Save your work](save-your-work.md)).

   You should now see each repository with unsaved changes named, or the statement that every one is clean.

3. Claude makes the ledger of the project, the report of its state made from its documents at the moment of reading. It names the renders the ledger lists as stale, as a fact. It makes no offer for them, because the renders are left to the release.

   You should now see the stale renders named, or none.

4. Claude closes with one sentence. Either nothing lives only in this conversation and shutting the command line loses nothing, or the list of what it would lose.

   You should now see that one closing sentence.

## What you have afterwards

You have a statement of what a shutdown would lose, and an offer for each remedy that is yours to accept: the write of an agreed round and the `/save` of each repository with changes. `/end` itself writes nothing and runs nothing but its scripts. A remedy happens only if you say yes to its offer.

## If something goes wrong

- A repository shows "not under git". It is a project outside git, and there is nothing for `/save` to do there.
- The status script reports a standing step of a conflict in a repository. It names the number of files in conflict and says that the step of a conflict comes first, then the save. Settle it before you close.
- The registration line reports missing keys. Run `/setup`, as the line says.

The messages of the other scripts are not recorded in the inputs of this page.

## A worked example

The closing when everything is safe:

> Nothing lives only in this conversation, every repository is clean, and shutting the command line loses nothing.

The closing when something would be lost:

> Shutting the command line now would lose: the round on the intent, agreed but not written (offer: write it); unsaved changes in the project `my-slug` (offer: `/save my-slug`); and the render `my-render` is stale (a fact, no offer).

## See also

- [Save your work](save-your-work.md): the save it offers.
- [Documents and records](../about/documents-and-records.md): why state lives in files and never in the conversation.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.34 from the files the front-matter names; never edited by hand.
