origin: pasted into the conversation by the principal on 2026-10-17; written in Czech by a model in a session outside the forge as a review of the second challenge of the architect, `challenges/2026-10-17-challenge-architect-2.md` (on the solution design 0.19), with a verdict and a way of mending for each challenge and answers to the challenger's questions; translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-17

# Review of the architect's second challenge, of the solution design 0.19

## CHL.0310, one direction and one source: accept whole

All three cases are real and have one door:

- Both directions. `/merge <branch>` on main merges the branch into
  main; `/merge main` on a branch merges main into the branch. The
  driver's ordering rule is written exactly for the second direction,
  test 3 requires it, and a long branch without taking main in as it
  goes ends in a week of conflicts in one walkthrough, as the
  challenger says.
- The source. main is always `origin/main` after a fetch (a
  contributor's local main may be stale); the branch is local where
  it exists locally (a worktree, a project without an origin), else
  `origin/<branch>` after a fetch. My sentence "the contributor's
  branch lives on the origin" decided the one-person case silently
  and wrongly.
- The end of a branch. `forge-branch --done <name>`: after the merge
  it removes the worktree and deletes the branch; git itself refuses
  to delete an unmerged branch, which is the right safeguard.

## CHL.0320, the order of the releases: accept, with one adjustment

The argument holds: the reflow is the one irreversible change that
reaches every line of every project and every fork, and its
justification for merging is reasoning, not observation (nobody saw
a false conflict of neighbouring positions; the gain of the reflow
is diff and blame, not merging). The driver removes three of the
five evidenced collisions and costs no reflow. An adjustment against
the challenger: C1 (threads as files) need not go with A2. Cutting
`threads.md` into files changes no lines, is reversible and keeps
"one parser of threads" with B. Hence: the first release B0, A, B,
C1, `ours`, the registration, the unique names of reports (three
lines, they belong where the branches and `/merge` are), M without
"land first"; right after it the driver, `/merge`, the worktree; then
F1, F2; A2 as a release of its own at a moment when nothing is in
flight, with a `.git-blame-ignore-revs` holding the hash of the
conversion (git's `blame.ignoreRevsFile`, which GitHub honours), the
mitigation of blame the design lacks. The principal's verdict "A2
first" was made without this evidence; a new decision citing
CHL.0320 is exactly what a DEC is for.

## CHL.0330, the conflict resolution without a record, the shape of a driver conflict: accept

- The record. The verdict on every conflict is written by the
  walkthrough of `/merge` as a `changed` record into the artefact's
  history: the subject the item, the reason "merge of <branch>: the
  chosen wording and why", `Was` the other one. The version token
  `+`, since the record belongs to the landing that is under way (see
  CHL.0360).
- The driver's output. Always the standard markers, because git's
  detection of a conflict, rerere and zdiff3 all rest on them: for an
  immutable unit the record from the base stays in the file, followed
  by a conflict block with both variants; for a mutable block the
  markers around both versions of the block. The walkthrough reads
  the markers as for way 1; only the default verdict differs: for an
  immutable unit "restore the base" (a breach), with the option of
  taking a variant where it was a legitimate correction of a typo in
  a reason.

## CHL.0340, rerere is not load-bearing: accept, with its consequence for `/save`

The challenger is right: rerere keys on a concrete automerge, and
five commits replayed one by one do not give the one the walkthrough
resolved. My "load-bearing" was untrue. The right closing of the
window has two parts:

- `/merge` ends with the push, as `/release` does. A refused push
  (someone pushed meanwhile) is not resolved by a rebase but by a
  merge of `origin/main` into the local main, with the driver and a
  walkthrough where needed, and the push again. A merge commit is
  never rebased.
- From that follows a rule for forge-save: where it finds a merge
  commit among the commits to push, it pulls by merge
  (`--no-rebase`), not by rebase; a rebase would drop it and replay
  the branch's commits one by one. The rebase stays for one's own
  linear commits, as it was always meant. rerere stays on as a
  convenience, not as a mechanism.

## CHL.0350, the engine's attributes: accept, trivial

The engine's root README, RELEASE-NOTES, CONTRIBUTING and `docs/**`
lie outside the prefix. The engine gets a list of its own, not the
template with a prefix. It is not a formality: the engine is branched
and `/render readme` on a branch is allowed.

## CHL.0360, the place of the landing and the deadlock: accept and simplify

The refusal "land first" was mine and deadlocks exactly as the
challenger writes. A simpler rule, which removes the deadlock and the
question "which version" alike: on main, while a history carries
unlanded `+` records, every new record of that history carries `+`
too and lands with them; the landing is the first act of forge-save
(before add), so after the check whose settlement writes `closed`
records with `+`. A round on main in that window joins the landing
(one version per landing, as on a branch). The attribution holds:
all `+` records precede the following `landed`. And the report "N
unlanded records" is not a finding inside `/save`; it is the state
`/save` is just landing.

## Answers to the challenger's questions

- Two windows on a project without an origin: yes, to be expected; a
  project "not under git" and a project without a remote are
  properties in the doctrine, not defects. Hence the local branch in
  `/merge`.
- A false conflict of neighbours: not observed, derived from the
  measurement of wrapping. It confirms CHL.0320.
- The handle: a gap. The author of a block must be an exact key, not
  a free line of a role. `/setup` writes `author: <handle>` into
  `CLAUDE.local.md` (the same string that goes into the author column
  of a history), `ids.md` keys on it, and with an existing `ids.md`
  and no matching block the write step refuses the allocation with
  the fix; it never falls back to the sequence, which would reopen
  the hole of POS.1110.
- A branch of the engine and `/render`: yes, allowed; CHL.0350 is a
  defect.
- Blame: whoever uses it, the ignore-revs file costs one line.

## Where it lands

Intent: POS.1760 (both directions, the source, the end of a branch,
the push as the last step, a merge instead of a rebase on refusal,
the record of the verdict), POS.1630 and POS.1660 ("join the
landing" instead of "land first", the landing as the first act of
the save), POS.1690 (the engine's attributes a list of its own;
forge-save pulling a merge commit by merge), POS.1730 (the handle as
the key, the refusal), POS.1750 and THR.0620 (the new order, A2 on
its own, blame ignore-revs), a DEC on the reversal of the verdict
"A2 first". Design: SOL.0820, 0530, 0730, 0750 (the output of a
conflict), 0790, 0800 (without "land first", without TBC.0080 as a
block of the first release), 0740 (rerere a convenience), a new part
`forge-branch --done`.
