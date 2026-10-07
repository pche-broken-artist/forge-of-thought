---
date: 2026-10-07
project: forge
check: light
target: projects/forge
reviewer: check light (isolated context)
---

# Check (light) — projects/forge — 2026-10-07

1 finding

## Findings
### FND.1020 — low — A file of no kind sits in the project root, registered nowhere
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\proposal-documentation.md:1-20 (front-matter `date`, `title`, `author`, `judged: not yet`; its own opening says it is "a working file, not a document of a kind the forge knows" and that "a check will name it")
- **Rule:** CLAUDE.md, Document kinds — "Document" is the word for every file of a project and every document has one kind, and the kinds table has none for a handed-over proposal; CLAUDE.md, Ledger — the ledger is the single source of truth for state, and the file has no row in any table and no companion. No DEC in `decisions.md` accepts it as it stands (DEC.0010 and DEC.0140 concern other matters).
- **Fix:** On the principal's word, walk the proposal through and then delete the file or move it as its own note says (what he accepts landing in the intent, the solution design and the recipes), or give working files a home first (the brief `next-gen`, "Further outputs and working files"); until then one line under Waiting on principal citing the file would make the ledger say what is open.

Everything else verified squares up and is not reported: front-matter and status of the three briefs, the intent (4.58), the solution design (0.3) and the six recipes against their companions' newest records and `last_change`; the log shape of every companion written since the archives; the Briefs, Documents, Renders and Published tables against disk and the renders' provenance front-matter (C:\pche\_dev\forge-of-thought\README.md, RELEASE-NOTES.md, CONTRIBUTING.md, projects\forge\renders\*.md); the 4 sources and 39 research notes against the ledger and both `00-INDEX.md` files (the `.docx` without an extract is the normal case); every review and challenge file cited by the Findings and Challenges tables exists, including the untracked C:\pche\_dev\forge-of-thought\projects\forge\reviews\2026-10-05-check-single-source-of-truth.md; the Dependencies table is empty and no citation points outside the project; Waiting on principal names exactly the 35 threads of C:\pche\_dev\forge-of-thought\projects\forge\threads.md plus the open and parked findings and CHL.0150. The four findings of the last `light` run (FND.0890 to FND.0930) stay resolved; none stands again.
