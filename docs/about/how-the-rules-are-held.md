---
generated: 2026-10-10
made: derived
inputs-hash: 1ab6b7292b273bb6
inputs:
  - CLAUDE.md
  - .claude/settings.json
  - scripts/hook-walkthrough.py
  - projects/forge/10-intent.md
  - projects/forge/40-solution-design.md
---

# About how the rules are held

This page explains how the forge keeps its rules in force: where a
rule lives, how it reaches a session, what is repeated so that it
survives a long conversation, what the harness enforces and what it
cannot. It is for the extender who wants to add or move a rule
without weakening the whole, and for the evaluator who wants to know
how much of the forge's behaviour rests on text and how much on a
mechanism. It was put together from `CLAUDE.md`,
`.claude/settings.json`, `scripts/hook-walkthrough.py`, the forge
intent and the forge solution design.

## One always-on core, everything else a file read when needed

The forge has one file that is loaded into every session and every
subagent: `CLAUDE.md` at the engine root, the universal core. It
carries only what must hold everywhere: the roles, the prime
directives, the working methods in short, the document kinds, the
chain, the repository layout, persistence, versioning, the ID
scheme, the reviewers, the ledger and the list of commands. It is
the file the harness loads into every session, so there is no real
alternative to it; what it costs is its size, since everything in it
is paid for at every prompt.

Everything else is a file read when its situation arises: a command
is its skill (`.claude/skills/<command>/SKILL.md`), an artefact of
the chain is its definition (`.claude/skills/forge/states/<state>.md`)
paired with its template, a reviewer is its agent file under a
contract skill, a shape is its skeleton in `templates/`. A rule of
one artefact is not in the core but in that artefact's definition.
The pattern is the same throughout: always-on is a sentence and a
pointer, the detail is a file read when it is needed.

Instance facts, who the principal is and what language the
conversation runs in, are not in the core either. They live in
`CLAUDE.local.md`, a gitignored file at the engine root that the
core names only as a thing that exists, never by value. That file
reaches every subagent, the isolated reviewers included, so only
what must be always-on and is harmless in a public report belongs
there.

## One mechanism lives in one place

Whatever the forge has a procedure for, a command, a skill, a
script, an agent, is used through its own definition whenever its
situation arises, never re-described or improvised. A command that
needs another's mechanism cites it by path and adds nothing of its
own to how that mechanism runs: a release regenerates the README
through the render command and ends by running the save command,
git is touched through the scripts in `scripts/`, reviews run
through the reviewer agents. The rules of a mechanism, its
isolation, its wrapping, its provenance, what it may read, are
written once, in its definition.

The reason is drift. A procedure stated in two places is a defect:
the two copies drift apart, and the copy without a rule silently
loses it. Where a shape had no owner at all, it gets a skeleton in
`templates/` rather than a second description. A one-line reminder
at the point of action that names its owner is not a restatement:
it is what Claude reads when he acts, and the citation keeps it
honest. A check, `single-source-of-truth`, sweeps the whole
operating layer for restatements on the principal's word; it is
expensive by design and never runs at a release on its own, so that
the rule costs a release nothing and the sweep is honest when it
runs.

The same rule holds for the scripts: what several of them share
lives in a module beside them (`forge_repos.py`, `forge_tools.py`,
`docs_map.py`), never twice.

## A rule that must hold in a long conversation is repeated

Text loaded once dissolves as a conversation grows. A rule that
must hold through a long conversation is therefore not trusted to
`CLAUDE.md` alone: it is repeated at every prompt by a hook.
`.claude/settings.json` registers one `UserPromptSubmit` hook, run
as `python` with `${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.py`
as its one argument, and the harness adds what the script prints to
the context of that turn. The command is given in exec form and
anchored at the project root through the placeholder, because a
hook runs in the session's working directory, not the engine root,
and a relative path would resolve against the wrong place.

The script prints five lines:

- the walkthrough rule: one item per reply, acknowledge the last
  verdict, put one item forward, close a proposition with
  `(a)ccept / (m)odify / (r)eject / (p)ark`, stop; a question from
  the principal keeps the item open;
- when a walkthrough or an interview is running, work by
  `.claude/skills/walkthrough/SKILL.md`;
- tools: where the forge has a script in `scripts/`, use the script,
  never the raw tool; git only through `scripts/forge-*.py`, reading
  state included;
- own commands: before running anything of one's own that is not
  plain reading, say what it does and why, and wait for the
  principal's yes;
- consent: write, run and change nothing that was not agreed and
  approved; a yes covers exactly what was asked, never its
  consequences.

The first two lines are the walkthrough; the last three are lines of
conduct, the principal's rules. A hook is context, not enforcement:
it is the nearest thing to a wall the harness offers for a rule of
conduct, and it is judged by behaviour.

## The harness enforces what it can

Where the harness offers a mechanism, the forge uses it rather than
relying on conduct alone. Protection rests on the permission system
of Claude Code, not on an OS-level sandbox: commands and file
operations run under permission prompts and allowlists, and web
access is approved per domain on first use. An OS-level sandbox was
tried and deliberately dropped, since it is unavailable on Windows,
where enforcing it would have meant no shell at all.

Three things are enforced this way.

- **Deny rules.** `.claude/settings.json` denies Claude the user's
  sensitive paths (`~/.ssh`, `~/.aws`) and the raw `git` command in
  both shells (`Bash(git *)`, `PowerShell(git *)`). The scripts in
  `scripts/` are thereby the only door to git, reading state
  included; the rule binds the forge, not the principal, whose own
  git from the shell is his. In the same file `attribution.commit`
  is empty and `attribution.sessionUrl` is false, so no
  `Co-Authored-By` or `Claude-Session` trailer is added or proposed:
  a commit message is the one the principal confirmed, word for
  word.
- **Guarded commands.** A command that writes, scaffolds, commits or
  regenerates (`/save`, `/release`, `/spinoff`, `/setup`,
  `/new-project`, `/new-artefact`, `/import-project`, `/ingest`,
  `/render`, `/publish`, `/document`) carries
  `disable-model-invocation: true` in the front-matter of its skill,
  so that Claude cannot start it on his own judgement: the principal
  invokes it by slash, or asks in words and Claude follows the
  command's definition read by path. The guarantee that every
  sensitive action arrives as one step on the principal's word thus
  rests on the harness as well as on `CLAUDE.md`. Maps, reports and
  rosters (`/forge`, `/ledger`, `/check`, `/critique`, `/challenge`,
  `/research`, bare `/recipe`) carry no such field and stay Claude's
  to start, since he is meant to propose them.
- **Isolation of reviewers and generators.** Every reviewer and every
  render runs in an isolated subagent that sees the project's
  documents, or the recipe and its inputs, never the working
  conversation. Speed is bought with context, never with a weaker
  model.

What the harness cannot enforce stays a process rule: immutability
of reviews, challenges, sources and research is a convention, not a
git mechanism, since git protects nothing from a commit that
rewrites a file and a mechanism would be one more layer that still
would not stop a hand edit.

## A subagent may take the session's copy for the file

A subagent sees the session's whole context: `CLAUDE.md` as the
session read it, the assistant's memory and `CLAUDE.local.md`
included. It may take that copy for the file on disk, and the copy
may be older than the file. Two consequences follow. Every agent
that writes an outward-facing file, a reviewer's report, a render, a
page of the documentation, says in its definition that instance
facts are not material and that every input is read from disk in
its run. And the generated files are scanned mechanically before
they are kept: the documentation has its check script,
`scripts/docs-check.py`, and renders are scanned likewise. Instance
facts never enter a reviewer's report, not even where they would
explain a finding, because a report is a public file or may be
quoted into one.

## One model, chosen once

The whole forge runs on one model, the session model, chosen in one
deliberate place: `.claude/settings.local.json`, gitignored, created
by `/setup`. Every agent declares `model: inherit` rather than a pin
of its own, because a pin ages and the strongest model the forge
runs on should be a decision, never an accident. The intent names
two exceptions: the headless conversions behind `/publish`, which
have no session model and carry an explicit default of their own in
a `--model` parameter, and the documentation writer, where a
mirrored page leaves the model no room and is written on a faster
model while a derived page runs on the session model, the choice
made by the page's entry in the map, never per run.

## The forge's behaviour never lives in the assistant's memory

Claude Code keeps a per-directory memory outside the repository.
Whatever it learns there about how the forge should work, a working
method, a rule of a command, a convention, is written into
`CLAUDE.md`, the commands or the templates and removed from memory,
so that every instance of the forge behaves the same and a new user
meets the same forge as its author. Memory is left with what is
personal to one principal; instance facts go to `CLAUDE.local.md`;
the commit identity is git's, resolved per host by the user's own
git configuration, and the forge sets none.

## The forge explains itself from its own definitions

Because every mechanism lives in one place, the forge can be read
from those places. `/man [command | method]`, alias `/manual`, is
the forge's manual: a reader of the definitions, never a text of its
own. It is named after the Unix manual, `/help` being a built-in of
Claude Code, and exists for the newcomer's first hour and for the
reader who opens the repository.

## See also

- [About what the forge is made of](../extend/what-it-is-made-of.md): the files of the operating layer.
- [Configuration](../reference/configuration.md): the settings, exactly.
