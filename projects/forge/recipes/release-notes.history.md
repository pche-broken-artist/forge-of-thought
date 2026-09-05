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
| 0.10 | At an approved major the minors since the previous major fold into the major's section — every Notes line of the span in the six groups, superseded lines dropped — and their sections leave the file; between majors every release keeps its section (POS.0730, intent 3.38, the principal's suggestion after the third render). First applies at 4.0. | Claude | 2026-09-05 |
| 0.9 | The bullet shows both sides of a Notes line — what changed with its pointer, then "For you:" and what it means for the reader — carried verbatim from the row; the principal's direction after the second render, which had the consequence without the fact (POS.0310, intent 3.37). | Claude | 2026-09-05 |
| 0.8 | A major's heading says "approved" only; the tag is named in the highlights when a row or decision records it. The 0.7 render had written "tag v3", "tag v2", "tag v1": the real tag is `v3.0`, and the public history starts at 3.0, so v1 and v2 never existed — a false claim caught by the principal's review (POS.0810). | Claude | 2026-09-05 |
| 0.7 | THR.0310 closed (intent 3.35, POS.0730 rewritten): one section per release of the engine — every version — newest first, six fixed groups (Action required, Added, Changed, Removed, Fixed, Rejected) compiled from the Notes lines of the intent's history rows, never distilled; approved majors carry the tag on the heading and a highlights paragraph; the Unreleased section dropped; the reader named as the user of the engine who takes upgrades through `forge-pull`; the previous edition in the narrative shape replaced whole once. | Claude | 2026-09-05 |
| 0.6 | Rendered by every `/release` of the engine, not by every `/save` (POS.1100, intent 3.33); "ordinary release" replaces "ordinary save" in the Instructions. | Claude | 2026-09-05 |
| 0.5 | Instructions require the intent's current vocabulary (resource index, document, artefact, history companion) even where an older history row uses a word since renamed — check-forge finding of the 3.30 save: the regenerated Unreleased head had picked up "material index" from the rows around THR.0230. The render is not regenerated for this; the next save brings it current. | Claude | 2026-09-05 |
| 0.4 | The fine-grained log named in the companion `10-intent.history.md` in Instructions and Template too, not only in Inputs (check-forge finding of the 3.21 save). | Claude | 2026-09-04 |
| 0.3 | Inputs read the intent's Version History from its companion `10-intent.history.md`, the intent itself for the current state. First row of the companion (POS.0310): 0.1 and 0.2 (2026-08-17) live in git. | Claude | 2026-09-04 |
