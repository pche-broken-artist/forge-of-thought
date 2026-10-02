---
date: 2026-10-02
project: forge
lens: clarity
target: intent v4.49
reviewed: 10-intent.md v4.49 with 10-intent.threads.md (read whole);
  10-intent.history.md (searched by item ID, never loaded whole);
  decisions.md (DEC.0010–0180); ledger.md (updated 2026-10-02);
  reviews/2026-09-06-critique-clarity-3.md (FND.0400–0430,
  regression); the five check reports of 2026-10-02 (FND.0440–0820,
  a check's and not this lens's, read so that nothing of theirs is
  raised twice); the earlier critic reports of 2026-08-17 to
  2026-09-06, read for the locations and fixes of their findings,
  all verified in earlier runs; templates/intent.md and
  .claude/skills/forge/states/intent.md, for the sections the
  intent's own template requires. The briefs are outside the
  target and were not read.
reviewer: critic lens clarity (isolated context)
---

# Critique (clarity) — 2026-10-02

## Delta summary
- **New:** FND.0830, FND.0840, FND.0850, FND.0860, FND.0870, FND.0880
- **Verified resolved:** FND.0400, FND.0410, FND.0420, FND.0430
- **Still open:** none
- **Newly obsolete:** none
- **Respected:** FND.0090 (rejected, DEC.0090); POS.0550 now says
  "branches allowed and left to git", so the condition of the
  decision fell and nothing returns. FND.0450 and FND.0480 are a
  check's and rejected (DEC.0150, DEC.0160); nothing below asks for
  the sentences they keep to leave.

## Scope note
Target: the intent alone, with its threads file, read as the record
of current intent and with no memory of the other layers. The
front-matter agrees with itself and with the ledger: `version: 4.49`,
`status: draft`, a status word of the set POS.0300 gives. Since the
last run of this lens (3.47) the intent was cleaned whole (4.42), the
threads moved into a file of their own, and the Elicitation group
(POS.1300 to POS.1380) was added; four of the six findings sit where
that new material meets positions that were not rewritten with it.

## Regression
- **FND.0400: verified resolved.** POS.0120 now settles both
  readings: "Dated once means one date, the day the position took
  its present shape; earlier steps are found by searching the history
  for the position's ID", and "A number stays only where it is the
  rule or a threshold, never as a measurement." The positions the
  finding named carry one date each (POS.0130, POS.0310, POS.0570,
  POS.0930, POS.0980, POS.1100); POS.0950 keeps the two dates of its
  one reversal by DEC.0150. The measurements named have left
  (POS.0310, POS.1100). Whether every other position keeps to the
  rule is the `history` check's concern, not this lens's; see
  Recommendations.
- **FND.0410: verified resolved.** The clause "the intent measured
  against this rule once, before 4.0, THR.0240" is gone from
  POS.0120, and no citation of THR.0240 for a sweep of the intent
  remains.
- **FND.0420: verified resolved.** POS.0570 names the owner: "which
  checks run where is POS.1140's". The half-sentence before it, "the
  bookkeeping check to the save", still restates the composition and
  still reads as if `light` ran at a save only; with the owner named
  it is a residue, noted under Recommendations.
- **FND.0430: verified resolved.** THR.0240 dates the clause: "(then
  still carrying the git identities, since moved out, POS.0950)".

## Findings

### FND.0830 [medium] [contradiction]
- **Location:** 10-intent.md POS.0120 ("the definitions of the
  elicitation stay whole until their state files have been rewritten
  and tried (POS.1380), and then the intent keeps their assignment
  and aim") against POS.1380 ("The definitions are not tried before
  they are used: they live in the state files of `/forge`, are used
  on real work at once and mended there as the work shows") and
  POS.1330, POS.1340, POS.1350 ("The seven blocks are
  `.claude/skills/forge/states/…`")
- **Issue:** POS.0120 makes a trial the condition under which the
  definitions leave the intent, and cites POS.1380 for it; POS.1380
  says there is no trial. The clause is also overtaken: POS.1330 to
  POS.1350 already keep only what each definition is to achieve and
  name the state file, so the state "stay whole until" describes is
  past. POS.1380 has a smaller case of the same kind: "The engine is
  released once that move is done" follows a sentence that reports
  the move as done, so a reader cannot tell whether a release is
  still awaited.
- **Why it matters:** POS.0120 is the rule every item is measured by,
  the one the `history` check reads. A reader following it expects
  the three definitions in full in the intent and a trial still to
  come; the citation he follows says the opposite. The ledger
  already holds the contradiction as a line of free text under
  Waiting on principal, with no ID.
- **Suggested fix:** In POS.0120 cut the example down to the rule it
  illustrates ("Until the file exists, the item keeps the full
  information too") or reword it to the present state (the
  definitions live in their state files, POS.1330 to POS.1350 keep
  their aim), without the word "tried". In POS.1380 say the release
  in the tense that holds.

### FND.0840 [medium] [contradiction]
- **Location:** 10-intent.md POS.0930 ("Every command, chain state
  and reviewer runs on the session model"; "The one exception is
  `scripts/md2pptx.ps1`: a headless run has no session model")
  against POS.1150 ("`-Engine claude` makes the designed document
  through headless Claude Code and the official docx skill … and is
  the engine of `/publish`") and POS.0590 ("`/publish` makes the
  designed file through a model and its document skills"); and
  POS.0740 ("The conversion is done by a model, never by a
  deterministic converter") and POS.1150 ("a deterministic
  conversion, unlike `md2pptx` (POS.0740)") against their own
  closing sentences on two engines
- **Issue:** Three positions state the shape before `/publish` as
  absolute and are amended by a later sentence instead of rewritten.
  (1) POS.0930 names one exception to the session model; by POS.1150
  a second script makes a headless model run, and by POS.0590 a
  command, `/publish`, runs through such a model for both formats.
  The intent does not say which model the headless Word run uses.
  (2) POS.0740 opens with "never by a deterministic converter" and
  closes with `-Engine pandoc`, which POS.0590 calls "deterministic,
  cheap"; POS.1150 opens by contrasting itself with `md2pptx` as the
  deterministic one and closes with a model engine of its own. The
  phrase "the default and all of the above" is what keeps each item
  from contradicting itself, and the reader has to apply it
  backwards. (3) POS.0930 says "A per-recipe `model:` is deferred"
  while POS.0740 says "a presentation recipe may recommend one in
  its Format section"; the two are about different steps, and
  neither says so.
- **Why it matters:** POS.0930 is the position a reader opens to
  learn what runs on which model; it answers "the session model,
  one exception" where the document elsewhere describes two headless
  runs behind a command. A reader of the first half of POS.0740 or
  POS.1150 acts on a rule the second half withdraws.
- **Suggested fix:** Rewrite POS.0740 and POS.1150 in their present
  shape (two engines each, which is the default, which command uses
  which, and the reason each engine exists), the superseded
  absolutes going to the history with `Was`. In POS.0930 state the
  exception as the headless conversions behind `/publish` and cite
  both positions; say in one clause that the deferred per-recipe
  `model:` is the render's, not the Format section's line.

### FND.0850 [medium] [contradiction]
- **Location:** 10-intent.md POS.0940 ("That is the whole migration
  path of any instance …: after `forge-pull`, `/check project` on
  each project says what the conventions changed") against POS.0310
  ("its checks: `.claude/agents/check-light.md` and
  `.claude/agents/check-history.md`"; "A Version History table … is
  a `/check` finding settled by that move; that is how a project
  migrates"), POS.0440 ("a project's ledger is converted through a
  finding of the `light` check") and POS.1140 ("`light` —
  front-matter against the companion and the form of its log, the
  ledger against the files"; "each owning one concern and none
  another's")
- **Issue:** POS.0940 names one check, `project`, as the whole
  migration path. The two migrations the intent itself describes,
  the history table moved to the archive and the retired state word
  in a ledger, are findings of `light` by POS.0310, POS.0440 and
  POS.1140, and a check owns no other's concern. The sentence of
  POS.1140 that reassigns a rule "an older position attributes to
  `/check` as one procedure" does not reach POS.0940, which names
  the check.
- **Why it matters:** POS.0940 is the instruction for every other
  instance after an upgrade. A user who does what it says runs
  `/check project` and is told nothing of the migration this very
  version carries.
- **Suggested fix:** In POS.0940 name no check: "the checks say what
  the conventions changed (which check owns what: POS.1140)", or
  name the two a release composes, citing POS.1140 as the owner.

### FND.0860 [low] [ambiguity]
- **Location:** 10-intent.md POS.1080 ("Every versioned kind keeps
  its Version History in an append-only companion
  `<file>.history.md` (POS.0310)") and POS.0710 ("a recipe keeps its
  Version History in the companion like every versioned kind
  (POS.0310)") against POS.0310 ("The history is a log"; "A Version
  History table, in the body of a document or in its companion, is a
  `/check` finding")
- **Issue:** The capitalised term names two things. In POS.1080 and
  POS.0710 it is what every versioned document keeps; in POS.0310,
  the owner both cite, it is the retired table whose presence is a
  finding, and the thing kept is called "its history", a log.
- **Why it matters:** A reader of POS.1080, which calls itself "the
  one page from which all of this is read", takes the companion to
  hold a Version History and meets, in the cited owner, that a
  Version History in the companion is a defect.
- **Suggested fix:** Write "its history" in POS.1080 and POS.0710,
  leaving "Version History table" to POS.0310 as the name of the
  older form.

### FND.0870 [low] [duplication]
- **Location:** 10-intent.md POS.1330, POS.1340, POS.1350 against
  POS.0110, POS.0120, POS.0130, POS.0140, POS.0210 and REJ.0220
- **Issue:** The three positions that keep what each definition is
  to achieve restate what the older positions on the same artefacts
  hold, and neither side names the other as owner. "rough on
  purpose, the chiselling being the intent's" (POS.1330) and "A
  brief is rough on purpose, neither perfect nor detailed: the
  chiselling is the intent's" (POS.0110). "It is his by his
  approval, whoever first said a thought" (POS.1330), "what is in it
  the principal approved, whoever first said it" (POS.0110) and
  "what is in the brief the principal approved, whoever first said
  it" (REJ.0220). "carries the in-scope substance of the intent to
  the recipients, complete and precise … delegated or open on
  purpose is complete, silent is not" (POS.1350) and "carries the
  whole in-scope substance of the intent … a silent omission is a
  defect; leaving a matter out is legitimate only as an explicit
  delegation" (POS.0130). "a substance change goes to the intent
  first" (POS.1350, POS.0140, and POS.0900, which cites POS.0140).
  "every position with its provenance" (POS.1340) and "names what it
  comes from, a brief or a source" (POS.0120).
- **Why it matters:** POS.1340 gives "nothing twice" as a mark of a
  complete intent. POS.0110 and POS.1330 both carry "Present shape
  2026-10-02", so the next change to what a brief is must be made in
  two items and a rejection; the copy that is missed keeps the old
  rule, the pattern of FND.0300, FND.0350 and FND.0420.
- **Suggested fix:** One owner per sentence. Either POS.1330 to
  POS.1350 keep the aim of the elicitation alone (what the finding
  is to reach, Claude's part, the course in a clause) and cite
  POS.0110, POS.0120 and POS.0130 for what the artefact is; or the
  older positions cite the newer. REJ.0220 keeps the direction
  dropped and its reason and cites POS.0110 for what stands.

### FND.0880 [low] [gap]
- **Location:** 10-intent.md, section structure (Essence, Positions,
  Rejected directions, Candidate structure for assignment) against
  the section "Facts" its template carries; POS.0230, POS.1340,
  POS.1120
- **Issue:** The intent has no Facts section and no FCT item, and
  gives no reason, where its last section does give one ("Not
  applicable: this project's handover artefacts are the core
  itself"). The document itself says an intent holds "positions,
  facts, threads and rejections" (POS.1340) and that "Without a
  prefix of its own, a fact would have passed for a position"
  (POS.0230), and then carries what it calls facts inside positions:
  "Facts of the mechanism: the skill arrives at the end of the first
  user message, after the task, not in the system prompt; a headless
  `--agent` run preloads nothing" (POS.1120); "Grounds: in Claude
  Code custom commands have been merged into skills" (POS.1130).
  The "no retrofit" of POS.0230 is said of the origin of threads,
  not of facts.
- **Why it matters:** A reader cannot tell whether the absence is
  deliberate (the facts of this project stay with the positions they
  ground) or the retrofit simply never happened; and the one project
  that defines the FCT prefix shows it nowhere in use.
- **Suggested fix:** A document fix either way, the choice the
  principal's: a Facts heading with one line saying why it is empty,
  as Candidate structure has; or the passages the document itself
  labels facts moved under FCT IDs, their positions citing them.

## Recommendations
<!-- Not findings, not gates: wording that is hard to test, groups that
overlap, items that could be split. The principal may ignore these
without recording anything. -->
- "Reviewer": POS.0400 says `/release` "runs no reviewer on its own"
  while POS.1140 gives as its reason "one mechanism for every
  reviewer" and POS.1120 counts check among the kinds; POS.0540
  leaves the word undecided on purpose. Noted in the last run as a
  residue; the reason added to POS.1140 since then uses the word as
  decided. Writing "neither the critic nor the challenger" in
  POS.0400 would remove the clash without deciding the word.
- POS.0600 opens "thoughts are the raw material … and forged
  assignments are the product"; POS.0620 forbids any one-line
  description to "name the assignment as the goal", and POS.0780 has
  a run end at "an artefact the principal stands behind". The naming
  position describes the forge in the way the next position but one
  rules out.
- POS.0850 gives five verdict words ("`accept`, `modify` …,
  `reject`, `park` and `obsolete`") and a verdict line of four
  letters; how `obsolete` is given is not said in the item.
- "Publish" carries three senses: what the principal alone decides
  (POS.0430), the making of a designed file that "sends nothing
  anywhere" (POS.0590, which claims agreement with POS.0430), and
  making the engine public (POS.0980, POS.0760, POS.0970).
- POS.0570: "the bookkeeping check to the save" could go, the owner
  being cited in the same sentence; "The full check left the save"
  uses a name no check in POS.1140 carries.
- POS.0310 says the front-matter of "the document" carries "version,
  date, status" under a rule stated "without exception … the recipe
  alike"; POS.0710 gives a recipe "an updated date" and "no status
  field". One clause in POS.0310 would carry the exception.
- POS.0710 says `/render` "regenerates the output mechanically";
  POS.0810 opens "Regeneration is stochastic". The first means
  "without composition by the principal"; the word invites the other
  reading.
- POS.1080's table has no place for `10-intent.threads.md`: POS.0120
  calls it "part of the intent as the history is", yet the history
  is a kind of its own and the intent's row says "Versioned: yes"
  where the threads have "no version". A clause under the table, as
  the one on binaries, would settle it.
- Threads. THR.0470 is settled but for one question (whether large
  files are split), and carries the finished nine-step plan and its
  course; by POS.0120 a settled thread leaves the file, so closing
  it and opening the one question on its own would let the file say
  what is being worked. THR.0350 still lists "the sweep of this
  project's ledger" as to do. THR.0290 is headed "Research on the
  reviewer mechanism" over a body on `/research`; THR.0200 cites
  "readme recipe 0.24"; THR.0210 names "both contract skills" where
  three exist. The last three stand from earlier runs.
- POS.0300 asks "both critic lenses" before a major's tag; the
  ledger records the principal's word that `essence` is not run on
  this project. The ledger is not this lens's target; noted so that
  the position and the word are read together.
- POS.0990 to POS.1060 (the public face, the README of a project,
  the logo, dependencies, memory, the form of a source, `/setup`,
  `/import-project`) stand under "Growth path"; items may move
  between groups without a change of ID (POS.0220). From the last
  run.
- Several positions carry more than one date (POS.0190, POS.1090,
  and the "Since 2026-09-27" amendments of FND.0840) against "dated
  once" in POS.0120. Whether a text belongs in the item or its
  history is the `history` check's; named here only because the rule
  was this lens's FND.0400.

## Advisory checklist
<!-- Answer yes / no / delegated / n-a with one line each. -->
- Objective outcome-phrased and unambiguous? **yes**: the Essence and
  POS.0780 say what the forge is and where a run ends; POS.0600's
  first sentence pulls the other way (Recommendations).
- Scope boundaries stated, with out-of-scope items where the topic
  invites creep? **yes**: POS.0780, THR.0140, the REJ list, the
  public boundary of POS.0980.
- Requirement style of the assignment's definition kept throughout?
  **n-a**: no assignment by design (`terminal: intent`); the style
  binds assignments.
- Constraints separated from requirements (no leaked solutioning)?
  **n-a**: no assignment; the intent's own rule for detail is
  POS.0120, contradicted in one clause (FND.0830).
- Deliverables actionable, with owners and timing where relevant?
  **n-a**: the handover artefacts are the core and the README, as
  the last section says.
- Open questions each have an owner? **yes**: every thread sits with
  the principal and Claude's parts are marked as his; one known
  contradiction lived in the ledger as free text without an ID
  (FND.0830).
- Success criteria present, or explicitly delegated, or deliberately
  absent? **deliberately absent**: POS.0780; what a major must pass
  is POS.0300.
- Detail of the assigning kind, not the solving kind? **n-a**: the
  intent is the working document and may solve; where older detail
  was amended instead of rewritten it now contradicts itself
  (FND.0840).
- Terms section present and matching what the document actually
  uses? **n-a**: the Terms rule binds assignments; the terms used in
  two senses here are "Version History" (FND.0860), "reviewer" and
  "publish" (Recommendations).
