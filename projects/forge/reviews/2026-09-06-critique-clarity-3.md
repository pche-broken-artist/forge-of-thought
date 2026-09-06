---
date: 2026-09-06
project: forge
lens: clarity
target: intent v3.47
reviewed: 10-intent.md v3.47; 10-intent.history.md (rows 3.44–3.47,
  for last_change and version agreement); decisions.md (DEC.0010–0100);
  ledger.md (updated 2026-09-06); reviews/2026-09-06-critique-clarity-2.md
  (FND.0350–0390, regression); reviews/2026-09-06-critique-clarity.md
  (FND.0290–0340, verified in the second run of the day and not
  re-tested). reviews/2026-09-05-critique-harness.md carries a lens
  suffix of its own and is not this lens's; the retired single-critic
  reports (2026-08-17, 2026-08-27) were verified on 2026-09-03.
reviewer: critic lens clarity (isolated context)
---

# Critique (clarity) — 2026-09-06 (third run)

## Delta summary
- **New:** FND.0400, FND.0410, FND.0420, FND.0430
- **Verified resolved:** FND.0350, FND.0360, FND.0370, FND.0380,
  FND.0390
- **Still open:** —
- **Newly obsolete:** —
- **Respected:** FND.0090 (overruled, DEC.0090); nothing in 3.47
  touches its condition.

## Scope note
Target: the intent alone, read as the record of current intent. The
ledger, the decisions and the history companion were read for
regression and for the front-matter test only. The front-matter agrees
with the companion: `version: 3.47`, `status: draft`, and `last_change`
summarises row 3.47. Version 3.47 is the sweep of the positions by the
rule of POS.0120; this run therefore reads every position against that
rule as the document now states it, which is where two of the four
findings come from.

## Regression
- **FND.0350 — verified resolved.** POS.1100 owns the current shape:
  "`/save` runs the `light` check (POS.1140) and then commits and
  pushes …; `/release` … the checks POS.1140 composes, with their
  walkthrough (POS.0570)". "Full check" is gone from POS.1100 and
  POS.1110 ("its checks find what two branches broke"). POS.0570 opens
  by naming what belongs to the release and what to the save — but its
  wording of the save's half is FND.0420.
- **FND.0360 — verified resolved.** POS.1120 names the check's contract
  `check-contract` with its reason ("the suffix because `check/` is the
  command, POS.1130") and records the deferred skill's outcome: "three
  contracts and no common skill, reopened only if a fourth kind repeats
  them".
- **FND.0370 — verified resolved.** POS.1140: "A rule an older position
  attributes to `/check` as one procedure belongs to the check that
  owns its concern by this list — bookkeeping, ledger, dependencies and
  indexes to `light`, structure, recipes and renders to `project` —
  never to two."
- **FND.0380 — verified resolved.** POS.1130: "The reviewers' contracts
  (POS.1120) are skills of the same directory, not user-invocable."
- **FND.0390 — verified resolved.** POS.1120 owns the sentence ("the
  engine check verifies that every skill an agent names exists");
  POS.0400 and POS.0420 carry a citation only.

## Findings

### FND.0400 [medium] [ambiguity]
- **Location:** 10-intent.md POS.0120 (the position rule: "a stance
  with its reason and its citations, dated once. How it was reached —
  trials, measurements, counts, findings settled, what others do — is
  the history row's, the ledger's or a research note's, never the
  position's") against POS.0130, POS.0310, POS.0570, POS.0930,
  POS.0950, POS.0980, POS.1100
- **Issue:** The rule the sweep of 3.47 was made by admits two readings
  on each of its two clauses, and the swept positions show both. (1)
  "Dated once": POS.0570 closes with four decision dates and four
  history pointers ("decided 2026-09-05 (history 3.33) … the same day
  (history 3.30) … 2026-09-06 (history 3.44) … 2026-09-04 (history
  3.23)"), POS.0950 with three, POS.0310 with two, POS.0130 with two
  ("dropped 2026-08-08 and 2026-08-15, history 1.12 and 1.15"),
  POS.0930 with two — all but POS.0130 named in row 3.47 as "cut …
  dated once". Under the reading "one date per position" they were not
  cut; under "one date per decision the position records" they were.
  (2) "Measurements … never the position's": POS.0310 keeps "a history
  that had grown to 40 % of this intent", POS.1100 "over a hundred
  thousand tokens at every save", POS.0930 the trial in which "a
  smaller model loosened pinned wording, dropped prescribed elements
  and leaned on the previous render", POS.0980 the execution
  ("rewritten … including its immutable documents … the brief was
  rewritten into English … Separating … without publishing would have
  been a fallback only if … it was not"). Each of these is the reason
  of the stance, which the rule admits, and a measurement or trial,
  which the rule sends to the records. The rule does not say which
  wins.
- **Why it matters:** POS.0120 is now the yardstick of every position
  written from here and of the sweep that precedes 4.0; two sweepers
  reading it as it stands would cut different things, and the next
  round either cuts what 3.47 kept or keeps what it cut.
- **Suggested fix:** One clause in POS.0120 settling each reading —
  for instance "dated once per decision it records" (or "once, with
  later decisions dated in the history rows it cites"), and "a
  measurement or trial stays where it is the reason of the stance, in
  one clause; its course and its figures are the record's". Then let
  the seven positions above stand or fall by the clause as written,
  in one pass.

### FND.0410 [medium] [contradiction]
- **Location:** 10-intent.md POS.0120 ("the intent measured against
  this rule once, before 4.0, THR.0240") vs the front-matter
  `last_change` ("the intent swept by the position rule of POS.0120
  (CHL.0180) — every position read, nineteen cut …") and THR.0240
- **Issue:** POS.0120 states the sweep of the intent as a future event
  and cites THR.0240 as its home. The same version's `last_change` and
  history row record the sweep as done. THR.0240 is the size of
  CLAUDE.md and carries nothing about a sweep of the intent — a reader
  following the citation finds nothing to follow.
- **Why it matters:** A reader of POS.0120 in 3.47 expects a sweep
  still to come and looks for it in a thread that does not hold it;
  the one position that states the rule for positions carries a
  pending action that is not pending.
- **Suggested fix:** In POS.0120 replace the clause with the fact
  ("the intent swept by this rule at 3.47, before 4.0") or drop it —
  the history row and the ledger hold the record; remove the citation
  of THR.0240, or move the residue that is genuinely open (CLAUDE.md's
  own sweep, if that was meant) into THR.0240 in words.

### FND.0420 [low] [ambiguity]
- **Location:** 10-intent.md POS.0570 ("The project's full conformance
  — the `project` check, for the engine `engine` too — and the renders
  belong to the release, the `light` check to the save") vs POS.1140
  ("`/save` runs `light`; `/release` runs `light` and `project`, for
  the engine `engine` too")
- **Issue:** POS.0570 assigns the `light` check to the save alone;
  POS.1140, the owner of the composition, gives it to both. A reader
  building `/release` from POS.0570 runs `project` (and `engine`) and
  no `light`; one building from POS.1140 runs all three. POS.0570 is
  the position that went stale at 3.44 (FND.0350) and is drifting from
  the owner again, one version after the fix.
- **Why it matters:** The same step, two answers, at every release; and
  the pattern FND.0300 and FND.0350 named — the copy without the owner
  loses the rule — is repeating in the same item.
- **Suggested fix:** Reduce POS.0570's opening to what it owns — that
  the checks and the renders belong to the release and the release
  comes after the walkthrough — and cite POS.1140 for which checks run
  where, without restating them.

### FND.0430 [low] [contradiction]
- **Location:** 10-intent.md THR.0240 ("the instance facts of
  `CLAUDE.local.md` (principal, language, git identities) thereby
  reach an isolated reviewer that needs none of them") vs POS.0950
  ("the git identities — names, e-mail addresses, hosts — live beside
  it in `identities.local.md`, gitignored, loaded by nobody")
- **Issue:** THR.0240 describes, in the present tense, `CLAUDE.local.md`
  as carrying the git identities into every reviewer's context.
  POS.0950 (3.46) moved them out of that file precisely so that they
  reach no reviewer. Row 3.47 left the threads untouched "since a
  thread carries the state of its discussion" — but this clause is a
  fact the document has since overtaken, not a state of discussion,
  and the same row records the identical stale clause being trimmed
  from POS.1030.
- **Why it matters:** THR.0240 is the thread a reader opens to learn
  what reaches a reviewer; it tells him the leak POS.0950 closed is
  still open.
- **Suggested fix:** Date the clause ("principal, language and — until
  3.46 — the git identities") or cite POS.0950 in it; the measurement
  itself (about 600 lines, once per reviewer run) stays as the
  thread's evidence.

## Recommendations
<!-- Not findings, not gates: wording that is hard to test, groups that
overlap, items that could be split. The principal may ignore these
without recording anything. -->
- POS.1050 fills `identities.local.md` "from its template" without
  naming it, where POS.0950 names `templates/CLAUDE.local.md` for the
  other file; a builder of `/setup` has to guess the path.
- POS.1030–POS.1060 (memory, the form of a source, `/setup`,
  `/import-project`) sit under "### Growth path", separated from the
  group by a blank line, though each is an operating-environment rule;
  items may move between groups without ID change (POS.0220).
- POS.0160 still restates part of the POS.1080 table (append-only,
  freely rewritten, immutable) for five kinds; a citation of POS.1080
  would carry it.
- POS.0180 and POS.1040 both state that the `doc2md` extract
  `sources/<slug>.md` is the source; POS.1040 owns the form, POS.0180
  could cite it.
- POS.0300 requires "both critic lenses and one challenge" before a
  major's tag; the ledger's road to 4.0 lists the checks and `essence`
  only. The ledger is not this lens's target — noted so the plan and
  the position are read together.
- THR.0290 is headed "Research on the reviewer mechanism" while its
  body is what `/research` gains from kinds; the heading is the
  thread's original scope, half of which closed at 3.44.
- Residues noted in earlier runs and left by the principal, still
  present: POS.0540 "one agent per kind of check" against POS.1140's
  word "check"; POS.1120 lists check among "each kind" of reviewer
  while POS.0540 leaves the word undecided; THR.0210 names "both
  contract skills" where three exist; POS.0850 says twice that a table
  or questionnaire of verdicts "is never put in front of the
  principal"; POS.0830's Linux verification is owned by nobody;
  THR.0200 cites "readme recipe 0.24".

## Advisory checklist
<!-- Answer yes / no / delegated / n-a with one line each. -->
- Objective outcome-phrased and unambiguous? **yes** — the Essence and
  POS.0780 say what the forge is and where a run ends.
- Scope boundaries stated, with out-of-scope items where the topic
  invites creep? **yes** — POS.0780, THR.0140, the REJ list, the public
  boundary of POS.0980.
- Requirements written as shall / shall not, one idea each, no
  duplicates? **n-a** — no assignment by design; among the positions
  the check composition is written in two places that now differ
  (FND.0420).
- Constraints separated from requirements (no leaked solutioning)?
  **n-a** — no assignment; positions and threads are separated, and
  3.47 moved the story of the positions to the records — the rule it
  did that by is the ambiguity of FND.0400.
- Deliverables actionable, with owners and timing where relevant?
  **n-a** — the handover artefacts are the core and README.
- Open questions each have an owner? **yes** — every THR sits with the
  principal and is mirrored in the ledger with its trigger or order;
  one action inside a position points at a thread that does not hold
  it (FND.0410).
- Success criteria present, or explicitly delegated, or deliberately
  absent? **deliberately absent** — POS.0780; no SCR convention binds
  the intent layer. What a major must pass is now stated (POS.0300).
- Detail of the assigning kind, not the solving kind? **n-a** — no
  assignment; the intent is the working document and may solve.
- Terms section present and matching what the document actually uses?
  **n-a** — the Terms rule binds assignments; the term that carries
  two readings here is "dated once" (FND.0400).
- Any item that cannot be understood without an external link? **no**
  — external tools, plugins and hosts are named with their role in
  the text.
