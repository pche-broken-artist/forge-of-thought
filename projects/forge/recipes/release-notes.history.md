---
project: forge
document: recipes/release-notes.md
---

# History — recipes/release-notes.md

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

- 2026-09-30 | 0.11 | PCHe | Inputs | changed | The archive of the intent's history added, for the versions before the log (step 3 of THR.0470).
- 2026-09-30 | 0.11 | PCHe | Instructions | changed | A section is derived from the records of the log, the kind giving the group and the Action carried word for word; a version before the log is compiled from its archived Notes (POS.0730, step 3 of THR.0470).
- 2026-10-02 | 0.12 | PCHe | Instructions | changed | The way to two instructions moved to the history: the migration one came from, and how the minors stood before 4.0 (FND.0520). | Was: (the migration of 2026-09-05, POS.0730) [...] The sections of 3.1–3.x in the current edition are therefore carried over verbatim until 4.0 and folded then.
- 2026-10-10 | 0.13 | PCHe | Inputs | changed | The solution design's history added, the layer below the intent the project has had since 4.59 (FND.1390).
- 2026-10-10 | 0.13 | PCHe | Instructions | changed | A section is derived from the log of every input history, the intent's and the layers' below it, as the skeleton says (FND.1390). | Was: in the log:
- 2026-10-25 | 0.14 | PCHe | the file | changed | FND.2710: the comment brought to templates/recipe.md as it stands. | Was: <!-- A recipe is the iterated thing; its render is generated output. Never polish a render by hand: change the recipe, run /render release-notes. Recipes are tools: version + updated date in front-matter and no status (a recipe is never approved); its history lives in the companion <recipe>.history.md, last_change derived from the records of the newest version. -->
- 2026-10-25 | 0.15 | PCHe | Instructions | changed | The fold applies to every major: the sections of 2.1 to 2.21, 1.1 to 1.24 and 0.1 to 0.11, compiled before the rule and carried over since, fold into 3.0, 2.0 and 1.0 at the next render (the fold of the old minors, deferred since 2026-10-23).
