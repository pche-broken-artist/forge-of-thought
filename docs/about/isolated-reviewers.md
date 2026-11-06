---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 64a90de1603aff88
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

The isolated reviewers are the three kinds of reviewer the forge has:
the [critic](the-critic.md), the [challenger](the-challenger.md) and
the [check](the-check.md), each run as a subagent (a separate run of
Claude with a context of its own) that reads the project's documents
and never sees the working conversation. This page explains why the
reviewers are blind to the conversation, how a run is started, filed
and settled, and what it means when the reviewers agree. It is for the
principal (the person whose thinking is being forged) who runs them,
for the extender who adds a lens, a persona or a check, and for the
evaluator who wants to know what a report is worth.

## What it is

A reviewer is one of three kinds of agent of one shape, each with a
job the others do not have:

- the critic judges the quality of the documents, never the
  substance, and returns findings
- the challenger judges the substance of the thinking, never the
  quality of the documents, and returns challenges
- the check verifies mechanical conformance with the conventions,
  never substance or quality, and returns findings

All three run as isolated subagents. A reviewer reads the project's
documents and the engine's rules from disk in its own run. It sees
nothing of the conversation in which the principal and Claude have
worked. That blindness is the source of its value.

The same isolation holds for every isolated subagent of the forge,
not only for the reviewers: a renderer, a documentation agent and a
research agent are isolated in the same way, though they are not
reviewers. What holds for each of them is one sentence: it sees
nothing of the conversation, it reads every input from disk in its
own run, and it lets no instance fact into what it returns. It reads
from disk because the copy of the core rules in its context may be
older than the file.

A reviewer runs on the session model. The session is the running
conversation in Claude Code, and the session model is the model that
conversation runs on. The whole forge runs on one model. Speed is
bought with context, never with a weaker reviewer. A challenger may
search the web.

## How it works

### A run starts on the principal's word

Every reviewer is invoked by hand. No reviewer runs on Claude's own
judgement. The word may be given once, in the definition of a command
that names the checks it runs: `/save` and `/release` have it so, and
a check they name runs as part of them. What is ruled out is a run
Claude decides on by itself.

### What a reviewer carries and what it reads

A reviewer carries what every subagent carries: the core rules of the
forge and the instance file. It reads the project's documents from
disk. The critic and the challenger take an optional target: an
[artefact](../reference/glossary.md) of the chain, named as the state
map names it, or any file of the project by its path. Without a
target they read the whole chain. A check takes a project by its slug,
or the engine itself.

### One contract per kind, one Lens per member

The challenger has personas, the critic has lenses, the check has
checks. Each member is one agent file. The shared behaviour of a kind
is written once, in one contract for that kind, and is preloaded into
every agent file of the kind. The agent file owns only its Lens
section: what it reads, what it goes after, its own categories and
its own report sections. A Lens is a specialisation of its contract,
never a replacement. It may narrow what is read or make a shared rule
stricter. It may never rename, drop or duplicate a shared rule or
field. The protocol changes in the contract alone. A new persona,
lens or check is added only by the principal's decision, and only
where what it would find genuinely differs from what the others find.

### The agent returns, the command files

Every reviewer returns its report with its findings unnumbered and
writes nothing. The command that started it gives each finding or
challenge its ID from the project's one sequence, files the report
and remakes the [ledger](../reference/glossary.md) (the state report
made from the documents at read time). This happens one report at a
time. Reviewers of any kind may therefore run in parallel, and no ID
is given twice.

The report is immutable and dated. Its name is its date, the time to
the minute and four hex characters of a content hash:
`YYYY-MM-DD-<kind>-<name>-HHMM-<hash>.md`. A critic's report and a
check's report land in `reviews/`; a challenger's report lands in
`challenges/`. A check that finds nothing files nothing.

### Instance facts never enter a report

An instance fact is whatever the instance file and Claude's memory
carry about the installation: names, roles, addresses, hosts. None
of them enters a reviewer's report, not even where it would explain a
finding. A report is a public file, or may be quoted into one.

### Nothing blocks

There are no hard quality gates. Findings and challenges are
advisory. The principal alone decides what is published.

### Settled by walkthrough

Every report is settled by a [walkthrough](../use/walk-through-a-list.md),
one item per message, each closed with a verdict. Every finding and
every challenge ends in one of two ways: it is fixed, or it is
explicitly rejected with a recorded reason in a decision record.
Rejecting and parking are legitimate outcomes. Silently ignoring is
not. An accepted challenge is mended wherever it needs to be, and a
challenge that mends nothing was not accepted. A challenge of a layer
below the intent is mended in that layer and changes nothing above
it. The exception is a challenge that shows that what is wanted
cannot be realised, or only at a price not worth paying: then a
thread is opened in the intent and what is wanted is decided there.

### When to run a challenger

An artefact is best challenged before the next layer is first
derived from it, while accepted challenges are still cheap to absorb.
Whether it runs again later, after a draft or before approval, is
left to the judgement of whoever is running the process.

### Isolation is not independence

The author, the critic and the challengers share one model family.
What that family systematically cannot see, none of them will find.
Agreement between the reviewers is therefore never treated as
validation. It means only that the artefact is consistent under one
set of priors. The calibration point lies outside: review by people
or by a model of [another model family](another-model-family.md),
invited at the principal's discretion. Where several engines answer
one question, Claude lays the answers side by side with the engines
named, and the principal is the chairman: agreement is consistency,
difference is spelled out.

## Why

The reviewers are blind to the conversation because that blindness
is the source of their value. A reviewer that had followed the
conversation would share its assumptions. One that reads only the
documents judges what the documents say.

Every subagent reads its inputs from disk in its own run because the
copy of the core rules in its context may be older than the file on
disk.

A reviewer runs on the principal's word alone because a run costs
tokens, some checks a great deal, and what is spent is his to decide.
There is no other reason.

Review of quality and challenge of substance are two reviewers, not
one, because an agent doing both does neither properly. The formal
audit benefits from a clean context. The substantive challenge
benefits from a different register entirely.

The shared behaviour of a kind is one contract because a copy is a
second place for the same rule. There is one contract per kind and no
common one, because the shared texts of the kinds differ almost
whole; the few sentences common to all stay in each contract in its
own words.

The command numbers and files, never the agent, for every kind alike,
for three reasons:

- a finding without an ID has no place for its verdict, so a rejected
  one would return at the next run
- a check that every save runs would otherwise write into the project
  at every save
- two reviewers run at once would otherwise take one ID

Because the IDs are given in one place, reviewers may run in
parallel.

A report is named by its date, its time and a content hash because two
branches must not make the same name. The first report of a day on
two branches would, since `/save` runs its check on every branch, and
the time alone is not enough for two people.

Instance facts never enter a report because a report is a public
file, or may be quoted into one.

The reviewers' agreement is never validation because they share one
model family with the author, and what that family cannot see, none
of them will find.

## A worked example

A principal works on a project with the slug `example-project`. The
intent has been through an hour of conversation, and the principal
wants it challenged before the first assignment is derived from it.

1. He types `/challenge <persona>`. The command starts the challenger
   as an isolated subagent. The subagent reads the brief and the
   intent from disk, with the engine's rules. The hour of
   conversation is not in front of it.
2. In the same minute he types `/critique <lens>`. A second subagent
   starts, reads the same files and knows nothing of the first.
3. The challenger returns its challenges unnumbered and writes
   nothing. The command gives them their IDs from the project's one
   sequence, files the report in `challenges/` under
   `YYYY-MM-DD-challenge-<persona>-HHMM-<hash>.md` and remakes the
   ledger. Then the critic returns its findings, and the command does
   the same for them, filing the report in `reviews/`. No ID is given
   twice, though both ran at once.
4. One challenge would be easier to explain with a name that stands
   only in the instance file. The report does not carry it. The
   challenge is written so that the point stands without the name.
5. The principal walks through the challenges one per message. He
   accepts the first and mends the intent where the challenge lands.
   He rejects the second with a reason, which is recorded as a
   decision. He parks the third. Nothing blocked the intent while
   he decided.
6. After the mend he runs a second persona. It raises nothing against
   the mended passage. He reads this as consistency under one set of
   priors, not as proof that the passage is right: both personas run
   on the model family that wrote the intent with him. When he wants
   a calibration point, he invites a colleague to read the intent.
   A reviewer on another model family is not built yet; what the
   forge has on that link is said on the page
   [Another model family](another-model-family.md).

## See also

- [The critic](the-critic.md): what the critic judges.
- [The challenger](the-challenger.md): what the challenger judges.
- [The check](the-check.md): what a check verifies.
- [Another model family](another-model-family.md): the link to a model
  of another family, and why its reviewers are not built yet.
- [Walk through a list](../use/walk-through-a-list.md): how findings
  are settled.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter
names; never edited by hand.
