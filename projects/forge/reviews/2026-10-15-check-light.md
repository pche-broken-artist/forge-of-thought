---
date: 2026-10-15
project: forge
check: light
target: projects/forge
reviewer: check light (isolated context)
---

# Check (light) — C:\pche\_dev\forge-of-thought\projects\forge — 2026-10-15

1 finding

## Findings

### FND.1680 — low (advisory) — The Dependencies row cites a library bundle that is not on disk alongside
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:105` (`projects/lib-allwyn/sources/fork-brd/ (bundle, its 00-INDEX.md)`) and the matching index entry `C:\pche\_dev\forge-of-thought\projects\forge\sources\00-INDEX.md:48-52`; against the library on disk: `C:\pche\_dev\forge-of-thought\projects\lib-allwyn\sources\` holds `allwyn.potx`, `allwyn-full.potx`, `allwyn.dotm`, `allwyn-cz-regulatory-report.md`, `it-pack/` and `00-INDEX.md` only — no `fork-brd/` and no inner index; the string `fork-brd` occurs nowhere in `projects/lib-allwyn/`, and the library's own ledger (`C:\pche\_dev\forge-of-thought\projects\lib-allwyn\ledger.md:4`, `updated: 2026-10-03`) registers no such bundle. The research notes `research/2026-10-13-the-brd-layer-of-the-fork-against-todays-engine.md` and `…-what-a-brd-contains-…` cite the bundle by that path (ledger rows 155-156). The check of 2026-10-14 saw the path on disk; today it is gone, so the library clone on disk is behind the state the dependency was registered against (or the bundle was never saved and pushed from the library side).
- **Rule:** CLAUDE.md, Ledger and POS.1020 — every path in the Dependencies table exists on disk; the library document is maintained by its owner and cited by path.
- **Fix:** bring the library on disk to the state that holds the bundle — `/pull lib-allwyn` if it was pushed, else save and push it from the instance that registered it on 2026-10-13; the ledger row and the index entry stay as they are (registration is correct, only the disk is behind).

## Facts
- `00-brief.md` carries no version and no companion: the placeholder accepted under DEC.0010, not raised.
- `sources/word-default-a4.docx` is a binary without an extract (POS.1040): the normal case.
- No `work/` directory and an empty Work table: the normal case before a first work product.
- Everything else conforms, confirmed against disk: the Documents rows (intent 5.9, solution design 0.16, both `draft`, dated 2026-10-14) match the front-matter, and each `last_change` summarises the 5.9 / 0.16 records of its companion; the four briefs' front-matter (1.0 approved, 1.0 approved, 0.3 draft, 0.1 draft) matches the Briefs rows; the seven recipes carry `updated`, no status, 0.x versions matching the Renders rows and the newest records (readme 0.66, release-notes 0.13, contributing 0.3, ba-intro 0.1, cto-pitch 0.6, ceo-pitch 0.6, executive-pitch 0.8); all thirteen companions exist with the template's comment and every record in the one-line log shape (the two archived briefs' logs are empty since the move, their archives present; eight archives in all); the eight Renders rows mirror the provenance front-matter of README.md, docs/README.md, RELEASE-NOTES.md, CONTRIBUTING.md and the four Markdown renders word for word (ba-intro: sixteen docs pages v5.3 and CONTRIBUTING.md); the three Published rows and the three files of `published/` agree one to one; the five sources and the forty-four research notes are registered and both `00-INDEX.md` files carry one entry per file (the sources index the library bundle as a sixth, cited entry); every file of `reviews/` (39) and `challenges/` (4) is cited by a Findings or Challenges row, the four files outside the naming convention under DEC.0140; every state word is the template's; FND.1670 of yesterday's report stands resolved on disk (the Waiting line names recipe 0.66), FND.0650 and FND.1440 rightly parked; the thirty-four threads under Waiting on principal are exactly the thirty-four open in `threads.md`; the header `kind: thought`, `updated: 2026-10-14`, nothing in the project changed since.
