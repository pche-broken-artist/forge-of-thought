---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About persistence in git

This page explains how the forge keeps its work in git and why it is
built that way: the one door to git, the two commands that save, the
place of branches, where the commit identity comes from, and what git
is not asked to do. It is for anyone who uses the forge, extends it or
weighs whether to adopt it. It was put together from the Persistence
section of `CLAUDE.md` and from the positions and rejected directions
of the forge's own intent (`projects/forge/10-intent.md`) that give
the reasons.

## Repositories

The engine is one git repository with a remote of its own. Every
project under `projects/` is a repository of its own, with whatever
remote and visibility its owner gives it; the engine ignores them, the
forge's own project excepted, and the scripts recognise a project by
the repository inside its directory. No remote is configured anywhere
in the forge: git carries that information itself, and the scripts
carry no URL and no identity.

Putting a project under git, and adding a remote, is the user's own
one-off act when the project is created. The commands that create a
project write files only. A project that is not under git is a
property, not a defect: a sensitive project may be kept local, with a
repository and no remote, or with no repository at all. The first
keeps the history that renders and recipes rely on, the second does
not.

## One door to git

The scripts in `scripts/` are the only door to git, and that includes
reading state: there are no exceptions. Each script is described in
full by its own help header. Between them they commit and push, bring
in changes from the remotes by fast-forward (on the engine this is the
upgrade channel), report state without changing anything, bring an
existing project in, and create or switch a branch. How many scripts
there are is whatever the door needs, never a rule.

For Claude this is a wall of the harness, not conduct alone: the deny
rules of `.claude/settings.json` enforce it, so the rule does not
depend on Claude remembering it. The rule binds the forge, not the
principal. His own git from the shell is his, and saves he makes
directly from the shell are unaffected by anything on this page.

A commit carries no attribution trailer. The commit message is the one
the principal confirmed, word for word.

## Two doors, two speeds

Saving and releasing are two commands.

- **`/save`** runs the light check and then commits and pushes on
  whatever branch is checked out. It renders nothing, and it takes
  seconds.
- **`/release`** runs on `main` only and refuses elsewhere, naming the
  branch. It runs its checks and settles their findings with the
  principal, re-renders the README and the release notes, and then
  saves with the release message. The release number is the version of
  the intent; at an approved major the release receives the tag
  `v<major>`. Any other tag is given on request, with a free name, and
  may be set on a branch as well.

Which checks each command runs is its own definition's
(`.claude/skills/save/SKILL.md`, `.claude/skills/release/SKILL.md`).

Why two: the renders cost minutes and tokens beyond reason if they ran
at every save, and a quick save without renders had already been the
practice for weeks. With the renders at the release only, the README
on `main` is current at every release and, in between, stale visibly
on the `/forge` map, never silently. Only the major's tag has a fixed
name, so that the checks and the release notes can rely on it: an
integer is a released major, anything else a snapshot.

A single command that re-rendered only what had moved since the last
save was considered and rejected. It would have spared perhaps a third
of the engine's saves and nothing on projects, whose README input, the
ledger, changes at every operation, and it would have added a
staleness state that several commands must all read alike. The
two-command shape saves everything and adds nothing.

## `main` and branches

`main` is the released line. Branches are voluntary and belong to git.
Whoever wants one gets it through one forge script, which creates a
branch or switches to it, and switches back to `main`; the status
script reports the current branch. Nobody is forced onto a branch:
whoever does not use them works on `main`, saves and now and then
releases, and sees none of this.

Merging, rebasing and conflicts stay git's, by hand or by merge
request, never the forge's. The reason is that the principal does not
want a wrapper of git. The boundary is drawn so that the script does
only what changes where the next commit lands, creation and switching,
and nothing that rewrites history. The forge's only knowledge of a
merge is that `/release` runs on `main` afterwards and its checks find
what two branches broke. One hole is known and left until it happens:
two parallel branches taking the same next free ID.

A fixed working branch in every repository, with a forge switch that
merged it into `main` at release, was rejected. It would have been the
first step towards that wrapper, putting merge and conflict logic in
the forge's hands and asking someone who is not a developer to
understand two branches, while forcing a branch on those who do not
need one. Its switching half survives as the voluntary branch script;
the merging half stays git's.

The forge stays a single-user tool per instance. More people means
more instances, coordinated through git.

## The commit identity

The commit identity is git's business, not the forge's. It is resolved
per git host by the user's own git configuration, outside the engine,
and the forge sets no identity anywhere. An identity kept by the forge
would only duplicate what the user's configuration already resolves,
and would have added a file, a template and several steps for a case
that had not arisen. One host serving two identities is accepted as a
risk the user resolves by hand.

What the forge keeps is an offer. On first run, `/setup` asks for the
hosts the user pushes to, with a name and an e-mail for each, and
offers to write his git configuration for them together with one
global guard. The guard means that no global name or e-mail stands in
as a default: a commit in a repository on a host with no identity
configured fails aloud instead of silently taking a default, and a
save commits nothing until git resolves an identity for the
repository. Everything is written on the user's word, never
overwriting what is there; declined, it is printed for him to apply by
hand. `/setup` runs no git operation itself.

## Immutability is a process rule

Some documents of the forge are never edited once made: reviews,
challenges, sources and research. That immutability is a rule of the
process, kept by convention, not a mechanism of git. Git records what
happens to those files; it does not prevent it.

## Portability of the scripts

The forge runs beyond Windows. `scripts/` is the only layer bound to a
platform, and its scripts are written to run unchanged on Linux and
macOS: cross-platform PowerShell 7 with nothing Windows-only, external
tools found on the path, and usage examples in the help free of
Windows-specific paths. Until the set has been run on Linux this is a
writing rule, not a claim. New scripts are written in Python, on the
feedback of the forge's users; the PowerShell scripts are rewritten to
it in time and stand as they are until then.

## See also

- [Save your work](../use/save-your-work.md): the save.
- [Release a version](../use/release-a-version.md): the release.
- [Work on a branch](../use/work-on-a-branch.md): branches.
- [Scripts](../reference/scripts.md): the scripts themselves.
