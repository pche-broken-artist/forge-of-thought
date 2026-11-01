---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 1784ccb436dd91b0
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
`.claude/skills/<name>/SKILL.md`, that the person types as `/<name>`.
This page is for the extender who wants to add a new command to the
engine. It shows the file to write, the row to add, when the command
must be guarded against Claude starting it on its own, and how to
prove the addition is sound.

## Before you start

A new command is a change to the forge like any other.
It goes through the chain described in
[Make a change to the forge](how-a-change-is-made.md).
The addition is recorded and released as any change of the forge.

Look at [Commands](../reference/commands.md) first.
A command that already does the job is used, not written again.

Three words recur on this page:

- the principal: the person whose thinking is being forged, and the
  final authority on what is written;
- the harness: Claude Code, the program that runs Claude, reads the
  skills and offers them as slash commands;
- a skill: a file named `SKILL.md` in its own directory under
  `.claude/skills/`, the shape every command takes.

Other terms of the forge are each explained in one line in the
[Glossary](../reference/glossary.md).

## The files

- `.claude/skills/<name>/SKILL.md`: the command itself, a front-matter
  and a body.
- Supporting files beside it, only where the command dispatches over a
  roster: one file per member, read by path and registered as nothing.
  The definitions of `/forge` (`.claude/skills/forge/states/<state>.md`)
  and the genres of `/recipe`
  (`.claude/skills/recipe/genres/<genre>.md`) are the models.
  A supporting file carries a description and no registration field.
- `CLAUDE.md`, section Commands: one row for the new command.

## Steps

1. **Choose the name.**
   The name must not collide with a built-in command of Claude Code.
   A skill takes over a command of the same name.
   The engine's own cases show the rule.
   The first-run command is `/setup`, not `/init`, because the built-in
   `/init` generates a CLAUDE.md and would send a newcomer to exactly
   the wrong action.
   The manual is `/man`, because `/help` is a built-in.

2. **Write the front-matter.**
   - `description`: one line that says what the command does.
     The harness shows it when it lists the commands.
   - `argument-hint`: the arguments the command takes, always in
     quotes, such as `"[project-slug]"`.
     The quotes are required because a front-matter with CRLF line
     endings and an unquoted hint of two bracketed items fails to parse.
     The harness then shows the body's first line as the description.
     A command that takes no argument leaves the field out.
   - `disable-model-invocation: true`: only where the command is
     guarded (step 3).

3. **Decide whether the command is guarded.**
   A command is guarded when it changes files the moment it runs, with
   no round and no `write` from the principal in between.
   Commands that write, scaffold, commit or regenerate are of this kind,
   such as `/save`, `/release`, `/ingest`, `/render` and `/document`.
   The guard is the line `disable-model-invocation: true`.
   It keeps Claude from starting the command on its own judgement.
   The principal starts a guarded command by typing it, or asks for it
   in words, and then Claude follows the command's file read by path.
   The description of a guarded command also leaves the context Claude
   always carries.

   A command needs no guard in two cases:
   - it writes only at the end of a round, on the principal's word;
   - it files the immutable record of a run the principal asked for.

   The reason is that the principal's word is already part of its
   procedure.
   Maps, reports and rosters stay unguarded, such as `/forge`,
   `/ledger`, `/check` and `/end`.
   Claude is meant to propose them.

4. **Write the body.**
   The body says what the command does, in order where it has steps.
   Where the command needs a mechanism the forge already has (a script,
   another command, an agent, a check), the body names it by its path
   and adds nothing of its own to how it runs.
   A procedure written out in a second place is a defect, because the
   two copies drift apart.
   A one-line reminder at the point of action that names its owner is
   not such a copy.
   The `/ledger` and `/end` skills are the smallest models: a few lines
   each, every mechanism cited by path.

5. **Add the row to `CLAUDE.md`.**
   The Commands table has two columns: the command with its arguments,
   and its purpose in one line.
   The row matches the skill: same name, same arguments.

## Prove it

Run the engine check:

```
/check engine
```

Among other things it compares the Commands table of `CLAUDE.md` with
the skills on disk under `.claude/skills/`.
A command in the table without a skill, or a skill without a row, is a
finding.
The reviewers' contracts are skills too, and the check leaves them out
of the comparison.

Then run the check that looks for a rule stated in more than one place:

```
/check single-source-of-truth
```

It finds a body that restates the procedure of another mechanism
instead of citing it.
This check runs only when the principal asks for it, never on its own
at a release.

## Record and release

The new command is recorded and released as any change of the forge,
as [Make a change to the forge](how-a-change-is-made.md) describes.

## A worked example

A read-only report command called `<name>`, taking an optional project
slug, written as `.claude/skills/<name>/SKILL.md`:

```
---
description: Report <what> for one project or for all of them
argument-hint: "[project-slug]"
---

Make the ledger of project $0 (or of every project if none given)
by its script, and report <what> from it as <owning skill path>
says. This command writes nothing but the ledger the script writes.
```

It changes no file of its own the moment it runs, so it carries no
guard and Claude may propose it.
Had it scaffolded or committed something on the spot, the front-matter
would carry one line more:

```
disable-model-invocation: true
```

The row in the Commands table of `CLAUDE.md`:

```
| `/<name> [slug]` | report <what> from the ledger |
```

Then `/check engine` and `/check single-source-of-truth`, and the
change is recorded and released.

## See also

- [Make a change to the forge](how-a-change-is-made.md): the chain the
  change goes through.
- [Commands](../reference/commands.md): the commands that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
