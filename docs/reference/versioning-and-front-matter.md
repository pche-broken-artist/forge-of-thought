---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 835996396fe57663
inputs:
  - CLAUDE.md#Versioning & status
  - templates/intent.md
  - templates/brief.md
  - templates/recipe.md
  - templates/work.md
---

# Versioning and front-matter

This page states the version scheme of the forge and the front-matter fields of an artefact, a brief, a recipe and a work specification. It is for anyone who writes or checks the header of a versioned document. The reasons are on [Versioning and history](../about/versioning-and-history.md), and the terms are in the [Glossary](../reference/glossary.md).

## The version scheme

Integers denote signed-off versions.

| Version | Meaning |
|---|---|
| `0.1`, `0.2`, ... | drafts before the first approval |
| `1.0` | approved |
| `1.1`, `1.2`, ... | changes made after approval, not yet approved themselves |
| `2.0` | the next approved version, incorporating all changes since `1.0` |

## The status rule

The status is one of `draft`, `approved` or `superseded`.

The status agrees with the number: an integer version is `approved`, any other version is not.

A recipe carries no status and stays at a `0.x` version.

## The front-matter fields

### An artefact

The intent is the example the template gives. Every artefact carries the same fields.

| Field | Holds |
|---|---|
| `version` | the version, from `0.1` |
| `date` | the date, `YYYY-MM-DD` |
| `status` | `draft`, `approved` or `superseded` |
| `last_change` | derived from the records of the newest version in the history companion; never written by hand |
| `project` | the slug of the project |
| `audience` | who reads the document |

### A brief

Only the header is fixed; the text below it is free-form.

| Field | Holds |
|---|---|
| `project` | the slug of the project |
| `title` | the working title |
| `date` | the date, `YYYY-MM-DD` |
| `author` | the principal (the person whose thinking is forged) |
| `version` | the version, from `0.1` |
| `status` | `draft` at the start; the status rule above applies |
| `last_change` | derived from the records of the newest version in `00-brief.history.md` |

### A recipe

| Field | Holds |
|---|---|
| `project` | the slug of the project |
| `purpose` | the purpose of the render |
| `audience` | who reads the render |
| `version` | the version, from `0.1`; stays `0.x` |
| `updated` | the date of the last update, `YYYY-MM-DD`, in place of `date` |
| `last_change` | derived from the records of the newest version in `recipes/<recipe>.history.md` |
| `output` | optional; a path that overrides the default `renders/<recipe>.md` |
| `languages` | optional; a list such as `cs, en`: the first is primary, the rest are its translations, one render per language in `renders/<recipe>.<lang>.md` |

A recipe has no `status` and no `date`.

### A work specification

| Field | Holds |
|---|---|
| `version` | the version, from `0.1` |
| `date` | the date, `YYYY-MM-DD` |
| `status` | `draft`, `approved` or `superseded` |
| `last_change` | derived from the records of the newest version in `work/<name>.spec.history.md` |
| `project` | the slug of the project |
| `file` | `work/<name>.<ext>`: the file this specification makes, named by the work alone |

## The companion and the archive

Every versioned document keeps its history in an append-only companion beside it, never in its body. This holds for every artefact, every recipe and every work specification.

| File | Is |
|---|---|
| `<file>.history.md` | the history companion: a log with one record per change; a round is one version and as many records as it made changes |
| `<file>.history.archive.md` | a history table written before the log; it moves there as it stands, is immutable from then on, and the log begins with the next version |

The companion has no ledger row. It is handed over with its document by the link into git.

The shape of a record is on [History companion](../reference/history-companion.md).

`last_change` is derived by the write step that appends the records of the newest version.

## See also

- [History companion](../reference/history-companion.md): the record's shape.
- [Versioning and history](../about/versioning-and-history.md): why.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
