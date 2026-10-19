---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: e8da86fa5bf0c4a4
inputs:
  - CLAUDE.md#Persistence (git)
  - templates/gitattributes
  - projects/forge/10-intent.md#POS.0550
  - projects/forge/10-intent.md#POS.0830
  - projects/forge/10-intent.md#POS.0950
  - projects/forge/10-intent.md#POS.1100
  - projects/forge/10-intent.md#POS.1200
  - projects/forge/10-intent.md#POS.1490
  - projects/forge/10-intent.md#POS.1710
  - projects/forge/40-solution-design.md#SOL.0730
  - projects/forge/10-intent.md#REJ.0160
  - projects/forge/10-intent.md#REJ.0170
---

# Persistence in git

Persistence in git is the way the forge keeps the engine and every
project in git repositories, and the rules by which Claude reaches
them. This page explains why the scripts are the only door to git,
why saving and releasing are two separate commands, and how files
made for a reader behave at a merge. It is written for anyone who
uses the forge, extends it or weighs it up.

## What it is

The engine is one git repository with a remote.
Every project under `projects/` is a git repository of its own.
The scripts recognise a project as a repository by its `.git`
directory.
A project that is not under git is a legitimate shape, not a defect.

`main` is the released line.
Branches are voluntary and left to git.
Merging is git's, by hand or by merge request.

The forge touches git only through the scripts in `scripts/`.
This holds for reading state as well as for changing it, with no
exceptions.
The scripts carry no URL and no identity.
What each script does is said in its own help header; the page
[Scripts](../reference/scripts.md) lists them.

## How it works

### The scripts are the only door

For Claude the rule is a wall of the harness, not conduct alone.
The harness is the program Claude runs in, here Claude Code.
Deny rules in `.claude/settings.json` stop Claude from calling git
in any other way.
The rule binds the forge, not the principal (the person whose
thinking is being forged; see the
[Glossary](../reference/glossary.md)).
The principal's own git from the shell is his, and a save made
directly from the shell is unaffected.
How many scripts there are is not a rule: it is whatever the door
needs.

### Two doors, two speeds

Two commands take work out to the remote.

- `/save`: runs the `light` check, then commits and pushes on
  whatever branch is checked out, with no render; it takes seconds.
  `/save --quick` leaves the check out and nothing else.
- `/release`: runs on `main` only and refuses on any other branch,
  naming it; it runs its checks, makes the README and the release
  notes again, and saves with the release message and, at an
  approved major version, the tag `v<major>`.

Which checks each command runs is said in its own definition.
Only the major's tag has a fixed name.
Any other tag is the principal's request, with a free name, on a
branch as well.
The pages [Save your work](../use/save-your-work.md) and
[Release a version](../use/release-a-version.md) show how each is
used.

### The door inward

`/pull` is the door inward.
It looks at the remote and says the state of a repository against
its origin as a fact: up to date, behind, ahead, diverged or no
origin.
It pulls only a repository that is clean and behind.
Every other state gets an offer, not an action:

- behind with unsaved work: `/save` first;
- ahead: `/save`;
- diverged: the principal merges through git, or lets `/save`
  rebase his own linear commits onto the remote.

The forge never pulls or merges on its own judgement.
The page [Pull from the remote](../use/pull-from-the-remote.md)
shows the command in use, and
[Work on a branch](../use/work-on-a-branch.md) shows branches.

### Files made for a reader

Some files are made for a reader and are made again from their
sources:

- the renders;
- the README, the release notes and `CONTRIBUTING.md`;
- the documentation in `docs/`;
- the Markdown companions of the published files.

These are made only on `main`.
At a merge, git takes the local side of each of them (`merge=ours`),
and the file is made again afterwards.
A published file (`.pptx`, `.docx`) is marked `binary` and is never
merged.
The template `templates/gitattributes` says which paths take which
way, and `/new-project` copies it into a project's `.gitattributes`.

A release, a documentation run and a publish refuse a repository
that is behind its origin or diverged from it.
The reason is the rebase that `/save` does.
In a rebase the two sides of a merge swap, so `merge=ours` keeps the
other side.
A fresh README would then silently lose to an older one, and a
major's tag would mark the wrong state.

### The registration on the machine

Neither way of merging is built into git.
`/setup` registers them, and the git settings they need, once per
machine and on the principal's word, in the global git
configuration.
`forge-status` says when the registration is missing.
This matters because an unregistered clone silently falls back to a
conflict.

### Identity, immutability, migration

The commit identity is git's, not the forge's.
It is resolved per host by the user's own git configuration, and
the forge sets none.
`/setup` offers that configuration and one global guard
(`user.useConfigOnly = true`, with no global name or e-mail).
With the guard, a commit in a repository whose host has no identity
fails aloud instead of silently taking a default.

Immutability of documents (reviews, challenges, sources, research)
is a process rule, not a git mechanism.

A release that changes the shape of files comes with a migration:
`/migrate [slug]`, through `scripts/forge-migrate.py`.
It runs once per project, on one clone, on the principal's word and
never on Claude's.
Until a project is migrated, nothing writes into it: the state map,
the checks and every writing command say what `templates/project.md`
says and stop.

### The scripts beyond Windows

The scripts are Python 3.8 or newer, run as
`python scripts/<name>.py`.
`python` on PATH is their one prerequisite.
A system that has only `python3` gives it that name.
`scripts/` is the only platform-bound layer, and its scripts are
written to run unchanged on Linux and macOS.
Paths are composed with `pathlib`, and external tools are found on
PATH.
This is a writing rule, not a verified claim: portability counts as
verified only once the set has been run on Linux.

## Why

**One door.**
The reason the scripts are the only door to git is not recorded.
What is recorded is the kind of enforcement: a wall of the harness,
not a rule Claude is merely asked to keep.

**Two commands.**
Making the renders at every save cost minutes and tokens beyond
reason.
With the renders made only at the release, the README on `main` is
current at every release.
Between releases it is stale visibly, in the state map, never
silently.

Two other shapes were rejected:

- Stale-only rendering at the save (one command that remade only
  the renders whose inputs had moved): it would save perhaps a third
  of the engine's saves and nothing on projects, whose README input
  moves at every operation. It would also add a staleness state that
  several commands must all read alike. Two commands save all of
  that and add nothing.
- A fixed working branch with a switch that merges into `main` at
  the release: it would be a first step towards wrapping git, with
  merge and conflict logic in the forge's hands. It would make a
  non-developer understand two branches, and it would force a branch
  on those who need none. The switching half survives as the
  voluntary branch script; the merging half stays git's.

**Looking, not pulling.**
The principal may work on more than one machine.
A clone behind its origin is then the normal case, and a state map
drawn from it shows the wrong state.
A pull or a merge made on Claude's judgement would be work done
without the principal's word.
The state against the origin is the last word of the state map.
This is because that map runs over several screens and the state is
its key message.

**Files for a reader taken as ours.**
These files are made again from their sources after a merge, so
keeping one side loses nothing.
Why they are made only on `main`, beyond that, is not recorded.
The refusals of a release, a documentation run and a publish follow
from the rebase described above.

**Attributes in the repository, registration on the machine.**
The ways of merging are written per project as attributes, rather
than in a global configuration alone.
This is because the attributes travel with the repository and the
registration does not.

**Identity left to git.**
An identity kept by the forge duplicated what the user's own
configuration already resolved, and every repository carried the
same identity twice.
The engine carries no instance facts, and the git identities live
outside it.

**Immutability by convention.**
Git protects nothing from a commit that rewrites a file.
The rule costs nothing.
A mechanism would be one more layer to maintain and would still not
stop an edit by hand.

**Python.**
`python` is the same Python the document conversion already needed.

**Migration.**
The reason a migration runs once, on one clone, is not recorded.

## A worked example

A principal keeps a project `my-project` on two machines.
On the second machine the state map ends with "behind" and offers
`/pull`.
The repository is clean, so `/pull` fast-forwards it.
Had the principal skipped the pull and asked for `/release`, the
release would have refused, because the repository is behind.
A rebase in the following save would otherwise have let the older
README from the remote win over the fresh one.
After the pull he works on `main`, runs `/save`, then `/release`,
and the release goes through: its checks, a new README and new
release notes, the release message and, at an approved major, the
tag.

## See also

- [Save your work](../use/save-your-work.md): the save.
- [Release a version](../use/release-a-version.md): the release.
- [Pull from the remote](../use/pull-from-the-remote.md): the pull.
- [Work on a branch](../use/work-on-a-branch.md): branches.
- [The ledger, made from the records](the-ledger.md): why the ledger
  is made at read time and kept out of git.
- [Scripts](../reference/scripts.md): the scripts themselves.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
