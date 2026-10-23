---
generated: 2026-10-23
version: 5.34
made: derived
inputs-hash: 9176eb50fd55d5a6
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

The ledger is the one file that says where a project stands. A
script makes it afresh from the project's other files each time it
is wanted. This page explains why it is made that way and where the
state it shows really lives. It is for anyone who uses the forge,
extends it or judges it. The tables, their columns and the state
words, exactly, are on [Ledger](../reference/ledger.md).

## What it is

The ledger (`ledger.md` in a project's root) is the single source of
truth for the state of a project. It shows the following:

- the briefs, and how far the intent has absorbed each
- the documents of the chain, with version, status and date
- the renders and the published files made from them
- the work products and whether each is current
- the sources, the research notes and the dependencies on other
  projects (registration only)
- the findings of the critic and of the checks, and the challenges
- what waits on the principal (the person whose thinking is being
  forged)

The ledger is made at read time. The script
`scripts/forge-ledger.py` builds it from the project's documents and
writes it as a file git ignores. It is never kept in git.

Nobody writes a row of the ledger, by hand or by a command. Every
command that changes state makes the ledger again through the
script. The state map, `/ledger`, `/end` and the checks call the same
script. How you read the state is on
[See where a project stands](../use/see-where-a-project-stands.md).

A layer of the chain that a project does not have gets no row. It is
not missing.

## How it works

### What the script reads

The script reads the kinds of document a project already keeps:

- the project file, for the ledger's header
- the headers of the artefacts, for the briefs and the documents
- the histories, for the date of a document, the mining of a brief,
  the state of a work product and the closing of a finding or a
  challenge
- the decisions, for their Verdict lines
- the resource indexes, for the sources and the research
- the review and challenge reports, for the findings and the
  challenges
- the provenance of the renders and of the documentation index
- the companions of the published files
- the work specifications
- the threads, for what waits on the principal
- `ledger.archive.md`, where a project has one

Dependencies are found as citations of another project's documents
in the chain, the indexes, the recipes, the work and the research.
What these kinds of document are is on
[Documents and records](./documents-and-records.md).

### Where the state lives

What only a hand-kept ledger once knew now lives in a record or a
field where it belongs. A record is one line appended to the history
of the document that changed. The places are these:

- The mining of a brief: a record in the intent's history, with the
  brief's file as its subject. It stands there because the mining
  changes the intent, not the brief.
- A finding or a challenge settled: a record of kind `closed`, in
  the history of the artefact whose version settled it, or of the
  intent where no version did.
- A finding or a challenge rejected, parked or obsolete: the Verdict
  line of a decision. These three are the principal's verdict, so
  they are never a record of a history.
- The state of a work product: records in its specification's
  history (current, stale or by hand).
- The date, origin and form of a source: fields of its entry in the
  sources index.
- The provenance of a published file: a companion file beside it.
  Whether the file is current or stale is computed.

A record of state only carries the current version and does not
raise it. A round that only closes findings and changes no content
is therefore not a new version. Such a record does not move a
document's date in the ledger either. It does mark a render stale, as
every raise does.

### Waiting on the principal

What waits on the principal is a rule, not a list someone keeps. The
script applies it to the following:

- the open threads, each by its first sentence and its last dated
  paragraph
- the open questions whose owner is the principal
- the open findings of a critic and the open challenges, which wait
  for his verdict
- under a heading of its own, the parked findings and challenges
  with their decision

The open findings of a check are not on it, because Claude mends
those in a walkthrough (a list worked one item per message, each
closed by the principal's verdict). The parked ones stand apart
because no script can judge whether the event a parking waits for
has come. Free text without an ID has no place there.

### Reports and unreadable files

The Reports section says what the merged files cannot say by
themselves. It stands only when there is something to report:

- an ID defined twice
- a closed thread touched by a commit later than the one that closed
  it
- a thread cited somewhere with neither a thread file nor a closing
  record

A file the script cannot parse does not break the run. It is named
on a line `unparsed:` in the ledger's header, its row drops, and the
script still ends without an error. The light check reports such a
file, and a save commits and pushes on.

### The archive

A project migrated from the time of the hand-kept ledger keeps that
ledger as `ledger.archive.md`, immutable. The script reads it for
every brief, work product, finding and challenge that has no record
of the new shape. A newer record overrides it. How the migration
does this is on [Upgrades and migration](./upgrades-and-migration.md).

### State on the remote

The price of the rule is that the ledger is not on the remote. Where
the state is wanted there, a release on `main` writes
`renders/state.md` from the script's output. It is a tracked render,
like the README, made only on `main`.

## Why

The ledger is made at read time because it was the one file present
at every collision of two people, or two windows, on one project.
Every operation wrote it. Made at read time, it stops being a thing
to merge, and merge requests on the server stop conflicting on it.
How two people work on one project is on
[Working together on one project](./working-together.md).

Waiting on the principal is a rule because the hand-kept list
differed from any rule in both directions.

Committing the ledger only at a release is not done, because nothing
is added to git by force.

## A worked example

A critic's report names a finding. In the ledger it is born open. The
principal then settles it by changing an artefact, and the change is
written with a closing record in that artefact's history:

```
- YYYY-MM-DD | 0.4 | <author> | FND.0010 | closed | the term defined at its first use
```

The record carries the artefact's current version, 0.4, and does
not raise it. The next time the script runs, the finding's row in the
Findings table reads:

| ID | Severity | Category | State | Source review | Resolution |
|---|---|---|---|---|---|
| FND.0010 | `<severity>` | `<category>` | resolved | `<the report that first named it>` | the term defined at its first use |

Had the principal rejected the finding instead, a decision's Verdict
line would have set the state to `rejected`, with the decision as
the resolution.

## See also

- [Ledger](../reference/ledger.md): the tables, their columns and the
  state words, exactly.
- [See where a project stands](../use/see-where-a-project-stands.md):
  the map and `/ledger`, which read it.
- [Documents and records](./documents-and-records.md): the kinds of
  document the ledger is made from.
- [Upgrades and migration](./upgrades-and-migration.md): the
  migration that turned a hand-kept ledger into an archive.
- [Working together on one project](./working-together.md): why the
  ledger never conflicts when two people work on one project.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-23 for version 5.34 from the files the
front-matter names; never edited by hand.
