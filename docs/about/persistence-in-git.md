---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: ed0da1f880615518
inputs:
  - CLAUDE.md#Persistence (git)
  - .claude/settings.json
  - scripts/hook-git.py
  - projects/forge/10-intent.md#POS.0550
  - projects/forge/10-intent.md#POS.0830
  - projects/forge/10-intent.md#POS.0950
  - projects/forge/10-intent.md#POS.1100
  - projects/forge/10-intent.md#POS.1200
  - projects/forge/10-intent.md#POS.1490
  - projects/forge/10-intent.md#POS.1710
  - projects/forge/40-solution-design.md#SOL.0520
  - projects/forge/40-solution-design.md#SOL.0740
  - projects/forge/10-intent.md#REJ.0160
  - projects/forge/10-intent.md#REJ.0170
---

# Persistence in git

Persistence in git is the way the forge keeps the engine and every
project in git: Claude writes to git only through the forge's
scripts, and reads git freely. This page explains how that line is
held, why saving and releasing are two commands of two speeds, and
why the forge looks at the remote but never merges on its own. It is
for anyone who uses the forge, extends it or weighs it up.

## What it is

The engine is one git repository with a remote.
Every project under `projects/` is a git repository of its own, where
its owner wants one.
A project with no repository of its own is a project outside git.
The forge writes its files to disk and runs no git on it.
Being "not under git" is a property of a project, not a defect.

The rule at the centre is one sentence: the scripts in `scripts/` are
the door to a write of git, and reading git directly is open.
"Claude" here is the model working with the principal (the person
whose thinking is forged, with final authority over all content).
Nothing of Claude's own commits, pushes, pulls, merges, rebases,
creates a branch or a tag, or touches a remote or a configuration
except through a script.
The one exception is the few commands that finish settling a
conflict, which run only on the principal's yes.
How many scripts there are is not a rule: there are as many as the
door needs.
The scripts themselves are listed on [Scripts](../reference/scripts.md).

## How it works

### The wall between reading and writing

Claude runs in a harness (the program Claude runs in, which carries
out its tools and asks for permissions).
The harness runs a hook before every shell command Claude sends.
A hook is a small program the harness calls at a fixed moment.
This one is `scripts/hook-git.py`, configured in
`.claude/settings.json`.

The hook reads the whole command and finds every call of git in it.
It answers in one of three ways:

- allow: a command that only reads git;
- ask: one of the few commands that finish the step of a conflict;
  the harness puts the command to the principal and runs it on his
  yes;
- deny: everything else; the answer names the script to use instead
  where one exists.

A part of a command that is not git is left to the harness.
Over a whole command, a deny outranks an ask and an ask outranks an
allow.
What the hook cannot read, it denies.

Claude has two shell tools.
The hook watches the one through which Claude runs git.
The other shell tool is closed to git whole by a deny rule in
`.claude/settings.json`.
So there is one parser and one door.

The rule binds the forge, not the principal.
His own git from his own shell is his.

### The commit

A commit carries the message the principal confirmed, word for word.
The settings of the harness turn off every attribution line, so no
co-author or session line is added or proposed.
The commit identity is git's, not the forge's.
Git resolves it per host from the user's own git configuration, which
`/setup` offers to write.
The recommended guard is a global setting that makes git refuse a
commit where no identity is configured, with no global name or e-mail
beside it.
The scripts carry no URL and no identity.

### Two doors, two speeds

Saving and releasing are two commands.

- `/save`: runs the light check (the quick check of the forge's
  bookkeeping), then commits and pushes on whatever branch is checked
  out; it makes no render and takes seconds. `/save --quick` leaves
  the check out.
- `/release`: runs on `main` only and refuses elsewhere; it runs its
  checks, re-renders the README and the release notes, then saves
  with the release message and, at an approved major version, the tag
  `v<major>`.

Any other tag is the principal's request, with a free name.
How each is used is on [Save your work](../use/save-your-work.md) and
[Release a version](../use/release-a-version.md).

### The door inward

`/pull` is the door inward.
It looks at the remote and says the state of each repository as a
fact: up to date, behind, ahead, diverged, or no origin.
It pulls only a repository that is clean and behind.
For every other state it offers the next step and runs nothing
unasked.
The forge never pulls or merges on its own judgement.
How a pull runs is on [Pull from the remote](../use/pull-from-the-remote.md).

### Branches and merging

`main` is the released line.
Branches are voluntary.
A script creates a branch or switches to one, and nothing forces a
branch on anyone (see [Work on a branch](../use/work-on-a-branch.md)).
Merging is git's, by the principal's hand or by a merge request.

### When a save meets a conflict

The one rebase the forge does is `/save`'s, which puts the
principal's own commits on top of the remote.
A rebase that conflicts is left standing, not aborted: the commit is
made and nothing is lost.
The conflict is then settled in the step of a conflict.
Claude lays both sides out in a walkthrough (one conflict per
message, each closed with the principal's verdict).
The principal decides, and Claude writes the chosen wording into the
file.
The finishing commands of git then run on the hook's ask.
A save that finds a rebase or a merge still standing refuses before
it stages anything.
So conflict markers are never committed.
The step itself is on [Settle a conflict](../use/settle-a-conflict.md).

### Ways of merging

Every file of a project has a way of merging that the forge tells
git; the three ways, and what the forge promises two people on one
project, are on
[Working together on one project](../about/working-together.md).
The files made for a reader (the renders, the README, the release
notes, the documentation, the published files) are made only on
`main` and taken as `ours` at a merge, that is, the local side wins.
A release, a documentation run and a publish therefore refuse a
repository that is behind or diverged from its origin, and offer
`/pull`.

`ours` is a merge driver that is not built into git.
`/setup` registers it once per machine, on the user's word, in the
global git configuration, with the git settings it needs.
The status script says when the registration is missing.

### What is not in git

The ledger (the table of a project's state, made from its documents)
is not in git at all.
It is made at read time; why is on
[The ledger, made from the records](../about/the-ledger.md).

Immutability of documents is a process rule, not a git mechanism.

### Where the scripts run

The scripts are Python 3.8 or newer, run as
`python scripts/<name>.py`.
`python` on PATH is their one prerequisite.
A system that has only `python3` gives it that name.
`scripts/` is the only layer bound to a platform.
It is written to run unchanged on Linux and macOS.
The git scripts and some others have been run on Linux.
For the conversions and the hooks, running on Linux is a writing
rule, not a verified claim, until a run there says otherwise.

## Why

**Why reading is open.**
Reading changes nothing.
To serve reading as well, the scripts would have had to copy git verb
by verb.

**Why writing goes through scripts.**
The reason Claude writes git only through scripts, rather than by
typing git, is not recorded as such.
What is recorded is the wish to stay clear of a wrapper of git:
merge and conflict logic in the forge's hands, and branches a
non-developer must understand.

**Why a hook and not deny rules.**
A deny rule of the harness matches the text usually typed, not the
command.
So a write spelled a little differently passes it.
A deny rule cannot be narrowed by an allow rule.
A hook does not override it either.
Two walls with one hole read worse than one.
The cost of the hook is that its reading of the shell is a heuristic.
That is why what it cannot read, it denies.
An ask holds even in the harness's automatic permission mode, and a
deny holds in every mode.

**Why the other shell tool is closed to git whole.**
So that there is one parser and one door.

**Why no attribution line.**
The commit message is the one the principal confirmed.
Any further reason is not recorded.

**Why two commands.**
The renders cost minutes and tokens beyond reason at every save.
With the renders made only at a release, the README on `main` is
current at every release.
Between releases it is stale visibly, never silently.
One command that re-rendered only what had moved was rejected.
It would have spared a share of the engine's saves and nothing on
projects, whose README input moves at every operation.
It would also have added a staleness state that several commands must
all read alike.

**Why branches are voluntary.**
A fixed working branch that the forge merged into `main` was
rejected.
It was the first step towards a wrapper of git: merge and conflict
logic in the forge's hands, and two branches a non-developer must
understand.
It would also have forced a branch on those who do not need one.
The switching half survives as the voluntary branch script.
The merging half stays git's.

**Why the forge looks but never pulls on its own.**
A principal who works on more than one machine has a clone behind its
origin as the normal case.
A state map drawn from such a clone is a map of the wrong state.
A pull or a merge made on Claude's judgement would be work done
without the principal's word.

**Why a conflicting rebase is left standing.**
The commit is already made, so nothing is lost.
The conflict is settled by a person, as the forge's help, not its
mechanism.

**Why files for a reader refuse a repository behind or diverged.**
The rebase of a save turns `ours` round.
A fresh README would then silently lose to an older one.
A major's tag would mark a wrong state.

**Why the registration of `ours` is reported.**
An unregistered clone silently falls back to a conflict on those
files.
The registration is made once per machine rather than per repository.
That way a migration of a repository never has to touch it.

**Why the identity is git's.**
An identity kept by the forge duplicated what the user's own
configuration already resolved.
The guard exists so that a commit on a host with no identity fails
aloud instead of silently taking a default.
One host serving two identities is accepted as a risk the user
resolves by hand.

**Why immutability is a process rule.**
Git protects nothing from a commit that rewrites a file.
The rule costs nothing.
A mechanism would be one more layer to maintain, and it still would
not stop a hand edit.

**Why Python.**
It is the same Python the document conversion already needed.

## A worked example

The principal works on a project with the placeholder slug
`my-project`, on `main`, and asks for a save.

1. Claude reads the project's state and recent history through git
   directly. The hook allows it, because it only reads.
2. Claude runs `/save my-project`. The light check runs, and the
   principal confirms the commit message.
3. The save script commits and puts the commit on top of the remote,
   which another clone has moved on. Two edits to the same sentence
   conflict. The script leaves the rebase standing and prints the
   files in conflict.
4. Claude lays the two sides out in a walkthrough. The principal
   picks one wording, and Claude writes it into the file.
5. Claude asks to stage the file and continue the rebase. The hook
   answers ask, the harness puts each command to the principal, and
   they run on his yes.
6. Claude runs `/save my-project` again, and the clean repository is
   pushed.

Had Claude tried to commit with git directly at step 2, the hook
would have denied it and named the save script.

## See also

- [Save your work](../use/save-your-work.md): the save.
- [Release a version](../use/release-a-version.md): the release.
- [Pull from the remote](../use/pull-from-the-remote.md): the pull.
- [Work on a branch](../use/work-on-a-branch.md): branches.
- [Settle a conflict](../use/settle-a-conflict.md): the step of a
  conflict, the one place Claude's git asks the principal.
- [Working together on one project](../about/working-together.md):
  the three ways of merging and what the forge promises two people on
  one project.
- [The ledger, made from the records](../about/the-ledger.md): why
  the ledger is made at read time and kept out of git.
- [Scripts](../reference/scripts.md): the scripts themselves.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
