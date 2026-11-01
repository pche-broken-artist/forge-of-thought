---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 2948e34365ad22ac
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

The forge keeps the engine and every project in git, and Claude
touches git only through the scripts in `scripts/`. This page
explains how that door is built and held, why there are two doors
outward at two speeds, how the door inward works, and what the
forge leaves to git itself. It is for anyone who uses the forge,
extends it or judges it, and it stands on its own: the how-to pages
it links to say what you type, this page says what holds and why.

## What it is

The engine is one git repository with a remote. Its `main` is the
released line. Branches are voluntary and left to git.

Every project under `projects/` is a repository of its own, with
whatever remote and visibility its owner gives it. The engine does
not know the projects. Initialising a project's repository and
adding its remote are the one-off act of the principal (the person
whose thinking is forged) at creation. The scripts carry no remote
address and no identity. Git carries that information itself.

The scripts recognise a project's repository by one question put to
git: whether the project's directory is the top of a repository. They
never look for a `.git` folder. A project whose top lies elsewhere,
such as a directory inside somebody else's repository, or that has no
repository at all, is for the forge a project outside git. The
scripts write its files to disk and run no git. The repository above
it belongs to its owner and is asked nothing. "Not under git" is a
property of a project, not a defect.

The scripts in `scripts/` are the door to a write of git. Nothing of
Claude's own commits, pushes, pulls, merges, rebases, branches, tags,
stashes, resets or touches a remote or a configuration except through
a script. Reading git directly is open. The one exception to the door
is the few commands that finish the step of a conflict, which run on
the principal's yes. How many scripts there are is not a rule: the
door has as many as it needs. The scripts themselves are listed in
[Scripts](../reference/scripts.md).

A commit carries the message the principal confirmed, word for word,
and no attribution line.

The ledger (the state of a project, made from its documents at read
time) is not in git at all. Why it is made at read time is said in
[The ledger, made from the records](the-ledger.md).

Immutability of a document is a process rule, not a git mechanism.

## How it works

### The wall between reading and writing

The line between reading git and writing it is held for Claude by a
hook of the harness. The harness is the program Claude runs in; a
hook is a small program the harness runs before a tool is used. The
hook is the forge's own, `scripts/hook-git.py`, registered in
`.claude/settings.json` on the one shell tool through which Claude
runs git. It reads the whole command Claude is about to run, finds
every call of git in it past the shell's separators and git's own
global options, and answers in one of three ways:

- allow, for a command that only reads;
- ask, for the few commands that finish the step of a conflict, so
  that the harness puts the command to the principal and runs it on
  his yes;
- deny, for everything else, naming the script of the forge to use
  instead.

Whatever the hook cannot read, it denies. A part of the command that
is not git is left to the harness. Over a whole command deny outranks
ask, and ask outranks allow. The ask holds in the automatic
permission mode; a deny holds in every mode. The hook reads no file
and writes nothing.

The other shell tool stays closed to git whole, by a deny rule in the
same settings file. So there is one parser and one door.

The rule binds the forge, not the principal. His own git from his own
shell is his, and a save made directly from the shell is unaffected.

The same settings file switches off the attribution the harness
would otherwise add to a commit. So the commit message is the one
the principal confirmed, and nothing is appended to it.

### Two doors, two speeds

Two commands write outward, and they differ in speed.

`/save` runs the light check and then commits and pushes on whatever
branch is checked out. It renders nothing and takes seconds. The
message is drafted from the records and confirmed by the principal,
or given on the command line. `/save --quick` leaves the light check
out and changes nothing else. What you type is in
[Save your work](../use/save-your-work.md).

`/release` runs from `main` only and refuses elsewhere, naming the
branch. It runs its checks and settles their findings with the
principal. It offers the documentation. It re-renders the README and
the release notes. It then saves with the release message, "release"
and the intent's version, and at an approved major with the tag of
the major, `v` and the integer. The closing save runs without a
second light check. Because the release ran that check already.
Inside a release the order is fixed: checks, documentation, README
and release notes, state render, save. Because the README reads the
documentation's index, so the documentation must come first. The
release has no quick way of its own, since its checks are the
condition of a release. What you type is in
[Release a version](../use/release-a-version.md).

Only the major's tag has a fixed name. Any other tag is the
principal's request, with a free name, on a branch as well.

### The door inward

`/pull` is the door inward. It looks at the remote and says the state
of the repository against its origin as a fact: up to date, behind,
ahead, diverged, or no origin. Each state has one offer. A clean
repository that is behind is pulled. A repository behind with unsaved
work is saved first. A repository ahead is saved. A diverged
repository is merged by the principal's own hand, or `/save` rebases
his own linear commits onto the remote. The forge never pulls or
merges on its own judgement. What you type is in
[Pull from the remote](../use/pull-from-the-remote.md).

`/save` pushes a clean repository that is ahead of its origin. A
branch without an upstream is counted against the remote's branch of
the same name after a fetch. So a rebase finished by hand and a clone
switched to a branch both have a door to the push.

### Branches and merging

Branches are voluntary. A script of the forge switches to a branch
or creates one; see [Work on a branch](../use/work-on-a-branch.md).
Merging is git's, by hand or by merge request: the integrator merges
on his own clone with git itself, outside the forge's scripts. What
git leaves standing is settled in the step of a conflict.

### The step of a conflict

A conflict that `/save` meets in its rebase is left standing, not
aborted. The commit is made and nothing is lost. The script prints
the files in conflict and the step that follows, and the status
script says that a rebase or a merge is in progress.

The step of a conflict is the forge's help, not its mechanism. Claude
reads both sides and lays them out as a walkthrough (one item per
message, each closed with a verdict of the principal). The principal
decides. Claude writes the chosen wording into the file, since the
conflict markers are text, and a record of the change into the
history of the document as for any change. Then the finishing
commands of git, such as `git add` and `git rebase --continue`, run
on the hook's ask and the principal's yes. Then `/save` again. A save
that finds a rebase or a merge already standing refuses before it
stages anything. So conflict markers are never committed. The whole
step is in [Settle a conflict](../use/settle-a-conflict.md), the one
place where Claude's git asks the principal.

### The ways of merging and the files made on `main`

Every file has a way of merging, set by path: the record files merge
as text with both tails kept, and the files made for a reader are
taken as `ours` at a merge; the three ways and what the forge
promises two people on one project are in
[Working together on one project](working-together.md).

Whatever makes a derived file or migrates a project, that is
`/release`, `/publish`, `/document` and `/migrate`, runs on `main`
only. Each refuses a repository that is behind or diverged from its
origin and offers `/pull`. A migration runs once per project, on one
clone, under git or not, on the principal's word; everyone else
pulls before working on.

`ours` is a merge driver that git does not have built in. `/setup`
registers it once per machine, on the principal's word, in his global
git configuration, together with the settings it needs: the rebase
backend that honours merge drivers, since the other backend ignores
them, and the renormalisation of line endings, since a file committed
with Windows line endings before normalisation would otherwise
conflict whole. The status script says when the registration is
missing.

### Identity

The commit identity is git's business, not the forge's. It is
resolved per host by the principal's own configuration, outside the
engine, and the forge sets no identity anywhere. The recommended
guard, offered by `/setup`, is that git is told to use only a
configured identity and is given no global one. So a repository on a
machine with no identity configured fails aloud instead of taking a
default.

### Where the scripts run

The scripts are Python. `python` on PATH is their one prerequisite,
Python 3.8 or newer, run as `python scripts/<name>.py`. A system that
has only `python3` gives it that name. `scripts/` is the only
platform-bound layer of the forge, and it is written to run unchanged
on Linux and macOS: paths are composed with `pathlib`, external tools
such as `git`, `pandoc` and `markitdown` are resolved from PATH, and
the usage examples in the scripts' help carry nothing Windows-only.
Each script carries its help in its module docstring. What several
scripts share lives in a module beside them, never twice.

What has been verified is narrower than what is written to hold. The
git scripts, the ledger script and the documentation state script
have run on Linux. The conversions and the two hooks are a writing
rule until a run says otherwise. Nothing has run on macOS, where the
whole set is the writing rule alone.

## Why

**Why reading is open and writing is not.** Reading changes nothing.
The scripts had to copy git verb by verb to serve reading, which
served nobody. Why writing goes through scripts rather than through
Claude's own git commands is not recorded in the files this page is
made from, beyond the rejected directions below.

**Why a wall and not conduct alone.** The door is enforced by the
harness, not trusted to a rule Claude reads. The reason a rule alone
was not enough is not recorded.

**Why a hook and not deny rules on the writing verbs.** A deny rule of
the harness matches the text usually typed, not the command: a push
written with a path option in front of it passes a rule written for
the plain form. A deny rule cannot be carved by an allow rule and is
not overridden by a hook. Two walls with one hole read worse than one.
The cost of the hook is a parser of the shell that is a heuristic.
So what it cannot read, it denies.

**Why the harness and not a sandbox of the operating system.** Such
a sandbox is unavailable on Windows, where enforcing it would have
meant no shell at all.

**Why the other shell tool is closed whole.** So that there is one
parser and one door.

**Why two doors.** The renders cost minutes and tokens beyond reason
at every save, and the two-speed save had existed in practice before
it was written down. With the renders at the release only, the
README on `main` is current at every release and stale in between
visibly, shown by the state map of `/forge`, never silently. Two
directions were rejected in its favour. One was rendering at the save
only what had gone stale: it would have saved perhaps a third of the
engine's saves and nothing on a project, whose README input moves at
every operation, and it would have added a staleness state that the
save, the state map and the check must all read alike. The other was
a fixed working branch with a switch of the forge that merges it at
the release: it was the first step towards a wrapper of git that the
principal does not want, with merge and conflict logic in the forge's
hands and two branches a non-developer must understand, forced on
those who do not need a branch. Of it the switching half survives as
the voluntary branch script. The merging half stays git's.

**Why the forge never pulls or merges on its own.** The principal may
work on more than one machine. So a clone behind its origin is the
normal case, and a state map drawn from it is a map of the wrong
state. A pull or a merge made on Claude's judgement would be work
done without the principal's word.

**Why a conflict is left standing.** The commit is made and nothing
is lost. Why the step is settled by a walkthrough rather than by a
mechanism of the forge is given by the rejected working branch above:
merge and conflict logic is not to be in the forge's hands.

**Why the derived files are made on `main` only and refuse a
repository behind or diverged.** The files made for a reader are
taken as `ours` at a merge. The rebase of a save turns `ours` round.
So a fresh README would silently lose to an older one, and a major's
tag would mark a wrong state.

**Why the registration of `ours` is per machine.** An unregistered
clone silently falls back to a conflict on the derived files, which
is why the status script reports the missing registration. The
registration belongs to the machine, not to the project, so that a
migration never touches it.

**Why the identity is git's.** An identity kept by the forge
duplicated what the principal's own configuration already resolved,
and every repository carried the same identity twice. Names, e-mail
addresses and hosts are instance facts, and the engine carries none.

**Why immutability is a process rule.** Git protects nothing from a
commit that rewrites a file. The rule costs nothing. A mechanism
would be one more layer to maintain that still would not stop a hand
edit.

**Why Python.** It was decided on the feedback of the forge's users,
and it is the same Python the document conversion needed already.

**Why "not under git" is a property.** The repository above a project
is its owner's and is asked nothing, not even what it tracks. A
project outside git is migrated the same as any other, since none of
the refusals of git applies to it.

## A worked example

A project with the slug `my-project` lives in `projects/my-project`,
a repository of its own with an origin.

After a round over the intent, the principal says `write`, Claude
writes the round, and the principal says `/save my-project`. The
light check runs, Claude drafts the commit message from the records
of the round, the principal confirms it, and the save script commits
and pushes on the branch that is checked out. The commit carries the
confirmed message and nothing else. Were Claude to try a push of its
own, the hook would deny it and name the save script instead.

On a second machine the next morning, the state map of `/forge
my-project` ends with the state against the origin: behind. The
principal says `/pull my-project`. The repository is clean and
behind, so it is fast-forwarded. Had he made a commit there first,
the state would have been diverged and the forge would have offered
rather than pulled.

Later the same day two clones have both moved, and `/save my-project`
rebases the principal's commits onto the remote. One file of the
intent conflicts. The save leaves the conflict standing and prints
the file and the step that follows. Claude lays both sides out, one
conflict one question, the principal chooses the wording, Claude
writes it into the file and a record into the intent's history, and
the hook puts `git add` and `git rebase --continue` to the principal,
who says yes. Then `/save my-project` again pushes the clean
repository.

At the end of the iteration the intent reaches version 2.0, an
approved major. The principal says `/release my-project` on `main`.
The checks run and their findings are settled, the documentation is
offered, the README and the release notes are re-rendered, the state
render is remade, and the closing save, without a second light check,
commits "release 2.0" and tags it `v2`. Had a colleague pushed in the
meantime, the release would have refused the repository as behind and
offered `/pull` first.

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

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
