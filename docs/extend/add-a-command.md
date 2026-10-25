---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 03b6e95f1411b787
inputs:
  - CLAUDE.md#Commands
  - .claude/skills/ledger/SKILL.md
  - .claude/skills/end/SKILL.md
  - .claude/agents/check-engine.md
  - projects/forge/10-intent.md#POS.1090
  - projects/forge/10-intent.md#POS.1070
  - projects/forge/10-intent.md#POS.1050
  - projects/forge/10-intent.md#POS.1190
  - projects/forge/40-solution-design.md#SOL.0100
  - projects/forge/40-solution-design.md#SOL.0110
---

# Add a command

A command of the forge is a skill: one file that Claude Code turns
into a command you type with a slash, such as `/ledger`. This page
is for the extender who wants to add a new command. It covers the
file you write, the row it gets in the table of commands, when the
command must be guarded so that Claude cannot start it unasked, how
to name it and how to prove it fits.

## Before you start

A new command is a change to the engine, and it travels the chain
described in [Make a change to the forge](how-a-change-is-made.md).
The addition is recorded and released as any change of the forge.

Two words recur below:

- principal: the person whose thinking is forged, and the final
  authority on everything the forge writes.
- harness: the program that runs Claude and reads the skill files,
  here Claude Code.

The commands that already exist are listed in
[Commands](../reference/commands.md). Every other term of the forge
is in the [Glossary](../reference/glossary.md).

## The files

- `.claude/skills/<name>/SKILL.md`: the command itself. Every
  command lives in this shape.
- Supporting files beside it, only where the command dispatches over
  a roster. The `/forge` command reads one definition per state from
  `.claude/skills/forge/states/<state>.md`. The `/recipe` command
  reads one genre file per genre from
  `.claude/skills/recipe/genres/<genre>.md`. Such a file is read by
  its path and registered as nothing. It carries a description and no
  registration field.
- `CLAUDE.md`, section Commands: one row for the new command in the
  table of commands.

"Command" is the word for what you invoke by slash. "Skill" is the
word for the file shape, which commands share with the contracts of
the reviewers.

## Steps

1. **Choose the name.** The name must not collide with a built-in
   command of Claude Code. A collision sends the reader to the wrong
   action. The forge's first-run command is `/setup` and not `/init`,
   because Claude Code's built-in `/init` generates a `CLAUDE.md`,
   and a newcomer would be sent to exactly the wrong action at the
   most sensitive moment. The forge's manual is `/man` (after the
   Unix manual) and not `/help`, because `/help` is a built-in of
   Claude Code.

2. **Write the front-matter.** It holds these fields:
   - `description`: one line saying what the command does.
   - `argument-hint`: the arguments the command takes, always in
     quotes. Leave it out where the command takes no argument, as
     `/end` does.
   - `disable-model-invocation: true`: only where the command is
     guarded (step 3).

   The hint is quoted because a front-matter with CRLF line endings
   and an unquoted hint of two bracketed items fails to parse. The
   harness then shows the first line of the body as the description.

3. **Decide whether the command is guarded.** A guarded command
   carries `disable-model-invocation: true`, so that Claude cannot
   start it on its own judgement. The test is what the command does
   the moment it runs:
   - It changes files at once, with no round of conversation and no
     `write` from the principal in between: guard it. Commands that
     write, scaffold, commit or regenerate are of this kind, such as
     `/save`, `/render` or `/new-project`.
   - It writes only at the end of a round on the principal's word,
     or it files the immutable record of a run the principal asked
     for: no guard. The principal's word is already part of its
     procedure.
   - It is a map, a report or a roster, such as `/forge`, `/ledger`
     or `/check`: no guard. Claude is meant to propose these, so it
     must be able to start them.

   A guarded command still works when the principal asks for it in
   words. Claude then reads the command's file by its path and
   follows it. The description of a guarded command leaves the
   context Claude carries at all times. The guard sits in the
   harness so that the rule of acting step by step, on the
   principal's word, rests on the harness as well as on `CLAUDE.md`.

4. **Write the body.** The body says what the command does for the
   principal, in order. Where the command needs a mechanism the
   forge already has (a command, a skill, a script, an agent), the
   body cites it by path and adds nothing of its own to how it runs.
   A procedure written in two places is a defect, because the two
   copies drift and the copy without a rule silently loses it. A
   one-line reminder at the point of action that names its owner is
   not a copy. Where a shape has no owner at all, it gets a template
   rather than a second description. The two smallest commands show
   the scale:
   - `.claude/skills/ledger/SKILL.md` makes the ledger (the one
     record of a project's state, built by a script when it is read)
     and reports it by citing the step of `/forge` that owns that
     report.
   - `.claude/skills/end/SKILL.md` lists four numbered steps, runs
     nothing but the status script and writes nothing.

5. **Add the row to `CLAUDE.md`.** In the section Commands, add one
   row to the table: the command with its arguments, and its purpose
   in one line. The full description of the command stays in its
   skill.

## Prove it

Run the engine check:

```
/check engine
```

It compares the table of commands in `CLAUDE.md` with the skills on
disk, `.claude/skills/*/SKILL.md`, the contracts of the reviewers
excepted. A command without a row, or a row without a skill, is a
finding. It also compares the command set of the README with
`CLAUDE.md`.

Then run the check for a rule stated twice:

```
/check single-source-of-truth
```

It sweeps the whole operating layer for steps, rules or a shape
repeated outside their owner. It runs on the principal's word, never
at a release on its own.

Read the command back as the manual prints it:

```
/man <name>
```

## Record and release

The new skill and the new row are recorded and released as any
change of the forge, as described in
[Make a change to the forge](how-a-change-is-made.md).

## A worked example

You add a report command `/<name>` that takes an optional project
slug. It only reads and reports, so it is not guarded.

`.claude/skills/<name>/SKILL.md`:

```
---
description: <one line: what the command reports>
argument-hint: "[project-slug]"
---

<What the command does, in order. Every mechanism of another
command, skill, script or agent cited by its path, never restated.>
```

The row in `CLAUDE.md`, section Commands:

```
| `/<name> [slug]` | <what the command is for, in one line> |
```

Had the command written files the moment it runs, its front-matter
would carry one more line:

```
disable-model-invocation: true
```

Then run `/check engine` and `/check single-source-of-truth`, and
read the result back with `/man <name>`.

## See also

- [Make a change to the forge](how-a-change-is-made.md): the chain
  the change goes through.
- [Commands](../reference/commands.md): the commands that exist.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
