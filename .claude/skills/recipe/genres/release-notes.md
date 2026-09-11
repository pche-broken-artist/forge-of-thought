---
description: Compose or iterate a thought project's release-notes recipe — one section per release in six fixed groups, compiled from the Notes lines of the chain's history rows
---

Genre: release-notes. Skeleton: `templates/recipe-release-notes.md`.
Output: `RELEASE-NOTES.md` in the project root (POS.1000 of the forge
intent). Thought projects only — a library has no intent and
therefore no release notes; its history is git.

Why every thought project carries this recipe and when its render is
made is CLAUDE.md, Document chain 7's; the skeleton owns the shape
(POS.0730 of the forge intent).

Role: interviewer, lightly — this genre has few degrees of freedom.
Elicit:
1. **Which companions feed the notes.** The default is every chain
   artefact but the brief — the intent, the assignment, later layers
   as they appear; a project may narrow it (the forge itself reads
   the intent alone).
2. **The reader.** The recipients tracking the project by default; a
   different reader changes what Action required means.
3. **Language.** The render's language is what this recipe declares
   (CLAUDE.md, prime directive 6); propose the project's language
   from its ledger header and ask, never assume.

Compose the recipe from the skeleton, delete unused placeholders and
all template comments, and offer `/render release-notes` as the next
step.
