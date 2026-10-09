---
generated: 2026-10-09
made: derived
inputs-hash: ba5e32b71d60a16b
inputs:
  - CLAUDE.md
  - .claude/settings.json
  - scripts/hook-walkthrough.py
  - projects/forge/10-intent.md
  - projects/forge/40-solution-design.md
---

# About how the rules are held

This page explains how the forge keeps its rules in force: what is
loaded into every session, what is read only when its situation
arises, what is repeated at every prompt, what the harness enforces
and where the limits of each of these lie. It is for the extender
who wants to change the forge without loosening it, and for the
evaluator who wants to know what actually holds the thing together.
It was put together from `CLAUDE.md`, `.claude/settings.json`,
`scripts/hook-walkthrough.py`, the forge intent and the forge
solution design.

## One always-on core

The forge has one file that every session and every subagent
carries: `CLAUDE.md` in the engine root. It is the file Claude Code
loads into every session, and it carries only what must hold
everywhere: the roles, the prime directives, the working methods in
short, the document kinds, the chain, the repository layout,
persistence, versioning, the ID scheme, the reviewers, the ledger
and the list of commands. A rule that belongs to one artefact is not
there; it stands in that artefact's definition.

Everything else is a file read when its situation arises: a command
is its skill (`.claude/skills/<command>/SKILL.md`), an artefact of
the chain is its definition (`.claude/skills/forge/states/<state>.md`)
paired with its template, a reviewer is its agent file with the
shared conduct in one contract skill, a document's shape is a
skeleton in `templates/`. The pattern is deliberate: always-on is
one sentence and a pointer, the detail is a file read when it is
needed. What the core costs is its size, since everything in it
reaches every session and every subagent.

## One mechanism lives in one place

Whatever the forge has a procedure for, a command, a skill, a
script, an agent, is used through its own definition whenever its
situation arises, never re-described or improvised. A command that
needs another's mechanism cites it by path and adds nothing of its
own to how it runs: a release regenerates the README and release
notes through the render command and ends by running the save
command, git is touched through the scripts in `scripts/`, reviews
run through the reviewer agents. The rules of a mechanism, its
isolation, its wrapping, its provenance, what it may read, are
written once, in its own definition.

The reason is drift. A procedure stated in two places is a defect,
because the two copies drift apart and the copy without a rule
silently loses it. Where a shape had no owner at all, it is given a
skeleton rather than a second description. A one-line reminder at
the point of action that names its owner is not a restatement: it
is what Claude reads when he acts, and the citation keeps it honest.
A check, `single-source-of-truth`, carries this rule over the whole
operating layer; it is run on the principal's word and never by a
release on its own, so that the rule costs a release nothing and the
sweep is honest when it runs.

## A rule repeated at every prompt

Text loaded once dissolves as a conversation grows. A rule that
must hold through a long conversation is therefore not trusted to
`CLAUDE.md` alone: it is repeated at every prompt by a hook.
`.claude/settings.json` registers one `UserPromptSubmit` hook,
`python` with `${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.py` as
its one argument, and whatever the script prints is added to the
context of that turn. The placeholder anchors the script at the
root the session started in, because a hook runs in the session's
working directory, not the engine root.

The hook prints five lines:

- the walkthrough rule: one item per reply; acknowledge the last
  verdict, put one item forward, close a proposition with
  `(a)ccept / (m)odify / (r)eject / (p)ark`, stop; a question from
  the principal keeps the item open;
- the pointer: when a walkthrough or an interview is running, work
  by `.claude/skills/walkthrough/SKILL.md`;
- tools: where the forge has a script (`scripts/*.py`), use the
  script, never the raw tool; git only through
  `scripts/forge-*.py`, reading state included;
- own commands: before running anything of one's own that is not
  plain reading, say what it does and why, and wait for the
  principal's yes;
- consent: write, run and change nothing that was not agreed and
  approved; a yes covers exactly what was asked, never its
  consequences.

The first two lines are the walkthrough's; the last three are the
principal's rules of conduct. The full shape of the walkthrough and
the elicitation interview stays in the skill the second line points
to, read when one runs. A hook is context, not enforcement: it is
the nearest thing to a wall the harness offers for a rule of conduct,
and the forge says so.

## What the harness enforces

Where the harness can enforce the principal's word, the forge lets
it, so that a guarantee rests on the harness as well as on
`CLAUDE.md`. Protection relies on Claude Code's permission system,
not on an operating-system sandbox: commands and file operations run
under permission prompts and allowlists, and web access is approved
per domain on first use.

Three things are set in the engine's own files.

- **Deny rules.** `.claude/settings.json` denies Claude the user's
  sensitive paths (`~/.ssh`, `~/.aws`) and the raw `git` command in
  both shells (`Bash(git *)`, `PowerShell(git *)`). The scripts in
  `scripts/` are thereby the only door to git for Claude, reading
  state included; the rule binds the forge, not the principal, whose
  own git from the shell is his. In the same file `attribution.commit`
  is empty and `attribution.sessionUrl` is false, so no trailer is
  added or proposed to a commit: the message is the one the principal
  confirmed, word for word.
- **Guarded commands.** A command that writes, scaffolds, commits or
  regenerates (`/save`, `/release`, `/spinoff`, `/setup`,
  `/new-project`, `/new-artefact`, `/import-project`, `/ingest`,
  `/render`, `/publish`) carries `disable-model-invocation: true` in
  its front-matter, so that Claude cannot start it on his own
  judgement: the principal invokes it by slash, or asks in words and
  Claude follows the command's definition read by path. The guard
  also takes the descriptions of these commands out of the always-on
  context.
- **What stays Claude's to start.** Maps, reports and rosters
  (`/forge`, `/ledger`, `/check`, `/critique`, `/challenge`,
  `/research`, `/recipe`) carry no such field, since Claude is meant
  to propose them.

Immutability of documents is not among these: it remains a process
rule enforced by convention, because git protects nothing from a
commit that rewrites a file and a mechanism would be one more layer
that still would not stop a hand edit.

## What a subagent sees, and the scan

A subagent sees the session's whole context: `CLAUDE.md` as the
session read it, `CLAUDE.local.md` and the assistant's memory
included. It may take that copy for the file on disk. Two
consequences follow. Every agent that writes an outward-facing file
says in its own definition that instance facts are not material and
that an input is read from disk, not taken from context. And the
generated files are scanned mechanically before they are kept.

For the same reason `CLAUDE.local.md`, the instance's own file,
gitignored at the engine root, holds only what must be always-on and
is harmless in a public report: who the principal is, by role, and
the conversation language. Instance facts never enter a reviewer's
report, not even where they would explain a finding, because a
report is a public file or may be quoted into one. The git
identities, names, e-mail addresses, hosts, live in the user's own
git configuration outside the engine; the scripts carry no URL and
no identity.

## One model

The whole forge runs on one model, the session model, chosen once
in one deliberate place: `.claude/settings.local.json`, gitignored,
created by `/setup`. Every reviewer agent declares `model: inherit`
explicitly; there are no per-agent pins, because a pin ages and the
model the forge runs on should be a decision, never an accident.
Speed is bought with context, not with a weaker model: a reviewer, a
check and a render each run in an isolated subagent that sees only
its files, and the working conversation is spent on verdicts rather
than on reading.

Two exceptions are deliberate. A headless conversion behind
`/publish` has no session model, so `scripts/md2pptx.py` and
`scripts/md2docx.py` carry a default of their own in `--model`, an
explicit parameter rather than a pin. And a mirrored page of the
documentation leaves the model no room, so it is written on a faster
model, while a derived page, like the map, is written on the session
model; the choice is made mechanically by the page's entry, never
per run.

## Behaviour never lives in memory

Claude Code keeps a per-directory memory outside the repository.
Whatever it learns there about how the forge should work, a working
method, a rule of a command, a convention, is written into
`CLAUDE.md`, the commands or the templates and removed from memory,
so that every instance of the forge behaves the same and a new user
meets the same forge as the principal. Memory is left with what is
personal to one principal: his idiom, his private choices. Instance
facts go to `CLAUDE.local.md`.

## The forge explains itself

`/man [command | method]`, alias `/manual`, is the forge's manual: a
reader of the forge's own definitions, never a text of its own,
because a second text would be a second copy that drifts. What a
command does in full is its skill, and `/man <command>` prints it.
The name follows the Unix manual; `/help` is a built-in of Claude
Code.

## See also

- [About what the forge is made of](../extend/what-it-is-made-of.md): the files of the operating layer.
- [Configuration](../reference/configuration.md): the settings, exactly.
