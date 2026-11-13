---
description: Work the threads of a project — bare = the open threads, with a text = the birth of a thread, with an ID = that thread taken up
argument-hint: "[text | THR.NNNN] [project-slug]"
---

A thread (POS.0120, POS.1680) is one matter of a project set aside
to be taken up later: a task, a question, a decision to make, an
idea; the forge does not ask which. This skill owns the rules of a
thread: what it holds, its birth, its upkeep, its life and its
closing. The shape of its file is `templates/thread.md`'s. The
project is the slug given last, else the project in context; if
that is ambiguous, ask.

**Bare.** Remake the ledger (`python scripts/forge-ledger.py
<slug>`) and print the open threads from it: those something waits
on first, then by priority, high to low. Nothing is written.

**With a text: the birth.** Claude drafts the thread whole from
what the principal said and shows it once: the matter, what is
known of it, what will close it, what it concerns, where it came
from, its priority and what waits on it. What the principal said he
takes as said; what he did not say Claude proposes, the priority
and the blocking among it, and marks as his proposal. The draft
closes with the verdict line, and `accept` writes the thread as
shown, under the next free number. An input that holds several
matters is shown as several threads in the one draft. Claude asks a
question only where the matter itself is unclear, never on the
form. Before he drafts he looks whether the project already has an
open thread on the matter; where it has, he says so and proposes a
continuation of that one instead, on the same verdict; a closed
thread on the matter is cited by the new one. A thread is born on
the principal's command only (POS.0120): from his own word, from a
document he names, an issue among them, or from Claude's synthesis
when he asks for it. Claude may say that a matter deserves a
thread; he drafts one when the principal says so. The birth is a
`created` record in the intent's history, or in the history of
`00-brief.md` while the project has no intent
(`scripts/forge-record.py`).

**With an ID: the thread taken up.** Claude reads the thread and
says where the matter stands and what is open now; the work then
runs as the matter needs, and where it changes a document the forge
has a definition for, an artefact, a recipe, a work product, by
that definition. At its end, on the principal's word, what was
reached is saved into the thread as one dated paragraph, or the
thread is closed: what was decided is written where it belongs
first, so that nothing decided stays in the closed thread alone.

**What a thread holds.** Its one matter and what is known of it
while it is unsettled: the situation and its evidence, what was
said and tried, the plan of a change under way, the proposals that
await a decision, an unfinished conversation, Claude's view marked
as his. Every continuation says where the matter stands and what
is open now. It does not hold: a second matter, which is a thread
of its own; what has been decided, which goes into the artefact it
concerns; the text of a source, which is cited by path; its origin
a second time, which the header says; and the thing being made, a
brief, a specification, a document, which lives in its own file
with the thread pointing there.

**The header.** Its fields and their values are
`templates/thread.md`'s. `priority` says when the matter is taken
up, not how much it binds; `blocks` stands only where something
waits. A thread without `priority` is read as medium and one
without `owner` as owner not said; neither is a finding.

**Upkeep.** Claude keeps the form of a thread by himself and asks
nothing about it: the owner and the date of opening, the first
sentence whole, each continuation one dated paragraph. When he
works with a thread and sees that it is settled, that what waited
on it is done, or that its priority no longer fits what the
principal says, he says so once and proposes the change. He does
not close a thread, change its priority or sort the threads on his
own judgement: the header changes on the principal's word. The
threads a project already has are sorted on his word, in the way he
asks for.

**Life and closing.** Freely rewritten while open, the header too;
no version, no history of its own. A thread is never moved,
renamed or deleted, the one exception the renumbering at an ID
clash (POS.0220). Closing is a last dated paragraph saying how the
matter ended and where what was decided now stands,
`status: closed`, and a `closed` record in the intent's history, or
the brief's while there is no intent, saying when and by what, no
`Was`: the closed file is immutable and is the archive; what
returns is a new thread citing the old one.
