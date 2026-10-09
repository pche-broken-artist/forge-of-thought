---
date: 2026-10-09
project: forge
lens: clarity
target: intent v4.64
reviewed: 10-intent.md v4.64 with threads.md (both read whole);
  decisions.md (searched for the findings of the last run);
  ledger.md (updated 2026-10-09); reviews/2026-10-02-critique-clarity.md
  (FND.0830 to FND.0880, regression); the check reports of
  2026-10-02 to 2026-10-09 listed in reviews/ (a check's, read by
  name only so that nothing of theirs is raised twice);
  40-solution-design.md v0.7 (SOL.0150, SOL.0160, SOL.0220 only, read
  to name where a passage of FND.1230 is already realised);
  templates/intent.md and .claude/skills/forge/states/intent.md, for
  the sections the intent's own template requires. The briefs are
  outside the target and were not read.
reviewer: critic lens clarity (isolated context)
---

# Critique (clarity) - 2026-10-09

## Delta summary
- **New:** FND.1210, FND.1220, FND.1230, FND.1240, FND.1250,
  FND.1260, FND.1270, FND.1280, FND.1290, FND.1300
- **Verified resolved:** FND.0830, FND.0840, FND.0850, FND.0860,
  FND.0870, FND.0880
- **Still open:** none
- **Newly obsolete:** none
- **Respected:** FND.0090 (rejected, DEC.0090; its condition fell at
  3.33 and nothing returns). FND.0450 and FND.0480 are a check's and
  rejected (DEC.0150, DEC.0160); nothing below asks for the sentences
  they keep to leave.

## Regression
- **FND.0830: verified resolved.** POS.0120 no longer makes a trial
  the condition under which the definitions leave the intent; the
  clause now reads "Where a project has no solution design, the item
  names the file ... it keeps the full information". POS.1380 has no
  sentence on a release still awaited.
- **FND.0840: verified resolved.** POS.0740 and POS.1150 are no
  longer items of the intent; POS.0930 states the exception as "the
  headless conversions behind `/publish`" and says the deferred
  per-recipe model is the render's. (The same item has since grown a
  second exception: FND.1240.)
- **FND.0850: verified resolved.** POS.0940 names the two checks a
  release composes and cites the owner: "`/check light` and `/check
  project` on each project say what the conventions changed (which
  check owns what: POS.1140)".
- **FND.0860: verified resolved.** POS.1080 and POS.0710 both say
  "its history"; "Version History" survives only in POS.0310 as the
  name of the older table and in THR.0230's list of engine parts.
- **FND.0870: verified resolved.** POS.1330 and POS.1350 cite
  POS.0110 and POS.0130 for what the artefact is ("a brief as
  POS.0110 has it", "an assignment as POS.0130 has it"); POS.1340
  cites POS.0120 for provenance; the restated sentences are gone.
- **FND.0880: verified resolved.** A Facts section stands and says
  why it is empty.

## Findings

### FND.1210 [medium] [contradiction]
- **Location:** 10-intent.md POS.0300 ("A major of the forge intent
  ... passes more than a minor before its tag: every check,
  `single-source-of-truth` included, both critic lenses and one
  challenge") against threads.md THR.0550 ("`essence` is not run on
  this project ... the principal keeps the offer in the release skill
  and declines it on forge ... Open until then") and THR.0570 ("what
  POS.0300 asks of a major is every check, both lenses of the critic
  and one challenge, the lens `essence` to be deferred by his word
  (THR.0550)").
- **Issue:** The position makes both lenses a condition of the
  major's tag; a thread of the same artefact records the principal's
  word that one of the two is not run on this project, and another
  thread plans the next major on that footing. The last run noted
  this while the word lived in the ledger only; it is now inside the
  artefact, and a major is on the table (THR.0570). The document
  cannot say whether 5.0 passes with one lens.
- **Why it matters:** POS.0300 is the one place that says what the
  principal's signature under a major attests ("The word closes the
  major; the test says what the word attests"). As written, the test
  of the coming major cannot be met, and a reader of the position
  alone would report the major as short of its own rule.
- **Suggested fix:** Let POS.0300 carry its own exception, in a
  clause: "a lens the principal has declined for the project by his
  recorded word is not asked of it", or name the condition under
  which `essence` is asked (the chain of the project having more
  than one artefact below the brief, as THR.0550 reasons). THR.0550
  then closes into the position or stays as the record of the
  condition, not as the contradiction of the rule.

### FND.1220 [medium] [contradiction]
- **Location:** 10-intent.md POS.1380 ("Locked artefacts are
  untouched by the change"); threads.md THR.0170 ("only if a brief in
  draft turns out to need structured, position-level work before it
  can be locked and mined"), THR.0230 ("as a brief born in the forge
  ... mined into the intent once locked") against POS.0110 ("It is
  not locked and not immutable: what it said at any version stands in
  its history and in git"), POS.0920 ("A brief is mined into the
  single intent when the principal says so, approved or not") and
  THR.0520 ("The locking of a brief is withdrawn (POS.0110,
  POS.0920, POS.0320)").
- **Issue:** The document retires the lock and keeps it as a
  condition in three places. In THR.0230 it is the condition under
  which the next brief, `engine-split`, enters the intent; in
  THR.0170 the condition under which a branch document would be
  considered; in POS.1380 the class of artefact a change of a
  definition leaves alone. Under POS.0110 no artefact is locked, so
  POS.1380's sentence names an empty class and THR.0230's course
  names a step the forge no longer has. REJ.0210's "before its lock"
  is a dated record of what happened and is not at issue.
- **Why it matters:** A reader who takes up THR.0230 waits for a
  lock that cannot come, or asks what stands in its place; a reader
  of POS.1380 cannot tell which artefacts a change of a definition
  may touch, since the class it names does not exist.
- **Suggested fix:** THR.0230 and THR.0170: "once the principal says
  to mine it" / "before it is mined", citing POS.0920. POS.1380:
  say what the sentence protects in today's words, for example
  "Artefacts already approved are untouched by the change", or cut
  it if nothing is protected.

### FND.1230 [medium] [scope-creep]
- **Location:** 10-intent.md POS.1050 ("The interview closes with
  the git identity, which is git's (POS.0950): `/setup` asks for the
  hosts the user pushes to, a name and an e-mail for each, and offers
  to write his git configuration for them, together with a global
  guard, never overwriting existing content, all written on the
  user's word; declined, printed for him to apply by hand"),
  POS.1060 ("it clones the repository, through the forge's clone
  script (POS.0550), into `projects/<repository name>`; a
  nonconforming name is fixed by renaming the directory afterwards"),
  POS.0180 ("`/ingest` creates it at registration when the bundle
  lacks one and validates a supplied one against the contents,
  origin dates best effort, never asked for"; "If a bundle's files
  ever need separate fates, a file may be split out to its own ledger
  row").
- **Issue:** The intent's own test (POS.1390: "How the command does
  it, what it is built of, its steps and their order and the checks
  it runs, is solution") puts these sentences in the solution design,
  and the solution design already carries them: SOL.0150 (what
  `/setup` writes, in what order, what it leaves and what it says),
  SOL.0160 (`/import-project` calls the clone script), SOL.0220 and
  SOL.0230 (what `/ingest` does with a bundle and its index). The
  three positions are not on the list of THR.0520's second pass
  (POS.0060 to POS.1380, twenty-two items), so the pass as planned
  would leave them. The Aim of the intent's definition: "It does not
  solve ... how it is realised is the solution design's."
- **Why it matters:** Two homes for one procedure drift (POS.1070);
  the intent's copy is the one a reader of the intent trusts and the
  one no check keeps true against the skill (POS.1420 gives that
  role to the solution design's items).
- **Suggested fix:** Belongs to `40-solution-design.md`, where it
  already stands; the move is a cut in the intent with the sentence
  that keeps what is wanted. POS.1050: replace the quoted sentence
  with "The interview closes with the git identity, which is git's
  (POS.0950): `/setup` offers to write the user's git configuration
  and its guard, on his word and never overwriting (SOL.0150)."
  POS.1060: replace the quoted clause with "it brings the repository
  in through the scripts-only door (POS.0550) under its own name as a
  project (SOL.0160)". POS.0180: replace "`/ingest` creates it at
  registration ... never asked for" with "created at registration
  where the bundle lacks one (SOL.0220)", and cut the sentence on
  splitting a file out of a bundle, which describes a ledger
  operation and not a want; the full wording goes to the history
  with `Was`, and the SOL items add the cut detail where they lack
  it (the origin dates best effort, the validation of a supplied
  index, the split of a file).

### FND.1240 [low] [contradiction]
- **Location:** 10-intent.md POS.0930 ("One model for the whole
  forge. Every command, chain state and reviewer runs on the session
  model"; "The one exception is the headless conversions behind
  `/publish`"; "a mirrored page is written on a faster model and a
  derived page, like the planner, on the session model, the choice
  made mechanically by the page's entry") and POS.0530 ("the session
  model, chosen once, with no per-agent pins (POS.0930)").
- **Issue:** The item opens with an absolute, names one exception,
  and then adds a second in the sentence that reports the
  documentation writer; "the one exception" is no longer true inside
  the item that says it. POS.0530 cites POS.0930 for "no per-agent
  pins" where POS.0930 now gives the writer agent a model by page
  kind. The same pattern as FND.0840: an absolute amended by a later
  sentence instead of rewritten.
- **Why it matters:** POS.0930 is the position a reader opens to
  learn what runs on which model, and it answers "one, with one
  exception" over a body that lists two.
- **Suggested fix:** Rewrite the opening and the exception in the
  present shape: "the session model everywhere but in two places:
  the headless conversions behind `/publish`, which have no session,
  and the mirrored pages of the documentation, which leave the model
  no room (POS.1450)"; POS.0530 cites POS.0930 "for the two
  exceptions" or drops "with no per-agent pins".

### FND.1250 [low] [contradiction]
- **Location:** 10-intent.md POS.0600 ("thoughts are the raw
  material ... and forged assignments are the product"), POS.0620
  ("the assignment is only where version 1 of the chain happens to
  end"), POS.0700 ("solution architecture and integration are
  intended ... the mechanics of a layer (commands, agents, reviewer
  calibration) are designed when that layer is actually taken up"),
  POS.0100 ("so later layers - a BRD (`30-brd.md`), a solution
  design - can be added"), POS.0970 ("the intention is decided, the
  implementation comes with the first library") against the Essence
  ("The chain ends where the project needs it to ... many end at the
  intent"), POS.1400 ("The solution design is an artefact of the
  chain, `40-solution-design.md`"), POS.1430 and threads.md THR.0510
  ("the library of today is rather a proof of concept").
- **Issue:** Five positions describe a chain that ends at the
  assignment, a solution design still to be added and a library still
  to be implemented, where the Essence, POS.1400 and THR.0510
  describe the present. THR.0520 names three of them as "behind the
  positions" (POS.0600, POS.0620, the last sentence of POS.0970) and
  records no verdict; POS.0700 and POS.0100 are of the same kind and
  named nowhere.
- **Why it matters:** The naming position (POS.0600) describes the
  forge in the way the position after it (POS.0620) forbids any
  one-line description to do, and a reader of POS.0700 is told the
  solution layer's mechanics are not designed while POS.1400,
  POS.1420 and POS.1430 are those mechanics.
- **Suggested fix:** Wording only, the stance unchanged: POS.0600
  "forged artefacts are the product, an assignment among them";
  POS.0620 "because an assignment is one place a chain may end, not
  the goal"; POS.0700 drop "solution architecture and" from the
  intended layers and say the mechanics of a layer are designed when
  it is taken up, "as the solution design's were (POS.1400)";
  POS.0100 "as the solution design (`40-solution-design.md`) was";
  POS.0970 "the first library exists" or the sentence cut.

### FND.1260 [low] [contradiction]
- **Location:** 10-intent.md POS.0550 ("every user project is
  likewise a repository with whatever remote and visibility its
  owner gives it") against POS.0940 ("a project starting 'not under
  git' is a property, not a defect. A project without a repository,
  or with a repository and no origin, is a legitimate shape").
- **Issue:** One position says every project is a repository, the
  other that a project without one is legitimate. Both are the
  principal's stance and both are dated; the first is the older
  wording left standing when the second was decided.
- **Why it matters:** POS.0550 is the position on persistence a
  reader opens first; it tells him a project is always under git,
  and a check written to it would report the shape POS.0940 permits.
- **Suggested fix:** POS.0550: "every user project is a repository
  of its own where its owner wants one, with whatever remote and
  visibility he gives it (POS.0940)".

### FND.1270 [low] [ambiguity]
- **Location:** 10-intent.md POS.1450 ("The README is cut to what
  orients and points, its chapters the readme skeleton's
  (`templates/recipe-readme.md`, the one owner); English only, a
  translation a render") and POS.0060 ("The forge as a system
  dictates only that a project has one output language: the
  artefacts ... Everything else a project holds - records, state,
  research and recipes - is always English ... a render may be in any
  language its recipe declares") with POS.1080's table (the kinds
  `page` and `map`).
- **Issue:** "English only, a translation a render" hangs by a
  semicolon on the README sentence inside a paragraph about the
  documentation. One reader takes it of the README, which POS.0060
  already covers as a render in its recipe's language; another takes
  it of the pages, which POS.0060 does not cover: POS.0060 names the
  artefacts, the records, state, research, recipes and renders, and
  the kinds `page` and `map` that POS.1080 added on the same day fall
  under none of its words. Whether the documentation of a project in
  another language is English or the project's language is said in
  neither place plainly.
- **Why it matters:** POS.0060 claims to be the whole language rule
  of a project ("dictates only that ..."); a project in another
  language, the case the rule exists for, cannot read off it what
  language its documentation is generated in.
- **Suggested fix:** In POS.0060 one clause placing the two kinds
  ("the documentation's pages and map are English, like the records,
  a translation a render" or "in the project's language, like the
  artefacts", whichever is wanted); in POS.1450 say the subject:
  "The pages are English only ..." or "The README is ... English
  only ...", not a clause that may belong to either.

### FND.1280 [low] [gap]
- **Location:** 10-intent.md POS.1090 ("A command that writes,
  scaffolds, commits or regenerates - `/save`, `/release`,
  `/spinoff`, `/setup`, `/new-project`, `/new-artefact`,
  `/import-project`, `/ingest`, `/render`, `/publish` - is guarded by
  the harness ... Maps, reports and rosters (`/forge`, `/ledger`,
  `/check`, `/critique`, `/challenge`, `/research`, `/recipe`) stay
  Claude's to start") and POS.1450 ("It is made by a command of its
  own, `/document [slug]`, in one run that asks nothing"; "A release
  never regenerates the documentation: it reports the age ... and
  offers `/document`").
- **Issue:** POS.1090 divides the commands into two enumerated
  lists, and `/document`, a command of the intent that writes and
  regenerates eighty files in one run that asks nothing, stands in
  neither. POS.1450 does not cite POS.1090 and "offers" is the only
  word that hints at the answer. The same list puts `/recipe` among
  what Claude may start, while the item's own last sentence makes the
  birth of a recipe a step that "happens on the principal's word,
  never as a by-product of another operation"; which half of
  `/recipe` (bare, the roster; with a genre, a new versioned
  document) the list means is not said.
- **Why it matters:** POS.1090 is where the guarantee of Step by
  step is said to rest on the harness; a command missing from its
  lists is a command whose guard a reader cannot tell, and the one
  missing is the most expensive write the forge has.
- **Suggested fix:** Add `/document` to the guarded list and let
  POS.1450 cite POS.1090 for who starts it; for `/recipe` say "bare
  `/recipe`, the roster" in the second list, the composition of a
  recipe falling under the step the last sentence names.

### FND.1290 [low] [gap]
- **Location:** 10-intent.md POS.0930 ("the trial of 2026-10-09
  showed Opus more complete on derived pages and Sonnet sufficient on
  mirrored ones (THR.0340)"), REJ.0240 ("Considered 2026-09-08
  (THR.0340, the guide and the reference as renders into `docs/`)");
  the closing section "Candidate structure for the layer below" ("A
  `20-assignment.md` would duplicate them for an audience that does
  not exist; see the ledger").
- **Issue:** THR.0340 is cited twice as if a reader could turn to
  it; threads.md does not carry it and neither citation says it is
  closed, where POS.0830 and POS.0950 show the document's own way
  ("THR.0150 closed", "THR.0580 closed 2026-10-09"). The closing
  section sends the reader to the ledger for a reason the ledger no
  longer holds (the `terminal:` line was withdrawn with POS.1400,
  THR.0520), and its reason speaks of an assignment while the
  project's layer below is the solution design, which exists and
  leads; the template's own instruction for the section is "deleted
  once the layer exists and leads".
- **Why it matters:** Two pointers inside the artefact resolve to
  nothing, and the one section the template says to delete stands
  with a reason written for a chain the project no longer has.
- **Suggested fix:** "(THR.0340, closed 2026-10-09)" in POS.0930 and
  REJ.0240, or the citation cut where the sentence stands without it.
  The closing section deleted as the template says; or, if kept
  because no assignment is wanted, one sentence in the present: "No
  assignment is made for this project (THR.0470); its layer below is
  the solution design (POS.1400), which leads."

### FND.1300 [low] [duplication]
- **Location:** 10-intent.md POS.0900 against POS.0140; POS.1460
  against POS.1090; POS.0860 against POS.0070.
- **Issue:** The group head of Working methods says some methods
  "name a position that already stands elsewhere", and the naming
  position then carries more than, or the same as, the one it names.
  POS.0900 cites POS.0140 at its end and holds the wider rule (the
  whole chain, a change from below); POS.0140 alone reads as a rule
  of the assignment only, so the owner is the narrower text. POS.1460
  cites POS.1090 for the birth of a versioned document, and POS.1090
  cites "Step by step" for the same sentence: each names the other as
  owner. POS.0860 repeats POS.0070 word for word ("Nothing enters
  content because Claude proposed it") beside the citation.
- **Why it matters:** The next change to intent-first or to the
  birth step is made in two items, and the copy that is missed keeps
  the old rule, the pattern of FND.0300, FND.0350 and FND.0870.
- **Suggested fix:** One owner per sentence: POS.0140 widened to the
  whole chain (its scope today) and POS.0900 cut to its name and the
  `??`-like additions it has none of, or POS.0900 made the owner and
  POS.0140 a citation; the birth step said once, in POS.1460, and
  POS.1090 citing it; POS.0860's repeated sentence cut to the
  citation.

## Recommendations
<!-- Not findings, not gates: wording that is hard to test, groups that
overlap, items that could be split. The principal may ignore these
without recording anything. -->
- POS.1420 says "A check keeps it true against what realises it" in
  the present tense; THR.0520 lists "which check keeps a solution
  design true against what realises it" as open and POS.1140's roster
  has none. "A check is to keep it true" would say what holds.
- POS.1080 says the artefacts "are listed nowhere else" than the
  state directory, and POS.1310 lists "the four artefacts of today's
  chain" by name. The rule is meant for the operating layer and the
  renders; saying so would keep the intent from breaking it.
- POS.0410 says "The critic has two lenses"; THR.0320 records a
  third decided in substance. One clause ("today") would carry it.
- Threads that have stopped being worked: THR.0470 is settled but
  for one question (whether large files are split) and carries the
  finished nine-step plan with "Until a step is done, what it changes
  stands as it stood on 2026-09-28", every step being done; THR.0350
  still lists "the sweep of this project's ledger" as to do. By
  POS.0120 a settled thread leaves the file; closing each and opening
  what is left on its own would let the file say what is being
  worked. From the last run.
- Stale words in threads, from the last run: THR.0210 names "both
  contract skills" where POS.1120 counts three; THR.0200 cites
  "readme recipe 0.24"; THR.0290 is headed "Research on the reviewer
  mechanism" over a body on `/research`. THR.0370 names
  `scripts/md2docx.py` and `md2pptx.ps1` in one breath after POS.0830
  made every script Python; THR.0400 proposes `scripts/hook-gate.ps1`.
- THR.0570 dates the presentation "the week after next by the
  principal's word of 2026-10-04"; a reader after that week cannot
  tell whether it has happened. The week itself would say it.
- POS.0570: "The full check left the save" uses a name no check in
  POS.1140 carries; "the bookkeeping check to the save" restates what
  the citation in the same sentence owns. From the last run.
- POS.0850 gives five verdict words and a verdict line of four
  letters; how `obsolete` is given is not said in the item. From the
  last run.
- "Publish" carries three senses: what the principal alone decides
  (POS.0430), the making of a designed file that sends nothing
  anywhere (POS.0590), and making the engine public (POS.0980,
  POS.0760). From the last run.
- POS.1140: "A check's findings are filed like a critic's ... The
  session gives the IDs and files the report, never the agent" reads
  two ways, since a critic's are filed by the agent (POS.0400);
  "filed in the same shape as a critic's" would settle it.
- POS.1080's table has no row for `threads.md`, which POS.0120 calls
  "part of the intent as the history is" while the history is a kind
  of its own; a clause under the table, as the one on binaries, would
  settle it. From the last run.
- POS.0710 says `/render` "regenerates the output mechanically,
  undated"; POS.0810 opens "Regeneration is stochastic" and every
  render "opens with its provenance, citing ... versions". The first
  means "without composition by the principal"; the word invites the
  other reading, and "undated" sits oddly beside provenance. From the
  last run.
- Whether a position keeps to "dated once" and "never as a
  measurement" (POS.0120) is the `history` check's; named only
  because POS.1450 carries a page count and a generation date beside
  its decision date, and POS.1140 two dates.
