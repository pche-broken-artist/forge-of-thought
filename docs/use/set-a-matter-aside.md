---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 4a3755bad914514d
inputs:
  - .claude/skills/thread/SKILL.md
  - templates/thread.md
  - templates/ledger.md#Waiting on principal
---

# Set a matter aside as a thread

This page shows how to set a matter of a project aside with
`/thread`, how to see what is open and how to take a thread up again.
A thread is one matter set aside to be taken up later: a task, a
question, a decision to make or an idea. The forge does not ask which
it is. The page is for you, the principal, that is, the person whose
thinking is being forged.

## When to use it

Use it when a matter comes up that you do not want to settle now but
do not want to lose. Use it also to see what is open in a project, or
to go back to a matter you set aside earlier. What a thread is, what
it holds and why it is a file of its own is explained in
[Threads](../about/threads.md).

## The command

```
/thread [text | THR.NNNN] [slug]
```

The slug names the project and goes last. Without it, the project in
context is used, and where that is ambiguous Claude asks.

The three forms are these:

- `/thread` alone lists the open threads.
- `/thread <text>` is the birth of a thread from what you say.
- `/thread <ID>` takes the thread with that ID up.

## What happens

### Seeing what is open

1. Type `/thread` alone. Claude remakes the project's ledger (the
   file that holds the state of the project, made from its documents
   each time it is read) and prints the open threads from it.
   Nothing is written.

   You should now see the open threads in the ledger's order: first
   those something waits on, then the rest by priority, each with its
   first sentence and its last dated paragraph. The order is described
   in [Ledger](../reference/ledger.md), under the list of what waits on
   the principal.

### The birth of a thread

1. Type `/thread` and your text. Claude first looks whether the
   project already has an open thread on the matter.

   You should now see either a proposal to continue that thread, or
   the draft of a new one. A closed thread on the same matter is not
   continued: the new thread cites it.

2. Claude drafts the thread whole from what you said and shows it
   once. The draft holds:

   - the matter
   - what is known of it
   - what will close it
   - what it concerns
   - where it came from
   - its priority
   - what waits on it

   What you said is taken as said. What you did not say, the priority
   and what waits on the thread among it, Claude proposes and marks as
   its proposal. It asks a question only where the matter itself is
   unclear, never about the form.

   You should now see the draft, closed by the verdict line
   `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. The line
   works as in [Walk through a list](walk-through-a-list.md).

3. Answer the verdict line. `accept` writes the thread as shown, a
   file of its own in `threads/` under the next free number. An input
   that holds several matters is shown as several threads in the one
   draft.

   You should now see the new thread named by its number. The birth is
   recorded in the history of the project's intent, or of its brief
   while it has no intent.

A thread is born on your command only. It can come from your own word,
from a document you name or from Claude's synthesis when you ask for
it. Claude may say that a matter deserves a thread, and it drafts one
when you say so.

### Taking a thread up

1. Type `/thread` and the ID. Claude reads the thread and says where
   the matter stands and what is open now.

   You should now see a short statement of the state of the matter.

2. The work then runs as the matter needs. Often it is a round of the
   intent, as in [Forge the intent](forge-the-intent.md). Where the
   work changes an artefact, a recipe or a work product, it runs
   through that document's own command.

3. At the end, on your word, one of two things happens:

   - What was reached is saved into the thread as one dated
     paragraph.
   - The thread is closed. What was decided is written where it
     belongs first, so that nothing decided stays in the closed thread
     alone.

   You should now see either a new dated paragraph in the thread or
   the thread marked closed.

## What you have afterwards

After a birth you have a file `threads/THR.NNNN.md` in the project,
open, with a header that says what it concerns, where it came from,
whose it is, its priority, what waits on it (only where something
does) and whether it is open. After taking a thread up you have the
same file with a new dated paragraph, or closed.

A thread without a priority is read as medium. A thread without an
owner is read as owner not said. Neither is a fault.

Closing is a last dated paragraph that says how the matter ended and
where what was decided now stands. The closing is recorded in the
history. The closed file is never changed again. When the matter
returns, it comes back as a new thread that cites the old one.

The open threads reach the project's overview too. The map of
[See where a project stands](see-where-a-project-stands.md) names the
threads something waits on and the high ones, and counts the rest.

## Claude and the upkeep of a thread

Claude keeps the form of a thread by itself and asks nothing about it.
When it sees that a thread is settled, that what waited on it is done
or that its priority no longer fits what you say, it says so once and
proposes the change. It never closes a thread, changes its priority or
sorts the threads on its own judgement. The header changes on your
word.

## If something goes wrong

- Claude cannot tell which project you mean: it asks for the slug. Give
  it as the last argument.
- The input holds several matters: the draft shows several threads.
  Answer for them together, or modify the draft.
- You do not want the draft as shown: answer `modify` or `reject`. Only
  `accept` writes the thread.
- Two threads turn out to carry the same number: this is a clash of
  IDs. The younger one is renumbered, as the forge's rule for IDs says.
  See the [Glossary](../reference/glossary.md) for the terms.

## A worked example

You type, with a placeholder slug:

```
/thread Decide whether the onboarding guide is one document or two my-project
```

Claude finds no open thread on the matter and shows a draft:

```
Thread (new)
  matter:      Decide whether the onboarding guide is one document
               or two.
  known:       The guide now mixes a first-day path and a reference
               for later; nothing else is said.
  closes when: the choice is made and written into the guide's
               specification.
  concerns:    work/onboarding-guide.spec.md
  origin:      the principal
  priority:    medium (Claude's proposal)
  blocks:      the next edition of the guide (Claude's proposal)

(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

You answer `a`. Claude writes the thread as `threads/<ID>.md` and
names its number.

Some days later you type:

```
/thread <ID> my-project
```

Claude reads the thread and says that the matter is still open, that
the choice between one document and two is not made, and that the next
step is to compare the two shapes. You work on it, then say "save".
Claude adds one dated paragraph with what was reached. Later, once the
choice is written into the specification, you say "close". Claude
writes the choice into the specification first, then adds the closing
paragraph and marks the thread closed.

## See also

- [Threads](../about/threads.md): what a thread is, what it holds and
  does not, and why threads are files of their own.
- [See where a project stands](see-where-a-project-stands.md): the
  `/forge` map, which names the threads something waits on and the
  high ones and counts the rest.
- [Forge the intent](forge-the-intent.md): the round of the intent a
  thread is often taken up in.
- [Walk through a list](walk-through-a-list.md): the verdict line the
  draft of a thread closes with.
- [Ledger](../reference/ledger.md): the Waiting list the open threads
  are printed from, and its order.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
