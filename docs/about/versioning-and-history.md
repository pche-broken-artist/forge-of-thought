---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: a28a0117720a534f
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

A version number in the forge says whether a document has been signed
off, and its history says how it got there. This page explains what
the numbers mean, what a major is, what a document's header carries
and where its history lives, and why it is built that way. It is for
anyone who uses the forge, extends it or weighs it. The exact fields
and the scheme in full stand in
[Versioning and front-matter](../reference/versioning-and-front-matter.md);
the shape of one record stands in
[History companion](../reference/history-companion.md).

## What it is

### The version number

Integers denote signed-off versions. The scheme runs like this:

- `0.1, 0.2, …`: drafts before the first approval.
- `1.0`: approved.
- `1.1, 1.2, …`: changes made after approval, not yet approved
  themselves.
- `2.0`: the next approved version, incorporating all changes since
  `1.0`.

A document's status is one of `draft`, `approved` and `superseded`.
The status must agree with the number. An integer version is
`approved`, and anything else is not.

A recipe (the versioned file a render is made from) is the exception.
It carries no status and stays at `0.x` for its whole life. The
reason is not recorded.

### What a major is

A major is an integer version of an intent (the trunk document of a
project, which holds the positions of the principal, that is, the
person whose thinking is being forged). The principal's word closes a
major. A major approves the intent as the record of what the
principal holds at that date. The package of features it names is
finished and goes out. What is still open stays open in its thread
(one open matter, kept in a file of its own). A position marked for a
later pass stays marked. The approval says what is done; it does not
say that nothing is left.

For the engine's own intent, a major also passes a wider review than
a minor before its tag. Its findings are settled or deferred by the
principal's word. The word closes the major, and the review says what
the word attests. It attests two things:

- The documents conform to the conventions and to each other.
- The thinking has been challenged.

It attests nothing of how Claude behaves on those documents. That
behaviour is verified by the author's own use, until the forge has a
test of it. Where the tag of a major is proposed is described in
[Release a version](../use/release-a-version.md).

### The header

A header carries nothing that changes with a round. A round is one
working conversation over a document, written once at its end. What
stays in a header is what does not change with the work:

- `project`.
- A brief's `title` and `author`.
- An index's `directory`.
- `version` and `status`, which change with a version and never with
  a single operation.

The date of a document and its last change are not in the header.
Whatever reads them computes them from the history, such as the
`/history` command or the ledger (the state report a script builds
from the documents when it is read).

### The history companion

Every versioned document keeps its history in a companion file beside
it, named `<file>.history.md`. The rule has no exception: a brief, an
intent, an assignment, every later artefact, a recipe and a work
specification all keep one. The body of the document is its current
state. The companion is the record.

The companion is append-only. It is a log, and one record is one
change on one line. Records are added at the end and never rewritten.
So the order of the file is the order of the changes. One version may
hold several records, even of the same item.

A record says:

- the date;
- the version;
- the author, that is, the one who decided the change, by the handle
  the instance gives its principal, never the one who typed it;
- the subject: an item's ID, several IDs, or a place without an ID
  (a section, or the file as a whole);
- the kind: `created`, `changed`, `closed`, `removed` or `approved`;
- the reason, left out on `created`, because the wording is already in
  the document;
- `Action`, where there is one: what the user must do after the
  change;
- `Was`, where wording left an item or a place: word for word the part
  that ceased to hold, always last.

The companion is part of its document. It has no row of its own in
the ledger and travels with the document.

## How it works

### Records of state

Some records change no content. They record a state:

- the mining of a brief (how far its substance has entered the
  intent);
- a finding or a challenge closed;
- a thread closed;
- the state of a work product, in its specification's history.

A record of state only carries the current version and does not raise
it. So a round that only closes findings after a check, and changes no
content, is not a version. A record of state still marks a render
stale, as every raise does.

### Writing a record

A record is written in the same step as the change it records. Before
a write, Claude reflects back to the principal both the new wording of
every item touched and the record the history will receive, `Was`
included. What the user must do after the change is written with it,
in `Action`, by whoever made the change.

### Reading a history

A history is searched, never loaded whole. Before Claude proposes a
change to an item, it reads the item's history through
`/history <ID>`. A script gathers everything the project holds of that
one item and prints it in full:

- its wording today;
- every record whose subject it is;
- the records of other items that mention it;
- the rows of the archive that mention it;
- every other place in the project that cites it.

Claude adds a few sentences of its own on top, marked as such. How to
run it is described in
[Read the history of an item](../use/read-the-history-of-an-item.md).

### What derives from the log

The log is the single primary. The commit messages that `/save` and
`/release` draft are derived from it. The release notes are derived
from it too: their sections come from the records since the previous
release. One thing is never derived. What the reader must do is taken
word for word from the `Action` field of the records.

### The archive

Some companions were written before the log, as a table. Such a table
moves as it stands to `<file>.history.archive.md` and is immutable
from then on. Nothing in it is converted, and its rows stay in the
words they were written in. The log begins with the next version. The
history of an item is a search of both files. A Version History table
still found in a document or its companion is a finding of the check,
settled by that move on the principal's word.

## Why

- **Integers mean approval.** The forge follows the group BRD
  convention. A scheme where the major number meant a change of scope
  was rejected, because a change of scope is a reason for re-approval
  anyway.
- **Nothing in a header changes with a round.** A header field
  written at every operation is a certain conflict between any two
  rounds on the same document, whatever the rounds were about.
- **The way to an item stays out of the item.** Why an item changed,
  what was said, the trials and the research that turned it go into
  its record. The body stays the current state.
- **The author is there from the first record.** A log is never
  rewritten, so a field it lacks cannot be added to what was already
  written.
- **One log is the primary.** Commit messages and release notes are
  derived from it by mechanism, so there is one place to say what
  changed. A reader of the release notes wants to see plainly what
  was added, changed and removed.
- **A history is read by a script.** The history of one item is
  scattered over the log, the archive and the records of other items.
  Reading a whole log is ruled out, so the search was once done by
  hand and differently every time. What is deterministic is now a
  script's work, and the judgement is what remains for Claude.
- **The archive is kept as written.** The reason for converting
  nothing is not recorded.
- **A recipe stays at `0.x`.** The reason is not recorded.

## A worked example

A generic history companion of an assignment, after three rounds:

```
- 2026-01-10 | 0.1 | <author> | 20-assignment.md | created
- 2026-01-10 | 0.1 | <author> | REQ.0010, REQ.0020, REQ.0030 | created
- 2026-01-14 | 0.2 | <author> | REQ.0020 | changed | the deadline was a guess; the recipients set it | Was: The report shall be delivered within two weeks.
- 2026-01-14 | 0.2 | <author> | REQ.0030 | removed | duplicated REQ.0010 | Was: The recipients shall list the current tools.
- 2026-01-16 | 0.2 | <author> | FND.0040 | closed | resolved by the rewording of REQ.0020
- 2026-01-20 | 1.0 | <author> | 20-assignment.md | approved
```

The first two records mark the birth: one of the file and one naming
every item born with it. The `0.2` round made two changes, so it has
two records under one version. The record that closes a finding is a
record of state: it carries `0.2` and raises nothing. The approval is
a record of the document as a whole and carries no `Was`.

## See also

- [Versioning and front-matter](../reference/versioning-and-front-matter.md):
  the fields and the scheme, exactly.
- [History companion](../reference/history-companion.md): the record's
  shape.
- [Read the history of an item](../use/read-the-history-of-an-item.md):
  reading one item's history by command.
- [Release a version](../use/release-a-version.md): where the tag of a
  major is proposed.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
