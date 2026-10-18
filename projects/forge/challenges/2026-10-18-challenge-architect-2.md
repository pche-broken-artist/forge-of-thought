---
date: 2026-10-18
project: forge
target: work/collaboration-cutover.md (by hand; its specification work/collaboration-cutover.spec.md v0.4; the plan as reworked after DEC.0240 and the architect's challenge of the morning)
reviewed: projects/forge/work/collaboration-cutover.md (whole); projects/forge/work/collaboration-cutover.spec.md v0.4; projects/forge/work/collaboration-cutover.spec.history.md; projects/forge/40-solution-design.md v0.23 (SOL.0200 to SOL.0230, SOL.0300, SOL.0330, SOL.0500 to SOL.0550, SOL.0640, SOL.0670 to SOL.0830, TBC.0010 to TBC.0080); projects/forge/10-intent.md v5.22 (POS.0220, POS.0400 to POS.0450, POS.0550, POS.1100, POS.1110, POS.1120, POS.1200, POS.1560 to POS.1770); projects/forge/threads.md (THR.0620 row 9, THR.0640 to THR.0700); projects/forge/decisions.md (DEC.0210 to DEC.0240); projects/forge/00-brief-collaboration.md v0.8 (What prompted it, Mechanism D and M, Promise, impact, order, verification, Open); projects/forge/00-brief-collaboration.history.md (the record of 0.7); projects/forge/sources/cutover-plan-critique.md; projects/forge/sources/cutover-challenge-review.md; projects/forge/sources/cutover-challenge-review-2.md; projects/forge/challenges/2026-10-18-challenge-architect.md; projects/forge/ledger.md (the Challenges table, the row of FND.1690); projects/forge/reviews/2026-10-16-check-light.md (the heading of FND.1690); scripts/forge-save.py (whole); scripts/forge-clone.py (whole); scripts/forge_repos.py (whole); .gitignore (whole); .claude/agents/check-light.md (the ledger lines); CLAUDE.md as delivered in context, no challenge rests on a wording that could have changed
reviewer: challenger persona architect (solution architect, isolated context)
---

# Peer review (architect) — 2026-10-18

## Overall read

The plan now carries every accepted challenge of the three days in
the row where it belongs: the fixture born old and carried by its
script, the clones of real projects gone, the allocation over the
local branches in the second release, the second machine's acts at
every release, the origins of the engine's threads as a round. What
remains is of three kinds. First, the one gate before the first
release that survived the withdrawal of the clones kept a closing
written for a migrated clone and now runs over unmigrated projects
in place, where "writes a gitignored file" is not true and the
hand-kept ledger it is diffed against is the file it overwrites.
Second, two matters of the layer above that the plan inherits as
settled and are not: the trigger of the fourth release, by its new
wording, has already fired on the forge's own evidence, and the one
remedy the design has for a clash of IDs, the exception to "never
renumbered", has no step that builds it and a test written to avoid
the case that would show it. Third, small mechanics: the first row
uses a door built eleven rows later, the tag of the way back comes
after two building commits, and the tags that were to make the
fixture outlive the stretch live in a directory that does not.

## Challenges

### CHL.0560 — R1.09's "dry over every project in place" overwrites the hand-kept ledger it is diffed against and leaves a change a bare save pushes; its pass criterion was written for a migrated clone and cannot be graded over the old shape
- **Severity:** major
- **Challenge:** R1.09 closes with the ledger script run "dry over
  every project in place, since it writes a gitignored file and
  stages nothing", the output to differ from the hand-kept ledger
  "only in Waiting from the rule, lines named unrecognised and
  origins guessed, everything else equal". Three things are wrong
  with that as the plan stands. The file is gitignored only after
  step B of the migration takes it out of the index (SOL.0800); on
  the five real projects at R1.09, which R1.25 migrates last,
  `ledger.md` is a tracked file, so a run "in place" writes the
  script's output over the hand-kept ledger, which is the reference
  of the diff, and leaves a modified tracked file in every real
  repository, which the next bare `forge-save` of the stretch (`add
  -A`, commit, push to origin; lines 59 to 100) commits and pushes
  from an engine that is half-built; the design gives the script no
  output path and no print mode, "dry" is a word in the closing and
  no mode of SOL.0680. And the pass criterion: the critique of
  2026-10-17 (`sources/cutover-plan-critique.md`, Closings) said in
  so many words that over an old-shape project the script "gives no
  Findings, Challenges or Waiting", since those live in records the
  migration makes and in `ledger.archive.md`, which does not exist
  before step B; the answer then was the migrated clone, and the
  criterion "everything else equal" was written for it. DEC.0240
  removed the clone and kept the criterion. Over an unmigrated
  project the Findings, Challenges, the Briefs' mining and the Work
  states have no record of the new shape and no archive to fall
  back on, so the diff fails in a fourth class the closing does not
  name, or the script reads the old ledger's own tables as its
  archive when `ledger.archive.md` is absent, which "the shape one
  release back tolerated" might mean but nothing says. As written,
  the one test of the parser over the irregular real records
  (TBC.0050: "the test of the parser over the irregular records and
  the list of what the migration cannot derive") is either
  destructive or ungradeable.
- **Why it matters:** This is the gate that stops the first release
  (TBC.0050, "a red one stops it"); a gate that cannot be read as
  green or red is passed by habit, and the one way to make it
  readable, clones, was just withdrawn for good reasons. The
  overwrite is the smaller harm, it is `--undo`'s and git's to
  restore, but it is exactly the kind of change to a real project
  during the freeze that DEC.0230 promised would not happen.
- **What would change my mind:** The ledger script given an output
  other than `ledger.md` (a path, or stdout) so that "dry" is a mode
  and the tracked file is never touched; and the pass criterion
  restated for the old shape, either by naming the tables the
  script cannot derive before the migration as a fourth class, or by
  the script reading the hand-kept ledger's tables as the archive
  where no `ledger.archive.md` exists, said in SOL.0680 as what
  "one release back" means at this release.
- **Epistemic status:** that `ledger.md` is tracked before the
  migration and swept by a bare save, from `forge-save.py` and
  `forge_repos.repos_to_visit` read today and SOL.0800's step B;
  what the script can derive from the old shape, from SOL.0680 and
  SOL.0690 as written and the critique's own statement; that
  "one release back" does not cover it is my reading of SOL.0680,
  and I ask below.

### CHL.0570 — The fourth release's trigger, "a second clone of the same author writing into a project", has already fired on the brief's own evidence; the plan treats it as future and builds it on the first release alone
- **Severity:** major
- **Challenge:** DEC.0240 widened the trigger to "a second author or
  a second clone of the same author writing into a project", and
  the plan's heading and its dependency line ("the fourth the first
  and its trigger") follow. The brief records the collision at the
  save of 0.6 on 2026-10-17, "the ledger on both sides, a double
  FND.1690": FND.1690 is a finding of the forge's own project filed
  by the light check of 2026-10-16, and two files with it on two
  sides means two clones each ran a save on the engine's project;
  DEC.0230 says the engine's main is pulled by the principal's
  second machine; agentic-platform's two evidenced merges are the
  brief's opening fact. By the wording of DEC.0240 the trigger fired
  before the first release was planned. Two readings are possible
  and the plan chooses neither. One: the trigger means what it says,
  the fourth release is due with the second, and the plan's
  dependency is wrong as well, since R4.02 extends the allocation
  R2.13 builds (SOL.0790 writes the branch allocation and the block
  allocation into one rule, and the review's second piece says the
  renumbering at a clash must see the block too), so a fourth
  release built on the first alone would build the allocation twice.
  Two: the trigger means something narrower than it says, two clones
  with branches in flight at once, because two clones on main that
  pull before writing allocate over the pulled state and do not
  collide, and the risk of writing while behind is one the principal
  already carries today and the map's last word now names; then the
  heading should say that, and the known limit of POS.1730 should
  say that the principal's two machines live under it until a second
  author comes.
- **Why it matters:** The difference is one release built now or
  later, and whether the forge after the second release is safe for
  its one real user on his two machines, which is the only
  collaboration it will see for a while. A trigger that has fired
  and is kept as a future event is a decision not taken, and the
  plan's dependency line would send the fourth release down a wrong
  path if it fires by surprise between the first and the second.
- **What would change my mind:** The principal saying the second
  machine only pulls and never writes into a project (then the
  double FND.1690 needs another explanation), or the trigger
  restated as two clones with branches in flight at once, with the
  sequential case named as covered by pull before writing; or the
  blocks moved into the second release's package, which is where
  R4.02 belongs technically once R2.13 exists.
- **Epistemic status:** FND.1690's origin and the brief's sentence
  read today; that the two sides were the principal's two machines
  rather than another account is my inference from DEC.0230, not
  stated anywhere; the dependency of R4.02 on R2.13 from SOL.0790 as
  written.

### CHL.0580 — The one remedy for a clash of IDs, the exception to "never renumbered", has no step that builds it, no command that owns it, and the only test that could show it is written to avoid the case
- **Severity:** major
- **Challenge:** POS.0220 and SOL.0790 now say what happens when a
  merge shows two items with one number: the item of the branch that
  landed second takes a new number by the allocation over the local
  branches, a `changed` record "ID clash at merge" with `Was`, the
  citations corrected in that branch, a thread's file renamed. No
  row of any release builds it. It is not `/merge`'s walkthrough as
  R2.06 describes it, since a clash is not a git conflict: the
  driver leaves two immutable records with one key side by side
  without markers (SOL.0750), and two `POS.1780` in different places
  of the intent merge as clean text; the clash is first seen by the
  ledger script's report (SOL.0680, "a duplicate ID") after the
  merge is committed and pushed, and the report is a line in a
  derived file nobody acts on by a mechanism. So the first clash
  will be mended by Claude improvising a renumbering across a
  history, an intent and possibly a thread file, against prime
  directive 10. And the test that would exercise it, R2.13, is
  written so that it cannot occur: "the second allocating after the
  save of the first" sequences away the race POS.1730 calls a known
  limit, two windows allocating in one round before either saves,
  which is the brief's opening case, one matter in each window, each
  round hours long. The gate passes by construction and proves the
  allocation, not the forge's answer to its limit.
- **Why it matters:** The case is the one the second release is named
  for, one person in two windows, and its failure damages an
  immutable history that is never renumbered except by this one
  procedure; a procedure that exists in a position and nowhere in a
  skill is the kind of gap the forge's own rule forbids.
- **What would change my mind:** A row in the second release naming
  the owner of the remedy (the ledger script reporting, and a
  command or a step of `/merge` or of the walkthrough performing the
  renumbering on the word, with the thread rename through
  `forge_repos` since a rename is a git act) and closing with the
  race run once on the fixture: two branches allocating before either
  saves, the duplicate reported, the remedy applied, the history and
  the thread file right afterwards. Or the design saying the remedy
  is by hand and why that is acceptable.
- **Epistemic status:** the mechanism from SOL.0750 and SOL.0680 as
  written; that no row builds it is the plan's text; that the race
  will occur is my judgement of how the principal works two matters.

### CHL.0590 — The stretch is equated with the release, not with the shape change: a third of its rows change nothing the migration migrates and could ship before it, shortening the freeze and rehearsing the second machine's path once with no migration in it
- **Severity:** minor
- **Challenge:** DEC.0230's price is the freeze: no work on any
  project between the sittings, six to eight of them. The stretch as
  planned carries rows that touch neither a template, nor a header,
  nor a record, nor the ledger: R1.01 (filing by the command), R1.08
  (the fifth digit, "no ID rewritten"), R1.12 (the push of an ahead
  repository), R1.18 (unique names of reports), R1.28 (`/ingest`
  asking the Role), R1.10's clone target, R1.00's fixture script and
  the skip by name, and R1.14's registrations of `ours`, the backend
  and renormalize, which are harmless without the attributes. Nine
  rows of twenty-nine; an ordinary release before the stretch would
  carry them, the second machine would pull it the normal way, and
  `pre-r1` would then mark the true start of the shape change. The
  least that would do was not weighed: the review that sized the
  stretch counted the ledger script, the migration, the skills, the
  templates, the fixture and the release, and the rows above fell
  into it unpriced. I will not overstate the gain: a sitting, maybe
  two, and the fixture script checked against the templates of the
  day while they still exist, which R1.00 can do only before R1.04.
- **Why it matters:** Every sitting of the stretch is days of
  calendar in which five projects stand still, and the way back
  grows with every building commit under the tag.
- **What would change my mind:** The principal saying the sittings
  are consecutive days and the freeze costs nothing; or a reason the
  rows above must be in the stretch that I have not seen.
- **Epistemic status:** which rows touch the shape, from their
  `files` column and SOL.0800's marks; the size of the gain, my
  estimate.

### CHL.0600 — The first row uses a door built eleven rows later, the tag of the way back comes after two building commits, and two closings still say "the clone the principal makes"
- **Severity:** minor
- **Challenge:** R1.00 closes with the two fixture projects "cloned
  through `forge-clone <url> <name>` (R1.10)", and R1.10 is where the
  second argument is built; `forge-clone.py` today derives the name
  from the URL and refuses an existing directory, so R1.00 cannot
  close until R1.10, against the method's own rule that the
  mechanism precedes its use. R1.26 takes the tag "before R1.01",
  but R1.00 already changes `forge-save.py` and adds `fixture.py`,
  two building commits under no tag, so `pre-r1` does not mark the
  state before the first building commit as DEC.0230 says. And R1.02
  and R2.01 keep "none; the clone the principal makes" in their
  files column after DEC.0240 put every test on the fixture and
  forbade a hand clone; a builder reading the row makes the clone.
- **Why it matters:** Small, but all three are at the start of the
  stretch, where a wrong first step costs the most and the rule
  "mechanism before use" was the plan's own answer to CHL.0470.
- **What would change my mind:** The clone target moved into R1.00
  as the one line it is, R1.26 said to precede R1.00, and the two
  columns corrected; or a reason the order is right that I missed.
- **Epistemic status:** the plan's text against `forge-clone.py`
  read today; no judgement needed.

### CHL.0610 — The tags that make "a fixture of release N-1" a command live on a bare remote in the gitignored `tmp/` of one machine, so the lasting test bed accepted for CHL.0520 lasts as long as that directory
- **Severity:** minor
- **Challenge:** SOL.0830 and R1.00 put the fixture's remote at
  `tmp/fixture.git`, tagged `shape-<version>` at every release with a
  migration, so that R5.04 and the one-release-back tolerance have a
  bed. `tmp/` is gitignored and per machine; on the second machine,
  or on this one after a cleanup, `fixture.py` makes the shape it
  carries, 5.22, and the only road from there to the shape of release
  N-1 is the migration script, which runs every step whose mark is
  missing and arrives at N, not N-1. So "one release back" is
  testable only where the tag happens to survive, and the fixture
  the second machine can make is always the oldest shape or the
  newest.
- **Why it matters:** The point of CHL.0520 was that the migration's
  regression test outlive the stretch that wrote it; it outlives it
  on one disk.
- **What would change my mind:** `fixture.py` able to stop the
  migration at a named mark (`--shape <version>`), which needs
  nothing kept; or the fixture's remote somewhere that is not
  `tmp/`; or the design saying the second machine never tests.
- **Epistemic status:** `tmp/` from `.gitignore` read today;
  SOL.0800's "runs only the steps that are missing" as written.

## What is strong
- The fixture carried by its own script in the old shape, migrated
  by the migration it tests, and the tests on it alone: the first
  release's gates are now real tests on a bed the forge's own door
  can reach, and no real project is touched before its turn.
- The second machine's acts at every release and the origins of the
  engine's threads as a round close the two seams the morning's
  review opened, with nothing invented beyond what was asked.
- The dependency line at the head of the file is the right kind of
  sentence: it says what needs what, and it is short enough to be
  wrong visibly, which CHL.0570 exercises.

## Questions I cannot answer from the documents
- Does "the shape one release back tolerated" in SOL.0680 mean that
  at the first release the ledger script reads the hand-kept
  `ledger.md`'s tables as its archive where `ledger.archive.md` is
  absent? CHL.0560 is smaller if yes, and the overwrite remains.
- Were the two sides of the collision of 2026-10-17 (the double
  FND.1690) the principal's two machines, or another account? And
  does the second machine write into projects today, or only pull?
  CHL.0570 stands or falls on the answer.
- Who writes `fixture: true` into the fixture's project file: does
  `fixture.py` put it into the old-shape ledger header for step B0 to
  carry over, or does the script add it after the migration? Neither
  is said; the map is the only reader, so it is small.
- Are the sittings of the stretch meant to be consecutive days?
  CHL.0590 weighs nothing if they are.
