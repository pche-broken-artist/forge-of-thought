---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: f364a8ae1aba1052
inputs:
  - templates/ledger.md
  - CLAUDE.md#Ledger
  - scripts/forge-ledger.py
---

# Ledger

The ledger is the file `ledger.md` of a project: the one place
where the state of the project is read, made from its documents at
the moment it is asked for. This page gives its header, its tables
and columns, its state words and its reports, and says for each
column where it is read from. It is for the user who reads a ledger
and the extender who changes how it is made. A ledger holds no state
of its own: nobody writes a row. The principal (the person whose
thinking is forged) reads it; the ledger script writes it.

## How it is made

Command, from the root of the engine:

```
python scripts/forge-ledger.py <slug>
```

The argument is the project's slug or the path of the project's
directory. The option `--out PATH` writes the ledger there instead
of into the project, which is a dry run.

- The ledger is gitignored and never kept in git.
- The script writes `ledger.md` only for a project of the current
  shape whose ledger is not tracked by git.
- For a project of the shape before the migration, or where the
  ledger is tracked, the script prints the ledger to standard output
  and does not write the file.
- An unparsable file never stops the script. The exit code is 0.

`ledger.archive.md` is the hand-kept ledger as it stood at the
migration, and it is immutable. Its Briefs, Work, Findings and
Challenges rows are read for every item that has no record of the
new shape. A newer record overrides the archive row. The script
reads the archive's Sources, Dependencies and Published rows the
same way, and a project not yet migrated is read whole from its
hand-kept ledger as the archive.

## The header

The header is the front-matter and the title.

| Line | Holds | Read from |
|---|---|---|
| `project` | the slug | the project file |
| `updated` | the day the ledger was made | the day of the run |
| `kind` | `thought` or `library` | the project file, echoed |
| `language` | the project's language | the project file, echoed |
| `shape` | present only for a project of the shape before the migration | the script |
| `unparsed:` | one line per file the script could not parse, `unparsed: <file>:<line> (<what>)` | the script |

The title is `# Ledger - <slug>`. An unparsable file is a line in
the header and never a row of a table.

## The tables

A project of kind `thought` keeps every table below. A project of
kind `library` keeps only Renders, Sources, Dependencies, Research
and Waiting on principal. The Findings table returns in a library
with a check's first finding.

### Briefs

One row per brief (`00-brief.md` and `00-brief-<name>.md`).

| Column | Read from |
|---|---|
| File | the file name |
| Version | the brief's header |
| Status | the brief's header |
| Mined | the newest mining record of the intent's history; `pending` until one exists |
| Note | the same record; `-` until one exists |

State words of Mined, how far the intent has absorbed the brief:

- `pending`: not yet mined
- `partial`: mined in part; Note says what remains
- `mined`: absorbed
- `dropped`: not taken up; Note names the rejected direction

### Documents

One row per layer of the chain below the briefs. A layer the project
does not have gets no row.

| Column | Read from |
|---|---|
| File | the file name |
| Version | the document's header |
| Status | the document's header |
| Date | the newest content record of its history |

A state record (a mining, a work state, a closing) does not move
Date.

### Renders

One row per render file, from the render's own provenance
front-matter. A translation cites the primary render.

| Column | Read from |
|---|---|
| Render | the file, with its plain file where one exists |
| Audience | the render's recipe |
| Recipe | the provenance |
| Inputs | the provenance |
| Generated | the provenance |

The documentation index has a row from its own front-matter: Recipe
is "none: derived by scripts/docs-index.py", Inputs are the
documentation map and the intent's version.

### Published

One row per designed file, from its companion
`published/<recipe>.md`.

| Column | Read from |
|---|---|
| File | the companion |
| Recipe | the companion |
| From render | the companion |
| Model | the companion |
| Published | the companion |
| State | the render's generated date against the one the companion names |

State words:

- `current`: the render's generated date is the one the companion
  names
- `stale`: the render is newer or missing

### Work

One row per work product.

| Column | Read from |
|---|---|
| File | the specification's header |
| Specification | the specification's header |
| Inputs | the newest state record of the specification's history |
| Made | the same record |
| State | the same record |

State words: `current`, `stale`, `by hand`. Until a record exists,
Inputs and Made are `-` and State is `stale`.

### Sources

Registration only, one row per entry of `sources/00-INDEX.md`.

| Column | Read from |
|---|---|
| File | the entry's heading |
| Date | the entry's Date field |
| Date origin | the entry's Date field |
| Form | the entry's Form field |

What a source is and is for stays in the index, never in the ledger.

### Dependencies

Registration only. A row is one cited directory of another project,
a library's or any other's, found in the chain, the indexes, the
recipes, the work and the research. No version is kept, because the
owner maintains those documents.

| Column | Read from |
|---|---|
| Path | the cited directory |
| Library | the cited project's slug |
| Used by | the citing files |
| Note | the archive row, where there is one |

### Research

Registration only, one row per note in `research/`, or one row per
bundle of one research, read by its head `00-plan.md`. A bundle
without a head is a row that says so.

| Column | Read from |
|---|---|
| File | the note, or the bundle directory |
| Date | the front-matter |
| Derived from | the front-matter |

What a note answers stays in `research/00-INDEX.md`.

### Findings

The findings of the critic and of the checks, one sequence. A
finding is born by its report in `reviews/`.

| Column | Read from |
|---|---|
| ID | the report's heading |
| Severity | the report's heading |
| Category | the report's heading; a check's category is `conformance` |
| State | `open` at birth; then the newest record, decision or report below |
| Source review | the first report that names the finding |
| Resolution | the same newest source |

State and Resolution come from the newest of:

- a `closed` record with the finding as its subject: State
  `resolved`, Resolution the record's reason
- a decision's Verdict: State `rejected`, `parked` or `obsolete`,
  Resolution the decision
- a later report that names the finding as reopened under Known as:
  State `open` again

`overruled` in an older record reads as `rejected`.

### Challenges

One sequence, born by the report in `challenges/`.

| Column | Read from |
|---|---|
| ID | the report's heading |
| State | `open` at birth; then the newest record or decision below |
| Headline | the report's heading, with the severity in brackets |
| Source review | the report |
| Resolution | the same newest source |

State and Resolution come from the newest of:

- a `closed` record: State `accepted`, Resolution the record's
  reason
- a decision's Verdict: State `rejected`, `parked` or `obsolete`,
  Resolution the decision

### Waiting on principal

One line per matter. A line cites its source and never copies it.
The lines stand in this order:

1. The open threads. Those that something waits on come first, then
   the rest by priority. Each line carries its priority and what
   waits on it in brackets, its first sentence and its last dated
   paragraph.
2. The open items of a document marked with the principal as owner
   (the TBCs).
3. The open findings of a critic and the open challenges.
4. Under Parked, the parked findings and challenges with their
   decision.

Free text without an ID has no place here.

### Reports

What the merged files cannot say. The section stands only when there
is something to report. There are three reports:

- an ID defined twice
- a closed thread touched by a later commit
- a thread cited with neither a thread file nor a closed record

## See also

- [See where a project stands](../use/see-where-a-project-stands.md):
  reading the ledger through `/ledger`.
- [The ledger, made from the records](../about/the-ledger.md): why
  the ledger is made from the records.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
