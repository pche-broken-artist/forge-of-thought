---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - .claude/settings.json
  - scripts/hook-walkthrough.ps1
  - projects/forge/10-intent.md
  - projects/forge/40-solution-design.md
---

# About how the rules are held

This page explains how the forge keeps its rules in force: what is
always loaded, what is read only when it is needed, what a hook
repeats at every prompt and what the harness holds. It is for someone
who wants to extend the forge, or to judge how far its behaviour can
be relied on. It was put together from `CLAUDE.md`,
`.claude/settings.json`, the help header of
`scripts/hook-walkthrough.ps1`, and the forge's own intent and
solution design.

## One always-on core, everything else read when needed

`CLAUDE.md` in the engine root is the file Claude Code loads into
every session, and it holds for every subagent. It carries only what
must hold everywhere: the roles, the prime directives, the working
methods in short, the document kinds, the chain, the layout,
persistence, versioning, the ID scheme, the reviewers, the ledger and
the list of commands. Its cost is its size, which is why it is kept
to that.

A rule that belongs to one thing is not in that file. It lives in the
file read when that thing's situation arises: the command's
definition, the artefact's definition, a reviewer's contract, a
template. The always-on part stays small and the detail is reached by
path at the moment it applies. The walkthrough method is the model
case: what is always present is the rule in short and a pointer, and
the full shape is `.claude/skills/walkthrough/SKILL.md`, read whenever
a walkthrough or an interview runs.

Facts of one installation, such as who the principal is and which
language the conversation runs in, are not properties of the system
and are kept out of the engine's files. They sit in `CLAUDE.local.md`
at the engine root, gitignored, so that the shared rules are the same
everywhere.

## One mechanism, one place

Whatever the forge has a procedure for, whether a command, a skill, a
script or an agent, is used through its own definition whenever its
situation arises, never re-described or improvised. A command that
needs another's mechanism cites it by path and adds nothing of its
own to how it runs. So `/release` regenerates the README and release
notes through `/render` and ends by running `/save`, git is touched
through the scripts in `scripts/`, and reviews run through the
reviewer agents.

The reason is that two copies drift, and the copy without a rule
silently loses it. A procedure stated in two places is therefore a
defect. A restatement means steps, rules or a shape repeated; a
one-line reminder at the point of action that names its owner is not
one, since it is what Claude reads when he acts and the citation
keeps it honest. Where a shape had no owner at all, it gets a
skeleton rather than a second description. The check
`single-source-of-truth` sweeps the whole operating layer for
restatements, run on the principal's word.

## Text loaded once dissolves: the hook

A rule in `CLAUDE.md` is in context from the start, but as a
conversation grows, text loaded once dissolves. A rule that must hold
through a long conversation is therefore not trusted to `CLAUDE.md`
alone: it is repeated at every prompt by a hook.

The engine's `.claude/settings.json` registers one `UserPromptSubmit`
hook. It runs `pwsh` with
`${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.ps1`, so the script is
found from the engine root whatever the session's working directory,
and Claude Code adds what it prints to the context of that turn. The
script reads nothing, writes nothing and takes no arguments. It
prints:

- the one-item walkthrough rule, with the verdict line that closes a
  proposition;
- a pointer to the walkthrough skill for the full shape;
- three lines of conduct: use the forge's scripts rather than the raw
  tool, say what a command of one's own does and wait for a yes before
  running it, and change nothing that was not agreed and approved.

This is the same pattern as the core: always-on is one sentence and a
pointer, the detail a file read when its situation arises. A hook is
context, not enforcement. It puts the rule in front of Claude again
at every turn; whether it holds is judged by behaviour.

## What the harness holds

Where the harness can carry the principal's word, the forge leans on
it as well as on conduct.

- **Deny rules.** `.claude/settings.json` lists under
  `permissions.deny` the `git` command in both shells
  (`Bash(git *)`, `PowerShell(git *)`) and reading `~/.ssh` and
  `~/.aws`. This is how the rule that the scripts are the only door
  to git, reading state included, is carried by the harness and not
  by conduct alone. The rule binds the forge, not the principal: his
  own git from the shell is his. In the same file commit attribution
  is empty and the session link is off, so Claude Code adds no
  trailer and the commit message is the one the principal confirmed.
- **Commands that write.** The commands that write, scaffold, commit
  or regenerate (`/save`, `/release`, `/spinoff`, `/setup`,
  `/new-project`, `/new-artefact`, `/import-project`, `/ingest`,
  `/render`, `/publish`) carry `disable-model-invocation: true` in
  their front-matter, so that Claude cannot start them on his own
  judgement. The principal invokes them by slash, or asks in words and
  Claude follows the command's definition, read by path. The rule that
  a step needing consent runs only on the principal's word thereby
  rests on the harness as well as on `CLAUDE.md`.
- **Maps, reports and rosters.** `/forge`, `/ledger`, `/check`,
  `/critique`, `/challenge`, `/research` and `/recipe` carry no such
  field and stay Claude's to start, since he is meant to propose them.
- **Web access.** The user approves it per domain on first use.

All of this relies on Claude Code's permission system, not an
operating-system sandbox. A sandbox was tried and dropped: it is
unavailable on Windows, where enforcing it meant no shell at all.

## One model for the whole forge

Every command, chain state and reviewer runs on the session model.
The reviewer agents declare `model: inherit`, and the session model is
chosen once, in `.claude/settings.local.json`, gitignored, which
`/setup` creates. The strongest model the forge runs on is thereby a
decision, never an accident of a per-agent pin that has aged, and
every pin would be one more convention to keep. Speed is bought with
context, not with a weaker model: `/render` and the checks run in
isolated subagents that see only their inputs, never the working
conversation. The one exception is the headless conversions behind
`/publish`, which have no session model and carry a default of their
own as an explicit parameter.

## Behaviour lives in the engine, not in memory

Claude Code keeps a per-directory memory outside the repository.
Whatever it learns there about how the forge should work, whether a
working method, a rule of a command or a convention, is written into
`CLAUDE.md`, the commands or the templates and removed from memory.
That way every instance of the forge behaves the same, and a new user
meets the same forge as its principal. Memory is left with what is
personal to one principal, and instance facts go to `CLAUDE.local.md`.

## The forge explains itself

`/man [command | method]`, with the alias `/manual`, is the forge's
manual. It is a reader, never a text of its own: it prints what the
forge's own definitions say, so the explanation is not a second copy
that could drift from the rule it explains.

## See also

- [About what the forge is made of](../extend/what-it-is-made-of.md): the files of the operating layer.
- [Configuration](../reference/configuration.md): the settings, exactly.
