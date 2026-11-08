---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: b0782bcd82ced7f3
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

Working together on one project means that two people, or two
branches of one person, change the same repository and git has to
bring the two sides together. This page says what the forge
promises in that case, how each kind of file of a project merges,
and how the work of several people on one project is arranged. It
is for the user who shares a project, for the extender who touches
the files that make it work, and for the evaluator who wants to
know where the forge ends and git begins.

## What it is

Every file of a project has one of three ways of merging. The forge
tells git which one through the project's `.gitattributes`, a file
created from the template `templates/gitattributes`. The forge
itself never merges, pulls or rebases on its own judgement: the
merge stays git's.

The three ways are these.

- **Text.** The artefacts, the recipes, the work specifications,
  the threads and the project file; the record files too, that is
  the histories, the decisions, the resource indexes and the
  documentation map. These carry no attribute and are merged by
  git's text merge. What git leaves in conflict is settled by a
  person in the step of a conflict ([Settle a
  conflict](../use/settle-a-conflict.md)).
- **Derived.** State and the documents for a reader. The
  [ledger](the-ledger.md), the single file that says where a
  project stands, is never in git and is made at read time. The
  documents for a reader (the renders, the README, the release
  notes, CONTRIBUTING, the documentation, the state render and the
  published companions) are in git, made only on `main`, taken as
  `ours` at a merge and made again. The published files themselves
  (`.pptx`, `.docx`) are marked `binary` and never merged.
- **Immutable and unique.** Reviews, challenges, research, sources
  and closed threads. These never conflict: a report's name is
  unique across branches too. Immutability stays a process rule,
  not a lock in git.

The attributes template carries `text=auto` for every file, so that
line endings do not fight between machines, `merge=ours` on
`renders/**`, `docs/**`, `published/*.md` and the three root files
`/README.md`, `/RELEASE-NOTES.md` and `/CONTRIBUTING.md`, and
`binary` on `published/*.pptx` and `published/*.docx`. The three
root files are anchored with a leading slash. A bare name would
match at every depth, `recipes/readme.md` among them. Where the
file system ignores case, a bare name would match in every case as
well.

`ours` is not built into git. `/setup` registers it, once per
machine and on the user's word, in the global git configuration,
with the settings it needs. The status report says when the
registration is missing, because an unregistered clone silently
falls back to a conflict.

## How it works

### What the forge promises

One person on one project saves and pulls, nothing more
([Save your work](../use/save-your-work.md)). With two people, or
two branches, the forge promises the following.

- Derived state never conflicts: it is made anew at read time.
- A conflict in a history, in `decisions.md` or in an index is two
  tails appended after one last line. It is settled by keeping
  both.
- A conflict in an artefact is the same item or sentence changed on
  both sides. It is settled by a person with Claude's help, in the
  step of a conflict.
- IDs stay one sequence per project, taken at the write, with no
  block and no reading over the branches. A number taken twice is
  reported by the ledger script after the merge and settled by
  renumbering the younger item with a record, in a walkthrough,
  that is one item per message with a verdict on each, never by
  Claude alone ([Stable IDs](stable-ids.md)).
- A version given twice, two branches that both raised a document
  to the same number, is found by git itself. Both sides appended
  their records to the end of the document's history, and the two
  tails conflict as text whenever both raised it. The header's
  `version:` line conflicts only where the two numbers differ and
  merges silently where they are the same. Whoever merges settles
  it in the step of a conflict: the merged document takes the next
  number and one `changed` record names the merge and what was
  joined, the records of both sides keeping their numbers.
- A merge request without conflict is merged on the server. A
  merge request with conflict is fetched and settled on a clone,
  because the server merges with no attribute of the forge's.

### Several people on one project

The work of several people on one project has one model: one
integrator and any number of contributors. A hosted project's
`main` is protected by default, so nobody pushes to it directly.

- A contributor works on a branch ([Work on a
  branch](../use/work-on-a-branch.md)) and saves it; `/save` pushes
  the branch.
- The integrator, typically the principal (the person whose
  thinking is being forged), merges it. Where the merge request has
  no conflict, the merge happens on the server. Where it has one,
  the integrator merges on his own clone with git itself, outside
  the forge's scripts, and settles what git leaves standing in the
  step of a conflict.
- A merge request on the server is for reading and for the merge
  that needs no hand.
- A second author never writes into the integrator's clone.

The server merges with no attribute of the forge's. Two people who
both append to any history or to the decisions therefore have a
conflicting merge request there, and the forge's path is the
branch, `/save`, the integrator's clone and the step of a conflict.

The save rebases one's own commits onto the remote only where both
sides moved on, that is where the histories diverged. A branch
merely ahead of the remote, a merge commit among its commits, is
pushed as it stands. So the integrator's merge of a branch and a
contributor's merge of the upstream keep their merge commit, and
nothing of the other side is replayed.

The renders of a release, the documentation, the state render and
the published files are made only on `main` ([Persistence in
git](persistence-in-git.md)). Two branches that make the same one
conflict on the server and are settled by making it again.

### Two windows of one person

Two windows of one person on two projects collide nowhere, each
project being a repository of its own. On one project the forge
solves nothing: the person either does work the two windows can
merge afterwards, or arranges it himself through git, with a
branch, or with a second clone where a branch in one working tree
is not enough, because a branch switched in one working tree is
seen by both windows. A bare `/save` is for one window, since it
commits every repository with changes, the other window's
half-written work included. Why two windows on one project are left
to git is not recorded.

## Why

The ledger was the one file present at every collision the forge
had seen, with the histories, the decisions, the index of sources
and the regenerated renders beside it. Made at read time, the
ledger stopped being a thing to merge, and the threads as files of
their own removed most of the rest.

Two people on one project are the exception, and the exception is
handled with git. For that reason the forge has no merge driver of
its own for the record files: a driver merging them as sets of
records fails where the merge happens on the server and for a
contributor without the registration, and it would have been the
most code of the plan for a case of a few times a year. `merge=union`
for the record files was let go with it: union duplicates and does
not order, by git's own documentation, and the record files merge
as text, a conflict in them two tails kept both. A merge command of
the forge with a script of its own was let go because the same help
needs no new mechanism: it is the step of a conflict in `/save` and
on the hook's ask, and the merge stays git's.

A number or a version taken twice is settled by detection and the
existing remedy, because a clash is a few times a year on a project
of one or two people and detection costs nothing, where blocks of
IDs, an allocation over the local branches and a version written as
a landing would have cost the most code.

The model of one integrator and contributors is consistent with a
forge built around the principal, and it removes every need to
write to `main` from a branch, which the default protection of a
hosted `main` refuses anyway.

## A worked example

A contributor and an integrator share the thought project
`<slug>`. The contributor creates a branch through `forge-branch`,
changes an item of the intent and records the change in the
intent's history, then runs `/save <slug>`: the save commits and
pushes the branch. Meanwhile the integrator, on `main`, has
recorded a change of his own in the same history.

The contributor opens a merge request. The server finds the two
tails of the intent's history in conflict and refuses to merge.
The integrator fetches the branch to his own clone and merges it
with git itself. The intent merges cleanly, since the two sides
changed different items. The history is left in conflict, two
tails after one last line. The renders and the README are taken as
`ours` by the attributes and will be made again on `main` at the
next release.

Claude lays the two tails out as a walkthrough in the step of a
conflict, the integrator keeps both, Claude writes the wording and
the finishing commands of git run on his yes. If both sides had
raised the intent to the same version, the merged intent would take
the next number with one `changed` record naming the merge. The
integrator then runs `/save <slug>`: `main` is merely ahead of the
remote, the merge commit among its commits, so the save pushes it
as it stands and replays nothing. The ledger, made at read time,
shows the merged state and reports an item number that both sides
had taken, if any, for the walkthrough that renumbers the younger.

## See also

- [Settle a conflict](../use/settle-a-conflict.md): the step of a
  conflict, done.
- [Persistence in git](persistence-in-git.md): the doors to git and
  why the files for a reader are made on `main` only.
- [Work on a branch](../use/work-on-a-branch.md): switching a
  repository to a branch.
- [Save your work](../use/save-your-work.md): the save, which pushes
  a merge made by hand as it stands.
- [The ledger, made from the records](the-ledger.md): why the
  ledger is made at read time.
- [Stable IDs](stable-ids.md): how an item number taken twice is
  settled.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
