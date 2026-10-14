---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: 67d42b18a34945a4
inputs:
  - CLAUDE.md#Isolated reviewers
  - projects/forge/10-intent.md#POS.0400
  - projects/forge/10-intent.md#POS.1120
  - projects/forge/10-intent.md#POS.0430
  - projects/forge/10-intent.md#POS.0440
  - projects/forge/10-intent.md#POS.0450
  - projects/forge/10-intent.md#POS.0540
  - projects/forge/10-intent.md#POS.0790
  - projects/forge/10-intent.md#REJ.0080
---

# The isolated reviewers

An isolated reviewer is an agent that reads a project's documents
and reports on them without ever seeing the conversation in which
those documents were made. This page says what the three kinds of
reviewer of the forge have in common, how a review runs and is
settled, and why the reviewers' isolation is the source of their
value and never a proof that the thinking is right. It is for the
person who orders a review, for the one who adds a lens, a persona
or a check, and for the evaluator who asks what a clean report
means.

## What it is

The forge has three kinds of reviewer, of one shape:

- [The critic](the-critic.md): judges document quality, never
  substance; its results are findings (`FND`).
- [The challenger](the-challenger.md): judges the substance of the
  thinking, never document quality; its results are challenges
  (`CHL`).
- [The check](the-check.md): verifies mechanical conformance with
  the conventions, never substance or quality; its results are
  findings (`FND`).

Each kind has members. The critic has lenses, the challenger has
personas, the check has checks. Each member is one agent file
(`critic-<lens>`, `challenger-<persona>`, `check-<name>`), and the
agent file owns only its Lens section: what the member reads, what
it goes after, its categories and its own report sections. All that
the members of one kind share is written once, in one contract per
kind: a skill the agent file names in its front-matter and that is
preloaded into every member of the kind. The contract owns conduct
and isolation, the subject and its boundary, the way of working, the
shape of the output and the step that writes the ledger. The ledger
is the one file of a project that says its state. Which lenses,
personas and checks exist is the roster of each kind, printed by
the bare command of that kind and listed on the kind's own page.

A reviewer is isolated. It runs as a subagent, that is a separate
run of Claude, launched with a task of its own and with no memory of
the conversation that launched it. It reads the project's documents
and the engine's rules. It carries what every subagent carries:
the engine's `CLAUDE.md` and the instance file `CLAUDE.local.md`,
where an instance is one installation of the forge. A challenger may
also search the web. It never sees the working conversation.

A reviewer runs on the session model. A session is one sitting of
the conversation between the principal and Claude, and the principal
is the person whose thinking is forged. The whole forge runs on one
model. Speed is bought with context, never with a weaker reviewer.

## How it works

Every reviewer is invoked by hand:

- `/critique <lens> [artefact] [slug]` runs one lens of the critic.
- `/challenge <persona> [artefact] [slug]` runs one persona of the
  challenger.
- `/check <check> [slug]` runs one check.

The critic and the challenger take an optional target. The target is
an artefact, that is a document of the chain, named as the state map
of `/forge` names it, by its definition: `brief`, `intent`,
`assignment` and the later layers as they come. Without a target the
whole chain is reviewed. So that one file or one transition can be
reviewed alone. A check takes a project by its slug, or the engine.

No reviewer runs on Claude's own judgement. What a save and a
release run is defined by those two commands, and the composition of
checks is the caller's. Checks never call each other.

Each run produces one report. The report is immutable and dated:

- a critique lands in `reviews/YYYY-MM-DD-critique-<lens>.md`;
- a challenge lands in
  `challenges/YYYY-MM-DD-challenge-<persona>.md`;
- a check lands in `reviews/YYYY-MM-DD-check-<name>.md`, filed by
  the command from what the agent returns; a run that finds nothing
  files nothing.

Each finding and each challenge also gets a row in the ledger. The
report is a public file, or may be quoted into one. Instance facts
never enter it: names, roles, addresses and hosts, whatever the
instance file and the assistant's memory carry, stay out even where
they would explain a finding.

Nothing blocks. There are no hard quality gates. A report informs,
and the principal alone decides what is published.

A report is settled by walkthrough: the items are worked one per
message, in order of weight, each closed with a verdict, and the
verdicts are written once at the end of the round ([Walk through a
list](../use/walk-through-a-list.md)). Every finding and every
challenge is either fixed or explicitly rejected with a recorded
reason, a decision record (`DEC`). Rejecting and parking are
legitimate outcomes. Silently ignoring is not. The states in the
ledger carry the words of the verdicts. The state `open` means not
yet judged. The state `resolved` is the critic's, a fix that is in
the document.

An accepted challenge is mended wherever it needs to be. A challenge
that mends nothing was not accepted. A challenge of a layer below
the intent is mended in that layer and changes nothing above it.
Unless it shows that what is wanted cannot be realised, or only at
a price not worth paying: then a thread is opened in the intent,
citing the challenge, and what is wanted is decided there. Nothing
enters the intent because a reviewer wrote it. It enters only
because the principal composed it. A challenge may inspire, and an
accepted challenge may change the intent by subtraction as readily
as by addition.

An artefact is best challenged before the next layer is first
derived from it: the intent before the first assignment. Because
accepted challenges are still cheap to absorb then. Whether a review
runs again later, after a draft or before an approval, is left to
the judgement of whoever is running the process. No rule prescribes
it.

A new lens, a new persona or a new check is added only by the
principal's decision, and only where what it finds genuinely differs
from what the existing members find. The reason for the second
condition is not recorded. The new member is a specialisation of its
contract, never a replacement. It may narrow what is read or make a
shared rule stricter. It never renames, drops or duplicates a shared
rule or field. The protocol changes in the contract alone. The
contract never names a member. It is addressed to every member of
its kind, never a template with placeholders.

## Why

The reviewers are isolated because their blindness is the source of
their value. The formal audit of a document benefits from a clean
context.

Document review and substantive challenge are two reviewers and not
one, because an agent that does both does neither properly. The
formal audit wants a clean context. The substantive challenge wants
a different register entirely.

Mechanical conformance runs on the same mechanism as the critic and
the challenger: its own contract, one agent per check, a roster, a
run by hand. Because the mechanism takes further kinds as they
come. Whether a check is called a review is not decided, and it does
not matter to the mechanism. A check is read-only and advisory. It
reports and proposes, and the principal decides what is fixed.
Conformance is never substance or document quality, which remain the
critic's and the challenger's territory.

Each kind has one contract of its own and there is no common
contract above the three. Because the shared texts of the kinds
differ almost whole. The few sentences common to all stay in each
contract in its own words. A common contract is reopened only if a
fourth kind repeats them. The contract is written once, never a
copy, so that the protocol of a kind changes in one place.

Every reviewer runs on the session model because speed is bought
with context, never with a weaker reviewer.

Nothing blocks because findings and checklists are advisory and the
principal alone decides what is published.

Isolation is not independence. The author, the critic and the
challengers share one model family. What that family systematically
cannot see, none of them will find. Agreement between the reviewers
is therefore never treated as validation. It only means that the
artefact is consistent under one set of priors. The calibration
point lies outside the forge: review by humans, or by a different
model family, invited at the principal's discretion. Challengers on
a different model family are planned and not built.

Instance facts never enter a report because a report is a public
file, or may be quoted into one.

## A worked example

A project with the slug `<slug>` has an intent at version 0.3, and
the principal is about to derive the first assignment from it. This
is the moment a challenge is cheapest, so the principal types
`/challenge <persona> intent <slug>`.

Claude launches the challenger as a subagent. The subagent carries
the contract of the challenger and the Lens of `<persona>`, reads
the intent and the other documents of `<slug>` and the engine's
rules, and may search the web. It knows nothing of what the
principal and Claude said while the intent was drafted. It returns
its challenges, and the command files them as
`challenges/YYYY-MM-DD-challenge-<persona>.md`, one row per
challenge in the ledger, each in the state `open`. Claude offers a
walkthrough.

The walkthrough runs one challenge per message. The first is
accepted: the intent is mended where the challenge bites. The second
is rejected: the principal gives his reason and a decision record
keeps it. The third is parked. The ledger now carries the three
verdicts, and no challenge was ignored in silence.

Later the principal saves the project. The save runs its check. The
check reads the files of `<slug>` against the conventions, finds
nothing and files nothing. The challenger found nothing it could
not settle, and the check found nothing at all. That tells the
principal the intent is consistent under one set of priors. It does
not tell him the intent is right. For that he hands the intent to a
colleague to read.

## See also

- [The critic](the-critic.md): what the critic judges.
- [The challenger](the-challenger.md): what the challenger judges.
- [The check](the-check.md): what a check verifies.
- [Walk through a list](../use/walk-through-a-list.md): how findings
  are settled.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-14 for version 5.9 from the files the
front-matter names; never edited by hand.
