---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 52bc5cf0cb2d4086
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

The isolated reviewers are three kinds of reviewer that look at a
project's documents without ever seeing the conversation in which
those documents were made. This page explains what they share, how a
review runs from the call to the filed report, and why they are built
this way. It also explains what the agreement of several reviewers
means and what it does not mean. It is written for anyone who uses
the reviewers, extends them or weighs whether to trust them.

## What it is

The forge has three kinds of reviewer, all of one shape:

- [The critic](the-critic.md): judges the quality of the documents,
  never the substance. Its results are findings (`FND`).
- [The challenger](the-challenger.md): judges the substance of the
  thinking, never the quality of the documents. Its results are
  challenges (`CHL`).
- [The check](the-check.md): verifies mechanical conformance with the
  conventions, never substance or quality. Its results are findings
  (`FND`).

Each reviewer runs as an isolated subagent. A subagent is a separate
run of Claude, started for one job, with a context of its own. The
reviewer reads the project's documents and the engine's rules. It
never sees the working conversation between the principal and Claude.
The principal is the person whose thinking is being forged, and the
final authority on all content.

That blindness is the source of the reviewers' value.

## How it works

### What every isolated subagent holds to

Every isolated subagent of the forge sees nothing of the conversation,
reads every input from disk in its own run, and lets no instance fact
into what it returns. This holds for a reviewer, and equally for the
other isolated agents of the forge: the agent that makes a render, the
documentation agents and the research agent. Those other agents are
not reviewers.

An instance is one installation of the forge. Its instance facts are
what the instance file `CLAUDE.local.md` and the assistant's memory
carry: names, roles, addresses, hosts.

The subagent reads its inputs from disk. This is because the copy of
the core file (`CLAUDE.md`) that it carries in its context may be
older than the file on disk.

A challenger may also search the web.

### The model

Every reviewer runs on the session model. A session is one working
conversation with Claude, and the session model is the model that
conversation runs on. The whole forge runs on one model. Speed is
bought with context, never with a weaker reviewer.

### From the call to the filed report

1. The principal calls a reviewer by hand: `/critique`, `/challenge`
   or `/check`. No reviewer runs on Claude's own judgement. What a
   save and a release run is said by those commands.
2. The reviewer reads what it needs from disk and does its one job.
3. The reviewer returns its report with its findings unnumbered. It
   writes nothing itself.
4. The command gives the findings their IDs and files the report,
   one report at a time. A check that finds nothing files nothing.
5. The report is immutable and dated. Its name carries the date, the
   time to the minute and four hex characters of a content hash, in
   the shape `YYYY-MM-DD-<kind>-<name>-HHMM-<hash>.md`.
6. The findings are settled by walkthrough: one item at a time, each
   with a verdict from the principal. How that runs is described in
   [Walk through a list](../use/walk-through-a-list.md).

Every finding and challenge ends either fixed or rejected with a
recorded reason. Rejecting and parking are legitimate outcomes.
Silently ignoring one is not. An accepted challenge is mended
wherever it needs to be. A challenge that mends nothing was not
accepted.

Nothing blocks. There are no hard quality gates. Findings and
challenges are advisory, and the principal alone decides what is
published.

### One contract per kind

The shared behaviour of each kind of reviewer is written once, in one
contract. The contract covers conduct and isolation, the subject and
its boundary, the way of working and the shape of the report. Each
member of a kind (a lens of the critic, a persona of the challenger,
a check) has an agent file of its own. That file owns only its Lens:
what it reads, what it goes after, its categories and its own report
sections.

A Lens is a specialisation of its contract, never a replacement. It
may narrow what is read. It may make a shared rule stricter. It never
renames, drops or duplicates a shared rule. The protocol changes in
the contract alone.

New members of a kind come only by the principal's decision. They
come only where what they find genuinely differs from what the
existing members find.

### No instance fact in a report

Instance facts never enter a reviewer's report. This holds even where
an instance fact would explain a finding. The reason is that a report
is a public file, or may be quoted into one.

## Why

**Why the reviewers are blind to the conversation.** A reviewer that
never saw the conversation judges only what stands in the documents.
That blindness is the source of its value.

**Why review and challenge are two reviewers.** One agent doing both
does neither properly. The formal audit of a document benefits from a
clean context. The challenge of the substance benefits from a
different register entirely. The check stays apart from both because
it verifies conformance, never substance or document quality.

**Why one contract per kind and not one for all.** The shared texts of
the three kinds differ almost whole. A shared behaviour written once
is never copied, so a change to it is made in one place.

**Why the command numbers and files the report.** A finding without
an ID has no place for its verdict. A rejected finding would then
return at the next run. The IDs of a project's findings and
challenges are given in one place for a further reason: a check that
every save runs would otherwise write into the project at every save.
Two reviewers run at once would otherwise take the same ID. Because
the agent returns its findings unnumbered, reviewers of any kind may
run in parallel.

**Why every report name carries a content hash.** Two branches must
not make the same name. The first report of a day on two branches
would collide, since a save runs a check on every branch. The time
alone is not enough when two people work on one project.

**Why the reviewers are called by hand.** The reason is not recorded.

**When to challenge.** An artefact is best challenged before the next
layer is first derived from it. At that point accepted challenges are
still cheap to absorb. Whether to run a review again later is left to
the judgement of whoever runs the process.

### Isolation is not independence

The author and the reviewers share one model family. What that family
systematically cannot see, none of them will find. So agreement
between the reviewers is never treated as validation. It only means
that the artefact is consistent under one set of priors.

The calibration point lies outside: review by people, or by a model of
a different family, invited at the principal's discretion. The link to
another model family carries research today, and reviewers on it are
not built yet ([Another model family](another-model-family.md)).

A challenge may inspire, but nothing enters a document because a
reviewer wrote it. It enters only because the principal composed it.
An accepted challenge may change the thinking by taking something away
as readily as by adding something.

## A worked example

A principal has a draft intent in a project with the placeholder slug
`<slug>`. Before deriving the first assignment from it, the principal
wants both an isolated look at its wording and a challenge of its
substance. Both reviewers are called by hand and run at the same
time:

```
/critique <lens> intent <slug>
/challenge <persona> intent <slug>
```

```
principal ── calls ──► critic      ── reads from disk ──► 10-intent.md
          ── calls ──► challenger  ── reads from disk ──► 10-intent.md
                          │                 │
                          ▼                 ▼
               report, findings    report, challenges
                  unnumbered          unnumbered
                          │                 │
                          └──► command ◄────┘
                     numbers and files, one report at a time
                          │
                          ▼
   reviews/YYYY-MM-DD-critique-<lens>-HHMM-<hash>.md      (FND)
   challenges/YYYY-MM-DD-challenge-<persona>-HHMM-<hash>.md (CHL)
                          │
                          ▼
            walkthrough: fixed, rejected with a reason, or parked
```

Neither reviewer saw why the principal wrote what he wrote. Each
judged only the file. Because the command gives the IDs one report at
a time, the two parallel runs never take the same number. If both
reports raise nothing serious, that is consistency under one set of
priors, not proof that the intent is sound.

## See also

- [The critic](the-critic.md): what the critic judges.
- [The challenger](the-challenger.md): what the challenger judges.
- [The check](the-check.md): what a check verifies.
- [Another model family](another-model-family.md): the link to a
  model of another family, and why its reviewers are not built yet.
- [Walk through a list](../use/walk-through-a-list.md): how findings
  are settled.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
