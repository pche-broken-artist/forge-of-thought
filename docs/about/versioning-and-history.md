---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: a46779dbc9ee1f25
inputs:
  - CLAUDE.md#Versioning & status
  - templates/history.md
  - projects/forge/10-intent.md#POS.0300
  - projects/forge/10-intent.md#POS.0310
  - projects/forge/10-intent.md#POS.1570
  - projects/forge/10-intent.md#POS.1630
  - projects/forge/10-intent.md#POS.0730
  - projects/forge/10-intent.md#POS.1510
  - projects/forge/10-intent.md#REJ.0110
---

# Versioning and history

A version number in the forge says whether a document has been
signed off, and the history of the document lives in a separate log
beside it. This page explains what the numbers mean, what a major
version of an intent is, why a header carries so little, and how the
history companion works. It is for anyone who uses the forge, extends
it or wants to judge it. The exact fields and the record's shape are
on the reference pages linked at the end; every term of the forge is
in one line in the [Glossary](../reference/glossary.md).

## What it is

Every versioned document has a version number.
The versioned documents are these:

- every artefact (a document of the chain, such as the brief, the
  intent or the assignment)
- every recipe (the versioned file a render is made from)
- every work specification (the way and the why of a work product)

An integer denotes a signed-off version:

- `0.1, 0.2, …`: drafts before the first approval
- `1.0`: approved
- `1.1, 1.2, …`: changes made after approval, not yet approved
  themselves
- `2.0`: the next approved version, incorporating all changes since
  `1.0`

The header of a document carries a `status` (`draft`, `approved` or
`superseded`).
The status must agree with the number.
An integer version is `approved`, and anything else is not.
A recipe carries no status and stays at 0.x for life.
The reason a recipe stays at 0.x is not recorded.

Every versioned document keeps its history in a companion file
beside it, named `<file>.history.md`.
The body of the document is the current state.
The companion is the record of how it got there.

## How it works

### The header

A header carries nothing that changes with a round of work (a round
is one working conversation, written once at its end as one
version).
It holds `version` and `status`.
Beside them it holds only what does not change with the work: the
`project`, a brief's `title` and `author`, an index's `directory`.
The date of a document and its last change are not in the header.
They are computed from the history by whatever reads them, such as
`/history` and the ledger (the file that holds the state of a
project).

### A major version of an intent

A major version (`1.0`, `2.0` and so on) of an intent closes a set of
features that the principal names.
The principal is the person whose thinking is forged, with the final
word on all content.
His word closes the major.
Before its tag, a major passes a fuller test than a minor: the
checks, the critics and a challenge, with their findings settled or
deferred by his word.
The test says what the word attests.

A major approves the intent as the record of what the principal holds
at that moment.
The package it names is finished and goes out.
What is still open stays open in its thread.
A position marked for a later pass stays marked.
The approval says what is done, not that nothing is left.

The test of a major attests two things:

- the documents conform to the conventions and to each other
- the thinking has been challenged

It attests nothing of how the model behaves on the documents.
That behaviour is verified by the author's own use until the forge
has a test of it.
Where the tag of a major is proposed is described in
[Release a version](../use/release-a-version.md).

### The history companion

The history is a log.
One record is one change and one line.
Records are appended at the end of the file and never rewritten.
So the order of the file is the order of the changes.
A round is one version, and it holds as many records as it made
changes, several of one item included.

A record has these fields, in this order:

- date
- version
- author: the one who decided the change, by the handle the instance
  gives its principal, never the one who typed it
- subject: an ID, several IDs where the line holds for each, or a
  place without an ID (a section or the file)
- kind: `created`, `changed`, `closed`, `removed` or `approved`
- reason: left out on `created`, because the wording is in the
  document
- `Action:`: what the user must do after the change, only where
  there is something
- `Was:`: word for word the wording that ceased to hold, always
  last, only where wording left an item or a place

The record is written in the same step as the change.
Before a write, Claude shows the new wording and the records it will
append, `Was` included.
The way to an item goes into its record, never into the item.
That way covers why it changed, what was said, trials, measurements
and which research turned it.
At the birth of a document there is one record of the file and one
naming every item born with it.

### Records of state

Some records change no content and only say a state:

- the mining of a brief (how far its content has been taken into the
  intent)
- a finding or a challenge settled
- a thread closed
- the state of a work product (current, stale or by hand)

A record of state only carries the current version and does not
raise it.
A state record still marks a render stale, as every raise does.

### Reading the history

Claude reads the history of an item through `/history <ID>` before it
proposes a change to that item.
A script gathers what the project holds of the item: its wording
today, its records, the records of other items that mention it, the
rows of the archive and every other place that cites it.
The history is searched by that script, never loaded whole.
How to run it is in
[Read the history of an item](../use/read-the-history-of-an-item.md).

### The archive

A companion written before the log keeps its table untouched.
It moves as it stands to `<file>.history.archive.md` and is immutable
from then on.
The log begins with the next version.
The history of an item is then a search of both files.
A Version History table in the body of a document or in its
companion is a `/check` finding.
That finding is settled by the move to the archive, on the
principal's word, project by project.

The companion is part of its document.
It has no row of its own in the ledger and is handed over with the
document.

## Why

Integers denote approval because the scheme is aligned with a
business requirements document (BRD) standard.
A scheme where the major number means a change of scope was
rejected.
A change of scope is a reason for a new approval anyway.

The header carries nothing that changes with a round because a field
written at every operation is a certain conflict between any two
rounds on the same artefact, whatever the rounds were about.

A state record does not raise the version so that a round that only
closes findings after a check, and changes no content, is not a
version.

The history lives beside the document and not in it because the
body is the current state and the companion is the record.
The reason the way to an item is kept out of the item itself is not
recorded beyond that.

The author field is there from the first record because a log is
never rewritten.
A field the log lacks cannot be added to what was already written.

The log is the single primary.
The commit messages that `/save` and `/release` draft are derived
from it, and so are the release notes.
The release notes are derived at the release from the records since
the previous release.
One thing in them is never derived: what the reader must do is
written with the change, in `Action`, and carried into the release
notes' *Action required* word for word.
The reason is that a reader wants to see plainly what was added,
changed and removed.

The history of an item is read by one command because that history
is scattered over the log, the archive and the records of other
items.
Without the command the search was done by hand, and differently
every time.
What is deterministic belongs to a script, and the judgement is what
remains for the model.
The reason reading a whole log is forbidden is not recorded.

The old history stays in an archive, unconverted, because its rows
are a record and stay in the words they were written in.

## A worked example

A generic history companion of one assignment, after a few rounds:

```
- YYYY-MM-DD | 0.1 | <author> | 20-assignment.md | created
- YYYY-MM-DD | 0.1 | <author> | REQ.0010, REQ.0020, OOS.0010 | created
- YYYY-MM-DD | 0.2 | <author> | REQ.0020 | changed | the deadline follows the supplier's plan | Action: re-read the plan | Was: The report shall be delivered monthly.
- YYYY-MM-DD | 0.2 | <author> | FND.0010 | closed | resolved by the new wording of REQ.0020
- YYYY-MM-DD | 1.0 | <author> | 20-assignment.md | approved
```

The second round is version 0.2, with two records.
The record of `REQ.0020` carries the reason, what the reader must do
and the old wording.
The record of `FND.0010` is a record of state only: it carries the
current version and does not raise it.

## See also

- [Versioning and front-matter](../reference/versioning-and-front-matter.md): the fields and the scheme, exactly.
- [History companion](../reference/history-companion.md): the record's shape.
- [Read the history of an item](../use/read-the-history-of-an-item.md): reading one item's history by command.
- [Release a version](../use/release-a-version.md): where the tag of a major is proposed.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
