---
generated: 2026-10-09
made: derived
inputs-hash: 53cb7dde4c467c9c
inputs:
  - CLAUDE.md
  - templates/history.md
  - projects/forge/10-intent.md
---

# About versioning and history

This page explains how a versioned document of the forge carries its
version number and its status, and where the record of its changes
lives. It is for the user who composes documents and sees the numbers
move, for the extender who adds a kind of document and must give it
the same behaviour, and for the evaluator who wants to know why the
scheme is as it is. It was put together from `CLAUDE.md`, from
`templates/history.md` and from the forge's own intent
(`projects/forge/10-intent.md`): the rules come from the first two,
the reasons from the third.

## What is versioned

Two kinds of document carry a version: the artefacts of the chain (a
brief, an intent, an assignment, every later layer) and the recipes a
render is made from. Everything else is either a record, which is
appended to or immutable, or state, which is freely rewritten and has
no version at all. The rules below hold for every versioned document
alike, with no exception.

## The number scheme

Integers denote signed-off versions. The scheme runs:

- `0.1, 0.2, …` drafts before the first approval
- `1.0` the document approved
- `1.1, 1.2, …` changes made after approval, not yet approved themselves
- `2.0` the next approved version, which incorporates every change
  since `1.0`

A document is rewritten freely between approvals: a draft at `0.4` and
a changed document at `1.3` are both working states. What the
recipients of an assignment hold is a version reached by a link into
git, not a file that is frozen in any way the file itself would show.

Why this scheme and not another: an earlier design had
`MAJOR.MINOR` with the major meaning a change of scope. It was dropped
for the convention where the integer means approval, because a scope
change is a reason for re-approval anyway, so the approval reading
covers it. The scheme is also the one already in use around the forge
for comparable documents, so a reader meets no second convention.

## Status agrees with the number

The front-matter of a versioned document carries `version`, `date`,
`status` and `last_change`. The status is one of `draft`, `approved`
or `superseded`, and it must agree with the number: an integer version
is `approved`, anything else is not. The two fields are never set
independently of each other.

`last_change` is not written by hand. The step that appends the
records of a write derives it from the records of the newest version,
so it always says what the history says.

## A recipe stays 0.x

A recipe is a tool, not a record of thinking: it is iterated and never
approved. So it carries `updated` in place of `date`, carries no
status, and stays at `0.x` for life. It still keeps a history
companion like every other versioned document; what it lacks is the
approval step, not the record.

## The history lives beside the document, never in it

Every versioned document keeps its history in an append-only
companion `<file>.history.md` beside it, never in its body: the body
is the current state, the companion is the record. The companion is
part of its document: it has no row of its own in the ledger and is
handed over with the document by the link into git.

The companion is a log. One record is one change and one line,
appended at the end of the file and never rewritten, so the order of
the file is the order of the changes. A working round is one version
and as many records as it made changes; a version may hold several
records, of the same item too. The shape of a record is
`templates/history.md`'s:

```
- <date> | <version> | <author> | <subject> | <kind> | <reason> | Action: <what the user must do> | Was: <wording that ceased to hold>
```

The subject is an item's ID, several IDs where the whole line holds
for each, or a place without an ID: the heading of a section, or the
file name where the change is of the document as a whole. The kinds
are `created`, `changed`, `closed` (a thread or an open question
settled), `removed` (an item leaves the document and its ID is never
used again) and `approved` (of the document as a whole). A record of
creation needs no reason: the wording is in the document. At the
birth of a document the log opens with one record of the file and one
naming every item born with it. `Action` and `Was` stand only where
the record has them, `Was` always last. Lines are not wrapped.

`Was` is, word for word, the part of the wording that ceased to hold.
It is written wherever wording leaves an item or a place; a record of
a change to the document as a whole carries none.

`Action` is what the user must do after the change, written with the
change by whoever made it. It is the one thing never derived later:
the release notes carry it word for word into their *Action required*.

The record is written in the same step as the change it records, and
the reflection before a write shows both: the new wording of every
item touched and the record the history will receive, `Was` included.
So a write confirms what the reader has already seen rather than
surprising him.

## Why the way to an item does not belong in the item

The reason for keeping the record out of the body is that an item
says what is wanted now, and the way to it is something else. Why it
changed, what was said, trials, measurements, which research turned
it: all of that goes into the item's record, never into the item.
The item stays readable as the current position; the record keeps
the path.

The path is not lost by being kept apart. Before Claude proposes a
change to an item, he searches the history and its archive for the
item's ID, and says in the proposal what bears on the change, a
direction once tried and dropped above all. The history is searched,
never loaded whole: a log that only grows would otherwise become a
cost at every write.

## The log is the single primary

The commit messages `/save` and `/release` draft, and the release
notes, are derivations of the log, never written independently of it.
Release notes are a log of releases, not a story: their sections are
derived at the release from the records since the previous release,
one sentence per change from the user's side, and at a major the
minors since the previous major are folded into it, which is the
scheme's own reading of "the next approved version, incorporating all
changes since". A reader wants to see plainly what was added, changed
and removed, and a derivation from one primary gives him that without
a second account to keep in step.

## The author of a record

Every record names its author: the one who decided the change, by the
handle the instance gives its principal, never the one who typed it.
The field is there from the first record, because a log is never
rewritten and a field it lacks cannot be added later to what was
already written.

## A history written before the log

A companion written before the log was introduced held a table rather
than a log. Such a table is kept as it stands: it moves, untouched, to
`<file>.history.archive.md`, immutable from then on, and the log
begins with the next version. Nothing is converted; its rows are a
record and stay in the words they were written in. The history of an
item is from then on a search of both files.

A Version History table still standing in the body of a document or
in its companion is a finding of `/check`, settled by that move on the
principal's word, project by project.

## What is never versioned because it is never edited

Reviews, challenges, sources and research carry no version because
they are immutable: a source from its registration, the others from
their creation. Corrections happen downstream, in the documents that
cite them.

## See also

- [Versioning and front-matter](../reference/versioning-and-front-matter.md): the fields and the scheme, exactly.
- [History companion](../reference/history-companion.md): the record's shape.
