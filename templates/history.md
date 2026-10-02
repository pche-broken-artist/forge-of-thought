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
always last, paragraphs in it divided by `<br>`. At the birth of a
document, one record of the file and one naming every item born
with it. Lines are not wrapped. -->

- YYYY-MM-DD | 0.1 | <author> | <file> | created
- YYYY-MM-DD | 0.1 | <author> | POS.0010, POS.0020, THR.0010 | created
