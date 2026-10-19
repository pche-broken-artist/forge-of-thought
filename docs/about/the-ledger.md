---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: d347fa31309bab32
inputs:
  - CLAUDE.md#Ledger
  - templates/ledger.md
  - templates/history.md
  - scripts/forge-ledger.py
  - projects/forge/10-intent.md#POS.1600
  - projects/forge/10-intent.md#POS.1610
  - projects/forge/10-intent.md#POS.1620
  - projects/forge/10-intent.md#POS.1630
  - projects/forge/10-intent.md#POS.1650
---

# The ledger, made from the records

The ledger is the one file that says where a project stands, and a
script makes it at read time from the project's other documents. This
page explains what the ledger holds, where the state it shows really
lives and why nobody keeps it by hand. It is for anyone who uses the
forge, extends it or weighs it. The exact tables, their columns and
their state words are on [Ledger](../reference/ledger.md).

## What it is

`ledger.md` is the single source of truth for the state of a project.
It has one table for each of these:

- briefs
- documents (the layers of the chain below the briefs)
- renders
- published files
- work products
- sources
- research
- dependencies
- findings
- challenges

Below the tables stands what waits on the principal (the person whose
thinking is forged in the project, and its final authority). A
section of reports follows where there is something to report.

The ledger is made at read time and is never kept in git. The script
`scripts/forge-ledger.py` builds it from the project's documents and
writes it as a gitignored file. Nobody writes a row. Every command
that changes state makes the ledger afresh by the script. The state
map, `/ledger`, `/end` and the checks call the same script, so each of
them reads a ledger made from the files as they are now. How you read
it is on [See where a project stands](../use/see-where-a-project-stands.md).

Sources, research and dependencies are registration only in the
ledger. What a source or a research note is and what it is for lives
in the `00-INDEX.md` of its directory. A library document is cited by
its path and carries no version.

A project of the kind `library` has a smaller ledger. It keeps only
Renders, Sources, Dependencies, Research and Waiting on principal. Its
Findings table returns with the first finding of a check.

## How it works

### The documents it is made from

The script reads the project's documents of several kinds and takes
each column from one record or field. The kinds are described on
[Documents and records](documents-and-records.md). In outline:

- the project file: the ledger's header, with the slug, the day the
  ledger was made, and the kind and language as read from that file
- the headers of the artefacts: the version and status of the briefs
  and the layers
- the histories: the date of a document, the mining of a brief, the
  state of a work product, the closing of a finding or a challenge
- the decisions: their Verdict lines
- the resource indexes: Sources and Research
- the reports of the reviewers in `reviews/` and `challenges/`: the
  findings and the challenges
- the provenance front-matter of the renders and of the documentation
  index: Renders
- the companions of the published files: Published
- the work specifications: Work
- the threads (the open matters of the project, one file each): what
  waits on the principal
- `ledger.archive.md`, where the project has one

### Where the state really lives

What only a hand-kept ledger once knew now lives in records and
fields, each where it belongs. A record is one line of the
append-only history beside a versioned document. A record stands in
the history of the document that changed, never in a header field.
The reason recorded is that a branch can then write it.

- The mining of a brief (how far the intent has absorbed it): a record
  in the intent's history with the brief's file as its subject. The
  reason is that the mining changes the intent and not the brief.
- The settling of a finding or a challenge: a record of kind `closed`
  with the finding or challenge as its subject. It stands in the
  history of the artefact whose version settled it. It stands in the
  intent's history where no version settled it or where the check was
  of the engine. A finding so closed reads as `resolved`, a challenge
  as `accepted`.
- A finding or a challenge `rejected`, `parked` or `obsolete`: the
  Verdict line of a decision. The reason is that all three are the
  principal's verdict.
- A work product's state (`current`, `stale` or `by hand`): records in
  its specification's history.
- A source's date, the origin of that date and its form: fields of its
  entry in `sources/00-INDEX.md`.
- The libraries a project relies on: the citations of
  `projects/lib-*/` found anywhere in the project. No field holds
  them.
- The provenance of a published file: a companion beside it. Whether
  the file is `current` or `stale` is computed against the render's
  generated date.

A record of state only carries the current version and does not
raise it. Such records are a mining, a work product's state, a
finding closed and a thread closed. The reason is that a round which
only closes findings after a check, and changes no content, is then
not a version. A state record still marks a render stale, as every
raise of a version does. Because a state record does not move it, the
date of a document in the ledger comes from the newest record that
changed content.

### What waits on the principal

Waiting on principal is a rule, not a list someone keeps. The script
applies it to the files:

- the open threads, each by its first sentence and its last dated
  paragraph
- the open questions (TBC items) whose owner is the principal
- the open findings of a critic, which wait for his verdict
- the open challenges, which wait for his verdict as well
- under a heading of its own, Parked: the parked findings and
  challenges with their decision

The open findings of a check are not on this list. Claude mends them
in a walkthrough (one item per message, each closed by the
principal's verdict). The parked ones stand apart because no script
can judge whether the event a parking waits for has come. A decision
whose action is unfinished becomes a thread. Free text without an ID
has no place under Waiting. An unfinished conversation is saved into
its thread, never into the ledger.

### What the files cannot say

The Reports section says what the files cannot say by themselves. It
stands only when there is something in it:

- an ID defined twice
- a closed thread touched by a later commit
- a thread cited with neither a thread file nor a `closed` record

A file the script cannot read does not break the run. The file is
named in the ledger's header as a line `unparsed: <file>:<line>`, and
its row drops. The light check reports it. `/save` commits and pushes
on, because checks inform and the save is what does not lose work.

### The archive

A project migrated from a hand-kept ledger keeps that ledger as
`ledger.archive.md`. The archive is immutable. Its Briefs, Work,
Findings and Challenges rows are read for every item that has no
record of the new shape, and a newer record overrides them. A project
not yet migrated is read whole from its hand-kept ledger as the
archive. How the migration works is on
[Upgrades and migration](upgrades-and-migration.md).

### The state on the remote

Because the ledger is not in git, it is not on the remote. Where the
state is wanted there, a release on `main` writes `renders/state.md`
from the script's output. It is a tracked render like the README and
is made only on `main`. Nothing is added to git by force, so the
ledger itself is never committed, not even at a release.

## Why

- The ledger was the one file present at every collision of two
  people or two windows on one project. The reason is that every
  operation wrote it.
- Made at read time, it stops being a thing to merge. Merge requests
  on the server stop conflicting on it.
- The hand-kept list of what waits on the principal differed from any
  rule in both directions. A rule applied by the script replaces it.
- The price is that the ledger is not on the remote. The state render
  of a release answers that where it is wanted.

## A worked example

A finding of a critic is born in its report, and the ledger shows it
open. The report's file name and the finding's heading give the row:

```
reviews/2026-01-10-critique-<lens>-0930-a1b2.md

| ID       | Severity   | Category   | State | Source review                               | Resolution |
|----------|------------|------------|-------|---------------------------------------------|------------|
| FND.0120 | <severity> | <category> | open  | 2026-01-10-critique-<lens>-0930-a1b2.md     | —          |
```

The principal accepts the finding, and the intent at version 1.2 is
changed to settle it. The same write appends one closing record to
`10-intent.history.md`. The record carries the current version and
does not raise it:

```
- 2026-01-12 | 1.2 | <author> | FND.0120 | closed | the term is defined at its first use
```

The next command that changes state makes the ledger afresh. The
script finds the `closed` record as the newest word on the finding,
and the row now reads:

```
| ID       | Severity   | Category   | State    | Source review                               | Resolution                           |
|----------|------------|------------|----------|---------------------------------------------|--------------------------------------|
| FND.0120 | <severity> | <category> | resolved | 2026-01-10-critique-<lens>-0930-a1b2.md     | the term is defined at its first use |
```

The finding also leaves Waiting on principal, since it is no longer
open. Nobody edited the row: the record is where the state lives.

## See also

- [Ledger](../reference/ledger.md): the tables, their columns and the
  state words, exactly.
- [See where a project stands](../use/see-where-a-project-stands.md):
  the map and `/ledger`, which read it.
- [Documents and records](documents-and-records.md): the kinds of
  document the ledger is made from.
- [Upgrades and migration](upgrades-and-migration.md): the migration
  that turned a hand-kept ledger into an archive.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
