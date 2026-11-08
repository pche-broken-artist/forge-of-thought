---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 40ee2c84ba6128f7
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
  - projects/forge/40-solution-design.md#SOL.0110
  - projects/forge/40-solution-design.md#SOL.0520
---

# How the rules are held

The rules of the forge are held by a small set of mechanisms that
work together: one always-on file, a hook that repeats a rule at
every prompt, a few settings of the harness, a wall on git, and the
conduct of Claude itself. This page explains those mechanisms, how
they fit together and why each is shaped as it is. It is written for
the extender who changes the forge and the evaluator who wants to
know what keeps Claude on its rules through a long conversation and
inside an isolated subagent (a separate run of Claude that does one
job and returns its result). The principal (the person whose
thinking is forged, and the final authority on all content) will
meet these mechanisms in use without needing to know them. The
harness is Claude Code, the program that runs Claude and its tools.
A session is one run of that program, from the moment it is opened.
The terms of the forge are collected in the [Glossary](../reference/glossary.md).

## What it is

The forge is a set of instructions, not a program that runs by
itself. Its rules hold only as far as Claude reads them and acts on
them. Four things keep them in force.

- One always-on core, the file `CLAUDE.md` at the engine root. The
  harness loads it into every session and into every subagent. It
  carries what must hold everywhere: the roles, the prime
  directives, the working methods in short, the document kinds, the
  chain, the layout, persistence, versioning, the ID scheme, the
  reviewers, the ledger (the single source of truth for state, made
  at read time) and the list of commands.
- Everything else is a file read when its situation arises: a
  definition, a skill, a template, a script, an agent. The files of
  the operating layer are described in
  [What the forge is made of](../extend/what-it-is-made-of.md).
- Two hooks and a few deny rules in `.claude/settings.json`. These
  are what the harness enforces mechanically; they are listed
  exactly in [Configuration](../reference/configuration.md).
- Conduct: the working methods, above all the step-by-step method,
  described in [The working methods](working-methods.md).

A fifth thing is a boundary rather than a mechanism: the forge's
behaviour never lives in the assistant's private memory.

## How it works

### One mechanism in one place

Whatever the forge has a procedure for, a command, a skill, a
script or an agent, is used through its own definition whenever its
situation arises. It is never re-described and never improvised. A
command that needs another's mechanism cites it by path and adds
nothing of its own to how it runs. The rules of a mechanism, such
as its isolation, its provenance and what it may read, are written
once, in its own definition. A procedure stated in two places is a
defect.

The always-on core follows the same pattern. Where a rule has a
shape of its own, the core carries one sentence and a pointer, and
the detail lives in a file read when its situation arises. The
walkthrough is the first instance of this pattern. A walkthrough is
any list of items that need the principal's decision, worked one
item per message. The core carries the one-item rule and the
pointer to `.claude/skills/walkthrough/SKILL.md`. That skill holds
the full shape of the item, the verdict, the elicitation interview
and the write-up, and it is read whenever a walkthrough or an
interview runs. The skill is not a command.

A rule of one artefact is not in the core but in that artefact's
definition.

### A rule repeated at every prompt

A rule that must hold through a long conversation is not trusted to
`CLAUDE.md` alone. A hook of the harness, `scripts/hook-walkthrough.py`,
runs on every prompt the principal sends. `.claude/settings.json`
registers it as a `UserPromptSubmit` hook, and the harness adds what
it prints to the context of that turn. The script reads nothing,
writes nothing and takes no arguments. The settings invoke it as
`python` with the script's path under `${CLAUDE_PROJECT_DIR}`, so
that it is found from whatever directory the session started in.

What the hook prints is six lines, in the reader's words:

- The walkthrough rule: one item per reply. Claude acknowledges the
  last verdict, puts one item forward, closes a proposition with the
  verdict line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`
  and stops. A question from the principal keeps the item open:
  Claude answers, then closes the item again.
- The pointer: when a walkthrough or an interview is running, Claude
  works by `.claude/skills/walkthrough/SKILL.md`.
- Tools: where the forge has a script in `scripts/`, Claude uses the
  script, never the raw tool. Git is read directly; every write of
  git goes through `scripts/forge-*.py`.
- Own commands: before Claude runs anything of its own that is not
  plain reading, it says what the command does and why, and waits
  for the principal's yes.
- Consent: Claude writes, runs and changes nothing that was not
  agreed and approved. A yes covers exactly what was asked, never
  its consequences.
- Decisions: every question that asks the principal to decide is one
  proposition with Claude's recommendation as what `accept` means,
  and it ends with the verdict line. Such questions are a step that
  needs consent, a choice between options, an either/or, and whether
  to write. A yes that carries a question is `q`. Only a question
  for information Claude lacks ends with the question alone.

A hook is context, not enforcement. It is the nearest thing to a
wall that the harness offers for a rule of conduct, and it does not
guarantee that the rule is kept.

### What the harness enforces

The harness enforces the principal's word where it can. The
protection is the permission system of Claude Code and not a sandbox
of the operating system: commands and file operations run under
permission prompts and allowlists, and `.claude/settings.json`
carries shared deny rules.

The settings file holds three deny rules and two hooks.

- Two deny rules keep Claude from reading two sensitive paths,
  `~/.ssh` and `~/.aws`.
- One deny rule, `PowerShell(git *)`, keeps the PowerShell tool from
  git whole. There is one parser and one door for git, and it is the
  Bash tool.
- The per-prompt hook described above.
- A second hook, `scripts/hook-git.py`, registered as a `PreToolUse`
  hook on the Bash tool. It holds the line between reading git and
  writing it: it allows a reading call of git, denies a writing one
  and names the script of the forge to use instead, and puts the few
  commands that finish the step of a conflict to the principal, so
  that the harness runs them on his yes. How this wall works and
  what it means for a project in git is explained in
  [Persistence in git](persistence-in-git.md).

### A command that changes files starts on the principal's word

Some commands change files the moment they run, with no round of
conversation and no `write` in between. Such a command starts on
the principal's word and never on Claude's judgement. The principal
invokes it by slash, or asks in words and Claude invokes the skill
itself through the harness's Skill tool. Claude never replays the
steps of the skill by hand from its definition.

The guard on these commands is conduct: the step-by-step method and
the wall on git. No command of the forge carries the harness field
`disable-model-invocation`, which would block the model from
starting it. Every skill is model-invocable, and the descriptions of
all commands stay in the always-on context.

What separates a guarded command from the rest is the criterion
above. A command that writes only at the end of a round on the
principal's word, or files the immutable record of a run he asked
for, needs no guard, because the word is already in its procedure.
The maps and the rosters stay Claude's to start, since Claude is
meant to propose them. A run of a reviewer or a research is proposed
by Claude and started on the principal's word.

### Inside a subagent

Every isolated subagent of the forge, a reviewer, a renderer, a
documentation agent or a research agent alike, sees nothing of the
working conversation. It reads every input from disk in its own run.
It lets no instance fact into what it returns. A subagent sees the
session's whole context, including `CLAUDE.md` as the session read
it and the assistant's memory, and it may take that copy for the
file on disk. So every agent that writes an outward-facing file says
in its definition that instance facts are not material and that an
input is read from disk, and the generated files are scanned
mechanically before they are kept.

The instance facts, who the principal is by role and what language
the conversation runs in, live in `CLAUDE.local.md`, a file of the
instance kept out of the repository. Everything in that file
reaches every subagent, the isolated reviewers included. Therefore
only what must be always-on and is harmless in a public report lives
there.

### One model

Every command, every state of the chain and every reviewer runs on
the session model. Speed is bought with context, not with a weaker
model: a render, a check and a review each run in an isolated
subagent that sees only its files, and the working conversation is
spent on verdicts, not on reading. The session model is chosen in
one deliberate place, as an instance preference. Two exceptions are
named: the headless conversions behind `/publish`, which have no
session model and each carry an explicit default of their own, and
the writer of a mirrored page of the documentation, which runs on a
faster model because a mirrored page leaves the model no room.

### Nothing in the assistant's memory

Claude Code keeps a per-directory memory outside the repository.
Whatever Claude learns there about how the forge should work, a
working method, a rule of a command, a convention, is written into
`CLAUDE.md`, the commands or the templates and removed from memory.
Memory is left with what is personal to one principal, such as his
idiom and his private choices. Instance facts go to `CLAUDE.local.md`.

### One door to the manual

The forge explains itself through one door, `/man`, with the alias
`/manual`. It is named after the Unix manual, because `/help` is a
built-in of Claude Code. The manual is a reader with no text of its
own. It reads the definitions and the documentation in the run and
never answers from memory. A need said in free words, `/man
<question>`, is answered with the way the forge has for it, said in
plain sentences and cited by path, never retold. Where the forge has
nothing, the answer says so, and what Claude would do without a
mechanism is marked as its own. There is no second help command. How
to use the manual is described in
[Look up a command, or ask how to do something](../use/look-up-a-command.md).

## Why

The core is one file because it is the file Claude Code loads into
every session. What it costs is its size. The intent records no
alternative that was weighed.

A rule that must hold through a long conversation is repeated by a
hook because text loaded once dissolves as the conversation grows.
The repetition is judged by behaviour, not by the text being
present. The pattern of one sentence and a pointer in the core,
with the detail in a file read when its situation arises, keeps the
core small while the rule stays reachable.

One mechanism lives in one place because two copies drift, and the
copy without a rule silently loses it. Where a shape has no owner at
all, it gets a skeleton rather than a second description. A one-line
reminder at the point of action that names its owner is not a
restatement, since it is what Claude reads when it acts, and the
citation keeps it honest.

The protection is the permission system and not a sandbox of the
operating system because such a sandbox is unavailable on Windows,
where enforcing it meant no shell at all. The wall on git is a hook
and not a deny rule on the writing verbs because a prefix rule
matches the text usually typed and not the command, so that a
differently spelled call passes it; a deny rule cannot be carved by
an allow rule and is not overridden by a hook; and two walls with
one hole read worse than one. The other shell tool is closed to git
whole so that there is one parser and one door.

The guard on a command that changes files is conduct and not the
harness field that blocks the model, because that field did not make
Claude wait for the principal's word. It made Claude mimic the
command outside the skill, where the principal could not see it, and
the mimicry became its standard. Invoking the skill itself keeps
the run inside the definition, where it is visible.

Every isolated subagent reads its inputs from disk because the copy
of the core in its context may be older than the file. The generated
files are scanned mechanically because a subagent may take the
session's copy of a file, the assistant's memory included, for the
file on disk, and a definition alone cannot be relied on to keep
every instance fact out of what it writes.

One model runs the whole forge so that the strongest model the forge
runs on is a decision and never an accident of a pin that has aged.
Every pin is a convention to keep, and the routine commands are slow
for the size of the context they carry, not for the model.

The forge's behaviour is kept out of the assistant's memory so that
every instance of the forge behaves the same and a new user meets
the same forge as the principal.

The manual is one door with no second help command because a second
name for a question is one more thing to learn.

## A worked example

A principal and Claude are deep in a long conversation over a list
of findings from a critique. With every prompt the principal sends,
the per-prompt hook adds its six lines to the turn, so that the
one-item rule stands in front of Claude at the fiftieth message as
it did at the first. Claude acknowledges the last verdict, puts the
next finding forward with its recommendation, and closes with
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. The
principal answers `a`, and the verdict is carried to the one write
at the end of the round.

At the end of the round the principal types `write`, and Claude
writes the agreed changes. The principal then says in words that he
wants the project saved. Saving changes files the moment it runs,
so Claude does not type `git commit` into the Bash tool and does not
replay the steps of the save by hand. It invokes the skill of
`/save` itself, and the save runs inside its own definition. Had
Claude typed `git commit` into the Bash tool, the git hook would
have denied the command and named `scripts/forge-save.py` as the
door. Had it reached for the PowerShell tool, the deny rule would
have closed git to it whole.

Later Claude launches a reviewer as an isolated subagent. The
reviewer carries a copy of `CLAUDE.md` in its context, but it reads
the file from disk before it relies on a rule, because the copy may
be older. It returns its report without a name, a host or any other
fact of the instance, and the report is scanned before it is kept.

Finally the principal asks, in free words, how a project is saved
without running the check. Claude does not answer from memory. It
invokes `/man` with the question, the manual reads the definition
of `/save` in the run, and the answer names the way the forge has
for it, cited by the path of that definition.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): the files of the operating layer.
- [Persistence in git](persistence-in-git.md): the hook that holds the line between reading and writing git.
- [The working methods](working-methods.md): the step-by-step method the guard rests on.
- [Look up a command, or ask how to do something](../use/look-up-a-command.md): the manual, `/man`, as you use it.
- [Configuration](../reference/configuration.md): the settings, exactly.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
