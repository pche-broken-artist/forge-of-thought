---
date: 2026-10-09
project: forge
check: light
target: projects/forge
reviewer: check light (isolated context)
---

# Check (light) — projects/forge — 2026-10-09

3 findings

## Findings
### FND.1030 — low — A second file of no kind sits in the project root, registered nowhere
- **Where:** projects/forge/docs-map.md:1-6 (front-matter `generated`, `target: engine`, `owner: projects/forge`, `previous: none`; no `version`, no companion)
- **Rule:** CLAUDE.md, Document kinds — every file of a project has one kind, and the kinds table has none for a documentation map; CLAUDE.md, Ledger — the ledger is the single source of truth for state, and the file has no row in any table (the Waiting on principal line of THR.0340 at ledger.md:333-339 names it only as the input the `docs/` pages were generated from). No DEC in `decisions.md` accepts it as it stands. Same class as FND.1020, a different file.
- **Fix:** On the principal's word, give the map a kind and a home through the brief `documentation` (its birth was 2026-10-09, THR.0340) or move it out of the project root to the engine's gitignored `tmp/` until then; a ledger row cannot be written before the kind exists.

### FND.1020 — low — The handed-over proposal of 2026-10-05 still sits in the project root without a kind or a row
- **Where:** projects/forge/proposal-documentation.md:1-12
- **Rule:** CLAUDE.md, Document kinds; CLAUDE.md, Ledger (as filed in `reviews/2026-10-07-check-light.md`).
- **Fix:** As the ledger's own Waiting line says (ledger.md:338-339, "superseded in substance, not yet deleted"): delete the file on the principal's word, or move it to the engine's gitignored `tmp/`.
- **Known as:** FND.1020, still open

### FND.1040 — low — The brief `next-gen` carries the date of its birth while its newest version is six days younger
- **Where:** projects/forge/00-brief-next-gen.md:4 (`date: 2026-10-03`) against :6 (`version: 0.3`) and :8 (`last_change: 0.3 (2026-10-09): …`); the companion's newest record is dated 2026-10-09 (00-brief-next-gen.history.md:23)
- **Rule:** CLAUDE.md, Versioning & status — front-matter carries `version`, `date`, `status` and `last_change`, `last_change` derived from the records of the newest version; `templates/brief.md:4-8` shows `date` and the date in `last_change` as one date. The owner does not define `date` in words; the intent (10-intent.md:2-3, 4.59 of 2026-10-09) and the solution design (40-solution-design.md:2-3, 0.3 of 2026-10-04) carry the date of the newest version, and the ledger's Briefs table has no Date column to disagree with. Raised as a front-matter inconsistency with itself, not as a ledger mismatch.
- **Fix:** immediate fix: set `date: 2026-10-09` in the front-matter of 00-brief-next-gen.md, with the write of the current round, so that `date` and `last_change` name the same version's day as in every other versioned document of the project.

Verified and not reported: front-matter and status of the five briefs (the placeholder `00-brief.md` under DEC.0010), the intent 4.59, the solution design 0.3 and the six recipes against their companions' newest records and `last_change`; the log shape of every record written since the archives (fields in order, one line each, `Was` last; the two 4.59 records of the intent, the 0.3 record of `next-gen`, the birth record of `documentation`); `threads.md` carries no version by the intent's definition (Threads and files) and needs no companion; the Briefs, Documents, Renders and Published tables against disk and against the provenance front-matter of README.md, RELEASE-NOTES.md, CONTRIBUTING.md and the three files of `renders/`; the 4 sources and 39 research notes against the ledger and both `00-INDEX.md` files (the `.docx` without an extract is the normal case, POS.1040); every file cited by the Findings and Challenges tables exists in `reviews/` (19) and `challenges/` (3), no uncited file; the Dependencies table is empty and no index entry, recipe or chain citation points outside the project; no state word outside the template; Waiting on principal names exactly the 35 threads of `threads.md` plus the open and parked findings and CHL.0150. FND.0890 to FND.0930 stay resolved; none stands again.
