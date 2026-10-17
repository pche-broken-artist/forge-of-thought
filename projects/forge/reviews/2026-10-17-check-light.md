---
date: 2026-10-17
project: forge
check: light
target: projects/forge
reviewer: check light (isolated context)
---

# Check (light) - C:\pche\_dev\forge-of-thought\projects\forge - 2026-10-17

1 finding

## Findings

### FND.1720 - low - The brief `collaboration` puts eleven points to the principal and the ledger's Waiting on principal does not cite it
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:378-470` (the section Waiting on principal, no line for the brief) against `C:\pche\_dev\forge-of-thought\projects\forge\00-brief-collaboration.md:538-561` (the section "Open, for the principal to decide", eleven points) and the Briefs row `ledger.md:35` ("open: eleven points listed in the brief"). The brief is a draft 0.6 of today, handed over with the principal's judgement outstanding; the same case was settled for the recipe `ba-intro` by FND.1510 and for a handed-over matter by FND.1600.
- **Rule:** CLAUDE.md, Ledger (Waiting on principal names what waits, one line per matter, cite never copy) and `templates/ledger.md`, Waiting on principal.
- **Fix:** immediate fix: one line under Waiting on principal citing the brief `collaboration` 0.6 and its section "Open, for the principal to decide", nothing of the eleven points copied.

## Facts
- `00-brief.md` carries no version and no companion: the placeholder accepted under DEC.0010, not raised.
- `sources/word-default-a4.docx` is a binary without an extract (POS.1040): the normal case; no `sources/.gitignore` exists and none is needed, nothing was converted in place.
- No `work/` directory and an empty Work table: the normal case before a first work product.
- FND.1680 of the report of 2026-10-15 stands resolved on disk: `C:\pche\_dev\forge-of-thought\projects\lib-allwyn\sources\fork-brd\00-INDEX.md` is present, the one Dependencies row points at it; no index entry, recipe or chain citation points outside the project without a row.
- Everything else conforms, confirmed against disk: the Documents rows (intent 5.12, solution design 0.17, both `draft`, 2026-10-15) match the front-matter and each `last_change` summarises the newest records of its companion (`10-intent.history.md:363`, `40-solution-design.history.md:60-62`); the five briefs' front-matter (1.0 approved, 1.0 approved, 0.3 draft, 0.1 draft, 0.6 draft) matches the Briefs rows, the new `00-brief-collaboration.history.md` carries the template's comment and twenty-three records in the one-line log shape, 0.1 to 0.6 all of today, author the instance's handle, `last_change` 0.6 derived from the 0.6 records; the seven recipes carry `updated`, no status, 0.x versions matching their newest records; all fourteen companions and eight archives present, every record in the log shape (the fourteen non-record bullet lines are the template's comment line, one per companion); the eight Renders rows mirror the provenance front-matter of README.md, docs/README.md, RELEASE-NOTES.md, CONTRIBUTING.md and the four Markdown renders word for word; the three Published rows and the three files of `published/` agree one to one; the twelve sources (seven of them registered today) and the forty-seven research notes (two of them today's) are registered in the ledger and both `00-INDEX.md` files carry one entry per file, the sources index the library bundle as a thirteenth, cited entry; every file of `reviews/` (40) and `challenges/` (4) is cited by a Findings or Challenges row, the four files outside the naming convention under DEC.0140; every state word is the template's; the thirty-six threads under Waiting on principal are exactly the thirty-six open in `threads.md`, TBC.0010 and TBC.0020 are carried by the lines of THR.0370 and THR.0520 they point to, TBC.0030 has its own line; header `kind: thought`, `language: en`, `updated: 2026-10-17`.
