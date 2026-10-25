---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: 2829d65f8f86ea5b
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

A thought in Forge of Thought travels a chain of versioned documents.
It starts as a rough text and ends in a saved release. This page
follows one invented idea along that route, station by station, in
the order the idea meets them. It is for anyone who uses the forge,
extends it or weighs it, and wants the whole route in one view before
reading about the parts.

## What it is

The route is the document chain with everything that stands around
it. The chain is a row of versioned documents, called artefacts. Each
artefact has a definition: a file that says what the artefact is, how
it is found and what rules it keeps. Each definition is paired with a
template, which says what comes out. The chain starts at a brief. Its
trunk is the intent. Below the intent a project takes the layers it
needs, and none of them is a condition of another. The page
[The document chain](the-document-chain.md) describes the chain as a
star.

Two parties work the chain:

- the principal: the person whose thinking is being forged, with the
  final word on all content;
- Claude: it proposes, structures and keeps the documents in order,
  and never decides.

Around the chain stand four things that a thought meets on the way:

- blind reviewers, who press on the documents and on the thinking;
- research, where a position will rest on what the world already
  knows;
- outputs for every audience, generated from the chain;
- git, where everything is saved and released.

The route in one picture:

```
 sources and research (at any stage)
          |
          v
  brief --> intent --> [ assignment ] --> [ BRD ] --> [ solution design ]
              |            the layers a project takes; many end at the intent
              |
              +--> renders (through recipes), the README and release notes
              +--> work products (beside the chain)
              +--> documentation (generated the same way)

 reviewers at every layer        save and release through git
```

## How it works

### The brief

A brief is the principal's text of one whole of thinking. It says
what he wants and why. It is free-form: any structure he finds useful,
no required content and no IDs, only a small header. It holds
thoughts to be processed, not decisions. A thought in a brief may be
changed, reworked or dropped when it is mined into the intent.

A brief may arrive in three ways, all equally legitimate:

- finished from outside, stored as it came;
- begun outside and finished with Claude;
- born with Claude from the first word.

A brief is versioned like every artefact. It is composed in a round
or two and then mined.

### The intent

The intent is the working document. It holds the current state of
what the principal intends, as positions. A position says what the
principal holds and why, and names what it comes from: a brief or a
source.

The intent is found by elicitation. Claude draws out by questions
what the principal has not yet put into words. The intent is not a
log. It is rewritten for coherence every round. The way to each
change (why it changed, what was said, what was tried) is written
into the intent's history, a companion file beside it, in the same
step.

Matters that are still open live in threads. A thread is a file of
its own beside the intent. It says what is open and where it came
from. An unfinished conversation is saved into its thread. A settled
thread stays as it is, and what holds goes into the intent.

The iteration default is intent-first. A change of substance is made
in the intent and carried down from there.

### The layers below the intent

Below the intent a project takes the layers it needs. Many projects
end at the intent, where what is wanted needs no solution written
down. A layer a project does not have is not missing. The number in
a file name orders the files and prescribes no sequence.

The layers the chain has are these:

- the assignment: the handover document for the recipients
  (complete, precise, structured and self-contained);
- the BRD: the business requirements that the stakeholders of each
  area review on their own;
- the solution design: how the things wanted are realised.

The assignment carries the whole in-scope substance of the intent.
A silent omission is a defect. A matter may be left out only as an
explicit delegation to the recipients.

The solution design is derived from the lowest layer the project has
above it. That layer is the intent alone, the assignment or the BRD.
Whether a solution design is written is the principal's word.

### The reviewers at every layer

At every layer, isolated reviewers press on what was written. Each
runs in a subagent: a separate run of Claude that sees only the files
it is given and never the working conversation. There are two kinds
of reviewer, and beside them the checks:

- the critic: the quality of the documents, through one of its
  lenses;
- the challenger: the substance of the thinking, through one of its
  personas;
- the check: the mechanical conformance with the conventions.

The principal invokes them by hand, through `/critique`,
`/challenge` and `/check`. Each run produces an immutable, dated
report. Its findings are settled in a walkthrough: the items are put
to the principal one at a time, and he gives a verdict on each. The
page [The isolated reviewers](isolated-reviewers.md) says why the
reviewers never see the conversation.

### Research where a position will rest on it

A research is planned before anything is searched. Claude shows the
plan and the principal confirms it in a walkthrough. The plan names
the purpose, the angles from which the topic is looked at, the
assumptions, what is left out, and the questions to be answered. A
research comes in two depths:

- quick: one question, answered and filed as one note;
- deep: one isolated agent per question, filed as a bundle with the
  plan and a synthesis at its head.

A deep research fits where a position, a layer of the chain or a
design will rest on the answer. The page
[How a research is made](the-research.md) describes the plan and the
depths.

### Sources at any stage

External inputs live in the project's `sources/`: transcripts,
offers, documents, standards. They are immutable once registered.
They may arrive at any stage: before the brief as material for
writing it, during the work on the intent, or after. Registering a
source does not take it in. The principal alone directs how and when
a source is used. When the content of a source enters the intent, it
is his explicit act, cited with the file it came from. What someone
said in a meeting is never silently turned into the principal's own
position.

### Outputs for every audience

A render is an output for one audience, generated from the chain.
Examples are a pitch, an architecture picture, an executive summary
and the repository README. A render is never edited by hand. What is
iterated is its recipe: one file that holds the inputs, the audience,
the instructions and the template of the output. Every render opens
with its provenance, citing the recipe and every input with their
versions. A render assigns nothing and is not part of the chain. The
page [Renders and recipes](renders-and-recipes.md) describes how an
output is generated from the artefacts.

A work product is an output made with work of its own: a model, an
analysis, a worked task, in whatever form the work needs. It takes
its inputs from the chain and the resources and adds work of its
own. It is two files:

- the file that holds the content;
- beside it, a specification that holds the way and the why.

The principal works with the file freely. A conclusion that is to
hold goes into the intent first. The page
[The work product](the-work-product.md) describes it in full.

The documentation is generated the same way. It is pages of one topic
each with an index, made from a documentation map that the reader
never sees. It is never composed by hand.

### Saved and released

Everything is saved to git. Two commands do it, at two speeds:

- `/save` runs a light check and then commits and pushes, with no
  render;
- `/release` runs on the main line only, runs its checks, regenerates
  the README and the release notes, and then saves with the release
  message.

### The main courses of events

- A round of work: Claude reads the definition of the target
  artefact, the conversation runs, and one write at the round's end
  changes the artefact, appends its records to the history and brings
  the ledger (the single source of truth for a project's state)
  current.
- A review: one isolated agent runs, its report is filed with IDs,
  and its findings are settled by walkthrough and written in one
  round.
- A render: the output is generated in an isolated subagent from a
  recipe and its inputs, with its provenance; a designed file is then
  made from the render as it lies on disk, on the principal's command.
- Persistence: a save runs its check and commits and pushes; a
  release runs its checks, settles them, regenerates the README and
  the release notes, and saves.

## Why

The brief is rough on purpose. A required structure would force
premature tidiness. The chiselling belongs to the intent, and a
brief polished until the intent has nothing left to do has gone too
far.

The intent exists because the context of a chat dies. Anything of
value must live in a file. The intent is the document to read when
returning to a project after weeks, instead of digging through old
conversations.

State lives in Markdown files of the project. It never lives in the
conversation or in the assistant's memory.

Many projects end at the intent, and no layer is a condition of
another. A solution design is worth writing where the way is not
obvious, where a choice has a price, or where two hands would solve
the same matter differently if it were not written down.

The reviewers are blind to the working conversation. That blindness
is the source of their value.

A research is planned first. Its quality is made by breaking the
topic into questions, not by the searching. The plan is where the
principal sees the questions before they cost anything.

A render is generated and its recipe iterated, so that the artefacts
remain the sole source of truth. The template of a recipe fixes the
structure, never the wording. Fixing the text would turn the recipe
into the render and make the inputs meaningless.

A work product is a kind of its own and not a render. Stretching the
render to cover it would have cost the rule that a render is never
edited by hand.

Save and release are two commands. Regenerating the renders costs
minutes and tokens beyond reason at every save. With the renders at
the release only, the README on the main line is current at every
release and visibly stale in between.

## A worked example

An invented thought: a team wants new colleagues to be productive in
their first week.

1. The principal writes a brief of a few paragraphs: what he wants of
   the first week, why it matters, and what is still open. A
   checklist from another team arrives and is registered as a source.
2. With `/forge`, Claude and the principal mine the brief into the
   intent. Claude asks one question at a time. At the round's end the
   principal confirms the write, and the intent holds the positions,
   one of them citing the checklist as its source. A question nobody
   can answer yet becomes a thread.
3. A challenger reads the intent blind and asks whether the idea has
   considered colleagues who join remotely. The principal accepts it
   in a walkthrough, and the intent changes in the next round.
4. One position will rest on what is known about onboarding
   elsewhere. Claude proposes a research plan, the principal confirms
   it, and the notes are filed in `research/`.
5. The principal wants the work handed to another team, so the
   project takes an assignment. It needs no BRD and no solution
   design, so it has none.
6. A recipe for a one-page summary for the management is composed,
   and the summary is generated from the intent.
7. The principal saves the work with `/save` and, when the
   assignment is approved, releases it with `/release`.

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
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
