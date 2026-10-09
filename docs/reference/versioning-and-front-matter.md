---
generated: 2026-10-09
made: mirrored
inputs:
  - CLAUDE.md
  - templates/intent.md
  - templates/brief.md
  - templates/recipe.md
---

# Versioning and front-matter

This page lists the version scheme, the front-matter fields of an
artefact and of a recipe, the rule that ties status to the version
number, and the names of the history files. It is for anyone who reads
or writes the documents of a project and needs the exact fields.

## Version scheme

Integers denote signed-off versions.

| Version | Meaning |
|---|---|
| `0.1`, `0.2`, … | drafts before first approval |
| `1.0` | approved |
| `1.1`, `1.2`, … | changes made after approval, not yet approved themselves |
| `2.0` | the next approved version, incorporating all changes since `1.0` |

## Front-matter of an artefact

Every artefact opens with a front-matter block. The intent's skeleton
carries these fields:

| Field | Content |
|---|---|
| `version` | the version number, as in the scheme above |
| `date` | date of the version, `YYYY-MM-DD` |
| `status` | `draft`, `approved` or `superseded` |
| `last_change` | derived from the records of the newest version in the document's history companion; never written by hand |
| `project` | the project's slug |
| `audience` | who reads the document (the intent's skeleton: principal and Claude only) |

The brief's skeleton has a header of its own: `project`, `title`
(working title), `date`, `author`, `version`, `status` and
`last_change`. Only this header is fixed in a brief; the text below it
is free-form.

### Status words

| Word | Use |
|---|---|
| `draft` | the version is not an integer |
| `approved` | the version is an integer |
| `superseded` | the document has been replaced |

### Status rule

Status must agree with the number: an integer version is `approved`,
anything else is not.

## Front-matter of a recipe

| Field | Content |
|---|---|
| `project` | the project's slug |
| `purpose` | what the render is for |
| `audience` | who reads the render |
| `version` | the version number; a recipe stays `0.x` |
| `updated` | date of the last change, `YYYY-MM-DD`; takes the place of `date` |
| `last_change` | derived from the records of the newest version in `recipes/<recipe>.history.md` |
| `output` | optional; a path that overrides the default `renders/<recipe>.md` |

A recipe has no `status` field.

## Companion and archive files

Every versioned document, every artefact and every recipe alike, keeps
its history in an append-only companion beside it, never in its body.

| File | Holds |
|---|---|
| `<file>.history.md` | the history of `<file>`: one record per change |
| `<file>.history.archive.md` | a history table written before the log; immutable |
| `recipes/<recipe>.history.md` | the history of a recipe |

A companion has no ledger row and is handed over with its document.

## See also

- [History companion](history-companion.md): the record's shape.
- [About versioning and history](../about/versioning-and-history.md): why.
