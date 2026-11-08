---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 1dd2a87c0311d799
inputs:
  - CLAUDE.md#Commands
  - .claude/skills/ledger/SKILL.md
  - .claude/skills/end/SKILL.md
  - .claude/agents/check-engine.md
  - .claude/agents/check-single-source-of-truth.md
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
whose thinking is being forged) invokes as `/<name>`, and one row in
the Commands table of `CLAUDE.md`. This page is for the extender who
wants to add one. It says which files a new command consists of,
what each must carry, how a command that writes is kept from
starting on Claude's own judgement, and how the addition is proved,
recorded and released.

## Before you start

A new command is a change of the forge like any other. It goes
through the chain described in
[Make a change to the forge](how-a-change-is-made.md): it is recorded
in the forge's own project and released with the next release, never
dropped into `.claude/skills/` alone.

Two words the page uses: the *harness* is Claude Code, the program
that runs Claude and in which the skills, the agents and the hooks
are its mechanisms; a *skill* is the file shape of a command, and
"command" stays the word for what the principal invokes by slash.
The forge's other terms are one line each in the
[Glossary](../reference/glossary.md).

Before you write, look at the commands that exist, listed in
[Commands](../reference/commands.md). A command that needs a
mechanism another command, a script or an agent already has does not
describe that mechanism again: it cites the owner by path. A
procedure stated in two places is a defect, because the two copies
drift and the copy without a rule silently loses it.

## The files

A command consists of these files.

- `.claude/skills/<name>/SKILL.md`: the skill. Its front-matter
  carries `description`, the one line the roster and the always-on
  context show, and, where the command takes arguments, a quoted
  `argument-hint`. Its body says what the command does, step by step
  where there are steps, and cites every mechanism of another by its
  path.
- Supporting files beside it, only where the command dispatches over
  a roster: `.claude/skills/<name>/<kind>/<member>.md`, one file per
  member, read by path, registered as nothing, carrying a description
  and no registration field. The state files of `/forge` and the
  genre files of `/recipe` are the two examples the forge has.
- One row in the Commands table of `CLAUDE.md`: the command with its
  arguments in the first column, its purpose in one line in the
  second.

No command carries a field of the harness that blocks the model from
invoking it. Every skill is model-invocable, and the descriptions of
all commands stay in the always-on context.

## Steps

1. **Choose the name.** The name must not collide with a built-in of
   Claude Code, because a skill of a built-in's name would send a
   newcomer to the wrong action: `/init` and `/help` are built-ins,
   which is why the forge's first run is `/setup` and its manual
   `/man`. A skill shadows a command of the same name, so a name
   already taken replaces the old command whole.

2. **Write the skill.** Create `.claude/skills/<name>/SKILL.md`. Put
   `description` in the front-matter. Where the command takes
   arguments, add `argument-hint` and quote its value: an unquoted
   hint of two bracketed items in a front-matter with CRLF line
   endings fails to parse, and the harness then shows the body's first
   line as the description. In the body, say what the command does
   for the person. Where it needs another's mechanism, write the path
   of that owner and nothing of how the owner runs. A one-line
   reminder at the point of action that names its owner is not a
   restatement; the same steps, rules or shape written a second time
   is.

3. **Decide whether the command is guarded, and say so in the body.**
   A guarded command is one that changes files the moment it runs,
   with no round and no `write` in between: it writes, scaffolds,
   commits or regenerates. Such a command starts only on the
   principal's word, never on Claude's judgement. The principal
   invokes it by slash, or asks in words and Claude invokes the skill
   itself, through the harness's Skill tool. Claude never replays the
   skill's steps by hand. The guard is conduct, not a field of the
   file: the step-by-step method, by which every action needing the
   principal's consent arrives as one step and runs on his word, and
   the wall on git, by which git is touched only through the scripts
   in `scripts/`. Why the guard is conduct rather than a field is
   said in [How the rules are held](../about/how-the-rules-are-held.md).
   Two kinds of command need no guard, because the word is already in
   their procedure: one that writes only at the end of a round on the
   principal's word, and one that files the immutable record of a run
   he asked for. A map or a roster, such as `/forge`, `/ledger` or a
   bare `/check`, stays Claude's to start, since Claude is meant to
   propose them.

4. **Add supporting files only where the command dispatches over a
   roster.** Put them in a directory beside the skill, one file per
   member with a description. The skill reads them by path.

5. **Add the row to the Commands table of `CLAUDE.md`.** The table is
   the one list of the commands; what a command does in full is its
   skill's file, and `/man <name>` prints it.

Two skills of the forge show the smallest shapes. `/ledger` takes a
slug, so its front-matter has `description` and a quoted
`argument-hint`; its body is a few sentences that run a script and
cite the `/forge` skill for the one procedure of the report. `/end`
takes no argument, so its front-matter has `description` alone; its
body is a short numbered list that writes nothing and offers every
remedy.

## Prove it

Run the two checks in this order. Each is a check of the forge,
run as an isolated subagent (a reader that never sees the working
conversation), and each is started on the principal's word.

```
/check engine
```

The `engine` check verifies the core against itself: among other
things, the Commands table of `CLAUDE.md` against the skills that
exist as `.claude/skills/*/SKILL.md`, and the README against
`CLAUDE.md` for the same command set. A row without a skill, or a
skill without a row, is a finding. The README is a render regenerated
at the release, so a command missing from it is fixed in the README's
recipe, not in the README.

```
/check single-source-of-truth
```

The `single-source-of-truth` check reads the whole operating layer,
every skill and its supporting files among them, and verifies that
every rule, procedure and file shape is written in one place and
cited everywhere else. A restatement in your skill of what another
file owns is a finding; the fix is a reference to the owner and the
deletion of the copy. This check is long by design and is run on the
principal's word, not at every release: run it after the round on
the operating layer that added the command.

## Record and release

The addition is recorded and released as any change of the forge:
the chain is [Make a change to the forge](how-a-change-is-made.md).
The new command appears in the README, which is a render, at the next
release.

## A worked example

The extender adds a command `/<name>` that reports something about a
project and takes its slug.

The skill, `.claude/skills/<name>/SKILL.md`, in the shape the forge
defines (the content is a placeholder, taken from no command):

```
---
description: <What the command does, in one line>
argument-hint: "[slug]"
---

<What the command does for the person, in a few sentences or a
short numbered list. Where it needs a script, a command or an agent
that exists, it names the owner by path, such as
`scripts/<script>.py` or `.claude/skills/<other>/SKILL.md`, and says
nothing of how the owner runs.>
```

The row in the Commands table of `CLAUDE.md`:

```
| `/<name> [slug]` | <what the command does, in one line> |
```

The command only reports, so it needs no guard and Claude may start
it. Had it written a file the moment it ran, its body would say that
it starts on the principal's word, and Claude would invoke it as a
skill through the Skill tool, never replay its steps by hand.

Then `/check engine`, then `/check single-source-of-truth`, then the
change is recorded and released as
[Make a change to the forge](how-a-change-is-made.md) says.

## See also

- [Make a change to the forge](how-a-change-is-made.md): the chain
  the change goes through.
- [How the rules are held](../about/how-the-rules-are-held.md): why
  the guard is conduct and not a field of the harness.
- [Commands](../reference/commands.md): the commands that exist.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
