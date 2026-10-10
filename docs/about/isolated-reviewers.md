---
generated: 2026-10-10
made: derived
inputs-hash: cc9d19f8addc5aba
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About the isolated reviewers

This page explains what the reviewers of the forge are, how the
three kinds share one shape and why they are built to be blind. It
is for anyone who runs a review, adds a reviewer or judges whether
the reviews mean anything: the user, the extender and the evaluator.
It was put together from the Isolated reviewers section of
`CLAUDE.md`, which gives the mechanism, and from the Review and
Operating environment positions of `projects/forge/10-intent.md`,
which give the reasons.

## Three kinds, one shape

A reviewer is a subagent that reads a project's documents and
writes a report. The forge has three kinds, each with one job and
none with another's:

| Kind | Judges | Varied by | Produces | Filed in |
|---|---|---|---|---|
| the critic | document quality, never substance | lenses | findings, `FND` | `reviews/YYYY-MM-DD-critique-<lens>.md` |
| the challenger | the substance of the thinking, never document quality | personas | challenges, `CHL` | `challenges/YYYY-MM-DD-challenge-<persona>.md` |
| the check | mechanical conformance with the conventions, never substance or quality | checks | findings, `FND` | `reviews/YYYY-MM-DD-check-<name>.md` |

Quality and substance are two reviewers and not one on purpose.
The forge once considered merging document review and substantive
challenge into a single reviewer and rejected it: an agent doing
both does neither properly. The formal audit benefits from a clean
context, the substantive challenge from a different register
entirely. The check came later and was built on the same mechanism
rather than a new one: its own contract, one agent per check, a
roster, a run by hand. Whether a check is called a review was left
undecided, because it makes no difference to the mechanism, which
takes further kinds as they come.

Each kind is run by its own command, `/critique <lens>`,
`/challenge <persona>` and `/check <check>`, and each command,
given bare, lists its roster and recommends a fit. The critic and
the challenger take an optional target, an artefact named the way
`/forge` names it, by its state; without one they read the whole
chain, so that one file or one transition can be reviewed alone. A
check takes a project by its slug, or the engine.

## Why they are blind

Every reviewer runs isolated. It sees the project's documents and
nothing else: never the working conversation in which the
documents were composed, nothing of what was said, meant or agreed
along the way. That blindness is the source of its value. A
reviewer that could be told what was meant would judge the
intention; a blind one judges only what is on the page, which is
all a recipient will ever get.

They run on the session model, the one model the whole forge runs
on. Speed is bought with context, never with a weaker reviewer:
a review is reasoning work, and a cheaper model would read less
sharply, not merely more slowly.

## Invoked by hand, settled by walkthrough

No reviewer runs on Claude's own judgement. Each is invoked by
hand, and what a save or a release runs is said in the definition
of the save and the release, nowhere else. The reports are
immutable and dated: a run is a record of what a reviewer saw on
that day, and a correction happens in the document, never in the
report. A check that finds nothing files nothing.

The best moment to challenge an artefact is before the next layer
is first derived from it, the intent before the first assignment,
while an accepted challenge is still cheap to absorb. Whether a
reviewer runs again later, after a draft or before an approval, is
left to the judgement of whoever runs the process; no rule
prescribes it.

Every report is settled by walkthrough, item by item. The states a
finding or a challenge may take are the ledger's; `open` means only
that it has not yet been judged.

## Nothing blocks, nothing is ignored

There are no hard quality gates. Findings and challenges are
advisory; the principal alone decides what is published, and a
missing section may be a deliberate delegation rather than a
defect. The check, too, is read-only and advisory: it reports and
proposes, the principal decides what is fixed.

The counterpart of that freedom is that nothing is silently
ignored. Every finding and every challenge is either fixed or
explicitly rejected with a recorded reason, a decision record.
Rejecting and parking are legitimate outcomes; ignoring is not. An
accepted challenge is mended wherever it needs to be, and one that
mends nothing was not accepted. A challenge of a layer below the
intent is mended in that layer and changes nothing above it, unless
it shows that what is wanted cannot be realised, or only at a price
not worth paying: then a thread is opened in the intent, citing the
challenge, and what is wanted is decided there. A challenge may
inspire, but nothing enters the intent because a reviewer wrote it,
only because the principal composed it, and an accepted challenge
may change the intent by subtraction as readily as by addition.

## One contract per kind, a Lens per file

Each kind has one contract, a skill written once and preloaded into
every agent of that kind. The contract owns what every lens,
persona or check of its kind shares: conduct and isolation, the
subject and its boundary, the way of working and the shape of the
report. An agent file, `critic-<lens>`, `challenger-<persona>` or
`check-<name>`, carries only its Lens section: what it reads, what
it goes after, its categories and its own report sections.

A Lens is a specialisation of its contract, never a replacement.
It may narrow what is read or make a shared rule stricter; it may
never rename, drop or duplicate a shared rule or field. The
protocol changes in the contract alone, and the contract never
names a lens.

There is one contract per kind and no common one above them,
because the shared texts of the three kinds differ almost whole;
the few sentences common to all are kept in each contract in its
own words, and a common contract is reopened only if a fourth kind
repeats them. New lenses, personas and checks are made from the
skeletons in `templates/` only by the principal's decision, and
only where what they find genuinely differs: personas that would
say the same things in different words are noise.

## Isolation is not independence

Isolation protects a reviewer from the conversation, not from the
author's priors. The author, the critic and the challengers share
one model family. What that family systematically cannot see, none
of them will find, and agreement between the reviewers is therefore
never treated as validation: it means only that the artefact is
consistent under one set of priors.

The calibration point lies outside the forge: review by humans or
by a different model family, invited at the principal's discretion.
Human review of the forge by experienced practitioners has taken
place and shaped it through the ordinary door, like any other
input. Challengers on a different model family are a decided
direction, not a built mechanism; their mechanics are designed
when taken up.

## What never enters a report

A report is a public file, or may be quoted into one. Instance
facts, whatever the local instance file and the assistant's memory
carry (names, roles, addresses, hosts), never enter a reviewer's
report, not even where they would explain a finding.

## See also

- [About the critic](the-critic.md): what the critic judges.
- [About the challenger](the-challenger.md): what the challenger judges.
- [About the check](the-check.md): what a check verifies.
- [Walk through a list](../use/walk-through-a-list.md): how findings are settled.
