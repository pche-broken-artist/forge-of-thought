---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: cdeb6c4013693604
inputs:
  - CLAUDE.md#Working methods
  - .claude/skills/walkthrough/SKILL.md
  - projects/forge/10-intent.md#Working methods
  - projects/forge/10-intent.md#POS.1410
---

# The working methods

The working methods are the named ways a working conversation in the
forge runs: its vocabulary of collaboration between the principal
(the person whose thinking is being forged, and the final authority
on its content) and Claude. This page is for a user who wants to know
how a conversation with Claude will go, and for an evaluator who
wants to know why it goes that way. It says what each method is and
the reason given for it.

## What it is

A working method is a way of working that applies whenever its
situation arises. None is a command. A command has one input and
starts on demand; a method applies whatever produced its situation.
Each method has a name, so that the definitions of the commands and
the README can refer to it. The principal can also invoke any method
in a word.

The forge has these methods, in this order:

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

The short meaning of every term of the forge used here is in the
[Glossary](../reference/glossary.md).

## How it works

### Walkthrough

A walkthrough is the way a list of items needing the principal's
decision is worked: one item per message, in order of weight. The
list may be any of these:

- critique findings;
- challenges;
- the differences between two requirement sets;
- open threads;
- open questions before a handover;
- proposals of a source.

Claude puts one item in front of the principal and stops. An item
carries what it says and the evidence behind it, what would change
and for whom, and Claude's recommendation with its reason. Where the
recommendation is to accept, the item shows the concrete text the
document would receive, not a description of the edit. A table that
asks for every verdict at once is never put in front of the
principal, and neither is a questionnaire of several questions.

Every item ends in one proposition, worded so that `accept` has
exactly one meaning: yes to what is in front of the principal. The
message closes with the verdict line:

```
(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

The verdict words are one set for every walkthrough, whatever
produced the list:

- `accept`: agreed, the text goes in as shown.
- `modify`: a discussion opens on the item, and the solution found
  is put forward to be accepted.
- `question`: the principal asks about the open item; nothing
  changes, Claude answers and closes the item again with the verdict
  line.
- `reject`: not agreed, nothing changes, the reason is recorded.
- `park`: not now; the item waits and comes back.
- `obsolete`: no longer relevant, with a note why.

The principal may answer with a single letter (`a`, `m`, `q`, `r` or
`p`) when that letter is his whole message. No other word of the
forge has a letter. `write`, `obsolete` and every command are typed
in full. The words themselves are listed in
[Verdict words](../reference/verdict-words.md), and the walkthrough
as a procedure you follow is
[Walk through a list](../use/walk-through-a-list.md).

The verdicts are carried in the conversation and written once, at
the end of the round. Whatever produces a list ends by offering a
walkthrough: `/critique`, `/challenge`, the state map of `/forge`,
and a comparison made on request. The principal may also call for
one at any moment.

A hook (a small script that runs automatically at every prompt the
principal sends) repeats the one-item rule and four lines of conduct
each time. It is `scripts/hook-walkthrough.py`, configured in
`.claude/settings.json`. The full shape of a walkthrough is read from
`.claude/skills/walkthrough/SKILL.md` whenever a walkthrough or an
interview runs.

### Propose, never decide

Claude criticises, challenges, inspires and lays out options. The
principal composes.

The sign `??` asks for Claude's honest opinion of what the principal
has just written. It works when it stands alone at the end of his
message, or as his whole message. Claude answers with three points at
most, marked as its own, and nothing is written or filed. This is not
the isolated challenger (a reviewer that runs without seeing the
conversation). It adds to Claude's duty to say at once what does not
fit, and never replaces that duty.

### Step by step

Any action needing the principal's consent arrives as one step.
Such actions include a write, a commit, a push, a rename, and
anything hard to reverse. The step states the exact operation, its
target and the reason, and it runs on the principal's word.

- A plan the principal has seen is not consent for its steps.
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

Each of these is one proposition, and `accept` means Claude's
recommendation. Only a question for information Claude lacks closes
with the question alone. A message that says yes and asks a question
is `question`, never consent.

### Elicitation interview

Claude draws out by questions what the principal has not yet
articulated. It asks one question per message, and acknowledges the
answer before it asks the next. The shape is the walkthrough's. The
interview is the form a conversation takes. Elicitation itself is the
process of finding a document of the chain, and it uses research and
sources beside the interview: see [Elicitation](elicitation.md).

### In pieces

The principal may send one longer thought as several messages, a
piece at a time. He closes it with a word such as "done". Until that
word, Claude answers each piece with at most one line of
acknowledgement: no question, no analysis, no warning. After it, the
pieces are one input, read and worked as a whole. One input is one
write, so a brief dictated this way moves one version per block, not
per sentence. It is not a mode: it is one input split for the
sender's comfort.

### Draft early

An early draft is a tool for drawing out what the principal wants,
not an output.

### Reflect back

Before anything is written, Claude restates what it understood the
principal to have said. It is the companion of one write per round.

### One write per round

A working conversation is one round. What is agreed in it is carried
in the conversation and written once, at its end, on the principal's
word. The word that orders the write is `write`, typed in full. On
`write`, Claude reflects the whole round back and writes on the
principal's yes. When the round looks finished, Claude offers `write`
beside the verdict line. Until the write, everything agreed is
nowhere yet, and Claude says so.

### Intent-first

A change of substance goes into the intent first and propagates from
there down the whole chain the project has. This holds whichever
layer showed the need for it. A change may come from below, when
solving shows that what is wanted must change; then the intent
changes first. Only wording is fixed downstream directly.

### Handing over

How a document of the chain is composed is the principal's choice,
made document by document. He finds it together with Claude by
elicitation, or he hands it over with a few sentences of what he
wants.

Handed over, Claude works the document's definition alone. It works
from what it was given, from research and from the sources, within
the bounds the principal sets. It returns a proposal with a short
list of what it assumed and what it chose. Each choice comes with
what it was chosen against. The same is said in plain words in the
document, at the place where it stands, until the principal has
judged it. Nothing is derived from the proposal, and nothing is done
on it, before his judgement. What a test can tell of the work is told
by a test, and the principal's judgement is for what no test can
tell.

Found together, the first rule of the forge holds as it stands: where
Claude is unsure it asks, and it fills no gap by assumption.

### Recommend, do not push

Every option Claude lays out comes with a recommendation and its
reason, stated once. A declined recommendation is not argued again
unless new facts appear.

### Plain speech

A message to the principal opens with the outcome in plain
sentences: what was done, what was not, what is proposed. Detail
follows only where needed. The message ends with one simple question,
never a compound one.

A thread, a position or a decision is named by what it is, in words.
Its ID follows in brackets as an address, never alone. A state map
names the few live matters in words and gives the rest as a count.
No metaphor and no invented word stands for a mechanism of the forge:
the thing is said in a plain clause.

### Kind, not count

A rule says what kind of content belongs and what does not. It never
sets a count or a length. When a rule has failed to hold, the answer
is not a stricter number. The answer is the question what kind of
content slipped through.

## Why

- **Walkthrough, one item per message.** Text loaded once dissolves
  as the conversation grows. That is why a hook repeats the one-item
  rule at every prompt instead of trusting the rules file alone. A
  hook is context, not enforcement. It is the nearest thing to a wall
  that the harness (the program Claude runs in) offers.
- **The verdict `question`.** It exists so that a question is never
  mistaken for a modification or a yes.
- **Letters for the verdicts only.** No other word has a letter so
  that nothing which writes or saves can be set off by a slip.
  `question` writes nothing.
- **The verdict line on every decision.** It closes every question
  that asks the principal to decide so that every decision is
  answered in the same system.
- **Propose, never decide.** Authorship is the principal's: the
  author is the one who sends a thing into the world and answers for
  it, and Claude is a tool.
- **Step by step.** Consent is given to a concrete operation, never
  to its description. This is because a step hard to reverse must be
  seen by the principal at the moment it happens, not in a plan read
  earlier. A remark or a question is input for a revised proposal,
  in handed-over work as in joint work. Handing over covers making
  the proposal, never changing it while the principal judges it. The
  verdict line closes every step so that the word is a letter, and so
  that a yes that carries a question is `question`. The reason a run
  of several agents must state its model and its size is not
  recorded.
- **Elicitation interview.** It draws out by questions rather than
  filling gaps by assumption.
- **In pieces.** Claude asks nothing until the closing word. This is
  because the pieces are incomplete, and a question would ask what
  the principal is about to write.
- **Draft early.** Concrete text sharpens the principal's reaction.
- **Reflect back.** It is done so that the write is a confirmation
  and not a surprise.
- **One write per round.** The method exists for its name, so that
  the principal can invoke it in a word. It stands beside the
  walkthrough, whose verdicts reach the write this way. Claude offers
  `write` beside the verdict line so that the principal always sees
  both ways on. The reason the rule writes once rather than item by
  item is not recorded.
- **Intent-first.** The reason is not recorded.
- **Handing over.** The principal's attention is the scarce thing,
  and whether a matter deserves it is his to say, not the forge's.
  Claude lists what it assumed and chose so that the principal judges
  decisions and not prose.
- **Recommend, do not push.** The reason is not recorded.
- **Plain speech.** The principal reads the first lines and expects
  the point there. He carries no IDs in his head. A word Claude made
  up explains nothing.
- **Kind, not count.** A numeric limit is easy to check, and so
  Claude reaches for it. But it cuts meaning where the matter needs
  more words. It also answers a problem of kind with a rule of
  amount.

## A worked example

The principal runs a critique on a project `my-project`, and it
returns three findings. The critique ends by offering a walkthrough,
and the principal accepts. Claude puts the heaviest finding in front
of him alone:

> A requirement of the assignment uses "should" where the style asks
> for "shall". Readers of the assignment would read it as optional.
> Recommended: change it to "The service shall log every request."
>
> (a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark

The principal answers `q` and nothing else. Claude asks what he wants
to ask. He asks whether other requirements have the same wording.
Claude answers, and closes the same finding again with the verdict
line. Nothing has changed and nothing is written. The principal now
answers `a`. Claude's next message opens with one line naming the
verdict ("accepted, carried to the write") and then carries the
second finding, nothing else.

After the third finding, Claude offers `write` beside the verdict
line. The principal types `write`. Claude reflects the whole round
back: the new wording of each accepted finding and what is recorded
for the others. On the principal's yes, it writes the round as one
version.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the
  walkthrough as a procedure.
- [Elicitation](elicitation.md): the process the elicitation
  interview is one instrument of.
- [Verdict words](../reference/verdict-words.md): the words the
  principal types.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
