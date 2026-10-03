---
date: 2026-10-03
project: forge
check: light
target: projects/forge
reviewer: check light (isolated context)
---

# Check (light) — projects/forge — 2026-10-03

1 finding

## Findings
### FND.0890 — low — The change of THR.0520 at 4.52 has no record in the intent's history, though `last_change` names it
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\10-intent.history.md:161-165` (the five records of 4.52: POS.1390 to POS.1420, POS.0900, POS.0110, POS.0160, operating layer; none with the subject THR.0520); against `C:\pche\_dev\forge-of-thought\projects\forge\10-intent.md:5` (`last_change` 4.52: "THR.0520 walked through, ten matters ... the plan of six steps in the thread") and `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:252-255` ("walked through 2026-10-03 (intent 4.52) ... the plan of six steps in the thread"). The only record of THR.0520 is its birth at 4.51 (`10-intent.history.md:159`). I did not compare the thread's text against its 4.51 wording (no access to git); the finding rests on `last_change` and the ledger both saying the thread was changed at 4.52.
- **Rule:** CLAUDE.md, Versioning & status: a round is one version and as many records as it made changes; the record is written in the same step as the change; `last_change` is derived from the records of the newest version. The threads file is part of the intent (CLAUDE.md, Document chain 2), so a change to a thread is recorded in `10-intent.history.md`.
- **Fix:** Append one record to `10-intent.history.md` in the shape of `templates/history.md` (`2026-10-03 | 4.52 | <author> | THR.0520 | changed | <reason> | Was: <the wording that ceased to hold, if any>`), on the principal's word; the existing records stay untouched.
