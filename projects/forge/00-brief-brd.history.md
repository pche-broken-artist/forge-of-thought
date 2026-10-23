---
project: forge
document: 00-brief-brd.md
---

# History — 00-brief-brd.md

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

- 2026-10-16 | 0.1 | PCHe | 00-brief-brd.md | created
- 2026-10-16 | 0.1 | PCHe | What I want, Why, The shape, What I do not want, The material, Still open | created
- 2026-10-16 | 0.2 | PCHe | the file | changed | the principal's judgement of the handed-over 0.1: it does not make much sense; for him the brief is about starting from the fork's BRD, already implemented in the forge, checking the standards for what is missing and improving it, since the base exists; he did not understand the assumptions listed (the option taken, a BRD from the intent, the sign-off, the report) nor CHL.0030, which were written in the forge's English in Czech words; the IDs of the fork listed and the first of them put to a verdict; the open points said plainly, none dropped | Was: A layer of the chain for business requirements: `30-brd.md`, below the assignment and above the solution design, where POS.0700 has foreseen it. … The analyst works the BRD as its principal, with Claude as the analyst's partner … Born through `/new-artefact brd` as the first real use of that command and of the definition shape (POS.1310, POS.1380) … The shape follows option 2 of the research of the fork's layer: a generic definition, the fork's substance where it held on real work, the instance's roster and publishing kept out of the engine.<br>Why: People already write BRDs with a model … What is proposed now must be worth it on its own …<br>The shape, as far as the mechanism is part of the idea: the finding, what must be found (the Map), the phasing mandatory, items with IDs, use cases at user-goal level, no new kind of reviewer, the instance's part to the library.<br>What I do not want: the fork's layer copied as it is; a roster that must be filled; a figure from the skeleton as a requirement; the company's names in the engine; a BRD that designs.<br>Still open: a BRD from the intent (assumed); the sign-off left to the instance (Claude's view); a BRD or the solution design for a coding agent; the report of THR.0360; CHL.0030 revisited; the first run on the agentic platform.
