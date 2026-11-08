---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: de4912e968360b5d
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

A version number in the forge says whether a document is signed off,
and a document's history lives in a companion file beside it, never
in its body. This page explains what the numbers mean, what a major
of an intent is, where the record of every change is kept and why it
is kept that way. It is for anyone who works with a project's
documents, extends the forge or evaluates it; the exact fields and
the record's shape are on the reference pages it links.

## What it is

The forge versions three kinds of document: every artefact of the
chain, every render recipe and every work specification. The scheme
is the house scheme, aligned with the group BRD standard, and its
one rule is that integers denote signed-off versions
([Versioning and front-matter](../reference/versioning-and-front-matter.md)
has the fields and the scheme exactly):

- `0.1, 0.2, …` are drafts before the first approval.
- `1.0` is approved.
- `1.1, 1.2, …` are changes made after approval, not yet approved
  themselves.
- `2.0` is the next approved version, incorporating all changes
  since `1.0`.

The status of a document (`draft | approved | superseded`) must
agree with the number. An integer version is `approved`; anything
else is not.

Every versioned document keeps its history in an append-only
companion `<file>.history.md` beside it
([History companion](../reference/history-companion.md) gives the
record's shape). The body is the current state; the companion is the
record. There is no exception: the brief, the intent, the assignment,
every later artefact, the recipe and the work specification alike
keep one.

## How it works

### The header

A header carries nothing that changes with a round. It holds
`version` and `status`, which change with a version and never with an
operation, beside what does not change with the work at all: the
`project`, a brief's `title` and `author`, an index's `directory`.
There is no date and no last-change field. The date and the last
change of a document are computed from its history by whatever reads
them, such as `/history` or the ledger (the project's state report,
built from the documents).

### The recipe

A recipe is versioned by the same scheme but carries no status. It
stays `0.x` unless the principal (the person whose thinking is being
forged) names an integer, `1.0` or `2.0`. When he does, the recipe
takes it and the count goes on from there, `2.1`, `2.2`. Claude never
proposes the integer. The number means nothing beyond his own mark:
nothing guards it and nothing reads it. A render cites the recipe's
version, and the recipe's date is computed from its history like any
other. [Renders and recipes](renders-and-recipes.md) explains the
recipe, the one versioned kind that is never approved.

### A major of an intent

A major of an intent closes a set the principal names. Before its
tag it passes more than a minor does: every check, the critic lenses
and one challenge, with their findings settled or deferred by his
word. Before the tag the parked items whose condition has come are
walked, that is, put to him one at a time for a verdict. So that a
parking expires by a word and never by silence. The principal's word
closes the major; the test says what the word attests.

A major approves the intent as the record of what the principal
holds at that date. The package it names is finished and goes out.
What is open stays open in its thread, and a position marked for a
later pass stays marked. The approval signs nothing over: it says
what is done, not that nothing is left.

The test of a major attests that the documents conform to the
conventions and to each other, and that the thinking has been
challenged. It attests nothing of how the model behaves on them;
behaviour is verified by the author's own use until the forge has a
test of it. Where the tag of a major is proposed is said in
[Release a version](../use/release-a-version.md).

### The history log

The companion is a log: one record per change, one line each,
appended at the end and never rewritten. So the order of the file is
the order of the changes. A round is one version and as many records
as it made changes; a version may hold several records, of the same
item too.

Each record carries:

- the date and the version;
- the author: the one who decided the change, by the handle the
  instance gives its principal, never the one who typed it; where
  the instance gives no handle, a write that would append a record
  stops and offers `/setup`;
- the subject: an item's ID, several IDs where the whole line holds
  for each, or a place without an ID, such as the heading of a
  section or the file name where the change is of the document as a
  whole;
- the kind: `created`, `changed`, `closed` (a thread or an open
  question settled), `removed` (an item leaves the document and its
  ID is never used again) or `approved` (of the document as a whole,
  such as the approval of a brief or of a major);
- the reason, left out on `created`, since the wording is in the
  document;
- `Action`, only where there is one: what the user must do after the
  change, written with the change by whoever made it;
- `Was`, always last and only where wording left an item or a place:
  word for word the part of the wording that ceased to hold; a record
  of a change to the document as a whole carries none.

At the birth of a document the log opens with two records: one of
the file and one naming every item born with it.

The record is written in the same step as the change it records. The
reflection Claude gives before a write shows both: the new wording of
every item touched and the record the history will receive, `Was`
included.

### A record of state only

A record of state only carries the current version and does not
raise it. Such records are the mining of a brief into the intent, a
finding or a challenge settled, a thread closed and the state of a
work product (made, stale or by hand). So a round that only closes
findings after a check and changes no content is not a version. A
state record does mark a render stale, as every raise does. A
rejected, parked or obsolete finding is a decision's verdict, never a
record of the history.

### The log as the single primary

The log is the single primary. The commit messages that `/save` and
`/release` draft and the release notes are derivations from it. The
release notes are derived from the records since the previous
release; at a major the minors since the previous major are folded
into it, which is the scheme's own reading of a major as the version
"incorporating all changes since". One thing is never derived: what
the reader must do is written in the `Action` field of its record,
and the release notes carry it word for word.

### Reading the history of an item

Before Claude proposes a change to an item, it reads the item's
history through one command, `/history <ID>`
([Read the history of an item](../use/read-the-history-of-an-item.md)).
A script gathers what the project holds of the item: its wording
today, every record whose subject it is, the records of other items
that mention it, the rows of the archive that mention it and every
other place in the project that cites it. Claude adds a few sentences
of its own on top, marked as such, and nothing is derived from them.
What it finds is said in the proposal only where it bears on the
change, a direction once tried and dropped above all. The history is
searched, never loaded whole.

### The companion and the archive

The companion is part of its document. It has no row of the ledger
and is handed over with the document by the link into git.

A companion written before the log keeps its table untouched. It
moves as it stands to `<file>.history.archive.md`, immutable from
then on, and the log begins with the next version. Nothing is
converted: the rows of the archive stay in the words they were
written in, and the history of an item is a search of both files. A
Version History table, in the body of a document or in its
companion, is a finding of `/check`, settled by that move on the
principal's word, project by project.

## Why

The integer means approval because approval is the fact a reader
needs from a number: whether what he holds was signed off. A scheme
in which the major number means a change of scope does not hold the
same information, and a scope change is a reason for re-approval
anyway, so the approval reading covers it.

A recipe stays `0.x` because approval has a meaning only where
someone receives the document, and a recipe is received by nobody:
it is a tool, iterated continuously, not a record of thinking.

The header carries no date because a header field written at every
operation is the certain conflict of every pair of rounds in every
artefact, whatever the rounds were about. Computing the date from
the history asks for no write at every round.

The way to an item does not belong in the item. Why it changed, what
was said, the trials, the measurements and the research that turned
it go into its record, never into the wording, so that the body stays
the current state and the companion the whole record.

The author field is there from the first record because a log is
never rewritten and a field it lacks cannot be added to what was
written.

The history is searched by a script because the history of an item
is scattered over the log, the archive and the records of other
items, and reading a whole log is forbidden. Done by hand, the search
was done differently every time. What is deterministic belongs to a
script; the judgement is what remains for the model.

The release notes derive from the log because a reader wants to see
plainly what was added, changed and removed, and the log already
holds that, one change per record.

## A worked example

A generic companion of an assignment, after its birth, one change
and one finding settled. The slug and the handle are placeholders;
the lines are not wrapped.

```
---
project: <slug>
document: 20-assignment.md
---

# History — 20-assignment.md

- 2026-03-02 | 0.1 | <author> | 20-assignment.md | created
- 2026-03-02 | 0.1 | <author> | REQ.0010, REQ.0020, DEL.0010 | created
- 2026-03-14 | 0.2 | <author> | REQ.0020 | changed | the recipients asked for one date, not a quarter | Action: re-render the one-page summary | Was: delivered within the second quarter
- 2026-03-20 | 0.2 | <author> | FND.0030 | closed | the term aligned with the glossary
```

The first two records are the birth: one of the file, one naming
every item born with it, no reason on either. The third is a change
of one item in a new version: the reason stands in the record, the
`Action` says what the user must do after it, and `Was` is the exact
wording that ceased to hold. The fourth is a record of state only: a
finding settled in the version that settled it, so it carries `0.2`
and raises nothing.

## See also

- [Versioning and front-matter](../reference/versioning-and-front-matter.md): the fields and the scheme, exactly.
- [History companion](../reference/history-companion.md): the record's shape.
- [Read the history of an item](../use/read-the-history-of-an-item.md): reading one item's history by command.
- [Release a version](../use/release-a-version.md): where the tag of a major is proposed.
- [Renders and recipes](renders-and-recipes.md): the recipe, the one versioned kind that is never approved.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
