---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 60040c95ff44af25
inputs:
  - templates/history.md
  - CLAUDE.md#Versioning & status
---

# History companion

The history companion is the file `<file>.history.md` that sits beside a versioned document and records every change made to it. This page gives its shape, record by record, for the user who reads it and for the extender who writes records.

## The file

The companion has a front-matter of two keys, a heading and the records.

| Part | Content |
|---|---|
| `project` | the slug of the project |
| `document` | the versioned document the history belongs to |
| heading | `# History — <file>` |
| records | one line each, appended at the end, never rewritten |

Lines are not wrapped.

## The record line

One record is one line. Its fields come in this order, divided by ` | `:

```
<date> | <version> | <author> | <subject> | <kind> | <reason> | Action: <what the user must do> | Was: <wording that ceased to hold>
```

| Field | Content |
|---|---|
| date | the date of the change, `YYYY-MM-DD` |
| version | the version of the document the change belongs to |
| author | the one who decided the change, by the handle the instance gives its principal (the person whose thinking is forged) |
| subject | what changed: an ID, or a place without an ID |
| kind | one of the five kinds below |
| reason | why the item changed: what was said, trials, measurements, which research turned it |
| `Action:` | what the user must do after the change |
| `Was:` | the wording that ceased to hold |

## The five kinds

- `created`: the item or the file is born.
- `changed`: the item has a new wording.
- `closed`: the item is settled and closes.
- `removed`: the item is taken out.
- `approved`: the version is signed off.

## The subject

The subject is one of:

- an ID.
- several IDs, where the whole line holds for each of them.
- a place without an ID: a section, or the file.
- in the forge's own project, the operating layer.

## Fields left out

- `reason` is left out on `created`.
- `Action` is written only where the record has an action.
- `Was` is written only where the record has a wording that ceased to hold.
- `Was` is always last.
- Paragraphs inside `Was` are divided by `<br>`.
- A thread that closes carries its last text in `Was`.

## The two records at a document's birth

At the birth of a document there are two records:

- one of the file.
- one naming every item born with it.

```
YYYY-MM-DD | 0.1 | <author> | <file> | created
YYYY-MM-DD | 0.1 | <author> | <ID>, <ID>, <ID> | created
```

Each is written as a list item with a leading `- ` in the file.

## Rules of the log

- The log is append-only: a record is added, never rewritten.
- A round is one version and as many records as it made changes.
- A record is written in the same step as the change it records.
- The way to an item goes into its record, never into the item.
- The companion is part of its document: it has no ledger row and is handed over with the document by the link into git.
- The log is the single primary: the commit messages that a save and a release draft, and the release notes, are derived from it.

## The archive

A companion written before the log keeps its table untouched. It moves as it stands to `<file>.history.archive.md`, immutable from then on, and the log begins with the next version. The history of an item is a search of both files. A Version History table in the body of a document, or in its companion, is a finding of a check, settled by that move on the principal's word, project by project.

## See also

- [Versioning and front-matter](versioning-and-front-matter.md): the fields the companion feeds.
- [Read the history of an item](../use/read-the-history-of-an-item.md): reading one item's records by command.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
