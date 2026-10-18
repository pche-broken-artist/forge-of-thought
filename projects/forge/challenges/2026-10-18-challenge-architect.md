---
date: 2026-10-18
project: forge
target: work/collaboration-cutover.md (by hand; its specification work/collaboration-cutover.spec.md v0.3; the plan as reworked after DEC.0230 and the architect's fourth challenge)
reviewed: projects/forge/work/collaboration-cutover.md (whole); projects/forge/work/collaboration-cutover.spec.md v0.3; projects/forge/work/collaboration-cutover.spec.history.md; projects/forge/40-solution-design.md v0.22 (SOL.0530, SOL.0550, SOL.0670 to SOL.0830, TBC.0010 to TBC.0080); projects/forge/10-intent.md v5.21 (POS.1100, POS.1700, POS.1710, POS.1730, POS.1740, POS.1750, POS.1760, POS.1770, REJ.0270 to REJ.0320); projects/forge/threads.md (THR.0620 row 9, THR.0640, THR.0650, THR.0690, THR.0700); projects/forge/decisions.md (DEC.0210, DEC.0220, DEC.0230); projects/forge/00-brief-collaboration.md v0.8 (What prompted it, F2, M, Promise, impact, order, verification); projects/forge/sources/cutover-plan-critique.md; projects/forge/sources/cutover-challenge-review.md; projects/forge/challenges/2026-10-17-challenge-architect-4.md; projects/forge/ledger.md (Work products and Challenges tables); scripts/forge-save.py (whole); scripts/forge-clone.py (whole); scripts/forge_repos.py (repos_to_visit, project_path); .claude/skills/release/SKILL.md (step 1); .claude/skills/setup/SKILL.md (the git configuration it writes today); CLAUDE.md as delivered in context, no challenge rests on a wording that could have changed
reviewer: challenger persona architect (solution architect, isolated context)
---

# Peer review (architect) — 2026-10-18

## Overall read

The plan is now the one DEC.0230 asked for: the first release on main
in one stretch behind a tag, the fixture born old and migrated, every
gate after what it tests, the boundary shipped with the driver, the
blocks of IDs on a trigger. Of the eight challenges of the two days
before, every accepted one is in the file where it belongs and the
three the branch's withdrawal made obsolete are gone with it. What is
left is of two kinds. One is a thing the withdrawal of the branch
moved rather than removed: the throwaway clones of every project,
which the two pre-release tests need and which the one tree cannot
hold through the forge's own door. The other sits a layer above the
plan and the plan inherits it: the trigger of the fourth release is
not the event that produces the collision it is meant to close, and
the mechanism it waits for would not close it. The rest is small:
what the fixture is after the stretch, three mechanics of the third
release, and a second machine the plan never mentions although it is
the first second clone the forge will have.

## Challenges

### CHL.0500 — The throwaway clones of every project have no way into the one tree: `forge-clone` names by URL and has no target, the flag that guards a clone has no home before the migration makes it, and a bare save pushes a migrated clone to its real origin
- **Severity:** major
- **Challenge:** R1.13 closes with `--apply` and `--undo` "on a
  throwaway clone of the fixture and of every project", and R1.09
  with the ledger script run over "throwaway clones of every project
  (R1.13)". DEC.0230 settled CHL.0460 as obsolete with the words "the
  throwaway clones live under `projects/` of the one tree as
  fixture-flagged projects". Three things stand between that sentence
  and a clone. First, the door: `forge-clone.py` derives the directory
  from the last segment of the URL and refuses an existing directory;
  `projects/flow-ba`, `projects/agentic-platform` and the other four
  are taken, so a clone of any real project through the forge's door
  fails by construction, whether from the origin or from the local
  path, and no step gives the script a target name (R1.10 changes it
  to read the project file, nothing else). The same holds for the
  fixture itself: R1.00 clones `fixture-a` and `fixture-b` "through
  `forge-clone`" from one URL, `tmp/fixture.git`, whose last segment
  is `fixture`; the second clone fails and neither carries the name
  the plan gives it. Second, the flag: `fixture: true` lives in
  `project.md`, which an old-shape project does not have until step
  B0 of the migration makes it from the ledger's header, and the
  ledger's header has no such field to carry over; so between the
  clone and its `--apply` the guard does not exist, and after
  `--apply` it exists only if the migration was told to write it,
  which no step says. Third, the sweep: `forge-save.py` bare visits
  every `projects/<slug>/.git`, runs `git add -A`, commits whatever
  changed and pushes wherever `origin` points. A throwaway clone made
  by hand from the real origin under another name, which is the only
  way left, has the real origin; after `--apply` it has changes; the
  next bare save of the stretch, which the plan expects since the
  engine's own project is to be exercised "at every save", commits
  the migrated shape and pushes it to the project's real remote from
  an engine that is half-built and unreleased. That is the failure
  CHL.0460 named, moved from the second tree into the first. A clone
  made from the local path instead is safe by git's default
  (`receive.denyCurrentBranch` refuses a push into a checked-out
  branch), but the plan does not say which, and the difference is
  the whole risk.
- **Why it matters:** These two closings are the only evidence the
  design put before the first release that a real project is never
  the first to be migrated (TBC.0050, CHL.0280). Built where the plan
  leaves them, the clones are made by hand in raw git, which the
  brief is removing, and the first real project migrated may be one
  pushed by a bare save nobody meant.
- **What would change my mind:** `forge-clone` given a target name as
  part of R1.10 and the fixture script using it; the clones named in
  R1.13 as made from the local path of each project, or the guard
  given a home an unmigrated clone can carry (a name pattern the
  sweep skips, or a line in the ledger's header that B0 carries into
  `project.md`); or the two tests moved onto the fixture's two
  projects alone, with the dry run over the real projects done
  read-only in place, which `forge-ledger.py` can do without any
  clone since it writes a gitignored file and stages nothing.
- **Epistemic status:** the name derivation and the refusal from
  `forge-clone.py` lines 43 to 49, the sweep from `forge-save.py`
  lines 59 to 100 and `forge_repos.repos_to_visit`, both read today;
  the refusal of a push into a checked-out branch is git's default,
  from memory, not verified here.

### CHL.0510 — Two branches of one author take the same ID, which is the second release's own use case; the fourth release's trigger is the wrong event and its mechanism would not close the hole
- **Severity:** major
- **Challenge:** POS.1100 says "the hole of two branches taking the
  same ID is closed by POS.1730". POS.1730 closes it between authors:
  a block per handle, the next free number inside my block. Two
  branches of the same handle read the same block and both take its
  next free number; two windows of one person on one project are two
  worktrees on two branches (POS.1700, R2.07, R2.08), the use case
  the second release builds and the brief opens with ("the same when
  one person works on two branches, or in two windows at once"). So
  after the second release every pair of branches of the principal
  that each open a thread, a decision or a position collide on the
  number; the driver unions the two immutable records side by side,
  the ledger script reports "a duplicate ID", and the ID scheme says
  never renumbered, so the project keeps two POS.1780 for good, and
  no document says what is done then. The plan's own test knows it:
  R2.12's first test adds "a decision with IDs from different
  hundreds (or, before F2, with the ledger script's report
  expected)", a gate written to expect the collision and pass. And
  the fourth release waits for "a second author writing into a
  project" (DEC.0220: the blocks "change nothing until a second
  author exists"), which is true of the blocks and false of the hole:
  the event that produces the collision is a second branch, and the
  second release makes branches cheap. When the trigger finally
  fires, the blocks fix the case between authors and leave the case
  within one author as it was.
- **Why it matters:** The promise of POS.1750 is that the record
  files merge by themselves and conflict only where two people
  changed the same item; a merge that silently gives two items one
  address, on the first day one person uses the feature the release
  is named for, is the opposite of that promise, and it damages a
  history that is never renumbered. This is a matter for the layer
  above the plan; the plan inherits it in the trigger of its fourth
  section and in the gate of R2.12.
- **What would change my mind:** A rule I have not found that makes
  the two windows of one person share an allocation; or the design
  taking the one-clone case the cheap way, since both worktrees are
  one repository: "the next free number is neither used nor
  reserved" read over every local branch through `forge_repos`,
  which needs no network and no block; or the trigger of the fourth
  release restated as "a second branch on a project", which the
  second release itself satisfies, with the blocks extended to the
  one-author case.
- **Epistemic status:** the allocation from POS.1730 and SOL.0790
  as written; the collision is mechanism, not judgement; that the
  two-windows case is the first one to occur is my judgement of who
  will use branches first.

### CHL.0520 — The fixture is born from "the templates of the day", so after the stretch it is born new-shaped and the migration has nothing to test: the test of SOL.0800 is one-shot, and nothing tests "one release back" or the conversion step on it
- **Severity:** minor
- **Challenge:** SOL.0830 wants the fixture "born in the shape of the
  day from the templates of the day" and "brought to the new shape
  by the migration itself, which it thereby tests"; R1.00 says the
  same. Both hold together only inside the first stretch. R1.04
  takes `date` and `last_change` out of the templates and R1.06 drops
  `templates/threads.md`; a `fixture.py` that fills the templates
  fills fields that are gone from that row on, and one that runs
  after the release makes a fixture in the new shape, which
  `forge-migrate` has nothing to do with. So the apply-and-undo of
  R1.13 runs once, on the clones made before R1.04 and kept on disk;
  on the second machine, or on this one after R1.24, the migration
  has no test bed. The two places that need one later are in the
  plan: R2.02 and SOL.0680 tolerate "the shape one release back", and
  R5.04 adds the conversion step to the migration and closes with "a
  dry run on every project", which is the real projects again.
- **Why it matters:** The migration is the one script that rewrites
  every project of every clone and must come out the same
  everywhere; its regression test should outlive the stretch that
  wrote it, or the next shape change starts from zero.
- **What would change my mind:** `fixture.py` carrying the old shape
  as its own content rather than reading the templates, or a tag on
  `tmp/fixture.git` the script can reset the two projects to, so
  that "the fixture of release N-1" is a command; or the design
  saying the migration's test is meant to die with the release.
- **Epistemic status:** SOL.0830's and R1.00's wording against the
  order of R1.04 and R1.06; no judgement needed.

### CHL.0530 — Three mechanics of the third release cannot run as written: the ignore-revs file needs the hash of a commit the script never makes, the conversion has no mark so the refusal of the old shape does not fire on an unconverted project, and the blame configuration is set on one machine
- **Severity:** minor
- **Challenge:** R5.04 has the migration's conversion step write the
  hash of the conversion commit into `.git-blame-ignore-revs`, and
  SOL.0800 and POS.1740 have the script commit nothing, `/save`
  following. A commit's hash exists after the commit; the script
  cannot write it before `/save` makes the commit, and after it the
  file is a second commit by someone the plan does not name, for the
  engine (R5.06) and for each project (R5.07) alike. Second, the
  marks SOL.0800 recognises are the project file, no `date`,
  `threads/`, `.gitattributes` and the ledger out of the index; the
  conversion adds none, so after R5.07's release an unconverted
  project passes the marks, the map and the writing skills do not
  refuse it, R5.02's light rule finds a line with two sentences on
  every wrapped paragraph, and a round written into it mixes
  one-sentence lines into 72-column prose until someone runs
  `/migrate` by habit. Third, R5.08 sets `blame.ignoreRevsFile` "on
  this machine"; without it the gain DEC.0210 names for the release,
  blame, is absent on every other clone, which git does not say.
- **Why it matters:** The third release is the one whose reason to
  exist is diff and blame; two of the three mechanics are the gain
  itself.
- **What would change my mind:** The skill `/migrate` running the
  save and then writing the hash as its own second save, said in
  R5.04; a sixth mark for the conversion; R5.08 named in the release
  notes' Action for every machine.
- **Epistemic status:** the hash from how git works, consensus; the
  marks from SOL.0800 as written.

### CHL.0540 — The second machine is not in the plan, and it is the first second clone the forge will ever have
- **Severity:** minor
- **Challenge:** DEC.0230 binds the second machine to not pulling the
  engine until the first release; the plan then says nothing more of
  it. R1.14, R2.04 and R5.08 run `/setup` "on this machine", so after
  each release the second machine runs with `ours` unregistered, the
  driver unregistered, the rebase backend as its git has it and no
  blame configuration; `forge-status` reports the first two from
  R1.12 on, which is degrading aloud, but the release notes' Action
  of R1.24 says "migrate every project", which on the second machine
  is the wrong act in both directions: its projects are to be pulled,
  since R1.25 migrates each on this clone, and `/migrate` on a
  project behind its origin refuses anyway. Nothing in the plan says
  "on every other machine: pull the engine, run `/setup`, pull every
  project", which is the whole upgrade path of POS.1740 seen from
  the clone that does not migrate, and the one the colleagues of
  POS.1770 will walk. The freeze itself ("no pull on the second
  machine until the release") is a habit with no mechanism; a
  `forge-pull` there fast-forwards into a half-built engine without
  a word.
- **Why it matters:** Every release of this brief changes what a
  machine must have registered; the second machine is where that
  path is walked for the first time by someone who is not building,
  and it is cheap to rehearse now and expensive to learn from a
  colleague's clone later.
- **What would change my mind:** One line per release naming the
  second machine's acts after the pull, in the plan or in the release
  notes' Action; or the registration moved into the repository where
  git allows it, which SOL.0740 rejected for the driver and may not
  have weighed for `blame.ignoreRevsFile`.
- **Epistemic status:** the registrations from SOL.0740 and
  SOL.0710 as written; that the second machine will be upgraded by
  habit rather than by a list is my judgement.

### CHL.0550 — The engine's own 35 threads get their origin guessed by the script with nobody judging, and the round that corrects them has no step
- **Severity:** minor
- **Challenge:** CHL.0480 was settled with the migration of the
  engine's project "by the script directly", R1.23 saying so, and
  the review's mend named "the judgement of the origins as a round
  by hand". The plan has the first half and not the second: C1 cuts
  `threads.md` with `origin` guessed from the text, default the
  principal, and the engine's threads are the ones where the guess
  is most often wrong, since THR.0620, THR.0670 and THR.0680 are
  Claude's syntheses by their own words and others are a document's.
  No row of release 1 reads the printed guesses and settles them, so
  the engine's thread files carry the default until someone notices.
- **Why it matters:** Small; but a thread's origin is the one field
  that says whose idea a matter was, and the engine's threads are
  the forge's record of its own thinking.
- **What would change my mind:** A row after R1.23, a walkthrough of
  the printed guesses, closing with the thread files saved.
- **Epistemic status:** the plan's text against the mend recorded
  in the ledger for CHL.0480; no judgement needed.

## What is strong
- The fixture born in the old shape and migrated, and every gate
  placed after what it tests, make the first release's two
  pre-release tests real tests rather than green by construction.
- The boundary shipped with the driver and `/merge` is the right
  package; the long-branch test among R2.12 is where it is proven.
- DEC.0230 states its price plainly: no project work between the
  sittings, a tag, and the principal's own git as the way back. A
  risk said is a risk taken.

## Questions I cannot answer from the documents
- How are the throwaway clones of the real projects meant to be
  made, from which source, and under which names? CHL.0500 hangs on
  the answer.
- Has the project `agentic-platform` already a second author by
  handle? The brief speaks of "a research made from another account";
  if that account's handle differs, the trigger of the fourth release
  has already fired, and the migration of that project must be told
  to whoever holds the other clone.
- Is `fixture.py` to read the templates at run time, or to carry the
  shape it makes? CHL.0520 reads differently in the two cases.
- When the ledger script reports a duplicate ID after a merge, what
  is the remedy the design intends, given that IDs are never
  renumbered?
