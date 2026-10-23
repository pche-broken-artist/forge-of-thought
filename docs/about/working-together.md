---
generated: 2026-10-23
version: 5.34
made: derived
inputs-hash: 74880ae6bbdd2720
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
changing the same project repository and bringing their work back
into one line through git. This page explains what the forge promises
in that case, how each kind of file of a project merges, and why it is
built that way. It is for anyone who uses the forge with someone else,
for anyone who extends it, and for anyone judging whether it fits a
team. A short definition of every term used here is in the
[Glossary](../reference/glossary.md).

## What it is

Every file of a project has one of three ways of merging. The forge
tells git which way through the project's `.gitattributes` file. The
forge itself never merges, pulls or rebases on its own judgement:
merging stays git's.

The three ways are these.

- **Text.** The artefacts (the documents of the chain), the recipes,
  the work specifications, the threads, the project file, and the
  record files: the histories, `decisions.md`, the resource indexes
  and the documentation map. Git merges them as text. What git leaves
  in conflict is settled by a person.
- **Derived.** The ledger (the one report of a project's state) is
  never in git and is made at read time, so there is nothing to merge.
  The documents for a reader are in git but made only on `main`: the
  renders, the README, the release notes, `CONTRIBUTING.md`, the
  documentation, the state render and the published companions. At a
  merge git takes `ours` for them, and they are made again. The
  published files themselves are marked binary and never merged.
- **Immutable and unique.** Reviews, challenges, research, sources and
  closed threads never change once written, so they never conflict.
  The name of a report is unique across branches too. Immutability is
  a rule of the process, not a lock: nothing is locked.

## How it works

### The attributes file

Every project carries a `.gitattributes` made from the engine's
template `templates/gitattributes`. The template carries these lines:

- `* text=auto`: line endings are normalised, so that files do not
  fight between machines.
- `merge=ours` on `renders/**`, `README.md`, `RELEASE-NOTES.md`,
  `CONTRIBUTING.md`, `docs/**` and `published/*.md`.
- `binary` on `published/*.pptx` and `published/*.docx`.

The record files carry no attribute and merge as text. `/new-project`
creates the file, and `/check project` reports a project without it.

The engine carries a list of its own. This is because its derived
files lie at its root: `README.md`, `RELEASE-NOTES.md`,
`CONTRIBUTING.md` and `docs/` at the root, and the renders and the
published companions under `projects/forge/`.

`ours` is not built into git. `/setup` registers it once per machine,
on your word, in your global git configuration, with the git settings
it needs. The status report says when the registration is missing.
This matters because a clone without the registration silently falls
back to a conflict.

### What the forge promises

With one person on one project, you save with `/save` and pull with
`/pull`, and nothing more is needed.

With two people, or two branches, the forge promises the following.

- **Derived state:** it is made anew at read time and never conflicts.
- **A record file:** a conflict in a history, in `decisions.md` or in
  an index is two tails appended after one last line. It is settled by
  keeping both.
- **An artefact:** a conflict is the same item or sentence changed on
  both sides. It is settled by a person with Claude's help, in the
  step of a conflict.
- **IDs:** they stay one sequence per project, taken at the write.
  Two branches that took the same number are reported by the ledger
  script after the merge, and the younger number is renumbered with a
  record. How that is done is on [Stable IDs](stable-ids.md).
- **A version given twice:** when two branches both raised a document
  to the same version, git itself finds it, because the `version:`
  line of the header conflicts. It is settled in the step of a
  conflict by whoever merges. The merged document takes the next
  number and one `changed` record that names the merge and what was
  joined. The records of both sides keep their numbers.

The step of a conflict runs like this. A conflict that `/save` meets
is left standing, not aborted. Claude lays both sides out as a
walkthrough (one item per message, each closed with a verdict). The
principal (the person whose thinking is forged, with the final word on
all content) decides. Claude writes the wording. The git commands that
finish the merge run only after the principal says yes. The step is
done on [Settle a conflict](../use/settle-a-conflict.md).

### One integrator and contributors

The work of several people on one project follows one model: one
integrator and any number of contributors.

1. A contributor works on a branch and saves it. `/save` pushes the
   branch. Switching to a branch is on
   [Work on a branch](../use/work-on-a-branch.md).
2. The integrator merges the branch. The integrator is a maintainer
   of the repository, typically the principal.
3. Where the merge request has no conflict, the integrator merges it
   on the server.
4. Where it has a conflict, the integrator fetches it and settles it
   on their own clone, in the step of a conflict.

The second path exists because the server merges with no attribute of
the forge's. On the server, two people who both appended to any
history or to `decisions.md` have a conflicting merge request. A merge
request on the server is for reading and for the merge that needs no
hand.

`/save` rebases your own linear commits. A branch that carries a merge
commit is merged by hand, because the forge has no door of its own for
it. The documents for a reader are made only on `main`. Two branches
that made the same one conflict on the server, and are settled by
making it again on `main`. Why these files are made on `main` only is
on [Persistence in git](persistence-in-git.md).

### Two windows of one person

Two windows of one person on one project are not solved by the forge.
The person either does work the two windows can merge afterwards, or
arranges it through git. Git's answer is a branch, or a second clone
where a branch in one working tree is not enough. A second clone is
needed because a branch switched in one working tree is seen by both
windows. On two different projects the windows never collide, since
each project is a repository of its own.

A bare `/save` is for one window only. This is because it commits
every repository with changes, including the other window's
half-written work.

## Why

The ledger was the one file present on both sides at every collision
that was seen in practice. Beside it stood the histories, the
decisions, the index of sources and the regenerated renders. Made at
read time, the ledger stopped being a thing to merge. Why the ledger
is made at read time is on
[The ledger, made from the records](the-ledger.md).

Two people on one project are the exception, and the exception is
handled with git. The forge is built around the principal. The model
of one integrator removes every need to write to `main` from a
branch. It also fits a hosted repository, where `main` is commonly
protected by default and refuses a push from everyone.

IDs and versions are settled by detection, not by prevention. A clash
happens a few times a year on a project of one or two people.
Detection with the existing remedy costs nothing, where prevention
would have cost the most code.

Three mechanisms were considered and let go.

- **A union merge for the record files.** Union duplicates lines and
  does not order them, by git's own documentation.
- **A merge driver of the forge's own for the record files**, which
  would have joined them as sets of records. A driver fails where the
  merge happens on the server, and for a contributor whose machine
  lacks the registration. It would also have been the most code for a
  case of a few times a year. The record files merge as text instead,
  a conflict in them two tails kept both.
- **A merge command of the forge.** The same help comes without a new
  mechanism, from the step of a conflict in `/save` and on the
  principal's yes. The merge stays git's.

## A worked example

A project `example-project` has an integrator and one contributor.

1. The contributor switches their clone to a branch `new-idea`, works
   on the intent, and runs `/save`. The branch is pushed. Their round
   raised the intent from version 0.4 to 0.5 and appended records to
   its history.
2. Meanwhile the integrator worked on `main`. They also raised the
   intent to 0.5 and appended records to the same history.
3. The contributor opens a merge request. The server reports a
   conflict, because it merges with no attribute of the forge's.
4. The integrator fetches the branch and merges it on their own clone.
   Git reports three things:
   - the history has two tails after one last line;
   - the intent's `version:` line conflicts;
   - one item of the intent was changed on both sides.
   A render of the project conflicts nowhere, because `merge=ours`
   keeps the one on `main`.
5. In the step of a conflict, Claude lays out the history's two tails,
   and both are kept. It lays out the changed item; the principal
   decides its wording, and Claude writes it. The intent takes version
   0.6 with one `changed` record that names the merge and what was
   joined.
6. On the principal's yes, the commands that finish the merge run.
   The ledger is made at the next read, and the render is made again
   on `main`.
7. If both sides had taken the same item number, the ledger script
   would report it after the merge, and the younger one would be
   renumbered with a record.

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
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-23 for version 5.34 from the files the
front-matter names; never edited by hand.
