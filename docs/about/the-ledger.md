---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: caf831c884c0125e
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
is made afresh from the project's other files every time it is
read. This page explains what the ledger is, where the state it
shows really lives, how a script puts it together and why the forge
chose to make it at read time rather than keep it in git. It is for
anyone who works with a project, extends the forge or evaluates it;
the exact tables and their columns are on the page
[Ledger](../reference/ledger.md), and the commands that read the
ledger are on [See where a project stands](../use/see-where-a-project-stands.md).

## What it is

The ledger (`ledger.md` in the project's root) is the single source
of truth for the state of a project. Its tables cover the briefs,
the documents of the chain, the renders, the published files, the
work products, the sources, the research, the dependencies on
another project's documents, the findings of the critic and of the
checks, the challenges, and what waits on the principal (the person
whose thinking is being forged). The kinds of document these tables
are read from are explained on
[Documents and records](documents-and-records.md).

The ledger is made at read time. A script,
`scripts/forge-ledger.py`, builds it from the project's documents
and writes it as a file that git ignores. Nobody writes a row by
hand, and no command writes a row either: every command that
changes the state of a project remakes the ledger by running the
script. The ledger adds nothing of its own. It shows, in one place,
what the other files already say.

Two things follow from this for the reader. The ledger is not on
the remote, since it is not in git. And a layer below the intent
that a project does not have is not missing: it simply gets no row,
and neither the state map nor the checks say anything of it.

A project of kind `library` keeps a reduced ledger: only the tables
Renders, Sources, Dependencies, Research and Waiting on principal.
Its Findings table returns with the first finding of a check.

## How it works

### Where the state lives

What only the ledger once knew now lives in a record or a field
where it belongs, never in a header field of a document. The reason
is that a record can be written on a branch, where a header field
would be fought over. Each kind of state has its place:

- the mining of a brief (how far the intent has absorbed it,
  `pending`, `partial`, `mined` or `dropped`, with a note): a record
  in the history of the intent, with the brief's file as its subject,
  because the mining changes the intent and not the brief; its
  version column says which version of the intent mined it;
- the settling of a finding or of a challenge: a record of kind
  `closed` with the finding or challenge as its subject, in the
  history of the artefact whose version settled it; where no version
  did, or where the check was of the engine, the record stands in the
  history of the intent; a finding so closed is `resolved`, a
  challenge `accepted`;
- a finding or a challenge that is `rejected`, `parked` or
  `obsolete`: the Verdict line of a decision in `decisions.md`, never
  a history record, because all three are the principal's verdict;
- the state of a work product (`current`, `stale` or `by hand`, with
  what it was made from and when): records in the history of its
  specification;
- the date, the origin of the date and the form of a source: fields
  of its entry in `sources/00-INDEX.md`; the ledger registers the
  source and says nothing of what it is for;
- the provenance of a published file: a companion file beside it;
  the ledger computes the state `current` or `stale` by comparing
  the render's generated date with the one the companion names;
- a dependency on another project's documents: the citations of
  that project's directory found in the chain, the indexes, the
  recipes, the work and the research; no field and no version, since
  those documents are maintained by their owner.

A record of state only, such as a mining, a work product's state or
a finding closed, carries the current version of its document and
does not raise it. So a round that only closes findings after a
check, and changes no content, is not a new version. The Date
column of the Documents table comes from the newest content record,
and a state record does not move it. A state record does mark a
render stale, as every raise does.

The history of each versioned document is the append-only companion
`<file>.history.md` beside it, one record per change. The shape of
a record is one line: date, version, author, subject, kind, reason,
and where the record has them an `Action` and a `Was`. The kinds
are `created`, `changed`, `closed`, `removed` and `approved`.

### Waiting on the principal

The section Waiting on principal is a rule, not a hand-kept list.
The script fills it from the documents, one line per matter, each
citing its ID rather than copying its text:

- the open threads, each by its first sentence and its last dated
  paragraph;
- the open questions (`TBC` items) whose owner is the principal;
- the open findings of a critic and the open challenges, which wait
  for the principal's verdict;
- under a heading Parked, the parked findings and challenges with
  the decision that parked them, because no script can judge whether
  the event a parking waits for has come.

The open findings of a check are not listed there. Claude mends
them in a walkthrough (the forge's way of working a list one item
at a time). Free text without an ID has no place in this section,
and an unfinished conversation is saved into its thread of the
intent, never into the ledger. A decision with an unfinished action
becomes a thread.

### The reports

The script also reports what the merged files cannot say by
themselves. The Reports section stands only when there is something
to report, and it knows three things:

- an ID defined twice;
- a closed thread touched by a commit later than the one that
  closed it;
- a thread cited somewhere in the project that has neither a thread
  file nor a `closed` record.

A file the script cannot read is not a crash and not a report. Its
row drops, and the header of the ledger carries a line
`unparsed: <file>:<line>` that names it. The light check reports
it, and a save commits and pushes on, because checks inform and the
save is what keeps work from being lost. The script also tolerates
the shape of files one release back, and it ends with exit code 0.

### The archive

A project that was migrated from the shape in which the ledger was
kept by hand keeps that ledger as `ledger.archive.md`, immutable.
The script reads its Briefs, Work, Findings and Challenges rows for
every item that has no record of the new shape, and a newer record
overrides the archive. A project not yet migrated is read whole
from its hand-kept ledger as the archive; on such a project the
script never writes `ledger.md`. The reason the archive is kept
immutable is not recorded. The migration itself is explained on
[Upgrades and migration](upgrades-and-migration.md).

### The state on the remote

Where the state is wanted on the remote, a release on `main` writes
`renders/state.md` from the output of the ledger script. It is a
tracked render like the README, and it is made only on `main`.
Committing the ledger itself only at a release was ruled out,
because nothing is added to git by force.

## Why

The ledger was the one file present at every collision of two
people, or two windows, on one project: every operation wrote it.
Made at read time, it stops existing as a thing to merge, and merge
requests on the server stop conflicting on it. The price is that
the ledger is not on the remote, which the state render pays for.
How this lets two people work on one project without conflict is
explained on [Working together on one project](working-together.md).

State lives in records and fields, never in a header, so that a
branch can write it. The record stands in the history of the
document that changed.

Waiting on principal is a rule because the hand-kept list differed
from any rule in both directions: it listed what no rule would, and
it missed what a rule would list.

## A worked example

A critic's report in `reviews/` names a finding with the ID
`FND.0120`. From that moment the ledger shows it as open, with the
severity and the category read from the heading of the report:

```
| ID       | Severity   | Category   | State | Source review          | Resolution |
|----------|------------|------------|-------|------------------------|------------|
| FND.0120 | <severity> | <category> | open  | reviews/<report>.md    | —          |
```

The finding is fixed in a layer of the chain, and the version that
fixed it is the one that layer carries at that moment. One line is
appended to the history companion of that layer,
`<layer>.history.md`, the version unchanged, since a record of state
does not raise it:

```
- 2026-03-04 | 0.6 | <author> | FND.0120 | closed | the success criteria named the measure and the date it is read
```

The next time the ledger is made, the script finds this record as
the newest word on `FND.0120` and the row reads:

```
| ID       | Severity   | Category   | State    | Source review          | Resolution                                                     |
|----------|------------|------------|----------|------------------------|----------------------------------------------------------------|
| FND.0120 | <severity> | <category> | resolved | reviews/<report>.md    | the success criteria named the measure and the date it is read |
```

The finding also leaves the section Waiting on principal, because
it is no longer open. Had the principal instead rejected it, the
word would stand as a Verdict line in `decisions.md`, and the row
would read `rejected` with the decision as its resolution.

## See also

- [Ledger](../reference/ledger.md): the tables, their columns and the state words, exactly.
- [See where a project stands](../use/see-where-a-project-stands.md): the map and `/ledger`, which read it.
- [Documents and records](documents-and-records.md): the kinds of document the ledger is made from.
- [Upgrades and migration](upgrades-and-migration.md): the migration that turned a hand-kept ledger into an archive.
- [Working together on one project](working-together.md): why the ledger never conflicts when two people work on one project.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
