---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - .claude/skills/ledger/SKILL.md
  - .claude/skills/man/SKILL.md
  - .claude/agents/check-engine.md
  - projects/forge/10-intent.md
  - projects/forge/40-solution-design.md
---

# Add a command

This page is for someone who extends the forge and wants to give it a
new slash command. It was put together from the forge's `CLAUDE.md`,
the `ledger` and `man` skills, the `engine` check, the forge intent
and the forge solution design; the steps below are derived from what
those files say about how a command is shaped, guarded, listed and
verified.

## What a command is

Every command of the forge is a skill: one file,
`.claude/skills/<name>/SKILL.md`. "Command" is the word for what you
invoke by slash; "skill" names the file shape. A skill of a given
name takes the place of a command of the same name, so a command is
moved to a skill whole, never in part.

## Steps

1. **Choose a name that does not collide with a built-in of Claude
   Code.** The forge names its commands away from the built-ins on
   purpose: `/setup` is not `/init`, because the built-in `/init`
   generates a `CLAUDE.md` and would send a newcomer to exactly the
   wrong action; `/man` is not `/help`, because `/help` is Claude
   Code's own.

2. **Create `.claude/skills/<name>/SKILL.md` with its front-matter.**
   - `description`: one line saying what the command does and, where
     the command has a bare form, what bare means.
   - `argument-hint`: always quoted, for example
     `argument-hint: "[project-slug]"`. A front-matter with CRLF line
     endings and an unquoted hint of two bracketed items fails to
     parse, and the harness then shows the body's first line as the
     description.
   - `disable-model-invocation: true` if the command writes,
     scaffolds, commits or regenerates. Such a command is guarded by
     the harness so that Claude cannot start it on his own judgement:
     you invoke it by slash, or ask for it in words and Claude follows
     its definition read by path. The guarded commands today are
     `/save`, `/release`, `/spinoff`, `/setup`, `/new-project`,
     `/new-artefact`, `/import-project`, `/ingest`, `/render` and
     `/publish`. Maps, reports and rosters (`/forge`, `/ledger`,
     `/check`, `/critique`, `/challenge`, `/research`, `/recipe`)
     carry no such field and stay Claude's to start, since he is meant
     to propose them. The reason is that the forge's rule of Step by
     step then rests on the harness as well as on `CLAUDE.md`. A
     side effect: the description of a guarded command leaves the
     always-on context.

3. **Write the body: what the command does.** Where the command needs
   a mechanism that another command, skill, script or agent already
   owns, cite it by path and add nothing of your own to how it runs.
   One mechanism lives in one place; a procedure stated in two places
   is a defect, because the two copies drift and the copy without a
   rule silently loses it. A one-line reminder at the point of action
   that names its owner is not a restatement. The smallest model in
   the forge is `.claude/skills/ledger/SKILL.md`: it points to the
   step of the `/forge` skill that owns the report, and to the `light`
   check for reconciling the ledger, rather than describing either.

4. **Put supporting files beside it if the command dispatches over a
   roster.** The state files of `/forge` and the genre files of
   `/recipe` are the pattern: they sit under the dispatcher's
   directory (`.claude/skills/forge/states/<state>.md`,
   `.claude/skills/recipe/genres/<genre>.md`), are read by path,
   register as nothing and carry a description but no guard.

5. **Add a row to the Commands table of `CLAUDE.md`.** The row gives
   the command with its arguments and its purpose. `/man` reads this
   table for its overview and prints a command's page from the skill
   itself (its `description`, its `argument-hint`, the row's purpose,
   the roster where the skill names one); the README states the same
   command set as `CLAUDE.md`. Nothing about the command needs to be
   written for `/man` separately.

## How you know it is right

- `/check engine` verifies the Commands table of `CLAUDE.md` against
  the skills actually present in `.claude/skills/`, and the README
  against `CLAUDE.md`.
- `/check single-source-of-truth` verifies that nothing in the
  operating layer restates a procedure owned elsewhere. It runs on
  your word, not at a release on its own.
- `/man <name>` shows the command's page as a user will see it.

## Record the change

A new command is a change of the forge like any other. A process
change is complete only once the forge's own intent is updated and
the README re-rendered.

## See also

- [Make a change to the forge](how-a-change-is-made.md): the chain the change goes through.
- [Commands](../reference/commands.md): the commands that exist.
