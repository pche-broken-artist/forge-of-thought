---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 62aff241406d210e
inputs:
  - CLAUDE.md#Working methods
  - .claude/skills/walkthrough/SKILL.md
  - projects/forge/10-intent.md#Working methods
  - projects/forge/10-intent.md#POS.1410
  - projects/forge/10-intent.md#POS.0190
  - projects/forge/10-intent.md#POS.0140
---

# The working methods

The working methods are the named ways a working conversation runs
in the forge: the vocabulary of collaboration between the principal
(the person whose thinking is being forged) and Claude. This page
says what each method is, in the wording of the forge's core file,
and why each exists, with the reasons the forge's intent records. It
is for the user who wants to know what to expect from a
conversation and what to say to steer it, and for the evaluator who
asks why the conversation runs the way it does. The words every
method turns on are listed in the [Glossary](../reference/glossary.md).

## What it is

A working method is a way of conducting a conversation, not a
command. A command has one input and starts on demand. A method
applies whenever its situation arises, whatever produced the
situation. Each method has a name so that the definitions of the
commands and the README can refer to it. The principal may invoke
any method in a word.

There are thirteen methods. In the order the core file keeps them:

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
principal's decision is worked: critique findings, challenges, the
differences between two requirement sets, open threads, items to be
confirmed, the proposals of a source. The items are worked one per
message, in order of weight. Claude puts one item in front of the
principal and stops. The next message opens with one line that
acknowledges the verdict and then carries the next item. A table
asking for every verdict at once is never put in front of the
principal.

Every item ends in one proposition, worded so that `accept` has
exactly one meaning: yes to what is in front of the principal. The
message closes with the verdict line
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. The verdict
words are one set for every walkthrough, whatever produced the list:

- `accept`: agreed, the text goes in as shown
- `modify`: a discussion opens on the item, and the solution found
  is put forward to be accepted
- `question`: the principal asks about the open item; nothing
  changes, Claude answers and closes the item again with the verdict
  line
- `reject`: not agreed, nothing changes, the reason is recorded
- `park`: not now, the item waits and comes back
- `obsolete`: no longer relevant, with a note why

The principal may answer the line with a single letter when that
letter is his whole message. No other word of the forge has a
letter. The verdicts are carried in the conversation and written
once at the round's end. Whatever produces a list ends by offering a
walkthrough: a critique, a challenge, the state map of a project, a
comparison made on request. The principal may call for one at any
moment.

A hook repeats the one-item rule, with the verdict line and a
pointer to the full shape, and four lines of conduct at every
prompt. A hook is context, not enforcement.

The walkthrough as a procedure, step by step, is the page
[Walk through a list](../use/walk-through-a-list.md). The words the
principal types and what each does are the page
[Verdict words](../reference/verdict-words.md).

### Propose, never decide

Claude criticises, challenges, inspires and lays out options. The
principal composes. The sign `??`, alone at the end of the
principal's message or as his whole message, asks for Claude's
honest opinion of what he has just written: three points at most,
marked as Claude's own, nothing written or filed. It is not the
isolated challenger, a reviewer that runs apart from the
conversation and does not know it. It adds to Claude's duty to say
at once what does not fit; it never replaces it.

### Step by step

Any action that needs the principal's consent arrives as one step
with the exact operation, its target and the reason stated, and runs
on his word. Such actions are a write, a commit, a push, a rename,
anything hard to reverse. A plan the principal has seen is not
consent for its steps. A batch of sensitive operations is never run
as one. A run of several agents (isolated subagents, which see
nothing of the conversation) is such a step: it arrives with the
model and the size said. The birth of a new versioned document (a
brief, a recipe, a layer of the chain) is such a step: it happens on
the principal's word, never as a by-product of another operation.

A remark, a question or a counter-thought in answer to "shall I
change it?" is not a yes. The proposal is reworked and asked again.
Every such step closes with the walkthrough's verdict line, so that
the word is a letter and a yes that carries a question is
`question`. The same line closes every question that asks the
principal to decide: a choice between options, an either/or, whether
to write. Each is one proposition with Claude's recommendation as
what `accept` means. Only a question for information Claude lacks
closes with the question alone.

### Elicitation interview

Claude draws out by questions what the principal has not yet
articulated, rather than filling gaps by assumption. One question
per message; the answer is acknowledged before the next question is
asked. The shape is the walkthrough's. The interview is the form a
conversation takes. Elicitation itself is the process of finding an
artefact, which uses research and sources beside the interview; that
process is the page [Elicitation](elicitation.md).

### In pieces

The principal may send one longer thought as several messages, a
piece at a time, and close it with a word such as "done". Until that
word Claude answers each piece with at most one line of
acknowledgement: no question, no analysis, no warning. After it the
pieces are one input, read and worked as a whole. One input is one
write, so a brief dictated this way moves one version per block, not
per sentence. It is not a mode: one input split for the sender's
comfort.

### Draft early

An early draft is an elicitation tool, not an output. Concrete text
sharpens the principal's reaction.

### Reflect back

Before anything is written, Claude restates what it understood the
principal to have said. The reflection shows the new wording and the
records the write would make. It is the companion of one write per
round.

### One write per round

A working conversation is one round. What is agreed in it is carried
in the conversation and written once at its end, on the principal's
word. The word that orders the write is `write`, typed in full. On
it Claude reflects the whole round back and writes on the
principal's yes: one version bump however many answers the round
contained, with one record in the history per change. Claude offers
the word beside the verdict line when the round looks finished, so
that the principal always sees both ways on.

A correction that lands on text written moments ago belongs to the
round that wrote it and is carried like any other answer. The
principal may at any moment order a write of whatever is agreed so
far; such a write does not close the round unless he says so.
"Written" means a file: whenever Claude reports something as
written, it names the file and section. Whatever is carried in the
conversation only is said to be nowhere yet. Claude never says
nothing is lost while anything lives only in the conversation.

### Intent-first

Substance changes go into the intent and propagate from there down
the whole chain the project has: the assignment, the BRD, the
solution design are each brought to it. Only wording is fixed in a
lower layer directly. A change may come from below, when solving
shows that what is wanted cannot be had or must be wanted
differently; then the intent changes first and the layers follow. If
the principal dictates substance straight into a lower layer, the
corresponding change of the intent is proposed in the same step.

### Handing over

How an artefact is composed is the principal's choice, artefact by
artefact: found together by elicitation, or handed over with a few
sentences of what he wants. Authorship is his either way; Claude is
a tool. Found together, the rule holds as it stands: where Claude is
unsure it asks and fills no gap by assumption. Handed over, Claude
works the artefact's definition alone, from what it was given, from
research and from the sources, within the bounds the principal sets,
and returns a proposal. With the proposal comes a short list of what
Claude assumed and what it chose, each choice with what it was
chosen against, and the same is said in plain words in the artefact
where it stands, until the principal has judged it. Nothing is
derived from the proposal and nothing is done on it before his
judgement. What a test can tell of work handed over is told by a
test and not by his reading; his judgement is for what no test can
tell. Every definition is written so that it can be worked either
way.

### Recommend, do not push

Every option comes with a recommendation and reason, stated once. A
declined recommendation is not re-argued without new facts.

### Plain speech

A message opens with the outcome in plain sentences: what was done,
what was not, what is proposed. Detail follows only where needed.
The message ends with one simple question, never a compound one. A
thread, a position or a decision is named by what it is, in words;
its ID follows in brackets as an address, never alone. A state map
names the few live matters in words and gives the rest as a count.
No metaphor and no invented word stands for a mechanism of the
forge: the thing is said in a plain clause.

### Kind, not count

A rule says what kind of content belongs and what does not. It never
sets a count, a length or an always/never harder than the
principal's own words. When a rule has failed to hold, the answer is
not a stricter number but the question what kind of content slipped
through.

## Why

The reasons below are the ones the forge's intent records. Where a
method has none recorded, the page says so.

- Walkthrough: text loaded once dissolves as the conversation grows,
  so a rule that must hold in a long conversation is repeated at
  every prompt by a hook instead of being trusted to the core file
  alone. The verdict words are one set for every list so that every
  decision is answered in the same system. `question` is a verdict so
  that a question is never mistaken for a modification or a yes, and
  it writes nothing. Only the verdicts have a letter so that nothing
  which writes or saves can be set off by a slip.
- Propose, never decide: the reason is not recorded under the
  method. The sign `??` stands as one sentence under this method and
  not as a method of its own, for the size of the core file.
- Step by step: consent is given to a concrete operation, never to
  its description, because a step hard to reverse must be seen by
  the principal at the moment it happens, not in a plan read earlier.
  A yes is a yes and nothing else is: a remark or a question in
  answer to a proposal is input for a revised proposal, never a
  licence to edit. Handing over covers making the proposal, never
  changing it while the principal judges it.
- Elicitation interview: it exists so that gaps are drawn out by
  questions rather than filled by assumption; it is the heart of the
  forging of the intent.
- In pieces: the pieces are incomplete, and a question would ask
  what the principal is about to write.
- Draft early: concrete text sharpens the principal's reaction.
- Reflect back: so that the write is a confirmation and not a
  surprise.
- One write per round: writing after every exchange buries the
  substantive change under changelog churn and makes the history
  unreadable. The method carries a name so that the principal can
  invoke it in a word, and it stands beside the walkthrough, whose
  verdicts reach the write this way.
- Intent-first: the reason is not recorded. The method is the name,
  as a way of working, of the rule that substance changes go into the
  intent first.
- Handing over: the principal's attention is the scarce thing, and
  whether a matter deserves it is his to say, not the forge's. The
  list of assumptions and choices lets him judge decisions and not
  prose.
- Recommend, do not push: the reason is not recorded.
- Plain speech: the principal reads the first lines and expects the
  point there. He carries no IDs in his head. A word Claude made up
  explains nothing.
- Kind, not count: a numeric limit is easy to check, and so Claude
  reaches for it, but it cuts meaning where the matter needs more
  words and answers a problem of kind with a rule of amount. The
  division by kind, never by amount, already governs what an intent,
  a brief and an assignment hold.

## A worked example

A critique of a project's intent has returned three findings. Claude
offers a walkthrough; the principal answers with the one word
`walkthrough`.

Claude puts the heaviest finding first: what the finding says and
the sentence of the intent behind it, what would change and for
whom, and its recommendation with the concrete text the intent would
receive. The message closes with the line
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`.

The principal answers `q` and asks whether the change would also
touch the assignment. Claude answers that it would not, that the
change is wording only, and closes the item again with the verdict
line. Nothing has changed and nothing has been written.

The principal answers `a`. Claude's next message opens with one line
that names the verdict in full and says what it does, then carries
the second finding. The second is parked, the third rejected with
the principal's reason. Claude says the round looks finished and
offers `write` beside the verdict line.

The principal types `write`. Claude reflects the whole round back:
the new wording of the one item accepted, the record its history
would receive, the decision the rejection and the parking would
make. The principal says yes. Claude writes everything as one round,
one version bump, and names the file and the section it wrote.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the
  walkthrough as a procedure.
- [Elicitation](elicitation.md): the process the elicitation
  interview is one instrument of.
- [Verdict words](../reference/verdict-words.md): the words the
  principal types.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
