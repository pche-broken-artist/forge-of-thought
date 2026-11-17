---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 27476129047cb0c1
inputs:
  - CLAUDE.md#Isolated reviewers
  - .claude/skills/check/SKILL.md
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

The isolated reviewers are the three kinds of reviewer the forge has:
the critic, the challenger and the check. Each runs apart from the
working conversation and judges only what stands in the project's
files. This page is for whoever runs a reviewer, adds one or weighs
what a reviewer's verdict is worth. It says why the reviewers never
see the conversation, how a report comes to be and what it means when
the reviewers agree.

## What it is

The forge has three kinds of reviewer. They have one shape and
strictly separate jobs:

- [The critic](the-critic.md) reads the quality of the documents,
  never the substance.
- [The challenger](the-challenger.md) reads the substance of the
  thinking, never the quality of a document.
- [The check](the-check.md) reads mechanical conformance with the
  conventions, never the quality of a document and never the
  substance.

The critic and the check return findings. The challenger returns
challenges. What this page says of a finding holds for a challenge as
well.

The shape the three share:

- A reviewer runs as an isolated subagent (a separate run of Claude
  with a context of its own, started by a command). It sees the
  project's documents and never the working conversation.
- It runs on the session model (the model the working conversation
  runs on, chosen once for an instance, that is for one
  installation).
- It runs on the word of the principal (the person whose thinking is
  being forged), never on Claude's own judgement.
- It returns a report. The report is filed immutable and dated.
- Its findings are settled by a walkthrough (the findings worked one
  at a time, each closed by the principal's verdict).
- Nothing it finds blocks anything.
- What it shares with the other reviewers of its kind is written
  once, in a contract. Its own agent file owns only its Lens (the
  section that says what this one reviewer reads and what it goes
  after).

Each kind has its members. The critic has lenses, the challenger has
personas, the check has checks. Each member is one agent file.

The reviewers are not the only isolated subagents of the forge. The
agent that renders an output, the agents that write the documentation
and the agent that runs a research are isolated in the same way. None
of them is a reviewer. Three rules hold for every isolated subagent:

- It sees nothing of the conversation.
- It reads every input from disk in its own run. The copy of the core
  file (`CLAUDE.md`) that it receives at its start may be older than
  the file on disk.
- It lets no instance fact (a fact of one installation) into what it
  returns.

## How it works

```
the principal's word
        |
        v
the command starts the reviewer
        |
        v
the reviewer, an isolated subagent:
  reads the files from disk, sees nothing of the conversation,
  writes nothing
        |
        v   the report, its findings unnumbered
        |
the command numbers the findings and files the report,
one report at a time
        |
        v
the walkthrough: the principal's verdict on each finding
```

**On the principal's word.** The principal starts a reviewer by hand,
with `/critique`, `/challenge` or `/check`. The word may also be given
once, in the definition of a command (the file that says what the
command does) that names the checks it runs. `/save` and `/release`
have it so: whoever orders a save has ordered the checks the save
names. What is ruled out is a run on Claude's own judgement. Neither
the critic nor the challenger runs at a save.

**The run.** The command starts the agent as an isolated subagent.
The agent reads its inputs from disk. It writes no file. It returns
its report to the command, the findings in it unnumbered.

**The filing.** The command numbers the findings and files the
report. It files one report at a time. No ID is then given twice, and
reviewers of any kind may run in parallel. A finding carries an ID
with the prefix `FND`, a challenge one with the prefix `CHL`. The
findings of the critic and of the check take their IDs from one
sequence of the project. A check that finds nothing files nothing.

**The report.** A filed report is immutable: it is never edited. It
is dated, and its name carries three things that keep it apart from
every other report:

- its date
- the time to the minute
- four hexadecimal characters of a hash of its content

```
YYYY-MM-DD-<kind>-<name>-HHMM-<hash>.md
```

No instance fact enters a report. A report is a public file, or may
be quoted into one. The rule holds even where such a fact would
explain a finding.

**The settlement.** The findings of a report are settled by a
walkthrough: [Walk through a list](../use/walk-through-a-list.md)
says how. Every finding is either fixed or explicitly rejected with a
recorded reason. Rejecting and parking are legitimate outcomes.
Silently ignoring a finding is not. An accepted finding is mended
wherever it needs to be, and one that mends nothing was not accepted.

**Nothing blocks.** There are no hard quality gates. Checklists and
findings are advisory. The principal alone decides what is published.

**The next run.** A reviewer that meets a finding already filed
reports it under the ID it has, in one of three states:

- still open
- reopened
- verified resolved

A rejected finding is not raised again.

**When a reviewer is worth running.** An artefact (a document of the
chain, the versioned documents derived one from another; the
[Glossary](../reference/glossary.md) has every term of the forge) is
best challenged before the next layer is first derived from it.
Accepted challenges are then still cheap to absorb. Whether a
reviewer runs again later, after a draft or before approval, is left
to the judgement of whoever runs the process. No rule prescribes it.

**Contract and Lens.** The shared behaviour of a kind of reviewer is
one contract, written once and never copied. The critic, the
challenger and the check own one contract each. A contract owns four
things:

- conduct and isolation
- the subject and its boundary
- the way of working
- the shape of the output

An agent file carries its Lens section and nothing else of the shared
behaviour. A Lens is a specialisation of its contract, never a
replacement. It may narrow what is read or make a shared rule
stricter. It never renames, drops or duplicates a shared rule or
field. The protocol changes in the contract alone. A new lens,
persona or check comes only by the principal's decision, and only
where what it finds genuinely differs from what the others find.

## Why

**Why the reviewers are blind.** The blindness is the source of their
value. A reviewer sees only the files. Its report is therefore a
judgement of what the files say, and of nothing that was only said in
the conversation.

**Why every input is read from disk.** The copy of the core file an
agent receives at its start may be older than the file on disk. What
it reads in its own run is current.

**Why no instance fact enters a report.** A report is a public file,
or may be quoted into one.

**Why three kinds and not one.** One reviewer for both the documents
and the thinking is ruled out. An agent doing both does neither
properly. The formal audit benefits from a clean context. The
substantive challenge benefits from a different register entirely.
Mechanical conformance runs on the same mechanism as a third kind,
and the mechanism takes further kinds as they come. The reason is one
mechanism for every reviewer. A finding without an ID has no place
for its verdict. A rejected one would then return at the next run,
and nobody could tell why one reviewer's findings are kept and
another's are not.

**Why on the principal's word alone.** A run costs tokens, some
checks a great deal. What is spent is for the principal to decide.
There is no other reason.

**Why the session model.** Every command and every reviewer runs on
one model. The strongest model the forge runs on is then a decision,
never the accident of a model fixed for one agent long ago. Speed is
bought with context, never with a weaker reviewer: a reviewer in a
context of its own carries only the files, and the working
conversation is spent on verdicts, not on reading. The forge has two
exceptions to the one model. Neither is a reviewer.

**Why the command numbers and files, never the agent.** The IDs of a
project's findings and challenges are given in one place. An agent
that filed its own report would break that in two ways. A check that
every save runs would write into the project at every save. Two
reviewers run at once would take one ID.

**Why the name carries the time and a hash.** Two branches must never
make the same name. The first report of a day on two branches would
have one name without them: a save runs a check on every branch. The
time alone is not enough for two people.

**Why one contract per kind.** The shared texts of the three kinds
differ almost whole. The few sentences common to all stay in each
contract in its own words. A common contract is considered again only
if a fourth kind repeats them.

**Why agreement is not validation.** Isolation is not independence.
The author (Claude, in the working conversation), the critic and the
challengers are of one model family. What that family systematically
cannot see, none of them will find. Agreement between the reviewers
is therefore never treated as validation. It means only that the
artefact is consistent under one set of priors (the assumptions a
model brings to whatever it reads). The calibration point lies
outside the forge's own reviewers: review by people or by a model of
a different family, invited at the principal's discretion.
[Another model family](another-model-family.md) says how such a model
is reached and why its reviewers are not built yet. A reviewer's
wording carries no authority either. Nothing enters the intent (the
document where what is wanted is decided) because a reviewer wrote
it, only because the principal composed it. An accepted challenge may
change the intent by subtraction as readily as by addition.

**Where no reason is given.** For three rules the reason is not
recorded:

- that nothing blocks
- that a filed report is immutable
- that a new lens, persona or check comes only by the principal's
  decision

## A worked example

A principal has finished a round on the project `my-project` and
wants two reviewers on it at once: one lens of the critic and one
check.

1. **The word.** The principal types `/critique <lens>` and
   `/check <check> my-project`. Claude has started neither before
   that.
2. **The runs.** Each command starts its agent as an isolated
   subagent, and the two run at the same time. Each reads the
   project's files from disk. Neither sees what was said in the
   round.
3. **The returns.** The critic's agent returns a report with two
   findings, the check's agent a report with one. No finding carries
   an ID yet. Neither agent has written a file. Neither report
   carries a fact of the installation it ran on.
4. **The filing.** The reports are filed one after the other. The
   two findings of the first report get the next two free IDs of the
   project's sequence of findings. The finding of the second report
   gets the ID after those. The two files land in `reviews/`:

   ```
   reviews/2027-03-04-<kind>-<name>-1412-a3f1.md
   reviews/2027-03-04-<kind>-<name>-1412-09c7.md
   ```

   `<kind>` and `<name>` say which reviewer ran. A second person who
   files the first report of the same day on another branch gets a
   name of its own: the time and the hash differ.
5. **The walkthrough.** The principal takes the three findings one
   at a time. The first finding of the critic and the finding of the
   check are accepted, and the fixes are written into the documents.
   The second finding of the critic is rejected, and the reason is
   recorded as a decision. Nothing waited on any of the three: the
   principal was free to publish with all of them open.
6. **The next run.** Later the same lens of the critic runs again.
   It reports the first finding under the ID it has, as verified
   resolved. It does not raise the rejected finding again.
7. **The agreement.** The second run has nothing new to say, and a
   challenger run after it agrees. The principal reads that as
   consistency under one model family, not as proof, and asks a
   person to read the document as well.

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

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
