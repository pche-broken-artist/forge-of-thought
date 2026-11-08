---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: f9cedb23be86eea6
inputs:
  - CLAUDE.md#Working methods
  - .claude/skills/walkthrough/SKILL.md
  - projects/forge/10-intent.md#Working methods
  - projects/forge/10-intent.md#POS.1410
  - projects/forge/10-intent.md#POS.0190
  - projects/forge/10-intent.md#POS.0140
---

# The working methods

The working methods are the named ways a working conversation in the
forge runs: the vocabulary of collaboration between the principal
(the person whose thinking is forged) and Claude. This page says what
each method is, how it works and why it exists, for the user who
works with Claude and for the evaluator who wants to know what
conduct the forge promises. Terms of the forge not explained here are
in the [Glossary](../reference/glossary.md).

## What it is

A working method is a named way of running one situation of a
conversation. Each has a name so that the definitions of the commands
can refer to it and so that the principal can invoke it in a word.
None is a command. A command has one input and starts on demand. A
method applies whenever its situation arises, whatever produced the
situation.

There are thirteen methods. They are listed here in the order the
core file `CLAUDE.md` keeps them:

- Walkthrough
- Propose, never decide (with the sign `??`)
- Step by step
- Elicitation interview
- In pieces
- Draft early
- Reflect back
- One write per round (with the word `write`)
- Intent-first
- Handing over
- Recommend, do not push
- Plain speech
- Kind, not count

## How it works

### Walkthrough

A walkthrough is the way any list of items that needs the principal's
decision is worked. Such a list may be the findings of a critique,
the challenges of a peer review, the differences between two
requirement sets, open threads, open questions before a handover or
the proposals of a source. The items are worked one per message, in
order of weight. Every item ends in one proposition. The proposition
is worded so that `accept` has exactly one meaning: yes to what is in
front of the principal. The message closes with the verdict line
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`.

The verdict words are one set for every walkthrough, whatever
produced the list. They are described in [Verdict
words](../reference/verdict-words.md). The producing command says
only what `accept` writes. The principal may answer the line with a
single letter when that letter is his whole message. No other word of
the forge has a letter.

The verdicts are carried in the conversation and written once at the
end of the round. Whatever produces a list ends by offering a
walkthrough: a critique, a challenge, the state map of a project, a
comparison made on request. The principal may call for one at any
moment. The shape of an item, of a verdict and of the write-up is
defined in `.claude/skills/walkthrough/SKILL.md`, which Claude reads
whenever a walkthrough or an interview runs. The procedure, step by
step, is on the page [Walk through a
list](../use/walk-through-a-list.md).

A per-prompt hook, `scripts/hook-walkthrough.py` configured in
`.claude/settings.json`, repeats the one-item rule and four lines of
conduct at every prompt. The hook is context, not enforcement.

### Propose, never decide

Claude criticises, challenges, inspires and lays out options. The
principal composes.

The sign `??`, alone at the end of the principal's message or as his
whole message, asks for Claude's honest opinion of what he has just
written. The answer is three points at most, marked as Claude's own.
Nothing is written or filed. The sign is not the isolated challenger
(a reviewer that runs apart from the conversation and never sees it).
It adds to Claude's duty to say at once what does not fit and never
replaces it.

### Step by step

Any action that needs the principal's consent arrives as one step.
Such an action is a write, a commit, a push, a rename, anything hard
to reverse. The step states the exact operation, its target and the
reason, and it runs on the principal's word. A plan the principal has
seen is not consent for its steps. A batch of sensitive operations is
never run as one.

A run of several agents is such a step. It arrives with the model and
the size said. The birth of a new versioned document, a brief, a
recipe or a layer of the chain, is such a step too: it happens on the
principal's word, never as a by-product of another operation.

A remark, a question or a counter-thought in answer to "shall I
change it?" is not a yes. The proposal is reworked and asked again.

Every such step closes with the walkthrough's verdict line. So does
every question that asks the principal to decide: a choice between
options, an either/or, whether to write. Each is one proposition with
Claude's recommendation as what `accept` means. Only a question for
information Claude lacks closes with the question alone. A message
that says yes and asks a question is `question`, never consent.

### Elicitation interview

Claude draws out by questions what the principal has not yet
articulated, rather than filling gaps by assumption. The interview
runs one question per message, and the answer is acknowledged before
the next question is asked. The shape is the walkthrough's. The
interview is the form a conversation takes. Elicitation itself is the
process of finding an artefact, which uses research and sources
beside the interview; that process is described on the page
[Elicitation](elicitation.md).

### In pieces

The principal may send one longer thought as several messages, a
piece at a time, and close it with a word such as "done". Until that
word Claude answers each piece with at most one line of
acknowledgement: no question, no analysis, no warning. After that
word the pieces are one input, read and worked as a whole. One input
is one write, so a brief dictated this way moves one version per
block, not per sentence. This is not a mode and no magic: one input
split for the sender's comfort.

### Draft early

An early draft is an elicitation tool, not an output. Drafting early
is not a violation of sequence.

### Reflect back

Before anything is written, Claude restates what it understood the
principal to have said. The reflection shows the new wording and the
records that go with it. Reflect back is the companion of one write
per round.

### One write per round

A working conversation is one round. What is agreed in it is carried
in the conversation and written once at its end, on the principal's
word. This holds for any working conversation over the intent or over
open items, whatever the entry door: an interview on the intent, a
sweep of threads, the resolving of findings. One round is one version
bump, however many answers it contained, with one record in the
history per change.

The word that orders the write is `write`, typed in full. On it
Claude reflects the whole round back and writes on the principal's
yes. Claude offers the word beside the verdict line when the round
looks finished, so that the principal always sees both ways on.

The principal may at any moment order a write of whatever is agreed
so far. Such a write does not close the round unless he says so. A
correction that lands on text written moments ago belongs to the
round that wrote it and is carried like any other answer.

"Written" means a file. Whenever Claude reports something as written,
it names the file and the section. Whatever is carried in the
conversation only is said to be nowhere yet. Claude never says
nothing is lost while anything lives only in the conversation.

### Intent-first

Substance changes go into the intent and propagate from there down
the whole chain the project has: the assignment, the BRD, the
solution design are each brought to it. Only wording is fixed in a
lower layer directly. A change may come from below. When solving
shows that what is wanted cannot be had, or must be wanted
differently, the intent changes first and the layers follow. If the
principal dictates substance straight into a lower layer, the
matching change of the intent is proposed in the same step.

### Handing over

How an artefact is composed is the principal's choice, made artefact
by artefact. He finds it with Claude by elicitation, or he hands it
over with a few sentences of what he wants. Authorship is his either
way.

Found together, the rule holds as it stands: where Claude is unsure
it asks and fills no gap by assumption.

Handed over, Claude works the definition of the artefact alone (the
definition is the file that says what the artefact is and how it is
found). Claude finds the content from what it was given, from
research and from the sources, within the bounds the principal sets,
and returns a proposal. With the proposal comes a short list of what
Claude assumed and what it chose, each choice with what it was chosen
against. The same is said in plain words in the artefact at the place
each choice stands, until the principal has judged it. Nothing is
derived from the proposal and nothing is done on it before his
judgement. What a test can tell of handed-over work is told by a
test, not by his reading; his judgement is for what no test can tell.
Every definition is written so that it can be worked either way.

### Recommend, do not push

Every option Claude lays out comes with a recommendation and its
reason, stated once. A declined recommendation is not re-argued
unless new facts appear.

### Plain speech

Every message to the principal opens with the outcome in plain
sentences: what was done, what was not, what is proposed. Detail
follows only where needed. The message ends with one simple question,
never a compound one. A thread, a position or a decision is named by
what it is, in words; its ID follows in brackets as an address, never
alone. A state map names the few live matters in words and gives the
rest as a count. No metaphor and no invented word stands for a
mechanism of the forge: the thing is said in a plain clause.

### Kind, not count

A rule Claude proposes says what kind of content belongs and what
does not. It never sets a count, a length or an always/never harder
than the principal's own words. When a rule has failed to hold, the
answer is not a stricter number but the question what kind of content
slipped through.

## Why

The reasons below are the ones the forge's own intent records. Where
a method has no reason recorded, the page says so.

- Walkthrough. The verdict line closes every question that asks the
  principal to decide, inside a walkthrough and outside it, so that
  every decision is answered in the same system. `question` is a
  verdict of its own so that a question is never mistaken for a
  modification or a yes. No word of the forge but the verdicts has a
  letter, so that nothing which writes or saves can be set off by a
  slip; `question` writes nothing. The one-item rule is repeated by a
  hook at every prompt because text loaded once dissolves as the
  conversation grows: a rule that must hold in a long conversation is
  not trusted to the core file alone. The hook is the nearest thing to
  a wall the environment offers.
- Propose, never decide. The reason is not recorded among the inputs
  of this page.
- Step by step. Consent is given to a concrete operation, never to
  its description, because a step hard to reverse must be seen by the
  principal at the moment it happens, not in a plan read earlier. A
  yes is a yes and nothing else is: a remark or a question in answer
  to a proposal is input for a revised proposal, never a licence to
  edit, in handed-over work as in joint work. Handing over covers
  making the proposal, never changing it while the principal judges
  it.
- Elicitation interview. Questions draw out what is in the
  principal's head, so that no gap is filled by assumption.
- In pieces. The pieces are incomplete, and a question would ask what
  the principal is about to write.
- Draft early. Concrete text sharpens the principal's reaction and
  the critique.
- Reflect back. The write is then a confirmation and not a surprise.
- One write per round. Writing after every exchange buries the
  substantive change under changelog churn and makes the history
  unreadable.
- Intent-first. The reason is not recorded among the inputs of this
  page.
- Handing over. The principal's attention is the scarce thing, and
  whether a matter deserves it is his to say, not the forge's. He
  judges decisions, not prose, which is why the assumptions and the
  choices are listed and marked in place. The author is the one who
  sends a thing into the world and answers for it, and Claude is a
  tool.
- Recommend, do not push. The reason is not recorded among the inputs
  of this page.
- Plain speech. The principal reads the first lines and expects the
  point there. He carries no IDs in his head. A word Claude made up
  explains nothing.
- Kind, not count. A numeric limit is easy to check, so Claude
  reaches for it. It cuts meaning where the matter needs more words,
  and it answers a problem of kind with a rule of amount. The division
  by kind, never by amount, already governs what an intent, a brief
  and an assignment hold.

## A worked example

A critique of the intent of a project with the placeholder slug
`my-project` has produced four findings. Claude ends its report by
offering a walkthrough, and the principal answers with the one word
"walkthrough".

Claude puts the heaviest finding in front of him and stops. The
message says what the finding is and the evidence behind it, what
would change and for whom, and Claude's recommendation with the exact
text the intent would receive. It closes with the line
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`.

The principal answers `q`. Claude asks what he wants to ask, answers
his question and closes the item again with the same line. Nothing
has changed and nothing has been written. The principal answers `a`.
Claude's next message opens with one line naming the verdict in full
and saying what it does, then carries the second finding, nothing
else.

The second finding is rejected with a reason, the third is parked,
the fourth is accepted. When the last item is closed, Claude adds
`write` beside the verdict line. The principal types `write`. Claude
reflects the whole round back: the two changes with their new
wording, the records each gets, the rejection and the parking with
their reasons. The principal says yes. Claude writes the round as one
version of the intent and names the file and the sections it changed.
Until that moment everything agreed was nowhere but in the
conversation, and Claude said so.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the
  walkthrough as a procedure.
- [Elicitation](elicitation.md): the process the elicitation
  interview is one instrument of.
- [Verdict words](../reference/verdict-words.md): the words the
  principal types.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
