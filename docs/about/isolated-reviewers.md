---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: fc0277c2f2e55331
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
  - projects/forge/10-intent.md#REJ.0080
---

# The isolated reviewers

The isolated reviewers are the three kinds of reviewer of the forge:
the critic, the challenger and the check. Each one reads a project's
documents in a run of its own, without ever seeing the conversation
in which they were written. This page explains what the three have
in common, how a review runs from the call to the settled result,
and why it is built so. It is for anyone who uses the reviewers, who
adds a new one, or who wants to judge what a review can and cannot
prove.

## What it is

There are three kinds of reviewer, with strictly separate jobs:

- [The critic](the-critic.md): the quality of a document, never its
  substance. Its results are findings (`FND`).
- [The challenger](the-challenger.md): the substance of the
  thinking, never the quality of the document. Its results are
  challenges (`CHL`).
- [The check](the-check.md): mechanical conformance with the
  conventions, never substance or quality. Its results are findings
  (`FND`).

All three share one shape. Each runs as an isolated subagent (a
separate run of Claude, started for one job, that sees nothing but
what it reads from disk). It reads the project's documents and the
engine's rules. It never sees the working conversation between
Claude and the principal (the person whose thinking is being
forged). A challenger may also search the web.

Every reviewer runs on the session model. The session is the one
running conversation with Claude, and its model is the one every
reviewer inherits, because the whole forge runs on one model.

The challenger works through personas, the critic through lenses and
the check through checks. Each persona, lens or check is one agent
file. The behaviour shared by all members of one kind is written
once, in one contract for that kind. The agent file carries only its
own Lens section: what it reads and what it goes after. Terms such
as artefact, chain and finding are defined in one line each in the
[Glossary](../reference/glossary.md).

## How it works

A review always starts by hand. The principal calls it with
`/critique`, `/challenge` or `/check`. No reviewer runs on Claude's
own judgement. Where a save or a release runs a check, that is said
by the save and the release, not by the reviewer.

The critic and the challenger take an optional target: one artefact
of the chain, or any file of the project by its path. Without a
target they read the whole chain. A check takes a project by its
slug, or the engine.

The agent does not write anything. It returns its report to the
command, with its findings or challenges unnumbered. The command
then does three things, one report at a time:

1. It gives each finding or challenge its ID.
2. It names the report by its date, the time to the minute and four
   hex characters of a hash of its content, in the form
   `YYYY-MM-DD-<kind>-<name>-HHMM-<hash>.md`. The script
   `scripts/forge-report.py` completes the name.
3. It files the report: a critique or a check in `reviews/`, a
   challenge in `challenges/`.

A check that finds nothing files nothing.

Once filed, a report is immutable: it is never edited.

The principal then settles the report by walkthrough. A walkthrough
takes the items one per message, in order of weight, each closed
with a verdict (see [Walk through a list](../use/walk-through-a-list.md)).
Every finding and challenge ends either fixed or rejected with a
recorded reason in a decision. Rejecting and parking are legitimate
outcomes. Ignoring an item in silence is not. An accepted challenge
is mended wherever it needs to be. A challenge that mends nothing was
not accepted.

Nothing a reviewer says blocks anything. There are no hard quality
gates. Findings and challenges are advice, and the principal alone
decides what is published.

Instance facts never enter a report. These are the facts of one
installation: names, roles, addresses, hosts. They stay out even
where they would explain a finding.

## Why

**Why blind.** The reviewers never see the conversation, and that
blindness is the source of their value. Beyond that statement, how
the blindness adds value is not recorded.

**Why the session model.** Speed is bought with context, never with
a weaker reviewer.

**Why three kinds and not one.** An agent doing both document review
and substantive challenge does neither properly. The formal audit
benefits from a clean context. The substantive challenge benefits
from a different register entirely. The check stays out of both
territories: it checks conformance, and substance and quality remain
the work of the critic and the challenger. The check runs on the
same mechanism as the other two, so that there is one mechanism for
every reviewer.

**Why one contract per kind.** Shared behaviour is written once,
never copied. A lens is a specialisation of its contract, never a
replacement. It may narrow what is read or make a shared rule
stricter. It never renames, drops or duplicates a shared rule. The
protocol changes in the contract alone. There is one contract per
kind rather than one for all, because the shared texts of the kinds
differ almost whole.

**Why the command numbers and files.** The IDs of a project's
findings and challenges are given in one place. Two reviewers run at
once would otherwise take the same ID. A check that every save runs
would otherwise write into the project at every save. Because the
agent returns its findings unnumbered, reviewers of any kind may run
in parallel. A finding needs an ID so that its verdict has a place.
Without one, a rejected finding would return at the next run.

**Why the name carries the time and a hash.** Two branches must not
make the same name. The first report of a day on two branches would
collide, since every save runs a check on whatever branch it is on.
The time alone is not enough when two people work on one project.

**Why by hand, and why immutable.** The reason a reviewer is never
started on Claude's own judgement is not recorded. The reason a
report is immutable is not recorded either.

**Why nothing blocks.** The principal alone decides what is
published, so a finding informs and never stops.

**Why no instance facts.** A report is a public file, or may be
quoted into one.

**When to challenge.** An artefact is best challenged before the
next layer is first derived from it. At that point accepted
challenges are still cheap to absorb. Whether to run again later is
left to the judgement of whoever runs the process.

### Isolation is not independence

The author, the critic, the challenger and the check share one model
family. What that family systematically cannot see, none of them
will find. Agreement between the reviewers is therefore never
treated as validation. It only means the artefact is consistent
under one set of priors.

The calibration point lies outside, in review by people or by a
model of a different family, invited at the principal's discretion;
how such a model is reached is told on
[Another model family](another-model-family.md).

A challenge may inspire, but nothing enters the intent because a
reviewer wrote it. It enters only because the principal composed it.
An accepted challenge may change the intent by taking something away
as readily as by adding.

## A worked example

A principal works on a project, here `example-project`, and wants
the substance of its intent questioned before the next layer is
drawn from it. He calls a challenger persona on the intent:

```
/challenge <persona> intent example-project
```

Claude starts the persona's agent as an isolated subagent. The agent
reads the intent and the chain around it from disk, and nothing of
the conversation. It returns a report holding, say, four challenges,
none of them numbered.

The command gives the four challenges their IDs (`CHL.NNNN`, the
next free numbers of the project) and files the report under a name
such as:

```
challenges/2026-01-15-challenge-<persona>-1430-a3f9.md
```

The time and the hash of the content in that name keep it apart from
a report made the same day on another branch.

The principal walks through the four challenges one by one. He
accepts one, and the intent is mended. He rejects one, and the
reason is recorded in a decision. He parks one. He asks a question
on the last before judging it. None of the four blocks anything.

If a second challenger agrees with the first, that agreement says
the intent is consistent under one model family's priors. It does
not say the intent is right.

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

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
