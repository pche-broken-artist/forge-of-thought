---
date: 2026-10-17
project: forge
check: light
target: projects/forge
reviewer: check light (isolated context)
---

# Check (light) — C:\pche\_dev\forge-of-thought\projects\forge — 2026-10-17

1 finding

## Findings

### FND.1730 — low — TBC.0070, opened at solution design 0.18 and owned by the principal, has no line under Waiting on principal
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:387-483` (the section Waiting on principal: lines for TBC.0030 and for the threads, none for TBC.0070) against `C:\pche\_dev\forge-of-thought\projects\forge\40-solution-design.md:1260-1263` (TBC.0070, owner: principal, the reservation of IDs where main is protected against a direct push, SOL.0790, no thread it points to). Of the other two TBCs born at 0.18, TBC.0060 (`40-solution-design.md:1256`) is Claude's and waits on no one; TBC.0050 (`40-solution-design.md:1252`) points to THR.0650, whose line (`ledger.md:456-457`) still says only the forge-pull test deferred 2026-10-11, not the four tests the 5.13 record added to the thread (`10-intent.history.md:380`). The same case was settled for TBC.0030 and TBC.0040 by FND.1650.
- **Rule:** CLAUDE.md, Ledger (Waiting on principal names what waits, one line per matter, cite never copy) and `templates/ledger.md`, Waiting on principal.
- **Fix:** immediate fix: one line under Waiting on principal citing TBC.0070 (a few words, its state), and the line of THR.0650 widened to say the four tests of the brief `collaboration`, so that TBC.0050 is carried by it as TBC.0010 and TBC.0020 are by theirs.

## Facts
- `00-brief.md` carries no version and no companion: the placeholder accepted under DEC.0010, not raised.
- `sources/word-default-a4.docx` is a binary without an extract (POS.1040): the normal case; no `sources/.gitignore` exists and none is needed, nothing was converted in place.
- No `work/` directory and an empty Work table: the normal case before a first work product.
- Everything else conforms, confirmed against disk: the Documents rows (intent 5.15, solution design 0.18, both `draft`, 2026-10-17) match the front-matter, each `last_change` summarises the newest records of its companion (`10-intent.history.md:383` for 5.15, 5.13 and 5.14 recorded at lines 364-382; `40-solution-design.history.md:63-82` for 0.18), every record in the one-line log shape of `templates/history.md`, author the instance's handle; the six briefs' front-matter (1.0, 1.0, 0.3, 0.2, 0.1, 0.8) matches the Briefs rows, `00-brief-collaboration.history.md:45-51` carries the 0.7 and 0.8 records its `last_change` derives from; the seven recipes carry `updated`, no status, 0.x versions; the eight Renders rows mirror word for word the provenance front-matter of `README.md`, `docs/README.md`, `RELEASE-NOTES.md`, `CONTRIBUTING.md` and the four Markdown renders; the three Published rows and the three files of `published/` agree one to one; the sixteen files of `sources/` (the two of today, `design-critique.md` and `design-critique-2.md`, among them) and the forty-six notes of `research/` each have a ledger row and an entry in their `00-INDEX.md`, the sources index carrying the library bundle as a seventeenth, cited entry and no other outward citation existing in the chain, the recipes or the indexes; the one Dependencies path `projects/lib-allwyn/sources/fork-brd/00-INDEX.md` is present; every file of `reviews/` (41, the report of 2026-10-17 cited by FND.1720) and `challenges/` (4) is cited by a Findings or Challenges row, the four files outside the naming convention under DEC.0140; every state word is the template's; the thirty-seven threads under Waiting on principal are exactly the thirty-seven open in `threads.md`; header `kind: thought`, `language: en`, `updated: 2026-10-17`.
