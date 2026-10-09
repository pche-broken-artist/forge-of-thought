---
generated: 2026-10-09
made: derived
inputs-hash: f8e62cf5657fa026
inputs:
  - CLAUDE.md
  - projects/forge/40-solution-design.md
  - projects/forge/10-intent.md
---

# About how a thought travels

This page tells the course of one thought through the forge, from
the moment it is written down to the moment it is released, in the
order a thought meets each station. It is for the user who works in
the forge, the extender who adds to it and the evaluator who wants to
understand what happens to an idea here without running anything. It
was put together from the universal core (`CLAUDE.md`), the solution
design of the forge and the positions of its intent that say what
each station is for.

## The idea in one picture

The forge is a workshop where thought is tempered and shaped. Any
idea, a process redesign, a platform initiative, an organisational
topic, anything, travels a chain of versioned documents from the
idea put together onward, under isolated adversarial review. Two
people are at work: the principal, whose thinking is being forged
and who holds final authority on all content, and Claude, the
principal's cognitive extension, who owns structure, order and
process discipline and proposes but never decides.

The chain ends where the project needs it to. Every chain starts at
a brief and its trunk is the intent; below the intent a project takes
the layers it needs, none a condition of another, and many end at the
intent. A layer a project does not have is not missing.

## It arrives as a brief

A thought enters as a brief: the principal's own text of one whole of
thinking, what he wants and why, with what he chose to take from the
finding around it. The brief is free-form, any structure the
principal finds useful, no required content and no IDs. It holds
thoughts to be processed, not decisions: they may be changed,
reworked or dropped when mined, and only the intent turns them into
positions.

A brief is rough on purpose, neither perfect nor detailed. The
chiselling belongs to the intent, and a brief polished until the
intent has nothing left to do has gone too far. It is where thoughts
are thrown in before they are sifted; not all of them survive. The
brief may arrive finished from outside and be stored as it came, be
begun outside and finished with Claude, or be born in the forge from
the first word; the forge does not distinguish the three. A project
may have more than one brief: every later whole of thinking that
would otherwise land in the intent as a batch of unproven positions
is born as a brief of its own and mined when the principal says so.

## It is chiselled into the intent

The intent is the working document: the consolidated current state
of the principal's intent. It is not a log. It is rewritten for
coherence every round, with the changes recorded in its history
beside it. It exists because chat context dies and anything of value
must live in a file: it is the document to read when returning to a
project after weeks, instead of excavating old conversations.

The chiselling is elicitation. Claude never fills a gap by
assumption; he asks, one question per message, and helps the
principal extract what is in his head, including what he has not yet
articulated. An early draft is a legitimate tool of that work,
because concrete text sharpens the reaction, and before any write
Claude reflects back what was understood, so the write confirms
rather than surprises. Many iterations are the normal mode.

What the intent holds is structured, items with stable IDs rather
than prose:

- positions, what the principal holds and why it holds, each naming
  what it comes from, a brief or a source, and dated once;
- facts, what is the case as the principal or a source states it,
  not a stance;
- rejected directions, with the reason each was dropped, so the
  trace survives;
- open threads, kept in a file of their own beside the intent: what
  is unresolved, where it came from and the working debate for as
  long as it is unsettled. A settled thread leaves that file, what
  holds goes into the intent, and its last wording is kept word for
  word in the history.

The way to an item, why it changed, what was said, trials, which
research turned it, goes into the history in the same step that
writes the item, never into the item itself.

Substance changes go intent-first and propagate from there down
whatever chain the project has. A change may come from below, when
solving shows that what is wanted must change, and then the intent
changes first; only wording is fixed downstream directly.

## Below the intent, the layers the project needs

Where the thought is to be handed over, the project takes an
assignment: the distilled handover document for the recipients,
complete, precise, structured and self-contained. It carries the
whole in-scope substance of the intent. Nothing is left out for the
sake of brevity, a silent omission is a defect, and leaving a matter
out is legitimate only as an explicit delegation. What keeps it an
assignment rather than a solution is the kind of content, never the
amount. The recipients may be teams, colleagues or the principal's
future self; what they do with it is their own run of the forge, and
their feedback has no channel of its own: the principal processes it
and feeds his conclusions back into the intent.

Where the way is not obvious, where a choice has a price, or where
two hands would solve the same matter differently if it were not
written down, the project takes a solution design: how the things
wanted are realised. It is derived from the lowest layer the project
has above it, and it is read by whoever realises the solution, a
person or an agent, without the principal in the room. From the
artefacts of the chain the thing must be buildable without a look at
the finished product. Whether a project takes either layer, the
principal says; many projects end at the intent, where what is
wanted needs no solution written down.

Every artefact has a definition that says what it is, how it is
found and what rules it keeps, paired with a template that says what
comes out. The chain grows by adding a layer's definition, without
reworking anything that exists.

## At every layer, blind reviewers

At any station the principal may call a reviewer. Reviewers are
isolated: each runs in a subagent that sees the project's documents
only and never the working conversation. That blindness is the
source of their value. Three kinds, strictly separate:

- the critic reads for document quality, never substance, through a
  chosen lens, and produces findings;
- the challenger presses on the substance of the thinking, never
  document quality, through a chosen persona, and produces
  challenges, each with a severity, a falsifiable "what would change
  my mind" and an epistemic status, and with a ban on fabrication;
- the check verifies mechanical conformance with the conventions,
  never substance or quality.

Every run produces an immutable, dated report. Nothing a reviewer
finds blocks anything: critiques inform, only the principal decides.
The findings and challenges are settled by walkthrough, one item per
message, each closed with a verdict, and every verdict is recorded;
a rejected finding or challenge is a decision with its reason, kept
like any other. An accepted challenge is mended where it needs to
be, and where that is the substance, the intent changes first.

## Outputs for every audience, generated

The artefacts stay the sole source of truth. Whatever an audience
needs to see, a pitch, an architecture picture, an executive
summary, the repository README, is a render: generated from the
chain and never edited by hand. What is iterated is its recipe, the
inputs, the audience, the instructions and the output template in
one versioned file; the render is regenerated from it whenever the
thinking moves, and it opens with its provenance, citing the recipe
and every input with their versions. A render assigns nothing and is
not part of the chain. The boundary is authorship: an article the
principal writes is a layer of the chain, its translation is a
render. Where a recipe names a format, a plain file is made beside
the Markdown, and a designed file may be made from it on the
principal's command.

The documentation of a project travels the same way. It is a set of
pages of one topic each, with an index, generated from the project's
documents and never composed by hand: a page either mirrors the files
that own its topic or is derived from named evidence, and says which.
A run regenerates only the pages whose inputs changed, decided
mechanically. A page is not a render, no recipe stands behind it, but
it cannot drift from what it mirrors for the same reason a render
cannot.

## Sources and research, at any stage

External inputs, transcripts, offers, documents, standards, may
arrive at any stage of a project's life: before the brief as material
for writing it, during intent work, or after. They are stored in the
project's sources, immutable once registered, and catalogued in a
light index that says what each is for. Registration does not imply
intake: a source's role is individual, and the principal alone
directs how and when each source is used. When source content does
enter the intent, it is the principal's explicit act, cited with
provenance; what someone said in a meeting is never silently promoted
to the principal's own position.

Research is the same kind of resource: before inventing, current
best practice is looked up, and a durable answer to one question is
stored as an immutable note and indexed. Neither index tracks
anything, and neither is an automatic input of any command.

## Everything is saved to git, and released

State lives in Markdown files of the project, never in the
conversation and never in the assistant's memory. Every project is a
git repository of its own; the engine is another. Two doors, two
speeds: a save runs its check and then commits and pushes on
whatever branch is checked out, no render, seconds. A release runs
from the released line only, runs its checks, settles them,
regenerates the README and the release notes, and then saves with
the release message and, at an approved major, the tag. The release
number is the intent's version. The renders cost minutes at every
save and are made at the release only, so the README is current at
every release and visibly stale in between, never silently. A
release does not regenerate the documentation: it reports the age of
the index against the intent's version and offers the run.

## The main courses of events

A round of work: the definition of the target artefact is read, the
conversation runs by the working methods, and one write at the
round's end changes the artefact, appends the records to its history
and brings the ledger current.

A review: one isolated agent is launched, its report is filed with
IDs, and the findings are settled by walkthrough and written in one
round.

A render: the Markdown is generated in an isolated subagent from a
recipe and its inputs and opens with its provenance; the designed
file, when wanted, is made from the render as it lies on disk.

A save: the light check runs, then the repository is committed and
pushed through the forge's own script, on whatever branch is checked
out.

A release: the release checks run and are settled, the README and
the release notes are regenerated, and the repository is saved with
the release message and the tag.

## See also

- [About the document chain](the-document-chain.md): the chain as a
  star and why files are numbered in tens.
- [About the isolated reviewers](isolated-reviewers.md): why the
  reviewers never see the conversation.
- [About renders and recipes](renders-and-recipes.md): how an output
  is generated from the artefacts.
