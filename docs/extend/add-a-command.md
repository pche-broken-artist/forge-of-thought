---
generated: 2026-10-23
version: 5.34
made: derived
inputs-hash: 55f053fcb9cea725
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

A command of the forge is a skill file that the principal (the person
whose thinking is forged) invokes by a slash, such as `/ledger`. This
page is for an extender who wants to add a new command. It says which
file to write, what goes into its front-matter, when the command must
be guarded against Claude starting it unasked, and how to prove the
addition before it is released.

## Before you start

A new command is a change to the forge's operating layer. It goes
through the chain every change goes through, described in
[Make a change to the forge](how-a-change-is-made.md). The addition is
recorded and released as any change of the forge.

Decide two things first.

- **The name.** Choose a name that does not collide with a built-in
  command of Claude Code (the program Claude runs in, here called the
  harness). A collision sends a reader to the wrong action. That is
  why the first-run command is `/setup` and not `/init`: the built-in
  `/init` generates a `CLAUDE.md`. It is also why the manual is `/man`:
  `/help` is a built-in.
- **Whether it is guarded.** A command is guarded when it changes files
  the moment it runs, with no round and no `write` in between. Such
  commands write, scaffold, commit or regenerate (`/save`, `/render`
  and `/document` are among them). A guarded command cannot be started
  by Claude on its own judgement. The principal invokes it by slash, or
  asks in words, and Claude then follows the command's definition read
  by its path.

A command needs no guard in two cases.

- It writes only at the end of a round, on the principal's word. The
  word is already in the procedure.
- It files the immutable record of a run the principal asked for. The
  word is already in the procedure here as well.

Maps, reports and rosters (`/forge`, `/ledger`, `/check`, `/critique`,
`/challenge`, `/research`) stay unguarded. Claude is meant to propose
them, so it must be able to start them.

## The files

- `.claude/skills/<name>/SKILL.md`: the command itself. Every command
  lives as a skill in this shape. "Command" is the word for what is
  invoked by slash; "skill" is the word for the file shape.
- Supporting files beside it, only where the command dispatches over a
  roster. The `/forge` command reads one definition per state from
  `.claude/skills/forge/states/<state>.md`, and `/recipe` reads one
  genre file per genre from `.claude/skills/recipe/genres/<genre>.md`.
  A supporting file is read by its path and registered as nothing. It
  carries a description and no registration field, and it needs no
  guard.
- `CLAUDE.md`, section Commands: one row in the Commands table, with
  the command as it is typed and its purpose. The full content of a
  command belongs to its skill; the row only names it. The current
  rows are listed in [Commands](../reference/commands.md).

## Steps

1. Create the directory `.claude/skills/<name>/` and the file
   `SKILL.md` in it.
2. Write the front-matter.
   - `description`: one line that says what the command does.
   - `argument-hint`: the arguments as the reader types them, always in
     quotes. A front-matter with CRLF line endings and an unquoted hint
     of two bracketed items fails to parse. The harness then shows the
     body's first line as the description.
   - `disable-model-invocation: true`: only where the command is
     guarded. Leave the field out for a map, a report or a roster. A
     guarded command's description leaves the context Claude always
     carries.
3. Write the body. It says what the command does, in order.
4. Where the command needs a mechanism that another command, skill,
   script or agent already owns, cite that owner by its path. Add
   nothing of your own to how that mechanism runs. Restating a
   procedure in a second place is a defect, because the two copies
   drift and the copy without a rule silently loses it. A one-line
   reminder at the point of action that names its owner is not a
   restatement.
5. Where the command dispatches over a roster, add one supporting file
   per member beside `SKILL.md`.
6. Add the row to the Commands table in `CLAUDE.md`.

The smallest existing commands make good models to read before you
write: `.claude/skills/ledger/SKILL.md` (a report, unguarded, with a
quoted hint) and `.claude/skills/end/SKILL.md` (a report with numbered
steps and no arguments).

## A worked example

A new guarded command `/<name>` that takes an optional project slug.
The skill file `.claude/skills/<name>/SKILL.md`:

```markdown
---
description: <what the command does, in one line>
argument-hint: "[project-slug]"
disable-model-invocation: true
---

<What the command does for project $0, step by step.>

1. <A step of its own.>
2. Remake the ledger through the script that owns it, cited by its
   path: `python scripts/forge-ledger.py <slug>`.
```

The row added to the Commands table of `CLAUDE.md`:

```markdown
| `/<name> [slug]` | <its purpose in one line> |
```

For a map, a report or a roster, the same file without the line
`disable-model-invocation: true`.

## Prove it

Run the engine check:

```
/check engine
```

Among other things it verifies that the Commands table in `CLAUDE.md`
and the skills in `.claude/skills/*/SKILL.md` agree. The reviewers'
contracts are skills of the same directory and are excepted. A command
without a row, or a row without a skill, is a finding (the result a
reviewer reports).

Then run the check that a rule is stated in one place only:

```
/check single-source-of-truth
```

It reads the whole operating layer for restatements of a procedure.
The engine check leaves that concern to it.

## Record and release

The new command is recorded and released as any change of the forge,
through the chain described in
[Make a change to the forge](how-a-change-is-made.md). Every term used
here is defined in one line in the [Glossary](../reference/glossary.md).

## See also

- [Make a change to the forge](how-a-change-is-made.md): the chain the
  change goes through.
- [Commands](../reference/commands.md): the commands that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-23 for version 5.34 from the files the
front-matter names; never edited by hand.
