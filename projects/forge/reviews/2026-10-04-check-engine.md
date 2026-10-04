---
date: 2026-10-04
project: forge
check: engine
target: the engine root
reviewer: check engine (isolated context)
---

# Check (engine) — engine (C:\pche\_dev\forge-of-thought) — 2026-10-04

3 findings

## Findings

### FND.0950 — medium — The forge's readme recipe still pins the locked, immutable brief, withdrawn at 4.53, so the README regenerated at the next release will carry it again
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\recipes\readme.md:140-141 ("yours by your approval and locked once it is done"), :229-233 ("a brief composed and then locked (draft → approved)"), :236-238 ("draft → locked"), :250-252 (the pinned callout "a locked brief is immutable — composed, then locked, never touched again"), :335 (the pinned diagram node `00-brief<br>(draft → locked)`), :560-561 ("the brief-immutability callout and the brief-rule paragraph (composed then locked …)")
- **Rule:** README ↔ CLAUDE.md, and the rename/removal sweep of this check: a claim CLAUDE.md or the intent no longer supports is a recipe defect, fixed in the recipe. POS.0110 of the forge intent (C:\pche\_dev\forge-of-thought\projects\forge\10-intent.md:407-410): a brief "is not locked and not immutable", it is versioned like every artefact and changed after 1.0 as any artefact is. CLAUDE.md, Versioning & status (C:\pche\_dev\forge-of-thought\CLAUDE.md:497-499) no longer lists a brief among the immutable documents. The withdrawal is recorded in THR.0520 (C:\pche\_dev\forge-of-thought\projects\forge\threads.md:983-984).
- **Fix:** Iterate the readme recipe before the release render so that the six passages follow POS.0110 (a draft until approved at 1.0, then changed like any artefact), and drop the brief-immutability callout or replace it with a principle that still holds.

### FND.0960 — medium — The readme recipe describes a chain of three artefacts and pins a diagram in which the solution design is a future layer hanging off a BRD
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\recipes\readme.md:234-249 ("The three chain artefacts get paragraphs of equal weight": brief, intent, assignment), :328-360 (the pinned mermaid block: `BRD -.-> SD["40-solution-design"]`, `class B,I,A built`, `class BRD,RFP,ART,ST,SD,IMP future`, and the sentence that the dashed layers, "solution design" among them, are "never presented as planned or existing")
- **Rule:** README ↔ CLAUDE.md: same chain. CLAUDE.md, Document chain (C:\pche\_dev\forge-of-thought\CLAUDE.md:207-219): which artefacts the forge has is the listing of `.claude/skills/forge/states/`, "listed nowhere else", the table of artefacts in the README is rendered from the definitions, and below the intent no layer is a condition of another. That directory holds four definitions, `solution-design.md` among them. POS.1310 names four artefacts (C:\pche\_dev\forge-of-thought\projects\forge\10-intent.md:246-248). POS.1400 has the solution design derived from the intent alone, the assignment or the BRD (10-intent.md:702-707).
- **Fix:** Iterate the recipe so that the per-artefact paragraphs and the table are drawn from the definitions on disk rather than a count of three, and re-pin the diagram with `40-solution-design` as built and reachable from the intent directly.

### FND.0970 — low — Three citations still point at numbered items of CLAUDE.md, Document chain that no longer exist
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\ingest\SKILL.md:47-48 ("CLAUDE.md, Document chain 5"); C:\pche\_dev\forge-of-thought\.claude\skills\render\SKILL.md:7-8 ("CLAUDE.md, Document chain 7"); C:\pche\_dev\forge-of-thought\projects\forge\recipes\readme.md:263 ("as CLAUDE.md, Document chain 7, says")
- **Rule:** Core internal consistency: the skills against CLAUDE.md. Document chain now has four numbered items (C:\pche\_dev\forge-of-thought\CLAUDE.md:221-315): External inputs is item 2, Renders is item 4. Every other citation in the core already names the item ("Document chain, External inputs", "Document chain, Renders").
- **Fix:** Replace the three numbers with the item's name, "Document chain, External inputs" in the skill `ingest` and "Document chain, Renders" in the skill `render` and in the readme recipe.
