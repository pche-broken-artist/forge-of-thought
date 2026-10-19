---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 649e8642f06517c5
inputs:
  - CLAUDE.md#Versioning & status
  - templates/intent.md
  - templates/brief.md
  - templates/recipe.md
  - templates/work.md
  - templates/index.md
---

# Versioning and front-matter

This page states the version scheme and the header fields (the front-matter) of an artefact, a brief, a recipe, a work specification and a resource index, exactly as the forge has them. It is for anyone who writes, reads or checks these documents. The principal (the person whose thinking is forged) and Claude author them; the ledger (the forge's state table, made at read time) and the history read them.

## The version scheme

Integers denote signed-off versions.

| Version | Meaning |
|---|---|
| `0.1`, `0.2`, ... | drafts before first approval |
| `1.0` | approved |
| `1.1`, `1.2`, ... | changes made after approval, not yet approved themselves |
| `2.0` | the next approved version, incorporating all changes since `1.0` |

## The status rule

- `status` is one of `draft`, `approved`, `superseded`.
- Status agrees with the number: an integer version is `approved`, anything else is not.
- A recipe carries no status and stays at `0.x`.

## What a header carries

A header carries nothing that changes with a round. It holds `version` and `status`, beside what does not change with the work: `project`, a brief's `title` and `author`, an index's `directory`.

The date and the last change of a document are computed from its history by whatever reads them (the `/history` command, the ledger). They are never carried in the header.

## The header fields by document

### Artefact

| Field | Holds |
|---|---|
| `version` | the version, as the scheme above |
| `status` | `draft`, `approved` or `superseded` |
| `project` | the slug of the project |
| `audience` | who the document is for |

### Brief

| Field | Holds |
|---|---|
| `project` | the slug of the project |
| `title` | the working title |
| `author` | the principal who wrote the brief |
| `version` | the version, as the scheme above |
| `status` | `draft`, `approved` or `superseded` |

Only the header of a brief is fixed. The text below it is free-form.

### Recipe

| Field | Holds |
|---|---|
| `project` | the slug of the project |
| `purpose` | the purpose of the render |
| `audience` | who the render is for |
| `version` | the version, as the scheme above; no `status` |
| `output` | optional; a path that overrides the default `renders/<recipe>.md` |
| `languages` | optional; the first language is primary, the rest are its translations, one render per language at `renders/<recipe>.<lang>.md` |

### Work specification

| Field | Holds |
|---|---|
| `version` | the version, as the scheme above |
| `status` | `draft`, `approved` or `superseded` |
| `project` | the slug of the project |
| `file` | the file the specification makes, `work/<name>.<ext>`, named by the work alone |

### Resource index

| Field | Holds |
|---|---|
| `project` | the slug of the project |
| `directory` | `sources` or `research` |

## The companion and archive files

Every artefact, every recipe and every work specification keeps its history in a companion file beside it, never in its body.

| File | What it is |
|---|---|
| `<file>.history.md` | the append-only log, one record per change, in the shape `templates/history.md` owns |
| `<file>.history.archive.md` | a history table written before the log, moved here untouched; immutable from then on |

- The companion is part of its document. It has no ledger row.
- The history of an item is a search of both files.
- A Version History table in the body of a document, or in its companion, is a `/check` finding. The finding is settled by moving the table to the archive file, on the principal's word.

## See also

- [History companion](history-companion.md): the record's shape.
- [Versioning and history](../about/versioning-and-history.md): why.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
