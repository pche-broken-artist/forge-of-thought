---
project: forge
document: recipes/release-notes.md
---

# Version History — recipes/release-notes.md

<!-- Append-only companion of a versioned document (CLAUDE.md, Document
kinds and Versioning & status). One row per version bump, newest first,
human-readable — what changed and why. Appended by the write step that
bumps the document's version, which also rewrites last_change: in the
document's front-matter from the newest row; never edited by hand, rows
never rewritten. Not a ledger row: the companion is part of its
document. -->

| Version | Modification | Author | Date |
|---|---|---|---|
| 0.6 | Rendered by every `/release` of the engine, not by every `/save` (POS.1100, intent 3.33); "ordinary release" replaces "ordinary save" in the Instructions. | Claude | 2026-09-05 |
| 0.5 | Instructions require the intent's current vocabulary (resource index, document, artefact, history companion) even where an older history row uses a word since renamed — check-forge finding of the 3.30 save: the regenerated Unreleased head had picked up "material index" from the rows around THR.0230. The render is not regenerated for this; the next save brings it current. | Claude | 2026-09-05 |
| 0.4 | The fine-grained log named in the companion `10-intent.history.md` in Instructions and Template too, not only in Inputs (check-forge finding of the 3.21 save). | Claude | 2026-09-04 |
| 0.3 | Inputs read the intent's Version History from its companion `10-intent.history.md`, the intent itself for the current state. First row of the companion (POS.0310): 0.1 and 0.2 (2026-08-17) live in git. | Claude | 2026-09-04 |
