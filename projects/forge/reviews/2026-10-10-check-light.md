---
date: 2026-10-10
project: forge
check: light
target: projects/forge
reviewer: check light (isolated context)
---

# Check (light) — projects/forge — 2026-10-10

3 findings

## Findings

### FND.1360 low — The ledger's `updated` date lags the state it records by a day
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:5` (`updated: 2026-10-09`); against `ledger.md:36-37` (Documents rows dated 2026-10-10), `ledger.md:260-274` (FND.1210 to FND.1350 resolved at intent 4.65 and solution design 0.8, both dated 2026-10-10 in `10-intent.md:2-3` and `40-solution-design.md:2-3`), `ledger.md:387-388` (THR.0600 opened 2026-10-10)
- **Rule:** CLAUDE.md, Ledger — the single source of truth for state, kept current after every operation; the header field is `templates/ledger.md:6`.
- **Fix:** immediate fix: set `updated: 2026-10-10`.

### FND.1370 low — Waiting on principal names a recipe version that no longer stands
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:370-373` (the POS.1450 line: "the README re-rendered from recipe 0.59"); against `C:\pche\_dev\forge-of-thought\projects\forge\recipes\readme.md:5-7` (version 0.60, 2026-10-10) and `recipes\readme.history.md:30` (the 0.60 record)
- **Rule:** CLAUDE.md, Ledger — Waiting on principal matches what is actually open. The matter itself is still open (`README.md:5` carries `recipe: recipes/readme.md v0.58`).
- **Fix:** immediate fix: write "recipe 0.60" in the line.

### FND.1380 low — Two header comments of the ledger stand behind `templates/ledger.md`
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:10-17` (the head comment lacks the three lines on `kind:` that `C:\pche\_dev\forge-of-thought\templates\ledger.md:13-15` added on 2026-10-09 under FND.0980); `ledger.md:43-44` (the Renders comment in its older wording, where `templates\ledger.md:42-47` now says who writes the row and when, and that the documentation index has a row, added under FND.1000 and FND.1100)
- **Rule:** CLAUDE.md, Ledger — the ledger's tables are `templates/ledger.md`'s; the ledger's comments behind their template were settled the same way under FND.0920 (`reviews/2026-10-04-check-light.md`) and the companions' under FND.1200 (`reviews/2026-10-09-check-light-3.md`).
- **Fix:** immediate fix: replace both comments with the template's wording.
