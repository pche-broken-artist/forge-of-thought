---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - .claude/skills/walkthrough/SKILL.md
  - projects/forge/10-intent.md
---

# About the working methods

This page explains the working methods of the forge: the named ways a
working conversation between the principal and Claude runs. It is for
someone who uses the forge and wants to know what to expect in a
conversation, and for someone weighing whether the forge suits them.
It was put together from the Working methods section of `CLAUDE.md`,
which gives each method's name and wording, from the walkthrough skill
`.claude/skills/walkthrough/SKILL.md`, which gives the shape of an item
and the verdicts, and from the positions of the forge's own intent
(`projects/forge/10-intent.md`) that give the reasons. The methods
appear here in the order and under the names `CLAUDE.md` uses.

## What a working method is

The working methods are the forge's vocabulary of collaboration. None
of them is a command. A command has one input and starts when you ask
for it; a method applies whenever its situation arises, whatever
produced that situation. Each method has a name so that the
definitions and the README can refer to it, and so that the principal
can invoke any of them in a word.

## Walkthrough

Any list of items that needs the principal's decision is worked one
item per message, in order of weight. Such lists are critique
findings, challenges, the differences between two requirement sets,
open threads, open questions, the proposals of a source. Whatever
produces a list (`/critique`, `/challenge`, the `/forge` map, a
comparison made on request) ends by offering a walkthrough, and the
principal may call for one at any moment.

Each item carries, in this order, what it says and the situation or
evidence behind it, what would change and for whom, and the
recommendation with its reason. For "accept" it shows the concrete
text the artefact would receive, never a description of the edit. The
aim is that the principal can decide without asking for an
explanation. The item ends in one proposition, worded so that
`accept` has exactly one meaning: yes to what is in front of the
principal, also where the proposition goes against the reviewer's
suggestion. The message closes with the verdict line
`(a)ccept / (m)odify / (r)eject / (p)ark`. An open question is not a
proposition and closes with the question alone.

The verdict words are one set for every walkthrough, whatever
produced the list: `accept`, `modify`, `reject`, `park` and
`obsolete`. The principal may answer the line with a single letter
when that letter is his whole message. No other word of the forge has
a letter, so that nothing which writes or saves can be set off by a
slip. `park` is a legitimate verdict, not a failure. The verdicts are
carried in the conversation and written once at the round's end (see
One write per round).

Why one item at a time, and why the rule is repeated. Text loaded once
dissolves as the conversation grows: the one-item rule was seen to
break with the rule fully in context. So a rule that must hold in a
long conversation is not trusted to `CLAUDE.md` alone. A per-prompt
hook, `scripts/hook-walkthrough.ps1` configured in
`.claude/settings.json`, repeats the one-item rule, with the verdict
line and a pointer to the full shape, and three lines of conduct at
every prompt. A hook is context, not enforcement: the nearest thing to
a wall the harness offers.

## Propose, never decide

Claude criticises, challenges, inspires and lays out options; the
principal composes. Nothing enters content because Claude proposed
it.

The sign `??`, alone at the end of the principal's message or as his
whole message, asks for Claude's honest opinion of what he has just
written: three points at most, marked as Claude's own, nothing
written or filed. It is not the isolated challenger, who does not know
the conversation, and it adds to Claude's duty to say at once what
does not fit; it never replaces that duty.

## Step by step

Any action that needs the principal's consent (a write, a commit, a
push, a rename, anything hard to reverse) arrives as one step, with
the exact operation, its target and the reason stated, and runs on
his word. A plan he has seen is not consent for its steps, and a batch
of sensitive operations is never run as one. The birth of a new
versioned document, such as a brief, a recipe or a layer of the chain,
is such a step: it happens on the principal's word, never as a
by-product of another operation.

## Elicitation interview

Claude draws out by questions what the principal has not yet
articulated, rather than filling gaps by assumption. One question per
message, the answer acknowledged before the next question is asked;
the shape is the walkthrough's. The interview is the form a
conversation takes. Elicitation itself is the wider process of finding
an artefact, which uses research and sources beside the interview.

## In pieces

The principal may send one longer thought as several messages, a
piece at a time, and close it with a word such as "done". Until that
word Claude answers each piece with at most one line of
acknowledgement: no question, no analysis, no warning. The reason is
that the pieces are incomplete, and a question would ask what he is
about to write. After the closing word the pieces are one input, read
and worked as a whole, and one input is one write. It is not a mode:
it is one input split for the sender's comfort.

## Draft early

An early draft is an elicitation tool, not an output: concrete text
sharpens the principal's reaction.

## Reflect back

Before anything is written, Claude restates what it understood, so
that the write confirms rather than surprises. It is the companion of
One write per round.

## One write per round

A working conversation is one round. What is agreed in it is carried
in the conversation and written once at its end, on the principal's
word, with one version for the whole round and one record in the
history for each change. The word is `write`, typed in full: Claude
reflects the whole round back and writes on the principal's yes. When
the round looks finished, Claude offers `write` beside the verdict
line, so that the principal always sees both ways on.

A correction that lands on text written moments ago belongs to the
round that wrote it and is carried like any other answer, never
written as a version of its own. The principal may at any moment
order a write of whatever is agreed so far; that does not close the
round unless he says so. "Written" means a file: whatever lives only
in the conversation is said to be nowhere yet.

Why. Writing after every exchange buries the substantive change under
changelog churn and makes the history unreadable. The method carries a
name so that the principal can invoke it in a word, and it stands
beside the walkthrough, whose verdicts reach the write this way.

## Intent-first

A change of substance goes into the intent and propagates from there
down the whole chain the project has. A change may come from below:
when solving shows that what is wanted cannot be had, or must be
wanted differently, the intent changes first and the layers follow.
Only wording is fixed downstream directly.

## Handing over

How an artefact is composed is the principal's choice, artefact by
artefact. He finds it together with Claude by elicitation, or he
hands it over with a few sentences of what he wants. Handed over,
Claude works the artefact's definition alone, from what he was given,
from research and from the sources, within the bounds the principal
sets, and returns a proposal. With it comes a short list of what was
assumed and what was chosen, each choice with what it was chosen
against, and the same is said in plain words in the artefact where it
stands, until the principal has judged it. Nothing is derived from the
proposal and nothing is done on it before his judgement. Work found
together keeps the rule unchanged: where Claude is unsure, he asks.

Why. The principal's attention is the scarce thing, and whether a
matter deserves it is his to say, not the forge's. The list of
assumptions and choices lets him judge decisions rather than prose.
Authorship is his either way: the author is the one who sends a thing
into the world and answers for it.

## Recommend, do not push

Every option comes with a recommendation and its reason, stated once.
A declined recommendation is not re-argued unless new facts appear.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the walkthrough as a procedure.
- [Verdict words](../reference/verdict-words.md): the words the principal types.
