---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 927fe95fb3bb2779
inputs:
  - templates/ledger.md
  - CLAUDE.md#Ledger
  - scripts/forge-ledger.py
---

# Ledger

The ledger is the file `ledger.md` of a project: the single source of truth for its state, made from the project's documents each time it is wanted. This page is for the user and the extender who need its header, its tables, the state words and the place each column is read from. The principal is the person whose thinking is forged in the project.

## How it is made

- The command is `python scripts/forge-ledger.py <slug>`.
- The slug `forge` names the engine's own project.
- The script builds `ledger.md` in the shape of `templates/ledger.md`.
- Nobody writes a row. What only the ledger once knew lives in records, in a field of an index entry, in a published companion or in the Verdict of a decision.
- Every command that changes state remakes the ledger by the script.
- The ledger is never kept in git. The script writes `ledger.md` only where git does not track it. Where git tracks it, the script writes nothing and prints the ledger to standard output, and a dry run goes to a file given with `--out PATH`.
- A file the script cannot parse never stops it. The exit code is 0, and the file is named in the header.
- A layer below the intent that a project does not have gets no row and is not reported as missing.

## The header

| Field | Holds |
|---|---|
| `project` | the slug of the project |
| `updated` | the day the ledger was made |
| `kind` | the kind of the project, echoed from the project file |
| `language` | the language of the project, echoed from the project file |
| `shape` | present only for a project not yet migrated: it says the ledger was read from the hand-kept ledger as the archive |
| `unparsed:` | one line `unparsed: <file>:<line> (<what>)` for each file the script could not parse; the line is not a row of any table |

## Tables and where their columns are read from

The tables stand in this order. Every table is made from records and headers, never from rows kept by hand.

### Briefs

One row per brief (`00-brief.md` and `00-brief-<name>.md`).

| Column | Read from |
|---|---|
| File | the file name |
| Version | the brief's header |
| Status | the brief's header |
| Mined | the newest mining record of the intent's history; `pending` until one exists |
| Note | the same record; `—` until one exists |

State words of Mined:

- `pending`
- `partial`
- `mined`
- `dropped`

The word says how far the intent has absorbed the brief. Note says what remains (partial) or the rejected direction (dropped).

### Documents

One row per layer of the chain below the briefs.

| Column | Read from |
|---|---|
| File | the file name |
| Version | the document's header |
| Status | the document's header |
| Date | the newest content record of the document's history; a state record does not move it |

### Renders

One row per render file, from the render's own provenance front-matter. A translation cites the primary render.

| Column | Read from |
|---|---|
| Render | the file; a plain file made beside it is named in the cell |
| Audience | the recipe's header |
| Recipe | the render's provenance |
| Inputs | the render's provenance |
| Generated | the render's provenance |

The documentation index has a row of its own, read from its front-matter:

- Render: `docs/README.md`, the documentation index.
- Recipe: `none: derived by scripts/docs-index.py`.
- Inputs: the documentation map and the version of the intent.

### Published

One row per designed file, from its companion `published/<recipe>.md`.

| Column | Read from |
|---|---|
| File | the companion |
| Recipe | the companion |
| From render | the companion |
| Model | the companion |
| Published | the companion |
| State | the companion against the render |

State words:

- `current`: the render's generated date is the one the companion names.
- `stale`: the render is newer or missing.

### Work

One row per work product.

| Column | Read from |
|---|---|
| File | the specification's header |
| Specification | the specification's header |
| Inputs | the newest state record of the specification's history; `—` until one exists |
| Made | the same record; `—` until one exists |
| State | the same record; `stale` until one exists |

State words:

- `current`
- `stale`
- `by hand`

### Sources

Registration only, one row per entry of `sources/00-INDEX.md`. What a source is and is for stays in the index.

| Column | Read from |
|---|---|
| File | the heading of the entry |
| Date | the Date field of the entry |
| Date origin | the Date field of the entry |
| Form | the Form field of the entry |

### Dependencies

Registration only. A row stands for a directory of a library cited in the chain, the indexes, the recipes, the work or the research, one row per cited directory. No version is kept, because the owner maintains a library's documents.

| Column | Read from |
|---|---|
| Path | the cited directory |
| Library | the library named in the citation |
| Used by | the citing files |
| Note | the archive, where it has one |

### Research

Registration only, one row per note in `research/`. What a note answers stays in `research/00-INDEX.md`.

| Column | Read from |
|---|---|
| File | the file name |
| Date | the note's front-matter |
| Derived from | the note's front-matter |

### Findings

The findings of the critic and of the checks, in one sequence. A finding is born by its report in `reviews/`.

| Column | Read from |
|---|---|
| ID | the heading of the report |
| Severity | the heading of the report |
| Category | the heading of the report; a check's category is `conformance` |
| State | the newest of the sources below; `open` at birth |
| Source review | the first report that names the finding |
| Resolution | the same source as the state |

State and Resolution come from the newest of these:

- a `closed` record with the finding as its subject: state `resolved`, the record's reason as resolution;
- the Verdict of a decision: `rejected`, `parked` or `obsolete`, with the decision as resolution;
- a later report that names the finding as reopened under Known as: state `open` again.

State words:

- `open`
- `resolved`
- `rejected`
- `parked`
- `obsolete`

The word `overruled` in an older record reads as `rejected`.

### Challenges

One sequence, born by the report in `challenges/`.

| Column | Read from |
|---|---|
| ID | the heading of the report |
| State | the newest of the sources below; `open` at birth |
| Headline | the heading of the report, with the severity in brackets |
| Source review | the report |
| Resolution | the same source as the state |

State and Resolution come from the newest of these:

- a `closed` record: state `accepted`, the record's reason as resolution;
- the Verdict of a decision: `rejected`, `parked` or `obsolete`, with the decision as resolution.

State words:

- `open`
- `accepted`
- `rejected`
- `parked`
- `obsolete`

## Waiting on principal

This section is made by a rule, not kept as a list. It holds one line for each of these matters, each citing its source and never copying it:

- each open thread, by its first sentence and its last dated paragraph;
- each open question (TBC) whose owner is the principal;
- each open finding of a critic;
- each open challenge.

Under the heading Parked, with their decision, stand the parked findings and challenges with the decision that parked them.

Free text without an ID has no place in this section. Where nothing waits, the section holds one line saying so.

## Reports

This section holds what the merged files cannot say. It stands only when there is something to report. The script reports:

- an ID defined twice, with the files that define it;
- a closed thread touched by a later commit;
- a thread cited with neither a thread file nor a closed record.

## The archive

`ledger.archive.md` is the hand-kept ledger as it stood at the migration. It is immutable. The script reads its Briefs, Work, Findings and Challenges rows for every item that has no record of the new shape, and a newer record overrides the archive row. It also supplies the Published rows that have no companion yet, the Date, Form and Date origin of sources whose entries lack them, and the Note of a dependency.

## Which tables a library keeps

A project of kind `thought` keeps every table. A project of kind `library` keeps:

- Renders
- Sources
- Dependencies
- Research
- Waiting on principal

The tables Briefs, Documents, Published, Work and Challenges are dropped. The Findings table returns with a check's first finding.

## See also

- [See where a project stands](../use/see-where-a-project-stands.md): reading the ledger through `/ledger`.
- [The ledger, made from the records](../about/the-ledger.md): why the ledger is made from the records.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
