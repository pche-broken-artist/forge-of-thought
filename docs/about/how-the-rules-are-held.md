---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: da265d0ae99eb9a7
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
---

# How the rules are held

The rules of the forge are held by a layered arrangement: one
always-on core that every session and every subagent loads, files
that are read when their situation arises, a hook that repeats at
every prompt what must not fade, and a few walls that the harness
can enforce. This page explains that arrangement for the extender
who changes the operating layer and for the evaluator who wants to
know what keeps Claude on the rules through a long conversation and
inside a subagent (a separate run of Claude that sees nothing of the
conversation). It says what holds the rules, how each part works and
why it is so.

## What it is

The harness is Claude Code, the program the forge runs in: its slash
commands, skills, agents and hooks are the mechanisms, and the forge
is what they are told. A session is one conversation in it. The
principal is the person whose thinking is forged; Claude proposes
and the principal decides.

The rules are held in five ways.

- The core, `CLAUDE.md` at the engine root: the one file the harness
  loads into every session and every subagent. It carries what must
  hold everywhere: the roles, the prime directives, the working
  methods in short, the document kinds, the chain, the layout,
  persistence, versioning, the ID scheme, the reviewers, the ledger
  (the one file that says the state of a project, made at read time)
  and the list of commands. A rule of one artefact is not in the
  core but in that artefact's definition. Beside the core stands the
  instance file, `CLAUDE.local.md`: it says who the principal is, by
  role, and what language the conversation runs in, and it is kept
  out of the repository.
- Everything else: a file read when its situation arises. A command
  is a skill, a method has its skill, an artefact has its definition
  and its template, a script carries its help in its header. What
  these files are is said on [What the forge is made of](../extend/what-it-is-made-of.md).
- A hook at every prompt: a small script the harness runs on every
  message of the principal and whose output it adds to the context
  of that turn. It repeats the rule of the walkthrough (a list of
  items worked one per message, each closed with a verdict) and four
  lines of conduct.
- The walls of the harness: deny rules in the settings and a second
  hook that judges every git command before it runs.
- Conduct: the step-by-step method, by which anything that needs the
  principal's consent arrives as one step and runs on his word.

Three further rules keep the arrangement whole. One mechanism lives
in one place. Every isolated subagent reads its inputs from disk.
The forge's behaviour never lives in the assistant's memory.

## How it works

### One always-on core, the rest read when needed

The core is what the harness loads into every session and every
subagent, so whatever stands in it is in context at every moment.
Everything that is not in the core is in a file with an owner: a
skill, a definition, a template, a script. Such a file is read when
its situation arises. The pattern the core follows is: always-on is
one sentence and a pointer, the detail is a file read when its
situation arises. The walkthrough is the first instance of that
pattern. Its rule stands in the core in short, with a pointer to
`.claude/skills/walkthrough/SKILL.md`, and the shape of the item, of
the verdict, of the interview and of the write-up lives in that
skill, read whenever a walkthrough or an interview runs.

The instance file reaches every subagent, the isolated reviewers
included. Only what must be always-on and is harmless in a public
report lives there. The git identities, that is names, e-mail
addresses and hosts, live in the user's own git configuration
outside the engine. The session model lives in
`.claude/settings.local.json`, gitignored, so that the model the
whole forge runs on is chosen in one deliberate place.

### One mechanism lives in one place

Whatever the forge already has a procedure for, a command, a skill, a
script or an agent, is used through that procedure whenever its
situation arises. It is never re-described or improvised. A command
that needs another's mechanism cites it by path and adds nothing of
its own to how it runs. The rules of a mechanism, its isolation, its
wrapping, its provenance and what it may read, are written once, in
its own definition. A procedure stated in two places is a defect.
Where a shape had no owner at all, it gets a skeleton rather than a
second description. A one-line reminder at the point of action that
names its owner is not a restatement, because it is what Claude
reads when it acts, and the citation keeps it honest.

### A hook repeats what must hold through a long conversation

A rule that must hold in a long conversation is not trusted to the
core alone. The settings, `.claude/settings.json`, carry one hook of
the kind the harness runs on every prompt of the principal; its
script is `scripts/hook-walkthrough.py`. The harness adds what the
script prints to the context of that turn. The script reads nothing,
writes nothing and takes no arguments. The settings invoke it in
exec form with its path given through the harness's placeholder for
the project root, because a hook runs in the session's working
directory and not the engine root.

What the hook prints is six lines.

- The one-item rule of the walkthrough: one item per reply,
  acknowledge the last verdict, put one item forward, close a
  proposition with the verdict line, stop; a question from the
  principal keeps the item open.
- The pointer to the walkthrough skill, to be worked by whenever a
  walkthrough or an interview is running.
- Tools: where the forge has a script, Claude uses the script, never
  the raw tool; git is read directly and every write of it goes
  through the forge's scripts.
- Own commands: before running anything of its own that is not plain
  reading, Claude says what it does and why and waits for the
  principal's yes.
- Consent: Claude writes, runs and changes nothing that was not
  agreed and approved; a yes covers exactly what was asked, never
  its consequences.
- Decisions: every question that asks the principal to decide is one
  proposition with Claude's recommendation as what accept means, and
  it ends with the verdict line; a yes that carries a question is a
  `q`; only a question for information Claude lacks ends with the
  question alone.

The verdict line is `(a)ccept / (m)odify / (q)uestion / (r)eject /
(p)ark`. A hook is context, not enforcement: it is the nearest thing
to a wall the harness offers for a rule of conduct.

### The harness enforces what it can

The harness enforces the principal's word where it can. The settings
carry three deny rules. Two keep Claude from the user's sensitive
paths, the SSH and the AWS directories of the home folder. The third
keeps the PowerShell tool from git altogether, so that git runs
through one shell tool only, Bash, where a hook can judge it.

That hook is the second one of the settings, `scripts/hook-git.py`,
run before every Bash command Claude sends: it holds the line
between reading git and writing it, and it answers in one of three
ways, allow for a reading of git, ask for the few commands that
finish the step of a conflict, so that the harness puts the command
to the principal and runs it on his yes, and deny for everything
else, naming the script of the forge to use instead. The scripts in
`scripts/` are the door to a write of git. What the step of a
conflict is and how the scripts serve git is said on
[Persistence in git](persistence-in-git.md). The exact settings are
on [Configuration](../reference/configuration.md).

### A command that changes files starts on the principal's word

A command that writes, scaffolds, commits or regenerates starts on
the principal's word and never on Claude's judgement. The principal
invokes it by slash, or he asks in words and Claude invokes the
skill itself, never its steps replayed by hand. The guard is
conduct, the step-by-step method described on
[The working methods](working-methods.md), and the wall on git.

What separates a guarded command from the rest is this. A guarded
command changes files the moment it runs, with no round and no
`write` in between. A command that writes only at the end of a round
on the principal's word, or that files the immutable record of a run
he asked for, needs no guard, because the word is already in the
procedure. A map, a report or a roster stays Claude's to start,
since Claude is meant to propose them. The composition of a recipe
is the birth of a versioned document and is a step of its own.

No command of the forge carries the harness's field
`disable-model-invocation`, which blocks the model from invoking a
skill. Every skill is model-invocable, and the descriptions of all
commands stay in the always-on context.

### Inside a subagent

Every isolated subagent of the forge, a reviewer, a renderer, a
documentation agent or a research agent alike, sees nothing of the
conversation. It reads every input from disk in its own run. It
lets no instance fact into what it returns. Every agent that writes
an outward-facing file says in its definition that instance facts
are not material and that an input is read from disk, and the
generated files are scanned mechanically before they are kept. The
research agent's brief carries the same in its own words, because
its packet also goes to an engine that reads no file of the forge.

The whole forge runs on one model, the session model: every command,
every chain state and every reviewer. Speed is bought with context,
never with a weaker reviewer: a render, a check and a review each
run in an isolated subagent that sees only its files, and the
working conversation is spent on verdicts, not on reading. Two
exceptions are named. The headless conversions behind `/publish`
have no session model, so each carries a default of its own, as an
explicit parameter. A mirrored page of the documentation leaves the
model no room, so it is written on a faster model, the choice made
by the page's entry and never per run.

### The forge's behaviour never lives in memory

The harness keeps a per-directory memory outside the repository.
Whatever Claude learns there about how the forge should work, a
working method, a rule of a command, a convention, is written into
the core, the commands or the templates and removed from memory.
Memory is left with what is personal to one principal, his idiom and
his private choices, and instance facts go to the instance file.

### The forge explains itself through one door

The manual is `/man`, alias `/manual`: a reader with no text of its
own. It reads the definitions and the documentation in the run and
never answers from memory. A need said in free words, `/man` with a
question, gets the way the forge has for it, said in plain sentences
and cited by path, never retold. Where the forge has nothing, the
answer says so and marks what Claude would do without a mechanism as
its own. The name follows the Unix manual, because `/help` is a
built-in of the harness. There is no second help command. How you
use the manual is on
[Look up a command, or ask how to do something](../use/look-up-a-command.md).

## Why

The core is one file because it is the file the harness loads into
every session. What it costs is its size, and so a rule of one
artefact lives in that artefact's definition, not in the core.

The rest is read when its situation arises because text loaded once
dissolves as the conversation grows. The hook exists for the same
reason: a rule that must hold through a long conversation is
repeated at every prompt and not trusted to text loaded once. A hook
is context and not enforcement; that cost is accepted because a hook
is the nearest thing to a wall the harness offers.

One mechanism lives in one place because two copies drift, and the
copy without a rule silently loses it.

The other shell tool is closed to git whole so that there is one
parser and one door.

The guard on a command is conduct and the wall on git, not the
harness's field, because the field did not make Claude wait for the
word. It made Claude mimic the command outside the skill, where the
principal could not see it, and the mimicry became its standard.

A subagent reads its inputs from disk because it sees the session's
whole context, the core as the session read it and the assistant's
memory included, and may take that copy for the file on disk. The
copy of the core in its context may be older than the file.

Instance facts never enter what a subagent returns because a report
is a public file, or may be quoted into one. Only what is harmless
in such a file lives in the instance file, because the instance file
reaches every subagent.

One model for the whole forge, so that the strongest model the forge
runs on is a decision and never an accident of a pin that has aged.
Per-command pinning to a faster model is set aside, because the
routine commands are slow for the size of the context they carry and
not for the model, and every pin is a convention to keep.

The forge's behaviour lives in the engine and never in memory, so
that every instance of the forge behaves the same and a new user
meets the same forge as the principal.

There is one door for help and no second help command, because a
second name for a question is one more thing to learn.

## A worked example

The principal is deep in a long conversation over the intent of a
project with the slug `my-project`. He writes: "good, save it".

The hook has just run on that message, so the context of this turn
carries the one-item rule and the four lines of conduct again, as it
did at every message before. Claude does not write anything yet. It
puts one step forward, the save of `my-project` with the exact
operation and its reason, and closes it with the verdict line
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. The
principal answers `a`.

Claude invokes the skill `/save my-project`. It does not replay the
steps of the save by hand, because a mechanism is used through its
own definition, and the save reaches git through
`scripts/forge-save.py`.

Had Claude typed `git commit` into the Bash tool instead, the git
hook would have judged the command before it ran, denied it and
named `scripts/forge-save.py` as the way. Had it typed the same into
the PowerShell tool, the deny rule of the settings would have kept
git from running there at all. Neither is a promise of behaviour:
the hook at every prompt is context, and the walls hold only where
the harness can judge a command.

Later the principal asks for a check of the project. A check is a
report, so Claude may start it. The check runs in an isolated
subagent that sees nothing of the conversation and reads the
project's files from disk, since the copy of the core in its context
may be older. The report comes back to the conversation, and the
findings are settled there by walkthrough.

Then the principal asks: "how do I bring an old project in?" Claude
does not answer from memory. It invokes `/man` with the question,
which reads the definitions and the documentation in the run and
names the way the forge has for it, cited by path.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): the files of the operating layer.
- [Persistence in git](persistence-in-git.md): the hook that holds the line between reading and writing git.
- [The working methods](working-methods.md): the step-by-step method the guard rests on.
- [Look up a command, or ask how to do something](../use/look-up-a-command.md): the manual, `/man`, as you use it.
- [Configuration](../reference/configuration.md): the settings, exactly.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
