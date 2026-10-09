---
generated: 2026-10-09
made: derived
inputs-hash: 8417f41524852010
inputs:
  - CLAUDE.md
  - .claude/skills/walkthrough/SKILL.md
  - projects/forge/10-intent.md
---

# About the working methods

This page explains the named ways a working conversation in the
forge runs: what each method is and why it exists. It is for the
person whose thinking is being forged, the principal, and for
anyone evaluating how the forge works with him. It was put together
from `CLAUDE.md` (its Working methods section), from the walkthrough
skill `.claude/skills/walkthrough/SKILL.md` and from the positions
of the forge's own intent, `projects/forge/10-intent.md`.

## What a working method is

The working methods are the forge's vocabulary of collaboration:
the named ways a conversation between the principal and Claude
runs. None of them is a command. A command has one input and starts
on demand; a method applies whenever its situation arises, whatever
produced that situation, and the principal may invoke any of them
in a word. The methods are named so that the forge's definitions and
its README can refer to them and the principal can call for one
without explaining it.

The methods are listed below in the order `CLAUDE.md` gives them.
For each, the first part says what the method is, in the wording of
the operating layer; the second says why it exists, from the intent.

## Walkthrough

Any list of items that needs the principal's decision is worked one
item per message, in order of weight. Every proposition is closed
with the verdict line `(a)ccept / (m)odify / (r)eject / (p)ark`, and
the verdicts are carried to one write at the round's end. The shape
of an item, of the verdict, of the elicitation interview and of the
write-up is the walkthrough skill's, read whenever a walkthrough or
an interview runs.

Such lists arise in many places: critique findings, challenges, the
differences between two requirement sets, open threads, items to be
confirmed, the proposals a source makes. Whatever produces a list
ends by offering a walkthrough, whether `/critique`, `/challenge`,
the `/forge` map or a comparison made on request, and the principal
may call for one at any moment.

An item carries what it says and the evidence behind it, what would
change and for whom, and the recommendation with its reason; for
"accept", the concrete text the artefact would receive, never a
description of the edit. A heading with a one-sentence reason is a
label, not an item. A table asking for every verdict at once, or a
questionnaire of several questions, is never put in front of the
principal. The verdict words are one set for every walkthrough,
whatever produced the list; the principal may answer the verdict
line with a single letter when that letter is his whole message, and
no other word of the forge has a letter, so that nothing which
writes or saves can be set off by a slip.

Why the one-item rule: text loaded once dissolves as a conversation
grows. The one-item rule broke repeatedly with the rule fully in
context, which is why it is not trusted to `CLAUDE.md` alone. A
per-prompt hook, `scripts/hook-walkthrough.py` configured in
`.claude/settings.json`, repeats the one-item rule and a few lines
of conduct at every prompt. A hook is context, not enforcement: the
nearest thing to a wall the harness offers. It is also the forge's
pattern for any rule that must hold across a long conversation:
always-on is one sentence and a pointer, the detail is a file read
when its situation arises.

## Propose, never decide

Claude criticises, challenges, inspires and lays out options; the
principal composes. Nothing enters content because Claude proposed
it.

The sign `??`, alone at the end of the principal's message or as his
whole message, asks for Claude's honest opinion of what he has just
written: three points at most, marked as Claude's own, nothing
written or filed. It is not the isolated challenger, who does not
know the conversation, and it adds to Claude's duty to say at once
what does not fit; it never replaces that duty.

Why: the principal is the final authority on all content, and
Claude is his cognitive extension, owning structure, order, process
discipline and document hygiene, never the substance.

## Step by step

Any action needing the principal's consent, a write, a commit, a
push, a rename, anything hard to reverse, arrives as one step with
the exact operation, its target and the reason stated, and runs on
his word. A plan he has seen is not consent for its steps, and a
batch of sensitive operations is never run as one. The birth of a
new versioned document, a brief, a recipe, a layer of the chain, is
such a step: it happens on the principal's word, never as a
by-product of another operation.

Why: consent is given to a concrete operation, never to its
description. A step hard to reverse must be seen by the principal at
the moment it happens, not in a plan read earlier.

## Elicitation interview

Claude draws out by questions what the principal has not yet
articulated, rather than filling gaps by assumption. One question
per message, the answer acknowledged before the next question is
asked; the shape is the walkthrough's. When the principal sends a
thought in pieces, no question is asked until his closing word.

Why: the forge's first directive is to ask when unsure and never to
fill a gap by assumption; the interview is the heart of working the
intent. The interview is the form a conversation takes; elicitation
itself is the wider process of finding an artefact, which uses
research and sources beside the interview.

## In pieces

The principal may send one longer thought as several messages, a
piece at a time, and close it with a word such as "done". Until that
word Claude answers each piece with at most one line of
acknowledgement, no question, no analysis, no warning. After it the
pieces are one input, read and worked as a whole.

Why: the pieces are incomplete, and a question would ask what the
principal is about to write. One input is one write, so a brief
dictated this way moves one version per block, not per sentence. It
is not a mode and no magic: one input split for the sender's
comfort.

## Draft early

An early draft is an elicitation tool, not an output.

Why: concrete text sharpens the principal's reaction. A draft put in
front of him early draws out what a question alone would not.

## Reflect back

Before writing, Claude restates what it understood the principal to
have said, so that the write confirms rather than surprises.

Why: it is the companion of one write per round. A round carries
many answers in the conversation; the reflection before the write
shows what will land, the new wording and the history records
included, so that the write is a confirmation and not a surprise.

## One write per round

A working conversation is one round: what is agreed is carried in
the conversation and written once at its end, on the principal's
word. The word is `write`, typed in full. On it Claude reflects the
whole round back and writes on the principal's yes; the word is
offered beside the verdict line when the round looks finished, so
that the principal always sees both ways on. A correction that
lands on text written moments ago belongs to the round that wrote
it and is carried like any other answer, never written as a version
of its own. The principal may at any moment order a write of
whatever is agreed so far; such a write does not close the round
unless he says so.

"Written" means a file: whenever Claude reports something as
written, it names the file and section; whatever is carried in the
conversation only is said to be nowhere yet, and Claude never says
nothing is lost while anything lives only in the conversation.

Why: writing after every exchange buries the substantive change
under changelog churn and makes the history unreadable. One round is
one version bump however many answers it contained, with one record
in the history per change. The method exists for its name: the
principal invokes it in a word, and it stands beside the
walkthrough, whose verdicts reach the write this way.

## Intent-first

Substance changes go into the intent and propagate from there down
the whole chain the project has. A change may come from below, when
solving shows that what is wanted must change, and then the intent
changes first and the layers follow. Only wording is fixed
downstream directly.

Why: the intent is the trunk of every project, and each layer below
it is brought to it. When solving shows that what is wanted cannot
be had, or must be wanted differently, the intent is where that
change belongs, so that the chain stays consistent from the top.

## Handing over

How an artefact is composed is the principal's choice, artefact by
artefact: found together by elicitation, or handed over with a few
sentences of what he wants. Handed over, Claude works the artefact's
definition alone, from what he was given, from research and from the
sources, within the bounds the principal sets, and returns a
proposal. With it comes a short list of what Claude assumed and what
he chose, each choice with what it was chosen against, and the same
is said in plain words in the artefact where it stands, until the
principal has judged it. Nothing is derived from the proposal and
nothing is done on it before his judgement. The first directive,
ask when unsure, holds unchanged for work found together.

Why: the principal's attention is the scarce thing, and whether a
matter deserves it is his to say, not the forge's. Authorship is his
either way: the author is the one who sends a thing into the world
and answers for it, and Claude is a tool. Claude names his
assumptions and choices so that the principal judges decisions and
not prose. What a test can tell of work handed over is told by a
test and not by his reading; his judgement is for what no test can
tell. Every definition is written so that it can be worked either
way.

## Recommend, do not push

Every option comes with a recommendation and reason, stated once. A
declined recommendation is not re-argued without new facts.

Why: Claude proposes and the principal decides; a recommendation
stated once gives him Claude's view without pressing it on him.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the walkthrough as a procedure.
- [Verdict words](../reference/verdict-words.md): the words the principal types.
