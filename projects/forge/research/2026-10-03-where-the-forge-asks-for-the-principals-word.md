---
project: forge
type: research
topic: where the forge asks for the principal's word - every consent point of the definitions, what each came from, what each protects, and how many answers a save, a release and a check run cost
date: 2026-10-03
derived_from: the engine's own definitions as they stood on 2026-10-03 after commit 1d8d4d2 (CLAUDE.md; .claude/skills/*/SKILL.md with the state files; .claude/settings.json; scripts/hook-walkthrough.ps1); 10-intent.md v4.50 with 10-intent.threads.md and decisions.md; searches of 10-intent.history.md, 10-intent.history.archive.md and sources/forge-run-record-health.md; ledger.md (Findings, Challenges); the draft 00-brief-next-gen.md v0.1, section Automation
status: immutable
---

# Where the forge asks for the principal's word

## Question

Where does the forge ask for the principal's word, and what did each
such point come from? The draft brief `00-brief-next-gen.md` says
under Automation that the forge is built on the owner's word, that in
places this is a needless burden (typically checks and releases), and
that it is to be found where the word protects something and where it
is only ceremony. This note catalogues the consent points, traces the
origin of each, classifies what each protects, and counts the answers
two real flows cost. It designs no agent.

## How it was read

No web source: the subject is the engine, and its definitions and its
own record are the primary source.

- Read in full: CLAUDE.md; every command skill, the walkthrough skill,
  the three reviewer contracts and the three state files of `/forge`;
  `.claude/settings.json`; `scripts/hook-walkthrough.ps1`;
  `10-intent.md` v4.50; `decisions.md`;
  `sources/forge-run-record-health.md`; the research note
  `2026-09-14-save-and-release-duration.md`.
- Read in part: `10-intent.threads.md` (THR.0290, THR.0350, THR.0400,
  THR.0410, THR.0430, THR.0490, THR.0500); the ledger's Findings,
  Challenges and Waiting on principal.
- Searched, never loaded whole: `10-intent.history.md` and
  `10-intent.history.archive.md`, for the IDs and the phrases named
  in the table below.
- Not read: the conversation transcripts, the assistant's private
  memory, and the permission prompts of the harness itself, which
  depend on the permission mode of a session and stand in no
  definition.

Epistemic status. A statement that cites a file with a line, or an
ID, is verified at that place. "History" means
`10-intent.history.md` by line; "archive" means
`10-intent.history.archive.md` by the version of its row. A statement
marked *(hypothesis)* is this note's own reading. "No recorded
origin" means the searches named above found none; it does not mean
none exists.

A consent point is counted wherever a definition makes an operation
wait for the principal: he must type the command, confirm a proposal,
give a verdict, or say a word such as `write`.

## Key findings

### The catalogue

Classes of what a point protects: **I** irreversibility or outward
effect; **A** the principal's authorship of substance; **C** cost
(tokens, minutes); **B** bookkeeping only. A point may carry two; the
first named is the stronger.

Cross-cutting rules

| # | What waits for his word | Stated in | Origin | Class |
|---|---|---|---|---|
| C.01 | A new convention, prefix or section: proposed, decided, then written | CLAUDE.md:42 (prime directive 2); POS.0030 (intent:66) | Stated from the start; no record of a change of POS.0030 in the history or the archive. One recorded breach: a ledger section added unilaterally (run record, F.06) | A |
| C.02 | The write of a round: the word `write`, then the round reflected back, then his yes | CLAUDE.md:71 (prime directive 9), :138, :140; walkthrough skill:77-93; POS.0190 (intent:592), POS.0890, POS.1210 | The principal's request at 0.11, 2026-08-02 (archive, row 0.11); reason in POS.0190: a write after every exchange buries the change under churn. Sharpened by two recorded failures: "written" said of what lived only in the conversation (run record, F.01, P.01) and one conversation giving every correction a version (history:38, intent 4.21 to 4.25). The word `write` with reflection and yes: his of 2026-09-27 (POS.1210) | A, B |
| C.03 | Any action hard to reverse (a write, a commit, a push, a rename): one step, the exact operation, its target and reason; a seen plan is not consent | CLAUDE.md:118-125 (Step by step) | Moved at 3.3, 2026-08-30, from the assistant's private memory into the engine by POS.1030 (archive, row 3.3). The failure behind the memory note is not recorded | I, A |
| C.04 | The birth of a versioned document (a brief, a recipe, a layer) | CLAUDE.md:123-125; POS.1090 (intent:1417-1421) | Recorded failure: a second recipe and its render created without a word, and a brief version written under another command (run record, F.06, P.05, G.07) | A, I |
| C.05 | A verdict on every item of a list: one item per message, `accept / modify / reject / park` | CLAUDE.md:99-112; walkthrough skill:13-68; POS.0850 (intent:110); hook line 25 | Recorded failure: the one-item rule broken about thirteen times (run record, F.02); the failure the principal minds most (THR.0350, threads:415-418). The failure was Claude bundling items and moving on before an item was agreed, not the principal being asked too seldom *(hypothesis on what the record shows)* | A for challenges and critique findings; B for conformance findings |
| C.06 | A command of Claude's own beyond plain reading: explained first, run on his yes; nothing written, run or changed that was not agreed; a yes covers what was asked, never its consequences | hook lines 27-29; THR.0400 (threads:529-539) | Recorded failure of 2026-09-20: git state read past the scripts twice, and on a bare yes to one change its consequences written as well, in an automatic permission mode (THR.0400; archive, row of 2026-09-20) | I, A |
| C.07 | Raw `git` and two sensitive paths denied to Claude; no attribution trailer on a commit | settings.json:2-12; POS.1200 (intent:1084) | The same failure of 2026-09-20, decided 2026-09-21; the trailers: commit 1fe1dae had carried both unseen (history:56). A wall, not a question: it asks nothing | I |
| C.08 | Nine commands only the principal can start: `/save`, `/release`, `/spinoff`, `/setup`, `/new-project`, `/import-project`, `/ingest`, `/render`, `/publish` | `disable-model-invocation: true` in each skill's front-matter; POS.1090 (intent:1402) | A reviewer's finding: FND.0210, high, of the harness critique (`reviews/2026-09-05-critique-harness.md`:97-115), settled at 3.30 (archive, row 3.30) | I, C |
| C.09 | Substance: nothing enters content because Claude proposed it; a thread closes only on his word; a source's content enters the intent only by his explicit act | CLAUDE.md:113-117, :253; intent state file:42; POS.0070, POS.0180 | A principle of the collaboration model (POS.0010, POS.0070). Reinforced by a recorded failure: Claude's constructions presented as facts, about fourteen times (run record, F.04) | A |

The chain

| # | What waits for his word | Stated in | Origin | Class |
|---|---|---|---|---|
| C.10 | The lock of a brief | brief state file:39-41, :130; CLAUDE.md:206 onward; POS.0110 | A principle: immutability runs from the lock (POS.0110, POS.0320). No recorded failure | I, A |
| C.11 | The approval of a version and the move to the next state: a recommendation, never a gate | intent state file:82-84; assignment state file:78-79; POS.0300 | A principle (POS.0430, REJ.0030). The test of a major of the forge intent came from a challenge, CHL.0190 accepted (archive, row 3.46) | A, I |
| C.12 | The assignment's joint pass: questions up front, then one verdict per group | assignment state file:81-108; POS.1350 | The brief `elicitation`, 2026-09-28. Already batched on purpose: "most items are craft derived from the intent and a verdict on each is ceremony" (POS.1350, intent:315-316) | A |
| C.13 | A research step: proposed against a named need, run on his word | brief state file:106-116; intent state file:64-65 | The definitions of 2026-09-28 (POS.1330, POS.1340). No recorded failure in the documents read | C |
| C.14 | A run of a reviewer (critic, challenger, check): by hand only, never on Claude's judgement | CLAUDE.md:544; critique skill:20-22; check skill:22-23; intent state file:67-69; POS.0400 | "Both invoked by hand" since 3.16, 2026-09-03 (archive, row 3.16); "no reviewer runs on its own" at a release since 3.33 (archive, row 3.33). No recorded failure. The cost is measured: a check 131 to 405 seconds (THR.0410, threads:602-606) | C |
| C.15 | A new persona, lens or check | CLAUDE.md:554-555; POS.0420 | A principle: personas that say the same in other words are noise (POS.0420). No recorded failure | A |

Resources

| # | What waits for his word | Stated in | Origin | Class |
|---|---|---|---|---|
| C.16 | Personal matter stops `/ingest` before storing: store, redact or drop | ingest skill:27-32; POS.1040 | Recorded failure: an identifying detail stored before asking (run record, E.04, F.06, G.09) | I |
| C.17 | For every binary, one question: convert to Markdown? | ingest skill:54-71; POS.1040 | Decided at 3.4, 2026-08-30, for the weight of the repository (archive, row 3.4). No recorded failure | B *(hypothesis: the answer follows from the kind of file in most cases)* |
| C.18 | The role of a source: "what is it for?", never inferred unasked | ingest skill:72-79; POS.1040 | Recorded failure: Claude's readings written into the source index needed two corrections (run record, F.03), with the principal's addition that the role is always asked (THR.0350, threads:440-441) | A |
| C.19 | A source changed since registration: what to do with it | ingest skill:15-25; POS.0180 | A principle (immutability); confirmed by DEC.0170 | I |

Rendering

| # | What waits for his word | Stated in | Origin | Class |
|---|---|---|---|---|
| C.20 | A render: only on `/render` or by `/release` | render skill:8-10; POS.0810 (intent:678) | A challenge: CHL.0040, major, accepted at 2.8 (ledger, Challenges; archive, row 2.8); "never on Claude's own judgement" added at 3.4 (archive, row 3.4). Cost measured: 191 to 342 seconds (THR.0410) | C, I |
| C.21 | The delta of the regenerated README and release notes, ruled on before the release commit | release skill:47-50; POS.0810 | The same challenge, CHL.0040: outward-facing documents regenerated by a process that never gives the same words twice | I |
| C.22 | A published file: only on `/publish`; a stale render named and the word is his | publish skill:8-12, :26-29; POS.0590 | The principal's decision of 2026-09-27, by cost (POS.0590, intent:1176-1189) | C, I |
| C.23 | A recipe: composed with him, the language asked | recipe skill:32-44 | A principle; the birth of a recipe is C.04 | A |

Persistence

| # | What waits for his word | Stated in | Origin | Class |
|---|---|---|---|---|
| C.24 | The save itself: commit and push | save skill (front-matter, step 4); C.08 | C.08. A recorded harm of a push: a private directory carried into the public repository and `main` rewritten once (DEC.0120) | I |
| C.25 | The commit message: drafted from the records of the round, proposed, confirmed | save skill:28-35; release skill:58-66 | The principal's request at 1.7, 2026-08-04, as a relief: he confirms a message instead of writing one (archive, row 1.7). Word for word since the trailers of commit 1fe1dae (POS.1200) | B, with a small I (a public log) |
| C.26 | A tag | save skill:36-42; release skill:66-73; POS.1100 | Decided at 3.33 with the split of save and release (archive, row 3.33) | I |
| C.27 | The `light` check at a save, its findings settled through `/check`; a save never waits on a finding | save skill:23-27; POS.0430 | A check before a save: the principal's request at 1.3, 2026-08-04, "recommended procedure, never a gate" (archive, row 1.3). Narrowed to `light` because the full check cost minutes and a walkthrough every time (POS.0570, intent:1109-1110) | B |
| C.28 | The checks of a release, their findings settled by walkthrough; never fixed silently, never an unsettled finding | release skill:23-34; POS.0570 | The same request of 1.3, kept at the release by the split of 3.33 | B; A where a fix changes a rule |
| C.29 | `/critique essence` offered once at a release | release skill:35-41; POS.0400 | Decided 2026-09-05 (archive, row 3.33) | C |
| C.30 | Which repository, when `/release` is typed without a slug | release skill:12-14 | Archive, row 3.34 | B |
| C.31 | The findings a check marks "immediate fix": offered as one step | check skill:52-54; check contract:43-45 | No recorded origin. Already a batch | B |
| C.32 | The remaining findings of a check: the walkthrough, a rejected one by a DEC | check skill:55-61; POS.1140 | Findings filed and settled like a critic's since 2026-10-02, so that a rejected one does not return (POS.1140, intent:1478-1488) | B; A where a rule is worth changing |
| C.33 | The migration of a project to newer conventions | POS.0820; POS.0310; POS.0940 | The first challenge of the intent, at 2.8 (archive, row 2.8) | A, I |

The instance and projects

| # | What waits for his word | Stated in | Origin | Class |
|---|---|---|---|---|
| C.34 | Edits of the user's git configuration; the removal of a global identity | setup skill:30-49; POS.1050 | A principle: the only edits outside the engine | I |
| C.35 | A new project: its kind, its language, its brief | new-project skill:16-25, :61-66 | A principle | A |
| C.36 | The clone of an imported project | import-project skill:13 | POS.1060. No recorded failure | I |
| C.37 | A spin-off: his explicit instruction, the list of items, the approval of the derived brief | spinoff skill:7-22; CLAUDE.md:593 | A principle. No recorded failure | A, I |

### What the catalogue shows

1. **Four ways of asking.** The principal types the command (C.08);
   he confirms a proposal (a message, a tag, a lock, a delta); he
   gives a verdict per item (C.05); he says `write` and then yes
   (C.02). Only the third grows with the size of a list.
   *(Hypothesis, this note's grouping.)*

2. **Every recorded failure is of one kind.** Where a consent point
   has a recorded failure behind it, Claude acted, wrote or claimed
   beyond the word given: F.01, F.04 and F.06 of the run record, the
   incident of 2026-09-20 (THR.0400), the trailers of commit 1fe1dae
   (POS.1200), the private directory of DEC.0120. The searches found
   no recorded case in which a conformance finding fixed without a
   verdict of its own did harm. Verified as a result of the searches
   named above, not as a fact about what never happened.

3. **About a third of the points have no failure behind them.**
   C.10, C.13 to C.15, C.17, C.19, C.29 to C.31 and C.34 to C.37
   stand on a principle or a decision with no recorded incident.
   Two of the points that weigh on a save were asked for as reliefs
   or as recommended procedure: the proposed commit message (archive,
   row 1.7) and the check before a save (archive, row 1.3).

4. **The burden sits in the conformance findings.** The ledger's
   Findings table holds 88 findings: 82 resolved, 4 rejected, 2
   parked; of the 53 low ones 49 resolved, 2 rejected, 2 parked
   (counted from `ledger.md` on 2026-10-03). On 2026-10-02 alone six
   reports filed 45 findings (the checks `single-source-of-truth`
   19, `history` 10, `engine` 7, `project` 2, `light` 1, the critique
   `clarity` 6). By the letter each is one message and one verdict.

5. **The practice already delegates, and no definition says how.**
   The record holds the principal's word to settle findings in bulk
   by Claude's recommendation five times: the low findings of the
   release of 2026-09-20 (DEC.0130); ten of twelve at 4.30 (archive,
   row 4.30); seven of fifteen at 4.45 (history:113); the low ones of
   the `single-source-of-truth` report at 4.48 (history:135); all
   nine of the release checks at 4.49 (history:145). Three rejections
   were recorded as "settled by Claude on the principal's word"
   (DEC.0150, DEC.0160, DEC.0170), one of them of a medium finding.
   The `/check` procedure knows the batch of "immediate fix" findings
   and the walkthrough, nothing between (check skill:52-61). A
   procedure used five times and written nowhere is the kind of gap
   prime directive 10 names *(hypothesis as to the reading of the
   directive)*.

6. **The forge has removed ceremony before, each time by naming a
   class.** A verdict per group in place of a verdict per item of an
   assignment (POS.1350); the status `in_review` and its standing
   walkthrough dropped as a rule made in haste for one case whose
   cause was another (REJ.0230); the full check moved out of the save
   (POS.0570); a single letter for a verdict (POS.0850); the
   staleness of a render no longer a finding (archive, row 4.29).

7. **One open thread pulls the other way.** The hard half of
   THR.0400, a gate in front of the tools, would ask at every write
   into the repository, "a dialog per write, an isolated render
   included" (threads:548). The brief already names the tension.

### The flows, step by step

Counts are what the definitions demand, computed from the skills; the
answers of a real session were not measured.

**`/save` of one repository** (save skill).

| Step | What happens | Answers |
|---|---|---|
| start | the principal types `/save` | 1 |
| 1 | `forge-status` | 0 |
| 1a | the `light` check; clean | 0 |
| 2 | the commit message proposed | 1 (0 with `-m`) |
| 3 | a tag, only if he asked | 0 |
| 4 | `forge-save` runs | 0 |

Two answers when the check is clean, one with `-m`; one message more
per further repository with changes. Where `light` reports findings:
one answer for the batch of immediate fixes, one for the offer of a
walkthrough, one verdict per remaining finding, then `write` and the
yes. With n remaining findings that is n + 4 more, unless he declines
the walkthrough, which a save allows (save skill:26-27).

**`/release` of the engine** (release skill).

| Step | What happens | Answers |
|---|---|---|
| start | the principal types `/release forge` | 1 (2 without a slug) |
| 1 | `forge-status`, the branch | 0 |
| 2 | `light`, `engine`, `project`; clean | 0 |
| 3 | `/critique essence` offered | 1 |
| 4 | two renders; the delta reported and ruled on | 1 |
| 5 | `/save`: the `light` check again, the message proposed | 1 |
| 5 | at an approved major, the tag proposed | 1 |

Four answers for a clean release, five at a major. With findings at
step 2: up to one answer per report for its immediate fixes, one for
the offer, one verdict per remaining finding, `write` and the yes.
Accepting the essence lens adds a second list settled the same way.

The release of 2026-10-02 (intent 4.49) filed nine findings, none
marked as an immediate fix (the phrase stands in none of the five
check reports of that day). By the letter: 1 to start, 1 for the
offer, 9 verdicts, `write` and yes, the essence offer, the delta, the
message: 16 answers *(computed)*. The record says the nine were
"settled by Claude, on the principal's word to settle them all"
(history:145): one answer in place of ten.

The minutes are a second cost beside the answers. At that release
the isolated runs took 131 to 160 seconds for `light`, 315 for
`project`, 405 for `engine`, 241 for the release notes and 191 to
342 for the README (THR.0410). The `light` check runs at step 2 and
again inside the `/save` of step 5 (save skill:23); the measurement
of 2026-09-06 shows the second run as "pre-save light check 1:33"
(`research/2026-09-14-save-and-release-duration.md`).

**A check run with its walkthrough** (check skill). One answer to
start it, one for the immediate fixes, one for the offer, one verdict
per finding, `write` and the yes. The `single-source-of-truth` report
of 2026-10-02, 19 findings: 23 answers by the letter *(computed)*. As
recorded, the one high and the four medium findings were settled one
by one and the fourteen low ones on one word (history:135).

## Options with trade-offs

Each option names the class it touches and the recorded failure that
speaks against going further.

1. **Leave the definitions as they are.** The delegation of low
   findings goes on as an improvised word, differently worded each
   time. Costs nothing to build. The risk is the one of 2026-09-20: a
   broad yes read as covering more than was asked (THR.0400), with no
   definition to say what the word covers.

2. **Define the bulk settlement of class B findings.** One named
   way, in the `/check` procedure, to settle a stated class of
   findings by Claude's recommendation on one word, the whole shown
   in the reflection before the write, each rejection still a DEC
   with its reason. This writes down what the record shows five
   times. What it risks: severity is the reviewer's, not the
   principal's, and a low conformance finding in this project can
   move wording of CLAUDE.md, which is the product here. Two
   findings of the `history` check were rightly rejected because the
   intent must stay understandable (DEC.0150, DEC.0160), a judgement
   no check can make. The guard that remains is C.02: nothing is
   written before he has seen the round.

3. **Drop the verdict for class B and keep only the reflection.**
   Claude carries every recommended fix and the principal strikes
   what he does not want at the write. Fewest answers. The risk: a
   reflection of forty items is skimmed, and the one consent left
   becomes a formality. The run record's F.03 described such a
   position, a document to audit; REJ.0230 warns that the cause there
   was another, so the evidence is weak in both directions.

4. **Merge the confirmations of a save and a release.** The commit
   message is a derivation of records he confirmed at the write
   (POS.0310), so it could be shown and not asked; the essence offer
   and the tag could ride on the command's arguments. Saves one to
   three answers per release. The risk is small and named: a text in
   a public log he has not seen (commit 1fe1dae). A message shown
   before the script runs keeps most of the guard.

5. **Consent once per task for class C.** Where the principal hands
   a task over whole, as the brief describes, the word for research
   steps and reviewer runs is given once, with a stated bound, and
   not per run. The risk is cost without a ceiling (a check takes two
   to seven minutes, a render three to six) and that every reviewer
   run returns a list someone must settle, so the burden moves from
   starting runs to reading results. No failure is recorded for this
   class, which is also why nothing shows where its limit lies.

6. **Never delegate classes I and A.** A push, a tag, a lock, a
   publish, personal matter at ingest, the user's git configuration;
   positions, challenges, the closing of a thread, a new convention.
   Every recorded failure of the forge lies here (finding 2), and the
   harm of DEC.0120 could be undone only by rewriting `main`.

## Relevance to this project and recommendation

For the section Automation of `00-brief-next-gen.md`. The
recommendation is this note's own, offered once.

- **Carry the four classes into the brief as the measure it asks
  for.** The owner's word protects something in classes I and A,
  where every recorded failure lies. It is ceremony, by the forge's
  own record, in class B: 93 per cent of all findings and 49 of 53
  low ones ended resolved, and the principal has five times replaced
  the verdicts with one word. Class C is neither: the word there
  buys control of cost, and could be given once per task.
- **Take option 2 first, then option 4.** Both write down what the
  practice already does or what a position already allows, both keep
  the reflection before the write as the guard of authorship, and
  neither needs an agent. Option 5 belongs to the brief's "task
  handed over whole" and is best decided with it. Option 3 is not
  recommended: it removes the one question that the low findings
  rejected by DEC.0150 and DEC.0160 show to be needed.
- **Decide THR.0400 together with this.** A gate that asks at every
  write and a wish to be asked less are one question seen from two
  sides: which writes are class B.
- **Before deciding, count one real release.** The numbers above are
  computed from the definitions. One release counted from its
  conversation would show how many answers the harness's own
  permission prompts add, which no definition states.

What stays uncertain: the real number of answers in a session; the
prompts of the permission system; whether the immediate fixes of
several reports are offered once or per report (the check skill says
"at once" of one report); the failure behind Step by step (C.03),
which the record does not hold; and whether "low" is a fair proxy for
"bookkeeping", since severity is set by the reviewer.

Consult when: deciding which of the principal's words may be given
once for a class or a task, changing what `/save`, `/release` or
`/check` ask, or weighing the gate of THR.0400.
