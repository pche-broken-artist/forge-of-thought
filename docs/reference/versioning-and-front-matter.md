---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: b8117c9bfbff6974
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

This page states the version scheme of the forge and the header fields (the front-matter) of an artefact, a brief, a recipe, a work specification and a resource index. It is for anyone who reads or writes these headers and needs the fields exactly. The terms of the forge are one line each in the [Glossary](glossary.md).

## The version scheme

Integers denote signed-off versions.

| Version | Meaning |
|---|---|
| `0.1`, `0.2`, ... | drafts before first approval |
| `1.0` | approved |
| `1.1`, `1.2`, ... | changes made after approval, not yet approved themselves |
| `2.0` | the next approved version, incorporating all changes since `1.0` |

## What a header carries

A header carries nothing that changes with a round of work. It carries `version` and `status`, and beside them what does not change with the work: `project`, a brief's `title` and `author`, an index's `directory`.

The date and the last change of a document are computed from its history by whatever reads them. They are never carried in the header.

## The status rule

`status` is one of `draft`, `approved` or `superseded`. Status must agree with the number:

- An integer version is `approved`.
- Any other version is not `approved`.
- A recipe carries no status and stays at `0.x`.

## The header fields by document

### An artefact (the intent, and the other artefacts of the chain)

The shape is that of the intent template.

| Field | Value |
|---|---|
| `version` | the version, as above (`0.1` in a new document) |
| `status` | `draft`, `approved` or `superseded` |
| `project` | the project's slug |
| `audience` | who the document is for |

### A BRD

A BRD has the four fields of an artefact and adds one.

| Field | Value |
|---|---|
| `version` | the version, as above |
| `status` | `draft`, `approved` or `superseded` |
| `project` | the project's slug |
| `parent` | the document it descends from: `20-assignment.md` or `10-intent.md` |

A BRD made from a source is a work product, not an artefact of the chain.

### A brief

Only the header is fixed. The text below it is free-form.

| Field | Value |
|---|---|
| `project` | the project's slug |
| `title` | a working title |
| `author` | the principal who wrote the brief |
| `version` | the version, as above |
| `status` | as above |

### A recipe

| Field | Value |
|---|---|
| `project` | the project's slug |
| `purpose` | what the render is for |
| `audience` | who the render is for |
| `version` | the version, always `0.x`; a recipe has no `status` |
| `output` | optional: a path that overrides the default `renders/<recipe>.md` |
| `languages` | optional: the first language is primary, the rest are its translations; one render per language, `renders/<recipe>.<lang>.md` |

### A work specification

| Field | Value |
|---|---|
| `version` | the version, as above |
| `status` | `draft`, `approved` or `superseded` |
| `project` | the project's slug |
| `file` | the file this specification makes, `work/<name>.<ext>`, named by the work alone |

### A resource index

The index of `sources/` and of `research/`.

| Field | Value |
|---|---|
| `project` | the project's slug |
| `directory` | `sources` or `research` |

An index carries no `version` and no `status`. A research note and a research plan carry no version either; their front-matter is on [Research note and bundle](research-bundle.md).

## The companion and the archive

Every versioned document keeps its history in a companion beside it, never in its body. Every artefact, every recipe and every work specification has one, without exception.

| File | What it is |
|---|---|
| `<file>.history.md` | the companion: an append-only log, one record per change |
| `<file>.history.archive.md` | a history table written before the log, kept untouched and immutable |

A recipe's companion is `recipes/<recipe>.history.md`. A work specification's companion is `work/<name>.spec.history.md`.

The companion is part of its document. It has no ledger row and is handed over with the document by the link into git.

A companion written before the log keeps its table untouched. The table moves as it stands to `<file>.history.archive.md`, and the log begins with the next version. A Version History table in the body of a document, or in its companion, is a finding of the conformance check. It is settled by that move, on the principal's word, project by project. The principal is the person whose thinking is being forged.

The shape of a record is on [History companion](history-companion.md). Why the history is kept apart from the document is on [Versioning and history](../about/versioning-and-history.md).

## See also

- [History companion](history-companion.md): the record's shape.
- [Versioning and history](../about/versioning-and-history.md): why.
- [Research note and bundle](research-bundle.md): the front-matter of a research note and plan, which carry no version.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
