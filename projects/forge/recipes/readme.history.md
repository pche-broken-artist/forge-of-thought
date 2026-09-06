---
project: forge
document: recipes/readme.md
---

# Version History — recipes/readme.md

<!-- Append-only companion of a versioned document (CLAUDE.md, Document
kinds and Versioning & status). One row per version bump, newest first,
human-readable — what changed and why. Appended by the write step that
bumps the document's version, which also rewrites last_change: in the
document's front-matter from the newest row; never edited by hand, rows
never rewritten. Not a ledger row: the companion is part of its
document. -->

| Version | Modification | Author | Date |
|---|---|---|---|
| 0.38 | The reviewers no longer counted in the masthead bullets, the deep-dive summary and the heading of section 8 ("Isolated reviewers", "blind adversarial reviewers"), so that the render does not age with a further kind on the reviewer mechanism (POS.0540, POS.1120; FND.0290 of the clarity critique of 2026-09-06). | Claude | 2026-09-06 |
| 0.37 | "Saving and syncing" recast to the two doors of POS.1100 — `/save` commits and pushes, `/release` checks, renders and saves from `main`, branches voluntary through `forge-branch` (POS.1110); `/release` joins the prose paragraph under the Commands table. Check-forge finding of the first release, 2026-09-05: the 0.36 row had claimed alignment while the instruction still named the old pre-commit steps. | Claude | 2026-09-05 |
| 0.36 | README regenerated at every `/release`, not at every `/save` (POS.1100, intent 3.33); the closing section "About this README" and the renders paragraph of the pitch say so. | Claude | 2026-09-05 |
| 0.35 | Conventions gains the document-kinds table of CLAUDE.md (POS.1080) with the history-companion sentences; the language rule says documents, not artefacts. First row of the companion (POS.0310): the recipe's history from 0.1 to 0.34 lives in git and in the intent's rows that name it. | Claude | 2026-09-04 |
