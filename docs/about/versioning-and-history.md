---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 27747619ce927fb7
inputs:
  - CLAUDE.md#Versioning & status
  - templates/history.md
  - projects/forge/10-intent.md#POS.0300
  - projects/forge/10-intent.md#POS.0310
  - projects/forge/10-intent.md#POS.0730
  - projects/forge/10-intent.md#POS.1510
  - projects/forge/10-intent.md#REJ.0110
---

# Versioning and history

A version number in the forge says whether a document has been
signed off, and a document's history is a log kept in a separate
file beside it. This page explains what the numbers mean, what a
major of an intent is and where the record of a document's changes
lives, for the user who writes and approves documents, the extender
who changes the forge and the evaluator who wants to know what a
version attests. The exact fields are in
[Versioning and front-matter](../reference/versioning-and-front-matter.md);
the exact shape of a record is in
[History companion](../reference/history-companion.md); the other
terms are in the [Glossary](../reference/glossary.md).

## What it is

Every versioned document of the forge carries a version number in
its front-matter. The scheme is the house scheme, aligned with the
group BRD standard, and its one rule is that integers denote
signed-off versions:

- `0.1, 0.2, …` are drafts before the first approval.
- `1.0` is approved.
- `1.1, 1.2, …` are changes made after approval, not yet approved
  themselves.
- `2.0` is the next approved version, incorporating all changes
  since `1.0`.

The front-matter also carries a status (`draft`, `approved` or
`superseded`), and the status must agree with the number. An
integer version is `approved`; anything else is not. A recipe is
the one versioned kind that departs from this: it carries `updated`
in place of `date`, has no status, and stays `0.x` for life. The
reason a recipe is never approved is not recorded in the inputs of
this page.

A major of an intent is an integer version of it. It closes a
package of features that the principal (the person whose thinking
is being forged) names. It approves the intent as the record of what
the principal holds at that date. The package it names is finished
and goes out; what is open stays open in its thread, and a position
marked for a later pass stays marked. The approval signs nothing
over: it says what is done, not that nothing is left. Before its
tag a major passes a test that a minor does not. The test attests
that the documents conform to the conventions and to each other and
that the thinking has been challenged. It attests nothing of how
the model behaves on the documents. The principal's word closes the
major, and the test says what that word attests. Where the tag of a
major is proposed is in [Release a version](../use/release-a-version.md).

A document's history is not in the document. Every versioned
document, every artefact and every recipe alike, without exception,
keeps its history in an append-only companion `<file>.history.md`
beside it. The body is the current state; the companion is the
record.

## How it works

The companion is a log: one record per change, one line each,
appended at the end and never rewritten. The order of the file is
therefore the order of the changes. A round of work is one version
and as many records as it made changes; a version may hold several
records, of the same item too.

A record carries the date, the version, the author, the subject,
the kind of the change, the reason, and where the record has them
an `Action` and a `Was`. The subject is an ID, several IDs where the
whole line holds for each, or a place without an ID: the heading of
a section, or the file name where the change is of the document as
a whole. The kinds are five:

- `created`: an item or the document is born; no reason is given,
  because the wording is in the document.
- `changed`: the wording of an item or a place changed.
- `closed`: a thread or an open question is settled.
- `removed`: an item leaves the document, and its ID is never used
  again.
- `approved`: the document as a whole is approved, as a brief is or
  as a major is.

`Was` is, word for word, the part of the wording that ceased to
hold. It is written wherever wording leaves an item or a place; a
record of a change to the document as a whole carries none. Where
`Was` holds several paragraphs they are divided by `<br>`, and
`Was` always stands last. `Action` is what the user must do after
the change, written with the change by whoever made it.

The author of a record is the one who decided the change, by the
handle the instance (one installation of the forge) gives its
principal, never the one who typed it. The field is present from
the first record.

The record is written in the same step as the change it records.
Before a write, Claude reflects back both the new wording of every
item touched and the record the history will receive, `Was`
included. The `last_change` field of the front-matter is derived
from the records of the newest version by the write step that
appends them, never by hand.

At the birth of a document the log receives two records: one of the
file and one naming every item born with it.

The way to an item goes into its record, never into the item: why
it changed, what was said, which trials and measurements were made,
which research turned it. Before Claude proposes a change to an
item, it reads the item's history through one command, `/history
<ID>`. A script gathers what the project holds of the item: its
wording today, every record whose subject it is, the records of
other items that mention it, the rows of the archive that mention
it and every other place in the project that cites it. Claude adds
a few sentences of its own on top, marked as such, and nothing is
derived from them. The history is searched by the script, never
loaded whole. What Claude finds is said in its proposal only where
it bears on the change, a direction once tried and dropped above
all. How the command is used is in
[Read the history of an item](../use/read-the-history-of-an-item.md).

The log is the single primary. The commit messages that `/save` and
`/release` draft are derived from it, and so are the release notes:
their sections are derived at a release from the records since the
previous release, one sentence per change with a pointer, and at a
major the minors since the previous major are folded into it. One
thing is never derived: what the reader must do is carried from the
`Action` field of the record into the release notes word for word.

The companion is part of its document. It has no row of its own in
the ledger (the one file that holds a project's state) and is handed
over with the document by the link into git.

A companion written before the log existed kept a table instead.
Such a table is not converted. It moves as it stands to
`<file>.history.archive.md`, immutable from then on, and the log
begins with the next version. Its rows are a record and stay in the
words they were written in. The history of an item is then a search
of both the log and the archive. A Version History table found in
the body of a document or in its companion is a `/check` finding,
settled by that move on the principal's word, project by project.

## Why

Integers denote approval because the scheme follows the group BRD
convention. A scheme where the major number meant a scope change
was considered and rejected: a scope change is a reason for
re-approval anyway, so the approval reading covers it.

A major signs nothing over because an approval says what is done,
not that nothing is left. Its test attests nothing of the model's
behaviour because behaviour is verified by the author's own use
until the forge has a test of it.

The history lives beside the document, not in it, because the body
is the current state and the companion is the record. The way to an
item does not belong in the item.

The log is kept as the single primary so that commit messages and
release notes can be derived from it by mechanism. The release notes
are a log of releases rather than a story because a reader wants to
see plainly what was added, changed and removed. `Action` is never
derived because what the reader must do is written with the change
by the one who made it.

The author field is present from the first record because a log is
never rewritten, and a field it lacks cannot be added to what was
already written.

A history is read through one command, never loaded whole, because
the history of an item is scattered over the log, the archive and
the records of other items. Reading a whole log is forbidden, so
the search used to be done by hand and differently every time. What
is deterministic is given to a script; the judgement is what remains
for the model.

An old table moves to an archive untouched because its rows are a
record and stay in the words they were written in.

## A worked example

A generic companion of an assignment, after its birth and one
later round. The author is the handle the instance gives its
principal; `<handle>` stands in for it here.

```
- 2026-03-02 | 0.1 | <handle> | 20-assignment.md | created
- 2026-03-02 | 0.1 | <handle> | REQ.0010, REQ.0020, DEL.0010 | created
- 2026-03-09 | 0.2 | <handle> | REQ.0020 | changed | the recipients asked for a date instead of a quarter | Action: re-plan the delivery against the date | Was: delivered by the end of the second quarter
- 2026-03-09 | 0.2 | <handle> | DEL.0010 | removed | the deliverable is folded into REQ.0020 | Was: a plan of the delivery, returned before the work starts
```

The first two lines are the birth: one record of the file and one
naming every item born with it, with no reason. The third is a
change of one item in the next round: the reason, what the user
must do, and the wording that ceased to hold, word for word. The
fourth removes an item, and its ID is never used again. The version
`0.2` holds two records, one round and one version.

## See also

- [Versioning and front-matter](../reference/versioning-and-front-matter.md): the fields and the scheme, exactly.
- [History companion](../reference/history-companion.md): the record's shape.
- [Read the history of an item](../use/read-the-history-of-an-item.md): reading one item's history by command.
- [Release a version](../use/release-a-version.md): where the tag of a major is proposed.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
