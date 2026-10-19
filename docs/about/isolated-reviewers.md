---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 304cbe53db399bae
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
they were written. This page explains what they share, how a run of
one becomes a filed report, and why they are built this way. It is
for anyone who uses the forge, extends it or weighs whether to trust
it.

## What it is

The forge has three kinds of reviewer, all of one shape:

- [The critic](./the-critic.md): document quality, never substance.
  Its results are findings, with IDs of the prefix `FND`.
- [The challenger](./the-challenger.md): the substance of the
  thinking, never document quality. Its results are challenges, with
  IDs of the prefix `CHL`.
- [The check](./the-check.md): mechanical conformance with the
  conventions, never substance or quality. Its results are findings,
  with IDs of the prefix `FND`.

The jobs are strictly separate, and each kind has its own output.

Each reviewer runs as an isolated subagent. A subagent is a separate
instance of Claude, started for one job, that sees only what it is
given. A reviewer reads the project's documents and the engine's
rules. It also carries what every subagent carries: the forge's core
file `CLAUDE.md` and the instance file. A challenger may also search
the web. A reviewer never sees the working conversation between
Claude and the principal (the person whose thinking is being forged).

Every reviewer runs on the session model, that is the one model the
principal's Claude Code session runs on. The whole forge runs on one
model.

## How it works

**Invoked by hand.** A reviewer is started by its command:
`/critique <lens>`, `/challenge <persona>` or `/check <check>`. No
reviewer runs on Claude's own judgement. Which reviewers a save and a
release run is said by those two commands. Bare `/critique`,
`/challenge` and `/check` list the members of their kind and
recommend one that fits. The critic and the challenger take an
optional target: one artefact of the chain, or any file of the
project by its path. Without a target they review the whole chain. A
check takes a project by its slug, or the engine.

**One contract per kind, one Lens per member.** The members of a
kind are the critic's lenses, the challenger's personas and the
checks. Each member is one agent file. The behaviour all members of
a kind share is written once, in one contract for that kind, and is
loaded into every member's agent file. The contract owns the
conduct and the isolation, the subject and its boundary, the way of
working and the shape of the report. The agent file owns only its
Lens section: what it reads and what it goes after. A Lens is a
specialisation of its contract, never a replacement. It may narrow
what is read or make a shared rule stricter. It never renames, drops
or duplicates a shared rule or field. A change to the protocol is
made in the contract alone. A new lens, persona or check is added
only by the principal's decision, and only where what it finds
genuinely differs from what the others find.

**The agent writes nothing; the command files.** The reviewer
returns its report with its findings unnumbered. It writes no file.
The command that started it gives the findings their IDs and files
the report. Each finding's state is then shown in the project's
ledger (the record of a project's state).

**Reports are immutable and dated.** A critic's and a check's
report goes into the project's `reviews/` folder, a challenger's
into `challenges/`. Each report is named by its date, the time to
the minute and four hex characters of a content hash:

```
reviews/YYYY-MM-DD-critique-<lens>-HHMM-<hash>.md
challenges/YYYY-MM-DD-challenge-<persona>-HHMM-<hash>.md
reviews/YYYY-MM-DD-check-<name>-HHMM-<hash>.md
```

The script `scripts/forge-report.py` completes the name. Once
written, a report is never edited. A check that finds nothing files
nothing.

**Settled by walkthrough.** The principal settles a report in a
walkthrough, that is one item per message, each closed with a
verdict (see [Walk through a list](../use/walk-through-a-list.md)).
Every finding and every challenge is either fixed or rejected with a
recorded reason. Rejecting and parking are legitimate outcomes.
Silently ignoring one is not. An accepted challenge is mended
wherever it needs to be. A challenge that mends nothing was not
accepted.

**Nothing blocks.** There are no hard quality gates. Findings and
challenges are advisory. The principal alone decides what is
published.

**Instance facts stay out.** What the instance file and Claude's
memory carry (names, roles, addresses, hosts) never enters a
report. This holds even where such a fact would explain a finding.

## Why

**Blindness is the source of their value.** A reviewer that never
saw the conversation reads the documents as they stand. It does not
know what was meant, only what was written.

**One model, never a weaker reviewer.** Speed is bought with
context, never with a weaker reviewer.

**Review and challenge are two reviewers.** An agent doing both
would do neither properly. The formal audit of a document benefits
from a clean context. The challenge of the substance benefits from a
different register entirely. The check is kept apart from both: it
checks conformance, and substance and document quality remain the
critic's and the challenger's territory.

**One contract, written once.** The shared behaviour of a kind is
never copied into each member. There is one contract per kind and no
common one for all three, because the shared texts of the kinds
differ almost whole. The reason a Lens may only narrow and never
replace its contract is not recorded.

**The command numbers, not the agent.** The IDs of a project's
findings and challenges are given in one place. Two reviewers run at
once would otherwise take the same ID. A check that every save runs
would otherwise write into the project at every save. Because the
agent returns its findings unnumbered, reviewers of any kind may run
in parallel. A finding without an ID would have no place for its
verdict, so a rejected finding would come back at the next run.

**A unique name for every report.** Two branches must not make the
same name. The first report of a day on two branches would collide,
because `/save` runs a check on every branch. The time alone is not
enough when two people work on one project, so a content hash is
added.

**Instance facts stay out of reports.** A report is a public file,
or may be quoted into one.

**Challenge early.** An artefact is best challenged before the next
layer of the chain is first derived from it. At that point accepted
challenges are still cheap to absorb. Whether a challenge runs again
later is left to the judgement of whoever runs the process. No rule
prescribes it.

**Isolation is not independence.** The author, the critic and the
challengers share one model family. What that family systematically
cannot see, none of them will find. Agreement between the reviewers
is therefore never treated as validation. It only means the artefact
is consistent under one set of assumptions. The point of calibration
lies outside: review by humans or by a different model family,
invited at the principal's discretion. A challenge may inspire, but
nothing enters the intent because a reviewer wrote it. It enters
only because the principal composed it. An accepted challenge may
change the intent by taking something away as readily as by adding.

**Not recorded.** Why reviewers are invoked by hand: the reason is
not recorded. Why reports are immutable: the reason is not recorded.
Why reports are settled by walkthrough: the reason is not recorded.

## A worked example

The principal of a project `my-project` wants two looks at its
intent: one at the writing, one at the thinking.

1. The principal runs `/critique <lens> intent` and, at the same
   time, `/challenge <persona> intent`. Two isolated subagents
   start. Neither sees the conversation, and neither sees the other.
2. Each reads the intent and the chain around it and returns its
   report. The critic's report holds three findings, unnumbered. The
   challenger's holds four challenges, unnumbered. Neither writes a
   file.
3. The `/critique` command numbers the findings in the project's one
   sequence of `FND` IDs and files
   `reviews/YYYY-MM-DD-critique-<lens>-HHMM-<hash>.md`. The
   `/challenge` command numbers the challenges as `CHL` and files
   `challenges/YYYY-MM-DD-challenge-<persona>-HHMM-<hash>.md`.
   Because only the commands give IDs, the two parallel runs never
   take the same number.
4. The principal walks through each report. Two findings are fixed
   in the intent, one is rejected with a recorded reason. One
   challenge is accepted and mended in the intent, one is parked,
   two are rejected with reasons.
5. Both reviewers found the intent's central argument sound. That
   agreement says the intent is consistent under one model's
   assumptions. It does not say the argument is right.

```
 working conversation          (never seen by a reviewer)

   project documents  ---->  critic     --+
                       ---->  challenger --+--> report, findings unnumbered
                       ---->  check      --+
                                            |
                                            v
                                  command: numbers, files
                                            |
                                            v
                             principal: walkthrough, verdicts
```

## See also

- [The critic](./the-critic.md): what the critic judges.
- [The challenger](./the-challenger.md): what the challenger judges.
- [The check](./the-check.md): what a check verifies.
- [Walk through a list](../use/walk-through-a-list.md): how findings
  are settled.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
