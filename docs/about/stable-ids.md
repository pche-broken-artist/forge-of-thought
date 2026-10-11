---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 7df6010775b5997f
inputs:
  - CLAUDE.md#ID scheme
  - projects/forge/10-intent.md#POS.0200
  - projects/forge/10-intent.md#POS.0220
  - projects/forge/10-intent.md#POS.0230
  - projects/forge/10-intent.md#REJ.0020
  - projects/forge/10-intent.md#REJ.0100
---

# Stable IDs

A stable ID is the address of one item of a document: a three-letter
prefix, a dot and four digits, given once and never changed. This
page says what the scheme is, how an item is numbered and grouped,
and why the forge writes its documents as items with such addresses
rather than as prose. It is for anyone who reads, writes or evaluates
a document of the chain and wants to know why `REQ.0020` means the
same thing on every page, in every review and in every later version.
The prefixes themselves and the numbering rules, exactly as they
stand, are in [ID scheme](../reference/id-scheme.md); the words of
the forge are in the [Glossary](../reference/glossary.md).

## What it is

Every item of a document of the chain carries an ID in the format
`PREFIX.NNNN`. The prefix is three letters and says what kind of item
it is: a requirement, a position, a fact, a thread, a finding, a
decision and so on. The number is four digits. The ID is global:
it points at one item, and at that item only, wherever it is cited.
The ID is stable: it is never renumbered. An item may move from one
group to another without a change of its ID.

Items stand in groups, and a group is a plain heading. A group has no
ID, no metadata and no lifecycle of its own. Groups are at most two
levels deep.

Which prefix belongs to which kind of item and where each kind lives
is a fixed vocabulary of the forge. It is a house convention, aligned
with a BRD standard where that standard has an equivalent. No
universal standard for such prefixes exists; the convention is
derived from the standard the principal's organisation already uses.
The principal is the one whose thinking is being forged, the final
authority on all content.

## How it works

Within a group, items are numbered in tens: `REQ.0010`, `REQ.0020`,
`REQ.0030`. Each new group starts at the next hundred: the second
group of requirements begins at `REQ.0100`, the third at `REQ.0200`.
When a group runs out of numbers between its neighbours, the next
item takes the next free number anywhere in the sequence. The reason
for the tens and the hundreds is not recorded.

Once an item has its ID, the ID is its name for good. When the
document is reworked, items are added, reworded, rejected or moved
between groups; none of that touches an ID. A gap left by a dropped
item stays a gap. A later version of the document cites the same
item by the same address as the earlier one.

The prefix says the kind of item. Three kinds of the intent are worth
telling apart, because they look alike on the page and are not:

- A position (`POS`) is what the principal holds or wants: a stance.
- A fact (`FCT`) is what is the case. The principal states it on his
  word, or a source states it and the fact cites the source's file.
  Verification of a fact is never demanded.
- A thread (`THR`) is an unresolved matter to elicit next. It names
  the artefact it concerns and carries its origin: the principal's
  word, which is the default and needs no mark; a document, named by
  its path; or Claude's own synthesis.

What Claude has worked out is never a fact, since a fact is the
principal's word or a source's. Making a source's fact the
principal's own stance is a new position, not an edit of the fact.

The three-letter dotted form replaced single-letter and hyphenated
prefixes such as `R-001` and `P-01`. It was chosen to align with the
BRD standard. Beyond that alignment, no reason for three letters
rather than another length is recorded.

## Why

The forge prefers structured items with stable IDs over prose, even
at a very high level of abstraction. Narrative is confined to the
sections where it belongs, such as the purpose and context of a
document and its objective. The reason is that an item with a stable
ID can be cited, reviewed, traced into the layer below and changed
one at a time. Prose cannot be pointed at. A reviewer's finding, a
decision, a requirement that realises a position in the layer below:
each of these names the item it concerns by its address, and the
address holds across every version of the document.

The ID is never renumbered because everything that cites it would
otherwise point at the wrong item. The ID is global for the same
reason: a citation must resolve to one item wherever it is read.

Groups are plain headings and not entities of their own. Workstreams
with IDs and a lifecycle of their own were rejected as structure for
its own sake. Plain heading groups together with stable global IDs
achieve the same at lower cost. Because the group carries nothing
but its heading, an item can move between groups freely: nothing
about the item changes except where it stands. The cap of two levels
of depth is a rule of the convention; its reason is not recorded.

A fact, a position and a thread have prefixes of their own because
they would otherwise be confused. Without a prefix of its own, a fact
would have passed for a position: what is the case would have read as
what the principal wants. A thread carries its origin so that a
hypothesis of Claude's stays visibly its own until the principal
takes it up. A matter the principal raised, a matter a document
raised and a matter Claude synthesised are three different things for
the one who decides what to do with them next.

## A worked example

An assignment on a placeholder project `my-idea` opens with two
groups of requirements and one out-of-scope item. The groups are
headings; the items carry the IDs:

```
## Scope of the service

- **REQ.0010** The service shall accept a request in the agreed
  form.
- **REQ.0020** The service shall answer within the agreed time.

## Operation

- **REQ.0100** The service shall be run by the recipients.
- **REQ.0110** The service shall report its state daily.

## Out of scope

- **OOS.0010** The service shall not store the request after the
  answer.
```

A review of the assignment finds that the second requirement is
ambiguous. The finding names it as `REQ.0020`. The principal decides
the requirement is a matter of operation, not of scope, and moves it
under Operation. The item keeps its ID:

```
## Scope of the service

- **REQ.0010** The service shall accept a request in the agreed
  form.

## Operation

- **REQ.0020** The service shall answer within the agreed time, the
  time being the one named in the Terms.
- **REQ.0100** The service shall be run by the recipients.
- **REQ.0110** The service shall report its state daily.
```

The finding still points at the right item. A new requirement of
operation added later takes `REQ.0120`. A thread opened on the same
project because a registered document raised a question would read
`THR.0010` with its origin given as the document's path, such as
`sources/offer-vendor.md`; a thread the principal raised in
conversation would carry no origin mark at all.

## See also

- [ID scheme](../reference/id-scheme.md): the prefix table and the numbering rules, exactly.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
