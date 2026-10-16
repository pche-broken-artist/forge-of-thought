---
date: 2026-10-16
project: forge
check: light
target: projects/forge
reviewer: check light (isolated context)
---

# Check (light) — C:\pche\_dev\forge-of-thought\projects\forge — 2026-10-16

3 findings

## Findings

### FND.1690 — low — The Waiting on principal line for the layer with an external audience (THR.0360) still says the brief `brd` is "to be born"
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:400-402`. The brief exists: `C:\pche\_dev\forge-of-thought\projects\forge\00-brief-brd.md` is at version 0.2, status draft, dated 2026-10-16, and the Briefs row at `ledger.md:34` says the same.
- **Rule:** CLAUDE.md, Ledger: "Waiting on principal" matches what is actually open, and the ledger is kept current after every operation.
- **Fix:** immediate fix: rewrite the line to say the brief `brd` was born 2026-10-16 and stands at 0.2 draft, with the IDs being decided one at a time, citing the Briefs row and not copying it.

### FND.1700 — low — The ledger header `updated:` is a day behind the ledger's own content
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:5` (`updated: 2026-10-15`). The ledger has been changed since: the Briefs row `ledger.md:34` records a brief born 2026-10-16.
- **Rule:** `templates/ledger.md` header (`updated: YYYY-MM-DD`); CLAUDE.md, Ledger (keep it current after every operation).
- **Fix:** immediate fix: set `updated: 2026-10-16`.

### FND.1710 — low — The Dependencies row for the library bundle `fork-brd` does not list the new brief that cites it
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:106` ("Used by": `sources/00-INDEX.md; the research of the BRD layer of 2026-10-13`). Not listed: the citations at `C:\pche\_dev\forge-of-thought\projects\forge\00-brief-brd.md:29` (`projects/lib-allwyn/sources/fork-brd/template-brd.md`) and `:86` (`projects/lib-allwyn/sources/fork-brd/`). Both paths exist on disk.
- **Rule:** CLAUDE.md, Ledger and POS.1020: every chain citation pointing outside the project has a row in Dependencies. The row exists, but its "Used by" column no longer names everything that uses it (`templates/ledger.md`, Dependencies).
- **Fix:** immediate fix: add `00-brief-brd.md` to the row's "Used by" cell.

## Facts
- `00-brief.md` has no version and no companion. This is the placeholder accepted under DEC.0010, so it is not raised.
- `sources/word-default-a4.docx` is a binary without an extract. Under POS.1040 that is the normal case.
- There is no `work/` directory and the Work table is empty. That is the normal case before a first work product.
