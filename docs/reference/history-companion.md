---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: c6b3be25b4f947b7
inputs:
  - templates/history.md
  - CLAUDE.md#Versioning & status
---

# History companion

The history companion is the file `<file>.history.md` that lies beside a versioned document and records every change made to it. This page gives its shape, record by record, for the reader who writes or checks one. The principal is the person whose thinking is being forged; the ledger is the file that holds the state of a project.

## The file

Every versioned document has one companion: every artefact, every recipe and every work specification, no exception. The companion is append-only and is part of its document. It has no ledger row. It is handed over with the document by the link into git.

The body of the document is the current state. The companion is the record.

## Front-matter

| Field | Holds |
|---|---|
| `project` | the slug of the project |
| `document` | the versioned document this history belongs to |

The heading below it reads `# History - <file>`.

## The record line

One record per change, one line each, appended at the end and never rewritten. Lines are not wrapped. The fields are separated by ` | ` and stand in this order:

```
- <date> | <version> | <author> | <subject> | <kind> | <reason> | Action: <what the user must do> | Was: <wording that ceased to hold>
```

| Field | Holds |
|---|---|
| date | the date of the change, as `YYYY-MM-DD` |
| version | the version of the document that carries the change |
| author | the one who decided the change, by the handle the instance gives its principal |
| subject | what changed (see Subject) |
| kind | one of the five kinds (see Kind) |
| reason | why it changed |
| `Action:` | what the user must do after the change |
| `Was:` | the wording that ceased to hold |

A round of work is one version and as many records as it made changes.

## Kind

The kind is one of five words:

- `created`
- `changed`
- `closed`
- `removed`
- `approved`

A thread that closes gets a `closed` record, with no `Was`. The rules of a thread belong to the definition of the intent.

## Subject

The subject is one of these:

- one ID
- several IDs, where the whole line holds for each of them
- a place without an ID: a section, or the file
- in the forge's own project, the operating layer

## When a field is left out

- The reason is left out on `created`.
- `Action` is present only where the record has an action.
- `Was` is present only where the record has a wording that ceased to hold.
- `Was` is always the last field.
- Paragraphs inside `Was` are divided by `<br>`.

## What goes into a record

The way to an item goes into its record and never into the item. That covers why it changed, what was said, trials, measurements and which research turned it. The record is written in the same step as the change.

## The two records at a document's birth

At the birth of a document there are two records:

1. One record of the file, with the file as subject and kind `created`.
2. One record naming every item born with it, with the IDs as subject and kind `created`.

```
- YYYY-MM-DD | 0.1 | <author> | <file> | created
- YYYY-MM-DD | 0.1 | <author> | POS.0010, POS.0020, THR.0010 | created
```

## Records of state

A record of state carries the current version and does not raise it. It has these shapes:

| What it records | Where it stands | Shape |
|---|---|---|
| the mining of a brief | the history of the intent, with the brief's file as subject | `00-brief-<name>.md \| changed \| mined: pending \| partial \| mined \| dropped, <note>` |
| a finding settled | the history of the artefact whose version settled it, or of the intent where no version did or the check was of the engine | `FND.NNNN \| closed \| <what fixed it>`, with `resolved` as the word for a finding |
| a challenge settled | the same place | `FND.NNNN \| closed \| <what fixed it>` shape with `CHL.NNNN` as subject, with `accepted` as the word for a challenge |
| a work product made | the history of its specification | `<file> \| changed \| state: current; made <date> from <the inputs with their versions>` |
| a specification written after a making | the same history | `<file> \| changed \| state: stale` |
| the principal's word that the file is worked by hand | the same history | `<file> \| changed \| state: by hand` |

## What is never a record

`rejected`, `parked` and `obsolete` are the verdict of a decision, as the decisions template has them. They are never a record in a history.

## The archive

A companion written before the log keeps its table untouched. It moves as it stands to `<file>.history.archive.md`, immutable from then on, and the log begins with the next version. The history of an item is a search of both files.

A Version History table, in the body of a document or in its companion, is a finding of the check. It is settled by that move, on the principal's word, project by project.

## See also

- [Versioning and front-matter](versioning-and-front-matter.md): the fields the companion feeds.
- [Read the history of an item](../use/read-the-history-of-an-item.md): reading one item's records by command.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
