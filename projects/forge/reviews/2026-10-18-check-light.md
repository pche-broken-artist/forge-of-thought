---
date: 2026-10-18
project: forge
check: light
target: projects/forge
reviewer: check light (isolated context)
---

# Check (light) — C:\pche\_dev\forge-of-thought\projects\forge — 2026-10-18

2 findings

## Findings

### FND.1740 — low — TBC.0010 of the work specification, owned by the principal, has no line under Waiting on principal
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:419-519` (the section Waiting on principal: no line for the work product or its open point) against `C:\pche\_dev\forge-of-thought\projects\forge\work\collaboration-cutover.spec.md:53` (`TBC.0010 (owner: principal) Whether single-source-of-truth runs at every release of the plan or at the first and the last only. Closed by: his word.`). The Work row (`ledger.md:84`, state `by hand`) carries the file, not the open point. The same case was settled for the design's TBCs by FND.1650 and FND.1730.
- **Rule:** CLAUDE.md, Ledger (Waiting on principal names what waits, one line per matter, cite never copy) and `templates/ledger.md`, Waiting on principal.
- **Fix:** immediate fix: one line under Waiting on principal citing TBC.0010 of `work/collaboration-cutover.spec.md` by file, since the design has a TBC.0010 of its own, a few words and its state.

### FND.1750 — low — The line of THR.0650 says the four tests come after the first and the second release; the design at 0.22 says before the second, none after the first
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:491-494` ("the four tests of the brief `collaboration` (TBC.0050), after the first and the second release") against `C:\pche\_dev\forge-of-thought\projects\forge\40-solution-design.md:1362-1370` (TBC.0050: "the four of THR.0650 before the second release's own release, none after the first") and the records of 0.22 at `C:\pche\_dev\forge-of-thought\projects\forge\40-solution-design.history.md:127-128`. The line was written 2026-10-17 (FND.1730) and the design moved on 2026-10-18.
- **Rule:** CLAUDE.md, Ledger (the ledger is kept current after every operation; a matter with an ID gets its state in a few words) and `templates/ledger.md`, Waiting on principal.
- **Fix:** immediate fix: the line's words brought to "the four tests of the brief `collaboration` (TBC.0050) before the second release, none after the first".

## Facts
- `00-brief.md` carries no version and no companion: the placeholder accepted under DEC.0010, not raised.
- `sources/word-default-a4.docx` is a binary without an extract (POS.1040): the normal case; no `sources/.gitignore` exists and none is needed, nothing was converted in place.
- Four review files are named outside the convention: accepted as they are by DEC.0140, as the ledger itself says at `ledger.md:361-362`.
