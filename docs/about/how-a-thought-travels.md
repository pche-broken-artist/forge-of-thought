---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 6a552ab1fef27269
inputs:
  - CLAUDE.md#Document chain
  - projects/forge/40-solution-design.md#How the parts work together
  - projects/forge/10-intent.md#POS.0110
  - projects/forge/10-intent.md#POS.0120
  - projects/forge/10-intent.md#POS.0130
  - projects/forge/10-intent.md#POS.1800
  - projects/forge/10-intent.md#POS.1990
  - projects/forge/10-intent.md#POS.1400
  - projects/forge/10-intent.md#POS.0400
  - projects/forge/10-intent.md#POS.0540
  - projects/forge/10-intent.md#POS.1860
  - projects/forge/10-intent.md#POS.0710
  - projects/forge/10-intent.md#POS.0180
  - projects/forge/10-intent.md#POS.1100
  - projects/forge/10-intent.md#POS.1520
---

# How a thought travels through the forge

The road of a thought through the forge is a chain of versioned
documents that begins at a rough brief and ends at a saved release.
This page follows one invented thought along that road, station by
station, in the order the thought meets them. It is for a user, an
extender or an evaluator who wants to see the whole road once before
reading about a single station. Every term of the forge is said in
one line in the [Glossary](../reference/glossary.md).

## What it is

The forge is not a program. It is a set of instructions that Claude
reads, with the deterministic work kept in scripts. A thought that is
worked in the forge does not live in the conversation and does not
live in Claude's memory. It lives in the Markdown files of a project,
and a project is a directory.

The thought belongs to the principal (the person whose thinking is
being forged). Claude proposes and the principal composes.

The road has this shape:

```
 sources and research (may arrive at any stage)
      |             |                |
      v             v                v
    brief  --->  intent  --->  layers the project needs
   (rough)     (positions)     (assignment, BRD, user stories,
                                solution design; many take none)
      ^             ^                ^
      |             |                |
 reviewers who never saw the conversation
 (critic: the documents; challenger: the thinking;
  checks: the conventions)

 outputs:  renders through recipes, work products,
           the documentation
 git:      everything saved, then released
```

The chain ([The document chain](the-document-chain.md)) starts at a
brief, and the intent is its trunk. Below the intent a project takes
the layers it needs.

The thought followed on this page is invented. A principal who leads
a team thinks that a new colleague takes too long before he can work
on his own. He wants the first week of a newcomer to go differently.

## How it works

### 1. The thought arrives as a brief

A brief is the principal's text of one whole of thinking: what he
wants and why. It is free-form. Any structure the principal finds
useful is allowed and none is required. It has no required content
and no IDs, only a minimal header. A brief holds thoughts to be
processed, not decisions. A thought of a brief may be changed,
reworked or dropped later, and only the intent turns it into a
position.

A brief is rough on purpose. Its usual shape is light:

- the topics of the whole, each with a few sentences of what the
  principal wants of it;
- the research that verifies or limits a topic, cited beside it;
- what is still open.

What is gathered before a brief is wide: research, sources, the
principal's ideas and Claude's. What goes into the brief and what
stays out is the principal's decision. A brief is composed in a round
or two. It may arrive in three ways, and the forge does not
distinguish them:

- it arrives finished from outside and is stored as it came;
- it is begun outside and finished with Claude in the forge;
- it is born in the forge from the first word.

A brief is versioned like every artefact (a document of the chain).
It is a draft until the principal approves it, and it may change
after that.

In the example, the principal writes one page with four topics:

- what a newcomer needs on the first day;
- who answers his questions;
- how the team learns whether the first week worked;
- a printed handbook for every newcomer.

One line of the page says what is open: who keeps the list of what a
newcomer needs.

### 2. The brief is worked into the intent

The intent (`10-intent.md`) is the working document of the project:
the consolidated current state of what the principal wants. The
thoughts of the brief are turned into positions there. The forge
calls this mining the brief. A position says what the principal holds
and why it holds, and it names what it comes from: a brief or a
source. Not every thought of a brief survives.

The work runs in rounds. Claude reads the definition of the intent
(the file that says what an artefact is and how it is found: by
questions, research and sources). An artefact is composed in one of
two ways:

- by elicitation: Claude draws the content out by questions;
- handed over: Claude proposes, with its assumptions and choices
  listed, and the principal judges.

One write at the end of a round changes the intent, appends the
records to its history and brings the ledger (the file that shows
the state of the project) up to date.

The intent is not a log. It is rewritten for coherence in every
round, and the changes are recorded in its history. The way to a
position does not belong in the position: why it changed, what was
said on the way, which research turned it. All of that is written
into the history in the same step that writes the position. What is
still being worked waits in a thread: the intent says what holds,
the threads say what is being worked.

In the example, Claude asks what "work on his own" means. The
principal answers that the newcomer closes one ordinary task without
help. Three topics become positions, each citing the brief. The
printed handbook does not survive the questions and is dropped. The
open matter of who keeps the list waits in a thread.

### 3. The project takes the layers it needs

Below the intent a project takes the layers it needs. No layer is a
condition of another, and a layer the project does not have is not
missing. Many projects end at the intent, where what is wanted needs
no solution written down.

| Layer | File | What it is |
|---|---|---|
| Assignment | `20-assignment.md` | the distilled handover document for the recipients |
| BRD | `30-brd.md` | the business requirements, broken into rules that the stakeholders of each area review on their own |
| User stories | `35-user-stories.md` | the layer above broken into behaviour seen from the outside ([The user stories](the-user-stories.md)) |
| Solution design | `40-solution-design.md` | how the things wanted are realised |

The number in a file name orders the files and prescribes no
sequence. The gaps of ten leave room for a layer to be added without
renumbering. Each layer is an artefact with a definition of its own,
and the definition names the inputs of the artefact.

The assignment is complete, precise, structured and self-contained.
It carries the whole in-scope substance of the intent. A matter is
left out only as an explicit delegation, and a silent omission is a
defect. What the recipients do with an assignment handed to them is
their own run of the forge.

The solution design is derived from the lowest layer the project has
above it. It is worth writing in three cases:

- the way is not obvious;
- a choice has a price;
- two hands would solve the same matter differently if it were not
  written down.

Whether it is written, the principal says. From the artefacts of the
chain the thing must be buildable without a look at the finished
product.

In the example, the principal wants to hand the matter over to the
leads of three teams. The project takes an assignment and nothing
below it. No system is to be built and the way is obvious, so the
chain of this project ends at the assignment.

### 4. Reviewers who never saw the conversation press on the thought

At every layer the principal may call a reviewer
([The isolated reviewers](isolated-reviewers.md)). There are three
kinds of one shape:

- the critic reads the quality of the documents;
- the challenger reads the substance of the thinking;
- the checks read mechanical conformance, never substance or
  document quality.

Each runs as an isolated subagent (a separate run of Claude that
sees the files it is given and never the working conversation). The
critic has lenses, the challenger has personas, and there is one
agent per kind of check. The critic and the challenger may be given
a target: one artefact, or any file of the project by its path.
Without a target they read the whole chain.

A review leaves a dated report that is never changed afterwards. Its
findings carry IDs and are settled in a walkthrough (the findings
are put to the principal, who decides each). What he decided is
written in one round. The checks are read-only and advisory: they
report and propose, and the principal decides what is fixed.

No reviewer runs on Claude's own judgement. A run happens on the
principal's word. The word may be given once, in the definition of a
command that names the checks it runs: a save and a release have it
so. Neither the critic nor the challenger runs at a save.

In the example, the principal calls the critic on the intent, and
the report names a position that can be read in two ways. He calls a
challenger, which asks what becomes of the newcomer when the
colleague who answers his questions is away. He runs a check, which
reports where a file departs from the conventions. The principal
decides each finding in a walkthrough, and one round writes what he
decided.

### 5. Research is run where a position will rest on it

A research ([How a research is made](the-research.md)) answers what
the world outside already knows. It is planned before it is searched.
Claude shows the plan before anything is searched, and the principal
confirms it in a walkthrough. The plan holds:

- the purpose;
- the perspectives from which the topic is looked at;
- the assumptions;
- what is left out;
- the cards, each one question answered by one kind of evidence from
  one kind of source;
- the agents and the rule that fixed their count.

A research has two depths:

- quick: one card, filed as one note;
- deep: one isolated agent per card, filed as a bundle with the plan
  and the synthesis at its head.

Claude proposes the depth in the plan with its reason, and the
principal decides. Quick fits where one question is to be answered
and cited. Deep fits where a position, a layer of the chain or a
design will rest on the answer. Every agent sees a packet composed
from the forge's own definition and nothing of the conversation. The
synthesis is made by Claude from the notes alone, with its own view
last and apart. A note, a bundle and its plan are immutable from
their filing.

In the example, one position says that a named colleague accompanies
every newcomer through the first week. The principal wants to know
what is known about such accompanying before the assignment rests on
it. Claude proposes a deep research and shows the plan. The principal
strikes one card in the walkthrough and confirms the rest. The
synthesis limits the position, and the position is rewritten in the
next round on the intent. Which research turned it is written into
the history.

### 6. Outputs are generated for every audience

A project makes three kinds of output beside its artefacts.

**Renders** ([Renders and recipes](renders-and-recipes.md)). A
render is an output for one audience, generated from the chain: a
pitch, an architecture picture, an executive summary, the README of
the repository. A render is never edited by hand. What is iterated
is its recipe. A recipe is one versioned file that holds:

- the inputs;
- the audience;
- the instructions;
- the template of the output.

The template fixes the structure and what information appears where,
never the wording. A render is generated in an isolated subagent and
opens with its provenance, which cites the recipe and every input. A
render assigns nothing and is not part of the chain: the artefacts
stay the source of truth. The boundary between the two is
authorship. An article the principal writes is a layer of the chain,
and its translation is a render.

An output is made in two steps, each with its own command. `/render`
makes the render and its plain file: it is cheap and repeated
freely. `/publish` makes the designed file: it is expensive and runs
only on the principal's command.

**Work products** ([The work product](the-work-product.md)). A work
product is an output that is neither an artefact nor a render: any
result of Claude's work the principal asked for, such as a model, an
analysis or a worked task. It takes its inputs from the chain and
the resources and adds work of its own. It is two files: the file
that holds the content, and beside it the specification that holds
the way and the why. The file is made again from the specification
whenever the specification changes, and the principal works with the
file freely. What a work product shows flows back into the intent.

**The documentation.** The documentation is generated, never
composed by hand: pages of one topic each, with an index, for the
user, the extender and the evaluator.

What comes back from the recipients has no channel of its own. The
principal processes it and feeds the conclusions back into the
intent.

In the example, the principal and Claude compose a recipe for a
one-page summary for the management, and the summary is rendered.
The principal also asks for an analysis of the hours the first week
costs a team. The analysis is a work product: a table, with its
specification beside it. What the table shows becomes a position in
the next round on the intent.

### 7. Everything is saved to git and released

Save and release are two commands. A save runs the light check and
then commits and pushes: no render, a matter of seconds. The
principal may leave the check out for a save he wants on the remote
at once. A release runs its checks and settles them with the
principal, regenerates the README and the release notes, and then
saves with the release message. At an approved major version it also
sets a tag. The number of a release is the version of the intent. A
release offers the documentation as well, and the README is made
from the documentation as the release leaves it.

In the example, the principal saves after every round. When the
assignment is approved, he releases: the checks run, he settles what
they report, the README and the release notes are regenerated, and
the release is saved to git.

### Sources and research arrive at any stage

External inputs (transcripts, offers, documents, standards) live in
`sources/` of the project and are immutable once registered. They
may arrive at any stage of a project's life:

- before the brief, as material for writing it;
- during the work on the intent;
- after it.

`/ingest` stores, registers and catalogues a source, and nothing
more. Registration does not imply intake. What a source is for is
individual (a standard to verify against, inspiration, a meeting
record, material to absorb). It is noted as the Role of the source
in the index of the directory. The Role is the principal's word: it
is asked for before the entry is written and never inferred. The
principal alone directs how and when a source is used. When the
content of a source does enter the intent, it is his explicit act,
cited with provenance.

Research arrives at any stage too. A brief cites the research that
verifies or limits its topics. The definition of every artefact says
how the artefact is found: by questions, research and sources. A
position, a layer of the chain or a design may rest on a research.

The directories `sources/` and `research/` each carry an index: a
light catalogue that tells Claude and the principal what resources
exist and what they are for without re-reading them. The index
tracks nothing, and no command takes it as an automatic input.

In the example, the notes of a meeting with the team leads arrive
after the intent stands. They are registered as a source with the
Role of a meeting record. One lead said in the meeting that the
first week should begin with a real task. That sentence is not the
principal's position. He takes it up in a round on the intent, and
the new position cites the file.

### The main courses of events

The main courses of events, each in one sentence:

- **A round of work.** `/forge` reads the definition of the target
  artefact, the working conversation runs, and one write at the
  round's end changes the artefact, appends the records to its
  history and brings the ledger up to date.
- **A review.** `/critique`, `/challenge` or `/check` launches one
  isolated agent, its report is filed with IDs, and the findings are
  settled by walkthrough and written in one round.
- **A render.** `/render` generates the Markdown in an isolated
  subagent from a recipe and its inputs and writes the provenance,
  and `/publish` makes the designed file from the render as it lies
  on disk.
- **A save.** `/save` runs the light check and then commits and
  pushes.
- **A release.** `/release` runs its checks, settles them,
  regenerates the README and the release notes, and then saves with
  the release message and tag.

## Why

The reasons recorded for the shape of the road:

- **The thought lives in files.** The context of a chat dies, and
  anything of value must live in a file. The intent is the document
  to read when returning to a project after weeks, instead of
  digging through old conversations.
- **A brief is rough and free-form.** A required structure would
  force premature tidiness. A brief polished until the intent has
  nothing left to do has gone too far.
- **The way to a position goes into the history.** It is written in
  the same step as the position, while the whole context is at hand.
- **The layers are taken as needed.** Where what is wanted needs no
  solution written down, the chain ends at the intent.
- **The assignment has no size target.** Its length is whatever
  fidelity requires: the goal is to have it right, not short.
- **The reviewers never see the conversation.** That blindness is
  the source of their value.
- **A reviewer runs on the principal's word.** A run costs tokens
  (some checks cost a great deal), and what is spent is his to
  decide.
- **A reviewer may be pointed at any file.** What Claude composes
  and the principal judges (a work product above all) deserves the
  isolated look as much as the chain. The cost is a report that
  sometimes says there was nothing to find.
- **A research is planned first.** The quality of a research is made
  by its decomposition into questions, not by the searching. The
  plan is where the principal sees the questions before they cost
  anything.
- **A recipe fixes the structure, never the wording.** Each
  rendering derives the words again from the current inputs. A text
  fixed in the template would turn the recipe into the render and
  make the inputs meaningless.
- **A work product is a kind of its own.** The principal works with
  its file freely, and a render is never edited by hand. Stretching
  the render to cover such an output would cost that rule.
- **Save and release are two commands.** Renders at every save would
  cost minutes and tokens beyond reason. With the renders at the
  release only, the README is current at every release and visibly
  stale in between, never silently.
- **A source is registered without being taken in.** What a source
  is for is individual, and what someone said in a meeting is never
  silently promoted to the principal's own position.
- **Feedback from the recipients has no channel of its own.** The
  reason is not recorded.

## See also

- [The document chain](the-document-chain.md): the chain as a star.
- [The user stories](the-user-stories.md): the stories, the layer
  between the BRD and the solution design.
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

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
