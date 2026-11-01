---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 736f34c6f5483b9e
inputs:
  - .claude/skills/history/SKILL.md
  - scripts/forge-history.py
---

# Read the history of an item

This page shows how to see the whole history of one item (a position, a requirement or a part of the solution) with `/history`, for anyone who wants to know what an item says today and how it came to say it. The command only reads: it writes nothing and changes no file. A term you do not know is in the [Glossary](../reference/glossary.md).

## When to use it

Use it before you propose a change to an item, or whenever you ask why an item reads as it does. The history of a document is kept as a log beside it, and the command searches that log for the one item you name, so nothing has to be loaded whole into the conversation. [Versioning and history](../about/versioning-and-history.md) gives the reason for that arrangement.

## The command

```
/history <ID> [slug]
```

- `<ID>` is the item's ID, such as `REQ.0120`. A short form is accepted: `pos580` is read as `POS.0580`.
- `[slug]` is the project. Without it, Claude takes the project in context. `forge` is the engine's own project. If the project is ambiguous, Claude asks.
- `--full` is an option of the script. Without it, each earlier wording (the "Was" of a record) is shortened to its first sentences. With it, every one is printed whole.

## What happens

1. Claude runs the history script for the item and the project.

   You should now see the script's output printed unshortened, in three parts.

2. The first part, "Today", names the file that holds the item and gives its wording as it stands now.

   You should now see the item's text, from the line that opens it to the next item or heading.

3. The second part, "Timeline", gives one line per event, oldest first, each with its version and, where the log has one, its date. The events are:
   - `born`, `changed`, `closed`, `removed` and `approved`, from the records of every history log of the project whose subject names the item
   - `mentioned by <ID>`, from the records of other items that name it in their reason, Action or Was
   - `archive`, from the rows of the history archives that mention it

   A record's reason follows its line. Its Action and its Was follow as marked lines. The shape of a record is described in [History companion](../reference/history-companion.md).

   You should now see the item's life in order, from its birth to its latest change.

4. The third part, "Cited today", lists every other place in the project that names the item, as file and line with the line shortened. These are decisions, threads, the ledger, reviews, challenges and the other artefacts.

   You should now see what hangs on the item.

5. Claude adds at most three sentences of its own, marked as its own. They say what the item holds today, how it moved (when it was born, how many times it changed, at which version it last changed) and what hangs on it, such as a thread, a finding or a challenge among the citations.

   You should now see a short note from Claude after the script's output, marked as Claude's.

## What you have afterwards

You have the item's wording, its timeline and its citations in the conversation. Nothing is written anywhere. If the reading suggests a change, Claude proposes it in the round that owns the item; the note itself changes nothing.

## If something goes wrong

- An ID that nothing in the project knows is said so, as the script says it. Claude never guesses a near ID, so check the number and the prefix and ask again.
- The pages of the documentation, the documentation map, the renders, the resources and the working folder are never searched. They are outputs or inputs, not the project's record, so a mention there does not appear.

## A worked example

You want to know how a requirement of a project came to read as it does. The project's slug is `my-project` and the item is `REQ.0120`.

```
/history req120 my-project
```

You see the file that holds `REQ.0120` and its wording today. Below it the timeline lists the item's birth and each later change, oldest first, with the version of each, and below that the places that cite it. Claude closes with up to three sentences, marked as its own. To read every earlier wording whole, run the script with `--full`.

## See also

- [Versioning and history](../about/versioning-and-history.md): why the history is a log beside the document and is searched, never loaded whole.
- [History companion](../reference/history-companion.md): the shape of a record the script reads.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
