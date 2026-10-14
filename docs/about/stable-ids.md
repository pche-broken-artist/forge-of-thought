---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: ea11a9b70ab5cb2d
inputs:
  - CLAUDE.md#ID scheme
  - projects/forge/10-intent.md#POS.0200
  - projects/forge/10-intent.md#POS.0220
  - projects/forge/10-intent.md#POS.0230
  - projects/forge/10-intent.md#REJ.0020
  - projects/forge/10-intent.md#REJ.0100
---

# Stable IDs

A stable ID is the address of one item of a document of the forge:
a requirement, a position, a fact, a thread, a finding, a decision.
Every such item carries one, in the shape `PREFIX.NNNN`, and the ID
never changes once given. This page says what the scheme is, how it
numbers items and why the forge writes its documents as items with
IDs rather than as prose. It is for anyone who reads or writes a
document of the forge: the user who works with the principal (the
person whose thinking is forged), the extender who adds to the
engine and the evaluator who judges how it works. The prefix table
and the numbering rules as a plain listing are in the
[ID scheme](../reference/id-scheme.md); every term of the forge in
one line is in the [Glossary](../reference/glossary.md).

## What it is

An ID has the format `PREFIX.NNNN`. The prefix is three letters.
The number has four digits. Each prefix names one kind of item,
such as `REQ` for a requirement of an assignment, `POS` for a
position the principal holds, `FCT` for a fact, `THR` for an open
thread, `FND` for a finding of a reviewer and `DEC` for a decision.
Each kind of item lives in one document: requirements in the
assignment, positions and facts in the intent, threads in the
project's `threads.md`, findings in the ledger (the single source
of truth for the project's state) and in the review reports,
decisions in `decisions.md`.

IDs are global and stable. Global means that an ID is unique across
the project, not only within a group or a document. Stable means
that an item keeps its ID for its whole life. It is never
renumbered, not when items around it are dropped, not when it moves
to another group and not when the document is rewritten.

## How it works

Items are numbered in tens: the first item of a group is `0010`,
the next `0020`, and so on. Each new group starts at the next
hundred: a second group begins at `0100`, a third at `0200`. When a
group runs out of room, a new item takes the next free number
anywhere. The reason for the gaps of ten and of a hundred is not
recorded in the inputs of this page.

Groups are plain headings. They carry no ID, no metadata and no
lifecycle. A document nests groups at most two levels deep. The
reason for the cap at two levels is not recorded.

Because the ID is global and the group is only a heading, an item
may move from one group to another without changing its ID. Whoever
cited the item before the move still finds it after the move.

The vocabulary of prefixes is a house convention. It is aligned
with a company standard for business requirement documents where
that standard has an equivalent. No universal standard for prefixes
exists.

## Why

**Items over prose.** Structured items with stable IDs are
preferred to prose, even at very high abstraction. Narrative is
confined to the two sections where it belongs, Purpose and Context
and Objective. The reason is that an item with a stable ID can be
cited, reviewed, traced into the layer below and changed one at a
time. Prose cannot be pointed at: a reviewer cannot name the
sentence it objects to, a decision cannot say which item it
settles, and an assignment cannot say which position of the intent
each of its requirements carries down.

**Headings over workstreams.** Groups were deliberately left as
plain headings. Workstreams as entities of their own, with their
own IDs and lifecycle, were considered and rejected as structure for
its own sake. Plain heading groups together with stable global IDs
achieve the same at lower cost.

**Three letters, dotted.** Single-letter and hyphenated prefixes
such as `R-001` or `P-01` were replaced by the three-letter dotted
form. The reason given is alignment with the company standard the
prefixes follow.

**A prefix of its own for a fact, a position and a thread.** A fact
(`FCT`) is what is the case. It is stated by the principal on his
word or by a source cited to its file. Verification is never
demanded. A position (`POS`) is what the principal holds or wants.
The two are kept apart by prefix because without a prefix of its
own a fact would have passed for a position. When the principal
makes a source's fact his own stance, that is a new position, not a
change to the fact.

A thread (`THR`) is an unresolved matter to elicit next. It names
the artefact it concerns and carries its origin. The origin is one
of three: the principal's word, which is the default and needs no
mark; a document, cited by path; or Claude's synthesis. The origin
is carried so that a hypothesis of Claude's stays visibly its own
until the principal takes it up. What Claude has worked out is never
written as a fact. Because a fact is the principal's word or a
source's, Claude's own reasoning has no place under `FCT` and lives
as a thread with its origin marked.

## A worked example

An assignment of a placeholder project has two groups of
requirements. The groups are headings; the items carry the IDs.

```
## Onboarding

- **REQ.0010** The recipient shall publish a welcome page for every
  new team member.
- **REQ.0020** The recipient shall record each onboarding in the
  team's register.

## Reporting

- **REQ.0100** The recipient shall report onboarding figures every
  month.
```

The first group starts at `0010` and counts in tens; the second
starts at the next hundred. If the principal later decides that
`REQ.0020` belongs under Reporting, the item moves under that
heading and keeps the number `REQ.0020`. A review that cited
`REQ.0020` still points at the right item. If a new requirement is
needed under Onboarding, it becomes `REQ.0030`; if Onboarding were
ever full, the item would take the next free number anywhere.

In the same project's `threads.md`, a thread that Claude raised from
its own reading of the sources carries the mark of its origin,
Claude's synthesis, beside the matter and the artefact it concerns.
A thread the principal raised himself carries no mark. A thread
raised by a document names that document by its path.

## See also

- [ID scheme](../reference/id-scheme.md): the prefix table and the numbering rules.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
