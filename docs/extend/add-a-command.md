---
generated: 2026-10-10
made: derived
inputs-hash: 5114fc85af3b2cb4
inputs:
  - CLAUDE.md
  - .claude/skills/ledger/SKILL.md
  - .claude/skills/man/SKILL.md
  - .claude/agents/check-engine.md
  - projects/forge/10-intent.md
  - projects/forge/40-solution-design.md
---

# Add a command

This page is for the extender who wants to give the forge a new
command: what a command is made of, where it lives, what else has to
change with it and how the result is verified. It was put together
from `CLAUDE.md`, the skills `ledger` and `man`, the agent
`check-engine`, the forge intent and the forge solution design; the
procedure below is derived from what those files say, not stated as
such in any one of them.

## What a command is

A command is a skill: one file, `.claude/skills/<name>/SKILL.md`.
"Command" is the word for what the user invokes by slash; "skill"
names the file shape, which commands share with the reviewers'
contracts (skills of the same directory that no user invokes). What a
command does in full is its skill file; `/man <command>` prints that
file's purpose, arguments and roster, read at the moment of the call,
never from a text of its own.

A skill shadows a command file of the same name, so a command is
moved to the skill shape whole, never half. A skill's body loads only
when the command is invoked, so a new command costs the always-on
context nothing.

## Step 1: choose a name that collides with nothing

Claude Code has built-in commands of its own, and a forge command of
the same name would send the user to the wrong action. Two names of
the forge were chosen around this: the first-run command is `/setup`
and not `/init`, because the built-in `/init` generates a `CLAUDE.md`
and the collision would strike a newcomer at the most sensitive
moment; the manual is `/man` and not `/help`, because `/help` is
Claude Code's. Before settling a name, make sure it is not a built-in.

## Step 2: write the front-matter

The front-matter carries three things.

- `description`: one line saying what the command does and, where
  the command takes an optional argument, what the bare call means
  (the bare `/check`, for instance, lists the roster). The rosters
  the bare commands print and the overview `/man` prints are read
  from these lines, so the line is what the user sees first.
- `argument-hint`: the arguments, always quoted. The solution design
  records why: a front-matter with CRLF line endings and an unquoted
  hint of two bracketed items fails to parse, and the harness then
  shows the body's first line as the description.
- `disable-model-invocation: true`: present on every command that
  writes, scaffolds, commits or regenerates, absent on the rest. With
  the field, Claude cannot start the command on his own judgement;
  the principal invokes it by slash, or asks in words and Claude
  follows the skill file, read by path. The commands guarded today
  are `/save`, `/release`, `/spinoff`, `/setup`, `/new-project`,
  `/new-artefact`, `/import-project`, `/ingest`, `/render`,
  `/publish` and `/document`. Maps, reports and rosters (`/forge`,
  `/ledger`, `/check`, `/critique`, `/challenge`, `/research`, bare
  `/recipe`) carry no such field and stay Claude's to start, since he
  is meant to propose them. The reason is the rule the forge calls
  Step by step: an action needing the principal's consent runs on
  his word, and the harness is to hold that line beside `CLAUDE.md`,
  not `CLAUDE.md` alone. A guarded command's description thereby
  leaves the always-on context; a guarded command asked for in words
  is followed the way a dispatcher follows a state file.

## Step 3: write the body

The body says what the command does. Where the command needs a
mechanism the forge already has (a render, a save, a check, a report
another command already makes), it cites that mechanism by path and
adds nothing of its own to how it runs: the rules of a mechanism
(its isolation, its wrapping, its provenance, what it may read) are
written once, in that mechanism's own definition. Restating a
procedure in a second place is a defect in the forge: the two copies
drift, and the copy without a rule silently loses it. A one-line
reminder at the point of action that names its owner is not a
restatement; steps, rules or a shape repeated are.

The smallest model of this is the `ledger` skill. `/ledger` reports
the state of a project from its ledger, in the shape the bare
`/forge` map reports it. Its skill does not describe that report: it
names the step of the `forge` skill that owns the procedure, by path,
and says that `/ledger` is the door to a ledger-only reading. It then
draws its boundary the same way, naming the `light` check as the
owner of reconciling the ledger with what is on disk, and tells
Claude to point there rather than do it. A body of a few lines is
complete when every mechanism it needs is cited rather than retold.

The `man` skill shows the same discipline on a larger body: it is a
reader of the files that own what it prints (`CLAUDE.md`, the
skills, the agents, the state and genre files) and states nothing
that lives there.

## Step 4: supporting files, where the command dispatches

A command that dispatches over a roster keeps the members of that
roster as files beside it, read by path: the state files of `/forge`
live in `.claude/skills/forge/states/<state>.md`, the genre files of
`/recipe` in `.claude/skills/recipe/genres/<genre>.md`. A supporting
file carries a description and no registration field, is registered
as nothing and needs no guard: the guard sits on the dispatcher. The
roster a bare call prints, and the roster `/man <command>` prints, is
the scan of those files. A future member of the roster is then one
new file, and the dispatcher stays untouched.

## Step 5: add the row to the Commands table

`CLAUDE.md` has one table of the commands, under Commands: the
command with its arguments in the first column, its purpose in one
line in the second, the bare meaning included where there is one
("bare = the lens roster"). Add the new command's row. Bare `/man`
prints its overview from this table, and `/man <command>` prints the
row's purpose beside the skill's own description and hint. The README
is a render and is regenerated at every release; its command set has
to agree with this table, and a README claim the table no longer
supports is a recipe defect, fixed in the readme recipe, never in the
README by hand.

## Step 6: prove it

Two checks verify what this page asks for, each owning one concern.

- `/check engine` reads the core against itself: among other things
  it verifies the Commands table of `CLAUDE.md` against the skills
  that exist in `.claude/skills/*/SKILL.md` (the reviewers' contracts
  excepted), and that any skill an agent names in its front-matter
  exists, since the harness skips a missing one silently. A row
  without a skill, or a skill without a row, is a finding. This
  check runs at every release.
- `/check single-source-of-truth` sweeps the whole operating layer
  for procedures stated twice and for direct operations that bypass
  their owner. It is expensive by design and runs on the principal's
  word, before a major or after a round on the operating layer, never
  at a release on its own. Run it when the new command's body is
  done.

A check's findings are filed in `reviews/` and settled by walkthrough
like any reviewer's; a run that finds nothing files nothing.

## Step 7: record it as a change of the forge

A new command is a change of the forge like any other, and the forge
runs through its own process: the change is complete only once the
forge intent is updated and the README re-rendered. The chain the
change goes through is on the page linked below.

## See also

- [Make a change to the forge](how-a-change-is-made.md): the chain
  the change goes through.
- [Commands](../reference/commands.md): the commands that exist.
