---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 88bf489bb59ab636
inputs:
  - CLAUDE.md#Working methods
  - .claude/skills/walkthrough/SKILL.md
  - projects/forge/10-intent.md#Working methods
  - projects/forge/10-intent.md#POS.1410
---

# The working methods

The working methods are the named ways a working conversation
between the principal (the person whose thinking is being forged)
and Claude runs. This page is for anyone who works with the forge or
weighs it. It says what each method is and why it exists, in the
order the forge itself keeps them.

## What it is

The working methods are the forge's vocabulary of collaboration.
None of them is a command. A command has one input and starts on
demand. A method applies whenever its situation arises, whatever
produced that situation. Each method has a name. The definitions of
the commands and the README can refer to it by that name. The
principal can invoke any method in a word.

There are thirteen methods:

- Walkthrough
- Propose, never decide
- Step by step
- Elicitation interview
- In pieces
- Draft early
- Reflect back
- One write per round
- Intent-first
- Handing over
- Recommend, do not push
- Plain speech
- Kind, not count

## How it works

### Walkthrough

A walkthrough is the way any list of items that needs the
principal's decision is worked. Such lists include critique
findings, challenges, the differences between two requirement sets,
open threads, open questions before a handover and the proposals of
a source. The items are worked one per message, in order of weight.
The steps of a walkthrough as a procedure are on
[Walk through a list](../use/walk-through-a-list.md).

Claude puts one item in front of the principal and stops. An item
carries, in this order:

- what the item says, and the situation or evidence behind it;
- what would change, and for whom;
- the recommendation with its reason, and for `accept` the concrete
  text the artefact would receive, never a description of the edit.

Every item ends in one proposition. The proposition is worded so
that `accept` has exactly one meaning: yes to what is in front of
the principal. That holds also where the proposition goes against
the reviewer's suggestion. The message closes with the verdict line:

```
(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

The verdict words are one set for every walkthrough, whatever
produced the list:

- `accept`: agreed, the text goes in as shown.
- `modify`: a discussion opens on the item, and the solution found
  is put forward to be accepted.
- `question`: the principal asks about the open item. Nothing
  changes and nothing is written. Claude answers and closes the item
  again with the verdict line.
- `reject`: not agreed, nothing changes, the reason is recorded.
- `park`: not now. The item waits and comes back.
- `obsolete`: no longer relevant, with a note why.

The principal may answer the verdict line with a single letter when
that letter is his whole message. No other word of the forge has a
letter: `write`, `obsolete` and every command are typed in full. The
words the principal types are listed on
[Verdict words](../reference/verdict-words.md).

The next message opens with one line that acknowledges the verdict
and then carries the next item. A table that asks for every verdict
at once, or a questionnaire of several questions, is never put in
front of the principal. The verdicts are carried in the conversation
and written once at the round's end.

Whatever produces a list ends by offering a walkthrough. That
includes `/critique`, `/challenge`, the state map of `/forge` and a
comparison made on request. The principal may also call for a
walkthrough at any moment.

A per-prompt hook repeats the one-item rule and four lines of
conduct at every prompt. A hook here is a small script that runs at
every prompt of the principal and puts its text in front of Claude.
It is `scripts/hook-walkthrough.py`, configured in
`.claude/settings.json`. A hook is context, not enforcement.

### Propose, never decide

Claude criticises, challenges, inspires and lays out options. The
principal composes.

The sign `??` asks for Claude's honest opinion of what the principal
has just written. It works alone at the end of his message, or as
his whole message. Claude answers with three points at most, marked
as its own. Nothing is written or filed. This is not the isolated
challenger, which does not know the conversation. It adds to
Claude's duty to say at once what does not fit, and never replaces
that duty.

### Step by step

Any action that needs the principal's consent arrives as one step.
Such actions include a write, a commit, a push, a rename and
anything hard to reverse. The step states the exact operation, its
target and the reason, and it runs on his word.

- A plan he has seen is not consent for its steps.
- A batch of sensitive operations is never run as one.
- A run of several agents is such a step. It arrives with the model
  and the size said.
- The birth of a new versioned document (a brief, a recipe, a layer
  of the chain) is such a step. It happens on the principal's word,
  never as a by-product of another operation.

A remark, a question or a counter-thought in answer to "shall I
change it?" is not a yes. The proposal is reworked and asked again.

Every such step closes with the walkthrough's verdict line. So does
every question that asks the principal to decide:

- a choice between options;
- an either/or;
- whether to write.

Each is one proposition, and Claude's recommendation is what
`accept` means. Only a question for information Claude lacks closes
with the question alone.

### Elicitation interview

Claude draws out by questions what the principal has not yet
articulated. It asks one question per message and acknowledges the
answer before it asks the next. The interview follows the shape of
the walkthrough. The interview is the form a conversation takes.
Elicitation itself is the process of finding an artefact, and it
uses research and sources beside the interview. That process is
described on [Elicitation](elicitation.md).

### In pieces

The principal may send one longer thought as several messages, a
piece at a time. He closes it with a word such as "done". Until that
word, Claude answers each piece with at most one line of
acknowledgement: no question, no analysis, no warning. After it, the
pieces are one input, read and worked as a whole. One input is one
write, so a brief dictated this way moves one version per block, not
per sentence.

### Draft early

An early draft is an elicitation tool, not an output.

### Reflect back

Before anything is written, Claude restates what it understood the
principal to have said. Reflect back is the companion of one write
per round.

### One write per round

A working conversation is one round. What is agreed in it is carried
in the conversation and written once at its end, on the principal's
word. The word that orders the write is `write`, typed in full.
Claude then reflects the whole round back and writes on the
principal's yes. When the round looks finished, Claude offers the
word `write` beside the verdict line. The verdicts of a walkthrough
reach the write this way.

### Intent-first

A change of substance goes into the intent first and propagates from
there down the whole chain the project has. A change may come from
below, when solving shows that what is wanted must change. Then the
intent changes first. Only wording is fixed downstream directly.

### Handing over

How an artefact is composed is the principal's choice, artefact by
artefact. He finds it together with Claude by elicitation, or he
hands it over with a few sentences of what he wants. Authorship is
his either way.

Handed over, Claude works the artefact's definition alone. It works
from what it was given, from research and from the sources, within
the bounds the principal sets. It returns a proposal, and with it a
short list of what it assumed and what it chose. Each choice comes
with what it was chosen against. The same is said in plain words in
the artefact, at the place each choice stands, until the principal
has judged it. Nothing is derived from the proposal and nothing is
done on it before his judgement. Found together, the rule holds as
it stands: where Claude is unsure, it asks and fills no gap by
assumption.

### Recommend, do not push

Every option comes with a recommendation and its reason, stated
once. A declined recommendation is not re-argued without new facts.

### Plain speech

A message opens with the outcome in plain sentences and ends with
one simple question. A thread, a position or a decision is named by
what it is. Its ID follows in brackets as an address, never alone.
No invented word stands for a mechanism of the forge.

### Kind, not count

A rule says what kind of content belongs and what does not. It never
sets a count or a length. A rule that failed is not answered with a
stricter number. It is answered with the question what kind of
content slipped through.

## Why

The reasons, method by method, as far as they are recorded:

- **The names.** Each method has a name so that it can be referred
  to and invoked in a word.
- **Walkthrough.** The verdict line closes every decision, in a
  walkthrough and outside it, so that every decision is answered in
  the same system. `question` is a verdict of its own so that a
  question is never mistaken for a modification or a yes. Only the
  verdict words have a letter. The purpose is that nothing which
  writes or saves can be set off by a slip, and `question` writes
  nothing.
- **The hook beside the walkthrough.** Text loaded once dissolves as
  the conversation grows. A rule that must hold in a long
  conversation is therefore repeated at every prompt and not trusted
  to `CLAUDE.md` alone. Only a sentence and a pointer are always on.
  The detail is a file read when its situation arises.
- **Propose, never decide.** The reason for the method is not
  recorded here. `??` is one sentence under this method and not a
  method of its own. The reason is the size of `CLAUDE.md`.
- **Step by step.** Consent is given to a concrete operation, never
  to its description. Because a step hard to reverse must be seen by
  the principal at the moment it happens, a plan read earlier does
  not count. A yes is a yes and nothing else is. A remark or a
  question is input for a revised proposal, never a licence to edit.
  The verdict line closes the step so that the principal's word is a
  letter, and a yes that carries a question is `question`.
- **Elicitation interview.** Claude draws out what the principal has
  not articulated rather than filling gaps by assumption.
- **In pieces.** The pieces are incomplete. A question would ask what
  he is about to write. It is not a mode: it is one input, split for
  the sender's comfort.
- **Draft early.** Concrete text sharpens the principal's reaction.
- **Reflect back.** The write is then a confirmation, not a surprise.
- **One write per round.** The method exists for its name, so that
  the principal can invoke it in a word. The word `write` is offered
  beside the verdict line so that the principal always sees both
  ways on. The reason for the rule itself is not recorded here.
- **Intent-first.** The reason is not recorded here.
- **Handing over.** The principal's attention is the scarce thing.
  Whether a matter deserves it is his to say, not the forge's.
  Choices are listed so that the principal judges decisions, not
  prose. The author is the one who sends a thing into the world and
  answers for it, and Claude is a tool.
- **Recommend, do not push.** The reason is not recorded.
- **Plain speech.** The principal reads the first lines and expects
  the point there. He carries no IDs in his head. A word Claude made
  up explains nothing.
- **Kind, not count.** A numeric limit is easy to check, and so
  Claude reaches for it. But it cuts meaning where the matter needs
  more words, and it answers a problem of kind with a rule of
  amount. The division by kind, never amount, already governs what
  an intent, a brief and an assignment hold.

## A worked example

A critique has returned three findings on a project `<slug>`. Its
list ends with the offer of a walkthrough, and the principal accepts
it.

1. Claude puts the weightiest finding in front of him: what it says
   and where, what would change, its recommendation, and the exact
   new text of the item. The message ends with
   `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`.
2. The principal types `q` alone. Claude asks what he wants to ask.
   He asks whether the new text narrows the item. Claude answers,
   nothing is written, and the item closes again with the verdict
   line.
3. The principal types `a`. The next message opens with one line
   naming the verdict in full ("accepted") and what it does, then
   carries the second finding, and nothing else.
4. The second finding gets `p`. It waits and comes back.
5. After the third finding Claude offers `write` beside the verdict
   line. The principal types `write`. Claude reflects the whole
   round back. On his yes, everything carried is written as one
   round.

Until step 5, everything agreed lives only in the conversation and
is nowhere yet.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the
  walkthrough as a procedure.
- [Elicitation](elicitation.md): the process the elicitation
  interview is one instrument of.
- [Verdict words](../reference/verdict-words.md): the words the
  principal types.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
