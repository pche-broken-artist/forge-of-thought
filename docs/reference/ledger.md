---
generated: 2026-10-09
made: mirrored
inputs:
  - templates/ledger.md
  - CLAUDE.md
---

# Ledger

The facts of the ledger file as its template states them: the header
fields, each table with its columns, the state words and which tables
a library keeps. It is for the user who reads a project's ledger and
for the extender who changes the template or a command that writes it.

The ledger is the single source of truth for a project's state. It is
freely rewritten and kept current after every operation. It cites and
never copies: what a resource is and is for lives in the directory's
`00-INDEX.md`, not here.

## Header

The ledger opens with front-matter.

| Field | Value |
|---|---|
| `project` | the project's slug |
| `kind` | `thought` or `library` |
| `language` | language of the chain's artefacts, ISO 639-1; English when absent |
| `updated` | date of the last update, `YYYY-MM-DD` |

## Tables

A project of kind `thought` keeps every table below.

### Briefs

One row per brief (`00-brief.md` and `00-brief-<name>.md`).

| Column | Holds |
|---|---|
| File | the brief's file |
| Version | its version |
| Status | `draft` (being composed) or `approved` (1.0 and on) |
| Mined | how far the intent has absorbed it |
| Note | what remains (when `partial`), or the rejected direction (when `dropped`) |

Mined words:

| Word | Meaning |
|---|---|
| `pending` | not yet absorbed |
| `partial` | partly absorbed; the Note says what remains |
| `mined` | absorbed |
| `dropped` | not taken up; the Note cites the rejected direction |

### Documents

One row per artefact below the brief level, starting with the intent.
A row is added when a layer is born; a layer the project does not have
gets no row.

| Column | Holds |
|---|---|
| File | the artefact's file |
| Version | its version |
| Status | `draft`, `approved` or `superseded`; it agrees with the version number, so an integer version is `approved` |
| Date | the date of the version |

### Renders

Generated outputs, one row per recipe in `recipes/`. A row mirrors the
provenance in the render's front-matter.

| Column | Holds |
|---|---|
| Render | the render |
| Audience | whom it is for |
| Recipe | the recipe it is made from |
| Inputs | what it was generated from |
| Generated | when it was generated |

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

State words: `current` is set by `/publish`; `stale` is set by every
`/render` of that recipe.

### Sources

Registration only: external inputs, immutable once registered.

| Column | Holds |
|---|---|
| File | the source's file or bundle |
| Date | best-effort origin date |
| Date origin | `content`, `file` or `ingested` |
| Form | `text`, `extract of <original>` or `binary`; one form per source |

### Dependencies

Registration only: documents of other repositories the project relies
on, typically library documents, cited by path. No version is kept,
because library documents are maintained by their owner.

| Column | Holds |
|---|---|
| Path | the path of the document |
| Library | the library it lives in |
| Used by | where it is used |
| Note | a note |

### Research

Registration only: immutable dated notes written by `/research`, or
recorded expert estimates.

| Column | Holds |
|---|---|
| File | the note |
| Date | its date |
| Derived from | what it was derived from |

### Findings

The findings of the critic and of the checks, in one sequence.

| Column | Holds |
|---|---|
| ID | the finding's ID |
| Severity | its severity |
| Category | its category |
| State | `open`, `resolved`, `rejected`, `parked` or `obsolete` |
| Source review | the review that raised it |
| Resolution | for `resolved`, the assignment version, or for a check's finding what fixed it; for `rejected`, a decision ID |

The word `overruled` in an older record reads as `rejected`.

### Challenges

The peer-review challenges.

| Column | Holds |
|---|---|
| ID | the challenge's ID |
| State | `open`, `accepted`, `rejected`, `parked` or `obsolete` |
| Headline | its headline |
| Source review | the challenge report that raised it |
| Resolution | for `accepted`, the intent version; for `rejected`, a decision ID |

## Waiting on principal

A list, one line per matter waiting on the principal. A matter that
has an ID gets one line: the ID, a few words and its state; its
substance stays in the thread or the record. Free text is for a matter
with no ID yet, which gets one at the next write. An unfinished
conversation is saved into its thread of the intent, never here.

## Library

A project of kind `library` keeps only Renders, Sources,
Dependencies, Research and Waiting on principal. The Briefs,
Documents, Published, Findings and Challenges tables are deleted at
scaffold time. The Findings table returns with a check's first
finding.

## See also

- [See where a project stands](../use/see-where-a-project-stands.md): reading the ledger through `/ledger`.
