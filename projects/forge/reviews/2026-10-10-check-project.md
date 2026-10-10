---
date: 2026-10-10
project: forge
check: project
target: projects/forge
reviewer: check project (isolated context)
---

# Check (project) — projects/forge — 2026-10-10

2 findings

## Findings

### FND.1390 — low — The release-notes recipe reads the intent's history only, while the project now has a layer below the intent whose history the genre skeleton lists as an input
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\recipes\release-notes.md:20-35 (Inputs) and :47-48 (the instruction "derived from the records of its version in the log")
- **Rule:** `templates/recipe-release-notes.md`, Inputs (lines 22-23: `<NN-layer>.history.md`, one line per layer below the intent the project has, with its archive) and Instructions (lines 38-40: the records of the intent's history and those of the layers below it); a genre skeleton extends the shape of `templates/recipe.md`, never replaced by the recipe (CLAUDE.md, Document chain, Renders). The project has `40-solution-design.md` 0.8 with `40-solution-design.history.md` (ledger Documents table, C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:40); recipe 0.12 of 2026-10-02 predates the layer and names neither.
- **Fix:** At the recipe's next iteration, before the release render of 5.0, add `projects/forge/40-solution-design.history.md` to the Inputs and let the instruction say "the log of every input history", as the skeleton does, so that the solution design's records reach the reader of the release notes.

### FND.1400 — low — The readme recipe carries a section the recipe skeleton and the readme genre skeleton do not have
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\recipes\readme.md:234-265 (`## Pinned facts (not rendered)`)
- **Rule:** `templates/recipe.md` owns the shape of a recipe (Inputs, Instructions, Format, Template); `templates/recipe-readme.md` extends it for the genre and has no such section; a new section is never introduced unilaterally, it is proposed, decided and then written down (CLAUDE.md, prime directive 2). The section is treated as an owner by SOL.0460 and SOL.0500 (C:\pche\_dev\forge-of-thought\projects\forge\40-solution-design.md:556, 581-598) and by the map, while the brief `documentation` still lists "the place of the pinned facts" under Still open (C:\pche\_dev\forge-of-thought\projects\forge\00-brief-documentation.md:137-138): the mechanism is in use but its shape is written in no skeleton.
- **Fix:** On the principal's word, either give the readme genre skeleton an optional section for facts the recipe owns until they have an owner, or move the facts to a document whose kind owns them; until then the recipe's shape stands outside its skeleton.

## Facts
- projects/forge is not a repository — it has no `.git` of its own and is tracked by the engine's repository (CLAUDE.md, Persistence: every project is gitignored by the engine, `projects/forge` excepted); no way in is needed.
- `POS.0005` and `REJ.0125` outside the tens, and the group "Working methods" starting at POS.0850, stand as accepted by DEC.0110 and DEC.0130; the two recorded one-off edits of immutables by DEC.0110; the four review files named outside the convention by DEC.0140; `00-brief.md` as a placeholder by DEC.0010; the Published line dropped from `recipes/ceo-pitch.md` until a first publish by the resolution of FND.0750.
