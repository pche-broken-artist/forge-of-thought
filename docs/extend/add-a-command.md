---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: c563fa4c606b880a
inputs:
  - .claude/reference/commands.md
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
`.claude/skills/<name>/SKILL.md`, invoked by the slash `/<name>`.
This page is for the person who extends the forge. It shows what the
file carries, where the command is listed, how the addition is
proved and how a command that writes waits for the word of the
principal (the person whose thinking is forged).

## Before you start

A command is added as any change of the forge is made. The page
[Make a change to the forge](how-a-change-is-made.md) describes the
chain the change goes through, and the addition is recorded and
released as any change of the forge.

Two words are kept apart. "Command" is the word for what is invoked
by slash. "Skill" names the shape of the file. Not every skill is a
command: the contracts of the reviewer agents are skills of the same
directory that nobody invokes by slash, and they have no row in the
table of commands.

Read the two smallest commands first, as models:

- `.claude/skills/ledger/SKILL.md`: a command with one optional
  argument. Its body is two short paragraphs. The first says what
  the command does and cites by path the script and the step of
  another skill it relies on. The second says what the command
  writes.
- `.claude/skills/end/SKILL.md`: a command without arguments. Its
  body opens with one sentence on what the command is for and what
  it writes, then gives numbered steps. Where a step touches what
  another command or a section of `CLAUDE.md` owns, it names the
  owner and repeats nothing of it.

The terms of the forge on this page, such as roster, round and
render, each stand in one line in the
[Glossary](../reference/glossary.md).

## The files

| File | What you do |
|---|---|
| `.claude/skills/<name>/SKILL.md` | You create it. It is the command: a front-matter and a body. |
| one file per member, in a directory beside `SKILL.md` | You create them only where the command dispatches over a roster. |
| `.claude/reference/commands.md` | You add one row: the command with its arguments, and its purpose in a line. |

The skill file alone makes the command, and no other file registers
it. The table of commands lists it. `CLAUDE.md` names the table and
carries no table of its own.

## Steps

### 1. Choose the name

The name of the directory is the name of the command:
`.claude/skills/<name>/SKILL.md` gives `/<name>`.

Choose a name that does not collide with a built-in command of
Claude Code. `/init` and `/help` are built-ins of Claude Code. The
forge's command for the first run is therefore named `/setup`, and
its manual is named `/man`.

The page [Commands](../reference/commands.md) lists the commands
that exist, and with them the names already taken.

### 2. Decide whether the command is guarded

A guarded command starts only on the principal's word, never on
Claude's judgement. What the command does to files decides it:

- A command that changes files the moment it runs, with no round and
  no `write` in between, is guarded. A round is a working
  conversation whose result is written once, at its end, on the
  principal's word `write`. The commands that write, scaffold,
  commit or regenerate are of this kind, such as `/save`, `/release`
  and `/render`.
- A command that writes only at the end of a round, on the
  principal's word, needs no guard. The word is already in its
  procedure.
- A command that files the immutable record of a run the principal
  asked for needs no guard, for the same reason.
- A command that shows a state map, a state report or a roster, such
  as `/forge`, `/ledger` or the bare `/check`, is Claude's to start.
  Claude is meant to propose them.

The answer adds nothing to the file. No command of the forge carries
`disable-model-invocation` (the field of the harness that blocks
Claude from invoking a skill). The harness is Claude Code (the
program that loads the skills and shows the commands). Every skill
is model-invocable: Claude can invoke it. Do not add the field.

What holds a guarded command back is conduct:

- The principal invokes the command by slash, or asks for it in
  words.
- Asked in words, Claude invokes the command as a skill, through the
  Skill tool of the harness. It never replays the steps by hand from
  the text of the skill.
- Behind this conduct stand the step-by-step method (such a step
  runs on the principal's word) and the wall on git (git is touched
  through the scripts in `scripts/`, never directly).

Why the guard is conduct and not a field of the harness is explained
in [How the rules are held](../about/how-the-rules-are-held.md).

### 3. Write the skill

Create `.claude/skills/<name>/SKILL.md` with a front-matter and a
body.

The front-matter carries two fields:

- `description`: what the command does, in one line. The
  descriptions of all commands stay in Claude's context at all
  times. The body loads only when the command is invoked.
- `argument-hint`: the arguments of the command, always in quotes.
  The `end` skill takes no arguments and carries no hint.

The body holds the command itself:

- It says what the command does and what it writes. Both models say
  in one sentence what the command writes and what it leaves alone.
- It describes the command's own job and nothing else.
- It cites every mechanism of another by path and adds nothing to
  how that mechanism runs. A script is cited by the line that runs
  it, such as `python scripts/<script>.py <slug>`. A step of another
  skill is cited by the path of the skill and the step. A rule of
  `CLAUDE.md` is cited by its section.
- It performs nothing directly that a script, a command or an agent
  exists for:
  - git outside the scripts in `scripts/`
  - a conversion outside `doc2md.py`
  - a render outside `/render`
  - a review outside the reviewer agents
  - a check outside the check agents

A one-line reminder at the point of action that names its owner is
not a restatement. It may stay.

You should now see the harness show `/<name>` with your description.
Where it shows the first line of the body instead, the front-matter
did not parse. An unquoted hint of two bracketed items in a file
with CRLF line endings fails this way.

### 4. Add supporting files where the command dispatches over a roster

A command dispatches over a roster where its argument names one
member of a set and each member has a file of its own. Two commands
of the forge show the shape:

- `/forge`: one definition per state,
  `.claude/skills/forge/states/<state>.md`
- `/recipe`: one file per genre,
  `.claude/skills/recipe/genres/<genre>.md`

Put the files of the members in a directory beside `SKILL.md`, as
these two do. A supporting file is read by path and is registered
nowhere. It carries a description and no registration field.

### 5. Add the row

Add one row to the table in `.claude/reference/commands.md`. The
first column holds the command with its arguments, in a code span.
The second column holds the purpose of the command in a line. One
row of the table shows the shape:

```markdown
| `/ledger [slug]` | state report from the ledger |
```

The ledger is the file that holds the state of a project. A script
makes it.

Write the arguments as the other rows write them: square brackets
around an argument that may be left out, angle brackets around one
that must be given. Where the bare command does something of its
own, the purpose says so, as in `bare = the check roster`.

The row is one line. What the command does in full is said by its
skill, and the row repeats none of it.

## Prove it

Two checks prove the addition. A check verifies conformance with the
conventions. It judges neither the quality of a document nor the
thinking in it.

```
/check engine
```

The engine check verifies the core of the engine (`CLAUDE.md`, the
templates, the skills, the agents and the scripts) against itself
and against the intent of the forge (the document that holds its
design positions). For a new command it compares the table of
commands with the skills in `.claude/skills/*/SKILL.md`, the
contracts of the reviewer agents excepted. A skill without a row
shows there, and so does a row without a skill. The check takes
minutes at most, and a release can afford it every time.

You should now see a report that raises nothing about `/<name>`: the
table and the skills agree.

```
/check single-source-of-truth
```

This check reads the whole operating layer of the engine, never a
changed part of it:

- `CLAUDE.md`
- every skill, with its supporting files
- every agent
- every template
- the help headers of the scripts

It holds the rule that one mechanism lives in one place:

- A restatement is a finding: the same steps, rules or shape in two
  places, whatever the wording. The fix is a reference to the owner
  and the deletion of the copy.
- A direct operation is verified too: no skill performs directly
  what a script, a command or an agent exists for.

The check is long by design. It runs on the principal's word. It
fits before a major version or after a round on the operating layer,
not at every release. The first line of its report says how many
files it read.

You should now see a report with no finding on
`.claude/skills/<name>/` or on the new row.

## Record and release

The addition is recorded and released as any change of the forge.
The steps are on the page
[Make a change to the forge](how-a-change-is-made.md).

Two things belong to a new command in particular:

- The intent of the forge names the guarded commands one by one. A
  guarded command joins that list in the same change.
- The README carries the same set of commands as the table. It is a
  render (a file regenerated from its recipe), and the release
  regenerates it after the engine check. A README that does not yet
  show the new command is no finding of that check.

## A worked example

A new command `/<name>` takes an optional project slug and one
option. It reads the state of a project through a script and reports
it.

1. The name `<name>` is no built-in of Claude Code and no row of the
   table of commands.
2. The command changes no file the moment it runs. It is not
   guarded.
3. The file `.claude/skills/<name>/SKILL.md`:

   ```markdown
   ---
   description: <What the command does, in one line>
   argument-hint: "[slug] [--option value]"
   ---

   <What the command does for the project named, and what it
   writes.>

   1. <A step of the command's own.>
   2. <A step another mechanism owns, cited and not retold: `python
      scripts/<script>.py <slug>`, or step N of
      `.claude/skills/<other>/SKILL.md`.>
   3. <What the command reports at the end.>
   ```

4. The command dispatches over no roster. It has no supporting
   files.
5. The row in `.claude/reference/commands.md`:

   ```markdown
   | `/<name> [slug] [--option value]` | <the purpose of the command in a line> |
   ```

6. The proof, typed one after the other:

   ```
   /check engine
   /check single-source-of-truth
   ```

A command `/<name>` that regenerated a file the moment it ran would
have the same front-matter and the same kind of row. No field would
be added. The principal would type `/<name> <slug>` or ask for it in
words, and Claude would invoke the skill through the Skill tool on
that word alone.

## See also

- [Make a change to the forge](how-a-change-is-made.md): the chain
  the change goes through.
- [How the rules are held](../about/how-the-rules-are-held.md): why
  the guard is conduct and not a field of the harness.
- [Commands](../reference/commands.md): the commands that exist.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
