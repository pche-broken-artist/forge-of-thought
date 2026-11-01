---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 0fb283f16a8e6a0a
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

A version number in the forge says whether a document is a draft or
has been signed off, and a document's history lives in a separate
file beside it, never in its body. This page explains what the
number means, what a major of an intent is and what its test
attests, why a header carries so little, and how the history
companion records every change. It is for anyone who reads, writes
or evaluates a versioned document of a project: the principal (the
person whose thinking is being forged), an extender of the forge,
or an evaluator of its documents. The exact fields and the scheme
are listed in [Versioning and
front-matter](../reference/versioning-and-front-matter.md); the
shape of one record is in [History
companion](../reference/history-companion.md).

## What it is

Every versioned document of a project carries a version number in
its front-matter. The scheme is the house scheme, aligned with the
group BRD standard: integers denote signed-off versions.

- `0.1, 0.2, …` are drafts before the first approval.
- `1.0` is approved.
- `1.1, 1.2, …` are changes made after approval, not yet approved
  themselves.
- `2.0` is the next approved version, incorporating all changes
  since `1.0`.

The status of a document is one of `draft`, `approved` and
`superseded`. The status must agree with the number: an integer
version is `approved`, anything else is not.

One kind is versioned but never approved: the recipe, the file a
render is made from. A recipe carries a version and no status
field. It stays 0.x unless the principal names an integer. When he
names one, `1.0` or `2.0`, the recipe takes it and the count goes on
from there, `2.1`, `2.2`. Claude never proposes the integer. The
number means nothing beyond the principal's own mark, and nothing
guards or reads it. A render cites the recipe's version in its
provenance. How a recipe is composed and iterated is explained in
[Renders and recipes](renders-and-recipes.md).

Every versioned document keeps its history in an append-only
companion, `<file>.history.md`, beside it, never in its body. The
body is the current state; the companion is the record. The rule
has no exception: the brief, the intent, the assignment, every
later layer of the chain, the recipe and the work specification
alike. The companion is part of its document: it has no row of its
own in the ledger (the project's state, built by a script at read
time), and it is handed over with the document by the link into
git.

## How it works

### The header

A header carries nothing that changes with a round. What stays in
it is what does not change with the work: `project`, a brief's
`title` and `author`, an index's `directory`, and `version` and
`status`, which change with a version and never with an operation.
The date of a document and its last change are not written in the
header. Whatever reads them, such as `/history` or the ledger,
computes them from the history at that moment. The date of a recipe
is computed the same way.

### A major of an intent

A major of an intent is an integer version of it. It closes a set of
features the principal names. Before its tag it passes a fuller test
than a minor does, and the findings of that test are settled or
deferred by the principal's word. The word closes the major; the
test says what the word attests. Where the tag of a major is
proposed is shown in [Release a version](../use/release-a-version.md).

A major approves the intent as the record of what the principal
holds at that date. The package it names is finished and goes out.
What is open stays open in its thread, and a position marked for a
later pass stays marked. The approval signs nothing over: it says
what is done, not that nothing is left.

The test of a major attests that the documents conform to the
conventions and to each other, and that the thinking has been
challenged. It attests nothing of how the model behaves on them.
Behaviour is verified by the author's own use until the forge has a
test of it.

### The history companion

The history is a log. One record is one change and one line.
Records are appended at the end of the file and never rewritten, so
the order of the file is the order of the changes. A round is one
version and as many records as it made changes; a version may hold
several records, of the same item too.

A record names its subject: the ID of the item it touches, several
IDs where the whole line holds for each, or a place without an ID,
such as the heading of a section or the file name where the change
is of the document as a whole.

A record has one of five kinds.

- `created`: an item or the document is born; no reason is written,
  because the wording is in the document.
- `changed`: wording changed.
- `closed`: a thread or an open question was settled; the record
  says what was decided and where it now stands.
- `removed`: an item leaves the document and its ID is never used
  again.
- `approved`: the document as a whole was approved, such as a brief
  or a major.

`rejected`, `parked` and `obsolete` are not kinds of a record. They
are the Verdict of a decision and live in the decisions file.

A record names its author: the one who decided the change, by the
handle the instance gives its principal, never the one who typed
it. Where the instance gives no handle, a write that would append a
record stops before it writes and offers `/setup`; the handle is
never guessed. The field is there from the first record, because a
log is never rewritten and a field it lacks cannot be added to what
was written.

A record carries the reason for the change. The way to an item, why
it changed, what was said, trials, measurements, which research
turned it, goes into its record and never into the item. A record
may carry `Action:`, what the user must do after the change,
written with the change by whoever made it. `Was` is, word for word,
the part of the wording that ceased to hold; it stands wherever
wording leaves an item or a place, always last, with paragraphs in
it divided by `<br>`. A record of a change to the document as a
whole carries no `Was`. Lines of the log are not wrapped.

The record is written in the same step as the change it records.
The reflection Claude gives before a write shows both: the new
wording of every item touched and the record the history will
receive, `Was` included.

At the birth of a document the log opens with one record of the file
and one record naming every item born with it.

### Records of state

A record of state only carries the current version and does not
raise it. Such records are a mining of a brief, a finding or a
challenge settled, a thread closed, and the state of a work product.
So a round that only closes findings after a check and changes no
content is not a version. A state record still marks a render stale,
as every raise of the version does.

The template gives each its shape. The mining of a brief is recorded
in the intent's history with the brief's file as subject, as
`changed` with `mined: pending`, `partial`, `mined` or `dropped` and
a note. A finding or a challenge settled is recorded as `closed`
with what fixed it, in the history of the artefact whose version
settled it, or in the intent's history where no version did or the
check was of the engine. A work product's state is recorded in its
specification's history: `state: current` with the date of the
making and the inputs with their versions, `state: stale` after a
write of the specification, `state: by hand` on the principal's
word.

### Reading a history

Before Claude proposes a change to an item, it searches the history
and its archive for the item's ID, through one command, `/history
<ID>`. A script gathers what the project holds of the item: its
wording today, every record whose subject it is, the records of
other items that mention it, the rows of the archive that mention it
and every other place in the project that cites it. Claude adds a
few sentences of its own on top, marked as such, and nothing is
derived from them. What it finds is said in the proposal only where
it bears on the change, a direction once tried and dropped above
all. A history is searched, never loaded whole. How the command is
used is shown in [Read the history of an
item](../use/read-the-history-of-an-item.md).

### The archive

A companion written before the log keeps its table untouched. It
moves as it stands to `<file>.history.archive.md`, immutable from
then on, and the log begins with the next version. Nothing is
converted: its rows are a record and stay in the words they were
written in. The history of an item is a search of both files. A
Version History table, in the body of a document or in its
companion, is a finding of `/check`, settled by that move on the
principal's word, project by project.

### What derives from the log

The log is the single primary. The commit messages that `/save` and
`/release` draft and the release notes are derivations from it. The
release notes are made at a release from the records since the
previous release, one section per release, newest first; at a major
the minors since the previous major are folded into it. One thing in
them is never derived: what the reader must do is taken word for
word from the `Action` field of the record.

## Why

Integers denote approval because the scheme is the group's BRD
convention, and the forge keeps to it. A scheme where the major
meant a scope change was considered and rejected: a scope change is
a reason for re-approval anyway, so the integer already covers it.

A recipe stays 0.x because approval has a meaning only where someone
receives the document, and a recipe is received by nobody. It is
iterated continuously, as a tool and not as a record of thinking.

A header carries nothing that changes with a round because a header
field written at every operation is the certain conflict of every
pair of rounds in every artefact, whatever the rounds were about.
Computing the date from the history asks for no write at every
round.

The way to an item goes into its record and not into the item
because the body is the current state and the companion is the
record. A further reason is not recorded.

The author field is there from the first record because a log is
never rewritten, and a field it lacks cannot be added to what was
already written.

A record of state does not raise the version so that a round which
only closes findings and changes no content is not counted as a
version.

The history is read through one command because the history of an
item is scattered over the log, the archive and the records of other
items, and reading a whole log is forbidden. Done by hand, the
search was done differently every time; what is deterministic is a
script's, and the judgement is what remains for the model.

The release notes derive from the log because a reader wants to see
plainly what was added, changed and removed. Why the log, rather
than anything else, is the single primary is not recorded beyond
that.

An old companion is archived rather than converted because its rows
are a record, and a record stays in the words it was written in.

## A worked example

A generic history companion of an assignment, after its birth and
one later round. The handle `<author>` stands for the principal's
handle as the instance gives it.

```
---
project: <slug>
document: 20-assignment.md
---

# History — 20-assignment.md

- 2026-03-02 | 0.1 | <author> | 20-assignment.md | created
- 2026-03-02 | 0.1 | <author> | REQ.0010, REQ.0020, REQ.0100 | created
- 2026-03-09 | 0.2 | <author> | REQ.0020 | changed | the recipients asked which systems the rule covers; the item now names them | Action: tell the recipients that the scope of REQ.0020 is now explicit | Was: The service shall log every change.
- 2026-03-09 | 0.2 | <author> | REQ.0100 | removed | folded into REQ.0020, which now covers the case | Was: The service shall log every change to a customer record.
```

The first two lines are the birth of the document: one record of the
file and one naming every item born with it, no reason on either.
The third and the fourth are one round and one version, `0.2`, with
two records. Each carries the reason, the third an `Action` for the
user, and both a `Was` with the wording that ceased to hold. The
version stays below `1.0`, so the document's status is `draft`.

## See also

- [Versioning and front-matter](../reference/versioning-and-front-matter.md): the fields and the scheme, exactly.
- [History companion](../reference/history-companion.md): the record's shape.
- [Read the history of an item](../use/read-the-history-of-an-item.md): reading one item's history by command.
- [Release a version](../use/release-a-version.md): where the tag of a major is proposed.
- [Renders and recipes](renders-and-recipes.md): the recipe, the one versioned kind that is never approved.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
