---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 19f4242eeadc4714
inputs:
  - templates/history.md
  - CLAUDE.md#Versioning & status
---

# History companion

The history companion is the file `<file>.history.md` that lies beside every versioned document and records each change to it, one line per change. This page gives its shape exactly, for the user who reads it and the extender who writes records into it.

## Where it lives

Every versioned document keeps its history in a companion beside it, never in its body. Artefacts, recipes and work specifications alike have one, with no exception. The body is the current state; the companion is the record. The companion is part of its document: it has no row in the ledger (the state report made at read time) and is handed over with the document through git. It is append-only.

## Front-matter

```
---
project: <slug>
document: <file>
---
```

- `project`: the slug of the project the document belongs to.
- `document`: the versioned document the history belongs to.

The title below the front-matter is `# History - <file>`.

## The record line

One record per change, one line each, appended at the end and never rewritten. Lines are not wrapped.

```
- <date> | <version> | <author> | <subject> | <kind> | <reason> | Action: <what the user must do> | Was: <wording that ceased to hold>
```

The fields stand in this order:

| Field | Holds |
|---|---|
| date | the date of the change |
| version | the version the change made, or the current one for a record of state |
| author | the one who decided the change, by the handle the instance file gives the principal (the person whose thinking is forged) |
| subject | what changed (see Subject) |
| kind | one of the five kinds |
| reason | why the change was made |
| `Action:` | what the user must do after the change |
| `Was:` | the wording that ceased to hold |

A round of work is one version and as many records as it made changes.

## The five kinds

- `created`: the thing was born.
- `changed`: the thing was altered.
- `closed`: the thing was settled and shut.
- `removed`: the thing was taken away.
- `approved`: the version was signed off.

## Subject

The subject is one of these:

- an ID
- several IDs, where the whole line holds for each
- a place without an ID: a section, or the file
- in the forge's own project, the operating layer

## When a field is left out

- `reason` is left out on `created`.
- `Action` and `Was` appear only where the record has them.
- A thread that closes gets a `closed` record with no `Was`.

`Was` is always last. Paragraphs inside `Was` are divided by `<br>`.

## The author

The author is the handle the instance file gives the principal. Where the instance file gives none, a write that would append a record stops before it writes and offers `/setup`, which adds the line. The handle is never guessed.

## The two records at a document's birth

At the birth of a document there are two records:

```
- YYYY-MM-DD | 0.1 | <author> | <file> | created
- YYYY-MM-DD | 0.1 | <author> | POS.0010, POS.0020, THR.0010 | created
```

The first is of the file. The second names every item born with it.

## Records of state

A record of state carries the current version and does not raise it. There are three shapes.

The mining of a brief is written in the history of the intent, with the brief's file as subject:

```
- <date> | <version> | <author> | 00-brief-<name>.md | changed | mined: pending | partial | mined | dropped, <note>
```

A finding or a challenge settled is written as:

```
- <date> | <version> | <author> | FND.NNNN | closed | <what fixed it>
```

- It goes into the history of the artefact whose version settled it.
- It goes into the history of the intent where no version settled it, or where the check was of the engine.
- The state is `resolved` for a finding and `accepted` for a challenge.

A work product's state is written in the history of its specification:

- After a making: `<file> | changed | state: current; made <date> from <the inputs with their versions>`
- After a write of the specification following a making: `<file> | changed | state: stale`
- On the principal's word: `<file> | changed | state: by hand`

## What is never a record

`rejected`, `parked` and `obsolete` are a decision's verdict. They are written in the decisions record, never in a history companion.

## The archive

A companion written before the log keeps its table untouched. It moves as it stands to `<file>.history.archive.md`, which is immutable from then on. The log begins with the next version. The history of an item is a search of both files.

A Version History table, in the body of a document or in its companion, is a finding of the conformance check. It is settled by that move, on the principal's word, project by project.

## See also

- [Versioning and front-matter](versioning-and-front-matter.md): the fields the companion feeds.
- [Read the history of an item](../use/read-the-history-of-an-item.md): reading one item's records by command.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
