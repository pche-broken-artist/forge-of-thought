---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 8252460042176486
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

The ledger is the single source of truth for the state of a project:
one file, `ledger.md`, made at read time by a script from the
project's own documents and never kept in git. This page explains
what the ledger holds, where the state it shows really lives, and why
it is made afresh instead of being written. It is for anyone who uses
the forge, extends it or evaluates it. The tables, their columns and
the state words, exactly, are the [Ledger](../reference/ledger.md)
reference page's; how to read the state of a project through the
state map and `/ledger` is [See where a project
stands](../use/see-where-a-project-stands.md).

## What it is

The ledger is a report of state, not a record of it. A script,
`scripts/forge-ledger.py`, builds it from the project's documents and
writes it as a file git ignores. Nobody writes a row. Every command
that changes state remakes the ledger by the script. The state map of
a project, `/ledger`, `/end` and the checks call the same script.

The principal is the person whose thinking is being forged. The ledger
shows him, and Claude, where the project stands in one place:

- its briefs, each with how far the intent has absorbed it;
- its documents, the layers of the chain below the briefs, each with
  its version, its status and its date;
- its renders, with the recipe and the inputs each was made from;
- its published files, each current or stale against its render;
- its work products, each current, stale or by hand;
- its sources and its research, by registration only;
- its dependencies, the documents of another project it cites;
- the findings of the critics and the checks, and the challenges,
  each with its state and its resolution;
- what waits on the principal;
- what the script found that the files cannot say by themselves.

The shape of the ledger is the template `templates/ledger.md`: it
owns what each table holds and which record or field each column is
read from, and the script keeps the template's comments in the
ledger it writes. A library, a project that holds shared material
and no chain, keeps fewer tables: Renders, Sources, Dependencies,
Research and Waiting on principal; its Findings table returns with a
check's first finding.

Resources and dependencies are registration only. What a source is
and is for lives in the index of its directory, `00-INDEX.md`, never
in the ledger. A document of another project, cited by path, carries
no version in the ledger, because it is maintained by its owner.

A layer below the intent that a project does not have is not missing:
it gets no row, and the state map and the checks say nothing of it.
The kinds of document the ledger is made from, and what each kind is,
are [Documents and records](documents-and-records.md).

## How it works

### The state lives in records and fields

What only the ledger once knew now lives in records and fields, each
where it belongs, and the script reads it from there. A record stands
in the history of the document that changed. The history is the
append-only companion of a versioned document, one line per change,
in the shape `templates/history.md` owns.

- The mining of a brief, how far the intent has absorbed it, is a
  record in the intent's history with the brief's file as its
  subject: `mined: pending | partial | mined | dropped`, with a note.
  It stands in the intent's history because the mining changes the
  intent and not the brief. Its version column says which version
  of the intent mined it.
- The settling of a finding or a challenge is a record of kind
  `closed` with the finding or the challenge as its subject. It
  stands in the history of the artefact whose version settled it, or
  in the intent's history where no version did or where the check was
  of the engine. A closed finding reads as resolved, a closed
  challenge as accepted, the record's reason as the resolution.
- `rejected`, `parked` and `obsolete` are never a record of a
  history. They come from the Verdict line of a decision in
  `decisions.md`, because all three are the principal's verdict.
- A work product's state is a record in its specification's history:
  the making writes `state: current; made <date> from <the inputs
  with their versions>`; a write of the specification after a making
  writes `state: stale`; the principal's word writes `state: by
  hand`.
- A source's date, the origin of that date and its form are fields of
  its entry in `sources/00-INDEX.md`.
- The provenance of a published file is a companion beside it,
  `published/<recipe>.md`; the state current or stale is computed
  against the render's generated date.
- The dependencies are the citations of another project's documents
  found in the chain, the indexes, the recipes, the work and the
  research: no field, no row anybody writes.

A record of state only, a mining, a work product's state, a finding
closed, a thread closed, carries the current version of its document
and does not raise it. So a round that only closes findings after a
check and changes no content is not a new version. A state record
marks a render stale, as every raise of the version does. In the
Documents table the date of a document comes from its newest content
record; a state record does not move it.

A record is read in the history of the document, not in its header,
so that a branch can write it.

### Waiting on the principal is a rule

The section Waiting on principal is not a list anyone keeps. It is
made by a rule, one line per matter, each citing an ID and never
copying the matter:

- the open threads, each by its first sentence and its last dated
  paragraph;
- the open questions (`TBC`) whose owner is the principal;
- the open findings of a critic and the open challenges, which wait
  for his verdict;
- under a heading Parked of its own, the parked findings and
  challenges with their decision.

The open findings of a check are not there, because Claude mends
them in a walkthrough (the method by which a list of items is
decided one item at a time). The parked ones stand apart because no
script can judge whether the event a parking waits for has come. A
decision with an unfinished action becomes a thread. Free text
without an ID has no place in the section. An unfinished
conversation is saved into its thread of the intent, never into the
ledger.

### The Reports section

The script reports what the merged files cannot say by themselves.
The section stands only when there is something to report:

- an ID defined twice;
- a closed thread touched by a commit later than the one that closed
  it;
- a thread cited anywhere in the project that has neither a file nor
  a `closed` record.

The light check compares nothing with the ledger and reports what
the script finds.

A file the script cannot parse is not a crash and not a row. The row
drops aloud: the ledger's header carries a line `unparsed:` naming
the file and the line, the script ends with exit code 0, and the
light check reports it. A save commits and pushes on, because checks
inform and the save is what does not lose work. The script tolerates
the shape of one release back.

### The archive of a migrated project

A project that was brought to the present shape by a migration keeps
its hand-kept ledger as `ledger.archive.md`, immutable from then on.
The script reads the archive's Briefs, Work, Findings and Challenges
rows for every item that has no record of the new shape, and a newer
record overrides it. A project not yet migrated is read whole from
its hand-kept ledger as the archive, and its `ledger.md` is never
written. The migration itself is [Upgrades and
migration](upgrades-and-migration.md).

### The state on the remote

The ledger is not on the remote; that is the price of making it at
read time. Where the state is wanted there, a release on `main`
writes `renders/state.md` from the script's output: a tracked render
like the README, made only on `main`. Nothing is added to git by
force. So committing the ledger only at a release is out.

### Where the script writes

The script writes `ledger.md` only on a project of the current shape
whose ledger is out of git's index. On a project of the shape before
the migration, under git or not, and wherever the ledger is tracked,
it prints to standard output or to a path given with `--out`; the
dry run of a real project goes to `tmp/`. It needs Python 3.8 or
newer and git on the path.

## Why

The ledger was the one file present at every collision of two people
or two windows on one project, because every operation writes it.
Made at read time, it stops existing as a thing to merge, and merge
requests on the server stop conflicting on it. How two people share
one project without the ledger in their way is [Working together on
one project](working-together.md).

The state lives in records so that nothing of it needs a header
field or a row, and so that a branch can write it.

Waiting on principal is a rule because the hand-kept list differed
from any rule in both directions.

The Reports section exists because a merge of text cannot see an ID
given twice, a closed thread reopened by a later commit or a thread
cited with nothing behind it; only a reading of the whole project
can.

The reason the archive of a hand-kept ledger is kept immutable
rather than rewritten is not recorded.

## A worked example

A critic found that a heading of the assignment did not match its
template. The finding was born by its report in `reviews/` and stood
in the ledger as open. The principal accepted it in a walkthrough,
the assignment was corrected, and the write appended one record to
the assignment's history, with the finding as its subject and the
current version of the assignment, which the record does not raise:

```
- 2026-03-04 | 1.2 | <author> | FND.0120 | closed | heading renamed to match the template
```

The next run of the script reads that record as the newest word on
the finding and yields this row of the Findings table, the ID, the
severity, the category and the source review taken from the report
that gave birth to it, the state and the resolution from the record:

| ID | Severity | Category | State | Source review | Resolution |
|---|---|---|---|---|---|
| FND.0120 | <severity> | <category> | resolved | <the report in reviews/> | heading renamed to match the template |

Nobody wrote the row. Had the principal rejected or parked the
finding instead, the row would read `rejected` or `parked` from the
Verdict line of his decision, and the parked one would stand under
Parked in Waiting on principal with that decision beside it.

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

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
