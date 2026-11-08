---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: f1c752283cc43397
inputs:
  - CLAUDE.md#Versioning & status
  - templates/intent.md
  - templates/brief.md
  - templates/brd.md
  - templates/user-stories.md
  - templates/recipe.md
  - templates/work.md
  - templates/index.md
---

# Versioning and front-matter

This page lists the version scheme of the forge and the header fields
(the front-matter) of each versioned document and of a resource index.
It is for anyone who reads or writes these headers: a user, an
extender or an evaluator. The principal is whoever's thinking is being
forged.

## The version scheme

Integers denote signed-off versions.

| Version | Meaning |
|---|---|
| `0.1`, `0.2`, ... | drafts before the first approval |
| `1.0` | approved |
| `1.1`, `1.2`, ... | changes made after approval, not yet approved themselves |
| `2.0` | the next approved version, incorporating all changes since `1.0` |

## What a header carries

A header carries nothing that changes with a round of work. It carries
`version` and `status`, and beside them what does not change with the
work: `project`, a brief's `title` and `author`, an index's
`directory`.

The date and the last change of a document are not in its header.
Whatever reads them computes them from the document's history.

## The status rule

`status` is one of `draft`, `approved` or `superseded`. Status must
agree with the number: an integer version is `approved`, anything
else is not.

A recipe carries no status. It stays at `0.x` unless the principal
names an integer, from which the count goes on. Claude never proposes
an integer for a recipe.

## Header fields by document

### Artefact

An artefact is a document of the chain, such as the intent.

| Field | Value |
|---|---|
| `version` | the version, as above |
| `status` | `draft`, `approved` or `superseded` |
| `project` | the project's slug |
| `audience` | who reads it (the intent's template gives `principal + Claude only`) |

A BRD and the user stories add `parent:`, the document they derive
from.

| Document | Values of `parent` |
|---|---|
| BRD | `20-assignment.md` or `10-intent.md` |
| User stories | `30-brd.md` or `10-intent.md` (a small change, on the principal's word) |

A BRD or user stories made from a source are a work product, not an
artefact of the chain.

### Brief

| Field | Value |
|---|---|
| `project` | the project's slug |
| `title` | the working title |
| `author` | the principal's handle |
| `version` | the version, as above |
| `status` | `draft`, `approved` or `superseded` |

Only this header of a brief is fixed. The text below it is free-form.

### Recipe

| Field | Value |
|---|---|
| `project` | the project's slug |
| `purpose` | what the render is for |
| `audience` | who the render is for |
| `version` | the version, as above; no `status` field |
| `output` | optional; a path that overrides the default `renders/<recipe>.md`, read relative to the project root, a leading slash meaning the engine root |
| `languages` | optional; the first language is primary, the rest are its translations, one render per language as `renders/<recipe>.<lang>.md` |

### Work specification

| Field | Value |
|---|---|
| `version` | the version, as above |
| `status` | `draft`, `approved` or `superseded` |
| `project` | the project's slug |
| `file` | the file this specification makes, as `work/<name>.<ext>`, named by the work alone |

### Resource index

| Field | Value |
|---|---|
| `project` | the project's slug |
| `directory` | `sources` or `research` |

An index carries no `version` and no `status`. The front-matter of a
research note and of a research plan, which carry no version either,
is on [Research note and bundle](research-bundle.md).

## The companion and the archive

Every versioned document keeps its history in an append-only companion
beside it, never in its body. The companion of a document is part of
it and has no ledger row.

| File | Name |
|---|---|
| Companion | `<file>.history.md` |
| Archive | `<file>.history.archive.md` |

The archive holds a history table written before the log. It is
immutable. The shape of a record is on
[History companion](history-companion.md).

Examples of companion names: `30-brd.history.md` for a BRD,
`35-user-stories.history.md` for user stories.

## See also

- [History companion](history-companion.md): the record's shape.
- [Versioning and history](../about/versioning-and-history.md): why.
- [Research note and bundle](research-bundle.md): the front-matter of a research note and plan, which carry no version.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
