---
date: 2026-10-12
project: forge
check: light
target: projects/forge
reviewer: check light (isolated context)
---

# Check (light) — C:\pche\_dev\forge-of-thought\projects\forge — 2026-10-12

2 findings

## Findings

### FND.1580 — low — The ledger has no Work table, and its header comment still lists the tables of a library without it
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:63-73` (the sections run Published → Sources; no `## Work` between them) and `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:16-19` (the `library` reduction names "Briefs, Documents, Published, Findings and Challenges"), against `C:\pche\_dev\forge-of-thought\templates\ledger.md:58-66` (the Work table with its comment; "Kind: `thought` keeps every table below", template line 16-19 naming Work among the tables a library drops), `C:\pche\_dev\forge-of-thought\CLAUDE.md:655-658` (the ledger's tables include "work products") and `C:\pche\_dev\forge-of-thought\.claude\skills\work\SKILL.md:20` and `:30` (bare `/work` reads the ledger's Work table; a birth writes its row into it, so the table is expected to stand before the first product).
- **Rule:** The ledger is shaped as `templates/ledger.md` says for its kind (CLAUDE.md, Ledger; the template's header comment is the one owner of the reduction by kind).
- **Fix:** immediate fix: insert the `## Work` section with the template's comment and empty table between Published and Sources, and bring the header comment to the template's wording (Work among the tables a library deletes). No `work/` directory exists in the project, so the table is empty: the normal case.

### FND.1590 — low — Twelve history companions carry the skeleton's comment as it stood before 5.4; one carries the current one
- **Where:** `10-intent.history.md:16-17`, `40-solution-design.history.md:16-17`, `00-brief-public-engine.history.md:16-17`, `00-brief-elicitation.history.md:16-17`, `00-brief-next-gen.history.md:16-17`, `00-brief-documentation.history.md:16-17`, `recipes/readme.history.md:16-17`, `recipes/release-notes.history.md:16-17`, `recipes/contributing.history.md:16-17`, `recipes/executive-pitch.history.md:16-17`, `recipes/cto-pitch.history.md:16-17`, `recipes/ceo-pitch.history.md:16-17` (all under `C:\pche\_dev\forge-of-thought\projects\forge\`): "`Was` always last, paragraphs in it divided by `<br>`. At the birth of a document", against `C:\pche\_dev\forge-of-thought\templates\history.md:16-18` ("… divided by `<br>`; a thread that closes carries its last text in `Was`. At the birth of a document", the sentence added at intent 5.4, POS.0310). `recipes/ba-intro.history.md:16-18`, born 2026-10-11, has the current wording.
- **Rule:** The form of the log is `templates/history.md`'s (CLAUDE.md, Versioning & status); the same kind of drift was settled before as FND.1200 and FND.1380.
- **Fix:** immediate fix: replace the comment in the twelve companions with the template's wording; the records stay untouched.

## Facts
- The source `word-default-a4.docx` is a binary without an extract (POS.1040): the normal case, not a finding.
- The brief `00-brief.md` carries no version and no companion: the placeholder accepted under DEC.0010, not raised.
- FND.1500 and FND.1510 of the light check of 2026-10-12 stand resolved in the ledger (both `ba-intro` cells say sixteen pages, `ledger.md:61` and `:71`; the recipe's judgement named in the THR.0570 line, `ledger.md:351-354`): verified, not reopened.
- No `work/` directory and no `sources/.gitignore` exist in the project; the Dependencies table is empty and no index entry, recipe or chain file cites a path outside the project: consistent, not a finding.
