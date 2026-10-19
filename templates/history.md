---
project: <slug>
document: <file>          # the versioned document this history belongs to
---

# History — <file>

<!-- The history of a versioned document: CLAUDE.md, Versioning &
status. One record per change, one line each, appended at the end,
never rewritten:
- <date> | <version> | <author> | <subject> | <kind> | <reason> | Action: <what the user must do> | Was: <wording that ceased to hold>
Kinds: created | changed | closed | removed | approved. The subject
is an ID, several IDs where the whole line holds for each, or a
place without an ID: a section, the file, or in the forge's own
project the operating layer. Reason is left out on
`created`; `Action` and `Was` only where the record has them, `Was`
always last, paragraphs in it divided by `<br>`; a thread that
closes gets a `closed` record saying when and by what, no `Was`:
the closed file is the archive (POS.1680). At the birth of a
document, one record of the file and one naming every item born
with it. Lines are not wrapped.
A record of state only carries the current version and does not
raise it (POS.1630). Its shapes: the mining of a brief, in the
intent's history with the brief's file as subject,
`00-brief-<name>.md | changed | mined: pending | partial | mined |
dropped, <note>`; a finding or a challenge settled, `FND.NNNN |
closed | <what fixed it>`, in the history of the artefact whose
version settled it, or of the intent where no version did or the
check was of the engine, resolved for a finding, accepted for a
challenge; a work product's state, `<file> | changed | state: by
hand` or the making's record, in its specification's history.
`rejected`, `parked` and `obsolete` are a decision's Verdict
(templates/decisions.md), never a record here (POS.1610). -->

- YYYY-MM-DD | 0.1 | <author> | <file> | created
- YYYY-MM-DD | 0.1 | <author> | POS.0010, POS.0020, THR.0010 | created
