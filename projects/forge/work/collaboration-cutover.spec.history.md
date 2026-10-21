---
project: forge
document: work/collaboration-cutover.spec.md
---

# History — work/collaboration-cutover.spec.md

<!-- The history of a versioned document: CLAUDE.md, Versioning &
status. One record per change, one line each, appended at the end,
never rewritten:
- <date> | <version> | <author> | <subject> | <kind> | <reason> | Action: <what the user must do> | Was: <wording that ceased to hold>
Kinds: created | changed | closed | removed | approved. The subject
is an ID, several IDs where the whole line holds for each, or a
place without an ID: a section, the file, or in the forge's own
project the operating layer. Reason is left out on
`created`; `Action` and `Was` only where the record has them, `Was`
always last, paragraphs in it divided by `<br>`; a thread that
closes gets a `closed` record, no `Was` (the rules of a thread:
`.claude/skills/forge/states/intent.md`, Threads and files). At the birth of a
document, one record of the file and one naming every item born
with it. Lines are not wrapped.
A record of state only carries the current version and does not
raise it (POS.1630). Its shapes: the mining of a brief, in the
intent's history with the brief's file as subject,
`00-brief-<name>.md | changed | mined: pending | partial | mined |
dropped, <note>`; a finding or a challenge settled, `FND.NNNN |
closed | <what fixed it>`, in the history of the artefact whose
version settled it, or of the intent where no version did or the
check was of the engine, resolved for a finding, accepted for a
challenge; a work product's state in its specification's history:
the making's record `<file> | changed | state: current; made <date>
from <the inputs with their versions>`, a write of the specification
after a making `<file> | changed | state: stale`, the principal's
word `<file> | changed | state: by hand`.
`rejected`, `parked` and `obsolete` are a decision's Verdict
(templates/decisions.md), never a record here (POS.1610). -->

- 2026-10-17 | 0.1 | PCHe | work/collaboration-cutover.spec.md | created
- 2026-10-17 | 0.2 | PCHe | work/collaboration-cutover.spec.md | changed | Worked handed over on the principal's word: the task, the inputs, the method (steps per release in the order shape, mechanism, use, tests, run), ASM.0010 to ASM.0030, TBC.0010, the making; the file made in the same round, 55 steps over five releases.
- 2026-10-17 | 0.2 | PCHe | ASM.0010, ASM.0020, ASM.0030, TBC.0010 | created
- 2026-10-17 | 0.2 | PCHe | work/collaboration-cutover.spec.md | changed | Renamed from operating-layer-plan on the principal's word: the name says what the change of the operating layer is about, since the next such plan would otherwise carry the same name; the three files, the headers and the ledger row follow. | Was: work/operating-layer-plan.spec.md, work/operating-layer-plan.md
- 2026-10-18 | 0.3 | PCHe | Task, Inputs | changed | Brought up to the plan and the decisions since 0.2: four releases of DEC.0220, the first on main in one stretch (DEC.0230); SOL.0830, TBC.0080, the three decisions and the two reviews the file was worked against added to the inputs. | Was: the five releases of DEC.0210 … Dead after the fifth release<br>Inputs without DEC.0220, DEC.0230, SOL.0830, TBC.0080 and the two sources.
- 2026-10-18 | 0.3 | PCHe | ASM.0040 | created
- 2026-10-18 | 0.3 | PCHe | TBC.0010 | closed | The principal's word of 2026-10-18: single-source-of-truth runs after the first and after the third release, `check engine` between; the check is expensive by design and its question moves in R1 (the skills stop writing the ledger) and R3 (one sentence per line), not in R2 and R4. | Action: R5.06 of the file gains `single-source-of-truth` among its checks. | Was: - **TBC.0010** (owner: principal) Whether `single-source-of-truth` runs at every release of the plan or at the first and the last only. Closed by: his word.
- 2026-10-18 | 0.4 | PCHe | Inputs | changed | The architect's second challenge of the plan settled on the principal's word of 2026-10-18 (`sources/cutover-challenge-review-2.md`): DEC.0240 and the review added; the plan's rows R1.00, R1.09, R1.10, R1.13, R1.24, R2.11, R2.12, R5.04, R5.07, R4.06 and the heading of the fourth release changed by hand, R1.29 and R2.13 born.
- 2026-10-18 | 0.4 | PCHe | TBC.0020 | created
- 2026-10-18 | 0.4 | PCHe | Inputs | changed | The architect's second challenge of the plan (`challenges/2026-10-18-challenge-architect-2.md`, CHL.0560 to CHL.0610) settled in a walkthrough on the principal's word of 2026-10-18, all six accepted, CHL.0570 as modified: the plan's rows changed by hand, a Preparation section before the stretch with R1.01, R1.18, R1.08, R1.12, R1.14, R1.28, R1.00 moved into it and R0.01, R0.02 born, R2.14 born, R1.26, R1.10, R1.09, R1.02, R2.01, R1.24, R5.07, the heading of release 4 and the intro changed; the inputs unchanged, the report filed in the ledger.
- 2026-10-18 | 0.4 | PCHe | Task, Inputs | changed | The cut of DEC.0250 on the principal's word of 2026-10-18: the preparation and the first release now, the rest deferred as rows under one heading, R0.02 dropped, R1.00 the fixture by hand; DEC.0250 and THR.0710 among the inputs. | Was: the four releases of DEC.0220, the first on `main` in one stretch (DEC.0230), each broken into steps
- 2026-10-18 | 0.5 | PCHe | Inputs | changed | FND.1760 of the light check of 2026-10-18 (reviews/2026-10-18-check-light-2.md), the first catch of the rule of POS.1520 at 5.21: SOL.0530, SOL.0150, SOL.0160, SOL.0420, SOL.0460, SOL.0500 and POS.0220, each with the step it serves, added. | Was: - 40-solution-design.md: SOL.0670 to SOL.0830, each with its `Where` and its release mark; SOL.0300 and SOL.0330; TBC.0050, TBC.0060, TBC.0080<br>- 10-intent.md: POS.1560 to POS.1770, POS.1120, POS.1140
- 2026-10-18 | 0.6 | PCHe | Method, Inputs | changed | The principal's word of 2026-10-18 (DEC.0260): the release of the preparation dropped as cost without use, `/document` and the renders to be made again right after the stretch; the preparation ships by its saves on main and ends with the tag `pre-r1`, the first step of the stretch; R0.01 dropped in the plan, DEC.0260 among the inputs. | Was: the preparation an ordinary release before the stretch (DEC.0240, CHL.0590), its run `/document`, `/release` as R0.01.
- 2026-10-19 | 0.7 | PCHe | TBC.0090 | changed | Renumbered from TBC.0020: the number was already the design's (40-solution-design.md, since 2026-10-04) and IDs are global; the younger item takes the next free number (POS.0220), the clash reported by the ledger script's first run (R1.09). | Was: TBC.0020
- 2026-10-17 | 0.7 | PCHe | work/collaboration-cutover.md | changed | state: by hand; made 2026-10-17 from 40-solution-design.md v0.24 (SOL.0670 to SOL.0830, SOL.0300, SOL.0330, SOL.0530, SOL.0150, SOL.0160, SOL.0420, SOL.0460, SOL.0500, TBC.0050, TBC.0060, TBC.0080), 10-intent.md v5.22 (POS.1560 to POS.1770, POS.1120, POS.1140, POS.0220), threads.md (THR.0620, THR.0650, THR.0690, THR.0700, THR.0710), decisions.md (DEC.0210 to DEC.0260), 00-brief-collaboration.md v0.8 (M), sources/cutover-plan-critique.md, sources/cutover-challenge-review.md, sources/cutover-challenge-review-2.md
