---
generated: 2026-10-23
version: 5.33
made: derived
inputs-hash: 8e26704720598f22
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
signed off, and a document's history is a separate log beside it
that records every change with its reason. This page explains what
the numbers mean, what a major version is, why a document's header
holds so little, and where and why the history lives. It is for
anyone who uses the forge, extends it or evaluates it. The exact
fields and the exact shape of a record are reference matters,
described in
[Versioning and front-matter](../reference/versioning-and-front-matter.md)
and [History companion](../reference/history-companion.md).

## What it is

The forge numbers versions by one rule: integers denote signed-off
versions. The person whose thinking is forged is called the
principal. Signing off is the principal's approval.

- `0.1, 0.2, …`: drafts before the first approval.
- `1.0`: approved.
- `1.1, 1.2, …`: changes made after approval, not yet approved
  themselves.
- `2.0`: the next approved version, incorporating all changes since
  `1.0`.

A document carries a `status` beside its `version`, one of `draft`,
`approved` or `superseded`. The status must agree with the number.
An integer version is `approved`, and anything else is not. A recipe
(the versioned file that says how a render is made) carries no
status. A recipe stays at `0.x` for its whole life.

Every versioned document keeps its history in a companion file
beside it, named `<file>.history.md`. This holds without exception:
every artefact of the chain, every recipe and every work
specification. The body of the document is its current state. The
companion is the record of how it got there.

## How it works

### Rounds and versions

Work on a document runs in rounds. A round is one working
conversation whose agreed changes are written once at its end. A
round is one version. It produces as many records in the history as
it made changes.

### What the header holds

A header carries nothing that changes with a round. What stays in it
is what does not change with the work:

- `project`.
- `title` and `author`, in a brief.
- `directory`, in an index.
- `version` and `status`, which change with a version, never with an
  operation.

The date of a document and its last change are not in the header.
Whatever needs them computes them from the history, such as the
`/history` command and the ledger (the state report the forge builds
from the documents at read time).

### The history log

The history is a log. One record is one change and one line. Records
are appended at the end of the file and never rewritten, so the
order of the file is the order of the changes. A version may hold
several records, of the same item too.

A record names:

- the date and the version it belongs to;
- its author: the one who decided the change, by the handle the
  instance gives its principal, never the one who typed it;
- its subject: an item's ID, several IDs where the line holds for
  each, or a place without an ID (a section, or the file as a
  whole);
- its kind: `created`, `changed`, `closed`, `removed` or `approved`;
- its reason, left out on `created` because the wording is in the
  document;
- `Action`, where there is one: what the user must do after the
  change, written with the change by whoever made it;
- `Was`, where wording left an item or a place: word for word the
  part that ceased to hold, always last.

The record is written in the same step as the change it records.
Before a write, Claude shows both the new wording of every item
touched and the records the history will receive, `Was` included.

### Records of state

Some records change no content and only say a state. Examples are
the mining of a brief into the intent, a finding or a challenge
closed, a thread closed and the state of a work product. A record of
state only carries the current version and does not raise it. Like
every raise of a version, a state record marks a render built from
the document as stale.

### Reading a history

A history is searched, never loaded whole. The history of one item
is read through one command, `/history <ID>`. A script gathers the
item's wording today, every record whose subject it is, the records
of other items that mention it, the rows of the archive that mention
it and every other place in the project that cites it. Claude adds a
few sentences of its own on top, marked as such. Before Claude
proposes a change to an item, it reads that item's history this way.
How to run it is described in
[Read the history of an item](../use/read-the-history-of-an-item.md).

### What derives from the log

The log is the single primary. The commit messages that `/save` and
`/release` draft are derived from it. The release notes are derived
from it too: at each release, from the records since the previous
release. One thing is never derived. What the reader must do is
taken word for word from the `Action` field of the records into the
release notes' *Action required*. At a major, the minors since the
previous major are folded into it.

### The companion travels with its document

The companion is part of its document. It has no row of its own in
the ledger. It is handed over with the document by the link into
git.

### The archive

A companion written before the log keeps its old table untouched.
That table moves as it stands to `<file>.history.archive.md`, which
is immutable from then on. Nothing in it is converted. The log
begins with the next version. The history of an item is a search of
both files. A Version History table, in the body of a document or in
its companion, is a finding of `/check`. It is settled by that move,
on the principal's word, project by project.

### What a major is

A major is an integer version, that is an approved one. A major
approves the intent as the record of what the principal holds at
that date. The package it names is finished and goes out. What is
open stays open in its thread (a thread is one open matter of the
intent). The approval signs nothing over: it says what is done, not
that nothing is left. The principal's word closes the major.

A major can be tested before its tag by reviewer runs, with their
findings settled or deferred by the principal's word. The test says
what the word attests. It attests that the documents conform to the
conventions and to each other, and that the thinking has been
challenged. It attests nothing of how the model behaves on them.
Behaviour is verified by the author's own use until the forge has a
test of it. Where the tag of a major is proposed is described in
[Release a version](../use/release-a-version.md).

## Why

- **Integers mean approval.** The scheme follows a group BRD
  convention. A scheme where the first number meant a change of scope
  was rejected. A change of scope is a reason for a new approval
  anyway.
- **Status agrees with the number.** The reason is not recorded
  beyond the scheme itself.
- **A recipe stays 0.x.** The reason is not recorded.
- **Nothing in the header changes with a round.** A header field
  written at every operation is a certain conflict between any two
  rounds on any artefact, whatever the rounds were about. Computing
  the date and the last change from the history means no field asks
  for a write at every round.
- **The way to an item goes into the record, not the item.** Why an
  item changed, what was said, trials, measurements and the research
  that turned it go into its record. The body stays the current
  state, and the companion stays the record.
- **The author field is there from the first record.** A log is
  never rewritten, so a field it lacks cannot be added to what was
  already written.
- **A state record does not raise the version.** A round that only
  closes findings after a check and changes no content is not a
  version.
- **The log is the single primary.** Commit messages and release
  notes are derivations by mechanism, so they cannot drift from it.
  A reader of the release notes wants to see plainly what was added,
  changed and removed.
- **One command reads an item's history.** The history of an item is
  scattered over the log, the archive and the records of other
  items. Searched by hand, it was searched differently every time.
  What is deterministic belongs to a script, and the judgement is
  what remains for the model.
- **A history is never loaded whole.** The reason is not recorded.

## A worked example

A generic history companion, taken from no project. The first two
records are the birth of the document: one record of the file and
one naming every item born with it. The third is a change in a later
round, with its reason, an `Action` and the wording that ceased to
hold. The fourth is a record of state only: it closes a finding and
carries the current version without raising it.

```
---
project: <slug>
document: 20-assignment.md
---

# History — 20-assignment.md

- YYYY-MM-DD | 0.1 | <author> | 20-assignment.md | created
- YYYY-MM-DD | 0.1 | <author> | REQ.0010, REQ.0020, CON.0010 | created
- YYYY-MM-DD | 0.2 | <author> | REQ.0020 | changed | the recipients need a fixed reporting cadence | Action: re-read REQ.0020 before the next planning | Was: Progress shall be reported regularly.
- YYYY-MM-DD | 0.2 | <author> | FND.0010 | closed | resolved by the rewording of REQ.0020
```

## See also

- [Versioning and front-matter](../reference/versioning-and-front-matter.md):
  the fields and the scheme, exactly.
- [History companion](../reference/history-companion.md): the
  record's shape.
- [Read the history of an item](../use/read-the-history-of-an-item.md):
  reading one item's history by command.
- [Release a version](../use/release-a-version.md): where the tag of
  a major is proposed.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-23 for version 5.33 from the files the
front-matter names; never edited by hand.
