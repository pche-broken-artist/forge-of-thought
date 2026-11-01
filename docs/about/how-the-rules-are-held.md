---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 1d8dfc1b90879fcc
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
  - projects/forge/10-intent.md#REJ.0500
  - projects/forge/10-intent.md#POS.1200
  - projects/forge/40-solution-design.md#The instruction layer
---

# How the rules are held

The rules of Forge of Thought are held in layers: one file that is
always loaded, files read only when their situation arises, a hook
that repeats the rules most easily lost, and settings of the harness
that keep Claude away from what it must not touch on its own. This
page explains those layers and why they are built that way. It is
for the extender who changes a rule and needs to know where the rule
must live, and for the evaluator who wants to know how far the
forge's behaviour can be relied on.

## What it is

Three words are used throughout this page:

- the principal: the person whose thinking is being forged, with
  final authority on all content;
- the harness: Claude Code, the program that runs Claude, loads its
  files, runs its hooks and applies its settings;
- a session: one conversation of Claude in the harness.

The rules are held in these layers:

| When it acts | What holds the rule | Where it lives |
|---|---|---|
| Every session and every subagent | the universal core | `CLAUDE.md` |
| Every session and every subagent | the instance facts | `CLAUDE.local.md` |
| When its situation arises | the definition of a command, method or artefact | `.claude/skills/...`, `templates/...` |
| At every prompt of the principal | the per-prompt hook | `scripts/hook-walkthrough.py` |
| Before every shell command Claude sends | the git hook | `scripts/hook-git.py` |
| Always | the deny rules of the harness | `.claude/settings.json` |
| When Claude would start a command that changes files | the guard of the harness | the harness |
| When someone asks how the forge does something | the manual, `/man` | read from the definitions and the documentation |

The exact settings are on
[Configuration](../reference/configuration.md). The files of the
operating layer, one by one, are on
[What the forge is made of](../extend/what-it-is-made-of.md). Every
term of the forge in one line is in the
[Glossary](../reference/glossary.md).

## How it works

### One always-on core

`CLAUDE.md` in the engine root is the file the harness loads into
every session. It carries what must hold in every session and for
every subagent (a separate run of Claude, launched for one job, that
does not see the working conversation). That is the roles, the prime
directives, the working methods in short, the kinds of document, the
chain, the layout, persistence, versioning, the ID scheme, the
reviewers, the ledger and the list of commands. A rule of one
artefact is not in this file. It is in that artefact's definition.

Beside it stands `CLAUDE.local.md`. It holds the facts of one
installation (who the principal is by role, the language of the
conversation). It is kept out of the repository. It also reaches
every subagent, the isolated reviewers included. Only what must be
always-on and is harmless in a public report is therefore put there.

Everything else is a file read when its situation arises. The
pattern is one sentence and a pointer in the core, and the detail in
a file read at the moment it is needed. The walkthrough is the first
case of it. `CLAUDE.md` carries the rule in short and points to
`.claude/skills/walkthrough/SKILL.md`. Claude reads that skill
whenever a walkthrough (one item needing the principal's decision
put forward per message, closed by a verdict line) or an elicitation
interview runs.

### One mechanism in one place

Whatever the forge has a procedure for (a command, a skill, a
script, an agent) is used through its own definition whenever its
situation arises. It is never described again or improvised. A
command that needs another command's mechanism cites it by path and
adds nothing of its own to how it runs. The rules of a mechanism
(isolation, wrapping, provenance, what may be read) are written
once, in its own definition. A procedure stated in two places is a
defect.

A one-line reminder at the point of action that names its owner is
not a restatement. An example of the shape is "not under git is a
fact, not a defect (CLAUDE.md, Persistence)". Steps, rules or a
shape repeated are a restatement. The `single-source-of-truth` check
sweeps the whole operating layer for restatements, on the
principal's word.

### A hook repeats what a long conversation loses

A rule that must hold through a long conversation is repeated at
every prompt by a hook. It is not trusted to `CLAUDE.md` alone. The
hook is a `UserPromptSubmit` hook in `.claude/settings.json`. The
harness runs `scripts/hook-walkthrough.py` on every prompt of the
principal and adds what the script prints to the context of that
turn.

The script prints the walkthrough rule:

- one item per reply: acknowledge the last verdict, put one item
  forward, close a proposition with
  `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`, and stop;
- a question from the principal keeps the item open: Claude answers,
  then closes the item again.

It prints the pointer to the full shape: when a walkthrough or an
interview is running, Claude works by
`.claude/skills/walkthrough/SKILL.md`.

It prints four lines of conduct:

- tools: where the forge has a script, Claude uses the script and
  never the raw tool;
- own commands: before running anything of its own that is not plain
  reading, Claude says what it does and why, and waits for the
  principal's yes;
- consent: Claude writes, runs and changes nothing that was not
  agreed and approved, and a yes covers exactly what was asked;
- decisions: every question that asks the principal to decide is one
  proposition, with Claude's recommendation as what accept means,
  and ends with the verdict line.

A yes that carries a question counts as `q`. Only a question for
information Claude lacks ends with the question alone.

The hook's command is anchored at the engine root. The settings call
`python` with `${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.py` as
its one argument. A relative path would be resolved against the
session's working directory, which need not be the engine root.

A hook is context, not enforcement. It puts the rule in front of
Claude again at every prompt. It is the nearest thing to a wall that
the harness offers for conduct.

### The harness enforces what it can

The harness keeps Claude from some things directly:

- deny rules in `.claude/settings.json` keep Claude from reading the
  user's sensitive paths (the SSH and AWS folders of the home
  directory);
- a deny rule keeps the PowerShell tool from git entirely, so that
  git runs through one shell tool only;
- web access is approved by the user per domain.

A second hook, `scripts/hook-git.py`, runs before every command
Claude sends through the Bash tool and holds the line between
reading git and writing it. How it does so, and which scripts are
the door to a write of git, is on
[Persistence in git](persistence-in-git.md).

A command that changes files the moment it runs is guarded by the
harness, so that Claude cannot start it on its own judgement. Such a
command writes, scaffolds, commits or regenerates with no round and
no `write` in between. The principal invokes it by slash, or asks in
words and Claude follows the command's definition, read by path. A
command that writes only at the end of a round on the principal's
word needs no guard. Nor does a command that files the immutable
record of a run the principal asked for. The principal's word is
already in their procedure. Maps, reports and rosters stay Claude's
to start, because Claude is meant to propose them.

### A subagent reads from disk

A subagent sees the session's whole context. That includes
`CLAUDE.md` as the session read it and the assistant's memory. It
may take that copy for the file on disk, and the copy may be older.
Every isolated subagent of the forge (a reviewer, a renderer, a
documentation agent, a research agent) therefore reads every input
from disk in its own run. It sees nothing of the conversation. It
lets no instance fact into what it returns. Every agent that writes
an outward-facing file says in its definition that instance facts
are not material. The generated files are scanned mechanically for
instance facts before they are kept.

### One model

Every command, chain state and reviewer runs on the session model.
The session model is chosen in one place, as a preference of the
instance. There are two exceptions. A headless conversion behind
`/publish` has no session model and takes an explicit default of its
own. The documentation writer writes a mirrored page on a faster
model and a derived page on the session model, chosen by the page's
entry in the documentation map and never per run. Speed is bought
with context, not with a weaker model: a job is run in an isolated
subagent that sees only its inputs.

### Nothing in the assistant's memory

The harness keeps a memory per directory, outside the repository.
Whatever Claude learns there about how the forge should work (a
working method, a rule of a command, a convention) is written into
`CLAUDE.md`, the commands or the templates, and removed from memory.
Memory is left with what is personal to one principal, such as his
idiom and his private choices. Facts of the instance go to
`CLAUDE.local.md`.

### One door to the manual

The forge explains itself through one command, `/man` (alias
`/manual`). It is a reader with no text of its own. It reads the
definitions and the documentation in the run and never answers from
memory. Given a command or a method, it prints its definition. Given
a need in free words, it answers with the way the forge has for it,
in plain sentences, cited by path and never retold. Where the forge
has nothing, the answer says so. What Claude would do without a
mechanism is then marked as its own. How you use it is on
[Look up a command, or ask how to do something](../use/look-up-a-command.md).

There is no second help command. The command is named after the
Unix manual, because `/help` is a built-in of the harness.

## Why

- **Text loaded once fades.** As a conversation grows, a rule loaded
  once at the start dissolves. The rule that must hold is therefore
  repeated at every prompt.
- **The core costs its size.** `CLAUDE.md` is loaded into every
  session and every subagent. Detail is therefore kept in files read
  when their situation arises, and the core carries a sentence and a
  pointer.
- **Two copies drift.** A procedure stated in a second place drifts
  from the first, and the copy without a rule silently loses it.
  That is why one mechanism lives in one place.
- **A hook is not a wall.** The per-prompt hook only adds context.
  For what can be enforced, the forge uses the harness: the deny
  rules, the git hook and the guard on commands that change files.
  The principal's word then rests on the harness as well as on
  `CLAUDE.md`.
- **One parser and one door for git.** The PowerShell tool is closed
  to git so that only one shell tool reaches git, and one hook reads
  every git command.
- **A subagent's copy may be stale.** The copy of `CLAUDE.md` in a
  subagent's context may be older than the file. Reading from disk
  and scanning the output mechanically keep stale rules and instance
  facts out of what it returns.
- **The strongest model is a decision.** With one session model, the
  model the forge runs on is chosen deliberately. It is never the
  accident of a pinned model that has aged. Every pin is also one
  more convention to keep.
- **Every instance behaves the same.** Behaviour kept in one
  person's memory would make that instance differ from every other.
  Kept in the engine, a new user meets the same forge as the
  principal.
- **A manual that is read cannot drift.** `/man` has no text of its
  own, so it cannot disagree with the definitions it reads.
- **A second name is one more thing to learn.** A separate help
  command would add a second name for a question, and an alias costs
  a skill file of its own.

## A worked example

A principal works through a long list of findings on a placeholder
project `<slug>`, deep into a conversation.

1. The principal sends a verdict on one finding. Before Claude
   answers, the harness runs the per-prompt hook. The walkthrough
   rule and the four lines of conduct stand in the context of this
   turn, however long the conversation has grown.
2. Claude acknowledges the verdict, puts the next finding forward,
   closes it with the verdict line, and stops.
3. The principal answers "yes, but does this touch the template?".
   By the rule the hook printed, a yes that carries a question is
   `q`. Claude answers the question and puts the item to the
   principal again.
4. At the end of the round the principal says `write`. Claude
   reflects the round back and writes it once.
5. Suppose Claude then reaches for git directly and sends a raw
   `git commit` through the Bash tool. The git hook refuses it and
   names the forge's script to use instead. The commit goes through
   the forge's scripts, on the principal's word.
6. Later, a reviewer is launched as a subagent. It reads the
   project's files and `CLAUDE.md` from disk in its own run, not
   from the copy in the session's context, and returns its report
   with no instance fact in it.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): the
  files of the operating layer.
- [Persistence in git](persistence-in-git.md): the hook that holds
  the line between reading and writing git.
- [Look up a command, or ask how to do something](../use/look-up-a-command.md):
  the manual, `/man`, as you use it.
- [Configuration](../reference/configuration.md): the settings,
  exactly.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
