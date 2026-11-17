---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: abeea53cf8c093a3
inputs:
  - CLAUDE.md#Versioning & status
  - templates/history.md
  - projects/forge/10-intent.md#POS.0300
  - projects/forge/10-intent.md#POS.0310
  - projects/forge/10-intent.md#POS.0710
  - projects/forge/10-intent.md#POS.1570
  - projects/forge/10-intent.md#POS.1630
  - projects/forge/10-intent.md#POS.0730
  - projects/forge/10-intent.md#POS.1510
  - projects/forge/10-intent.md#REJ.0110
---

# Versioning and history

A version number says whether a document has been signed off, and
the history of a document is a log kept in a file beside it. This
page explains what the number means, what a major is, where the
history lives and why both are built this way. It is for whoever
uses the forge, extends it or evaluates it.

## What it is

Every versioned document carries a version number and keeps a
history. Three kinds of document are versioned:

- every artefact (a brief, an intent, an assignment and every later
  document of the chain)
- every recipe (the versioned file a render is generated from; see
  [Renders and recipes](renders-and-recipes.md))
- every work specification (the specification of a work product)

Each of these terms has a line in the
[Glossary](../reference/glossary.md).

The number follows one scheme, in which integers denote signed-off
versions:

- `0.1, 0.2, …`: drafts before first approval
- `1.0`: approved
- `1.1, 1.2, …`: changes made after approval, not yet approved
  themselves
- `2.0`: the next approved version, incorporating all changes since
  1.0

The history is kept in a companion file (`<file>.history.md`) beside
the document and never in its body. The body is the current state.
The companion is the record. The rule has no exception among the
versioned documents.

The companion is a log. One record is one change and one line.
Records are appended at the end of the file and never rewritten.

## How it works

### The number and the status

The header of a document carries a `status` beside its `version`:
`draft | approved | superseded`. The status must agree with the
number. An integer version is `approved`. Anything else is not.

### The number of a recipe

A recipe carries a version and no status. It stays at 0.x as long as
the principal (the person whose thinking is being forged) names no
integer. When the principal names one, such as 1.0 or 2.0, the
recipe takes it and the count goes on from there: 2.1, 2.2. Claude
never proposes an integer. The number is the principal's own mark
and not an approval: nothing guards it and nothing reads it. A
render cites the version of its recipe.

### A major

A major is an approved version, that is an integer. The versions
between two majors are minors.

A major of the forge's own intent closes a set of features that the
principal names. Before its tag (see
[Release a version](../use/release-a-version.md), where the tag of a
major is proposed) it passes more than a minor does:

- every check, the check `single-source-of-truth` included
- both lenses of the critic
- one challenge
- the principal's word on their findings, each settled or deferred
- a pass through the parked items whose condition has come

Check, critic, challenge and finding each have a line in the
[Glossary](../reference/glossary.md).

The principal's word closes the major. The test says what that word
attests. It attests that the documents conform to the conventions
and to each other, and that the thinking has been challenged. It
attests nothing of how Claude behaves on the documents. Behaviour is
verified by the author's own use of the forge until the forge has a
test of it.

A major approves the intent as the record of what the principal
holds at that date. The package the major names is finished and goes
out. What is open stays open in its thread (the file an open matter
is kept in). A position (an item of the intent) marked for a later
pass stays marked. The approval signs nothing over: it says what is
done, not that nothing is left.

The approval enters the history as a record of the kind `approved`,
which is a record of the document as a whole. In the release notes
(a log of releases, one section per release) a major folds in the
minors since the previous major. This is the scheme's own reading of
a major: "the next approved version, incorporating all changes
since".

### The header

A header carries nothing that changes with a round (see
[Glossary](../reference/glossary.md)). It keeps `version` and
`status`, which change with a version and never with an operation.
Beside them it keeps only what does not change with the work, such
as `project`. The date and the last change of a document are not in
its header. Whatever reads them computes them from the history: the
command `/history` and the ledger (the file that shows the state of
a project) both do. The fields are listed in
[Versioning and front-matter](../reference/versioning-and-front-matter.md).

### The record

The order of the file is the order of the changes. A version may
hold several records, and several of the same item. The template of
a history gives the shape of a record:

```
- <date> | <version> | <author> | <subject> | <kind> | <reason> | Action: <what the user must do> | Was: <wording that ceased to hold>
```

What the fields carry:

- The author is the one who decided the change, never the one who
  typed it. The handle is the one the instance (one installation of
  the forge) gives its principal.
- The subject is the ID of the item the change touches. Where the
  change touches what has no ID, the subject is the place: the
  heading of a section, or the file name where the change is of the
  document as a whole.
- The kind says what happened, such as `created`, `changed` or
  `closed`.
- The reason says why. A record of creation needs none: the wording
  is in the document.
- `Action` says what the reader of the release notes must do after
  the change. It is written with the change by whoever made it. A
  record carries it only where there is something to do.
- `Was` is word for word the part of the wording that ceased to
  hold. It is written wherever wording leaves an item or a place,
  and it stands last. A record of a change to the document as a
  whole carries none.

The whole shape and every kind are given in
[History companion](../reference/history-companion.md).

### Records of state

A record of state only carries the current version and does not
raise it. Such records are:

- the mining of a brief: the state of a brief, recorded in the
  history of the intent with the file of the brief as subject
- a finding or a challenge settled, and a thread closed
- the state of a work product, recorded in the history of its
  specification

A record of state marks a render stale, as every raised version
does.

### Writing a record

A record is written in the same step as the change it records. The
reflection before the write (Claude shows what it is about to write)
shows both: the new wording of every item touched and the record the
history will receive, `Was` included.

The record is appended at the end of its file by the script
`scripts/forge-record.py` and never by an edit (see
[Scripts](../reference/scripts.md)). The end of an append-only file
is found by a mechanism and never by hand. This holds for a history
and for the file of decisions alike.

The handle of the author comes from the instance. Where the instance
gives its principal no handle, a write that would append a record
stops before it writes and offers the command `/setup`, which adds
the handle. The handle is never guessed.

### Reading a history

The history of one item is read through one command, `/history
<ID>` (see
[Read the history of an item](../use/read-the-history-of-an-item.md)).
A script gathers what the project holds of the item:

- its wording today
- every record whose subject it is
- the records of other items that mention it
- the rows of the archive that mention it
- every other place in the project that cites it

The script prints all of it for that one item. Claude adds a few
sentences of its own on top and marks them as its own. Nothing is
derived from them.

This is the one way Claude reads the history of an item before it
proposes a change to the item. What it finds is said in the proposal
only where it bears on the change: above all a direction once tried
and dropped. The history is searched, never loaded whole.

The archive is a history written before the log. It is kept as it
stands beside the log and is immutable. Nothing in it is converted:
its rows are a record and stay in the words they were written in.
The history of an item is a search of both.

### What is derived from the log

The log is the single primary. Two things are derived from it by
mechanism:

- the commit messages that the commands `/save` and `/release` draft
- the release notes, whose sections are derived at a release from
  the records since the previous release

One thing is never derived: what the reader must do. It is written
with the change in the `Action` field of its record. The release
notes carry it word for word.

The companion is part of its document. It has no row of its own in
the ledger.

## Why

**Integers for approval.** The scheme is a house scheme, aligned
with a BRD standard in which integers denote signed-off versions. A
scheme of the form MAJOR.MINOR, in which MAJOR means a change of
scope, is rejected. A change of scope is a reason for re-approval
anyway.

**A recipe is never approved.** A recipe is a tool, not a record of
thinking. Approval has a meaning only where someone receives the
document, and a recipe is received by nobody. It is iterated
continuously. An integer on a recipe therefore means nothing beyond
the principal's own mark.

**A header free of what changes with a round.** A header field
written at every operation is the certain conflict of every pair of
rounds in every artefact, whatever the rounds were about. With the
date and the last change computed from the history, no field asks
for a write at every round.

**Parked items before a major.** The parked items whose condition
has come are gone through before the tag. The purpose: a parking
expires by the principal's word and never by silence.

**The history beside the document.** The way to an item does not
belong in the item. Why it changed, what was said, the trials, the
measurements and the research that turned it go into its record. The
body stays the current state.

**Appended at the end, by a script.** The order of the file is the
order of the changes, and the file is read by that order. A record
placed by an editor that can put a line anywhere breaks the order.
The reason for writing the record in the same step as the change is
not recorded.

**The author from the first record.** A log is never rewritten, and
a field it lacks cannot be added to what was written. The author is
therefore named from the first record on.

**A record of state raises no version.** A round that only closes
findings after a check changes no content. Such a round is not a
version.

**One primary.** Commit messages and release notes are derivations
of the log. The release notes are a log of releases, not a story.
The reason: a reader wants to see plainly what was added, changed
and removed. Why what the reader must do is never derived is not
recorded.

**Searched, never loaded whole.** The history of an item is
scattered over the log, the archive and the records of other items.
Reading a whole log is forbidden. A search by hand runs differently
every time. What is deterministic belongs to a script, and the
judgement is what remains for Claude.

## A worked example

Three records from the history of an intent (`10-intent.md`) in a
project with the brief `00-brief-pilot.md`. `<author>` stands for
the handle of the principal.

```
- 2026-03-02 | 0.1 | <author> | 10-intent.md | created
- 2026-03-09 | 0.2 | <author> | Scope | changed | the second site has no data yet | Action: plan the pilot for one site | Was: The pilot covers both sites.
- 2026-03-12 | 0.2 | <author> | 00-brief-pilot.md | changed | mined: partial, the cost figures still to come
```

The first record is the birth of the file. Its kind is `created`,
and it carries no reason: the wording is in the document. At the
birth of a document a second record of the same kind names every
item born with it.

The second record is one change, and it raised the version to 0.2.
Its subject is a place without an ID: the section `Scope`. Where a
change touches an item, the ID of the item stands there instead. The
reason follows the kind. `Action` says what the reader must do.
`Was` stands last and gives word for word the sentence that ceased
to hold. The new wording is not in the record: it is in the body of
the intent.

The third record is a record of state only. It says how far the
brief has been mined. It carries the current version (0.2) and does
not raise it.

## See also

- [Versioning and front-matter](../reference/versioning-and-front-matter.md):
  the fields and the scheme, exactly.
- [History companion](../reference/history-companion.md): the
  record's shape, and the archive of a history written before the
  log.
- [Read the history of an item](../use/read-the-history-of-an-item.md):
  reading one item's history by command.
- [Release a version](../use/release-a-version.md): where the tag of
  a major is proposed.
- [Renders and recipes](renders-and-recipes.md): the recipe, the one
  versioned kind that is never approved.
- [Scripts](../reference/scripts.md): the script that appends a
  record or a decision at the end of its file.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
