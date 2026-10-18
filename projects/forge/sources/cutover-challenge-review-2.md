origin: pasted into the conversation by the principal on 2026-10-18 in two pieces; written in the conversation's language by a model in a session outside the forge as a review of the architect's second challenge of the cutover plan, `challenges/2026-10-18-challenge-architect.md` (on `work/collaboration-cutover.md`), with a verdict and a way of mending for each challenge and answers to the challenger's questions, the second piece three corrections of the first; translated into English at registration on the principal's word, the wording kept as close as the translation allows
date: 2026-10-18

# Review of the architect's second challenge of the cutover plan

## CHL.0510, two branches of one author take the same ID: accept, the mend in the intent

Blocks per handle settle the collision between authors; two branches
of the same handle read the same block and both take its next
number. Two windows of one person are, at the same time, the case
the brief opens with and the one the second release builds. After
the merge the driver leaves the two records side by side, the script
reports a duplicate, and "never renumbered" means two POS.1780 for
good. R2.12 even expects it as a pass.

The remedy is cheap, because both trees are one repository: the next
free number is read over every local branch, not from the working
tree alone. `forge_repos` gives `git for-each-ref refs/heads` and the
highest number of the prefix in the histories and the thread files of
every branch (`git grep` over the refs, no checkout); the allocation
takes the maximum over the branches plus the step. No network, no
block, and it covers both cases of one author: two worktrees and
sequential branches. Two clones of one author (the second machine) it
does not cover; that is the same case as two authors, so a block; a
known limit. To write: POS.1730 (the rule of the free number over the
local branches, blocks per handle only between clones and authors),
POS.1100 citing both, R2.12's first test no longer tolerating the
collision, a new step in the second release (the allocation over the
branches in the walkthrough and in `forge_repos`). The trigger of the
fourth release stays a second author, but a second clone of the same
author is a trigger too; widen it.

To the challenger's question: if agentic-platform has a second
account with another handle (the brief speaks of research "from
another account"), the trigger has fired already and that project
gets its blocks at the migration. And the remedy of a duplicate,
which the design says nowhere: the younger record takes a new number
(a `changed` record with the reason "ID clash at merge", `Was` the
old number, the citations corrected in the branch that landed
second). It is the one exception to "never renumbered" and must be
written in POS.0220 as such.

## CHL.0500, the throwaway clones: accept, and simplify

`forge-clone` derives the name from the last segment of the URL and
refuses an existing directory; `tmp/fixture.git` gives `fixture`,
the second clone fails, and the real projects cannot be cloned at
all. And the guard `fixture: true` does not exist before the
migration. The simplest remedy is the last one the challenger
offers: the tests on the fixture only, the real projects without
clones. The ledger script writes a gitignored file and stages
nothing, so a dry run over the real projects in place is safe; the
migration has its `--apply` and `--undo` test on the fixture and over
the real projects a dry run only (R1.13 has that already). What
remains is the fixture: `forge-clone <url> <name>` (an optional
target, one line in R1.10, the fixture script uses it), and the guard
by name, not by a field: a bare save skips `projects/fixture-*`;
`fixture: true` in `project.md` stays for the map, but the sweep must
not depend on a file that does not exist before the migration.

## CHL.0520, the fixture dies with the first release: accept

The fixture reads the templates of the day; after R1.04 it can no
longer make the old shape. Let `fixture.py` carry the old shape as
its own content (not from the templates), and let the bare remote
get a tag `shape-5.x`, so that "a fixture of the shape of release
N-1" is a command; after every release with a migration the script
adds the next tag. With that the `--apply`/`--undo` test, "one
release back" and the conversion step (R5.04) have a lasting bed;
without it R2.02 and SOL.0680 are untested claims.

## CHL.0530, three mechanics of the third release: accept

The hash for `.git-blame-ignore-revs` does not exist before the
commit; `/migrate` in the conversion step runs the save itself and
writes the hash by a second save. An exception to "the migration
commits nothing", written down.

A sixth mark for the conversion (say `wrapping: sentences` in
`project.md`, written by the conversion), otherwise the refusal of
the old shape does not fire and the light rule reports every wrapped
paragraph.

`blame.ignoreRevsFile` into the Action of the release notes for every
machine, or directly as a registration of `/setup` beside the driver.

## CHL.0540, the second machine: accept

It is the first "foreign" clone the forge will have, and the upgrade
path from the view of a clone that does not migrate is nowhere. One
Action line per release: "on every other machine: `forge-pull` of
the engine, `/setup`, `/pull` of every project; `/migrate` does not
run there". And the freeze of the second machine during the
building is a habit; the mechanism is cheap: `forge-pull` of the
engine refuses when origin/main has no release tag higher than the
local one, except on the principal's word. Optional; today DEC.0230
covers it.

## CHL.0550, the origins of the engine's threads: accept

My note on CHL.0480 had two halves and the plan took one. A row
after R1.23: a walkthrough over the printed guesses of the origin of
the 35 threads, closed by the saved thread files; the engine's are
exactly the ones where the default "the principal" is most often
wrong.

## Into the write

POS.1730, POS.1100, POS.0220 (the exception of renumbering at a
clash), DEC.0220 (the trigger widened by a second clone), SOL.0790
and SOL.0830 (the fixture with its own old shape and the tags, the
guard by name, clones of the fixture only), SOL.0800 (the sixth
mark, the second save for the hash); the plan: R1.10 with the clone
target, R1.13 and R1.09 without clones of the real projects, a new
row after R1.23, a new step of the allocation over the branches in
the second release, R2.12 without a tolerated collision, R5.04 and
R5.08 by 0530, the Action for the second machine in every release
step.

## Second piece: three corrections

The allocation over the branches must see "another block" too,
otherwise the renumbering at a clash makes the next clash. POS.0220
gives the younger record "a new number", but if at that moment it is
allocated from the same block (or sequence) both branches drew from,
the new number may clash with a third branch not yet landed. Right:
the new number is taken by the allocation over the local branches
(the new POS.1730), which sees the third branch. One citation in
POS.0220.

The renumbering meets a thread too. A thread has its file name from
its ID; "the second takes a new number" for a THR means renaming
`threads/THR.1780.md`, which POS.1680 forbids ("never moved, renamed
or deleted"). Either an exception beside the exception (the renaming
at a clash, with a `changed` record), or for a thread the younger
stays as a new thread under a new name and the old one is closed by
a citation. I recommend the first, it is the same exception; write
it into POS.0220 and POS.1680.

R2.12 and a DEC with the same ID. Let the test "two branches each
opening a thread, no duplicate after the merge" cover all three
kinds of records (THR, DEC, POS): for a DEC it is the block of
`decisions.md`, for a POS an item of the intent; the mechanism of the
allocation is the same, but the parsing of the highest number over
the refs is per file. One sentence in the closing.
