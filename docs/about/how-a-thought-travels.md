---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: eed3aa4aabb69fa2
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

The forge is a workshop in which one idea travels a chain of
versioned documents, from a rough brief to a saved release, under the
eyes of reviewers that never see the conversation. This page follows
one invented thought the whole way, station by station, in the order
the thought meets them. It is for whoever uses the forge, extends it
or judges it, and it explains what happens and why; how each step is
done is said on the pages of the steps.

## What it is

The journey of a thought is the [document chain](the-document-chain.md)
with everything that works on it. The chain starts at a brief and its
trunk is the intent. Below the intent a project takes the layers it
needs, an assignment, a BRD, a solution design, and none of them is a
condition of another. Many projects end at the intent. A layer a
project does not have is not missing.

Around the chain stand the things that are not the chain. Sources and
research may arrive at any stage, before the brief as much as after
it. Reviewers press on the documents and on the thinking at every
layer. Outputs for every audience are generated from the chain and
never written into it. Everything is saved to git and, now and then,
released.

Two words recur on this page. The principal is whoever's thinking is
being forged: he supplies the ideas and the decisions, and he is the
final authority on all content. Claude is his cognitive extension: it
proposes, structures and keeps the process in order, and never
decides.

## How it works

### It arrives as a brief

A brief is the principal's text of one whole of thinking: what he
wants and why, with what he chose to take from the finding around it.
It is free-form. Any structure the principal finds useful is allowed,
prose, headings, tables or use cases, and none is required. It has no
IDs and only a minimal header. It holds thoughts to be processed, not
decisions: they may be changed, reworked or dropped later, and only
the intent turns them into positions. A brief is rough on purpose. Its
usual shape is light: the topics of the whole, a few sentences of
what the principal wants of each, the research that verifies or
limits it cited beside it, and what is still open. It is composed in a
round or two and then mined.

A brief may come to the forge in three ways, and the forge treats them
alike:

- it arrives finished from outside and is stored as it came;
- it is begun outside and finished with Claude in the forge;
- it is born in the forge from the first word.

What was found around the thought and did not enter the brief lives
in the project's research and sources where it is a finding or a
source, and otherwise nowhere. A brief is versioned like every
artefact: a draft until the principal approves it, and changed after
that as any artefact is. It is the provenance of its whole: a position
mined from it cites it.

### It is chiselled into the intent

The intent is the working document: the consolidated current state of
the principal's intent. It is not a log. It is rewritten for coherence
every round, and the changes are recorded in its history, a companion
file beside it. A position says what the principal holds and why it
holds, in as many words as it takes to be understood without loss of
meaning, and names what it comes from, a brief or a source. The way
to a position, why it changed, what was said, trials and
measurements, goes into the history in the same step, never into the
position. What is open lives in threads beside the intent, one file
per thread: the intent says what holds, the threads what is being
worked.

The intent is found by elicitation. Every artefact of the chain has a
definition, a file that says what the artefact is, how it is found,
by questions, research and sources, and what rules it owns; a
template beside it says what comes out. A round of work runs by the
working methods of the forge: Claude reads the definition, the
conversation draws out what the principal has not yet articulated,
and one write at the round's end changes the artefact, appends the
records to its history and brings the
[ledger](../reference/glossary.md) current (the ledger is the single
source of truth for the project's state, made from its files at read
time). Drafting early is a legitimate tool of that elicitation.

### Below the intent, the layers the project needs

Substance changes go into the intent first and propagate from there
down whatever chain the project has. The layers below are these.

The assignment is the distilled handover document for the recipients:
complete, precise, structured, self-contained and versioned. It
carries the whole in-scope substance of the intent. Nothing is left
out for the sake of brevity, and a silent omission is a defect.
Leaving a matter out is legitimate only as an explicit delegation,
an item that says what the recipients are to produce or what is still
to be confirmed. There is no size target in either direction: length
is whatever fidelity requires.

The BRD stands below the assignment and above the solution design and
breaks its parent into the business rules, the agreed behaviour and
the qualities that the stakeholders review and the delivery estimates
from.

The solution design says how the things wanted are realised. It is
derived from the lowest layer the project has above it, the intent
alone, the assignment or the BRD, and whatever stands above it is its
input. It is worth writing where the way is not obvious, where a
choice has a price, or where two hands would solve the same matter
differently if it were not written down. Whether it is written, the
principal says.

Feedback from the recipients has no channel of its own. The principal
processes it and feeds the conclusions back into the intent.

### At every layer, blind reviewers

Three kinds of review press on a project, each with one job:

- the critic reads the documents for their quality, never their
  substance, through a chosen lens;
- the challenger reads the thinking for its substance, never the
  documents' quality, through a chosen persona;
- the check verifies the mechanical conformance of the files with the
  conventions, never substance or quality.

Each runs as an [isolated reviewer](isolated-reviewers.md), that is,
as a [subagent](../reference/glossary.md) (a run of Claude of its own,
with its own context) that reads the files it is given and never sees
the working conversation. Each is invoked by hand. Each returns an
immutable, dated report, which is filed with IDs and then settled by
[walkthrough](../reference/glossary.md), the forge's way of working a
list one item per message, each item closed with the principal's
verdict. What is accepted is written in one round. The critic and the
challenger take an optional target: one artefact of the chain, or any
file of the project, a work product among them; without a target they
read the whole chain. No reviewer runs on Claude's own judgement.

### Sources and research arrive at any stage

External inputs, transcripts, offers, documents and standards, live in
the project's sources. A source is immutable once registered. It may
arrive before the brief as material for writing it, during intent
work, or after. Registering a source does not mean taking it in: what
a source is for, a standard to verify against, inspiration, a meeting
record or material to absorb, is the principal's word, recorded in
the sources' index, and he alone directs how and when a source is
used. When source content does enter the intent, it is his explicit
act, cited with provenance to the file. What someone said in a
meeting is never silently promoted to the principal's own position.

A [research](the-research.md) is planned before it is searched. Claude
shows the plan and the principal confirms it in a walkthrough: the
purpose, the perspectives from which the topic is looked at, the
assumptions, what is left out, and the cards, each one question
answered by one kind of evidence from one kind of source. A research
has two depths. A quick research answers one card, filed as one note.
A deep research runs one isolated agent per card and files a bundle
with the plan and the synthesis at its head and one note per card.
Claude proposes the depth: quick where one question is to be answered
and cited, deep where a position, a layer of the chain or a design
will rest on the answer. The synthesis is Claude's, from the notes
alone. A note, a bundle and its plan are immutable from their filing.

### Outputs for every audience

A [render](renders-and-recipes.md) is an audience-specific output
generated from the chain: a pitch, an architecture picture, an
executive summary, the repository README. A render is never edited by
hand. What is iterated is its recipe, one versioned file that holds
the inputs, the audience, the instructions and the output template;
the render is regenerated from it mechanically, in an isolated
subagent, and opens with its provenance, the recipe and every input
with their versions. A render assigns nothing and is not part of the
chain: the artefacts remain the sole source of truth. The boundary
between the two is authorship, not audience: an article the principal
writes is a layer of the chain, its translation is a render. Where a
recipe names a format, a plain file is made from the render by a
script; a designed file is made from it through a model, only on the
principal's command. Every project has a README as a render of its
own recipe, and a thought project has release notes the same way.

A [work product](the-work-product.md) is an output that is neither an
artefact nor a render: any result of Claude's work the principal asked
for, a model, an analysis, a worked task, in whatever form the work
needs. It takes its inputs from the chain and the resources, adds work
of its own, is iterated and is handed over as a result of the project.
It is two files: the file that holds the content, and beside it a
specification that holds the way and the why, versioned with its
history. The file is made from the specification again whenever it
changes. What the work shows flows back into the intent.

The documentation is generated the same way, never composed by hand:
pages of one topic each, with an index, for the user, the extender
and the evaluator, made from a map that lies beside the project's
ledger and is never shown to the reader. One command makes it, in one
run that asks nothing and regenerates only what changed.

### Saved to git and released

Saving and releasing are two commands of two speeds. A save runs a
light check and then commits and pushes on whatever branch is checked
out, with no render, in seconds. A release runs from the main branch
only. It runs its checks and settles them, regenerates the
documentation, the README and the release notes, writes the state of
the project as a render, and then saves with the release message and,
at an approved major, a tag. The release number is the intent's
version. Only the tag of an approved major has a fixed name. The
documentation comes before the README. Because the README reads the
documentation's index, it has to be made after it.

## The main courses of events

- A round of work: Claude reads the definition of the target
  artefact, the conversation runs by the working methods, and one
  write at the round's end changes the artefact, appends the records
  to its history and brings the ledger current.
- A review: a critic, a challenger or a check launches one isolated
  agent, its report is filed with IDs, and the findings are settled by
  walkthrough and written in one round.
- A render: the Markdown is generated in an isolated subagent from a
  recipe and its inputs with its provenance written first, and the
  designed file is made from the render as it lies on disk.
- Persistence: a save runs the light check and commits and pushes; a
  release runs its checks, regenerates the README and the release
  notes and saves with the release message and tag.

## Why

A brief is rough on purpose. A required structure would force
premature tidiness, and a brief polished until the intent has nothing
left to do has gone too far: the chiselling is the intent's work.

Because chat context dies, anything of value must live in a file, and
the intent is that file. It is the document to read when returning to
a project after weeks, instead of excavating old conversations. It is
rewritten for coherence and always reads as the current state; the
history keeps the way there.

The assignment leaves nothing out in silence. A silent omission is a
defect, and the goal is to have it right, not short.

The layers below the intent are optional. Many projects end where
what is wanted needs no solution written down. Where a solution design
is written, its purpose is that the thing can be built from the
artefacts alone, without a look at the finished product: the product
is never a source of its own design.

The reviewers are blind to the conversation. That blindness is the
source of their value. They run on the principal's word alone.
Because a run costs tokens, some a great deal, what is spent is his
to decide.

A research is planned first. Its quality is made by the decomposition
into questions, not by the searching, and the plan is where the
principal sees the questions before they cost anything.

A render is generated and never edited. The artefacts are to remain
the sole source of truth. Its recipe fixes the structure and never
the wording. Because fixing the text in the template would turn the
recipe into the render and make the inputs meaningless, each
rendering re-derives the words from the current inputs. The work
product is a kind of its own. Stretching the render to cover it would
have cost the rule that a render is never edited by hand.

Saving and releasing are two commands. The renders cost minutes and
tokens beyond reason at every save. With the renders at the release
only, the README on the main branch is current at every release and
stale in between visibly, never silently.

Content of a source enters the intent only by the principal's
explicit act, cited with provenance. So that what someone said in a
meeting is never silently promoted to his own position, the forge
never does it for him. Why a source is immutable once registered is
not recorded. Why the documentation is generated rather than composed
by hand is not recorded.

## A worked example

A team lead wants to replace the weekly status meeting of her team
with a written update. She is the principal of a new project.

She writes a brief of a page: the meeting takes an hour of eight
people, the written update should take ten minutes, the exceptions
she can think of, and a question she cannot yet answer, whether the
update is read at all. A transcript of the last meeting is dropped
into the project's sources and registered; its role, a record of what
the team raised, is asked for and noted. The brief is approved and
then mined.

Over three rounds the brief becomes an intent. Each round is an
elicitation: Claude asks what "read at all" means, she answers, and
at the round's end one write turns the answers into positions, each
saying what she holds and why and citing the brief; the question of
how reading is to be known stays a thread beside the intent. One
position wants to rest on what the world knows about written updates
in teams. Claude proposes a deep research, shows the plan with its
cards, she confirms it in a walkthrough, and the notes come back as
an immutable bundle; the position cites the note it rests on, and the
intent is rewritten for coherence once more.

Before handing anything over she runs a challenger against the
intent. The report arrives blind, is filed, and its challenges are
walked through one by one; one is accepted and mended in the intent,
two are rejected with their reasons recorded. A critic then reads the
intent for its quality.

Because the team is to carry the change out, the project needs an
assignment. The assignment carries the whole in-scope substance of
the intent and delegates one matter explicitly: the team is to
propose the template of the update and return it. The project ends
there. The way is obvious and no choice has a price, so no BRD and no
solution design is written, and nothing says they are missing.

A recipe for a one-page summary for the team is composed, and the
render is generated from it, opening with the version of the
assignment it was made from. The team's feedback comes back in
conversation; the lead processes it and feeds two conclusions into
the intent, and the assignment follows. A work product, a small model
of the hours saved, is worked beside the chain, its specification
saying what it starts from and how it is made. The project is saved
along the way and, when the assignment is approved, released from the
main branch: the checks run, the documentation, the README and the
release notes are regenerated, and the release is committed.

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

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
