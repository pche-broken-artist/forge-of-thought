---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 1a9b06d14ef341b0
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

This page states the version scheme of the forge and the header
fields (the front-matter) of an artefact, a brief, a recipe, a work
specification and a resource index. It is for anyone who reads or
writes these documents and needs the fields exactly. The principal is
the person whose thinking is being forged.

## The version scheme

Integers denote signed-off versions.

| Version | Meaning |
|---|---|
| `0.1`, `0.2`, ... | drafts before the first approval |
| `1.0` | approved |
| `1.1`, `1.2`, ... | changes made after approval, not yet approved themselves |
| `2.0` | the next approved version, incorporating all changes since `1.0` |

## The status rule

- `status` is one of `draft`, `approved` or `superseded`.
- Status agrees with the number: an integer version is `approved`,
  anything else is not.
- A recipe carries no status.

## What a header carries

A header carries nothing that changes with a round of work. It holds
`version` and `status`, and beside them what does not change with the
work: `project`, the `title` and `author` of a brief, the `directory`
of an index.

The date and the last change of a document are computed from its
history by whatever reads them, never carried in the header.

## Header fields by document

| Document | Fields |
|---|---|
| Artefact (such as the intent) | `version`, `status`, `project`, `audience` |
| BRD | `version`, `status`, `project`, `parent` |
| User stories | `version`, `status`, `project`, `parent` |
| Brief | `project`, `title`, `author`, `version`, `status` |
| Recipe | `project`, `purpose`, `audience`, `version`, optional `output`, optional `languages` |
| Work specification | `version`, `status`, `project`, `file` |
| Resource index | `project`, `directory` |

### Artefact

- `version`: as the scheme above.
- `status`: `draft | approved | superseded`.
- `project`: the slug of the owning project.
- `audience`: who reads the document. The intent template carries
  `principal + Claude only`.

### BRD and user stories

These carry the artefact's fields and add `parent`, the document
the artefact is made from.

- BRD: `parent` is `20-assignment.md` or `10-intent.md`. A BRD made
  from a source is a work product, not an artefact of the chain.
- User stories: `parent` is `30-brd.md`, or `10-intent.md` for a
  small change on the principal's word. Stories made from a source
  are a work product.

### Brief

- `project`: the slug of the owning project.
- `title`: the working title.
- `author`: the principal.
- `version` and `status`: as the scheme above.

Only this header is fixed. The text below it is free-form.

### Recipe

- `project`, `purpose` and `audience`: the project's slug, what the
  render is for and who reads it.
- `version`: starts at `0.1` and stays `0.x`. An integer is set only
  on the principal's word, as his own mark and not as an approval.
  Claude never proposes one.
- No `status`.
- `output` (optional): a path that overrides the default
  `renders/<recipe>.md`. It is read relative to the project root, and
  a leading slash means the engine root.
- `languages` (optional): a list such as `cs, en`. The first is the
  primary and the rest are its translations, one render per language
  at `renders/<recipe>.<lang>.md`.

### Work specification

- `version`, `status` and `project`: as an artefact.
- `file`: the file the specification makes, `work/<name>.<ext>`,
  named by the work alone.

### Resource index

- `project`: the slug of the owning project.
- `directory`: `sources` or `research`.

An index carries no version and no status.

## The companion's file name

Every versioned document (every artefact, every recipe and every work
specification) keeps its history in an append-only companion beside
it, never in its body:

- `<file>.history.md`: the history companion.
- `<file>.history.archive.md`: a history table written before the
  log, immutable.

The body is the current state and the companion the record. Its shape
is on the page History companion.

## See also

- [History companion](history-companion.md): the record's shape, and the archive of a history written before the log.
- [Versioning and history](../about/versioning-and-history.md): why.
- [Research note and bundle](research-bundle.md): the front-matter of a research note and plan, which carry no version.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
