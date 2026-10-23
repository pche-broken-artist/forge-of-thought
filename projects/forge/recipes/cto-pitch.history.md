---
project: forge
document: recipes/cto-pitch.md
---

# History — recipes/cto-pitch.md

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
closes gets a `closed` record, no `Was` (the rules of a thread:
`.claude/skills/forge/states/intent.md`, Threads and files). At the birth of a
document, one record of the file and one naming every item born
with it. Lines are not wrapped. The author is the handle the
instance file gives its principal (CLAUDE.md, Versioning & status);
where it gives none, a write that would append a record stops before
it writes and offers `/setup`, which adds the line (POS.1050); the
handle is never guessed.
A record of state only carries the current version and does not
raise it (POS.1630). Its shapes: the mining of a brief, in the
intent's history with the brief's file as subject,
`00-brief-<name>.md | changed | mined: pending | partial | mined |
dropped, <note>`; a finding or a challenge settled, `FND.NNNN |
closed | <what fixed it>`, in the history of the artefact whose
version settled it, or of the intent where no version did or the
check was of the engine, resolved for a finding, accepted for a
challenge; a work product's state in its specification's history:
the making's record `<file> | changed | state: current; made <date>
from <the inputs with their versions>`, a write of the specification
after a making `<file> | changed | state: stale`, the principal's
word `<file> | changed | state: by hand`.
`rejected`, `parked` and `obsolete` are a decision's Verdict
(templates/decisions.md), never a record here (POS.1610). -->

- 2026-10-04 | 0.6 | PCHe | Instructions | changed | The status of block 4 was a fact of 2026-09-27 and no longer held: the solution design is a layer of the chain since intent 4.54 and the forge has its own, and the BRD layer is not built, its step paused by the principal on 2026-10-04. The variant for test analysts and UX/UI stands as it was, the principal's fact. The Template's placeholder follows. | Was: today the chain ends at the intent and the assignment; a BRD layer is in development and testing; a modified variant of the forge for test analysts and UX/UI is at the plan stage.
- 2026-10-04 | 0.6 | PCHe | Format | changed | The Published line written in the skeleton's shape with what the ledger records of the published file: the model; the template it was made with is recorded nowhere and is said so (FND.0750). | Was: Published file, made by `/publish` through a model: not set; `/publish` asks before its first run.
