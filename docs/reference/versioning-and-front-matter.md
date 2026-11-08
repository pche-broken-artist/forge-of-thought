---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: c01e24df8981ed19
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

This page states the version scheme of the forge and the header fields (the front-matter) of an artefact, a brief, a recipe, a work specification and a resource index. It is for anyone who reads or writes these headers. The principal is whoever's thinking is being forged. The ledger is the state report that the forge makes from the documents at read time.

## The version scheme

Integers denote signed-off versions.

| Version | Meaning |
|---|---|
| `0.1`, `0.2`, ... | drafts before the first approval |
| `1.0` | approved |
| `1.1`, `1.2`, ... | changes made after approval, not yet approved themselves |
| `2.0` | the next approved version, incorporating all changes since `1.0` |

## What a header carries

A header carries nothing that changes with a round of work. It carries `version` and `status`, beside what does not change with the work: `project`, the `title` and `author` of a brief, the `directory` of an index.

The date and the last change of a document are computed from its history by whatever reads them. They are never carried in the header.

## The status rule

`status` is one of `draft`, `approved` or `superseded`. Status must agree with the number: an integer version is `approved`, anything else is not.

A recipe carries no status. It stays at `0.x` unless the principal names an integer, from which the count goes on. Claude never proposes one.

## Header fields by document

### Artefact (the intent)

| Field | Value |
|---|---|
| `version` | the version, as above |
| `status` | `draft`, `approved` or `superseded` |
| `project` | the project slug |
| `audience` | who the document is for; the template gives `principal + Claude only` |

### Artefact below the intent (a BRD, the user stories)

A BRD and the user stories carry the fields of the intent, without `audience`, and add one.

| Field | Value |
|---|---|
| `version` | the version, as above |
| `status` | `draft`, `approved` or `superseded` |
| `project` | the project slug |
| `parent` | the document it is made from |

The `parent` values the templates give:

- a BRD: `20-assignment.md` or `10-intent.md`
- the user stories: `30-brd.md` or `10-intent.md` (a small change, on the principal's word)

A BRD or user stories made from a source are a work product, not an artefact of the chain.

### Brief

| Field | Value |
|---|---|
| `project` | the project slug |
| `title` | a working title |
| `author` | the principal's handle |
| `version` | the version, as above |
| `status` | `draft`, `approved` or `superseded` |

Only the header is fixed. The text below it is free-form.

### Recipe

| Field | Value |
|---|---|
| `project` | the project slug |
| `purpose` | what the render is for |
| `audience` | who the render is for |
| `version` | `0.x`, an integer only on the principal's word |
| `output` | optional; a path that replaces the default `renders/<recipe>.md`, read relative to the project root, a leading slash meaning the engine root |
| `languages` | optional; a list such as `cs, en`, the first primary, the rest its translations, one render per language as `renders/<recipe>.<lang>.md` |

A recipe has no `status`.

### Work specification

| Field | Value |
|---|---|
| `version` | the version, as above |
| `status` | `draft`, `approved` or `superseded` |
| `project` | the project slug |
| `file` | the file this specification makes, `work/<name>.<ext>`, named by the work alone |

### Resource index

| Field | Value |
|---|---|
| `project` | the project slug |
| `directory` | `sources` or `research` |

An index carries no `version` and no `status`. A research note and a research plan also carry no version; their front-matter is on [Research note and bundle](research-bundle.md).

## Companion and archive files

Every versioned document keeps its history in an append-only companion beside it, never in its body. The companion is part of its document and has no ledger row.

| File | What it is |
|---|---|
| `<file>.history.md` | the history companion of a versioned document |
| `<file>.history.archive.md` | a history table written before the log, moved there as it stands, immutable |
| `recipes/<recipe>.history.md` | the history of a recipe |
| `work/<name>.spec.history.md` | the history of a work specification |

The shape of a record is on [History companion](history-companion.md). A Version History table in the body of a document, or in its companion, is a finding of the check, settled by moving it to the archive file on the principal's word, project by project.

The reasons for these rules are on [Versioning and history](../about/versioning-and-history.md).

## See also

- [History companion](history-companion.md): the record's shape.
- [Versioning and history](../about/versioning-and-history.md): why.
- [Research note and bundle](research-bundle.md): the front-matter of a research note and plan, which carry no version.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
