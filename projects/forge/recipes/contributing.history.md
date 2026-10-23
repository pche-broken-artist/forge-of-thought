---
project: forge
document: recipes/contributing.md
---

# History — recipes/contributing.md

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

- 2026-10-04 | 0.1 | PCHe | recipes/contributing.md | created
- 2026-10-10 | 0.2 | PCHe | Inputs | changed | docs/README.md added, the documentation index for the three readers and where each begins; the documentation exists since 4.62 and the file did not say where a visitor finds his way; the principal's word of 2026-10-10.
- 2026-10-10 | 0.2 | PCHe | Instructions | changed | A section "Find your way" right after the opening: the documentation, the three readers, the two pages for whoever wants to change something; the pages of docs/ named among the generated files, a fix going into the file the page mirrors. The principal's word of 2026-10-10.
- 2026-10-10 | 0.2 | PCHe | Template | changed | The section "Find your way" after the opening; the document section names the pages of docs/. | Was: <Generated files and their recipes.>
- 2026-10-11 | 0.3 | PCHe | Instructions | changed | Who decides what, in one sentence, and what a pull request for a change of behaviour carries and does not carry: the page and CONTRIBUTING listed three things where the process has seven steps, and "the principal" stood for two people (documentation audit F.18). | Was: For a change of behaviour say what the pull request carries: the position in `projects/forge/10-intent.md` saying what is wanted and why, with its record in the history beside it; the item in `projects/forge/40-solution-design.md` where the change solves something; and the change itself.
- 2026-10-11 | 0.3 | PCHe | Template | changed | The placeholder of "A change of how the forge behaves" follows (the same record). | Was: <Why the chain comes first, in two sentences; what the pull request carries; talk first.>
