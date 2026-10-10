---
generated: 2026-10-10
made: mirrored
inputs-hash: 5c414df8f8443a1a
inputs:
  - templates/history.md
  - CLAUDE.md
---

# History companion

This page states the shape of the history companion, the file
`<file>.history.md` that sits beside every versioned document. It is
for the user who reads a history and the extender who writes records
into one.

## Where it lives

Every versioned document, every artefact and every recipe alike, keeps
its history in an append-only companion beside it, never in its own
body. The body is the current state; the companion is the record. The
companion is part of its document: it has no ledger row and travels
with the document through git.

## Front-matter

| Key | Value |
|---|---|
| `project` | the project's slug |
| `document` | the versioned document this history belongs to |

The heading below it is `# History - <file>`.

## The record line

One record per change, one line each, appended at the end and never
rewritten. A round is one version and as many records as it made
changes. The fields run in this order, divided by ` | `:

```
- <date> | <version> | <author> | <subject> | <kind> | <reason> | Action: <what the user must do> | Was: <wording that ceased to hold>
```

| Field | Content |
|---|---|
| date | the date of the change, `YYYY-MM-DD` |
| version | the version the change belongs to |
| author | the one who decided the change, by the handle the instance gives its principal |
| subject | what the record is about (see below) |
| kind | one of the five kinds |
| reason | why the change was made |
| `Action:` | what the user must do after the change |
| `Was:` | the wording that ceased to hold |

## The five kinds

| Kind |
|---|
| `created` |
| `changed` |
| `closed` |
| `removed` |
| `approved` |

## The subject

The subject is one of:

- an ID;
- several IDs, where the whole line holds for each;
- a place without an ID: a section, the file, or, in the forge's own
  project, the operating layer.

## Fields left out

- The reason is left out on a `created` record.
- `Action` and `Was` appear only where the record has them.
- `Was` is always last. Paragraphs inside it are divided by `<br>`.

## Lines are not wrapped

A record stays on one line, however long.

## Records at a document's birth

At the birth of a document there are two records, both at version 0.1
and kind `created`:

- one with the file as subject;
- one naming every item born with it.

```
- YYYY-MM-DD | 0.1 | <author> | <file> | created
- YYYY-MM-DD | 0.1 | <author> | POS.0010, POS.0020, THR.0010 | created
```

## The archive

A companion written before the log existed, one that holds a table, is
kept untouched. It moves as it stands to `<file>.history.archive.md`,
immutable from then on, and the log begins with the next version. The
history of an item is a search of both files. A Version History table
in the body of a document or in its companion is a `/check` finding,
settled by that move on the principal's word, project by project.

## See also

- [Versioning and front-matter](versioning-and-front-matter.md): the fields the companion feeds.
