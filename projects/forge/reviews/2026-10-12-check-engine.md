---
date: 2026-10-12
project: forge
check: engine
target: the engine root (C:\pche\_dev\forge-of-thought)
reviewer: check engine (isolated context)
---

# Check (engine) — the engine (C:\pche\_dev\forge-of-thought) — 2026-10-12

6 findings (one further matter known as FND.1440, still parked)

## Findings

### FND.1520 — low — The work skill attributes the language of a work specification to prime directive 6, which places neither the specification nor the file
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\work\SKILL.md:11-13 ("prime directive 6: the specification in the project's language, the file in whatever language the work needs"), against C:\pche\_dev\forge-of-thought\CLAUDE.md:52-65 (prime directive 6 places the artefacts of the chain, the briefs, records, state, research, recipes and renders; the work kind is not named) and C:\pche\_dev\forge-of-thought\projects\forge\10-intent.md:789-820 (POS.1520 says nothing of the language either).
- **Rule:** Core internal consistency: a skill cites a mechanism by path to its owner and the owner carries the rule (CLAUDE.md, prime directive 10; POS.1070); a new kind's rules are not introduced in a skill alone (prime directive 2).
- **Fix:** Intent-first: one sentence in POS.1520 saying in which language the specification and the file are written, mirrored into prime directive 6's list (the specification beside the artefacts of the chain, the file as `## Making` says), so the skill's citation holds.

### FND.1530 — low — Versioning & status says "every artefact and every recipe alike, no exception" where Document kinds now has a third versioned kind
- **Where:** C:\pche\_dev\forge-of-thought\CLAUDE.md:518-520, against C:\pche\_dev\forge-of-thought\CLAUDE.md:195 (the work row: "Versioned: yes, the specification") and C:\pche\_dev\forge-of-thought\templates\work.md:1-8 (the specification carries version, date, status, last_change and a history companion).
- **Rule:** Core internal consistency: Document kinds ↔ Versioning & status (CLAUDE.md); the templates agree with Versioning & status.
- **Fix:** Reword to "every artefact, every recipe and every work specification alike, no exception" (POS.0310's own enumeration, 10-intent.md:943-944, is the intent's to bring along in the same round).

### FND.1540 — low — POS.1080 says the documents fall into five groups while its own table, and CLAUDE.md's, have six
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\10-intent.md:881 ("fall into five groups"), against 10-intent.md:890-904 (six groups: artefacts, records, state, rendering, work, resources) and C:\pche\_dev\forge-of-thought\CLAUDE.md:183-197 (the same six).
- **Rule:** Core ↔ forge intent: the core's Document kinds table is "the one page from which all of this is read, in the intent, in CLAUDE.md and in the README alike" (POS.1080), and the position's sentence contradicts the table it introduces.
- **Fix:** "six groups" in POS.1080, recorded with the round that added the work kind.

### FND.1550 — low — The readme recipe cites a closed thread, THR.0340, as the owner of the pinned facts' place
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\recipes\readme.md:262-263 ("brief `documentation`, THR.0340: the place of the pinned facts"), against C:\pche\_dev\forge-of-thought\projects\forge\threads.md (THR.0340 absent, closed 2026-10-09 per POS.0930 and REJ.0240) and C:\pche\_dev\forge-of-thought\projects\forge\10-intent.md:1647-1650 (POS.1450: facts no file owns have one place in the project that both the README and the documentation read).
- **Rule:** Core ↔ forge intent: nothing closed is still advertised in the core; a rule is cited at its owner (POS.1070). The README is a render the core names and this recipe is its source.
- **Fix:** Cite POS.1450 (and SOL.0500, which names the recipe as that place) in the heading's note instead of the brief and the thread.

### FND.1560 — low — The executive-pitch recipe still presents the idea as "locked" and never changing, a rule withdrawn with the brief's locking
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\recipes\executive-pitch.md:88 (S02: "The idea enters as written and never changes"; diagram "idea (locked) → working shape (rewritten)"), against C:\pche\_dev\forge-of-thought\projects\forge\10-intent.md:452-455 (POS.0110: a brief "is not locked and not immutable") and threads.md:729-730 (THR.0520: "The locking of a brief is withdrawn").
- **Rule:** Rename/removal sweep: a term the principal has dropped survives in a tool, not a historical record; the same defect as FND.0950 in the readme recipe. The stale render `renders/executive-pitch.md` is not a finding (POS.0570).
- **Fix:** Reword S02 to the brief as approved on the principal's word and then mined ("idea (approved)"), at the recipe's next iteration.

### FND.1570 — low — THR.0400 names the proposed gate `scripts/hook-gate.ps1`, a PowerShell script, after the scripts became Python
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\threads.md:457-458, against C:\pche\_dev\forge-of-thought\CLAUDE.md:478-488 (Portability: Python 3.8 or newer, nothing Windows-only) and 10-intent.md:1262-1266 (POS.0830: the scripts are Python, done 2026-10-09, THR.0150 closed). The other `.ps1` mentions in the thread (threads.md:479, :495) and in THR.0370 (:430) recount incidents of their date and stand as record.
- **Rule:** Rename/removal sweep: a live proposal still carries a dropped form; the thread is open work, not a historical record.
- **Fix:** `scripts/hook-gate.py` in the proposal, when the thread is next written.

### low — POS.1420 claims a check that keeps the solution design true against what realises it, and no check does
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\10-intent.md:786-787, against the five check files C:\pche\_dev\forge-of-thought\.claude\agents\check-*.md.
- **Rule:** Core ↔ forge intent: every POS is honoured by the core documents.
- **Fix:** As agreed 2026-10-10: word the sentence as what is wanted, naming THR.0520, in the first 5.x round.
- **Known as:** FND.1440, still parked
