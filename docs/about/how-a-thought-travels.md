---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: fa7b82a2aa0f776c
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

A thought travels through Forge of Thought as a chain of versioned
Markdown documents, from a rough brief to a saved release. This page
follows one invented thought along that way, station by station, for
anyone who uses the forge, extends it or judges it: what each station
is for, what happens there, and why the forge is built so.

## What it is

The forge is not a program. It is a set of instructions that Claude
Code reads, with the deterministic work kept at its edge in scripts.
Claude Code is the harness, that is, the program that runs Claude and
its tools. A project is a directory of files: the artefacts of the
[document chain](the-document-chain.md), their history logs, the
ledger (the one file that holds the state of the project), the
records of the reviewers and the resources. State lives in those
files, never in the conversation and never in Claude's memory.

Two work on a thought. The principal is the person whose thinking is
being forged; he supplies the ideas, the answers and the decisions.
Claude proposes; the principal composes. Every artefact of the chain
is composed that way, and nothing enters the chain without the
principal's word.

The way a thought takes has a fixed order of stations. It arrives as
a brief. It is chiselled into the intent, the trunk of the chain.
Below the intent the project takes the layers it needs, such as an
assignment or a solution design, and many projects end at the intent.
At every layer, reviewers that never see the conversation press on
the documents and on the thinking. Outputs for every audience are
generated from the chain, work products are made beside them where
the project needs work of its own, and the documentation is generated
the same way. Everything is saved to git and, now and then, released.
Sources and research arrive at any stage of this way.

## How it works

### It arrives as a brief

A brief is the principal's text of one whole of thinking: what he
wants and why, with what he chose to take from the finding around
it. It is free-form. Any structure the principal finds useful is
allowed, no content is required, and it carries no item IDs, only a
minimal header. It holds thoughts to be processed, not decisions:
they may be changed, reworked or dropped when the brief is mined, and
only the intent turns them into positions.

A brief is rough on purpose. Its usual shape is light: the topics of
the whole, each with a few sentences of what the principal wants of
it, the research that verifies or limits it cited beside it, and what
is still open. It is composed in a round or two and then mined. It is
where thoughts are thrown in before they are sifted; not all of them
survive, and the sifting belongs to the intent. What stays out of
the brief lives in `research/` or `sources/` where it is a finding or
a source, and otherwise nowhere.

A brief may come from three places, and the forge does not
distinguish them:

- it arrives finished from outside and is stored as it came;
- it is begun outside and finished with Claude in the forge;
- it is born in the forge from the first word.

A brief is versioned like every artefact: a draft until the principal
approves it, and changed after that as any artefact is. It is the
provenance of its whole: a position mined from it cites the brief and
its version.

### It is chiselled into the intent

The intent is the working document: the consolidated current state
of what the principal holds. It is not a log. It is rewritten for
coherence every round, with the changes recorded in its history
companion beside it. A position in the intent says what the principal
holds and why, in as many words as it takes to be understood without
loss of meaning, and names what it comes from: a brief or a source.
The way to a position, that is, why it changed, what was said on the
way, trials and measurements, goes into the history in the same step
that writes the position, never into the position itself.

What is still open lives in a file of threads beside the intent. The
intent says what holds; the threads say what is being worked. A
thread carries the working debate for as long as it is unsettled, and
it is where an unfinished conversation is saved. A settled thread
leaves the file: what holds goes into the intent, and the record of
its closing in the history keeps the thread's last wording.

Work on the intent runs through the command `/forge`, which reads the
definition of the target artefact and runs the conversation by the
working methods of the forge. Substance changes go into the intent
first and propagate from there down the chain. Drafting early is a
legitimate tool on the way.

### Below the intent, the layers the project needs

Below the intent a project takes the layers it needs, and no layer
below the intent is a condition of another. Many projects end at the
intent, where what is wanted needs no solution written down. A layer
a project does not have is not missing: `/forge` and the checks say
nothing of it.

The assignment is the distilled handover document for the
recipients: complete, precise, structured, self-contained and
versioned. It carries the whole in-scope substance of the intent.
Nothing is left out for the sake of brevity, and a silent omission is
a defect. Leaving a matter out is legitimate only as an explicit
delegation to the recipients. There is no size target in either
direction: length is whatever fidelity requires.

The solution design says how the things wanted are realised. It is
derived from the lowest layer the project has above it: the intent
alone, the assignment or another layer between. It is worth writing
where the way is not obvious, where a choice has a price, or where
two hands would solve the same matter differently if it were not
written down; whether it is written, the principal says. From the
artefacts of the chain the thing must be buildable without a look at
the finished product.

Every artefact of the chain has a definition, a state file that says
what the artefact is, how it is found by questions, research and
sources, and what rules it owns; a template beside it says what comes
out. The files are numbered with gaps of ten, so that a layer can be
added without renaming anything.

### At every layer, blind reviewers

Two kinds of review press on a thought, and both are
[isolated reviewers](isolated-reviewers.md). The critic reads for
document quality and produces findings. The challenger presses on the
substance of the thinking and produces challenges. Each runs as an
isolated subagent, that is, a separate run of Claude that sees only
the files it is given and never the working conversation. Both are
invoked by hand by the principal, through `/critique` and
`/challenge`; both produce an immutable, dated report and rows in the
ledger. Each may take one artefact as its target; without one, it
reads the whole chain.

The reports are settled by walkthrough: the findings and challenges
are worked through with the principal one at a time, each to a
verdict, and the verdicts are written in one round. Beside the two
reviewers, a check reads the files of a project against the
conventions of the forge, through `/check`, in an isolated agent of
the same kind. No reviewer runs at a save, and a release runs no
reviewer on its own.

### Sources and research at any stage

External inputs such as transcripts, offers, documents and standards
live in the project's `sources/` directory. They may arrive at any
stage of a project's life: before the brief, as material for writing
it, during the work on the intent, or after. A source is immutable
once registered. The command `/ingest` stores, registers and
catalogues a source, and nothing more. Registration does not imply
intake: what a source is for is the principal's word, recorded in the
directory's index, and he alone directs how and when a source is
used. When the content of a source does enter the intent, it is the
principal's explicit act, cited with provenance to the file; what
someone said in a meeting is never silently promoted to the
principal's own position.

A research note answers one question about the world outside and is
immutable; the notes live in `research/` and are made through
`/research`. Both directories carry a light index of what is there
and what it is for, so that Claude and the principal know the
resources without re-reading them. The index is an automatic input of
no command: a contradiction between the intent and a source is not a
finding.

### Outputs for every audience

A render is an audience-specific output generated from the chain: a
pitch, an architecture picture, an executive summary, the README of
the repository. What is iterated is its recipe: the inputs, the
audience, the instructions and the output template, in one versioned
file composed with the principal. The command `/render` regenerates
the output from the recipe, and `/publish` makes a designed file from
the render on the principal's command. A render is never edited by
hand, assigns nothing and is not part of the chain: the artefacts
stay the source of truth. How this is done is
[Renders and recipes](renders-and-recipes.md).

A [work product](the-work-product.md) is an output that is neither an
artefact nor a render: any result of Claude's work the principal
asked for, such as a model, an analysis or a worked task, in whatever
form the work needs. It takes its inputs from the chain and the
resources, adds work of its own, is iterated, is handed over as a
result of the project, and what it shows flows back into the intent.
It is two files: the file that holds the content, and a specification
beside it that holds the way and the why. The principal works with
the file freely; a conclusion that is to hold goes into the intent
first.

The documentation of a project is generated the same way, never
composed by hand: pages of one topic each, with an index, for the
user, the extender and the evaluator, made by `/document` from a map
that is never shown to the reader.

### Saved and released

Everything lives in git, and the scripts of the forge are the only
door to it. Two commands move a project outward, at two speeds.
`/save` runs the light check and then commits and pushes on whatever
branch is checked out; no render is made, and it takes seconds.
`/release` runs from the main branch only: it runs its checks, settles
them with the principal, regenerates the README and the release notes
from the chain, and then saves with the release message and, at an
approved major, a tag.

Feedback from the recipients of an assignment has no channel of its
own. The principal processes it and feeds the conclusions back into
the intent, and the change travels down the chain again from there.

### The main courses of events

- A round of work: `/forge` reads the definition of the target
  artefact, the conversation runs by the working methods, and one
  write at the round's end changes the artefact, appends the records
  to its history and brings the ledger current.
- A review: `/critique`, `/challenge` or `/check` launches one
  isolated agent, its report is filed with IDs, and the findings are
  settled by walkthrough and written in one round.
- A render: `/render` generates the Markdown in an isolated subagent
  from a recipe and its inputs and writes the provenance; `/publish`
  makes the designed file from the render as it lies on disk.
- A save: `/save` runs the light check and commits and pushes through
  the save script.
- A release: `/release` runs its checks, settles them, regenerates the
  README and the release notes and then saves with the release
  message and tag.

## Why

The brief is rough on purpose. A required structure would force
premature tidiness, so none is required and none is forbidden. The
chiselling belongs to the intent, and a brief polished until the
intent has nothing left to do has gone too far.

The intent exists because a conversation ends and its context is
lost. Anything of value must live in a file, so the intent is the
document to read when returning to a project after weeks, instead of
excavating old conversations. It is rewritten for coherence rather
than appended to, so that it reads as the current state; the history
beside it keeps the way to every position.

The assignment carries the whole in-scope substance because a silent
omission is a defect. The goal is to have it right, not short, so the
defect is excess of the wrong kind, solving instead of assigning,
never length as such.

No layer below the intent is a condition of another, because each
artefact names its inputs in its definition and the number in a file
name orders the files without prescribing a sequence. The chain is a
star, not a fixed line. Many projects end at the intent because what
is wanted there needs no solution written down.

The reviewers never see the working conversation because that
blindness is the source of their value. They are invoked by hand and
settled by walkthrough.

Sources are kept apart from the intent because registration is not
intake. A source may be a standard to verify against, an inspiration
or a record of what someone else said, so the principal alone directs
how it is used, and nothing of it becomes his position without his
explicit act. Why a source is immutable once registered is not
recorded in the inputs of this page.

A render is generated rather than written because the artefacts must
stay the sole source of truth: content fixes go into the recipe or
the inputs, and the file is made again. The template of a recipe
fixes the structure and never the wording, because fixing the words
would turn the recipe into the render and make the inputs
meaningless. The boundary between the chain and a render is
authorship, not audience: an article the principal writes is a layer
of the chain, its translation is a render.

The work product is a kind of its own because a render could not hold
it: stretching the render to cover it would have cost the rule that a
render is never edited by hand, and an artefact of the chain is the
principal's thinking in items with IDs, which a file of any form
cannot carry.

Why the documentation is generated rather than composed by hand is
not recorded in the inputs of this page.

Save and release are two commands because the renders cost minutes
and tokens beyond reason at every save. With the renders at the
release only, the README on the main branch is current at every
release and stale in between visibly, never silently.

Isolation is bought with subagents, and git is reached through
scripts alone: the harness denies Claude raw git, so the scripts are
the only door, and a reviewer, a check and a render each run in a
subagent that sees the files it is given and nothing else.

## A worked example

The thought is invented and belongs to no project: a team's weekly
status meeting is to be replaced by a written update. The project's
placeholder slug is `written-updates`.

The thought arrives as a brief. The principal writes three short
paragraphs: what he wants (one written update each week instead of
the meeting), why (the meeting costs every member an hour, and most
of it is listening), and what he has not decided (who reads the
update and what happens to the questions it raises). A transcript of
the last team discussion is dropped into `sources/`, registered
through `/ingest`, and given its role in the index: a record of what
the team said, not the principal's own view.

The brief is mined into the intent. Through `/forge` Claude reads the
definition of the intent and asks what the brief leaves open: who the
update is for, what it must say, what a reader does with a question.
Each answer becomes a position with its reason, citing the brief and
its version as provenance. One thought of the brief, a daily update,
does not survive the questions; it leaves as a rejected direction
with the reason it was dropped. One matter stays open, how a question
raised by an update is answered, and becomes a thread beside the
intent. At the end of the round Claude asks whether to write, and
writes once: the intent, its history records, the ledger.

The reviewers press on the intent. The principal runs a critic lens:
an isolated subagent reads the brief and the intent, never the
conversation, and files findings on the quality of the document, such
as a position that gives no reason. A challenger persona presses on
the substance and challenges the unstated assumption that every
member will read a written update. Both reports are walked through
with the principal one item at a time; what he accepts is mended in
the intent in one round, and what he rejects is recorded as a
decision with its reason.

The project takes one layer below the intent. The team lead will run
the change, so an assignment is written: it carries the whole
substance of the intent, and the one matter the principal leaves to
the team, the form of the update, stands in it as an explicit
delegation. No solution design is written, because the way is
obvious; the chain of this project ends at the assignment, and
nothing says that a layer is missing.

Outputs are generated. A recipe for a one-page note to the team is
composed with the principal, and `/render` makes the note from the
assignment; when the intent changes, the note is made again rather
than edited. Beside it a work product is made: an analysis of what
the meeting costs, with its specification naming the transcript and
the positions it starts from and the method it uses; the conclusion
it supports goes into the intent first, as every conclusion that is
to hold does.

Everything is saved and released. After each round `/save` runs the
light check and commits and pushes. When the assignment is approved,
`/release` runs from the main branch: its checks are settled, the
README and the release notes are regenerated from the chain, and the
project is saved with the release message. When the team's feedback
arrives, the principal processes it and feeds the conclusions into
the intent, and the thought travels the chain once more.

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

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
