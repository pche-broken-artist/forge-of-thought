---
date: 2026-10-13
project: forge
check: light
target: projects/forge
reviewer: check light (isolated context)
---

# Check (light) — C:\pche\_dev\forge-of-thought\projects\forge — 2026-10-13

3 findings

## Findings

### FND.1610 — medium — The Documents table is two versions behind the intent and one behind the solution design
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:39-40` (10-intent.md | 5.6 | draft | 2026-10-12; 40-solution-design.md | 0.14 | draft | 2026-10-12) against `C:\pche\_dev\forge-of-thought\projects\forge\10-intent.md:2-3` (version 5.8, date 2026-10-13) and `C:\pche\_dev\forge-of-thought\projects\forge\40-solution-design.md:2-3` (version 0.15, date 2026-10-13); the history companions carry the records of 5.7 and 5.8 (`10-intent.history.md:352-353`) and of 0.15 (`40-solution-design.history.md:53`), and `last_change` in both front-matters is derived from them.
- **Rule:** CLAUDE.md, Ledger — the ledger is the single source of truth for state, kept current after every operation; the Documents table mirrors front-matter (`templates/ledger.md`, Documents).
- **Fix:** immediate fix: set the two rows to `10-intent.md | 5.8 | draft | 2026-10-13` and `40-solution-design.md | 0.15 | draft | 2026-10-13`.

### FND.1620 — low — The `strategy` matter under Waiting on principal still has no ID after two writes of the intent
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:360-364` (the free-text line ends "a thread at the next write of the intent"); the intent has since been written twice on 2026-10-13, 5.7 and 5.8 (`C:\pche\_dev\forge-of-thought\projects\forge\10-intent.history.md:352-353`), and `C:\pche\_dev\forge-of-thought\projects\forge\threads.md` has no thread on it (the only hits for "strateg" are THR.0620's and the brief next-gen's examples at lines 541 and 837; no THR.0660 exists).
- **Rule:** CLAUDE.md, Ledger — free text under Waiting on principal only for a matter with no ID yet, which gets one at the next write. Follows FND.1600 (light check of 2026-10-13, resolved by the line): the deferral that line set has lapsed; not the same finding, so not reopened.
- **Fix:** open a thread for the `strategy` artefact at the next write of the intent and cut the line to the ID with a few words and its state; if the principal prefers the matter tracked in the ledger of the project ai-strategy alone, say so in the line instead.

### FND.1630 — low — One Findings row names its source review with a directory prefix where every other row carries the bare file name
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:322` (`reviews/2026-10-13-check-light.md`) against the 158 rows above it (`2026-10-12-check-light-2.md` and the like).
- **Rule:** CLAUDE.md, Ledger — the ledger's tables are `templates/ledger.md`'s; one form per column, as the table itself has established it.
- **Fix:** immediate fix: write the cell as `2026-10-13-check-light.md`.

## Facts
- The source `word-default-a4.docx` is a binary without an extract (POS.1040): the normal case, not a finding.
- The brief `00-brief.md` carries no version and no companion: the placeholder accepted under DEC.0010, not raised.
- No `work/` directory and no `sources/.gitignore` exist; the Work table is empty and consistent with the disk; the Dependencies table is empty and no chain file, brief, thread, recipe or resource index cites a path outside the project: consistent, not a finding. The `Action` of the 5.7 record (renaming an existing work product's files) has nothing to act on in this project.
- Every other table agrees with the disk: the four briefs with their front-matter; all thirteen history companions present with the template's front-matter and comment, the newest records in the log's shape, `last_change` of the intent and of the solution design derived from their newest records; the eight Renders rows mirror the provenance of README.md, RELEASE-NOTES.md, CONTRIBUTING.md, docs/README.md and the four files of `renders/`; the three Published rows have their files and the three files their rows; the five sources and forty-two research notes each have a ledger row and an index entry and every row and entry its file; every file of `reviews/` and `challenges/` is cited by a Findings or Challenges row (the four files named outside the convention accepted under DEC.0140); every open thread of `threads.md` (thirty-three) has its line under Waiting on principal.
