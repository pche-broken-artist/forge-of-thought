---
generated: 2026-10-10
made: derived
inputs-hash: 045bf249e11445b6
inputs:
  - CLAUDE.md
  - projects/forge/40-solution-design.md
  - projects/forge/10-intent.md
---

# About how a thought travels

This page follows one thought through the forge, from the moment it
is written down to the moment it is released, in the order it meets
each station. It is for anyone who wants the whole course in one
view before reading about any one part: the user who will work this
way, the extender who will add to it, and the evaluator who wants to
understand what the thing is. It was put together from `CLAUDE.md`,
from the solution design of the forge and from the intent of the
forge, which give the chain, the reasons for its stations and the
main courses of events.

## The idea: a chain of documents under blind review

The forge is a workshop where thought is tempered and shaped. Any
idea, a process redesign, a platform initiative, an organisational
topic, travels a chain of versioned documents from the moment it is
put together onward, under isolated adversarial review. Two people
are at work: the principal, whose thinking is being forged and who
is the final authority on all content, and Claude, the principal's
cognitive extension, who owns structure, order, process discipline
and document hygiene, and who proposes but never decides.

The forge is not a program. It is a set of instructions that Claude
Code reads, with deterministic work kept at its edge in scripts.
Everything of value lives in Markdown files of the project, never in
the conversation and never in the assistant's memory, because a
conversation dies and a file does not.

## It arrives as a brief

A thought enters as a brief: the principal's own text of one whole
of thinking, what he wants, why, and what he chose to take from the
finding around it. The brief is free-form, any structure the
principal finds useful and no required content, because a required
structure would force premature tidiness. It is rough on purpose,
neither perfect nor detailed: it is where thoughts are thrown in
before they are sifted, and not all of them survive. A brief
polished until the intent has nothing left to do has gone too far.

A brief may arrive finished from outside, be begun outside and
finished with Claude, or be born in the forge from the first word;
the forge does not distinguish the three. Nothing in a brief marks
who first said what: whatever is in it, the principal approved. A
project may have more than one brief: a later whole of thinking that
would otherwise land in the intent as a batch of unproven positions
is born as a brief of its own, where it can be tempered before it
enters the trunk.

## It is chiselled into the intent

The brief is mined into the intent, the trunk of every project and
the working document: the consolidated current state of the
principal's thinking. The chiselling happens by elicitation: Claude
draws out by questions what the principal has not yet articulated,
one question at a time, and never fills a gap by assumption. A draft
early is a legitimate tool of that elicitation, because concrete
text sharpens the reaction.

The intent is made of items with stable IDs rather than prose:
positions the principal holds, each with the reason it holds and
what it comes from, a brief or a source; facts, what is the case as
the principal or a source states it; rejected directions, with the
reason each was dropped. What is still open is kept as threads in a
file beside the intent, each naming the artefact it concerns and
carrying the working debate until it is settled. The intent is not a
log: it is rewritten for coherence every round, and every change is
recorded in an append-only history companion beside it, the way to
an item in the record and never in the item. It exists because chat
context dies: it is the document to read when returning to a project
after weeks, instead of excavating old conversations.

Work on the intent runs in rounds. A round is one working
conversation; what is agreed is carried in the conversation,
reflected back so the write confirms rather than surprises, and
written once at the round's end on the principal's word: one version
bump for the whole round, its changes recorded in the history.
Many iterations are the normal mode, and an intent may grow and
change substantially between versions.

## Below the intent, the layers the project needs

The chain ends where the project needs it to. Below the intent a
project takes the layers it needs, none a condition of another, and
many end at the intent, where what is wanted needs no solution
written down. A layer the project does not have is not missing.

Two layers the forge has today are the assignment and the solution
design. The assignment is the distilled handover document for the
recipients, who may be teams, colleagues or the principal's future
self: complete, precise, structured and self-contained. It carries
the whole in-scope substance of the intent, and a silent omission is
a defect; leaving a matter out is legitimate only as an explicit
delegation. Length is whatever fidelity requires, and the defect is
solving instead of assigning, never length as such.

The solution design says how the things wanted are realised. It is
worth writing where the way is not obvious, where a choice has a
price, or where two hands would solve the same matter differently if
it were not written down; whether it is written, the principal says.
From the artefacts of the chain the thing must be buildable without
a look at the finished product: the product is what is built, never
a source of its own design.

Substance changes go intent-first and propagate down whatever chain
the project has; a change may come from below, when solving shows
that what is wanted must change, and then the intent changes first.
Only wording is fixed in a lower layer directly. Every artefact has
a definition that says what it is and how it is found, and the chain
grows by adding a definition, without reworking anything that
exists.

## Sources and research, at any stage

External inputs, transcripts, offers, documents, standards, may
arrive at any stage of a project's life: before the brief as
material for writing it, during intent work, or after. They are
stored in the project's sources, immutable once registered, and
catalogued in a light index that says what each is and what it is
for. Registration does not imply intake: the principal alone directs
how and when each source is used, and when source content does enter
the intent it is his explicit act, cited with provenance. What
someone said in a meeting is never silently promoted to the
principal's own position.

Research is the other resource: before inventing, Claude looks up
current best practice, and durable findings are stored as dated
notes, immutable, and indexed beside the sources. Neither sources
nor research are an automatic input of anything: Claude reaches for
a file by its own judgement or on request.

## At every layer, blind reviewers

At any layer the principal may call a reviewer. Three kinds exist,
of one shape and strictly separate jobs: the critic reads for
document quality, never substance; the challenger presses on the
substance of the thinking, never document quality; the check
verifies mechanical conformance with the conventions, never
substance or quality. Each runs as an isolated subagent that sees
the project's documents and never the working conversation, and
that blindness is the source of its value. No reviewer runs on
Claude's own judgement: each is invoked by hand.

Every run leaves an immutable, dated report with findings or
challenges under stable IDs, and every one of them ends in a
recorded verdict: the items are settled by walkthrough, one item
per message, accepted, modified, rejected or parked, and the
verdicts are written in one round. A rejected finding or challenge
is recorded as a decision with its reason, so nothing a reviewer
said disappears without trace. Reviewers inform and never block:
only the principal publishes.

## Outputs for every audience, generated

A render is an audience-specific output generated from the chain: a
pitch, an architecture picture, an executive summary, the repository
README. A render is never edited by hand. What is iterated is its
recipe, which names the inputs, the audience, the instructions and
the output template in one versioned file; the render is regenerated
from it mechanically, and regenerated again when the thinking moves,
so that the artefacts stay the only source of truth. The boundary
between chain and render is authorship: an article the principal
writes is a layer of the chain, its translation is a render. Where
a recipe names a format, a plain Word or PowerPoint file is made
beside the Markdown; a designed file is made from the render only on
the principal's command.

The documentation of a project is generated the same way, from the
project's own documents: pages of one topic each, for the user, the
extender and the evaluator, in a standard outline of five sections
filled only where the project has material. Each page either
mirrors the files that own its topic or is derived from named
evidence, and says which, so a page cannot drift from what it
mirrors. A run regenerates only the pages whose inputs changed. The
documentation is never composed or maintained by hand.

## Saved to git, released with a README and release notes

Every project is a git repository of its own, and the scripts of the
forge are the only door to git. Two doors, two speeds: a save runs
its check and commits and pushes on whatever branch is checked out,
no render, in seconds; a release runs on the main branch only, runs
its checks and settles them, regenerates the README and the release
notes from the settled documents, and then saves with the release
message and, at an approved major version, a tag. The renders are
made at the release only because they cost minutes and tokens beyond
reason at every save; between releases the README is stale visibly,
never silently. Immutability of documents is a process rule, not a
git mechanism.

## The main courses of events

- **A round of work.** The definition of the target artefact is
  read, the conversation runs by the working methods, and one write
  at the round's end changes the artefact, appends the records to its
  history and brings the ledger current.
- **A review.** A critique, a challenge or a check launches one
  isolated agent, its report is filed with IDs, and the findings are
  settled by walkthrough and written in one round.
- **A render.** The Markdown is generated in an isolated subagent
  from a recipe and its inputs, with its provenance written at its
  head; the designed file, when wanted, is made from the render as it
  lies on disk.
- **A save.** The light check runs, and the repository is committed
  and pushed on the current branch through the forge's own script.
- **A release.** From the main branch only, the checks run and are
  settled, the README and the release notes are regenerated, and the
  repository is saved with the release message and tag.

## See also

- [About the document chain](the-document-chain.md): the chain as a
  star and why files are numbered in tens.
- [About the isolated reviewers](isolated-reviewers.md): why the
  reviewers never see the conversation.
- [About renders and recipes](renders-and-recipes.md): how an output
  is generated from the artefacts.
