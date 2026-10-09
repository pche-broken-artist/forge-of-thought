---
generated: 2026-10-09
made: mirrored
inputs:
  - templates/history.md
  - CLAUDE.md
---

# History companion

This page states the shape of `<file>.history.md`, the companion that
keeps the history of a versioned document, as the skeleton
`templates/history.md` owns it. It is for the user who reads a history
and for the extender who writes or checks one.

## Where it lives

Every versioned document, artefacts and recipes alike, keeps its
history in a companion `<file>.history.md` beside it, never in its
body. The companion is append-only: one record per change, one line
each, appended at the end, never rewritten. A round of work is one
version and as many records as it made changes.

## Front-matter

| Key | Value |
|---|---|
| `project` | the project's slug |
| `document` | the versioned document this history belongs to |

The heading is `# History - <file>`.

## The record line

```
- <date> | <version> | <author> | <subject> | <kind> | <reason> | Action: <what the user must do> | Was: <wording that ceased to hold>
```

| Field | Position | Content |
|---|---|---|
| date | 1 | the date of the change, `YYYY-MM-DD` |
| version | 2 | the version the change belongs to |
| author | 3 | the one who decided the change, by the handle the instance gives its principal |
| subject | 4 | what changed (below) |
| kind | 5 | one of the five kinds (below) |
| reason | 6 | why it changed |
| `Action:` | 7 | what the user must do after the change |
| `Was:` | last | the wording that ceased to hold |

## Kinds

`created`, `changed`, `closed`, `removed`, `approved`.

## The subject

The subject is one of:

- an ID;
- several IDs, where the whole line holds for each;
- a place without an ID: a section, the file, or, in the forge's own
  project, the operating layer.

## Fields left out

- The reason is left out on `created`.
- `Action` and `Was` appear only where the record has them.

## `Was`

`Was` is always the last field. Paragraphs within it are divided by
`<br>`.

## Lines are not wrapped

A record is one line and is never wrapped, unlike the prose of other
documents, which is hard-wrapped at about 72 columns.

## At a document's birth

Two records are written, both at the first version:

1. one record of the file, with the file as subject;
2. one record naming every item born with the document, as its
   subject, IDs listed.

Both carry kind `created` and no reason.

## The archive

A companion written before the log keeps its table untouched. It moves
as it stands to `<file>.history.archive.md`, which is immutable from
then on, and the log begins with the next version. The history of an
item is a search of both files. A Version History table in the body of
a document or in its companion is a `/check` finding, settled by that
move on the principal's word, project by project.

## See also

- [Versioning and front-matter](versioning-and-front-matter.md): the fields the companion feeds.
