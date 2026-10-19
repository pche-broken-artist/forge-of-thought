---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: adfe7dbdd16e3589
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
`.claude/skills/<name>/SKILL.md`, that the principal starts by typing
`/<name>`. The principal is the person whose thinking is forged and
who has the final word on it. This page is for the extender who adds
a new command to the engine. It says which files you write, what
goes into them, when the command must be guarded and how you prove
the addition.

## Before you start

A new command is a change to the forge like any other. It goes
through the chain described in
[Make a change to the forge](how-a-change-is-made.md), and it is
recorded and released as any change of the forge.

Look at [Commands](../reference/commands.md) first. Your command
must not do what an existing one already does. If it needs another
command's mechanism, it uses that mechanism and does not describe it
again.

Choose a name that does not collide with a built-in command of
Claude Code. Claude Code is the harness, that is the program Claude
runs in and that reads the skills. A skill of the same name as a
built-in sends the reader to the wrong action. The forge names its
manual `/man` because `/help` is a built-in, and its first-run
command `/setup` because the built-in `/init` writes a `CLAUDE.md`.

## The files

- `.claude/skills/<name>/SKILL.md`: the command itself (front-matter
  and body).
- Supporting files beside it, where the command dispatches over a
  roster: one file per member, such as the definitions of `/forge`
  in `.claude/skills/forge/states/` and the genres of `/recipe` in
  `.claude/skills/recipe/genres/`. They are read by path, carry a
  description and no registration field, and are registered as
  nothing.
- `CLAUDE.md`, section Commands: one new row in the table.

A command and a skill are not two things here. "Command" is the word
for what the principal invokes by slash; "skill" is the shape of the
file. See the [Glossary](../reference/glossary.md) for both terms.

## Steps

1. **Write the front-matter.** It carries these fields:
   - `description`: what the command does, in one line. This is what
     the roster and the harness show.
   - `argument-hint`: the arguments, always in quotes, for example
     `"[project-slug]"`. Leave it out where the command takes no
     argument, as `/end` does.
   - `disable-model-invocation: true`: only where the command is
     guarded (step 2).

   The quotes on `argument-hint` are required. A front-matter with
   CRLF line endings and an unquoted hint of two bracketed items
   fails to parse. The harness then shows the first line of the body
   as the description.

   You should now see your command in Claude Code's list of
   commands, with your description beside it.

2. **Decide whether the command is guarded.** A command is guarded
   when it changes files the moment it runs, with no round and no
   `write` in between. Commands that write, scaffold, commit or
   regenerate are guarded, such as `/save`, `/release`, `/render` and
   `/document`. A guarded command carries
   `disable-model-invocation: true`, so that Claude cannot start it
   on its own judgement. The principal starts it by slash. Where he
   asks for it in words, Claude reads the command's definition by
   path and follows it.

   A command needs no guard when it writes only at the end of a round
   on the principal's word, or files the immutable record of a run he
   asked for. Maps, reports and rosters stay unguarded, such as
   `/forge`, `/ledger`, `/check` and `/end`. Claude is meant to
   propose them, so it must be able to start them.

   You should now have the field in the front-matter of a guarded
   command, and no such field in an unguarded one.

3. **Write the body.** The body says what the command does, as steps
   where it has steps, and what it writes or does not write. Every
   mechanism that belongs to another command, skill, script or agent
   is cited by its path, never described again. The two smallest
   skills of the engine are good models:
   - `.claude/skills/ledger/SKILL.md`: a few lines that run one
     script and name, by path, the step of `/forge` that owns the
     report.
   - `.claude/skills/end/SKILL.md`: four numbered steps, each naming
     the script or the section of `CLAUDE.md` it uses, and one line
     that says the command writes nothing.

   A one-line reminder at the point of action that names its owner is
   allowed. Steps, rules or a shape copied from another owner are a
   defect.

   You should now have a body in which every mechanism you did not
   write yourself appears as a path.

4. **Add supporting files, if the command dispatches.** Where the
   command picks one member of a roster, put one file per member in a
   directory beside `SKILL.md`. Give each a description and no
   registration field.

   You should now see the members as files in that directory, and
   nothing new in the list of commands.

5. **Add the row to `CLAUDE.md`.** In the Commands table, add one
   row: the command with its arguments, and its purpose in a few
   words.

   You should now see the command in the table, written the same way
   as the hint in its front-matter.

## A worked example

A guarded command `<name>` that takes one optional project slug.

`.claude/skills/<name>/SKILL.md`:

```
---
description: <what the command does, in one line>
argument-hint: "[slug]"
disable-model-invocation: true
---

<What the command does for project $0, step by step.>

1. <A step that runs a script, named by its path in scripts/.>
2. <A step that uses another command's mechanism, cited by the path
   of its skill.>
3. <What is written, and where.>
```

The row in `CLAUDE.md`, section Commands:

```
| `/<name> [slug]` | <what the command is for, in a few words> |
```

If `<name>` only reported and wrote nothing, the line
`disable-model-invocation: true` would be left out.

## Prove it

Run the engine check:

```
/check engine
```

It verifies the Commands table of `CLAUDE.md` against the skills on
disk, among the other parts of the core. A command in the table
without a skill, or a skill without a row, is a finding.

Run the check for rules stated in more than one place:

```
/check single-source-of-truth
```

It finds a body that restates another owner's procedure. It runs
only when the principal asks for it.

Read the command as a reader will see it:

```
/man <name>
```

It prints the skill.

## Record and release

Record and release the command as described in
[Make a change to the forge](how-a-change-is-made.md). The README
lists the same command set as `CLAUDE.md`, and it is regenerated
from its recipe at the release. Where the README's wording of the
commands needs changing, the change goes into the recipe, not into
the README.

## See also

- [Make a change to the forge](how-a-change-is-made.md): the chain
  the change goes through.
- [Commands](../reference/commands.md): the commands that exist.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
