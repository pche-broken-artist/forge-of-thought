---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 86ff9bd19d4de5b0
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

A stable ID is the address of one item of a document of the forge: a
prefix and a number, given once and never changed. This page
explains why every item carries one, how the numbers are given, and
what happens in the one case where two items end up with the same
number. It is for anyone who writes, reads or evaluates the
documents of a project: the principal (the person whose thinking is
forged), an extender of the forge and an evaluator of its results.
The full list of prefixes and the numbering rules in short stand on
the [ID scheme](../reference/id-scheme.md) page.

## What it is

Every item of a versioned document carries an ID of the form
`PREFIX.NNNN`. The prefix is two or three letters and says what kind
of item it is. The number is four digits as long as the number fits.
A fifth digit is taken only beyond 9999, as in `POS.10000`. No zero
is ever added to an existing ID when the fifth digit arrives. Every
sorting of IDs is numeric, by prefix and then by number.

An ID is global and stable: it names one item across the whole
project and is never renumbered. There is one exception, two items
with one number, and it is described below.

Items are gathered in groups. A group is a plain heading: it has no
ID, no metadata and no lifecycle. Depth is capped at two levels. An
item may move from one group to another without changing its ID.

## How it works

### Numbering

Items are numbered in tens: `REQ.0010`, `REQ.0020`, and so on. Each
new group starts at the next hundred: `REQ.0100`, `REQ.0110`. When a
group runs out of room, the overflow takes the next free number
anywhere in the sequence.

A project has one sequence per prefix, and the number is taken at the
moment the item is written. There is no block of numbers reserved per
author and no reading across branches before a number is taken. The
reason is given under Why.

### The one exception: two items with one number

Two items of one project may come to carry the same number. The usual
ways are these:

- a merge of two branches, each of which took the next free number
- an edit by hand
- two windows writing at the same time
- documents born apart and later joined into one project

However the clash came about, it is settled in one way. The older
item keeps its number. The younger item takes a new one. The younger
is the item whose `created` record in the history is the later. At a
merge, the item of the branch merged second takes the next free
number of the merged state. Where the histories do not decide, the
principal's word decides.

The renumbering is written as a change of the younger item. Its
history gets a `changed` record whose reason names the clash and
whose `Was` field holds the old number. Every citation of the old
number is corrected. Where the item is a thread (one open matter of
the intent, kept as a file of its own), the file is renamed with the
new number.

The ledger (the single source of truth for state, built from the
documents at read time) does not fix a clash. The script that builds
the ledger reports the clash and writes nothing. The renumbering is a
write into the artefacts, and it is Claude's with the principal,
worked in a walkthrough (one item per message, closed by the
principal's verdict), never Claude's alone. After a merge, the clash
is one of the things settled on the
[Settle a conflict](../use/settle-a-conflict.md) page.

A finding of a filed report may clash too. A report is otherwise
immutable. A clashing finding is nevertheless renumbered in the
report itself, with the same `changed` record. This is the one
exception to a report's immutability. The reason is that the ID lives
in the report's heading and the ledger reads it there. A record alone
would leave two numbers standing.

## Why

### Why structure over prose

Structured items with stable IDs beat prose, even at very high
abstraction. Narrative is confined to the few sections that carry it,
such as a purpose or an objective. An item with a stable ID can be
cited, reviewed, traced into the layer below and changed one at a
time. Prose cannot be pointed at.

Workstreams as first-class entities with IDs and a lifecycle of their
own were considered and rejected as structure for its own sake. Plain
heading groups with stable global IDs achieve the same at lower cost.

### Why a dotted prefix of two or three letters

Single-letter and hyphenated prefixes, such as `R-001` or `P-01`,
were rejected. They were replaced by the dotted `PREFIX.NNNN`,
aligned with an existing BRD standard where an equivalent prefix
exists. No universal standard for prefixes exists; the vocabulary is
a house convention derived from that standard.

Two letters are allowed beside three because some prefixes of the BRD
had two letters already, and the user story prefix joined them. The
only limit was the scripts, which matched three letters alone. They
were widened, and the ledgers of existing projects were unchanged by
it.

### Why a fifth digit

A prefix has 99 hundreds. Numbered in tens, with a new group at each
hundred, a prefix may outgrow four digits on use alone. Widening the
number when that happens costs nothing that is kept, so the rule
allows a fifth digit rather than renumbering.

### Why a fact, a position and a thread have prefixes of their own

A fact is what is the case. It is stated by the principal on his
word, or by a source and cited to its file. Verification is never
demanded. A position is what the principal holds or wants. Making a
source's fact his own stance is a new position. Without a prefix of
its own, a fact would have passed for a position.

A thread carries its origin: the principal's word, a document by its
path, or Claude's synthesis. This is so that a hypothesis of Claude's
stays visibly his until the principal takes it up. What Claude has
worked out is never recorded as a fact, because a fact is the
principal's word or a source's.

### Why detection rather than reserved numbers

Blocks of IDs per author, allocation of numbers over the local
branches and a version taken as a landing were considered and
rejected. A clash is a few times a year on a project of one or two
people. Detecting it after the fact, with the remedy already in
place, costs nothing. The rejected directions would have cost the
most code of the plan.

## A worked example

Two people work on one thought project, each on a branch of their
own. The assignment's second group ends at `REQ.0120`. Each adds a
requirement and, as the rule says, takes the next free number at the
write: both items become `REQ.0130`.

The branches are merged. The script that builds the ledger is run on
the project and reports that `REQ.0130` stands twice. It writes
nothing.

Claude lays the clash before the principal in a walkthrough. The
item whose `created` record is the earlier is the older and keeps
`REQ.0130`. The other item came in on the branch merged second, so it
takes the next free number of the merged state, `REQ.0140`. Its
history receives a `changed` record: the reason names the clash with
`REQ.0130`, and `Was` holds `REQ.0130`. The one place in the solution
design that cited the younger item is corrected to `REQ.0140`. Had
the younger item been a thread, its file would have been renamed to
the new number as well. The ledger, rebuilt, shows one `REQ.0130`
and one `REQ.0140`.

## See also

- [ID scheme](../reference/id-scheme.md): the prefix table and the
  numbering rules.
- [Settle a conflict](../use/settle-a-conflict.md): where a number
  taken twice usually shows up, after a merge.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
