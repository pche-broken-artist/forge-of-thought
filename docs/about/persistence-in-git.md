---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: 95b006720fc3a09c
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
every project in git repositories, and the rules Claude follows when
it touches them. This page explains why the scripts are the only
door to a write of git, why there are two doors of different speed
for going outward and one door for coming in, and why some files
are made only on `main`. It is written for the user who works with
the forge, the extender who changes it and the evaluator who judges
it.

## What it is

The engine is one git repository with a remote. Every project under
`projects/` is a repository of its own. The scripts recognise a
project's repository by asking git whether the project's directory
is the top of a repository. A project whose directory is not the top
of its own repository is, for the forge, a project outside git. The
forge runs no git on it, whatever repository lies above it. A
project "not under git" is a property, not a defect.

`main` is the released line. Branches are voluntary and left to git.
Merging is git's, done by hand or by a merge request (see
[Work on a branch](../use/work-on-a-branch.md)).

Four rules shape everything else:

- The scripts in `scripts/` are the door to a write of git.
- Reading git directly is open to Claude.
- The commit identity is git's, never the forge's.
- Immutability of documents is a process rule, not a git mechanism.

The scripts themselves are described on [Scripts](../reference/scripts.md).
Every term used here has its one line in the
[Glossary](../reference/glossary.md).

## How it works

### One door for a write, an open door for a read

Nothing of Claude's own commits, pushes, pulls, merges, rebases,
creates branches or tags, or touches a remote or a configuration
except through a script. Reading git (its status, its log, a diff)
needs no script. How many scripts there are is whatever the door
needs. That number is not a rule.

The line between reading and writing is held by a hook of the
harness. The harness is the program Claude runs in, here Claude
Code. A hook is a small program the harness runs before a command of
Claude's is carried out. The forge's hook is `scripts/hook-git.py`,
registered in `.claude/settings.json` on the shell tool Claude uses
for git. It reads the whole command, finds every call of git in it,
and gives one of three answers:

- allow: a command that only reads.
- ask: one of the few commands that finish the step of a conflict.
  The harness puts the command to the principal (the person whose
  thinking is being forged) and runs it on his yes.
- deny: everything else, with the name of the script to use instead
  where one exists.

What the hook cannot read, it denies. A part of a command that is
not git is left to the harness.

The other shell tool is closed to git whole by a deny rule in the
same settings file. So there is one parser of commands and one door.

The rule binds the forge, not the principal. His own git from his
own shell is his, and saves made directly from the shell are
unaffected.

A commit carries the message the principal confirmed, word for
word. The settings switch off the attribution lines the harness
would otherwise add to a commit, so no such line is added or
proposed.

### The step of a conflict

When a save meets a conflict, the save leaves it standing and does
not abort it. The commit is made and nothing is lost. The script
prints the files in conflict and the step that follows. In the step
of a conflict Claude lays both sides out as a walkthrough (a list of
decisions worked one item per message), the principal decides, and
Claude writes the chosen wording into the file. The finishing
commands of git, such as `git add` and `git rebase --continue`, then
run on the hook's ask. After that comes `/save` again. A save that
finds a rebase or a merge already standing refuses before it stages
anything, so that conflict markers are never committed. The step
itself is described on [Settle a conflict](../use/settle-a-conflict.md).

### Two doors, two speeds outward

```
            /save   (seconds)                  any branch
 work  ──>  light check, commit, push    ──>  the remote

            /release   (minutes)               main only
 work  ──>  checks, README and release   ──>  the remote,
            notes, release message, tag        tagged at a major

            /pull   (inward)
 the remote ──>  look, say the state, pull only a clean
                 repository that is behind
```

- `/save` runs the light check, then commits and pushes on whatever
  branch is checked out. It makes no render. `/save --quick` leaves
  the check out and nothing else. See
  [Save your work](../use/save-your-work.md).
- `/release` runs on `main` only and refuses elsewhere, naming the
  branch. It runs its checks with their walkthrough, re-renders the
  README and the release notes, and saves with the release message.
  At an approved major it adds the tag `v<major>`. It has no quick
  way, because its checks are the condition of a release. See
  [Release a version](../use/release-a-version.md).

### One door inward

`/pull` looks at the remote and says the state of each repository as
a fact: up to date, behind, ahead, diverged, or no origin. It pulls
only a clean repository that is behind, and offers the rest. With
unsaved work it offers `/save` first. When the repository is
diverged, the user merges by his own hand or lets `/save` rebase his
own commits onto the remote. The forge never pulls or merges on its
own judgement. See [Pull from the remote](../use/pull-from-the-remote.md).

### Every file has a way of merging

Each file of a repository has a way of merging, set by its path.
The three ways and what the forge promises two people on one
project are explained on
[Working together on one project](working-together.md). The record
files merge as text, both tails kept.

The files made for a reader, such as the README, are made only on
`main` and taken as `ours` at a merge. In the rebase of a save,
`ours` turns round. A fresh README would then silently lose to an
older one, and a major's tag would mark a wrong state. So whatever
makes a derived file or migrates a project runs on `main` only:
`/release`, `/publish`, `/document` and `/migrate`. Each refuses a
repository that is behind or diverged from its origin, and offers
`/pull`.

`ours` is a merge driver that git does not have built in. `/setup`
registers it once per machine, on the user's word, in the user's
global git configuration, together with the git settings it needs.
The registration belongs to the machine, not to the project.
`forge-status` says when the registration is missing. An
unregistered clone silently falls back to a conflict.

### Identity and its guard

The commit identity is resolved per git host by the user's own git
configuration. The forge sets no identity anywhere, and the scripts
carry no URL and no identity. `/setup` offers the per-host
configuration and a recommended guard: git is told to use only a
configured identity, and no global name or e-mail is set. A
repository on a host with no configured identity then fails aloud
instead of taking a default.

### The scripts run beyond Windows

`scripts/` is the only platform-bound layer of the forge. The scripts
are Python 3.8 or newer, and `python` on PATH is their one
prerequisite. A system that has only `python3` gives it that name.
They are written to run unchanged on Linux and macOS. The git
scripts, the ledger script and the documentation state script have
run on Linux. The conversions and the two hooks are a writing rule
still, not a claim, until a run on Linux says otherwise.

## Why

- **Reading is open** because reading changes nothing, and the
  scripts would otherwise have had to copy git verb by verb to serve
  it.
- **Writing goes through scripts.** Why the door to a write is the
  scripts in the first place is not recorded beyond the rule itself.
  What is recorded is the boundary: a pull or a merge made on
  Claude's judgement would be work done without the principal's
  word.
- **A hook, not conduct alone and not deny rules.** A deny rule
  matches the text usually typed, not the command, so a write
  spelled another way passes it. A deny rule cannot be carved open
  by an allow rule and is not overridden by a hook. Two walls with
  one hole read worse than one. The cost is that the hook's reading
  of the shell is a heuristic, so what it cannot read it denies.
- **The other shell tool is closed whole** so that there is one
  parser and one door.
- **No attribution line**: the commit message is the one the
  principal confirmed. A further reason is not recorded.
- **Two doors.** The renders cost minutes and tokens beyond reason
  at every save. With the renders made at the release only, the
  README on `main` is current at every release and visibly stale in
  between, never silently. A single save that re-rendered only what
  moved was rejected: it would save little, nothing on projects, and
  would add a state of staleness that several commands must read
  alike.
- **No forge switch that merges.** A fixed working branch that the
  release merges into `main` was rejected. It would have been the
  first step towards a wrapper of git the principal does not want:
  merge and conflict logic in the forge's hands, and two branches a
  non-developer must understand, forced on those who need no branch.
  The voluntary branch command survives; the merging stays git's.
- **The forge looks before it pulls.** The principal works on more
  than one machine, so a clone behind its origin is the normal case,
  and a map drawn from it would be a map of the wrong state.
- **Derived files on `main` only**, because `ours` turns round in
  the rebase of a save, as described above.
- **The registration is reported**, because an unregistered clone
  silently falls back to a conflict on the derived files.
- **The identity is git's**, because an identity kept by the forge
  duplicated what the user's own configuration already resolved.
  The guard makes a missing identity fail aloud.
- **Immutability is a process rule.** Git protects nothing from a
  commit that rewrites a file. The rule costs nothing, and a
  mechanism would be one more layer to maintain that still would
  not stop a hand edit.

## A worked example

A user works on a project with the placeholder slug `my-project`, on
a branch of his own.

1. He runs `/save my-project`. The light check runs, then the commit
   and the push on his branch. No render is made.
2. Back on `main`, on a second machine, he runs `/release my-project`.
   The clone is behind its origin, so the release refuses and offers
   `/pull`.
3. He runs `/pull my-project`. The repository is clean and behind, so
   it is pulled.
4. He runs `/release my-project` again. The checks run with their
   walkthrough, the README and the release notes are re-rendered, and
   the release is saved with its message, and with its tag at an
   approved major.

At no point did Claude type a write of git itself: every write went
through a script.

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

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
