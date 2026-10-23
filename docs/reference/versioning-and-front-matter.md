---
generated: 2026-10-23
version: 5.33
made: mirrored
inputs-hash: da4695095f6a496c
inputs:
  - CLAUDE.md#Versioning & status
  - templates/intent.md
  - templates/brief.md
  - templates/recipe.md
  - templates/work.md
  - templates/index.md
---

# Versioning and front-matter

This page states the version scheme of the forge and the header fields (the front-matter) of an artefact, a brief, a recipe, a work specification and a resource index. It is for anyone who reads or writes these files and needs the fields exactly as they stand.

## The version scheme

Integers denote signed-off versions.

| Version | Meaning |
|---|---|
| `0.1`, `0.2`, ... | drafts before the first approval |
| `1.0` | approved |
| `1.1`, `1.2`, ... | changes made after approval, not yet approved themselves |
| `2.0` | the next approved version, incorporating all changes since `1.0` |

## What a header carries

A header carries nothing that changes with a round of work. It holds `version` and `status`, and beside them what does not change with the work: `project`, a brief's `title` and `author`, an index's `directory`.

The date and the last change of a document are not in its header. They are computed from its history by whatever reads them (the `/history` command, the ledger).

## The status rule

- `status` takes one of `draft`, `approved`, `superseded`.
- Status must agree with the number: an integer version is `approved`, anything else is not.
- A recipe carries no status and stays at a `0.x` version.

## Header fields by document

### Artefact (the intent, and the other documents of the chain)

The fields below are those of the intent template.

| Field | Value |
|---|---|
| `version` | the version, `0.1` in a new document |
| `status` | `draft`, `approved` or `superseded` |
| `project` | the slug of the project |
| `audience` | for whom the document is written (the template gives `principal + Claude only`) |

### Brief

| Field | Value |
|---|---|
| `project` | the slug of the project |
| `title` | the working title |
| `author` | the principal |
| `version` | the version, `0.1` in a new brief |
| `status` | `draft` in a new brief |

Only this header is fixed. The text below it is free-form.

### Recipe

| Field | Value |
|---|---|
| `project` | the slug of the project |
| `purpose` | the purpose of the render |
| `audience` | the audience of the render |
| `version` | the version, `0.1` in a new recipe |
| `output` | optional: a path that overrides the default `renders/<recipe>.md` |
| `languages` | optional: a list of languages, the first primary and the rest its translations, one render per language in `renders/<recipe>.<lang>.md` |

A recipe has no `status`.

### Work specification

| Field | Value |
|---|---|
| `version` | the version, `0.1` in a new specification |
| `status` | `draft`, `approved` or `superseded` |
| `project` | the slug of the project |
| `file` | `work/<name>.<ext>`: the file this specification makes, named by the work alone |

### Resource index

| Field | Value |
|---|---|
| `project` | the slug of the project |
| `directory` | `sources` or `research` |

A resource index has no `version` and no `status`.

## Companion and archive files

Every versioned document (every artefact, every recipe and every work specification) keeps its history in an append-only companion beside it.

| File | What it is |
|---|---|
| `<file>.history.md` | the companion: the log of the document, one record per change; the shape of a record is in the history companion page |
| `<file>.history.archive.md` | a history table written before the log, moved here as it stands and immutable from then on |

The companion is part of its document. It has no ledger row. The history of an item is a search of both files.

## See also

- [History companion](history-companion.md): the record's shape.
- [Versioning and history](../about/versioning-and-history.md): why.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.33 from the files the front-matter names; never edited by hand.
