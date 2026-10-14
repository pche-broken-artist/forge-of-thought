---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 46ef20c7b4c39006
inputs:
  - templates/ledger.md
  - CLAUDE.md#Ledger
---

# Ledger

The ledger is the file `ledger.md` of a project: the single source of truth for its state, as a header and a set of tables. This page lists the header, every table with its columns and the state words, for the user who reads a ledger and the extender who writes to one. The principal is the person whose thinking is being forged.

## The header

The header is front-matter at the top of the file.

| Field | Holds |
|---|---|
| `project` | the project's slug |
| `kind` | `thought` or `library` |
| `language` | the language of the chain's artefacts, as an ISO 639-1 code |
| `updated` | the date of the last update, `YYYY-MM-DD` |

A ledger without `kind` reads as `thought`. At an import that is a fact the command reports. At a check it is a finding with a one-line fix.

## Tables

A thought project keeps every table below. The ledger is freely rewritten and kept current after every operation.

### Briefs

One row per brief (`00-brief.md` and `00-brief-<name>.md`).

| Column | Holds |
|---|---|
| File | the brief's file |
| Version | its version |
| Status | its state word |
| Mined | how far the intent has absorbed it |
| Note | what remains (when `partial`) or the rejected direction (when `dropped`) |

Status words:

| Word | Meaning |
|---|---|
| `draft` | being composed |
| `approved` | version 1.0 and on; changed after that as any artefact is |

Mined words:

| Word | Meaning |
|---|---|
| `pending` | not yet absorbed |
| `partial` | partly absorbed |
| `mined` | absorbed |
| `dropped` | not taken into the intent |

### Documents

One row per layer below the intent, added when the layer is born. A layer the project does not have gets no row.

| Column | Holds |
|---|---|
| File | the document's file |
| Version | its version |
| Status | its status |
| Date | its date |

### Renders

One row per rendered recipe, written by `/render` at the first render and kept by every later one. The row mirrors the render's front-matter provenance.

| Column | Holds |
|---|---|
| Render | the render |
| Audience | who it is for |
| Recipe | the recipe it was made from |
| Inputs | what it was made from |
| Generated | when it was generated |

The documentation index has a row too, written by `/document`:

| Column | Value |
|---|---|
| Recipe | `none, derived by scripts/docs-index.py` |
| Inputs | the documentation map with its generated date, and the intent's version |

### Published

Designed files made by `/publish`, one row per file.

| Column | Holds |
|---|---|
| File | the published file |
| Recipe | the recipe |
| From render | the render it was made from |
| Model | the model that made it |
| Published | when it was published |
| State | `current` or `stale` |

State words:

| Word | Meaning |
|---|---|
| `current` | set by `/publish` |
| `stale` | set by every `/render` of that recipe |

### Work

One row per work product, written by `/work` at the specification's birth and kept by every making.

| Column | Holds |
|---|---|
| File | the work file |
| Specification | the specification's version |
| Inputs | what the work is made from |
| Made | when it was made |
| State | `current`, `stale` or `by hand` |

State words:

| Word | Meaning |
|---|---|
| `current` | set by the making |
| `stale` | set by a write of the specification not followed by a making |
| `by hand` | set on the principal's word, when he has worked the file and does not want it remade |

### Sources

Registration only. External inputs, immutable once registered. What a source is and is for lives in `sources/00-INDEX.md`, never in the ledger.

| Column | Holds |
|---|---|
| File | the source's file |
| Date | the best-effort origin date |
| Date origin | `content`, `file` or `ingested` |
| Form | `text`, `extract of <original>` or `binary`; one form per source |

### Dependencies

Registration only. Documents of other repositories the project relies on, typically library documents, cited by path from an index entry, a recipe or the chain. They carry no version, because library documents are maintained by their owner. What a document is for lives where it is used.

| Column | Holds |
|---|---|
| Path | the document's path |
| Library | the library that holds it |
| Used by | where it is used |
| Note | a note |

### Research

Registration only. Immutable dated notes written by `/research`, or recorded expert estimates. What a note answers lives in `research/00-INDEX.md`, never in the ledger.

| Column | Holds |
|---|---|
| File | the note's file |
| Date | its date |
| Derived from | what it was derived from |

### Findings

Findings of the critic and of the checks, in one sequence.

| Column | Holds |
|---|---|
| ID | the finding's ID |
| Severity | its severity |
| Category | its category |
| State | its state word |
| Source review | the review that holds it |
| Resolution | for `resolved`, the assignment version, or for a check's finding what fixed it; for `rejected`, the decision ID |

State words: `open`, `resolved`, `rejected`, `parked`, `obsolete`. The word `overruled` in an older record reads as `rejected`.

### Challenges

| Column | Holds |
|---|---|
| ID | the challenge's ID |
| State | its state word |
| Headline | its headline |
| Source review | the review that holds it |
| Resolution | for `accepted`, the intent version; for `rejected`, the decision ID |

State words: `open`, `accepted`, `rejected`, `parked`, `obsolete`.

### Waiting on principal

A list of lines, one per matter that waits on the principal.

## The rule: cite, never copy

The ledger cites and never copies. A matter that has an ID gets one line: the ID, a few words, its state. Its substance stays in the thread or the record. Free text is for a matter with no ID yet, which gets one at the next write. An unfinished conversation is saved into its thread of the intent, never into the ledger.

A layer below the intent that a project does not have is not missing: `/forge` and the checks say nothing of it.

## Which tables a library keeps

| Kind | Tables |
|---|---|
| `thought` | every table above |
| `library` | Renders, Sources, Dependencies, Research and Waiting on principal |

A library's Briefs, Documents, Published, Work, Findings and Challenges tables are deleted at scaffold time. The Findings table returns with a check's first finding.

## See also

- [See where a project stands](../use/see-where-a-project-stands.md): reading the ledger through `/ledger`.
- [Documents and records](../about/documents-and-records.md): why the ledger is the single source of truth.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
