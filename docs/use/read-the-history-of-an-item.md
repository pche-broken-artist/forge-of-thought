---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 20530f5ebb494f7a
inputs:
  - .claude/skills/history/SKILL.md
  - scripts/forge-history.py
---

# Read the history of an item

This page shows how to see the whole history of one item (a position, a requirement or any other part with an ID) by typing `/history`. It is for you, the principal (the person whose thinking is forged), when you want to know what an item says today and how it came to say it.

## When to use it

Use it when you want to know how one item moved: when it was born, how often it changed and what else in the project names it. Claude reads an item's history the same way before it proposes a change to that item. The history is kept as a log beside each document and is searched for one item at a time, never loaded whole. The reasons are on [Versioning and history](../about/versioning-and-history.md).

## The command

```
/history <ID> [slug]
```

- `<ID>` is the item's ID, such as `REQ.0120`. A short form such as `req120` is accepted and read as `REQ.0120`.
- `[slug]` is the project. Without it the command uses the project in context. `forge` is the engine's own project. If the project is ambiguous, Claude asks.
- `--full` prints every Was whole. Without it each Was is shortened to its first sentences.

The command is read-only. It writes nothing and runs nothing but its script.

## What happens

1. Claude takes the project from the slug you gave, else from the context.
   You should now see no question, or one question if the project is ambiguous.
2. Claude runs the history script for the item and prints what the script printed, unshortened. The output has three parts:
   - Today: the file that holds the item and its wording as it stands now.
   - Timeline: one line per event, oldest first, each with its version and, where the log has one, its date. The events are `born`, `changed`, `closed`, `removed` and `approved`, taken from the history logs of the project. Where another item's record names this one, the line reads `mentioned by <ID>`. Rows of the history archives that mention the item appear as `archive`. A record's reason follows its line, and its Action and Was follow as marked lines. The shape of a record is described on [History companion](../reference/history-companion.md).
   - Cited today: every other place in the project that names the ID, as file and line number with the line shortened. These are decisions, threads, the ledger, reviews, challenges and the other documents.

   You should now see the item's wording first, then its timeline from oldest to newest, then the list of citations.
3. Claude adds at most three sentences of its own, marked as Claude's. They say what the item says today, how it moved (born when, changed how many times, last at which version) and what hangs on it (a thread, a finding or a challenge among the citations).
   You should now see a short remark clearly marked as Claude's own, after the script's output.

## What you have afterwards

You have the full history of one item on screen. Nothing is written anywhere. If the reading suggests a change, Claude proposes it in the round that owns the item, not in this command.

The script does not search the pages of the documentation, the documentation map, the renders, the sources, the research or the `tmp/` folder. They are outputs or inputs, not the project's record.

## If something goes wrong

- If nothing in the project knows the ID, the script says so, and Claude passes that on. The command never guesses a near ID.
- If the project is ambiguous, Claude asks which one you mean. Give the slug as the second argument.
- If the ID is not of the shape `PREFIX.NNNN` and not a short form, the script does not read it as an ID. Retype it, for example `req120`.

## A worked example

You want the history of requirement 120 in a project with the slug `my-project`.

```
/history req120 my-project
```

Claude runs the script and prints three parts. First comes the file that holds `REQ.0120` and its wording today. Then comes the timeline, for example a `born` line at an early draft version, a few `changed` lines with their reasons, and a `mentioned by` line where another item's record names it. Last come the citations, such as a decision or a thread that names `REQ.0120`, each as file and line.

Below that Claude adds up to three sentences, marked as its own, such as "Claude: the requirement was born at 0.2 and changed three times, last at 1.1; a thread still cites it." To see every Was in full, add the flag:

```
/history req120 my-project --full
```

## See also

- [Versioning and history](../about/versioning-and-history.md): why the history is a log beside the document and is searched, never loaded whole.
- [History companion](../reference/history-companion.md): the shape of a record the script reads.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
