---
project: forge
document: 00-brief-research.md
---

# History — 00-brief-research.md

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

- 2026-10-24 | 0.1 | PCHe | 00-brief-research.md | created
- 2026-10-24 | 0.1 | PCHe | What I want, Why now, What I take and what I do not, How I want it built, Later, Open | created
- 2026-10-24 | 0.2 | PCHe | How I want it built, Later | changed | the first trial on the Antigravity CLI (tmp/research/2026-10-24-trial/source-quality): the engine returned a full note in ten minutes; three of its fourteen sources invented or misnumbered (two arXiv IDs naming other papers, a blog that does not exist), two URLs wrong to real studies, every source "read partially" with no opening recorded; the URL check therefore moves from Later into the first version as scripts/forge-cite.py, and the principal's wish for a summary first (the bundle's Summary, the note's In short) is added; the headless permission question is answered by the trial (a headless run denies what it cannot ask about; --allow-all with --sandbox is the standard) and leaves Later | Was: Try it, tune it, and only then write it into the intent, the design and whatever else it touches.<br>Later: … the check of every cited URL as a program; … what a headless run does when a tool asks for permission; …
- 2026-10-24 | 0.3 | PCHe | How I want it built | changed | the principal's word during the first run the new way (the RFP research): the person says the depth, quick or deep, as a parameter in the shape /save --quick already has; without it Claude proposes the depth in the plan; quick keeps the card before the search, the note's shape and the citation check, and drops the second engine, the plan review and the synthesis
