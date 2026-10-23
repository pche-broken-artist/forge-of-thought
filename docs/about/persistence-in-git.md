---
generated: 2026-10-23
version: 5.34
made: derived
inputs-hash: e84d747198659da5
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

Persistence in git is the way Forge of Thought keeps the engine and
every project in git repositories, and the rules that say how Claude
may touch them. This page explains why every write of git goes
through the scripts, why reading is open, and why there are two
doors out (a save and a release) and one door in (a pull). It is for
anyone who uses the forge, extends it or weighs it up.

## What it is

The engine is one git repository with a remote. `main` is the
released line. Branches are voluntary and left to git.

Every project under `projects/` is a repository of its own. A
project counts as one when git names the project's directory as the
top of its repository. Anything else is a project outside git, and
the forge runs no git on it, whatever repository lies above it. A
project "not under git" is a property, not a defect.

The principal (the person whose thinking is forged, with the final
word on everything) creates a project's repository and adds its
remote once, by hand, at creation. The scripts carry no URL and no
identity.

## How it works

### The door to a write

The scripts in `scripts/` are the door to a write of git. Nothing
Claude does on its own commits, pushes, pulls, merges, rebases,
branches, tags, or touches a remote or a configuration except
through a script. The scripts themselves are listed on
[Scripts](../reference/scripts.md).

Reading git directly is open to Claude.

### The hook that holds the line

The line between reading and writing is held by a hook of the
harness. The harness is the program Claude runs in. A hook is a
script the harness starts before a command runs, and it may let the
command through, refuse it or put it to the principal. The hook is
`scripts/hook-git.py`, registered in `.claude/settings.json` on the
shell tool through which Claude runs git.

The hook reads the whole command and finds every call of git in it.
It gives one of three answers:

- allow: a command that only reads git;
- ask: the few commands that finish the step of a conflict, which
  the harness puts to the principal and runs on his yes;
- deny: everything else, with the script to use instead named in
  the refusal.

Over a whole command, deny outranks ask and ask outranks allow. A
part the hook cannot read is denied.

The other shell tool is closed to git whole by a deny rule in the
same settings file. So there is one door and one reader of commands.

The rule binds the forge, not the principal. His own git from his
own shell is his.

### The commit

A commit carries the message the principal confirmed, word for
word. No attribution line is added or proposed: the settings file
turns the harness's commit attribution off.

### Two doors, two speeds

Two commands take work out to the remote:

- `/save`: runs the light check, then commits and pushes on
  whatever branch is checked out, with no render; `--quick` leaves
  the check out;
- `/release`: runs on `main` only and refuses elsewhere; it runs its
  checks, re-renders the README and the release notes, and saves
  with the release message and, at an approved major version, the
  tag `v<major>`.

Any other tag is the principal's request, with a free name. How to
run each is on [Save your work](../use/save-your-work.md) and
[Release a version](../use/release-a-version.md).

### The door inward

`/pull` is the door inward. Claude looks at the remote and says the
state as a fact: up to date, behind, ahead, diverged, or no origin.
Each state has one offer. It pulls only a clean repository that is
behind. The forge never pulls or merges on its own judgement. How to
run it is on [Pull from the remote](../use/pull-from-the-remote.md).

### Branches and merging

`main` is the released line. A branch is voluntary: one script
creates it or switches to it, and whoever does not want branches
works on `main` and sees none of this. Merging is git's, by the
principal's hand or by a merge request. How to work on one is on
[Work on a branch](../use/work-on-a-branch.md).

### A conflict

A conflict that a save meets is left standing, not aborted. The
commit is made and nothing is lost. It is settled in the step of a
conflict:

1. Claude reads both sides and lays them out in a walkthrough (one
   item per message, each closed with the principal's verdict).
2. The principal decides.
3. Claude writes the chosen wording into the file.
4. The finishing commands of git, such as `git add` and
   `git rebase --continue`, run on the hook's ask.
5. `/save` runs again.

A save that finds a rebase or a merge already standing refuses
before it stages anything. So conflict markers are never committed.
The step is on [Settle a conflict](../use/settle-a-conflict.md).

### How each file merges

Every file of a project has a way of merging, and the forge tells
git which one. The ways and what the forge promises two people on
one project are on
[Working together on one project](../about/working-together.md).

The files made for a reader (the README, the release notes, the
documentation, a published file) are made only on `main`. At a
merge they are taken as `ours`, the side already in place. A
release, a documentation run and a publish therefore refuse a
repository that is behind its origin or diverged from it. The reason
is that the rebase a save does turns `ours` round. A fresh README
would then silently lose to an older one, and a major's tag would
mark a wrong state.

### The registration on each machine

`ours` is a merge driver that is not built into git. `/setup`
registers it once per machine, on the principal's word, in the
global git configuration, together with the git settings it needs.
The status script says when the registration is missing. The reason
is that an unregistered clone silently falls back to a conflict.

### The identity

The commit identity is git's, not the forge's. It is resolved per
host by the principal's own git configuration, and the forge sets
none. `/setup` offers that configuration and one global guard: no
global name or e-mail, and git told to use only what the
configuration gives. With the guard, a commit in a repository whose
host has no identity fails aloud instead of taking a default.

### Immutability

Some documents are never edited once written, such as sources and
reviews. That is a process rule, not a git mechanism.

### A migration

A release that changes the shape of files comes with a migration,
`/migrate`. It runs once per project, on one clone, on the
principal's word, never on Claude's. Until a project is migrated,
nothing writes into it.

### The scripts and the platforms

The scripts are Python 3.8 or newer, run as
`python scripts/<name>.py`. `python` on PATH is their one
prerequisite. A system that has only `python3` gives it that name.

`scripts/` is the only platform-bound layer. Its scripts are written
to run unchanged on Linux and macOS. The git scripts, the ledger
script and the documentation state script have run on Linux. For
the conversions and the two hooks this is a writing rule, not a
verified claim.

## Why

**Why reading is open.** Reading changes nothing. Serving reads
through the scripts would have meant copying git verb by verb.

**Why writes go through the scripts at all.** The reason is not
recorded.

**Why a hook and not deny rules.** Deny rules of the harness were
tried for the writing verbs and not kept, for three reasons:

- a prefix rule matches the text usually typed, not the command, so
  a write with an option in front of the verb passes it;
- a deny rule cannot be carved open by an allow rule and is not
  overridden by a hook, so it could not leave room for the asked
  commands;
- two walls with one hole read worse than one.

The cost of the hook is that its reading of the shell is a
heuristic. So what it cannot read, it denies.

**Why a wall of the harness and not conduct alone.** The reason is
not recorded beyond the rule itself.

**Why the permission system and not a sandbox.** A sandbox at the
level of the operating system was tried and dropped. It is not
available on Windows, where enforcing it meant no shell at all.

**Why two commands.** The renders cost minutes and tokens beyond
reason at every save. With the renders made at the release only, the
README on `main` is current at every release. In between it is stale
visibly, on the state map, never silently.

Two other shapes were rejected:

- one save that regenerates only the renders whose inputs moved:
  it saves perhaps a third of the engine's saves and nothing on
  projects, whose README input moves at every operation, and it adds
  a staleness state that several commands must all read alike;
- a fixed working branch that the release merges into `main`: it is
  the first step towards a wrapper of git that the principal does
  not want, puts merge and conflict logic in the forge's hands,
  gives a non-developer two branches to understand, and forces a
  branch on those who do not need one. Its switching half survives
  as the voluntary branch script; its merging half stays git's.

**Why the forge never pulls or merges on its own.** The principal
works on more than one machine, so a clone behind its origin is the
normal case. A map drawn from it is a map of the wrong state. A pull
or a merge made on Claude's judgement would be work done without the
principal's word.

**Why the identity is git's.** An identity kept by the forge
duplicated what the principal's own configuration already resolved.
Every repository carried the same identity twice. One host serving
two identities is accepted as a risk the principal resolves by hand.

**Why immutability is a process rule.** Git protects nothing from a
commit that rewrites a file. The rule costs nothing. A mechanism
would be one more layer to maintain and still would not stop an edit
by hand.

## A worked example

The principal works on `my-project` on two machines. On the second
machine he has saved work, and the remote has moved on from the
first machine.

1. He runs `/save my-project`. The light check runs, and the save
   commits his work.
2. The remote is ahead, so the save rebases his own commits onto it.
   One artefact conflicts. The save leaves the rebase standing and
   prints the file in conflict and the step that follows.
3. Claude lays out both sides of the conflict as a walkthrough. The
   principal picks the wording, and Claude writes it into the file.
4. Claude sends `git add` and then `git rebase --continue`. The
   harness puts each to the principal, and each runs on his yes.
5. He runs `/save my-project` again. The clean repository is pushed.
6. Later, on `main` and up to date with the remote, he runs
   `/release my-project`. Had the clone still been behind, the
   release would have refused.

## See also

- [Save your work](../use/save-your-work.md): the save.
- [Release a version](../use/release-a-version.md): the release.
- [Pull from the remote](../use/pull-from-the-remote.md): the pull.
- [Work on a branch](../use/work-on-a-branch.md): branches.
- [Settle a conflict](../use/settle-a-conflict.md): the step of a
  conflict, the one place Claude's git asks the principal.
- [Working together on one project](../about/working-together.md):
  the three ways of merging and what the forge promises two people
  on one project.
- [The ledger, made from the records](../about/the-ledger.md): why
  the ledger is made at read time and kept out of git.
- [Scripts](../reference/scripts.md): the scripts themselves.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-23 for version 5.34 from the files the
front-matter names; never edited by hand.
