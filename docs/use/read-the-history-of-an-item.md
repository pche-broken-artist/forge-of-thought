---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: fb6f6cf7777f2414
inputs:
  - .claude/skills/history/SKILL.md
  - scripts/forge-history.py
---

# Read the history of an item

This page shows how you see the whole history of one position, requirement or other numbered item with `/history`. It is for anyone who wants to know what an item says today, how it came to say it and what else in the project refers to it. The command only reads; it changes nothing.

## When to use it

Use it before you propose a change to an item, or whenever you ask why an item reads as it does. Each item carries a stable ID such as `REQ.0120`, and the command gathers everything the project holds about that one ID. The history of a document is a log kept beside it and is searched, never loaded whole, so this command is the way to read one item's part of it. The reason is given in [Versioning and history](../about/versioning-and-history.md).

## The command

```
/history <ID> [slug]
```

- `<ID>` is the item's ID. A short form is accepted: `pos580` is read as `POS.0580`.
- `[slug]` names the project. Without it, Claude takes the project in context, and asks if that is ambiguous. `forge` is the engine's own project.

Claude runs the history script for you. To run the script yourself, type:

```
python scripts/forge-history.py <ID> <slug>
```

Add `--full` to print every "Was" whole instead of shortened to its first sentences. A "Was" is the item's previous wording, kept in the record of the change.

## What happens

1. Claude runs the script for the item and the project.
   You should now see the item as it stands today: the file that holds it and its wording.
2. The script prints the timeline, oldest first. Each line has a version, a date where the log has one, and what happened:
   - `born`, `changed`, `closed`, `removed` or `approved`, from the history logs of the project's documents and recipes;
   - `mentioned by <ID>`, from the records of other items that name this one;
   - `archive`, from the rows of an older history table that mention it.

   A record's reason follows its line. Its Action and its Was follow as marked lines. The shape of such a record is described in [History companion](../reference/history-companion.md).
   You should now see the item's life from birth to its latest version.
3. The script prints every other place in the project that names the ID, as file and line number with the line shortened: decisions, threads, the ledger, reviews, challenges and other documents.
   You should now see what else hangs on the item.
4. Claude adds at most three sentences of its own, marked as its own: what the item says today, how it moved (born when, changed how many times, last at which version) and what hangs on it.
   You should now see a short comment set apart from the printed output.

## What you have afterwards

You have the printed history in the conversation and nothing else. Nothing is written to any file. If the reading suggests a change, Claude proposes it in the round that owns the item, and does not make it here.

## If something goes wrong

- If nothing in the project knows the ID, the script says so. Claude never guesses a near ID, so check the ID and run the command again.
- If the project is ambiguous, Claude asks which slug you mean.
- The pages of `docs/`, the documentation map, the renders, the sources, the research and `tmp/` are never searched. An ID that appears only there is reported as unknown.

## A worked example

You want the history of requirement `REQ.0120` in a project with the placeholder slug `my-project`, with every earlier wording in full:

```
python scripts/forge-history.py REQ.0120 my-project --full
```

Through the command, the same request without `--full` is:

```
/history req120 my-project
```

You see, in order:

1. The item today, with the file that holds it.
2. A timeline from its birth to its latest change, each line with a version and a date, followed by its reason.
3. The list of citations, each as file and line.
4. At most three sentences from Claude, marked as its own.

## See also

- [Versioning and history](../about/versioning-and-history.md): why the history is a log beside the document and is searched, never loaded whole.
- [History companion](../reference/history-companion.md): the shape of a record the script reads.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
