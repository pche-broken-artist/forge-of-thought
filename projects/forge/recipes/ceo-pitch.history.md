---
project: forge
document: recipes/ceo-pitch.md
---

# Version History — recipes/ceo-pitch.md

<!-- Append-only companion of a versioned document (CLAUDE.md, Document
kinds and Versioning & status). One row per version bump, newest first,
human-readable — what changed and why. Appended by the write step that
bumps the document's version, which also rewrites last_change: in the
document's front-matter from the newest row; never edited by hand, rows
never rewritten. Not a ledger row: the companion is part of its
document. -->

| Version | Modification | Author | Date |
|---|---|---|---|
| 0.5 | The round of 2026-09-27 (intent 4.28, POS.0590): an output is made in two steps, and the base recipe skeleton gains an optional `## Format` section for what each needs. The build line that 0.4 had folded into Instructions becomes that section: format `docx`; the plain file, made by `/render` through pandoc, on A4 and without a reference document, as the line had it; the published file, made by `/publish` through a model, not set - nobody has said what it should look like, so `/publish` asks before its first run. Nothing the renderer writes changes; the render was not repeated. | Claude, with the principal | 2026-09-27 |
| 0.4 | A finding of the project check of 2026-09-20, fixed on the principal's word: the recipe carried a `Build instructions` section, which only the presentation genre's skeleton has, and a heading with a hyphen where `templates/recipe.md` has a dash. The one build line is now the last bullet of Instructions, marked as not rendered, and the heading follows the skeleton. Nothing the renderer writes changes, so the render of 0.3 stands and was not repeated. | Claude, with the principal | 2026-09-20 |
| 0.3 | The principal's addition of 2026-09-20 to "About me": he was CTO of some of the largest Czech online companies, and today he is a CTO within a global group that is the second largest in the world in its field. The group is described in those words and never named, so the pitch stays free of company names; the two decades now span both. | Claude, with the principal | 2026-09-20 |
| 0.2 | The principal's direction of 2026-09-20: the public pitches carry a section about him, since he appears on GitHub under his full identity, linked with his LinkedIn, and it is no secret who he is. The closing block "A personal note" becomes "About me" and keeps what it said: who he is, in the words of his public GitHub profile which he pointed to, cut for this reader - the career first (two decades as CTO of some of the largest Czech online companies, one who assigns work to teams every day), the craft in one clause, AI as a cognitive extension, nothing on programming eras or the history of philosophy - then the forge and the offer, then one contact line with e-mail, LinkedIn and GitHub. The must-not-appear rule excepts the author from "any person"; no employer is named, though the profile names one, because the pitch stays free of company names. Merged into the existing block rather than added as a seventh, since the render already stands at the upper end of its length. | Claude, with the principal | 2026-09-20 |
| 0.1 | Initial recipe, on the principal's order of 2026-09-20: the executive pitch, until now a five-slide deck (`recipes/executive-pitch.md`, left as it is), recast as a short public document of about the length of the CTO pitch, with an optional Word file. Composed by Claude on his own judgement, the principal reads the result. The principal's direction: less on what the forge is, more on what it can mean for a CEO - efficiency, quality, the transformation of an IT department into AI. From the deck it keeps the reader (a CEO who knows AI as a chat), the one contrast (a chat gives an answer, the forge a decision one can stand behind) and the vocabulary discipline; it drops the deck's worked example with its counts, which THR.0380 holds as a loose end. The benefits are stated as what the mechanism changes and why it should pay, never as measured gains, since nothing has been measured. The two pieces of work appear anonymised by their kind, as in the public CTO pitch; a must-not-appear list guards the public boundary; long dashes are banned from the render. | Claude | 2026-09-20 |
