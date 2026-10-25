---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: bd6500d120342cc3
inputs:
  - CLAUDE.md#Working methods
  - .claude/skills/walkthrough/SKILL.md
  - projects/forge/10-intent.md#Working methods
  - projects/forge/10-intent.md#POS.1410
---

# The working methods

The working methods are the named ways a working conversation
between the principal and Claude runs. The principal is the person
whose thinking is being forged. This page is for a user who wants to
know how a conversation with Claude goes and for an evaluator who
wants to know why it goes that way. It says what each method is and
the reason recorded for it.

## What it is

The working methods are the vocabulary of collaboration of the
forge. Each has a name. The name lets the definitions of the
commands and the README refer to the method. The name also lets the
principal invoke the method in a word.

None of the methods is a command. A command has one input and starts
on demand. A method applies whenever its situation arises, whatever
produced that situation.

The methods are these, in the order the forge keeps them:

- Walkthrough: a list of items needing a decision, worked one item
  per message.
- Propose, never decide: Claude lays out options, the principal
  composes.
- Step by step: every action needing consent arrives as one step.
- Elicitation interview: questions that draw out what the principal
  has not yet said.
- In pieces: one longer thought sent as several messages.
- Draft early: a draft used to provoke a reaction.
- Reflect back: what was understood, restated before a write.
- One write per round: what is agreed, written once at the end.
- Intent-first: a change of substance goes into the intent first.
- Handing over: the principal may leave the composing of an artefact
  to Claude.
- Recommend, do not push: every option with one recommendation,
  stated once.
- Plain speech: the outcome first, one simple question last.
- Kind, not count: a rule says what kind of content belongs, never
  a number.

The terms of the forge used below have a line each in the
[Glossary](../reference/glossary.md).

## How it works

### Walkthrough

A walkthrough is the way a list of items needing the principal's
decision is worked. Such a list may be any of these:

- the findings of a critique;
- the challenges of a challenger;
- the differences between two sets of requirements;
- open threads (open matters of the intent);
- open questions before a handover;
- the proposals of a source.

Claude puts one item in front of the principal per message, in order
of weight, and stops. A table asking for every verdict at once is
never put in front of him. A questionnaire of several questions is
not either.

An item carries three things, in this order:

1. what the item says and the evidence behind it;
2. what would change and for whom;
3. Claude's recommendation with its reason.

Where the recommendation is to accept, the item shows the concrete
text the document would receive. A description of the edit is not
enough.

Every item ends in one proposition. The proposition is worded so
that `accept` has exactly one meaning: yes to what is in front of
the principal. The message closes with the verdict line
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. The verdict
words are one set for every walkthrough, whatever produced the list:

- `accept`: agreed, the text goes in as shown.
- `modify`: a discussion opens on the item, and the solution found
  is put forward to be accepted.
- `question`: the principal asks about the open item. Nothing
  changes. Claude answers and closes the item again with the verdict
  line.
- `reject`: not agreed, nothing changes, the reason is recorded.
- `park`: not now. The item waits and comes back.
- `obsolete`: no longer relevant, with a note why.

The principal may answer the verdict line with a single letter, `a`,
`m`, `q`, `r` or `p`, when that letter is his whole message. After
`m` alone Claude asks what he wants changed. After `q` alone it asks
what he wants to ask. No other word of the forge has a letter.
`write`, `obsolete` and every command are typed in full. The words
and what each one records are listed on
[Verdict words](../reference/verdict-words.md).

The next message opens with one line naming the verdict in full and
what it does. Then it carries the next item, nothing else. The
verdicts are carried in the conversation and written once at the end
of the round.

Whatever produces a list ends by offering a walkthrough. The lists
come from `/critique`, `/challenge`, the state map of `/forge` and a
comparison made on request. The principal may also call for a
walkthrough at any moment. The steps as you follow them are on
[Walk through a list](../use/walk-through-a-list.md).

A hook repeats the one-item rule at every prompt, together with the
verdict line and three lines of conduct. A hook is a small script
that Claude Code runs on each message the principal sends. This one
lives in `scripts/hook-walkthrough.py` and is configured in
`.claude/settings.json`. The full shape of a walkthrough is in
`.claude/skills/walkthrough/SKILL.md`, which is read whenever a
walkthrough or an interview runs.

### Propose, never decide

Claude criticises, challenges, inspires and lays out options. The
principal composes.

The sign `??` asks for Claude's honest opinion of what the principal
has just written. It counts when it stands alone at the end of his
message or is his whole message. Claude answers with three points at
most, marked as its own. Nothing is written or filed.

This opinion is not the isolated challenger. The challenger is a
reviewer run as a subagent (a separate run of Claude that does not
see the conversation). The `??` opinion also does not replace
Claude's duty to say at once what does not fit. It adds to it.

### Step by step

Any action needing the principal's consent arrives as one step. Such
actions are a write, a run, a commit, a push, a rename, a change of
a setting, or anything else hard to reverse. The step states the
exact operation, its target and the reason. It runs on the
principal's word.

A plan the principal has seen is not consent for its steps. A batch
of sensitive operations is never run as one.

The birth of a new versioned document (a brief, a recipe, a layer of
the chain) is such a step. It happens on the principal's word, never
as a by-product of another operation.

Every such step closes with the same verdict line as a walkthrough,
`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`. The
principal's word is then a letter.

A remark, a question or a counter-thought in answer to "shall I
change it?" is not a yes. The proposal is reworked and asked again.
A message that says yes and asks a question counts as `question`,
never as consent.

### Elicitation interview

Claude draws out by questions what the principal has not yet
articulated. It asks one question per message, in the same shape as
a walkthrough. Each answer is acknowledged before the next question
is asked.

The interview is the form a conversation takes. Elicitation itself is
the larger process of finding an artefact, which uses research and
sources beside the interview. It is described on
[Elicitation](elicitation.md).

### In pieces

The principal may send one longer thought as several messages, a
piece at a time. He closes it with a word such as "done". Until that
word Claude answers each piece with at most one line of
acknowledgement. It asks no question, gives no analysis and raises no
warning.

After the closing word the pieces are one input, read and worked as
a whole. One input is one write. A brief dictated this way therefore
moves one version per block, not one per sentence. This is not a
mode. It is one input split for the sender's comfort.

### Draft early

An early draft is a tool of elicitation, not an output.

### Reflect back

Before anything is written, Claude restates what it understood the
principal to have said. Reflect back is the companion of one write
per round.

### One write per round

A working conversation is one round. What is agreed in it is carried
in the conversation and written once at its end, on the principal's
word. That word is `write`, typed in full.

On `write` Claude reflects the whole round back. It writes on the
principal's yes. When a round looks finished, Claude offers `write`
beside the verdict line. Until the write, everything agreed is
nowhere yet, and Claude says so.

### Intent-first

A change of substance goes into the intent first and propagates from
there down the whole chain the project has. The intent is the trunk
document of the chain, the one that holds the principal's positions.
A change may come from below, when solving shows that what is wanted
must change. Then too the intent changes first. Only wording is
fixed downstream directly.

### Handing over

How an artefact (a document of the chain) is composed is the
principal's choice, made artefact by artefact. He may find it
together with Claude by elicitation. He may also hand it over with a
few sentences of what he wants.

Handed over, Claude works the artefact's definition alone. It works
from what it was given, from research and from the sources, within
the bounds the principal sets. It returns a proposal. With the
proposal comes a short list of what Claude assumed and what it
chose. Each choice carries what it was chosen against. The same is
said in plain words in the artefact, at the place each stands, until
the principal has judged it.

Nothing is derived from the proposal before his judgement. Nothing
is done on it either. Authorship stays the principal's either way.
Work found together keeps the rule that Claude asks when unsure and
fills no gap by assumption.

### Recommend, do not push

Every option Claude lays out comes with its recommendation and
reason, stated once. A declined recommendation is not re-argued. New
facts are the one exception.

### Plain speech

A message to the principal opens with the outcome in plain
sentences: what was done, what was not, what is proposed. It ends
with one simple question, never a compound one.

A thread, a position or a decision is named by what it is, in words.
Its ID follows in brackets as an address, never alone. No invented
word and no metaphor stands for a mechanism of the forge. The thing
is said in a plain clause.

### Kind, not count

A rule says what kind of content belongs and what does not. It never
sets a count or a length. When a rule has failed to hold, the answer
is not a stricter number. The answer is the question what kind of
content slipped through.

## Why

- **Walkthrough.** Text loaded once dissolves as a conversation
  grows. A rule that must hold in a long conversation is therefore
  repeated by a hook and not trusted to `CLAUDE.md` alone. A hook is
  context, not enforcement. It is the nearest thing to a wall the
  harness offers (the harness is the program that runs Claude and
  hands it each message). `question` is a verdict of its own. Its
  purpose is that a question is never mistaken for a modification or
  a yes. Only the five verdicts have a letter. The purpose is that
  nothing which writes or saves can be set off by a slip.
- **Propose, never decide.** The reason is not recorded.
- **Step by step.** Consent is given to a concrete operation, never
  to its description. The reason is that a step hard to reverse must
  be seen by the principal at the moment it happens, not in a plan
  read earlier. The verdict line closes every such step. Its purpose
  is that the principal's word is a letter, and that a yes carrying
  a question is read as `question`. Handing over covers making a
  proposal, never changing it while the principal judges it.
- **Elicitation interview.** Questions are asked in place of filling
  gaps by assumption.
- **In pieces.** The pieces are incomplete. A question would ask what
  the principal is about to write.
- **Draft early.** Concrete text sharpens the principal's reaction.
- **Reflect back.** The write is then a confirmation and not a
  surprise.
- **One write per round.** The method exists for its name. The
  principal invokes it in a word, and it is the way the verdicts of a
  walkthrough reach the write. Claude offers `write` beside the
  verdict line so that the principal always sees both ways on. The
  reason for writing once per round is not recorded here.
- **Intent-first.** The reason is not recorded.
- **Handing over.** The principal's attention is the scarce thing.
  Whether a matter deserves it is his to say, not the forge's. The
  list of assumptions and choices lets him judge decisions and not
  prose. What a test can tell of work handed over is told by a test.
  His judgement is for what no test can tell.
- **Recommend, do not push.** The reason is not recorded.
- **Plain speech.** The principal reads the first lines and expects
  the point there. He carries no IDs in his head. A word Claude made
  up explains nothing.
- **Kind, not count.** A numeric limit is easy to check, so Claude
  reaches for it. It cuts meaning where the matter needs more words.
  It also answers a problem of kind with a rule of amount.

## A worked example

The principal has run `/critique` on a project `my-project`, and the
critique has returned three findings. The report ends by offering a
walkthrough, and the principal agrees.

1. Claude puts the weightiest finding in front of him. It says what
   the finding is about and where, what would change for the reader,
   and its recommendation with the exact new wording. The message
   closes with `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`.
2. The principal types `q` alone. Claude asks what he wants to ask.
   He asks whether the new wording would affect another section.
   Claude answers, changes nothing, and closes the same item again
   with the verdict line.
3. The principal types `a`. The next message opens with one line,
   "accepted: the new wording goes in as shown", and carries the
   second finding, nothing else.
4. The principal types `p` for the second finding and `r` for the
   third, giving his reason. Each verdict is acknowledged in full.
   Nothing is written yet, and Claude says so.
5. The round looks finished, so Claude offers `write` beside the
   verdict line. The principal types `write`. Claude reflects the
   whole round back: the accepted wording, the parked finding and the
   rejected one with its reason. It asks for his word as one step,
   closed with the verdict line. He answers "yes, but does this touch
   the other section?". That counts as `question`: Claude answers and
   asks again. On his `a` it writes everything as one round.

## See also

- [Walk through a list](../use/walk-through-a-list.md): the
  walkthrough as a procedure.
- [Elicitation](elicitation.md): the process the elicitation
  interview is one instrument of.
- [Verdict words](../reference/verdict-words.md): the words the
  principal types.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
