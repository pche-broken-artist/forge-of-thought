---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: f0e07ea61cdd38ce
inputs:
  - CLAUDE.md#Document chain
  - projects/forge/40-solution-design.md#How the parts work together
  - projects/forge/10-intent.md#POS.0110
  - projects/forge/10-intent.md#POS.0120
  - projects/forge/10-intent.md#POS.0130
  - projects/forge/10-intent.md#POS.1800
  - projects/forge/10-intent.md#POS.1400
  - projects/forge/10-intent.md#POS.0400
  - projects/forge/10-intent.md#POS.1860
  - projects/forge/10-intent.md#POS.0710
  - projects/forge/10-intent.md#POS.0180
  - projects/forge/10-intent.md#POS.1100
  - projects/forge/10-intent.md#POS.1520
---

# How a thought travels through the forge

The journey of a thought is the path one idea takes in Forge of
Thought, from a rough brief to a saved release. This page follows one
invented, generic thought along that path, station by station, in the
order the thought meets them. It is for anyone who wants the whole
picture before the parts: a user about to start, an extender who
wants to know where an addition would sit, an evaluator judging
whether the design holds together.

## What it is

The forge turns a thought into a chain of versioned documents. The
person whose thinking is forged is the principal: he supplies the
ideas, the answers and the decisions, and he has the final word on
all content. Claude proposes and keeps the structure; the principal
composes.

A thought meets these stations:

- the brief: the principal's rough text of what he wants and why;
- the intent: the working document where the thought is chiselled
  into positions (that is, what the principal currently holds, and
  why);
- the layers below the intent, as the project needs them;
- the reviewers, who press on the documents and on the thinking;
- research, where a position will rest on what the world already
  knows;
- the outputs: renders for each audience, work products, the
  documentation;
- git, where everything is saved and released.

Sources and research are not stations in a row. They can arrive at
any stage.

```
            sources and research, at any stage
                          |
  brief --> intent --> assignment --> BRD --> solution design
               |          (each layer only where the project needs it)
               |
      reviewers press at every layer
               |
  renders, work products, documentation, generated from the chain
               |
            saved to git and released
```

Every station is one of the documents the page
[The document chain](the-document-chain.md) describes. A term of the
forge used here and not explained is in the
[Glossary](../reference/glossary.md).

## How it works

### The brief

The thought arrives as a brief. A brief is the principal's text of
one whole of thinking: what he wants, why, and what he chose to take
from what was found around it. It is free-form: no required content,
no IDs, only a minimal header. It holds thoughts to be processed, not
decisions. A brief may arrive finished from outside, be begun outside
and finished with Claude, or be born with Claude from the first word.

A brief is rough on purpose. A brief polished until the intent has
nothing left to do has gone too far.

### The intent

The brief is then mined into the intent. Claude and the principal
work it by elicitation: Claude draws out by questions what the
principal has not yet put into words. Each thought that survives
becomes a position that says what the principal holds and why, and
names what it comes from, a brief or a source.

The intent is the consolidated current state of the principal's
thinking. It is not a log. It is rewritten for coherence every round,
and each change is recorded in a history kept beside it. The way to a
position (why it changed, what was said, which research turned it)
goes into that history, never into the position. What is still open
lives in threads, one file per open matter beside the intent.

### The layers below the intent

Below the intent a project takes the layers it needs. None is a
condition of another, and many projects end at the intent. A layer a
project does not have is not missing.

- **The assignment** is the handover document for the recipients:
  complete, precise and self-contained. It carries the whole
  in-scope substance of the intent. A silent omission is a defect;
  leaving a matter out is legitimate only as an explicit delegation.
- **The BRD** breaks its parent into business rules the stakeholders
  of each area review on their own.
- **The solution design** says how the things wanted are realised. It
  is derived from the lowest layer the project has above it.

A change of substance goes into the intent first and is then carried
down through every layer the project has. A change may also come from
below: when solving shows that what is wanted must be wanted
differently, the intent changes first and the layers follow.

### The reviewers

At every layer, isolated reviewers press on what was written. Each
runs as a subagent (that is, a separate run of Claude that sees only
the files it is given) and never sees the working conversation. There
are two kinds of review of one shape:

- the critic: the quality of the documents, its results called
  findings;
- the challenger: the substance of the thinking, its results called
  challenges.

A third kind, the check, verifies mechanical conformance with the
conventions. The principal invokes each reviewer by hand. Each
produces a dated report that is never changed afterwards. Its results
are settled in a walkthrough (that is, one item per message, each
closed with the principal's verdict). The page
[The isolated reviewers](isolated-reviewers.md) says more.

### Research

Research is run where a position, a layer of the chain or a design
will rest on what the world already knows. A research is planned
before anything is searched. Claude shows the plan: the purpose, the
perspectives, the assumptions, what is left out, and the questions,
each answered by one kind of evidence from one kind of source. The
principal confirms the plan in a walkthrough. A research has two
depths: a quick one for one question to be answered and cited, and a
deep one where something will rest on the answer. The page
[How a research is made](the-research.md) says more.

### Sources

External inputs (transcripts, offers, documents, standards) are
stored in the project's sources. A source is never changed once it is
registered. A source may arrive at any stage: before the brief as
material for writing it, during the work on the intent, or after.
Registration does not mean intake. The principal alone directs how
and when a source is used. When the content of a source enters the
intent, it does so by his explicit act, cited with its provenance.
What someone said in a meeting never silently becomes the principal's
own position.

### The outputs

Outputs for each audience are renders: a pitch, an architecture
picture, an executive summary, the repository README. A render is
generated from the chain and never edited by hand. What is iterated
is its recipe: one file that names the inputs, the audience, the
instructions and the output template. A render assigns nothing; the
artefacts stay the source of truth. The page
[Renders and recipes](renders-and-recipes.md) says more.

Where the project needs work of its own (a model, an analysis, a
worked task), a work product is made beside the renders. It takes its
inputs from the chain and the resources and adds work of its own. It
is two files:

- the file that holds the content;
- the specification beside it, which holds the way and the why.

What a work product shows flows back into the intent. The page
[The work product](the-work-product.md) says more.

The documentation is generated in the same way: pages of one topic
each, made from a documentation map and never composed by hand.

### Saved and released

Everything is saved to git. Saving and releasing are two separate
steps. A save runs a light check and then commits and pushes, with no
render. A release runs its checks, regenerates the README and the
release notes, and then saves with the release message.

### The main courses of events

- **A round of work:** Claude reads the definition of the target
  artefact, the conversation runs by the working methods, and one
  write at the round's end changes the artefact, appends the records
  to its history and brings the ledger (the one record of the
  project's state, made from the documents) current.
- **A review:** one isolated reviewer runs, its report is filed with
  IDs, and its results are settled by walkthrough and written in one
  round.
- **A render:** the Markdown is generated in an isolated subagent from
  a recipe and its inputs, with its provenance; the designed file is
  then made from the render as it lies on disk.
- **Persistence:** a save checks, commits and pushes; a release runs
  its checks, settles them, regenerates the README and the release
  notes, and saves with the release message.

## Why

The brief has no required structure. A required structure would force
premature tidiness.

The intent exists because the context of a chat dies. Anything of
value must live in a file. The intent is the document to read when
returning to a project after weeks, instead of digging through old
conversations.

Many projects end at the intent. Where what is wanted needs no
solution written down, no lower layer is needed. A solution design is
worth writing where the way is not obvious, where a choice has a
price, or where two hands would solve the same matter differently if
it were not written down. Whether it is written, the principal says.

The reviewers never see the working conversation. That blindness is
the source of their value.

A research is planned before it is searched. The quality of a
research is made by how the topic is broken into questions, not by the
searching. The plan is where the principal sees the questions before
they cost anything.

A render is never edited by hand, and its recipe fixes structure, not
wording. Each rendering derives the words again from the current
inputs. Fixing the text in the template would turn the recipe into
the render and make the inputs meaningless.

The work product is a kind of its own rather than a stretched render.
Stretching the render to cover it would have cost the rule that a
render is never edited by hand.

Why the documentation is generated rather than written by hand: the
reason is not recorded.

Saving and releasing are two steps. The renders cost minutes and
tokens beyond reason at every save. With the renders made at the
release only, the README is current at every release and visibly
stale in between, never silently.

## A worked example

An invented thought, taken from no project: a team wants to replace
its weekly status meeting with a written update.

1. The principal writes a brief of a few paragraphs: what he wants,
   why the meeting costs too much, and what is still open. A survey
   of the team's views arrives at the same time and is registered as
   a source.
2. The brief is mined into the intent. Elicitation brings out what
   the principal had not said: who reads the update, and what must
   still be decided face to face. Each surviving thought becomes a
   position; the survey enters only where the principal cites it.
3. The principal asks for an assignment, because the change is to be
   handed to a team lead. The project needs no BRD and no solution
   design, so it has none.
4. A critic finds a gap between a position and the assignment. A
   challenger asks what happens when an update is not written. Both
   are settled by walkthrough, and the intent changes first.
5. One position rests on what is known about written status updates
   elsewhere. A quick research is planned, confirmed and filed.
6. A recipe for a one-page summary for the team is written, and the
   summary is rendered from the assignment.
7. The work is saved after each round and released when the
   principal is satisfied.

## See also

- [The document chain](the-document-chain.md): the chain as a star.
- [The isolated reviewers](isolated-reviewers.md): why the reviewers
  never see the conversation.
- [How a research is made](the-research.md): how a research is
  planned before it is searched.
- [Renders and recipes](renders-and-recipes.md): how an output is
  generated from the artefacts.
- [The work product](the-work-product.md): an output made with work
  of its own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
