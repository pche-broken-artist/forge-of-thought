---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: ba0a10a7d2f3e0ff
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
form `PREFIX.NNNN`, and it is never renumbered. This page explains
why items carry such IDs, how the numbers are given and the one case
in which a number does change: two items that share one number. It is
for anyone who uses the forge, extends it or weighs it up.

## What it is

Every item of a document carries an ID of the form `PREFIX.NNNN`.
The prefix is three letters and says what kind of item it is. A
requirement is `REQ`, a position of the principal (the person whose
thinking is being forged) is `POS`, a fact is `FCT` and a thread is
`THR`. The full list of prefixes and where each lives is on
[ID scheme](../reference/id-scheme.md).

The number has four digits as long as the number fits. It takes a
fifth digit only beyond 9999, as in `POS.10000`. No zero is added to
an existing ID. Every sorting of IDs is numeric, by prefix and then
by number.

An ID is global within its project and stable. It is never
renumbered, with one exception, described below.

## How it works

### Giving a number

Items are numbered in tens: `REQ.0010`, `REQ.0020`. Each new group
starts at the next hundred: `REQ.0100`, `REQ.0110`. When the room is
used up, an item takes the next free number anywhere.

Groups are plain headings. A group has no ID, no metadata and no
lifecycle. Items may move between groups freely, and their IDs do
not change when they move. Groups go at most two levels deep.

IDs are one sequence per project. A number is taken at the moment
the item is written. There are no blocks of numbers set aside per
author or per branch.

### Two items with one number

The one exception to "never renumbered" is two items with one number
in one project. It does not matter how they came to share it:

- a merge of two branches, each of which took the same next number;
- an edit by hand;
- documents of one project born apart, each starting its own count.

Every such clash is settled the same way:

- The older item keeps its number. The older is the one whose
  `created` record in the history is the earlier.
- The younger item takes a new number. At a merge, the item of the
  branch merged second takes the next free number of the merged
  state. Where the histories do not decide which is younger, the
  principal decides.
- The renumbering is written in the history as a `changed` record.
  Its reason names the clash, and its `Was` gives the old number.
- Every citation of the younger item is corrected to the new number.
- If the item is a thread (one open matter of the intent, kept in a
  file of its own), its file is renamed with it.

The ledger script finds the clash. The ledger is the state report
of a project, made from its documents each time it is read. The
script reports the clash and writes nothing, because the renumbering
is a write into the artefacts. Claude does the renumbering with the
principal, in a walkthrough (one item put to the principal at a
time, each with a verdict). Claude never renumbers alone.

After a merge, a number taken twice usually shows up beside other
conflicts of the merge; what you do then is on
[Settle a conflict](../use/settle-a-conflict.md).

## Why

### Why items and not prose

An item with a stable ID can be cited, reviewed, traced into the
layer below and changed one at a time. Prose cannot be pointed at.
This is why structured items stand even at a very high level of
abstraction, and narrative is kept to the few sections meant for it.

Plain heading groups together with stable global IDs do the work
that groups with IDs of their own would do. Groups with their own
IDs and lifecycle were rejected as structure for its own sake.

### Why three-letter dotted prefixes

The form `PREFIX.NNNN` with a three-letter prefix replaced earlier
single-letter and hyphenated prefixes such as `R-001` and `P-01`. It
follows an existing requirements standard where an equivalent
prefix exists. No universal standard for prefixes exists, so the
vocabulary is a house convention.

### Why a fact, a position and a thread have prefixes of their own

A fact (`FCT`) is what is the case. It is stated by the principal on
his word, or by a source cited to its file. A position (`POS`) is
what the principal holds or wants. Without a prefix of its own, a
fact would pass for a position. Taking a source's fact as his own
stance is therefore a new position.

A thread (`THR`) carries its origin: the principal's word, a
document by its path, or Claude's own synthesis. The reason is that
a hypothesis of Claude's stays visibly Claude's until the principal
takes it up. What Claude has worked out is never a fact, since a
fact is the principal's word or a source's.

### Why a fifth digit

A prefix has 99 hundreds. Items are numbered in tens and each new
group starts a new hundred, so a prefix may outgrow four digits on
use alone. Widening to a fifth digit costs nothing that is kept.

### Why detection and not blocks of numbers

A clash happens only a few times a year on a project of one or two
people. Detecting it with the ledger script and settling it with the
existing remedy costs nothing. The alternatives were rejected: blocks
of IDs set aside per author and an allocation of numbers read over
the local branches. They would have cost the most code of the plan.

## A worked example

Two people work on one project, each on a branch. The last
requirement on `main` is `REQ.0220`.

1. On the first branch, a requirement is written as `REQ.0230`. Its
   `created` record is dated earlier.
2. On the second branch, a different requirement is also written as
   `REQ.0230`.
3. The first branch is merged, then the second. The project now has
   two items numbered `REQ.0230`.
4. The ledger script reports the clash and changes nothing.
5. Claude puts the clash to the principal in a walkthrough. The item
   of the branch merged second is the younger. It takes the next
   free number of the merged state, say `REQ.0240`.
6. The history gets a `changed` record for `REQ.0240`. Its reason
   names the clash with `REQ.0230`, and its `Was` reads `REQ.0230`.
7. Every place that cited the second requirement now cites
   `REQ.0240`. The first requirement keeps `REQ.0230` untouched.

## See also

- [ID scheme](../reference/id-scheme.md): the prefix table and the
  numbering rules.
- [Settle a conflict](../use/settle-a-conflict.md): where a number
  taken twice usually shows up, after a merge.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
