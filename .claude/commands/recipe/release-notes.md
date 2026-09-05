---
description: Compose or iterate a thought project's release-notes recipe — one section per release in six fixed groups, compiled from the Notes lines of the chain's history rows
argument-hint: [project-slug]
disable-model-invocation: true
---

Genre: release-notes. Skeleton: `templates/recipe-release-notes.md`.
Output: `RELEASE-NOTES.md` in the project root (POS.1000 of the forge
intent). Thought projects only — a library has no intent and
therefore no release notes; its history is git.

Every thought project carries this recipe: `/new-project` scaffolds
it from the skeleton, which owns the shape (POS.0730 of the forge
intent); every `/release` of the project regenerates the render. The
recipe is iterated; the render is never edited by hand.

Role: interviewer, lightly — this genre has few degrees of freedom.
Elicit:
1. **Which companions feed the notes.** The default is every chain
   artefact but the brief — the intent, the assignment, later layers
   as they appear; a project may narrow it (the forge itself reads
   the intent alone).
2. **The reader.** The recipients tracking the project by default; a
   different reader changes what Action required means.
3. **Language.** English by default; ask if the readers differ.

Compose the recipe from the skeleton, delete unused placeholders and
all template comments, and offer `/render release-notes` as the next
step.
