---
date: 2026-10-09
project: forge
check: light
target: projects/forge
reviewer: check light (isolated context)
---

# Check (light) — projects/forge — 2026-10-09

2 findings

## Findings
### FND.1050 — low — Waiting on principal says the README is not yet cut while the ledger's own Renders row and the readme recipe's history record the cut as done today
- **Where:** projects/forge/ledger.md:335-341 (the THR.0340 line: "the README not yet cut"), against ledger.md:47 (README.md rendered 2026-10-09 from recipe v0.58) and projects/forge/recipes/readme.history.md:26-27 (0.57 of 2026-10-09: "The README is cut to what orients and points"; 0.58 the documentation link on the first line). The same line also carries a matter no longer open: "`proposal-documentation.md` deleted 2026-10-09 (FND.1020 resolved)", a resolved finding named under what waits.
- **Rule:** CLAUDE.md, Ledger — the ledger is the single source of truth for state and is kept current after every operation; under Waiting on principal a matter with an ID gets one line, the ID, a few words, its state; Lens of this check — Waiting on principal matches what is actually open.
- **Fix:** immediate fix: in the THR.0340 line drop "the README not yet cut" (or say the README was cut and re-rendered 2026-10-09, recipe 0.58) and drop the clause on `proposal-documentation.md` and FND.1020, which is resolved in the Findings table (ledger.md:240) and waits on nothing.

### FND.1030 — low — The documentation map sits in the project root without a kind and without a row
- **Where:** projects/forge/docs-map.md:1-6 (front-matter `generated`, `target`, `owner`, `previous`; no `version`, no companion, no row in any ledger table; named only inside the THR.0340 line of Waiting on principal, ledger.md:337-338)
- **Rule:** CLAUDE.md, Document kinds — every file of a project has one kind; CLAUDE.md, Ledger — the single source of truth for state (as filed in `reviews/2026-10-09-check-light.md`). No DEC in `decisions.md` accepts it as it stands.
- **Fix:** As filed: on the principal's word give the map a kind and a home through the brief `documentation` (THR.0340), or move it out of the project root to the engine's gitignored `tmp/` until then; a ledger row cannot be written before the kind exists.
- **Known as:** FND.1030, still open
