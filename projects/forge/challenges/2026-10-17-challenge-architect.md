---
date: 2026-10-17
project: forge
target: solution-design v0.18
reviewed: projects/forge/40-solution-design.md v0.18 (whole); projects/forge/40-solution-design.history.md (records of 0.1 to 0.18); projects/forge/00-brief-collaboration.md v0.8; projects/forge/10-intent.md v5.15 (POS.0060, POS.0120, POS.0220, POS.0300, POS.0310, POS.0320, POS.0330, POS.0550, POS.0820, POS.0930, POS.0940, POS.0960, POS.1080, POS.1100, POS.1110, POS.1200, POS.1400, POS.1420, POS.1490, POS.1510, POS.1570 to POS.1750, REJ.0150 to REJ.0170, REJ.0270 to REJ.0310, the closing section); projects/forge/threads.md (2026-10-17, THR.0090, THR.0520, THR.0530, THR.0600, THR.0620, THR.0640, THR.0650, THR.0690 among the rest); projects/forge/decisions.md (the headings DEC.0010 to DEC.0200; DEC.0190 and DEC.0200 in full); projects/forge/ledger.md (Challenges table, Waiting on principal); projects/forge/sources/00-INDEX.md; projects/forge/sources/merge-design-review.md; projects/forge/research/2026-10-17-mergeable-shared-records-in-git.md; projects/forge/research/2026-10-17-git-merge-drivers-and-their-limits.md; projects/forge/challenges/2026-10-09-challenge-cto.md (CHL.0200 to CHL.0240); .claude/skills/forge/states/solution-design.md; .claude/skills/walkthrough/SKILL.md (From verdicts to the write); scripts/forge-save.py (whole); CLAUDE.md as delivered in context, not re-read from disk, no challenge rests on its wording; web: docs.gitlab.com (default branch protection), git 2.26 release notes (rebase backend)
reviewer: challenger persona architect (solution architect, isolated context)
---

# Peer review (architect) — 2026-10-17

## Overall read

The design pass of 0.18 turns the brief `collaboration` into fifteen
parts that make every file of a project mergeable by one of four
ways, with the ledger out of git, a record driver, the version as a
boundary and IDs reserved through main. The frame is right and the
hard thinking has been done where it is hardest, in the driver and
the boundary. What the design does not look at is the act the whole
thing exists for: the merge itself, which it has now pushed off the
server and back into a terminal the forge does not open; and the
ground it will land on, a company host whose default forbids the one
push the reservation needs, branches and forks in flight when the
migration reflows every line, and a save that depends on a parser
with no degraded form. The four releases are sequenced for doctrine,
not for what a colleague meets first.

## Challenges

### CHL.0250 — The merge is the one step left outside the forge, and the design has just taken the server merge away
- **Severity:** major; a dealbreaker for the brief's own aim if the
  collaborators are the analysts the project's research names, which
  I cannot see from here
- **Challenge:** The path of collaboration as SOL.0730 and POS.1690
  state it is: a branch, `/save` (a rebase with the driver), a local
  merge into main, `/save`. The third step is raw git typed by the
  user in a terminal: `forge-branch` creates and switches
  (SOL.0510), `forge-land` appends `landed` records (SOL.0760),
  nothing of the forge merges a branch into main, and Claude is
  denied git by the wall (SOL.0520). Before this design that was
  tolerable because the merge request existed as the other door;
  the design itself now says the server merges without the driver,
  so "two people who both append to any history or to the decisions
  will always have a conflicting merge request" (SOL.0730) — that is
  every pair of branches that both ran any round — and declares the
  merge request "a tool for reading". So the one act in which the
  driver's value materialises, the local merge, is the one act the
  forge gives no door to, and the fallback printed by `forge-save`
  at a conflicting rebase is `git pull --rebase`, resolve, `add`,
  `rebase --continue` (SOL.0780), which today's script already ends
  with "ask Claude for help" (`scripts/forge-save.py`, line 97)
  while Claude is the one party that cannot. POS.1490 is not the
  obstacle: it forbids a merge on the forge's own judgement, and
  `/pull` already fast-forwards on the user's word; `/save` already
  runs `git pull --rebase`, which is a merge in all but name. A
  merge of a named branch into main on the user's word — fetch,
  merge with the driver, stop and report a conflict exactly as
  `/save` does, then `forge-land` — is the choice that was never
  made; the design's Choice fields weigh a worktree against a second
  clone and a driver against `union`, never a door for the merge
  against none.
- **Why it matters:** The brief's aim is that work of several people
  "stops being a pain". With this design the pain moves from the
  ledger, where a developer could at least resolve it, to a hand
  merge with a custom driver, `rebase.backend` and `rerere` in play,
  which a non-developer cannot do and the forge will not. The first
  colleague on a branch reaches the end of the designed path and
  finds a terminal.
- **What would change my mind:** Either a statement in the design,
  where the collaborator reads it, that branches and merges are for
  users who type git, and the brief's audience narrowed to match; or
  one more script or option of `forge-branch` that performs the
  local merge into main on the user's word, with the same abort and
  report as the rebase of `/save`.
- **Epistemic status:** the mechanism from the design, the research
  on drivers (F6, hosting platforms merge without drivers) and
  `forge-save.py`; the audience from the threshold-of-entry research
  cited in CHL.0210; the weight my judgement.

### CHL.0260 — The reservation of IDs pushes to main, and main is protected by default on the host the evidence came from
- **Severity:** major
- **Challenge:** SOL.0790 reserves a block by a commit pushed
  straight to `origin/main` by plumbing, from a branch, at the
  reflection before every write that brings a new item; TBC.0070
  records that this does not work where main is protected and marks
  it "Blocks realisation: no", "a decision when a project meets it".
  On GitLab the default branch is protected by default at the level
  "Fully protected": developers cannot push to it, maintainers can
  (verified today at docs.gitlab.com, Default branch). The brief's
  evidence is the company project `agentic-platform`, where several
  people will branch; unless every collaborator is a maintainer of
  every project, the fourth release's mechanism refuses on its first
  real target, and the retry loop ("a refused push means fetch and
  try again") retries a refusal that never changes. Beside the
  limit, the mechanism has a price the item does not state: one
  commit on main per prefix per branch, bypassing `/save`'s identity
  check and the light check; a local main left behind at every
  reservation, which the map then reports and the reflection reads
  as "pull first"; and the network at every round that opens a
  thread. The alternative was set up to lose: REJ.0270 rejects a
  block from a hash of the branch name by the birthday paradox,
  which is the arithmetic of random blocks. A block per author,
  assigned once by hand in `ids.md` on main through an ordinary
  `/save` — the author's handle is already what every record
  carries — needs no push, no compare-and-swap and no network at the
  reflection, works on protected main and offline, spends a hundred
  per prefix per person instead of per branch, and leaves the rare
  collision to the ledger script's duplicate report that exists
  anyway. For the two or three people the brief calls the case, it
  is the least that would do, and it was never weighed.
- **Why it matters:** The fourth release closes "the last hole of
  POS.1110" and is the only one of the four that needs the server to
  behave in a particular way; the one host the forge has evidence
  from behaves the other way by default. A known limit that the
  default triggers is not a limit, it is the case.
- **What would change my mind:** A fact, as a FCT, that the
  company's GitLab lets every intended collaborator push to main on
  the forge's projects; or a count of expected branches per person
  high enough that a block per author runs out before a block per
  branch would.
- **Epistemic status:** the GitLab default verified today at the
  vendor's documentation; the per-author alternative my judgement;
  the retry behaviour read from SOL.0790 as written.

### CHL.0270 — The migration reflows every line of prose and sees no branch, fork or clone in flight; the release that carries it goes out before the test
- **Severity:** major
- **Challenge:** SOL.0800 runs A2 at the end of one run: every
  artefact, thread, decision, skill, agent, template, `CLAUDE.md`
  and render rewritten to one sentence per line, proven by pandoc's
  syntax tree. The script refuses an unclean repository, one behind
  its origin, or one not on main; it does not look for any other
  branch, local or on the origin, nor at a fork. A branch made
  before the reflow cannot be merged or rebased afterwards by any
  driver the design has: the text driver sees every paragraph the
  branch touched changed on both sides, the reflow on one and the
  work on the other, so the conflict lands exactly on the branch's
  work, item by item, in two different wrappings. For the engine
  the same holds for every divergent clone: the colleague's fork
  from which the BRD layer comes (`projects/lib-allwyn/sources/
  fork-brd/`, a fork at intent 2.8), a user's local changes that
  THR.0300 wants to protect, the second clone on the machine that
  SOL.0740 tolerates by a release. `--undo` works from a manifest of
  what the script created and took out of the index; the reflow is
  neither, so the one-way door of the migration is the step the
  manifest cannot undo, reversible only by raw git. And the order:
  TBC.0050 runs the four tests "after the first and the second
  release", while the research on drivers says the driver under
  rebase is "a mechanical inference ... to be tested on a throwaway
  clone before the forge relies on it" (F1), and the first release
  reaches every clone by fast-forward with the migration as its
  Action required. What fails is found in a colleague's clone after
  his projects are migrated.
- **Why it matters:** The migration is the largest conflict the
  project will ever see, made by the forge itself, at the moment the
  design is meant to make conflicts rare. Whoever has a branch open
  that week loses the clean path for it; whoever runs a fork of the
  engine loses the ability to take anything from main again.
- **What would change my mind:** The migration listing, before
  `--apply`, every branch of the repository and of its origin that
  is not merged into main, and refusing or asking; the reflow run as
  a step of its own at a moment nothing is in flight, not bundled
  into the one run; and the four tests run on a clone of a real
  project before the first release goes out, not after.
- **Epistemic status:** the three-way merge mechanism, consensus;
  the fork a fact of the sources index; the sequencing read from
  TBC.0050 and the research; the weight my judgement.

### CHL.0280 — The ledger script is a single point of failure for the map and the save, strict by rule, with no degraded form and no word on what the save does when it fails
- **Severity:** major
- **Challenge:** SOL.0680 makes one script the reader of eleven
  kinds of document, called by every `/forge` map, `/ledger`,
  `/end`, `check-light` at every `/save`, `check-project` and the
  README recipe, and it "exits with an error over an unparsable
  file". The files it parses are written by the model, one record a
  line, under a shape that has changed at each release since
  2026-09-29 and changes again four times in this design (`+`,
  `landed`, the `closed` state record, the Verdict line of a
  decision). The design's own history shows the shapes that reach
  the file: a record with "As before." for its reason
  (`40-solution-design.history.md`, the second SOL.0150 record of
  0.8) and an elision "[...]" inside a `Was` (the SOL.0650 record of
  0.17). Today such a row costs one wrong ledger line; under
  SOL.0680 one malformed record in any file halts the map and the
  light check, and because a history is append-only, the repair is
  an edit of an immutable line, a breach by the forge's own rule.
  SOL.0530 says `/save` runs the light check; neither it nor
  SOL.0680 says what the save does when the check cannot build the
  ledger: refuse, and a typo blocks every save of the project until
  someone breaks immutability; proceed, and "never silently drops a
  row" is moot at the one moment it matters. The strictness is right
  for the driver, where a bad merge must not exit zero; a read-time
  projection has a cheaper safe form that was not weighed: build
  what parses, name what did not, let only the check turn it into a
  finding. The driver gets "the shape one release back tolerated";
  the ledger script gets no such sentence.
- **Why it matters:** The map runs at every prompt and the check at
  every save; this script becomes the thing that must work for the
  forge to be usable at all, and it is the part the design itself
  calls "the most complex script of the engine". A mechanism that
  turns a model's typo into a blocked save, repairable only by a
  breach, will be repaired by breaches.
- **What would change my mind:** The design stating what `/save`
  does on a ledger error and why; and one measured run of a
  prototype parser over the histories, decisions and indexes of the
  five projects as they stand, with the count of records it cannot
  read.
- **Epistemic status:** my judgement; the evidence lines from the
  files named.

### CHL.0290 — `merge=ours` turns round in the rebase of `/save`, so a release made on a clone that is behind tags the other person's README silently
- **Severity:** major
- **Challenge:** In a rebase "ours" is the upstream. `/release`
  renders the README and the release notes and then runs `/save`:
  commit, `pull --rebase`, push (SOL.0530, `forge-save.py` line 95).
  With `merge=ours` on `README.md`, `RELEASE-NOTES.md`, `renders/**`
  and `docs/**` (SOL.0730), a clone that is behind by a colleague's
  release and releases without pulling will, at the rebase, have its
  fresh renders replaced by the colleague's older ones with no
  conflict and no word, and push a release commit, and at a major a
  tag, whose README belongs to the previous intent. The outside
  review named the reversal (`sources/merge-design-review.md`, part
  one, point 2) and the brief answered that after B there is nothing
  to regenerate into git; the renders are in git and are made at
  every release, so the answer covers the ledger and not them. The
  design declares two clones on main unsupported and sequential; a
  declared-unsupported case that fails silently with a wrong tagged
  release is not a boundary, it is a defect with a sign on it. The
  map's "behind: pull first" is a recommendation; `/release` has
  `forge-status --remote` at hand and does not refuse.
- **Why it matters:** This is the evidenced case in its exact shape:
  two people, one clone behind. The old failure was a visible
  conflict in the ledger; the new one is a clean push of the wrong
  files, which the ledger script may mark stale afterwards if anyone
  looks.
- **What would change my mind:** `/release` refusing when the
  repository is behind its origin, which costs one line; or `ours`
  taken off the renders so that the conflict stays the alarm, the
  release's own renders being the thing to keep.
- **Epistemic status:** the reversal of ours and theirs in a rebase,
  consensus (git documentation; the review says the same); the order
  of the release read from SOL.0530 and the script; the weight my
  judgement.

### CHL.0300 — The design makes the migration a precondition of every write, and the layer above says a migration is a per-project decision never assumed
- **Severity:** minor
- **Challenge:** SOL.0800 has the map, `check-project` and every
  writing skill say "shape before the migration, run `/migrate`" on
  a project of the old shape and refuse to write, for libraries too.
  POS.0820 says an artefact remains valid under the conventions it
  was written to, that nonconformance of a finished or dormant
  project is a fact to report and never a defect to chase, and that
  bringing a project to newer conventions is an explicit decision
  made per project and never assumed. After this design the decision
  is still the principal's, but it can no longer be "no": the engine
  is one for all projects, and a user with one migrated and one
  unmigrated project can write into only one of them. The ledger
  script already reads "the archive for every item without a record
  of the new shape", so reading the old shape is in reach; what is
  missing is one release of writing it, the tolerance the driver is
  given and the writing skills are not. Nothing in the design says
  this narrowing of POS.0820 was seen; the intent was not changed
  for it.
- **Why it matters:** A seam between the layers: a position the
  design silently narrows will be found by a user on a dormant
  project, not by a check.
- **What would change my mind:** POS.0820 narrowed in the intent to
  say that a release which changes the shape of files makes the
  migration a condition of writing; or the writing skills tolerating
  the old shape for one release, as the driver does.
- **Epistemic status:** my judgement; the two texts as they stand.

## What is strong
- The four ways as a frame, and the ledger out of git: the one file
  present at both evidenced merges stops existing as a thing to
  merge. That is the right first cut and the research supports it.
- The version as a boundary record instead of a rewrite of records:
  the only design in the three outside reviews that keeps
  append-only without an exception, and the ordering rule for the
  three operations is genuinely worked out.
- The driver that conflicts on a changed or deleted immutable unit
  and exits non-zero over a damaged file, against `union`: the
  failure the field's reports share is designed out.
- Threads as files, which shrinks the driver to line and block
  units; and "Not built; the N-th release" on every new part with a
  rule for turning it over, so that the design cannot quietly claim
  what does not exist.

## Questions I cannot answer from the documents
- Who are the first collaborators on `agentic-platform`, and do they
  type git? CHL.0250 is a footnote for developers and a dealbreaker
  for analysts.
- Is the company host GitLab, and are the intended collaborators
  maintainers of the forge's projects there, or developers?
- Do any branches exist today across the five projects, and does the
  colleague's fork of the engine still live and expect to take from
  main?
- Has any parser been run over today's histories and decisions to
  see how many records the strict reading would reject?
- What does `/save` do today when `check-light` fails to run at all,
  as against reporting findings?
