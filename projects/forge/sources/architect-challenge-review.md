origin: pasted into the conversation by the principal on 2026-10-17; written in Czech by a model in a session outside the forge as a review of the challenge `challenges/2026-10-17-challenge-architect.md` (the persona architect on the solution design 0.18), with a verdict and a way of mending for each challenge; translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-17

# Review of the architect's challenge of the solution design 0.18

## CHL.0250, the local merge as raw git: accept

The design made the local merge the only path (the server does not
merge with the driver) and at the same time left it as the one step
outside the forge. For an analyst who does not type git it really is
a dealbreaker. REJ.0170 rejected a fixed working branch with an
automatic switch, not the merge of a named branch on the user's
word; `/save` already rebases and `/pull` pulls on the word, so
POS.1490 holds with a command `/merge <branch>` too: the script runs
`git merge` on main (the driver is in the global config, so the
records merge by themselves), and the remaining conflicts, which by
definition are the legitimate ones (the same item changed twice), go
through a walkthrough: one conflict, one question, the principal
gives the verdict, Claude writes the chosen wording (the conflict
markers are text in Markdown, which Claude may edit), the script
stages and commits on confirmation. None of this is a merge on the
forge's judgement; it is elicitation over a conflict, exactly the
mechanism the forge has. The same may later be taken over by `/save`
in place of today's abort of the rebase (a thread, not now). A change
of POS.1490 and of the text "merging is git's, by hand": the merge is
git's, through the forge's door, on the word.

## CHL.0260, the reservation by push to a protected main: accept, and it goes further

GitLab protects the default branch by default (push and merge for
maintainers only). The consequence is wider than the reservation:
the whole path "a local merge into main, `/save`" needs a push to
main, so the role of a maintainer. For a company project that means
a model the design has not yet said: one integrator (a maintainer,
typically the principal) and N contributors. A contributor: a branch,
`/save` (the push of the branch). The integrator: `/merge <branch>`
locally with the driver, `/save` on main. The MR on the server is for
reading, as the brief says. This model is consistent with the forge
being built around the principal, and it removes the need for
plumbing entirely:

- A block per author, assigned once by hand in `ids.md` by the
  integrator through an ordinary round and `/save`; the contributor
  has it after `/pull`. No network at the reflection, works offline
  and on a protected main. Two concurrent hand assignments are
  settled by the driver (immutable lines, union) and by the overlap
  check.
- With five digits, give an author a thousand per prefix (a hundred
  IDs at a step of ten), not a hundred; a hundred would run out at
  fifteen threads, and every exhaustion waits on the integrator.
- A further simplification: everyone writes from his own block, the
  integrator too. "The next free number" is then "the next in my
  block", the rule "neither used nor reserved" falls away and with
  it the competition for a hundred between main and the branches;
  groups by hundreds hold inside a block. A project without `ids.md`
  (one author, the engine) runs as today.

My plumbing was the right answer to a badly put question; the
challenger's version is simpler and survives GitLab's default.

## CHL.0270, the migration and branches in flight: accept, with one correction

The reflow (A2) on main gives every open branch a conflict on every
changed paragraph, since every line changes. `/migrate` must know it:
before `--apply` it looks at the origin (`for-each-ref`), lists the
branches not merged into main and refuses until they are landed or
knowingly given up. For a branch that must not die there is a tool:
the conversion is deterministic and idempotent, so the branch's
commits can be rewritten with the conversion applied to every tree
(each commit expressed anew over the converted parent) and then
rebased onto the converted main; the conflicts shrink to the real
ones. That is a bounded feature, but not for the first release: a
TBC owned by Claude, until then "land first" holds. Forks of the
engine with their own changes the same, a known limit.

A correction of the challenger: `--undo` does restore the reflow; the
script stages nothing, so `git restore` from the index restores every
changed tracked file; the manifest covers only the created files and
the removals from the index. That is how it must be written; today it
is not there.

And the test of the driver under rebase before the second release,
not after: a stub driver of five lines on a throwaway clone verifies
`rebase.backend merge`, the reversal of ours and renormalize within
an hour. The same for `ours` under rebase before the first release,
since CHL.0290 rests on it.

## CHL.0280, the ledger script as a single point of failure: accept

Three things. (a) An unparsable file is a finding, not a crash: the
row drops aloud (the ledger's header says "unparsed: file, line"),
the light check is red, but `/save` commits and pushes on; prime
directive 5 says checks inform and the save is what does not lose
work. Write it into SOL.0680 and into `/save`. (b) The tolerance of
the shape one release back, as the driver has it. (c) Before the
first release, run the parser dry over all of today's projects and
diff the output against the hand-kept ledger: it is at once the test
of the parser over the irregular records the challenger names and
the list of what the migration cannot derive. Without it the first
release rests on a script that never ran over real files.

## CHL.0290, `ours` in the rebase at a release: accept, cheap

`/release` (and likewise `/document` and `/publish`, everything that
makes files of way 3 on main) refuses when the repository is behind
or diverged; `forge-status --remote` is at hand. Otherwise the fresh
README silently loses to the colleague's older one and the tag of a
major marks a wrong state. One condition in three skills.

## CHL.0300, the migration as a condition of writing against POS.0820: accept as a fix of the intent

The design is right in substance: after B the engine cannot write
the old shape, and keeping two modes of writing would be madness.
But the intent must say what the design does: the upgrade of the
engine is on the user's word (`forge-pull`), and after an upgrade
that changes the shape, a project of the old shape is for reading,
not for writing, until the user migrates it. Narrow POS.0820 with the
reason, not leave the narrowing silent in the design.

## What follows for the write

Intent: POS.1490 (the merge through the forge's door on the word),
POS.1730 (blocks per author, from one's own block, no plumbing, no
rule "neither used nor reserved"), POS.1710 (the integrator and the
contributors as a stated model; a release only when current),
POS.0820 (the old shape for reading). REJ: the plumbing onto
origin/main (rejected: the protected main, the network at the
reflection). Design: a new part `/merge` with the walkthrough of
conflicts; SOL.0790 rewritten; SOL.0800 with the check of branches
and a TBC on the conversion of a branch; SOL.0680 and `/save` on the
failure of the script; SOL.0530 on the refusal at "behind"; the TBC
of the tests widened by two preliminary tests (the stub driver, the
dry run of the parser) before the releases, not after; the TBC on
the protected main closes with it.

On the challenger's questions: GitLab with its default protection is
thus the normal environment, not an edge case, and the model of an
integrator plus contributors is the answer that admits it.
