---
date: 2026-10-17
project: forge
target: work/collaboration-cutover.md (by hand, made from work/collaboration-cutover.spec.md v0.2; reworked 2026-10-17 after sources/cutover-plan-critique.md and sources/cutover-challenge-review.md)
reviewed: projects/forge/work/collaboration-cutover.md (whole); projects/forge/work/collaboration-cutover.spec.md v0.2; projects/forge/work/collaboration-cutover.spec.history.md; projects/forge/sources/cutover-plan-critique.md; projects/forge/sources/cutover-challenge-review.md; projects/forge/40-solution-design.md v0.21 (SOL.0300, SOL.0330, SOL.0460, SOL.0500, SOL.0510, SOL.0520, SOL.0530, SOL.0550, SOL.0640, SOL.0670 to SOL.0830, TBC.0010 to TBC.0080); projects/forge/10-intent.md v5.17 (POS.1560 to POS.1770); projects/forge/threads.md (THR.0620 row 9, THR.0640, THR.0650, THR.0690, THR.0700); projects/forge/decisions.md (DEC.0210, DEC.0220); projects/forge/00-brief-collaboration.md v0.8 (F2, M, Promise, impact, order, verification); projects/forge/ledger.md (Work products and Challenges tables); projects/forge/challenges/2026-10-17-challenge-architect-3.md; .claude/skills/release/SKILL.md; .claude/skills/save/SKILL.md; .claude/skills/pull/SKILL.md; .claude/skills/setup/SKILL.md; .claude/skills/document/SKILL.md; .claude/skills/work/SKILL.md; .claude/skills/check/SKILL.md (the filing); .claude/settings.json; scripts/forge-save.py (whole); scripts/forge_repos.py (whole); scripts/forge-branch.py and scripts/forge-clone.py (help headers and the name derivation); CLAUDE.md as delivered in context, no challenge rests on a wording that could have changed
reviewer: challenger persona architect (solution architect, isolated context)
---

# Peer review (architect) — 2026-10-17

## Overall read

The plan is the reworked one: four releases of DEC.0220, the fixture
first, the migration before the ledger script, the engine's own
project migrated early, the boundary in the second release, the tag
per project, the blocks of IDs on a trigger. Those were the right
mends and they are in. What the rework added is a place: the first
release is built on the branch `r1` in a second tree of the engine,
and that place has consequences the plan does not yet carry. The
engine's own project lives inside the engine's repository, so the
branch branches the forge's record of itself; the second tree holds
no project but that one, so the "throwaway clones of every project"
the two central tests need have no stated home; and the release at
the branch's end runs where the release skill refuses to run. Beside
the place, the three gates that stop a release are ordered before the
parts they test, and one closing repeats the pattern of CHL.0390 one
row later. The thinking under the plan is sound; what follows is
what the branch costs and where the steps cannot run as written.

## Challenges

### CHL.0440 — The branch branches the forge's own project: the merge of `r1` into main is a merge across the migration unless main is frozen, and nothing freezes it
- **Severity:** major
- **Challenge:** `projects/forge` is a tracked directory of the engine
  (SOL.0500), so the branch `r1` carries a second copy of the intent,
  the design, the decisions, the threads, the histories and the
  ledger. R1.23 migrates that copy on `r1`: `ledger.md` leaves the
  index, `threads.md` is cut into files and removed, every artefact
  loses `date` and `last_change`, the indexes gain fields on every
  entry, the histories gain records. The plan says main "stays for
  the daily work on the projects with the finished engine" and says
  nothing of what main's `projects/forge` receives over six to eight
  sittings. It will receive something unless a rule forbids it: a
  bare `/save` in the main tree runs the light check on the engine
  and files a finding into `projects/forge/reviews/` and the
  ledger's Findings table when it finds one (`/save` 1a, the `/check`
  filing); and ASM.0020 says the intent and the design change where
  building shows they must, intent-first, which is a round on
  `projects/forge`, and the plan does not say in which tree it is
  run. One such round on main and the merge of R1.24 is: `ledger.md`
  and `threads.md` modified on one side and deleted on the other,
  the header of `10-intent.md` changed on both, two histories
  appended on both sides and merged as text because the driver is
  the second release, an index entry added on one side into entries
  rewritten on the other. That is the collision the brief begins
  from, with the migration on top of it, resolved by the principal's
  hand in raw git, and the resolution then needs the main-side
  additions re-migrated by hand (a thread added into `threads.md`
  cut into a file, a `last_change` dropped). The tag of R1.26 is
  taken on `r1` after nine rows of building; for the engine the way
  back is main's tip before the merge, which needs no tag, and a tag
  mid-branch marks a half-built engine, not a state before.
- **Why it matters:** The merge of `r1` is the one step of the first
  release done by hand and without any of the tooling the release
  builds; the plan already calls it "the last manual git". Whether
  it is a fast-forward or the hardest merge of the whole programme
  is decided by a rule the plan does not state. With main frozen for
  the engine (every round on `projects/forge` on `r1`, `/save` with a
  slug only in the main tree, no bare save there) the merge is a
  fast-forward and costs nothing; the price is one line and a habit
  for the duration.
- **What would change my mind:** A line in the plan saying what main
  may receive during the build and where the rounds of ASM.0020 run;
  or the merge shown to be a fast-forward by construction; or the
  engine's own project excluded from the branch in some way I have
  not seen.
- **Epistemic status:** the mechanism from `forge-save.py`, the save
  and check skills and SOL.0800's steps; that main will receive a
  commit is my judgement of habit, the plan itself expecting bare
  saves in the second tree (R1.00).

### CHL.0450 — R1.24 runs `/document` and `/release` on the branch, where both refuse; merging first and releasing on main was not weighed
- **Severity:** major
- **Challenge:** R1.24 reads "`/document`, `/release` on the branch's
  tree, then the one manual merge of `r1` into main". The release
  skill's first step stops on any branch but main and names the way
  back; POS.1690 has the renders of a release and the documentation
  made only on main; SOL.0530 keeps that. No step of the plan
  changes the rule: R1.20 touches the release and document skills
  for the refusals behind and diverged only. So the step either
  breaks the rule by hand for one release, unsaid, or does not run.
  The alternative was not weighed: merge `r1` into main first (a
  fast-forward under CHL.0440), then `/document` and `/release` on
  main in the main tree. That order gives the README and the release
  notes rendered from the merged state, the release commit at main's
  tip, and makes the release notes' own sentence, "the merge of `r1`
  was the last manual git", true before the notes that say it. The
  plan's order gives a release commit on `r1` that main then merges
  behind it, renders made from a state main never had alone, and
  whatever a bare `/save` in the main tree does with the merge
  commit before R2.09, which is the step that teaches `forge-save`
  not to rebase one away.
- **Why it matters:** This is the step that closes the first release
  and it cannot run as written; the fix is to swap two clauses.
- **What would change my mind:** A reason the release must be made on
  `r1` that main after the merge does not satisfy; I found none.
- **Epistemic status:** the refusal from the release skill as it
  stands; the rest the plan as written.

### CHL.0460 — The second tree holds only `projects/forge`: the throwaway clones of every project have no stated home, and the home they will get carries the real origins
- **Severity:** major
- **Challenge:** R1.13 closes with `--apply` and `--undo` "on a
  throwaway clone of the fixture and of every project", and R1.09
  with the ledger script run over "throwaway clones of every project
  (R1.13)". The tree `../forge-of-thought@r1` carries in `projects/`
  only `projects/forge` (POS.1700, "a property to know"); the other
  projects are in the main tree, gitignored, and the scripts of the
  second tree resolve only `projects/<slug>` under their own root
  (`forge_repos.ENGINE_ROOT`). So the clones must be made in the
  second tree, through `forge-clone`, and the plan does not say from
  where. Cloned from each project's origin they are indistinguishable
  from the real projects to every script: `forge-save` bare visits
  every `projects/<slug>/.git`, and the one guard the plan built,
  `fixture: true`, covers the two fixture projects and not these.
  After `--apply` the clone has changes; the next bare save in that
  tree, which the plan expects there, commits the migrated shape and
  pushes it to the project's real origin from an engine that is
  half-built and unreleased. Cloned instead from the main tree's
  local path, a push is refused by git's default for a checked-out
  branch, and the clone is throwaway by construction. Two smaller
  things the tree also lacks: the gitignored instance files
  (`CLAUDE.local.md`, `.claude/settings.local.json`), which
  SOL.0770's script copies from R2.07 on and the principal's hand
  must copy before; and the assistant's memory, which the harness
  keys on the working directory, so the second tree starts without
  what the first has learnt.
- **Why it matters:** The dry run of the ledger script and the
  migration's apply-and-undo are the two tests the design moved
  before the first release so that a real project is never the first
  to be migrated; built where the plan leaves them, the first real
  project migrated may be one pushed by habit.
- **What would change my mind:** R1.13 naming the source of the
  clones as the main tree's path, or a guard on the clones a bare
  save honours; the instance files named in the sentence that makes
  the tree.
- **Epistemic status:** the resolution of repositories and the bare
  save from the scripts as they stand; the refusal of a push to a
  checked-out branch is git's default (`receive.denyCurrentBranch`),
  from memory, not verified here.

### CHL.0470 — The three gates that stop a release are placed before the parts they test, against the method's own rule
- **Severity:** major
- **Challenge:** The specification orders a release shape, mechanism,
  use, tests, run, because a script cannot read a template that does
  not exist. R1.02, `ours` under rebase, stands third: before the
  attributes exist in a template and in the fixture (R1.07) and
  before `/setup` registers `merge.ours.driver`, the rebase backend
  and renormalize (R1.14), which POS.1690 says git does not have
  built in. What R1.02 can test there is git with an attribute and a
  configuration typed by hand, which is raw git and not the forge,
  and not the thing that must be true for R1.20's refusal to rest
  on. R2.01, the stub driver under rebase, stands first in its
  release: before the way-2 attributes (R2.03) and before `/setup`
  registers a driver (R2.04). And R1.00, the fixture, stands first
  of all and makes "a decision with a Verdict, threads, an index, a
  published companion, `fixture: true`" before the template of the
  project file (R1.03), the Verdict field and the index fields
  (R1.05) and the thread file (R1.06) exist; its files column names
  `templates/project.md`, which R1.03 then creates. Either the
  fixture script dictates the shape and the templates follow it,
  the reverse of the method, or the fixture is made twice.
- **Why it matters:** These are the three tests whose red result
  stops a release (TBC.0050). A gate that runs before the thing it
  gates is green by construction and stops nothing; the first red
  will come on a real project.
- **What would change my mind:** R1.02 after R1.07 and R1.14, R2.01
  after R2.04, R1.00 after R1.07 or split into a bare remote now and
  its content when the shape exists.
- **Epistemic status:** the order from the plan and the dependencies
  from the design's Where lists; the registration's necessity from
  POS.1690. On a modern git the default rebase backend is already
  `merge`, from memory, which would make one of the three
  registrations redundant but not the other two.

### CHL.0480 — R1.23 closes with a command built sixteen rows later and checks whose agents learn the new shape afterwards; the window the review called one step is seven rows
- **Severity:** minor
- **Challenge:** R1.23 closes with "`/migrate forge`, the light and
  project checks clean". The skill `/migrate` is R1.19, the last code
  step before the release; at R1.23 there is the script with
  `--apply` and nobody to judge the origins of the threads, which
  SOL.0800 gives to Claude "within the same command". The agents
  `check-light` and `check-project` are taught the ledger script in
  R1.16 and the old shape's refusal in R1.19; at R1.23 they check the
  old conventions against a project that has just lost `date`,
  `last_change`, `threads.md` and a tracked ledger, so "clean" is
  the closing CHL.0390 already found impossible for R1.22, one row
  on. The review accepted the early migration on the condition that
  the window between it and R1.17 and R1.16 "lasts one step"; the
  plan then puts R1.10 and R1.11, the scripts that read the header
  and compute the version and the date from the records, after the
  migration too, so for seven rows the engine's own project has
  neither a ledger header nor a `date` while the scripts still read
  them.
- **Why it matters:** The forge builds itself with itself; every
  save of the engine in those rows runs the light check on a project
  the check cannot yet read.
- **What would change my mind:** R1.23 closing with the script's own
  verification and the checks after R1.16, the judgement of the
  origins named as a round by hand; R1.10 and R1.11 before R1.23.
- **Epistemic status:** the order from the plan; what the old agents
  verify from SOL.0330.

### CHL.0490 — Two parts of the design have no step, and the tests disagree with TBC.0050 in both directions
- **Severity:** minor
- **Challenge:** The state render: POS.1650 and SOL.0530 have a
  release on main write `renders/state.md` from the ledger script;
  no step of any release makes it, though R1.24 and R2.11 cite
  SOL.0530. The Role before the write: SOL.0750 and POS.1670 have
  `/ingest` ask what a source is for before its entry is written,
  since the indexes become mutable blocks; no step touches the
  ingest skill. The tests: TBC.0050 says the four tests of THR.0650
  run after the first and the second release; the plan runs them
  once, R2.12, and says nothing of the four after the first, which
  is right in substance (no branch, no driver, a merge by hand) and
  leaves the TBC saying what the plan does not do. And R2.12 runs
  after R2.11 by the letter of a TBC written when the boundary was
  a release later; now that the driver, the merge and the boundary
  are all in the second release and the fixture exists, nothing
  prevents the four from running before R2.11, where a red result
  would still stop the release whose reason for merging the
  releases was that a wrong boundary damages histories for good.
- **Why it matters:** Small, but the state render is the one piece
  of state the remote will carry at all, and the four tests are the
  only evidence the promise of POS.1750 is kept.
- **What would change my mind:** A step for each, or the design
  saying they are not wanted; R2.12 before R2.11, or a reason to
  release first.
- **Epistemic status:** the design's text against the plan's; no
  judgement needed.

## What is strong
- The dependencies between releases are now said, the trigger of the
  fourth is said, and the fixture is a project the scripts can
  reach: every accepted challenge of the previous run is in the
  plan where it belongs.
- Migrating the engine's own project early and refusing the old
  shape last is the right pair; the remaining steps exercise the new
  shape on the one project that records the building.
- The closings of R1.09 and R5.01 now have a truth value.

## Questions I cannot answer from the documents
- Will any round of the forge's own project be run in the main tree
  during the first release, or is everything on `projects/forge` to
  happen on `r1`? CHL.0440 is a line in the plan if the latter, and
  a merge nobody wants if the former.
- From where are the throwaway clones of every project to be made,
  and is a bare `/save` ever to be run in the second tree? CHL.0460
  hangs on both.
- Is there a reason the release of R1.24 must be made on the branch
  rather than on main after the merge? I found none in the
  documents.
- Is the fixture meant to be of the new shape from its birth, or to
  be remade once the templates exist? CHL.0470 reads differently in
  the two cases.
