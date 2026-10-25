---
date: 2026-10-25
project: forge
check: project
target: projects/forge
reviewer: check project (isolated context)
---

# Check (project) — projects/forge — 2026-10-25

2 findings

## Findings

### FND.2710 — low — The readme and release-notes recipes open with a comment that describes a header the forge no longer has
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\recipes\readme.md:11-16 ("Recipes are tools: version + updated date in front-matter and no status ...; its Version History lives in the companion <recipe>.history.md, last_change summarising the newest row"); C:\pche\_dev\forge-of-thought\projects\forge\recipes\release-notes.md:11-16 (the same comment, "last_change derived from the records of the newest version")
- **Rule:** A header carries nothing that changes with a round, neither an updated date nor a last change (CLAUDE.md, Versioning & status; POS.1570); the recipe skeleton's comment says only that a recipe's shape is the skeleton's and its versioning Versioning & status's (`templates/recipe.md`, lines 12-14). The front-matter of both recipes already conforms (project, purpose, audience, version, output); only the comment behind it still names `updated` and `last_change`.
- **Fix:** immediate fix: replace the comment in both recipes by the skeleton's wording at the recipes' next iteration, leaving the front-matter and the sections as they are.

### FND.2720 — low — A research note corrected after its creation, recorded in the intent's history and settled by no decision
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\10-intent.history.archive.md:24 (row 4.35: `research/2026-09-30-adding-a-new-type-to-the-engine.md` "was corrected to the seven blocks, with a section on the elicitor, before its first save - an exception to the immutability of a research note, on the principal's word, since the note was two hours old and not yet in git"); the note C:\pche\_dev\forge-of-thought\projects\forge\research\2026-09-30-adding-a-new-type-to-the-engine.md
- **Rule:** Research notes are immutable from creation; corrections happen downstream (CLAUDE.md, Versioning & status, Immutable documents; Document kinds, research). DEC.0110 accepts two other recorded one-off edits of immutables (2026-08-30, 2026-09-04) and says no later check raises them; this edit of 2026-09-30 is outside it and no later DEC names it, so the record stands as an exception without a verdict.
- **Fix:** On the principal's word, a DEC on the pattern of DEC.0110 accepting the recorded correction of 2026-09-30 as it stands, never raised again; or, if he prefers the rule kept whole, a downstream note citing the original, nothing edited.

## Facts
- projects/forge is not a repository of its own: it is tracked by the engine's repository (CLAUDE.md, Persistence: `projects/forge` is the exception to the engine's ignore of `projects/*`). For that reason it has no `.gitattributes` and its `.gitignore` does not list the ledger; both are the engine root's: C:\pche\_dev\forge-of-thought\.gitattributes lines 1-16 cover `projects/forge/renders/**` and `projects/forge/published/*`, and the engine's `.gitignore` the ledger, as the project check of 2026-10-23 recorded. `renders/state.md` carries the ledger's front-matter, not a render's provenance, by design: the release skill writes it from the ledger script and says the Renders table does not list it (`.claude/skills/release/SKILL.md`, lines 64-69; POS.1650).
- Earlier decisions accept these states, so they are not raised again: POS.0005 and REJ.0125 outside the tens (DEC.0110); the group "Working methods" starting at POS.0850 (DEC.0130); the two recorded one-off edits of immutable documents of 2026-08-30 and 2026-09-04 (DEC.0110); the four review files named outside the convention (DEC.0140); `00-brief.md` as a placeholder (DEC.0010); the two report names with a run number before the tail (FND.2430, resolved: the files stay as they are).
