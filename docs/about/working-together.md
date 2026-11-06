---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 8b6e089ebb382c81
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

Working together on one project is the case where two people, or two
branches of one person, change the same project and their work has to
be joined. This page explains what the forge promises for that case,
how every file of a project merges, and what is left to git and to the
people. It is written for the user who shares a project, for the
extender who adds a file and must know which way it merges, and for
the evaluator who wants to know where the forge's promise ends.

## What it is

Every file of a project has one of three ways of merging. The forge
tells git which way through a file in the project's root,
`.gitattributes`, made from a template of the engine
(`templates/gitattributes`). The forge itself never merges, pulls or
rebases on its own judgement: the merge is git's, and a person
settles what git cannot.

The first way is **text**. These files are merged by git as text, and
what git leaves in conflict is settled by a person:

- the artefacts: the documents of the chain, such as the brief and
  the intent
- the recipes: the files a render is made from
- the work specifications
- the threads: the open matters of the intent, one file each
- the project file
- the record files: the histories, the decisions, the resource
  indexes and the documentation map

The record files carry no attribute of their own. They merge as text
like the rest. A conflict in a record file has one shape: both sides
appended records after the same last line, so the conflict is two
tails, and it is settled by keeping both.

The second way is **derived**. These files are made from the others
and are never worth a merge:

- the ledger: the project's state report, made from the documents at
  read time, never in git
- the documents for a reader: the renders, the README, the release
  notes, CONTRIBUTING, the documentation, the state render and the
  published companions (the Markdown file beside a published file,
  carrying its provenance)

The documents for a reader are in git. They are made only on `main`,
taken as `ours` at a merge and made again. The published files
themselves, a `.pptx` or a `.docx`, are marked binary and are never
merged.

The third way is **immutable and unique**. These files are never
edited after they are made, and each carries a name no other branch
can take:

- the reviews and the challenges, whose names are completed by a
  script so that they stay unique across branches
- the research notes
- the sources
- the closed threads

Such a file never conflicts. Its immutability is a rule of the
process, not a mechanism of git: nothing is locked.

## How it works

### The attributes file

The template `templates/gitattributes` carries three kinds of entry.
`* text=auto` normalises line endings, so that files do not fight
between machines. `merge=ours` stands on `renders/**`, `README.md`,
`RELEASE-NOTES.md`, `CONTRIBUTING.md`, `docs/**` and
`published/*.md`. `binary` stands on `published/*.pptx` and
`published/*.docx`. Everything else merges as text. `/new-project`
creates the file in every new project, and `/check project` reports a
project without it. The engine carries a list of its own, because its
derived files lie at its root, `README.md`, `RELEASE-NOTES.md`,
`CONTRIBUTING.md` and `docs/`, and its renders and published
companions under `projects/forge/`.

`ours` is not built into git. `/setup` registers the merge driver
`ours`, with the git settings it needs, in the user's global
configuration, once per machine and on the user's word, through
`scripts/forge-config.py`. The status report (`forge-status`) says
when the registration is missing, because an unregistered clone
silently falls back to a conflict on every file that should have been
taken as `ours`.

### What the forge promises

One person on one project saves and pulls, through `/save` and
`/pull`, as always. The promise for two people, or two branches, is
this:

- Derived state never conflicts. The ledger is made anew at read time
  and is not in git; the documents for a reader are taken as `ours`
  and made again on `main`.
- A conflict in a history, in `decisions.md` or in a resource index
  is two tails appended after one last line, and it is settled by
  keeping both.
- A conflict in an artefact is the same item or sentence changed on
  both sides. It is settled by a person with Claude's help, in the
  step of a conflict ([Settle a conflict](../use/settle-a-conflict.md)).
- IDs stay one sequence per project, sequential, taken at the write
  as always, with no block and no reading over the branches. Two
  branches that took the same number are found after the merge by the
  script that makes the ledger. The clash is settled by renumbering
  the younger item with a record, in a walkthrough (the method by
  which items needing a decision are worked one per message), never
  by Claude alone ([Stable IDs](stable-ids.md)).
- A version given twice, when two branches both raised a document to
  the same number, is settled by whoever merges. The merged document
  takes the next number and one `changed` record naming the merge and
  what was joined; the records of both sides keep their numbers. Git
  itself finds the case: both sides appended their records to the end
  of the document's history, which conflicts as text whenever both
  raised it. The header's `version:` line conflicts only where the two
  numbers differ, and merges silently where they are the same, so the
  history, not the header, is the sign. It is settled in the same step
  of a conflict.

Two windows of one person on one project are not solved. The person
either does work the two windows can merge afterwards, or arranges it
through git, by a branch or by a second clone. A second clone is
needed where a branch in one working tree is not enough, because a
branch switched in one working tree is seen by both windows. On two
projects the windows collide nowhere, because each project is a
repository of its own. A bare `/save` is for one window only, since it
commits every repository with changes, the other window's half-written
work included.

### Several people: one integrator and contributors

The work of several people on one project has one stated model. A
contributor works on a branch and saves it; `/save` pushes the branch
([Work on a branch](../use/work-on-a-branch.md)). The integrator, a
maintainer of the hosted repository and typically the principal (the
person whose thinking is being forged), merges the branch. Where the
merge request has no conflict, it is merged on the server. Where it
has one, the integrator fetches it and settles it on his own clone,
with git itself, outside the forge's scripts, through the step of a
conflict. The server merges with no attribute of the forge's. So two
people who both append to any history or to the decisions have a
conflicting merge request there, and the forge's path for that case
is a branch, `/save`, the integrator's clone and the step of a
conflict. A merge request on the server is for reading and for the
merge that needs no hand.

A hosted project's `main` is protected by default: push and merge to
it belong to the maintainers. The model fits that default, and it
removes every need to write to `main` from a branch.

### Where the forge's own scripts stop

`forge-save` rebases a person's own linear commits. A branch carrying
a merge commit is merged by hand, because the forge has no door of its
own for it. A conflict `forge-save` meets is left standing, not
aborted: the commit is made and nothing is lost, and the conflict is
settled in the step of a conflict. In that step Claude lays both sides
out as a walkthrough, the principal decides, Claude writes the
wording, and the finishing commands of git run on the hook's ask. The
hook (`scripts/hook-git.py`) is the wall between reading git, which
is open, and writing it, which goes through the scripts of `scripts/`
([Persistence in git](persistence-in-git.md)).

The renders of a release, the documentation, the state render and the
published files are made only on `main`. Two branches that make the
same one conflict on the server, and the conflict is settled by
making the file again.

## Why

The ledger was the one file present at every collision the forge had
seen, beside it the histories, the decisions, the index of sources and
the regenerated renders. Made at read time and kept out of git, the
ledger stopped being a thing to merge, and the threads kept as files
removed most of the rest ([The ledger, made from the
records](the-ledger.md)).

Two people on one project are the exception, and the exception is
handled with git. For that reason the record files have no way of
merging of their own. A merge driver of the forge's that would join
the record files as sets of records was let go: it fails where the
merge happens on the server, and for a contributor without the
registration, and it would have been the most code of the plan for a
case that arises a few times a year. `merge=union` for the record
files was let go with it: by git's own documentation union duplicates
and does not order, and the record files merge well enough as text,
their conflict two tails kept both. A `/merge` command of the forge
with a script of its own was let go too, because the same help without
a new mechanism is the step of a conflict in `/save` and on the hook's
ask; the merge stays git's.

The IDs stay one sequence with detection after the merge, rather than
blocks per author or an allocation over the branches, because a clash
comes a few times a year on a project of one or two people, and
detection with the existing remedy costs nothing where the other
mechanisms would have cost the most code.

The integrator model, rather than a push to `main` by everyone, exists
because the default protection of a hosted `main` refuses such a push.
The model is consistent with a forge built around the principal, and
the engine's own project is the one place where several hands meet,
as on any open-source repository.

## A worked example

A project with the slug `<slug>` has two people: the principal, who
integrates, and a contributor. The contributor switches to a branch,
reworks one position of the intent, raises the intent from 2.3 to 2.4
and writes a record into `10-intent.history.md`; a review is filed in
`reviews/` under a name completed by the forge. `/save` commits and
pushes the branch.

Meanwhile the principal, on `main`, changes a different position of
the intent, raises it to 2.4 as well, appends his own record to the
history and releases: the README and the state render are made again
on `main`.

The contributor opens a merge request. The server reports a conflict,
since the history of the intent has two tails, and the server reads
none of the forge's attributes. The principal fetches the branch and
merges it on his own clone with git. What git leaves standing:

- `10-intent.md`: the two positions differ, so the text merges; the
  header's `version:` line says 2.4 on both sides and merges silently.
- `10-intent.history.md`: two tails after one last line, in conflict.
- `README.md` and `renders/state.md`: taken as `ours`, nothing to
  settle.
- `reviews/...`: a new file with a unique name, no conflict.

In the step of a conflict Claude lays the two tails out, the principal
decides, and both are kept. The two tails show that both sides raised
the intent to 2.4: the merged intent takes 2.5, and one `changed`
record names the merge and what was joined, the records of both sides
keeping their numbers. The finishing commands of git run on the hook's
ask. The README and the state render are made again at the next
release on `main`, and the ledger, made at read time, needs nothing.

## See also

- [Settle a conflict](../use/settle-a-conflict.md): the step of a
  conflict, done.
- [Persistence in git](persistence-in-git.md): the doors to git and
  why the files for a reader are made on `main` only.
- [Work on a branch](../use/work-on-a-branch.md): switching a
  repository to a branch.
- [The ledger, made from the records](the-ledger.md): why the ledger
  is made at read time.
- [Stable IDs](stable-ids.md): how an item number taken twice is
  settled.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
