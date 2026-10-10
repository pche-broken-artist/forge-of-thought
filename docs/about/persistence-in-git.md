---
generated: 2026-10-10
made: derived
inputs-hash: 8f993b9b44dff877
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About persistence in git

This page explains how the forge keeps its work in git and why it
keeps it that way: for the user who saves and releases, for the
extender who touches the scripts, and for the evaluator who wants to
know where the forge stops and git begins. It was put together from
the Persistence section of `CLAUDE.md`, Portability among it, and
from the positions and rejected directions of the forge's own intent
in `projects/forge/10-intent.md` that give the reasons.

## What is in git

The engine is one git repository with a remote. `main` is the
released line. Every project under `projects/` is a repository of
its own, which the engine ignores (the forge's own project
excepted) and the scripts recognise by the `.git` directory inside
the project. Creating a project's repository and giving it a remote
is the user's one-off act at creation; the forge never does it. A
project that is not under git is a property of that project, not a
defect: a sensitive project may be kept local, with or without a
remote.

The forge carries no remote address and no identity anywhere: git
holds that information itself.

## One door: the scripts

The scripts in `scripts/` are the only door to git, reading state
included, with no exception. For Claude this is a wall of the
harness, not a rule of conduct alone: the deny rules of
`.claude/settings.json` enforce it. The rule binds the forge, not
the principal: his own git from the shell is his, and saves made
directly from the shell are unaffected by anything below.

The scripts that serve the engine and every project repository, each
described in full by its own help header:

- `forge-save.py` commits and pushes.
- `forge-pull.py` fast-forwards from the remotes; on the engine this
  is the upgrade channel.
- `forge-status.py` reports state without changing anything.
- `forge-clone.py` brings an existing project in; `/import-project`
  is its door.
- `forge-branch.py` switches to a branch or creates it.

How many scripts there are is not a rule: it is whatever the door
needs. What they share lives in a module beside them, never twice.

## Two doors, two speeds

Saving and releasing are two commands, because they cost different
things.

`/save` runs the light check and then commits and pushes on whatever
branch is checked out. No render is made. It takes seconds.

`/release` runs from `main` only and refuses elsewhere, naming the
branch. It runs its checks, re-renders the README and the release
notes, and then saves with the release message; an approved major
receives the tag `v<major>`. Which checks each command runs is said
in its own definition (`.claude/skills/save/SKILL.md`,
`.claude/skills/release/SKILL.md`).

Why two: the renders cost minutes and tokens beyond reason at every
save, and a two-speed save had existed in practice for weeks before
it was made explicit. With the renders at the release only, the
README on `main` is current at every release and stale in between
visibly, never silently.

Only the major's tag has a fixed name, so that the checks and the
release notes can rely on it: an integer is a released major,
anything else a snapshot. Any other tag is the principal's request,
with a free name, on a branch as well.

A middle way was considered and rejected: a save that regenerates
only the renders whose inputs moved. It would have saved perhaps a
third of the engine's saves and nothing on projects, whose README
input moves at every operation, and it would have added a staleness
state that several commands must all read alike. The two-command
shape saves everything and adds nothing.

## Branches are git's

Branches are voluntary and belong to git. Whoever wants one gets it
through the one forge script that creates or switches a branch and
never types git; `forge-status.py` reports the current branch.
Nothing forces a branch: whoever does not use them works on `main`,
saves, now and then releases, and sees none of this.

Merging, rebasing and conflicts stay git's, by hand or by merge
request. The forge's only knowledge of a merge is that a release
runs on `main` after it and its checks find what two branches broke.
One hole is known and left until it happens: two parallel branches
taking the same next free ID.

The reason is a boundary the principal set: he does not want a
wrapper of git. The script does creation and switching, which only
change where the next commit lands, and nothing that rewrites
history. A fixed working branch per repository, with the release
merging it into `main`, was rejected as the first step towards that
wrapper: merge and conflict logic in the forge's hands, two branches
a non-developer must understand, and a branch forced on those who
need none. The forge stays a single-user tool per instance; more
people means more instances and coordination by git.

## Identity is git's

The commit identity is git's business, not the forge's. It is
resolved per host by the user's own git configuration, outside the
engine, and the forge sets no identity anywhere. `/setup` offers to
write that configuration, on the user's word and never overwriting.

The recommended guard, also offered by `/setup`, is a global setting
that makes git use only an explicitly configured identity, with no
global name or address: a repository on a host with no identity
configured then fails aloud instead of taking a default, and a save
commits nothing until git resolves an identity for the repository.
The case of one host serving two identities is accepted as a risk
the user resolves by hand.

Why the forge keeps no identity: an identity kept by the forge
duplicated what the user's own configuration already resolved, every
repository carried the same identity twice, and the forge had gained
a file, a template and three steps for a case that had not occurred.

A commit carries no attribution trailer. The commit message is the
one the principal confirmed, word for word.

## Immutability is a process rule

Reviews, challenges, sources and research are never edited after
they are created or registered. That is a rule of the process,
enforced by convention, not a mechanism of git. The reason: git
protects nothing from a commit that rewrites a file, the rule costs
nothing, and a mechanism would be one more layer to maintain that
still would not stop a hand edit.

## Portability

The forge runs beyond Windows. `scripts/` is the only
platform-bound layer, and its scripts are written to run unchanged
on Linux and macOS: Python 3.8 or newer, run as
`python scripts/<name>.py`. `python` on PATH is the one prerequisite
of the scripts, the same Python the document conversion needed
already; a system that has only `python3` gives it that name.
Nothing in them is Windows-only: paths are composed with `pathlib`,
external tools (`git`, `markitdown`, `pandoc`, `claude`) are
resolved from PATH, and the usage examples in the scripts' help are
free of platform-specific paths and invocations.

Portability is verified by running the set on Linux. Until that has
been done it is a writing rule, not a verified claim.

## See also

- [Save your work](../use/save-your-work.md): the save.
- [Release a version](../use/release-a-version.md): the release.
- [Work on a branch](../use/work-on-a-branch.md): branches.
- [Scripts](../reference/scripts.md): the scripts themselves.
