---
date: 2026-10-18
project: forge
check: light
target: projects/forge
reviewer: check light (isolated context)
---

# Check (light) — C:\pche\_dev\forge-of-thought\projects\forge — 2026-10-18

3 findings

## Findings

### FND.1760 — medium — The work file cites seven items of the design and the intent that its specification's Inputs do not name
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\work\collaboration-cutover.md:32` (SOL.0150, R1.14), `:46` (SOL.0500, R1.07), `:56` (SOL.0160, R1.15), `:57` (SOL.0420, SOL.0460, R1.20), `:88` (POS.0220, R2.14) and SOL.0530 at `:35, 55, 57, 58, 61, 78, 81, 85, 90, 91, 105, 116` — against `C:\pche\_dev\forge-of-thought\projects\forge\work\collaboration-cutover.spec.md:28-34` (Inputs: SOL.0670 to SOL.0830, SOL.0300, SOL.0330, TBC.0050, TBC.0060, TBC.0080; POS.1560 to POS.1770, POS.1120, POS.1140; the five THR; DEC.0210 to DEC.0250). SOL.0530 appears in the specification's Method (`:43`) but not among its Inputs.
- **Rule:** POS.1520 of `10-intent.md` as changed at 5.21 (`10-intent.history.md:420`: a work file that has moved past the way and the why; the light check gains the rule) and CLAUDE.md, Document kinds (the specification beside the file holds the way and the why).
- **Fix:** at the next write of the specification (0.5, one record) the Inputs gain SOL.0150, SOL.0160, SOL.0420, SOL.0460, SOL.0500, SOL.0530 and POS.0220, each with the step it serves.

### FND.1770 — low — The Work row's Inputs cell stands at the specification's 0.2 while the row says v0.4
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:84` ("40-solution-design.md v0.20 (SOL.0670 to SOL.0820, …, TBC.0050 to TBC.0080) … threads.md (THR.0620, THR.0650, THR.0690, THR.0700), decisions.md (DEC.0210), 00-brief-collaboration.md v0.8 (M)") against `C:\pche\_dev\forge-of-thought\projects\forge\work\collaboration-cutover.spec.md:28-34` (SOL.0670 to SOL.0830; TBC.0050, TBC.0060, TBC.0080; THR.0710 added; DEC.0210 to DEC.0250; the three sources) and its records at `collaboration-cutover.spec.history.md:26, 29, 32`.
- **Rule:** `templates/ledger.md`, Work comment (one row per work product, Specification = its version, the row kept by `/work`); CLAUDE.md, Ledger (kept current after every operation).
- **Fix:** immediate fix: the Inputs cell brought to the specification's Inputs at 0.4 (SOL.0670 to SOL.0830, SOL.0300, SOL.0330, TBC.0050, TBC.0060, TBC.0080; POS.1560 to POS.1770, POS.1120, POS.1140; THR.0620, THR.0650, THR.0690, THR.0700, THR.0710; DEC.0210 to DEC.0250; brief section M; the three sources).

### FND.1780 — low — A history companion carries the template's placeholder comment in its front-matter
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\00-brief-brd.history.md:3` (`document: 00-brief-brd.md  # the versioned document this history belongs to`); the other fourteen companions carry the bare field.
- **Rule:** CLAUDE.md, Versioning & status (the companion in the shape `templates/history.md` owns); `templates/history.md:3` gives the comment as the skeleton's annotation, not as content.
- **Fix:** immediate fix: the trailing comment deleted from the field.

## Facts
- `00-brief.md` carries no version and no companion: the placeholder accepted under DEC.0010, not raised.
- `sources/word-default-a4.docx` is a binary without an extract (POS.1040): the normal case; no `sources/.gitignore` exists and none is needed.
- Four review files are named outside the convention: accepted as they are by DEC.0140 (`ledger.md:365-366`).
