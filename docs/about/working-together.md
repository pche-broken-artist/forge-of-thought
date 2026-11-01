---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 34d67eeb96be5c68
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

Working together on one project means two people, or two branches,
changing the same project repository and joining their work with a
git merge. This page explains what the forge promises in that case,
how each kind of file of a project merges, and why it is built that
way. It is for anyone who shares a project, extends the forge or
weighs whether it fits a team.

## What it is

Every file of a project has one of three ways of merging. The forge
tells git which way each file takes through the project's
`.gitattributes` file. The forge itself never merges, pulls or
rebases on its own judgement. The merge belongs to git.

The three ways:

- **Text.** The artefacts (the documents of the chain, see the
  [Glossary](../reference/glossary.md)), the recipes, the work
  specifications, the threads (one open matter of the intent each,
  one file each) and the project file. The record files take this
  way too: the histories, the decisions, the resource indexes and
  the documentation map. Git merges them as text. What git leaves in
  conflict is settled by a person in the step of a conflict (see
  [Settle a conflict](../use/settle-a-conflict.md)).
- **Derived.** The ledger is the single source of truth for state.
  It is never in git and is made at read time from the documents
  (see [The ledger, made from the records](the-ledger.md)), so there
  is nothing to merge. The documents for a reader are in git:
  the renders, the README, the release notes, CONTRIBUTING, the
  documentation, the state render and the published companions. They
  are made only on `main`, taken as `ours` at a merge and made again.
  The published files themselves are marked binary and never merged.
- **Immutable and unique.** Reviews, challenges, research, sources
  and closed threads. They are never edited after they are written,
  so they never conflict. A report's name is unique across branches
  too. Immutability is a rule of the process: nothing is locked.

## How it works

### The attributes file

Every project carries a `.gitattributes` made from the engine's
template `templates/gitattributes`. `/new-project` creates it, and
`/check project` reports a project without it. The template carries:

| Path | Attribute | Meaning |
|---|---|---|
| `*` | `text=auto` | line endings normalised, so that files do not fight between machines |
| `renders/**` | `merge=ours` | the renders, the state render among them |
| `README.md` | `merge=ours` | the README |
| `RELEASE-NOTES.md` | `merge=ours` | the release notes |
| `CONTRIBUTING.md` | `merge=ours` | CONTRIBUTING |
| `docs/**` | `merge=ours` | the documentation |
| `published/*.md` | `merge=ours` | the published companions |
| `published/*.pptx` | `binary` | a published PowerPoint file, never merged |
| `published/*.docx` | `binary` | a published Word file, never merged |

The record files carry no attribute and merge as text. The engine
carries a list of its own, because its derived files lie at its root
and under `projects/forge/`.

`ours` is not built into git. `/setup` registers it once per machine
in the user's global git configuration, through
`scripts/forge-config.py`, on the user's word. `forge-status` says
when the registration is missing. This matters because a clone
without the registration silently falls back to a conflict.

### What the forge promises

With one person on one project, the person saves with `/save` and
brings in changes with `/pull`.

With two people, or two branches:

- **Derived state never conflicts.** The ledger is made anew at read
  time.
- **A conflict in a record file is two tails.** Both sides appended
  records after the same last line. It is settled by keeping both.
- **A conflict in an artefact is the same item or sentence changed
  on both sides.** It is settled by a person with Claude's help, in
  the step of a conflict.
- **IDs stay one sequence per project.** A number is taken at the
  write, as always, with no blocks reserved and no reading over the
  branches. Two branches that took the same number are reported by
  the ledger script after the merge. The younger item is then
  renumbered, with a record, as [Stable IDs](stable-ids.md)
  describes. That happens in a walkthrough (one item per message,
  each closed with a verdict of the principal, the person whose
  thinking the project forges and who has the final word on its
  content), never by Claude alone.
- **A version given twice is settled by whoever merges.** This is
  the case where two branches both raised one document to the same
  version number. The merged document takes the next number and one
  `changed` record that names the merge and what was joined. The
  records of both sides keep their numbers.

Git itself finds a version given twice. Both sides appended their
records to the end of the document's history, and that conflicts as
text whenever both raised the version. The header's `version:` line
conflicts only where the two numbers differ. Where they are the
same, that line merges silently. Either way it is settled in the
step of a conflict.

### The step of a conflict

The step of a conflict is Claude's help, not a mechanism of its own.
A conflict that `forge-save` meets is left standing, not aborted, and
the commit is kept. Then:

1. Claude reads both sides and lays them out as a walkthrough, one
   conflict one question.
2. The principal decides.
3. Claude writes the chosen wording into the file.
4. The git commands that finish the step run on the ask of the hook
   `scripts/hook-git.py` (a check that stands between Claude and
   every write to git), each on the principal's yes.
5. `/save` runs again.

### Several people: one integrator, several contributors

A hosted project's `main` is protected by default: push and merge
belong to its maintainers. The work of several people on one project
therefore follows one model:

- **A contributor** works on a branch (see
  [Work on a branch](../use/work-on-a-branch.md)) and saves it.
  `/save` pushes the branch.
- **The integrator** is a maintainer and typically the principal. The
  integrator merges the branch.
  - Where the merge request has no conflict, the integrator merges it
    on the server.
  - Where it has a conflict, the integrator fetches it and merges it
    on his own clone, through the step of a conflict.

The server merges with no attribute of the forge's. Two people who
both appended to a history or to the decisions therefore have a
conflicting merge request there. A merge request on the server is
for reading and for the merge that needs no hand.

The documents for a reader are made only on `main`. Two branches
that made the same one conflict on the server. They are settled by
making that document again on `main`.

### Two windows of one person

Two windows of one person on one project are not solved by the
forge. A bare `/save` commits every repository with changes, so it
also takes the other window's half-written work. On two different
projects the windows never collide, because each project is a
repository of its own. On one project the person either does work
the two windows can merge afterwards, or arranges it through git. A
branch is one answer. A second clone is the answer where a branch is
not enough, because a branch switched in one working tree is seen by
both windows.

## Why

**The ledger was the one file present at every collision.** At the
merges the forge looked at, the ledger was the one file changed on
both sides. Beside it stood the histories, the decisions, the index
of sources and the regenerated renders. Made at read time and kept
out of git, the ledger stopped being a thing to merge. Keeping the
threads as files of their own removed most of the rest.

**Two people on one project are the exception.** The exception is
handled with git, not with machinery of the forge's own.

**No merge driver of the forge's own for the record files.** A
driver that merged the record files as sets of records was let go
for three reasons:

- It fails where the merge happens on the server.
- It fails for a contributor whose machine lacks the registration.
- It would be the most code of all for a case that arises a few
  times a year.

**No union merge.** Git's `merge=union` duplicates lines and does
not order them, by git's own documentation. The record files merge
as text instead, and a conflict in them is two tails kept both.

**No merge command of the forge.** The same help, without a new
mechanism, is the step of a conflict in `/save` and on the hook's
ask. The merge stays with git.

**Detection rather than reservation for IDs and versions.** A clash
comes a few times a year on a project of one or two people.
Detection with the existing remedy costs nothing.

**One integrator.** The model removes every need to write to `main`
from a branch, which the default protection of a hosted repository
refuses. It is also consistent with a forge built around the
principal.

**Derived files on `main` only.** `merge=ours` turns round in the
rebase that `/save` runs. A fresh README would silently lose to an
older one. So everything that makes a derived file refuses a
repository behind or diverged from its origin (see
[Persistence in git](persistence-in-git.md)).

## A worked example

A contributor and the integrator share the project `<slug>`.

1. The contributor switches to the branch `scope-review`, adds a
   position to `10-intent.md`, raises its version from 0.4 to 0.5
   and appends a record to `10-intent.history.md`. `/save` commits
   and pushes the branch. The contributor opens a merge request.
2. Meanwhile the integrator, on `main`, also raised `10-intent.md`
   to 0.5 and appended a record to its history.
3. On the server the merge request shows a conflict in
   `10-intent.history.md`: both sides appended after the same last
   line. The server knows no attribute of the forge's, so the
   integrator fetches the branch and merges it on his own clone.
4. Git leaves the history in conflict. The `version:` line merged
   silently, because both sides wrote 0.5. Claude lays out the
   conflict as a walkthrough. The integrator keeps both tails.
5. Because the version was given twice, the merged `10-intent.md`
   takes 0.6, with one `changed` record naming the merge and what
   was joined. The records of both sides keep their 0.5.
6. Had both sides changed the same sentence of the intent, that
   sentence would be a second question of the same walkthrough.
7. Any README or render that both sides touched is taken as `ours`
   and made again on `main`. The ledger is made at read time. If both
   sides took the same item number, the ledger script reports it,
   and the younger item is renumbered in a walkthrough.
8. The finishing git commands run on the hook's ask, and the
   integrator runs `/save`.

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

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
