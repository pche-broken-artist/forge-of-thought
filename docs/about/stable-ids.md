---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 0835e3dfeabf1f68
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

A stable ID is the address every item of a document carries, such as
`POS.0310` or `REQ.0120`, and it never changes once given. This page
explains why items carry IDs at all, how the numbers are given, why
they are never renumbered, and what happens in the one case where
two items end up with the same number. It is for anyone who uses the
forge, extends it or weighs it up.

## What it is

An item is one numbered statement in a document: a requirement, a
position the principal holds, a fact, an open thread. The principal
is the person whose thinking is being forged, and the final
authority on all content.

Every item carries an ID in the form `PREFIX.NNNN`:

- `PREFIX`: three letters that say what kind of item it is, such as
  `REQ` for a requirement or `POS` for a position.
- `NNNN`: the number, four digits as long as the number fits.

The full list of prefixes and the numbering rules stand in
[ID scheme](../reference/id-scheme.md). A term of the forge not
explained here is in the [Glossary](../reference/glossary.md).

IDs are global and stable. An ID is never renumbered, with one
exception, described below. An item may move from one group to
another and keep its ID.

## How it works

### How a number is given

- Items are numbered in tens: `REQ.0010`, `REQ.0020`.
- Each new group starts at the next hundred: `REQ.0100`, `REQ.0110`.
- When a group overflows, the item takes the next free number
  anywhere.
- Groups are plain headings. A group has no ID, no metadata and no
  lifecycle. Groups nest at most two levels deep.

IDs are one sequence per project. A number is taken at the moment
the item is written. There are no blocks of numbers reserved for one
author or one branch.

### The fifth digit

An ID keeps four digits as long as the number fits. It takes a fifth
digit only beyond 9999, as in `POS.10000`. No zero is added to an
existing ID: `POS.0310` stays `POS.0310` after `POS.10000` exists.

Every sorting of IDs is numeric, by prefix and then by number.
Sorted as text, `POS.10000` would fall between `POS.1000` and
`POS.1010`. Sorted by number, it comes after `POS.9990`.

### The one exception: two items with one number

Two items in one project can end up with the same number. This can
happen in several ways:

- two branches of the project each took the same number, and were
  then merged;
- someone edited a document by hand;
- two documents were born apart and only later found to share a
  number.

However it happened, the clash is settled the same way:

1. The older item keeps its number.
2. The younger item takes a new number.
3. The change gets a `changed` record in the document's history. Its
   reason names the clash, and its `Was` field holds the old number.
4. Every citation of the younger item is corrected to the new
   number.
5. If the younger item is a thread, its file is renamed with it.

The younger item is the one whose `created` record in the history is
the later. After a merge, the item of the branch merged second takes
the next free number of the merged state. Where the histories do not
decide, the principal's word decides.

The ledger is the project's state report, built by a script from the
documents each time it is read. The ledger script reports the clash
and writes nothing. The renumbering is a write into the documents,
so Claude does it together with the principal. Claude never does it
alone. It is worked through as a walkthrough, that is, one item per
message, each closed by the principal's verdict.

A clash usually shows up after a merge. What to do then is in
[Settle a conflict](../use/settle-a-conflict.md).

## Why

### Why items, not prose

Structured items with stable IDs beat prose, even at a very high
level of abstraction. An item with a stable ID can be cited,
reviewed, traced into the layer below and changed one at a time.
Prose cannot be pointed at.

Workstreams as entities with IDs and a lifecycle of their own were
rejected as structure for its own sake. Plain heading groups plus
stable global IDs achieve the same at lower cost.

### Why the fifth digit

A prefix has 99 hundreds. Items are numbered in tens, and each new
group starts at a new hundred. So a prefix may outgrow four digits
on use alone. Widening to a fifth digit only where needed costs
nothing that already exists.

### Why three-letter dotted prefixes

Single-letter and hyphenated prefixes such as `R-001` or `P-01` were
rejected. They were replaced by the three-letter dotted
`PREFIX.NNNN`, aligned with an existing convention for business
requirement documents. No universal standard for prefixes exists;
the vocabulary is a house convention.

### Why a fact, a position and a thread each have a prefix

- A fact (`FCT`) is what is the case. The principal states it on his
  word, or a source states it and is cited by its file. Its
  verification is never demanded.
- A position (`POS`) is what the principal holds or wants. When the
  principal makes a fact from a source his own stance, that is a new
  position.

Without a prefix of its own, a fact would have passed for a
position.

A thread (`THR`) is an open matter still to be worked out. It
carries its origin: the principal's word, a document by its path, or
Claude's own synthesis. The principal's word is the default and
needs no mark. The origin is kept so that a hypothesis of Claude's
stays visibly Claude's until the principal takes it up. What Claude
has worked out is never a fact, because a fact is the principal's
word or a source's.

### Why detection, not reserved blocks

A clash happens only a few times a year on a project of one or two
people. Detecting it and settling it by the existing rule costs
nothing.

The alternatives were rejected. Blocks of IDs reserved per author,
and allocation of numbers by looking over the local branches, would
have cost the most code of the plan.

## A worked example

A project `my-project` has positions up to `POS.0300`. Two people
work on two branches.

- On the first branch, a new position is written as `POS.0310`.
- On the second branch, a different new position is also written as
  `POS.0310`.

The second branch is merged after the first. The ledger script now
reports that `POS.0310` is taken twice, and changes nothing.

The item of the branch merged second is the younger. Claude lays the
clash out to the principal, and on the principal's word:

- the younger position becomes `POS.0320`, the next free number of
  the merged state;
- its history gets a `changed` record whose reason names the clash,
  with `Was` set to `POS.0310`;
- every citation of that position is corrected to `POS.0320`.

The older `POS.0310` is untouched. Had the clashing items been
threads, the younger thread's file would have been renamed from
`threads/THR.0310.md` to `threads/THR.0320.md` as well.

## See also

- [ID scheme](../reference/id-scheme.md): the prefix table and the
  numbering rules.
- [Settle a conflict](../use/settle-a-conflict.md): where a number
  taken twice usually shows up, after a merge.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
