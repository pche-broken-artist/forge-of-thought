---
date: 2026-11-08
project: forge
check: project
target: projects/forge
reviewer: check project (isolated context)
---

# Check (project) — projects/forge — 2026-11-08

1 finding

## Findings

### FND.3910 — low — The contributor's engine check of 2026-11-02, an immutable report, was edited at the merge: its first finding now reads FND.3890, born as FND.3820
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\reviews\2026-11-02-check-engine-1528-01b4.md:15 (`### FND.3890 — medium — …`); the renumbering recorded in C:\pche\_dev\forge-of-thought\projects\forge\10-intent.history.md:782 ("FND.3890 | changed | renumbered from FND.3820 of the contributor's engine check of 2026-11-02, which collided with FND.3820 of the light check of 2026-11-07 (POS.0220) | Was: FND.3820"); the ledger C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:605 and :612 reads both numbers from the record and the report consistently.
- **Rule:** A review is immutable from its creation; corrections happen downstream (CLAUDE.md, Versioning & status, Immutable documents; Document kinds, review). POS.0220 settles a clash by renumbering the younger item "with a `changed` record … its citations corrected", and calls that "a write into the artefacts"; a report is no artefact and the one place the FND lives besides the ledger (CLAUDE.md, ID scheme, FND). The record exists, but no owner says that a clash of FND numbers may be settled inside the report, and no DEC accepts this edit: DEC.0110, DEC.0330 and DEC.0370 each accept one named edit of an immutable and no other, and the merge rule POS.1790 speaks of the artefacts' IDs and versions only. The reopening of 2026-10-24 was treated the same way (FND.2960, DEC.0350).
- **Fix:** On the principal's word, a DEC on the pattern of DEC.0350 accepting the edited report as recorded, never raised again; and, where the forge is to have a way for the next merge, one sentence in POS.0220 or POS.1790 saying how a finding of an immutable report is renumbered after a merge (the record and the ledger alone, the report left as filed, or the report edited as the one exception).

## Facts
- projects/forge is not a repository of its own: the engine's repository tracks it (CLAUDE.md, Persistence). It therefore has no `.gitattributes` of its own: the engine root's C:\pche\_dev\forge-of-thought\.gitattributes lines 10-18 carry the three anchored root files, `projects/forge/renders/**` and `projects/forge/published/*` (SOL.0730). Its `.gitignore` carries only `/tmp/`; the ledger and the Office lock files are ignored by the engine root's `.gitignore`.
- `renders/state.md` carries the ledger's front-matter, not a render's provenance, by design (POS.1650).
- The group "Research" of the intent starts at POS.1860: formed 2026-10-25 by moving four existing items out of the group Review (intent history, 5.38), which POS.0220 allows; "Operating environment" starts at POS.0510 because POS.0500 was removed (intent history, 4.56). Neither is a finding.
- The history of `00-brief-user-stories.md` (records of 2026-11-02 to 2026-11-06) names its sections and quotes its `Was` wording in Czech, the brief's language until its translation at 0.6; the records' own words are English and a brief keeps its language (CLAUDE.md, prime directive 6). Not a finding.
- Earlier decisions accept these states, so they are not raised again: POS.0005 and REJ.0125 outside the tens (DEC.0110); the group "Working methods" starting at POS.0850 (DEC.0130); the recorded one-off edits of immutables of 2026-08-30 and 2026-09-04 (DEC.0110), of 2026-09-30 (DEC.0330, FND.2720 rejected) and the reopening of the research bundle of 2026-10-24 (DEC.0350, FND.2960 rejected); the four review files named outside the convention (DEC.0140), the two with a run number before the tail (FND.2430, resolved as they stand) and the critique report of another engine (DEC.0370, FND.3560 rejected); `00-brief.md` as a placeholder (DEC.0010). FND.3550 is resolved: `templates/recipe.md` now says how a leading slash in `output:` is read, and the three root recipes stand.
