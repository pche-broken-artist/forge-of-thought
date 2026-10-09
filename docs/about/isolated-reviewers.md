---
generated: 2026-10-09
made: derived
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About the isolated reviewers

This page explains how the forge reviews a project: what kinds of
reviewer there are, why they are built as they are and what their
verdicts are worth. It is for someone using the forge, someone
extending it with a new reviewer, and someone judging whether to trust
it. It was put together from `CLAUDE.md` (its section on isolated
reviewers), which gives the mechanism, and from the forge intent
(`projects/forge/10-intent.md`), which gives the reasons.

## Three kinds, one shape

The forge has three kinds of reviewer. Each has its own job and none
does another's.

| Kind | Judges | Varies by | Produces |
|---|---|---|---|
| critic | the quality of the documents, never the substance | lens | findings (FND) |
| challenger | the substance of the thinking, never the quality of the documents | persona | challenges (CHL) |
| check | mechanical conformance with the conventions, never substance or quality | check | findings (FND) |

What the three share is one shape. Every reviewer runs as an isolated
subagent. It sees the project's documents and nothing of the working
conversation. It runs on the session model, the same one the whole
forge runs on: speed is bought with context, never with a weaker
reviewer. It is invoked by hand. Its run ends in a dated report that
is never edited afterwards, and what it found is entered in the
project's ledger. A check that finds nothing files no report.

What each kind goes after is described on its own page: [About the
critic](the-critic.md), [About the challenger](the-challenger.md) and
[About the check](the-check.md).

## Why they are isolated

The reviewers are blind to the conversation on purpose, and that
blindness is the source of their value. A reviewer that has heard what
the author meant reads that meaning into the text. A reviewer that has
only the documents reads what is written, and it cannot be told what
was meant. Whatever the documents leave unsaid, it cannot fill in.

## Why review and challenge are two reviewers

Putting the review of a document and the challenge of its substance
into one reviewer was considered and rejected: an agent doing both
does neither properly. The formal audit of a document benefits from a
clean context, while the challenge of the substance benefits from a
different register entirely. So the critic and the challenger are
separate. The checks are a third kind on the same mechanism, limited
to mechanical conformance: they report and propose, and the principal
decides what is fixed.

## One contract per kind, and a lens that only narrows

The behaviour all members of a kind share is written once, as one
contract for that kind. The contract owns the conduct and the
isolation, the subject and its boundary, the way of working and the
shape of the report. The agent file of a single lens, persona or
check carries only its own Lens section: what it reads and what it
goes after.

A Lens section is a specialisation of its contract, never a
replacement. It may narrow what is read or make a shared rule
stricter. It may never rename, drop or duplicate a shared rule or
field, and when the protocol changes, it changes in the contract
alone. There is one contract per kind and no common one, because the
shared texts of the kinds differ almost whole. A new lens, persona or
check is added only by the principal's decision, and only where what
it would find genuinely differs from what already exists: reviewers
that would say the same things in different words are noise.

## Nothing blocks

The reviewers inform; the principal alone decides what is published.
There are no hard quality gates. Yet nothing a reviewer raises is
silently ignored: every finding and every challenge is either fixed
or explicitly rejected with its reason recorded as a decision.
Rejecting and parking are legitimate outcomes; ignoring is not.

No reviewer runs on Claude's own judgement. The principal invokes it,
or a save or a release runs the checks that its own definition names.
What comes back is settled in a walkthrough, one item at a time,
described in [Walk through a list](../use/walk-through-a-list.md).

An accepted challenge is mended wherever it needs to be, and one that
mends nothing was not accepted. A challenge of a layer below the
intent is mended in that layer and changes nothing above it, unless it
shows that what is wanted cannot be realised, or only at a price not
worth paying; then a thread is opened in the intent and what is wanted
is decided there.

An artefact is best challenged before the next layer is first derived
from it, the intent before the first assignment, while accepted
challenges are still cheap to absorb. Whether to challenge again
later is left to whoever runs the process.

## Isolation is not independence

The author, the critic and the challengers share one model family.
What that family systematically cannot see, none of them will find.
Agreement between the reviewers is therefore never treated as
validation: it means only that the artefact is consistent under one
set of priors.

The calibration point lies outside: review by humans or by a different
model family, invited at the principal's discretion. Challengers on a
different model family are a decided direction, not something the
forge has today. Whatever a reviewer writes may inspire, but nothing
enters the intent because a reviewer wrote it, only because the
principal composed it, and an accepted challenge may change the intent
by taking something away as readily as by adding.

## What never enters a report

A report is a public file, or may be quoted into one. Instance facts,
the names, roles, addresses and hosts that belong to one particular
forge and its principal, never enter a reviewer's report, not even
where they would explain a finding.

## See also

- [About the critic](the-critic.md): what the critic judges.
- [About the challenger](the-challenger.md): what the challenger judges.
- [About the check](the-check.md): what a check verifies.
- [Walk through a list](../use/walk-through-a-list.md): how findings are settled.
