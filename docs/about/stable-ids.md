---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About stable IDs

This page explains why every item in a forge document carries an ID,
how those IDs behave and why the prefixes are cut the way they are.
It is for anyone who uses the forge, extends it or weighs whether to
adopt it. It was put together from the ID scheme in `CLAUDE.md` and
from the positions and rejected directions of the forge's own intent
(`projects/forge/10-intent.md`) that give the reasons.

## Items, not prose

The forge holds that structured items with stable IDs beat prose,
even at a very high level of abstraction. A requirement, a position,
a fact or an open question is written as an item of its own with an
ID, not as a sentence buried in a paragraph. Narrative is kept to two
places only: Purpose & Context and Objective. Everything else is an
item.

An ID gives every item a handle that outlives its wording. The
history of a document records each change against the item's ID, and
before a change to an item is proposed, the history and its archive
are searched for that ID. This works only because the ID never
changes.

## How an ID is built

An ID has the form `PREFIX.NNNN`: a prefix of three letters, a dot
and four digits. The prefix says what kind of item it is.

Items are numbered in tens, so a group runs `REQ.0010`, `REQ.0020`
and so on. Each new group starts at the next hundred (`REQ.0100`,
`REQ.0110`). The gaps leave room for an item to be added where it
belongs without renumbering its neighbours. When a range is full, the
next free number anywhere is taken.

## Global and stable

IDs are global and stable: once given, an ID is never renumbered.
An item may move from one group to another and keep its ID. What
the item is called by, wherever it is cited, therefore stays true
however the document is reorganised.

## Groups are only headings

Groups are plain headings. They carry no ID, no metadata and no
lifecycle of their own, and nesting goes at most two levels deep.

Giving groups (workstreams, for example) their own IDs and lifecycle
was considered and rejected as structure for its own sake: plain
heading groups together with stable global IDs achieve the same at
lower cost. Because an item's ID does not depend on its group,
nothing is lost when a group is renamed, split or dissolved.

## Why a fact, a position and a thread each have a prefix

The prefixes separate kinds of content that would otherwise blur
into one another.

- **A fact and a position.** A fact is what is the case, stated by
  the principal on his word or by a source cited to its file;
  verification is never demanded. A position is what the principal
  holds or wants. Without a prefix of its own, a fact would have
  passed for a position. When the principal makes a source's fact
  his own stance, that is a new position, not a relabelled fact.
- **A thread.** A thread is an open matter still to be worked out. It
  has its own prefix so that what is unresolved is never mistaken
  for what is held.

## Why a thread carries its origin

Every thread records where it came from: the principal's word, a
document named by its path, or Claude's own synthesis. The
principal's word is the default and needs no mark.

The reason is to keep authorship visible. A hypothesis Claude has
worked out stays visibly Claude's until the principal takes it up.
For the same reason, what Claude has worked out is never recorded as
a fact, since a fact is the principal's word or a source's. Threads
written before origin was marked were not retrofitted.

## A house convention

No universal standard for ID prefixes exists. The forge's prefix
vocabulary is a house convention, aligned with an existing BRD
standard wherever that standard has an equivalent. The dotted
three-letter form replaced an earlier style of single-letter,
hyphenated prefixes (`R-001`, `P-01`), which was dropped in favour
of `PREFIX.NNNN` for that alignment.

The full list of prefixes, what each means and where each lives is
on the reference page linked below.

## See also

- [ID scheme](../reference/id-scheme.md): the prefix table and the
  numbering rules, exactly.
