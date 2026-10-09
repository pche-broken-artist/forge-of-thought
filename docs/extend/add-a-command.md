---
generated: 2026-10-09
made: derived
inputs-hash: c37fbc1214a64c77
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
slash command. It was put together from `CLAUDE.md`, the skills
`ledger` and `man`, the agent `check-engine`, the forge intent and
the solution design: it derives from them what a command is made
of, where it is registered, how it is named and how the result is
proved. The chain the change itself goes through, from the forge
intent to the release, is the page [Make a change to the
forge](how-a-change-is-made.md).

## What a command is

A command is a skill: one file, `.claude/skills/<name>/SKILL.md`,
which the user invokes as `/<name>`. "Command" is the word for what
the user invokes by slash; "skill" names the file shape, and not
every skill is a command: the reviewers' contracts live in the same
directory and are not invocable by the user. A skill of a given
name shadows a command file of the same name, so a command is moved
to the skill shape whole, never half.

The body of a command loads only when the command is invoked, so a
new command costs the always-on context nothing beyond its
`description`.

## Step 1: write the skill file

Create `.claude/skills/<name>/SKILL.md` with a front-matter and a
body.

The front-matter carries:

- `description`: one line saying what the command does, and what
  the bare command does where it takes an optional argument (for
  instance that bare, it prints a roster). `/man <name>` prints
  this line as the command's purpose, and the bare rosters of
  `/check`, `/critique` and `/challenge` are built from the
  `description` of each file they dispatch over, so the line is
  what the user reads before running anything.
- `argument-hint`, always quoted: for instance
  `argument-hint: "[slug]"`. The quoting is not taste: a
  front-matter with CRLF line endings and an unquoted hint of two
  bracketed items fails to parse, and the harness then shows the
  first line of the body as the description.
- `disable-model-invocation: true` where the command writes,
  scaffolds, commits or regenerates. This is the guard: with it,
  Claude cannot start the command on his own judgement; the
  principal invokes it by slash, or asks for it in words and Claude
  then follows the command's definition read by path. The guarded
  commands today are `/save`, `/release`, `/spinoff`, `/setup`,
  `/new-project`, `/new-artefact`, `/import-project`, `/ingest`,
  `/render` and `/publish`. A command that only maps, reports or
  lists a roster (`/forge`, `/ledger`, `/check`, `/critique`,
  `/challenge`, `/research`, `/recipe`) carries no such field and
  stays Claude's to start, because he is meant to propose those.
  The reason the guard sits in the harness and not in conduct
  alone: the working method Step by step, by which every action
  needing the principal's consent arrives as one step and runs on
  his word, then rests on the harness as well as on `CLAUDE.md`.

A skeleton:

```
---
description: <what the command does; bare = <what bare does>>
argument-hint: "[<argument>]"
disable-model-invocation: true
---

<the body>
```

The body says what the command does for the person, in the
person's terms. Where it needs a mechanism the forge already has (a
procedure of another command, a script, an agent, a check), it
cites that mechanism by path and adds nothing of its own to how it
runs; it never restates the procedure. One mechanism lives in one
place: a procedure stated twice is a defect, because the two copies
drift and the copy without a rule silently loses it. A one-line
reminder at the point of action that names its owner is not a
restatement; repeated steps, rules or a shape are.

The smallest model of this is the `ledger` skill
(`.claude/skills/ledger/SKILL.md`): a few lines, read-only, which
say that the report is made as the bare `/forge` map makes it, name
the step of `.claude/skills/forge/SKILL.md` that owns that
procedure, and point reconciling the ledger with reality to the
`light` check rather than doing it themselves.

## Step 2: supporting files, where the command dispatches over a roster

A command that dispatches over a set of things, as `/forge` does
over states and `/recipe` over genres, keeps them as supporting
files beside it (`.claude/skills/<name>/<group>/<member>.md`).
These are read by path by the dispatcher, registered as nothing,
and carry a description and no registration field. They need no
guard of their own: the guard is the dispatcher's. `/man <name>`
prints such a roster from the skill, each entry with the
`description` of its own file, so a roster member without a
description is invisible there.

## Step 3: register the row in `CLAUDE.md`

Add one row to the Commands table of `CLAUDE.md`, Commands: the
command with its arguments in the first column, its purpose in the
second, with what bare means where that applies. The table is where
the command is listed; what the command does in full stays its
skill's.

Two readers derive from this row rather than from a text of their
own:

- `/man`, the forge's manual, is a reader and never a text of its
  own. Bare, it prints the Commands table as a list; with a
  command, it prints the skill's `description`, its `argument-hint`
  (or, failing one, the row of `CLAUDE.md`) and the row's purpose
  in full, then the roster where the skill names one, and closes by
  naming the skill file.
- The README is a render, regenerated at every release, and must
  carry the same command set as `CLAUDE.md`. A command in the
  README that `CLAUDE.md` no longer supports is a defect of the
  README's recipe, fixed there.

## Naming

Name the command so that it does not collide with a built-in of
Claude Code. The forge has two precedents. The first run is
`/setup` and not `/init`, because Claude Code's own `/init`
generates a `CLAUDE.md`, and the collision would send a newcomer to
exactly the wrong action at the most sensitive moment. The manual is
`/man` and not `/help`, because `/help` is Claude Code's own
command, hence the Unix name.

## Proof

Two checks prove the addition; both are run by hand and their
findings are settled by walkthrough.

- `/check engine` verifies the core against itself and against the
  forge intent. Among what it verifies: the Commands table of
  `CLAUDE.md` against the skills actually present in
  `.claude/skills/*/SKILL.md` (the reviewers' contracts excepted),
  and that the README carries the same command set as `CLAUDE.md`.
  It runs at every release, so a table row without a skill, or a
  skill without a row, does not survive one.
- `/check single-source-of-truth` sweeps the whole operating layer
  for restatements and direct operations: it verifies that the new
  body cites every borrowed mechanism and restates none. It is
  expensive by design and runs on the principal's word, never by a
  release on its own, so the sweep is honest when it runs: run it
  after a round on the operating layer such as this one.

## Record the change

A new command is a change of the forge like any other. The forge is
run through its own process: a process change is complete only
once the forge intent is updated and the README re-rendered. The
solution design names where the commands live and which are
guarded; where the new command changes what it states, it changes
too. How the change travels is the page [Make a change to the
forge](how-a-change-is-made.md).

## See also

- [Make a change to the forge](how-a-change-is-made.md): the chain
  the change goes through.
- [Commands](../reference/commands.md): the commands that exist.
