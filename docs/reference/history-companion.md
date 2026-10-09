---
generated: 2026-10-09
made: mirrored
inputs-hash: e053db81385c8419
inputs:
  - templates/history.md
  - CLAUDE.md
---

# History companion

This page states the shape of the history companion, the file `<file>.history.md` that sits beside every versioned document. It is for anyone who reads or writes one, or who builds a tool or a new kind of document that has to keep one.

## Where it lives

Every versioned document, artefact and recipe alike, keeps its history in an append-only companion `<file>.history.md` beside it, never in its body. The body is the current state, the companion the record. The history is a log with one record per change. A round of work is one version and as many records as it made changes.

## Front-matter

| Key | Value |
|---|---|
| `project` | the project's slug |
| `document` | the versioned document this history belongs to |

The heading under it is `# History - <file>`.

## The record line

One record is one line, appended at the end of the file and never rewritten. The fields come in this order, divided by ` | `:

| Position | Field | Content |
|---|---|---|
| 1 | date | the date of the change, `YYYY-MM-DD` |
| 2 | version | the version of the document that carries the change |
| 3 | author | the one who decided the change, by the handle the instance gives its principal |
| 4 | subject | what changed, see below |
| 5 | kind | one of the five kinds, see below |
| 6 | reason | why it changed |
| 7 | `Action:` | what the user must do after the change |
| 8 | `Was:` | the wording that ceased to hold |

## The five kinds

| Kind | Used for |
|---|---|
| `created` | an item or a file is born |
| `changed` | an item is altered |
| `closed` | an item is settled |
| `removed` | an item is taken out |
| `approved` | a version is signed off |

## The subject

The subject is one of these:

- an ID;
- several IDs, where the whole line holds for each of them;
- a place without an ID: a section, the file, or, in the forge's own project, the operating layer.

## When a field is left out

- The reason is left out on `created`.
- `Action` and `Was` are written only where the record has them.
- `Was` is always last. Paragraphs inside it are divided by `<br>`.

## Lines are not wrapped

A record stays on one line however long it is. The hard wrap at about 72 columns that applies to prose elsewhere does not apply to the records.

## At a document's birth

A new document opens its history with two records, both with the first version:

1. one record of the file, with the file as subject;
2. one record naming every item born with the document.

Skeleton:

```
- YYYY-MM-DD | 0.1 | <author> | <file> | created
- YYYY-MM-DD | 0.1 | <author> | POS.0010, POS.0020, THR.0010 | created
```

## The archive

A companion written before the log existed keeps its old version table untouched. That table moves as it stands to `<file>.history.archive.md`, which is immutable from then on, and the log begins with the next version. The history of an item is a search of both files. A Version History table left in the body of a document, or in its companion, is a finding of the conformance check, settled by that move on the principal's word, project by project.

The companion is part of its document: it has no ledger row and is handed over with the document through git. `last_change` in the document's front-matter is derived from the records of the newest version.

## See also

- [Versioning and front-matter](versioning-and-front-matter.md): the fields the companion feeds.
