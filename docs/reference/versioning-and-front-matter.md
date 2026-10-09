---
generated: 2026-10-09
made: mirrored
inputs-hash: ae50c8fa30262e63
inputs:
  - CLAUDE.md
  - templates/intent.md
  - templates/brief.md
  - templates/recipe.md
---

# Versioning and front-matter

This page lists the version scheme of the forge, the front-matter fields of an artefact and of a recipe, the rule that ties status to the version number, and the names of the history files. It is for anyone who reads, extends or judges a project's documents and needs the exact fields.

## The version scheme

Integers denote signed-off versions.

| Version | Meaning |
|---|---|
| `0.1`, `0.2`, ... | drafts before first approval |
| `1.0` | approved |
| `1.1`, `1.2`, ... | changes made after approval, not yet approved themselves |
| `2.0` | the next approved version, incorporating all changes since `1.0` |

## Front-matter of an artefact

The artefact skeleton (shown by the intent) carries these fields.

| Field | Content |
|---|---|
| `version` | the version number, as in the scheme above; a new document starts at `0.1` |
| `date` | the date, `YYYY-MM-DD` |
| `status` | one of `draft`, `approved`, `superseded` |
| `last_change` | derived from the records of the newest version in the document's history companion |
| `project` | the project slug |
| `audience` | who the document is for (the intent skeleton gives "principal + Claude only") |

The brief has its own header, and only that header is fixed; the text below it is free-form. Its fields are `project`, `title` (a working title), `date`, `author`, `version`, `status` and `last_change`. Its `last_change` skeleton reads as a one-line note of the version, the date and what changed (`0.1 (YYYY-MM-DD): draft begun.`).

## Front-matter of a recipe

| Field | Content |
|---|---|
| `project` | the project slug |
| `purpose` | the purpose of the render |
| `audience` | who the render is for |
| `version` | the version number; a recipe stays `0.x` |
| `updated` | the date of the last update, `YYYY-MM-DD`, in place of `date` |
| `last_change` | derived from the records of the newest version in `recipes/<recipe>.history.md` |
| `output` | optional; a path that overrides the default `renders/<recipe>.md` |

A recipe has no `status`.

## The status rule

Status must agree with the number: an integer version is `approved`, anything else is not.

## History files

Every versioned document, every artefact and every recipe alike, keeps its history in an append-only companion beside it, never in its body.

| File | What it is |
|---|---|
| `<file>.history.md` | the history companion: a log, one record per change, in the shape `templates/history.md` owns |
| `<file>.history.archive.md` | a history table written before the log, moved here as it stands; immutable from then on |

For a recipe the companion is `recipes/<recipe>.history.md`. The history of an item is a search of both files. `last_change` is derived from the records of the newest version by the write step that appends them, never set by hand.

## See also

- [History companion](history-companion.md): the record's shape.
- [About versioning and history](../about/versioning-and-history.md): why.
