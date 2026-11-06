---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: be961d792ca8dde4
inputs:
  - .claude/skills/history/SKILL.md
  - scripts/forge-history.py
---

# Read the history of an item

`/history` prints the whole history of one item of a project, such as a position, a requirement or a part of a solution, found by its ID. It is for you when you want to know how an item came to read as it does before you propose a change to it. Claude is the agent that runs in Claude Code and does the work with you, and the principal is the person whose thinking is being forged.

## When to use it

- You want to see what an item says today and every change it went through.
- You want to know what else in the project names it, such as a thread, a finding or a challenge.
- Claude is about to propose a change to an item: this is the one way it reads the item's history first, because the history is searched for the one item and never loaded whole into the conversation (see [Versioning and history](../about/versioning-and-history.md)).

## The command

```
/history <ID> [slug]
```

- `<ID>` is the item's ID in the form `PREFIX.NNNN`. A short form is accepted: `pos580` is read as `POS.0580`.
- `[slug]` names the project. Without it, Claude takes the project in context, and asks if that is ambiguous. `forge` is the engine's own project.
- `--full` prints every `Was` (the earlier wording of a record) whole instead of shortened.

## What happens

1. Claude settles the project from the slug or from context.

   You should now see no question, or one question if the project is ambiguous.

2. Claude runs the history script for the ID and prints what the script printed, unshortened. The script only reads and changes nothing, and no model is involved in it. It prints three parts:
   - Today: the file that holds the item and its wording as it stands.
   - Timeline: one line per event, oldest first, each with its version, its date where the log has one, and what happened (`born`, `changed`, `closed`, `removed`, `approved`). It also shows `mentioned by <ID>` where the record of another item names this one, and `archive` where a row of an older history table mentions it. A record's reason follows its line, with its action and its `Was` as marked lines. `Was` is shortened to its first sentences unless you gave `--full`.
   - Cited today: every other place in the project that names the ID, as file and line, with the line shortened. These are decisions, threads, the ledger (the state of the project, made at read time), reviews, challenges and the other documents.

   You should now see the three parts, one after the other.

3. Claude adds at most three sentences of its own, marked as its own. They say what the item says today, how it moved (when it was born, how many times it changed, at which version it last changed) and what hangs on it.

   You should now see a short remark marked as Claude's.

The record shape the script reads is described in [History companion](../reference/history-companion.md).

## What you have afterwards

You have the item's history on screen. Nothing is written anywhere. If the reading suggests a change, Claude proposes it in the round that owns the item, not in this command.

## If something goes wrong

- The ID is unknown to the project: the script says that nothing in the project knows it. Claude does not guess a near ID. Check the ID and the project slug and run it again.
- The project is unclear: Claude asks which one you mean. Give the slug.

The pages of `docs/`, the documentation map, the renders, the sources, the research and `tmp/` are never searched, because they are outputs or inputs, not the project's record.

## A worked example

You want the full history of a requirement in a project with the placeholder slug `my-project`.

```
/history REQ.0120 my-project --full
```

The script prints the file and wording of `REQ.0120` under Today. Under Timeline it prints the events oldest first, for instance a `born` line, then a `changed` line with its reason, its action and its whole `Was`. Under Cited today it lists the decisions and threads that name the ID. Claude then adds up to three sentences marked as its own.

## See also

- [Versioning and history](../about/versioning-and-history.md): why the history is a log beside the document and is searched, never loaded whole.
- [History companion](../reference/history-companion.md): the shape of a record the script reads.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
