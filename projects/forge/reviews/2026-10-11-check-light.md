---
date: 2026-10-11
project: forge
check: light
target: projects/forge
reviewer: check light (isolated context)
---

# Check (light) — C:\pche\_dev\forge-of-thought\projects\forge — 2026-10-11

1 finding

## Findings

### FND.1490 low — A matter under Waiting on principal still has no ID after three later writes
- **Where:** `C:\pche\_dev\forge-of-thought\projects\forge\ledger.md:393-397` (the free-text line: the new output of `forge-pull.py` and the states `behind` and `diverged` of `remote_state` untested, a test on a throwaway clone deferred 2026-10-11); nothing in `C:\pche\_dev\forge-of-thought\projects\forge\threads.md` or `C:\pche\_dev\forge-of-thought\projects\forge\40-solution-design.md` carries the matter (SOL.0510 at line 684 names the states, not that they are untested; the only "untested" in the threads is THR.0500's, line 852, on another subject).
- **Rule:** CLAUDE.md, Ledger — the ledger cites and never copies; under Waiting on principal free text only for a matter with no ID yet, which gets one at the next write. The line was written in the round of intent 5.1 (`10-intent.history.md:318-323`); the intent has since been written at 5.2 and 5.3 and the solution design at 0.10 to 0.13 (`40-solution-design.history.md:43-50`) without the matter receiving an ID.
- **Fix:** at the next write of the intent open a thread for the deferred test of `forge-pull.py` (or, if the principal prefers, record it as the open part of SOL.0510) and cut the ledger line to the ID, a few words and its state.
