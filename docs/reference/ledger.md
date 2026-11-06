---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 2e256333a1982205
inputs:
  - templates/ledger.md
  - CLAUDE.md#Ledger
  - scripts/forge-ledger.py
---

# Ledger

The ledger is the file `ledger.md` of a project: the single source of truth for its state, in tables, for the principal (the person whose thinking is forged) and for anyone who extends the forge. This page states its header, its tables, where each column is read from and the words its states use.

## How it is made

- It is made by `python scripts/forge-ledger.py <slug>` at the time it is read.
- It is never kept in git. The script writes it as a gitignored file.
- Nobody writes a row. Every command that changes state remakes the ledger with the script.
- The shape is that of `templates/ledger.md`, whose comments the script keeps.
- The script can print to standard output, or to a path given with `--out`, instead of writing the file (a dry run).
- On a project of the shape before the migration, `ledger.md` is the hand-kept ledger and the script does not write it. The same holds where git tracks the ledger.
- An unparsable file is not a crash. The script exits with 0 and names the file in the header.

## The header

| Field | Holds |
|---|---|
| `project` | the slug |
| `updated` | the day the ledger was made |
| `kind` | read from the project file, echoed |
| `language` | read from the project file, echoed |
| `shape` | present only on a project of the shape before the migration |
| `unparsed:` | one line per file the script could not parse, as `unparsed: <file>:<line> (<what>)` |

## The tables

A project of kind `thought` keeps every table. A project of kind `library` keeps only Renders, Sources, Dependencies, Research and Waiting on principal. Its Findings table returns with a check's first finding.

### Briefs

One row per brief (`00-brief.md` and `00-brief-<name>.md`).

| Column | Read from |
|---|---|
| File | the brief's file name |
| Version | the brief's header |
| Status | the brief's header |
| Mined | the newest mining record of the intent's history; `pending` until one exists |
| Note | the same record; `—` until one exists |

State words of Mined:

- `pending`: the intent has not absorbed the brief.
- `partial`: the intent has absorbed part of it; Note says what remains.
- `mined`: the intent has absorbed it.
- `dropped`: Note gives the rejected direction.

### Documents

One row per layer of the chain below the briefs. A layer the project does not have gets no row.

| Column | Read from |
|---|---|
| File | the layer's file name |
| Version | the header |
| Status | the header |
| Date | the newest content record of the history; a state record does not move it |

### Renders

One row per render file, read from the render's own provenance front-matter. A translation cites the primary render.

| Column | Read from |
|---|---|
| Render | the file; a plain file made beside it is named in brackets |
| Audience | the render's recipe |
| Recipe | the provenance |
| Inputs | the provenance |
| Generated | the provenance |

The documentation index has a row of its own, read from its front-matter. Its Recipe is "none: derived by scripts/docs-index.py". Its Inputs are the documentation map and the version of the intent.

### Published

One row per designed file, read from its companion `published/<recipe>.md`.

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

State words:

- `current`
- `stale`
- `by hand`

Until a record exists, Inputs and Made are `—` and State is `stale`.

### Sources

Registration only: one row per entry of `sources/00-INDEX.md`. What a source is and is for lives in the index.

| Column | Read from |
|---|---|
| File | the entry |
| Date | the entry's Date field |
| Date origin | the entry's Date field |
| Form | the entry's Form field |

### Dependencies

Registration only: the citations of another project's documents, a library's or any other's. They are found in the chain, the indexes, the recipes, the work and the research. There is one row per cited directory and no version, because the owner maintains those documents.

| Column | Read from |
|---|---|
| Path | the cited directory |
| Library | the slug of the cited project |
| Used by | the citing files |
| Note | the archive, where it has one; else `—` |

### Research

Registration only: one row per note in `research/`, or per bundle of one research. A bundle is read by its head, `00-plan.md`. A bundle without a head is said so in the row. What a note answers lives in `research/00-INDEX.md`.

| Column | Read from |
|---|---|
| File | the note, or the bundle's directory |
| Date | the front-matter |
| Derived from | the front-matter |

### Findings

The findings of the critic and of the checks, in one sequence. A finding is born by its report in `reviews/`.

| Column | Read from |
|---|---|
| ID | the heading of the report |
| Severity | the heading |
| Category | the heading; a check's category is `conformance` |
| State | `open` at birth, then the newest of the sources below |
| Source review | the first report that names the finding |
| Resolution | the newest of the sources below |

State and Resolution come from the newest of these:

- a `closed` record with the finding as its subject gives `resolved` and the record's reason.
- a decision's Verdict gives `rejected`, `parked` or `obsolete`, and the decision.
- a later report that names the finding as reopened under Known as gives `open` again.

`overruled` in an older record reads as `rejected`.

### Challenges

One sequence, born by the report in `challenges/`.

| Column | Read from |
|---|---|
| ID | the heading |
| State | `open` at birth, then the newest of the sources below |
| Headline | the heading, with the severity in brackets |
| Source review | the report |
| Resolution | the newest of the sources below |

State and Resolution come from the newest of these:

- a `closed` record gives `accepted` and the record's reason.
- a decision's Verdict gives `rejected`, `parked` or `obsolete`, and the decision.

## Waiting on principal

This section lists what waits on the principal, one line per matter, citing and never copying. It is a rule, not a list written by hand. It holds:

- the open threads, each by its first sentence and its last dated paragraph.
- the open questions marked to be confirmed whose owner is the principal.
- the open findings of a critic and the open challenges.
- under "Parked, with their decision", the parked findings and challenges with their decision.

Free text without an ID has no place here. An unfinished conversation is saved into its thread of the intent, never into the ledger. Where nothing waits, the section says so.

## Reports

The section lists what the merged files cannot say. It stands only when there is something to report:

- an ID defined twice.
- a closed thread touched by a later commit.
- a thread cited with neither a thread file nor a closed record.

## The archive

`ledger.archive.md` is the hand-kept ledger as it stood at the migration, and it is immutable. Its Briefs, Work, Findings and Challenges rows are read for every item without a record of the new shape. A newer record overrides the archive.

## See also

- [See where a project stands](../use/see-where-a-project-stands.md): reading the ledger through `/ledger`.
- [The ledger, made from the records](../about/the-ledger.md): why the ledger is made from the records.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
