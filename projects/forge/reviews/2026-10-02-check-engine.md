---
date: 2026-10-02
project: forge
check: engine
target: the engine (C:\pche\_dev\forge-of-thought)
reviewer: check engine (isolated context)
---

# Check (engine) — engine (C:\pche\_dev\forge-of-thought) — 2026-10-02

7 findings

## Findings

### FND.0760 — medium — CLAUDE.md still opens by calling the brief a "verbatim record", the wording dropped at 4.48
- **Where:** C:\pche\_dev\forge-of-thought\CLAUDE.md:6-7 ("travels a fixed chain of versioned documents from verbatim record onward"), against CLAUDE.md:156, 185-186 and 204-205 (the brief is "the idea put together", "Claude may work on the text")
- **Rule:** Rename/removal sweep of this check. "Stored verbatim" left POS.0060 at 4.48 because it "read as a ban on Claude working on the text of a brief" (C:\pche\_dev\forge-of-thought\projects\forge\10-intent.history.md:134). POS.0110 says a brief "is not the record of the finding". Only historical records may still carry the dropped term.
- **Fix:** Reword CLAUDE.md:7 so the chain starts at what the brief now is, e.g. "from the idea put together onward".

### FND.0770 — medium — The forge's readme recipe pins the dropped "verbatim" brief in three places, so the README regenerated at this release will carry it again
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\recipes\readme.md:119-120 ("your own text, locked verbatim once it is done"), :148-150 ("the briefs are the exception, stored verbatim in whatever language they were written"), :492 ("an idea is dumped verbatim as a brief")
- **Rule:** README ↔ CLAUDE.md: a claim that CLAUDE.md or the intent no longer supports is a recipe defect, fixed in the recipe. CLAUDE.md, prime directive 6 (CLAUDE.md:60-61, "kept in whatever language they are written in"); POS.0060 and POS.0110 of the forge intent; the brief's definition (C:\pche\_dev\forge-of-thought\.claude\skills\forge\states\brief.md:118-131).
- **Fix:** Iterate the recipe before the release render so the three passages follow prime directive 6 and POS.0110 (kept in the language it was written in; the principal's by his approval, composed and then locked).

### FND.0780 — medium — POS.1370 (how sure a claim is, said in words) has no home in the operating layer
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\10-intent.md:345-355 (POS.1370). Nothing in C:\pche\_dev\forge-of-thought\CLAUDE.md (prime directives, 31-90), `.claude/skills/` or `templates/` states it; the nearest text, prime directive 1 (CLAUDE.md:32-39), covers only what Claude reads in a source.
- **Rule:** Core ↔ forge intent: every POS is honoured by the core documents. POS.1370 says the rule "is Claude's conduct and therefore holds in every layer of the chain and in the conversation"; POS.1030 says the forge's behaviour lives in the engine.
- **Fix:** Give the rule one sentence in CLAUDE.md, beside prime directive 1: what Claude brings as knowledge says in plain words whether it is verified and on what, unverified, or a hypothesis.

### FND.0790 — low — POS.1320's rule that Claude says aloud how each area of a Map stands is in no definition
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\10-intent.md:269-282 (POS.1320, the sentence added at 4.46), against the Map blocks of C:\pche\_dev\forge-of-thought\.claude\skills\forge\states\brief.md:85-93, intent.md:44-47 and assignment.md:44-48, and CLAUDE.md:195-202, which cites POS.1310 only.
- **Rule:** Core ↔ forge intent: every POS is honoured by the core documents. POS.1320 gives four standings (found, considered and left open, considered and found not to apply, not looked at), said aloud and nothing recorded.
- **Fix:** Cite POS.1320 beside POS.1310 in the definition paragraph of CLAUDE.md, Document chain (195-202), as the owner of how a Map is walked, so the three state files inherit it without restating it.

### FND.0800 — low — The recipe skeletons carry `updated`, while Versioning & status names `date` for every versioned document
- **Where:** C:\pche\_dev\forge-of-thought\CLAUDE.md:464-467, against C:\pche\_dev\forge-of-thought\templates\recipe.md:6, recipe-presentation.md:6, recipe-readme.md:6 and recipe-release-notes.md:6.
- **Rule:** Templates agree with CLAUDE.md, Versioning & status (front-matter fields). POS.0710 says a recipe carries "a version and an updated date in front-matter … and no status"; that sentence left Document chain 7 at 4.49 (CLAUDE.md:278-279 now points to Versioning & status), which states only the missing status.
- **Fix:** Extend the recipe clause at CLAUDE.md:467 to "a recipe carries `updated` in place of `date`, no status, and stays 0.x".

### FND.0810 — low — POS.0850 still names the critique and challenge skills as owners of what each verdict writes
- **Where:** C:\pche\_dev\forge-of-thought\projects\forge\10-intent.md:119-129, against C:\pche\_dev\forge-of-thought\.claude\skills\walkthrough\SKILL.md:83-91, critique\SKILL.md:42-44, challenge\SKILL.md:48-51 and check\SKILL.md:57-60.
- **Rule:** Core ↔ forge intent, and POS.0120 ("where the item and its file say different things, that is a finding"). Since 4.48 the walkthrough skill owns what `reject`, `park` and `obsolete` write; the producing commands, `/check` among them, say only what `accept` writes.
- **Fix:** Mend POS.0850's pointer: the walkthrough skill for the shared verdicts, the three producing commands for `accept`.

### FND.0820 — low — "UK English" survives in two genre skeletons after the demand for British English was dropped
- **Where:** C:\pche\_dev\forge-of-thought\templates\recipe-readme.md:33; C:\pche\_dev\forge-of-thought\templates\recipe-release-notes.md:75
- **Rule:** Rename/removal sweep. The 4.49 record of POS.0250 (C:\pche\_dev\forge-of-thought\projects\forge\10-intent.history.md:137) drops the demand because the language is the project's (POS.0060). The drop named the assignment's sentences only; the same reason reaches these skeletons, which `/new-project` scaffolds into every project whatever its language. CLAUDE.md, prime directive 6, leaves a render's language to its recipe, and `/recipe` step 2 asks for it (C:\pche\_dev\forge-of-thought\.claude\skills\recipe\SKILL.md:32-37).
- **Fix:** Replace "UK English" in both skeletons with a language placeholder, as C:\pche\_dev\forge-of-thought\templates\recipe-presentation.md:30 has it (`Language: <English>`).
