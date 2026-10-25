---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: d18561f066e0f392
inputs:
  - templates/ledger.md
  - CLAUDE.md#Ledger
  - scripts/forge-ledger.py
---

# Ledger

This page lists the shape of a project's ledger, the file that states
where the project stands: its header, every table with its columns and
the place each column is read from, the state words, the Waiting on
principal section and the Reports section. It is for the user who reads
a ledger and for the extender who changes what feeds it.

The ledger is made at read time by `python scripts/forge-ledger.py
<slug>` from the project's documents. It is written as `ledger.md` in
the project, kept out of git, and nobody writes a row by hand. The
shape is owned by `templates/ledger.md`; the script keeps that file's
comments in the ledger it makes.

## Header

| Line | Content |
|---|---|
| `project` | the project's slug |
| `updated` | the day the ledger was made |
| `kind` | `thought` or `library`, echoed from the project file |
| `language` | the project's language, echoed from the project file |
| `shape` | present only on a project of the shape before the migration: the ledger is then read from the hand-kept ledger as the archive |
| `unparsed:` | one line `unparsed: <file>:<line> (<what>)` for each file the script could not parse; never a row, never a crash |

The title line is `Ledger` followed by the slug.

## Tables of a thought project

A thought project keeps every table below. A table is registration or
state only: what a source, a note or a dependency is for lives in the
resource index or where it is used.

### Briefs

One row per brief (`00-brief.md` and `00-brief-<name>.md`).

| Column | Read from |
|---|---|
| File | the brief's file name |
| Version | the brief's header |
| Status | the brief's header |
| Mined | the newest mining record of the intent's history; `pending` until one exists |
| Note | the same record; `—` until one exists |

Mined words:

- `pending`: the intent has not absorbed the brief.
- `partial`: the intent has absorbed part of it; the Note says what remains.
- `mined`: the intent has absorbed it.
- `dropped`: the brief is set aside; the Note names the rejected direction.

### Documents

One row per layer of the chain below the briefs. A layer the project
does not have gets no row.

| Column | Read from |
|---|---|
| File | the layer's file name |
| Version | the header |
| Status | the header |
| Date | the newest content record of the layer's history |

A state record (a mining, a work state, a closing) does not move the
Date. Where no content record exists, the Date is read from the header,
then from the archive.

### Renders

One row per render file, read from the render's own provenance
front-matter. A translation cites the primary render. The root README,
release notes and contributing file are rows too; a render with a plain
file (`.pptx`, `.docx`, `.mp4`) names it in the first column.

| Column | Read from |
|---|---|
| Render | the render's path |
| Audience | the `audience` of its recipe |
| Recipe | the provenance |
| Inputs | the provenance |
| Generated | the provenance |

The documentation index has a row from its own front-matter, read when
the index is derived. Its Recipe is "none: derived by
scripts/docs-index.py", its Inputs are the documentation map and the
intent's version, and its Audience is the three readers of the
documentation.

### Published

One row per designed file, read from its companion
`published/<recipe>.md`.

| Column | Read from |
|---|---|
| File | the companion |
| Recipe | the companion |
| From render | the companion |
| Model | the companion |
| Published | the companion |
| State | computed |

State words:

- `current`: the render's generated date is the one the companion names.
- `stale`: the render is newer or missing.

### Work

One row per work product.

| Column | Read from |
|---|---|
| File | the specification's header |
| Specification | the specification's header |
| Inputs | the newest state record of the specification's history |
| Made | the same record |
| State | the same record |

State words: `current`, `stale`, `by hand`. Until a record exists, Made
and Inputs are `—` and State is `stale`.

### Sources

Registration only: one row per entry of `sources/00-INDEX.md`. An entry
that points to a library's document is a dependency and has no row here.

| Column | Read from |
|---|---|
| File | the entry's heading |
| Date | the entry's Date field |
| Date origin | the entry's Date field, the part after "from the" |
| Form | the entry's Form field |

### Dependencies

Registration only: the citations of another project's documents, a
library's or any other's, found in the chain, the indexes, the recipes,
the work and the research. There is one row per cited directory, and no
version, since the owner of those documents maintains them. The reviews,
challenges, sources, published files, renders, documentation and the
ledger files are not read, since they quote.

| Column | Read from |
|---|---|
| Path | the cited directory |
| Library | the cited project's slug |
| Used by | the citing files |
| Note | the archive, else `—` |

### Research

Registration only: one row per note in `research/`, or one row per
bundle of one research. A bundle is read by its head `00-plan.md`. A
bundle without a head is shown with the words "a bundle without
00-plan.md". What a note answers lives in `research/00-INDEX.md`.

| Column | Read from |
|---|---|
| File | the note, or the bundle directory |
| Date | the front-matter `date`, else the date in the file name |
| Derived from | the front-matter `derived_from` |

### Findings

The findings of the critic and of the checks form one sequence.

| Column | Read from |
|---|---|
| ID | the heading of the report in `reviews/` |
| Severity | the heading |
| Category | the heading; a check's category is `conformance`; a critic's, where the heading has none, is `—` |
| State | see below |
| Source review | the first report that names the finding |
| Resolution | see below |

A finding is born open by its report. State and Resolution then come
from the newest of these:

- A `closed` record with the finding as its subject: State `resolved`,
  Resolution the record's reason.
- A decision's Verdict: State `rejected`, `parked` or `obsolete`,
  Resolution the decision (for a parked finding, with the condition it
  is parked until).
- A later report that names the finding as reopened under "Known as":
  State `open`, Resolution "reopened by" that report.

State words: `open`, `resolved`, `rejected`, `parked`, `obsolete`. The
word `overruled` in an older record reads as `rejected`.

### Challenges

One sequence, born by the report in `challenges/`.

| Column | Read from |
|---|---|
| ID | the heading of the report |
| State | see below |
| Headline | the heading, with the severity in brackets |
| Source review | the report |
| Resolution | see below |

State and Resolution come from the newest of a `closed` record
(State `accepted`, Resolution the record's reason) or a decision's
Verdict (`rejected`, `parked` or `obsolete`, Resolution the decision).
State words: `open`, `accepted`, `rejected`, `parked`, `obsolete`.

## Tables of a library

A library keeps Renders, Sources, Dependencies, Research and Waiting on
principal. The Findings table returns with a check's first finding.
Briefs, Documents, Published, Work and Challenges are left out.

## Waiting on principal

What waits on the principal is a rule, not a list kept by hand. Each
matter is one line that cites its source and never copies it. The lines
are:

- Each open thread, by its first sentence and its last dated paragraph.
- Each TBC whose owner is the principal, with the file it stands in.
- Each open finding of a critic.
- Each open challenge.

Under the heading "Parked, with their decision" stand the parked
findings and challenges, each with its decision. Free text without an
ID has no place in the section. Where nothing waits, the section says
so in one line. On a project of the shape before the migration with no
threads file, the section says the threads were not read.

## Reports

The section says what the merged files cannot say. It stands only when
there is something to report, and is left out otherwise. It reports:

- An ID defined twice.
- A closed thread touched by a later commit.
- A thread cited with neither a thread file nor a closed record.

A file the script could not parse is not a report: it is an `unparsed:`
line of the header.

## The archive

`ledger.archive.md` is the hand-kept ledger as it stood at the
migration and is immutable. Its rows for Briefs, Work, Findings and
Challenges are read for every item without a record of the current
shape, and a newer record overrides them. A project not yet migrated is
read whole from its hand-kept ledger as the archive.

## Where it is written

The script writes `ledger.md` only on a project of the current shape
whose ledger is out of git's index. On a project of the shape before
the migration, and where the ledger is tracked by git, it prints to the
terminal and does not write. With `--out PATH` it writes there instead.
Its exit code is 0.

## See also

- [See where a project stands](../use/see-where-a-project-stands.md): reading the ledger through `/ledger`.
- [The ledger, made from the records](../about/the-ledger.md): why the ledger is made from the records.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
