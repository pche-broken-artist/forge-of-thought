---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: deb14db38c1fa3eb
inputs:
  - CLAUDE.md#Versioning & status
  - templates/intent.md
  - templates/brief.md
  - templates/brd.md
  - templates/recipe.md
  - templates/work.md
  - templates/index.md
---

# Versioning and front-matter

This page states the version scheme of the forge and the header fields (the front-matter) of an artefact, a brief, a recipe, a work specification and a resource index. It is for anyone who writes, reads or checks these documents and needs the fields exactly.

## The version scheme

Integers denote signed-off versions.

| Version | Meaning |
|---|---|
| `0.1`, `0.2`, ... | drafts before the first approval |
| `1.0` | approved |
| `1.1`, `1.2`, ... | changes made after approval, not yet approved themselves |
| `2.0` | the next approved version, incorporating all changes since `1.0` |

## What a header carries

A header carries nothing that changes with a round of work. It holds `version` and `status`, beside what does not change with the work: `project`, a brief's `title` and `author`, an index's `directory`.

The date and the last change of a document are computed from its history by whatever reads them. They are never carried in the header.

## The status rule

`status` is one of `draft`, `approved` or `superseded`. Status must agree with the number: an integer version is `approved`, anything else is not. A recipe carries no status and stays at `0.x`.

## The fields by document

### Artefact (the intent, the assignment and the other documents of the chain)

The intent's template shows the header every artefact has.

| Field | Value |
|---|---|
| `version` | the version, starting at `0.1` |
| `status` | `draft`, `approved` or `superseded` |
| `project` | the project slug |
| `audience` | who the document is for |

### BRD

The fields of an artefact, and one more.

| Field | Value |
|---|---|
| `version` | as above |
| `status` | as above |
| `project` | the project slug |
| `parent` | the document the BRD descends from: `20-assignment.md` or `10-intent.md` |

### Brief

| Field | Value |
|---|---|
| `project` | the project slug |
| `title` | the working title |
| `author` | the principal's handle |
| `version` | the version, starting at `0.1` |
| `status` | `draft`, `approved` or `superseded` |

Only the header is fixed. The text below it is free-form.

### Recipe

| Field | Value |
|---|---|
| `project` | the project slug |
| `purpose` | what the render is for |
| `audience` | who the render is for |
| `version` | the version, starting at `0.1`; there is no `status` |
| `output` | optional: a path that overrides the default `renders/<recipe>.md` |
| `languages` | optional: the first language is primary, the rest are its translations, one render per language in `renders/<recipe>.<lang>.md` |

### Work specification

| Field | Value |
|---|---|
| `version` | the version, starting at `0.1` |
| `status` | `draft`, `approved` or `superseded` |
| `project` | the project slug |
| `file` | the file this specification makes, `work/<name>.<ext>`, named by the work alone |

### Resource index

| Field | Value |
|---|---|
| `project` | the project slug |
| `directory` | `sources` or `research` |

An index carries no `version` and no `status`.

## Companion and archive files

Every versioned document keeps its history in a companion beside it, never in its body. The companion is append-only.

| File | Holds |
|---|---|
| `<file>.history.md` | the history of the document, one record per change |
| `<file>.history.archive.md` | a history table written before the log, immutable |

A companion written before the log keeps its table untouched. It moves as it stands to `<file>.history.archive.md`, and the log begins with the next version. The history of an item is a search of both files. A Version History table in the body of a document, or in its companion, is a finding that this move settles.

## See also

- [History companion](history-companion.md): the record's shape.
- [Versioning and history](../about/versioning-and-history.md): why.
- [Research note and bundle](research-bundle.md): the front-matter of a research note and plan, which carry no version.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
