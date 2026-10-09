---
generated: 2026-10-09
made: mirrored
inputs-hash: d95e2b21d3a5646f
inputs:
  - templates/ledger.md
  - CLAUDE.md
---

# Ledger

This page lists the fields and tables of a project's `ledger.md`, the single source of truth for the project's state, and the state words each table uses. It is for a user who reads or keeps a ledger and for an extender who needs its exact shape. The skeleton is `templates/ledger.md`. The ledger is freely rewritten and kept current after every operation.

## Header

| Field | Value |
|---|---|
| `project` | the project's slug |
| `kind` | `thought` or `library` |
| `language` | language of the chain's artefacts, an ISO 639-1 code; English when absent |
| `updated` | date of the last update, `YYYY-MM-DD` |

## Tables of a thought project

A project of kind `thought` keeps every table below.

### Briefs

One row per brief (`00-brief.md` and `00-brief-<name>.md`).

| Column | Meaning |
|---|---|
| File | the brief's file |
| Version | its version |
| Status | `draft` or `approved` |
| Mined | `pending`, `partial`, `mined` or `dropped` |
| Note | what remains (for `partial`), or the REJ (for `dropped`) |

Status words: `draft` is a brief being composed; `approved` is 1.0 and on, changed after that as any artefact is.

Mined words say how far the intent has absorbed the brief: `pending`, `partial`, `mined`, `dropped`.

### Documents

One row per layer below the intent, added when the layer is born. A layer the project does not have gets no row.

| Column | Meaning |
|---|---|
| File | the document's file |
| Version | its version |
| Status | its status |
| Date | its date |

### Renders

Generated outputs, one row per recipe in `recipes/`. A row mirrors the provenance in the render's front-matter.

| Column |
|---|
| Render |
| Audience |
| Recipe |
| Inputs |
| Generated |

### Published

Designed files made by `/publish`, one row per file.

| Column |
|---|
| File |
| Recipe |
| From render |
| Model |
| Published |
| State |

State words: `current` or `stale`. `/publish` sets a file to `current`; every `/render` of that recipe sets it to `stale`.

### Sources

Registration only. External inputs, immutable once registered. What a source is and is for lives in `sources/00-INDEX.md`, not in the ledger.

| Column | Meaning |
|---|---|
| File | the source's file |
| Date | best-effort origin date |
| Date origin | `content`, `file` or `ingested` |
| Form | `text`, `extract of <original>` or `binary`; one form per source |

### Dependencies

Registration only. Documents of other repositories the project relies on, typically library documents, cited by path. No version is kept: library documents are maintained by their owner. What the document is for lives where it is used (the index entry or the recipe).

| Column |
|---|
| Path |
| Library |
| Used by |
| Note |

### Research

Registration only. Immutable dated notes written by `/research`, or recorded expert estimates. What a note answers lives in `research/00-INDEX.md`.

| Column |
|---|
| File |
| Date |
| Derived from |

### Findings

Findings of the critic and of the checks, in one sequence.

| Column |
|---|
| ID |
| Severity |
| Category |
| State |
| Source review |
| Resolution |

State words: `open`, `resolved`, `rejected`, `parked`, `obsolete`.

Resolution: for `resolved`, the assignment version, or for a check's finding what fixed it; for `rejected`, a `DEC.NNNN`.

An older record that says `overruled` reads as `rejected`.

### Challenges

| Column |
|---|
| ID |
| State |
| Headline |
| Source review |
| Resolution |

State words: `open`, `accepted`, `rejected`, `parked`, `obsolete`.

Resolution: the intent version for `accepted`, a `DEC.NNNN` for `rejected`.

### Waiting on principal

A list, one line per matter waiting on the principal. The ledger cites and never copies. A matter that has an ID gets one line: the ID, a few words, its state; its substance stays in the thread or the record. Free text is for a matter with no ID yet, which gets one at the next write. An unfinished conversation is saved into its thread of the intent, never here.

## Tables of a library

A project of kind `library` keeps only Renders, Sources, Dependencies, Research and Waiting on principal. The Briefs, Documents, Published, Findings and Challenges tables are deleted when it is scaffolded. The Findings table returns with a check's first finding.

## See also

- [See where a project stands](../use/see-where-a-project-stands.md): reading the ledger through `/ledger`.
