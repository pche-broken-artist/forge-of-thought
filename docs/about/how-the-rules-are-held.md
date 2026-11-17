---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 535a7ce5eec4a85c
inputs:
  - CLAUDE.md#What this workspace is
  - CLAUDE.md#Prime directives
  - CLAUDE.md#Working methods
  - CLAUDE.md#Isolated reviewers
  - CLAUDE.md#Commands
  - CLAUDE.md#ID scheme
  - CLAUDE.md#Repository layout
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
  - projects/forge/40-solution-design.md#SOL.0110
  - projects/forge/40-solution-design.md#SOL.0520
---

# How the rules are held

How the rules are held is the forge's answer to one question: what
keeps a rule in force through a long conversation and inside a
[subagent](../reference/glossary.md) (an agent Claude launches for
one job, such as a review or a render), when the rule is only text
that Claude reads. This page explains the ways the forge uses and the
reasons recorded for each. It is for the extender, who must know
where a new rule belongs, and for the evaluator, who wants to know
which rules are enforced and which are asked of Claude.

## What it is

The forge runs in Claude Code. The slash commands, the skills, the
agents and the hooks are mechanisms of Claude Code, and the forge is
what they are told. A rule of the forge is therefore text in a file
of the operating layer (the files that tell Claude how the forge
works, listed in
[What the forge is made of](../extend/what-it-is-made-of.md)).

Two things work against a rule that is only text. The first is
length: text loaded once dissolves as the conversation grows. The
second is a stale copy: a subagent receives the forge's core file
(`CLAUDE.md`) as the session read it and may take that copy for the
file on disk. A session is one conversation with Claude in Claude
Code.

The forge holds a rule in four ways:

| How a rule is held | What carries it | When it reaches Claude |
|---|---|---|
| Always on | the core `CLAUDE.md`, the instance file `CLAUDE.local.md`, the description of every command | in every session; the two files in every subagent as well |
| Read on demand | a skill, a file of `.claude/reference/` | when its situation arises |
| Repeated | the lines that `scripts/hook-walkthrough.py` prints | at every prompt |
| Enforced by the harness | the deny rules and `scripts/hook-git.py`, both configured in `.claude/settings.json` | when Claude uses a tool |

The [harness](../reference/glossary.md) is Claude Code: the agent the
forge runs in, whose hooks and permission rules the engine's settings
configure. The engine is the repository that holds the forge itself.

Beside the four ways stand rules on where a rule lives and how it is
read:

- One mechanism lives in one place and is cited by path everywhere
  else.
- Every isolated subagent reads its inputs from disk.
- The whole forge runs on one model.
- The forge's behaviour never lives in the assistant's memory.
- The forge explains itself through one command: `/man`.

## How it works

### The core and the files it points to

`CLAUDE.md` at the root of the engine is the universal core. Claude
Code loads it into every session, and it reaches every subagent. It
carries what must hold everywhere, such as the prime directives and
the working methods in short. A rule of one artefact (a document of
the chain a thought travels) is not in the core. It stands in the
[definition](../reference/glossary.md) of that artefact.

Beside the core stands the instance file (`CLAUDE.local.md`). An
[instance](../reference/glossary.md) is one installation of the
forge, and the file holds its facts:

- who the [principal](../reference/glossary.md) is (the principal is
  the person whose thinking is being forged)
- the language the conversation runs in
- the handle the principal signs records with

The file stands at the root of the engine, is kept out of the
repository and is filled by `/setup` on a new machine. Everything in
it reaches every subagent, the isolated reviewers included.

The description of every command stays in the always-on context as
well. Everything else is a file read when its situation arises. The
skill of a command (the file `.claude/skills/<name>/SKILL.md`, which
says what the command does) is read when the command runs. The files
of `.claude/reference/` are read when something is looked for:

- `.claude/reference/commands.md`: the table of the commands, read
  when a command is looked for.
- `.claude/reference/id-prefixes.md`: the table of the ID prefixes,
  read when a prefix is looked for.
- `.claude/reference/repository-layout.md`: the root of the engine,
  file by file, read when a file of the engine is looked for.

The core names each of these files and says when it is read. The
table or the listing itself stands in the file.

The pattern is one always-on sentence and a pointer, with the detail
in a file read when its situation arises. The
[walkthrough](../reference/glossary.md) is the first case of the
pattern. A walkthrough is the way a list of items that need the
principal's decision is worked: one item per message, every
proposition closed with the verdict line
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. The core
carries the rule in short and names
`.claude/skills/walkthrough/SKILL.md`. That file holds the full shape
and is read whenever a walkthrough or an elicitation interview
(questions that draw out what the principal has not yet articulated)
runs.

### One mechanism in one place

Whatever the forge has a procedure for, such as a command or a
script, is used through the file that defines it whenever its
situation arises. It is never described a second time and never
improvised. A command that needs the mechanism of another cites it by
path and adds nothing of its own to how it runs. The rules of a
mechanism, such as its isolation or what it may read, are written
once, in its own file. A procedure stated in two places is a defect.

The principal's request in free words is the command. What the
principal asks for runs through the file that defines it, as if the
command had been typed. What runs only on the principal's word still
does.

Two things are not a second place. A one-line reminder at the point
of action that names its owner is not a restatement. A shape that had
no owner at all gets a template, not a second description.

A check named `single-source-of-truth` carries the rule over the
whole operating layer. A check is a reviewer of mechanical
conformance with the conventions. This one runs on the principal's
word and never at a release on its own.

### What is repeated at every prompt

A rule that must hold in a long conversation is not trusted to the
core alone. The engine's settings register a hook on every prompt:
`scripts/hook-walkthrough.py`. A hook is a program the harness runs
at a fixed moment. The harness adds what this hook prints to the
context of the turn. The hook prints:

- The one-item rule of the walkthrough: one item per reply. Claude
  acknowledges the last verdict, puts one item forward, closes a
  proposition with the verdict line and stops. A question from the
  principal keeps the item open: Claude answers, then closes the item
  again.
- The pointer to the full shape: while a walkthrough or an interview
  is running, Claude works by `.claude/skills/walkthrough/SKILL.md`.
- Lines of conduct, which are the principal's rules:
  - Tools: where the forge has a script, Claude uses the script and
    never the raw tool. Git is read directly, and every write of git
    goes through the forge's scripts.
  - Skills: where the forge has a skill for what is asked or for what
    Claude is about to do, Claude runs the skill at once and never
    does its work by hand.
  - Own commands: before running anything of its own that is not
    plain reading, Claude says what it does and why, and waits for
    the principal's yes.
  - Consent: Claude writes, runs and changes nothing that was not
    agreed and approved. A yes covers exactly what was asked, never
    its consequences.
  - Decisions: every question that asks the principal to decide is
    one proposition, with Claude's recommendation as what `accept`
    means, and ends with the verdict line. A yes that carries a
    question is `q`. Only a question for information Claude lacks
    ends with the question alone.

### What the harness enforces

The harness enforces the principal's word where it can. What it is
told to enforce stands in the engine's settings file
(`.claude/settings.json`); the settings, exactly, are in
[Configuration](../reference/configuration.md).

- Two deny rules keep Claude from reading two sensitive paths under
  the home directory: `~/.ssh` and `~/.aws`. A deny rule is a
  permission rule of the harness that refuses a use of a tool.
- A third deny rule (`PowerShell(git *)`) refuses git in the
  PowerShell tool, which is the other shell tool beside Bash.
- A second hook (`scripts/hook-git.py`) runs before every command
  Claude sends through the Bash tool and holds the line between
  reading git and writing it: it allows a command that reads git,
  puts the few commands that finish the step of a conflict to the
  principal, and denies every other command of git, naming the
  script of the forge to use instead
  ([Persistence in git](persistence-in-git.md)).
- Attribution is switched off: `attribution.commit` is empty and
  `attribution.sessionUrl` is false. Claude Code then adds and
  proposes no trailer to a commit: the commit message is the one the
  principal confirmed, word for word.

The protection is the permission system of the harness, not a sandbox
of the operating system. Commands and file operations run under
permission prompts and allowlists.

Both hooks are started in exec form: `python` with the path of the
script as its one argument. The path is anchored at the root of the
project by the placeholder `${CLAUDE_PROJECT_DIR}`. A relative path
would be resolved against the session's working directory and not
against the root of the engine.

### Commands that start on the principal's word

A command that changes files the moment it runs, with no round and no
`write` in between, starts on the principal's word and never on
Claude's judgement. A [round](../reference/glossary.md) is one
working conversation: what is agreed in it is written once at its
end, on the principal's word `write`. The principal invokes such a
command by slash, or asks in words and Claude invokes the skill
itself. Claude never replays the steps of the skill by hand.

The guard is conduct and the hook on git. The conduct is the
step-by-step method
([The working methods](working-methods.md)): an action that needs the
principal's consent arrives as one step, with the exact operation,
its target and the reason stated, and runs on the principal's word.
The harness has a field that blocks the model from invoking a skill
(`disable-model-invocation`). No command of the forge carries it:
every skill can be invoked by Claude.

Other commands need no such guard:

- A command that writes only at the end of a round, on the
  principal's word, has the word in its procedure already.
- A command that files the immutable record of a run the principal
  asked for has it as well.
- A command that shows an overview or a roster stays Claude's to
  start. Claude is meant to propose it.
- A run of a reviewer or of a research is proposed by Claude and
  started on the principal's word.

### Inside a subagent

An isolated subagent sees nothing of the conversation. It does
receive the core as the session read it, the instance file and the
assistant's memory, and it may take such a copy for the file on disk.
Every isolated subagent therefore reads every input from disk in its
own run, whatever its job. It lets no instance fact into what it
returns. Every agent that writes an outward-facing file says both
rules in its own file. The generated files are scanned mechanically
before they are kept.

### One model

Every command, every state of the chain and every reviewer runs on
the session model, which is the model chosen for the session. It is
chosen in one deliberate place, as a preference of the instance.
Speed is bought with context and not with a weaker model: a render (a
generated output) and a check each run in an isolated subagent that
sees only its files, never the working conversation. Two exceptions
are named:

- The headless conversions behind `/publish`. A headless run has no
  session model, so each conversion takes a default of its own, as
  an explicit parameter.
- The documentation writer. A mirrored page (a page that restates
  what its inputs say) is written on a faster model. A derived page
  (a page put together from evidence in several files) is written on
  the session model. The choice is made mechanically, by how the
  page is made, never per run.

### Nothing in the assistant's memory

Claude Code keeps a memory per directory, outside the repository. The
forge's behaviour never lives there. Whatever Claude Code learns
there about how the forge should work, such as a working method or a
rule of a command, is written into the core, a command or a template
and removed from the memory. The memory is left with what is personal
to one principal, such as an idiom or a private choice. Instance
facts go to `CLAUDE.local.md`.

### One manual

The forge explains itself through one command: `/man`
([Look up a command, or ask how to do
something](../use/look-up-a-command.md)). The manual is a reader and
has no text of its own. It reads the documentation and the files that
define the forge in the run and never answers from memory. A need
said in free words gets the way the forge has for it, in plain
sentences and cited by path, never retold. Where the forge has
nothing, the answer says so and marks what Claude would do without a
mechanism as Claude's own. There is no second help command.

## Why

**A small core and pointers.** The core is the file Claude Code loads
into every session, and what it costs is its size. One always-on
sentence and a pointer was chosen against the whole method in the
core. The instance file is kept small for a reason of its own:
everything in it reaches every subagent, so only what must be always
on and is harmless in a public report lives there.

**One place.** Two copies of a procedure drift, and the copy without
a rule silently loses it. A one-line reminder that names its owner is
no copy: it is what Claude reads when it acts, and the citation keeps
it honest. The check on the rule runs only on the principal's word.
The purpose is that the rule costs a release nothing and that the
sweep is honest when it runs.

**Repetition.** Text loaded once dissolves as the conversation grows.
A hook that repeats a rule was chosen against trusting text loaded
once. The cost is that a hook of this kind is context and not
enforcement. Of a gate that would enforce the lines of conduct, the
half on git is built, as the second hook, and the rest is open. The
repetition is a trial, judged by behaviour.

**The permission system.** A sandbox of the operating system was the
alternative, and it was not taken: it is unavailable on Windows,
where enforcing it meant no shell at all.

**The hook on git.** The rule that git is written only through the
forge's scripts is held by the harness and not by conduct alone, on
every way Claude can reach git. The purpose is one door to a write of
git (one way in, through the forge's scripts) and one parser: this is
why the PowerShell tool is closed to git whole. The parser is a
heuristic, and what it cannot read it denies.

**No blocking field.** The field that blocks the model from a command
did not make Claude wait for the principal's word. It made Claude
mimic the command outside the skill, where the principal could not
see it, and the mimicry became its standard. Conduct and the hook on
git were chosen against the field.

**Reading from disk.** The copy of the core in a subagent's context
may be older than the file. A report of a subagent is a public file,
or may be quoted into one. The ban on instance facts therefore holds
even where a fact would explain a finding.

**One model.** The strongest model the forge runs on is to be a
decision and never an accident of a pin that has aged. Pinning single
commands to a faster model is rejected for now: the routine commands
are a small share of the work, they are slow for the size of the
context they carry and not for the model, and every pin is a
convention to keep. The documentation writer is an exception for a
reason of its own: a mirrored page leaves the model no room.

**No memory.** The purpose is that every instance of the forge
behaves the same and that a newcomer meets the same forge as the
principal.

**One manual.** A manual with a text of its own would be a second
place for what the forge's files already say. A second help command
was rejected: a second name for a question is one more thing to
learn.

## A worked example

A principal and Claude are late in a long conversation. They are
settling the findings of a review, one by one.

1. The principal sends a verdict on one finding. The harness runs the
   per-prompt hook and adds what it prints to the context of the
   turn. The one-item rule stands in front of Claude again, however
   long ago the core was loaded. Claude acknowledges the verdict,
   puts the next finding forward, closes it with the verdict line and
   stops.
2. The principal then asks, in free words, for the work to be saved.
   The request is the command. `/save` changes files the moment it
   runs, so it starts on this word and not before. Claude invokes
   the skill of `/save` itself, and the skill is read now, when its
   situation has arisen.
3. Suppose Claude had replayed the save by hand and sent
   `git commit -m "<message>"` through the Bash tool. The hook on git
   judges the command before it runs and answers deny. The reason it
   gives names the rule (the scripts in `scripts/` are the only door
   to a write of git) and the script to use instead:
   `python scripts/forge-save.py <slug> -m "<message>"`.
4. `git status` sent the same way reads git, and the hook allows it.
5. A command that begins with `git`, sent through the PowerShell
   tool, meets the deny rule `PowerShell(git *)`.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): the
  files of the operating layer.
- [Persistence in git](persistence-in-git.md): the hook that holds
  the line between reading and writing git.
- [The working methods](working-methods.md): the step-by-step method
  the guard rests on.
- [Look up a command, or ask how to do
  something](../use/look-up-a-command.md): the manual, `/man`, as you
  use it.
- [Configuration](../reference/configuration.md): the settings,
  exactly.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
