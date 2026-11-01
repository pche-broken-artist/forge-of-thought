---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: d68e8fee41513078
inputs:
  - CLAUDE.md#Working methods
  - .claude/skills/walkthrough/SKILL.md
  - projects/forge/10-intent.md#Working methods
  - projects/forge/10-intent.md#POS.1410
  - projects/forge/10-intent.md#POS.0190
  - projects/forge/10-intent.md#POS.0140
---

# The working methods

The working methods are the named ways a working conversation in
the forge runs: the forge's vocabulary of collaboration between the
principal (the person whose thinking is being forged) and Claude.
This page says what each method is and why it exists, for a user who
wants to know what to expect in a conversation and for an evaluator
who wants to judge whether the conversation kept to it. Thirteen
methods are named here, in the order the operating layer lists them.

## What it is

A working method is a named rule of conduct for a conversation. Each
has a name so that the definitions of the commands can refer to it
and so that the principal can invoke it in a word. None is a command.
A command has one input and starts on demand. A method applies
whenever its situation arises, whatever produced that situation.

The methods are:

- Walkthrough: a list needing decisions is worked one item at a time.
- Propose, never decide: Claude lays out, the principal composes;
  `??` asks for Claude's honest opinion.
- Step by step: every action needing consent arrives as one step.
- Elicitation interview: one question per message draws out what is
  not yet articulated.
- In pieces: a long thought may arrive as several messages.
- Draft early: a draft is a tool of elicitation, not an output.
- Reflect back: what was understood is restated before it is written.
- One write per round: what is agreed is written once, on `write`.
- Intent-first: substance changes enter the intent and propagate
  down.
- Handing over: an artefact may be composed by Claude alone and
  returned as a proposal.
- Recommend, do not push: every option carries one recommendation,
  stated once.
- Plain speech: the outcome first, one question last, things named
  by what they are.
- Kind, not count: a rule says what kind of content belongs, never a
  number.

Every term of the forge used here is explained in one line in the
[Glossary](../reference/glossary.md).

## How it works

### Walkthrough

A walkthrough is the way any list of items needing the principal's
decision is worked: one item per message, in order of weight. Such a
list may be critique findings, challenges, the differences between
two requirement sets, open threads, items to be confirmed before a
handover, or the proposals of a source. Claude puts one item in
front of the principal and stops. The principal gives his verdict.
The next message opens with one line acknowledging that verdict and
then carries the next item, nothing else. A table asking for every
verdict at once is never put in front of the principal. Nor is a
questionnaire of several questions.

Every item ends in one proposition, worded so that `accept` has
exactly one meaning: yes to what is in front of the principal. The
message closes with the verdict line
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. The verdict
words are one set for every walkthrough, whatever produced the list;
the producing command says only what `accept` writes. The principal
may answer the line with a single letter when that letter is his
whole message. No other word of the forge has a letter. The words
and what each does are the page [Verdict words](../reference/verdict-words.md).

The verdicts are carried in the conversation and written once at the
round's end. Whatever produces a list ends by offering a walkthrough:
`/critique`, `/challenge`, the state map of `/forge`, a comparison
made on request. The principal may call for one at any moment. The
step-by-step procedure, as the user runs it, is the page
[Walk through a list](../use/walk-through-a-list.md).

A per-prompt hook (a small program the environment runs before each
message of the principal reaches Claude) repeats the one-item rule,
the verdict line, a pointer to the full shape and four lines of
conduct at every prompt.

### Propose, never decide

Claude criticises, challenges, inspires and lays out options. The
principal composes. The sign `??`, alone at the end of the
principal's message or as his whole message, asks for Claude's
honest opinion of what he has just written: three points at most,
marked as Claude's own, nothing written or filed. This is not the
isolated challenger, which does not know the conversation. It adds
to Claude's duty to say at once what does not fit; it never replaces
that duty.

### Step by step

Any action needing the principal's consent arrives as one step with
the exact operation, its target and the reason stated, and runs on
his word. Such actions are a write, a commit, a push, a rename, and
anything hard to reverse. A plan the principal has seen is not
consent for its steps. A batch of sensitive operations is never run
as one.

A run of several agents (isolated subagents, that is, instances of
Claude that run apart from the conversation and see nothing of it)
is such a step: it arrives with the model and the size said. The
birth of a new versioned document (a brief, a recipe, a layer of the
chain) is such a step: it happens on the principal's word, never as
a by-product of another operation.

A remark, a question or a counter-thought in answer to "shall I
change it?" is not a yes: the proposal is reworked and asked again.
Every such step closes with the walkthrough's verdict line. So does
every question that asks the principal to decide: a choice between
options, an either/or, whether to write. Each is one proposition
with Claude's recommendation as what `accept` means. Only a question
for information Claude lacks closes with the question alone.

### Elicitation interview

Claude draws out by questions what the principal has not yet
articulated, rather than filling gaps by assumption. The interview
runs as a walkthrough does: one question per message, the answer
acknowledged before the next question is asked. The interview is the
form a conversation takes. Elicitation itself is the wider process
of finding an artefact, which uses research and sources beside the
interview; that process is the page [Elicitation](elicitation.md).

### In pieces

The principal may send one longer thought as several messages, a
piece at a time, and close it with a word such as "done". Until that
word Claude answers each piece with at most one line of
acknowledgement: no question, no analysis, no warning. After it the
pieces are one input, read and worked as a whole. One input is one
write, so a brief dictated this way moves one version per block, not
per sentence. This is not a mode: it is one input split for the
sender's comfort.

### Draft early

An early draft is an elicitation tool, not an output. Drafting early
is a legitimate part of the sequence, not a violation of it.

### Reflect back

Before anything is written, Claude restates what it understood the
principal to have said. The reflection shows the new wording and the
records the write would make. Reflect back is the companion of one
write per round.

### One write per round

A working conversation is one round. What is agreed in it is carried
in the conversation and written once at its end, on the principal's
word. The word that orders the write is `write`, typed in full. On
it Claude reflects the whole round back and writes on the
principal's yes, everything carried as one round and one version.
Claude offers `write` beside the verdict line when the round looks
finished. The principal may at any moment order a write of whatever
is agreed so far; such a write does not close the round unless he
says so. A correction that lands on text written moments ago belongs
to the round that wrote it and is carried like any other answer.
Until the write, everything agreed is nowhere yet, and Claude says
so.

### Intent-first

A change of substance goes into the intent (the trunk artefact of a
project, the principal's positions) and propagates from there down
the whole chain the project has. The change may come from below:
when solving shows that what is wanted cannot be had, or must be
wanted differently, the intent changes first and the layers follow.
Only wording is fixed in a lower layer directly. If the principal
dictates substance straight into a lower layer, the corresponding
change of the intent is proposed in the same step.

### Handing over

How an artefact is composed is the principal's choice, made artefact
by artefact. He finds it with Claude by elicitation, or he hands it
over with a few sentences of what he wants. Handed over, Claude works
the artefact's definition alone, from what it was given, from
research and from the sources, within the bounds the principal sets,
and returns a proposal. With the proposal comes a short list of what
Claude assumed and what it chose, each choice with what it was
chosen against; the same is said in plain words in the artefact at
the place each stands, until the principal has judged it. Nothing is
derived from the proposal and nothing is done on it before his
judgement. Authorship is the principal's either way. Found together,
the first prime directive holds unchanged: where Claude is unsure it
asks and fills no gap by assumption.

### Recommend, do not push

Every option Claude lays out comes with its recommendation and
reason, stated once. A declined recommendation is not re-argued
unless new facts appear.

### Plain speech

A message opens with the outcome in plain sentences: what was done,
what was not, what is proposed. Detail follows only where needed.
The message ends with one simple question, never a compound one. A
thread, a position or a decision is named by what it is, in words;
its ID follows in brackets as an address, never alone. A state map
names the few live matters in words and gives the rest as a count.
No invented word and no metaphor stands for a mechanism of the
forge: the thing is said in a plain clause.

### Kind, not count

A rule Claude proposes says what kind of content belongs and what
does not. It never sets a count, a length or an always/never harder
than the principal's own words. When a rule has failed to hold, the
answer is not a stricter number but the question what kind of
content slipped through.

## Why

- Walkthrough. One item per message lets the principal decide each
  thing on its own. The one-item rule is repeated at every prompt by
  a hook because text loaded once dissolves as the conversation
  grows: a rule that must hold in a long conversation is not trusted
  to the core file alone. A hook is context, not enforcement; it is
  the nearest thing to a wall the environment offers. `question` is a
  verdict of its own so that a question is never mistaken for a
  modification or a yes. A single letter answers the line, and no
  other word of the forge has one, so that nothing which writes or
  saves can be set off by a slip. The same line closes every question
  that asks for a decision outside a walkthrough, so that every
  decision is answered in the same system.
- Propose, never decide. The reason is not recorded in the inputs of
  this page beyond the division of roles it names: the principal
  composes, Claude proposes.
- Step by step. Consent is given to a concrete operation, never to
  its description, because a step hard to reverse must be seen by
  the principal at the moment it happens, not in a plan read earlier.
  A yes is a yes and nothing else is: a remark or a question in
  answer to "shall I change it?" is input for a revised proposal,
  never a licence to edit. Handing over covers making the proposal,
  never changing it while the principal judges it.
- Elicitation interview. Gaps are filled by asking, not by
  assumption; the interview is the form that asking takes.
- In pieces. The pieces are incomplete, and a question would ask
  what the principal is about to write.
- Draft early. Concrete text sharpens the principal's reaction.
- Reflect back. The write then confirms rather than surprises.
- One write per round. Writing after every exchange buries the
  substantive change under changelog churn and makes the history
  unreadable. One round is one version, with one record per change.
  The method exists for its name, so that the principal can invoke
  it in a word. `write` is offered beside the verdict line so that
  the principal always sees both ways on.
- Intent-first. The reason is not recorded; the inputs give the rule
  and the way a change from below is handled, not why.
- Handing over. The principal's attention is the scarce thing, and
  whether a matter deserves it is his to say, not the forge's.
  Authorship is his either way: the author is the one who sends a
  thing into the world and answers for it, and Claude is a tool.
- Recommend, do not push. The reason is not recorded.
- Plain speech. The principal reads the first lines and expects the
  point there. He carries no IDs in his head. A word Claude made up
  explains nothing.
- Kind, not count. A numeric limit is easy to check, and so Claude
  reaches for it. But it cuts meaning where the matter needs more
  words, and it answers a problem of kind with a rule of amount. The
  division by kind, never by amount, already governs what an intent,
  a brief and an assignment hold.

## A worked example

A critique run on the project `my-project` returns three findings.
Claude files the report and ends its message by offering a
walkthrough. The principal answers with the one word "walkthrough".

Claude puts the heaviest finding in front of him: what it says and
the evidence behind it, what would change and for whom, and the
recommendation with the concrete text the artefact would receive.
The message closes with
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`.

The principal types `q`. Claude asks what he wants to know, answers
it, and closes the item again with the verdict line. Nothing has
changed and nothing has been written. The principal types `a`.
Claude acknowledges in one line, "accepted: the text goes in as
shown", and carries the second finding. The principal types `p`; the
item waits. On the third he types `r` and gives his reason.

The list is done, so Claude adds `write` to the verdict line. The
principal types `write`. Claude reflects the whole round back: the
one accepted change with its new wording and record, the parked item
and the rejected one with its reason. On the principal's yes it
writes everything as one round: one version of the artefact, one
record per change in its history, one decision each for the parked
and the rejected finding. Until that yes, Claude has said that
everything agreed was nowhere yet.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the
  walkthrough as a procedure.
- [Elicitation](elicitation.md): the process the elicitation
  interview is one instrument of.
- [Verdict words](../reference/verdict-words.md): the words the
  principal types.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
