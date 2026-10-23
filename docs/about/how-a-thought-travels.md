---
generated: 2026-10-23
version: 5.34
made: derived
inputs-hash: 4ed745d2c1986400
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

The forge moves one idea through a series of versioned documents,
from a rough first text to a saved and released state. This page
follows one invented idea along that way, in the order the idea
meets each station. It is for anyone who wants the whole picture
before the detail: someone about to use the forge, someone about to
extend it, or someone judging whether it fits their work.

## What it is

A thought in the forge belongs to the principal (the person whose
thinking is being forged, who has the final word on all content).
Claude works with the principal and proposes; the principal
composes.

The thought travels a [chain of documents](the-document-chain.md).
Each document of the chain is an artefact. Every artefact has a
definition that says what the artefact is and how it is found, and a
template that says what comes out. The chain starts at a
[brief](../reference/glossary.md), and its trunk is the
[intent](../reference/glossary.md). Below the intent a project takes
only the layers it needs. Many projects end at the intent.

Around the chain stand the other things a thought meets on its way:

- the resources: sources (external inputs) and research notes, which
  may arrive at any stage;
- the [reviewers](isolated-reviewers.md), which press on the
  documents and on the thinking;
- the [renders](renders-and-recipes.md), outputs for an audience
  generated from the chain through recipes;
- the [work products](the-work-product.md), outputs made with work of
  their own;
- the documentation, generated in the same way as a render;
- git, where everything is saved and released.

```
  sources and research (at any stage)
              |
              v
  brief --> intent --> [assignment] --> [solution design]
              |         layers below the intent: only those
              |         the project needs
              |
              +--> renders (through recipes)
              +--> work products (inputs from the chain)
              +--> documentation
              |
  reviewers press on every layer
              |
              v
  saved to git, released
```

## How it works

### The brief

The thought arrives as a brief. A brief is the principal's text of
one whole of thinking: what he wants and why. It is free-form. It
needs no structure, no required content and no IDs, only a small
header. It holds thoughts to be processed, not decisions. A brief is
rough on purpose, because the chiselling of the thought belongs to
the intent.

A brief may arrive in three ways, and all three are equally
legitimate:

- finished outside the forge and stored as it came;
- begun outside and finished with Claude in the forge;
- born in the forge from the first word.

Where a source supports, limits or contradicts a thought of the
brief, the brief names the source beside it.

### The intent

The brief is then mined into the intent. The intent is the working
document: the consolidated current state of what the principal
holds. It is made of positions. A position says what the principal
holds and why, and names what it comes from, a brief or a source.

The intent is not an append-only log. It is rewritten for coherence
every round, and the changes are recorded in its history beside it.
The way to a position (why it changed, what was said, what was
tried) goes into that history, never into the position.

The intent is found by elicitation: Claude draws out by questions
what the principal has not yet put into words. Matters still open
are kept as threads, one file each beside the intent. The intent
says what holds; the threads say what is being worked.

### The layers below the intent

Below the intent a project takes the layers it needs, and no layer
is a condition of another. A layer a project does not have is not
missing.

- **The assignment** is the handover document for the recipients
  (the people or teams who will take the work on). It carries the
  whole in-scope substance of the intent. Nothing is left out for
  brevity, and a silent omission is a defect. A matter is left out
  only as an explicit delegation.
- **The solution design** says how the things wanted are realised.
  It is derived from the lowest layer the project has above it: the
  intent alone, or the assignment.

Feedback from recipients has no channel of its own. The principal
processes it and brings his conclusions back into the intent.

### Sources and research at any stage

Sources may arrive at any stage of a project: before the brief as
material for writing it, during the work on the intent, or after.
A source is stored, registered and catalogued, and nothing more.
Registration does not mean the source is taken in. What each source
is for is the principal's word, and the principal alone directs how
and when it is used. When the content of a source enters the intent,
that is the principal's explicit act, cited with the file it comes
from.

### The reviewers

At every layer, isolated reviewers press on the documents and on the
thinking. Each runs in a subagent: a separate run of Claude that
sees only the files it is given and never the working conversation.

- **The critic** judges the quality of the documents.
- **The challenger** judges the substance of the thinking.
- **The check** verifies mechanical conformance with the conventions.

The principal invokes them by hand. Each produces a dated report
that is never changed. Its findings are settled in a walkthrough
(the items put before the principal one by one, each decided by
him). The decisions are written in one round.

### Renders, work products and the documentation

From the chain the project may generate renders: outputs for one
audience, such as a pitch, an executive summary or the repository
README. A render is never edited by hand. What is iterated is its
recipe, one file with the inputs, the audience, the instructions and
the output template. The render is regenerated from the recipe. A
render opens with its provenance, which cites the recipe and every
input with their versions. A render assigns nothing and is not part
of the chain: the artefacts stay the source of truth.

An output is made in two steps. The first generates the Markdown,
and a plain file where the recipe names a format. The second makes
a designed file through a model, and only on the principal's
command.

Where the project needs work of its own (a model, an analysis, a
worked task), it makes a work product beside the renders. A work
product takes its inputs from the chain and the resources and adds
work of its own. It is two files: the file that holds the content,
and beside it a specification that holds the way and the why. What
the work shows flows back into the intent.

The documentation of a project is generated in the same spirit:
pages of one topic each, made from a documentation map in one run,
and never composed by hand.

### Saved and released

Everything is saved to git. A save runs a light check, then commits
and pushes. A release runs only on the main line of the repository.
It runs its checks, regenerates the README and the release notes,
and then saves with the release message and a tag where the version
calls for one.

### The main courses of events

- **A round of work:** Claude reads the definition of the target
  artefact, the conversation runs by the working methods, and one
  write at the round's end changes the artefact, appends the records
  to its history and brings the ledger (the file that holds the
  project's state, made from its documents) current.
- **A review:** one isolated reviewer is launched, its report is
  filed with IDs, and its findings are settled by walkthrough and
  written in one round.
- **A render:** the Markdown is generated in an isolated subagent
  from a recipe and its inputs, with its provenance, and the designed
  file is made from that render as it lies on disk.
- **Persistence:** a save checks, commits and pushes; a release
  checks, regenerates the README and the release notes, and saves
  with the release message and tag.

## Why

- **The brief is rough** because a required structure would force
  premature tidiness. A brief polished until the intent has nothing
  left to do has gone too far.
- **The intent exists** because the context of a chat dies and
  anything of value must live in a file. It is the document to read
  when returning to a project after weeks, instead of digging
  through old conversations.
- **The assignment is complete** because its goal is to be right,
  not short. Length is whatever fidelity requires.
- **A project takes only the layers it needs** because many ideas
  need no solution written down. A solution design is worth writing
  where the way is not obvious, where a choice has a price, or where
  two people would solve the same matter differently if it were not
  written down.
- **The reviewers never see the conversation** because that
  blindness is the source of their value.
- **A recipe is iterated rather than the render** because the
  artefacts remain the one source of truth. The boundary between the
  chain and a render is authorship: the principal composes an
  artefact, a render is generated from artefacts.
- **A work product is a kind of its own** because stretching the
  render to cover it would have cost the rule that a render is never
  edited by hand.
- **A source is never promoted silently** so that what someone said
  in a meeting does not become the principal's own position without
  his act.
- **Save and release are two steps** because regenerating the
  renders at every save would cost minutes and tokens beyond reason.
  With the renders made at the release only, the README on the main
  line is current at every release and visibly stale in between,
  never silently.
- **The documentation is generated:** the reason is not recorded.

## A worked example

An invented thought, followed from start to end:

1. The principal wants the weekly planning meeting of a team to take
   half the time. He writes a few rough paragraphs: what he wants of
   the meeting, why, and what he does not know yet. That is the
   brief.
2. The principal registers a set of meeting notes as a source and
   says what it is for: material to absorb.
3. With Claude he mines the brief into the intent. Claude asks what
   "half the time" is measured against. The answer becomes a
   position. A question nobody can answer yet becomes a thread.
4. The team that will change the meeting needs a handover, so the
   project takes an assignment. It needs no solution design, so it
   has none, and nothing is missing.
5. The principal runs a critic on the assignment and a challenger on
   the intent. Each reports blind. The findings are settled in a
   walkthrough, and one finding sends a change back into the intent
   first.
6. A recipe for a one-page summary for the team's lead is written,
   and the summary is rendered from it.
7. The principal asks for an analysis of a month of meeting agendas.
   It becomes a work product, and what it shows flows back into the
   intent as a position.
8. The work is saved to git along the way. When the assignment is
   ready to hand over, the principal releases, and the README and
   the release notes are regenerated with it.

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

Generated on 2026-10-23 for version 5.34 from the files the
front-matter names; never edited by hand.
