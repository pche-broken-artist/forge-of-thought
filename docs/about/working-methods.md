---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: e80c4823102fc601
inputs:
  - CLAUDE.md#Working methods
  - .claude/skills/walkthrough/SKILL.md
  - projects/forge/10-intent.md#Working methods
  - projects/forge/10-intent.md#POS.1410
---

# The working methods

The working methods are the named ways a working conversation in
the forge runs: the vocabulary of collaboration between the
principal (the person whose thinking is being forged) and Claude.
This page says what each method is, in the words of the operating
layer, and why it exists, in the words of the forge's intent. It is
for the user who works with Claude in a conversation and for the
evaluator who wants to see what that conversation is held to. The
procedure of a walkthrough, step by step, is on
[Walk through a list](../use/walk-through-a-list.md); the words the
principal types are on [Verdict words](../reference/verdict-words.md);
every term of the forge is in the [Glossary](../reference/glossary.md).

## What it is

A working method is a named way a conversation runs. Each has a
name so that a command's definition and the README can refer to it
and so that the principal can invoke it in a word. None is a
command. A command has one input and starts on demand. A method
applies whenever its situation arises, whatever produced it. The
methods, in the order the operating layer keeps them:

- Walkthrough: a list that needs decisions is worked one item at a
  time.
- Propose, never decide: Claude lays out, the principal composes;
  `??` asks for Claude's opinion.
- Step by step: an action that needs consent arrives as one step
  and runs on the principal's word.
- Elicitation interview: Claude draws out by questions what the
  principal has not yet articulated.
- In pieces: the principal sends one thought as several messages
  and closes it with a word.
- Draft early: an early draft is an instrument, not an output.
- Reflect back: what was understood is restated before it is
  written.
- One write per round: the conversation is written once, at its
  end, on the word `write`.
- Intent-first: a change of substance enters the intent first.
- Handing over: the principal chooses, artefact by artefact,
  whether to find it with Claude or to hand it over.
- Recommend, do not push: every option carries a recommendation,
  stated once.
- Plain speech: the outcome first, in plain sentences, and one
  question at the end.
- Kind, not count: a rule says what kind of content belongs, never
  a number.

## How it works

### Walkthrough

A walkthrough is the method by which any list of items that needs
the principal's decision is worked one item per message, in order
of weight. Such a list may be any of these:

- the findings of a critique;
- the challenges of a challenger;
- the differences between two requirement sets;
- the open threads of a project;
- the open questions of an artefact before it is handed over;
- the proposals a source makes.

Whatever produces a list ends by offering a walkthrough. That
includes `/critique`, `/challenge`, the state map that `/forge`
shows and a comparison made on request. The principal may call for
a walkthrough at any moment.

Claude puts one item in front of the principal and stops. The item
carries, in this order, what the item says and the evidence behind
it, what would change and for whom, and the recommendation with
its reason. For an accept the recommendation shows the concrete
text the artefact would receive, never a description of the edit.
A heading with a one-sentence reason is a label, not an item. A
check whether Claude has understood an item is an item of its own.
A table asking for every verdict at once is never put in front of
the principal.

Every item ends in one proposition, worded so that `accept` has
exactly one meaning: yes to what is in front of the principal. The
proposition says what changes, or that nothing changes, and what is
recorded. Where it goes against the reviewer's suggestion, it says
so. The message closes with the verdict line
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. The
verdict words are one set for every walkthrough, whatever produced
the list:

- `accept`: agreed, the text goes in as shown;
- `modify`: a discussion opens on the item, and the solution found
  is put forward to be accepted;
- `question`: the principal asks about the open item, nothing
  changes, Claude answers and closes the item again with the
  verdict line;
- `reject`: not agreed, nothing changes, the reason is recorded;
- `park`: not now, the item waits and comes back;
- `obsolete`: no longer relevant, with a note why.

The principal may answer the verdict line with a single letter, `a`,
`m`, `q`, `r` or `p`, when that letter is his whole message. After
`m` alone Claude asks what he wants changed. After `q` alone Claude
asks what he wants to ask. No other word of the forge has a letter:
`write`, `obsolete` and every command are typed in full. The next
message opens with one line that names the verdict in full and says
what it does, then carries the next item. A question from the
principal keeps the item open until he closes it. `park` is a
legitimate verdict, not a failure.

The verdicts are carried in the conversation and written once at
the round's end. A per-prompt hook, `scripts/hook-walkthrough.py`
configured in `.claude/settings.json`, repeats the one-item rule and
three lines of conduct at every prompt.

### Propose, never decide

Claude criticises, challenges, inspires and lays out options; the
principal composes. The sign `??`, alone at the end of the
principal's message or as his whole message, asks for Claude's
honest opinion of what he has just written. The answer is three
points at most, marked as Claude's own, and nothing is written or
filed. This opinion is not the isolated challenger, a reviewer that
runs apart from the conversation and does not know it. It adds to
Claude's duty to say at once what does not fit; it never replaces
that duty.

### Step by step

Any action that needs the principal's consent arrives as one step
with the exact operation, its target and the reason stated, and
runs on his word. Such actions are a write, a commit, a push, a
rename, and anything hard to reverse. A plan the principal has seen
is not consent for its steps. A batch of sensitive operations is
never run as one. The birth of a new versioned document is such a
step, whether a brief, a recipe or a layer of the chain: it happens
on the principal's word, never as a by-product of another
operation. A remark, a question or a counter-thought in answer to
"shall I change it?" is not a yes: the proposal is reworked and
asked again.

### Elicitation interview

Claude draws out by questions what the principal has not yet
articulated, rather than filling a gap by assumption. The interview
is the heart of `/forge intent`. It runs in the walkthrough's
shape: one question per message, the answer acknowledged before the
next question is asked. The interview is the form a conversation
takes; elicitation itself is the process of finding an artefact,
which uses research and sources beside the interview. That process
is described on [Elicitation](elicitation.md).

### In pieces

The principal may send one longer thought as several messages, a
piece at a time, and close it with a word such as "done". Until
that word Claude answers each piece with at most one line of
acknowledgement: no question, no analysis, no warning. After the
word the pieces are one input, read and worked as a whole. One
input is one write, so a brief dictated this way moves one version
per block, not per sentence. This is not a mode and no magic: one
input split for the sender's comfort.

### Draft early

An early draft is an elicitation tool, not an output. Concrete text
sharpens the principal's reaction.

### Reflect back

Before anything is written, Claude restates what it understood the
principal to have said. The write then confirms rather than
surprises. This method is the companion of one write per round.

### One write per round

A working conversation is one round. What is agreed in it is
carried in the conversation and written once at its end, on the
principal's word. The word is `write`, typed in full. On it Claude
reflects the whole round back and writes everything carried, on the
principal's yes, as one version. Claude offers the word beside the
verdict line when the round looks finished. Until the write,
everything agreed is nowhere yet, and Claude says so.

### Intent-first

A change of substance goes into the intent first and propagates
from there down the whole chain the project has. A change may come
from below, when solving shows that what is wanted must change;
then the intent changes first. Only wording is fixed downstream
directly.

### Handing over

How an artefact is composed is the principal's choice, made
artefact by artefact. Either he finds it with Claude by
elicitation, or he hands it over with a few sentences of what he
wants. Handed over, Claude works the artefact's definition alone:
the definition's Map says what must be found, and Claude finds it
from what it was given, from research and from the sources, within
the bounds the principal sets. Claude returns a proposal. With it
comes a short list of what it assumed and what it chose, each
choice with what it was chosen against; the same is said in plain
words in the artefact at the place each stands, until the principal
has judged it. Nothing is derived from the proposal and nothing is
done on it before his judgement. What a test can tell of
handed-over work is told by a test, not by his reading; his
judgement is for what no test can tell. Found together, the rule of
asking when unsure holds unchanged. Every definition is written so
that it can be worked either way.

### Recommend, do not push

Every option Claude lays out comes with a recommendation and its
reason, stated once. A declined recommendation is not re-argued
without new facts.

### Plain speech

A message opens with the outcome in plain sentences: what was done,
what was not, what is proposed. Detail follows only where needed.
The message ends with one simple question, never a compound one. A
thread, a position or a decision is named by what it is, in words;
its ID follows in brackets as an address, never alone. The state
map names the few live matters in words and gives the rest as a
count. No metaphor and no invented word stands for a mechanism of
the forge: the thing is said in a plain clause.

### Kind, not count

A rule Claude proposes says what kind of content belongs and what
does not. It never sets a count, a length or an always/never harder
than the principal's own words. When a rule has failed to hold, the
answer is not a stricter number but the question what kind of
content slipped through.

## Why

The reasons below are the intent's. Where the intent records none
among the inputs of this page, the page says so.

**Walkthrough.** One item per message exists because text loaded
once dissolves as a conversation grows. That is why a hook repeats
the rule at every prompt and the core file is not trusted alone. A
hook is context, not enforcement; it is the nearest thing to a wall
that the harness (the program that runs Claude) offers, and it is a
trial, judged by behaviour. `question` is a verdict of its own so
that a question is never mistaken for a modification or a yes;
`question` writes nothing. Only the verdict words have a letter, so
that nothing which writes or saves can be set off by a slip. Every
list ends by offering a walkthrough so that the principal always
has the method to hand, whatever produced the list.

**Propose, never decide.** The principal is the author and Claude a
tool. The `??` opinion stands as one sentence under this method and
not as a method of its own, for the size of the core file.

**Step by step.** Consent is given to a concrete operation, never
to its description. A step hard to reverse must be seen by the
principal at the moment it happens, not in a plan read earlier. A
yes is a yes and nothing else is: a remark or a question is input
for a revised proposal shown again, never a licence to edit, in
handed-over work as in joint work. Handing over covers making the
proposal, never changing it while the principal judges it.

**Elicitation interview.** Claude fills no gap by assumption; the
question is how what is in the principal's head is reached.

**In pieces.** The pieces are incomplete. A question asked before
the closing word would ask what the principal is about to write.

**Draft early.** Concrete text sharpens the reaction; a draft is
there to be reacted to.

**Reflect back.** So that the write is a confirmation and not a
surprise.

**One write per round.** The method exists for its name: the
principal invokes it in a word, and it stands beside the
walkthrough, whose verdicts reach the write this way. Claude offers
`write` beside the verdict line so that the principal always sees
both ways on: the next item, or the write. Why a round is written
once rather than item by item is owned by another position of the
intent; the reason is not recorded here.

**Intent-first.** The method is the name, as a way of working, of a
rule the intent owns elsewhere; the reason is not recorded here.

**Handing over.** The principal's attention is the scarce thing,
and whether a matter deserves it is his to say, not the forge's.
Authorship is his either way: the author is the one who sends a
thing into the world and answers for it, and Claude is a tool.
Claude says what it assumed and what it chose so that the principal
judges decisions and not prose.

**Recommend, do not push.** The reason is not recorded.

**Plain speech.** The principal reads the first lines and expects
the point there. He carries no IDs in his head. A word Claude made
up explains nothing.

**Kind, not count.** A numeric limit is easy to check, and so Claude
reaches for it. But a limit cuts meaning where the matter needs
more words, and it answers a problem of kind with a rule of amount.
The division by kind, never amount, already governs what an intent,
a brief and an assignment hold.

## A worked example

The principal has run `/critique` on the assignment of a project
with the placeholder slug `my-project`. The critic returns three
findings, and Claude ends its report by offering a walkthrough. The
principal answers with one word: "walkthrough".

Claude puts the heaviest finding in front of him and nothing else.
The message says what the finding is (a requirement written with
"should" where the assignment's style wants "shall"), what would
change (one item of the assignment, for the recipients who read
it), and the recommendation: accept, with the item's new wording
shown in full. It closes with
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`.

The principal types `q`. Claude asks what he wants to ask. He asks
whether the same wording appears elsewhere. Claude answers that it
does not, changes nothing, and closes the item again with the
verdict line. The principal types `a`. Claude's next message opens
with one line, "accept: the item will carry the wording shown", and
carries the second finding.

The second finding the principal parks with `p`; Claude names the
verdict, says the finding waits and comes back, and carries the
third. The third he rejects with `r` and gives his reason. Claude
names the verdict and says the reason will be recorded as a
decision. The list is finished, so Claude closes with the verdict
line and `write` beside it.

The principal types `write`. Claude reflects the whole round back:
the one item's new wording, the parked finding, the rejected one
with its reason and the records that will be appended. On his yes
Claude writes everything as one version of the assignment, with
its history records, the decision and the findings' states in the
ledger (the project's single source of truth for state). Until that
moment nothing had been written, and Claude said so.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the
  walkthrough as a procedure.
- [Elicitation](elicitation.md): the process the elicitation
  interview is one instrument of.
- [Verdict words](../reference/verdict-words.md): the words the
  principal types.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
