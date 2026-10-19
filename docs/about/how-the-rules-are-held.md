---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 7317c94ca34bc4a4
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

The forge holds its rules in a few layers: one core file that is
always loaded, files that are read when their situation arises, a
hook that repeats the rules that slip, and settings of the harness
that stop what they can. This page explains each layer, how the
layers work together and why the forge is built this way. It is
written for someone who extends the forge and for someone who
evaluates it. The words used here are explained in one line each in
the [Glossary](../reference/glossary.md).

## What it is

The forge is run by Claude inside Claude Code. On this page "the
harness" means Claude Code: the program that runs Claude, loads its
files and applies its settings. A "session" is one run of Claude Code
with its conversation. A "subagent" is a second Claude that the
session launches for one job and that never sees the working
conversation. The "principal" is the person whose thinking is being
forged and who decides everything about its content.

The rules of the forge reach Claude in these ways:

- The always-on core: `CLAUDE.md` at the engine root, which the
  harness loads into every session and every subagent.
- The instance file: `CLAUDE.local.md` beside it, kept out of the
  repository, which holds the facts of one installation and also
  reaches every subagent.
- Files read on demand: the skills, the agents, the templates and the
  definitions, each read when its situation arises.
- The per-prompt hook: `scripts/hook-walkthrough.py`, which repeats a
  few rules at every prompt.
- The settings of the harness: `.claude/settings.json`, whose deny
  rules and guards stop some actions outright.

The files that make up this operating layer are described in
[What the forge is made of](../extend/what-it-is-made-of.md).

## How it works

### One core, everything else read when needed

`CLAUDE.md` carries what must hold in every session and for every
subagent. That covers the roles, the prime directives, the working
methods in short, the kinds of document, the chain, the layout,
persistence, versioning, the ID scheme, the reviewers, the ledger and
the list of commands. A rule of one artefact is not in the core. It
stands in the definition of that artefact.

The core states a method in short and points to the file that holds
it in full. The walkthrough is the clearest case. A walkthrough is
the way any list of items needing the principal's decision is worked:
one item per message, each proposition closed with the verdict line.
`CLAUDE.md` carries that rule in a few lines and the pointer to
`.claude/skills/walkthrough/SKILL.md`. That skill holds the full
shape and is read whenever a walkthrough or an interview runs.

### One mechanism lives in one place

Whatever the forge has a procedure for is used through its own
definition whenever its situation arises. This holds for a command, a
skill, a script and an agent. A procedure is never described a second
time or improvised. A command that needs the mechanism of another
command cites it by path and adds nothing of its own to how it runs.
The rules of a mechanism (its isolation, its wrapping, its
provenance, what it may read) are written once, in its own
definition.

A procedure stated in two places is a defect. A one-line reminder at
the point of action that names its owner is not a second statement.
An example of such a reminder is "not under git is a fact, not a
defect (CLAUDE.md, Persistence)". Where a shape has no owner at all,
it gets a template rather than a second description. A check called
`single-source-of-truth` looks for restatements over the whole
operating layer. It runs on the principal's word, never on its own at
a release.

### A hook repeats what must hold in a long conversation

The harness can run a script at every prompt the principal sends and
add what the script prints to the context of that turn. The engine
configures one such hook in `.claude/settings.json`. It runs
`scripts/hook-walkthrough.py`. The script reads nothing, writes
nothing and takes no arguments. It prints these lines:

```
Walkthrough rule: one item per reply - acknowledge the last verdict, put one item forward, close a proposition with '(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark', stop. A question from the principal keeps the item open: answer, then close it again.
When a walkthrough or an interview is running, work by .claude/skills/walkthrough/SKILL.md.
Tools: where the forge has a script (scripts/*.py), use the script, never the raw tool. git only through scripts/forge-*.py, reading state included.
Own commands: before running anything of your own that is not plain reading, say what it does and why, and wait for the principal's yes.
Consent: write, run and change nothing that was not agreed and approved. A yes covers exactly what was asked, never its consequences.
```

The first two lines are the one-item rule of the walkthrough and the
pointer to its full shape. The last three are lines of conduct: the
rules of the principal. The hook command is anchored at the engine
root. The settings call `python` in exec form with
`${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.py` as its one
argument. Because a hook runs in the working directory of the
session, a relative path could miss the engine root. The placeholder
always names the root the session started in.

A hook is context, not enforcement. It puts the rule in front of
Claude again at every turn; it does not stop Claude from breaking
it. A gate that would enforce the three lines of conduct does not
exist yet.

### The harness stops what it can

The settings of the harness enforce part of the principal's word.
The deny rules in `.claude/settings.json` are these:

- `Read(~/.ssh/**)` and `Read(~/.aws/**)`: Claude cannot read these
  sensitive paths of the user.
- `Bash(git *)` and `PowerShell(git *)`: Claude cannot call `git`
  directly in either shell.

The scripts in `scripts/` are the only door to git for the forge,
reading the state included. The deny rules turn that rule into a wall
of the harness rather than conduct alone. The rule binds the forge,
not the principal: his own git from the shell remains his. The same
settings turn off the attribution the harness would add to a commit.
A commit message is the one the principal confirmed, word for word.
Web access is approved by the user, one domain at a time.

Some commands are guarded by the harness, so that Claude cannot start
them on its own judgement. These are the commands that change files
the moment they run, with no round and no `write` in between:

- `/save`, `/release`, `/pull`
- `/spinoff`, `/setup`, `/new-project`, `/new-artefact`,
  `/import-project`
- `/ingest`, `/render`, `/publish`, `/document`

The principal starts a guarded command by its slash. He may also ask
for it in words, and then Claude follows the definition of the
command, read by path. A command that writes only at the end of a
round on the principal's word needs no guard. Neither does a command
that files the immutable record of a run he asked for. Maps, reports
and rosters stay Claude's to start, such as `/forge`, `/ledger`,
`/check`, `/critique`, `/challenge`, `/research` and bare `/recipe`.

The exact settings are listed in
[Configuration](../reference/configuration.md).

### A subagent reads its inputs from disk

A subagent sees the whole context of the session. That includes
`CLAUDE.md` as the session read it and the assistant's memory. A
subagent may take that copy for the file on disk, although the file
may have changed since. So every agent that writes an outward-facing
file says two things in its own definition. Instance facts are not
material. Every input is read from disk. The generated files are then
scanned mechanically before they are kept.

The instance file reaches every subagent too, the isolated reviewers
included. So only what must be always-on and is harmless in a public
report lives in `CLAUDE.local.md`. Instance facts are forbidden in a
reviewer's report. The git identities live in the user's own git
configuration, outside the engine.

### One model for the whole forge

Every command, every state of the chain and every reviewer runs on
the session model. The session model is chosen in one deliberate
place: a preference of the instance, kept in
`.claude/settings.local.json` outside the repository. Speed is bought
with context, not with a weaker model. A job that can be isolated
runs in a subagent that sees only its inputs, never the working
conversation.

There are two exceptions. The headless conversions behind `/publish`
have no session model, so each takes a default of its own as an
explicit parameter. The documentation writer writes a mirrored page
on a faster model and a derived page on the session model. The choice
is made mechanically by the entry of the page in the documentation
map, never per run.

### The behaviour lives in the engine, not in memory

Claude Code keeps a memory for each directory, outside the
repository. Whatever that memory learns about how the forge should
work is written into `CLAUDE.md`, the commands or the templates. It is
then removed from the memory. A working method, a rule of a command
and a convention are all such things. The memory keeps only what is
personal to one principal, such as his idiom and his private choices.
Instance facts go to `CLAUDE.local.md`.

### The forge explains itself

`/man [command|method]` is the manual of the forge, with `/manual` as
its alias. It reads the definitions of the forge and prints them. It
is never a text of its own. It is named after the Unix manual.
Because `/help` is a built-in command of Claude Code, the name `/man`
was taken instead.

## Why

- **One place for each mechanism.** Two copies of a procedure drift
  apart. The copy that lacks a rule loses it silently.
- **A short core with pointers.** Always-on is one sentence and a
  pointer; the detail is a file read when its situation arises. The
  alternative was the whole method in `CLAUDE.md`. The cost of the
  core is its size, since the harness loads it into every session.
- **A hook.** Text loaded once dissolves as the conversation grows. A
  rule fully in context still breaks in a long conversation, so the
  rule that must hold is repeated at every prompt. The hook is the
  nearest thing to a wall the harness offers for conduct. It is a
  trial, judged by behaviour.
- **Deny rules and guards.** They let the principal's word rest on
  the harness as well as on `CLAUDE.md`. A guarded command changes
  files at once, with no point in its procedure where the principal
  gives his word. The other commands already carry his word in their
  procedure. Maps, reports and rosters are left to Claude because it
  is meant to propose them. Why git is reached only through the
  scripts: the reason is not recorded.
- **Inputs from disk and a mechanical scan.** A subagent can mistake
  the session's copy of a file for the file. An outward-facing file
  must carry no instance fact.
- **One model.** The strongest model the forge runs on is then a
  decision, never an accident of a pinned model that has aged. The
  routine commands are slow for the size of their context, not for
  their model, and every pin would be one more convention to keep. A
  smaller model drifts from a recipe that leaves it room. A mirrored
  page leaves the model no room, which is why it may run faster.
- **No behaviour in memory.** Every instance of the forge then
  behaves the same, and a new user meets the same forge as the
  principal.
- **A manual that reads.** A manual of its own would be a second
  statement of every mechanism.

## A worked example

The principal is deep in a long conversation, working through a list
of findings in project `my-project`. The following holds at his
fortieth prompt.

1. `CLAUDE.md` was loaded when the session began. It still says
   "one item per message", but it was read long ago.
2. The hook runs as he sends the prompt. Its five lines are added to
   this turn, so the one-item rule and the verdict line stand fresh
   beside his message.
3. The walkthrough skill was read when the walkthrough began. The
   hook's pointer names it again.
4. Claude wants to know whether the repository has unsaved changes.
   A raw `git status` through the shell would meet the deny rule
   `Bash(git *)`. It reads the state through
   `scripts/forge-status.py` instead, as the hook's line on tools
   says.
5. The round ends and the work should be committed. `/save` is a
   guarded command, so Claude proposes it. The principal types
   `/save my-project`, or asks for it in words.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): the
  files of the operating layer.
- [Configuration](../reference/configuration.md): the settings,
  exactly.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
