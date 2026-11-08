---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: d84ee5841bb30408
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
  - projects/forge/10-intent.md#POS.1860
  - projects/forge/10-intent.md#POS.0710
  - projects/forge/10-intent.md#POS.0180
  - projects/forge/10-intent.md#POS.1100
  - projects/forge/10-intent.md#POS.1520
---

# How a thought travels through the forge

A thought in the forge is one idea that travels a chain of versioned
documents, from a rough brief to a saved release, under review by
agents that never see the conversation in which it was worked. This
page follows one invented thought along that road, station by
station, for anyone who wants to see the whole before reading the
pages on its parts: the user who brings a thought, the extender who
adds a station, the evaluator who asks whether the road is sound.

## What it is

The road is the [document chain](the-document-chain.md): a brief at
its start, the intent as its trunk, and below the intent the layers
a project needs. Every artefact of the chain has a definition, the
file that says what the artefact is, how it is found and what rules
it owns, and a template that says what comes out. The one whose
thinking is forged is the principal: he supplies the ideas, the
answers and the decisions, and he is the final authority on all
content. Claude is his cognitive extension: it proposes, elicits,
structures and writes, and never decides.

The chain ends where the project needs it to. Many projects end at
the intent. Nothing below the intent is a condition of anything
else. A layer a project does not have is not missing: Claude and
the checks say nothing of it.

Around the chain stand three further groups of files. Records hold
what changed and why: the history companion of every versioned
document, the decisions, the reports of the reviewers. State is
made at read time: the ledger, the one file that says where
everything stands, built from the documents and never kept in git.
Resources are what arrives from outside: sources, immutable from
their registration, and research, immutable from its filing.

## How it works

The thought meets the stations in this order.

### It arrives as a brief

A brief is the principal's text of one whole of thinking: what he
wants and why, with what he chose to take from the finding around
it. It is free-form, with no required content and no IDs. It is
rough on purpose. It holds thoughts to be processed, not decisions:
they may be changed, reworked or dropped when mined. A brief may
arrive finished from outside, be begun outside and finished with
Claude, or be born in the forge from the first word. The forge
treats the three origins alike. A brief is versioned like every
artefact: a draft until the principal approves it, and changed after
that as any artefact is.

### It is chiselled into the intent

The intent is the working document: the consolidated current state
of what the principal holds. It is made of positions. A position
says what the principal holds and why, and names what it comes from,
the brief or a source. The intent is found by elicitation: Claude
asks, one question per message, and draws out what the principal has
not yet articulated. Every proposition that needs his decision is
worked as a walkthrough, that is, one item per message, each closed
with a verdict line on which he answers with one letter. What is
agreed is carried in the conversation and written once at the
round's end, on his word. Each round rewrites the intent for
coherence; it is not an append-only log. The way to a change, what
was said, what was tried and which research turned it, goes into the
history companion in the same step, never into the position. An open
matter of the intent lives in a thread, one file per thread, until
it is settled.

Not every thought of the brief survives the sifting. What stays out
lives in the resources where it was a finding or a source, and
otherwise nowhere.

### Sources and research arrive at any stage

A source is an external input as it arrived: a transcript, an offer,
a document, a standard. It may arrive before the brief, as material
for writing it, during the work on the intent, or after. Once
registered it is immutable. Registration does not imply intake: the
principal alone directs how and when each source is used, and when
source content enters the intent it is his explicit act, cited with
provenance to the file. What someone said in a meeting is never
silently promoted to the principal's own position.

A [research](the-research.md) is planned before it is searched.
Claude shows the plan, the purpose, the perspectives, the questions
to be answered and what is left out, and the principal confirms it
in a walkthrough before anything costs a search. It has two depths.
The quick one answers one question and files one note. The deep one
runs one isolated agent per question and files a bundle with the
plan and the synthesis at its head. Claude proposes the depth: quick
where one question is to be answered and cited, deep where a
position, a layer of the chain or a design will rest on the answer.
A note is immutable from its filing.

### Below the intent, the layers the project needs

Where a thought is to be handed to others, the intent is distilled
into an assignment: the handover document for the recipients,
complete, precise, structured and self-contained. It carries the
whole in-scope substance of the intent. A silent omission is a
defect; leaving a matter out is legitimate only as an explicit
delegation.

Below the assignment a project may take a BRD, the business
requirements that break the parent into rules, behaviour and
qualities the stakeholders review, so that the delivery can estimate
and the solution design can start. Below that it may take the
[user stories](the-user-stories.md), the parent broken into behaviour
seen from the outside, with the conditions under which it is
accepted.

The solution design says how the things wanted are realised. It is
derived from the lowest layer the project has above it: the intent
alone, the assignment, the BRD or the stories. It is worth writing
where the way is not obvious, where a choice has a price, or where
two hands would solve the same matter differently if it were not
written down. Whether it is written, the principal says. From the
artefacts of the chain the thing must be buildable without a look at
the finished product.

Substance changes go intent-first and propagate down the whole chain
the project has. A change may come from below, when solving shows
that what is wanted must change; then the intent changes first and
the layers follow. Only wording is fixed in a lower layer directly.

### At every layer, blind reviewers

Three kinds of [isolated reviewer](isolated-reviewers.md) press on
the documents, each run in a subagent, that is, a separate run of
Claude that sees the files it is given and never the working
conversation. The critic reads for document quality, through a lens
chosen for what it should look at: one lens reads each artefact on
its own, another distils the essence of every adjacent pair of the
chain and compares them. The challenger reads for the substance of
the thinking, through a persona that hunts the blind spots someone
of that trade would see. The check reads for mechanical conformance
with the conventions. Each produces an immutable, dated report. The
findings are settled by walkthrough and written in one round.

A reviewer runs on the principal's word alone, never on Claude's own
judgement. A reviewer may be pointed at the whole chain, at one
artefact, or at any file of the project.

### Outputs for every audience

A [render](renders-and-recipes.md) is an output generated from the
chain for one audience: a pitch, an architecture picture, an
executive summary, the repository README. What is iterated is never
the render but its recipe: inputs, audience, instructions and the
output template in one versioned file, composed with the principal.
The render is regenerated mechanically from the recipe, in an
isolated subagent, and opens with its provenance, the recipe and
every input with their versions. A render assigns nothing and is not
part of the chain. The boundary between the two is authorship: a
chain artefact is composed by the principal, a render is generated
from artefacts. An article the principal writes is a layer of the
chain; its translation is a render.

An output is made in two steps. The first generates the Markdown
and, where the recipe names a format, the plain file through a
script: deterministic, cheap, repeated freely. The second makes the
designed file through a model: expensive, only on the principal's
command.

A [work product](the-work-product.md) stands beside the renders
where the project needs work of its own: any result of Claude's work
the principal asked for, a model, an analysis, a worked task. It
takes its inputs from the chain and the resources, adds work of its
own, is iterated, is handed over as a result of the project, and
what it shows flows back into the intent. It is two files: the file
that holds the content and the specification beside it, which holds
the way and the why.

The documentation is generated the same way: pages of one topic each
with an index, for the user, the extender and the evaluator, made in
one run that asks nothing and regenerates only what changed.

### Saved to git and released

Every project is a git repository of its own, and the scripts of the
forge are the door to every write of it. Two doors, two speeds. A
save runs one light check and then commits and pushes on whatever
branch is checked out, in seconds. A release, from the main branch
only, runs its checks, settles them, regenerates the README and the
release notes, writes the state render and then saves with the
release message. At an approved major it adds the tag of the
version. The release number is the intent's version.

### The main courses of events

- A round of work: Claude reads the definition of the target
  artefact, the conversation runs by the working methods, and one
  write at the round's end changes the artefact, appends the records
  to its history and brings the ledger current.
- A review: one isolated agent is launched, its report is filed with
  IDs, and the findings are settled by walkthrough and written in
  one round.
- A render: the Markdown is generated in an isolated subagent from a
  recipe and its inputs, with its provenance; the designed file is
  made from the render as it lies on disk.
- Persistence: a save checks, commits and pushes; a release checks,
  regenerates the README and the release notes, writes the state
  render and saves with the release message and tag.

## Why

The brief is rough on purpose. A brief polished until the intent has
nothing left to do has gone too far, because the chiselling and the
sifting belong to the intent. No structure is required of it,
because a required one would force premature tidiness.

The intent exists because chat context dies and anything of value
must live in a file. It is the document to read when returning to a
project after weeks, instead of excavating old conversations. State
lives in the files of the project, never in the conversation and
never in the assistant's memory.

The chain ends where the project needs it to, because many projects
end at the intent, where what is wanted needs no solution written
down. Below the intent no layer is a condition of another, so that a
project takes only the layers it needs.

The reviewers never see the working conversation, because that
blindness is the source of their value. They run on the principal's
word alone, because a run costs tokens, some a great deal, and what
is spent is his to decide.

A research is planned before it is searched, because the quality of
a research is made by its decomposition into questions, not by the
searching, and the plan is where the principal sees the questions
before they cost anything.

A render is never edited by hand, so that the artefacts remain the
sole source of truth. Each rendering re-derives the words from the
current inputs, because fixing the text in the recipe would turn the
recipe into the render and make the inputs meaningless.

The work product is a kind of its own, because stretching the render
to cover it would have cost the rule that a render is never edited
by hand, and an artefact of the chain is thinking in items with IDs,
which a file of any form cannot carry.

Save and release are two doors, because the renders cost minutes and
tokens beyond reason at every save. With the renders at the release
only, the README on the main branch is current at every release and
stale in between visibly, never silently.

## A worked example

The principal has a thought: the team's weekly planning should move
from a meeting to a written round. He writes it down as it is, in a
page of prose with a table of the people it touches, and that page
is the brief of a new project with the placeholder slug `<slug>`.
Before it he has already dropped the minutes of the last three
planning meetings into the project's sources, where they are
registered and catalogued.

Claude reads the brief and begins the intent. It asks one question
at a time: what the written round is for, who writes, who reads,
what happens when nobody answers. Where the principal's answer rests
on what the minutes say, the position cites the file. Where the
principal wants to know how other teams run asynchronous planning,
Claude proposes a research, shows the plan, and the principal
confirms it before anything is searched. At the end of the round
Claude reflects back what it understood, the principal says write,
and the intent is written once, with its history records.

The principal points a challenger at the intent. The challenger, in
its own subagent, finds that the thought assumes everyone reads
their mail on the day of the round, and that nothing says what the
round decides when half the team is silent. The challenges come back
as a walkthrough; the principal accepts the first and parks the
second as a thread. The intent is rewritten for coherence in the
next round.

The thought is to be handed to the team. Claude distils the intent
into an assignment, complete and self-contained, and the principal
approves it, which makes it an integer version. The project ends
there: no BRD, no stories, no solution design, and none is missing.

For the team's wiki the principal composes a recipe: inputs the
assignment, audience the team, a template of what the page carries.
The render is generated from it, with its provenance at the top, and
regenerated whenever the assignment changes. Beside it Claude makes a
work product, a worked schedule of the first four rounds with its
specification, which the principal edits freely.

The principal saves. The check runs, the commit is made, the push
goes out. When the intent is approved he releases: the checks run,
the README and the release notes are regenerated, the state render
is written, and the release is saved with its message.

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

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
