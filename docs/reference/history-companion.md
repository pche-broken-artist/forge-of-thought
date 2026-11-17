---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 526c34623cf5726d
inputs:
  - templates/history.md
  - CLAUDE.md#Versioning & status
  - CLAUDE.md#Repository layout
---

# History companion

The history companion is the file `<file>.history.md` that lies beside a
versioned document and records what changed in it and why. This page
gives its shape record by record, for the user who reads it and the
extender who writes to it.

## The file

A history companion is part of its document: it has no row of the
ledger and travels with the document through git. Every versioned
document keeps one, whether an artefact, a recipe or a work
specification. The body of the document is its current state, and the
companion is the record.

The front-matter has two keys:

| Key | Holds |
|---|---|
| `project` | the slug of the project |
| `document` | the versioned document the history belongs to |

The heading is `# History - <file>`. The records follow as a list, one
record per line.

## The record line

One record per change, one line each, appended at the end and never
rewritten. Lines are not wrapped. The fields stand in this order,
divided by ` | `:

| Position | Field | Holds |
|---|---|---|
| 1 | date | the date of the change, `YYYY-MM-DD` |
| 2 | version | the version of the document at the change |
| 3 | author | the handle the instance file gives the principal |
| 4 | subject | what changed |
| 5 | kind | one of the five kinds |
| 6 | reason | why it changed |
| 7 | `Action:` | what the user must do |
| 8 | `Was:` | the wording that ceased to hold |

The full line reads:

```
- <date> | <version> | <author> | <subject> | <kind> | <reason> | Action: <what the user must do> | Was: <wording that ceased to hold>
```

The author is the one who decided the change. Where the instance file
gives no handle, a write that would append a record stops before it
writes and offers `/setup`, which adds the line. The handle is never
guessed.

## The five kinds

- `created`
- `changed`
- `closed`
- `removed`
- `approved`

## The subject

The subject is one of these:

- an ID
- several IDs, where the whole line holds for each
- a place without an ID: a section or the file
- in the forge's own project, the operating layer

## Fields left out

- `reason` is left out on `created`.
- `Action` and `Was` stand only where the record has them.
- `Was` is always last. Paragraphs inside it are divided by `<br>`.

## The two records at a document's birth

At the birth of a document, two records are written:

- one of the file, with the file as subject
- one naming every item born with it

```
- YYYY-MM-DD | 0.1 | <author> | <file> | created
- YYYY-MM-DD | 0.1 | <author> | POS.0010, POS.0020, THR.0010 | created
```

## Records of state

A record of state carries only the current version and does not raise
it. Its shapes:

- **The mining of a brief.** It stands in the intent's history, with
  the brief's file as subject:
  `00-brief-<name>.md | changed | mined: pending | partial | mined | dropped, <note>`.
- **A finding or a challenge settled.** The record is
  `FND.NNNN | closed | <what fixed it>`. It stands in the history of
  the artefact whose version settled it, or in the history of the
  intent where no version did or the check was of the engine. The
  word in the reason is `resolved` for a finding and `accepted` for a
  challenge.
- **A work product's state.** It stands in the history of its
  specification, in three shapes:
  - the making: `<file> | changed | state: current; made <date> from <the inputs with their versions>`
  - a write of the specification after a making: `<file> | changed | state: stale`
  - the principal's word: `<file> | changed | state: by hand`

## What is never a record

`rejected`, `parked` and `obsolete` are a decision's verdict, as the
template for decisions has it. They are never a record in a history.

## How a record is written

A record is appended at the end of the file through
`python scripts/forge-record.py`, in the same step as the change it
records, and never by an edit. The script is described on
[Scripts](scripts.md).

## The archive

Beside a history may stand `<file>.history.archive.md`: a history table
from before the log. It is immutable.

## See also

- [Versioning and front-matter](versioning-and-front-matter.md): the fields the companion feeds.
- [Read the history of an item](../use/read-the-history-of-an-item.md): reading one item's records by command.
- [Scripts](scripts.md): the record script, its two forms and what it refuses.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
