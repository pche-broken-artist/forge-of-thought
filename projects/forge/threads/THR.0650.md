---
id: THR.0650
concerns: solution-design
origin: Claude's synthesis
status: closed
---

The new output of `forge-pull.py`
(before, after, the commits between) and the states `behind` and
`diverged` of `remote_state` are untested, since no repository has
been behind its origin; a test on a throwaway clone the principal
makes by hand, raw git being denied to Claude (SOL.0510). Carried
in the ledger without an ID from intent 5.1 until 5.4 (FND.1490).
Deferred 2026-10-11; opened 2026-10-11.

The tests of the brief `collaboration` (POS.1750), 2026-10-17, four on
the fixture, never on a clone of a real project (DEC.0240): branches
on different artefacts (a record to a different history, a thread, a
decision and a position opened on each branch with their IDs
allocated over the local branches and no duplicate after the merge,
a research, a render, one branch a round of state only; the merge
without conflict, the state-only round raising no version); branches over the same artefact
changing different positions with the headers untouched (the test of
the history driver); a long branch pulling main into itself after a
landing, its `+` records staying unlanded; the same position changed
on both sides remaining a conflict exactly there.

Three tests before the releases, added 2026-10-17 on CHL.0270 and
CHL.0280: `ours` under rebase on a throwaway clone before the first
release, since the refusal of a release behind rests on the reversal;
a stub driver of a few lines under rebase before the second, to verify
`rebase.backend merge`, the reversal of ours and renormalize; and the
ledger script run dry over every project of today and diffed against
the hand-kept ledger before the first, the test of the parser over the
irregular records and the list of what the migration cannot derive.

The closings defined 2026-10-17 (CHL.0410): the ledger script's dry
run over a real project writes to `tmp/` through `--out`, never over
a tracked ledger, and passes when its output differs from the
hand-kept ledger only in three named classes, Waiting made from the
rule, lines the parser names as unrecognised and origins it guessed,
the old ledger's own tables read as the archive for what the records
do not yet carry, everything else equal (CHL.0560);
the conversion's proof on a screenplay is the player's events file
equal before and after, never the video; a test before a release that
is red stops the release, back to the design, the TBC open.

The test of `ours` under rebase run 2026-10-19 on the fixture (R1.02 of the cutover plan): a copy of the clone as a second clone of the same remote, each side appending a different line to `README.md` (`merge=ours` by `templates/gitattributes`), the second `forge-save` rebasing onto the first's push. Green: the rebase ran without a conflict, the replayed commit was dropped as "patch contents already upstream", the README kept the remote's text, the push went through and the clone stands clean and up to date; `ours` under rebase is upstream, as the refusal of a release behind its origin assumes (SOL.0530). The two tests before the second release and the four of the brief stand as they are.

Closed 2026-10-22: forge-pull's new output and the state behind ran
on the principal's second machine and work (his word of 2026-10-22);
of the tests before the releases, ours under rebase and the dry run
of the ledger script ran green on 2026-10-19; the results of the
tests still to come, the stub driver and the four of the brief
before the second release, are recorded in the cutover plan, in the
cell that closes each row, as the two of the first release were.

<!-- A thread (POS.1680): one open matter of the intent, in
threads/THR.NNNN.md; not an artefact: no title, no version, no
history of its own. Freely rewritten while open, the header too,
on a branch as well; never moved, renamed or deleted, the one
exception the renumbering at an ID clash (POS.0220). Closing is
`status: closed` and a `closed` record in the intent's history
saying when and by what; a closed thread is immutable and is the
archive, so it carries no `Was`; what returns is a new thread
citing the old one. The list of threads is the ledger's. -->
