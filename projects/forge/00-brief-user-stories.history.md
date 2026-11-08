---
project: forge
document: 00-brief-user-stories.md
---

# History — 00-brief-user-stories.md

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


- 2026-11-02 | 0.1 | FT- | 00-brief-user-stories.md | created
- 2026-11-02 | 0.1 | FT- | Co chci, Proč, Z čeho vychází, Tvar story, Formulace, Kdy jsou hotové, Jak vznikají, Kontrola a výstup, Co nechci, Změna enginu navíc, Postup | created
- 2026-11-02 | 0.2 | FT- | Tvar story | changed | at the judgement of the handed-over definition: only Reference is mandatory, the other parts left out where empty; the export leaves out references to a POS, which the stakeholders never see | Was: `Risks` volitelně, vždy s mitigací nebo důsledky; `Note` volitelně, jen odkaz na přílohu či technickou analýzu s vysvětlením, co se za ním skrývá; `Questions` (otázka → vlastník); `Reference` povinně (BR, NFR, DEP… nebo POS).
- 2026-11-02 | 0.2 | FT- | Kdy jsou hotové | changed | edge cases are not mandatory | Was: - Každá story má edge cases, nebo výslovně „žádné“.
- 2026-11-02 | 0.3 | FT- | Tvar story | changed | the trial project cut too fine: variants of one function were drafted as stories of their own and the principal merged six stories into two; a story is now one function, its variants criteria and edge cases | Was: no bullet on the cut of a story
- 2026-11-02 | 0.3 | FT- | Jak vznikají | changed | the trial project cut too fine; the cut is now agreed before the stories are drafted, names and a short description without references, which the analyst does not recall by number | Was: Claude navrhne celý seznam z BRD (u malé změny z intentu) s vazbou ke každé story a analytik ho projde story po story.
- 2026-11-04 | 0.4 | FT- | Kontrola a výstup | changed | a paste of the table into Jira and Confluence came out garbled; the export without a table after the principal's new pattern example-user-stories-v2.md | Was: - Render podle receptu vyrobí přesně formát exportu z Confluence (`sources/example-user-stories.md`): pevné nadpisy a věta o účelu, tabulka ID | Popis, jedna story na řádek.
- 2026-11-06 | 0.5 | FT- | Postup | changed | the trial project named by its kind, not by its domain: the engine is public and the trial stays outside it | Was: the trial project named by its domain
- 2026-11-08 | 0.6 | PCHe | 00-brief-user-stories.md | changed | translated into English on the principal's word, the forge's project being public and English throughout (CLAUDE.md, prime directive 6, allows a brief in any language; the translation is the principal's choice); the Czech original is version 0.5 in git; the sections renamed: Co chci → What I want, Proč → Why, Z čeho vychází → What it starts from, Tvar story → The shape of a story, Formulace → Wording, Kdy jsou hotové → When they are done, Jak vznikají → How they are made, Kontrola a výstup → Check and output, Co nechci → What I do not want, Změna enginu navíc → A change of the engine besides, Postup → The way | Was: the Czech text of 0.5
