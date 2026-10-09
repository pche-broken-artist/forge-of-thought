---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - templates/history.md
  - projects/forge/10-intent.md
---

# About versioning and history

This page explains how the forge numbers the versions of its
documents and how it keeps the record of what changed in them, with
the reason behind each rule. It is for anyone who uses the forge,
extends it or weighs whether to adopt it. It was put together from
the section Versioning & status of `CLAUDE.md`, the history skeleton
`templates/history.md` and the positions on versioning, history and
release notes in the forge's own intent
(`projects/forge/10-intent.md`), together with the versioning scheme
that intent records as rejected.

## Integers mean signed off

A version number says whether a document has been approved. Integers
denote signed-off versions:

- `0.1, 0.2, …` are drafts before the first approval;
- `1.0` is approved;
- `1.1, 1.2, …` are changes made after approval, not yet approved
  themselves;
- `2.0` is the next approved version, incorporating all changes since
  1.0.

The status in the front-matter (`draft | approved | superseded`) must
agree with the number: an integer version is `approved`, anything
else is not. A reader can tell from the number alone whether what he
holds has been signed off.

A recipe, the versioned file a render is made from, stays 0.x for its
whole life. Recipes are tools, iterated and never approved, so they
never reach an integer; a recipe carries `updated` in place of `date`
and has no status.

### Why not MAJOR.MINOR

An earlier direction, MAJOR.MINOR with the major number meaning a
change of scope, was dropped. It was replaced by the convention where
integers denote approval, because a change of scope is a reason for
re-approval anyway: the approval is what the number needs to show.

## The body is the state, the companion the record

Every versioned document, every artefact of the chain and every
recipe alike, with no exception, keeps its history in an append-only
companion `<file>.history.md` beside it, never in its body. The body
is the current state; the companion is the record of how it got
there.

The reason is that the way to an item does not belong in the item.
Why it changed, what was said, the trials, the measurements, which
research turned it: all of that goes into the record of the change,
and the item says only what currently holds. The document stays
readable as it is now, and its past stays available without
cluttering it.

The companion is part of its document. It has no row of its own in
the ledger and travels with the document when the document is handed
over by a link into git.

## A log of one record per change

The history is a log. One record is one change and one line; records
are appended at the end of the file and never rewritten, so the order
of the file is the order of the changes. A round of work is one
version and as many records as it made changes; a version may hold
several records, of the same item too.

Each record names:

- the date and the version;
- the author: the one who decided the change, by the handle the
  instance gives its principal, never the one who typed it;
- the subject: an item's ID, several IDs where the whole line holds
  for each, or a place without an ID, such as a section or the file;
- the kind: `created`, `changed`, `closed`, `removed` or `approved`;
- the reason, left out on `created` because the wording is in the
  document;
- `Action`, where there is one: what the user must do after the
  change, written with the change by whoever made it;
- `Was`, where wording leaves an item or a place: word for word the
  part of the wording that ceased to hold, always last.

The author field is there from the first record because a log is
never rewritten, and a field it lacks cannot be added to what was
already written.

The record is written in the same step as the change it records.
Before a write, the reflection shows both the new wording of every
item touched and the record the history will receive, `Was`
included, so what lands in the file is what was confirmed.

## Searched, never loaded whole

A history grows with every change. Before proposing a change to an
item, Claude searches the history and its archive for the item's ID,
and what he finds is raised only where it bears on the change, above
all a direction once tried and dropped. The history is searched,
never loaded whole.

## The single primary

The log is the single primary. The commit messages that `/save` and
`/release` draft and the release notes are derivations of it, and
`last_change` in the front-matter is derived from the records of the
newest version by the write step that appends them, never by hand.

Release notes are derived at each release from the records since the
previous one. One thing is never derived: what the reader must do is
written with the change, in the `Action` field of its record, and the
release notes carry it into their *Action required* word for word.
That is why `Action` is set down at the moment of the change, by the
one who knows what it requires.

## Histories written before the log

Some documents had a history before the log existed, kept as a
Version History table. Such a companion keeps its table untouched: it
moves as it stands to `<file>.history.archive.md`, immutable from
then on, and the log begins with the next version. Nothing is
converted; its rows are a record and stay in the words they were
written in. The history of an item is then a search of both files.

A Version History table, in the body of a document or in its
companion, is reported by `/check` as a finding, settled by that move
on the principal's word, project by project.

## See also

- [Versioning and front-matter](../reference/versioning-and-front-matter.md): the fields and the scheme, exactly.
- [History companion](../reference/history-companion.md): the record's shape.
