---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 9c725dff308552bb
inputs:
  - CLAUDE.md#Prime directives
  - CLAUDE.md#Working methods
  - .claude/settings.json
  - scripts/hook-walkthrough.py
  - projects/forge/10-intent.md#POS.0930
  - projects/forge/10-intent.md#POS.0950
  - projects/forge/10-intent.md#POS.1030
  - projects/forge/10-intent.md#POS.1070
  - projects/forge/10-intent.md#POS.1090
  - projects/forge/10-intent.md#POS.1170
  - projects/forge/10-intent.md#POS.1190
  - projects/forge/10-intent.md#POS.1200
  - projects/forge/40-solution-design.md#The instruction layer
---

# How the rules are held

The rules of the forge are held in files, and each file reaches
Claude at the moment its rule applies: one core that is always
present, the rest read when its situation arises, a hook that
repeats what a long conversation wears down, and a harness that
enforces what it can. This page explains how the forge keeps its
rules in force across a long conversation and inside a subagent,
and why it is built that way. It is written for the one who extends
the forge and for the one who evaluates it.

## What it is

The forge is run by Claude, the assistant, inside Claude Code: the
harness, that is the program that loads the instruction files, runs
the tools and starts the subagents. A session is one conversation
between the principal (the person whose thinking is being forged)
and Claude, from its start to its end. A subagent is an isolated run
of Claude that sees only the brief it is given, never the working
conversation; the reviewers, the render and the documentation run
as subagents.

The rules live in five places, each with its own reach.

- `CLAUDE.md` at the engine root: the universal core. The harness
  loads it into every session and into every subagent. It carries
  only what must hold everywhere: the roles, the prime directives,
  the working methods in short, the document kinds, the chain, the
  layout, persistence, versioning, the ID scheme, the reviewers, the
  ledger (the single source of truth for a project's state) and the
  list of commands.
- The rest of the operating layer, the files listed on the page
  [What the forge is made of](../extend/what-it-is-made-of.md): the
  definition of a command (its skill), the definition of an
  artefact, a template, an agent file, a script. Each is read when
  its situation arises, never before.
- `CLAUDE.local.md` at the engine root: the instance facts, that is
  who the principal is, by role, and what language the conversation
  runs in. It is kept out of the repository, created from
  `templates/CLAUDE.local.md` and filled by `/setup` on a new
  machine.
- The per-prompt hook: `scripts/hook-walkthrough.py`, configured in
  `.claude/settings.json` and run by the harness at every prompt.
- The settings of the harness in `.claude/settings.json`: the deny
  rules and the hook. The page [Configuration](../reference/configuration.md)
  gives them exactly.

Beside these five places stand three rules on what is not a place
for the forge's rules: the assistant's private memory, a second copy
of a procedure, and a manual written apart from the definitions.

## How it works

### One mechanism lives in one place

Whatever the forge has a procedure for, a command, a skill, a script
or an agent, is used through its own definition whenever its
situation arises. A command that needs another's mechanism cites it
by path and adds nothing of its own to how it runs. The rules of a
mechanism, such as its isolation, its wrapping, its provenance and
what it may read, are written once, in its own definition. A
procedure stated in two places is a defect. Where a shape had no
owner at all, it gets a template rather than a second description.
A one-line reminder at the point of action that names its owner is
not a restatement. The `single-source-of-truth` check sweeps the
whole operating layer for restatements, on the principal's word.

The walkthrough is the first instance of the pattern. A walkthrough
is the way any list of items needing the principal's decision is
worked: one item per message, in order of weight, every proposition
closed with the verdict line `(a)ccept / (m)odify / (r)eject /
(p)ark`. `CLAUDE.md` carries that rule in short and a pointer. The
full shape, of the item, of the verdict, of the elicitation
interview and of the write-up, lives in
`.claude/skills/walkthrough/SKILL.md`, read whenever a walkthrough
or an interview runs. The skill is not a command.

### A hook repeats what must hold through a long conversation

`.claude/settings.json` carries one `UserPromptSubmit` hook. The
harness runs it at every prompt and adds what it prints to the
context of that turn. The hook is started as `python` with
`${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.py` as its one
argument, in exec form. The placeholder names the root the session
started in, and the exec form hands the path to the program without
a shell. The script takes no arguments; its one prerequisite is
Python 3.8 or newer on PATH as `python`.

The hook prints five lines, copied here as the script has them.

- `Walkthrough rule: one item per reply - acknowledge the last verdict, put one item forward, close a proposition with '(a)ccept / (m)odify / (r)eject / (p)ark', stop. A question from the principal keeps the item open.`
- `When a walkthrough or an interview is running, work by .claude/skills/walkthrough/SKILL.md.`
- `Tools: where the forge has a script (scripts/*.py), use the script, never the raw tool. git only through scripts/forge-*.py, reading state included.`
- `Own commands: before running anything of your own that is not plain reading, say what it does and why, and wait for the principal's yes.`
- `Consent: write, run and change nothing that was not agreed and approved. A yes covers exactly what was asked, never its consequences.`

The first two lines are the walkthrough: the one-item rule with the
verdict line, and the pointer to the skill. The other three are
conduct: the scripts over the raw tool, the question before a
command of Claude's own, and the limit of a yes. A hook is context,
not enforcement: it puts the rule in front of Claude at every turn,
and nothing more.

### The harness enforces what it can

The deny rules of `.claude/settings.json` are a wall of the harness,
not conduct alone. Four stand there.

- `Read(~/.ssh/**)` and `Read(~/.aws/**)`: Claude cannot read the
  SSH and AWS directories under the home directory.
- `Bash(git *)` and `PowerShell(git *)`: Claude cannot run git from
  a shell. The scripts `scripts/forge-*.py` are its only door to
  git, reading state included.

The deny rules bind the forge, not the principal: his own git from
the shell is his. Web access is approved by the principal per
domain. The same settings file switches the commit attribution off:
a commit carries no `Co-Authored-By` and no `Claude-Session` trailer,
and its message is the one the principal confirmed, word for word.

A command that changes files the moment it runs is guarded by the
harness, so that Claude cannot start it on its own judgement. The
guarded commands are `/save`, `/release`, `/pull`, `/spinoff`,
`/setup`, `/new-project`, `/new-artefact`, `/import-project`,
`/ingest`, `/render`, `/publish` and `/document`. The principal
invokes such a command by slash, or asks for it in words, and Claude
then follows the command's definition read by path. What separates a
guarded command from the rest is the moment of the write. A guarded
command writes, scaffolds, commits or regenerates as soon as it
runs, with no round and no `write` in between. A command that writes
only at the end of a round, on the principal's word, needs no guard.
A command that files the immutable record of a run the principal
asked for needs no guard either, because the word is already in the
procedure. Maps, reports and rosters stay Claude's to start, since
Claude is meant to propose them: the state map `/forge`, `/ledger`,
`/check`, `/critique`, `/challenge`, `/research` and bare `/recipe`.

### What a subagent carries

A subagent sees the session's whole context: `CLAUDE.md` as the
session read it, `CLAUDE.local.md`, and the assistant's memory. It
may take the session's copy of a file for the file on disk, and the
copy may be older than the file. Three rules follow.

- Every agent that writes an outward-facing file says in its own
  definition that instance facts are not material and that every
  input is read from disk, in that run.
- The generated files are scanned mechanically before they are kept.
- Only what must be always-on and is harmless in a public report
  lives in `CLAUDE.local.md`. `CLAUDE.md` names the principal and the
  conversation language only as things that exist, never by value.
  The git identities, that is names, e-mail addresses and hosts,
  live in the user's own git configuration outside the engine, and
  the scripts carry no URL and no identity. Instance facts are
  forbidden in a reviewer's report.

### One model for the whole forge

Every command, every chain state and every reviewer runs on the
session model. The session model is chosen in one deliberate place,
`.claude/settings.local.json`, a gitignored file of the instance.
Speed is bought with context, not with weaker models: a render, a
check and a reviewer each run in an isolated subagent that sees only
its inputs, and the working conversation is spent on verdicts. Two
exceptions are named. The headless conversions behind `/publish`
have no session model, so each carries an explicit default of its
own as a parameter. The documentation writer writes a mirrored page,
one that leaves the model no room, on a faster model, and a derived
page on the session model; the choice is made by the page's entry
in the documentation map, never per run.

### The forge's behaviour never lives in memory

Claude Code keeps a per-directory memory outside the repository.
Whatever Claude learns there about how the forge should work, a
working method, a rule of a command or a convention, is written into
`CLAUDE.md`, the commands or the templates and removed from memory.
Memory is left with what is personal to one principal: his idiom and
his private choices. Instance facts go to `CLAUDE.local.md`.

### The forge explains itself

`/man [command | method]`, alias `/manual`, is the forge's manual. It
is a reader of the definitions, never a text of its own. It is named
after the Unix manual, because `/help` is a built-in of Claude Code.

## Why

The core is loaded into every session because that is what the
harness does with the file `CLAUDE.md` at the root; the intent
records no alternative. What the core costs is its size. So the core
carries only what must hold everywhere, and a rule of one artefact
lives in that artefact's definition. Always-on is one sentence and a
pointer; the detail is a file read when its situation arises.

One mechanism lives in one place because two copies drift, and the
copy without a rule silently loses it. The sweep that looks for
restatements runs on the principal's word and never at a release on
its own, so that the rule costs a release nothing and the sweep is
honest when it runs.

The hook exists because text loaded once dissolves as a conversation
grows: a rule that stands fully in context at the first message is
no longer in force at the fortieth. A rule that must hold through a
long conversation is therefore not trusted to `CLAUDE.md` alone. A
hook is the nearest thing to a wall the harness offers for a rule of
conduct, and it is still context, not enforcement.

The deny rules and the guarded commands exist so that the guarantee
of Step by step, the method by which any action needing consent
arrives as one step and runs on the principal's word, rests on the
harness as well as on `CLAUDE.md`. The criterion of a guard is the
moment of the write: where a round and the word `write` already
stand between Claude and the file, the procedure holds the consent,
and a guard would add nothing.

The instance facts live in one gitignored file at the root, against
instance facts in the engine's own files. The cost is that the file
reaches every subagent, the isolated reviewers included; so it must
stay small and harmless. An agent reads its inputs from disk and the
generated files are scanned because a subagent may take the
session's copy for the file.

One model for the whole forge means that the strongest model the
forge runs on is a decision and never an accident of a pin that has
aged. Per-command pinning to a faster model is rejected: the routine
commands are a small share of the work and slow for the size of the
context they carry, not for the model, and every pin is a convention
to keep. The documentation writer is the exception the deferral
waited for: a mirrored page leaves the model no room, and a derived
page does not.

The behaviour lives in the engine and never in memory so that every
instance of the forge behaves the same, and a new user meets the
same forge as the principal.

The manual reads the definitions so that it can never drift from
them. It exists for the newcomer's first hour and for the reader who
opens the repository.

## A worked example

The principal opens a session in the engine. The harness loads
`CLAUDE.md`; the walkthrough rule is there in short, with the pointer
to its skill. The principal runs `/critique clarity my-project`. The
critic runs as a subagent, reads the project's documents from disk,
and returns a report in which no instance fact stands. The command
files the report and ends by offering a walkthrough.

The walkthrough begins. Claude reads
`.claude/skills/walkthrough/SKILL.md` and puts the first finding
forward, closed with the verdict line. The conversation grows to
many messages. At every one of them the hook prints its five lines,
so the one-item rule and the three lines of conduct stand in front
of Claude at the fortieth message as they did at the first. Claude
puts forward no second item before the verdict on the first.

At the round's end the principal types `write`. Claude reflects the
whole round back and, on his yes, writes the intent of `my-project`
once and appends the records to its history. Nothing in that step
needs a guard: the round and the word stood between Claude and the
file.

The principal then asks for a save. `/save` is guarded, because it
commits the moment it runs; Claude could not have started it on its
own judgement. The principal invokes `/save my-project`, or asks in
words, and Claude follows `.claude/skills/save/SKILL.md` read by
path. The commit is made through `scripts/forge-save.py`; a raw
`git` call from the shell is denied by the harness. The commit
message is the one the principal confirmed, with no trailer.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): the files of the operating layer.
- [Configuration](../reference/configuration.md): the settings, exactly.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
