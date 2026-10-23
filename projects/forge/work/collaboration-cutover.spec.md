---
version: 0.8
status: draft
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
`collaboration`: the preparation and the first release, built on `main`
in one stretch and released 2026-10-19 (DEC.0230, DEC.0250, DEC.0260);
the second, third and fourth release of DEC.0220, deferred by DEC.0250
and let go on 2026-10-23 by the principal's word (brief 0.9, Principle),
kept as dropped rows; and the simplified second release built instead:
the conflict step, the hook's ask, the rules of ID and version after a
merge. Each release broken into steps in the order of building, every
step naming the part of the design it realises, the files it touches,
what closes it and its state, so that Claude follows it step by step on
the principal's word and the principal tunes the order and the cut. For
the principal and Claude. Dead after the simplified second release
(R6.07); it stays as it lies.

## Inputs
- 40-solution-design.md: SOL.0670 to SOL.0830, each with its `Where` and its release mark; SOL.0300 and SOL.0330; SOL.0520 (the hook's ask, R6.01, R6.05); TBC.0020 (the clash reported at R1.09); SOL.0530 (the release, every release's run), SOL.0150 (the instance file, R1.14), SOL.0160 (the scaffold, R1.15), SOL.0420 and SOL.0460 (the publish and the documentation refusing the old shape, R1.20), SOL.0500 (the engine's own attributes, R1.07); TBC.0050, TBC.0060, TBC.0080
- 10-intent.md: POS.1560 to POS.1770, POS.1120, POS.1140, POS.0220 (the renumbering at a clash, R2.14); POS.0550, POS.1200 (R6.04)
- threads/: THR.0620 (row 9), THR.0650, THR.0690, THR.0700, THR.0710 (the form of the deferred releases, open 2026-10-18 to 2026-10-23)
- decisions.md: DEC.0210, DEC.0220, DEC.0230, DEC.0240, DEC.0250, DEC.0260
- 00-brief-collaboration.md, section M (the steps of a migration run); v0.9, Principle and Promise (the redirection of 2026-10-23)
- sources/collaboration-simplification-challenge.md: the second of the two proposals of 2026-10-23, Claude's the first (the Method, Choices of 2026-10-23)
- research/2026-10-17-mergeable-shared-records-in-git.md and research/2026-10-17-git-merge-drivers-and-their-limits.md: the evidence against `merge=union` (REJ.0280), which both proposals of 2026-10-23 had wanted and which stands
- sources/cutover-plan-critique.md, sources/cutover-challenge-review.md, sources/cutover-challenge-review-2.md: the reviews the file was worked by hand against

## Method
One section per release. Within a release the steps in the order of
dependency: the shape first (templates, CLAUDE.md), since a script
cannot read a template that does not exist; the mechanism second
(scripts); the use third (skills, agents, definitions), since a skill
cannot call a script that does not exist; then the tests the release
needs before it (TBC.0050); then the release's run: the checks,
`/document`, `/release`, the marks of the design turned over (SOL.0530),
the migration where the release has one. The preparation has no run
of its own: it ships by its saves on main and ends with the tag
`pre-r1` (DEC.0260). A step carries an id (R1.01),
what is done, the part of the design it realises, the files, what closes
it (a test, a check, a run) and a state: todo, doing, done, dropped. The
state is the only thing that changes after the file is made.

**Choices of 2026-10-23**, the simplified second release, each with what
it was chosen against. The conflict step, `forge-save` leaving a
conflicting rebase standing and Claude laying both sides out in a
walkthrough, the person deciding, the finishing commands of git on the
hook's ask: chosen against the `/merge` skill with its own script and
the worktree (SOL.0820, SOL.0770), the same help without a new
mechanism; against `forge-save --continue` alone, since the ask also
serves a merge the integrator makes by hand; against git opened to
Claude whole, since the commit message word for word, the rebase before
the push and the check before a save would then rest on text alone. No
driver and no `merge=union` for the record files, a conflict in a log
settled by keeping both tails in the conflict step: chosen against the
driver (SOL.0750), the most code of the plan for a case of a few times a
year, and against union, which loses a line at the seam and exits 0 over
the damage (REJ.0280, the researches of 2026-10-17); both proposals of
the day had wanted union. IDs sequential, a clash reported by the ledger
script and settled by POS.0220 in a walkthrough; a version given twice
settled by whoever merges, with the next number and one record: chosen
against the blocks and the allocation over the branches (SOL.0790) and
against the landing with `+` (SOL.0760). The hook's ask narrow, a named
set of verbs: chosen against the deny rule narrowed to the destructive
verbs alone (THR.0710's second form).

## Assumptions
- **ASM.0010** The releases are built one at a time in the order of DEC.0210, each released before the next starts.
- **ASM.0020** A release is a round on the operating layer; the intent and the design change only where building shows they must, intent-first (CLAUDE.md, Working methods).
- **ASM.0030** The engine's own project migrates first, on this clone, within the first release; every other project after it, each on one clone, by the principal.
- **ASM.0040** During the first release no project is worked on and the engine is not pulled on the second machine until its release (DEC.0230); should that fail, the way back is the tag `pre-r1` on the engine and on every project.
- **ASM.0050** A second author of the engine's own project arrives through a pull request on GitHub and never writes into the principal's clone; the integrator merges locally where the server shows a conflict.
- **ASM.0060** Help at a conflict is the ceiling: nobody expects a merge without a person, and the forge promises none.
- **ASM.0070** The hook's ask on the named verbs is enough for the integrator to let Claude finish a merge or a rebase on his word; the ask holds in the automatic permission mode (tried 2026-10-21, THR.0710).

## Making
The file `work/collaboration-cutover.md`, English, Markdown: a heading
per release with the parts it carries, a table of its steps with the
columns id, step, part, files, closes with, state; no reasons, which
stay here and in the design. Made once from this specification by
Claude; from then on worked by hand, the states changed as the work
proceeds, the ledger row `by hand` on the principal's word.
