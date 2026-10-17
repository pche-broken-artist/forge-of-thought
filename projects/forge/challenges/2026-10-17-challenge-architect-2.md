---
date: 2026-10-17
project: forge
target: solution-design v0.19
reviewed: projects/forge/40-solution-design.md v0.19 (whole); projects/forge/40-solution-design.history.md (the records of 0.19); projects/forge/00-brief-collaboration.md v0.8 (whole); projects/forge/10-intent.md v5.16 (POS.0960, POS.1560 to POS.1770, POS.0400 to POS.0450, POS.0550, POS.1100, POS.1110, POS.1200, POS.0570, POS.0590); projects/forge/threads.md (THR.0090, THR.0530, THR.0620, THR.0650, THR.0690, THR.0700); projects/forge/ledger.md (Documents and Challenges tables); projects/forge/challenges/2026-10-17-challenge-architect.md (CHL.0250 to CHL.0300, all accepted); projects/forge/sources/architect-challenge-review.md; projects/forge/sources/architect-challenge-review-2.md; projects/forge/research/2026-10-17-mergeable-shared-records-in-git.md; projects/forge/research/2026-10-17-git-merge-drivers-and-their-limits.md; templates/history.md; .claude/skills/forge/states/solution-design.md; .claude/skills/save/SKILL.md; scripts/forge-save.py (whole); scripts/forge-pull.py and scripts/forge-branch.py (help headers); CLAUDE.md on disk (Versioning & status, "the log is the single primary"; the rest from the session's copy); web: git-scm.com, git-rebase and git-rerere documentation
reviewer: challenger persona architect (solution architect, isolated context)
---

# Peer review (architect) — 2026-10-17

## Overall read

0.19 takes the six challenges of the morning and mends each where it
was aimed: the merge has a door, the IDs need no push, the migration
looks for branches in flight, the ledger script degrades aloud, the
release refuses when behind. The design is now coherent on its own
terms, and it is a design of a mechanism that has not run. What is
left is of a different kind: not a wrong choice but a seam between
parts that were each mended alone. The merge door opens one way and
reads one source; the first release still carries the one-way
conversion and realises the least of the two merges the brief gives
as evidence; and two or three places where one part assumes of
another something the other does not say. None of it is fatal; two
of them will be the first thing a second person meets.

## Challenges

### CHL.0310 — The merge has one direction and one source: nothing brings main into a branch, and a local branch cannot be merged at all
- **Severity:** major
- **Challenge:** `/merge <branch>` runs on main only and merges
  `origin/<branch>` (SOL.0820, POS.1760). `forge-pull` is
  "fast-forward only" of the branch checked out from its own
  counterpart on the origin, and refuses a diverged repository
  (`scripts/forge-pull.py`, help); `forge-branch` creates and
  switches and says "merging ... stay[s] with git" (its help). So
  three cases the design itself describes have no door. First, main
  into a long branch: the driver's ordering rule is worked out for
  "a merge of main into a long branch (theirs has it ...)"
  (POS.1670), the ledger script reports a branch as `v<base>+N`
  against a main that moves, and the third test of THR.0650 is "a
  long branch pulling main into itself after a landing on main";
  the command that would do the pulling does not exist, and the
  test will be run with the raw git the design denies the user.
  Second, a branch that was never pushed: two windows of one person
  on one project are two working trees of local branches
  (SOL.0770); on a project without an origin, which `forge-save`
  supports ("commit kept locally"), there is no `origin/<branch>`
  to fetch, and on a project with one the merge of a local branch
  takes a round trip through the server for no reason. The second
  review's addition, "the contributor's branch exists on the
  origin, not locally", was written for the N-contributor case and
  silently decided the one-person case the other way. Third, the
  end of a branch: `forge-branch` creates a branch and its
  worktree, `/merge` merges it, and nothing removes the worktree
  at `projects/<slug>@<branch>/` or deletes the branch, so every
  finished branch leaves a tree the bare `forge-save` still visits
  and the map still lists. The choice never made: `/merge` as the
  one door for a merge in either direction, of a local or a
  remote branch, with its end.
- **Why it matters:** The brief's second case, one person in two
  windows, is the common one in a single-principal forge and it is
  the one that fails here: a week on `rework` while main moves
  daily ends with the whole week's conflicts in one walkthrough,
  because the branch could not take main in between. And the
  contributor on a protected host, the model of POS.1770, cannot
  refresh his branch from main through the forge either: his only
  path is switch to main, pull, make a new branch, which the design
  does not say.
- **What would change my mind:** The design stating that a branch
  never takes main and lives short, with the "switch, pull, new
  branch" path named as the way to refresh; or `/merge` taking a
  branch into main and main into the branch checked out, a local
  branch where one exists, and offering the removal of the worktree
  and the branch once merged.
- **Epistemic status:** the mechanism from the design and the two
  scripts' help headers; my judgement on the weight.

### CHL.0320 — The first release is the one-way door and realises the least of the evidenced pain; the two unevidenced remedies ride in it, the evidenced one waits behind it
- **Severity:** major
- **Challenge:** The brief's evidence is two merges of
  agentic-platform in which the files on both sides were the
  ledger, the histories, the decisions, the index of sources and
  the regenerated README and release notes (brief, What prompted
  it). After the first release (THR.0620; SOL.0680, SOL.0730) the
  ledger is gone and the renders are `ours`; the histories, the
  decisions and the indexes still merge as text, and by the
  design's own sentence two people who both ran a round "will
  always have a conflicting" merge in every history both touched,
  now met in `/merge`'s walkthrough, where the only right answer
  for an append-tail conflict is "both", written by Claude into a
  history file by hand. The part that removes those three of the
  five evidenced collisions is the driver, placed in the second
  release (SOL.0750). What the first release carries instead is the
  conversion to one sentence per line and the threads as files,
  whose justification is a conflict the evidence does not contain
  ("two branches editing two neighbouring positions", POS.1580;
  threads.md is not among the files of either merge), and it is
  exactly those two that make the first release a one-way door:
  the demand that every branch of every clone be landed first
  (SOL.0800), the tool of TBC.0080 wanted, the engine's forks cut
  off, and `--undo` good only until the first `/save`. The brief's
  reason for A2 before C1 is that the threads be cut already in
  sentences; that couples A2 to C1, not either of them to the
  ledger, so the pair can move together to a release of its own at
  a moment nothing is in flight, and the first release would then
  be B0, A, B, `ours`, the driver and `/merge`, with no "land
  first" demand. Two prices of the reflow are not stated: `git
  blame` on every prose file of every project points at the
  conversion commit from then on, while POS.1580 claims blame by
  sentence as a benefit (the mitigation, a `blame.ignoreRevsFile`
  with the conversion's hash, exists in git and on GitHub, from
  memory, not verified today, and is nowhere in the design); and
  the unique report names (SOL.0810), three lines in three skills,
  sit in the second release while branches and `/merge` are in the
  first, so two branches whose light check each found something on
  one day both file `YYYY-MM-DD-check-light.md`, an add/add
  conflict in an immutable file at the first `/merge`.
- **Why it matters:** The release with the largest blast radius is
  also the one that gives a second person the least, and the step
  that would give the most is behind it. If the first release is
  the one that goes wrong on a colleague's clone, there is no
  second.
- **What would change my mind:** An observed false conflict between
  two neighbouring positions in any project's history; or a reason,
  recorded, why the driver cannot precede the reflow; or the order
  restated with the reflow and the threads as a release of their
  own and the unique names moved into the first.
- **Epistemic status:** the evidence from the brief; the order from
  THR.0620 and the "Not built" marks; the blame mechanism from
  memory, flagged; the weight my judgement.

### CHL.0330 — The resolution of a conflict at `/merge` is the one content change without a record, and a driver's conflict has no shape the walkthrough can read
- **Severity:** minor
- **Challenge:** `/merge` ends with Claude writing the chosen
  wording into the file and the script staging and committing, "the
  message naming the branch" (SOL.0820). CLAUDE.md, Versioning &
  status, says the log is the single primary and the commit message
  a derivation, and that the record is written in the same step as
  the change. After a legitimate conflict, the same position changed
  on both sides, the merged history holds the branch's `changed`
  record with its `Was` and main's `changed` record with its `Was`,
  the item holds one of the two wordings or a third, and nothing
  says which or why; `/history` of that item shows two records as
  if both held. The ledger script's "merged unseen, review" catches
  two authors in one landing merged silently; a conflict seen and
  settled leaves less trace than one never seen. Beside it, the
  driver's conflict: for a way-2 file a conflict is by construction
  a changed or deleted immutable unit (SOL.0750), which the forge
  calls a breach, so the right question is never "which wording"
  but "restore the base", an edit of a history by Claude; and what
  the driver leaves in `%A` at a conflict, markers around records,
  both records, or the base, is unspecified, while the walkthrough
  assumes "the markers being text" of way 1.
- **Why it matters:** The forge's whole claim to a traceable
  history fails at the one moment two people's thinking actually
  met. Small today, because legitimate conflicts are rare by
  design; it is the kind of hole that is found in an audit, not in
  use.
- **What would change my mind:** The design saying what record the
  resolution leaves, in whose history and with what version token,
  or saying that the merge commit is the record and amending the
  rule that says it is not; and the driver's conflict output stated
  for each of its three cases.
- **Epistemic status:** the rule from CLAUDE.md on disk; the gap
  from SOL.0820 and SOL.0750 as written; my judgement.

### CHL.0340 — rerere is called load-bearing and git says the resolution must be re-applied; the guard that would hold is one the design already has
- **Severity:** minor
- **Challenge:** SOL.0740 sets `rerere.enabled true` as "the
  load-bearing mechanism of `/merge`", so that a resolution recorded
  at the merge "resolves the same hunks by itself at the replay"
  when `/save`'s `pull --rebase` drops the merge commit (SOL.0820).
  git's documentation says the rebase will "simply drop merge
  commits ... and put the rebased commits into a single, linear
  branch", and even with `--rebase-merges` "any resolved merge
  conflicts ... in these merge commits will have to be
  resolved/re-applied manually"; rerere reuses a resolution "as
  long as the recorded resolution is still applicable", matched on
  the conflicted automerge. A branch of five rounds is five commits;
  replayed one by one onto a moved main they produce five
  automerges, none of which is the one automerge the walkthrough
  resolved, so the match holds for a one-commit branch and is a
  hope for the rest (the keying of rerere on the conflict hunks is
  from memory, not in the page I read). The window is small, since
  `/merge` refuses when behind and only the integrator can push to
  a protected main, and that is the point: the guard that holds is
  the refusal, not rerere, and the simplest closing of the window
  is `/merge` ending with the save itself, as `/release` does, so
  that no commit of anyone can land between the merge and its push.
- **Why it matters:** A mechanism named load-bearing that bears in
  one case is the kind of thing that is trusted exactly once, on
  the day it matters.
- **What would change my mind:** The stub-driver test of TBC.0050
  extended by one case, a three-commit branch merged, resolved, and
  rebased over a new commit on main, showing rerere resolving it;
  or `/merge` pushing as its last step.
- **Epistemic status:** the rebase behaviour from git's
  documentation, verified today; rerere's keying from memory,
  flagged; the weight my judgement.

### CHL.0350 — The engine's `.gitattributes` with the prefix `projects/forge/` misses every way-3 file the engine actually has
- **Severity:** minor
- **Challenge:** SOL.0730 gives the engine "the same patterns with
  the prefix `projects/forge/`", so `merge=ours` lands on
  `projects/forge/README.md`, `projects/forge/renders/**`,
  `projects/forge/docs/**`. The engine's own README and release
  notes are rendered to the repository root (SOL.0410, `output:`),
  CONTRIBUTING.md to the root (SOL.0450), the documentation to
  `docs/` of the engine root (SOL.0460) and the player files to
  `docs/videos/` (SOL.0660). Of those, only `projects/forge/renders/`
  is under the prefix. The files CHL.0290 was about, the ones a
  release regenerates, get the text merge on the engine: a branch of
  the engine on which `/render readme` ran, which POS.1690 allows,
  conflicts with main's README at `/merge`; the refusal when behind
  covers the rebase of `/save` and not the merge.
- **Why it matters:** The engine is the one repository the
  principal branches today (`forge-branch forge work-release` is
  the script's own example), so this is the attribute file that
  will be exercised first.
- **What would change my mind:** The engine's attribute file stated
  as its own list, the root files and `docs/**` among it, rather
  than the template with a prefix.
- **Epistemic status:** the paths from the design's own items; no
  judgement needed.

### CHL.0360 — The landing's place in the save is stated three ways, and one of them deadlocks with "land first"
- **Severity:** minor
- **Challenge:** SOL.0530 says the save lands the `+` records
  "first"; SOL.0760 says `forge-save` calls `forge-land` "before
  committing", that is inside the script; the save skill runs the
  light check and settles its report before the script runs
  (`.claude/skills/save/SKILL.md`, steps 1a and 4). On main after a
  `/merge`, the intent's history holds `+` records; the light check
  calls the ledger script, which reports "N unlanded records" among
  what it finds (SOL.0680), and settling any finding writes a
  `closed` record into the history of the artefact or of the intent
  (SOL.0690) through the write step, which refuses "a document with
  unlanded `+` records ('land first: `/save`')" (SOL.0760), from
  inside `/save`. If a state record does not go through the write
  step, the design does not say so, and POS.1630 then has it carry
  "the current version", which on main between a merge and its
  landing is the base's number written after records that will
  compute to the next one. Either way the three sentences do not
  agree on when the landing happens relative to the check, and the
  order decides whether the first `/save` after the first `/merge`
  runs or stops. The third release, so there is time; but the
  seam is between two parts mended today in separate items.
- **Why it matters:** The first integrator's `/save` after the first
  `/merge` is the moment the whole path is tried; a stop there is
  back at the terminal CHL.0250 took away.
- **What would change my mind:** One sentence saying the landing is
  the first act of `/save` on main, before the check, and that a
  state record is exempt from "land first" or is written after the
  landing.
- **Epistemic status:** the three texts as written; my judgement
  that the write step is what writes a `closed` record, which the
  design leaves open.

## What is strong
- The six mends of the morning are each in the right place: the
  roles of POS.1770 remove the push to main from everyone but the
  integrator, and the blocks per author follow from it without a
  further mechanism.
- `/merge` as elicitation over a conflict is the right reading of
  POS.1490: the forge decides nothing, the user does, and the
  conflict markers are the one place a conflict can be read by
  someone who does not type git.
- The ledger script degrading aloud, with `/save` saving on, keeps
  prime directive 5 true at the one place it was about to be
  false.
- The tests moved before the releases, and the migration refusing
  with branches in flight: the design now says what it does not
  know and when it will.

## Questions I cannot answer from the documents
- Is a two-window run on a project without an origin expected, or
  will every project that gets a second window have a remote? The
  weight of CHL.0310's second case hangs on it.
- Has a false conflict between two neighbouring positions ever been
  seen in any merge, or is the reflow justified by reasoning alone?
- The handle: SOL.0790 keys an author's block on "the handle the
  instance gives its principal", a free line of a gitignored file
  whose template asks for a role ("the CTO"). What does the
  allocation do in a project that has `ids.md` for an author whose
  handle matches no block, or matches it in a different spelling:
  refuse the write, or fall back to the sequence and reopen the
  hole? Nothing says.
- Will a branch of the engine ever run `/render` or `/document`, or
  is the engine branched only for scripts and skills? CHL.0350 is a
  defect in the first case and a formality in the second.
- Is `git blame` used by anyone on these files? If not, CHL.0320's
  blame point is a price nobody pays.
