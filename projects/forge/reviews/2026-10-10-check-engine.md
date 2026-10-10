---
date: 2026-10-10
project: forge
check: engine
target: the engine
reviewer: check engine (isolated context)
---

# Check (engine) — the engine (C:\pche\_dev\forge-of-thought) — 2026-10-10

6 findings

## Findings

### FND.1410 — medium — POS.0950's rule for every agent that writes an outward-facing file is honoured by `/document` and not by `/render`
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\render\SKILL.md:21-37 (step 3, the subagent's prompt) and :58-62 (step 6, "verify the file exists and its provenance is correct"), against C:\pche\_dev\forge-of-thought\projects\forge\10-intent.md:1248-1256 (POS.0950: "every agent that writes an outward-facing file says in its definition that instance facts are not material and that an input is read from disk, and the generated files are scanned mechanically before they are kept"). The documentation side honours both halves: C:\pche\_dev\forge-of-thought\.claude\skills\docs-contract\SKILL.md:11-20 and C:\pche\_dev\forge-of-thought\scripts\docs-check.py:65 (`local_facts`). The render skill carries the read-from-disk half only (step 2); its prompt says nothing of instance facts in the subagent's context, and no mechanical scan runs on a render before it is kept — the README, the release notes and CONTRIBUTING.md are outward-facing files made this way. The closing record of THR.0580 (C:\pche\_dev\forge-of-thought\projects\forge\10-intent.history.md:255, :258) widened the rule "from CLAUDE.md to the whole context" and left the render skill only the read-from-disk sentence, which it has.
- **Rule:** Core ↔ forge intent: every POS is honoured by the core documents (POS.0950; POS.1030, the forge's behaviour lives in the engine).
- **Fix:** Either give `/render` step 3's prompt the sentence of the docs contract (whatever the context carries of the people who run this forge is not material) and step 6 a mechanical scan of the written file for the instance's facts as `docs-check.py` makes it, or, if the principal meant the documentation agents only, narrow POS.0950's "every agent" to them.

### FND.1420 — medium — The documentation agents' contract lacks the front-matter the three reviewer contracts carry, so it may not preload and is offered as a command
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\docs-contract\SKILL.md:1-3 (front-matter: `description` only), against C:\pche\_dev\forge-of-thought\.claude\skills\check-contract\SKILL.md:1-5, critic-contract\SKILL.md:1-5 and challenger-contract\SKILL.md:1-5 (`name: <contract>` and `user-invocable: false`) and C:\pche\_dev\forge-of-thought\.claude\skills\walkthrough\SKILL.md:1-4 (`user-invocable: false`); named in C:\pche\_dev\forge-of-thought\.claude\agents\docs-planner.md:6-7 and docs-writer.md:6-7 (`skills: - docs-contract`).
- **Rule:** Core internal consistency: every skill an agent names in `skills:` must load — Claude Code skips a missing one silently (this check's Lens); the Commands table ↔ the skills on disk (CLAUDE.md, Commands). Whether the harness resolves `skills:` by the directory name or by the `name` field is unverified from here; if by `name`, the planner and the writer run without their isolation and instance-facts rules and nobody is told. What is verified: without `user-invocable: false` the file is listed as a command `/docs-contract` that CLAUDE.md's table does not know, which the other contracts prevent.
- **Fix:** Add `name: docs-contract` and `user-invocable: false` to the front-matter, as the three reviewer contracts have them.

### FND.1430 — low — CLAUDE.md's layout comment describes the skills as three kinds and the agents as reviewers only; the documentation's contract and its two agents fit neither
- **Where:** C:\pche\_dev\forge-of-thought\CLAUDE.md:372-376 ("skills (the commands, the reviewers' contracts and the walkthrough method), agents, settings"), against C:\pche\_dev\forge-of-thought\.claude\skills\docs-contract\SKILL.md and C:\pche\_dev\forge-of-thought\.claude\agents\docs-planner.md, docs-writer.md; CLAUDE.md names neither (Document chain, Documentation, :329-340, points at the skill only; Isolated reviewers, :569-623, covers the reviewer agents).
- **Rule:** Core internal consistency: described agents ↔ `.claude/agents/`, and the layout comment ↔ what lies on disk (CLAUDE.md, Repository layout).
- **Fix:** Extend the comment to "skills (the commands, the contracts of the reviewers and of the documentation agents, and the walkthrough method), agents (the reviewers, the documentation's planner and writer), settings".

### FND.1440 — low — POS.1420 says a check keeps the solution design true against what realises it, and no check in the roster does
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\10-intent.md:785-786 ("A check keeps it true against what realises it."), against the five check files C:\pche\_dev\forge-of-thought\.claude\agents\check-*.md, none of which reads a solution design against the files it names; the question is held open in C:\pche\_dev\forge-of-thought\projects\forge\threads.md:959-960 (THR.0520, "which check keeps a solution design true against what realises it").
- **Rule:** Core ↔ forge intent: every POS is honoured by the core documents; POS.0120 (where an item and what realises it say different things, that is a finding, never mended in silence).
- **Fix:** Until the check exists, word the sentence as what is wanted and name the thread ("is to be kept true by a check, THR.0520"), so the position does not claim a mechanism the engine lacks.

### FND.1450 — low — "The system's own project" places the open threads THR in the intent, while the ID scheme places them in `threads.md`
- **Where:** C:\pche\_dev\forge-of-thought\CLAUDE.md:677-679 ("its brief, intent (design positions POS, open threads THR, rejected directions REJ)"), against CLAUDE.md:557 (THR "Lives in: the project's `threads.md`") and :391-392 (the layout's `threads.md`).
- **Rule:** Core internal consistency: CLAUDE.md against itself; POS.0120 (the threads live in a file of their own beside the intent). THR.0470 step 2 mended "what names the threads today" in CLAUDE.md and left this sentence.
- **Fix:** Reword to "its brief, intent (design positions POS, rejected directions REJ) with its threads (THR), decisions and ledger".

### FND.1460 — low — The brief skeleton pre-fills `last_change` by hand, where every other versioned skeleton derives it from the history
- **Where:** C:\pche\_dev\forge-of-thought\templates\brief.md:8 (`last_change: 0.1 (YYYY-MM-DD): draft begun.`), against C:\pche\_dev\forge-of-thought\templates\intent.md:5, assignment.md:5, solution-design.md:5, recipe.md:7 (`<derived from the records of the newest version in <file>.history.md>`).
- **Rule:** Templates agree with CLAUDE.md, Versioning & status (C:\pche\_dev\forge-of-thought\CLAUDE.md:517-519: `last_change` is derived from the records of the newest version by the write step that appends them, never by hand).
- **Fix:** Replace the value with `<derived from the records of the newest version in 00-brief.history.md>` as the other skeletons have it.
