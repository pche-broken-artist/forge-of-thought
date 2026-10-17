origin: pasted into the conversation by the principal on 2026-10-17; written in Czech by a model in a session outside the forge as a review of the architect's challenge of the cutover plan, `challenges/2026-10-17-challenge-architect-3.md` (on `work/collaboration-cutover.md`), with a verdict and a way of mending for each challenge and answers to the challenger's questions; translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-17

# Review of the architect's challenge of the cutover plan

## CHL.0370, where the first release is built: accept, a branch

The engine's main is the upgrade channel and the repository is
public; 27 saved intermediate states on origin/main (templates
without `date` while the write step writes it; skills without the
ledger while the map calls the script over the old shape; the refusal
of unmigrated projects) is a state nobody should see, even if today
only the principal's second machine pulls. A branch has two prices
and both are cheap: the engine has one working tree until R2.07, but
the principal's git is his (POS.1490 says so explicitly), so `git
worktree add ../forge-of-thought@r1 r1` by hand, once, puts the
building into a second tree and main stays for the daily work on
the projects with the finished engine; and the merge of the branch
into main at the end is the last manual git the brief removes, and
the release notes of the first release say so. The estimate: the
ledger script 1 to 2 sittings, the migration 1 to 2, the 26 skills
1, the templates and CLAUDE.md 1, the fixture and the tests 1, the
release 1; six to eight sittings, not three days, so the question is
not moot. A cut into two releases (the shape; the mechanism) would
not split the atomic core anyway, the ledger script with the skills
and the migration; keep one release, on a branch, with this weight
in THR.0620.

## CHL.0380, the fixture as a project: accept, with one correction

`forge_repos` knows only the engine root and `projects/<slug>`, and
the four tests are rounds of the forge by slug; so the fixture must
be `projects/fixture-a/` and `projects/fixture-b/`, two clones of one
bare remote in `tmp/fixture.git`. The correction: the bare remote
and the first commit need not be the principal's hand; the scripts
are the door to git, forge-clone and forge-branch call git, so
`scripts/fixture.py` (my earlier point) founds it itself,
deterministically, on both machines. The price "a bare `/save`
visits the fixture" is removed by a flag `fixture: true` in
`project.md`, which a bare save skips.

## CHL.0390, the engine's project locked: accept, and my unapplied remark

The version of the plan I read still had R1.22 before R1.23,
although I pointed it out last time; the challenger found it again
and goes further. Of the two windows take the first: migrate
`projects/forge` right after R1.13 and R1.09, then at once R1.17 and
R1.16, so that the window "the skills write a gitignored ledger, the
definitions do not yet write records" lasts one step; the remaining
fifteen steps then exercise the ledger script, threads as files and
the state records on a real project with every save of the engine.
The refusal of the old shape (R1.19) as the last code step before
R1.24; R1.22 dropped, `/release` runs the checks itself.

## CHL.0400, the interval between the second and the third release: accept, and merge the releases

Without F1 a round on a branch raises the header as on main, every
`/merge` collides on the `version` line with no rule who wins, and
above all: the records of both rounds carry the same version number,
and the third release, which reads "a record with a version is its
own boundary", makes of them two versions with one number that are
never renumbered. The second release would thus invite to branches
and permanently damage the histories of everyone who accepts. The
answer is not a sentence in the release notes but R3.01 to R3.04
into the second release: the driver, `/merge`, the worktree and the
version as a boundary are one release, "collaboration"; the stopgap
in R2.06 falls away. DEC.0210 thereby changes from five releases to
four; a new DEC citing CHL.0400.

## CHL.0410, three closings without a truth value: accept

- R1.09: the diff is non-empty by definition (Waiting from the rule,
  unrecognised lines, guessed origins); the pass is "a difference
  only in these three named classes, everything else equal".
- R5.01: an `.mp4` is never byte-identical; the proof is the player's
  events file (md2video writes it) equal before and after, plus the
  syntax tree.
- R1.02 and R2.01: the word for red: "stop, back to the design
  (SOL.0530 for `ours`, SOL.0740 for the backend), TBC.0050 open, the
  release does not run".

## CHL.0420, the way back: accept

Write the truth: the return to a tag is the principal's hand through
git (reset and force push, or revert), on a protected main a
maintainer only, and always the engine and all projects together,
since the engine after R1.24 refuses the old shape. The tag per
project immediately before its `/migrate` (in R1.25 and R5.07), the
engine's tag in R1.26.

## CHL.0430, the fourth release without a user: accept

The ID blocks change nothing until a second author writes into a
project, and the conversion does not depend on them. Let the plan
mark what is a dependency (1 → 2+3 → the rest) and what is a
decision; the trigger of the fourth release is "a second author on a
project", and A2 may go before it. The order then: 1, 2 (with F1),
A2, the blocks on the trigger.

## Answers to the questions

- The branch: see CHL.0370; today only the principal's second machine
  pulls the engine, but it is public.
- The fixture: driven by forge commands, the four tests are rounds;
  CHL.0380 holds.
- A second author: intended (the forge for analysts), the date
  unknown; hence a trigger, not an order.
- Sittings: six to eight for the first release, an estimate,
  unverified.
