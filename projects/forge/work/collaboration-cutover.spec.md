---
version: 0.2
date: 2026-10-17
status: draft
last_change: 0.2 (2026-10-17): the specification worked handed over: the task, the inputs, the method of steps per release, three assumptions, one open point, the making; the file made in the same round; renamed from operating-layer-plan to collaboration-cutover on the principal's word.
project: forge
file: work/collaboration-cutover.md
---

# Collaboration cutover — Work specification

<!-- A work product (CLAUDE.md, Document kinds; the command
.claude/skills/work/SKILL.md): this file holds the way and the why,
the file beside it the content. Versioning & status (its history
companion, templates/history.md); its language: prime directive 6. -->

## Task
A working plan of the building of the operating layer for the brief
`collaboration`: the five releases of DEC.0210, each broken into steps
in the order of building, every step naming the part of the design it
realises, the files it touches, what closes it and its state, so that
Claude follows it step by step on the principal's word and the principal
tunes the order and the cut. For the principal and Claude. Dead after
the fifth release and the migration of every project; it stays as it
lies.

## Inputs
- 40-solution-design.md: SOL.0670 to SOL.0820, each with its `Where` and its release mark; SOL.0300 and SOL.0330; TBC.0050, TBC.0060, TBC.0080
- 10-intent.md: POS.1560 to POS.1770, POS.1120, POS.1140
- threads.md: THR.0620 (row 9), THR.0650, THR.0690, THR.0700
- decisions.md: DEC.0210
- 00-brief-collaboration.md, section M (the steps of a migration run)

## Method
One section per release. Within a release the steps in the order of
dependency: the shape first (templates, CLAUDE.md), since a script
cannot read a template that does not exist; the mechanism second
(scripts); the use third (skills, agents, definitions), since a skill
cannot call a script that does not exist; then the tests the release
needs before it (TBC.0050); then the release's run: the checks,
`/document`, `/release`, the marks of the design turned over (SOL.0530),
the migration where the release has one. A step carries an id (R1.01),
what is done, the part of the design it realises, the files, what closes
it (a test, a check, a run) and a state: todo, doing, done, dropped. The
state is the only thing that changes after the file is made.

## Assumptions
- **ASM.0010** The releases are built one at a time in the order of DEC.0210, each released before the next starts.
- **ASM.0020** A release is a round on the operating layer; the intent and the design change only where building shows they must, intent-first (CLAUDE.md, Working methods).
- **ASM.0030** The engine's own project migrates first, on this clone, within the first release; every other project after it, each on one clone, by the principal.

## Open
- **TBC.0010** (owner: principal) Whether `single-source-of-truth` runs at every release of the plan or at the first and the last only. Closed by: his word.

## Making
The file `work/collaboration-cutover.md`, English, Markdown: a heading
per release with the parts it carries, a table of its steps with the
columns id, step, part, files, closes with, state; no reasons, which
stay here and in the design. Made once from this specification by
Claude; from then on worked by hand, the states changed as the work
proceeds, the ledger row `by hand` on the principal's word.
