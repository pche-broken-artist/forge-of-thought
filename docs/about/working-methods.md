---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: d713b4f8e554641f
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
between the principal (the person whose thinking is forged) and
Claude. Together they are the forge's vocabulary of collaboration.
This page says what each method is and why it exists. It is for
someone who works with the forge and wants to know what to expect of
a conversation and which word steers it. It is also for someone who
evaluates the forge and asks why the conversation runs this way.

## What it is

A working method is a way of conducting a conversation, and it has a
name. The name has two uses. The principal can invoke the method in
a word. The definition of a command and the README can refer to the
method by its name.

No method is a command. A command has one input and starts on
demand. A method applies whenever its situation arises, whatever
produced that situation.

Some terms of the forge stand on this page without an explanation,
such as intent, artefact, thread and agent. Each is said in one line
in the [Glossary](../reference/glossary.md).

## How it works

### Walkthrough

A walkthrough is the way a list of items that need the principal's
decision is worked, whatever produced the list. Such a list holds,
for example:

- critique findings
- challenges
- the differences between two requirement sets
- open threads
- TBC items (items still to be confirmed)
- the proposals of a source

Claude puts one item in front of the principal in one message and
stops. The items come in order of weight. The principal gives his
verdict. The next message opens with one line that acknowledges the
verdict and then carries the next item, nothing else. A table that
asks for every verdict at once is never put in front of the
principal. Neither is a questionnaire of several questions.

An item carries three things, in this order:

1. what the item says and the situation or evidence behind it
2. what would change and for whom
3. the recommendation with its reason and, for `accept`, the concrete
   text the artefact would receive

Every item ends in one proposition. In its wording `accept` has
exactly one meaning: yes to what is in front of the principal. The
message closes with the verdict line:

```
(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```

The verdict words are one set for every walkthrough:

- `accept`: agreed, the text goes in as shown.
- `modify`: a discussion opens on the item, and the solution found
  is put forward to be accepted.
- `question`: the principal asks about the open item. Nothing
  changes and nothing is written. Claude answers and closes the item
  again with the verdict line.
- `reject`: not agreed, nothing changes, the reason is recorded.
- `park`: not now. The item waits and comes back.
- `obsolete`: no longer relevant, with a note why.

The principal may answer the line with a single letter when that
letter is his whole message. No other word of the forge has a
letter: `write`, `obsolete` and every command are typed in full. The
words the principal types are the page
[Verdict words](../reference/verdict-words.md).

The verdicts are carried in the conversation and written once, at
the end of the round. A round is one working conversation: see One
write per round below.

Whatever produces a list that needs a decision ends by offering a
walkthrough:

- `/critique`
- `/challenge`
- the `/forge` map
- a comparison made on request

The principal may also call for a walkthrough at any moment. The
full shape of a walkthrough is defined in
`.claude/skills/walkthrough/SKILL.md`. The walkthrough as a
procedure is the page
[Walk through a list](../use/walk-through-a-list.md).

One rule of the walkthrough is repeated to Claude at every prompt. A
hook (the script `scripts/hook-walkthrough.py`, which runs at every
prompt) repeats:

- the one-item rule with the verdict line
- a pointer to the full shape of a walkthrough
- lines of conduct

### Propose, never decide

Claude criticises, challenges, inspires and lays out options. The
principal composes.

The sign `??` asks for Claude's honest opinion of what the principal
has just written. It counts when it stands alone at the end of his
message or is his whole message. Claude answers with three points at
most, marked as its own. Nothing is written or filed. The sign adds
to Claude's duty to say at once what does not fit and never replaces
that duty. It is not the isolated challenger either: the challenger
does not know the conversation.

### Step by step

Any action that needs the principal's consent arrives as one step.
The step states the exact operation, its target and the reason. It
runs on the principal's word. Such actions are:

- a write
- a commit
- a push
- a rename
- a change of a setting
- anything hard to reverse
- a run of several agents, which arrives with the model and the size
  said
- the birth of a new versioned document (a brief, a recipe, a layer
  of the chain), which happens on the principal's word and never as
  a by-product of another operation

A plan the principal has seen is not consent for its steps. A batch
of sensitive operations is never run as one.

Every such step closes with the verdict line of the walkthrough, and
the principal's word is then a letter. A remark, a question or a
counter-thought in answer to "shall I change it?" is not a yes. It
is input for a reworked proposal, which Claude puts to him again. A
message that says yes and asks a question is `question`, never
consent.

The same line closes every question that asks the principal to
decide:

- a choice between options
- an either/or
- whether to write

Each is one proposition, with Claude's recommendation as what
`accept` means. Only a question for information Claude lacks closes
with the question alone.

### Elicitation interview

Claude draws out by questions what the principal has not yet
articulated. It asks one question per message and acknowledges the
answer before it asks the next. The shape is that of the
walkthrough. The interview is the heart of `/forge intent` (the
command under which the intent is worked).

The interview is the form a conversation takes. Elicitation itself
is the process of finding an artefact, and it uses research and
sources beside the interview. That process is the page
[Elicitation](elicitation.md).

### In pieces

The principal may send one longer thought as several messages, a
piece at a time, and close it with a word such as "done". Until that
word Claude answers each piece with at most one line of
acknowledgement. It adds no question, no analysis and no warning.
After the closing word the pieces are one input, read and worked as
a whole. One input is one write: a brief dictated this way moves one
version per block, not per sentence. In pieces is not a mode. It is
one input split for the sender's comfort.

### Draft early

An early draft is an elicitation tool, not an output.

### Reflect back

Before anything is written, Claude restates what it understood the
principal to have said. Reflect back is the companion of one write
per round.

### One write per round

A working conversation is one round. What is agreed in it is carried
in the conversation and written once at its end, on the principal's
word. The word is `write`, typed in full. On `write` Claude reflects
the whole round back and writes on the principal's yes. Claude
offers the word beside the verdict line when the round looks
finished.

A round moves the version of a document once, however many answers
the round contained. Each change gets one record in the history of
the document. The principal may at any moment order a write of
whatever is agreed so far. Unless he says otherwise, the round stays
open after such a write. A correction that lands on text written
moments ago belongs to the round that wrote it. It is carried like
any other answer.

"Written" means a file. Whenever Claude reports something as
written, it names the file and the section. Whatever is carried only
in the conversation is said to be nowhere yet. Claude never says
that nothing is lost while anything lives only in the conversation.

### Intent-first

A change of substance goes into the intent first. From there it
propagates down the whole chain the project has: each lower layer,
such as the assignment, the BRD or the solution design, is brought
to it.

The need for the change may show in any layer. When solving shows
that what is wanted cannot be had, or must be wanted differently,
the intent changes first and the layers follow. If the principal
dictates substance straight into a lower layer, Claude proposes the
matching change of the intent in the same step. Only wording is
fixed in a lower layer directly.

### Handing over

How an artefact is composed is the principal's choice, made artefact
by artefact. There are two ways:

- Found together: the principal finds the artefact with Claude by
  elicitation. Where Claude is unsure, it asks and fills no gap by
  assumption.
- Handed over: the principal gives a few sentences of what he wants.
  Claude composes the whole and returns it for his judgement.

Handed over, Claude works the definition of the artefact alone,
within the bounds the principal sets. The definition says what must
be found. Claude finds it from what it was given, from research and
from the sources. It returns a proposal. With the proposal comes a
short list of what Claude assumed and what it chose, each choice
with what it was chosen against. The same is said in plain words in
the artefact, at the place each stands, until the principal has
judged it.

Nothing is derived from the proposal and nothing is done on it
before the principal has judged it. Handing over covers making the
proposal, never changing it while he judges it. What a test can tell
of work handed over is told by a test and not by his reading. His
judgement is for what no test can tell.

Authorship is the principal's either way. The author is the one who
sends a thing into the world and answers for it. Every definition is
written to be worked either way.

### Recommend, do not push

Every option Claude lays out comes with its recommendation and the
reason, stated once. A declined recommendation is not argued again
without new facts.

### Plain speech

Every message to the principal opens with the outcome in plain
sentences:

- what was done
- what was not
- what is proposed

Detail follows only where it is needed. The message ends with one
simple question, never a compound one. A thread, a position or a
decision is named by what it is, in words. Its ID follows in
brackets as an address and never stands alone. No metaphor and no
invented word stands for a mechanism of the forge: the thing is said
in a plain clause.

### Kind, not count

A rule that Claude proposes says what kind of content belongs and
what does not. It never sets a count or a length. It never sets an
always or a never harder than the principal's own words. When a rule
has failed to hold, the answer is not a stricter number. The answer
is the question what kind of content slipped through.

## Why

- **Walkthrough.** An item carries its situation, the change and the
  recommendation with the concrete text. The purpose is that the
  principal can decide without asking for an explanation. `question`
  is a verdict of its own and writes nothing. The purpose is that a
  question is never mistaken for a modification or a yes. Only the
  five verdicts of the line have a letter. The purpose is that
  nothing which writes or saves can be set off by a slip. The
  one-item rule is repeated at every prompt for this reason: text
  loaded once dissolves as the conversation grows. A rule that must
  hold in a long conversation is therefore not trusted to
  `CLAUDE.md` alone (the file that states the methods, which Claude
  loads once). The repetition is a trial, judged by behaviour. Why a
  list is worked one item per message and not as a whole: the reason
  is not recorded.
- **Propose, never decide.** The reason is not recorded.
- **Step by step.** Consent is given to a concrete operation, never
  to its description. A step that is hard to reverse must be seen by
  the principal at the moment it happens, not in a plan read
  earlier. The verdict line closes the step for two purposes. The
  principal's word is a letter. A yes that carries a question is
  `question` and not consent. The same line closes every question
  that asks for a decision, and the purpose is that every decision
  is answered in the same system.
- **Elicitation interview.** The interview stands where an
  assumption would otherwise stand: Claude asks rather than fills a
  gap.
- **In pieces.** The pieces are incomplete. A question would ask
  what the principal is about to write.
- **Draft early.** Concrete text sharpens the principal's reaction.
- **Reflect back.** The write is then a confirmation and not a
  surprise.
- **One write per round.** Writing after every exchange buries the
  substantive change under changelog churn and makes the history
  unreadable. Claude offers `write` beside the verdict line for a
  purpose of its own: the principal always sees both ways to go on.
  The method has a name for one purpose: the principal invokes it in
  a word.
- **Intent-first.** The rule is stated without a reason: the reason
  is not recorded.
- **Handing over.** The principal's attention is the scarce thing.
  Whether a matter deserves it is his to say, not the forge's. The
  list of assumptions and choices has a purpose of its own: he
  judges decisions and not prose.
- **Recommend, do not push.** The reason is not recorded.
- **Plain speech.** The principal reads the first lines and expects
  the point there. He carries no IDs in his head. A word Claude made
  up explains nothing.
- **Kind, not count.** A numeric limit is easy to check, and so
  Claude reaches for it. It cuts meaning where the matter needs more
  words. It answers a problem of kind with a rule of amount. The
  division by kind, never by amount, already governs what an intent,
  a brief and an assignment hold.

## A worked example

A conversation on the project `my-project` has left three points
open that need the principal's decision. He invokes a method in a
word: he types "walkthrough".

1. Claude puts the heaviest point in front of him and nothing else.
   An earlier answer of his sets the reply time at two days, a later
   one leaves it open. Claude says what would change and for whom,
   gives its recommendation with the reason and shows the sentence
   the document would receive. The message closes with
   `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`.
2. The principal types `q`. Claude names the verdict in full, says
   that nothing changes and nothing is written, and asks what he
   wants to ask. He asks whether the two days are working days.
   Claude answers and closes the item again with the verdict line.
3. The principal types `a`. Claude's next message opens with one
   line that acknowledges `accept` and then carries the second
   point. He parks it with `p`: the item waits and comes back. He
   accepts the third with `a`.
4. The round looks finished, and Claude offers the word `write`
   beside the verdict line. The principal types `write`. Claude
   reflects the whole round back: two sentences agreed, one point
   parked, nothing of it in a file yet. A write is a step that needs
   his consent. The reflection therefore closes with the verdict
   line.
5. The principal types `a`. Claude writes everything as one round
   and names the file and the section it wrote.

The one word brought four methods into play:

- the walkthrough
- step by step
- reflect back
- one write per round

## See also

- [Walk through a list](../use/walk-through-a-list.md): the
  walkthrough as a procedure.
- [Elicitation](elicitation.md): the process the elicitation
  interview is one instrument of.
- [Verdict words](../reference/verdict-words.md): the words the
  principal types.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
