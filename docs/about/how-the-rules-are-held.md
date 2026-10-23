---
generated: 2026-10-23
version: 5.33
made: derived
inputs-hash: ea8c714dcb589749
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

The rules of the forge are held in force by a small always-on core,
by files read when their situation arises, and by what the harness
(Claude Code, the program that runs Claude and its tools) can enforce.
This page explains how these parts work together through a long
conversation and inside a subagent (a separate run of Claude that
sees only what it is given). It is written for the extender who
changes the forge and for the evaluator who wants to know how far
its rules can be trusted.

## What it is

The forge keeps its rules in layers.

- `CLAUDE.md`: the universal core. It is loaded into every session
  (one conversation of Claude with the principal, the person whose
  thinking is being forged) and into every subagent.
- The skills, agents, templates and scripts: files read when their
  situation arises. Each owns one mechanism.
- `CLAUDE.local.md`: the instance facts of one installation. It also
  reaches every session and every subagent.
- The hooks and deny rules of `.claude/settings.json`: what the
  harness repeats or enforces on every prompt and every tool call.

The files that make up this operating layer are listed on
[What the forge is made of](../extend/what-it-is-made-of.md). Every
term of the forge has one line in the [Glossary](../reference/glossary.md).

## How it works

### One core, everything else read on demand

`CLAUDE.md` carries what must hold in every session and for every
subagent. That is the roles, the prime directives, the working
methods in short, the document kinds, the chain, the layout,
persistence, versioning, the ID scheme, the reviewers, the ledger
(the single source of truth for a project's state) and the list of
commands. A rule of one artefact is not in the core. It lives in that
artefact's definition.

Everything else is a file read when its situation arises. The core
carries a rule in one sentence and a pointer to the file that holds
the detail. The walkthrough (the way a list of decisions is worked
with the principal, one item per message) is the first case of this
pattern. `CLAUDE.md` gives the rule in short, and the full shape lives
in `.claude/skills/walkthrough/SKILL.md`, read whenever a walkthrough
or an interview runs.

### One mechanism in one place

Whatever the forge has a procedure for (a command, a skill, a script,
an agent) is used through its own definition whenever its situation
arises. It is never re-described or improvised. A command that needs
another command's mechanism cites it by path and adds nothing of its
own to how it runs. The rules of a mechanism (isolation, provenance,
what may be read) are written once, in its own definition. A
procedure stated in two places is a defect.

A one-line reminder at the point of action that names its owner is
not a restatement. An example is "not under git is a fact, not a
defect (CLAUDE.md, Persistence)". A restatement is steps, rules or a
shape repeated.

### A rule repeated at every prompt

A rule that must hold through a long conversation is not trusted to
`CLAUDE.md` alone. A per-prompt hook, `scripts/hook-walkthrough.py`,
is configured in `.claude/settings.json` as a `UserPromptSubmit` hook.
The harness runs it on every prompt and adds what it prints to the
context of that turn. It prints five lines:

```
Walkthrough rule: one item per reply - acknowledge the last verdict, put one item forward, close a proposition with '(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark', stop. A question from the principal keeps the item open: answer, then close it again.
When a walkthrough or an interview is running, work by .claude/skills/walkthrough/SKILL.md.
Tools: where the forge has a script (scripts/*.py), use the script, never the raw tool. git: read directly, every write through scripts/forge-*.py (the hook denies the rest).
Own commands: before running anything of your own that is not plain reading, say what it does and why, and wait for the principal's yes.
Consent: write, run and change nothing that was not agreed and approved. A yes covers exactly what was asked, never its consequences.
```

The first two lines are the walkthrough rule and the pointer to its
full shape. The other three are lines of conduct, the principal's
rules. The hook reads nothing and writes nothing.

A hook of this kind is context, not enforcement. It puts the rule in
front of Claude again at every turn. It does not make Claude follow
it.

### What the harness enforces

The harness enforces the principal's word where it can. Three things
stand in the forge's settings.

- Deny rules in `.claude/settings.json` keep Claude from reading the
  user's sensitive paths (`~/.ssh/**` and `~/.aws/**`). Web access is
  approved by the user per domain.
- A deny rule keeps the PowerShell tool from git altogether, so that
  git reaches Claude through one shell tool only.
- A second hook, `scripts/hook-git.py`, runs before every Bash command
  and holds the line between reading git, which is open, and writing
  it, which goes through the forge's scripts; how it works is
  explained on [Persistence in git](persistence-in-git.md).

A command that changes files the moment it runs is guarded by the
harness. That is `/save`, `/release`, `/pull`, `/spinoff`, `/setup`,
`/new-project`, `/new-artefact`, `/import-project`, `/ingest`,
`/render`, `/publish` and `/document`. Claude cannot start such a
command on its own judgement. The principal invokes it by its slash
command, or asks in words and Claude follows the command's definition
read by path.

A command that writes only at the end of a round on the principal's
word needs no guard. The same holds for a command that files the
immutable record of a run he asked for. The word is already part of
the procedure. Maps, reports and rosters (`/forge`, `/ledger`,
`/check`, `/critique`, `/challenge`, `/research`, bare `/recipe`)
stay Claude's to start, because Claude is meant to propose them.

The exact settings are on [Configuration](../reference/configuration.md).

### Subagents read from disk

A subagent sees the session's whole context. That includes
`CLAUDE.md` as the session read it and the assistant's memory. It may
take that copy for the file on disk. So every agent that writes an
outward-facing file says in its definition two things:

- instance facts are not material;
- every input is read from disk in its own run.

The generated files are also scanned mechanically before they are
kept.

`CLAUDE.local.md` reaches every subagent too, the isolated reviewers
included. Only what must be always-on and is harmless in a public
report lives there. Instance facts are forbidden in a reviewer's
report.

### One model

The whole forge runs on one model, the session model. Every command,
every state of the chain and every reviewer runs on it. The session
model is chosen in one place, as a preference of the instance. Speed
is bought with context, not with a weaker model: a subagent that sees
only its inputs does a mechanical job quickly. There are two
exceptions.

- The headless conversions behind `/publish` have no session model,
  so each takes a default of its own as an explicit parameter.
- The documentation writer writes a mirrored page on a faster model
  and a derived page on the session model, chosen by the page's entry
  in the documentation map.

### Nothing in the assistant's memory

Claude Code keeps a per-directory memory outside the repository. How
the forge should work never lives there. A working method, a rule of
a command or a convention learnt there is written into `CLAUDE.md`,
the commands or the templates, and removed from memory. Memory is
left with what is personal to one principal. Instance facts go to
`CLAUDE.local.md`.

### The forge explains itself

`/man [command | method]` (alias `/manual`) is the forge's manual. It
reads the forge's own definitions and has no text of its own.

## Why

- **The core is small and always on.** `CLAUDE.md` is the file Claude
  Code loads into every session. Its cost is its size. That is why the
  detail lives in files read on demand.
- **One place per mechanism.** Two copies of a procedure drift. The
  copy without a rule silently loses it.
- **A hook repeats the rule.** Text loaded once dissolves as the
  conversation grows. A rule seen at every prompt stays in front of
  Claude. A hook is the nearest thing to a wall that the harness
  offers for conduct.
- **One shell tool for git.** With the other shell closed to git,
  there is one parser and one door.
- **Guarded commands.** A guarded command changes files with no round
  and no `write` in between. The guard means the principal's consent
  rests on the harness as well as on `CLAUDE.md`.
- **Reading from disk and scanning.** A subagent may take the
  session's copy of a file for the file on disk. It may also carry
  instance facts it was never meant to use.
- **One model.** The strongest model the forge runs on is then a
  decision, never the accident of a pinned model that has aged. Every
  pin is also a convention to keep.
- **No behaviour in memory.** Every instance of the forge behaves the
  same, and a new user meets the same forge as the principal.
- **`/man` reads the definitions.** A manual with a text of its own
  would be a second place for each mechanism. It is named after the
  Unix manual, because `/help` is a built-in of Claude Code.

## A worked example

The principal runs a long working session on a project `my-project`.
A critic run has produced a list of findings, and Claude offers a
walkthrough.

1. The principal accepts the walkthrough. The hook prints its five
   lines into that turn. Claude reads
   `.claude/skills/walkthrough/SKILL.md` and puts the first finding
   forward, closed with the verdict line.
2. Many prompts later the walkthrough rule is still printed at the
   top of the turn. Claude puts one item forward, not three.
3. At the end the principal types `write`. Claude writes the agreed
   changes and proposes to save. It does not start `/save` itself:
   the command is guarded, and the principal types `/save my-project`.
4. Suppose Claude had tried to commit with a raw `git commit` in the
   Bash tool. The git hook answers with a deny that names the script
   to use instead.
5. Later the principal types `/document my-project`. The writer runs
   as a subagent, reads every input from disk and leaves instance
   facts out. The generated pages are scanned before they are kept.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): the
  files of the operating layer.
- [Persistence in git](persistence-in-git.md): the hook that holds the
  line between reading and writing git.
- [Configuration](../reference/configuration.md): the settings,
  exactly.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-23 for version 5.33 from the files the
front-matter names; never edited by hand.
