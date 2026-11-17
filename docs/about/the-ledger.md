---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: a4a293f4198bc882
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

The ledger is the one file that says where a project stands. This page
explains why it is made afresh every time it is read, and where the
state it shows is really kept. It is for anyone who works in a project,
extends the forge or evaluates it.

## What it is

The ledger (`ledger.md` in the directory of a project) is the single
source of truth for the project's state. It shows:

- the briefs, each with how far the intent has absorbed it
- the documents of the chain below the briefs
- the renders
- the published files
- the work products
- the sources
- the research
- the dependencies (the citations of another project's documents)
- the findings of the critic and of the checks
- the challenges
- what waits on the principal (the person whose thinking is being
  forged)

Every term of the forge on this page has a line in the
[Glossary](../reference/glossary.md). The kinds of document behind the
list are set out in [Documents and records](documents-and-records.md).
The tables of the ledger, their columns and the state words are in
[Ledger](../reference/ledger.md).

The ledger is made at read time. A script (`scripts/forge-ledger.py`)
builds it from the project's documents whenever it is read. The file
is written into the project's directory and ignored by git: it is
never kept in git.

Nobody writes a row of the ledger. Every command that changes state
makes the ledger afresh by the script. An unfinished conversation has
no place in the ledger: it is saved into its thread of the intent.

How the ledger is read in daily work is shown in
[See where a project stands](../use/see-where-a-project-stands.md).

## How it works

### The script reads the documents

The script fills the tables in the shape the ledger's template
(`templates/ledger.md`) gives, and it keeps the template's comments.
Each part of the ledger comes from one kind of document:

- the project file: the header of the ledger (the slug, with the kind
  and the language echoed under it)
- the headers of the artefacts (the documents of the chain): the
  version and the status of the briefs and of the documents
- the histories: the date of a document, the mining of a brief, the
  state of a work product, the closing of a finding or a challenge
- the decisions: their Verdict lines
- the resource indexes: the sources and the research
- the reports in `reviews/` and `challenges/`: the findings and the
  challenges
- the provenance of the renders and of the documentation index: the
  renders
- the published companions: the published files, each current or stale
  against the date its render was generated
- the work specifications: the work products
- the citations of another project's documents (in the chain, the
  indexes, the recipes, the work and the research): the dependencies
- the threads: what waits on the principal
- the archive of a hand-kept ledger: every item without a newer record
  (described below)

```
headers, histories, decisions, indexes, reports,
provenance, companions, specifications, threads
        |
        |   scripts/forge-ledger.py, at every read
        v
    ledger.md            never in git
        |
        |   a release on main
        v
    renders/state.md     tracked in git
```

### Where the state really lives

What only the ledger once knew lives in a record, or in a field of the
document it belongs to. A record is one line appended to the history
of a versioned document (the companion file that holds one record per
change and is never rewritten).

- the mining of a brief (how far the intent has absorbed it): a record
  in the intent's history, with the brief's file as its subject
- the settling of a finding or a challenge: a `closed` record in a
  history, or the Verdict line of a decision
- the state of a work product (`current`, `stale` or `by hand`): a
  record in the history of its specification
- the date and the form of a source: fields of its entry in the index
  of the sources
- the provenance of a published file: its companion
  (`published/<recipe>.md`)

A finding or a challenge is born by its report, with the state `open`.
After that the newest of these decides its state:

| Written as | Where | The ledger shows |
|---|---|---|
| a `closed` record | the history of the artefact whose version settled it, or the intent's history where no version did | `resolved` for a finding, `accepted` for a challenge |
| a Verdict line | a decision of the principal | `rejected`, `parked` or `obsolete` |
| a later report that names a finding as reopened | `reviews/` | `open` again |

### A record of state does not raise the version

A record that records state only is one of these:

- the mining of a brief
- the state of a work product
- the closing of a finding or a challenge
- the closing of a thread

Such a record carries the current version of its document and does not
raise it. It does not move the date the ledger shows for the document:
that date comes from the newest record of a change of content. It does
mark a render stale, as every raise of a version does.

### What waits on the principal

Waiting on the principal is a rule, not a list kept by hand. The
script applies the rule at every read. Each matter gets one line, and
the line cites the matter and never copies it:

- the open threads: those something waits on first, then by priority,
  each with its priority and what waits on it in brackets, its first
  sentence and its last dated paragraph
- the open questions whose owner is the principal
- the open findings of a critic and the open challenges: they wait for
  the principal's verdict
- the parked findings and challenges: under a heading of their own,
  each with its decision

The open findings of a check do not wait on the principal. Claude
mends them in a walkthrough (a list worked with the principal one item
per message). Free text without an ID has no place in the section. A
decision with an unfinished action becomes a thread.

### The reports

The Reports section says what the files, once merged, cannot say by
themselves. The section stands only when there is something to say:

- an ID defined twice
- a closed thread touched by a commit later than the one that closed
  it
- a thread cited somewhere in the project that has neither a thread
  file nor a `closed` record

A file the script cannot read does not break the run. Its row drops,
and the file is named in a line `unparsed: <file>:<line>` of the
ledger's header. A save (`/save`) still commits and pushes.

### The archive of a hand-kept ledger

A project that kept its ledger by hand before its migration keeps that
file as `ledger.archive.md`. It is the ledger as it stood at the
migration, and it is immutable. For every item that has no record of
the new shape, the script reads the archive's rows of these tables:

- Briefs
- Work
- Findings
- Challenges

A newer record overrides the archive. A project not yet migrated is
read whole from its hand-kept ledger, and the script prints the result
instead of writing `ledger.md`. The migration is described in
[Upgrades and migration](upgrades-and-migration.md).

### The state on the remote

The ledger is not on the remote (the copy of the repository on the
server). Where the state is wanted there, a release on `main` writes
`renders/state.md` from the script's output. That file is a tracked
render like the README. It is made only on `main`.

## Why

**Made at read time, never in git.** A ledger kept as a file in git is
written by every operation. That made it the one file present at every
collision of two people, or of two windows, on one project. Made at
read time, the ledger stops existing as a thing to merge, and merge
requests on the server stop conflicting on it. What this gives two
people on one project is told in
[Working together on one project](working-together.md).

**The price.** The ledger is not on the remote. The render of the
state pays that price where the state is wanted there. The ledger is
ignored by git, and nothing is added to git by force. Committing the
ledger itself only at a release is therefore ruled out.

**Records, not header fields.** What only the ledger knew lives in
records and never in a header field. The purpose is that a branch can
write it. A record stands in the history of the document that changed.
Where no history fits, the state stands in the document it belongs to:
the index entry of a source, the companion of a published file or the
principal's decision.

**No version for state alone.** A record of state does not raise the
version. A round that only closes findings after a check and changes
no content is therefore not a version.

**A rule for what waits.** A hand-kept list of what waits differed
from any rule in both directions. The parked findings and challenges
stand under a heading of their own. No script can judge whether the
event a parking waits for has come.

**A file that cannot be read.** Such a file is named, and the run goes
on. Checks inform and do not block, and a save is what does not lose
work.

**The archive.** The archive is read for every item without a newer
record. Why it is kept immutable: the reason is not recorded.

## A worked example

A critic's report names a finding. No record settles it yet, and the
ledger shows it open:

```
| ID | Severity | Category | State | Source review | Resolution |
|---|---|---|---|---|---|
| FND.0010 | <severity> | <category> | open | <report>.md | — |
```

A round on the intent then mends what the finding named, at version
0.4. The intent is the artefact whose version settled the finding. The
closing record is therefore one line appended to the intent's history:

```
- YYYY-MM-DD | 0.4 | <author> | FND.0010 | closed | the term is defined where it is first used
```

The fields are the date, the version, the author, the subject, the
kind and the reason. The record carries 0.4, the version the intent
already has, and does not raise it.

At the next read the script finds the record, and the ledger shows:

```
| ID | Severity | Category | State | Source review | Resolution |
|---|---|---|---|---|---|
| FND.0010 | <severity> | <category> | resolved | <report>.md | the term is defined where it is first used |
```

Nobody edited the row. The state `resolved` is how a `closed` record
reads for a finding, and the Resolution is the record's reason. A
finding the principal rejects gets no record in a history: the Verdict
line of the decision gives the state `rejected`, and the Resolution
names the decision.

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

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
