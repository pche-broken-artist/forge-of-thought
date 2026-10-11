---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: a0466f35e09606fd
inputs:
  - templates/history.md
  - CLAUDE.md#Versioning & status
---

# History companion

The history companion is the file `<file>.history.md` that lies beside every versioned document and records each change to it, one line per change. This page gives its shape exactly, for the user who reads it and the extender who writes it. A term of the forge that is not glossed here is in the [Glossary](glossary.md), and the fields the companion feeds are in [Versioning and front-matter](versioning-and-front-matter.md).

## Where it lies

| Fact | Value |
|---|---|
| Name | `<file>.history.md`, beside the document |
| Which documents | every versioned document, artefacts and recipes alike, without exception |
| Behaviour | append-only: a record is added at the end and never rewritten |
| Ledger row | none: the companion is part of its document |
| Hand-over | with the document, by the link into git |

## Front-matter

| Key | Value |
|---|---|
| `project` | the project's slug |
| `document` | the versioned document this history belongs to |

The heading under the front-matter is `# History - <file>`.

## The record line

One record is one line, appended at the end. The fields stand in this order, divided by ` | `:

```
- <date> | <version> | <author> | <subject> | <kind> | <reason> | Action: <what the user must do> | Was: <wording that ceased to hold>
```

| Position | Field | Holds |
|---|---|---|
| 1 | date | the date of the change, `YYYY-MM-DD` |
| 2 | version | the version of the document that carries the change |
| 3 | author | the one who decided the change, by the handle the instance gives its principal |
| 4 | subject | what the record is about (see Subject) |
| 5 | kind | one of the five kinds |
| 6 | reason | why the change was made |
| 7 | `Action:` | what the user must do after the change |
| 8 | `Was:` | the wording that ceased to hold |

## The five kinds

| Kind | Used for |
|---|---|
| `created` | an item or a document comes into being |
| `changed` | an item changes |
| `closed` | an item is closed |
| `removed` | an item is removed |
| `approved` | a version is approved |

## Subject

The subject is one of these:

- an ID
- several IDs, where the whole line holds for each of them
- a place without an ID: a section, or the file
- in the forge's own project, the operating layer

## When a field is left out

- The reason is left out on `created`.
- `Action` is written only where the record has one.
- `Was` is written only where the record has one.

## Order and form of the last fields

- `Was` is always the last field.
- Paragraphs inside a field are divided by `<br>`.
- Lines are not wrapped.

## The two records at a document's birth

At the birth of a document two records are written:

1. one record of the file
2. one record naming every item born with it

```
- YYYY-MM-DD | 0.1 | <author> | <file> | created
- YYYY-MM-DD | 0.1 | <author> | PREFIX.0010, PREFIX.0020 | created
```

## What goes into a record

The way to an item goes into its record and never into the item. That means why it changed, what was said, trials, measurements and which research turned it. The record is written in the same step as the change. A round is one version and as many records as it made changes.

## The archive

A companion written before the log keeps its table untouched. It moves as it stands to `<file>.history.archive.md`, which is immutable from then on. The log begins with the next version. The history of an item is a search of both files.

A Version History table, in the body of a document or in its companion, is a finding of the conformance check. The move to the archive settles it, on the principal's word, project by project.

## See also

- [Versioning and front-matter](versioning-and-front-matter.md): the fields the companion feeds.
- [Read the history of an item](../use/read-the-history-of-an-item.md): reading one item's records by command.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
