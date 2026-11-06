---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 8bc1fdf1b78d702f
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

The ledger is the one file that says where a project stands, and it
is made afresh every time it is read, by a script, from the project's
other files. This page explains what the ledger is, where the state
it shows really lives, and why it is built this way rather than kept
and edited. It is for anyone who uses the forge, extends it or
evaluates it; the exact tables and their columns are on the
[Ledger](../reference/ledger.md) reference page, and the commands
that show the ledger are on [See where a project
stands](../use/see-where-a-project-stands.md).

## What it is

The ledger (`ledger.md` in the project's directory) is the single
source of truth for a project's state. It shows, in one place, the
project's briefs, its documents, its renders, its published files,
its work products, its sources, its research, its dependencies, its
findings, its challenges and what waits on the principal (the person
whose thinking is being forged).

The ledger is made at read time. The script
`scripts/forge-ledger.py` builds it from the project's documents and
writes it as a file that git ignores. It is never kept in git.

Nobody writes a row of the ledger. Every command that changes the
state of a project remakes the ledger by running the script. The
state map of a project, `/ledger`, `/end` and the checks all call
the script rather than reading a stored file.

The ledger holds registration only for resources and dependencies.
What a source or a research note is and is for lives in the
`00-INDEX.md` of its directory, never in the ledger. A document of
another project, cited by path, carries no version in the ledger,
because it is maintained by its owner.

A layer of the chain that a project does not have is not missing: it
gets no row, and neither the state map nor the checks say anything
of it.

## How it works

### Where the state lives

Everything the ledger once knew on its own now lives in a record or
a field of the document the state belongs to. The ledger reads it
from there. The kinds of document it is read from are described on
[Documents and records](documents-and-records.md).

- The mining of a brief, that is how far the intent has absorbed it,
  is a record in the intent's history with the brief's file as its
  subject. It stands in the intent's history because the mining
  changes the intent, not the brief.
- The settling of a finding or a challenge is a `closed` record with
  the finding or the challenge as its subject. The record stands in
  the history of the artefact whose version settled it, or in the
  intent's history where no version did or where the check was of
  the engine. A finding so closed is `resolved`; a challenge so
  closed is `accepted`.
- A finding or a challenge that is `rejected`, `parked` or `obsolete`
  takes that state from the Verdict line of a decision in
  `decisions.md`, never from a history record, because all three are
  the principal's verdict.
- A work product's state is a set of records in the history of its
  specification: the record of a making, the record of a later write
  of the specification, the principal's word that the file is worked
  by hand.
- A source's date, the origin of that date and its form are fields
  of its entry in the sources index.
- The provenance of a published file is a companion beside it; the
  ledger computes from it whether the published file is current or
  stale against the render it was made from.
- The library a project relies on is a citation of that library's
  path in the project's files; there is no field for it.

A record of state only, such as a mining, a work product's state, a
finding closed or a thread closed, carries the document's current
version and does not raise it. So a round that only closes findings
after a check and changes no content is not a new version. Such a
record does not move the Date of a document in the ledger either;
only a record of a content change does.

### Waiting on the principal

What waits on the principal is a rule, not a list anyone keeps. The
section holds:

- the open threads, each shown by its first sentence and its last
  dated paragraph;
- the open questions (TBC items) whose owner is the principal;
- the open findings of a critic and the open challenges, which wait
  for the principal's verdict;
- under a heading of their own, the parked findings and challenges
  with the decision that parked them.

The open findings of a check are not in the section, because Claude
mends them in a walkthrough (a list worked one item per message, the
verdicts written once at the end). The parked items are listed
because no script can judge whether the event a parking waits for
has come. Free text without an ID has no place in the section; an
unfinished conversation is saved into its thread of the intent,
never into the ledger.

### The Reports section

The script reports what the merged files cannot say by themselves.
The Reports section stands only when there is something to report,
and it holds three kinds of line:

- an ID defined twice;
- a closed thread touched by a commit later than the one that closed
  it;
- a thread cited somewhere in the project that has neither a thread
  file nor a `closed` record.

A file the script cannot parse does not break the run. It becomes a
line `unparsed:` in the ledger's header, the row drops aloud, the
light check reports it, and `/save` commits and pushes on, because
checks inform and the save is what does not lose work.

### The archive

A project that was migrated to this shape keeps its former
hand-kept ledger as `ledger.archive.md`, immutable from the
migration. The script reads the archive for every item that has no
record of the new shape; a newer record overrides the archive. How a
project comes to have an archive is on [Upgrades and
migration](upgrades-and-migration.md).

### The state on the remote

The ledger itself is never on the remote. Where the state is wanted
there, a release on `main` writes `renders/state.md` from the
script's output: a tracked render like the README, made only on
`main`. Nothing is added to git by force, so committing the ignored
ledger only at a release is not done.

## Why

The ledger was the one file present at every collision of two
people, or two windows, on one project, because every operation
wrote it. Made at read time, it stops existing as a thing to merge,
and merge requests on the server stop conflicting on it. The price
is that the ledger is not on the remote; the state render at a
release pays it where the state is wanted there. What this means for
two people on one project is on [Working together on one
project](working-together.md).

State lives in records rather than in a header field so that a
branch can write it: a record is appended to the history of the
document that changed, and histories merge as text.

Waiting on the principal is a rule because the hand-kept list it
replaced differed from any rule in both directions: it listed what
no longer waited and missed what did.

A record of state does not raise the version so that closing
findings after a check, which changes no content, does not become a
version of its own.

## A worked example

A check has found something in a project, and its report has filed
the finding. The report gives the finding its ID, its severity and
its category, and the ledger shows it as `open` with that report as
its source. Claude then mends it, and the write that mends it
appends one record to the history of the document that was changed,
with the document's current version and the kind `closed`:

```
- YYYY-MM-DD | 1.2 | <author> | FND.0120 | closed | the heading re-wrapped to the column width
```

The next time the ledger is made, the script finds this record,
takes it as the newest word on the finding, and the finding's row in
the Findings table reads:

```
| FND.0120 | <severity> | conformance | resolved | reviews/YYYY-MM-DD-check-<name>-HHMM-<hash>.md | the heading re-wrapped to the column width |
```

The version `1.2` in the record is the document's version as it
stood; the record did not raise it. Had the principal rejected the
finding instead, no record would have been written: the state
`rejected` would come from the Verdict line of his decision in
`decisions.md`, and the Resolution column would name that decision.

## See also

- [Ledger](../reference/ledger.md): the tables, their columns and
  the state words, exactly.
- [See where a project stands](../use/see-where-a-project-stands.md):
  the map and `/ledger`, which read it.
- [Documents and records](documents-and-records.md): the kinds of
  document the ledger is made from.
- [Upgrades and migration](upgrades-and-migration.md): the migration
  that turned a hand-kept ledger into an archive.
- [Working together on one project](working-together.md): why the
  ledger never conflicts when two people work on one project.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
