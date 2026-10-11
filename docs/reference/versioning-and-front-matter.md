---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 662334ae68123e91
inputs:
  - CLAUDE.md#Versioning & status
  - templates/intent.md
  - templates/brief.md
  - templates/recipe.md
---

# Versioning and front-matter

This page states the version scheme of the forge and the front-matter fields of an artefact, a brief and a recipe, for anyone who reads or writes these documents. An artefact is a document of the chain, such as the intent; a recipe is the file that says how a render is made. Terms of the forge are in the [Glossary](glossary.md).

## The version scheme

Integers denote signed-off versions.

| Version | Meaning |
|---|---|
| `0.1`, `0.2`, ... | drafts before the first approval |
| `1.0` | approved |
| `1.1`, `1.2`, ... | changes made after approval, not yet approved themselves |
| `2.0` | the next approved version, incorporating all changes since `1.0` |

## The status rule

Status has three words: `draft`, `approved`, `superseded`. Status must agree with the number: an integer version is `approved`, anything else is not. A recipe carries no status and stays 0.x.

## Front-matter fields

### Artefact

The fields are those of the intent template.

| Field | Holds |
|---|---|
| `version` | the version, in the scheme above |
| `date` | the date, as `YYYY-MM-DD` |
| `status` | `draft`, `approved` or `superseded` |
| `last_change` | derived from the records of the newest version in the history companion |
| `project` | the slug of the project |
| `audience` | who reads the document |

### Brief

The brief carries `title` and `author` where an artefact carries `audience`. Only its header is fixed; the text below it is free-form.

| Field | Holds |
|---|---|
| `project` | the slug of the project |
| `title` | the working title |
| `date` | the date, as `YYYY-MM-DD` |
| `author` | the principal, the person whose thinking is forged |
| `version` | the version, in the scheme above |
| `status` | `draft`, `approved` or `superseded` |
| `last_change` | derived from the records of the newest version in the history companion |

### Recipe

| Field | Holds |
|---|---|
| `project` | the slug of the project |
| `purpose` | the purpose of the render |
| `audience` | who the render is for |
| `version` | the version, always 0.x |
| `updated` | the date of the last update, as `YYYY-MM-DD`, in place of `date` |
| `last_change` | derived from the records of the newest version in the recipe's history companion |
| `output` | optional; a path that overrides the default `renders/<recipe>.md` |

A recipe has no `status`.

## `last_change`

`last_change` is derived from the records of the newest version by the write step that appends them. It is never written by hand.

## Companion and archive files

| File | What it is |
|---|---|
| `<file>.history.md` | the history companion: an append-only log beside every versioned document, artefact and recipe alike, one record per change |
| `<file>.history.archive.md` | a history table written before the log, moved here untouched and immutable from then on; the log begins with the next version |

The companion has no ledger row. A Version History table in the body of a document or in its companion is a finding of the conformance check, settled by the move to the archive file on the principal's word, project by project.

## See also

- [History companion](history-companion.md): the record's shape.
- [Versioning and history](../about/versioning-and-history.md): why.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
