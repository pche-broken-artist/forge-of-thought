---
date: 2026-11-01
project: forge
check: project
target: projects/forge
reviewer: check project (isolated context)
---

# Check (project) — projects/forge — 2026-11-01

2 findings

## Findings

### FND.3550 — low — The three root recipes declare `output:` with a leading slash, a form no owner says how to read
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\recipes\readme.md:6 (`output: /README.md`); C:\pche\_dev\forge-of-thought\projects\forge\recipes\release-notes.md:6 (`output: /RELEASE-NOTES.md`); C:\pche\_dev\forge-of-thought\projects\forge\recipes\contributing.md:6 (`output: /CONTRIBUTING.md`)
- **Rule:** `templates/recipe.md` line 6 and the genre skeletons `templates/recipe-readme.md` line 6 and `templates/recipe-release-notes.md` line 6 declare `output:` as a path relative to the project (`README.md`); `/render` step 4 (`.claude/skills/render/SKILL.md` lines 47-53) lets an `output:` path lie outside the project only in the engine's `docs/videos/`, and the documentation says the same (docs/reference/render-provenance.md line 68). The engine's own README, release notes and CONTRIBUTING land at the engine root by CLAUDE.md, The system's own project, and the renders at the root do carry this recipe's provenance, but no owner says that a leading slash means the engine root; read as a path, `/README.md` points outside the repository (the Lens: the `output:` path points inside the repository).
- **Fix:** One sentence in the `output:` comment of `templates/recipe.md`, or in CLAUDE.md, The system's own project, saying how the path is read: relative to the project root, a leading slash the engine root, the form the engine's own project uses; the three recipes then stand as they are.

### FND.3560 — low — A critique report in `reviews/` carries a lens the roster does not have and a reviewer that is no agent of the forge
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\reviews\2026-10-23-critique-external-gemini-2153-337a.md (the filename; lines 4 and 7: `lens: external (Gemini)`, `reviewer: Gemini, outside the forge`)
- **Rule:** A critique report is named `reviews/YYYY-MM-DD-critique-<lens>-HHMM-<hash>.md`, `<lens>` a lens of the critic's roster, one agent file `critic-<lens>` each (CLAUDE.md, Isolated reviewers; Repository layout); the roster is `critic-clarity` and `critic-essence` (`.claude/agents/`). The reviewers on another model family are not built (C:\pche\_dev\forge-of-thought\projects\forge\40-solution-design.md, TBC.0030; THR.0740), so the name anticipates a mechanism with no definition. The report is immutable and cited by the ledger (FND.2530 to FND.2620), by `00-brief-brd.md` line 116 and by the clarity critique of 2026-10-25; no DEC accepts the name, DEC.0140 covering four other files only.
- **Fix:** On the principal's word, a DEC on the pattern of DEC.0140 accepting the name and the reviewer as they stand, never raised again; and the name of a report from another engine written into its owner when THR.0740 builds the mechanism.

## Facts
- projects/forge is not a repository of its own: the engine's repository tracks it (CLAUDE.md, Persistence). It therefore has no `.gitattributes` of its own: the engine root's C:\pche\_dev\forge-of-thought\.gitattributes lines 12-16 carry `projects/forge/renders/**` and `projects/forge/published/*` (SOL.0730). Its `.gitignore` carries only `/tmp/`; the ledger and the Office lock files are ignored by the engine root's `.gitignore` lines 15 and 22.
- `renders/state.md` carries the ledger's front-matter, not a render's provenance, by design (POS.1650).
- Earlier decisions accept these states, so they are not raised again: POS.0005 and REJ.0125 outside the tens (DEC.0110); the group "Working methods" starting at POS.0850 (DEC.0130); the recorded one-off edits of immutables of 2026-08-30 and 2026-09-04 (DEC.0110), of 2026-09-30 (DEC.0330, FND.2720 rejected) and the reopening of the research bundle of 2026-10-24 (DEC.0350, FND.2960 rejected); the four review files named outside the convention (DEC.0140) and the two with a run number before the tail (FND.2430, resolved as they stand); `00-brief.md` as a placeholder (DEC.0010). FND.2970 is resolved: the specification's closed TBC is TBC.0110.
