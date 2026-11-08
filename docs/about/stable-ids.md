---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 43687cb89ab7eaac
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

A stable ID is the address of one item of a document: a prefix, a
dot and a number, given once and never changed. This page explains
why every item of the forge carries one, how the numbers are given,
and what happens in the one case where two items end up with the same
number. It is for anyone who reads, extends or evaluates the forge
and wants to know why a requirement, a position or a thread is cited
by a code rather than by its words. The prefixes themselves and the
numbering rules in full are listed on the page
[ID scheme](../reference/id-scheme.md); the terms of the forge are in
the [Glossary](../reference/glossary.md).

## What it is

Every item of a document has the form `PREFIX.NNNN`. The prefix is
two or three letters and says what kind of item it is: a requirement,
a position, a thread, a finding. The number has four digits as long
as the number fits. It takes a fifth digit only beyond 9999, as in
`REQ.10000`. No zero is ever added to an existing ID. Every sorting of
IDs is numeric, by prefix and then by number.

An ID is global within its project and stable: once given, it is
never renumbered. An item may move from one group of a document to
another and keeps its ID. The one exception is the clash of two items
with one number, described below.

The document around the items is kept plain. Groups are headings
without IDs, metadata or lifecycle. Groups go at most two levels deep.
Narrative is confined to the Purpose & Context and Objective sections
of an artefact; everything else is an item with an ID.

## How it works

### Giving a number

Items are numbered in tens: `REQ.0010`, `REQ.0020`, `REQ.0030`. Each
new group starts at the next hundred: `REQ.0100`, `REQ.0110`. When a
group has used up its tens, the next item takes the next free number
anywhere in the prefix.

A project has one sequence per prefix. The number is taken at the
moment the item is written. There are no blocks of numbers reserved
per author or per branch, and nothing reads across branches to find a
free number.

### When two items share one number

Two items of one project can end up with the same number. The forge
does not ask how it happened. It may be a merge of two branches that
each took the next number. It may be an edit by hand. It may be two
windows open on the same project, or documents born apart from one
another. Every case is settled the same way.

The older item keeps its number. The younger item takes a new one.
The younger is the item whose `created` record in the history is the
later. At a merge the item of the branch merged second is the
younger, and it takes the next free number of the merged state. Where
the histories do not decide, the principal (the person whose thinking
is being forged) decides.

The renumbering is written down. The younger item gets a `changed`
record in the history whose reason names the clash and whose `Was`
holds the old number. Every citation of the old number is corrected
to the new one. A thread is a file of its own, named after its ID, so
a renumbered thread's file is renamed with it.

A finding of a filed report is treated the same way with one twist.
Reports are otherwise never edited. A finding that clashes is
renumbered in the report itself, with the same `changed` record. This
is the one exception to a report's immutability. The reason: the ID
of a finding lives in the heading of the report, and the ledger (the
single source of truth for the project's state, made by a script at
read time) reads it there. A record alone would leave two numbers
standing.

The ledger script detects the clash. After a merge it reports that a
number was taken twice and writes nothing. The renumbering is a write
into the artefacts, so it is Claude's work with the principal, done
in a walkthrough (the method where a list is worked one item per
message, each item closed with the principal's verdict), and never
Claude's alone. Where a clash usually shows up, after a merge, is
described on [Settle a conflict](../use/settle-a-conflict.md).

## Why

**Structure over prose.** An item with a stable ID can be cited,
reviewed, traced into the layer below and changed one at a time.
Prose cannot be pointed at. This holds even at very high abstraction,
so the forge structures its documents into items long before anything
is concrete.

**Plain groups.** Groups with IDs and a lifecycle of their own, such
as workstreams as first-class entities, were considered and rejected
as structure for its own sake. Plain heading groups together with
stable global IDs achieve the same at lower cost.

**Numbered in tens, a new group at the next hundred.** The reason for
this spacing is not recorded.

**A fifth digit beyond 9999.** A prefix has 99 hundreds. Numbered in
tens with a new group at each hundred, a prefix may outgrow four
digits on use alone. Widening the number only where it is needed
costs nothing, which is why no zero is added to the IDs that already
exist.

**Two letters as well as three.** The prefixes were first fixed at
three letters. The BRD, a business requirements document, already
used two-letter prefixes for its business requirements and use cases,
and the user story joined them. So two letters are allowed beside
three.

**A dotted prefix of letters, not a hyphenated single letter.**
Single-letter and hyphenated prefixes such as `R-001` or `P-01` were
replaced by the dotted `PREFIX.NNNN`, aligned with a standard for
business requirements documents the house already used. No universal
standard for prefixes exists; the vocabulary is a house convention
derived from that one.

**A prefix of its own for a fact, a position and a thread.** A
position is what the principal holds or wants. A fact is what is the
case, stated by the principal on his word or by a source cited to its
file. Without a prefix of its own, a fact would have passed for a
position. Making a source's fact the principal's own stance is a new
position, not a changed fact. A thread carries its origin: the
principal's word, a document by path, or Claude's synthesis. So a
hypothesis of Claude's stays visibly Claude's until the principal
takes it up. What Claude has worked out is never recorded as a fact,
because a fact is the principal's word or a source's.

**Detection and the existing remedy, not reserved blocks.** A clash
of numbers happens a few times a year on a project of one or two
people. Detecting it and settling it with the remedy that already
exists, a renumbering with a record, costs nothing. Blocks of IDs per
author and the allocation of numbers across the local branches were
considered and rejected: they would have cost the most code of any
part of the plan for little gain.

## A worked example

Two people work on one assignment of a project, each on a branch of
their own. Both add a requirement to the same group, and both take the
next free number, `REQ.0130`. Each branch has one `created` record for
its `REQ.0130` in the assignment's history.

The branches are merged. The ledger script, run after the merge,
reports that `REQ.0130` is taken twice and changes nothing.

Claude lays the two items before the principal in a walkthrough. The
item of the branch merged first is the older; it keeps `REQ.0130`. The
item of the branch merged second is the younger; it takes the next
free number of the merged state, `REQ.0140`. The assignment's history
gets one `changed` record for `REQ.0140` whose reason names the clash
and whose `Was` reads `REQ.0130`. The one place in the solution design
that cited the younger item is corrected to `REQ.0140`. From then on
both numbers are stable again, and neither is ever renumbered.

## See also

- [ID scheme](../reference/id-scheme.md): the prefix table and the
  numbering rules.
- [Settle a conflict](../use/settle-a-conflict.md): where a number
  taken twice usually shows up, after a merge.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
