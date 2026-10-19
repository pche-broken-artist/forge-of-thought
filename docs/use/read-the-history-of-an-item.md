---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 0e34756fe837287b
inputs:
  - .claude/skills/history/SKILL.md
  - scripts/forge-history.py
---

# Read the history of an item

This page shows how to see the whole history of one item (a position, a requirement or a part of a solution) with the command `/history`. It is for you, the principal (the person whose thinking is being forged), when you want to know where an item stands and how it got there. The command only reads: it changes no file.

## When to use it

Use it before you change an item, or when you wonder why an item says what it says. Claude uses the same command before it proposes a change to an item. The history of a document is kept as a log beside it, and the command searches that log for the one item you name, so nobody has to read the whole log (see [Versioning and history](../about/versioning-and-history.md)).

## The command

```
/history <ID> [slug]
```

- `<ID>` is the item's identifier, such as `REQ.0120`. A short form is accepted, so `pos580` is read as `POS.0580`.
- `[slug]` is the project. Without it, Claude takes the project in context. `forge` is the engine's own project. If the project is ambiguous, Claude asks.

Add `--full` when the script is run to print every "Was" whole instead of shortened.

## What happens

1. Claude settles the project from the slug or from the context.

   You should now see the project named, or one question if it was ambiguous.

2. Claude runs the history script for the ID and prints what the script printed, unshortened. The output has three parts:

   - Today: the file that holds the item and its wording as it stands now.
   - Timeline: one line per event, oldest first, with its version and, where the log has one, its date. An event is the item being born, changed, closed, removed or approved. The reason of a record follows its line, with its Action and its Was marked. Was is shortened to its first sentences unless `--full` is given.
   - Cited today: every other place in the project that names the ID, as file and line with the line shortened. These are the decisions, threads, ledger, reviews, challenges and other artefacts.

   The timeline also lists records of other items that mention this one, and rows of the history archives (tables kept from before the log began) that carry the ID.

   You should now see the item's wording, then its timeline from oldest to newest, then the list of citations.

3. Claude adds at most three sentences of its own, marked as its own. They say what the item says today, how it moved (born when, changed how many times, last at which version) and what hangs on it (a thread, a finding or a challenge among the citations).

   You should now see a short note from Claude marked as its own, below the script's output.

## What you have afterwards

You have the item's history in the conversation and nothing else. No file is written. If the reading suggests a change, Claude proposes it in the round that owns the item, not in this command.

## If something goes wrong

- An ID that nothing in the project knows (no item and no record) is said so. Claude does not guess a near ID. Check the ID and the project, then ask again.
- The pages of `docs/`, the documentation map, the renders, the sources, the research and `tmp/` are never searched. Only the project's own record is read, so a mention there does not appear.

## A worked example

You want to know how a requirement of a project came to be. You type:

```
/history req120 <slug>
```

Claude reads `req120` as `REQ.0120` and runs the script for the project `<slug>`. It prints the file and the wording of the requirement as it stands, then the timeline: the version in which the requirement was born, each later version that changed it, with the reason and the previous wording, and any record of another item that names it. Below that come the places that cite it today. Claude closes with up to three sentences marked as its own, for example that the requirement was born early, was changed twice and is cited by an open thread. If you want each earlier wording whole, you ask for `--full`.

## See also

- [Versioning and history](../about/versioning-and-history.md): why the history is a log beside the document and is searched, never loaded whole.
- [History companion](../reference/history-companion.md): the shape of a record the script reads.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
