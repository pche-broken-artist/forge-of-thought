---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 587d203948901234
inputs:
  - .claude/skills/thread/SKILL.md
  - templates/thread.md
  - projects/forge/10-intent.md#POS.0120
  - projects/forge/10-intent.md#POS.1680
  - projects/forge/40-solution-design.md#SOL.0720
  - projects/forge/40-solution-design.md#SOL.0960
---

# Threads

A thread is one matter of a project set aside to be taken up later.
This page explains what belongs in a thread and what does not. It
also explains how a thread lives and why every thread is a file of
its own. It is written for whoever works on a project with the forge
and for whoever weighs how the forge keeps what is unfinished.

## What it is

A thread is one matter of a project that has been set aside and will
be taken up later. The matter may be any of these:

- a task
- a question
- a decision to make
- an idea

The forge does not ask which of these it is.

A thread says five things about its matter:

- what the matter is
- where it came from
- how much it matters
- what waits on it, where something does
- what will close it

Beyond these it carries what is known of the matter until the matter
is taken up.

The threads stand beside the intent (the working document that holds
the current state of what the principal wants; see
[The intent](the-intent.md)). The principal is the person whose
thinking is being forged. The intent says what holds. The threads say
what is being worked.

A thread concerns something of the project. That may be:

- an artefact
- a recipe
- a work product
- any other document of the project

One thread may concern several of them. Artefact, recipe and work
product are terms of the forge, each given in one line in the
[Glossary](../reference/glossary.md).

Every thread is a file of its own in the directory `threads/` of its
project. The file is named `threads/THR.NNNN.md`, where `NNNN` stands
for the number of the thread. A thread is not an artefact. It has no
title, no version and no history of its own. Its header is its state.

## How it works

### What a thread holds

A thread holds its one matter and what is known of it while the
matter is unsettled:

- the situation and its evidence
- what was said and tried
- the plan of a change under way
- the proposals that await a decision
- an unfinished conversation
- Claude's view, marked as its own

Each time the thread is taken up, what was reached is added as one
dated paragraph, called a continuation. Every continuation says where
the matter stands and what is open now.

### What a thread does not hold

- a second matter: it is a thread of its own
- what has been decided: it goes into the document the thread
  concerns
- the text of a source: the source is cited by its path
- its origin a second time: the header says it
- the thing being made (such as a brief, a specification or another
  document): it lives in its own file, and the thread points there

Source is a term of the forge and has its line in the
[Glossary](../reference/glossary.md).

### The header

The header of a thread is its state. The template of a thread,
`templates/thread.md`, gives the fields:

- `id`: the number of the thread, which also names its file
- `concerns`: what of the project the thread concerns. An artefact is
  named as the command `/forge` names it. Any other document is named
  by its path in the project. Several are separated by commas.
- `origin`: where the matter came from. The default is the principal.
- `owner`: whose the thread is
- `priority`: `high`, `medium` or `low`
- `blocks`: what waits on the thread, in a few free words. The field
  stands only where something waits. Without it nothing waits.
- `status`: `open` or `closed`

The owner is the handle of whoever opened the thread. The instance
(one installation of the forge) gives its principal that handle. The
owner changes when the thread is handed over. The owner is never the
git identity.

The priority says when the matter is taken up. It does not say how
much an item of a document binds. The forge gives items no priority.

A thread without `priority` is read as medium. A thread without
`owner` is read as owner not said. Neither is reported as a finding
(a reviewer's result).

### The life of a thread

```
born on the principal's command
  -> open: rewritten freely, one dated paragraph each time it is taken up
  -> closed: immutable, the archive
  -> the matter returns: a new thread that cites the old one
```

**Birth.** A thread is born on the principal's command only. That
holds whatever the matter came from:

- the principal's own word
- a document the principal names
- Claude's synthesis, when the principal asks for it

Claude may say that a matter deserves a thread. It never opens one on
its own judgement. The command is `/thread`, and how it is used is
shown in
[Set a matter aside as a thread](../use/set-a-matter-aside.md). An
input that holds several matters becomes several threads. Where the
project already has an open thread on the matter, Claude says so and
proposes a continuation of that thread instead.

**While it is open.** An open thread is rewritten freely, the header
included. When it is taken up, Claude reads it and says where the
matter stands and what is open now. The work then runs as the matter
needs. At its end, on the principal's word, what was reached is saved
into the thread as one dated paragraph. An unfinished conversation on
the matter is saved into its thread in the same way.

Claude keeps the form of a thread by itself and asks nothing about
it. The header changes on the principal's word. Claude does not close
a thread or change its priority on its own judgement. It says so once
and proposes the change when it sees one of these:

- the thread is settled
- what waited on the thread is done
- the priority no longer fits what the principal says

**Closing.** Closing a thread is three things:

- a last dated paragraph: it says how the matter ended and where what
  was decided now stands
- the status `closed` in the header
- a record of the closing: it says when the thread was closed and by
  what

What was decided is written where it belongs before the thread is
closed. A closed thread is immutable and is the archive. A matter
that returns gets a new thread, and the new thread cites the old one.

A thread is never moved, renamed or deleted. The one exception is a
number taken twice at a merge, settled as
[Stable IDs](stable-ids.md) describes.

### What the history records

A thread has no version and no history of its own. Its birth and its
closing are records in the history of the intent (the record of what
changed in the intent). While the project has no intent, they are
records in the history of its brief (the document a project has
before it has an intent). A saving of the debate of a thread is not
recorded there.

### The list of the open threads

No list of the threads is kept by hand. The list of the open threads
is made by the ledger (the file that shows the state of a project,
remade each time it is needed; see
[The ledger, made from the records](the-ledger.md)). For each open
thread the ledger prints the matter, that is the first sentence of
the thread, and the last continuation.

## Why

**Why every thread is a file of its own.** A file per thread stands
against one file that would hold all the threads as blocks. Three
reasons are given for the file per thread:

- Two people who work on different threads never conflict.
- Claude reads only the threads it needs.
- No merge has to handle a block with an inner state.

The price is a directory of many small files. How files merge when
two people work on one project is explained in
[Working together on one project](working-together.md).

**Why the rules of a thread stand in a skill of their own.** A skill
is the text that says what a command does. The rules of a thread
stand in the skill of the command `/thread`
(`.claude/skills/thread/SKILL.md`). The other choice is to keep them
in the definition of the intent (definition is a term of the
[Glossary](../reference/glossary.md)). The reason for a skill of
their own: a thread is born outside the work on the intent too.

**Why the owner is a handle and not the git identity.** Two reasons
are given. A project outside git has no git identity. A git identity
would put a name and an address into a public file.

**Why a missing field is read and not required.** The purpose is that
no project need be migrated.

**Why what was decided is written elsewhere before a thread closes.**
The purpose is that nothing decided stays in the closed thread alone.

**Why a thread is born on the principal's command only.** The reason
is not recorded.

## A worked example

The header and the first two paragraphs of a generic thread, as they
stand in a file `threads/THR.NNNN.md`:

```
---
id: THR.NNNN
concerns: intent
origin: the principal
owner: <handle>
priority: high
blocks: the assignment
status: open
---

Whether the pilot runs in one team or in three is not decided. One
team gives a clean comparison with last year; three teams give a
result sooner, and each would need a coach of its own. The thread
closes when the principal has chosen and the choice stands in the
intent. Claude's view: one team first, since the comparison is what
the pilot is for. Opened 2026-03-02.

2026-03-09: The principal leans towards one team and wants the cost
of a coach known before the choice. Open now: the cost of one coach
for a quarter.
```

The header is the state of the thread. It says that the thread
concerns the intent, that the matter came from the principal, that
its priority is high, that the assignment waits on it and that it is
open.

The first paragraph opens with the matter in one whole sentence,
which the ledger prints. It goes on with the situation, with what
will close the thread and with Claude's view, marked as its own. It
ends with the day the thread was opened.

The dated paragraph is a continuation. It says where the matter
stands and what is open now.

When the principal has chosen, the choice is written into the intent
first. The thread then gets a last paragraph, dated and marked
`closed`, which says how the matter ended and where the choice now
stands. Its status becomes `closed`, and from then on the file is not
changed.

## See also

- [Set a matter aside as a thread](../use/set-a-matter-aside.md): the
  command `/thread`, which lists, bears and takes up threads.
- [The intent](the-intent.md): the intent, which says what holds
  while the threads say what is being worked.
- [The ledger, made from the records](the-ledger.md): the ledger,
  whose Waiting list is made from the open threads.
- [Working together on one project](working-together.md): how files
  merge when two people work on one project.
- [Stable IDs](stable-ids.md): how a number taken twice is settled.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
