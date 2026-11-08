---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 3348d0de37929d01
inputs:
  - .claude/skills/history/SKILL.md
  - scripts/forge-history.py
---

# Read the history of an item

`/history` prints the whole history of one item of a project, such as a position, a requirement or a part of the solution, by its ID. This page is for you, the principal (the person whose thinking is forged), when you want to know what an item says today, how it came to say it and what else in the project mentions it.

## When to use it

Use it before you change an item, so that you see what it was and why it moved. Use it also when you only want to know where an item came from and what depends on it. The history is kept in a log beside each document and is searched by a script, never loaded whole into the conversation. The reasons are on [Versioning and history](../about/versioning-and-history.md).

## The command

```
/history <ID> [slug]
```

- `<ID>` is the item's ID. A short form such as `pos580` is accepted and read as `POS.0580`.
- `[slug]` is the project. Without it, Claude takes the project in context. `forge` is the engine's own project. If the project is ambiguous, Claude asks.

A real line, with a placeholder slug:

```
/history req120 <slug>
```

Add `--full` when you want every "Was" (the wording before a change) printed whole. Without it each "Was" is shortened to its first sentences.

## What happens

1. Claude names the project: the slug you gave, else the project in context.

   You should now see no question, unless the project was ambiguous.

2. Claude runs `python scripts/forge-history.py <ID> <slug>` and prints what the script printed, unshortened. The script reads only, changes nothing and uses no model. It prints three parts:

   - Today: the file that holds the item and its wording as it stands.
   - Timeline: one line per event, oldest first, each with its version and, where the log has one, its date. An event is one of these:
     - `born`, `changed`, `closed`, `removed` or `approved`, from the records of the history logs that name the ID.
     - `mentioned by <ID>`, from the records of other items that name it.
     - `archive`, from the rows of an older history table that mention it.

     A record's reason follows its line, then its Action (what you must do after the change) and its Was.
   - Cited today: every other place in the project that names the ID, as file and line, such as decisions, threads, the ledger, reviews, challenges and other artefacts.

   You should now see the item's wording, its timeline and its citations, wrapped to a readable width.

3. Claude adds at most three sentences of its own, marked as its own. They say what the item says today, how it moved (born when, changed how many times, last at which version) and what hangs on it, such as a thread, a finding or a challenge among the citations.

   You should now see a short note from Claude clearly marked as its own.

## What you have afterwards

You have the item's full reading in the conversation. Nothing is written anywhere: the command is read-only. If the reading suggests a change, Claude proposes it in the round that owns the item, not here.

## If something goes wrong

- An ID that nothing in the project knows is said so. Claude never guesses a near ID. Check the ID and the slug, then run it again.
- The pages of `docs/`, the documentation map, the renders, the resources and `tmp/` are never searched. An item mentioned only there does not show.

The shape of a record the script reads is on [History companion](../reference/history-companion.md). Any term of the forge you do not know is in the [Glossary](../reference/glossary.md).

## A worked example

You want to see the history of requirement 120 in a project with the placeholder slug `<slug>`:

```
/history req120 <slug>
```

The script prints, in this shape:

```
Today
  <file that holds the item>
  <the item's wording>

Timeline
  <version> <date>  born
      <the reason of the record>
  <version> <date>  changed
      <the reason of the record>
      Action: <what you must do after the change>
      Was: <the first sentences of the old wording>
  <version>         mentioned by <ID of another item>

Cited today
  <file>:<line>  <the line, shortened>
```

Below it Claude adds, marked as its own, one to three sentences: what the item says, that it was born at the first version listed and changed once since, and that a thread cites it. To see the old wordings whole, you run the same command with `--full` at the end.

## See also

- [Versioning and history](../about/versioning-and-history.md): why the history is a log beside the document and is searched, never loaded whole.
- [History companion](../reference/history-companion.md): the shape of a record the script reads.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
