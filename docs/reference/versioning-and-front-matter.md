---
generated: 2026-10-10
made: mirrored
inputs-hash: dd470b47f55f607c
inputs:
  - CLAUDE.md
  - templates/intent.md
  - templates/brief.md
  - templates/recipe.md
---

# Versioning and front-matter

This page lists the version scheme and the front-matter fields of the versioned documents, for anyone who reads or writes them: the user, the extender and the evaluator.

## Version scheme

Integers denote signed-off versions.

| Version | Meaning |
|---|---|
| `0.1, 0.2, …` | drafts before first approval |
| `1.0` | approved |
| `1.1, 1.2, …` | changes made after approval, not yet approved themselves |
| `2.0` | the next approved version, incorporating all changes since 1.0 |

## Front-matter of an artefact

An artefact of the chain (the intent is the template's example) carries these fields.

| Field | Content |
|---|---|
| `version` | the version, per the scheme above |
| `date` | the date of the version |
| `status` | `draft`, `approved` or `superseded` |
| `last_change` | derived from the records of the newest version in the document's history companion |
| `project` | the project's slug |
| `audience` | who the document is for |

A brief carries `title` and `author` in place of `audience`. Its fields are `project`, `title`, `date`, `author`, `version`, `status` and `last_change`. Below the header a brief is free-form.

## The status rule

Status must agree with the version number: an integer version is `approved`, anything else is not.

## Front-matter of a recipe

| Field | Content |
|---|---|
| `project` | the project's slug |
| `purpose` | the purpose of the render |
| `audience` | who the render is for |
| `version` | the version; a recipe stays 0.x |
| `updated` | the date of the last update, in place of `date` |
| `last_change` | derived from the records of the newest version in `recipes/<recipe>.history.md` |
| `output` | optional; a path that overrides the default `renders/<recipe>.md` |

A recipe carries no `status`.

## Companion and archive files

Every versioned document, artefacts and recipes alike, keeps its history in an append-only companion beside it, never in its body.

| File | What it is |
|---|---|
| `<file>.history.md` | the history companion: a log, one record per change |
| `<file>.history.archive.md` | a history table that was written before the log; moved there as it stood, immutable from then on |

`last_change` is derived from the records of the newest version by the step that appends them, never by hand. The shape of a record is `templates/history.md`'s.

## See also

- [History companion](history-companion.md): the record's shape.
- [About versioning and history](../about/versioning-and-history.md): why.
