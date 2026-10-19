---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 663585abde05284f
inputs:
  - CLAUDE.md#ID scheme
  - projects/forge/10-intent.md#POS.0200
  - projects/forge/10-intent.md#POS.0230
  - projects/forge/10-intent.md#REJ.0020
  - projects/forge/10-intent.md#REJ.0100
---

# Stable IDs

A stable ID is the short address every item of a document carries,
such as `REQ.0010`, and it never changes once given. This page
explains what the address looks like, how numbers are given and why
the forge holds its documents as items with such addresses rather
than as prose. It is for anyone who uses the forge, extends it or
weighs it.

## What it is

An item is one statement of a document with an ID in front of it: a
requirement, a position, a fact, an open question and so on. Every ID
has the form `PREFIX.NNNN`. The prefix is always three letters and
says what kind of item it is. The number has four digits as long as
the number fits. It takes a fifth digit only beyond 9999, as in
`POS.10000`. No zero is added to an ID that already exists. The full
list of prefixes and the rules of numbering stand on
[ID scheme](../reference/id-scheme.md), and every term used here is
in the [Glossary](../reference/glossary.md).

An ID is global and stable. It is never renumbered.

## How it works

Items are numbered in tens: `REQ.0010`, `REQ.0020`. Items are
gathered under headings called groups. Each new group starts at the
next hundred: `REQ.0100`, `REQ.0110`. When a group runs out of
numbers, the item takes the next free number anywhere.

A group is a plain heading. It has no ID, no metadata and no
lifecycle of its own. Groups go at most two levels deep. An item may
move from one group to another, and its ID does not change when it
moves.

Every sorting of IDs is numeric: first by prefix, then by number. A
five-digit number therefore sorts after a four-digit one.

The reason for numbering in tens and starting groups at the hundred
is not recorded. The reason for the numeric sorting is not recorded
either.

## Why

### Items over prose

The forge writes its documents as structured items with stable IDs,
even where the thinking is still very abstract. Narrative is kept to
two places: the sections Purpose & Context and Objective.

The reason is that an item with a stable ID can be pointed at. It
can be:

- cited: another document or a record names it by its ID;
- reviewed: a reviewer's result names the item it is about;
- traced: an item in the layer below says which item above it
  carries forward;
- changed one at a time: one item is rewritten while the others
  stand.

Prose cannot be pointed at in this way.

### Groups are only headings

Groups could have been things of their own, with their own IDs and
lifecycle. That was rejected as structure for its own sake. Plain
heading groups together with stable global IDs achieve the same at
lower cost.

### Three letters and a dot

Single-letter and hyphenated prefixes, such as `R-001` or `P-01`,
were rejected. They were replaced by the three-letter dotted form
`PREFIX.NNNN`. The prefixes are aligned with an existing convention
for requirements documents where an equivalent exists. No universal
standard for prefixes exists, so the vocabulary is a house
convention derived from that one. No further reason against the old
form is recorded.

### A fact, a position and a thread each have their own prefix

The principal is the person whose thinking is being forged and who
decides everything in it. The intent (the document of what the
principal wants now) holds three kinds of item that look alike in
prose but are not alike:

- a fact (`FCT`): what is the case, stated by the principal on his
  word or by a source cited to its file;
- a position (`POS`): what the principal holds or wants;
- a thread (`THR`): an open matter still to be drawn out of the
  principal.

A fact needs a prefix of its own. Without one, a fact would pass for
a position. Taking a source's fact as the principal's own stance is
a new position. Verification of a fact is never demanded.

A thread carries its origin. The origin is one of three:

- the principal's word, which is the default and needs no mark;
- a document, named by its path;
- Claude's synthesis.

The origin is carried so that a hypothesis of Claude's stays visibly
Claude's until the principal takes it up. What Claude has worked out
is never a fact, because a fact is the principal's word or a
source's.

## A worked example

A generic intent opens with two groups:

```
## Scope
- **POS.0010** ...
- **POS.0020** ...
- **POS.0030** ...

## Delivery
- **POS.0100** ...
- **POS.0110** ...
```

A new position about scope is added. It takes `POS.0040`, the next
step of ten in its group.

`POS.0020` turns out to belong under Delivery. It moves there and is
still `POS.0020`. Whatever cited `POS.0020` still points at the same
item.

A third group, Risks, is opened. Its first item takes `POS.0200`,
the next hundred.

Much later the numbers pass 9999. The next position is `POS.10000`.
Sorted numerically, `POS.9990` comes before `POS.10000`. The older
IDs keep their four digits and gain no zero.

## See also

- [ID scheme](../reference/id-scheme.md): the prefix table and the
  numbering rules.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
