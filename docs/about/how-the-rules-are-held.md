---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: 8edb1e1ded3ce4a4
inputs:
  - CLAUDE.md#Prime directives
  - CLAUDE.md#Working methods
  - CLAUDE.md#Isolated reviewers
  - .claude/settings.json
  - scripts/hook-walkthrough.py
  - scripts/hook-git.py
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

The rules of the forge are held in force by a small always-on core,
by files read when their situation arises, by a hook that repeats
what must not fade, and by what the harness can refuse. This page
explains how those layers work together across a long conversation
and inside a subagent, and why each is there. It is for the extender
who changes the operating layer and for the evaluator who wants to
know how far the rules can be relied on.

## What it is

Claude works for the principal (the person whose thinking is
forged, with the final word on all content). It works inside the
harness (Claude Code, the program that runs Claude, loads its files
and executes its tools). A session is one run of that harness, one
conversation from start to end. A subagent is a separate run of
Claude launched for one job, which sees nothing of the conversation.

The rules reach Claude through these layers:

- the core: `CLAUDE.md` at the engine root, loaded into every
  session and every subagent;
- the instance file: `CLAUDE.local.md`, kept out of the repository,
  which carries the facts of one installation and also reaches every
  subagent;
- the definitions: the skills, agents, templates and scripts, each
  read when its situation arises;
- the per-prompt hook: a script that adds a few lines to the context
  at every prompt;
- the harness's own settings: deny rules, a second hook on git, and
  a guard on the commands that change files at once.

Which files make up the operating layer is set out in
[What the forge is made of](../extend/what-it-is-made-of.md). The
settings themselves, exactly as they stand, are in
[Configuration](../reference/configuration.md). Every term used here
has one line in the [Glossary](../reference/glossary.md).

## How it works

### One core, everything else read when needed

The core carries what must hold in every session and for every
subagent. That is the roles, the prime directives, the working
methods in short, the document kinds, the chain, the layout,
persistence, versioning, the ID scheme, the reviewers, the ledger
(the one source of truth for a project's state) and the list of
commands. A rule of one artefact is not in the core. It lives in
that artefact's definition.

The pattern is one sentence and a pointer in the core, with the
detail in a file read when its situation arises. The walkthrough
(the way a list of decisions is worked with the principal, one item
per message) is the first instance. The core states the rule in
short and names `.claude/skills/walkthrough/SKILL.md`. That skill
holds the full shape and is read whenever a walkthrough or an
interview runs.

### One mechanism in one place

Whatever the forge has a procedure for is used through its own
definition whenever its situation arises. That covers a command, a
skill, a script and an agent. A procedure is never described again
or improvised. A command that needs another command's mechanism
cites it by path and adds nothing of its own to how it runs. The
rules of a mechanism are written once, in its own definition.

A procedure stated in two places is a defect. A one-line reminder at
the point of action that names its owner is not a restatement. A
restatement repeats steps, rules or a shape.

### A hook repeats what must hold all conversation long

The harness can run a script at every prompt and add what it prints
to the context of that turn. The engine's `.claude/settings.json`
configures one such hook, `scripts/hook-walkthrough.py`. It reads
nothing and writes nothing. It prints six lines:

- the one-item rule of the walkthrough: one item per reply, the last
  verdict acknowledged, one proposition put forward and closed with
  `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`, then stop;
  a question from the principal keeps the item open;
- the pointer: while a walkthrough or an interview runs, Claude works
  by `.claude/skills/walkthrough/SKILL.md`;
- tools: where the forge has a script, Claude uses the script and
  never the raw tool;
- own commands: before running anything of its own that is not plain
  reading, Claude says what it does and why, and waits for the
  principal's yes;
- consent: Claude writes, runs and changes nothing that was not
  agreed and approved, and a yes covers exactly what was asked;
- decisions: every question that asks the principal to decide is one
  proposition, with Claude's recommendation as what accept means,
  closed with the verdict line; a yes that carries a question counts
  as a question.

A hook is context, not enforcement. It is the nearest thing to a
wall that the harness offers for conduct.

### The harness enforces what it can

The harness keeps the principal's word where a setting can do it.

- Deny rules in `.claude/settings.json` keep Claude from the user's
  sensitive paths.
- A deny rule keeps the PowerShell tool away from git altogether.
  Claude therefore runs git through one shell tool only, Bash.
- Web access is approved by the user per domain.
- A second hook, `scripts/hook-git.py`, runs before every Bash
  command and holds the line between reading git and writing it: a
  read passes, a write is refused with the forge's script to use
  instead. How that line works is explained in
  [Persistence in git](persistence-in-git.md).
- A command that changes files the moment it runs is guarded by the
  harness. Claude cannot start such a command on its own judgement.
  The principal invokes it by slash, or asks in words and Claude
  follows the command's definition, read by path.

The criterion of a guarded command is that it writes, scaffolds,
commits or regenerates with no round and no `write` in between. A
command that writes only at the end of a round on the principal's
word needs no guard. Neither does a command that files the immutable
record of a run the principal asked for. In both, the principal's
word is already part of the procedure. Maps, reports and rosters
stay Claude's to start. The reason is that Claude is meant to
propose them.

### Subagents read from disk

Every isolated subagent of the forge reads every input from disk in
its own run. That holds for a reviewer, a renderer, a documentation
agent and a research agent alike. A subagent sees the session's
whole context, including `CLAUDE.md` as the session read it and the
assistant's memory. It may take that copy for the file on disk. The
copy in its context may be older than the file.

Each subagent also lets no instance fact into what it returns. Every
agent that writes an outward-facing file says in its definition that
instance facts are not material and that an input is read from disk.
The generated files are scanned mechanically before they are kept.

### One model

The whole forge runs on one model, the session model. Every command,
chain state and reviewer runs on it (`model: inherit`). Speed is
bought with context, never with a weaker reviewer. Two exceptions
are named:

- the headless conversions behind `/publish`, which have no session
  model and take an explicit default;
- the documentation writer, which writes a mirrored page on a faster
  model and a derived page on the session model, chosen by the
  page's entry and never per run.

The session model is chosen in one deliberate place, an instance
preference.

### Nothing in the assistant's memory

The harness keeps a per-directory memory outside the repository.
Whatever Claude learns there about how the forge should work is
written into `CLAUDE.md`, the commands or the templates, and removed
from memory. That covers a working method, a rule of a command and a
convention. Memory keeps only what is personal to one principal.
Instance facts go to `CLAUDE.local.md`.

### The forge explains itself

`/man [command|method]`, alias `/manual`, is the forge's manual. It
reads the forge's own definitions and has no text of its own.

## Why

- **A small core and files read on demand.** The core is the file
  the harness loads into every session. What it costs is its size.
  Always-on is therefore one sentence and a pointer, and the detail
  lives in a file read when its situation arises.
- **The instance file stays small.** It reaches every subagent,
  reviewers included. Only what must be always-on and is harmless in
  a public report belongs there.
- **One place per mechanism.** Two copies of a procedure drift. The
  copy that lacks a rule silently loses it.
- **The hook.** Text loaded once dissolves as the conversation
  grows. A rule that must hold in a long conversation is therefore
  not trusted to `CLAUDE.md` alone.
- **The guard on commands.** The promise that every action needing
  consent arrives as one step and runs on the principal's word rests
  on the harness as well as on `CLAUDE.md`.
- **One shell for git.** There is then one parser and one door. A
  prefix deny rule matches the text usually typed, not the command.
  A variant spelling of a writing command passes it. The wall for
  writes is therefore the hook and not a deny rule.
- **Reading from disk.** The copy of a file in a subagent's context
  may be older than the file on disk. Instance facts in a subagent's
  context would otherwise reach a public file.
- **One model.** The strongest model the forge runs on is a
  decision, never an accident of a pin that has aged. Every pin is
  also a convention to keep.
- **No behaviour in memory.** Every instance of the forge behaves
  the same. A new user meets the same forge as the principal.
- **`/man` reads the definitions.** A manual with a text of its own
  would be a second place for each mechanism. It serves the
  newcomer's first hour and the reader who opens the repository. The
  name follows the Unix manual. The reason is that `/help` is already
  a built-in of the harness.

None of these layers guarantees behaviour. The hooks and the deny
rules narrow what can go wrong, and the rest rests on Claude
following the files it reads.

## A worked example

A principal works through five findings on a project
`example-project` in a long session.

1. At each prompt the per-prompt hook adds its six lines. Claude
   acknowledges the last verdict, puts the next finding forward
   alone and closes it with
   `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`.
2. The walkthrough is running, so Claude works by
   `.claude/skills/walkthrough/SKILL.md`, read from the file.
3. The principal answers one finding with "yes, but why this
   wording?". The hook's last line counts that as a question. Claude
   answers and closes the item again.
4. At the end Claude wants to commit with a raw `git commit` in
   Bash. The git hook refuses it and names the script to use. Claude
   proposes the save as one step instead.
5. The save commits the moment it runs. Claude does not start it on
   its own judgement. The principal types `/save example-project`.
6. Later the principal asks for a critique. The critic runs as an
   isolated subagent. It reads the project's files from disk, not
   from the session's copy, and returns a report with no instance
   fact in it.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): the
  files of the operating layer.
- [Persistence in git](persistence-in-git.md): the hook that holds
  the line between reading and writing git.
- [Configuration](../reference/configuration.md): the settings,
  exactly.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
