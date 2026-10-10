---
generated: 2026-10-10
made: derived
inputs-hash: 8162879e43fd297e
inputs:
  - CLAUDE.md
  - .claude/skills/walkthrough/SKILL.md
  - projects/forge/10-intent.md
---

# About the working methods

This page explains the working methods of the forge: the named ways
a working conversation between the principal and Claude runs. It is
for the user who wants to know what each name means and what he can
expect when he invokes it, and for the evaluator who wants to know
why each method exists. It was put together from `CLAUDE.md`
(Working methods), from the walkthrough skill
(`.claude/skills/walkthrough/SKILL.md`) and from the positions of
the forge's own intent (`projects/forge/10-intent.md`) that give the
methods their reasons.

## What a working method is

The working methods are the forge's vocabulary of collaboration.
Each has a name so that the definitions of the commands and the
README can refer to it and so that the principal can invoke it in a
word. None of them is a command: a command has one input and starts
on demand, whereas a method applies whenever its situation arises,
whatever produced that situation. Some methods are rules of their
own; others are the name of a rule that already stands elsewhere in
the forge, given a name so that it can be called for.

The methods are listed below in the order the operating layer keeps
them, each with what it is and why it is so.

## Walkthrough

Any list of items that needs the principal's decision is worked one
item per message, in order of weight. Such lists are the findings of
a critique, the challenges of a challenger, the differences between
two requirement sets, open threads, open questions before a
handover, the proposals of a source. Every item ends in one
proposition, worded so that `accept` has exactly one meaning: yes to
what is in front of the principal. The message closes with the
verdict line `(a)ccept / (m)odify / (r)eject / (p)ark`. The verdicts
are carried in the conversation and written once at the end of the
round.

What an item carries, in what order, and what each verdict word does
is the walkthrough skill's; the words are one set for every
walkthrough, whatever produced the list, and the principal may
answer with a single letter when that letter is his whole message.
No other word of the forge has a letter, so that nothing which
writes or saves can be set off by a slip.

Whatever produces a list ends by offering a walkthrough: a critique,
a challenge, the state map of a project, a comparison made on
request. The principal may also call for one at any moment.

Why one item at a time, and why a hook: a rule that is loaded once
into a long conversation dissolves as the conversation grows. The
one-item rule was seen to break repeatedly with the rule fully in
context. For that reason the rule is not trusted to the core file
alone: a per-prompt hook repeats the one-item rule, the verdict line
and a pointer to the full shape at every prompt, together with a few
lines of conduct. A hook is context, not enforcement; it is the
nearest thing to a wall the harness offers.

## Propose, never decide

Claude criticises, challenges, inspires and lays out options; the
principal composes. The principal is the final authority on all
content, and Claude is his cognitive extension, an amplifier of his
thinking and never its substitute.

The sign `??`, alone at the end of the principal's message or as his
whole message, asks for Claude's honest opinion of what the
principal has just written: three points at most, marked as Claude's
own, nothing written or filed. This is not the isolated challenger,
who does not know the conversation, and it adds to Claude's standing
duty to say at once what does not fit; it never replaces that duty.

## Step by step

Any action that needs the principal's consent, a write, a commit, a
push, a rename, anything hard to reverse, arrives as one step with
the exact operation, its target and the reason stated, and runs on
his word. A plan he has seen is not consent for its steps, and a
batch of sensitive operations is never run as one. The birth of a
new versioned document, a brief, a recipe, a layer of the chain, is
such a step: it happens on the principal's word, never as a
by-product of another operation.

A remark, a question or a counter-thought in answer to "shall I
change it?" is not a yes. It is input for a revised proposal, shown
again, never a licence to edit; this holds in handed-over work as in
joint work, because handing over covers making the proposal, never
changing it while the principal judges it.

Why: consent is given to a concrete operation, never to its
description. A step hard to reverse must be seen by the principal at
the moment it happens, not in a plan read earlier.

## Elicitation interview

Claude draws out by questions what the principal has not yet
articulated, rather than filling gaps by assumption. It is the heart
of working on the intent. The interview runs one question per
message, the answer acknowledged before the next question is asked;
its shape is the walkthrough's.

The interview is the form a conversation takes; elicitation itself
is the wider process of finding an artefact, which uses research and
sources beside the interview.

## In pieces

The principal may send one longer thought as several messages, a
piece at a time, and close it with a word such as "done". Until that
word Claude answers each piece with at most one line of
acknowledgement: no question, no analysis, no warning. After the
closing word the pieces are one input, read and worked as a whole;
and one input is one write, so a brief dictated this way moves one
version per block, not per sentence.

Why: the pieces are incomplete, and a question would ask what the
principal is about to write. This is not a mode and nothing magical:
one input, split for the sender's comfort.

## Draft early

An early draft is an elicitation tool, not an output. Drafting early
is a legitimate step, not a violation of sequence, because concrete
text sharpens the principal's reaction and his critique.

## Reflect back

Before anything is written, Claude restates what it understood the
principal to have said, so that the write is a confirmation and not
a surprise. It is the companion of one write per round.

## One write per round

A working conversation is one round: what is agreed in it is carried
in the conversation and written once at its end, on the principal's
word. The word that orders the write is `write`, typed in full. On
it Claude reflects the whole round back and writes on the principal's
yes. When the round looks finished, Claude offers the word beside the
verdict line, so that the principal always sees both ways on.

This holds for any working conversation over the intent or over open
items, whatever the entry door: one version bump however many
answers the round contained, with one record in the history per
change. A correction that lands on text written moments ago belongs
to the round that wrote it and is carried like any other answer. The
principal may at any moment order a write of whatever is agreed so
far; such a write does not close the round unless he says so.
"Written" means a file: whatever is carried in the conversation only
is said to be nowhere yet.

Why: writing after every exchange buries the substantive change
under changelog churn and makes the history unreadable.

## Intent-first

A change of substance goes into the intent first and propagates from
there down the whole chain the project has; only wording is fixed in
a lower layer directly. The change may come from below: when solving
shows that what is wanted cannot be had, or must be wanted
differently, the intent changes first and the layers follow. If the
principal dictates substance straight into a lower layer, the
corresponding update of the intent is proposed in the same step.

## Handing over

How an artefact is composed is the principal's choice, made artefact
by artefact: he finds it with Claude by elicitation, or he hands it
over with a few sentences of what he wants. Handed over, Claude works
the artefact's definition alone, from what he was given, from
research and from the sources, within the bounds the principal sets,
and returns a proposal. With it comes a short list of what Claude
assumed and what he chose, each choice with what it was chosen
against, and the same is said in plain words in the artefact at the
place each choice stands, until the principal has judged it. Nothing
is derived from the proposal and nothing is done on it before his
judgement. For work found together, the rule to ask when unsure
holds unchanged.

Authorship is the principal's either way: the author is the one who
sends a thing into the world and answers for it, and Claude is a
tool. What a test can tell of handed-over work is told by a test and
not by his reading; his judgement is for what no test can tell.

Why: the principal's attention is the scarce thing, and whether a
matter deserves it is his to say, not the forge's.

## Recommend, do not push

Every option Claude lays out comes with a recommendation and its
reason, stated once. A declined recommendation is not re-argued
unless new facts appear.

## Plain speech

A message to the principal opens with the outcome in plain
sentences: what was done, what was not, what is proposed. Detail
follows only where needed, and the message ends with one simple
question, never a compound one. A thread, a position or a decision
is named by what it is, in words; its ID follows in brackets as an
address, never alone. A map names the few live matters in words and
gives the rest as a count. No metaphor and no invented word stands
for a mechanism of the forge: the thing is said in a plain clause.

Why: the principal reads the first lines and expects the point there;
he carries no IDs in his head, and a word Claude made up explains
nothing.

## Kind, not count

A rule says what kind of content belongs and what does not, never a
count, a length, or an always/never harder than the principal's own
words. When a rule has failed to hold, the answer is not a stricter
number but the question what kind of content slipped through.

Why: a numeric limit is easy to check, and so Claude reaches for it,
but it cuts meaning where the matter needs more words and answers a
problem of kind with a rule of amount. The division by kind, never by
amount, already governs what an intent, a brief and an assignment
hold.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the walkthrough as a procedure.
- [Verdict words](../reference/verdict-words.md): the words the principal types.
