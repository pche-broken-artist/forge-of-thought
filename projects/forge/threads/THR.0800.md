---
id: THR.0800
concerns: brd
origin: Claude's synthesis
status: closed
---

The BRD's template has one open question stand twice, and the
ledger reports it as an ID defined twice. `templates/brd.md` puts a
TBC under its group where a rule is not known ("a TBC under its
group") and again under Open questions with its owner and whether
it blocks estimation, both with the same ID; `forge-ledger.py`
then reports "TBC.NNNN defined twice" in its Reports section. Found
in the trial of the user-stories layer on a small project, where
the BRD carried TBC.0010 and TBC.0020 in both places. What the
thread must settle: whether the group carries the question and Open
questions only cites it, or the reverse, or the ledger learns that
a TBC in Open questions is a citation; and the same for the
assignment and the solution design, where TBC lives too. To take
after the trial, with the position of the user-stories layer.
Opened 2026-11-02.

Closed 2026-11-08: a TBC is defined once, in Open questions, with
its owner and whether it blocks estimation; a BR or an NFR whose rule
is not known cites it in brackets, as it cites its parent. The slot
under the group taken out of `templates/brd.md`, the rule written into
the Requirement style of `states/brd.md`; the ledger's report of an ID
defined twice stands as it is. The assignment and the solution design
had one place each already (intent 6.20).

<!-- A thread (POS.1680), one file per thread in threads/; the header
is its state: what it concerns, where it came from, whether it is
open. The rules of a thread, its life and its closing:
`.claude/skills/forge/states/intent.md`, Threads and files. -->
