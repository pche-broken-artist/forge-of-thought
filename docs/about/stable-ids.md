---
generated: 2026-10-23
version: 5.34
made: derived
inputs-hash: 465b46285f195657
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

A stable ID is the address every item of a document carries, in the
form `PREFIX.NNNN`. Once an item has its ID, the number is never
renumbered. This page explains why every item carries such an ID and
why the number does not change. It also explains the one case where
a number does change: two items in one project that share one
number. It is written for anyone who uses the forge, extends it or
evaluates it. The prefixes themselves and the numbering rules are
listed in [ID scheme](../reference/id-scheme.md).

## What it is

An item is one requirement, one position, one thread or any other
single entry of a document. Each item carries an ID made of two
parts:

- a prefix: three letters that say what kind of item it is, such as
  `REQ` for a requirement or `POS` for a position the principal (the
  person whose thinking is being forged) holds;
- a number: four digits as long as the number fits.

The number takes a fifth digit only beyond 9999 (`POS.10000`). No
zero is added to an existing ID. Every sorting of IDs is numeric, by
prefix and then by number.

IDs are global and stable. An item keeps its ID for its whole life.
An item may move from one group of a document to another, and its ID
does not change. Groups are plain headings: they carry no ID, no
metadata and no lifecycle. A document has at most two levels of
groups.

## How it works

### Numbering

Items are numbered in tens: `REQ.0010`, `REQ.0020`. Each new group
starts at the next hundred: `REQ.0100`, `REQ.0110`. When a group
runs out of room, the next item takes the next free number anywhere.

IDs are one sequence per project. A number is taken at the moment
the item is written. There are no blocks of numbers set aside for
one author or for one branch.

### Two items with one number

A number can end up on two items in one project. This can happen in
several ways:

- two branches merged, each of which took the same number;
- a number typed by hand;
- documents of one project written apart from each other.

However it happened, the clash is settled the same way:

1. The older item keeps its number. The older item is the one whose
   `created` record in the history is earlier. At a merge, the item
   from the branch merged second is the younger. Where the histories
   do not decide, the principal decides.
2. The younger item takes a new number. At a merge, this is the next
   free number of the merged state.
3. The younger item gets a `changed` record in its history. The
   reason of the record names the clash, and its `Was` field holds the
   old number.
4. Every citation of the younger item is corrected to the new number.
5. If the younger item is a thread (one open matter of the intent,
   kept in a file of its own), its file is renamed with it.

The ledger (the state of a project, made by a script from the
documents at read time) reports the clash. The ledger script writes
nothing into the documents. The renumbering is a write into the
artefacts. Claude does it together with the principal, in a
walkthrough (a list of decisions worked one item at a time). Claude
never renumbers on its own.

After a merge of two branches, this is where a number taken twice
usually shows up. See [Settle a conflict](../use/settle-a-conflict.md).

## Why

### Why items instead of prose

An item with a stable ID can be cited. It can be reviewed, traced
into the layer below and changed one at a time. Prose cannot be
pointed at. This holds even for very abstract content. Narrative is
kept to the sections that set out purpose and context and the
objective.

### Why the number never changes

The reason for stability is the same as the reason for items: an ID
is only useful as an address if it keeps pointing at the same item.
A citation, a review or a trace into the layer below relies on it.

### Why a fifth digit

A prefix may outgrow four digits through use alone. Items are
numbered in tens and every new group starts at the next hundred, so
the numbers of a busy prefix climb quickly. The wider form costs
nothing to keep.

### Why a fact, a position and a thread have prefixes of their own

A fact (`FCT`) is what is the case. It is stated by the principal on
his own word, or by a source cited to its file. A position (`POS`) is
what the principal holds or wants. Without a prefix of its own, a
fact would pass for a position. A fact of a source becomes the
principal's stance only as a new position.

A thread (`THR`) carries its origin:

- the principal's word, the default, which needs no mark;
- a document, cited by its path;
- Claude's own synthesis.

The origin is kept so that a hypothesis of Claude's stays visibly
Claude's until the principal takes it up. For the same reason, what
Claude has worked out is never recorded as a fact.

### Why three-letter dotted prefixes

Single-letter and hyphenated prefixes (`R-001`, `P-01`) were rejected
and replaced by the three-letter dotted form `PREFIX.NNNN`. No
universal standard for prefixes exists. The prefixes are a house
convention, aligned with an existing requirements-document standard
where an equivalent exists.

### Why groups have no IDs

Workstreams as entities with their own IDs and lifecycle were
rejected as structure for its own sake. Plain heading groups together
with stable global IDs achieve the same at a lower cost.

### Why detection instead of blocks of IDs

A clash is rare on a project of one or two people: a few times a
year. Detecting the clash and settling it with the existing remedy
costs nothing. The alternatives were rejected because they cost the
most code:

- blocks of IDs reserved per author;
- allocation of numbers read over the local branches.

## A worked example

A project has requirements up to `REQ.0120`. Two people each work on
a branch of their own. Each adds a requirement and gives it the next
number, `REQ.0130`.

The first branch is merged, then the second. The project now holds
two items numbered `REQ.0130`. The ledger reports the clash and
changes nothing.

Claude lays the clash out to the principal in a walkthrough. The
item from the first branch is the older and keeps `REQ.0130`. The
item from the second branch is the younger. It takes the next free
number of the merged state, here `REQ.0140`. Its history gets a
`changed` record: the reason names the clash, and `Was` holds
`REQ.0130`. Every place that cited the second item as `REQ.0130` now
cites `REQ.0140`.

## See also

- [ID scheme](../reference/id-scheme.md): the prefix table and the
  numbering rules.
- [Settle a conflict](../use/settle-a-conflict.md): where a number
  taken twice usually shows up, after a merge.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-23 for version 5.34 from the files the
front-matter names; never edited by hand.
