---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 46e1a5333813346d
inputs:
  - .claude/skills/history/SKILL.md
  - scripts/forge-history.py
---

# Read the history of an item

This page shows how to see the whole history of one item of a project (a position, a requirement or a part of a solution) with the command `/history`. It is for the user, the principal (the person whose thinking is forged), who wants to know how an item came to say what it says before changing it.

## When to use it

Use it when you want to know when an item was born, how often it changed, why, and what else in the project refers to it. Claude uses the same command before it proposes a change to an item. The history is kept as a log beside each document, so the command searches the log for the one item instead of loading the whole log into the conversation. Why the history is kept that way is explained in [Versioning and history](../about/versioning-and-history.md).

## The command

```
/history <ID> [slug]
```

- `<ID>` is the item's ID, for example `REQ.0120`. A short form such as `req120` is accepted and read as `REQ.0120`.
- `[slug]` is the project. Without it, Claude takes the project in context, and asks you if that is ambiguous. `forge` is the engine's own project.
- `--full` prints every `Was` (the earlier wording a record keeps) whole instead of shortened. Without it, each `Was` is cut to its first sentences.

An example that can be typed as it stands:

```
/history req120 my-project
```

## What happens

1. Claude runs the history script for the item and the project, and prints what the script printed, unshortened. You should now see three parts.
2. The first part, **Today**, names the file that holds the item and gives its wording as it stands now. You should now see the item's text from the line that opens it to the next item or heading.
3. The second part, **Timeline**, has one line per event, oldest first, each with its version and, where the log has one, its date. The events are:
   - `born`, `changed`, `closed`, `removed` and `approved`, taken from the history logs of the project whose records name the item
   - `mentioned by <ID>`, taken from the records of other items that name this one in their reason, `Action` or `Was`
   - `archive`, taken from the rows of the history archives that mention the item

   After a record's line come its reason, then its `Action` and its `Was` as marked lines. You should now see the item's moves in the order they happened.
4. The third part, **Cited today**, lists every other place in the project that names the item, as file and line with the line shortened: decisions, threads, the ledger, reviews, challenges and the other artefacts. You should now see what hangs on the item.
5. Claude adds at most three sentences of its own, marked as such. They say what the item says today, how it moved (born when, changed how many times, last at which version) and what hangs on it. You should now see these sentences set apart from the script's output.

The pages of `docs/`, the documentation map, the renders, the resources and the working folder are never searched. They are outputs or inputs, not the project's record.

## What you have afterwards

You have the item's whole story on screen. Nothing is written: the command is read-only, it runs nothing but its script, and it changes no file. A change that the reading suggests is proposed in the round that owns the item, never by this command.

## If something goes wrong

- If no item and no record in the project carries the ID, the script says so. Claude does not guess a near ID. Check the ID and the project slug, and run the command again.
- If Claude cannot tell which project you mean, it asks. Name the slug, or `forge` for the engine's own project.
- A record is read in the shape described in [History companion](../reference/history-companion.md). Lines of a log that are not records, such as the heading or a comment, are skipped.

## A worked example

You want to know how requirement `REQ.0120` of a project called `my-project` came to be.

```
/history req120 my-project
```

The script prints the file that holds `REQ.0120` and its wording today. Under Timeline it prints, oldest first, a line for the version where the item was born, a line for each later change with its reason and its `Was`, and a line for any record of another item that mentions it. Under Cited today it lists, for instance, a thread and a decision that name it.

Claude then closes with at most three sentences of its own, marked as such: the item says this today, it was born at one version and changed twice, last at a later version, and a thread still refers to it.

To read every earlier wording whole, run the same command with the flag:

```
/history req120 my-project --full
```

## See also

- [Versioning and history](../about/versioning-and-history.md): why the history is a log beside the document and is searched, never loaded whole.
- [History companion](../reference/history-companion.md): the shape of a record the script reads.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
