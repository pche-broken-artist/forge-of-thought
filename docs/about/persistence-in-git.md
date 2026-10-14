---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: b2e33c5f07db70fb
inputs:
  - CLAUDE.md#Persistence (git)
  - projects/forge/10-intent.md#POS.0550
  - projects/forge/10-intent.md#POS.0830
  - projects/forge/10-intent.md#POS.0950
  - projects/forge/10-intent.md#POS.1100
  - projects/forge/10-intent.md#POS.1110
  - projects/forge/10-intent.md#POS.1200
  - projects/forge/10-intent.md#POS.1490
  - projects/forge/10-intent.md#REJ.0160
  - projects/forge/10-intent.md#REJ.0170
---

# Persistence in git

Persistence in git is how the forge keeps the engine and every
project: each is a git repository, and the forge reaches git only
through the scripts in `scripts/`. This page explains why the
scripts are the only door, why saving and releasing are two commands
of two speeds, and why the forge never pulls or merges on its own.
It is for the user who saves and releases, for the extender who
touches the scripts, and for the evaluator who wants the reasons.

## What it is

The engine is one git repository with a remote. `main` is the
released line. Branches are voluntary and left to git. Every project
under `projects/` is a repository of its own, which the engine does
not track (the forge's own project is the one exception). The scripts
recognise a project repository by the presence of its `.git`
directory.

Initialising a project's repository and adding its remote is the
principal's one-off act at creation. The principal is the person
whose thinking is forged; the term is explained in the
[Glossary](../reference/glossary.md). A project "not under git" is
a property, not a defect.

The scripts in `scripts/` are the only door to git. Reading state is
included: no exception. For Claude the door is a wall of the harness
(the environment that runs Claude and holds its permission rules):
the deny rules of `.claude/settings.json` enforce it. The rule binds
the forge, not the principal: the principal's own git from the shell
is his, and saves made directly from the shell are unaffected. How
many scripts there are is not a rule. Those that serve the engine and
every project repository are described on the
[Scripts](../reference/scripts.md) page and in each script's own
help header:

- `forge-save.py`: commits and pushes.
- `forge-pull.py`: fast-forwards from the remotes; on the engine
  this is the upgrade channel.
- `forge-status.py`: reports state without changing anything.
- `forge-clone.py`: brings an existing project in; `/import-project`
  is its door.
- `forge-branch.py`: switches to a branch or creates it; merging is
  git's, by hand or by merge request.

The scripts carry no URL and no identity. No remote is configured
anywhere in the forge: git carries that information itself.

**Two doors, two speeds.** `/save` and `/release` are two commands.
`/save` runs the light check and then commits and pushes on whatever
branch is checked out, with no render; it takes seconds. The job is
described on [Save your work](../use/save-your-work.md). `/release`
runs from `main` only and refuses elsewhere, naming the branch. It
runs its checks, settles their findings with the principal in a
walkthrough (the forge's way of working a list of items one at a
time, each closed with a verdict), re-renders the README and the
release notes, and then saves with the release message and, at an
approved major, the tag `v<major>`. The job is described on
[Release a version](../use/release-a-version.md). Which checks each
command runs is defined in its own skill. Any other tag is the
principal's request, with a free name, on a branch as well.

**The door inward.** `/pull` looks at the remote and says the state
as a fact: up to date, behind, ahead, diverged, or no origin. It
pulls only a clean repository that is behind and offers the rest.
The forge never pulls or merges on its own judgement. The job is
described on [Pull from the remote](../use/pull-from-the-remote.md).

**Identity.** The commit identity is git's, not the forge's. It is
resolved per host by the principal's own git configuration, through
`includeIf` stanzas, and the forge sets no identity anywhere. The
recommended guard is the git setting `user.useConfigOnly = true`
with no global name and no global e-mail. `/setup` offers to write
both the configuration and the guard.

**Immutability.** The immutability of reviews, challenges, sources
and research is a process rule, not a git mechanism.

**Portability.** The scripts are Python, 3.8 or newer, run as
`python scripts/<name>.py`. `python` on PATH is their one
prerequisite. A system that has only `python3` gives it that name.
`scripts/` is the only platform-bound layer of the forge and is
written to run unchanged on Linux and macOS: paths are composed with
`pathlib`, external tools are resolved from PATH, and the usage
examples in the scripts' help are free of platform-specific paths.
This is a writing rule, not a verified claim: it is verified by
running the set on Linux, and until then it stays a rule. Each
script carries its help in its module docstring. What several
scripts share lives in a module beside them, never twice.

## How it works

A day's work goes through `/save`. Whatever branch is checked out,
`/save` runs the light check, commits and pushes. The commit message
is the one the principal confirmed, word for word: Claude adds no
trailer and no attribution of its own. The one rebase the forge does
is `/save`'s, the principal's own commits onto the remote.

A finished version goes through `/release`. On `main`, the checks
run, their findings are settled, the README and the release notes
are regenerated, and the release commit lands with the release
message. The release number is the intent's version. At an approved
major, the tag `v<major>` is added. Only the major's tag has a fixed
name: an integer is a released major, anything else a snapshot.

Work on another clone goes through `/pull`. The `/forge` map and
`/pull` ask `forge-status --remote` for the state of the engine and
of the project against its origin. Each state has one offer:

- behind and clean: `/pull`.
- behind with unsaved work: `/save` first.
- ahead: `/save`.
- diverged: the principal merges by hand or lets `/save` rebase his
  commits onto the remote; nothing is pulled until he has.

The principal knows and decides; the forge runs none of it unasked.

Branches are there for whoever wants one, through one command:
`forge-branch <name>` creates the branch or switches to it, and
`forge-branch main` switches back. `forge-status` reports the
current branch. The script does creation and switching, which only
change where the next commit lands, and nothing that rewrites
history. Merge and conflicts stay git's. Nothing forces a branch:
whoever does not use them works on `main`, saves and now and then
releases, and sees none of this. The forge's only knowledge of a
merge is that `/release` runs on `main` after it, and its checks
find what two branches broke. How branches are used is described on
[Work on a branch](../use/work-on-a-branch.md).

The commit identity is resolved by git from the principal's own
configuration, per host. With the guard in place, a commit in a
repository on a host with no identity fails aloud instead of
silently taking a default, and a save commits nothing until git
resolves an identity for the repository.

Upgrading the engine is `forge-pull` on the engine: a fast-forward of
`main`.

## Why

**Why the scripts are the only door.** The reason the scripts, and
nothing else, are the door to git is not recorded. What is recorded
is why the door is a wall of the harness and not conduct alone: a
rule that must hold is enforced, not trusted to Claude's behaviour.
The rule binds the forge and not the principal because his own git
from the shell is his.

**Why two doors.** The renders cost minutes and tokens beyond reason
at every save, and the two-speed save had existed in practice before
it was made a rule. With the renders at the release only, the README
on `main` is current at every release and stale in between visibly,
through the `/forge` map, never silently. Only the major's tag has a
fixed name so that `/check` and the release notes can rely on it.

Two other shapes were rejected. One was stale-only rendering at the
save: one command, with `/save` regenerating only a render whose
recipe or input moved in that save, and a skipped-render mark in the
ledger (the single source of truth for a project's state). It was
rejected because it would save perhaps a third of the engine's saves
and nothing on projects, whose README input, the ledger, moves at
every operation; and because it would add a staleness state that
`/save`, `/forge` and `/check` must all read alike. The two-command
shape saves everything and adds nothing. The other was a fixed
working branch with a forge switch that merges: a `work` branch per
repository and `/release` merging it into `main`. It was rejected as
the first step towards a wrapper of git the principal does not want,
with merge and conflict logic in the forge's hands and two branches
a non-developer must understand, while forcing a branch on those who
do not need one. The switching half survives as the voluntary
`forge-branch`; the merging half stays git's.

**Why branches are voluntary and merging is git's.** The boundary
is the wrapper of git the principal does not want. The script does
only what changes where the next commit lands and nothing that
rewrites history. The forge stays a single-user tool per instance;
more people means more instances and coordination by git. One hole
is known and left until it happens: two parallel branches taking the
same next free ID.

**Why the forge never pulls or merges on its own.** The principal
works on more than one machine, so a clone behind its origin is the
normal case, and a state map drawn from it is a map of the wrong
state. A pull or a merge made on Claude's judgement would be work
done without the principal's word.

**Why the commit identity is git's.** An identity kept by the forge
would duplicate what the principal's own configuration already
resolves, and every repository would carry the same identity twice.
The guard exists so that a repository on a host with no identity
fails aloud instead of taking a default. The case of one host
serving two identities is accepted as a risk the principal resolves
by hand. The scripts carry no URL and no identity because instance
facts are out of the scripts: git configuration is the principal's.

**Why immutability is a process rule.** Git protects nothing from a
commit that rewrites a file. The rule costs nothing. A mechanism
would be one more layer to maintain that still would not stop a hand
edit.

**Why Python, and why `python` on PATH.** `python` is the same
Python the document conversion needed already, so the scripts add no
prerequisite of their own. Why the scripts are written for Linux and
macOS and not verified there is not recorded beyond the statement
that verification is done by running the set on Linux.

## A worked example

The principal works on the project `my-project`, a repository of
its own with an origin.

In the morning he opens a branch for a larger reworking of the
intent: `forge-branch rework` creates it and switches to it. Through
the day he saves twice with `/save`. Each save runs the light check
and then commits and pushes on `rework`; nothing is rendered, and
each save takes seconds. The README of the project is now stale, and
the `/forge` map shows it as such.

When the reworking is done, he merges `rework` into `main` by hand,
which is git's business and not the forge's, and switches back with
`forge-branch main`. He runs `/release`. The checks run on `main`,
and their findings are settled one by one in a walkthrough. The
README and the release notes are regenerated. The release commit
lands with the message "release 2.0", and because 2.0 is an approved
major, the tag `v2` is added. The README on `main` is current again.

The next day he opens the same project in another clone. `/pull`
asks `forge-status --remote` and says the state as a fact: behind,
clean. It offers the pull and, on his word, fast-forwards. Had the
clone carried unsaved work, `/pull` would have offered `/save` first
and pulled nothing.

## See also

- [Save your work](../use/save-your-work.md): the save.
- [Release a version](../use/release-a-version.md): the release.
- [Pull from the remote](../use/pull-from-the-remote.md): the pull.
- [Work on a branch](../use/work-on-a-branch.md): branches.
- [Scripts](../reference/scripts.md): the scripts themselves.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
