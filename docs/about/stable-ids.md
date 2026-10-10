---
generated: 2026-10-10
made: derived
inputs-hash: 6b26e0399228eb50
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About stable IDs

This page explains why every item in a document of the chain carries
an ID, what the ID looks like, and why the forge prefers items with
IDs over prose even where the thinking is still very abstract. It is
for anyone who reads or writes a forge document (the user), anyone
who adds to the forge (the extender) and anyone who judges whether a
project keeps the convention (the evaluator). It was put together
from `CLAUDE.md` and from the forge's own intent,
`projects/forge/10-intent.md`: the rules are the former's, the
reasons the latter's.

## What an ID is

Every item has an ID of the form `PREFIX.NNNN`: a prefix of exactly
three letters, a dot, and a four-digit number. `REQ.0010` is a
requirement; `POS.0010` is a position.

IDs are global and stable. Once given, an ID is never renumbered.
An item may move from one group to another, and it keeps its ID when
it does: the ID names the item, not its place in the document.

## How items are numbered

Items are numbered in tens, so `REQ.0010` is followed by `REQ.0020`.
Each new group starts at the next hundred: if one group runs
`REQ.0010`, `REQ.0020`, the next group begins at `REQ.0100`,
`REQ.0110`. The gaps leave room for an item to be inserted between
two others without touching anything that exists. When a group runs
out of room, the next item takes the next free number anywhere.

Groups are plain headings. A group has no ID, no metadata and no
lifecycle; it is a way of reading the items, not an entity of its
own. Groups go at most two levels deep.

## Why items with IDs, not prose

The forge writes structured items with stable IDs even at a very high
level of abstraction, and keeps narrative to the Purpose & Context and
Objective sections of a document. The reason is that an item with a
stable ID can be cited, reviewed, traced into the layer below and
changed one at a time. Prose cannot be pointed at: a reviewer
cannot name a sentence in a paragraph the way he names an item, a
decision cannot record which of several intertwined thoughts it
settles, and a change to one thought cannot be made without
rewriting the thoughts around it.

The same reasoning is why groups are only headings. Workstreams as
first-class entities, with IDs and a lifecycle of their own, were
considered and rejected as structure for its own sake: plain heading
groups together with stable global IDs achieve the same at lower
cost. The ID carries the identity; the heading only says where the
item sits for now.

## Why a fact, a position and a thread have prefixes of their own

The intent has three prefixes that could, at first sight, have been
one. They are kept apart because each says something different about
the standing of what is written.

A **position** (`POS`) is what the principal holds or wants: a stance.

A **fact** (`FCT`) is what is the case. It is stated by the principal
on his word, or by a source cited to its file; verification is never
demanded. A fact is not a stance. Without a prefix of its own, a fact
would have passed for a position, and the reader could not have told
what the principal wants from what he merely takes to be so. Making
a source's fact his own stance is a new position, not a change to the
fact.

A **thread** (`THR`) is an unresolved matter to elicit next. A thread
carries its origin: the principal's word (the default, which needs no
mark), a document by path, or Claude's synthesis. The origin is
marked so that a hypothesis of Claude's stays visibly his until the
principal takes it up. For the same reason, what Claude has worked
out is never a fact: a fact is the principal's word or a source's.

## Where the vocabulary comes from

The prefix vocabulary is a house convention. No universal standard
for ID prefixes exists; the forge's set is derived from a BRD
standard and aligned with it wherever an equivalent exists. The
requirement-side prefixes live in the assignment, the position, fact,
thread and rejected-direction prefixes in the intent, and the
finding, challenge and decision prefixes in the forge's own records.

Earlier forms were tried and dropped. Single-letter and hyphenated
prefixes such as `R-001` or `P-01` were replaced by the three-letter
dotted `PREFIX.NNNN`, aligned with the same BRD standard.

The full list of prefixes, what each means and where each lives is
the reference page below.

## See also

- [ID scheme](../reference/id-scheme.md): the prefix table and the numbering rules, exactly.
