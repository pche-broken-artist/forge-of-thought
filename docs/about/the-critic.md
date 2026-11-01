---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 1a9f30c916bf9b2a
inputs:
  - .claude/skills/critic-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0400
  - projects/forge/10-intent.md#POS.0410
  - projects/forge/10-intent.md#POS.0270
---

# The critic

The critic is the reviewer that judges how well the documents of a
project are written, never whether the thinking in them is right.
This page explains what the critic judges, why it has two lenses,
how it works and what it hands back. It is for anyone who uses the
critic, adds a lens to it or wants to judge whether it can be
trusted.

## What it is

The critic judges the quality of the project's
[artefacts](../reference/glossary.md) as documents. An artefact is a
document of the chain: the brief, the intent and every layer below
it that the project has.

The critic never judges the substance of the thinking. Whether the
objective is the real problem, which assumptions a plan rests on and
what it does to an organisation belong to the challenger, a separate
kind of reviewer. Where a document is sound but the thinking in it is
wrong, the critic says nothing.

The critic always looks through one lens. A lens is one angle of
reading, run as its own agent. There are two:

- `clarity`: reads each artefact on its own.
- `essence`: reads the chain, one adjacent pair of artefacts at a
  time (brief and intent, intent and assignment, every later layer
  and its parent).

What each lens goes after in detail is on
[Critic lenses](../reference/critic-lenses.md). How you start a run
is on [Critique the documents](../use/critique-the-documents.md).

## How it works

### An isolated reviewer

Each lens runs as an isolated subagent. A subagent is a separate
instance of Claude launched for one job: it sees nothing of the
working conversation and reads every input from disk in its own run.
It did not take part in drafting and is never told what the drafter
intended. It judges only what the documents say.

It runs on the session model, that is the model the whole working
session of Claude runs on. The principal (the person whose thinking
is being forged) starts every run by hand. No run of the critic
happens at a save. A release offers one run of `essence` and runs
none on its own.

### What it reads

Without a target, a lens reads everything it is meant to read:

- the briefs;
- the intent;
- the threads (the open matters of the intent, one file each);
- every layer below the intent that exists;
- the decisions;
- the ledger (the file that holds the state of the project);
- every earlier review report.

It reads these and never changes them.

### What a target does

A run may name a target. The target narrows the run in one of two
ways:

- An artefact, named the way the forge names it (`intent`,
  `assignment` and so on). `clarity` then reads that artefact alone.
  `essence` reads that artefact against its parent.
- Any file of the project, named by its path. The file is read with
  the chain around it. A work product (an output of the project made
  with work of its own) is read with its specification.

A transition between two artefacts is named by the lower one.
Because every layer has exactly one parent, no pair has to be typed.
Where the named file gives the lens nothing to work on, the report
says so and carries nothing else.

### How `essence` compares

For every adjacent pair, `essence` first writes down, blind, the
essence of the lower artefact in a few sentences. It then does the
same for the upper one, and compares the two. A finding of `essence`
is a difference between the two essences, not between the two texts.

### The way of working

Every lens works in the same way:

- **Regression first.** Before anything new, the lens tests again
  every finding of its own lens marked resolved since its last run.
  It reports each one as verified or reopened.
- **Rejected findings are respected.** A finding the principal
  rejected is not raised again. The exception is a document that has
  changed in a way that materially alters the situation. The lens
  then cites the decision that rejected it.
- **Each artefact against its own definition.** Every artefact has a
  definition: the file that says what that artefact is and owns its
  rules. The lens judges an artefact by its own definition, never by
  another's.
- **Deliberate omissions are never defects.** An assignment stays
  high-level on purpose, and its recipients are taken to be competent
  and senior. Completeness is the test, not brevity. The lens
  therefore never reports as a defect a missing list of
  stakeholders, a RACI, an impact analysis, a MECE breakdown, a table
  of contents, absent priorities, or a missing section that may be a
  task handed to the recipients. In a solution design it never
  reports a part whose detail is left to the file it names, a choice
  said to have had no real alternative, or a section deleted because
  it was empty.
- **Testability is a recommendation.** Wording that would be hard to
  test goes among the recommendations, never among the findings.
- **Sharp and few.** Five sharp findings beat twenty trivial ones.
  The lens never invents a finding to look thorough. It never softens
  one because the fix is inconvenient.
- **The fix of the document, not of the thinking.** The lens proposes
  how to mend the document. It proposes no substance and edits no
  artefact.

### What it produces

A lens returns one report and writes no file. The `/critique`
command files the report in the project's `reviews/` folder under a
dated name, and it gives each new finding its number in the
project's sequence of findings. A filed report is never changed.

The report holds:

- a summary of what changed since the last run: new findings,
  findings verified as resolved, findings still open and findings
  that have become obsolete;
- the findings, each with a severity (high, medium or low), a
  category defined by the lens, where it stands, what the problem is,
  why it matters and a suggested fix;
- recommendations, which are not findings and which the principal
  may ignore without recording anything;
- any further sections the lens defines for itself.

Every finding is advisory. The principal decides each one in a
walkthrough (one item at a time, each closed with a verdict), and
"rejected" is a legitimate outcome, not a failure.

## Why

**Why isolation.** The reviewer never sees the working conversation,
and that blindness is the source of its value.

**Why two lenses.** A single critic hunted formalities and never
guarded the chain. `clarity` covers the reading of each artefact on
its own. `essence` guards the chain: what one artefact passes down
to the next.

**Why a release offers `essence`.** It is the one lens that guards
the drift of the chain, and that drift is what a release would
publish.

**Why a file may be the target.** What Claude composes and the
principal judges deserves the isolated look as much as the chain
does, and a work product above all. The cost is a report that
sometimes says there was nothing to find.

**Why testability is only recommended.** Assignments are deliberately
high-level. Handing the making-concrete of an item to the recipients
as a deliverable is a legitimate outcome.

**Why deliberate omissions are not defects.** The principal sets the
direction. A missing section may be a task deliberately handed to the
recipients.

**Why rejected findings stay rejected.** The principal decides, and a
rejection is a legitimate outcome of a review.

**Why regression comes first.** The reason is not recorded.

**Why the lens returns its report instead of filing it.** The reason
is not recorded.

## A worked example

A generic run of `clarity` on an intent might return this one new
finding:

- **Severity:** medium
- **Category:** one of the categories the lens defines
- **Headline:** two positions use one term for two different things
- **Location:** `10-intent.md`, two positions of one group
- **Issue:** the word "owner" means the team that runs a service in
  the first position and the person who approves a change in the
  second.
- **Why it matters:** a recipient of the assignment cannot tell which
  of the two is meant where the word appears later.
- **Suggested fix:** keep "owner" for one meaning and name the other
  differently in both places.

The finding carries no number when the lens returns it. The command
gives it one when it files the report. The principal then accepts,
modifies, questions, rejects or parks it in a walkthrough.

To write a lens of your own, see
[Add a critic lens](../extend/add-a-critic-lens.md).

## See also

- [Critique the documents](../use/critique-the-documents.md): running a lens.
- [Critic lenses](../reference/critic-lenses.md): the lenses and their angles.
- [Add a critic lens](../extend/add-a-critic-lens.md): adding a lens of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
