---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 93883a0703ca76a9
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
project over time: each is a git repository of its own, saved,
released and pulled through the forge's own scripts and never
through git typed by Claude. This page is for a user who wants to
know what happens to his work when he saves, for an extender who
touches the scripts, and for an evaluator who asks why git is held
behind one door and why saving and releasing are two commands of two
speeds.

## What it is

The engine is one git repository with a remote. `main` is the
released line. Branches are voluntary and left to git. Every project
under `projects/` is a repository of its own, gitignored by the
engine; `projects/forge`, the forge's own project, is the one
exception. The scripts recognise a project repository by
`projects/<slug>/.git`.

Initialising a project's repository and adding its remote are the
principal's one-off act at creation. The principal is the person
whose thinking is forged, the one whose word every write and every
save waits for. A project "not under git" is a property, not a
defect. No remote is configured anywhere in the forge: git carries
that information itself.

The scripts in `scripts/` are the only door to git, reading state
included, with no exceptions ([Scripts](../reference/scripts.md)).
For Claude the door is a wall of the harness, that is, of the
program that runs Claude and holds its permission rules: the deny
rules of `.claude/settings.json` enforce it. The rule binds the
forge, not the principal. His own git from the shell is his, and a
save made directly from the shell is unaffected. How many scripts
there are is not a rule.

## How it works

### The scripts

Five scripts serve the engine and every project repository alike,
each described in full by its own help header:

- `forge-save.py` commits and pushes.
- `forge-pull.py` fast-forwards from the remotes; on the engine it
  is the upgrade channel.
- `forge-status.py` reports state without changing anything, the
  current branch and the state against the origin among it.
- `forge-clone.py` brings an existing project in; `/import-project`
  is the command that runs it.
- `forge-branch.py` switches to a branch or creates it.

Merging belongs to git, by hand or by merge request. The scripts
carry no URL and no identity. Each carries its help in its module
docstring. What several scripts share lives in a module beside them
(`forge_repos.py`, `forge_tools.py`, `docs_map.py`), never twice.

The scripts are Python, 3.8 or newer, run as
`python scripts/<name>.py`. `python` on PATH is their one
prerequisite; a system that has only `python3` gives it that name.
`scripts/` is the only platform-bound layer of the forge, and it is
written to run unchanged on Linux and macOS: nothing Windows-only,
paths composed with `pathlib`, the external tools (`git`,
`markitdown`, `pandoc`, `claude`) resolved from PATH, and the usage
examples in the help free of Windows-specific paths and invocations.
Portability is verified by running the set on Linux. Until then it
is a writing rule, not a claim.

### Two doors, two speeds

`/save` ([Save your work](../use/save-your-work.md)) runs the
`light` check and then commits and pushes on whatever branch is
checked out, through `forge-save`, with no render. It takes seconds.

`/release` ([Release a version](../use/release-a-version.md)) runs
from `main` only and refuses elsewhere, naming the branch. It runs
its checks and settles their findings with the principal before the
release commit, in a walkthrough, that is, the findings worked one
per message, each closed with his verdict. It re-renders the README
and the release notes. Then it saves with the release message
"release <intent version>" and, at an approved major, the tag
`v<major>`. The release number is the intent's version. Which checks
each command runs is said by its own definition
(`.claude/skills/save/SKILL.md`, `.claude/skills/release/SKILL.md`).

Only the major's tag has a fixed name, so an integer is a released
major and anything else a snapshot. Any other tag is the principal's
request with a free name, through `/save --tag` or `/release --tag`,
on a branch as well.

Between two releases the README on `main` is stale. The `/forge` map
(the state map of a project) shows it as stale, so the staleness is
visible and never silent.

### The door inward

`/pull` ([Pull from the remote](../use/pull-from-the-remote.md)) is
the door inward. The `/forge` map and `/pull` ask
`forge-status --remote` for the state of the engine and of the
project against its origin and say it as a fact: up to date, behind,
ahead, diverged, or no origin. Each state has one offer:

- behind and clean: `/pull`;
- behind with unsaved work: `/save` first;
- ahead: `/save`;
- diverged: the principal merges by hand or lets `/save` rebase his
  commits onto the remote, and nothing is pulled until he has.

`/pull` pulls only a clean repository that is behind and offers the
rest. The forge never pulls or merges on its own judgement. The one
rebase the forge does is the save's: the principal's own commits
onto the remote. On the engine, a pull is the upgrade, a
fast-forward of `main`.

### Branches

Branches ([Work on a branch](../use/work-on-a-branch.md)) are
voluntary and belong to git. `forge-branch <name>` creates the
branch or switches to it; `forge-branch main` switches back;
`forge-status` reports the current branch. Merge and conflicts stay
with git. Nothing forces a branch: whoever does not use them works
on `main`, saves, now and then releases, and sees none of this. The
forge's only knowledge of a merge is that `/release` runs on `main`
after it and its checks find what two branches broke. One hole is
known and left until it happens: two parallel branches taking the
same next free ID. The forge stays a single-user tool per instance,
that is, per installation; more people means more instances and
coordination by git.

### The commit identity

The commit identity belongs to git, never to the forge. It is
resolved per host by the principal's own git configuration outside
the engine (`includeIf` stanzas in `~/.gitconfig`), which `/setup`
offers to write. The forge sets no identity anywhere. The
recommended guard, also offered by `/setup`, is
`user.useConfigOnly = true` with no global `user.name` or
`user.email`. A repository on a host with no stanza then fails aloud
instead of taking a default, and a save commits nothing until git
resolves an identity for the repository. The case of one host
serving two identities is accepted as a risk the principal resolves
by hand.

A commit carries no attribution: Claude neither adds nor proposes a
`Co-Authored-By` or `Claude-Session` trailer, and the commit message
is the one the principal confirmed, word for word.

### Immutability

Immutability of documents is a process rule, not a git mechanism:
the forge does not edit an immutable document, and git is not asked
to prevent it.

## Why

**Why the scripts are the only door, and a wall of the harness.**
The reason why the door is enforced by the harness rather than by
Claude's conduct alone is not recorded. What is recorded is the
boundary: the rule binds the forge and leaves the principal's own
git alone.

**Why two commands.** The renders cost minutes and tokens beyond
reason at every save, and a two-speed save had existed in practice
for weeks before it was made a rule. With the renders at the release
only, the README on `main` is current at every release and stale in
between visibly, through the `/forge` map, never silently. One
alternative was rejected: a single `/save` that regenerates only a
render whose recipe or input moved, with a skipped mark in the
ledger (the file that holds a project's state). It would have saved
perhaps a third of the engine's saves and nothing on projects,
whose README reads the ledger, which moves at every operation; and
it would have added a staleness state that `/save`, `/forge` and
`/check` all had to read alike. The two-command shape saves
everything and adds nothing.

**Why the forge never pulls or merges on its own.** The principal
works on more than one machine, so a clone behind its origin is the
normal case, and a state map drawn from it would be a map of the
wrong state. A pull or a merge made on Claude's judgement would be
work done without the principal's word.

**Why branches are voluntary and merging belongs to git.** The
principal does not want a wrapper of git. The boundary is drawn so
that the script does creation and switching, which only change where
the next commit lands, and nothing that rewrites history. One
alternative was rejected: a fixed `work` branch per repository, one
script creating and switching it, and `/release` merging it into
`main`. It was the first step towards that wrapper, because merge
and conflict logic would have passed into the forge's hands and a
person who is not a developer would have had two branches to
understand, while a branch was forced on those who do not need one.
The switching half survives as the voluntary `forge-branch`; the
merging half stays with git.

**Why the commit identity is git's and the guard exists.** The
engine carries no instance facts, and names, e-mail addresses and
hosts are such facts; they live in the principal's own git
configuration outside the engine. An identity kept by the forge
duplicated what that configuration already resolved: every
repository carried the same identity twice, and the forge had gained
a file, a template and three identity steps for a case that had not
occurred. The guard exists so that a commit in a repository on a
host with no identity fails aloud instead of silently taking a
default.

**Why a commit carries no attribution trailer.** The reason is not
recorded; only the rule is.

**Why immutability stays a process rule.** Git protects nothing from
a commit that rewrites a file. The rule costs nothing. A mechanism
would be one more layer to maintain that still would not stop a hand
edit.

**Why the scripts are Python and the only platform-bound layer.** The
forge runs beyond Windows, so the one layer bound to a platform is
kept small and written to run unchanged elsewhere. Python was chosen
on the feedback of the forge's users, and it is the same Python the
document conversion needed already, so `python` on PATH remains the
one prerequisite.

**Why no remote is configured in the forge.** Git carries that
information itself, so the scripts need no URL.

## A worked example

A principal keeps a thought project `<slug>` and works on it from
two machines.

1. On the first machine he works on `main`, finishes a round of the
   intent and types `/save <slug>`. The `light` check runs, the
   commit and the push take seconds, and no render is touched. The
   project's README is now stale, and the `/forge` map says so.
2. On the second machine, the next day, `/forge <slug>` reports the
   project behind its origin and clean, and offers `/pull`. He types
   `/pull <slug>`; the forge fast-forwards and says what came in.
   Had there been unsaved work on that machine, the offer would have
   been `/save` first. Had the two machines diverged, the forge
   would have pulled nothing and left the merge to him.
3. When the intent reaches an approved version, he types
   `/release <slug>` on `main`. The checks run and he settles their
   findings in a walkthrough; the README and the release notes are
   re-rendered; the release commit "release 2.0" and the tag `v2`
   are pushed. On any other branch the same command refuses and
   names the branch.

## See also

- [Save your work](../use/save-your-work.md): the save.
- [Release a version](../use/release-a-version.md): the release.
- [Pull from the remote](../use/pull-from-the-remote.md): the pull.
- [Work on a branch](../use/work-on-a-branch.md): branches.
- [Scripts](../reference/scripts.md): the scripts themselves.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-11 for version 5.3 from the files the
front-matter names; never edited by hand.
