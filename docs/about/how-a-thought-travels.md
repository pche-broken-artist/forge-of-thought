---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - projects/forge/40-solution-design.md
  - projects/forge/10-intent.md
---

# About how a thought travels

This page follows one thought through Forge of Thought, from the
first rough text to a saved and released project, in the order the
thought meets each station. It is for anyone who uses the forge,
extends it or weighs whether to adopt it, and wants the whole course
in one view before reading about any single part. It was put
together from `CLAUDE.md` (its Document chain, Isolated reviewers and
Persistence sections), from the forge's own solution design (its
part on how the parts work together) and from the positions of the
forge's own intent that say what each station is for.

## The brief: the thought as it arrives

A thought enters as a brief: the principal's own text of one whole
of thinking, what he wants and why. It is free-form, with no
required structure and no IDs, because a required structure would
force premature tidiness. It holds thoughts to be processed, not
decisions: they may be changed, reworked or dropped later.

A brief is rough on purpose, neither perfect nor detailed. The
chiselling belongs to the next station, and a brief polished until
there is nothing left to do has gone too far. It may arrive finished
from outside, be begun outside and finished in the forge, or be born
in the forge from the first word; the forge treats the three alike.
A project may have more than one brief: a later large whole of
thinking gets a brief of its own, so that it can be tempered before
it enters the trunk.

## The intent: the thought chiselled

The brief is mined into the intent, the working document that holds
the consolidated current state of what the principal wants. It is
found by elicitation: questions that help the principal say what he
has not yet put into words. What it holds:

- **positions**: what the principal holds and why, each naming what
  it comes from, a brief or a source;
- **facts**: what is the case, as the principal or a source states
  it;
- **rejections**: directions dropped, with the reason they were
  dropped;
- **threads**: open matters still being worked, kept in a file of
  their own beside the intent, each naming the artefact it concerns.

The intent is not an append-only log. It is rewritten for coherence
every round, and what changed and why is recorded in its history
beside it. It exists because chat context dies and anything of value
must live in a file: it is the document to read on returning to a
project after weeks. The way to a position, what was said, tried or
measured, goes into the history; the intent says only what holds.

Substance changes go into the intent first and flow down from there.
When work further down shows that what is wanted must change, the
intent changes first.

## Below the intent: the layers a project needs

The brief and the intent are the trunk of every project. Below the
intent a project takes the layers it needs, none a condition of
another, and many end at the intent, where what is wanted needs no
more written down. A layer a project does not have is not missing.

- **The assignment** is the handover document for the recipients:
  complete, precise and self-contained. It carries the whole in-scope
  substance of the intent; leaving a matter out is legitimate only as
  an explicit delegation, and a silent omission is a defect.
- **The solution design** says how the things wanted are realised.
  It is worth writing where the way is not obvious, where a choice
  has a price, or where two hands would solve the same matter
  differently. It is derived from the lowest layer the project has
  above it. From the artefacts of the chain, the thing must be
  buildable without a look at the finished product.

Files of the chain are numbered so that a new layer can be added
without renaming anything that exists.

## Reviewers at every layer

At any layer, the principal may send isolated reviewers against the
documents. A critic judges the quality of the documents, a
challenger the substance of the thinking, and a check the mechanical
conformance with the forge's conventions. Each runs as a separate
agent that sees the project's files and never the working
conversation: that blindness is the source of its value. Each
produces a dated report that is never edited, and every finding or
challenge in it is settled with the principal one item at a time,
each ending in a recorded verdict: accepted, modified, rejected or
parked. No reviewer runs on its own; the principal invokes them,
and the save and the release run the checks their definitions name.

## Renders: the thought for each audience

From the artefacts, outputs are generated for every audience: a
pitch, an executive summary, an architecture picture, the
repository README. A render is never edited by hand. What is worked
on is its recipe, one file that holds the inputs, the audience, the
instructions and the output template, and the render is generated
anew from it whenever the thinking moves. A render assigns nothing
and is not part of the chain: the artefacts stay the source of
truth. The boundary is authorship: what the principal composes is a
layer of the chain, what is generated from it is a render.

## Saved and released

Everything lives in files of the project, never in the conversation,
and is kept in git. A save checks the project lightly and then
commits and pushes. A release runs its checks, regenerates the
README and the release notes, and then saves with the release
message and tag. The two are separate because generating the renders
at every save would cost time and tokens beyond reason; with the
renders at the release only, the README is current at every release
and visibly stale in between.

## Sources and research, at any stage

External inputs (transcripts, offers, documents, standards) and
research notes may arrive at any stage, even before the brief. They
are stored and catalogued, and never changed after that. Storing a
source does not take it in: the principal alone directs how and when
each one is used, and when its content enters the intent, it does
so as his explicit act, with its provenance cited.

## The main courses of events

- **A round of work:** the conversation over an artefact runs by the
  forge's working methods, and one write at the round's end changes
  the artefact, appends the records to its history and brings the
  ledger current.
- **A review:** one isolated agent is launched, its report is filed
  with IDs, and the findings are settled one by one and written in
  one round.
- **A render:** the output is generated in an isolated agent from a
  recipe and its inputs, opening with where it came from, and a
  designed file is made from it only on the principal's command.
- **A save:** a light check runs, and the project is committed and
  pushed.
- **A release:** the release checks run and are settled, the README
  and release notes are regenerated, and the project is saved with
  the release message and tag.

## See also

- [About the document chain](the-document-chain.md): the chain as a star and why files are numbered in tens.
- [About the isolated reviewers](isolated-reviewers.md): why the reviewers never see the conversation.
- [About renders and recipes](renders-and-recipes.md): how an output is generated from the artefacts.
