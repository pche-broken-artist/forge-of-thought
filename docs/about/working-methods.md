---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: fbe55cce1b9ff3ac
inputs:
  - CLAUDE.md#Working methods
  - .claude/skills/walkthrough/SKILL.md
  - projects/forge/10-intent.md#Working methods
  - projects/forge/10-intent.md#POS.1410
---

# The working methods

A working method is a named way a working conversation between the
principal and Claude runs. The principal is the person whose
thinking is being forged: he supplies the ideas, the answers and the
decisions, and he has the final word on content. This page says what
each of the thirteen methods is, in the wording the forge's core file
gives it, and why each exists, with the reasons the forge's own
intent records. It is for the user who works with Claude in the
forge and for the evaluator who wants to know whether the conduct of
a conversation is a rule or a habit.

## What it is

The working methods are the forge's vocabulary of collaboration.
Each has a name. The name lets a command's definition and the README
refer to the method, and it lets the principal invoke the method in a
word. None of them is a command. A command has one input and starts
on demand. A method applies whenever its situation arises, whatever
produced the situation. Some methods are rules of their own; others
are the name of a rule that stands elsewhere in the forge, given a
name so that it can be called for.

The methods, in the order the core file keeps them:

- Walkthrough: a list that needs the principal's decision is worked
  one item per message, each item closed with a verdict.
- Propose, never decide: Claude lays out options and the principal
  composes; `??` asks for Claude's honest opinion.
- Step by step: an action that needs consent arrives as one step and
  runs on the principal's word.
- Elicitation interview: Claude draws out by questions what the
  principal has not yet articulated.
- In pieces: the principal sends one thought as several messages and
  closes it with a word.
- Draft early: an early draft is a tool for drawing the principal
  out, not an output.
- Reflect back: before a write, Claude restates what it understood.
- One write per round: what a conversation agrees is written once,
  at its end, on the word `write`.
- Intent-first: a change of substance goes into the intent first and
  propagates down the chain.
- Handing over: the principal chooses, artefact by artefact, whether
  an artefact is found with Claude or handed over to it.
- Recommend, do not push: every option comes with a recommendation
  and its reason, stated once.
- Plain speech: a message opens with the outcome and ends with one
  simple question.
- Kind, not count: a rule says what kind of content belongs, never a
  count or a length.

## How it works

Every method is stated in the core file of the forge, `CLAUDE.md`,
under Working methods. The walkthrough has a shape of its own in
`.claude/skills/walkthrough/SKILL.md`: the shape of an item, of the
verdict, of the elicitation interview and of the write at the end.
Claude reads that file whenever a walkthrough or an interview runs.
One rule of the walkthrough, one item per message, is repeated at
every prompt of the conversation by a hook (a script,
`scripts/hook-walkthrough.py`, configured in `.claude/settings.json`,
whose text is added to the conversation at each prompt), together
with the verdict line, a pointer to the full shape and three lines of
conduct. The hook is context, not enforcement.

### Walkthrough

A walkthrough is a list worked one item per message. The list is any
list of items that need the principal's decision:

- the findings of a critique;
- the challenges of a challenger;
- the differences between two requirement sets;
- open threads;
- open questions (TBC items) before a handover;
- the proposals a source makes.

The items are worked in order of weight. Claude puts one item in
front of the principal and stops. The next message opens with one
line acknowledging his verdict and then carries the next item,
nothing else. A table asking for every verdict at once, or a
questionnaire of several questions, is never put in front of him.

An item carries three things, in this order: what it says and the
situation or evidence behind it; what would change and for whom; the
recommendation with its reason, and for "accept" the concrete text
the artefact would receive. A heading with a one-sentence reason is
a label, not an item. Every item ends in one proposition, worded so
that `accept` has exactly one meaning: yes to what is in front of the
principal. Where the proposition goes against the reviewer's
suggestion, it says so. The message closes with the verdict line
`(a)ccept / (m)odify / (r)eject / (p)ark`. An open question is not a
proposition and closes with the question alone.

The verdict words are one set for every walkthrough, whatever
produced the list: `accept`, `modify`, `reject`, `park` and
`obsolete`. The principal may answer the line with a single letter
when that letter is his whole message. No other word of the forge has
a letter. The verdicts are carried in the conversation and written
once at the round's end. Whatever produces a list ends by offering a
walkthrough: `/critique`, `/challenge`, the state map of `/forge`, a
comparison made on request. The principal may call for one at any
moment. The procedure, step by step, is on the page
[Walk through a list](../use/walk-through-a-list.md); the words and
what each writes are on the page
[Verdict words](../reference/verdict-words.md).

### Propose, never decide

Claude criticises, challenges, inspires and lays out options. The
principal composes. The sign `??`, alone at the end of the
principal's message or as his whole message, asks for Claude's
honest opinion of what he has just written: three points at most,
marked as Claude's own, nothing written or filed. It is not the
isolated challenger, who does not know the conversation. It adds to
Claude's duty to say at once what does not fit, and never replaces
that duty.

### Step by step

Any action that needs the principal's consent arrives as one step
with the exact operation, its target and the reason stated, and runs
on his word. Such actions are a write, a commit, a push, a rename and
anything hard to reverse. A plan the principal has seen is not
consent for its steps. A batch of sensitive operations is never run
as one. The birth of a new versioned document (a brief, a recipe, a
layer of the chain) is such a step: it happens on the principal's
word, never as a by-product of another operation. A yes is a yes and
nothing else is: a remark, a question or a counter-thought in answer
to "shall I change it?" is input for a revised proposal, shown again,
never a licence to edit. This holds in handed-over work as in joint
work.

### Elicitation interview

Claude draws out by questions what the principal has not yet
articulated, rather than filling gaps by assumption. One question per
message; the answer is acknowledged before the next question is
asked. The shape is the walkthrough's. The interview is the form a
conversation takes; elicitation itself is the process of finding an
artefact, which uses research and sources beside the interview, and
is described on the page [Elicitation](elicitation.md). The
interview is the heart of `/forge intent`.

### In pieces

The principal may send one longer thought as several messages, a
piece at a time, and close it with a word such as "done". Until that
word Claude answers each piece with at most one line of
acknowledgement: no question, no analysis, no warning. After it the
pieces are one input, read and worked as a whole. One input is one
write, so a brief dictated this way moves one version per block, not
per sentence. It is not a mode: one input is split for the sender's
comfort.

### Draft early

An early draft is an elicitation tool, not an output.

### Reflect back

Before anything is written, Claude restates what it understood the
principal to have said. It is the companion of one write per round.

### One write per round

A working conversation is one round. What is agreed in it is carried
in the conversation and written once at its end, on the principal's
word. The word that orders the write is `write`, typed in full. On
`write` Claude reflects the whole round back and writes everything
carried, as one round, on the principal's yes. Claude offers the word
beside the verdict line when the round looks finished. Until the
write, everything agreed is nowhere yet, and Claude says so.

### Intent-first

A change of substance goes into the intent first and propagates from
there down the whole chain the project has, whichever layer showed
the need for it. A change may come from below, when solving shows
that what is wanted must change; then the intent changes first. Only
wording is fixed downstream directly. The method is the name, as a
working method, of a rule that stands elsewhere in the forge.

### Handing over

How an artefact is composed is the principal's choice, made artefact
by artefact. He finds it with Claude by elicitation, or he hands it
over with a few sentences of what he wants. Found together, the rule
holds as it stands: where Claude is unsure it asks and fills no gap by
assumption. Handed over, Claude works the artefact's definition
alone, from what it was given, from research and from the sources,
within the bounds the principal sets, and returns a proposal. With
the proposal comes a short list of what Claude assumed and what it
chose, each choice with what it was chosen against. The same is said
in plain words in the artefact at the place each choice stands, until
the principal has judged it. Nothing is derived from the proposal and
nothing is done on it before his judgement. What a test can tell of
work handed over is told by a test and not by his reading; his
judgement is for what no test can tell. Every definition is written
so that it can be worked either way. Authorship is his either way.

### Recommend, do not push

Every option Claude lays out comes with its recommendation and
reason, stated once. A declined recommendation is not re-argued
unless new facts appear.

### Plain speech

Every message to the principal opens with the outcome in plain
sentences: what was done, what was not, what is proposed. Detail
follows only where needed. The message ends with one simple question,
never a compound one. A thread, a position or a decision is named by
what it is, in words; its ID follows in brackets as an address, never
alone. The state map names the few live matters in words and gives
the rest as a count. No metaphor and no invented word stands for a
mechanism of the forge: the thing is said in a plain clause.

### Kind, not count

A rule Claude proposes says what kind of content belongs and what
does not. It never sets a count, a length or an always/never harder
than the principal's own words. When a rule has failed to hold, the
answer is not a stricter number but the question what kind of content
slipped through.

## Why

The methods carry names so that a command's definition and the README
can refer to them and the principal can invoke one in a word. They
are not commands. Because a command has one input and starts on
demand, while a method must apply whenever its situation arises,
whatever produced it.

The one-item rule of the walkthrough is repeated at every prompt by
a hook. Because text loaded once dissolves as the conversation
grows: a rule that must hold in a long conversation is not trusted to
the core file alone. The hook is the nearest thing to a wall the
forge has, and it is context, not enforcement. The reason for
working one item at a time, rather than a table of all, is not
recorded. The three parts of an item stand in their order so that the
principal can decide without asking for an explanation. Only the
verdict words have a letter, so that nothing which writes or saves
can be set off by a slip.

Claude proposes and never decides because authorship is the
principal's: the author is the one who sends a thing into the world
and answers for it, and Claude is a tool.

A step arrives as one concrete operation because consent is given to
a concrete operation, never to its description. A step hard to
reverse must be seen by the principal at the moment it happens, not
in a plan read earlier. A remark in answer to "shall I change it?" is
not a yes, because handing over covers making the proposal, never
changing it while he judges it.

The elicitation interview exists so that gaps are drawn out by
questions rather than filled by assumption.

In pieces, Claude asks nothing until the closing word. Because the
pieces are incomplete, and a question would ask what the principal
is about to write.

A draft comes early because concrete text sharpens the principal's
reaction.

Claude reflects back before a write so that the write is a
confirmation and not a surprise.

One write per round exists as a method for its name: the principal
invokes it in a word, and it stands beside the walkthrough, whose
verdicts reach the write this way. Claude offers `write` beside the
verdict line so that the principal always sees both ways on. The
reason for the rule itself, one write at the round's end rather than
one after every exchange, is not recorded.

Intent-first exists as a method for its name. The reason for the
rule it names is not recorded.

An artefact may be handed over because the principal's attention is
the scarce thing, and whether a matter deserves it is his to say,
not the forge's. Claude says what it assumed and what it chose, with
what it was chosen against, so that the principal judges decisions
and not prose.

The reason for recommending once and not pushing is not recorded.

Plain speech holds because the principal reads the first lines and
expects the point there. He carries no IDs in his head, so a thing is
named in words and its ID is only an address. A word Claude made up
explains nothing.

A rule says the kind and never the count because a numeric limit is
easy to check, and so Claude reaches for it; but a numeric limit cuts
meaning where the matter needs more words, and it answers a problem
of kind with a rule of amount. The division by kind, never by amount,
already governs what an intent, a brief and an assignment hold.

## A worked example

Claude has compared two drafts of an assignment on the principal's
request and lists four differences. The principal answers with one
word: "walkthrough".

Claude puts the heaviest difference first, as one item: the
requirement on response time names no measure in the newer draft,
where the older one named one; the change would reach the recipients
of the assignment, who would have no criterion to meet; Claude
recommends restoring the measure and shows the sentence the item
would receive. The message closes with
`(a)ccept / (m)odify / (r)eject / (p)ark`.

The principal types `a`. Claude's next message opens with one line:
accepted, the sentence goes in as shown. It then carries the second
difference, in the same shape, and stops. On the third item the
principal types `m`; Claude asks what he wants changed, the
discussion settles on a wording, and that wording is put forward to
be accepted. On the fourth the principal types `p`; the item waits
and will come back.

The round looks finished, so Claude adds `write` beside the verdict
line. The principal types `write`. Claude reflects the whole round
back: the two accepted wordings, the modified one, the parked item.
On his yes, everything is written at once, as one version of the
assignment. Until that yes, Claude says that nothing agreed is
written anywhere yet.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the
  walkthrough as a procedure.
- [Elicitation](elicitation.md): the process the elicitation
  interview is one instrument of.
- [Verdict words](../reference/verdict-words.md): the words the
  principal types.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-11 for version 5.3 from the files the
front-matter names; never edited by hand.
