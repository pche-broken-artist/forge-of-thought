---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 1bba3a6df8ab8833
inputs:
  - CLAUDE.md#Document chain
  - projects/forge/40-solution-design.md#How the parts work together
  - projects/forge/10-intent.md#POS.0110
  - projects/forge/10-intent.md#POS.0120
  - projects/forge/10-intent.md#POS.0130
  - projects/forge/10-intent.md#POS.1400
  - projects/forge/10-intent.md#POS.0400
  - projects/forge/10-intent.md#POS.0710
  - projects/forge/10-intent.md#POS.0180
  - projects/forge/10-intent.md#POS.1100
  - projects/forge/10-intent.md#POS.1520
---

# How a thought travels through the forge

A thought in the forge is one idea of the principal (the person whose
thinking is being forged) that travels from a rough text to versioned
documents, reviewed outputs and a saved release. This page follows
one idea along that way, in the order the idea meets each station. It
is for anyone who wants the whole picture before reading about any
one part: a user, an extender or an evaluator.

## What it is

The way of a thought is a chain of documents, one feeding the next.
It starts at a brief and its trunk is the intent. Below the intent a
project takes the layers it needs, and many projects end at the
intent. Each document of the chain is an artefact: a versioned file
the principal composes with Claude. Around the chain stand the
things that serve it:

- reviewers, who press on the documents and on the thinking;
- outputs for every audience, generated from the chain;
- work products, made beside the chain where the project needs work
  of its own;
- the documentation, generated in the same way as the outputs;
- sources and research, which may arrive at any stage;
- git, where everything is saved and released.

The chain itself, its files and its definitions are described in
[The document chain](the-document-chain.md). Every term on this page
has one line in the [Glossary](../reference/glossary.md).

## How it works

### The brief

The idea first arrives as a brief. A brief is the principal's text of
one whole of thinking: what he wants and why. It is free-form, with
no required content and no IDs. It holds thoughts to be processed,
not decisions. It is rough on purpose. A brief may arrive finished
from outside, be begun outside and finished with Claude, or be born
in the forge from the first word.

### The intent

The brief is then mined into the intent. Mining means the thoughts of
the brief are sifted, and only the intent turns the ones that survive
into positions: what the principal holds and why. The forge calls
this work chiselling. Each artefact is found by questions, research
and sources, as its definition says.

The intent is the consolidated current state of what the principal
wants. It is not a log. It is rewritten for coherence every round,
and the changes of each round go into its history beside it. The way
to a position (what was said, what was tried, which research turned
it) is written into that history, not into the position. What is
still open lives in threads: files of their own beside the intent,
one open matter each.

The work runs intent-first: what changes in substance changes in the
intent before anything below it.

### The layers below the intent

Below the intent the project takes only the layers it needs. None is
a condition of another. Two such layers are:

- the assignment: the distilled handover document for the
  recipients of the work;
- the solution design: how the things wanted are realised.

The assignment carries the whole in-scope substance of the intent.
Nothing is left out for brevity. A matter may be left out only as an
explicit delegation to the recipients.

The solution design is derived from the lowest layer above it: the
intent alone, or the assignment. A project that lacks a layer is not
missing anything.

Feedback from the recipients has no channel of its own. The
principal works it through and brings his conclusions back into the
intent.

### The reviewers

At every layer, isolated reviewers press on what was written. Each
runs as a subagent, that is a separate instance of Claude started
for one job, which sees the files it is given and never the working
conversation. There are three kinds:

- the critic (`/critique`): the quality of the documents, never the
  substance;
- the challenger (`/challenge`): the substance of the thinking;
- the check (`/check`): mechanical conformance with the conventions.

The principal starts the critic and the challenger by hand. Each
report is filed, dated and never changed. Its results are settled by
walkthrough: the principal judges them one item at a time, and the
verdicts are written in one round. Why the reviewers are kept blind
is explained in [The isolated reviewers](isolated-reviewers.md).

### Outputs for every audience

From the chain the project generates renders: outputs for one
audience each, such as a pitch, an architecture picture, an
executive summary or the README. A render is never edited by hand.
What the principal iterates is its recipe: one versioned file with
the inputs, the audience, the instructions and the template of the
output. `/render` makes the Markdown from the recipe, and `/publish`
makes a designed file from that render where the principal asks for
one. Every render opens with its provenance: the recipe and every
input, with their versions. How this works in full is in
[Renders and recipes](renders-and-recipes.md).

### Work products

Where the project needs work of its own (a model, an analysis, a
worked task), Claude makes a work product beside the chain. It is
two files. One file holds the content. Beside it a specification
holds the way and the why: the task, the items and files it starts
from, the method, the assumptions and what is open. The file is
made again from the specification whenever the specification
changes. What the work shows flows back into the intent. See
[The work product](the-work-product.md).

### The documentation

The documentation of a project is generated in the same spirit: pages
of one topic each, made from a documentation map that lies beside
the project's ledger (the file that holds the state of the project).
It is never composed by hand. One command, `/document`, makes it and
regenerates only what changed.

### Sources and research

Sources and research may arrive at any stage: before the brief as
material for writing it, during the work on the intent, or after.
A source is an external input, such as a transcript, an offer, a
document or a standard. It is stored, registered and catalogued, and
never changed after registration. Registration does not mean the
source enters the thinking. The principal alone directs how and when
each source is used. When a source does enter the intent, it is his
explicit act, cited with the file it comes from. Research lives in
the project's `research/` directory, catalogued beside the sources.

### Saving and releasing

Everything is saved to git. Two commands do it:

- `/save` runs a light check and then commits and pushes, in
  seconds;
- `/release` runs its checks, settles them, regenerates the README
  and the release notes, and then saves with the release message and
  its tag.

### The main courses of events

- A round of work: `/forge` reads the definition of the target
  artefact, the conversation runs by the working methods, and one
  write at the round's end changes the artefact, appends the records
  to its history and brings the ledger current.
- A review: one isolated agent is launched, its report is filed with
  IDs, and its results are settled by walkthrough and written in one
  round.
- A render: the Markdown is generated in an isolated subagent from a
  recipe and its inputs, with its provenance, and the designed file
  is made from the render as it lies on disk.
- Persistence: a save runs its check and then commits and pushes; a
  release runs its checks, regenerates the README and the release
  notes, and then saves with its message and tag.

## Why

- The brief is rough on purpose. A required structure would force
  premature tidiness, and the chiselling belongs to the intent.
- The intent is a file and not a conversation. A conversation's
  context dies, so anything of value must live in a file. The intent
  is the document to read when returning to a project after weeks,
  instead of digging through old conversations.
- The way to a position goes into the history. It is written there in
  the same step as the position, while the whole context is at hand.
- The assignment leaves nothing out in silence. A silent omission is
  a defect, and leaving a matter out is legitimate only as an
  explicit delegation.
- Many projects end at the intent. There, what is wanted needs no
  solution written down. A solution design is worth writing where the
  way is not obvious, where a choice has a price, or where two hands
  would solve the same matter differently if it were not written
  down.
- The reviewers never see the conversation. That blindness is the
  source of their value.
- A render is never edited by hand. The artefacts stay the one source
  of truth, and each rendering derives its words again from the
  current inputs.
- A work product is a kind of its own and not a render. Stretching
  the render to cover it would have cost the rule that a render is
  never edited by hand.
- A source's word never becomes the principal's own in silence. What
  someone said in a meeting is not a position until the principal
  takes it in.
- Save and release are two commands. The renders cost minutes and
  tokens beyond reason at every save. With the renders made at the
  release only, the README is current at every release and visibly
  stale in between.
- The documentation is generated and never composed by hand. The
  reason is not recorded.

## A worked example

An invented thought, followed through a project with the placeholder
slug `my-idea`:

1. The principal wants a shorter onboarding for new colleagues. He
   writes a brief of a few topics, each with some sentences of what
   he wants, and what is still open.
2. Over a few rounds the brief is mined into the intent. Some
   thoughts become positions with their reasons; one is dropped; one
   question stays open as a thread.
3. A slide deck from a vendor arrives midway and is registered as a
   source. The principal decides it is a standard to check against,
   and later takes one of its facts into the intent with its
   provenance.
4. A challenger reads the intent blind and asks whether a shorter
   onboarding is the real problem. The principal settles the
   challenge in a walkthrough and changes one position.
5. The work is to be handed to a team, so the project takes an
   assignment. The way is obvious, so it takes no solution design.
6. A recipe for a one-page summary for the management is iterated,
   and the summary is rendered from the intent.
7. The team asks for an estimate of the effort. Claude makes it as a
   work product with its specification; one conclusion of it goes
   back into the intent.
8. The principal saves along the way and, when the whole is settled,
   releases the project with its README and release notes
   regenerated.

```
source ─┐            research ─┐
        ▼                      ▼
     brief ──► intent ──► assignment ──► solution design
                 │  ▲         (only the layers the project needs)
                 │  └──── work product (what it shows flows back)
                 ├──► renders, through recipes
                 └──► documentation
   reviewers press on every layer;   save ──► release
```

## See also

- [The document chain](the-document-chain.md): the chain as a star.
- [The isolated reviewers](isolated-reviewers.md): why the reviewers
  never see the conversation.
- [Renders and recipes](renders-and-recipes.md): how an output is
  generated from the artefacts.
- [The work product](the-work-product.md): an output made with work
  of its own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
