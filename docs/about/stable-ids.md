---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 0c4b0fcf1d6acf4a
inputs:
  - CLAUDE.md#ID scheme
  - projects/forge/10-intent.md#POS.0200
  - projects/forge/10-intent.md#POS.0220
  - projects/forge/10-intent.md#POS.0230
  - projects/forge/10-intent.md#POS.1790
  - projects/forge/10-intent.md#REJ.0020
  - projects/forge/10-intent.md#REJ.0100
---

# Stable IDs

A stable ID is the address of one item of a document: a three-letter
prefix and a number, given once and never changed. This page explains
why every item of the forge carries one, how the numbers are given,
and what happens in the one case where two items end up with the same
number. It is for anyone who works with the documents, extends the
forge or judges how it behaves. The prefixes themselves and the
numbering rules are listed on [ID scheme](../reference/id-scheme.md).

## What it is

Every item of an artefact carries an ID of the form `PREFIX.NNNN`.
The prefix has three letters and says what kind of item it is: a
requirement, a position, a thread, a fact, a finding. The number has
four digits as long as the number fits. It takes a fifth digit only
beyond 9999, so `REQ.10000` follows `REQ.9990`. No zero is ever added
to an existing ID when the fifth digit arrives.

IDs are global and stable. Global means the number is taken from one
sequence of the whole project, not from a sequence of a section or a
branch. Stable means the ID is never renumbered: an item keeps its
number for its whole life, and it may move from one group of a
document to another without the number changing.

The groups of a document are plain headings. They carry no ID, no
metadata and no lifecycle of their own, and they are nested at most
two levels deep.

## How it works

Numbers are given in tens: the first items of a group are
`REQ.0010`, `REQ.0020`, `REQ.0030`. Each new group starts at the next
hundred: `REQ.0100`, `REQ.0110`. When a group has no free number left
in its hundred, the next item takes the next free number anywhere in
the sequence. Every sorting of IDs is numeric, by prefix and then by
number, so that `REQ.0990` sorts before `REQ.10000`.

A number is taken at the moment of the write. There is no block of
numbers reserved for an author or a branch, and no reading over the
other branches before a number is given. Two people working on two
branches of one project may therefore both take the same number.

That is the one exception to "never renumbered": two items with one
number in one project. How the clash came about does not matter. A
merge of two branches, an edit by hand, two windows open on the same
document, or documents born apart and brought together are all settled
the same way:

- the older item keeps its number;
- the younger item takes a new number, the next free number of the
  merged state;
- the younger item receives a `changed` record in its history whose
  reason names the clash and whose `Was` field holds the old number;
- every citation of the younger item is corrected to the new number;
- where the younger item is a thread, its file under `threads/` is
  renamed with it, because a thread lives in one file named by its ID.

The younger item is the one whose `created` record is the later. At a
merge, the item of the branch merged second is the younger. Where the
histories do not decide, the principal (the person whose thinking is
being forged) decides.

The clash is found by the ledger script. The ledger is the project's
state report, made from the documents at read time. When the script
finds a number taken twice, it reports the clash and writes nothing.
The renumbering is a write into the artefacts, and Claude never does
it alone: it lays the clash out in a walkthrough (the forge's way of
working a list of decisions one item at a time, each closed with the
principal's verdict) and renumbers on the principal's word. After a
merge, this is the place where a number taken twice usually shows up;
how such a merge is finished is on
[Settle a conflict](../use/settle-a-conflict.md).

## Why

**Why items with IDs rather than prose.** An item with a stable ID
can be cited, reviewed, traced into the layer below and changed one at
a time. Prose cannot be pointed at. That is why structure is preferred
over prose even at a very high level of abstraction, and why narrative
is confined to the few sections that set the scene, such as purpose,
context and objective.

**Why groups are plain headings.** Groups with IDs and a lifecycle of
their own were considered and rejected as structure for its own sake.
Plain heading groups together with stable global IDs achieve the same
at lower cost, and an item can move between groups freely because the
group is not part of its address.

**Why three letters and a dot.** Single-letter and hyphenated prefixes
such as `R-001` or `P-01` are a rejected direction. They were replaced
by the three-letter dotted form, aligned with the convention the house
scheme is derived from. No universal standard for prefixes exists; the
set of prefixes is a house convention.

**Why the fifth digit.** A prefix has 99 hundreds. Numbered in tens,
with a new group at each hundred, a prefix may outgrow four digits on
use alone. Widening the number when that happens costs nothing, so the
scheme allows it rather than padding every existing ID.

**Why numbering in tens and groups at the next hundred.** The reason
is not recorded in the inputs of this page.

**Why a fact, a position and a thread have prefixes of their own.** A
position is what the principal holds or wants. A fact is what is the
case, stated by the principal on his word or by a source cited to its
file, and its verification is never demanded. Without a prefix of its
own, a fact would have passed for a position. Making a source's fact
into the principal's own stance is a new position, not a change to the
fact. A thread is an open matter still to be worked, and it carries
its origin: the principal's word, a document by path, or Claude's own
synthesis. The origin is marked so that a hypothesis of Claude's stays
visibly its own until the principal takes it up. What Claude has
worked out is never recorded as a fact, because a fact is the
principal's word or a source's.

**Why detection rather than blocks of IDs.** Blocks of numbers per
author, allocation of numbers over the local branches and hashed IDs
were all considered and are rejected directions. A clash is rare, a
few times a year on a project of one or two people, and detecting it
with the remedy that already exists (a renumbering with a record)
costs nothing. The rejected designs would have cost the most code of
the whole plan. So IDs stay one sequence per project, taken at the
write, and the ledger script watches for the clash.

## A worked example

A project with the placeholder slug `my-project` has an assignment
whose requirements run up to `REQ.0330`. Two people work on two
branches. Each adds one requirement, and each takes the next free
number as they see it: `REQ.0340` on both branches.

The branches are merged. The ledger script is run on the merged
state. It reports that `REQ.0340` is carried by two items and writes
nothing.

Claude reads the two `created` records. The item of the branch merged
second has the later record and is the younger. Claude lays the clash
out to the principal as one proposition in a walkthrough: the younger
item takes `REQ.0350`, the next free number of the merged state. On
the principal's word, Claude writes the new number into the
assignment, appends a `changed` record to the assignment's history
whose reason names the clash and whose `Was` reads `REQ.0340`, and
corrects every place that cited the younger item. The older item is
untouched. Had the younger item been a thread, its file under
`threads/` would have been renamed to the new number in the same step.

## See also

- [ID scheme](../reference/id-scheme.md): the prefix table and the
  numbering rules.
- [Settle a conflict](../use/settle-a-conflict.md): where a number
  taken twice usually shows up, after a merge.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
