---
date: 2026-09-06
project: forge
lens: clarity
target: intent v3.44
reviewed: 10-intent.md v3.44; 10-intent.history.md (rows 3.38–3.44,
  for last_change and version agreement); decisions.md (DEC.0010–0090);
  ledger.md (updated 2026-09-06); reviews/2026-09-06-critique-clarity.md
  (FND.0290–0340, regression); reviews/2026-09-03-critique-clarity.md
  (its findings were verified in the run of the same morning and were
  not re-tested). reviews/2026-09-05-critique-harness.md carries a lens
  suffix of its own and is not this lens's; the retired single-critic
  reports (2026-08-17, 2026-08-27) were verified on 2026-09-03.
reviewer: critic lens clarity (isolated context)
---

# Critique (clarity) — 2026-09-06 (second run)

## Delta summary
- **New:** FND.0350, FND.0360, FND.0370, FND.0380, FND.0390
- **Verified resolved:** FND.0290, FND.0300, FND.0310, FND.0320,
  FND.0330, FND.0340
- **Still open:** —
- **Newly obsolete:** —
- **Respected:** FND.0090 (overruled, DEC.0090); nothing in 3.44
  touches its condition.

## Scope note
Target: the intent alone, read as the record of current intent. The
ledger and decisions were read for regression only. The front-matter
agrees with the companion: `version: 3.44`, `status: draft`, and
`last_change` summarises the newest row (it lists six aligned positions
where the row lists seven, THR.0210 omitted — a summary, not a
mismatch).

## Regression
- **FND.0290 — verified resolved.** POS.0540 no longer says check is
  not a reviewer; POS.1120 no longer says it is "the third kind"; the
  decided sentence has left THR.0290, which now carries the `/research`
  point only. One residue: POS.1120 still lists check inside "each kind
  of reviewer — the critic, the challenger, check on the same
  mechanism (POS.0540)" while POS.0540 says whether it is called a
  review "is not decided" (Recommendations).
- **FND.0300 — verified resolved, with a caveat.** POS.0810 and
  POS.0930 now cite POS.1100 instead of restating the split, and the
  light check's content is named once. The failure mode the finding
  predicted, however, occurred at the very next change: 3.44 changed
  what `/save` runs and updated POS.0570 and POS.1140 but not the
  owner, POS.1100 — see FND.0350.
- **FND.0310 — verified resolved.** POS.1120 says "decided when the
  `check` contract is built"; POS.1140 gives the variants their word
  ("check"); "kind of reviewer" and "kind of check" are qualified where
  they were bare. That the deferral's event has now passed is FND.0360.
- **FND.0320 — verified resolved.** THR.0330 is closed and gone;
  POS.1130 carries no live count of commands ("twenty-two files moved"
  is a record of the migration, not a rule).
- **FND.0330 — verified resolved.** POS.0840 explains the bundle index
  by its template only; POS.0420 says "contract" for the shared
  behaviour and "skeleton" for the template throughout.
- **FND.0340 — verified resolved.** POS.0840 owns the index; POS.0180
  keeps the ingest-side facts ("in the shape POS.0840 owns"); POS.0160
  says "the resource indexes are POS.0840's".

## Findings

### FND.0350 [high] [contradiction]
- **Location:** 10-intent.md POS.1100 vs POS.0570 and POS.1140; POS.0570
  internally; POS.1100 and POS.1110 ("full check")
- **Issue:** POS.1100 — since 3.42 the one owner of the save/release
  split — says "`/save` is commit and push on whatever branch is checked
  out … with no check and no render". POS.0570 says "`/save` runs the
  `light` check only (POS.1100, POS.1140)" and POS.1140 says "`/save`
  runs `light`". POS.0570 also contradicts itself: it opens "The
  conformance check belongs to the release, not to the save" and later
  gives the save a check. POS.1100 describes the release as "the full
  check with its walkthrough (POS.0570)" and POS.1110 as "its full
  check", while POS.1140 replaced the full check with a composition
  (`light` and `project`, for the engine `engine` too) and names no
  full check. The citations are circular: POS.1100 sends the reader to
  POS.0570 for the check, POS.0570 sends him to POS.1100 and POS.1140.
- **Why it matters:** POS.1100 is the position a reader consults to
  learn what `/save` does, and it states the opposite of the current
  rule. Three positions now say three different things about a step
  that runs at every save; the owner is the stale one.
- **Suggested fix:** Rewrite POS.1100's two-command sentence to the
  current shape ("`/save` runs the `light` check and then commits and
  pushes …; `/release` runs the checks POS.1140 composes for it") and
  replace "full check" in POS.1100 and POS.1110 with the composition or
  a citation of POS.1140. Reword POS.0570's opening sentence so it
  names what belongs to the release (the project check, its walkthrough
  and the renders) rather than "the conformance check" as a whole.

### FND.0360 [medium] [contradiction]
- **Location:** 10-intent.md POS.1120 ("`.claude/skills/<kind>/SKILL.md`
  (`critic`, `challenger`, `check`)"; "decided when the `check`
  contract is built") vs POS.1140 ("one contract skill `checker`") and
  POS.1130 (every command lives as `.claude/skills/<name>/SKILL.md`)
- **Issue:** POS.1120 names the check's contract skill `check`, under
  the rule that the skill's directory is the kind's name. POS.1140
  names it `checker`. Under POS.1130 the `/check` command itself
  occupies `.claude/skills/check/SKILL.md`, so the name POS.1120 gives
  the contract is the command's, and the naming rule "one skill per
  kind at `<kind>/`" no longer holds for check. In the same item
  POS.1120 defers the further shared skill (the few sentences common
  to every kind) to "when the `check` contract is built"; POS.1140
  records that contract as built on 2026-09-06 and records no decision
  on the further skill.
- **Why it matters:** A reader of POS.1120 who goes to build or
  extend the layer looks for a skill that does not exist and finds a
  command in its place; and a deferral whose event has passed without
  a recorded outcome reads as an unmet promise rather than a decision.
- **Suggested fix:** In POS.1120 name the check's contract `checker`
  and state the naming rule as it now is (the reviewer kinds at
  `<kind>/`, the check contract at `checker/` because `check/` is the
  command), or cite POS.1140 for the name. Replace "decided when the
  `check` contract is built" with what was decided — kept as three
  contracts, or a further skill deferred to a named event.

### FND.0370 [low] [ambiguity]
- **Location:** 10-intent.md POS.0310, POS.0820, POS.0840, POS.0920,
  POS.0940, POS.0960, POS.1000, POS.1010, POS.1020, POS.1040 ("`/check`
  …") vs POS.1140
- **Issue:** Ten positions attribute a rule to "`/check`" as one
  procedure — "`/check` verifies index against directory" (POS.0840),
  "`/check` compares the table with the directory" (POS.0920),
  "`/check` verifies that every registered path exists on disk"
  (POS.1020), "a `/check` finding" (POS.0310), "expected by `/check`"
  (POS.1000). Since POS.1140, `/check` bare shows a roster and runs
  nothing; the rule belongs to one of four checks, "each owning one
  concern and none another's". POS.1140's list lets a reader derive the
  owner for most (`light` for indexes, ledger and dependencies;
  `project` for recipes and the body table), but the derivation is the
  reader's, and the exclusive-ownership rule makes it matter.
- **Why it matters:** The agents are written against these positions;
  two builders may put the same rule into two checks, which POS.1140
  forbids, or into none.
- **Suggested fix:** One sentence in POS.1140: a rule an older position
  attributes to `/check` belongs to the check that owns its concern by
  the list above — or name the check in the three or four positions
  where the owner is not obvious (POS.0960's "not a repository" report,
  POS.0310's body table, POS.1040's binary-without-extract case).

### FND.0380 [low] [contradiction]
- **Location:** 10-intent.md POS.1130 ("The reviewers' contracts
  (POS.1120) are skills of the same directory, invocable by nobody")
  vs POS.1120 ("`user-invocable: false` … its description still enters
  that session's context; `disable-model-invocation` … is not used")
- **Issue:** POS.1120 says the contract skill is hidden from the user's
  `/` menu only, and deliberately not from the model, because the
  field that would hide it from the model would also forbid the
  preload. POS.1130 says the contracts are invocable by nobody.
- **Why it matters:** The two sentences describe the same front-matter;
  a reader of POS.1130 would set the field POS.1120 rejects, and break
  the preload.
- **Suggested fix:** In POS.1130 say "not user-invocable (POS.1120)" or
  drop the clause and cite the position.

### FND.0390 [low] [duplication]
- **Location:** 10-intent.md POS.0400 ("`/check engine` verifies that
  the skill every file names exists"), POS.0420 ("`/check engine`
  verifies that the skill it names exists (POS.1070)"), POS.1120 ("the
  engine check replaces the copy comparison with one check: every
  skill an agent names exists")
- **Issue:** The one rule — the engine check verifies that every skill
  an agent names exists — is written three times, in the kinds-of-review
  position, the challenger position and the contract-skill position.
- **Why it matters:** The document's own POS.1070 names the failure
  mode, and FND.0300 has just shown it in this document: at the next
  change to the rule (a further check, a different owner) one copy
  moves and two stay.
- **Suggested fix:** Let POS.1120 own the sentence (it explains why the
  check exists) and reduce POS.0400 and POS.0420 to a citation.

## Recommendations
<!-- Not findings, not gates: wording that is hard to test, groups that
overlap, items that could be split. The principal may ignore these
without recording anything. -->
- POS.1120 still lists check inside "each kind of reviewer" while
  POS.0540 leaves undecided whether it is called a review; "each kind
  of reviewer and, on the same mechanism, check" would keep the two
  aligned without deciding the word.
- POS.0540 and POS.1120 say "one agent per kind of check" while
  POS.1140 fixes the variants' word as "check" ("the light check, the
  project check"); "one agent per check" in both would use the word
  POS.1140 chose.
- THR.0210's proposed solution names "both contract skills (POS.1120)";
  three now exist. Whether the sentence belongs in the `checker`
  contract as well is the thread's to say when it is taken up.
- POS.1120 carries a growing trial and build log (what arrived in which
  prompt, line counts before and after, which findings were settled,
  what the next run should check). Noted on 2026-09-06 (first run);
  the position is the rule, the companion and ledger hold the record.
- Residues noted in earlier runs and left by the principal, still
  present: POS.0850 states the recommendation-first rule twice;
  POS.0830 ends "until then it is a writing rule, not a claim" with the
  Linux verification owned by nobody; THR.0200 cites "readme recipe
  0.24" (the recipe is at 0.39); POS.0110 "every brief to date" as of
  2026-08-27; POS.0950 "adopted at 3.6".

## Advisory checklist
<!-- Answer yes / no / delegated / n-a with one line each. -->
- Objective outcome-phrased and unambiguous? **yes** — the Essence and
  POS.0780 say what the forge is and where a run ends.
- Scope boundaries stated, with out-of-scope items where the topic
  invites creep? **yes** — POS.0780, THR.0140, the REJ list, the public
  boundary of POS.0980.
- Requirements written as shall / shall not, one idea each, no
  duplicates? **n-a** — no assignment by design; among the positions
  one rule is written three times (FND.0390).
- Constraints separated from requirements (no leaked solutioning)?
  **n-a** — no assignment; positions and threads are cleanly separated
  in 3.44, THR.0290 carrying only what is open.
- Deliverables actionable, with owners and timing where relevant?
  **n-a** — the handover artefacts are the core and README.
- Open questions each have an owner? **yes** — every THR sits with the
  principal and is mirrored in the ledger with its trigger or order;
  one deferral inside a position has outlived its event (FND.0360).
- Success criteria present, or explicitly delegated, or deliberately
  absent? **deliberately absent** — POS.0780; no SCR convention binds
  the intent layer.
- Detail of the assigning kind, not the solving kind? **n-a** — no
  assignment; the intent is the working document and may solve.
- Terms section present and matching what the document actually uses?
  **n-a** — the Terms rule binds assignments; the terms that carry two
  senses here are "`/check`" (the dispatcher and any of its checks,
  FND.0370) and "full check" (a shape POS.1140 retired, FND.0350).
- Any item that cannot be understood without an external link? **no**
  — external tools, plugins and hosts are named with their role in
  the text.
