---
generated: 2026-10-09
made: derived
inputs-hash: d70ca5ea7ff9f056
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About persistence in git

This page explains how the forge keeps its work in git: what is a
repository, which way into git is open to whom, why saving and
releasing are two commands of different speed, what the forge leaves
to git on purpose, and why the rule that some documents are never
edited is a rule of process and not a mechanism of git. It is written
for anyone who uses the forge, extends it or judges it, and it was put
together from `CLAUDE.md` (the section on persistence, portability
among it) and from the positions and rejected directions of the forge
intent in `projects/forge/10-intent.md`, which give the reasons.

## What is a repository

The engine is one git repository with a remote of its own. Its `main`
branch is the released line. Every project under `projects/` is a
repository of its own, with whatever remote and visibility its owner
gives it; the engine ignores them in git (the forge's own project
excepted) and recognises a project repository by the `.git` directory
inside the project's folder. The engine does not know the projects:
initialising a project's repository and giving it a remote is the
owner's one-off act when the project is created, and the forge's
scaffolding commands never touch git. A project "not under git" is a
property of that project, not a defect: a sensitive project kept
local is a legitimate shape, as is a repository with no remote, which
keeps the history that renders and recipes rely on while the first
shape does not.

No remote is configured anywhere in the forge, and the scripts carry
no URL. Git carries that information itself.

## One door to git

The scripts in `scripts/` are the only door to git, reading state
included, no exceptions. For Claude this is a wall of the harness and
not conduct alone: the deny rules of `.claude/settings.json` enforce
it, so that Claude cannot reach git except through a forge script.
How many scripts there are is not a rule; it is whatever the door
needs. Each script is described in full by its own help, which is
where the reader looks for what it does and what it needs.

The rule binds the forge, not the principal. His own git from the
shell is his: a save made directly from the shell is unaffected by
anything the forge does, and the forge takes no notice of it.

The scripts that serve the engine and every project repository alike:
one commits and pushes, one fast-forwards from the remotes (on the
engine that is the upgrade channel), one reports state without
changing anything, one brings an existing project in, and one
switches to a branch or creates it. Merging is not among them.

## Two doors, two speeds

Saving and releasing are two commands because they cost differently.

`/save` runs the light check, then commits and pushes on whatever
branch is checked out. It renders nothing. It takes seconds.

`/release` runs from `main` only and refuses elsewhere, naming the
branch it found. It runs its checks and settles their findings with
the principal, re-renders the README and the release notes from the
settled sources, and then saves with the release message, which
carries the intent's version. At an approved major it adds the tag
`v<major>`. Only the major's tag has a fixed name, so that the checks
and the release notes can rely on it: an integer is a released major,
anything else a snapshot. Any other tag is the principal's request,
with a free name, on a branch as well.

Why two: the renders cost minutes and tokens beyond reason at every
save, and a two-speed save had existed in practice for weeks before it
was written down. With the renders at the release only, the README on
`main` is current at every release and stale in between visibly, never
silently: the project's state map shows the staleness, and the
staleness of a render is never a finding of a check, because the
release regenerates the README and the release notes anyway.

One alternative was rejected: a single save that regenerates only the
renders whose recipe or input moved in that save. It would have saved
perhaps a third of the engine's saves and nothing on projects, whose
README input moves at every operation, and it would have added a
staleness state that three commands must all read alike. The
two-command shape saves everything and adds nothing.

## Branches are voluntary and belong to git

`main` is the released line. Branches are allowed and left to git:
whoever wants one gets it through one forge command, which creates
the branch or switches to it, and switches back to `main` the same
way; the status script reports the current branch. Nothing forces a
branch. Whoever does not use them works on `main`, saves, now and then
releases, and sees none of this.

Merging, rebasing and conflicts stay git's, by hand or by merge
request. The forge's only knowledge of a merge is that a release runs
on `main` after it and its checks find what two branches broke. One
hole is known and left until it happens: two parallel branches taking
the same next free ID. The forge stays a single-user tool per
instance; more people means more instances and coordination by git.

The reason for the boundary is that the principal does not want a
wrapper of git. The branch script does creation and switching, which
only change where the next commit lands, and nothing that rewrites
history. A fixed working branch per repository, with a forge switch
that merged it into `main` at the release, was rejected as the first
step towards exactly that wrapper: merge and conflict logic in the
forge's hands, two branches a non-developer must understand, and a
branch forced on those who do not need one. The switching half of that
idea survived as the voluntary branch command; the merging half stayed
git's.

## Whose identity a commit carries

The commit identity is git's business, not the forge's. It is
resolved per host by the user's own git configuration, through
conditional stanzas that apply to a repository by where it lives, and
the forge sets no identity anywhere: not in the scripts, not in a
template, not in a file of the instance. `/setup` offers to write that
configuration for the hosts the user pushes to, on his word and never
overwriting what is there; declined, it prints the configuration for
him to apply by hand.

With it comes one recommended global guard: git told to use only the
configuration that applies, with no global name and address. A
repository on a host with no stanza then fails aloud instead of
silently taking a default, and a save commits nothing until git
resolves an identity for the repository. The case of one host serving
two roles is accepted as a risk the user resolves by hand.

This was a reversal. An identity kept by the forge duplicated what the
user's configuration already resolved, every repository carried the
same identity twice, and the forge had gained a file, a template and
three setup steps for a case that had not occurred. The identities
also belong outside the engine for another reason: whatever a file of
the instance carries reaches every subagent, the isolated reviewers
included, and a reviewer's report is a public file.

A commit carries no attribution trailer. The commit message is the
one the principal confirmed, word for word; nothing is added or
proposed beyond it.

## Immutability is a process rule

Reviews, challenges, sources and research are never edited; a source
from its registration, the others from their creation, and corrections
happen downstream. That rule is enforced by convention, not by git.

The reasons: git protects nothing from a commit that rewrites a file,
so a mechanism in git would not be a guarantee; the rule as a
convention costs nothing; and a mechanism would be one more layer to
maintain that still would not stop a hand edit. So the forge states
the rule and relies on the people and the checks that hold it.

## Portability of the scripts

`scripts/` is the only platform-bound layer of the forge, and its
scripts are written to run unchanged on Linux and macOS. They are
Python, 3.8 or newer, run as `python scripts/<name>.py`; `python` on
PATH is their one prerequisite, the same Python the document
conversion needed already, and a system that has only `python3` gives
it that name. Nothing in them is Windows-only: paths are composed
with `pathlib`, the external tools (`git`, `markitdown`, `pandoc`,
`claude`) are resolved from PATH, and the usage examples in their help
are free of Windows-specific paths. Each script carries its help in
its module docstring, and what several scripts share lives in a
module beside them, never twice.

Portability is verified by running the set on Linux. Until that has
been done it is a writing rule, not a verified claim.

## See also

- [Save your work](../use/save-your-work.md): the save.
- [Release a version](../use/release-a-version.md): the release.
- [Work on a branch](../use/work-on-a-branch.md): branches.
- [Scripts](../reference/scripts.md): the scripts themselves.
