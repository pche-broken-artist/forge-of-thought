---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 98f440b0d924f3c9
inputs:
  - templates/history.md
  - CLAUDE.md#Versioning & status
---

# History companion

This page states the shape of `<file>.history.md`, the companion that keeps the history of one versioned document, record by record. It is for the user who reads a history and for the extender who writes records. The principal is the person whose thinking is being forged.

## The file

The companion lies beside its document and is appended at the end, never rewritten. It has no ledger row and travels with its document.

Front-matter:

| Key | Value |
|---|---|
| `project` | the project's slug |
| `document` | the versioned document the history belongs to |

Body: the heading `# History — <file>`, then one record per line. Lines are not wrapped.

## The record line

```
- <date> | <version> | <author> | <subject> | <kind> | <reason> | Action: <what the user must do> | Was: <wording that ceased to hold>
```

The fields, in this order:

| Field | Content |
|---|---|
| date | the date of the change, `YYYY-MM-DD` |
| version | the version of the document at the change |
| author | the handle the instance file gives the principal; the author is the one who decided the change |
| subject | what changed (see Subject) |
| kind | one of the five kinds |
| reason | why the change was made |
| `Action:` | what the user must do after the change |
| `Was:` | the wording that ceased to hold |

## The five kinds

- `created`
- `changed`
- `closed`
- `removed`
- `approved`

## Subject

The subject is one of:

- an ID
- several IDs, where the whole line holds for each
- a place without an ID: a section, the file, or, in the forge's own project, the operating layer

## When a field is left out

- The reason is left out on `created`.
- `Action` and `Was` stand only where the record has them.
- `Was` is always last. Paragraphs in it are divided by `<br>`.
- A thread that closes gets a `closed` record with no `Was`. The rules of a thread are in `.claude/skills/forge/states/intent.md`, Threads and files.

## The author

The author is the handle the instance file gives its principal. Where the instance file gives none, a write that would append a record stops before it writes and offers `/setup`, which adds the line. The handle is never guessed.

## The two records at a document's birth

At the birth of a document there are two records:

```
- YYYY-MM-DD | 0.1 | <author> | <file> | created
- YYYY-MM-DD | 0.1 | <author> | POS.0010, POS.0020, THR.0010 | created
```

- The first is the record of the file.
- The second names every item born with it.

## Records of state

A record of state carries the current version and does not raise it. Its shapes:

| Matter | Where it is written | Record |
|---|---|---|
| the mining of a brief | the intent's history, the brief's file as subject | `00-brief-<name>.md \| changed \| mined: pending \| partial \| mined \| dropped, <note>` |
| a finding settled | the history of the artefact whose version settled it; the intent's history where no version did or the check was of the engine | `FND.NNNN \| closed \| <what fixed it>`, resolved for a finding |
| a challenge settled | as for a finding | `CHL.NNNN \| closed \| <what fixed it>`, accepted for a challenge |
| a work product made | the specification's history | `<file> \| changed \| state: current; made <date> from <the inputs with their versions>` |
| a specification written after a making | the specification's history | `<file> \| changed \| state: stale` |
| the principal's word that the file is his | the specification's history | `<file> \| changed \| state: by hand` |

## What is not a record

`rejected`, `parked` and `obsolete` are the verdict of a decision (see `templates/decisions.md`). They are never a record in a history.

## The archive rule

- A companion written before the log keeps its table untouched.
- It moves as it stands to `<file>.history.archive.md`, which is immutable from then on.
- The log begins with the next version.
- The history of an item is a search of both files.
- A Version History table in the body of a document, or in its companion, is a check finding. The move to the archive settles it, on the principal's word, project by project.

## See also

- [Versioning and front-matter](versioning-and-front-matter.md): the fields the companion feeds.
- [Read the history of an item](../use/read-the-history-of-an-item.md): reading one item's records by command.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
