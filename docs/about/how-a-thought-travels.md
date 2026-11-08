---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: 79eff467e9c32185
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

A thought travels through the forge as a chain of versioned Markdown
documents, from a rough brief to a saved release. This page follows
one invented thought along that way, station by station, for anyone
who uses the forge, extends it or evaluates it: what happens to the
idea at each place, what is made there, and why the way is shaped as
it is. It explains; it does not teach the commands. Where a command
is named, it is named in passing, and its own page says how it is
used.

## What it is

The forge is not a program. It is a set of instructions that Claude
Code, the agent for the command line, reads; deterministic work is
kept at its edge in scripts. The person whose thinking is forged is
the principal. Claude proposes; the principal composes and decides.

Everything the thought becomes lives in the files of one project
directory. Those files are:

- the artefacts of the chain, the documents the principal composes
  with Claude;
- their history logs, one append-only companion beside each
  versioned document;
- the ledger, the single source of truth for the project's state,
  made at read time from the documents and never kept in git;
- the reports of the reviewers;
- the resources, that is the sources and the research notes.

Nothing of value lives in the conversation or in Claude's memory.

The chain starts at a brief, and its trunk is the intent. Below the
intent a project takes the layers it needs. No layer is a condition
of another, and many projects end at the intent. How the layers hang
together is told on [The document chain](the-document-chain.md).
Beside the chain stand the things that are not the chain: the
reviews, the research, the sources, the renders, the work products
and the documentation. All of it is saved to git.

## How it works

Take one invented thought, taken from no project. A team lead wants
to replace a weekly status meeting with a short written report that
everyone reads before the week begins. What follows is the way that
thought takes.

### It arrives as a brief

The thought is written down as a brief: the principal's text of one
whole of thinking, what he wants and why, with what he chose to take
from the finding around it. The brief is free-form. Any structure the
principal finds useful is allowed, and none is required. It holds
thoughts to be processed, not decisions: a thought may be changed,
reworked or dropped later, and only the intent turns a thought into a
position.

A brief is rough on purpose. Its usual shape is light: the topics of
the whole, each with a few sentences of what the principal wants of
it, the research that verifies or limits it cited beside it, and what
is still open. It is composed in a round or two and then mined. Our
team lead's brief says, in a few paragraphs, why the meeting costs
too much, what the report should carry, who should read it, and that
he does not yet know how often it should go out.

Three origins are equally legitimate, and the forge does not
distinguish them:

- the brief arrives finished from outside and is stored as it came;
- it is begun outside and finished with Claude in the forge;
- it is born in the forge from the first word.

A brief is versioned like every artefact: a draft until the principal
approves it, and changed after that as any artefact is. It is the
provenance of its whole: a position mined from it cites it.

### It is chiselled into the intent

The intent is the working document: the consolidated current state of
the principal's thinking. Claude mines the brief into it by
elicitation, that is by questions, research and sources, as the
intent's definition says it is found. The intent is written once at
the round's end, and that one write changes the document, appends the
records to its history and brings the ledger current. Our team lead
is asked who owns the report, what happens when a section is empty,
and whether the meeting goes away or shrinks; his answers become
positions.

A position says what the principal holds and why it holds, in as
many words as it takes to be understood without loss of meaning, and
names what it comes from, a brief or a source. The intent is not an
append-only log. It is rewritten for coherence every round, and its
changes are recorded in its history. The way to a position, that is
why it was changed, what was said on the way, trials and
measurements, goes into the history in the same step that writes the
position, never into the position itself.

What is still open lives in threads, one file per thread beside the
intent. The intent says what holds; the threads say what is being
worked. A thread carries the working debate for as long as it is
unsettled, and it is where an unfinished conversation is saved. Once
settled, a thread stays as its file, immutable, and what holds goes
into the intent.

### Below the intent, the layers the project needs

Every artefact of the chain has a definition, its state file, worked
through `/forge` and paired with a template. The definition says what
the artefact is and how it is found; the template says what comes
out. Below the intent the project takes the layers it needs:

- an assignment, the distilled handover document for the recipients:
  complete, precise, structured, self-contained and versioned;
- a BRD, which breaks its parent into the rules, the agreed sequences
  of behaviour and the qualities that the stakeholders of each area
  review on their own;
- the user stories, the parent broken into behaviour seen from the
  outside with the conditions under which it is accepted, told on
  [The user stories](the-user-stories.md);
- a solution design, how the things wanted are realised, derived from
  the lowest layer the project has above it.

An assignment carries the whole in-scope substance of the intent.
Nothing is left out for the sake of brevity. Leaving a matter out is
legitimate only as an explicit delegation to the recipients, and a
silent omission is a defect. There is no size target in either
direction: length is whatever fidelity requires.

A solution design is worth writing where the way is not obvious,
where a choice has a price, or where two hands would solve the same
matter differently if it were not written down. Whether it is
written, the principal says. From the artefacts of the chain the
thing must be buildable without a look at the finished product.

Many thoughts end at the intent, where what is wanted needs no
solution written down. Our team lead's thought may well be one of
them: once the intent says what the report carries, who writes it
and when, the team can start. A layer a project does not have is not
missing: the state map and the checks say nothing of it, and the
ledger declares no end of the chain.

Iteration is intent-first, with drafting early as a legitimate tool.
The number in a file name orders the files and prescribes no
sequence.

### Reviewers press on it at every layer

At any layer the principal may call a reviewer on the documents or on
the thinking. There are three kinds, of one shape:

- the critic, for document quality, never substance: it reads
  through a lens and produces findings;
- the challenger, for the substance of the thinking, never document
  quality: it reads through a persona and produces challenges;
- the check, for mechanical conformance with the conventions, never
  substance or quality: each check owns one concern.

Each runs as an isolated subagent, that is a separate run of Claude
that sees the files it is given and never the working conversation,
on the session model, that is the one model the whole forge runs on.
That blindness is the source of its value; why it is so is told on
[The isolated reviewers](isolated-reviewers.md). Every reviewer is
invoked by hand and runs on the principal's word alone. Each produces
an immutable, dated report. The findings and the challenges are
settled by walkthrough, that is one item per message, each closed by
the principal's verdict, and written in one round. Reviewers are
advisory: they report and propose, and the principal decides what is
fixed. A critic or a challenger may take one artefact, any file of
the project, or the whole chain.

Our team lead calls a challenger on his intent. It asks whether the
meeting is the real problem or only where the problem shows, and
what would happen the first week a section stays empty. He settles
both by walkthrough; one changes a position.

### Research where a position will rest on what the world knows

Where a position, a layer of the chain or a design will rest on what
is already known outside the project, the principal has a research
made. A research is planned before anything is searched. Claude shows
the plan, and the principal confirms it in a walkthrough. The plan
holds:

- the purpose;
- the perspectives from which the topic is looked at, each with the
  cards that serve it;
- the assumptions, with a premortem answered once and marked as
  Claude's;
- what is left out;
- the cards, each one question answered by one kind of evidence from
  one kind of source;
- the agents and the rule that fixed their count.

There are two depths. A quick research is one card on the session
model alone, filed as one note. A deep research is one isolated agent
per card, filed as a bundle with the plan and the synthesis at its
head and one note per card. Without a word from the principal Claude
proposes the depth with its reason, quick where one question is to be
answered and cited, deep where a position or a layer will rest on the
answer, and the principal decides. The synthesis is Claude's, from
the notes alone, with its own view last and apart. A note, a bundle
and its plan are immutable from their filing. How a research is
planned is told on [How a research is made](the-research.md).

Our team lead asks what is known about written status reports in
teams of his size. One card, one note, cited beside the position it
limits.

### Sources arrive at any stage

External inputs, such as transcripts, offers, documents and
standards, live in the project's sources. They may arrive at any
stage of a project's life: before the brief as material for writing
it, during intent work, or after. A source is immutable once
registered. Registration does not imply intake: what a source is for
is individual, recorded as its role in the resource index, and the
principal alone directs how and when a source is used. When source
content does enter the intent, it is the principal's explicit act,
cited with provenance to the file. What someone said in a meeting is
never silently promoted to the principal's own position.

Our team lead drops the transcript of the last meeting into the
sources. It is registered and catalogued. Nothing of it enters the
intent until he says which sentence of it supports which position.

### Outputs for every audience

A render is an audience-specific output generated from the chain: a
pitch, a picture, a summary, the project's README. A render is never
edited by hand. What is iterated is its recipe: the inputs, the
audience, the instructions and the output template in one versioned
file, composed with the principal. The render is regenerated from the
recipe mechanically and opens with its provenance, citing the recipe
and every input with their versions. A render assigns nothing and is
not part of the chain: the artefacts remain the sole source of truth.
The boundary between the two is authorship: a chain artefact is
composed by the principal, a render is generated from artefacts. An
output is made in two steps. The render makes the Markdown and, where
the recipe names a format, the plain file; the publish step makes the
designed file through a model, only on the principal's command. How
this works is told on [Renders and recipes](renders-and-recipes.md).

Where the project needs work of its own, a work product is made
beside the chain: any result of Claude's work the principal asked
for, such as a model, an analysis or a worked task, in whatever form
the work needs. It is two files: the file that holds the content and
beside it a specification that holds the way and the why. The file
is remade from the specification whenever that changes, and the
principal works with the file freely. What the work shows flows back
into the intent. What a work product is and is not is told on [The
work product](the-work-product.md).

The documentation is generated the same way, never composed by hand:
pages of one topic each with an index, for the user, the extender
and the evaluator, made from a map that lies beside the project's
ledger and is never shown to the reader. One run makes it, asks
nothing and regenerates only what changed.

Our team lead has a recipe composed for a one-page summary for the
team, regenerates the summary whenever the intent changes, and has
the first report drafted as a work product beside the chain.

### Saved to git and released

Everything the thought became is saved to git. A save runs a light
check and then commits and pushes on whatever branch is checked out,
in seconds. A release runs from the main branch only. It runs its
checks and settles their findings with the principal, regenerates the
documentation, the README and the release notes, writes the state
render and then saves with the release message and a tag. The release
carries the version of the intent.

Our team lead saves after every round. When the intent is approved,
he releases, and the README of his project tells the team where the
thinking stands.

### The main courses of events

The whole journey is made of four courses of events, each one
sentence:

- A round of work: `/forge` reads the definition of the target
  artefact, the conversation runs by the working methods, and one
  write at the round's end changes the artefact, appends the records
  to its history and brings the ledger current.
- A review: `/critique`, `/challenge` or `/check` launches one
  isolated agent, its report is filed with IDs, and the findings are
  settled by walkthrough and written in one round.
- A render: `/render` generates the Markdown in an isolated subagent
  from a recipe and its inputs and writes the provenance, and
  `/publish` makes the designed file from the render as it lies on
  disk.
- Persistence: `/save` runs the light check and commits and pushes,
  and `/release` runs its checks, settles them, regenerates the README
  and the release notes and then saves with the release message and
  tag.

## Why

The brief is rough on purpose. A required structure would force
premature tidiness. The chiselling is the intent's work, and a brief
polished until the intent has nothing left to do has gone too far.

The intent exists because chat context dies and anything of value
must live in a file. It is the document to read when returning to a
project after weeks, instead of excavating old conversations. It is
rewritten for coherence, and the way to each position goes into the
history, so that the intent stays readable as the current state.

The assignment leaves nothing out in silence, because a silent
omission is a defect for the recipients, and a delegation they can
see is not. The size targets were dropped because the goal is to have
it right, not short.

The layers below the intent are taken as needed, because many
thoughts need no solution written down once what is wanted is clear,
and a layer a project does not have is then not missing.

The reviewers never see the conversation, because that blindness is
the source of their value. They run on the principal's word alone,
because a run costs tokens, some checks a great deal, and what is
spent is his to decide; there is no other reason. They are advisory:
they report and propose, and the principal decides what is fixed.

A research is planned before it is searched, because the quality of a
research is made by the decomposition into questions, not by the
searching. The plan is where the principal sees the questions before
they cost anything.

A source is registered and not taken in, because what a source is
for is individual: a standard to verify against, an inspiration, a
meeting record, material to absorb. What someone said in a meeting is
never silently promoted to the principal's own position.

A render is generated and never edited by hand, so that the artefacts
remain the sole source of truth. The boundary to the chain is
authorship, not audience, so that an article the principal writes is
a layer of the chain and its translation is a render.

A work product is a kind of its own. Stretching the render to cover
it was weighed and dropped, because it would have cost the rule that
a render is never edited by hand.

Why the documentation is generated rather than composed by hand is
not recorded in the inputs of this page.

Save and release are two commands, because the renders cost minutes
and tokens beyond reason at every save. With the renders at the
release only, the README on the main branch is current at every
release and stale in between visibly, never silently.

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

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
