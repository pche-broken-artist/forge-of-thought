---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 7f19a8e556d01a33
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
  - projects/forge/10-intent.md#POS.1970
  - projects/forge/40-solution-design.md#SOL.0520
  - projects/forge/40-solution-design.md#SOL.0740
  - projects/forge/10-intent.md#REJ.0160
  - projects/forge/10-intent.md#REJ.0170
---

# Persistence in git

Persistence in git is the way the forge keeps its files: the engine
is one git repository with a remote, and every project is a git
repository of its own. This page explains why Claude writes git only
through the scripts of the forge, why saving and releasing are two
commands of two speeds, and how pulling, branching and merging stay
with git and with the principal (the person whose thinking is
forged). It is for the user who saves and releases, for the extender
who adds or changes a script, and for the evaluator who asks what the
forge promises about the history of its files.

## What it is

The engine is one git repository with a remote. `main` is the
released line. Branches are voluntary and left to git. Every project
under `projects/` is a repository of its own, with whatever remote
and visibility its owner gives it. The scripts recognise such a
project by asking git whether the project's directory is the top of
a repository, never by looking for a `.git` folder. A project whose
top lies elsewhere, or that has no repository, is for the forge a
project outside git: the scripts write its files to disk and run no
git, whatever repository lies above it. Such a project comes in by
hand, a copy or a link into `projects/`. A project "not under git" is
a property, not a defect. Initialising a project's repository and
adding its remote are the principal's one-off act at creation.

The scripts in `scripts/` are the door to a write of git. Nothing of
Claude's own commits, pushes, pulls, merges, rebases, branches, tags,
stashes, resets or touches a remote or a configuration except through
a script. Reading git directly is open to Claude, since reading
changes nothing. The line between the two is held for Claude by a
hook of the harness (the program Claude runs in): it allows a reading
command, denies every write and names the script to use instead, and
puts the few commands that finish the step of a conflict to the
principal, which run on his yes. The other shell tool is closed to
git whole, so that there is one door. The rule binds the forge, not
the principal: his own git from the shell is his. How many scripts
there are is not a rule; the scripts themselves are listed in
[Scripts](../reference/scripts.md). The scripts carry no URL and no
identity: git carries that information itself.

A commit carries the message the principal confirmed, word for word,
and no attribution line.

Two doors, two speeds. `/save` runs the light check and then commits
and pushes on whatever branch is checked out, with no render; how it
runs is [Save your work](../use/save-your-work.md). `/release` runs
from `main` only, runs its checks, regenerates the README and the
release notes and then saves with the release message and the
major's tag; how it runs is
[Release a version](../use/release-a-version.md).

`/pull` is the door inward: the forge looks at the remote, says the
state as a fact, beside it what waits on GitHub outside git, pulls
only a clean repository that is behind, and never merges on its own;
how it runs is [Pull from the remote](../use/pull-from-the-remote.md).

Merging is git's. The integrator merges on his own clone with git
itself, by hand or by merge request, outside the forge's scripts;
what git leaves standing is settled in the step of a conflict. Every
file has a way of merging, and what the forge promises two people on
one project, is
[Working together on one project](working-together.md). The record
files merge as text, two tails kept both. The files made for a
reader, the README and release notes, the documentation, the
published files and the state render, are made only on `main` and
taken as `ours` at a merge. `ours` is a merge driver git does not
know until it is registered: `/setup` registers it once per machine,
with the git settings it needs, and the status script says when the
registration is missing. How a branch is taken and left is
[Work on a branch](../use/work-on-a-branch.md).

The ledger (the single source of truth for a project's state, made
at read time) is not in git at all; why is said in
[The ledger, made from the records](the-ledger.md).

The commit identity is git's, resolved per host by the principal's
own git configuration, with a guard so that a repository on a host
with no identity fails aloud instead of taking a default. The forge
sets no identity anywhere.

Immutability of documents is a process rule, not a git mechanism.

The scripts are Python, run as `python scripts/<name>.py`, and
`python` on PATH is their one prerequisite. They are written to run
unchanged on Linux and macOS. The engine's tests run in CI on Linux
and Windows at every push; what they cover is
[The tests](the-tests.md).

## How it works

### The wall between reading git and writing it

Protection relies on the permission system of the harness, not on a
sandbox of the operating system: commands and file operations run
under permission prompts and allowlists, and shared deny rules in
`.claude/settings.json` block sensitive paths. The line between
reading git and writing it is a hook of the forge's own,
`scripts/hook-git.py`, registered in that same file on the one shell
tool through which Claude runs git. The harness runs the hook before
every command Claude sends through that tool.

The hook reads the whole command, splits it at the shell's
separators, cuts out the body of a heredoc as text, and finds every
call of git in it past git's own global options. It answers in one
of three ways:

- allow, for a reading verb with reading flags;
- ask, for the few commands that finish the step of a conflict,
  named one by one, so that the harness puts the command to the
  principal and runs it on his yes: staging a file, continuing or
  aborting the rebase or the merge in progress, a plain merge of one
  branch, and taking one side of a file in conflict;
- deny, for everything else, naming the script of the forge to use
  instead where one exists.

Denied are the writing verbs, a verb the hook does not know (an alias
among them), a reading verb with a writing flag, a global option that
changes where or how git runs, git hidden inside another command (a
substitution or a wrapper that runs what it is given) and a part of
the command the hook cannot read. The shell's redirections are not
git's arguments and are stripped before a verb is judged. A part of
the command that is not git is left to the harness. Over a whole
command deny outranks ask, and ask outranks allow. An ask holds in
the automatic permission mode; a deny holds in every mode. The hook
reads no file and writes nothing.

The other shell tool stays closed to git whole by a deny rule of the
same settings file. The hook is for Claude's tools alone: the
principal's own git from the shell is his.

### A save

`/save` runs the light check, drafts the commit message from the
records, has the principal confirm it (or takes one given with
`-m`), and then commits and pushes on whatever branch is checked out,
through `scripts/forge-save.py`. It makes no render. `/save --quick`
leaves the light check out and nothing else. The script pushes a
clean repository that is ahead of its origin; a branch without an
upstream is counted against the remote's branch of the same name
after a fetch, so that a rebase finished by hand and a clone switched
to a branch have a door to the push. Where the branch has diverged
from the remote, the one rebase of the forge is this save's: the
principal's own linear commits are put onto the remote's.

A rebase that conflicts is left standing by the save, not aborted:
the commit is made and nothing is lost. The script prints the files
in conflict and the step that follows, and the status script says
that a rebase or a merge is in progress. A save that finds a rebase
or a merge already standing refuses before it stages anything, so
that conflict markers are never committed.

### The step of a conflict

The step of a conflict is the forge's help, not its mechanism.
Claude reads both sides and lays them out as a walkthrough (one item
per message, the principal's verdict on each), one conflict one
question. The principal decides. Claude writes the chosen wording
into the file, the markers being text, and a record into the history
of the artefact, as for any change. The commands that finish the
step, `git add`, `git rebase --continue` or `--abort`, `git merge
--continue` or `--abort`, `git merge <branch>`, `git checkout --ours`
or `--theirs` on a file, run on the hook's ask and the principal's
yes. Then `/save` runs again. The step in full is
[Settle a conflict](../use/settle-a-conflict.md).

### A release

`/release` runs on `main` only and refuses elsewhere, naming the
branch. It refuses a repository behind or diverged from its origin
and offers `/pull`. The order inside every release is fixed:

1. on the engine, the tests first, through `/test`; a red test stops
   the release; where pytest is missing the release says that the
   tests did not run and goes on only on the principal's word;
2. the checks, with their walkthrough;
3. the documentation, offered on the principal's word;
4. the README and the release notes, from the settled sources;
5. the state render;
6. the closing save, with the release message
   `release <intent version>` and, at an approved major, the tag
   `v<major>`; this save runs without the light check.

`/release --auto` runs the whole release through: the checks and
their agents without asking, the documentation on the one question
it asks before anything runs, the renders and the save with the
drafted message. It stops only where a thing is serious: a repository
behind or diverged, a finding that would change a position or a rule,
a new instance fact in a render, and always at the tag of a major,
which is a deliberate act. Only the major's tag has a fixed name. Any
other tag is the principal's request, with a free name, on a branch
as well.

Whatever makes a derived file or migrates a project, `/release`,
`/publish`, `/document` and `/migrate`, runs on `main` only and
refuses a repository behind or diverged from its origin, offering
`/pull`.

### The door inward

The state map of a project and `/pull` ask the status script, with
`--remote`, for the state of the engine and of the project against
its origin, and say it as a fact: up to date, behind, ahead,
diverged, or no origin. Where a repository has an origin, the script
also asks GitHub, through `gh` on PATH, for what lies there outside
git: the open pull requests and the discussions nobody of the
repository has answered. The map and the pull say it as a fact beside
the state of the branch, with one offer: look at it before anything
is written into the project. Whatever keeps the script from reading
it, the line says so and the map goes on. The forge reads it only; it
merges, answers and closes nothing.

Each state has one offer:

- behind and clean: `/pull`, which fast-forwards;
- behind with unsaved work: `/save` first;
- ahead: `/save`;
- diverged: the principal merges the remote's branch into his own by
  his own hand, or lets `/save` rebase his own linear commits onto
  the remote, a conflict settled in the step of a conflict; nothing
  is pulled until he has.

The reflection before a write reads that state from the last look at
the remote. The write step never fetches and only repeats the state
the reflection knew; an unknown or stale state never blocks a write.

### A migration

A release that changes the shape of files comes with a migration,
`/migrate [slug]`, through `scripts/forge-migrate.py`: once per
project, on one clone, under git or not, on the principal's word,
never on Claude's. Until a project is migrated nothing writes into
it: the state map, the checks and every writing command say what
`templates/project.md` says and stop.

### The registration on the machine

`/setup` registers, once per machine and on the principal's word,
through `scripts/forge-config.py`, in the global git configuration:

- the merge driver `ours`;
- the rebase backend that honours merge drivers, since the other
  backend ignores them;
- the renormalisation of line endings at a merge, since a file
  committed with Windows line endings before normalisation would
  otherwise conflict whole;
- the reuse of recorded resolutions, as a convenience;
- an offer of a conflict style that shows the common ancestor.

The status script reports a missing registration, since an
unregistered clone silently falls back to a conflict on the derived
files. The registration is the machine's, not the project's, and a
migration does not touch it.

### The identity

The commit identity is resolved per host by the principal's own git
configuration, one stanza per host, which `/setup` offers to write
through the same script. The recommended guard, also offered by
`/setup`, is git told to use only what is configured, with no global
name and no global e-mail: a repository on a host with no stanza then
fails aloud instead of taking a default, and a save commits nothing
until git resolves an identity for the repository.

### Portability

`scripts/` is the only platform-bound layer. Its scripts are Python
3.8 or newer, run as `python scripts/<name>.py`; a system that has
only `python3` gives it that name. Nothing is Windows-only: paths are
composed with `pathlib`, external tools (`git`, `markitdown`,
`pandoc`, `claude`) are resolved from PATH, and the usage examples in
the scripts' help are free of Windows-specific paths and
invocations. Each script carries its help in its module docstring;
what several scripts share lives in a module beside them, never
twice.

Portability is verified by a run, not claimed. The tests run in CI on
Linux and Windows at every push, the git scripts, the ledger, the
light check and the git hook's judgement among them. The conversions
are tested for their failure without the tool alone. The per-prompt
hook is a writing rule still, not a claim, until a run says
otherwise. Nothing has run on macOS: for it the whole set is the
writing rule alone.

## Why

Why a write of git goes through a script of the forge rather than
through git typed by Claude is not recorded in the inputs of this
page. Why reading is open is recorded: reading changes nothing, and
the scripts had to copy git verb by verb to serve it before it was
opened.

Why the line is a hook of the harness and not deny rules of the
harness: a prefix deny rule matches the text usually typed, not the
command, so that a differently written push passes it; a deny rule
cannot be carved by an allow rule and is not overridden by a hook;
and two walls with one hole read worse than one. The other shell tool
is closed to git whole so that there is one parser and one door.

Why the finishing commands of a conflict ask instead of going through
a script: the step of a conflict is the forge's help, not its
mechanism, and merge and conflict logic in the forge's hands would be
the first step towards a wrapper of git, which the principal does not
want. For the same reason merging stays git's and a fixed working
branch merged by the forge was rejected: it would put two branches
before a non-developer who must understand them, and force a branch
on those who do not need one. The switching half of that idea
survives as the voluntary branch command.

Why a commit carries no attribution line is not recorded in the
inputs of this page; what is recorded is that the message is the one
the principal confirmed, word for word.

Why two doors: the renders cost minutes and tokens beyond reason at
every save, and the two-speed save had existed in practice before it
was named. With the renders at the release only, the README on `main`
is current at every release and stale in between visibly, in the
state map, never silently. Rendering only the stale renders at every
save was rejected: it would have saved perhaps a third of the
engine's saves and nothing on a project, whose README input, the
ledger, moves at every operation, and it would have added a staleness
state that three commands must read alike. `/save --quick` is the
principal's for a save he wants on the remote at once; `/release` has
no quick way, since its checks are the condition of a release. The
closing save of a release runs without the light check because the
release ran it already. The documentation comes before the README
because the README reads the documentation's index. `/release --auto`
exists because a release done step by step was the forge's biggest
chore. The major's tag has a fixed name so that a check and the
release notes can rely on it: an integer is a released major,
anything else a snapshot. A release of the engine runs the tests
first; a save never runs them, because every push runs them in CI.

Why the forge looks at the remote and never pulls or merges on its
own: the principal works on more than one machine, so a clone behind
its origin is the normal case, and a map drawn from it is a map of
the wrong state; and a pull or a merge made on Claude's judgement
would be work done without the principal's word. Why the map also
says what waits on GitHub: a contribution seen on the morning it
arrives costs nothing, and the same contribution seen after a week of
one's own rounds costs renumbered items, re-dated versions and a
conflict at the merge. The write step never fetches because the
network was driven out of the write, so that an outage cannot spoil
the round.

Why the files made for a reader are made on `main` only, and why
whatever makes them refuses a repository behind or diverged: at a
merge they are taken as `ours`, and the rebase of a save turns `ours`
round, so a fresh README would silently lose to an older one and a
major's tag would mark a wrong state. A conflict is left standing
rather than aborted so that the commit is made and nothing is lost.

Why `ours` is registered per machine and not per repository: the
registration is the machine's, and a migration must not touch it.
The status script says when it is missing because an unregistered
clone falls back to a conflict without a word.

Why the forge keeps no identity and no URL: an identity kept by the
forge duplicated what the principal's own configuration already
resolved, every repository carried the same identity twice, and the
forge had gained a file, a template and three identity steps for a
case that had not occurred. The case of one host serving two
identities is accepted as a risk the principal resolves by hand. Git
carries the remote's address itself. The guard exists so that a
commit on a host with no identity fails aloud instead of silently
taking a default.

Why immutability is a process rule: git protects nothing from a
commit that rewrites a file, the rule costs nothing, and a mechanism
would be one more layer to maintain that still would not stop a hand
edit.

Why the scripts are Python: decided on the feedback of the forge's
users; `python` is the one prerequisite because it is the same Python
the document conversion needed already. Why portability is a run and
not a claim: a writing rule says what the scripts avoid, a run on the
platform says what works, and where nothing has run, as on macOS, the
page says so instead of claiming.

## A worked example

The principal works on the project `my-project` on two machines. On
the first he finishes a round and Claude asks whether to write. The
reflection before the write repeats the state of the remote from the
last look: behind. Claude recommends `/pull my-project` first. The
repository is clean and behind, so the pull fast-forwards it, and the
round is written.

He runs `/save my-project`. The light check runs, Claude drafts the
message from the records, he confirms it, and the script commits and
pushes on the branch checked out. Seconds, no render.

The next day, on the second machine, he had saved a round of his own
before pulling. Back on the first machine the state map ends with:
diverged. He runs `/save my-project`. The script commits his work and
rebases his own commits onto the remote's; one artefact conflicts,
and the save leaves the rebase standing, prints the file in conflict
and the step that follows. Claude lays out the two sides as a
walkthrough, one question for the one conflict; the principal picks
a wording; Claude writes it into the file and a record into the
artefact's history. The staging of the file and the continuing of
the rebase arrive as the hook's ask, he says yes, and `/save
my-project` pushes the clean repository.

Along the way Claude once reaches for a push typed directly. The hook
denies it and names `scripts/forge-save.py` as the door; nothing is
written to git. Looking at the log directly, by contrast, is allowed,
because it changes nothing.

At the end of the week he runs `/release my-project` on `main`. The
repository is up to date with its origin, so the release goes on: its
checks with their walkthrough, the documentation offered and made,
the README and release notes, the state render, and the closing save
with the message `release 3.0` and the tag `v3`, since the intent is
at an approved major. The closing save runs no second light check.

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
- [The tests](the-tests.md): the tests that make the portability rule
  a run.
- [Scripts](../reference/scripts.md): the scripts themselves.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
