---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 5e10e8e845d7e893
inputs:
  - CLAUDE.md#Prime directives
  - CLAUDE.md#Working methods
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

The rules of the forge are held by a small always-on core, by files
read when their situation arises, and by what the harness can enforce.
The harness is Claude Code, the program that runs Claude, loads its
files and decides which of its tools may run. This page explains how
the rules stay in force through a long conversation and inside a
subagent (an isolated helper run of Claude that never sees the working
conversation). It is written for the extender who changes the forge and
for the evaluator who wants to know how far its rules can be trusted.

## What it is

The rules live in four places, each with its own job.

- `CLAUDE.md`: the universal core, loaded into every session and every
  subagent. A session is one working conversation with Claude.
- The skills, the agents, the templates and the scripts: files read
  when their situation arises, each the one owner of its mechanism.
- Two hooks: small scripts the harness runs at fixed moments. One
  repeats rules at every prompt; the other judges every command of git
  Claude sends.
- `.claude/settings.json`: deny rules the harness applies before any
  tool runs, and the configuration of the two hooks.

Which files make up this operating layer is listed in
[What the forge is made of](../extend/what-it-is-made-of.md). The
settings, exactly as they stand, are in
[Configuration](../reference/configuration.md).

## How it works

### One core, everything else read on demand

`CLAUDE.md` carries what must hold in every session and for every
subagent. That means the roles, the prime directives, the working
methods in short, the document kinds, the chain, the layout,
persistence, versioning, the ID scheme, the reviewers, the ledger and
the list of commands. The ledger is the report of a project's state,
made from its documents. A rule of one artefact is not in the core.
It is in that artefact's definition, the file that says what the
artefact is and how it is found.

The pattern is the same everywhere: always-on is one sentence and a
pointer, and the detail is a file read when its situation arises. The
walkthrough shows it. A walkthrough is the way a list of items needing
the principal's decision is worked: one item per message, each closed
with the verdict line `(a)ccept / (m)odify / (q)uestion / (r)eject /
(p)ark`. The principal is the person whose thinking is being forged
and who has the final word on all content. `CLAUDE.md` carries the
walkthrough rule in short with a pointer to
`.claude/skills/walkthrough/SKILL.md`. That skill holds the full shape
and is read whenever a walkthrough or an interview runs.

Facts of one installation, such as who the principal is and what
language the conversation runs in, do not live in the core. They live
in `CLAUDE.local.md` at the engine root. That file is kept out of the
repository and filled by `/setup` on a new machine. The session model
lives in `.claude/settings.local.json`, also kept out of the
repository.

### One mechanism in one place

Whatever the forge has a procedure for (a command, a skill, a script,
an agent) is used through its own definition whenever its situation
arises. It is never re-described or improvised. A command that needs
another command's mechanism cites it by path and adds nothing of its
own to how it runs. A procedure stated in two places is a defect.

A one-line reminder at the point of action that names its owner is
not a restatement. An example of such a reminder is "not under git is
a fact, not a defect (CLAUDE.md, Persistence)". A restatement is steps,
rules or a shape repeated. Where a shape has no owner at all, it gets
a template rather than a second description. A check named
`single-source-of-truth` sweeps the whole operating layer for
restatements when the principal asks for it.

### A rule repeated at every prompt

A rule that must hold through a long conversation is repeated at every
prompt by a hook. `.claude/settings.json` runs
`scripts/hook-walkthrough.py` on every prompt the principal sends, and
the harness adds what the script prints to the context of that turn.
It prints these lines:

```
Walkthrough rule: one item per reply - acknowledge the last verdict, put one item forward, close a proposition with '(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark', stop. A question from the principal keeps the item open: answer, then close it again.
When a walkthrough or an interview is running, work by .claude/skills/walkthrough/SKILL.md.
Tools: where the forge has a script (scripts/*.py), use the script, never the raw tool. git: read directly, every write through scripts/forge-*.py (the hook denies the rest).
Own commands: before running anything of your own that is not plain reading, say what it does and why, and wait for the principal's yes.
Consent: write, run and change nothing that was not agreed and approved. A yes covers exactly what was asked, never its consequences. Every step that needs consent (a write, a run, a commit, a change of a setting) is a proposition and ends with the verdict line; a yes that carries a question is q.
```

The first two lines are the walkthrough rule and the pointer to its
skill. The other three are lines of conduct, the principal's rules.
The hook adds context. It does not enforce anything.

### What the harness enforces

The harness applies what it can of the principal's word.

- Deny rules in `.claude/settings.json` keep Claude from reading the
  user's sensitive paths, `~/.ssh/**` and `~/.aws/**`.
- A deny rule closes the PowerShell tool to git whole, `PowerShell(git
  *)`, so that Claude reaches git through one shell tool only, Bash.
- A second hook, `scripts/hook-git.py`, runs before every Bash command
  and holds the line between reading git and writing it: a reading
  command passes, the few commands that finish a conflict are put to
  the principal to run on his yes, and everything else is denied with
  the script of the forge to use instead. How that line is drawn is
  explained in [Persistence in git](persistence-in-git.md).
- Web access is approved by the user per domain.
- A command that changes files the moment it runs is guarded by the
  harness, so that Claude cannot start it on its own judgement. `/save`,
  `/render` and `/document` are such commands. The principal invokes
  one by slash, or asks in words and Claude follows the command's
  definition read by path. Maps, reports and rosters, such as `/forge`,
  `/ledger` and `/critique`, stay Claude's to start.

How the harness guards a command (the setting that does it) is not in
the files this page is made from.

### What a subagent sees

A subagent sees the session's whole context. That includes `CLAUDE.md`
as the session read it and the assistant's memory, and a subagent may
take that copy for the file on disk. Therefore every agent that writes
an outward-facing file says in its definition two things: instance
facts are not material, and every input is read from disk. The
generated files are then scanned mechanically for the instance's facts
before they are kept. `CLAUDE.local.md` reaches every subagent too,
the isolated reviewers included. So only what must be always-on and is
harmless in a public report lives there.

### One model

Every command, chain state and reviewer runs on the session model, the
one model chosen for the session in one deliberate place. Two
exceptions exist. The headless conversions behind `/publish` have no
session model, so each takes a default of its own as an explicit
parameter. The documentation writer writes a page that only restates
its inputs on a faster model, and a page that puts evidence together on
the session model; the choice is made by the page's entry in the
documentation map, never per run.

### Not in memory

The forge's behaviour lives in the engine and never in the assistant's
private memory. Claude Code keeps a memory per directory outside the
repository. Whatever it learns there about how the forge should work
(a working method, a rule of a command, a convention) is written into
`CLAUDE.md`, the commands or the templates and removed from memory.
Memory keeps only what is personal to one principal, such as his idiom
and his private choices.

### The forge explains itself

`/man [command|method]`, with the alias `/manual`, is the forge's
manual. It reads the forge's own definitions and has no text of its
own.

## Why

- **One core, the rest on demand.** `CLAUDE.md` is the file Claude
  Code loads into every session. There was no real alternative. What
  it costs is its size, so the detail goes into files read when their
  situation arises.
- **One mechanism in one place.** Two copies of a procedure drift, and
  the copy without a rule silently loses it. A reminder that names its
  owner is allowed because it is what Claude reads when it acts, and
  the citation keeps it honest.
- **A rule repeated at every prompt.** Text loaded once dissolves as
  the conversation grows. A rule that must hold in a long conversation
  is therefore not trusted to `CLAUDE.md` alone. A hook is context, not
  enforcement; it is the nearest thing to a wall the harness offers.
- **One shell tool for git.** The PowerShell tool is closed to git so
  that there is one parser and one door. The prefix deny rules of the
  harness are not the wall for the writing commands of git. A prefix
  rule matches the text usually typed, not the command, so a command
  written in an unusual form passes it. A deny rule cannot be carved
  out by an allow rule and is not overridden by a hook, and two walls
  with one hole read worse than one.
- **The guard on commands.** A guarded command changes files the
  moment it runs, with no round and no `write` in between. A command
  that writes only at the end of a round on the principal's word needs
  no guard, because the word is already in the procedure. Maps,
  reports and rosters stay Claude's to start because it is meant to
  propose them.
- **Inputs read from disk.** A subagent may take the session's copy of
  a file for the file on disk. Reading from disk and scanning the
  output keep instance facts out of what is published.
- **One model.** The strongest model the forge runs on is then a
  decision, never the accident of a pin that has aged. Speed is bought
  with context, not with weaker models. Every pin would be one more
  convention to keep.
- **Not in memory.** Every instance of the forge then behaves the
  same, and a new user meets the same forge as the principal.
- **`/man` as a reader.** A manual with a text of its own would be a
  second place for each mechanism. It is named after the Unix manual
  because `/help` is a built-in of Claude Code.

## A worked example

The principal runs a review of a project with the placeholder slug
`example-project`, and the review returns a list of twelve findings.
A finding is one result of a reviewer.

1. Claude offers a walkthrough. The rule is in `CLAUDE.md`, and Claude
   reads `.claude/skills/walkthrough/SKILL.md` for its shape.
2. Claude puts the first finding forward and closes it with the
   verdict line. The principal answers `a`.
3. Many prompts later, the conversation is long. At every prompt the
   walkthrough hook has printed its lines again, so the one-item rule
   stands fresh in the context of the turn. Claude puts forward one
   finding, not three.
4. At the end of the round the principal types `write`. Claude
   reflects the round back and writes on his yes.
5. Claude then proposes to save, as one step closed with the verdict
   line. If it tried `git commit` in Bash instead, the git hook would
   deny the command and name `python scripts/forge-save.py <slug> -m
   "<message>"` (`/save`) as the way to use. `/save` itself is a
   guarded command, so it runs when the principal invokes it.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): the
  files of the operating layer.
- [Persistence in git](persistence-in-git.md): the hook that holds the
  line between reading and writing git.
- [Configuration](../reference/configuration.md): the settings, exactly.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
