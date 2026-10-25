---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: 7fb097891fe0449f
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

The isolated reviewers are the three kinds of reviewer of Forge of
Thought: the critic, the challenger and the check. They share one
shape, and each runs apart from the conversation in which the work
is done. This page explains what that shape is, how a review runs
from the call to the filed report, and why the reviewers are kept
blind. It also says what it means when the reviewers agree. It is
written for anyone who uses the reviewers, extends them or weighs
what their reports are worth.

## What it is

There are three kinds of reviewer, and each has a job of its own:

- [The critic](the-critic.md): what the critic judges. It looks at
  document quality, never substance.
- [The challenger](the-challenger.md): what the challenger judges.
  It looks at the substance of the thinking, never document quality.
- [The check](the-check.md): what a check verifies. It looks at
  mechanical conformance with the conventions, never substance or
  quality.

Every reviewer runs as an isolated subagent. A subagent is a
separate run of Claude, started by a command, with its own context.
It reads the project's documents and the engine's rules and never
sees the working conversation. A challenger may also search the web.

The principal (the person whose thinking is being forged, and the
final authority on its content) is the one the reviewers serve. They
inform him, and they decide nothing.

What holds for every isolated subagent of the forge holds for the
reviewers too. Every isolated subagent follows three rules:

- It sees nothing of the conversation.
- It reads every input from disk in its own run.
- It lets no instance fact into what it returns.

An instance is one installation of the forge, and its instance facts
are the names, roles, addresses and hosts it carries. These rules
are not only the reviewers'. A renderer, a documentation agent and a
research agent follow them as well, although none of them is a
reviewer.

## How it works

### One shape for three kinds

Each kind of reviewer has one contract. The contract is the shared
behaviour of every member of that kind, written once. Each member of
a kind (a critic lens, a challenger persona, a check) is one agent
file. The agent file owns only its Lens section, that is, what this
member reads and what it goes after. A Lens section may narrow what
is read or make a shared rule stricter. It never renames, drops or
duplicates a shared rule. A change to the protocol is made in the
contract alone.

New members of a kind are added only by the principal's decision.
They are added only where what they find genuinely differs from what
the existing members find.

### The model

Every reviewer runs on the session model, that is, the model the
current conversation with Claude runs on. The whole forge runs on
one model. Speed is bought with context, never with a weaker
reviewer.

### From the call to the filed report

1. The principal calls a reviewer by hand. No reviewer runs on
   Claude's own judgement. What a save and a release run is defined
   by those two commands.
2. The reviewer reads its inputs from disk and does its work, blind
   to the conversation.
3. The reviewer returns its report with its findings unnumbered. It
   writes nothing.
4. The command numbers the findings and files the report, one report
   at a time.
5. The report is immutable and dated from then on.
6. The principal settles the findings in a walkthrough. A
   walkthrough is the forge's way of working a list, one item per
   message, each closed with a verdict. How it runs is said in
   [Walk through a list](../use/walk-through-a-list.md): how
   findings are settled.

A check that finds nothing files nothing.

Every finding and every challenge ends in one of two ways. Either it
is fixed, or it is rejected with a recorded reason. Rejecting and
parking are legitimate outcomes. Silently ignoring is not. An
accepted challenge is mended wherever it needs to be. A challenge
that mends nothing was not accepted.

### The name of a report

Every report is named by its date, the time to the minute and four
hex characters of a content hash:

```
YYYY-MM-DD-<kind>-<name>-HHMM-<hash>.md
```

A critic's report goes into `reviews/`, and so does a check's. A
challenger's report goes into `challenges/`. The name is completed
by `scripts/forge-report.py`.

### Nothing blocks

There are no hard quality gates. Findings and checklists are
advisory. The principal alone decides what is published.

### When to challenge

An artefact is best challenged before the next layer is first
derived from it. One case is the intent before the first assignment.
Another is a business requirements document before the solution
design. Whether a reviewer runs again later is left to the judgement
of whoever runs the process. No rule prescribes it.

### Isolation is not independence

The author, the critic and the challengers share one model family.
What that family systematically cannot see, none of them will find.
Agreement between the reviewers is therefore never treated as
validation. It only means the artefact is consistent under one set
of priors. The calibration point lies outside the forge's own
reviewers: review by people, or by a model of a different family, at
the principal's discretion. How the forge reaches another family,
and why its reviewers on it are not built yet, is said in
[Another model family](another-model-family.md): the link to a model
of another family, and why its reviewers are not built yet.

## Why

The reviewers never see the conversation, because their blindness is
the source of their value.

Every input is read from disk in the reviewer's own run, because the
copy of the core file in its context may be older than the file on
disk.

Instance facts never enter a report, not even where they would
explain a finding. The reason is that a report is a public file, or
may be quoted into one.

Document review and the challenge of substance are two reviewers,
not one. An agent doing both does neither properly. The formal audit
benefits from a clean context. The challenge of substance benefits
from a different register entirely.

The shared behaviour of a kind is one contract and never a copy in
each agent file. There is one contract per kind, because the shared
texts of the kinds differ almost whole.

The command numbers the findings and files the report, never the
agent. The reasons are four:

- A finding without an ID has no place for its verdict, so a
  rejected finding would return at the next run.
- The IDs of a project's findings and challenges are given in one
  place.
- A check that every save runs would otherwise write into the
  project at every save.
- Two reviewers run at once would otherwise take one ID.

Because the command gives the IDs, reviewers of any kind may run in
parallel.

A report name carries the time and a content hash so that two
branches never make the same name. The date alone would not do,
because the first report of a day on two branches would collide. The
time alone is not enough for two people.

Nothing blocks, because the principal alone decides what is
published.

## A worked example

A principal works on a project with the placeholder slug
`my-project`. He asks for one critic lens on the intent, with
`<lens>` standing for the lens he picks:

```
/critique <lens> intent my-project
```

The critic starts as a subagent. It knows nothing of the
conversation that came before. It reads the intent and the engine's
rules from disk and returns a report with three findings, none of
them numbered.

The command gives the three findings the next free numbers of the
project's one sequence of findings. It files the report into
`reviews/` under a name such as:

```
2030-01-15-critique-<lens>-1432-3fa9.md
```

From then on the report is never edited. The principal works the
three findings in a walkthrough. He accepts one, which is fixed in
the intent. He rejects one with a recorded reason. He parks the
third.

Suppose a challenger later finds nothing to add. That means the
intent is consistent under the priors this model family shares. It
does not mean the intent is right. For that, the principal turns to
people, or to a model of another family.

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

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
