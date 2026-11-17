---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 4ba5f8a9f85ae9e7
inputs:
  - CLAUDE.md#Persistence (git)
  - CLAUDE.md#What this workspace is
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
  - projects/forge/40-solution-design.md#SOL.0530
  - projects/forge/40-solution-design.md#SOL.0740
  - projects/forge/10-intent.md#REJ.0160
  - projects/forge/10-intent.md#REJ.0170
---

# Persistence in git

Persistence in git is the way Forge of Thought (the forge) keeps its
work: the engine and every project are git repositories, and Claude
writes to git only through the scripts in `scripts/`. This page
explains that rule and the hook that holds it, the two commands that
save and release, the command that pulls, and what git is not asked
to do. It is for whoever uses the forge, extends it or evaluates it.

## What it is

The [engine](../reference/glossary.md) (the forge itself, apart from
the projects worked in it) is one git repository with a remote. Every
project under `projects/` is a repository of its own. `main` is the
released line. Branches are voluntary and left to git.

On top of git the forge sets four things:

- **One door for a write.** Every write of git that Claude makes
  goes through a script in `scripts/`: the scripts are the door to a
  write of git. Reading git directly is open.
- **A hook that holds the line.** A hook (a script that runs before
  a command of Claude's is carried out) judges every command of git.
  It allows a reading command, denies a write and names the script
  to use instead.
- **Two doors, two speeds.** `/save` commits and pushes in seconds,
  on any branch. `/release` runs from `main` only, with its checks
  and its renders.
- **The door inward.** `/pull` brings in what the remote holds. The
  forge looks at the remote and offers. The principal (the person
  whose thinking is forged) decides.

Three things stand apart from this:

- The [ledger](the-ledger.md) (the state of a project, built from
  its documents whenever it is read): it is not in git at all.
- The commit identity: it is git's business, resolved by the
  principal's own git configuration.
- The immutability of a document: it is a process rule, not a
  mechanism of git.

## How it works

### The door and the hook

Every command of git that changes a repository, a remote or a
configuration is a write. Claude sends no write to git directly, with
the one exception named below: it runs the script that does the
write. A commit and a push, for example, are made by
`scripts/forge-save.py` (the script behind `/save`). How many scripts
there are is not a rule: there are as many as the door needs.
[Scripts](../reference/scripts.md) lists them.

Reading git directly is open to Claude.

The line between reading and writing is held by a hook of the
harness. The harness is Claude Code, the agent the forge runs in: the
engine's settings (`.claude/settings.json`) configure its hooks and
its permission rules. This hook, `scripts/hook-git.py`, runs before
every command Claude sends through its shell tool. It judges each
part of the command that calls git and gives one of three answers.

| What Claude sends | The hook's answer | What follows |
|---|---|---|
| a command of git that only reads | allow | the command runs and nothing is asked |
| one of the few commands that finish [the step of a conflict](../use/settle-a-conflict.md), such as `rebase --continue` | ask | the harness puts the command to the principal, and it runs on the principal's yes |
| any other command of git: a write, or a command the hook cannot read | deny | nothing runs; the reason names the rule and, where one exists, the script to use instead |
| a command that is not git | none | the command is left to the harness |

Over a whole command the stricter answer wins: deny outranks ask, and
ask outranks allow. The ask holds in every permission mode of the
harness. The hook itself reads no file and writes nothing.

Claude has a second shell tool. The other shell tool is closed to git
whole, by a permission rule of the same settings. One reader then
judges every command of git, and there is one door.

The rule binds the forge, not the principal. The hook is for Claude's
tools alone. What the principal types to git in the principal's own
shell is left to the principal.

### What a commit carries

A commit carries the message the principal confirmed, word for word.
It carries no attribution line. In the settings, `attribution.commit`
is empty and `attribution.sessionUrl` is false. With these two the
harness adds and proposes no `Co-Authored-By` or `Claude-Session`
trailer.

### Two doors, two speeds

Saving and releasing are two commands.
[Save your work](../use/save-your-work.md) and
[Release a version](../use/release-a-version.md) describe the two
jobs.

| | `/save` | `/release` |
|---|---|---|
| Where it runs | on whatever branch is checked out | on `main` only; elsewhere it refuses and names the branch |
| What it checks | the [light check](../reference/glossary.md) | its checks, their findings settled in a walkthrough |
| The tests of the engine | never: every push runs them in CI | first, at a release of the engine; a red test stops the release |
| Renders | none | the README and the release notes |
| The commit | the message the principal confirmed | the message `release <intent version>` and, at an approved major, the tag `v<major>` |
| What it costs | seconds | the renders cost minutes and tokens |

A render is a file generated from the documents of a project, such as
the README. A walkthrough takes the items one at a time, one question
each, and the principal decides. CI is the automated run of the tests
that follows a push.

A release runs in one order:

1. At a release of the engine, the tests. A red test stops the
   release. Where the tests cannot run, the release says so and goes
   on only on the principal's word.
2. The checks, with the walkthrough of their findings.
3. The documentation. The release never regenerates it: it reports
   the age of the documentation's index against the intent's version
   and offers `/document`.
4. The README and the release notes, rendered at every release with
   no test of staleness.
5. The state render: the ledger written out as a file by the ledger
   script.
6. The save. `/release` ends by running `/save` with the release
   message and the tag: it is not a second procedure. This closing
   save runs without a second light check, which the release has run
   already.

The release number is the version of the project's
[intent](../reference/glossary.md). Only the tag of a major has a
fixed name: an integer is a released major, and any other tag is a
snapshot made on request.

In the commands of git, the word `forge` names the whole: the engine
and the forge's own project where it is cloned beside the engine,
each with a commit of its own
([Projects and the engine](projects-and-the-engine.md)).

### The door inward

`/pull` is the door inward
([Pull from the remote](../use/pull-from-the-remote.md)). The forge
looks at the remote and offers. It never pulls or merges on its own.

`/pull` and the state map that `/forge` draws ask the status script
(`scripts/forge-status.py --remote`) for the state of the engine and
of the project against the origin. They say that state as a fact. A
state that calls for something has one offer.

| State against the origin | The one offer |
|---|---|
| behind, the repository clean | `/pull` |
| behind, with unsaved work | `/save` first |
| ahead | `/save` |
| diverged | the principal merges the remote's `main` by hand, or lets `/save` rebase the principal's own commits onto the remote; nothing is pulled until then |

`/pull` therefore pulls only a clean repository that is behind.

Beside the state of the branch, both say what waits on GitHub outside
git, that is the open pull requests and the unanswered discussions,
which the forge reads and never merges, answers or closes.

### Branches and merging

A branch is voluntary and belongs to git
([Work on a branch](../use/work-on-a-branch.md)). Switching to one
goes through a script (`scripts/forge-branch.py`), as every write
does.

Merging belongs to git, by hand or by merge request. The integrator
(whoever does the merging) merges on the integrator's own clone with
git itself, outside the forge's scripts. The forge does one rebase:
the rebase of `/save`, which puts the principal's own commits onto
the remote.

What git leaves standing is settled in the step of a conflict. A
conflict that the rebase of a save meets is left standing, not
aborted: the commit is made and nothing is lost. The principal is
told which files are in conflict and what follows, and the status
script reports that a rebase or a merge is in progress. A save that
finds a rebase or a merge already standing refuses before it stages
anything. That way conflict markers are never committed.

The step of a conflict is the forge's help, not its mechanism. Claude
reads both sides and lays them out as a walkthrough, one conflict per
question. The principal decides. Claude writes the chosen wording
into the file and records the change in the history of the document.
The commands of git that finish the step then run on the hook's ask,
and `/save` runs again.

Every file of a project has a way of merging, one of three, set out
in [Working together on one project](working-together.md).

### Derived files and the driver `ours`

The files made for a reader (the README among them) are derived
files: a command makes them from other files. They are made only on
`main`. At a merge they are taken as `ours`: one side's file is taken
whole, and no conflict arises.

Whatever makes a derived file or migrates a project (`/release`,
`/publish`, `/document`, `/migrate`) runs on `main` only. It refuses
a repository that is behind or diverged from its origin, and offers
`/pull`.

`ours` is a merge driver that is not built into git. `/setup`
registers it in the global git configuration through
`scripts/forge-config.py --register`, on the principal's word, once
per machine and once in each place where git reads another global
file. The registration carries the settings the driver needs:

- `merge.ours.driver true`: the driver itself.
- `rebase.backend merge`: the other backend of a rebase ignores
  drivers.
- `merge.renormalize true`: without it, files committed with CRLF
  line endings before normalisation would conflict whole.

The same step sets `rerere.enabled true` as a convenience and offers
`merge.conflictStyle zdiff3`. The status script
(`scripts/forge-status.py`) reports a missing registration.

### The ledger, the identity and immutability

**The ledger.** The ledger is made at read time: it is built from the
documents whenever it is read, and it is not kept in git. The price
is that the ledger is not on the remote.

**The commit identity.** The identity of a commit is git's business,
not the forge's. It is resolved per git host by the principal's own
git configuration, and the forge sets no identity anywhere. The
scripts carry no address of a remote and no identity of an author. No
remote is configured anywhere in the forge: git carries that
information itself. What the forge keeps is an offer and a guard.
`/setup` offers to write the configuration together with one global
guard: with it, a commit in a repository on a host with no identity
fails aloud instead of silently taking a default. A save checks that
git resolves an identity for the repository. Where git resolves none,
the save reports it with the command that sets one, and commits
nothing until one is set. One case is accepted as a risk: where one
host serves two identities, the principal resolves it by hand.

**Immutability.** A document that is immutable is so by a rule of the
process, kept by convention. Git is not asked to enforce it.

### Where the scripts run

The forge runs beyond Windows. `scripts/` is the only layer bound to
a platform, and its scripts are written to run unchanged on Linux and
macOS. They are Python (3.8 or newer), run as
`python scripts/<name>.py`. `python` on PATH is their one
prerequisite. A system that has only `python3` gives it that name.
Each script carries its help at its head, and what several scripts
share lives in one module beside them.

That nothing in them is Windows-only is a writing rule:

- paths are composed with `pathlib`;
- external tools are resolved from PATH;
- the usage examples in a script's help are free of Windows-specific
  paths and invocations.

How far a run has verified the rule differs by platform and by part:

- On Linux and Windows the engine's tests run in CI at every push
  (the matrix: `.github/workflows/tests.yml`). The git scripts, the
  ledger, the light check and the judgement of the git hook are
  among what they cover.
- The conversions of documents are tested only for how they fail
  where their tool is missing.
- The per-prompt hook (the script the harness runs at every prompt,
  `scripts/hook-walkthrough.py`) stays a writing rule until a run
  says otherwise.
- Nothing has run on macOS. For macOS the whole set is the writing
  rule alone.

What the tests are and how they are run is said in
[The tests](the-tests.md).

## Why

**Reading is open, a write goes through the door.** Reading changes
nothing, and to serve reading the scripts had to copy git verb by
verb. A write changes a repository, and it goes through a script. Why
a write must go through a script at all, beyond that contrast: the
reason is not recorded.

**A hook, not conduct alone.** A rule of conduct discourages a write
outside the scripts. The hook refuses it, on every way Claude can
reach git, and there is one door.

**A hook, not deny rules.** Two shapes of deny rule in the settings
were weighed against the hook: one rule on every command of git, and
rules on the writing commands. A deny rule matches the beginning of a
command as it is usually typed, and the same write spelled another
way passes it. A deny rule cannot be carved by an allow rule and is
not overridden by a hook. Two barriers with one gap read worse than
one. The hook has a cost: its reading of the shell is a heuristic.
What it cannot read, it therefore denies.

**One shell tool judged, the other closed.** With the other shell
tool closed to git whole there is one parser and one door.

**No attribution line.** The reason is not recorded.

**Two commands.** The renders cost minutes and tokens beyond reason
at every save. With the renders at the release only, the README on
`main` is current at every release. Between releases it is stale
visibly (the state map shows it) and never silently. Two other shapes
were rejected:

- One command, in which `/save` regenerates only a render whose own
  inputs moved in that save and the ledger marks a render that was
  skipped. It would save perhaps a third of the engine's saves and
  nothing on projects, where the README reads the ledger and the
  ledger moves at every operation. It would add a state of staleness
  that `/save`, `/forge` and `/check` must all read alike. Two
  commands save everything and add nothing.
- A fixed working branch in every repository, with one script that
  creates it and switches to it, and `/release` merging it into
  `main`. It was rejected as the first step towards a wrapper of git,
  which is not wanted: the logic of merges and conflicts in the
  forge's hands, and two branches a non-developer must understand. It
  would also force a branch on those who do not need one. The
  switching half survives as the voluntary branch script. The merging
  half stays with git.

**The order of a release.** The README reads the documentation's
index. The documentation therefore comes before the README. The
renders come after the checks and their walkthrough: a render made
from the settled sources is current by construction, and a render
made before them goes stale whenever a finding raises the intent's
version. The closing save leaves the light check out: the release has
run it already. A save never runs the tests: every push runs them in
CI.

**Looking and offering, never pulling or merging unasked.** The
principal works on more than one machine. A clone behind its origin
is therefore the normal case, and a state map drawn from it shows the
wrong state. A pull or a merge made on Claude's judgement would be
work done without the principal's word.

**Saying what waits on GitHub.** A contribution seen on the morning
it arrives costs nothing. The same contribution seen after a week of
one's own rounds costs renumbered items, re-dated versions and a
conflict at the merge.

**Merging left to git.** The reason is the one of the rejected
working branch above: the forge is not to become a wrapper of git.

**Derived files on `main` only, and the refusals.** In the rebase of
a save `ours` turns round: the two sides change places. A fresh
README would then silently lose to an older one, and the tag of a
major would mark a wrong state.

**The registration, and the report where it is missing.** An
unregistered clone silently falls back to a conflict on the derived
files. The registration is one per machine, chosen against a
registration per repository, which the migration of a project must
not touch.

**The ledger out of git.** Every operation writes the ledger. It was
therefore the one file present at every collision of two people or
two windows on one project. Made at read time, it stops existing as a
thing to merge, and merge requests on the server stop conflicting on
it ([The ledger, made from the records](the-ledger.md)).

**The identity left to git.** An identity kept by the forge would
duplicate what the principal's own configuration already resolves,
and every repository would carry the same identity twice.

**Immutability as a process rule.** Git protects nothing from a
commit that rewrites a file. The rule costs nothing. A mechanism
would be one more layer to maintain, and it still would not stop an
edit by hand.

**Python, and a run instead of a claim.** The scripts need the same
Python that the conversion of documents needed already. Portability
is verified by a run. Where no run has been made, the rule stays a
writing rule and is not a claim.

## A worked example

A principal works on a project with the placeholder slug
`my-project`, on `main`.

1. **A look.** The principal asks what changed since the last save.
   Claude reads the state and the log of the repository from git
   directly. The hook answers allow, and nothing is asked.
2. **A save.** A round of work is written, and the principal asks for
   a save. `/save my-project` runs the light check. Claude drafts the
   message from the records of what changed, and the principal
   confirms it. `scripts/forge-save.py` commits with that message,
   word for word and with no attribution line, and pushes. Had Claude
   sent the commit to git itself, the hook would have answered deny,
   and its reason would have named the rule and the script of
   `/save`.
3. **A pull.** The next morning, on another machine, the principal
   types `/pull my-project`. The forge looks at the remote: the
   repository is behind and clean, and one pull request waits on
   GitHub. The forge says both, and pulls.
4. **A conflict.** Later a colleague pushes to the same repository
   while the principal works on. The next save finds the repository
   diverged, rebases the principal's commits onto the remote and
   meets a conflict in one document. The save leaves the rebase
   standing, with the commit made, and names the file. Claude lays
   the two wordings out, the principal chooses, and Claude writes the
   chosen wording into the file. The commands that finish the step
   (`rebase --continue` among them) each get the hook's ask: the
   harness shows the command and runs it on the principal's yes.
   `/save my-project` runs again and pushes.
5. **A release.** The principal types `/release my-project`. The
   repository is on `main` and up to date, and the release runs. No
   tests run: the project is not the engine. The checks run and their
   findings are settled in a walkthrough. The release reports the age
   of the documentation and offers `/document`. The README and the
   release notes are rendered. The closing save commits with the
   message `release 0.4` (0.4 being the version of the project's
   intent in this example) and runs no second light check. Had the
   repository been behind or diverged, the release would have refused
   and offered `/pull`.

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

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
