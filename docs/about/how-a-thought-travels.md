---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: a3b36b2cd2e3d57d
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

A thought in the forge is one idea that moves through a chain of
versioned documents, from a rough brief to a saved release. This
page follows one invented, generic idea through every station it can
meet, in the order it meets them. It is for anyone who wants the
whole journey in one place before reading about each station: a
user, someone who extends the forge, or someone judging whether it
fits their work.

## What it is

The forge is a workshop for thinking. The principal (the person
whose thinking is being forged, with final authority on all content)
brings an idea. Claude helps the principal shape it, keeps the
structure and the order, and proposes without deciding. The idea
travels a chain of documents, each with a number in its file name so
that the chain can grow without renaming anything. The
[Glossary](../reference/glossary.md) has every term of the forge in
one line.

The journey has fixed stations and optional ones:

- the brief, where the idea arrives;
- the intent, the trunk every project has;
- the layers below the intent, taken only where the project needs
  them;
- the reviewers, who press on the documents at any layer;
- the research, run where a position will rest on what the world
  already knows;
- the outputs for an audience, the work products and the
  documentation, all made from the chain;
- the save and the release into git.

Sources and research can arrive at any stage.

```
sources ─┐                          ┌─ reviewers (any layer)
research ┤                          │
         ▼                          ▼
      brief ──► intent ──► [assignment] ──► [BRD] ──► [solution design]
                  │
                  ├──► renders (through recipes)
                  ├──► work products
                  └──► documentation
                              │
                              ▼
                       save ──► release
```

The layers in square brackets are optional. Many projects end at the
intent.

## How it works

The invented idea here is: "a team wants to change how it welcomes
new colleagues". The project has the placeholder slug `my-idea`.

### It arrives as a brief

The principal writes down what he wants and why, and what he does
not want. This text is the brief. A brief is free-form: any
structure the principal finds useful, no required content and no
item IDs. It holds thoughts to be processed, not decisions. It is
rough on purpose. Some thoughts in it will be dropped later.

A brief can arrive in three ways, and the forge treats them alike:

- finished outside and stored as it came;
- begun outside and finished with Claude;
- born with Claude from the first word.

A brief is versioned like every document of the chain. It stays the
provenance of what is later taken from it.

### It is chiselled into the intent

The intent is the working document: the current state of what the
principal holds. Claude draws the thoughts of the brief out into
positions by elicitation (questions that help the principal say what
he has not yet put into words). Taking positions out of a brief is
called mining it.

The intent is not a log. It is rewritten for coherence every round.
A round is one working conversation: answers are carried in the
conversation, and one write at its end changes the intent. Each
change goes into the intent's history, a log kept in a companion
file beside it. The way to a position (what was said, what was
tried, which research turned it) goes into that history, not into
the position.

Matters still open live as threads, one file each beside the intent.
A thread carries the debate while it is unsettled. What comes to hold
goes into the intent.

### It takes the layers it needs below the intent

Below the intent a project takes only the layers it needs. No layer
below the intent is a condition of another. A layer a project does
not have is not missing. Many projects end at the intent.

- **Assignment.** The handover document for the recipients:
  complete, precise and self-contained. It carries the whole
  in-scope substance of the intent. Leaving a matter out is allowed
  only as an explicit delegation.
- **BRD.** The business requirements that break the parent layer
  into rules the stakeholders of each area can review on their own.
- **Solution design.** How the things wanted are realised, derived
  from the lowest layer above it. It is worth writing where the way
  is not obvious, where a choice has a price, or where two hands
  would solve the same matter differently if it were not written
  down. Whether it is written, the principal says.

A change of substance goes into the intent first and then down the
chain the project has. Only wording is fixed in a lower layer
directly. More on the chain is in
[The document chain](the-document-chain.md).

### Blind reviewers press on it

At any layer the principal can call a reviewer. Each reviewer runs
as an isolated subagent (a separate Claude instance that sees only
the files it is given) and never sees the working conversation. That
blindness is where its value comes from.

- **The critic** looks at the quality of a document, through one of
  its lenses.
- **The challenger** looks at the substance of the thinking, through
  one of its personas.
- **The check** looks at mechanical conformance with the
  conventions.

Each produces a dated report that is never changed afterwards. The
principal settles the findings in a walkthrough (one item at a time,
each with a verdict), and the results are written in one round. More
is in [The isolated reviewers](isolated-reviewers.md).

### Research is planned and run where it carries weight

Suppose a position on welcoming new colleagues will rest on what is
already known about it. Claude then proposes a research. The plan is
shown first, before anything is searched, and the principal confirms
it in a walkthrough. The plan names the purpose, the perspectives,
the assumptions, what is left out, and the cards. A card is one
question, answered by one kind of evidence from one kind of source.

There are two depths. A quick research answers one card in one note.
A deep research runs one isolated agent per card and files a bundle
with the plan and a synthesis at its head. Claude proposes deep where
a position, a layer of the chain or a design will rest on the answer.
Notes and bundles are never changed once filed. More is in
[How a research is made](the-research.md).

### Sources arrive at any stage

The team's existing welcome checklist, or a transcript of a meeting
about it, is an external input. It is stored in the project's
`sources/` and never changed once registered. It can arrive before
the brief, during work on the intent, or later. Registering a source
does not mean its content is used. The principal alone says how and
when a source is used. When its content enters the intent, it is the
principal's explicit act, cited with its file. What someone said in a
meeting never silently becomes the principal's own position.

### Outputs are generated for every audience

The principal may want a short summary for the team's management.
That is a render: an output for one audience, generated from the
chain. A render is never edited by hand. What is iterated is its
recipe: one file with the inputs, the audience, the instructions and
the output template. Each render opens with its provenance: the
recipe and every input, with their versions. A render assigns
nothing and is not part of the chain. More is in
[Renders and recipes](renders-and-recipes.md).

The project may also need an output with work of its own, such as an
analysis of the current welcome process. That is a work product: the
file with the content, and beside it a specification of the way and
the why. The principal works with the file freely. A conclusion that
is to hold goes into the intent first. More is in
[The work product](the-work-product.md).

The documentation of a project is generated the same way: pages of
one topic each, made from a map and never composed by hand.

### It is saved to git and released

Every project is saved to git. A save runs a light check and then
commits and pushes, with no render. A release runs from the main
line only. It runs its checks, regenerates the README and the release
notes, and then saves with the release message and, at an approved
major version, a tag.

### The main courses of events

- **A round of work:** Claude reads the definition of the target
  document, the conversation runs by the working methods, and one
  write at the end changes the document, appends the records to its
  history and brings the ledger (the one record of the project's
  state, made from the documents when read) current.
- **A review:** one isolated agent runs, its report is filed with
  IDs, and the findings are settled by walkthrough and written in one
  round.
- **A render:** an isolated subagent generates the Markdown from a
  recipe and its inputs and writes the provenance; a designed file
  can then be made from the render as it lies on disk.
- **Persistence:** a save runs its check and commits and pushes; a
  release runs its checks, settles them, regenerates the README and
  the release notes, and then saves with the release message and tag.

## Why

- **A rough brief.** No structure is required, because a required
  one would force premature tidiness. The chiselling belongs to the
  intent. A brief polished until the intent has nothing left to do
  has gone too far.
- **An intent rewritten every round.** It exists because the context
  of a chat dies, and anything of value must live in a file. It is
  the document to read when returning to a project after weeks,
  instead of digging through old conversations.
- **Layers only where needed.** Many projects end at the intent,
  because what is wanted there needs no solution written down.
- **An assignment that leaves nothing out.** A silent omission is a
  defect. Length is whatever fidelity requires.
- **Blind reviewers.** Not seeing the conversation is the source of
  their value.
- **A plan before the search.** The quality of a research is made by
  breaking the topic into questions, not by the searching. The plan
  is where the principal sees the questions before they cost
  anything.
- **Renders never edited by hand.** The artefacts of the chain stay
  the only source of truth. The line between the chain and a render
  is authorship: the principal composes the chain, and a render is
  generated from it.
- **A work product as a kind of its own.** Stretching the render to
  cover it was weighed and dropped. It would have cost the rule that
  a render is never edited by hand.
- **Save and release as two commands.** Rendering at every save would
  cost minutes and tokens beyond reason. With the renders made at the
  release only, the README on the main line is current at every
  release, and visibly stale in between.
- **Sources at any stage.** The reason they may arrive at any stage
  is not recorded.
- **Documentation generated.** The reason it is generated rather
  than composed is not recorded.

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

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
