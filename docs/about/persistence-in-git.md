---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 0bb1d9d781cf7d3a
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
  - projects/forge/10-intent.md#POS.1600
  - projects/forge/10-intent.md#POS.1710
  - projects/forge/10-intent.md#POS.1970
  - projects/forge/10-intent.md#POS.1980
  - projects/forge/40-solution-design.md#SOL.0520
  - projects/forge/40-solution-design.md#SOL.0740
  - projects/forge/10-intent.md#REJ.0160
  - projects/forge/10-intent.md#REJ.0170
---

# Persistence in git

Persistence in git is how the forge keeps the engine and every
project in a git repository of its own, and how Claude is kept to a
few scripts whenever it writes to git. This page explains why the
scripts in `scripts/` are the only door to a write of git, why
reading git is open, and why saving and releasing are two commands
of two speeds. It is for the user who wants to understand what the
forge does with his repositories, for the extender who touches the
scripts or the hook, and for the evaluator who asks what is enforced
and what is only a rule.

## What it is

The engine is one git repository with a remote. `main` is its
released line. Branches are voluntary and left to git. Every project
under `projects/` is a repository of its own, and the engine does
not track it. A project without a repository is a project outside
git. On such a project the forge runs no git at all, whatever
repository may lie above it. "Not under git" is a property of a
project, not a defect.

The scripts in `scripts/` are the door to a write of git. Nothing of
Claude's own commits, pushes, pulls, merges, rebases, branches, tags,
stashes or resets, and nothing of its own touches a remote or a
configuration, except through a script. Reading git directly is
open to Claude. The line between the two is held by a hook of the
harness (the program Claude runs in). The one exception to the door
is the small set of commands that finish the step of a conflict,
which the hook puts to the principal (the person whose thinking is
being forged) and which run on his yes. The rule binds the forge,
not the principal: his own git from his own shell is his.

Two doors lead outward. `/save` is the fast one, on any branch.
`/release` is the full one, from `main` only. `/pull` is the door
inward. Merging is git's own, done by the integrator on his own
clone outside the forge's scripts. The scripts carry no URL and no
identity. The ledger (the state of a project, made from its
documents at read time) is not in git at all.

## How it works

### The wall between reading and writing

The hook is `scripts/hook-git.py`, registered in
`.claude/settings.json` on the shell tool through which Claude runs
git. Before every command of that tool runs, the hook reads the
whole command, splits it at the shell's separators, and finds every
call of git in it. It answers in three ways:

- allow, for a command that only reads;
- ask, for the few commands that finish the step of a conflict, so
  that the harness puts the command to the principal and runs it on
  his yes;
- deny, for everything else, naming the script of the forge to use
  instead.

Over a whole command, deny outranks ask and ask outranks allow. A
part of the command that is not git is left to the harness. The
hook reads no file and writes nothing. The other shell tool is
closed to git whole by a deny rule of the same settings file. So
there is one parser and one door.

The commands that finish the step of a conflict are named one by
one: staging a file, continuing or aborting a rebase or a merge, a
plain merge of one branch, and taking one side of a file in
conflict. The step itself is the forge's help, not its mechanism:
Claude lays both sides out as a walkthrough (one item per message,
each closed with a verdict), the principal decides, Claude writes
the chosen wording, and the finishing commands run on the hook's
ask. The step is described in [Settle a
conflict](../use/settle-a-conflict.md).

A commit carries the message the principal confirmed, word for
word, and no attribution line: the settings file leaves the commit
attribution empty and the session link off, so the harness adds and
proposes no trailer.

### Two doors, two speeds

`/save` runs the light check, then commits and pushes on whatever
branch is checked out, through `forge-save`. It renders nothing.
`/save --quick` leaves the light check out and changes nothing else.
The message is drafted from the records and confirmed, or given
with `-m`. A conflict that `forge-save` meets in its rebase is left
standing, not aborted: the commit is made, nothing is lost, the
script prints the files in conflict and the step that follows. A
save that finds a rebase or a merge already standing refuses before
it stages anything, so that conflict markers are never committed.
The job is [Save your work](../use/save-your-work.md).

`/release` runs from `main` only and refuses elsewhere, naming the
branch. Its order is fixed: its checks, the documentation, the
README and release notes, the state render, the save. For the
engine the tests run first, and a red test stops the release; what
the tests are is [The tests](the-tests.md). The documentation is
offered, because the README reads the documentation's index. The
release commit carries the release message, and at an approved
major the tag `v<major>`. The save a release ends with runs without
a second light check, because the release ran it already. Any other
tag is the principal's request, with a free name, from `/save` or
`/release` alike. The job is [Release a
version](../use/release-a-version.md).

In the commands of git the word `forge` names the whole, the engine
and the forge's own project cloned beside it, each its own commit;
why that is so is [Projects and the
engine](projects-and-the-engine.md).

### The door inward

`/pull` looks at the remote and says the state as a fact: up to
date, behind, ahead, diverged, or no origin. Beside the state it
says what waits on GitHub outside git, the open pull requests and
the unanswered discussions, or that it could not read it. It pulls
only a clean repository that is behind. Every other state gets an
offer, and nothing runs unasked: behind with unsaved work, save
first; ahead, save; diverged, the user merges by his own hand or
lets `/save` rebase his own commits onto the remote. The forge
never pulls or merges on its own judgement. The job is [Pull from
the remote](../use/pull-from-the-remote.md).

### Branches and merging

Branches are voluntary. Whoever wants one gets it through
`forge-branch`, which creates the branch or switches to it; the job
is [Work on a branch](../use/work-on-a-branch.md). Merging is git's,
by hand or by merge request: the integrator merges on his own clone
with git itself, outside the forge's scripts, and what git leaves
standing is settled in the step of a conflict.

Every file of a repository has a way of merging, and the record
files merge as text with both tails kept; the three ways and what
the forge promises two people on one project are [Working together
on one project](working-together.md). The files made for a reader,
the README and the release notes among them, are made only on
`main` and taken as `ours` at a merge. Therefore whatever makes a
derived file or migrates a project, `/release`, `/publish`,
`/document` and `/migrate`, runs on `main` only, refuses a
repository behind or diverged from its origin, and offers `/pull`.

`ours` is a merge driver that git does not have built in. `/setup`
registers it once per machine, on the user's word, together with the
git settings it needs, through `scripts/forge-config.py`. The status
script, `forge-status`, says when the registration is missing. The
registration belongs to the machine, not to the project.

### What the forge leaves to git and to the user

Initialising a project's repository and adding its remote are the
user's one-off act at creation. The commit identity is git's: it is
resolved per host by the user's own configuration, and the forge
sets none. `/setup` offers to write that configuration and one
global guard, so that a commit on a host with no identity fails
aloud instead of taking a default. Immutability of documents is a
process rule, not a git mechanism. The ledger is made at read time
by a script and is gitignored; why is [The ledger, made from the
records](the-ledger.md).

### Portability

The scripts are Python 3.8 or newer, run as
`python scripts/<name>.py`. `python` on PATH is their one
prerequisite; a system that has only `python3` gives it that name.
They are written to run unchanged on Linux and macOS, with nothing
Windows-only: paths composed with `pathlib`, external tools resolved
from PATH, usage examples free of Windows-specific paths. The
engine's tests run in CI on Linux and Windows at every push, the git
scripts, the ledger, the light check and the hook's judgement among
them. The conversions are tested for their failure without the tool
alone. The per-prompt hook is a writing rule until a run says
otherwise. Nothing has run on macOS: for it the whole set is the
writing rule alone. The scripts themselves are listed in
[Scripts](../reference/scripts.md); the terms of the forge are in the
[Glossary](../reference/glossary.md).

## Why

**Why the scripts are the door, and why reading is open.** Reading
changes nothing. The scripts had to copy git verb by verb to serve
reading, so reading was opened to Claude directly. How many scripts
there are is whatever the door needs, never a rule.

**Why a hook and not deny rules.** A prefix deny rule of the harness
matches the text usually typed, not the command, so a write spelled
differently passes it. A deny rule cannot be carved by an allow
rule, and it is not overridden by a hook. Two walls with one hole
read worse than one. So the wall for the writing verbs is one hook
that reads the whole command, and the other shell tool is closed to
git whole, so that there is one parser and one door.

**Why a commit carries no attribution line.** The reason is not
recorded.

**Why two doors.** The renders cost minutes and tokens beyond reason
at every save, and the two-speed save had existed in practice for
weeks before it was named. With the renders at the release only,
the README on `main` is current at every release and stale in
between visibly, never silently. Two shapes were rejected. One was a
save that regenerates only the renders whose inputs moved: it saved
little on the engine and nothing on a project, and it added a
staleness state that every reader of state had to read alike. The
other was a fixed working branch with a forge switch that merges
into `main`: it was the first step towards a wrapper of git, with
merge and conflict logic in the forge's hands and two branches a
non-developer must understand, forced on those who do not need one.
The switching half survived as the voluntary `forge-branch`; the
merging half stayed git's.

**Why the release's save runs no second light check.** The release
ran it already. A save never runs the tests, because every push runs
them in CI; a release of the engine runs them first, because its
checks are the condition of a release.

**Why derived files are made on `main` only.** The derived files are
taken as `ours` at a merge. In the rebase of `/save` that `ours`
turns round: a fresh README would silently lose to an older one, and
a major's tag would mark a wrong state. So whatever makes a derived
file or migrates a project refuses a repository behind or diverged
and offers `/pull`.

**Why the registration is the machine's.** An unregistered clone
silently falls back to a conflict on the derived files, so the
status script says when the registration is missing. One
registration per machine was chosen against one per repository,
which the migration must not touch.

**Why the forge never pulls on its own.** The principal works on
more than one machine, so a clone behind its origin is the normal
case, and a state map drawn from it is a map of the wrong state. A
pull or a merge made on Claude's judgement would be work done
without the principal's word. What waits on GitHub is said beside
the state because a contribution seen on the morning it arrives
costs nothing, and the same contribution seen after a week of one's
own rounds costs renumbered items, re-dated versions and a conflict
at the merge.

**Why the ledger is out of git.** The ledger was the one file
present at every collision of two people or two windows on one
project, since every operation writes it. Made at read time, it
stops existing as a thing to merge.

**Why the identity is git's.** An identity kept by the forge
duplicated what the user's own configuration already resolved, and
every repository carried the same identity twice. The guard makes a
missing identity fail aloud instead of taking a default.

**Why immutability is a process rule.** Git protects nothing from a
commit that rewrites a file. The rule costs nothing. A mechanism
would be one more layer to maintain that still would not stop a
hand edit.

**Why Python.** The scripts are Python on the feedback of the
forge's users, and `python` on PATH was the same Python the document
conversion needed already. Portability is verified by a run where
one exists, and said to be a writing rule where none does.

## A worked example

A principal works in a project with the placeholder slug
`my-project`, on a branch of his own.

1. He asks Claude to commit the round's changes. Claude tries a
   commit through the shell directly. The hook denies it and names
   `python scripts/forge-save.py my-project -m "<message>"` as the
   door. Claude runs `/save my-project` instead: the light check
   runs, the message drafted from the records is confirmed, and the
   commit is pushed on the branch.
2. The next morning, on another machine, he asks for a release.
   `/release my-project` refuses: the repository is behind its
   origin, and a README made here would lose to the one on the
   remote at the next rebase. It offers `/pull`.
3. `/pull my-project` says the state as a fact, clean and behind,
   and fast-forwards. It also says that one pull request waits on
   GitHub, unanswered, and offers to look at it first.
4. He merges the branch into `main` on his own clone with git
   itself. One record file conflicts. Claude lays both sides out in
   a walkthrough, he decides, Claude writes the wording, and the
   finishing commands run on the hook's ask and his yes.
5. `/release my-project` from `main` runs its checks, offers the
   documentation, re-renders the README and release notes, and
   saves with the release message and no second light check.

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
- [Projects and the engine](projects-and-the-engine.md): why `forge`
  names the engine and the forge's own project beside it.
- [The tests](the-tests.md): the tests that make the portability rule
  a run.
- [Scripts](../reference/scripts.md): the scripts themselves.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
