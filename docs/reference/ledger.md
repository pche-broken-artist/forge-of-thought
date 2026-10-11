---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 6f83e27e58f8cf5f
inputs:
  - templates/ledger.md
  - CLAUDE.md#Ledger
---

# Ledger

The ledger is the file `ledger.md` of a project: the single source of truth for the project's state. This page lists its header, its tables with their columns, its state words and the rules for what goes into it, for the user who reads a ledger and the extender who changes its shape.

## The rule of the ledger

- The ledger is freely rewritten.
- It is kept current after every operation.
- It cites and never copies: a matter that has an ID gets one line under Waiting on principal, made of the ID, a few words and its state. Its substance stays in the thread or the record.
- A matter with no ID yet is written as free text and gets an ID at the next write.
- An unfinished conversation is saved into its thread of the intent, never into the ledger.
- Sources and dependencies are registration only. What a source is and is for lives in the `00-INDEX.md` of its directory. A library document, cited by path, carries no version.
- A layer below the intent that a project does not have is not missing: it gets no row, and `/forge` and the checks say nothing of it.

## Header

The header is the front-matter of the file.

| Field | Meaning |
|---|---|
| `project` | The project's slug. |
| `kind` | `thought` or `library`. A ledger without it reads as `thought`. At an import that is a fact the command reports; at a check it is a finding with a one-line fix. |
| `language` | The language of the chain's artefacts, as an ISO 639-1 code. |
| `updated` | The date of the last update, `YYYY-MM-DD`. |

The title below the header reads `Ledger — <Project>`.

## Tables

| Table | Columns |
|---|---|
| Briefs | File, Version, Status, Mined, Note |
| Documents | File, Version, Status, Date |
| Renders | Render, Audience, Recipe, Inputs, Generated |
| Published | File, Recipe, From render, Model, Published, State |
| Sources | File, Date, Date origin, Form |
| Dependencies | Path, Library, Used by, Note |
| Research | File, Date, Derived from |
| Findings | ID, Severity, Category, State, Source review, Resolution |
| Challenges | ID, State, Headline, Source review, Resolution |

Waiting on principal is a list, one line per matter, not a table.

### Briefs

One row per brief: `00-brief.md` and every `00-brief-<name>.md`.

- Status: `draft` (being composed) or `approved` (version 1.0 and on; changed after that as any artefact is).
- Mined: `pending`, `partial`, `mined` or `dropped`. It says how far the intent has absorbed the brief.
- Note: says what remains for `partial`, or names the rejected direction for `dropped`.

### Documents

One row per layer of the chain, the intent first. A row is added when its layer is born. A layer the project does not have gets no row.

### Renders

One row per rendered recipe. `/render` writes it at the first render and every later render keeps it. The row mirrors the provenance in the render's front-matter.

The documentation index has a row too, written by `/document`:

- Recipe: `none, derived by scripts/docs-index.py`
- Inputs: the documentation map with its generated date, and the intent's version

### Published

One row per designed file made by `/publish`.

- State: `current` or `stale`. `/publish` sets it to `current`. Every `/render` of that recipe sets it to `stale`.

### Sources

Registration only. External inputs, immutable once registered.

- Date: the best-effort date of origin.
- Date origin: `content`, `file` or `ingested`.
- Form: `text`, `extract of <original>` or `binary`. A source has one form.

### Dependencies

Registration only. Documents of other repositories the project relies on, typically library documents, cited by path from an index entry, a recipe or the chain. They carry no version, because their owner maintains them. What a document is for is written where it is used.

### Research

Registration only. Immutable dated notes written by `/research`, or recorded expert estimates. What a note answers is written in `research/00-INDEX.md`.

### Findings

Findings of the critic and of the checks, in one sequence.

- State: `open`, `resolved`, `rejected`, `parked` or `obsolete`.
- Resolution for `resolved`: the assignment version, or, for a check's finding, what fixed it.
- Resolution for `rejected`: a decision ID.
- An older record that says `overruled` reads as `rejected`.

### Challenges

- State: `open`, `accepted`, `rejected`, `parked` or `obsolete`.
- Resolution for `accepted`: the intent version.
- Resolution for `rejected`: a decision ID.

### Waiting on principal

What waits on the principal, one line per matter, as the rule of the ledger above says.

## Tables by kind

| Kind | Tables kept |
|---|---|
| `thought` | every table above |
| `library` | Renders, Sources, Dependencies, Research and Waiting on principal |

A library deletes the Briefs, Documents, Published, Findings and Challenges tables when it is scaffolded. Its Findings table returns with the first finding of a check.

## Example

A header and the first rows of a new thought project, as the template shows them:

```
---
project: <slug>
kind: thought
language: en
updated: YYYY-MM-DD
---

## Briefs
| File | Version | Status | Mined | Note |
|---|---|---|---|---|
| 00-brief.md | 0.1 | draft | pending | — |

## Documents
| File | Version | Status | Date |
|---|---|---|---|
| 10-intent.md | 0.1 | draft | YYYY-MM-DD |
```

## See also

- [See where a project stands](../use/see-where-a-project-stands.md): reading the ledger through `/ledger`.
- [Documents and records](../about/documents-and-records.md): why the ledger is the single source of truth for state.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
