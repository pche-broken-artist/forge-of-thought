---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 1e2db27ee0f72412
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

A command of the forge is a skill: one file,
`.claude/skills/<name>/SKILL.md`, that the principal (the person
whose thinking is forged) invokes as `/<name>`. This page is for the
extender who wants to add one. It says which files are touched, what
the skill carries, when the command is guarded so that Claude cannot
start it on its own judgement, and how the addition is proved. Every
term of the forge used here is in the [Glossary](../reference/glossary.md).

## Before you start

A new command is a change of the forge like any other. It goes
through the chain described in
[Make a change to the forge](how-a-change-is-made.md), and it is
recorded and released as any change of the forge is.

Know the words first. "Command" is the word for what the principal
invokes by slash. "Skill" names the file shape, which commands and
the reviewers' contracts share: the contracts live in the same
directory, but no one invokes them by slash.

Look at the commands that exist before you name yours:
[Commands](../reference/commands.md) lists them. The name must not
collide with a built-in of Claude Code, the harness (the program that
runs Claude and the forge's commands). Two commands of the forge are
named as they are for that reason alone: `/setup` is not `/init`,
because the built-in `/init` generates a CLAUDE.md and the collision
would send a newcomer to exactly the wrong action at the most
sensitive moment; `/man` is not `/help`, because `/help` is a
built-in.

## The files

- `.claude/skills/<name>/SKILL.md`: the command itself. Its
  front-matter carries `description`, the one line Claude Code shows
  for it; `argument-hint`, where the command takes arguments, always
  quoted; and `disable-model-invocation: true`, where the command is
  guarded. Its body says what the command does.
- `.claude/skills/<name>/<kind>/<member>.md`: supporting files,
  only where the command dispatches over a roster, as `/forge` does
  over its state files and `/recipe` over its genre files. Each is
  read by path, registered as nothing, carries a description and no
  registration field, and needs no guard.
- `CLAUDE.md`, the Commands table: one row per command, the command
  with its arguments in the first column and its purpose in one line
  in the second.

## Steps

1. Choose the name. Check it against [Commands](../reference/commands.md)
   and against the built-ins of Claude Code.

2. Decide whether the command is guarded. The criterion: a guarded
   command changes files the moment it runs, with no round and no
   `write` in between. A command that writes only at the end of a
   round on the principal's word, or that files the immutable record
   of a run he asked for, needs no guard, because the word is already
   in the procedure. Maps, reports and rosters stay Claude's to
   start, since it is meant to propose them. The guarded commands
   today are `/save`, `/release`, `/pull`, `/spinoff`, `/setup`,
   `/new-project`, `/new-artefact`, `/import-project`, `/ingest`,
   `/render`, `/publish`, `/document` and `/migrate`.

3. Write the front-matter of `.claude/skills/<name>/SKILL.md`.
   - `description`: what the command does, in one line.
   - `argument-hint`: the arguments as the principal types them,
     in quotes. Every hint is quoted, because a front-matter with
     CRLF line endings and an unquoted hint of two bracketed items
     fails to parse, and the harness then shows the body's first
     line as the description. A command without arguments carries no
     hint.
   - `disable-model-invocation: true`: only where step 2 said
     guarded. The field keeps Claude from starting the command on
     its own judgement: the principal invokes it by slash, or asks
     in words, and Claude then follows the command's file read by
     path. A guarded command's description thereby also leaves the
     always-on context. A command that is Claude's to start carries
     no such field.

4. Write the body. It says what the command does, for the
   principal. Where the command needs a mechanism of another
   command, a skill, a script or an agent, it cites that mechanism by
   path and adds nothing of its own to how it runs: the rules of a
   mechanism are written once, in its own definition. Restating a
   procedure in a second place is a defect, because the two copies
   drift and the copy without a rule silently loses it. A one-line
   reminder at the point of action that names its owner is not a
   restatement. The body loads only when the command is invoked, so
   its length costs the always-on context nothing.

5. Where the command dispatches over a roster, put one supporting
   file per member beside it, each with a description and no
   registration field, and let the body read them by path.

6. Add the row to the Commands table of `CLAUDE.md`. What the
   command does in full stays in its skill; the row carries the
   command with its arguments and its purpose in one line.

## Prove it

Type each as it stands.

- `/man <name>` prints the skill. You should now see the file you
  wrote, which is the sign the command is in place.
- `/check engine` verifies the core against itself, the Commands
  table of `CLAUDE.md` against the skills in
  `.claude/skills/*/SKILL.md` among it. A row without a skill, or a
  skill without a row, is a finding.
- `/check single-source-of-truth` sweeps the operating layer for a
  procedure stated in more than one place. A body that retells
  another command's steps instead of citing them is a finding. This
  check runs on the principal's word and never at a release on its
  own, so that the rule costs a release nothing.

## Record and release

The addition is a change of the forge and is recorded and released
as any change of the forge is; the way is on
[Make a change to the forge](how-a-change-is-made.md). The engine
check reads the Commands table against the skills at a release, so
a row forgotten in step 6 is found there at the latest.

## A worked example

A report command, `/<name> [slug]`, that reads a project and says
something about it, and writes nothing. It is Claude's to start, so
it carries no guard.

`.claude/skills/<name>/SKILL.md`:

```
---
description: <what the command does, in one line>
argument-hint: "[slug]"
---

<What the command does for the principal, in a few sentences. Where
it needs the ledger, it names the script that makes the ledger by
path and says nothing of how the script runs. Where it reports as
another command reports, it names that command's skill and the step
by path, and the report has one procedure.>
```

The row in the Commands table of `CLAUDE.md`:

```
| `/<name> [slug]` | <what the command does, in one line> |
```

Had the command changed files the moment it ran, a scaffold or a
regeneration, the front-matter would carry one line more:

```
disable-model-invocation: true
```

Then `/man <name>`, `/check engine` and
`/check single-source-of-truth`, and the change is recorded and
released as the linked page says.

## See also

- [Make a change to the forge](how-a-change-is-made.md): the chain
  the change goes through.
- [Commands](../reference/commands.md): the commands that exist.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
