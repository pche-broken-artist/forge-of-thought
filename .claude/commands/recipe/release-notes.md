---
description: Compose or iterate a thought project's release-notes recipe — an Unreleased head plus one section per approved major of the intent
argument-hint: [project-slug]
---

Genre: release-notes. Skeleton: `templates/recipe-release-notes.md`.
Output: `RELEASE-NOTES.md` in the project root (POS.1000 of the forge
intent). Thought projects only — a library has no intent and
therefore no release notes; its history is git.

Every thought project carries this recipe: `/new-project` scaffolds
it from the skeleton; every `/save` that touches the project
regenerates the Unreleased head, released sections carried over
verbatim; at a major approval the head is recast as the new major's
section. The recipe is iterated; the render is never edited by hand.

Role: interviewer, lightly — this genre has few degrees of freedom.
Elicit:
1. **Granularity of the head.** How many themes; whether DEC records
   are named by ID or folded into prose.
2. **What a major section must always carry.** The narrative opening;
   whether "Open by design" lists every open THR or the principal's
   selection.
3. **Language.** English by default; ask if the readers differ.

Compose the recipe from the skeleton, delete unused placeholders and
all template comments, and offer `/render release-notes` as the next
step.
