---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 77ac616604ea4d23
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
project in git repositories: the scripts in `scripts/` are the one
door through which Claude writes to git, and two commands of two
speeds, the save and the release, use that door. This page explains
how the door is held, why reading git stays open, why there are two
doors of two speeds, and why the files made for a reader are made
only on `main`. It is for anyone who uses the forge, extends it or
weighs it.

## What it is

The engine is one git repository with a remote. Every project is a
repository of its own where its owner wants one.

- **`main`** is the released line.
- **Branches** are voluntary and belong to git (see
  [Work on a branch](../use/work-on-a-branch.md)).
- **Merging** is git's, done by hand or by a merge request.

The scripts in `scripts/` are the door to a write of git. Nothing
Claude does on its own commits, pushes, pulls, merges, rebases,
creates a branch or a tag, or touches a remote or a configuration
except through a script. Reading git directly is open to Claude.
The one exception to the door is the step of a conflict, described
below. The scripts themselves are listed in
[Scripts](../reference/scripts.md).

The rule binds the forge, not the principal (the person whose
thinking is forged). His own git from his own shell is his.

## How it works

### The hook that holds the door

The line between reading and writing is held for Claude by a hook of
the harness. The harness is the program Claude runs in; a hook is a
small program the harness starts before Claude's command runs. The
hook is `scripts/hook-git.py`, registered in `.claude/settings.json`
on the shell tool through which Claude runs git. It reads the whole
command, finds every call of git in it, and gives one of three
answers:

- **allow**: a command that only reads git.
- **ask**: the few commands that finish the step of a conflict. The
  harness puts the command to the principal and runs it on his yes.
  The ask holds in the automatic permission mode too.
- **deny**: everything else. The reason the hook gives names the
  rule and the script of the forge to use instead.

A command the hook cannot read and that names git is denied. Over a
whole command, a deny outranks an ask and an ask outranks an allow.
A part of a command that is not git is left to the harness.

The other shell tool is closed to git whole, by a deny rule in the
same settings file. So there is one parser and one door.

### The commit message

A commit carries the message the principal confirmed, word for word.
The settings file turns off the attribution line the harness would
otherwise add or propose, so no co-author or session line is
appended.

### Two doors, two speeds

- **`/save`** runs the light check and then commits and pushes, on
  whatever branch is checked out. It makes no render and takes
  seconds. With `--quick` it leaves the check out and nothing else.
  See [Save your work](../use/save-your-work.md).
- **`/release`** runs from `main` only and refuses on any other
  branch, naming it. It runs its checks with their walkthrough (one
  item put to the principal per message), regenerates the README and
  the release notes, and saves with the release message. At an
  approved major version it sets the tag `v<major>`. See
  [Release a version](../use/release-a-version.md).

Any other tag is the principal's request, with a free name, and may
be set by either door.

### The door inward

`/pull` is the door inward. The forge looks at the remote and says
the state of the repository against its origin as a fact: up to
date, behind, ahead, diverged, or no origin. Each state has one
offer:

- **behind and clean**: `/pull`, which fast-forwards.
- **behind with unsaved work**: `/save` first.
- **ahead**: `/save`.
- **diverged**: the principal merges by his own hand, or lets
  `/save` rebase his own linear commits onto the remote.

The forge pulls only a clean repository that is behind. It never
merges on its own. See [Pull from the remote](../use/pull-from-the-remote.md).

### The step of a conflict

A rebase that conflicts during `/save` is left standing, not
aborted. The commit is made and nothing is lost. The script prints
the files in conflict and the step that follows. Claude lays both
sides out in a walkthrough, the principal decides, and Claude writes
the chosen wording into the file. The commands that finish the step
(staging the file, continuing or aborting the rebase or the merge,
taking one side of a file) run on the hook's ask. Then `/save` runs
again. A save that finds a rebase or a merge already standing
refuses before it stages anything. So conflict markers are never
committed. The step is described in
[Settle a conflict](../use/settle-a-conflict.md).

### Ways of merging and the files made on `main`

Every file of a project has one of three ways of merging, and the
forge tells git which one; the three and what they promise two
people on one project are explained in
[Working together on one project](working-together.md).

The files made for a reader are the renders, the README, the release
notes, the documentation and the published files. They are made only
on `main`. At a merge they are taken as `ours` and made again.
Whatever makes such a file or migrates a project therefore runs on
`main` only:

- `/release`
- `/publish`
- `/document`
- `/migrate`

Each of them refuses a repository that is behind or diverged from
its origin, and offers `/pull`.

### The driver `ours`

`ours` is a merge driver that is not built into git. `/setup`
registers it in the global git configuration once per machine, on
the principal's word, with the git settings it needs. The
registration is written through `scripts/forge-config.py`. The
status script `scripts/forge-status.py` says when the registration
is missing.

### What git does not hold

- **The ledger** (the single record of a project's state) is not in
  git at all. It is made from the documents at read time; see
  [The ledger, made from the records](the-ledger.md).
- **The commit identity** is git's, resolved per host by the
  principal's own git configuration. The forge sets none. The
  recommended guard is a global setting that makes git use only the
  configured identity, with no global name or e-mail, offered by
  `/setup`.
- **Immutability** of documents is a process rule, not a git
  mechanism.

### Portability

The scripts are Python, run as `python scripts/<name>.py`. `python`
on PATH is their one prerequisite. A system that has only `python3`
gives it that name. The scripts are written to run unchanged on
Linux and macOS: paths are composed portably, external tools are
found on PATH, and the help carries no Windows-only paths.

- **Have run on Linux**: the git scripts, the ledger script and the
  documentation state script.
- **A writing rule until a run says otherwise**: the conversions and
  the two hooks.

## Why

**Why reading is open.** Reading changes nothing. A script for
reading would have had to copy git verb by verb to serve it.

**Why a hook and not deny rules.** A prefix deny rule of the harness
matches the text usually typed, not the command. A command written
in a slightly different form passes it. A deny rule cannot be carved
by an allow rule, and a hook does not override it. Two walls with
one hole read worse than one. The cost of the hook is that its
parser of the shell is a heuristic. Because of that, what it cannot
read, it denies.

**Why the other shell tool is closed whole.** So that there is one
parser and one door.

**Why the commit message has no attribution.** The commit message is
the one the principal confirmed, word for word.

**Why two doors.** The renders cost minutes and tokens beyond reason
at every save. With the renders made at the release only, the README
on `main` is current at every release. In between it is stale
visibly, shown on the state map, never silently. A save that
regenerated only the renders whose inputs had moved was weighed and
rejected. It would save little, because a project's README input
moves at every operation. It would also add a staleness state that
several commands must all read alike.

**Why branches are voluntary and merging is git's.** A fixed working
branch, with a forge switch that merges it into `main` at the
release, was weighed and rejected. It would be the first step towards
a wrapper of git the principal does not want. It would put merge and
conflict logic in the forge's hands. It would make a non-developer
understand two branches. It would force a branch on those who do not
need one. The switching half survives as a voluntary script; the
merging half stays git's.

**Why the forge looks at the remote but never pulls on its own.** The
principal works on more than one machine. A clone behind its origin
is the normal case, and a state map drawn from it is a map of the
wrong state. A pull or a merge made on Claude's judgement would be
work done without the principal's word.

**Why the files for a reader are made on `main` only, and why
behind or diverged is refused.** The rebase of a save turns `ours`
round. A fresh README would silently lose to an older one, and a
major's tag would mark a wrong state.

**Why `ours` is registered per machine.** An unregistered clone
silently falls back to a conflict on the derived files. One
registration per machine was chosen against one per repository,
which the migration must not touch.

**Why the identity is git's.** An identity kept by the forge would
duplicate what the principal's own configuration already resolves.
The guard exists so that a commit in a repository on a host with no
identity fails aloud instead of silently taking a default.

**Why immutability is a process rule.** Git protects nothing from a
commit that rewrites a file. The rule costs nothing. A mechanism
would be one more layer to maintain that still would not stop a hand
edit.

**Why Python.** It is the same Python the document conversion needed
already.

**Why the rule binds the forge and not the principal's shell.** The
reason is not recorded.

## A worked example

A principal works on a project `<slug>` on a branch and asks Claude
to commit.

1. Claude would reach for git directly. The hook denies the command
   and names the door: `python scripts/forge-save.py <slug>`, that
   is, `/save`.
2. Claude runs `/save`. The light check runs, the message is drafted
   from the records and confirmed by the principal, and the script
   commits and pushes on the branch.
3. The rebase onto the remote meets a conflict in one artefact. The
   save leaves it standing and prints the file. Claude lays both
   sides out, the principal chooses, Claude writes the wording.
   Claude then asks to stage the file and continue the rebase; the
   harness puts each command to the principal, and it runs on his
   yes. `/save` runs again and pushes.
4. The principal asks for a release. `/release` refuses on the
   branch and names it. Once the work is on `main` and the
   repository is neither behind nor diverged, `/release` runs its
   checks, regenerates the README and the release notes, and saves
   with the release message.

## See also

- [Save your work](../use/save-your-work.md): the save.
- [Release a version](../use/release-a-version.md): the release.
- [Pull from the remote](../use/pull-from-the-remote.md): the pull.
- [Work on a branch](../use/work-on-a-branch.md): branches.
- [Settle a conflict](../use/settle-a-conflict.md): the step of a
  conflict, the one place Claude's git asks the principal.
- [Working together on one project](working-together.md): the three
  ways of merging and what the forge promises two people on one
  project.
- [The ledger, made from the records](the-ledger.md): why the ledger
  is made at read time and kept out of git.
- [Scripts](../reference/scripts.md): the scripts themselves.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
