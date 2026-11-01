---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 962e18d6a541fd80
inputs:
  - templates/ledger.md
  - CLAUDE.md#Ledger
  - scripts/forge-ledger.py
---

# Ledger

This page states the shape of a project's ledger exactly: its header, its tables and their columns, the state words, the Waiting on principal rule and the Reports section, with the place each column is read from. It is for the user who reads a ledger and for the extender who changes how it is made. The ledger is the single place that holds the state of a project (briefs, documents, renders, findings and the rest).

## How it is made

- The ledger is made at the moment it is read, by `python scripts/forge-ledger.py <slug>`.
- It is built from the project's documents and written as `ledger.md` in the project.
- It is never kept in git. The project's ignore file keeps it out.
- Nobody writes a row. Every command that changes state makes the ledger again with the script.
- The shape is that of `templates/ledger.md`, and the comments of that template are kept in the ledger.
- `--out PATH` writes the ledger to another file instead (a dry run).
- A project whose files are still in the shape before the migration is not written: its `ledger.md` is the hand-kept ledger, and the script prints to the terminal instead.
- A project whose `ledger.md` is tracked by git is not written either: the script prints to the terminal.
- A project layer that the project does not have gets no row and is not reported missing.

## The header

| Line | Holds | Read from |
|---|---|---|
| `project` | the project's slug | the argument given to the script |
| `updated` | the day the ledger was made | the day of the run |
| `kind` | `thought` or `library` | the project file, echoed |
| `language` | the project's language | the project file, echoed |
| `shape` | present only for a project before the migration | the project file |
| `unparsed: <file>:<line> (<what>)` | one line per file the script could not parse | the run |

An unparsable file never stops the script. It becomes an `unparsed:` line of the header, never a table row, and the exit code stays 0.

## Which tables a project keeps

| Kind | Tables |
|---|---|
| `thought` | every table below |
| `library` | Renders, Sources, Dependencies, Research and Waiting on principal; the Findings table returns with the first finding of a check |

## The tables

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

| Word | Meaning |
|---|---|
| `pending` | the intent has not absorbed the brief |
| `partial` | the intent has absorbed part of it; the Note says what remains |
| `mined` | the intent has absorbed it |
| `dropped` | the brief is set aside; the Note names the rejected direction |

### Documents

One row per layer of the chain below the briefs.

| Column | Read from |
|---|---|
| File | the file name |
| Version | the document's header |
| Status | the document's header |
| Date | the newest content record of the document's history; a state record (a mining, a work state, a closing) does not move it |

### Renders

One row per render file, read from the render's own provenance front-matter. A translation cites the primary render.

| Column | Read from |
|---|---|
| Render | the render file |
| Audience | the audience of its recipe |
| Recipe | the provenance front-matter |
| Inputs | the provenance front-matter |
| Generated | the provenance front-matter |

The documentation index (`docs/README.md`) has a row of its own, read from its front-matter. Its Recipe reads "none: derived by scripts/docs-index.py". Its Inputs are the map and the intent's version.

### Published

One row per designed file, read from its companion `published/<recipe>.md`.

| Column | Read from |
|---|---|
| File | the companion |
| Recipe | the companion |
| From render | the companion |
| Model | the companion |
| Published | the companion |
| State | compared with the render's generated date |

State words:

| Word | Meaning |
|---|---|
| `current` | the render's generated date is the one the companion names |
| `stale` | the render is newer, or missing |

### Work

One row per work product.

| Column | Read from |
|---|---|
| File | the specification's header |
| Specification | the specification's header |
| Inputs | the newest state record of the specification's history |
| Made | the newest state record of the specification's history |
| State | the newest state record of the specification's history |

State words:

| Word | Meaning |
|---|---|
| `current` | the file is made from the specification as it stands |
| `stale` | the file is behind its inputs; also the state, with `—` in Inputs and Made, until a record exists |
| `by hand` | the file is worked by hand |

### Sources

Registration only, one row per entry of `sources/00-INDEX.md`. What a source is and is for lives in the index, never in the ledger.

| Column | Read from |
|---|---|
| File | the entry's heading |
| Date | the entry's Date field |
| Date origin | the entry's Date field |
| Form | the entry's Form field |

### Dependencies

Registration only. One row per cited directory of another project's documents (a library's or any other's), found in the chain, the indexes, the recipes, the work and the research. No version is shown: another project's documents are kept by their owner.

| Column | Read from |
|---|---|
| Path | the cited directory |
| Library | the cited project's slug |
| Used by | the citing files |
| Note | the hand-kept ledger archive, `—` otherwise |

### Research

Registration only. One row per note in `research/`, or per bundle of one research, which is read by its head `00-plan.md`. A bundle without that head is said as a row. What a note answers lives in `research/00-INDEX.md`.

| Column | Read from |
|---|---|
| File | the note, or the bundle's directory |
| Date | the front-matter of the note or of the head |
| Derived from | the front-matter of the note or of the head |

### Findings

The findings of the critic and of the checks, in one sequence.

| Column | Read from |
|---|---|
| ID | the heading in the report in `reviews/` |
| Severity | the heading |
| Category | the heading; a check's category is `conformance` |
| State | `open` at birth, then the newest of the records below |
| Source review | the first report that names the finding |
| Resolution | the record or decision that settled it |

State and Resolution come from the newest of these:

- a `closed` record with the finding as its subject: `resolved`, with the record's reason;
- the Verdict of a decision: `rejected`, `parked` or `obsolete`, with the decision;
- a later report that names the finding as reopened under Known as: `open` again.

`overruled` in an older record reads as `rejected`.

### Challenges

One sequence, born by the report in `challenges/`.

| Column | Read from |
|---|---|
| ID | the heading in the report |
| State | `open` at birth, then the newest of the records below |
| Headline | the heading, with the severity in brackets |
| Source review | the report |
| Resolution | the record or decision that settled it |

State and Resolution come from the newest of these:

- a `closed` record: `accepted`, with the record's reason;
- the Verdict of a decision: `rejected`, `parked` or `obsolete`, with the decision.

## Waiting on principal

One line per matter, citing and never copying. The section holds:

- each open thread, by its first sentence and its last dated paragraph;
- each TBC whose owner is the principal;
- each open finding of a critic;
- each open challenge;
- under "Parked, with their decision", the parked findings and challenges with their decision.

Free text without an ID has no place here. When nothing waits, the section says so in one line.

## Reports

The section holds what the merged files cannot say. It stands only when there is something to report, and it holds:

- an ID defined twice;
- a closed thread touched by a later commit;
- a thread cited with neither a thread file nor a closed record.

A file the script could not parse is not a report: it is an `unparsed:` line of the header.

## The archive

`ledger.archive.md` is the hand-kept ledger as it stood at the migration. It is immutable. Its Briefs, Work, Findings and Challenges rows are read for every item that has no record of the newer shape. A newer record overrides the archive row.

## See also

- [See where a project stands](../use/see-where-a-project-stands.md): reading the ledger through `/ledger`.
- [The ledger, made from the records](../about/the-ledger.md): why the ledger is made from the records.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
