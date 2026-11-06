---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 842c6e1aa9ddd6c0
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

The rules of the forge are held by a small set of mechanisms that
keep them in force where plain text would fade: one always-on core,
one owner per mechanism, a hook that repeats the rule that must
survive a long conversation, the harness where it can enforce, a
reading discipline for every isolated subagent, one model, no
behaviour in the assistant's memory, and one door through which the
forge explains itself. This page is for the extender who changes the
operating layer and for the evaluator who asks what keeps Claude to
the rules once a conversation has grown long or has left the
conversation altogether.

## What it is

The forge runs in Claude Code, the program for the command line that
the forge calls the harness. The harness loads one file, `CLAUDE.md`
at the engine root, into every session (one conversation in Claude
Code) and into every subagent (an isolated run of Claude with a
context of its own). That file is the always-on core. It carries
what must hold in every session and for every subagent: the roles,
the prime directives, the working methods in short, the document
kinds, the chain, the layout, persistence, versioning, the ID scheme,
the reviewers, the ledger and the list of commands. Everything else
is a file read when its situation arises: a command's skill, an
artefact's definition, a template, a script. The rule of one
artefact is not in the core but in that artefact's definition. What
those files are and where they live is the page [What the forge is
made of](../extend/what-it-is-made-of.md).

Beside the core stands one file of the instance (one installation
of the forge), `CLAUDE.local.md`, kept out of the repository. It
holds who the principal is, by role, and what language the
conversation runs in. The principal is the person whose thinking is
being forged. Everything in that file reaches every subagent, so
only what must be always-on and is harmless in a public report
lives there.

The rest of what holds the rules is not text but mechanism:

- a hook that prints at every prompt;
- deny rules and a second hook, set in `.claude/settings.json`;
- a guard of the harness on the commands that change files the
  moment they run;
- a reading rule for every isolated subagent, with a mechanical scan
  of what a subagent generates;
- one model for the whole forge, chosen in one place;
- a rule that moves what Claude learns about the forge out of its
  memory and into the engine;
- one manual command, `/man`, that reads and never recites.

## How it works

### One mechanism, one place

Whatever the forge has a procedure for, a command, a skill, a
script or an agent, is used through its own definition whenever
its situation arises. It is never re-described and never
improvised. A command that needs another's mechanism cites it by
path and adds nothing of its own to how it runs. The rules of a
mechanism, its isolation, its wrapping, its provenance, what it may
read, are written once, in its own definition. A procedure stated in
two places is a defect. Where a shape had no owner at all, it gets a
skeleton rather than a second description. A one-line reminder at
the point of action that names its owner is not a restatement. A
check named `single-source-of-truth` sweeps the whole operating
layer for restatements, on the principal's word and never at a
release on its own.

### The hook at every prompt

The always-on core is loaded once. A rule that must hold through a
long conversation is therefore not trusted to the core alone: a
hook, `scripts/hook-walkthrough.py`, registered in
`.claude/settings.json` as a hook on every prompt, prints the rule
again at every turn, and the harness adds what it prints to the
context of that turn. The hook reads nothing, writes nothing and
takes no argument. The settings invoke it in exec form, `python`
with the script's path as the one argument, and the path is anchored
at the engine root through the placeholder `${CLAUDE_PROJECT_DIR}`.
A relative path would be resolved against the session's working
directory, not the engine root.

What the hook prints is six lines: two on the walkthrough and four
of conduct. The walkthrough is the method by which any list of
items needing the principal's decision is worked one item per
message. The two walkthrough lines are:

- the one-item rule itself: one item per reply, the last verdict
  acknowledged, one item put forward, a proposition closed with
  `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`, then stop;
  a question from the principal keeps the item open, and Claude
  answers and then closes it again;
- the pointer to the file that holds the full shape,
  `.claude/skills/walkthrough/SKILL.md`, to be worked by whenever a
  walkthrough or an interview is running.

The four lines of conduct are the principal's rules:

- tools: where the forge has a script in `scripts/`, Claude uses the
  script and never the raw tool; git is read directly, and every
  write of git goes through a script `scripts/forge-*.py`;
- own commands: before running anything of its own that is not
  plain reading, Claude says what it does and why and waits for the
  principal's yes;
- consent: Claude writes, runs and changes nothing that was not
  agreed and approved; a yes covers exactly what was asked, never its
  consequences;
- decisions: every question that asks the principal to decide, a
  step that needs consent, a choice between options, an either/or,
  whether to write, is one proposition with Claude's recommendation
  as what `accept` means, and it ends with the verdict line; a yes
  that carries a question is `q`; only a question for information
  Claude lacks ends with the question alone.

The pattern is the one the forge applies everywhere: always-on is
one sentence and a pointer, the detail is a file read when its
situation arises. The detail here is the walkthrough skill, which
owns the shape of the item, of the verdict, of the elicitation
interview and of the write-up. A hook is context, not enforcement.

### What the harness enforces

The harness enforces the principal's word where it can. Three
things are set in `.claude/settings.json`; the file as it stands is
on the page [Configuration](../reference/configuration.md).

Two deny rules keep Claude from reading the user's sensitive paths,
`~/.ssh/**` and `~/.aws/**`. A third deny rule closes the PowerShell
tool to git whole. The one shell tool through which Claude runs git
is then Bash, so that there is one parser and one door. Web access
is approved by the user per domain.

A second hook, `scripts/hook-git.py`, runs before every Bash command
Claude sends and holds the line between reading git and writing it:
it answers allow for a reading git, ask for the few commands that
finish the step of a conflict, so that the harness puts the command
to the principal and runs it on his yes, and deny for everything
else, naming the script of the forge to use instead. The scripts in
`scripts/` are the door to a write of git. The rule binds the forge,
not the principal: his own git from the shell is his. How the
scripts and the hook work together is the page [Persistence in
git](persistence-in-git.md). The prefix deny rules of the harness
are not used as the wall for the writing verbs. A prefix rule
matches the text usually typed, not the command, so that a command
written another way passes it. A deny rule cannot be carved by an
allow rule and is not overridden by a hook. Two walls with one hole
read worse than one.

A command that changes files the moment it runs, with no round and
no `write` in between, is guarded by the harness, so that Claude
cannot start it on its own judgement. The principal invokes it by
slash, or asks in words and Claude follows the command's definition
read by path. A command that writes only at the end of a round on
the principal's word, or that files the immutable record of a run
the principal asked for, needs no guard. The word is already in the
procedure. Maps, reports and rosters stay Claude's to start, since
Claude is meant to propose them. The guarantee of the method Step by
step, that any action needing consent arrives as one step and runs
on the principal's word, thereby rests on the harness as well as on
the core.

### Inside a subagent

An isolated subagent sees nothing of the working conversation. It
does see the session's whole context as the harness hands it over:
`CLAUDE.md` as the session read it and the assistant's memory
included. It may take that copy for the file on disk, and the copy
may be older than the file. So every isolated subagent of the forge,
a reviewer, a renderer, a documentation agent or a research agent
alike, reads every input from disk in its own run, and every agent
that writes an outward-facing file says in its own definition that
an input is read from disk and that instance facts are not material.
No instance fact enters what a subagent returns: a report is a
public file, or may be quoted into one. The generated files are
scanned mechanically before they are kept. The research agent's
brief carries the same rules in its own words. Its packet also goes
to an engine that reads no file of the forge.

### One model

Every command, chain state and reviewer runs on the session model.
The session model is chosen in one deliberate place, an instance
preference in `.claude/settings.local.json`, a file kept out of the
repository. Speed is bought with context, not with a weaker model:
a render, a check and a reviewer each run in an isolated subagent
that sees only its files, and the working conversation is spent on
verdicts rather than on reading. Two exceptions are named. The
headless conversions behind `/publish` have no session model, so
each needs a default of its own, an explicit parameter rather than
a pin. The documentation writer writes a mirrored page, a page that
restates its inputs and leaves the model no room, on a faster model,
and a derived page on the session model; the choice is made by the
page's entry, never per run. A second engine beside the session
model is no exception to this: it runs beside, never instead, and
the session model keeps every job of the forge.

### Nothing of the forge in memory

Claude Code keeps a per-directory memory outside the repository.
Whatever Claude learns there about how the forge should work, a
working method, a rule of a command, a convention, is written into
`CLAUDE.md`, the commands or the templates and removed from memory.
Memory is left with what is personal to one principal, his idiom and
his private choices. Instance facts go to `CLAUDE.local.md`.

### One door to the manual

The forge explains itself from its own definitions through `/man`,
with `/manual` as its alias. The command is a reader and has no text
of its own. Given a command or a method, it reads the definition
that owns it. Given a need said in free words, `/man <question>`, it
answers with the way the forge has for that need, read from the
documentation and the definitions in the run, never from memory,
said in plain sentences and cited by path, never retold. Where the
forge has nothing, the answer says so and marks what Claude would do
without a mechanism as Claude's own. There is no second help command
and no further alias. How the manual is used is the page [Look up a
command, or ask how to do something](../use/look-up-a-command.md).
The name follows the Unix manual; `/help` is a built-in of Claude
Code.

## Why

One always-on core, because `CLAUDE.md` is the file Claude Code
loads into every session. The intent records no alternative that
was weighed. What the core costs is its size, which is why a rule of
one artefact lives in that artefact's definition and not in the
core.

The instance file stays small and harmless, because it reaches the
reviewers, whose reports are public files.

One mechanism in one place, because two copies drift, and the copy
without a rule silently loses it.

The hook, because text loaded once dissolves as the conversation
grows. A hook is the nearest thing to a wall the harness offers for
a rule of conduct. What it offers is context, not enforcement, and
this page makes no stronger claim.

The deny rule on the second shell tool and one hook on the first,
so that there is one parser and one door. Prefix deny rules are not
used for the writing verbs, because a prefix rule matches the typed
text and not the command, and two walls with one hole read worse
than one.

The guard on the commands that change files at once, because such a
command has no round and no `write` in which the principal's word
could be asked; the method Step by step then rests on the harness as
well as on the core.

Reading from disk inside a subagent, because the subagent's copy of
the core may be older than the file, and because its memory and
instance facts would otherwise leak into a public file.

One model, so that the strongest model the forge runs on is a
decision and never an accident of a pin that has aged. Every pin is
a convention to keep. A smaller model drifts from a recipe that
leaves it room, so the one place a faster model is used is the page
that leaves it none.

No behaviour in memory, so that every instance of the forge behaves
the same and a new user meets the same forge as the principal.

One door to the manual, because a second name for a question is one
more thing to learn, and an alias costs a skill file of its own.

## A worked example

A principal works through the findings of a critique on a project
with the slug `my-project`. The walkthrough is long. At the
fortieth prompt the core was read once, forty turns ago, and the
hook prints the one-item rule and the four lines of conduct again.
Claude puts the next finding forward, one item, and closes it with
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`.

The round ends and the principal says `write`. Claude writes the
agreed changes once and names the file and section it wrote. Claude
then proposes a save and stops, because `/save` changes files the
moment it runs and the harness guards it against being started on
Claude's own judgement. The principal types `/save my-project`, and
the command commits and pushes through the forge's script. Had
Claude instead typed `git push` into the Bash tool, the git hook
would have denied the command and named the script of the forge to
use instead; had it reached for the PowerShell tool, the deny rule
would have closed git to it whole.

A check the principal asks for runs in an isolated subagent. The
subagent carries the session's copy of `CLAUDE.md`, but it reads the
project's files and the engine's rules from disk in its own run, and
its report names no person, no host and no address. The report comes
back with its findings unnumbered; the command numbers and files it.

Later a newcomer asks in free words how a thing is done in the
forge. `/man` with that question reads the definitions and the
documentation in the run and answers with the way the forge has for
it, in plain sentences, cited by path. Nothing of the answer comes
from memory.

## See also

- [What the forge is made of](../extend/what-it-is-made-of.md): the
  files of the operating layer.
- [Persistence in git](persistence-in-git.md): the hook that holds
  the line between reading and writing git.
- [Look up a command, or ask how to do
  something](../use/look-up-a-command.md): the manual, `/man`, as you
  use it.
- [Configuration](../reference/configuration.md): the settings,
  exactly.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
