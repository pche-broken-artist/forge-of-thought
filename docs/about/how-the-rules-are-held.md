---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: 31a0409a408ef2c7
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

The rules of the forge are held by one always-on file, by files
that are read when their situation arises, by a hook that speaks at
every prompt and by the harness (Claude Code, the program that runs
Claude and sets the walls it works inside). This page is for
whoever extends the forge or judges it. It says where each rule
lives, how a rule reaches a long conversation and a subagent (an
isolated run of Claude that sees nothing of the working
conversation), what the harness refuses on its own, and why the
forge holds its rules this way instead of trusting one file.

## What it is

Holding a rule means two different things here. The first is that
the rule is in front of Claude at the moment its situation arises.
The second is that the harness refuses what the rule forbids, where
it can. The forge keeps the two apart.

What Claude reads is the operating layer: the files listed on
[What the forge is made of](../extend/what-it-is-made-of.md). Among
them one file is always on, `CLAUDE.md`, loaded into every session
(one conversation of Claude from its start to its end) and into
every subagent. Beside it stands the instance file,
`CLAUDE.local.md`, which also reaches every subagent. Everything
else is a file read when its situation arises: a skill, an agent, a
definition (the state file of an artefact), a template, the header
of a script.

What the harness refuses is written in its settings, given exactly
on [Configuration](../reference/configuration.md): deny rules on
tools and paths, the hook, and the switch that keeps a commit free
of attribution. A guard on the commands that change files the moment
they run belongs to the harness as well.

A hook is context, not enforcement. It is the nearest thing to a
wall the harness offers for a rule of conduct. Neither a hook nor a
deny rule is a promise that Claude will behave: the hook keeps the
rule in sight, the deny rule closes one door.

## How it works

### The always-on core and the instance file

`CLAUDE.md` in the engine root carries what must hold in every
session and for every subagent: the roles, the prime directives, the
working methods in short, the document kinds, the chain, the
layout, persistence, versioning, the ID scheme, the reviewers, the
ledger (the file that is the single source of truth for a project's
state) and the list of commands. A rule of one artefact is not
there. It stands in that artefact's definition.

Always-on is one sentence and a pointer. The detail is a file read
when its situation arises. The walkthrough (the method by which a
list of items needing the principal's decision is worked one item
per message) is the first instance of this pattern: `CLAUDE.md`
carries the rule in short and the path
`.claude/skills/walkthrough/SKILL.md`, and that skill holds the
whole shape of the item, the verdict, the elicitation interview and
the write-up. The skill is read whenever a walkthrough or an
interview runs. It is not a command.

`CLAUDE.local.md` stands at the engine root, kept out of the
repository, created from `templates/CLAUDE.local.md` and filled by
`/setup` on a new machine. It holds who the principal (the person
whose thinking is forged) is, by role, and what language the
conversation runs in. `CLAUDE.md` names these two only as things
that exist, never by value. Everything in the instance file reaches
every subagent, the isolated reviewers included. Therefore only
what must be always-on and is harmless in a public report lives
there. The git identities, that is names, e-mail addresses and
hosts, live in the user's own git configuration outside the engine.
Instance facts are forbidden in a reviewer's report.

### One mechanism lives in one place

Whatever the forge has a procedure for, a command, a skill, a
script or an agent, is used through its own definition whenever its
situation arises. It is never re-described and never improvised. A
command that needs another's mechanism cites it by path and adds
nothing of its own to how that mechanism runs. The rules of a
mechanism, its isolation, its wrapping, its provenance and what it
may read, are written once, in its own definition.

A procedure stated in two places is a defect. Where a shape had no
owner at all, it gets a template rather than a second description.
A restatement is steps, rules or a shape repeated. A one-line
reminder at the point of action that names its owner is not a
restatement, such as "not under git is a fact, not a defect
(CLAUDE.md, Persistence)".

The check `single-source-of-truth` carries this rule over the whole
operating layer. It runs on the principal's word and never at a
release on its own.

### The hook at every prompt

A rule that must hold through a long conversation is not trusted to
`CLAUDE.md` alone. It is repeated at every prompt by a hook. The
harness runs `scripts/hook-walkthrough.py` on every prompt of the
user, through the `UserPromptSubmit` hook of `.claude/settings.json`,
and adds what the script prints to the context of that turn.

The hook prints five lines. Two are on the walkthrough: the one-item
rule itself, with the verdict line that closes every proposition,
and the pointer to the skill that holds the full shape. Three are
lines of conduct, the principal's rules. This is what it prints,
word for word:

```
Walkthrough rule: one item per reply - acknowledge the last verdict, put one item forward, close a proposition with '(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark', stop. A question from the principal keeps the item open: answer, then close it again.
When a walkthrough or an interview is running, work by .claude/skills/walkthrough/SKILL.md.
Tools: where the forge has a script (scripts/*.py), use the script, never the raw tool. git only through scripts/forge-*.py, reading state included.
Own commands: before running anything of your own that is not plain reading, say what it does and why, and wait for the principal's yes.
Consent: write, run and change nothing that was not agreed and approved. A yes covers exactly what was asked, never its consequences.
```

The hook's command is anchored at the engine root. A hook runs in
the session's working directory, not the engine root, so a relative
path would be resolved against the wrong place. The settings
therefore invoke the script in exec form, `python` with
`${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.py` as its one
argument. The placeholder always names the root the session started
in, and the exec form hands the path to the program without a shell.

### What the harness enforces

The harness enforces the principal's word where it can. Its settings
hold four deny rules:

- `Read(~/.ssh/**)`: Claude is kept from the user's SSH keys.
- `Read(~/.aws/**)`: Claude is kept from the user's cloud
  credentials.
- `Bash(git *)`: no raw `git` from the Bash tool.
- `PowerShell(git *)`: no raw `git` from the PowerShell tool.

The last two make the scripts-only door to git a wall of the
harness, not conduct alone. The scripts in `scripts/` are the only
door to git, reading state included. The rule binds the forge, not
the principal: his own git from the shell is his. The same settings
switch off attribution in commits, so that no `Co-Authored-By` or
`Claude-Session` trailer is added or proposed. The commit message is
the one the principal confirmed, word for word.

A command that writes, scaffolds, commits or regenerates is guarded
by the harness, so that Claude cannot start it on its own judgement.
These are `/save`, `/release`, `/pull`, `/spinoff`, `/setup`,
`/new-project`, `/new-artefact`, `/import-project`, `/ingest`,
`/render`, `/publish` and `/document`. The principal invokes such a
command by slash, or asks in words and Claude follows the command's
definition read by path. What separates a guarded command from the
rest: a guarded command changes files the moment it runs, with no
round and no `write` in between. A command that writes only at the
end of a round on the principal's word, or files the immutable
record of a run he asked for, needs no guard, because the word is
already in the procedure. Maps, reports and rosters stay Claude's
to start, since it is meant to propose them: `/forge`, `/ledger`,
`/check`, `/critique`, `/challenge`, `/research`, bare `/recipe`
and the roster of each.

### Reading from disk inside a subagent

A subagent sees the session's whole context: `CLAUDE.md` as the
session read it and the assistant's memory included. It may take
that copy for the file on disk. So every agent that writes an
outward-facing file says in its definition two things: that instance
facts are not material, and that an input is read from disk. The
generated files are scanned mechanically before they are kept.

### One model

One model runs the whole forge. Every command, every chain state and
every reviewer runs on the session model, chosen in one deliberate
place, as an instance preference in `.claude/settings.local.json`,
kept out of the repository. Speed is bought with context, not with
weaker models: `/render` generates in an isolated subagent that sees
only the recipe and its inputs, every check executes its own
definition in an isolated subagent that sees only the files, and the
working conversation is spent on verdicts, not on reading.

Two exceptions are named. The headless conversions behind `/publish`
have no session model, so each needs a default of its own, an
explicit parameter rather than an aged pin. The documentation writer
writes a mirrored page, which leaves the model no room, on a faster
model, and a derived page on the session model. The choice is made
mechanically by the page's entry in the documentation map, never per
run.

### Nothing in the assistant's memory

The forge's behaviour lives in the engine, never in the assistant's
private memory. Claude Code keeps a per-directory memory outside the
repository. Whatever it learns there about how the forge should
work, a working method, a rule of a command, a convention, is
written into `CLAUDE.md`, the commands or the templates and removed
from memory. Memory is left with what is personal to one principal:
his idiom, his private choices. Instance facts go to
`CLAUDE.local.md`.

### The forge explains itself

`/man`, with its alias `/manual`, is the forge's manual. It is a
reader of the forge's own definitions, never a text of its own. It
is named after the Unix manual, because `/help` is a built-in of
Claude Code.

## Why

Text loaded once dissolves as the conversation grows. This is why a
rule that must hold through a long conversation is repeated at every
prompt and not trusted to `CLAUDE.md` alone. The hook is a trial,
judged by behaviour.

Two copies of a procedure drift, and the copy without a rule
silently loses it. This is why one mechanism lives in one place and
is cited by path everywhere else. The sweep that checks the rule is
expensive by design and runs on the principal's word, so that the
rule costs a release nothing and the sweep is honest when it runs.

`CLAUDE.md` is the one file Claude Code loads into every session.
This is why it is the always-on core. The design records no real
alternative. What it costs is its size.

Everything in the instance file reaches every subagent and may be
quoted into a public report. This is why the file stays small and
harmless, and why the git identities live in the user's own
configuration rather than in the forge.

A guarded command changes files the moment it runs, with no round
and no `write` in between. This is why the guarantee of Step by step
(any action needing the principal's consent arrives as one step and
runs on his word) rests on the harness as well as on `CLAUDE.md`.

The strongest model the forge runs on should be a decision, never an
accident of a pin that has aged. This is why there is one session
model, chosen in one place. Per-command pinning to a faster model is
rejected, because the routine commands are a small share of the work
and slow for the size of the context they carry, not for the model,
and because every pin is a convention to keep. A smaller model
drifts from a recipe that leaves it room, so the faster model is
given only the page that leaves no room.

Every instance of the forge should behave the same, and a new user
should meet the same forge as the principal. This is why nothing of
the forge's behaviour lives in the assistant's memory.

`/man` exists for the newcomer's first hour and for the reader who
opens the repository.

## A worked example

A session has run long over the project `my-project`. The principal
has asked for a critique of its intent, and the critique has ended
by offering a walkthrough of its findings. He accepts the offer.

His next prompt arrives. Before Claude answers, the harness runs the
hook and adds its five lines to the turn: the one-item rule with the
verdict line, the pointer to the walkthrough skill, and the three
lines of conduct. Claude reads
`.claude/skills/walkthrough/SKILL.md`, because the hook points
there and a walkthrough is now running. It puts the heaviest finding
forward, closes with
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`, and stops.
The principal answers `a`. At his next prompt the hook prints the
same five lines again, and Claude acknowledges the verdict, puts
the next finding forward and stops. The rule holds at the thirtieth
item as it held at the first, because it is in front of Claude at
every turn and not only in the file read at the start.

When the last verdict is given, the principal types `write`. Claude
reflects the whole round back and writes it once, on his yes. He
then asks, in words, that the project be saved. `/save` is a guarded
command: Claude has not started it on its own, and it now follows
the save's definition read by path. The save commits through one of
the `scripts/forge-*.py` scripts. Had Claude typed `git commit` into
the shell itself, the deny rule `Bash(git *)` would have refused it.
The commit carries the message the principal confirmed and no
trailer.

Nothing of this round is kept in the assistant's memory as a rule of
the forge. The one-item rule, the verdict line, the scripts-only
door and the guard all stand in the engine's files and settings, so
the next instance of the forge, on another machine, behaves the
same.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): the
  files of the operating layer.
- [Configuration](../reference/configuration.md): the settings,
  exactly.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
