---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: fa16e6ce110e3205
inputs:
  - .claude/skills/history/SKILL.md
  - scripts/forge-history.py
---

# Read the history of an item

This page shows how to see the whole history of one item (a position,
a requirement, a part of the solution design) with `/history`. It is
for the principal, the person whose thinking is forged, and for anyone
who wants to know how an item came to say what it says before
changing it.

## When to use it

Use it before you propose a change to an item, or whenever you want
to know when an item was born, how often it changed and what refers
to it. This is the one way Claude reads an item's history. The
history is a log kept beside each document, and the command searches
it for the one item instead of loading the whole log into the
conversation (see [Versioning and history](../about/versioning-and-history.md)).

## The command

```
/history req0120 my-project
```

The form is `/history <ID> [slug]`.

- `<ID>` is the item's ID. A short form such as `req0120` is
  accepted and read as `REQ.0120`.
- `[slug]` is the project. Left out, Claude takes the project in
  context and asks if that is ambiguous. `forge` is the engine's own
  project.

Add `--full` to the script's call if you want every Was printed whole
instead of shortened to its first sentences. Terms of the forge are
explained in the [Glossary](../reference/glossary.md).

## What happens

1. Claude runs the history script for the item and the project.
   You should now see the item as it stands today: the file that
   holds it and its wording.
2. The script prints the timeline, oldest first. You should now see
   one line per event with its version and, where the log has one,
   its date. The events come from three places:
   - the archive rows of the history archives that mention the item;
   - the item's own records (born, changed, closed, removed,
     approved);
   - the records of other items that mention it.
   A record's reason follows its line, and its Action and its Was
   follow as marked lines. The shape of a record is described in
   [History companion](../reference/history-companion.md).
3. The script prints every other citation in the project. You should
   now see each place that names the item, as file and line with the
   line shortened: decisions, threads, the ledger, reviews,
   challenges and the other artefacts.
4. Claude prints all of this unshortened and then adds at most three
   sentences of its own, marked as its own. You should now see what
   the item says today, how it moved (born when, changed how many
   times, last at which version) and what hangs on it (a thread, a
   finding or a challenge among the citations).

## What you have afterwards

You have the item's history in the conversation. Nothing is written
and nothing is derived from Claude's three sentences. If the reading
suggests a change, it is proposed in the round that owns the item.
The command is read-only.

## If something goes wrong

- An ID that nothing in the project knows is said so, as the script
  says it. Claude never guesses a near ID. Check the ID and the slug.
- The pages of `docs/`, the documentation map, the renders, the
  resources and `tmp/` are never searched, because they are outputs
  or inputs and not the project's record. A mention there does not
  show.

## A worked example

You type:

```
/history req0120 my-project
```

What you see has this shape (the lines are generic):

```
Today
  10-intent.md  REQ.0120  The system shall <what the item says>.

Timeline
  0.3   2026-01-10  born        <reason of the record>
  0.7   2026-02-02  changed     <reason of the record>
                    Action: <what to do after the change>
                    Was: <the earlier wording, shortened>
  1.0   2026-03-01  mentioned by REQ.0200  <reason of that record>

Cited today
  threads.md:41   <the line that names the item>
```

Claude then adds, marked as its own: the item says <what it says>;
it was born at 0.3 and changed once, last at 0.7; an open thread
cites it.

## See also

- [Versioning and history](../about/versioning-and-history.md): why the history is a log beside the document and is searched, never loaded whole.
- [History companion](../reference/history-companion.md): the shape of a record the script reads.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
