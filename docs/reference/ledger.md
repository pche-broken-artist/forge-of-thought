---
generated: 2026-10-10
made: mirrored
inputs-hash: 0093e5e8cad1272b
inputs:
  - templates/ledger.md
  - CLAUDE.md
---

# Ledger

This page lists the ledger of a project as its template states it: the header fields, every table with its columns, the state words, and which tables a library keeps. It is for the user who reads or checks a ledger and for the extender who changes what it holds.

The ledger (`ledger.md`) is the single source of truth for state. It is freely rewritten and kept current after every operation. It cites and never copies: what a resource is and is for lives in the index of its directory, not in the ledger.

## Header

| Field | Meaning |
|---|---|
| `project` | The project's slug. |
| `kind` | `thought` or `library`. A ledger without it reads as `thought`. |
| `language` | The language of the chain's artefacts, as an ISO 639-1 code. English when absent. |
| `updated` | The date of the last update, `YYYY-MM-DD`. |

## Tables

### Briefs

One row per brief (`00-brief.md` and `00-brief-<name>.md`).

| Column | Content |
|---|---|
| File | The brief's file name. |
| Version | The brief's version. |
| Status | `draft` (being composed) or `approved` (version 1.0 and on, changed after that as any artefact is). |
| Mined | How far the intent has absorbed the brief. |
| Note | What remains, for `partial`; the rejected direction, for `dropped`. |

Mined words:

| Word | Reading |
|---|---|
| `pending` | Not yet absorbed. |
| `partial` | Partly absorbed; the Note says what remains. |
| `mined` | Absorbed. |
| `dropped` | Set aside; the Note names the rejected direction. |

### Documents

One row per layer below the intent, added when the layer is born. A layer the project does not have gets no row.

| Column | Content |
|---|---|
| File | The document's file name. |
| Version | Its version. |
| Status | Its status. |
| Date | Its date. |

### Renders

Generated outputs: one row per rendered recipe, written at the first render and kept by every later one. The row mirrors the render's provenance front-matter.

| Column | Content |
|---|---|
| Render | The render's file. |
| Audience | Whom it is for. |
| Recipe | The recipe it was made from. |
| Inputs | What it was made from. |
| Generated | When it was generated. |

The documentation index has a row here too, written by the documentation command. Its Recipe is "none, derived by `scripts/docs-index.py`", and its Inputs are the map with its generated date and the intent's version.

### Published

Designed files made by the publish command, one row per file.

| Column | Content |
|---|---|
| File | The published file. |
| Recipe | The recipe it belongs to. |
| From render | The render it was made from. |
| Model | The model that made it. |
| Published | When it was published. |
| State | `current` or `stale`. |

State words: `current` is set when the file is published; `stale` is set by every render of that recipe.

### Sources

Registration only. External inputs, immutable once registered.

| Column | Content |
|---|---|
| File | The source's file or bundle. |
| Date | Best-effort origin date. |
| Date origin | `content`, `file` or `ingested`. |
| Form | `text`, `extract of <original>` or `binary`: one form per source. |

### Dependencies

Registration only. Documents of other repositories the project relies on, typically library documents, cited by path. They carry no version, because library documents are maintained by their owner.

| Column | Content |
|---|---|
| Path | The path of the document. |
| Library | The library it lives in. |
| Used by | Where it is used (an index entry, a recipe or the chain). |
| Note | A note. |

### Research

Registration only. Immutable dated notes written by the research command, or recorded expert estimates.

| Column | Content |
|---|---|
| File | The note's file. |
| Date | Its date. |
| Derived from | What it was derived from. |

### Findings

Findings of the critic and of the checks, in one sequence.

| Column | Content |
|---|---|
| ID | The finding's ID. |
| Severity | Its severity. |
| Category | Its category. |
| State | See below. |
| Source review | The review that raised it. |
| Resolution | For `resolved`: the assignment version, or for a check's finding what fixed it. For `rejected`: the decision's ID. |

State words: `open`, `resolved`, `rejected`, `parked`, `obsolete`. The word `overruled` in an older record reads as `rejected`.

### Challenges

| Column | Content |
|---|---|
| ID | The challenge's ID. |
| State | See below. |
| Headline | The challenge in a line. |
| Source review | The review that raised it. |
| Resolution | For `accepted`: the intent version. For `rejected`: the decision's ID. |

State words: `open`, `accepted`, `rejected`, `parked`, `obsolete`.

### Waiting on principal

Not a table: one line per matter that waits on the principal. A matter that has an ID gets one line (the ID, a few words, its state), and its substance stays in the thread or the record. Free text is for a matter with no ID yet, which gets one at the next write.

## Which tables a library keeps

A project of kind `thought` keeps every table above. A project of kind `library` keeps only Renders, Sources, Dependencies, Research and Waiting on principal. The Briefs, Documents, Published, Findings and Challenges tables are deleted when the library is scaffolded. The Findings table returns with the first finding of a check.

## See also

- [See where a project stands](../use/see-where-a-project-stands.md): reading the ledger through `/ledger`.
