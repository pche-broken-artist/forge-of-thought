---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 9ec149fd4d720ddf
inputs:
  - CLAUDE.md#Ledger
  - templates/ledger.md
  - templates/history.md
  - scripts/forge-ledger.py
  - projects/forge/10-intent.md#POS.1600
  - projects/forge/10-intent.md#POS.1610
  - projects/forge/10-intent.md#POS.1620
  - projects/forge/10-intent.md#POS.1630
  - projects/forge/10-intent.md#POS.1640
  - projects/forge/10-intent.md#POS.1650
---

# The ledger, made from the records

The ledger (`ledger.md`) is the one file that says the state of a
project: where each document stands and what is still open. This page
explains why the ledger is made from the other files each time it is
read, and where the state it shows really lives. It is for anyone who
uses the forge, extends it or weighs it. The exact tables and columns
are on [Ledger](../reference/ledger.md).

## What it is

The ledger is the single source of truth for the state of a project.
It shows these things:

- the briefs and how far the intent has absorbed each one;
- the documents of the chain, with version, status and date;
- the renders and the published files;
- the work products and whether each is current;
- the sources, the research and the dependencies on other projects'
  documents;
- the findings of the critic and of the checks, and the challenges;
- what waits on the principal (the person whose thinking is being
  forged).

The ledger is made at read time.
A script, `scripts/forge-ledger.py`, builds it from the project's
documents whenever it is needed.
The file is gitignored, so it is never kept in git.
Nobody writes a row of it by hand.
Every command that changes state makes the ledger afresh through the
script.
The state map and `/ledger` read it: see
[See where a project stands](../use/see-where-a-project-stands.md).

## How it works

### Where the state lives

What the ledger shows is kept in the documents it is made from. The
kinds of document are explained on
[Documents and records](documents-and-records.md). A record is one
line in the history of a versioned document (an append-only companion
file beside it). Each piece of state lives where it belongs:

- The mining of a brief (how far the intent has taken it in): a
  record in the intent's history, with the brief's file as its
  subject.
- A finding or a challenge settled: a record of kind `closed` with the
  finding as its subject. It stands in the history of the artefact
  whose version settled it, or in the intent's history where no
  version did.
- A finding or a challenge rejected, parked or made obsolete: the
  Verdict line of a decision, because all three are the principal's
  verdict.
- The state of a work product (current, stale or by hand): records in
  its specification's history.
- The date, date origin and form of a source: fields of its entry in
  the resource index.
- The provenance of a published file: a companion file beside it. The
  ledger computes from it whether the file is current or stale.
- The version, status and date of a document: its header and the
  newest content record of its history.

A record of state only carries the current version of the document
and does not raise it.
So a round that only closes findings and changes no content is not a
new version.

The script reads these kinds of document: the project file, the
headers of the artefacts, the histories, the decisions, the resource
indexes, the reviews and the challenges, the provenance of the renders
and of the documentation index, the published companions, the work
specifications, the threads and the archive of a migrated project. It
keeps the shape of the ledger template, with the template's own
comments.

### What waits on the principal

Waiting on principal is a rule, not a hand-kept list.
It holds:

- the open threads, each by its first sentence and its last dated
  paragraph;
- the open questions whose owner is the principal;
- the open findings of a critic and the open challenges, which wait
  for his verdict;
- under a heading of its own (Parked), the parked findings and
  challenges with their decision.

The open findings of a check are not on it, because Claude mends them
in a walkthrough (one item at a time, the principal deciding each).
Parked items stand apart, because no script can judge whether the
event a parking waits for has come.
Free text without an ID has no place there.

### The Reports section

The Reports section says what the merged files cannot say by
themselves. It stands only when there is something to say:

- an ID defined twice;
- a closed thread touched by a later commit;
- a thread cited somewhere with neither a thread file nor a `closed`
  record.

A file the script cannot read does not break the run.
It is named on a line `unparsed:` in the ledger's header, and the
script goes on.

### The archive of a migrated project

A project whose ledger was once kept by hand keeps that ledger as
`ledger.archive.md` after its migration. The archive is immutable. It
is read for every item that has no record of the new shape, and a
newer record overrides it. How the migration made it is on
[Upgrades and migration](upgrades-and-migration.md).

### The state on the remote

The price of a ledger outside git is that it is not on the remote.
Where the state is wanted there, a release on `main` writes
`renders/state.md` from the script's output. That file is a tracked
render like the README, made only on `main`. Nothing is added to git
by force.

## Why

Every operation used to write the ledger.
So it was the one file present at every collision of two people, or
two windows, on one project.
Made at read time, it stops being a thing to merge, and merge requests
stop conflicting on it.
How this lets two people work on one project is on
[Working together on one project](working-together.md).

Waiting on principal is a rule because the hand-kept list differed
from any rule in both directions.

A record of state does not raise the version, so that closing findings
without a change of content is not a new version.

## A worked example

A critic run has filed a report in `reviews/` that names a finding,
`FND.0040`. Until something settles it, the ledger shows it as open.
Version 0.3 of a project's assignment then fixes it, and the record
of that round in `20-assignment.history.md` reads:

```
- 2026-01-15 | 0.3 | <author> | FND.0040 | closed | the requirement reworded
```

The record carries the current version, 0.3, and does not raise it.
The next time the ledger is made, the Findings table shows the row:

```
| ID | Severity | Category | State | Source review | Resolution |
|---|---|---|---|---|---|
| FND.0040 | <severity> | <category> | resolved | 2026-01-10-critique-<lens>-0930-<hash>.md | the requirement reworded |
```

The state is `resolved` and the resolution is the record's reason.
The finding also leaves Waiting on principal. Nobody wrote the row:
it comes from the report and the record.

## See also

- [Ledger](../reference/ledger.md): the tables, their columns and the
  state words, exactly.
- [See where a project stands](../use/see-where-a-project-stands.md):
  the map and `/ledger`, which read it.
- [Documents and records](documents-and-records.md): the kinds of
  document the ledger is made from.
- [Upgrades and migration](upgrades-and-migration.md): the migration
  that turned a hand-kept ledger into an archive.
- [Working together on one project](working-together.md): why the
  ledger never conflicts when two people work on one project.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
