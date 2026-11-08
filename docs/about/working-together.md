---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 89ab4a3d38876d71
inputs:
  - CLAUDE.md#Persistence (git)
  - templates/gitattributes
  - projects/forge/10-intent.md#POS.1560
  - projects/forge/10-intent.md#POS.1690
  - projects/forge/10-intent.md#POS.1700
  - projects/forge/10-intent.md#POS.1750
  - projects/forge/10-intent.md#POS.1770
  - projects/forge/10-intent.md#POS.1790
  - projects/forge/10-intent.md#REJ.0280
  - projects/forge/10-intent.md#REJ.0340
  - projects/forge/10-intent.md#REJ.0350
---

# Working together on one project

Working together on one project is what happens when two people, or
two branches of one person, change the same project repository and
their changes have to be joined. This page says what the forge
promises in that case, how every kind of file of a project merges,
and why the forge leaves the merge itself to git. It is for the user
who shares a project, for the extender who adds a kind of file and
must say how it merges, and for the evaluator who wants to know
where a conflict can arise and where it cannot.

## What it is

Every file of a project has one of three ways of merging. The forge
tells git which way through the project's `.gitattributes`, a file
created from a template of the engine. The forge itself never
merges, pulls or rebases on its own judgement.

The first way is text. These files are merged by git's text merge,
and what git leaves in conflict is settled by a person:

- the artefacts (the documents of the chain)
- the recipes
- the work specifications
- the threads (one file per open matter of the intent)
- the project file
- the record files, that is the histories, the decisions, the
  resource indexes and the documentation map

The second way is derived. A derived file is made from other files
and is never the thing to merge. The ledger (the single source of
truth for the state of a project) is never in git and is made at
read time. The documents made for a reader are in git, made only on
`main`, taken as `ours` at a merge and made again afterwards:

- the renders
- the README
- the release notes
- CONTRIBUTING
- the documentation
- the state render
- the published companions

The published files themselves, the `.pptx` and `.docx` made
through a model, are `binary` and are never merged.

The third way is immutable and unique. These files never conflict,
and a report's name is unique across branches too:

- reviews
- challenges
- research
- sources
- closed threads

Immutability stays a process rule, not a git mechanism: nothing is
locked.

## How it works

### The attributes

The template of the attributes, `templates/gitattributes`, carries
three things. `text=auto` on every file normalises the line endings.
Because files would otherwise fight between machines. `merge=ours`
stands on the renders, the documentation, the state render and the
published companions. `binary` stands on the published files. The
record files carry no attribute and merge as text.

The three root files, `README.md`, `RELEASE-NOTES.md` and
`CONTRIBUTING.md`, are anchored with a leading slash in the
attributes. Because a bare name matches at every depth. Where the
file system ignores case, a bare name matches in every case too, and
`recipes/readme.md` would be taken as `ours` at a merge.

`/new-project` creates the file, and `/check project` reports a
project without it. The engine carries a list of its own. Because
its derived files lie at its root and under its own project.

The driver `ours` is not built into git. `/setup` registers it in
the global configuration once for every repository of the machine,
together with the git settings it needs, and the status report says
when the registration is missing. Because an unregistered clone
silently falls back to a conflict.

### What the forge promises

One person on one project saves and pulls, through `/save` and
`/pull`, with nothing more to think of.

With two people, or two branches, the forge promises this:

- Derived state is made anew at read time and never conflicts.
- A conflict in a history, in `decisions.md` or in an index is two
  tails appended after one last line, and is settled by keeping both.
- A conflict in an artefact is the same item or sentence changed on
  both sides, and is settled by a person with Claude's help in the
  step of a conflict ([Settle a conflict](../use/settle-a-conflict.md)).
- IDs stay one sequence per project, taken at the write, with no
  block and no reading over the branches. A number taken twice is
  reported by the ledger script after the merge and settled then, the
  younger renumbered with a record in a walkthrough (one item per
  message, the principal's verdict on each), never by Claude alone
  ([Stable IDs](stable-ids.md)).
- A version given twice, two branches that both raised one document
  to the same number, is found by git itself. Both sides appended
  their records to the end of the document's history, and that
  conflicts as text whenever both raised it. The header's `version:`
  line conflicts only where the two numbers differ and merges
  silently where they are the same. It is settled in the same step of
  a conflict: the merged document takes the next number and one
  `changed` record naming the merge and what was joined, the records
  of both sides keeping their numbers.
- A merge request without conflict is merged on the server. With a
  conflict it is fetched and settled on a clone. Because the server
  merges with no attribute of the forge's.

Two windows of one person on one project are not solved by the
forge. A bare `/save` commits every repository with changes, the
other window's half-written work included, so two windows take a
slug. On two projects the windows collide nowhere, each project
being a repository of its own. On one project the person either does
work the two windows can merge afterwards, or arranges it through
git: a branch, or a second clone where a branch in one tree is not
enough. Because a branch switched in one working tree is seen by
both windows.

### Several people: one integrator and contributors

A hosted project's `main` is protected by default, so pushing to it
and merging into it are the maintainers'. The work of several people
on one project therefore has one model. A contributor works on a
branch ([Work on a branch](../use/work-on-a-branch.md)) and saves it;
`/save` pushes the branch ([Save your work](../use/save-your-work.md)).
The integrator, a maintainer and typically the principal (the person
whose thinking is forged), merges it. Where the merge request has no
conflict, he merges it on the server. Where it has one, he merges on
his own clone with git itself, outside the forge's scripts, and what
git leaves standing is settled in the step of a conflict. A merge
request on the server is for reading and for the merge that needs no
hand. A second author never writes into the integrator's clone.

The step of a conflict is the forge's help, not its mechanism. A
conflict `/save` meets is left standing, not aborted. Claude reads
both sides and lays them out as a walkthrough, the principal decides,
Claude writes the chosen wording into the file, and the finishing
commands of git run on the hook's ask. The hook is the wall between
reading git and writing it; the scripts are the door to a write, and
the few commands that finish a conflict are put to the principal and
run on his yes.

The save rebases one's own commits onto the remote only where both
sides moved on, that is where the histories diverged. A branch
merely ahead of the remote, a merge commit among its commits, is
pushed as it stands. So that the integrator's merge of a branch and a
contributor's merge of the upstream keep their merge commit and
nothing of the other side is replayed.

The renders of a release, the documentation, the state render and the
published files are made only on `main`
([Persistence in git](persistence-in-git.md)). Two branches making
the same one conflict on the server and are settled by making it
again.

## Why

The ledger was the one file present at every collision, and beside
it stood the histories, the decisions, the index of sources and the
regenerated renders. Made at read time, the ledger stopped being a
thing to merge, and the threads as files of their own removed most of
the rest ([The ledger, made from the records](the-ledger.md)).

Two people on one project are the exception, and the exception is
handled with git. That is why the record files have no way of their
own: no driver of the forge's merging them as sets of records, and no
`merge=union`. The record files are text, and a conflict in them is
two tails kept both in the step of a conflict. A driver fails where
the merge happens on the server and for a contributor without the
registration, and it would be the most code of the plan for a case
of a few times a year. Union merge duplicates and does not order, by
git's own documentation.

There is no merge command of the forge either. The same help without
a new mechanism is the step of a conflict in `/save` and on the
hook's ask; the merge stays git's.

A number taken twice and a version given twice are found after the
merge and settled by the existing remedy, instead of being prevented
beforehand. Because a clash is a few times a year on a project of one
or two people, and detection with the existing remedy costs nothing,
where blocks of IDs, an allocation over the local branches and a
version taken as a landing would cost the most code.

The model of one integrator and contributors fits a forge built
around the principal and removes every need to write to `main` from
a branch. Because the default protection of a hosted `main` refuses a
push by everyone.

Why the forge leaves two windows of one person on one project to git
rather than solving it is not recorded. The direction is recorded:
where two windows meet is to be mapped from what each operation
writes, and when it comes to it the answer is git's.

## A worked example

A contributor and the integrator share the project `<slug>`.

The contributor switches the project to a branch of her own and works
there: she changes one position of the intent, adds a record to the
intent's history and raises the intent's version. Her `/save` commits
and pushes the branch. Nothing is rebased. Because only her side has
moved on.

Meanwhile the integrator, on `main`, has changed another position of
the intent, added a record to the same history and raised the intent
to the same version number.

The contributor opens a merge request. The server tries the merge and
finds a conflict: both sides appended a record to the end of the
intent's history. The integrator therefore fetches the branch and
merges on his own clone with git itself. Git joins the two positions
of the intent by its text merge, since they are different items. The
`version:` line of the intent merges silently, both sides having
written the same number. The history is left standing in conflict,
two tails after one last line. `README.md` and the renders are taken
as `ours`.

Claude lays the conflict out as a walkthrough. The integrator keeps
both tails. For the version given twice, the merged intent takes the
next number, and one `changed` record naming the merge and what was
joined is appended; the records of both sides keep their numbers.
Claude writes the wording, and the finishing commands of git run on
the hook's ask. If both sides had opened a thread with the same
number, the ledger script would report it after the merge, and the
younger thread would be renumbered with a record.

The integrator's `/save` pushes `main` as it stands, merge commit
included. Because the branch is merely ahead of the remote. The
README and the release notes are made again at the next release on
`main`, and the ledger, never in git, is made at the next read.

## See also

- [Settle a conflict](../use/settle-a-conflict.md): the step of a
  conflict, done.
- [Persistence in git](persistence-in-git.md): the doors to git and
  why the files for a reader are made on `main` only.
- [Work on a branch](../use/work-on-a-branch.md): switching a
  repository to a branch.
- [Save your work](../use/save-your-work.md): the save, which pushes a
  merge made by hand as it stands.
- [The ledger, made from the records](the-ledger.md): why the ledger
  is made at read time.
- [Stable IDs](stable-ids.md): how an item number taken twice is
  settled.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
