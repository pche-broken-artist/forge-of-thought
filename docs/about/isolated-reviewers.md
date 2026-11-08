---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: ef8f265763af2533
inputs:
  - CLAUDE.md#Isolated reviewers
  - projects/forge/10-intent.md#POS.0400
  - projects/forge/10-intent.md#POS.1120
  - projects/forge/10-intent.md#POS.1140
  - projects/forge/10-intent.md#POS.1720
  - projects/forge/10-intent.md#POS.0430
  - projects/forge/10-intent.md#POS.0440
  - projects/forge/10-intent.md#POS.0450
  - projects/forge/10-intent.md#POS.0540
  - projects/forge/10-intent.md#POS.0790
  - projects/forge/10-intent.md#POS.0930
  - projects/forge/10-intent.md#REJ.0080
---

# The isolated reviewers

The isolated reviewers are the three kinds of reviewer the forge
has: the critic, the challenger and the check. Each runs as an
isolated subagent (a separate run of Claude, given one task and
returning one result) that reads the project's documents from disk
and never sees the working conversation. This page explains, for the
user, the extender and the evaluator, why the reviewers are blind to
the conversation, how a run becomes a filed report, and what it
means when two reviewers agree.

## What it is

Three kinds of reviewer share one shape and do strictly separate
jobs, each with an output of its own:

- the critic judges the quality of the documents and never their
  substance; its results are findings (`FND`), filed in `reviews/`
  ([The critic](the-critic.md));
- the challenger judges the substance of the thinking and never the
  quality of the documents; its results are challenges (`CHL`),
  filed in `challenges/` ([The challenger](the-challenger.md));
- the check verifies mechanical conformance with the conventions and
  never substance or quality; its results are findings (`FND`),
  filed in `reviews/` ([The check](the-check.md)).

Each kind has members. The critic has lenses, the challenger has
personas, the check has checks. Each member is one agent file. The
shared behaviour of a kind is written once, in one contract skill
for that kind, and the agent file names its contract and owns only
its Lens section. A contract owns conduct and isolation, the subject
and its boundary, the way of working and the shape of the report. A
Lens is a specialisation of its contract and never a replacement: it
may narrow what is read or make a shared rule stricter. It never
renames, drops or duplicates a shared rule or field. The protocol
changes in the contract alone. New lenses, personas and checks come
only by the decision of the principal (the person whose thinking is
being forged), and only where what they would find genuinely
differs.

All three run on the session model, that is the model the working
conversation itself runs on. All three are blind to that
conversation, and their blindness is the source of their value.

One sentence holds for every isolated subagent of the forge, a
reviewer, a renderer, a documentation agent or a research agent
alike: it sees nothing of the conversation, it reads every input
from disk in its own run, and it lets no instance fact into what it
returns. Only the critic, the challenger and the check are
reviewers. A renderer, a documentation agent and a research agent
are isolated in the same way, and they review nothing.

## How it works

A reviewer runs on the principal's word alone. The word is given by
hand, through `/critique <lens> [artefact]`,
`/challenge <persona> [artefact]` or `/check <check> [slug]`. The
word may also be given once, in the definition of a command that
names the checks it runs; a save and a release have such a
definition. What is ruled out is a run on Claude's own judgement.
Bare `/critique`, `/challenge` and `/check` list their roster and
recommend a fit.

The critic and the challenger take an optional target: an artefact
of the chain, named as `/forge` names it, or any file of the project
named by its path. A file named by its path is read with the chain
around it, and a work product with its specification. Without a
target, the whole chain is reviewed. Where the file gives the lens
or the persona nothing to work on, the report says so and carries
nothing else. A check takes a project by its slug, or the engine.

In its run, a reviewer reads the project's documents and the
engine's rules from disk. It carries what every subagent carries,
the core file and the instance file, and nothing of the
conversation. A challenger may search the web. Every check executes
its own definition in an isolated subagent that sees only the files.

The reviewer returns its report with its findings unnumbered and
writes nothing. The command numbers the findings and files the
report, one report at a time. The report is immutable and dated. Its
name is its date, the time to the minute and four hex characters of
a content hash, `YYYY-MM-DD-<kind>-<name>-HHMM-<hash>.md`; the name
is completed by `scripts/forge-report.py` for every report alike. A
check that finds nothing files nothing. Instance facts, that is
whatever the instance file and Claude's memory carry (names, roles,
addresses, hosts), never enter a report, not even where they would
explain a finding.

A filed report is settled by walkthrough (a list worked one item per
message, each item closed with the principal's verdict), as
[Walk through a list](../use/walk-through-a-list.md) describes.
Every finding and every challenge is either fixed or explicitly
rejected with a recorded reason. Rejecting and parking are
legitimate outcomes. Silently ignoring one is not. An accepted
challenge is mended wherever it needs to be, and one that mends
nothing was not accepted. A challenge of a layer below the intent is
mended in that layer and changes nothing above it. The exception is
a challenge that shows that what is wanted cannot be realised, or
only at a price not worth paying: then a thread is opened in the
intent, citing the challenge, and what is wanted is decided there.
The states of findings and challenges are records the ledger (the
project's state report, made at read time from its documents) is
made from.

Nothing blocks. There are no hard quality gates. Findings and
challenges are advisory, and the principal alone decides what is
published.

An artefact is best challenged before the next layer is first
derived from it: the intent before the first assignment, a BRD
before the solution design. At that point accepted challenges are
still cheap to absorb. Whether a review runs again later, after a
draft or before an approval, is left to the judgement of whoever
runs the process; no rule prescribes it.

## Why

**Why the reviewers are blind to the conversation.** The inputs say
that this blindness is the source of their value, and say no more of
it. A clean context is also the reason given for keeping document
review apart from the substantive challenge: the formal audit
benefits from a clean context, and the substantive challenge
benefits from a different register entirely. One agent doing both
would do neither properly. The check runs on the same mechanism as
the two, so that there is one mechanism for every reviewer.

**Why every input is read from disk.** The copy of the core file in
a subagent's context may be older than the file on disk. A reviewer
therefore reads every input in its own run, and trusts nothing that
was loaded for it.

**Why no instance fact reaches a report.** A report is a public file,
or may be quoted into one. A name, a role, an address or a host in
it would make the instance visible wherever the report travels.

**Why the session model.** The whole forge runs on one model, so
that the strongest model the forge runs on is a decision and never
the accident of a pin that has aged. Speed is bought with context,
never with a weaker reviewer: the reviewer reads in its own context
and the working conversation is spent on verdicts, not on reading.

**Why a reviewer runs on the principal's word alone.** A run costs
tokens, some checks a great deal, and what is spent is the
principal's to decide. There is no other reason. The word may stand
once in a command's definition, so that a save or a release can run
its checks without a fresh word each time; a run on Claude's own
judgement is what is ruled out.

**Why the command numbers and files the report.** A finding without
an ID has no place for its verdict. A rejected finding without an ID
returns at the next run, and nobody can tell why one reviewer's
findings are kept and another's are not. The IDs of a project's
findings and challenges are given in one place, the session, never
by the agent. A check that every save runs would otherwise write
into the project at every save. Two reviewers run at once would
otherwise take one ID. Because the agent returns its findings
unnumbered and the command numbers them one report at a time,
reviewers of any kind may run in parallel.

**Why a report's name carries the minute and a hash.** Two branches
must not make the same name. The first report of a day on two
branches would, since the check a save runs happens on every branch,
and the time alone is not enough for two people. Names given before
the rule stay as they are, immutable.

**Why one contract per kind.** The shared behaviour of a kind is
written once and never copied, so that a change of the protocol is
made in one place. There is one contract per kind and no common one,
because the shared texts of the kinds differ almost whole; the few
sentences common to all stay in each contract in its own words.

**Why nothing blocks.** Findings are advisory, and the principal
alone decides what is published. No further reason is recorded.

**Why the reports are immutable and dated.** The reason is not
recorded in the inputs of this page.

**Why agreement is not validation.** Isolation is not independence.
The author, the critic and the challengers share one model family.
What that family systematically cannot see, none of them will find.
Agreement between the reviewers is therefore never treated as
validation: it only means that the artefact is consistent under one
set of priors. The calibration point lies outside, in review by
people or by a model of another family, invited at the principal's
discretion; how another family is reached is said in
[Another model family](another-model-family.md). Where several
engines answer one question, Claude lays the answers side by side
with the engines named, and the principal is the chairman: agreement
is consistency, difference is spelled out. A challenge may inspire,
but nothing enters the intent because a reviewer wrote it; it enters
only because the principal composed it. An accepted challenge may
change the intent by subtraction as readily as by addition.

## A worked example

The principal of a project `my-project` has just spent an hour with
Claude arguing an intent towards its next version. Before the first
assignment is derived from it, the principal asks for a challenge:
`/challenge <persona> intent my-project`.

A subagent starts with the persona's agent file and the challenger's
contract. It reads the intent and the chain around it from disk. It
knows nothing of the hour before: not what the principal almost
wrote, not what Claude proposed and was declined. It may search the
web. It returns its challenges unnumbered, severity and epistemic
status with each, and writes nothing.

The command numbers the challenges, `CHL.0010` onwards in the
project's one sequence, and files the report in `challenges/` as
`YYYY-MM-DD-challenge-<persona>-HHMM-<hash>.md`. The report is now
immutable. The same minute, a critic lens the principal started in
parallel returns its findings; they take `FND` numbers of their own,
and the two reports never collide.

Claude offers a walkthrough. One challenge per message, the heaviest
first: the principal accepts two and the intent is mended where it
needs to be; one is rejected with the reason recorded in the
project's decisions; one is parked. The ledger shows each challenge
in the state its verdict gave it. Nothing was blocked, and nothing
was written into the intent because the challenger said so.

A week later a second persona is sent in and raises no objection
where the first one did. That is consistency under one set of
priors, not proof that the intent is right. If the principal wants
calibration, the way is a reader of flesh and blood or a model of
another family.

## See also

- [The critic](the-critic.md): what the critic judges.
- [The challenger](the-challenger.md): what the challenger judges.
- [The check](the-check.md): what a check verifies.
- [Another model family](another-model-family.md): the link to a
  model of another family, and why its reviewers are not built yet.
- [Walk through a list](../use/walk-through-a-list.md): how findings
  are settled.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 7.0 from the files the
front-matter names; never edited by hand.
