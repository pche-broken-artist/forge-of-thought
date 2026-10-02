---
date: 2026-10-02
project: forge
check: light
target: projects/forge
reviewer: check light (isolated context)
---

# Check (light) — projects/forge — 2026-10-02

1 finding

## Findings

### FND.0730 — low — A history record carries a subject the log's shape does not have: `operating layer`
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\10-intent.history.md:134`
- **Rule:** `templates/history.md` (lines 12-14), the owner of the log's shape by CLAUDE.md, Versioning & status: the subject is an ID, several IDs, or a place without an ID, which is a section or the file. `operating layer` is none of these (the intent has a section "Operating environment" at `10-intent.md:1048`, no section of this name). The record also states a rule of its own in its last sentence ("A change of the operating layer that changes no item of the intent is recorded under this subject, one record a round"), which neither `templates/history.md`, CLAUDE.md nor the intent carries; a search of all three for the wording found only the template's line on a place without an ID.
- **Fix:** Either name the subject of this record as the template allows (the file, `10-intent.md`) while version 4.48 is still unsaved, or, on the principal's decision, add the operating layer to the places a subject may name in `templates/history.md`, so that the rule stands in its owner and not only in a record.

Nothing else in the lens's scope was found. No earlier `*-check-light.md` report exists in `reviews/`, and no row of the ledger's Findings table covers this, so the finding is new.
