---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 0c030a4050760efe
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
whose thinking is forged) invokes by slash and that Claude invokes
through the harness. This page is for you, the extender, who wants to
add one. It says which files you make, what goes into them, how a
command that writes is kept from starting unasked, and how you prove
the addition before you record and release it. The commands that
exist today are listed on [Commands](../reference/commands.md); the
words of the forge are in the [Glossary](../reference/glossary.md).

## Before you start

A new command is a change of the forge like any other: it is made,
recorded and released the way [Make a change to the
forge](how-a-change-is-made.md) describes. Nothing on this page
replaces that chain; this page only says what is particular to a
command.

Two words are kept apart. "Command" is the word for what the user
invokes by slash. "Skill" names the file shape, and commands and the
reviewers' contracts alike are skills of the same directory; a
contract is a skill the user does not invoke.

The harness is Claude Code, the program in which Claude and the
forge's skills run. Two things of it matter here. A skill shadows a
command file of the same name, so a command is moved to the skill
shape whole, never in part. And the body of a skill loads only when
the skill is invoked, while its `description` stays in the always-on
context: the description is what Claude sees of your command before
it runs.

## The files

| File | What it is |
|---|---|
| `.claude/skills/<name>/SKILL.md` | the command: its front-matter and its body |
| `.claude/skills/<name>/<supporting files>` | only where the command dispatches over a roster: one file per member, beside the dispatcher |
| `CLAUDE.md`, the Commands table | one row: the command with its arguments, and its purpose |

The supporting files are the shape `/forge` and `/recipe` use: the
state files of `/forge` live at
`.claude/skills/forge/states/<state>.md` and the genre files of
`/recipe` at `.claude/skills/recipe/genres/<genre>.md`. They are read
by path, registered as nothing, and carry a description and no
registration field. A command with no roster has no supporting
files.

## Steps

1. **Choose the name.** The name must not collide with a built-in
   command of Claude Code. The forge's first-run command is `/setup`
   and not `/init`, because `/init` is a built-in of Claude Code that
   generates a `CLAUDE.md` and the collision would send a newcomer
   to the wrong action. The manual is `/man` and not `/help`, because
   `/help` is a built-in.

2. **Write the front-matter.** It carries `description`, one line
   that says what the command does for the person, and, where the
   command takes arguments, `argument-hint`. The hint is always
   quoted. The reason: a front-matter with CRLF line endings and an
   unquoted hint of two bracketed items fails to parse, and the
   harness then shows the body's first line as the description. A
   command without arguments carries no hint; `/end` is the model.

3. **Write the body.** The body says what the command does, in the
   order it does it. Where the command needs a mechanism another
   command, a script or an agent already has, it cites that mechanism
   by path and adds nothing of its own to how it runs. One mechanism
   lives in one place and is used from there, because two copies of
   a procedure drift, and the copy without a rule silently loses it.
   A one-line reminder at the point of action that names its owner
   is not a restatement; steps, rules or a shape repeated are. The
   two smallest commands show the shape. `/ledger` is a body of two
   short paragraphs: it runs the ledger script by its path, cites
   the one procedure for the report by the path of the `/forge`
   skill and its step, and says it is read-only but for the file the
   script writes. `/end` is a description with four numbered steps:
   it writes nothing, runs nothing but the status script by its
   path, and makes every remedy an offer.

4. **Decide whether the command is guarded.** No command of the forge
   carries the harness field `disable-model-invocation`: every skill
   is model-invocable. What separates a guarded command from the
   rest is what it does to the disk. A command that writes,
   scaffolds, commits or regenerates changes files the moment it
   runs, with no round and no `write` in between; such a command
   starts only on the principal's word and never on Claude's
   judgement. The principal invokes it by slash, or asks for it in
   words and Claude invokes the skill itself through the harness's
   Skill tool, never its steps replayed by hand from the definition.
   A command that writes only at the end of a round on the
   principal's word, or that files the immutable record of a run he
   asked for, needs no guard, because the word is already in the
   procedure. Maps, reports and rosters stay Claude's to start,
   since it is meant to propose them. The guard is conduct: the
   step-by-step method, by which every action needing consent
   arrives as one step and runs on the principal's word, and the
   wall on git, the hook that denies Claude every write of git and
   names the script to use. Why the guard is conduct and not a field
   of the harness is said on [How the rules are
   held](../about/how-the-rules-are-held.md); in short, the field
   did not make Claude wait for the word. It made Claude mimic the
   command outside the skill, where the principal could not see it,
   and the mimicry became its standard. So a guarded command says in
   its body that it starts on the principal's word, and nothing in
   its front-matter blocks the model from it.

5. **Add the row to `CLAUDE.md`.** The Commands table of `CLAUDE.md`
   has one row per command: the command with its arguments in
   backticks, and its purpose in a few words. What the command does
   in full stays in its skill; the table only points. `/man
   <command>` prints the skill, so the row needs no more than the
   purpose.

6. **Add the supporting files**, where the command dispatches over a
   roster, one per member, beside the dispatcher.

## Prove it

Two checks are run, each on the principal's word.

```
/check engine
```

The `engine` check verifies the core against itself: the Commands
table of `CLAUDE.md` against the skills on disk in
`.claude/skills/*/SKILL.md`, the reviewers' contracts excepted, so a
row without a skill or a skill without a row is a finding. It also
verifies the core against the forge intent, and that the README,
which is a render regenerated at the release after the check, agrees
with `CLAUDE.md` in its command set.

```
/check single-source-of-truth
```

The `single-source-of-truth` check sweeps the whole operating layer
for a procedure stated in more than one place. It is the check that
catches a body that restated another command's steps instead of
citing them. It runs on the principal's word and never at a release
on its own, so that the rule costs a release nothing and the sweep
is honest when it runs.

## Record and release

The addition is recorded and released as any change of the forge:
the chain is on [Make a change to the
forge](how-a-change-is-made.md). The README carries the table of
commands as a render, regenerated at the release, so the new row
reaches the README through the release and never by hand.

## A worked example

A command `/<name> [slug]` that reads a project and reports, nothing
written. Its file, `.claude/skills/<name>/SKILL.md`:

```
---
description: <one line: what /<name> does for the person>
argument-hint: "[project-slug]"
---

<What the command does, step by step. Where it needs a mechanism of
another command, the path: "as `.claude/skills/<other>/SKILL.md`,
step N, says". Where it runs a script: "run
`python scripts/<script>.py <slug>`".>

<What it writes, or that it writes nothing.>
```

The row in the Commands table of `CLAUDE.md`:

```
| `/<name> [slug]` | <the purpose in a few words> |
```

Because `/<name>` only reports, it needs no guard and Claude may
start it. Had it written a file the moment it ran, its body would say
that it starts on the principal's word, and its front-matter would
still carry no field that blocks the model.

Then `/check engine` and `/check single-source-of-truth`, and the
change is recorded and released.

## See also

- [Make a change to the forge](how-a-change-is-made.md): the chain
  the change goes through.
- [How the rules are held](../about/how-the-rules-are-held.md): why
  the guard is conduct and not a field of the harness.
- [Commands](../reference/commands.md): the commands that exist.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
