---
date: 2026-10-04
project: forge
check: project
target: projects/forge
reviewer: check project (isolated context)
---

# Check (project) — projects/forge — 2026-10-04

2 findings

## Findings

### low — The Published line of the Format section is still "not set" in two recipes, and both have now passed the iteration the finding was parked until
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\recipes\cto-pitch.md:117-118; C:\pche\_dev\forge-of-thought\projects\forge\recipes\ceo-pitch.md:138-139
- **Rule:** `templates/recipe.md`, Format (lines 35-37): the Published line names `template <path | none>, model <name>`; recipes conform to the skeleton in their sections, and a file in `published/` traces to a recipe's Format section (CLAUDE.md, Document chain, Renders). Both recipes still read "not set; `/publish` asks before its first run", while C:\pche\_dev\forge-of-thought\projects\forge\published\cto-pitch.docx exists and the ledger's Published table (ledger.md:60) records its model. The finding was parked "until the next iteration of the recipes" (ledger.md:211, :314-315); both recipes were iterated to 0.6 on 2026-10-04 (C:\pche\_dev\forge-of-thought\projects\forge\recipes\cto-pitch.history.md:20, C:\pche\_dev\forge-of-thought\projects\forge\recipes\ceo-pitch.history.md:20) and the line was not touched.
- **Fix:** In the round that is open, write the Published line of `recipes/cto-pitch.md` in the skeleton's shape (template none, the model the ledger row records), and for `recipes/ceo-pitch.md` fill it the same way or drop it until a first publish; otherwise re-park FND.0750 with a condition that still lies ahead.
- **Known as:** FND.0750, still open (parked; the condition of its parking has passed)

### FND.0940 — low — The line of THR.0520 under Waiting on principal retells the thread's progress instead of citing it
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:262-268
- **Rule:** CLAUDE.md, Ledger: under Waiting on principal a matter that has an ID gets one line — the ID, a few words, its state — and its substance stays in the thread; the ledger cites and never copies. The line carries the date of the walkthrough with its intent version, the range of positions born from it, the plan of six steps, what step 5 produced with two versions, that the command has not been run, that the design is a proposal not yet read whole by the principal, and the pause of step 6 — all of which stands in the thread itself (C:\pche\_dev\forge-of-thought\projects\forge\threads.md:922-1012, the last of them word for word at :1009-1010).
- **Fix:** Cut the line to the ID, a few words and the present state, for example "THR.0520 — a layer for the solution; priority; steps 1 to 5 done, step 6 (the BRD) paused 2026-10-04", leaving the rest in the thread.

## Facts
- projects/forge is not a repository — it has no `.git` of its own and is tracked by the engine's repository (CLAUDE.md, Persistence: every project is gitignored by the engine, `projects/forge` excepted); no way in is needed.
- `POS.0005` and `REJ.0125` outside the tens, and the group "Working methods" starting at POS.0850, stand as accepted by DEC.0110 and DEC.0130; the four review files named outside the convention by DEC.0140; `00-brief.md` as a placeholder by DEC.0010.
