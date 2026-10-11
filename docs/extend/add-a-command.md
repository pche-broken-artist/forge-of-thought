---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 3a4160feb51da5ae
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

A command of the forge is a skill: one file,
`.claude/skills/<name>/SKILL.md`, that the principal (the person
whose thinking is forged) invokes by typing `/<name>`. This page is
for the extender who wants to add one. It says which files the
addition touches, what the front-matter of the skill must carry,
when the command is guarded so that Claude cannot start it on its
own judgement, and how the addition is proved. The commands that
exist today are listed in [Commands](../reference/commands.md); the
words of the forge are in the [Glossary](../reference/glossary.md).

## Before you start

A new command is a change to the forge. It goes through the same
chain as every other change, which is described in
[Make a change to the forge](how-a-change-is-made.md): the addition
is recorded and released as any change of the forge.

Choose the name first. The name must not collide with a built-in
command of Claude Code (the harness, that is the program Claude runs
in). The forge keeps two examples of such a choice: its first-run
command is `/setup` and not `/init`, because the built-in `/init`
generates a `CLAUDE.md` and the collision would send a newcomer to
the wrong action at the most sensitive moment; its manual is `/man`
and not `/help`, because `/help` is a built-in.

Know the words. "Command" is the word for what the principal invokes
by slash. "Skill" names the file shape; commands and the contracts
of the reviewers are skills alike, but a contract is not invocable
by the principal.

## The files

- `.claude/skills/<name>/SKILL.md`: the command itself, one file
  with a front-matter and a body.
- `.claude/skills/<name>/<group>/<member>.md`: supporting files,
  only where the command dispatches over a roster. The state files
  of `/forge` and the genre files of `/recipe` are the two cases the
  forge has (`.claude/skills/forge/states/<state>.md`,
  `.claude/skills/recipe/genres/<genre>.md`). A supporting file is
  read by path, registered as nothing, carries a description and no
  registration field, and needs no guard.
- `CLAUDE.md`, section Commands: one new row in the table, the
  command in the first column with its arguments, its purpose in
  the second. The engine check verifies this table against the
  skills on disk and the README against the table. `/man <name>`
  prints the skill itself, since the manual is a reader of the
  forge's definitions and never a text of its own.

A skill shadows a command file of the same name. So a command lives
as a skill whole, never as a command file beside a skill.

## Steps

1. Create `.claude/skills/<name>/SKILL.md` with its front-matter.
   The front-matter carries:
   - `description`: one line that says what the command does for the
     person and, where the command takes an optional argument, what
     the bare form does (the Commands table writes this as
     "bare = the lens roster", "bare = sweep sources/").
   - `argument-hint`: the arguments, always quoted, as in
     `argument-hint: "[project-slug]"`. A command without arguments
     carries no hint. The quoting matters: a front-matter with CRLF
     line endings and an unquoted hint of two bracketed items fails
     to parse, and the harness then shows the first line of the body
     as the description.
   - `disable-model-invocation: true`, only where the command is
     guarded (step 2).

2. Decide whether the command is guarded. The criterion is what the
   command does to files the moment it runs:
   - A command that changes files the moment it runs, with no round
     and no `write` in between (a write, a scaffold, a commit, a
     pull, a regeneration), is guarded: it carries
     `disable-model-invocation: true`, so that Claude cannot start it
     on its own judgement. The principal invokes it by slash, or
     asks for it in words and Claude follows the skill read by path.
     The guarded commands of the forge are `/save`, `/release`,
     `/pull`, `/spinoff`, `/setup`, `/new-project`, `/new-artefact`,
     `/import-project`, `/ingest`, `/render`, `/publish` and
     `/document`.
   - A command that writes only at the end of a round on the
     principal's word, or files the immutable record of a run he
     asked for, needs no guard. Because the principal's word is
     already in the procedure, the guard would add nothing.
   - Maps, reports and rosters (`/forge`, `/ledger`, `/check`,
     `/critique`, `/challenge`, `/research`, bare `/recipe`) stay
     Claude's to start, since Claude is meant to propose them. They
     carry no such field. `/end` is the model of such a report: it
     writes nothing, runs nothing but the status script, and every
     remedy it names is an offer.

   The guard has one side effect worth knowing. The descriptions of
   the guarded commands leave the always-on context of Claude. The
   body of a skill loads only when the command is invoked, guarded
   or not, so a new command costs the conversation no context until
   it runs.

3. Write the body. The body says what the command does, in order
   where there are steps. Where the command needs a mechanism that
   another command, skill, script or agent already has, the body
   cites that mechanism by path and adds nothing of its own to how
   it runs. The rules of a mechanism (its isolation, its wrapping,
   its provenance, what it may read) are written once, in the
   mechanism's own definition. Restating a procedure in a second
   place is a defect. Because two copies drift, and the copy without
   a rule silently loses it. A one-line reminder at the point of
   action that names its owner is not a restatement.

   The `ledger` skill is the smallest model of this: its whole body
   says that the report is made as step 3 of the bare `/forge` map
   in `.claude/skills/forge/SKILL.md`, that this command is the door
   to a ledger-only reading, that it is read-only, and that
   reconciling the ledger with reality belongs to `/check light`.
   Nothing of how the report is made stands in the `ledger` skill.

4. Where the command dispatches over a roster, add the supporting
   files beside it, one per member, each carrying a description and
   no registration field.

5. Add the row to the Commands table of `CLAUDE.md`. The purpose in
   the second column is one line; where the command has a bare
   form, the row says what bare means.

You should now see `/<name>` among the commands the harness offers,
and `/man <name>` should print the skill.

## Prove it

Type the checks as they stand:

```
/check engine
```

The engine check verifies the Commands table of `CLAUDE.md` against
the skills on disk in `.claude/skills/*/SKILL.md` (the reviewers'
contracts excepted), the README against `CLAUDE.md` for the same
command set, and every skill an agent names in its front-matter
against `.claude/skills/<name>/SKILL.md`, since Claude Code skips a
missing one silently. Where the new command runs a script, the check
also verifies that every file in `scripts/` is described in
`CLAUDE.md`.

```
/check single-source-of-truth
```

The single-source-of-truth check sweeps the whole operating layer
for restatements: a procedure of another mechanism repeated in the
new skill's body is a finding. This check is expensive by design and
runs on the principal's word, never at a release on its own; a round
on the operating layer, such as a new command, is one of the moments
it is meant for.

A check that finds nothing files nothing. A finding is settled by
walkthrough (the method that works a list one item per message,
each closed with a verdict).

## Record and release

The addition is recorded and released as any change of the forge:
the chain it goes through, what it touches beyond the files above
and how it is saved and released are said in
[Make a change to the forge](how-a-change-is-made.md). The forge
counts the cost of a new command as one more row of the Commands
table.

## A worked example

A report command, Claude's to start, that takes an optional project
slug. The file is `.claude/skills/<name>/SKILL.md`:

```
---
description: Report <what the command reports>; bare = every project
argument-hint: "[project-slug]"
---

Report <what> for project $0 (or for every project if none given).
The reading of the ledger is the bare `/forge` map's, step 3 in
`.claude/skills/forge/SKILL.md`; this command is the door for
<what> alone.

Read-only. Where a discrepancy with the files on disk is obvious
while reporting, name it and point to `/check light`.
```

The same command, were it to change files the moment it runs, would
carry one more line in its front-matter and nothing else would
differ:

```
---
description: <What the command changes on disk>; bare = every project
argument-hint: "[project-slug]"
disable-model-invocation: true
---
```

The row in the Commands table of `CLAUDE.md`:

```
| `/<name> [slug]` | <what the command does>; bare = every project |
```

Then `/man <name>` prints the skill, `/check engine` finds the row
and the skill in agreement, and `/check single-source-of-truth`
finds no procedure of another mechanism restated in the body.

## See also

- [Make a change to the forge](how-a-change-is-made.md): the chain the change goes through.
- [Commands](../reference/commands.md): the commands that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
