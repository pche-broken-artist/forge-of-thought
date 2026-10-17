---
date: 2026-10-17
project: forge
target: work/collaboration-cutover.md (by hand, made from work/collaboration-cutover.spec.md v0.2)
reviewed: projects/forge/work/collaboration-cutover.md (whole); projects/forge/work/collaboration-cutover.spec.md v0.2; projects/forge/work/collaboration-cutover.spec.history.md; projects/forge/sources/cutover-plan-critique.md; projects/forge/40-solution-design.md v0.20 (SOL.0160, SOL.0300, SOL.0330, SOL.0460, SOL.0510, SOL.0520, SOL.0530, SOL.0670 to SOL.0820, TBC.0010 to TBC.0080); projects/forge/10-intent.md v5.17 (POS.1560, POS.1580, POS.1590, POS.1600, POS.1620, POS.1630, POS.1640, POS.1650, POS.1660, POS.1680, POS.1690, POS.1700, POS.1710, POS.1720, POS.1730, POS.1740, POS.1750, POS.1770); projects/forge/threads.md (THR.0620, THR.0640, THR.0650, THR.0690, THR.0700); projects/forge/decisions.md (DEC.0210); projects/forge/00-brief-collaboration.md v0.8 (M, Promise, impact, order, verification); projects/forge/ledger.md (Work and Challenges tables); projects/forge/challenges/2026-10-17-challenge-architect.md; projects/forge/challenges/2026-10-17-challenge-architect-2.md; .claude/skills/release/SKILL.md; .claude/skills/work/SKILL.md; .claude/settings.json (deny rules); scripts/forge-save.py (whole); scripts/forge_repos.py (whole); scripts/forge-branch.py (help header); CLAUDE.md as delivered in context, no challenge rests on a wording that could have changed
reviewer: challenger persona architect (solution architect, isolated context)
---

# Peer review (architect) — 2026-10-17

## Overall read

The plan turns the design of the brief `collaboration` into 55 steps
over the five releases of DEC.0210, each step naming the part it
realises, the files it touches and what closes it, in the order
shape, mechanism, use, test, run. That is the right kind of
document for this job and the critique of the same day has already
put the fixture, the tag, the dependency of the ledger script on the
migration and the order of R1.16 and R1.17 where they belong. What
the plan does not say is where it is itself carried out and what it
costs: on which branch of the engine the 27 steps of the first
release are built and saved, over how many sittings, and what the
upgrade channel carries meanwhile. Beside that, the fixture is put
where no script of the forge can reach it, the tail of the first
release locks Claude out of the engine's own project for four
steps, and the interval between the second and the third release,
where the first two-person trial would by the plan's own word be
run, is left without the sentence the first interval gets. Nothing
here is a wrong choice; it is the choices the plan did not make.

## Challenges

### CHL.0370 — The plan does not say where release 1 is built, and the two possible answers cost different things; the duration that decides between them is not priced
- **Severity:** major
- **Challenge:** Every step of the plan is a change to the engine
  (scripts, skills, templates, CLAUDE.md) saved by `/save`, which
  commits and pushes "on whatever branch is checked out"
  (CLAUDE.md, Persistence; `scripts/forge-save.py`). The plan does
  not say which branch. If it is main, as every change to the engine
  has been so far, then for the whole duration of the first release
  `origin/main`, the upgrade channel of `forge-pull`, carries an
  engine in which the shape of files and the skills that write them
  change step by step: after R1.04 the templates have no `date`
  while the write step still writes it until R1.11; after R1.16 the
  26 skills no longer write the ledger while the map calls a script
  over projects of the old shape; after R1.19 every writing skill
  refuses an unmigrated project. Any instance that pulls between
  two saves gets one of those states, with no release notes to tell
  it so, and the engine is public. If it is a branch, then the
  engine has one working tree until R2.07, so the branch is the
  only place the principal can work for the duration, `/release` is
  main only and refuses it, and the merge of the branch into main is
  raw git, since `/merge` is R2.05: the first release would be
  landed by the very act the brief exists to remove. The plan's
  method says "a skill cannot call a script that does not exist",
  which orders the steps within a release and says nothing of what
  stands between the steps on the remote. Whether the first answer
  is acceptable depends on how long release 1 takes, and the plan
  carries no price: THR.0620 weighed every other row in sittings,
  row 9 says "5 releases", and the 27 steps include the script the
  design calls the most complex of the engine, a migration with an
  undo and a manifest, a sweep of 26 skills and a release. The
  principal is to "tune the order and the cut" (specification,
  Task) and has nothing to tune a cut with.
- **Why it matters:** The first release is the one with the largest
  blast radius (CHL.0320) and it is the one whose intermediate
  states will be the longest-lived on the remote. The alternative
  the migration's own design makes cheap, two or three smaller
  releases each with its own marks, since `forge-migrate` runs
  "only the steps that are missing" (SOL.0800), was not weighed
  against one release of 27 steps; that cut belongs to DEC.0210 and
  THR.0620, not to this plan, and the plan is where its price would
  first show.
- **What would change my mind:** A line in the plan naming the
  branch and, where it is main, the states the upgrade channel may
  carry between saves and what a puller is told; or a weight per
  release in sittings, from which it can be read that release 1 is
  a matter of days and the question moot.
- **Epistemic status:** the mechanism from `forge-save.py`,
  `forge-branch.py` and the release skill as they stand; the
  duration my judgement, unverified.

### CHL.0380 — The fixture is put where no script of the forge can reach it, and nine closings rest on it
- **Severity:** major
- **Challenge:** R1.00 places the fixture in "tmp/ of the engine,
  never a project". `forge_repos.repos_to_visit` resolves a
  repository as the engine root or as `projects/<slug>/.git` and
  nothing else (`scripts/forge_repos.py`); every git script, and
  through them every command, is bound to that. So "a save and a
  status on the fixture" (R1.12), "a clone on the fixture" (R1.10),
  "a merge in each direction on the fixture" (R2.05), "a worktree
  made, saved and ended on the fixture" (R2.07), "a save after a
  merge on the fixture" (R2.09), "a landing on the fixture" (R3.02),
  "a write on the fixture" (R4.02), the driver's three cases
  (R2.02) and the four tests of THR.0650 (R2.12) cannot be run on a
  repository in `tmp/` without raw git, which Claude is denied
  (`.claude/settings.json`, `Bash(git *)`) and the forge denies the
  user by doctrine. The four tests moreover are rounds of forge
  work, a record to a history, a thread, a decision, a research, a
  render, a state-only round, two of them concurrently on two
  branches: that is Claude working a project by slug through the
  commands, not a test a person runs by hand on a clone. The
  fixture can be what the plan says it must not be, a project:
  `projects/fixture-a/` and `projects/fixture-b/` cloned by
  `forge-clone` from one local bare remote, gitignored like every
  project, visited by a bare `/save` like every project (the one
  price). The plan has also not said who makes the bare remote and
  the first commit, the one act that is neither a forge script nor
  Claude's: it is the principal's hand, once, and should stand in
  the step.
- **Why it matters:** The fixture is the first step of the plan and
  the ground of every test the design moved before the releases
  (TBC.0050); built where the plan says, it is found unusable at
  R1.10 and the tests either slip to the real projects or to a
  terminal.
- **What would change my mind:** The scripts taking a path as well
  as a slug, which the design does not have and would be a change
  to SOL.0510; or the fixture named as a project under `projects/`
  with its two clones.
- **Epistemic status:** the resolution of repositories from the
  module as it stands; no judgement needed.

### CHL.0390 — The tail of release 1 locks Claude out of the engine's own project for four steps, and R1.22 cannot be clean by the plan's own rule
- **Severity:** major
- **Challenge:** R1.19 has the map, `check-project` and every
  writing skill refuse a project of the old shape; R1.23 migrates
  `projects/forge`. Between them lie R1.20, R1.21, R1.22 and R1.26.
  In that window the engine's own project is of the old shape, so
  by R1.19 no skill writes into it: no `/forge intent` for the
  intent-first change ASM.0020 expects building to force, no
  `/forge solution-design` for a mended part, no decision, no
  thread; the plan's own state is the one write that survives,
  because the file is worked by hand. R1.22 then runs the release's
  checks, `light` and `project` among them, over the unmigrated
  `projects/forge`: `check-project` says "shape before the
  migration" by construction, and the step's closing, "clean or
  settled", is settled only by migrating, which is the next step
  but one. R1.24 runs the same checks again inside `/release`, so
  R1.22 is both impossible to pass and redundant where it stands.
  Behind the window stands a choice the plan did not make: ASM.0030
  says the engine's project migrates "first, on this clone, within
  the first release", and the order migrates it last, at step 23 of
  27. Migrated right after R1.13 and R1.09, the real project would
  exercise the ledger script, threads as files and the state
  records through the remaining fifteen steps, every save of the
  engine a test; the price is a window of its own, between the
  migration and R1.16 and R1.17, in which the skills still write a
  ledger that is gitignored and the definitions do not yet write
  state records, so a round's state would be written where nothing
  reads it. Either window is survivable; the plan should pick one
  knowingly, and the refusal of R1.19 should in any case come after
  the migration of the one project the builder writes into daily.
- **Why it matters:** The forge is built with the forge; the one
  project that records the building is the one the plan makes
  unwritable at the moment the building is most likely to change
  the design.
- **What would change my mind:** R1.23 moved before R1.19, with the
  interval between the migration and R1.16 and R1.17 said aloud;
  or R1.19 split so that the refusal lands as the last step before
  R1.24 and R1.22 dropped into R1.24, where `/release` runs the
  checks anyway.
- **Epistemic status:** the order from the plan as written, the
  refusal from SOL.0800; my judgement on the better of the two
  windows.

### CHL.0400 — Between the second and the third release a round on a branch bumps the header and every merge of a worked branch conflicts on `version`; the plan says what the first interval cannot do and nothing of the second
- **Severity:** major
- **Challenge:** Release 2 brings the driver, `/merge` in both
  directions, the worktree and `forge-branch --done`: after it the
  forge invites branches and merges, and the plan's own sentence
  for the first interval, "nobody in two before the second release"
  (R1.24), says that the trial in two begins then. The version as a
  boundary is release 3: until R3.04 the write step bumps `version`
  and `status` in the header on a branch exactly as on main, and
  POS.1660, "a branch never changes an artefact's header", is not
  yet true. So in the interval the plan opens for two people, a
  branch that ran a round and a main that ran a round conflict on
  the header's `version` line at every `/merge`, which is the
  collision the brief begins from with two of its three fields
  removed, settled in the walkthrough with no rule for which version
  wins; and the records those rounds wrote carry two different
  version numbers for one landing, which the third release's
  reading, "a record with a version is its own boundary" (brief,
  M), will then take as two versions. R2.06 adds a stopgap in the
  same spirit: the `changed` record of a merge verdict "carrying
  the current version as a state record until the third release",
  a content change filed under the one kind of record POS.1630
  defines as changing no content. R2.11 has no sentence for the
  release notes of the second release as R1.24 has for the first.
- **Why it matters:** The second release is the one that makes the
  promise of POS.1750 look kept; the first colleague who takes it
  at its word meets the header conflict on his first merge and a
  history whose versions the third release reads wrongly. A
  sentence in the release notes costs nothing; a history with two
  boundaries for one landing is a breach to repair later.
- **What would change my mind:** The second release's notes saying
  that a branch round still writes the header and that at a merge
  main's header is kept and the branch's records read under the
  next landing; or the third release's R3.01 to R3.04 pulled into
  the second, since the plan already lets R2.06 reach for the `+`
  token it does not yet have.
- **Epistemic status:** the mechanism from POS.1660, SOL.0760 and
  the write step as it stands today; the reading of a version
  record as a boundary from the brief; my judgement on the weight.

### CHL.0410 — Three closings cannot close as written: the diff that is known not to match, the video that is never identical, and the test with no word for red
- **Severity:** minor
- **Challenge:** R1.09 closes by diffing the script's ledger against
  "the hand-kept ledger of each" project. POS.1620 records that the
  hand-kept Waiting list "differed from any rule in both
  directions", and SOL.0800 has the migration print "a Waiting line
  without an ID" and the guesses of `origin` for review: the diff
  is non-empty by the design's own expectation, and the step does
  not say what a pass is, so it closes on the builder's taste or
  never. R5.01 closes with "a screenplay rendered to video
  identical before and after"; an `.mp4` made twice is not
  byte-identical, encoders write timestamps, so the test is red on
  a correct conversion, while the thing to prove, that `md2video`
  reads a one-sentence-per-line screenplay as the same score, is
  proven by the player's events file or by the syntax tree the
  same step already uses. R1.02 and R2.01 close with "result
  recorded in THR.0650"; TBC.0050 says each of these tests "blocks
  the release it precedes", and the plan has no step, no branch and
  no owner for a red result, though red on R1.02 would mean the
  refusals of SOL.0530 rest on a reversal that does not happen as
  described, and red on R2.01 that `rebase.backend merge` or
  renormalisation does not do what SOL.0740 registers it for. A
  plan Claude follows "step by step on the principal's word" needs
  the word for red before the day it is red.
- **Why it matters:** These are the three steps that were added to
  make the plan safer, and each is weaker than the risk it guards
  because its closing cannot be read as true or false.
- **What would change my mind:** R1.09 saying what counts as a known
  difference (the Waiting list, the unparsed rows the script names)
  and that everything else must match; R5.01 proven by the events
  file; the two tests carrying "red: stop, back to the design,
  TBC.0050" or whatever the principal wants said.
- **Epistemic status:** the hand-kept difference from POS.1620; the
  encoder behaviour consensus; the rest the plan as written.

### CHL.0420 — The way back is a tag, which is a way back for someone who types git; a project cannot go back alone once the engine refuses its old shape; and the tag of R1.26 is taken too early for every project but one
- **Severity:** minor
- **Challenge:** R1.26 and R5.09 tag every project before the
  migration and the conversion as "the one way back after the
  first save". Going back to a tag after a push is `git reset
  --hard` and a forced push, or a revert commit: none of it is a
  forge script, Claude is denied git, and on a protected main
  (POS.1770) the force push is refused to everyone but a
  maintainer. The way back is real and it is not the forge's. It
  is also partial: after R1.24 the engine on `origin/main` refuses
  to write into a project of the old shape (R1.19), so a project
  rolled back to `pre-r1` is a project nobody can work until the
  engine too is taken back, and the engine's main has by then been
  pulled by every other instance. And the moment: R1.26 tags
  "every project" between R1.22 and R1.23, but only `projects/forge`
  migrates then; the others migrate at R1.25, after the release,
  and any save they receive in between makes `pre-r1` a state
  before the migration in name only. The tag belongs immediately
  before each project's `/migrate`, which `forge-save <slug>
  --tag` already allows per project.
- **Why it matters:** A plan that names a way back it cannot walk
  will not be read as having one on the day; saying plainly that
  rollback is the principal's hand through git, and that it is the
  engine and every project together or none, is cheaper than
  finding it out.
- **What would change my mind:** The two tag steps saying who walks
  back and how, and the tag moved into R1.25 and R5.07 per project.
- **Epistemic status:** the mechanism from the save script and the
  deny rules; the protected-main behaviour from POS.1770; no
  judgement needed on the timing.

### CHL.0430 — The fourth release realises nothing anyone needs today and the fifth waits behind it by assumption, not by dependency
- **Severity:** minor
- **Challenge:** Release 4 builds `ids.md`, the allocation from an
  author's block and the overlap check (SOL.0790) for N authors.
  Today there is one author on every project; a project without
  `ids.md` "allocates from the sequence as today" and the ledger
  script already reports a duplicate ID (SOL.0680), so until a
  second author writes into a project the fourth release changes
  nothing anyone sees. ASM.0010 orders the releases strictly, "each
  released before the next starts", so the conversion to one
  sentence per line (release 5), which depends on nothing in
  release 4, waits behind a release whose trigger has not come.
  The plan carries no trigger for release 4 and no statement that
  releases 4 and 5 are independent. This is DEC.0210's order and
  not the plan's to change; it is the plan's to say what in the
  order is a dependency and what is a decision, so that the
  principal can reorder on the day a second author appears or does
  not.
- **Why it matters:** Small in cost; but a release built ahead of
  its first user is a release tested by nobody until the day it
  matters, which is the pattern the plan's own tests were moved
  forward to avoid.
- **What would change my mind:** A second author expected on a
  project before the conversion is wanted; or the plan marking
  which release depends on which, with the rest as the principal's
  order.
- **Epistemic status:** the independence from the design's Where
  lists; the weight my judgement.

## What is strong
- The method of the specification, shape then mechanism then use
  then test then run, is the right order and the plan follows it
  with few exceptions.
- The critique of the same day is worked in where it should be:
  the fixture, the migration before the ledger diff, R1.17 with or
  before R1.16, the stub driver and `ours` under rebase before the
  releases they guard, the marks turned over at every release.
- Every step names the part it realises, so a step that drifts from
  the design is detectable by reading one SOL item; that is what
  will keep the plan honest when the design changes again.

## Questions I cannot answer from the documents
- On which branch of the engine will release 1 be built, and does
  any other instance pull `origin/main` of the engine between
  releases? CHL.0370 is a footnote if nobody pulls and nothing if
  release 1 takes three days.
- Is the fixture meant to be driven by the forge's commands, or by
  the principal typing git on a clone? CHL.0380 stands in the first
  case only, and the four tests of THR.0650 read as the first.
- Will a second author write into any project before the conversion
  is wanted? CHL.0430 hangs on it.
- How many sittings does the principal expect release 1 to take?
  The plan carries no number and the specification's Task says he
  is to tune the cut.
