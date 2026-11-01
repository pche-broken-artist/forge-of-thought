---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 99c38af3193879a6
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

The ledger is the one file that says where a project stands: its
briefs, its documents, its renders and everything else that has a
state. This page explains why the ledger is made afresh from the
other files each time it is read, and where the state it shows
really lives. It is for anyone who uses the forge, extends it or
weighs it.

## What it is

The ledger (`ledger.md` in a project's root) is the single source of
truth for a project's state. It is not written by hand. A script,
`scripts/forge-ledger.py`, builds it from the project's documents at
the moment it is read. The file is gitignored, so it is never kept in
git. The kinds of document it is made from are described in
[Documents and records](documents-and-records.md).

The ledger holds one table for each kind of state:

- Briefs: each brief and how far the intent has absorbed it.
- Documents: each layer of the chain below the briefs, with its
  version, status and date.
- Renders: each generated output and what it was made from.
- Published: each designed file and whether it is current or stale.
- Work: each work product and its state.
- Sources: the registered external inputs.
- Dependencies: the documents of other projects that this project
  cites.
- Research: the research notes.
- Findings: the findings of the critic and of the checks.
- Challenges: the challenges of the challengers.
- Waiting on principal: what waits for a decision of the principal
  (the person whose thinking is being forged).
- Reports: what the merged files cannot say by themselves.

The exact tables, their columns and their state words are in
[Ledger](../reference/ledger.md). A library project keeps only some
of these tables: Renders, Sources, Dependencies, Research and Waiting
on principal. Its Findings table returns with a check's first
finding.

Nobody writes a row of the ledger. Every command that changes state
makes the ledger afresh by the script. The state map and `/ledger`
read it, as [See where a project stands](../use/see-where-a-project-stands.md)
describes.

## How it works

### Where the state really lives

Whatever only the ledger once knew now lives in the file it belongs
to. Most of it is a record: one line in the history of a versioned
document (its append-only companion `<file>.history.md`). The rest
is a field of an index entry, a companion of a published file or the
verdict line of a decision.

- The mining of a brief: a record in the intent's history, with the
  brief's file as its subject. It stands in the intent's history
  because the mining changes the intent and not the brief.
- A finding or a challenge settled: a record of kind `closed` with
  the finding or challenge as its subject. It stands in the history
  of the artefact whose version settled it. Where no version settled
  it, or the check was of the engine, it stands in the intent's
  history.
- A finding or a challenge rejected, parked or made obsolete: the
  verdict line of a decision. All three are the principal's verdict,
  so none of them is a record of a history.
- A work product's state: a record in its specification's history
  (current, stale or by hand).
- A source's date, origin and form: fields of its entry in
  `sources/00-INDEX.md`.
- The provenance of a published file: a companion beside it. Whether
  the file is current or stale is computed from it.
- The libraries a project relies on: its citations of their paths,
  with no field of their own.

A record of state only carries the current version and does not
raise it. Such a record is a mining, a work product's state, a
finding closed or a thread closed. So a round that only closes
findings after a check and changes no content is not a new version.
A state record still marks a render stale, as every raise does. The
Documents table takes its date from the newest content record, so a
state record does not move that date either.

### What the script reads

The script reads these kinds of document:

- the project file, for the header;
- the headers of the artefacts, for Briefs and Documents;
- the histories, for the date of a document, the mining of a brief,
  the state of a work product and the closing of a finding or a
  challenge;
- the decisions, for their verdict lines;
- the resource indexes, for Sources and Research;
- the reviews and the challenges, for Findings and Challenges;
- the provenance of the renders and of the documentation index, for
  Renders;
- the published companions, for Published;
- the work specifications, for Work;
- the threads (the open matters of the intent, one file each), for
  Waiting on principal;
- the archive `ledger.archive.md`, described below.

A file the script cannot parse does not break the run. It is named on
a line `unparsed:` in the ledger's header, and its row drops aloud.
The light check reports it, and `/save` commits and pushes on.
Because checks inform and do not block, the save goes ahead. The save
is what keeps work from being lost.

### Waiting on principal is a rule

What waits on the principal is not a hand-kept list. It follows a
rule:

- the open threads, each by its first sentence and its last dated
  paragraph;
- the open questions (`TBC` items) whose owner is the principal;
- the open findings of a critic and the open challenges, which wait
  for his verdict;
- under a heading Parked of its own, the parked findings and
  challenges, each with its decision.

The open findings of a check are not on the list. Claude (the model
that works with the principal) mends them in a walkthrough (a list of
items worked one per message, the principal giving his verdict on
each). Parked items stand apart. Because no script can judge whether
the event a parking waits for has come, they are not mixed with the
open ones. Free text without an ID has no place in the list. A
decision with an unfinished action becomes a thread instead. An
unfinished conversation is saved into its thread, never into the
ledger.

### Reports

The Reports section says what the merged files cannot say by
themselves. It stands only when there is something to report:

- an ID defined twice (two items with one ID);
- a closed thread touched by a commit later than the one that closed
  it;
- a thread cited anywhere in the project that has neither a thread
  file nor a `closed` record.

### The archive of a migrated project

A project that kept its ledger by hand before it was migrated keeps
that ledger as `ledger.archive.md`. The archive is immutable. Its
Briefs, Work, Findings and Challenges rows are read for every item
that has no record of the new shape, and a newer record overrides
them. A project not yet migrated is read whole from its hand-kept
ledger as the archive, and the script never writes over it. The
migration itself is described in
[Upgrades and migration](upgrades-and-migration.md).

### The state on the remote

Because the ledger is not in git, it is not on the remote. Where the
state is wanted there, a release on `main` writes it as
`renders/state.md` from the script's output. That file is a tracked
render, like the README, and it is made only on `main`. Nothing is
added to git by force, so the ledger itself is never committed, not
even at a release.

## Why

The ledger was the one file present at every collision of two people
or two windows on one project. Every operation wrote it, so every
collision met it. Made at read time, it stops being a thing to merge,
and merge requests on the server stop conflicting on it. How this
lets two people work on one project is explained in
[Working together on one project](working-together.md).

What only the ledger knew had to move somewhere once the ledger left
git. It moved into records, which stand in the history of the
document that changed.

Waiting on principal became a rule because the hand-kept list differed
from any rule in both directions. It held what no rule would hold, and
it missed what a rule would hold.

The price is that the ledger is not on the remote. The state render
written at a release answers that where it matters.

## A worked example

A critic files a report that names a finding. The ledger shows the
finding as open. Later a new version of the intent mends what the
finding raised, and the history of the intent gains one closing
record, generic in its shape:

```
- YYYY-MM-DD | 1.3 | <author> | FND.0010 | closed | the ambiguous wording replaced by a testable one
```

The record carries the intent's current version, 1.3, and does not
raise it. The next time the ledger is made, the Findings table shows:

```
| ID | Severity | Category | State | Source review | Resolution |
|---|---|---|---|---|---|
| FND.0010 | <severity> | <category> | resolved | reviews/YYYY-MM-DD-critique-<lens>-HHMM-<hash>.md | the ambiguous wording replaced by a testable one |
```

The finding has also left Waiting on principal, because it is no
longer open. Had the principal rejected the finding instead, no
record would be written. A decision's verdict line would carry
`rejected`, and the row would read from it.

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

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
