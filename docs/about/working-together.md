---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 8cd11f59ec063291
inputs:
  - CLAUDE.md#Persistence (git)
  - templates/gitattributes
  - projects/forge/10-intent.md#POS.1560
  - projects/forge/10-intent.md#POS.1690
  - projects/forge/10-intent.md#POS.1700
  - projects/forge/10-intent.md#POS.1750
  - projects/forge/10-intent.md#POS.1770
  - projects/forge/10-intent.md#POS.1790
  - projects/forge/40-solution-design.md#SOL.0730
  - projects/forge/40-solution-design.md#SOL.0780
  - projects/forge/40-solution-design.md#SOL.0840
  - projects/forge/10-intent.md#REJ.0280
  - projects/forge/10-intent.md#REJ.0340
  - projects/forge/10-intent.md#REJ.0350
---

# Working together on one project

Working together on one project is the case where two people, or two
branches, change the same project and the changes have to be merged.
This page says what the forge promises in that case, how each kind of
file merges and why the merge itself is left to git. It is for whoever
shares a project with someone, extends the forge or weighs whether it
fits a team.

## What it is

A project is a git repository of its own. Every file of a project has
one of three ways of merging, and the forge tells git which one
through the project's `.gitattributes`:

- **Text.** Git merges the file as text. A person settles what git
  leaves in conflict.
- **Derived.** The file is made from other files. It is never merged
  by hand: it is made again.
- **Immutable and unique.** The file is immutable and its name is
  unique. It never conflicts.

The merge itself belongs to git. The forge never merges, pulls or
rebases on its own judgement. What it adds to git is three things:

- the attributes, which name the way of each file;
- a save that pushes a merge as it was made
  ([Save your work](../use/save-your-work.md));
- the step of a conflict
  ([Settle a conflict](../use/settle-a-conflict.md)), in which Claude
  lays both sides of a conflict out and the principal (the person
  whose thinking is being forged) decides.

## How it works

### The three ways

The kinds of file named here are terms of the forge. Each has its line
in the [Glossary](../reference/glossary.md).

| Way | Files | At a merge |
|---|---|---|
| Text | the artefacts, the recipes, the work specifications, the threads, the project file, the record files | git merges the file as text; a person settles what git leaves in conflict |
| Derived | the ledger (the file that holds the state of a project); the documents for a reader; the published files | the ledger is not in git and is made at read time; a document for a reader is taken as `ours` and made again; a published file is binary and never merged |
| Immutable and unique | reviews, challenges, research, sources, closed threads | never conflicts |

**Text.** The record files are text like the artefacts:

- the histories;
- the decisions;
- the resource indexes;
- the documentation map.

A conflict in a text file has one of two shapes. In an artefact it is
the same item or sentence changed on both sides. In a record file it
is two tails appended after one last line, and both are kept.

**Derived.** The ledger is never in git. It is made at read time and
never conflicts. The reason is given in
[The ledger, made from the records](the-ledger.md).

The documents for a reader are in git:

- the renders;
- the README;
- the release notes;
- CONTRIBUTING;
- the documentation;
- the state render;
- the published companions (`published/*.md`).

They are made only on `main`. At a merge git does not combine the two
sides of such a file: it keeps one side whole (`merge=ours`), and the
file is made again. The published files themselves are binary and are
never merged.

The commands that make a derived file (`/release`, `/publish` and
`/document`) run on `main` only. Each refuses a repository that is
behind its origin or has diverged from it, and offers `/pull`. Where
two branches made the same file all the same, they conflict on the
server and are settled by making the file again. Why these files are
made on `main` only is said in
[Persistence in git](persistence-in-git.md).

**Immutable and unique.** Reviews, challenges, research, sources and
closed threads never conflict. The name of such a file is unique
across branches too. Immutability is a process rule and not a git
mechanism: nothing is locked.

### The attributes

Every project carries a `.gitattributes` from the engine, copied from
`templates/gitattributes` when the project is created. Its lines,
without the comments:

```
* text=auto
renders/** merge=ours
/README.md merge=ours
/RELEASE-NOTES.md merge=ours
/CONTRIBUTING.md merge=ours
docs/** merge=ours
published/*.md merge=ours
published/*.pptx binary
published/*.docx binary
```

- The first line normalises line endings. Files then do not fight
  between machines.
- The lines with `merge=ours` name the documents for a reader.
- The lines with `binary` name the published files.
- The record files carry no attribute and merge as text.

The three root files are anchored with a leading slash. A bare name
matches at every depth. Where git ignores case (`core.ignorecase`, the
default on Windows and macOS), a bare name also matches in every case.
A bare `README.md` would then take `recipes/readme.md` as `ours`
without a conflict, and that file is a recipe, which merges as text.

The way of the derived files needs a registration on each machine,
made once for every repository on it. The status report says when the
registration is missing. The reason is that a clone without it
silently falls back to a conflict.

Beside the attributes every project carries a `.gitignore`. It keeps
out of git what never belongs there: the ledger and the lock files an
office program leaves beside an open document.

The engine carries the same for the derived files at its own root:
`README.md`, `RELEASE-NOTES.md`, `CONTRIBUTING.md` and `docs/**`. The
forge's own project (`forge`) carries the attributes like every
project.

### What the forge promises

One person on one project saves and pulls, with `/save` and `/pull`.

With two people, or two branches, on one project:

- The derived state is made anew at read time and never conflicts.
- A conflict in a history, in `decisions.md` or in an index is two
  tails. It is settled by keeping both.
- A conflict in an artefact is the same item or sentence changed on
  both sides. It is settled by a person with Claude's help, in the
  step of a conflict.
- IDs stay one sequence. A number taken twice is settled after the
  merge.
- A version given twice is found at the merge and settled in the same
  step.
- A merge request without conflict is merged on the server. A merge
  request with conflict is fetched and settled on a clone.

Two windows of one person on one project are not solved.

### The step of a conflict

A conflict the save meets is left standing and is not aborted. The
save names the files in conflict and the step that follows.

The step is a walkthrough (one conflict per question, each answered by
the principal's verdict). Claude reads both sides and lays them out.
The principal decides. Claude writes the chosen wording into the file.
For an artefact it adds a `changed` record to the history of the
artefact. For a record file both tails are kept.

The git commands that finish the step are not run by Claude alone:
each is put to the principal and runs on his yes. Every other write of
Claude to git goes through the forge's scripts. The save then pushes
the repository. The same step serves a merge the integrator made by
hand.

A save refuses a repository in which a rebase or a merge is already
standing, before it stages anything. Conflict markers are therefore
never committed. How the step is done is in
[Settle a conflict](../use/settle-a-conflict.md).

### A number or a version taken twice

IDs stay one sequence per project. A number is taken at the write, and
no other branch is read for it. Two branches that took the same number
are reported after the merge. The younger item is renumbered with a
record, in a walkthrough and never by Claude alone. How that is done
is in [Stable IDs](stable-ids.md).

A version given twice is two branches that both raised a document to
the same number. Git itself shows it. Both sides appended their
records to the end of the document's history, and the two tails
conflict as text. The `version:` line of the header conflicts only
where the two numbers differ. Where they are the same it merges
silently.

Whoever merges settles a version given twice, in the step of a
conflict. The merged document takes the next number and one `changed`
record that names the merge and what was joined. The records of both
sides keep their numbers.

### Several people on one project

The work of several people on one project has a stated model: one
integrator and any number of contributors.

- A contributor works on a branch and saves it. The save pushes the
  branch. Switching a project to a branch is in
  [Work on a branch](../use/work-on-a-branch.md).
- The integrator (a maintainer, typically the principal) merges the
  branch.

Where the integrator merges depends on the merge request:

- Where it has no conflict, it is merged on the server.
- Where it has a conflict, the integrator merges on his own clone with
  git itself, outside the forge's scripts. What git leaves standing is
  settled in the step of a conflict. He then saves on `main`.

```
contributor                    integrator
-----------                    ----------
works on a branch
saves: the branch is pushed
          |
          v
    merge request ---------->  no conflict: merged on the server
                  ---------->  conflict: merged on his own clone
                               with git itself
                                 -> the step of a conflict
                                 -> saves on main
```

A merge request on the server is for reading and for the merge that
needs no hand. The server applies none of the forge's attributes when
it merges. Two people who both append to a history or to the decisions
have a conflicting merge request there.

The save rebases one's own commits onto the remote only where both
sides moved on, that is where the histories diverged. A branch that is
merely ahead of the remote is pushed as it stands, a merge commit
among its commits included. The integrator's merge of a branch and a
contributor's merge of the upstream then keep their merge commit, and
nothing of the other side is replayed. Where a repository has diverged
from its origin, `/pull` offers the merge.

### Two windows of one person

With two windows open, a save is given the slug of the project. A bare
`/save` is for one window: it commits every repository with changes,
the other window's half-written work included. On two projects the
windows collide nowhere, each project being a repository of its own.

On one project the forge solves nothing. Whoever works in the two
windows either does work that the windows can merge afterwards, or
arranges it through git: a branch, or a second clone where a branch in
one working tree is not enough. A branch switched in one working tree
is seen by both windows.

## Why

- **The ledger is made at read time.** The ledger and the record files
  are the files present on both sides of a merge. The ledger made at
  read time and the threads kept as files take most of that away.
- **The merge stays with git.** Two people on one project are the
  exception, and the exception is handled with git.
- **No merge driver of the forge for the record files.** The record
  files are text, and a conflict in them is two tails, both kept in
  the step of a conflict. A driver fails where the merge happens on
  the server and for a contributor without the registration. It would
  be the most code for a case of a few times a year.
- **No union merge for the record files.** By git's own documentation
  a union merge duplicates and does not order.
- **No merge command of the forge.** The step of a conflict gives the
  same help without a new mechanism: it lives in the save and in the
  question put to the principal before git finishes. The merge stays
  with git.
- **The attributes lie in the project.** The attributes travel with
  the repository. The registration on a machine does not.
- **A conflict is settled on a clone.** The server applies none of the
  forge's attributes when it merges.
- **The save rebases only where the histories diverged.** A rebase
  drops a merge commit and replays what it brought in, and a
  contributor's branch meets exactly that.
- **One integrator.** A hosted project's `main` is protected by
  default, and the protection refuses a push to `main` by everyone.
  The model is consistent with a forge built around the principal. It
  removes every need to write to `main` from a branch.
- **A number taken twice is detected, not prevented.** A clash happens
  a few times a year on a project of one or two people. Detection with
  the existing remedy costs nothing. Preventing a clash in advance
  would cost the most code.
- **Two windows of one person on one project are left to git.** The
  reason is not recorded.

## A worked example

A project `my-project` has one contributor and one integrator, who is
the principal here. The intent of the project stands at version 0.4.

1. The contributor switches the project to a branch (`wording`) and
   changes one sentence of an item of the intent. The intent goes to
   version 0.5, with a record at the end of its history. The
   contributor saves, and the save pushes the branch.
2. Meanwhile the integrator works on `main`. He changes another item
   of the intent. The intent goes to version 0.5 there too, with a
   record of his own at the end of its history.
3. The merge request shows a conflict: both sides appended to the same
   history. The integrator merges the branch on his own clone with git
   itself, outside the forge's scripts.
4. Git merges what it can:
   - The intent merges as text. The two changes lie in different
     items, and the `version:` line carries 0.5 on both sides and
     merges silently.
   - The history of the intent is left in conflict: two tails after
     one last line.
   - The ledger takes no part: it is not in git.
5. The step of a conflict follows. Claude lays the two tails out, and
   both are kept. The two records show the version 0.5 given twice.
   The integrator settles it: the merged intent takes the next number
   (0.6) with one `changed` record that names the merge and what was
   joined. The two records of 0.5 keep their number.
6. The git commands that finish the merge run on the integrator's yes.
   His save pushes `main` as it stands. The repository is merely ahead
   of the remote: nothing is rebased, and the merge commit is kept.
7. The ledger is made anew at the next read. The documents for a
   reader are not merged by hand either: the commands that make them
   make them again on `main`.

Two variants of the same run:

- Had both sides changed the same sentence of the intent, git would
  have left the intent in conflict too. The integrator would decide
  the wording, and Claude would write it into the intent with a
  `changed` record in its history.
- Had both sides added an item under the same number, the clash would
  be reported after the merge. The younger item would be renumbered
  with a record, in a walkthrough.

## See also

- [Settle a conflict](../use/settle-a-conflict.md): the step of a
  conflict, done.
- [Persistence in git](persistence-in-git.md): the doors to git and
  why the files for a reader are made on `main` only.
- [Work on a branch](../use/work-on-a-branch.md): switching a
  repository to a branch.
- [Save your work](../use/save-your-work.md): the save, which pushes
  a merge made by hand as it stands.
- [The ledger, made from the records](the-ledger.md): why the ledger
  is made at read time.
- [Stable IDs](stable-ids.md): how an item number taken twice is
  settled.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
