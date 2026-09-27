---
project: forge
document: recipes/executive-pitch.md
---

# Version History — recipes/executive-pitch.md

<!-- Append-only companion of a versioned document (CLAUDE.md, Document
kinds and Versioning & status). One row per version bump, newest first,
human-readable — what changed and why. Appended by the write step that
bumps the document's version, which also rewrites last_change: in the
document's front-matter from the newest row; never edited by hand, rows
never rewritten. Not a ledger row: the companion is part of its
document. -->

| Version | Modification | Author | Date |
|---|---|---|---|
| 0.6 | The renderer of 2026-09-27 reported the vocabulary rule contradicting the Template: `assignment` banned yet used on S01, S02 and S05 in the plain sense of a task handed to a team, `recipe` banned yet used on S04; and the S04 hub asking for six outputs where the Content listed five. Settled at the release walkthrough of 2026-09-27: `assignment` allowed in its plain sense and never as a document's name, S04 says "description" instead of "recipe", the sixth output (a deck for the delivery team, from the Instructions) named in the Content and the diagram row pointing to it. Not yet rendered at 0.6. | Claude, with the principal | 2026-09-27 |
| 0.5 | The round of 2026-09-27 (intent 4.28, POS.0590): an output is made in two steps, and the section `Build instructions` becomes `Format`. It names the format, `pptx`; the plain file, made by `/render` through pandoc, without a template; and the published file, made by `/publish` through a model, with everything the old section told the model, word for word - no template, the model's own design, opus, the overflow and diagram rules. The instruction to copy the section into the render is gone: the render carries content only, and the model reads the section in the recipe. The render was not repeated, so the render of 0.4 still carries the old section. | Claude, with the principal | 2026-09-27 |
| 0.4 | The principal's review of the first render (2026-09-11): the opponents are no longer counted — the roster of reviewers grows, so the vocabulary rule and S03 say "opponents that never saw you" and S03 says each opponent has one job and more are added as the need shows; on-slide density raised from four to five lines per slide so that less of the Template's content is pushed into the notes. Re-render follows. | Claude | 2026-09-11 |
| 0.3 | Build instructions: the deck is built with the script's default visual style, no `.potx` and no move to a library — the principal's decision of 2026-09-10 (ledger, Waiting on principal); the 0.2 row's note that the recipe was bound for `lib-allwyn` is thereby withdrawn. Still not rendered; the render follows this bump. | Claude | 2026-09-11 |
| 0.2 | Inputs declared from the engine root (`projects/forge/10-intent.md`, `CLAUDE.md`), the base every other recipe and the ledger's Renders rows use — the project check of release 4.0 found the two relative paths resolving from no common base. Still not rendered; the recipe is bound for `lib-allwyn` (ledger, Waiting on principal). | Claude | 2026-09-06 |
| 0.1 | Composed by interview on 2026-08-30: five-slide C-level deck, story S01–S05 agreed; not yet rendered. Companion created 2026-09-04 (POS.0310) without a bump. | Claude | 2026-08-30 |
