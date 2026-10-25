---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: ef59d2e954590671
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

A version number in Forge of Thought says whether a document has
been signed off, and every versioned document keeps the record of
its changes in a history file beside it. This page explains what the
numbers mean, what a major of an intent is, why a document's header
carries no date, and how the history is kept and read. It is for
anyone who uses the forge, extends it or evaluates it. The exact
fields and the scheme are listed in
[Versioning and front-matter](../reference/versioning-and-front-matter.md).

## What it is

### The numbers

Integers denote signed-off versions.
The principal (the person whose thinking is being forged, and the
final authority on its content) is the one who signs off.

- `0.1, 0.2, …`: drafts before the first approval.
- `1.0`: approved.
- `1.1, 1.2, …`: changes made after approval, not yet approved
  themselves.
- `2.0`: the next approved version, incorporating all changes since
  `1.0`.

The scheme is aligned with the group BRD standard.
A document's header carries a `status` beside its `version`: one of
`draft`, `approved` and `superseded`.
The status must agree with the number.
An integer version is `approved`, and anything else is not.

A recipe is the exception.
A recipe (the versioned file that says how a render, an
audience-specific output, is made) carries no status.
It stays at `0.x` for life, because a recipe is iterated and never
approved.

### What the header carries

A header carries nothing that changes with a round.
A round is one working conversation over a document, written once at
its end.
The header keeps only what does not change with the work:

- `project`;
- a brief's `title` and `author`;
- an index's `directory`;
- `version` and `status`, which change with a version, never with an
  operation.

The date of a document and its last change are not in the header.
Whatever reads them computes them from the document's history: the
`/history` command, or the ledger (the state report of a project,
made by a script at read time).

### The history companion

Every versioned document keeps its history in an append-only
companion, `<file>.history.md`, beside it.
There is no exception: a brief, an intent, an assignment, every later
artefact, a recipe and a work specification alike.
The body of the document is its current state.
The companion is the record of how it got there.
The companion is part of its document.
It has no row of its own in the ledger, and it travels with the
document in git.

## How it works

### One record per change

The history is a log.
One record is one change and one line.
Records are appended at the end of the file and never rewritten, so
the order of the file is the order of the changes.
One version may hold several records, of the same item too.
The record's shape is set out in full in
[History companion](../reference/history-companion.md); its fields,
in order, are these:

- date;
- version: the version the change belongs to;
- author: the one who decided the change, by the handle the instance
  gives its principal, never the one who typed it;
- subject: an item's ID, several IDs where the whole line holds for
  each, or a place without an ID (a section, or the file);
- kind: `created`, `changed`, `closed`, `removed` or `approved`;
- reason: why the change was made, left out on `created`, since the
  wording is in the document;
- `Action:`: what the user must do after the change, only where there
  is something to do;
- `Was:`: word for word the wording that ceased to hold, always last.

The kinds mean the following:

- `created`: an item or the file is born. At the birth of a document
  there is one record of the file and one naming every item born with
  it.
- `changed`: wording changed.
- `closed`: a thread (one open matter of the intent) or an open
  question settled. The record says what was decided and where it now
  stands, and carries no `Was`.
- `removed`: an item leaves the document, and its ID is never used
  again.
- `approved`: the document as a whole is approved, such as a brief or
  a major.

The record is written in the same step as the change it records.
Before a write, Claude shows both the new wording of every item it
touches and the record the history will receive, `Was` included.

### Records of state only

Some records change no content and only say what state something is
in:

- the mining of a brief, in the intent's history, with the brief's
  file as subject;
- a finding or a challenge closed, in the history of the artefact
  whose version settled it;
- a thread closed;
- a work product's state, in its specification's history.

A record of state only carries the current version and does not raise
it.
So a round that only closes findings after a check, and changes no
content, is not a version.
A state record still marks a render stale, as every raise of a
version does.

### A major of an intent

A major is an integer version: the approval of the whole document.
In the forge's own project, a major of the intent closes a set of
features the principal names.
It passes a fuller test than a minor before its tag.
That test is the checks, both critic lenses and one challenge, their
findings settled or deferred by the principal's word.
The principal's word closes the major.
The test says what that word attests.

A major approves the intent as the record of what the principal
holds at that date.
The package it names is finished and goes out.
What is open stays open in its thread, and a position marked for a
later pass stays marked.
The approval says what is done, not that nothing is left.

The test of a major attests that the documents conform to the
conventions and to each other, and that the thinking has been
challenged.
It attests nothing of how the model behaves on those documents.
Behaviour is verified by the author's own use until the forge has a
test of it.
Where the tag of a major is proposed is described in
[Release a version](../use/release-a-version.md).

### Reading a history

Before Claude proposes a change to an item, it reads that item's
history.
It does this through one command, `/history <ID>`.
A script gathers what the project holds of the item:

- its wording today;
- every record whose subject it is;
- the records of other items that mention it;
- the rows of the archive that mention it;
- every other place in the project that cites it.

Claude adds a few sentences of its own on top, marked as such.
The history is searched by this script, never loaded whole.
How to run it yourself is shown in
[Read the history of an item](../use/read-the-history-of-an-item.md).

### The archive

A companion written before the log keeps its old table untouched.
The table moves as it stands to `<file>.history.archive.md`, which is
immutable from then on.
The log begins with the next version.
Nothing is converted: the old rows stay in the words they were
written in.
The history of an item is then a search of both files.
A Version History table found in the body of a document or in its
companion is a finding of `/check`.
It is settled by that move, on the principal's word, project by
project.

## Why

**Why integers mean approval.**
An earlier idea was rejected: `MAJOR.MINOR` with the major number
meaning a change of scope.
A change of scope is a reason for re-approval anyway.
So the number tracks approval, as the group convention does.

**Why the header carries no date.**
A header field written at every operation would be a certain conflict
between any two rounds on the same document, whatever the rounds were
about.
Computing the date and the last change from the history removes that
field, so no field asks for a write at every round.

**Why the way to an item lives in its record, not in the item.**
The body is the current state and the companion the record.
Why an item changed, what was said, trials, measurements and the
research that turned it go into its record.
The item itself states only what holds now.

**Why the author field is there from the first record.**
A log is never rewritten.
A field it lacks could never be added to what was already written.

**Why the log is the single primary.**
The commit messages that `/save` and `/release` draft, and the
release notes, are derived from the records.
Release notes are a log of releases, because a reader wants to see
plainly what was added, changed and removed.
One thing is never derived.
What the reader must do is written with the change, in the `Action`
field, and carried into the release notes word for word.

**Why a history is read through one command.**
The history of an item is scattered over the log, the archive and the
records of other items.
Without a command, the search was done by hand and differently every
time.
What is deterministic belongs to a script; the judgement is what
remains for the model.
Why a log is never loaded whole is not recorded.

**Why records of state do not raise the version.**
A round that only closes findings and changes no content should not
count as a version.

## A worked example

A generic history companion, with placeholder handle and IDs, as the
template shapes it:

```
- 2030-01-10 | 0.1 | JDo | 10-intent.md | created
- 2030-01-10 | 0.1 | JDo | POS.0010, POS.0020, THR.0010 | created
- 2030-01-17 | 0.2 | JDo | POS.0020 | changed | narrowed after the first review | Action: re-read the scope section | Was: The tool covers every team.
- 2030-01-17 | 0.2 | JDo | THR.0010 | closed | settled in POS.0020
- 2030-01-24 | 0.2 | JDo | FND.0030 | closed | fixed by the rewording of POS.0020
```

The first two lines record the birth of the document and of every
item born with it.
The third is a change of wording with its reason, an action for the
reader and the wording that ceased to hold.
The fourth closes a thread in the same version.
The last is a record of state only: it closes a finding a week later
and carries the current version, `0.2`, without raising it.

## See also

- [Versioning and front-matter](../reference/versioning-and-front-matter.md): the fields and the scheme, exactly.
- [History companion](../reference/history-companion.md): the record's shape.
- [Read the history of an item](../use/read-the-history-of-an-item.md): reading one item's history by command.
- [Release a version](../use/release-a-version.md): where the tag of a major is proposed.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
