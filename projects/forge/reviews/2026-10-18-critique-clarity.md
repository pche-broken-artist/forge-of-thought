---
date: 2026-10-18
project: forge
lens: clarity
target: all
reviewed: 10-intent.md v5.23 with threads.md (both read whole);
  40-solution-design.md v0.25 (read whole); 00-brief.md (placeholder,
  DEC.0010); 00-brief-public-engine.md v1.0; 00-brief-elicitation.md
  v1.0; 00-brief-next-gen.md v0.3; 00-brief-brd.md v0.2;
  00-brief-documentation.md v0.1; 00-brief-collaboration.md v0.8;
  decisions.md (DEC.0010 to DEC.0250); ledger.md (updated 2026-10-18);
  reviews/2026-10-09-critique-clarity.md (FND.1210 to FND.1300,
  regression); the check reports of 2026-10-02 to 2026-10-18 listed in
  reviews/ (a check's, read by name only so that nothing of theirs is
  raised twice); templates/intent.md, templates/solution-design.md,
  templates/brief.md and .claude/skills/forge/states/{intent,
  solution-design,brief}.md, for the sections each artefact's own
  template requires and the Aim each is judged against.
reviewer: critic lens clarity (isolated context)
---

# Critique (clarity) - 2026-10-18

## Delta summary
- **New:** FND.1830, FND.1840, FND.1850, FND.1860, FND.1870, FND.1880,
  FND.1890, FND.1900, FND.1910, FND.1920, FND.1930, FND.1940
- **Verified resolved:** FND.1210, FND.1220, FND.1230, FND.1240,
  FND.1250, FND.1260, FND.1270, FND.1280, FND.1290, FND.1300
- **Still open:** none
- **Newly obsolete:** none
- **Respected:** FND.0090 (rejected, DEC.0090; its condition fell at
  3.33 and nothing returns). FND.0450 and FND.0480 are a check's and
  rejected (DEC.0150, DEC.0160); nothing below asks for the sentences
  they keep to leave. The naming of the four review files is DEC.0140's
  and is not raised.

## Regression
- **FND.1210: verified resolved.** THR.0550 is closed and gone from
  threads.md; THR.0570 records that the test of the major ran on
  2026-10-09 with both lenses; POS.0300 holds as written and nothing in
  the artefact says a lens is declined.
- **FND.1220: verified resolved.** POS.1380 now reads "Artefacts
  already approved are untouched by the change"; THR.0170 says "before
  the principal says to mine it (POS.0920)"; THR.0230 says "mined into
  the intent when the principal says so (POS.0920)". No lock remains as
  a condition.
- **FND.1230: verified resolved.** POS.1050 ends at "offers to write
  the user's git configuration and its guard, on his word and never
  overwriting (SOL.0150)"; POS.1060 at "brings the repository in
  through the scripts-only door (POS.0550) under its own name as a
  project (SOL.0160)"; POS.0180 at "created at registration where the
  bundle lacks one (SOL.0230)", the sentence on splitting a file out
  gone.
- **FND.1240: verified resolved.** POS.0930 opens "with two exceptions
  named below" and names a first and a second; POS.0530 cites "the two
  exceptions POS.0930 names".
- **FND.1250: verified resolved.** POS.0600 "forged artefacts are the
  product, an assignment among them"; POS.0620 "an assignment is one
  place a chain may end, not the goal"; POS.0700 drops solution
  architecture and cites "as the solution design's were (POS.1400)";
  POS.0100 "as the solution design ... was and a BRD ... may be";
  POS.0970 "the first library exists".
- **FND.1260: verified resolved.** POS.0550: "a repository of its own
  where its owner wants one ... (POS.0940)".
- **FND.1270: verified resolved** as recorded: POS.1450 says "the
  README is English only, a translation a render"; the language of the
  pages is declared open in THR.0590, which names the finding.
- **FND.1280: verified resolved.** POS.1090 lists `/document` (and
  `/pull`) among the guarded commands, "bare `/recipe`, the roster"
  among Claude's, and says the composition of a recipe is the birth of
  a versioned document; POS.1450 cites POS.1090.
- **FND.1290: verified resolved.** POS.0930 and REJ.0240 cite
  "(THR.0340, closed 2026-10-09)"; the closing section says in the
  present that the layer below exists and why no assignment is derived.
- **FND.1300: verified resolved.** POS.0140 owns intent-first for the
  whole chain and the change from below, POS.0900 is its name and cites
  it; POS.1460 owns the birth step and POS.1090 refers to it; POS.0860
  keeps the citation and not the repeated sentence.

## Findings

### FND.1830 [medium] [contradiction] - At the state "diverged" one position offers `/merge`, another says `/merge` refuses a diverged repository
- **Location:** 10-intent.md POS.1490 ("diverged, the user merges
  through `/merge` (POS.1760) or lets `/save` rebase his commits onto
  the remote, and nothing is pulled until he has") against POS.1760
  ("It refuses a repository that is behind or diverged before it
  starts") and POS.1690 ("`/pull` says so at the state diverged": the
  path is "a branch, `/save` (a rebase with the driver), `/merge` into
  main (POS.1760) and `/save`").
- **Issue:** POS.1490 names `/merge` as the one offer the forge makes
  at "diverged"; POS.1760, the position that defines `/merge`, has it
  refuse exactly that state. POS.1690 gives a third answer, a path of
  four steps whose first is a branch, which POS.1490 does not say. The
  three cannot all hold for a reader on main whose clone has diverged
  from its origin.
- **Why it matters:** POS.1490 is the position on what the map and
  `/pull` say and offer at each state; the one state where the user
  needs an offer most is the one where the offer leads to a refusal.
- **Suggested fix:** Let POS.1490 carry the path of POS.1690 in words
  ("diverged: the local commits become a branch through `forge-branch`,
  `/save` rebases it, `/merge` brings it into main, `/save` pushes;
  nothing is pulled until he has"), or let POS.1760 say that `/merge`
  of `origin/main` into a diverged main is its path (the sentence on a
  refused push already describes one), whichever is wanted; the other
  two positions then cite the owner.

### FND.1840 [medium] [contradiction] - Older positions still have the ledger as the place where state is written, after POS.1600 to POS.1640 moved every state into records
- **Location:** 10-intent.md POS.1600 ("made at read time ... never in
  git"), POS.1610 ("What only the ledger knew lives in records, never
  in a header field"), POS.1640 ("`/check light` compares nothing with
  the ledger any more") against POS.0180 ("Origin dates ... recorded
  best-effort in the ledger"; "the ledger row is registration only"),
  POS.0920 ("the ledger tracks how far each is mined"), POS.1520 ("a
  file touched by hand and not remade is said so in the ledger's Work
  table"), POS.1140 ("`light` - ... the ledger against the files";
  "a row in the ledger"; "two reviewers run at once would otherwise
  take one ID and write one ledger twice"), POS.0400 ("both produce an
  immutable dated report and ledger rows"), POS.0440 ("a project's
  ledger is converted through a finding of the `light` check").
- **Issue:** Under POS.1600 nothing but the script writes the ledger,
  and under POS.1610 a source's date, a brief's mining and a work
  product's state are records of an index entry or a history. Six
  older positions still say the opposite in the present tense: the date
  is recorded in the ledger, the ledger tracks the mining, the hand
  state is said in the Work table, the reviewers produce ledger rows,
  the light check compares the ledger with the files. POS.0440's
  conversion of a ledger through a finding names an operation on a
  file the forge no longer keeps.
- **Why it matters:** A reader who opens POS.0180, POS.0920 or
  POS.1520 to learn where a state is written is sent to a file that
  POS.1600 says is never written; the one owner of each state
  (POS.1610) is contradicted by the positions that own the operations
  which produce it.
- **Suggested fix:** One clause in each older position, citing the
  owner: POS.0180 "recorded best-effort in the source's index entry
  (POS.1610) and shown in the ledger"; POS.0920 "the ledger shows how
  far each is mined, from the record of the mining in the intent's
  history (POS.1610)"; POS.1520 "is said so by a record in the
  specification's history (POS.1610), which the Work table shows";
  POS.1140 "`light` - ... what the ledger script reports (POS.1640)"
  and "a `closed` record in the history that settled it (POS.1610)" in
  place of "a row in the ledger", the clause "write one ledger twice"
  cut; POS.0400 "the records the ledger is made from (POS.1610)" in
  place of "ledger rows"; POS.0440's sentence on converting a ledger
  dated as done or cut. The full wording goes to the history with
  `Was`.

### FND.1850 [medium] [contradiction] - The role of a source is asked for after registration in two positions and before the entry is written in a third
- **Location:** 10-intent.md POS.0180 ("the principal's word, asked
  for once after registration and left empty until he gives it, never
  inferred unasked (POS.1040)"), POS.1040 ("after registration Claude
  always asks 'what is it for?', and he answers with the role or tells
  Claude to infer it") against POS.1670 ("`/ingest` asks what a source
  is for before its entry is written, so that Role is in the entry from
  its birth").
- **Issue:** Two positions place the question after registration and
  allow the entry to stand empty until the principal answers; the
  third places it before the entry is written so that no entry is ever
  born without a Role. Both are decided and dated; the two older ones
  were not brought to the newer.
- **Why it matters:** POS.0180 and POS.1040 are the positions that own
  `/ingest`; a reader of either builds a command that writes an empty
  Role, which POS.1670 was decided to prevent (a mutable block born
  without its payload).
- **Suggested fix:** POS.0180 "the principal's word, asked for before
  the entry is written (POS.1670), never inferred unasked (POS.1040)";
  POS.1040 "before the entry is written Claude always asks 'what is it
  for?' (POS.1670)", the clause "left empty until he gives it" cut from
  POS.0180 or restated as what happens when he gives none.

### FND.1860 [medium] [contradiction] - POS.1750 verifies the promise on a throwaway clone and, in its own last sentence, on a fixture project of the forge
- **Location:** 10-intent.md POS.1750 ("verified on a throwaway clone
  by four tests after the releases and three before them ... The
  fixture of the tests is a project of the forge, made by a script and
  driven by the forge's commands (POS.1590, CHL.0380)") against
  threads.md THR.0650 ("four on the fixture, never on a clone of a real
  project (DEC.0240)") and POS.1590 ("A fixture project, the test bed
  of the forge's own tests (POS.1750)").
- **Issue:** The item's opening clause is the wording before CHL.0380
  and DEC.0240, left standing when the last sentence was added: a
  throwaway clone is not a project of the forge made by a script, and
  THR.0650's dated paragraph rules the clone out in words. The same
  clause says the four tests run "after the releases"; the artefact
  says nothing else about their moment, so a reader has only the older
  word.
- **Why it matters:** POS.1750 is the position on what the forge
  promises, and its verification clause is the test of the promise; as
  written it names two places for one test.
- **Suggested fix:** "verified on the fixture of the forge's tests
  (POS.1590), a project made by a script and driven by the forge's
  commands, by four tests and by three before the releases: ..."; the
  last sentence then folds into the first and the moment of the four
  tests is said once, whichever it is.

### FND.1870 [medium] [ambiguity] - POS.1730 gives two rules for the next free number and no word on how they combine when both apply
- **Location:** 10-intent.md POS.1730 ("An ID on a branch of one clone
  is the next free number read over every local branch of the
  repository: ... the allocation takes the maximum over the branches
  plus the step; no network, no block"; "Between clones and between
  authors the number comes from a block of its author ... Everyone
  writes from his own block, the integrator too: the next free number
  is the next in my block"), with POS.0220 ("allocated over the local
  branches (POS.1730) ... never from the block or the sequence the two
  drew from").
- **Issue:** An author with a block who carries two local branches
  falls under both rules. One reader takes the maximum over the local
  branches within the block's range; another takes the maximum over
  the whole prefix across the branches, which lands outside the block
  and outside "everyone writes from his own block". POS.0220 adds that
  a number at a clash comes "never from the block", which in a project
  with blocks leaves no stated source, since the same position refuses
  the sequence where `ids.md` exists.
- **Why it matters:** POS.1730 is the one position on how a number is
  allocated; two competent builders of the second and fourth release
  would allocate differently, and the clash remedy of POS.0220 cannot
  be followed as written where blocks exist.
- **Suggested fix:** One sentence in POS.1730 saying how the two rules
  nest ("over the local branches, within the author's block where the
  project has one"), whichever is wanted; POS.0220's "never from the
  block or the sequence the two drew from" reworded to what it means
  (the number is read over the branches, not re-read from the block's
  or the sequence's last number).

### FND.1880 [low] [contradiction] - Whether every change of a thread is a record of the intent's history is said both ways
- **Location:** 10-intent.md POS.1760 ("the verdict on every conflict
  of an artefact is a `changed` record in its history, or in the
  intent's for a thread, as every change of a thread is") against
  POS.0120 ("the intent's history records the birth and the closing of
  a thread, not every saving of its debate") and POS.1680 ("A thread
  stays without a version and without a history of its own").
- **Issue:** POS.1760 states, as a general rule in a subordinate
  clause, that every change of a thread is a `changed` record in the
  intent's history; POS.0120 says the history records birth and
  closing only.
- **Why it matters:** The clause is the only place in the artefact
  that says every change of a thread is recorded, and it says it as if
  it were known; a reader of POS.1760 writes a record per saving of a
  thread's debate, which POS.0120 forbids.
- **Suggested fix:** POS.1760: "or in the intent's for a thread, where
  a thread's closing is recorded (POS.0120)", or the clause "as every
  change of a thread is" cut.

### FND.1890 [low] [contradiction] - The artefact requires a position to cite its brief with its version, and no position does
- **Location:** 10-intent.md POS.0110 ("A brief is the provenance of
  its whole: a position mined from it cites it with its version, and
  drift is measured against that version"), POS.0920 ("positions cite
  the brief and its version as provenance"), POS.1340 ("every position
  with its provenance") against every citation of a brief in the
  Positions: "Decided 2026-10-17 (brief `collaboration`)" in POS.1560
  to POS.1770, "from `00-brief-elicitation.md`" in POS.1300 to
  POS.1380, "from the brief `documentation`" in POS.1450, "from
  `00-brief-public-engine.md`" in POS.0760 and POS.0980; none carries
  a version.
- **Issue:** The rule is stated twice and kept nowhere in the same
  document; the one occurrence of a brief's version (POS.1480, "the
  brief `elicitation` 0.4") is a reason, not a provenance.
- **Why it matters:** The rule's own purpose, drift measured against
  the version mined, cannot be served by any citation in the artefact;
  a reader cannot tell whether the rule is the one that holds or the
  practice is.
- **Suggested fix:** Either the version added at the citations, from
  the Briefs table ("brief `collaboration` 0.8", "`00-brief-
  elicitation.md` 1.0"), or POS.0110 and POS.0920 cut to "cites it"
  with the measurement of drift against the version said to be the
  history's (the mining record of POS.1610 carries the version).

### FND.1900 [low] [style] - The closing note of threads.md stands in the middle of the file
- **Location:** threads.md, the paragraph "Note: the ID THR.0120 was
  inadvertently used twice ..." between THR.0680 and THR.0690.
- **Issue:** The note on duplicated and off-pattern IDs was the last
  paragraph of the file; THR.0690, THR.0700 and THR.0710 were appended
  after it, so a note about the file as a whole now interrupts the
  list.
- **Why it matters:** A reader working the threads in order meets a
  closing note and may stop there; the three newest threads are the
  ones being worked.
- **Suggested fix:** The note moved below THR.0710, or above THR.0090
  as a head note.

### FND.1910 [medium] [ambiguity] - The design marks "Not built" on its new items only; older items describe unbuilt behaviour in the present with no mark
- **Location:** 40-solution-design.md SOL.0120 ("the map ... refuses a
  project of the shape before the migration (SOL.0800)"), SOL.0150
  ("It also registers the merge drivers ... and writes `author:
  <handle>`"), SOL.0160 ("`/new-project` ... creates the project file,
  `.gitattributes`, `ids.md` and `threads/`"), SOL.0180 ("after a
  release that changes the shape of files says in Action required
  `/migrate <slug>`"), SOL.0210 ("made at read time by the ledger
  script and never in git"), SOL.0230 ("merging as a mutable block
  (SOL.0750)"), SOL.0400 ("On a branch the provenance cites
  `v<base>+N`"), SOL.0640 ("The Work table, made by the ledger script
  from the records") against SOL.0670 to SOL.0830, each closing with
  "Not built; the first release" or "Not built; deferred (DEC.0250,
  THR.0710)", and SOL.0530 ("its walkthrough walks the parts of this
  design marked 'Not built; the N-th release' for the N released and
  turns them over to built").
- **Issue:** The design's own device for saying what exists is the
  mark, and it is carried by the parts born from the brief
  `collaboration` only. The older items were brought to the new
  design by clauses in the present tense, so SOL.0160 reads as if
  `/new-project` creates `project.md` today and SOL.0210 as if the
  ledger were already made at read time. SOL.0530's walk keys on the
  words "the N-th release" and so never reaches an item marked
  "deferred".
- **Why it matters:** The Aim of the design is the solution as it
  stands today, read by whoever realises it without the principal in
  the room; the first thing that reader asks of an item is whether
  the file it names does this yet, and eight items answer wrongly.
- **Suggested fix:** Either the mark at every clause that is not built
  ("from the first release" / "deferred, SOL.0750"), or one sentence
  in the head stating the rule once: "a clause that cites an item
  marked Not built is not built either, and is built with it"; and
  SOL.0530's walk worded for both marks ("marked Not built for the
  release made").

### FND.1920 [medium] [contradiction] - How a bare save skips the fixture is said three ways, and the interim fixture matches none
- **Location:** 40-solution-design.md SOL.0510 ("`forge-save` without
  a slug skips a project whose project file says `fixture: true`"),
  SOL.0670 ("A fixture project carries `fixture: true`, and a bare
  `/save` skips it (SOL.0830)") against SOL.0830 ("A bare `/save`
  skips the fixture by name, `projects/fixture-*`, since the project
  file that would carry a flag does not exist before the migration;
  `fixture: true` in their project file stays for the map (CHL.0500)";
  "until then the fixture is one project `projects/fixture`, made by
  hand once").
- **Issue:** SOL.0510 and SOL.0670 have the skip keyed on the flag;
  SOL.0830 has it keyed on the name because the flag cannot exist in
  time, and keeps the flag for the map only. SOL.0830 then names the
  fixture of today `projects/fixture`, which the pattern
  `projects/fixture-*` does not match, so the one fixture that will
  exist first is skipped by neither rule as written.
- **Why it matters:** The skip is what keeps a bare save from pushing
  a test project to a real origin, the risk CHL.0500 named; the item
  that owns the fixture and the item that owns the save say different
  keys, and the interim case falls through both.
- **Suggested fix:** One key, said in SOL.0830 and cited from SOL.0510
  and SOL.0670 ("by name, `projects/fixture*`, the flag for the map"
  or "by the flag once the project file exists, by name before it"),
  and the interim name brought under the pattern or the pattern under
  the name.

### FND.1930 [low] [contradiction] - SOL.0510 names a `--reserve` of `forge-branch`, a reservation of IDs that SOL.0790 no longer has
- **Location:** 40-solution-design.md SOL.0510 ("`forge-branch.py`
  ... with `--worktree` or `--reserve` makes a working tree or a
  reservation of IDs (SOL.0770, SOL.0790)") against SOL.0790 (blocks
  "assigned by hand by the integrator in an ordinary round and saved";
  "against a reservation by plumbing onto main (REJ.0320)").
- **Issue:** The reservation by `forge-branch --reserve` is the
  plumbing REJ.0320 rejected; SOL.0790 describes no reservation and no
  such option, and the Where of SOL.0790 does not name
  `forge-branch.py`. SOL.0510's list of what the script does is the
  wording of the brief before the challenge.
- **Why it matters:** SOL.0510 is the roster of the git scripts; a
  builder of `forge-branch` reads an option whose mechanism the design
  rejected.
- **Suggested fix:** SOL.0510: "with `--worktree` makes a working tree
  (SOL.0770) and with `--done` ends a merged branch (SOL.0820)"; the
  reservation clause cut.

### FND.1940 [low] [contradiction] - The head says no part answers POS.0700 while SOL.0170 realises it, and the head's list of items added since 0.1 is four of twenty-odd
- **Location:** 40-solution-design.md, head ("No part answers
  POS.0600, POS.0700, POS.0780, POS.0790, POS.0980 and POS.1380";
  "The items added since (SOL.0170, SOL.0450, SOL.0460, SOL.0620 as
  rewritten) name their own dates and choices") against SOL.0170
  ("Realises: POS.1430, POS.0700") and SOL.0630 to SOL.0830.
- **Issue:** POS.0700 is both answered by no part and realised by one.
  The head's list of the items added since the move names four; the
  body carries twenty-one more (SOL.0630, SOL.0640, SOL.0650,
  SOL.0660, SOL.0670 to SOL.0830), so the sentence that tells a reader
  which items carry choices of their own is wrong for most of them.
- **Why it matters:** The head is what the reader of the design opens
  first to learn what in it is a one-off move and what is a designed
  choice; both of its sentences on that are stale.
- **Suggested fix:** POS.0700 removed from the head's list or from
  SOL.0170's Realises, whichever holds; the head's list replaced by
  the rule ("the items of 0.1 carry the one-off mark above; every item
  with a date of its own was added since") instead of an enumeration
  that ages.

## Recommendations
<!-- Not findings, not gates: wording that is hard to test, groups that
overlap, items that could be split. The principal may ignore these
without recording anything. -->
- The briefs gave the lens nothing to report. A brief is rough on
  purpose, and its definition says a tension, an alternative left
  undecided or a boundary left vague may stay in it, the resolving
  being the intent's; what is inside `collaboration` 0.8 that the
  intent later overturned (A2 first, the reservation by plumbing, the
  throwaway clone) is a dated record of the brief at its version, not
  a defect of the brief. One stale header: `00-brief-next-gen.md`'s
  fixed comment cites "CLAUDE.md, Document chain 1" for the rules
  where every other brief cites the definition.
- The positions of the brief `collaboration` (POS.1560 to POS.1770)
  speak in the present tense ("The ledger is made at read time",
  "Prose is written one sentence per line", "Threads are files") while
  THR.0620 row 9 and THR.0710 say most of it is not built and some of
  it deferred; the artefact being read is itself wrapped at 72
  columns. The intent says what holds, and a word ("is to be") or the
  horizon of POS.1360 at the group would carry it.
- POS.1110 says the hole of two branches taking the same ID "is
  closed by POS.1730"; POS.1730 says two windows allocating in one
  round "may still clash, a known limit". "Narrowed to" would say what
  holds.
- POS.1750 says the four tests run "after the releases"; THR.0650's
  paragraph of CHL.0410 does not say when, and the ledger's Waiting
  line (FND.1750) says before the second release and none after the
  first. The moment is said once in the position or left to the
  thread, not both.
- POS.1660 "the landing is the first act of the save, before the add,
  so after the check" reads as the script where "the save" elsewhere
  is the command that runs the check first; "the first act of
  `forge-save`" would settle it.
- Stale pointers in threads, the pattern of FND.1290: THR.0570 cites
  THR.0550 for the deferral of `essence` without "closed"; THR.0230
  cites THR.0220, THR.0350 and THR.0390 the same way; THR.0620 row 14
  sends the reader to "the closed record of THR.0630", which is in the
  history, not in this file. "(closed)" at each, as POS.0930 does for
  THR.0340.
- POS.0850 gives six verdict words and a verdict line of five
  letters; how `obsolete` is given is not said. From the last run.
- POS.0410 "The critic has two lenses"; THR.0320 records a third
  decided in substance. From the last run.
- POS.1080 says the artefacts "are listed nowhere else" than the state
  directory; POS.1310 lists the four by name. From the last run.
- POS.0310's list of record kinds lacks its conjunction before
  `approved`.
- SOL.0130 says "The genres today are `presentation`, `readme` and
  `release-notes`" and in the next sentence "The fourth genre,
  `screenplay`"; one list of four.
- SOL.0670 gives the project file three fields; SOL.0800 adds
  `wrapping: sentences` and SOL.0830 `fixture: true` without SOL.0670
  naming them. The owner of the file's fields is the one to list them.
- SOL.0790 says "The fifth digit is built within the first release"
  and three lines later "the fifth digit within the first"; once.
- TBC.0050 "before the second release's own release" reads as a slip
  for "before the second release".
- SOL.0120's Where names `templates/thread.md`, which SOL.0720 marks
  Not built; the design's rule for a file that does not exist yet is
  that the item carries the detail, which SOL.0720 does.
- "Publish" carries three senses in the intent (POS.0430, POS.0590,
  POS.0980); POS.0710's "undated" beside provenance. From the last
  run.
