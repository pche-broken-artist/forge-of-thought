---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: a228e6be10b622a9
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
---

# How a thought travels through the forge

A thought travels through the forge as a chain of versioned
documents, from a rough brief to a saved release. This page follows
one invented thought along that way, station by station, so that a
user, an extender or an evaluator sees what happens to an idea and in
what order. It explains the way; what to type at each station is the
matter of the page of that command.

## What it is

The forge is not a program. It is a set of instructions that Claude
reads, with the deterministic work kept at its edge in scripts. A
thought enters it as a brief and becomes a chain of documents, the
artefacts (the documents of the chain, each versioned). Every
artefact has a definition: a file that says what the artefact is and
how it is found, by questions, research and sources. Beside the
definition stands the artefact's template, which says what comes
out. Working on an artefact means invoking `/forge` with the name of
the target artefact; Claude then reads that definition.

The chain starts at a brief and its trunk is the intent. Below the
intent a project takes the layers it needs, and none is a condition
of another. A layer a project does not have is not missing. Why the
chain is a star rather than a line, and why its files are numbered in
tens, is said in [The document chain](the-document-chain.md).

Three things travel with every artefact. Its history is an
append-only companion beside it, one record per change. The
decisions of the principal (the person whose thinking is being
forged, and the final authority on all content) are an append-only
file of their own. The ledger (one file that is the single source of
truth for the state of the project) is freely rewritten and brought
current after every operation. State lives in these Markdown files
of the project, never in the conversation and never in Claude's
memory.

## How it works

Take one invented thought. A team lead wants to replace the weekly
status meeting with a written note that everyone reads before the
week starts. The project gets a placeholder slug, `status-note`. The
stations below are the ones the thought meets, in the order it meets
them.

### It arrives as a brief

The thought is written down as a brief: the principal's text of one
whole of thinking, what he wants and why. The brief is free-form. Any
structure the principal finds useful may be used (prose, headings,
tables, use cases), no content is required and no IDs are given;
only a minimal header stands at the top. The brief for `status-note`
might be a page of headings such as "what the note replaces", "who
writes it", "what is still open", with a few sentences under each.

The brief is rough on purpose. It holds thoughts to be processed,
not decisions: they may be changed, reworked or dropped when the
brief is mined, and only the intent turns them into positions. In
one image, the brief is where thoughts are thrown in before they are
sifted, and not all of them survive. A brief polished until the
intent has nothing left to do has gone too far. It is composed in a
round or two and then mined. Three origins are equally legitimate:
the brief arrives finished from outside and is stored as it came; it
is begun outside and finished with Claude; or it is born in the
forge from the first word.

The brief is not the record of the finding around it. The finding is
wide (research, sources, the principal's ideas and Claude's). What
goes into the brief and what stays out is the principal's decision.
What stays out lives in `research/` and `sources/` where it is a
finding or a source, and otherwise nowhere. Two marks survive in a
brief: a source citation where the identity of a source supports,
limits or contradicts a thought, and a short remark where a
reservation must stay visible. Nothing in a brief marks authorship:
what is in it the principal approved, whoever first said it.

### It is chiselled into the intent

The brief is mined into the intent, the working document of the
project. The intent is the consolidated current state of what the
principal holds. It is not a log: it is rewritten for coherence
every round, and what changed is recorded in its history. In one
image, the intent is where the thought is chiselled; the brief
supplied the rough stone.

The intent is made of positions. A position says what the principal
holds and why it holds, in as many words as it takes to be
understood without loss of meaning, and names what it comes from, a
brief or a source. For `status-note`, one position might say that
the note is written by the person who ran the week, with the reason
that nobody else knows the week well enough, and cite the brief it
was mined from. A source citation in the brief becomes a fact with
provenance at mining.

The way to a position does not belong in the position: why it was
changed, what was said on the way, trials, measurements, which
research turned it. All of that is written into the history in the
same step that writes the position, while the whole context is at
hand. A position is dated once, the day it took its present shape.

What is still open lives beside the intent in a file of threads, one
for the project. A thread names the artefact it concerns, says what
is open and where it came from, and carries the working debate for
as long as it is unsettled: what was said, what was tried, the
proposals that await a decision. It is where an unfinished
conversation is saved. A settled thread leaves the file: what holds
goes into the intent, and the record of its closing in the intent's
history carries the thread's last wording word for word. For
`status-note`, a thread might ask whether a week with nothing to
report still gets a note.

The work on the intent runs as elicitation: Claude draws out by
questions what the principal has not yet articulated, and drafts
early where concrete text sharpens the reaction. Substance changes
go into the intent first and propagate from there down whatever
chain the project has. Feedback from the recipients of a later layer
has no channel of its own: the principal processes it and feeds the
conclusions back into the intent.

### Sources and research arrive when they arrive

External inputs (transcripts, offers, documents, standards) live in
`sources/`, immutable once registered, under plain slug filenames.
They may arrive at any stage of a project's life: before the brief
as material for writing it, during the work on the intent, or after.
For `status-note`, a transcript of the last status meeting might be
dropped in before a word of the brief exists. `/ingest` stores,
registers and catalogues a source, and nothing more.

Registration does not imply intake. What a source is for is
individual (a standard to verify against, inspiration, a meeting
record, material to absorb) and is recorded as its role in the
directory's index, in the principal's words. The principal alone
directs how and when a source is used. When source content does
enter the intent, it is his explicit act, cited with provenance to
the file. What someone said in a meeting is never silently promoted
to the principal's own position. Research is kept the same way: a
durable answer to one question lives in `research/`, and every
`sources/` and `research/` directory carries a light index, so that
Claude and the principal know what resources exist without
re-reading them. The index is an automatic input of no command.

### Below the intent, the layers the project needs

Many projects end at the intent. There, what is wanted needs no
solution written down. The chain grows below the intent only where
the project needs it, and the two layers the forge has definitions
for are these.

The assignment is the distilled handover document for the
recipients: complete, precise, structured, self-contained and
versioned. It carries the whole in-scope substance of the intent.
Nothing is left out for the sake of brevity, and a silent omission
is a defect. Leaving a matter out is legitimate only as an explicit
delegation, an item that says what the recipients are to produce or
to confirm. There is no size target in either direction: length is
whatever fidelity requires. For `status-note`, the assignment would
hand the team what the note shall contain, what it shall not, and
what is theirs to decide. What the recipients do with an assignment
handed to them is their own run of the forge.

The solution design says how the things wanted are realised. It is
derived from the lowest layer the project has above it, the intent
alone or the assignment, and whatever stands above it is its input.
It is worth writing where the way is not obvious, where a choice has
a price, or where two hands would solve the same matter differently
if it were not written down. Whether it is written, the principal
says. For `status-note`, a solution design would be worth it if the
note's channel, its template and who may edit it were real choices
with a cost. From the artefacts of the chain the thing must be
buildable without a look at the finished product: the product is
what is built, never a source of its own design. How deep the chain
must go for that is the project's to decide.

### Reviewers press on it

At every layer the documents and the thinking are pressed on by
isolated reviewers. The critic reads for document quality and
produces findings. The challenger reads the substance of the
thinking through a chosen persona and produces challenges. The check
reads for mechanical conformance with the conventions. Each runs as
an isolated subagent (a separate run of Claude that sees only the
files it is given) on the session model, and never sees the working
conversation. That blindness is the source of its value. Why it is
so is said in [The isolated reviewers](isolated-reviewers.md).

Every reviewer is invoked by hand by the principal, and may be
pointed at one artefact or at the whole chain. For `status-note`,
the principal might run a challenger against the intent before the
assignment is begun, and a critic against the assignment once it
stands. Each run produces an immutable dated report and rows in the
ledger. The findings are then settled by walkthrough (one item per
message, each closed with the principal's verdict) and the verdicts
are written in one round. Nothing a reviewer says blocks the
principal.

### Outputs are generated, not written

Once the thinking stands, outputs for every audience are generated
from the chain: a pitch, an architecture picture, an executive
summary, the README of the project. Such an output is a render. A
render is never edited by hand. What is iterated is its recipe: the
inputs, the audience, the instructions and the output template in
one versioned file, composed with the principal. `/render`
regenerates the output from the recipe and the artefacts as they
stand, and every render opens with its provenance, citing the recipe
and every input with their versions. When the thinking moves, the
render is regenerated, not patched. How this works in detail is
said in [Renders and recipes](renders-and-recipes.md).

A render assigns nothing and is not part of the chain; the artefacts
remain the sole source of truth. The boundary between the two is
authorship, not audience: a chain artefact is composed by the
principal, a render is generated from artefacts. An article the
principal writes is a layer of the chain; its translation is a
render. For `status-note`, a one-page summary for the wider
department would be a render of the intent, made from a recipe that
names the intent as its input and the department as its audience.

The documentation of a project is made the same way. Its pages, one
topic each, and their index are generated from a map that is never
shown to the reader, by one run that asks nothing and regenerates
only what changed.

### It is saved and released

Everything is saved to git, and the scripts of the forge are the
only door to it. A save runs the light check and then commits and
pushes on whatever branch is checked out, with no render, in
seconds. A release runs on the main branch only. It runs its checks,
settles them by walkthrough, regenerates the README and the release
notes from the settled sources, and then saves with the release
message, named by the intent's version. An approved major carries a
tag with a fixed name, so that the checks and the release notes can
rely on it. For `status-note`, a release would leave a README and
release notes in the project root that say what the project is and
what each release changed.

### The main courses of events

A round of work: `/forge` with the name of the target artefact reads
its definition, the conversation runs by the working methods, and one
write at the round's end changes the artefact, appends the records
to its history and brings the ledger current.

A review: `/critique`, `/challenge` or `/check` launches one isolated
agent, its report is filed with IDs, and the findings are settled by
walkthrough and written in one round.

A render: `/render` generates the Markdown in an isolated subagent
from a recipe and its inputs and writes the provenance; `/publish`
makes the designed file from the render as it lies on disk, only on
the principal's command.

A save: `/save` runs the light check and commits and pushes through
the forge's own script.

A release: `/release` runs its checks, settles them, regenerates the
README and the release notes, and then saves with the release
message and tag.

## Why

The brief has no required structure. Because a required structure
would force premature tidiness, none is demanded, and none is
forbidden either.

The intent is a rewritten document and not a log. Because chat
context dies, anything of value must live in a file. The intent is
the document to read when returning to a project after weeks,
instead of excavating old conversations. The way to a position goes
into the history in the same step, while the whole context is at
hand.

The assignment leaves nothing out in silence. The goal is to have it
right, not short; the defect is excess of the wrong kind, solving
instead of assigning, never length as such.

The chain takes only the layers the project needs. Where what is
wanted needs no solution written down, the project ends at the
intent. A solution design earns its place only where the way is not
obvious, a choice has a price, or two hands would otherwise solve
the same matter differently.

The reviewers are blind to the conversation. The inputs say that
this blindness is the source of their value; what the blindness
protects against is said on the page of the reviewers.

A render is regenerated and never patched. The template of a recipe
fixes the structure and what information appears where, never the
wording. Each rendering re-derives the words from the current
inputs; fixing the text in the template would turn the recipe into
the render and make the inputs meaningless.

Save and release are two commands. The renders cost minutes and
tokens beyond reason at every save. With the renders at the release
only, the README on the main branch is current at every release and
stale in between visibly, never silently.

A source is used only as the principal directs. What a source is for
is individual, and what someone said in a meeting is not the
principal's own position; so it enters the intent only by his
explicit act, with provenance.

Why feedback from recipients has no channel of its own, and why the
documentation is generated rather than composed by hand, the inputs
state as rules; the reason is not recorded.

## See also

- [The document chain](the-document-chain.md): the chain as a star
  and why files are numbered in tens.
- [The isolated reviewers](isolated-reviewers.md): why the reviewers
  never see the conversation.
- [Renders and recipes](renders-and-recipes.md): how an output is
  generated from the artefacts.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-11 for version 5.3 from the files the
front-matter names; never edited by hand.
