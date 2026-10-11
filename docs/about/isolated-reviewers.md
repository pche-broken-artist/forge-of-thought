---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 6e9ab442c0f09d93
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

The isolated reviewers are three kinds of agent that read a project's
documents and report on them without ever seeing the conversation in
which those documents were made: the critic, the challenger and the
check. This page explains what the three kinds share, how a run of one
of them goes from the command to a settled report, and why their
blindness is deliberate and their agreement is not proof. It is for
the user who runs them, for the extender who adds a lens, a persona or
a check, and for the evaluator who wants to know what a clean report
does and does not mean. What each kind judges has a page of its own:
[The critic](the-critic.md), [The challenger](the-challenger.md) and
[The check](the-check.md). The terms of the forge are gathered in the
[Glossary](../reference/glossary.md).

## What it is

Three kinds of reviewer exist, each with one job and one output:

- the critic judges document quality and never substance; it has
  lenses, and it produces findings (`FND`) in `reviews/`
- the challenger judges the substance of the thinking and never
  document quality; it has personas, and it produces challenges
  (`CHL`) in `challenges/`
- the check verifies mechanical conformance with the conventions and
  never substance or quality; it has checks, each owning one concern
  and none another's, and it produces findings (`FND`) in `reviews/`

The three have one shape. Each runs as an isolated subagent, that is,
a separate run of Claude with a brief of its own. A reviewer reads
the project's documents and the engine's rules. It carries what every
subagent carries, the engine's core instructions and the instance
file. A challenger may also search the web. No reviewer sees the
working conversation, the exchange between the principal and Claude
in which the documents are composed. The principal is the person
whose thinking is being forged, the final authority on all content.

Every reviewer runs on the session model, that is, the model the
conversation itself runs on. The whole forge runs on one model.
Speed is bought with context, never with a weaker reviewer.

Every reviewer is invoked by hand. No reviewer runs on Claude's own
judgement. The critic and the challenger never run at a save. A
release offers the critic's `essence` lens once and runs no reviewer
on its own. Which checks a save and a release run is said by the
definitions of those two commands.

Every report is immutable and dated. The reports are settled by
walkthrough, the method by which a list of items is worked one item
per message and each item closed with the principal's verdict; see
[Walk through a list](../use/walk-through-a-list.md). Nothing blocks.
The findings and challenges are advisory, and the principal alone
decides what is published.

## How it works

### The command and the target

The critic is run with `/critique <lens> [artefact]`, the challenger
with `/challenge <persona> [artefact]`, the check with
`/check <check> [slug]`. Bare `/critique`, `/challenge` and `/check`
list the roster of their kind, taken from the `description` of each
agent file, and recommend a fit.

The critic and the challenger take an optional target: one artefact
of the chain, named as `/forge` names it, by its definition. Without
a target they read the whole chain. So one file or one transition
can be reviewed alone. A check takes a project by its slug, or the
engine.

### One contract per kind, one Lens per member

Each lens, persona and check is one agent file: `critic-<lens>`,
`challenger-<persona>`, `check-<name>`. The shared behaviour of a
kind is written once, in one contract skill, and preloaded into every
agent file of that kind; the agent's front-matter names its contract.
The agent file owns only its Lens section: what it reads, what it
goes after, its categories and its own report sections. The contract
owns conduct and isolation, the subject and its boundary, the way of
working, the shape of the output and the ledger step. The contract is
addressed to every lens of its kind and is never a template with
placeholders. The contract never names a lens; the lens file does.

A Lens is a specialisation of its contract, never a replacement. It
may narrow what is read. It may make a shared rule stricter. It may
never rename, drop or duplicate a shared rule or a field. The
protocol changes in the contract alone. A new lens, persona or check
is made by the skeleton of its kind in `templates/`, only by the
principal's decision, and only where what it would find genuinely
differs from what the existing ones find.

### What reaches the report

A report is a public file, or may be quoted into one. So instance
facts never enter it: names, roles, addresses, hosts, whatever the
instance file or Claude's memory carry, not even where they would
explain a finding.

A challenger's report has a fixed discipline, owned by its contract:
a severity for each challenge, an epistemic status, and a ban on
fabrication. What a lens reads and goes after is its own.

### Where the output lands

The critic files its findings as `reviews/YYYY-MM-DD-critique-<lens>.md`.
The challenger files its challenges as
`challenges/YYYY-MM-DD-challenge-<persona>.md`. The check returns its
report to the command, which files it as
`reviews/YYYY-MM-DD-check-<name>.md`; a check run that finds nothing
files nothing. Checks never call each other; which checks run
together is decided by the command that calls them, `/save` or
`/release`. Each run also adds rows to the ledger, the one file that
holds the project's state. The states of findings and challenges are
those the ledger template defines, and they carry the words of the
verdicts: `open` is a state only, not yet judged; `resolved` is the
critic's state for a fix that is in the document.

### Settling

Every finding and every challenge is either fixed or explicitly
rejected, with the reason recorded as a decision (`DEC`). Rejecting
and parking are legitimate outcomes. Silently ignoring is not.

An accepted challenge is mended wherever it needs to be. A challenge
that mends nothing was not accepted. A challenge of a layer below the
intent is mended in that layer and changes nothing above it. Unless
it shows that what is wanted cannot be realised, or only at a price
not worth paying: then a thread is opened in the intent, citing the
challenge, and what is wanted is decided there.

A challenge may inspire. Nothing enters the intent because a
reviewer wrote it, only because the principal composed it. An
accepted challenge may change the intent by subtraction as readily as
by addition.

### When to run a reviewer

An artefact is best challenged before the next layer is first derived
from it, the intent before the first assignment, because accepted
challenges are still cheap to absorb then. Whether a reviewer runs
again later, after a draft or before an approval, is left to the
judgement of whoever is running the process. No rule prescribes it.

## Why

**Why the reviewers are blind to the conversation.** That blindness
is the source of their value. The formal audit benefits from a clean
context. A longer argument than this is not recorded.

**Why there are three kinds and not one.** Merging document review
and substantive challenge into one reviewer was rejected. An agent
doing both does neither properly. The formal audit benefits from a
clean context, while the substantive challenge benefits from a
different register entirely. Mechanical conformance runs on the same
mechanism as the other two kinds: its own contract, one agent per
check, a roster and a run by hand. The mechanism takes further kinds
as they come. Whether a check is called a review is not decided and
does not matter to the mechanism. The check reports and proposes;
substance and quality stay the territory of the critic and the
challenger.

**Why one contract per kind, and no contract common to all.** Shared
behaviour is written once and never copied; the reason beyond the
rule itself is not recorded. The shared texts of the three kinds
differ almost whole, so each kind has a contract of its own and the
few sentences common to all stay in each contract in its own words.
A common contract would be reopened only if a fourth kind repeated
them.

**Why every reviewer runs on the session model.** Speed is bought
with context, never with a weaker reviewer. The whole forge runs on
one model.

**Why nothing blocks.** There are no hard quality gates because the
principal alone decides what is published. The reviewers inform that
decision; they do not take it.

**Why every finding is fixed or rejected with a reason.** Rejecting
and parking are legitimate; silently ignoring is not. The inputs
state the rule; a reason beyond it is not recorded.

**Why isolation is not independence.** The author, the critic and
the challengers share one model family. What that family
systematically cannot see, none of them will find. Agreement between
the reviewers is therefore never treated as validation. It only means
the artefact is consistent under one set of priors. The calibration
point lies outside: review by humans, or by a different model family,
invited at the principal's discretion. Challengers running on a
different model family are a planned direction and not part of the
forge today. External review by experienced practitioners has shaped
the forge already, through the ordinary door of the intent, like any
other input.

**Why instance facts never enter a report.** A report is a public
file, or may be quoted into one.

## A worked example

A thought project with the slug `my-project` has its intent at a
draft version, and the principal wants it read before the first
assignment is derived from it.

The principal types `/critique <lens> intent`. Claude starts the
critic for that lens as a subagent. The subagent reads the intent of
`my-project` and the engine's rules; it sees nothing of the
conversation in which the intent was drafted. It returns its report.
Claude files it as `reviews/YYYY-MM-DD-critique-<lens>.md` and adds
one row per finding to the ledger, each in the state `open`. The
report will never be edited again.

Claude offers a walkthrough. The principal takes the findings one
per message. One finding is fixed in the intent and its row becomes
`resolved`. One is rejected, with the reason recorded as a decision
(`DEC`), and its row says so. One is parked. None is left without a
verdict.

The principal then types `/challenge <persona> intent`. The
challenger reads the same intent, blind in the same way, and returns
its challenges in `challenges/YYYY-MM-DD-challenge-<persona>.md`,
each with a severity and an epistemic status. In the walkthrough one
challenge is accepted. The intent is mended where the challenge
showed the gap; a position is struck out rather than added, which is
as legitimate as an addition. The wording of the mend is the
principal's own, not the challenger's.

That both reviewers found the intent coherent says that it is
consistent under one set of priors. It does not say that the intent
is right. If the principal wants that question asked, he invites a
human reader or a reviewer of a different model family.

At the next save the checks run as the save's definition says. A
check that finds nothing files nothing; one that finds a convention
broken files `reviews/YYYY-MM-DD-check-<name>.md`, and its findings
are settled the same way.

## See also

- [The critic](the-critic.md): what the critic judges.
- [The challenger](the-challenger.md): what the challenger judges.
- [The check](the-check.md): what a check verifies.
- [Walk through a list](../use/walk-through-a-list.md): how findings
  are settled.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-11 for version 5.3 from the files the
front-matter names; never edited by hand.
