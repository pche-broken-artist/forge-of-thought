---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 1f23f7cc1b04605e
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

A stable ID is the address of one item of a document: a prefix, a dot
and a number, such as `REQ.0010`, given once and kept. This page
explains how the IDs are formed, why an ID is never renumbered and
what happens in the one case where two items carry the same number.
It is for whoever uses the forge, extends it or evaluates it.

## What it is

Every [item](../reference/glossary.md) carries an ID of the form
`PREFIX.NNNN`.

- The prefix has two or three letters. It says what kind of item it
  is.
- The number has four digits as long as it fits.
- The number takes a fifth digit only beyond 9999, as in `REQ.10000`.
- No zero is added to an existing ID.
- Every sorting of IDs is numeric by prefix and number.

An ID is global and stable. It is never renumbered. An item may move
from one group to another without a change of its ID.

The numbers are given like this:

- Items are numbered in tens: `REQ.0010`, `REQ.0020`.
- Each new group starts at the next hundred: `REQ.0100`, `REQ.0110`.
- Where a group has no number left, the next item takes the next free
  number anywhere.

A group is a plain heading. It has no ID, no metadata and no
lifecycle. Groups go two levels deep at most.

The prefixes, each with what it means, are listed on the page
[ID scheme](../reference/id-scheme.md).

## How it works

### One sequence per project

The IDs of a project stay one sequence. A number is taken at the
moment the item is written. No author holds a block of numbers.
Nothing reads over the branches before a number is taken.

### The one exception

Two items may come to carry one number in one project. This is the
only case in which an ID is renumbered. It comes about in several
ways:

- a merge of two branches that each took the same number
- an edit by hand
- documents born apart

However the two items came to one number, they are settled the same
way:

- The older item keeps its number.
- The younger item takes a new number.
- The change is written down in a `changed`
  [record](../reference/glossary.md). The reason of the record names
  the clash. Its field `Was` holds the old number.
- The citations of the younger item are corrected.
- Where the younger item is a [thread](../reference/glossary.md), its
  file is renamed with it.

Which of the two items is the younger is settled as follows:

- The younger item is the one whose `created` record is the later.
- At a merge, the item of the branch merged second takes the next
  free number of the merged state.
- Where the histories do not decide, the principal (the person whose
  thinking is forged) decides.

### Who renumbers

The script that builds the [ledger](../reference/glossary.md) (the
file that states where a project stands) reports the clash and writes
nothing. The renumbering is a write into the
[artefacts](../reference/glossary.md) (the documents of the chain).
Claude does it with the principal, in a
[walkthrough](../reference/glossary.md) (the items are put to the
principal one at a time, and the principal decides each). Claude
never renumbers alone.

Two branches that took the same number are reported after the merge.
That is where a number taken twice usually shows up: see
[Settle a conflict](../use/settle-a-conflict.md).

### A finding in a filed report

A [finding](../reference/glossary.md) (a reviewer's result) stands in
a report, and a filed report is immutable. A finding of a filed
report that clashes is renumbered in the report itself, with the same
`changed` record. This is the one exception to the immutability of a
report. The reason: the ID of a finding lives in the heading of the
report, and the ledger reads it there. A record alone would leave two
numbers standing.

## Why

### Why structure and not prose

Structured items with stable IDs beat prose, even at very high
abstraction. An item with a stable ID can be cited, reviewed, traced
into the layer below and changed one at a time. Prose cannot be
pointed at. Narrative is confined to Purpose & Context and Objective.

### Why a group carries no ID

Workstreams as first-class entities, with their own IDs and
lifecycle, are a rejected direction. They were structure for its own
sake. Plain heading groups together with stable global IDs achieve
the same at lower cost.

### Why two or three letters

Single-letter and hyphenated prefixes, such as `R-001` and `P-01`,
are a rejected direction. The dotted `PREFIX.NNNN` replaced them.

Two letters are allowed beside three. The reason: the prefixes `BR`
and `UC` of the [BRD](../reference/glossary.md) (one of the artefacts
of the chain) had two letters, and `US` of the user stories joined
them.

No universal standard for prefixes exists. The vocabulary of prefixes
is a house convention.

### Why a fifth digit

A prefix has 99 hundreds. Items are numbered in tens, and a new group
starts at each hundred. A prefix may therefore outgrow four digits on
use alone. The widening costs nothing that is kept.

### Why a fact and a position have prefixes of their own

- A fact (prefix `FCT`) is what is the case. The principal states it
  on the principal's own word, or a source states it and is cited to
  its file. Verification is never demanded.
- A position (prefix `POS`) is what the principal holds or wants.

Making a fact of a source the principal's own stance is a new
position. Without a prefix of its own, a fact would have passed for a
position.

### Why a thread carries its origin

A thread (prefix `THR`) carries its origin. The origin is one of
these:

- the principal's word
- a document, named by its path
- Claude's synthesis

The reason: a hypothesis of Claude's stays visibly Claude's until the
principal takes it up. What Claude has worked out is never a fact. A
fact is the word of the principal or of a source. The principal's
word is the default origin and needs no mark.

Why a thread has a prefix of its own: the reason is not recorded.

### Why detection and not blocks of IDs

A clash is rare: a few times a year on a project of one or two
people. Detection with the existing remedy costs nothing. Blocks of
IDs and the allocation of numbers over the local branches are
rejected directions. They would have cost the most code.

## A worked example

Two people work on one project, each on a branch of their own. Each
adds a requirement to the same group of the assignment. The last
number of the group is `REQ.0120`. Each of them takes the next one,
`REQ.0130`.

```
before the merge
  first branch    REQ.0130  the first requirement
  second branch   REQ.0130  the second requirement

after the merge
  REQ.0130  the first requirement
  REQ.0130  the second requirement

after the settlement
  REQ.0130  the first requirement
  REQ.0140  the second requirement
```

- After the merge the ledger script reports that `REQ.0130` stands
  twice. It writes nothing.
- Claude puts the clash to the principal in a walkthrough.
- The second branch was merged second. Its requirement is the
  younger and takes the next free number of the merged state,
  `REQ.0140`.
- A `changed` record is written for the younger requirement. The
  reason names the clash, and `Was` holds `REQ.0130`.
- Every citation of the younger requirement is corrected to
  `REQ.0140`.
- The first requirement keeps `REQ.0130`.

## See also

- [ID scheme](../reference/id-scheme.md): the prefix table and the
  numbering rules.
- [Settle a conflict](../use/settle-a-conflict.md): where a number
  taken twice usually shows up, after a merge.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
