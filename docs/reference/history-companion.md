---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 1f8d67a236a68694
inputs:
  - templates/history.md
  - CLAUDE.md#Versioning & status
---

# History companion

The history companion is the file `<file>.history.md` that lies beside a versioned document and records every change of it, one line per change. This page gives its shape exactly, for the user who reads it and for the extender who writes records into it.

## Where it lives

- Every versioned document has one companion: every artefact, every recipe and every work specification.
- The companion lies beside its document and is part of it. It has no ledger row.
- The body of the document is the current state. The companion is the record.
- A record is written in the same step as the change it records.
- The log is the single primary source: commit messages and release notes are derived from it.

## The front-matter

```
---
project: <slug>
document: <file>
---
```

- `project`: the slug of the project.
- `document`: the versioned document the history belongs to.

The heading below it is `# History - <file>`.

## The record line

One record is one line, appended at the end of the file and never rewritten. Lines are not wrapped.

```
- <date> | <version> | <author> | <subject> | <kind> | <reason> | Action: <what the user must do> | Was: <wording that ceased to hold>
```

The fields stand in this order:

| Field | What it holds |
|---|---|
| date | the date of the record, `YYYY-MM-DD` |
| version | the version of the document the record was written in |
| author | the handle of the one who decided the change |
| subject | what changed (see Subject) |
| kind | one of the five kinds |
| reason | why it changed |
| `Action:` | what the user must do after the change |
| `Was:` | the wording that ceased to hold |

The author is the handle the instance file gives its principal, that is, the person whose thinking is forged. Where the instance file gives none, a write that would append a record stops before it writes and offers `/setup`, which adds the line. The handle is never guessed.

## The five kinds

| Kind | Used for |
|---|---|
| `created` | an item or a file is born |
| `changed` | an item changes |
| `closed` | a thread closes, or a finding or a challenge is settled |
| `removed` | an item is taken away |
| `approved` | a version is signed off |

## The subject

The subject is one of:

- an ID
- several IDs, where the whole line holds for each
- a place without an ID: a section, or the file
- in the forge's own project, the operating layer

## When a field is left out

- `reason` is left out on `created`.
- `Action` and `Was` stand only where the record has them.
- `Was` is always last.
- Paragraphs inside `Was` are divided by `<br>`.
- A thread that closes gets a `closed` record without `Was`.

## The two records at a document's birth

At the birth of a document there are two records:

1. One record of the file, kind `created`.
2. One record naming every item born with it, kind `created`.

```
- YYYY-MM-DD | 0.1 | <author> | <file> | created
- YYYY-MM-DD | 0.1 | <author> | POS.0010, POS.0020, THR.0010 | created
```

## Records of state

A record of state carries the current version and does not raise it. Its shapes:

| What is recorded | Where | The record |
|---|---|---|
| the mining of a brief | the intent's history, the brief's file as subject | `00-brief-<name>.md \| changed \| mined: pending \| partial \| mined \| dropped, <note>` |
| a finding settled | the history of the artefact whose version settled it; the intent's history where no version did, or where the check was of the engine | `FND.NNNN \| closed \| <what fixed it>`, with the state `resolved` |
| a challenge settled | the same places | `CHL.NNNN \| closed \| <what fixed it>`, with the state `accepted` |
| a work product, made | the history of its specification | `<file> \| changed \| state: current; made <date> from <the inputs with their versions>` |
| a work product, specification written after a making | the history of its specification | `<file> \| changed \| state: stale` |
| a work product, by the principal's word | the history of its specification | `<file> \| changed \| state: by hand` |

In the mining record, the four states of a brief are `pending`, `partial`, `mined` and `dropped`.

## What is not a record

`rejected`, `parked` and `obsolete` are the verdict of a decision. They are never a record in a history.

## The archive

- A companion written before the log existed keeps its table untouched.
- That table moves as it stands to `<file>.history.archive.md`, immutable from then on.
- The log begins with the next version.
- The history of an item is a search of both files.
- A Version History table in the body of a document or in its companion is a `/check` finding. It is settled by that move, on the principal's word, project by project.

## See also

- [Versioning and front-matter](versioning-and-front-matter.md): the fields the companion feeds.
- [Read the history of an item](../use/read-the-history-of-an-item.md): reading one item's records by command.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
