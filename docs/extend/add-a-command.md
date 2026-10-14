---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: 5f77bf2fcb2e34d6
inputs:
  - CLAUDE.md#Commands
  - .claude/skills/ledger/SKILL.md
  - .claude/skills/end/SKILL.md
  - .claude/agents/check-engine.md
  - projects/forge/10-intent.md#POS.1090
  - projects/forge/10-intent.md#POS.1070
  - projects/forge/10-intent.md#POS.1050
  - projects/forge/10-intent.md#POS.1190
  - projects/forge/40-solution-design.md#The commands
---

# Add a command

A command of the forge is a skill: one file
`.claude/skills/<name>/SKILL.md`, which the harness (Claude Code, the
program Claude runs in and which reads the skill files) turns into
`/<name>`. This page is for the extender who adds a new command: it
says which files to make, what the front-matter must carry, when the
command is guarded so that Claude cannot start it on its own
judgement, and how the addition is proved before it is recorded and
released.

## Before you start

A new command is a change of the forge. It goes through the chain
every change goes through: [Make a change to the forge](how-a-change-is-made.md).
The addition is recorded and released as any change of the forge;
nothing on this page replaces that chain.

Look at the commands that exist before you add one:
[Commands](../reference/commands.md). "Command" is the word for what
you invoke by slash. "Skill" is the word for the file shape; the
contracts of the reviewers are skills of the same directory and are
not commands.

Decide what kind of command it is. The kind decides whether it is
guarded:

- A command that changes files the moment it runs, with no round and
  no `write` between the call and the change. It scaffolds, commits,
  pulls, regenerates or writes at once. Such a command is guarded.
- A command that writes only at the end of a round, on the word of
  the principal (the person whose thinking is forged), or that files
  the immutable record of a run the principal asked for. Such a
  command needs no guard, because the word is already in its
  procedure.
- A map, a report or a roster. Such a command stays Claude's to
  start, because Claude is meant to propose them.

Choose a name that does not collide with a built-in of Claude Code.
The forge's first-run command is `/setup` and not `/init`, because
`/init` is a built-in that generates a `CLAUDE.md`. The forge's
manual is `/man` and not `/help`, because `/help` is a built-in.

## The files

- `.claude/skills/<name>/SKILL.md`: the command, a front-matter and
  a body.
- `.claude/skills/<name>/<group>/<member>.md`: supporting files, only
  where the command dispatches over a roster, one file per member.
  `/forge` keeps one definition per state in
  `.claude/skills/forge/states/<state>.md`; `/recipe` keeps one genre
  per file in `.claude/skills/recipe/genres/<genre>.md`. A
  supporting file is read by path, registered as nothing, carries a
  description and no registration field, and needs no guard.
- `CLAUDE.md`, section Commands: one row of the table, the command
  with its arguments and its purpose in a few words.

The two smallest commands of the forge are the models to copy the
shape from. `.claude/skills/ledger/SKILL.md` is a report of one
project or of every project, read from the ledger (the file that
holds a project's state; see the
[Glossary](../reference/glossary.md)); it takes one optional slug.
`.claude/skills/end/SKILL.md` is a report that takes no argument at
all.

## Steps

1. Create `.claude/skills/<name>/SKILL.md` and write its
   front-matter:
   - `description`: one line that says what the command does for the
     person.
   - `argument-hint`: the arguments the command takes, in quotes,
     such as `"[project-slug]"`. Every hint is quoted. A
     front-matter with CRLF line endings and an unquoted hint of two
     bracketed items fails to parse, and the harness then shows the
     body's first line as the description. Leave the field out where
     the command takes no argument, as `/end` does.
   - `disable-model-invocation: true`: only where the command
     changes files the moment it runs. With the field, the
     principal invokes the command by slash, or asks for it in words
     and Claude follows the file read by path. A report, a map or a
     roster carries no such field and stays Claude's to start. The
     description of a guarded command thereby leaves the context
     Claude carries at all times.

   You should now see a front-matter of two lines, or of three where
   the command is guarded.

2. Write the body: what the command does, in steps where it has
   steps. Where the command needs a mechanism another command, a
   script or an agent already has, cite that mechanism by path and
   add nothing of your own to how it runs. A procedure stated in two
   places is a defect: the two copies drift, and the copy without a
   rule silently loses it. The two models show the shape. `/ledger`
   says in two short paragraphs that its report is the one the bare
   `/forge` map makes, cited by step and path, and that reconciling
   the ledger with the disk belongs to `/check light`. `/end` says in
   four numbered steps what it names and offers, runs the status
   script by its path, cites `/save` and `/render` by name, and
   writes nothing.

   You should now see a body that names every other mechanism by its
   path and restates none.

3. Where the command dispatches over a roster, put one supporting
   file per member beside `SKILL.md`, each with a description, and
   let the body say that each is read by path. Skip this step for a
   command with no roster.

4. Add the row to the Commands table of `CLAUDE.md`, in the shape of
   the rows around it: the command with its arguments in a code span,
   then its purpose. The table says the purpose only. What the
   command does in full stays in the skill, and `/man <name>` prints
   it.

   You should now see one new row and nothing else changed in the
   table.

## Prove it

Run the two checks. Each runs on the principal's word; no check
starts on Claude's own judgement.

```
/check engine
```

The engine check reads `CLAUDE.md`, the templates, the skills, the
agents and the scripts and verifies the Commands table against the
skills on disk, the reviewers' contracts excepted: a row without a
skill, or a skill without a row, is a finding. It also verifies that
the README and `CLAUDE.md` name the same command set. The README is a
render, regenerated at the release after this check, so a README
that does not yet show the new command is not a finding against it.

```
/check single-source-of-truth
```

This check sweeps the operating layer for a rule stated in more than
one place. A body that restates another command's procedure instead
of citing it by path is what it finds. It runs on the principal's
word and never at a release on its own, so that the rule costs a
release nothing.

Then type `/man <name>`. You should now see the skill printed as the
forge's manual page for the new command.

## Record and release

The addition is recorded and released as any change of the forge:
[Make a change to the forge](how-a-change-is-made.md). At the
release the README is regenerated and then names the same command
set as `CLAUDE.md`, the new command among it.

## A worked example

You add `/<name> [slug]`, a report: it reads the ledger of the
project the slug names and writes nothing. It is a report, so it
carries no guard.

The file `.claude/skills/<name>/SKILL.md`:

```
---
description: Report the renders of a project and whether each is current or stale
argument-hint: "[project-slug]"
---

Report the Renders table of the ledger of the project the slug
names, or of every project when no slug is given: each render and
whether it is current or stale. Stale is what `/render` step 5
defines (`.claude/skills/render/SKILL.md`); this command cites it
and restates nothing of it.

Read-only: this command writes nothing and runs nothing.
```

Had `/<name>` changed a file the moment it ran, the front-matter
would carry a third line, `disable-model-invocation: true`.

The row in `CLAUDE.md`, section Commands:

```
| `/<name> [slug]` | the renders of a project and whether each is current or stale |
```

Then:

1. `/check engine`. You should now see no finding that names
   `/<name>`.
2. `/check single-source-of-truth`. You should now see no finding on
   the body of `/<name>`.
3. `/man <name>`. You should now see the skill printed as the
   command's manual page.
4. Record and release the change as [Make a change to the forge](how-a-change-is-made.md)
   says.

## See also

- [Make a change to the forge](how-a-change-is-made.md): the chain the change goes through.
- [Commands](../reference/commands.md): the commands that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
