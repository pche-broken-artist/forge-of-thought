---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 2e0720d6dd144f41
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

This page states the version scheme of the forge and the header
fields of each versioned document and of the resource index. It is
for anyone who reads or writes a document header and wants the
fields exactly. The principal is the person whose thinking is being
forged.

## The version scheme

Integers denote signed-off versions.

| Version | Meaning |
|---|---|
| `0.1`, `0.2`, ... | drafts before first approval |
| `1.0` | approved |
| `1.1`, `1.2`, ... | changes made after approval, not yet approved themselves |
| `2.0` | the next approved version, incorporating all changes since `1.0` |

## What a header carries

A header carries `version` and `status`, beside what does not change
with the work: `project`, a brief's `title` and `author`, an index's
`directory`. It carries nothing that changes with a round of work.
The date and the last change of a document are computed from its
history by whatever reads them, never written in the header.

## The status rule

`status` is one of `draft`, `approved` or `superseded`. It agrees with
the number: an integer version is `approved`, anything else is not.
A recipe carries no status.

## Fields by document

### Artefact (for example the intent)

| Field | Value |
|---|---|
| `version` | the version, as above |
| `status` | `draft`, `approved` or `superseded` |
| `project` | the project's slug |
| `audience` | who reads the document (the intent's template gives "principal + Claude only") |

### BRD

The fields of an artefact, and one more:

| Field | Value |
|---|---|
| `parent` | the document the BRD comes from: `20-assignment.md` or `10-intent.md` |

A BRD made from a source is a work product, not a layer of the chain.

### Brief

| Field | Value |
|---|---|
| `project` | the project's slug |
| `title` | the working title |
| `author` | the principal's handle |
| `version` | the version, as above |
| `status` | `draft`, `approved` or `superseded` |

Only the header is fixed. The text below it is free-form. A later
brief is a file `00-brief-<name>.md`.

### Recipe

| Field | Value |
|---|---|
| `project` | the project's slug |
| `purpose` | what the render is for |
| `audience` | who reads the render |
| `version` | the version, starting at `0.1` |
| `output` | optional: a path that overrides the default `renders/<recipe>.md`; read relative to the project root, a leading slash meaning the engine root |
| `languages` | optional: a list in which the first language is primary and the rest are its translations, one render per language in `renders/<recipe>.<lang>.md` |

A recipe has no `status`. It stays at `0.x` unless the principal names
an integer. From that integer the count goes on. Claude never proposes
one.

### Work specification

The fields of an artefact (`version`, `status`, `project`), and one
more:

| Field | Value |
|---|---|
| `file` | the file this specification makes, `work/<name>.<ext>`, named by the work alone |

### Resource index

| Field | Value |
|---|---|
| `project` | the project's slug |
| `directory` | `sources` or `research` |

An index carries no `version` and no `status`.

## The companion and archive files

Every versioned document keeps its history in a companion file
beside it, never in its body.

| File | What it is |
|---|---|
| `<file>.history.md` | the history companion, append-only |
| `<file>.history.archive.md` | a history table written before the log existed, moved here untouched and immutable |

Examples: the BRD's companion is `30-brd.history.md`, and a recipe's
is `recipes/<recipe>.history.md`. A Version History table in the body
of a document or in its companion is a finding that is settled by
moving the table to the archive file, on the principal's word.

## See also

- [History companion](history-companion.md): the record's shape.
- [Versioning and history](../about/versioning-and-history.md): why.
- [Research note and bundle](research-bundle.md): the front-matter of a research note and plan, which carry no version.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
