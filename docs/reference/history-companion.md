---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 9e346369634532f1
inputs:
  - templates/history.md
  - CLAUDE.md#Versioning & status
---

# History companion

The history companion is the file `<file>.history.md` that lies beside a versioned document and records every change of it, one line per change. This page gives its shape exactly, for the person who reads it and for the one who extends the forge.

## Where it lies

Every versioned document keeps its history in a companion beside it, never in its own body. This holds for every artefact, every recipe and every work specification. The companion is part of its document: it has no ledger row and travels with the document through git.

The principal is the person whose thinking is being forged. The ledger is the state file the forge makes at read time from the documents.

## The front-matter

```
---
project: <slug>
document: <file>
---
```

- `project`: the slug of the project the document belongs to.
- `document`: the versioned document this history belongs to.

Below the front-matter comes the heading `# History — <file>`, then the records.

## The record line

One record is one line, appended at the end of the file and never rewritten. Lines are not wrapped.

```
- <date> | <version> | <author> | <subject> | <kind> | <reason> | Action: <what the user must do> | Was: <wording that ceased to hold>
```

| Field | What it holds |
|---|---|
| date | the date of the change, `YYYY-MM-DD` |
| version | the version of the document after the change |
| author | the handle the instance gives its principal; the one who decided the change |
| subject | what changed (see below) |
| kind | one of the five kinds (see below) |
| reason | why it changed |
| `Action:` | what the user must do after the change |
| `Was:` | the wording that ceased to hold |

The way to an item (why it changed, what was said, trials, measurements, the research that turned it) goes into its record and never into the item. The record is written in the same step as the change.

## The five kinds

- `created`
- `changed`
- `closed`
- `removed`
- `approved`

## The subject

The subject is one of these:

- an ID
- several IDs, where the whole line holds for each of them
- a place without an ID: a section, or the file
- in the forge's own project, the operating layer

## When a field is left out

- `reason` is left out on `created`.
- `Action` and `Was` stand only where the record has them.
- `Was` is always last. Paragraphs inside it are divided by `<br>`.
- A thread that closes gets a `closed` record with no `Was`.
- If the instance gives its principal no handle, a write that would append a record stops before it writes and offers `/setup`, which adds the line. The handle is never guessed.

## The two records at a document's birth

At the birth of a document there are two records:

- one record of the file
- one record naming every item born with it

```
- YYYY-MM-DD | 0.1 | <author> | <file> | created
- YYYY-MM-DD | 0.1 | <author> | POS.0010, POS.0020, THR.0010 | created
```

The IDs in the second line are placeholders that show the shape.

## Records of state

A record of state carries the current version and does not raise it. A round is otherwise one version and as many records as it made changes. There are three shapes.

**The mining of a brief.** It stands in the intent's history, with the brief's file as subject.

```
00-brief-<name>.md | changed | mined: pending | partial | mined | dropped, <note>
```

**A finding or a challenge settled.**

```
FND.NNNN | closed | <what fixed it>
```

- It stands in the history of the artefact whose version settled it.
- It stands in the history of the intent where no version settled it, or where the check was of the engine.
- The note is `resolved` for a finding and `accepted` for a challenge.

**A work product's state.** It stands in the history of its specification.

- The making: `<file> | changed | state: current; made <date> from <the inputs with their versions>`
- A write of the specification after a making: `<file> | changed | state: stale`
- The principal's word: `<file> | changed | state: by hand`

## What is never a record

`rejected`, `parked` and `obsolete` are a decision's verdict in the decisions file. They are never a record in a history companion.

## The archive

A companion written before the log existed keeps its table untouched. It moves as it stands to `<file>.history.archive.md`, immutable from then on, and the log begins with the next version. The history of an item is a search of both files.

A Version History table in the body of a document, or in its companion, is a finding of the check. It is settled by that move, on the principal's word, project by project.

## See also

- [Versioning and front-matter](versioning-and-front-matter.md): the fields the companion feeds.
- [Read the history of an item](../use/read-the-history-of-an-item.md): reading one item's records by command.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
