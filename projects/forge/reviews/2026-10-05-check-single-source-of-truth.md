---
date: 2026-10-05
project: forge
check: single-source-of-truth
target: the engine (C:\pche\_dev\forge-of-thought)
reviewer: check single-source-of-truth (isolated context)
---

# Check (single-source-of-truth) — engine (C:\pche\_dev\forge-of-thought) — 2026-10-05

7 findings; 69 files of the operating layer read whole (CLAUDE.md as it lies on disk — the copy in my launch context was a stale snapshot and was discarded —, 30 skill files with the 4 states and 3 genres, 9 agents, 19 templates, the help headers of 9 scripts, .claude/settings.json), plus the Findings table of C:\pche\_dev\forge-of-thought\projects\forge\ledger.md, the report C:\pche\_dev\forge-of-thought\projects\forge\reviews\2026-10-02-check-single-source-of-truth.md and the DEC headings of decisions.md. Of the nineteen findings of 2026-10-02, sixteen hold resolved on disk (FND.0540–0610, 0640, 0660–0700, 0720 verified); FND.0710 and the caveat part of FND.0720 are rejected (DEC.0170, DEC.0180) and are not raised. Two are reopened and one stands parked, below.

## Findings

### FND.0980 — medium — What a missing `kind:` header means is said twice, the two disagree, and the citation reaches no owner
- **Where:** C:\pche\_dev\forge-of-thought\.claude\agents\check-project.md:21-23; C:\pche\_dev\forge-of-thought\.claude\skills\import-project\SKILL.md:19-21; C:\pche\_dev\forge-of-thought\scripts\forge-clone.ps1:15-16
- **Rule:** One owner per rule, cited by path (CLAUDE.md, prime directive 10; POS.1070). The project check says a ledger without `kind:` is "a finding with the one-line fix"; `/import-project` and the clone script's header say "its absence is a fact, not a defect", and the skill cites CLAUDE.md, Persistence for it — which speaks of a project not under git (CLAUDE.md:415-416) and says nothing of the `kind:` header. The rule has no owner: `/new-project` (SKILL.md:16-20) and `templates/ledger.md:13-18` state the kind without saying what its absence means.
- **Fix:** Give the rule one owner — a sentence in the header comment of `templates/ledger.md` (the one owner of the kind's reduction already) saying what a missing `kind:` reads as and whether it is a finding — and cut `import-project` and `forge-clone.ps1` to "reported as a fact; what it means is the ledger skeleton's", `check-project` to a citation of the same.

### FND.0990 — medium — `/spinoff` writes the source assignment by hand where `/forge assignment` and Intent-first are the mechanism
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\spinoff\SKILL.md:27-31
- **Rule:** No direct operation where a mechanism exists (CLAUDE.md, prime directive 10; POS.1070). Steps 2–4 of the command cite the procedures that own the acts (`/new-project`, `/forge brief`, `/forge intent`, each "its Course"); step 5 then marks items superseded, replaces a group by a link item and writes the companion itself, outside the assignment's definition (`.claude/skills/forge/states/assignment.md`, Course: "a substance change asked for in the assignment goes to the intent first") and without touching the source intent that Intent-first (CLAUDE.md, Working methods) makes the first stop of a substance change.
- **Fix:** Have step 5 record the spin-off in the source intent through the `/forge intent` procedure and derive the superseded group and the link item through the `/forge assignment` procedure (its Course, "an intent that moved"), keeping in `/spinoff` only the DEC and the wording of the link item.

### FND.0650 — low — Genre checklists repeat the rules their skeletons carry
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\recipe\genres\presentation.md:23-25, 33-34 against C:\pche\_dev\forge-of-thought\templates\recipe-presentation.md:20-22, 41-42; C:\pche\_dev\forge-of-thought\.claude\skills\recipe\genres\readme.md:22-26 against C:\pche\_dev\forge-of-thought\templates\recipe-readme.md:18-21
- **Rule:** POS.1070; the genre file "carries the elicitation checklist and points at the canonical skeleton" (`.claude/skills/recipe/SKILL.md:7-10`). The picture-from-a-render clause and the Mermaid constraint stand word for word in checklist and skeleton; the input sets per kind likewise.
- **Fix:** Let each checklist item ask its question and leave the rule to the skeleton it points at.
- **Known as:** FND.0650, still open (parked)

### FND.0630 — low — Artefacts named by name in Isolated reviewers where Document chain says they are listed nowhere else
- **Where:** C:\pche\_dev\forge-of-thought\CLAUDE.md:567-568 against 212-213
- **Rule:** Rosters are the scan of their files and are named nowhere else (POS.1070; CLAUDE.md:212-213: "they are listed nowhere else"). The target list "(`brief`, `brief-<name>`, `intent`, `assignment`, later layers)" is a roster of artefacts written out, already without the solution design the directory holds.
- **Fix:** Cut the parenthesis to "an artefact named as `/forge` names it, by its state file".
- **Known as:** FND.0630, reopened

### FND.0620 — low — One rule echoed in three sections of CLAUDE.md: a layer a project does not have is not missing
- **Where:** C:\pche\_dev\forge-of-thought\CLAUDE.md:13-14, 215-217, 610-612
- **Rule:** One owner per rule, inside a file as across files (POS.1070). The Ledger section (610-612) is the owner the others cite (`.claude/agents/check-project.md:38`, `.claude/skills/forge/SKILL.md:28`, `templates/ledger.md:35-36`); Document chain (215-217) restates it in full and What this workspace is (13-14) once more.
- **Fix:** Keep the rule in Ledger, let Document chain point to it in a clause, and leave the opening paragraph its one sentence on where the chain ends.
- **Known as:** FND.0620, reopened

### FND.1000 — low — When a Renders row is born is said in three places that do not agree
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\recipe\SKILL.md:43-44; C:\pche\_dev\forge-of-thought\.claude\skills\render\SKILL.md:55-56; C:\pche\_dev\forge-of-thought\templates\ledger.md:39-40
- **Rule:** POS.1070. `/recipe` says the recipe is registered in the Renders table "when its first render exists"; `/render` step 6 updates the table to mirror the render; the ledger skeleton says "one row per recipe in recipes/" while the row "mirrors the render's front-matter provenance", which a recipe without a render has none of.
- **Fix:** Let the skeleton's comment own the moment ("one row per rendered recipe, written by `/render`"), cite it from `/render` step 6, and delete the sentence from `/recipe`.

### FND.1010 — low — Two script headers echo the commit-identity rule without naming its owner
- **Where:** C:\pche\_dev\forge-of-thought\scripts\forge-save.ps1:24-28; C:\pche\_dev\forge-of-thought\scripts\forge-clone.ps1:10-13
- **Rule:** A one-line reminder at the point of action is not a restatement only where it names its owner (the rule FND.0700 settled; POS.1070). The owner is CLAUDE.md, Persistence (407-414, 427: "the commit identity is git's … the scripts carry no URL and no identity"); `forge-status.ps1:11-12` shows the house style by citing it, these two headers restate the rule in three sentences and cite nothing.
- **Fix:** Cut each to one sentence ending "(CLAUDE.md, Persistence)".
