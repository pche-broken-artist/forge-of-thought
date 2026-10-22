---
id: THR.0520
concerns: intent, solution-design
origin: the principal
status: closed
---

The intent carries the solution, and a layer for the
solution is missing. Priority, to be worked at once. The
principal's word of 2026-10-03, a fault of the design from the
start that neither he nor Claude saw: the debate whether the forge
project lacks an assignment asked the wrong question. The intent is
the statement of what is wanted and why, and nothing else; how the
things of the intent are realised belongs in a document of its own,
the solution design. His picture of the chain: a brief, lighter
than the briefs written so far, a list of topics with links to
research and the verification of ideas, and then at once the
intent; after the intent an assignment or a BRD where the matter is
large and handed over, or straight a solution design, where the
solution lives. What he expects of it: the work stops going task by
task, since over an intent that is only the statement of what is
wanted he can ask Claude for a proposal of the whole solution and
work over that. Nothing is decided beyond this stance.
Evidence.
`research/2026-10-01-what-of-the-intent-belongs-to-an-assignment.md`
classified every item of the intent at 4.41: about a quarter stance
and reason, more than a half how the engine shall behave or be
built, the rest the way to it, since moved to the history. The note
called the larger part "directive to the realiser", asked whether
an assignment should carry it, and answered no. No rule forbids an
intent to solve, while POS.0210 forbids it to an assignment.
CLAUDE.md names `40-solution-design.md` as a later layer below the
assignment and the BRD, the recipients' work; a principal who is
his own realiser, where the solution follows the intent directly,
is not foreseen.
Walked through 2026-10-03, ten matters, every verdict the
principal's; what was decided stands in POS.1390 (the boundary),
POS.1400 (where the solution design stands, the ledger's
`terminal:` withdrawn with it, POS.0160), POS.1410 (how an artefact
is composed), POS.1420 (what the solution design is made of),
POS.0900 (a change runs the whole chain and may come from below)
and POS.0110 (the lighter brief). Research of the same day:
`research/2026-10-03-how-a-solution-design-is-built.md`.
The plan, agreed 2026-10-03. A command of its own for an
elicitation falls away, the elicitation being part of an artefact's
definition.

| Step | What | State |
|---|---|---|
| 1 | Decide what the solution design is | done 2026-10-03, intent 4.52 |
| 2 | Prepare the forge: the names of the artefacts leave the engine so that artefacts are read from disk; CLAUDE.md brought to the positions of step 1 | done 2026-10-03, intent 4.53, handed over to Claude and judged by the principal |
| 3 | Add the solution design by hand, its definition and its template, as the trial of step 2 | done 2026-10-04, intent 4.54, handed over to Claude and judged by the principal |
| 4 | Write the solution design of the forge project and move the solution out of its intent | done 2026-10-04, intent 4.56 and solution design 0.1, handed over to Claude, verified three times by an isolated agent and once mechanically, the findings settled with the principal |
| 5 | Draw from that the command that adds a new kind of artefact | done 2026-10-04, intent 4.57 and solution design 0.2: `/new-artefact` (POS.1430, SOL.0170), handed over to Claude and judged by the principal; not yet run |
| 6 | Make the BRD by that command, its first trial; with it the challenger persona of a business analyst | paused 2026-10-04 by the principal, to be done later |

What steps 2 and 3 did is in the records of the operating layer at
4.53 and 4.54. Left on purpose: the `terminal:` line in the ledgers
of the other projects, harmless and deleted at their next write;
the threads file of the other projects, renamed to `threads.md`
and its threads marked at their next write; the README, which is
re-rendered at the next release. Decided with step 2, the
principal's word of 2026-10-03: the one list of the forge's
artefacts is the listing of `.claude/skills/forge/states/`,
CLAUDE.md describes none of them, and the table of artefacts in the
README is rendered from the definitions; settled in step 3, the
head of a definition carries nothing new for that, the table being
rendered from `description`, Target and Inputs, and the readme
recipe is iterated for it before the next release. The
locking of a brief is withdrawn (POS.0110, POS.0920, POS.0320).
Step 4 is a
one-off: the solution is moved as it stands in the intent, and
where a reason can no longer be told from the intent or its
history, it is said to be unknown and none is invented; after it
the forge works as every project does, the solution after the
intent.
Open: whether a plan is a document of its own, taken up after the
first solution design exists; how it is told that a layer has
fallen behind its intent, since an artefact names no version of the
intent it was brought to; which check keeps a solution design true
against what realises it; whether work handed over is reflected
back before it is written, the rule of 2026-09-27 standing until
decided; a technical specification as a layer below the solution
design, which POS.1400 names since 4.55 and which is added by the
command of step 5 when a project first needs it, the forge itself
not being buildable from its artefacts until then; a second pass
of the intent, position by position with the principal, for the
solution that step 4 left in it because cutting it needs new
wording (POS.0060, POS.0120, POS.0410, POS.0420, POS.0440,
POS.0540, POS.0710, POS.0730, POS.0840, POS.0920, POS.0930,
POS.0940, POS.0960, POS.1000, POS.1020, POS.1040, POS.1070,
POS.1100, POS.1110, POS.1310, POS.1340, POS.1380). With them three
places the renders of 2026-10-04 showed to be behind the
positions: POS.0600 and POS.0620, which still speak of the
assignment as where version 1 ends, and the last sentence of
POS.0970, by which the implementation of a library is still to
come; the same sentence of the Essence was mended at 4.58. How step 4 ran: the working files, the three
reports and the mechanical check lie in the engine's
`tmp/solution-design/`, outside git; the design is a proposal the
principal has not read whole. The sections "A technical clean-up"
and "The shape of the whole" of the brief `next-gen` rest on this
thread. Opened 2026-10-03.

Closed 2026-10-22: steps 1 to 5 done between 2026-10-03 and
2026-10-04, step 6 living in the brief brd; what the thread left on
purpose was overtaken by the migration of 2026-10-19; its open
questions have their homes: a plan is a work product (POS.1520), the
check that keeps the design true is TBC.0020, the second pass of the
22 positions waits in the brief next-gen, a technical specification
comes by /new-artefact when a project needs it, work handed over is
POS.1410's; how a layer is told to have fallen behind its intent
joins TBC.0020.

<!-- A thread (POS.1680): one open matter of the intent, in
threads/THR.NNNN.md; not an artefact: no title, no version, no
history of its own. Freely rewritten while open, the header too,
on a branch as well; never moved, renamed or deleted, the one
exception the renumbering at an ID clash (POS.0220). Closing is
`status: closed` and a `closed` record in the intent's history
saying when and by what; a closed thread is immutable and is the
archive, so it carries no `Was`; what returns is a new thread
citing the old one. The list of threads is the ledger's. -->
