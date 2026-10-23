---
generated: 2026-10-23
version: 5.34
made: mirrored
inputs-hash: e2be9bf978c4b643
inputs:
  - templates/ledger.md
  - CLAUDE.md#Ledger
  - scripts/forge-ledger.py
---

# Ledger

This page lists the shape of the ledger exactly: its header, its tables, the columns of each table, the place each column is read from, the state words and the reports. It is for the reader who uses the ledger and for the extender who changes how it is made. The ledger is the file `ledger.md` of a project, the single source of truth for the project's state. It is made at read time by `python scripts/forge-ledger.py <slug>` and is never kept in git. Nobody writes a row by hand.

## The header

The header is front-matter. It carries these lines:

| Line | Read from |
|---|---|
| `project` | the slug given to the script |
| `updated` | the day the ledger was made |
| `kind` | the project file, echoed as read |
| `language` | the project file, echoed as read |
| `shape` | only for a project of the shape before the migration: a line saying the ledger is read from the hand-kept ledger as the archive |
| `unparsed: <file>:<line> (<what>)` | one line for each file the script could not parse; such a file is a line in the header, never a row |

The title line reads `Ledger` followed by the slug.

## The tables

A project of kind `thought` keeps every table. Each table stands under a heading of its own, followed by the template's comment.

### Briefs

One row per brief (`00-brief.md` and `00-brief-<name>.md`).

| Column | Read from |
|---|---|
| File | the brief's file name |
| Version | the brief's header |
| Status | the brief's header |
| Mined | the newest mining record of the intent's history; `pending` until one exists |
| Note | the same record; `—` until one exists |

Mined holds one of `pending`, `partial`, `mined`, `dropped`. The word says how far the intent has absorbed the brief. For `partial` the Note says what remains. For `dropped` the Note names the rejected direction.

### Documents

One row per layer of the chain below the briefs. A layer the project does not have gets no row.

| Column | Read from |
|---|---|
| File | the layer's file name |
| Version | the header |
| Status | the header |
| Date | the newest content record of the layer's history; a state record does not move it |

### Renders

One row per render file, read from the render's own provenance front-matter. A translation cites the primary render.

| Column | Read from |
|---|---|
| Render | the render file |
| Audience | the audience of its recipe |
| Recipe | the provenance |
| Inputs | the provenance |
| Generated | the provenance |

The documentation index has a row of its own, read from its own front-matter. Its Recipe is "none: derived by scripts/docs-index.py". Its Inputs are the documentation map and the version of the intent.

### Published

One row per designed file, read from its companion `published/<recipe>.md`.

| Column | Read from |
|---|---|
| File | the companion |
| Recipe | the companion |
| From render | the companion |
| Model | the companion |
| Published | the companion |
| State | computed: `current` or `stale` |

State is `current` when the render's generated date is the one the companion names. State is `stale` when the render is newer or missing.

### Work

One row per work product.

| Column | Read from |
|---|---|
| File | the specification's header |
| Specification | the specification's header |
| Inputs | the newest state record of the specification's history |
| Made | the newest state record |
| State | the newest state record |

State holds one of `current`, `stale`, `by hand`. Until a state record exists, Inputs and Made are `—` and State is `stale`.

### Sources

Registration only: one row per entry of `sources/00-INDEX.md`. What a source is and is for stays in that index.

| Column | Read from |
|---|---|
| File | the entry's heading |
| Date | the entry's Date field |
| Date origin | the entry's Date field |
| Form | the entry's Form field |

### Dependencies

Registration only. The table lists the citations of another project's documents, a library's or any other's. They are found in the chain, the indexes, the recipes, the work and the research. There is one row per cited directory. No version is recorded, because the owner of the other project maintains its documents.

| Column | Read from |
|---|---|
| Path | the cited directory |
| Library | the slug of the cited project |
| Used by | the citing files |
| Note | the archive, where it has one; otherwise `—` |

### Research

Registration only: one row per note in `research/`. What a note answers stays in `research/00-INDEX.md`.

| Column | Read from |
|---|---|
| File | the note's file name |
| Date | the note's front-matter |
| Derived from | the note's front-matter |

### Findings

The findings of the critic and of the checks form one sequence. A finding is born by its report in `reviews/`.

| Column | Read from |
|---|---|
| ID | the report's heading |
| Severity | the report's heading |
| Category | the report's heading; a check's category is `conformance` |
| State | see below |
| Source review | the first report that names the finding |
| Resolution | see below |

State is `open` when the finding is born. State and Resolution then come from the newest of these:

- a `closed` record with the finding as its subject: State is `resolved`, Resolution is the record's reason
- the Verdict of a decision: State is `rejected`, `parked` or `obsolete`, Resolution is the decision
- a later report that names the finding as reopened under Known as: State is `open` again

The word `overruled` in an older record reads as `rejected`.

### Challenges

The challenges form one sequence. A challenge is born by its report in `challenges/`.

| Column | Read from |
|---|---|
| ID | the report's heading |
| State | see below |
| Headline | the report's heading, with the severity in brackets |
| Source review | the report |
| Resolution | see below |

State is `open` when the challenge is born. State and Resolution then come from the newest of these:

- a `closed` record: State is `accepted`, Resolution is the record's reason
- the Verdict of a decision: State is `rejected`, `parked` or `obsolete`, Resolution is the decision

## The state words

| Subject | Words |
|---|---|
| Brief (Mined) | `pending`, `partial`, `mined`, `dropped` |
| Published file (State) | `current`, `stale` |
| Work product (State) | `current`, `stale`, `by hand` |
| Finding (State) | `open`, `resolved`, `rejected`, `parked`, `obsolete` |
| Challenge (State) | `open`, `accepted`, `rejected`, `parked`, `obsolete` |

## Waiting on principal

The principal is the person whose thinking is being forged. This section is a rule, not a list that anyone writes. It holds one line per matter, which cites the matter and never copies it:

- each open thread, by its first sentence and its last dated paragraph
- each open question whose owner is the principal
- each open finding of a critic
- each open challenge

Under the heading "Parked, with their decision" stand the parked findings and challenges with their decision. Free text without an ID has no place here. Where nothing waits, the section says so in one line. For a project of the shape before the migration that has no threads file, the section says the threads were not read.

## Reports

The Reports section holds what the merged files cannot say. It stands only when there is something to report. It has three reports:

- an ID defined twice, with the files that define it
- a closed thread touched by a later commit
- a thread cited with neither a thread file nor a closed record

## Library projects

A project of kind `library` keeps these tables: Renders, Sources, Dependencies, Research and Waiting on principal. The tables Briefs, Documents, Published, Work and Challenges are left out. The Findings table returns with a check's first finding.

## The archive

`ledger.archive.md` is the hand-kept ledger as it stood at the migration, immutable. Its rows of Briefs, Work, Findings and Challenges are read for every item that has no record of the current shape. A newer record overrides the archive row. Its rows of Published, Sources and Dependencies are read as well, for a published file without a companion, a source entry without a Date field and a note on a dependency. A project not yet migrated is read whole from its hand-kept ledger as the archive.

## Where it is written

`python scripts/forge-ledger.py <slug>` writes `ledger.md` into the project, gitignored. Option `--out PATH` writes to that path instead, as a dry run. For a project of the shape before the migration, or one whose `ledger.md` is tracked by git, the script prints the ledger to standard output and does not write the file. The exit code is 0 in every case.

## See also

- [See where a project stands](../use/see-where-a-project-stands.md): reading the ledger through `/ledger`.
- [The ledger, made from the records](../about/the-ledger.md): why the ledger is made from the records.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.34 from the files the front-matter names; never edited by hand.
