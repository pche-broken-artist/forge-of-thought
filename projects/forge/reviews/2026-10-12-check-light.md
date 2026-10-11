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

### FND.1500 low — The ledger's two rows for `ba-intro` say "seventeen pages of docs/", the render's provenance lists sixteen
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:61` (Renders row, Inputs) and `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:71` (Published row, From render); the render's front-matter `C:\pche\_dev\forge-of-thought\projects\forge\renders\ba-intro.md:10-25` lists sixteen `docs/` pages, and the recipe's Inputs `C:\pche\_dev\forge-of-thought\projects\forge\recipes\ba-intro.md:38-53` the same sixteen.
- **Rule:** `templates/ledger.md`, Renders comment — the row mirrors the render's front-matter provenance; the Published row says what the file was made from (CLAUDE.md, Document chain, Renders).
- **Fix:** immediate fix: write "sixteen pages of docs/ v5.3" in both cells (or list the pages as the render does).

### FND.1510 low — A handed-over recipe awaiting the principal's judgement has no line under Waiting on principal
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\recipes\ba-intro.md:7` and `:17` ("handed over … not yet judged by him"); `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:334-417` carries no line for it, and the presentation thread THR.0570 (`C:\pche\_dev\forge-of-thought\projects\forge\threads.md:795-831`) names only "his verdict on the two pitch renders", not this deck or its recipe.
- **Rule:** CLAUDE.md, Ledger — Waiting on principal lists what waits on the principal; a matter with no ID yet gets free text, and an ID at the next write.
- **Fix:** immediate fix: add one line under Waiting on principal — the recipe `ba-intro` 0.1, handed over 2026-10-11, its render and published deck made 2026-10-12, his judgement open (or, if he says the deck belongs to the presentation, fold it into the THR.0570 line and the thread at the next write of the intent).

## Facts
- The source `word-default-a4.docx` is a binary without an extract (POS.1040): the normal case, not a finding.
- The brief `00-brief.md` carries no version and no companion: the placeholder accepted under DEC.0010, not raised.
- FND.1490 of the previous light check stands resolved in the ledger (THR.0650 opened at 5.4, the line cut to the ID at `ledger.md:390-391`): verified, not reopened.
