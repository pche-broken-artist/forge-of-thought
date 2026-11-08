---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 690890d3bdd295a9
inputs:
  - templates/ledger.md
  - CLAUDE.md#Ledger
  - scripts/forge-ledger.py
---

# Ledger

The ledger is the file `ledger.md` of a project: the one place that states where the project stands, with its header, its tables, the matters waiting on the principal (the person whose thinking is forged) and its reports. This page is for the user and the extender who need its shape exactly: what each table holds and where each column is read from.

## How it is made

- The ledger is made at read time by `python scripts/forge-ledger.py <slug>`.
- The argument may also be the path of a project's directory.
- The script writes `ledger.md` into the project and keeps it out of git.
- Nobody writes a row by hand. Every command that changes state makes the ledger again with the script.
- With `--out PATH` the script writes there instead, a dry run that leaves the project's `ledger.md` alone.
- On a project of the shape before the migration, or where `ledger.md` is tracked by git, the script prints the ledger and does not write the file.
- A file the script cannot parse never stops it: the exit code stays 0 and the file is named in the header (see Reports).
- Resources and dependencies are registration only: what a source or a note is for is kept in the `00-INDEX.md` of its directory.

## The header

| Line | Content |
|---|---|
| `project` | The project's slug. |
| `updated` | The day the ledger was made. |
| `kind` | Echoed from the project file. |
| `language` | Echoed from the project file. |
| `shape` | Present only on a project of the shape before the migration: the ledger is then read from the hand-kept ledger as the archive. |
| `unparsed` | One line `unparsed: <file>:<line> (<what>)` for each file the script could not parse. |

## Tables

A project of kind `thought` keeps every table below. A table with nothing to list keeps its header row.

### Briefs

One row per brief (`00-brief.md` and `00-brief-<name>.md`).

| Column | Read from |
|---|---|
| File | The brief's file name. |
| Version | The brief's header. |
| Status | The brief's header. |
| Mined | The newest mining record of the intent's history; `pending` until one exists. |
| Note | The same record; `—` until one exists. |

Mined words:

- `pending`: the intent has not absorbed the brief.
- `partial`: the intent has absorbed it in part; Note says what remains.
- `mined`: the intent has absorbed it.
- `dropped`: the brief is set aside; Note gives the rejected direction.

### Documents

One row per layer of the chain below the briefs. A layer the project does not have gets no row.

| Column | Read from |
|---|---|
| File | The layer's file name. |
| Version | The document's header. |
| Status | The document's header. |
| Date | The newest content record of its history; a state record does not move it. |

### Renders

One row per render file. A translation cites the primary render.

| Column | Read from |
|---|---|
| Render | The render file, with its plain files (`.pptx`, `.docx`, `.mp4`) named beside it. |
| Audience | The audience of its recipe. |
| Recipe | The render's own provenance front-matter. |
| Inputs | The render's own provenance front-matter. |
| Generated | The render's own provenance front-matter. |

The documentation index has a row of its own, read from its own front-matter:

| Column | Value |
|---|---|
| Render | `docs/README.md`, the documentation index. |
| Audience | The three readers of the documentation. |
| Recipe | `none: derived by scripts/docs-index.py`. |
| Inputs | The map and the intent's version. |
| Generated | The index's own front-matter. |

### Published

One row per designed file.

| Column | Read from |
|---|---|
| File | The companion `published/<recipe>.md`. |
| Recipe | The companion. |
| From render | The companion. |
| Model | The companion. |
| Published | The companion. |
| State | Computed: see the state words. |

State words:

- `current`: the render's generated date is the one the companion names.
- `stale`: the render is newer than the companion names, or is missing.

### Work

One row per work product.

| Column | Read from |
|---|---|
| File | The specification's header. |
| Specification | The specification's header. |
| Inputs | The newest state record of the specification's history. |
| Made | The newest state record. |
| State | The newest state record. |

State words:

- `current`: the file was made from the specification as it stands.
- `stale`: the file is behind its specification; also the state while no record exists, with `—` for the other columns.
- `by hand`: the file was changed by hand.

### Sources

One row per entry of `sources/00-INDEX.md`. Registration only.

| Column | Read from |
|---|---|
| File | The entry's heading. |
| Date | The entry's Date field. |
| Date origin | The entry's Date field, the part after "from the". |
| Form | The entry's Form field. |

### Dependencies

One row per cited directory of another project, a library's or any other's. The citations are found in the chain, the indexes, the recipes, the work and the research. No version is kept, because the owner of those documents maintains them.

| Column | Read from |
|---|---|
| Path | The cited directory. |
| Library | The cited project's slug. |
| Used by | The citing files. |
| Note | The archive, where it has one; else `—`. |

### Research

One row per note in `research/`, or per bundle of one research. A bundle is read by its head `00-plan.md`; a bundle without a head is said so in the row. What a note answers is kept in `research/00-INDEX.md`.

| Column | Read from |
|---|---|
| File | The note, or the bundle directory. |
| Date | The front-matter of the note or of the head. |
| Derived from | The front-matter of the note or of the head. |

### Findings

The findings of the critic and of the checks, in one sequence.

| Column | Read from |
|---|---|
| ID | The heading in the report in `reviews/`. |
| Severity | The same heading. |
| Category | The same heading; a check's category is `conformance`. |
| State | The newest of the sources named below. |
| Source review | The first report that names the finding. |
| Resolution | The newest of the sources named below. |

A finding is born `open` by its report. State and Resolution then come from the newest of:

- A `closed` record with the finding as its subject: state `resolved`, the record's reason.
- A decision's Verdict: `rejected`, `parked` or `obsolete`, with the decision.
- A later report that names the finding as reopened under Known as: state `open` again.

An `overruled` in an older record is read as `rejected`.

### Challenges

One sequence, born by the report in `challenges/`.

| Column | Read from |
|---|---|
| ID | The heading in the report. |
| State | The newest of the sources named below. |
| Headline | The heading, with the severity in brackets. |
| Source review | The report. |
| Resolution | The newest of the sources named below. |

A challenge is born `open`. State and Resolution then come from the newest of:

- A `closed` record: state `accepted`, the record's reason.
- A decision's Verdict: `rejected`, `parked` or `obsolete`, with the decision.

## Waiting on principal

This section is a rule, not a list kept by hand. One line per matter, citing and never copying:

- Each open thread, by its first sentence and its last dated paragraph.
- Each open TBC whose owner is the principal.
- Each open finding of a critic.
- Each open challenge.
- Under a heading Parked, with their decision: the parked findings and the parked challenges.

Free text without an ID has no place here. An unfinished conversation is saved into its thread, never into the ledger. When nothing waits, the section says so in one line.

## Reports

What the merged files cannot say, found by the script. The section stands only when there is something to report:

- An ID defined twice.
- A closed thread touched by a later commit.
- A thread cited with neither a thread file nor a closed record.

The `unparsed:` line of the header, not a report row, names a file the script could not parse.

## Which tables a library keeps

A project of kind `library` keeps Renders, Sources, Dependencies, Research and Waiting on principal. Briefs, Documents, Published, Work and Challenges are left out. The Findings table returns with a check's first finding.

## The archive

`ledger.archive.md` is the hand-kept ledger as it stood at the migration, immutable. Its Briefs, Work, Findings and Challenges rows are read for every item that has no record of the new shape. A newer record overrides the archive row.

## See also

- [See where a project stands](../use/see-where-a-project-stands.md): reading the ledger through `/ledger`.
- [The ledger, made from the records](../about/the-ledger.md): why the ledger is made from the records.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
