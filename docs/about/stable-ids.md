---
generated: 2026-10-09
made: derived
inputs-hash: 040054f817549ba5
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About stable IDs

This page explains why every item in the forge carries an ID, what
the ID looks like, why it never changes, and why facts, positions and
threads have prefixes of their own. It is for anyone who uses the
forge, extends it or evaluates it. It was put together from the ID
scheme section of `CLAUDE.md` and from the positions and rejected
directions of the forge's own intent, `projects/forge/10-intent.md`.

## What an ID is

Every item of a chain document carries an ID of the form
`PREFIX.NNNN`: a three-letter prefix, a dot, four digits. The prefix
says what kind of item it is; the number names the item.

The numbering runs in tens, so the first items of a group read
`REQ.0010`, `REQ.0020` and so on, and each new group starts at the
next hundred: `REQ.0100`, `REQ.0110`. The gaps leave room for an item
to be inserted later. When the room runs out, overflow takes the next
free number anywhere; nothing is shifted to make space.

IDs are global and stable: once given, an ID is never renumbered.
An item may move from one group to another and keeps its ID when it
does.

## Groups are headings, nothing more

Items are gathered under groups, and a group is a plain heading: it
has no ID, no metadata and no lifecycle. Depth is capped at two
levels.

This is deliberate. The forge once considered workstreams as
first-class entities with IDs and a lifecycle of their own, and
rejected the idea as structure for its own sake: plain heading groups
plus stable global IDs achieve the same at lower cost. Because the ID
is global and the group is only a heading, regrouping is free; the
citation an ID gives survives any reorganisation of the document.

## Why structure over prose

The forge's rule is structure over prose, even at very high
abstraction: narrative is confined to the Purpose & Context and
Objective sections of an assignment, and everything else is an item
with an ID.

The reason is what an ID makes possible. An item with a stable ID can
be cited, reviewed, traced into the layer below and changed one at a
time. A reviewer can name the exact item a finding concerns; a
decision can record which item it settles; an assignment can say
which position of the intent a requirement carries down; a history
record can say which item a version changed. Prose cannot be pointed
at: a sentence in a paragraph has no name, and a reference to it
breaks as soon as the paragraph is rewritten.

## Why a fact, a position and a thread are told apart

The intent uses three prefixes where one might seem enough, and each
exists because of a distinction that would otherwise be lost.

A position (POS) is what the principal holds or wants: a stance. A
fact (FCT) is what is the case, stated either by the principal on his
own word, or by a source cited to its file; it is not a stance, and
verification of it is never demanded. Without a prefix of its own, a
fact would have passed for a position. The line between them is also
a line of authorship: making a source's fact into the principal's own
stance is a new position, not a relabelling of the fact. And what
Claude has worked out is never a fact, since a fact is the
principal's word or a source's.

A thread (THR) is an unresolved matter to elicit next. It names the
artefact it concerns and carries its origin: the principal's word,
which is the default and needs no mark; a document, cited by path; or
Claude's synthesis. The origin is carried so that a hypothesis of
Claude's stays visibly his until the principal takes it up. This
marking has applied from a fixed date on, with no retrofit of earlier
threads.

A rejected direction (REJ) keeps, with the reason it was dropped, what
the principal has decided against, so that a declined idea is not
re-argued from scratch.

## Where the prefixes come from

The prefix vocabulary is a house convention. No universal standard for
prefixes exists, so the forge derived its own from a BRD standard,
aligning with it wherever an equivalent prefix existed: the
requirement, out-of-scope, constraint, assumption, deliverable,
open-question and success-criterion prefixes of the assignment; the
position, thread, rejected-direction and fact prefixes of the intent;
and the finding, challenge and decision prefixes used internally by
the reviewers and the records.

The shape itself was also a choice. Single-letter and hyphenated
prefixes such as `R-001` or `P-01` were used early and replaced by the
three-letter dotted form, for the same alignment with that standard.

English is the notation throughout: the prefixes are English
abbreviations whatever language a project's artefacts are written in.

## See also

- [ID scheme](../reference/id-scheme.md): the prefix table and the numbering rules, exactly.
