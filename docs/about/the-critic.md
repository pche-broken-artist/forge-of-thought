---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: ff2de48682b2577e
inputs:
  - .claude/skills/critic-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0400
  - projects/forge/10-intent.md#POS.0410
  - projects/forge/10-intent.md#POS.0270
---

# The critic

The critic is the reviewer that judges the quality of a project's
artefacts as documents, read through a lens, and never the substance
of the thinking behind them. This page says what the critic is, how
a run of it works, what it produces and why it has two lenses. It is
for the person who runs a critique and reads its report, for the one
who wants to add a lens of his own, and for anyone who has to judge
whether a critique was sound. How a lens is run is said in
[Critique the documents](../use/critique-the-documents.md); the
lenses themselves are listed in
[Critic lenses](../reference/critic-lenses.md).

## What it is

The critic is one of the two isolated kinds of review the forge
has. Both kinds share one shape and differ in their job. The critic
judges document quality and produces findings, items with the
prefix `FND`. The challenger judges the substance of the thinking
and produces challenges, items with the prefix `CHL`. The critic
never duplicates the challenger's work: whether the objective is the
real problem, what assumptions the plan rests on, what it does to
the organisation, is not its subject. Where a document is sound but
the thinking is wrong, the critic says nothing.

The critic runs as an isolated subagent, that is a separate run of
Claude with a context of its own, on the same model as the session.
It never sees the working conversation between the principal and
Claude. The principal is the person whose thinking is being forged,
the one who supplies the ideas and makes the decisions. The critic
did not take part in drafting and is not told what the drafter
intended; it judges only what the documents say.

The critic reads through a lens. A lens is one angle of judgement,
defined in one agent file of its own, `critic-<lens>`. What every
lens shares is written once, in a contract
(`.claude/skills/critic-contract/SKILL.md`) that is loaded into each
lens agent at launch. A lens file owns only its Lens section, which
narrows the contract and never replaces it. The forge has two
lenses:

- `clarity` reads each artefact on its own.
- `essence` reads the chain, pair by pair, and compares what each
  artefact says in essence with what its parent says.

The principal invokes the critic by hand, through `/critique
<lens>`. Claude never runs it on its own judgement. No critique
runs at a save. A release offers `critique essence` once and runs
no reviewer by itself.

A run may take a target: one artefact of the chain, named as the
state map names it (`brief`, `intent`, `assignment`, and later
layers as they come). Without a target the critic reads the whole
chain.

The critic's findings are advisory. The principal decides what
becomes of each one, and a finding he rejects is a legitimate
outcome, not a failure of the critique.

## How it works

### What the critic reads

The critic reads the whole chain of the project and never modifies
any of it:

- the briefs (`00-brief*.md`)
- the intent (`10-intent.md`) and the project's `threads.md`
- every layer below the intent that the project has
- `decisions.md` and `ledger.md`
- every file in `reviews/`

A target narrows the reading. For `clarity` the target is the one
artefact it reads. For `essence` the target is that artefact
compared against its parent. A transition between two layers is
addressed by naming its downstream artefact. Because every layer
has exactly one parent, no arrow between two layers ever has to be
typed.

### Regression first

Before it looks for anything new, the critic re-tests every finding
of its own lens that was marked resolved since its last run, and
reports each one as verified or as reopened. Older reports exist
from a time when the forge had one critic without lenses; the
findings in such a report belong to the lens whose categories they
fall under. Reports of a check (`YYYY-MM-DD-check-<name>.md`) share
the same `FND` sequence but are never the critic's to re-test. The
reason regression comes first is not recorded.

### Respect for rejected findings

A finding the principal has rejected is not raised again. The one
exception is a document that changed in a way that materially
alters the situation; then the critic raises it again and refers to
the decision record that rejected it.

### Each artefact against its own definition

Every artefact of the chain has a definition, its state file under
`.claude/skills/forge/states/`. The critic judges an artefact
against its own definition and never against another's. Two
calibrations follow from the definitions:

- An assignment deliberately stays high-level, and its recipients
  are assumed competent and senior. Completeness is the test, not
  brevity. The following are never reported as defects: a missing
  stakeholder list, a missing RACI, a missing impact analysis, a
  missing MECE decomposition, a missing table of contents, absent
  priorities, and a missing section that may be a deliberate
  delegation to the recipients.
- A solution design holds only what cannot be read off the thing
  itself. The following are never reported as defects: a part whose
  detail is left to the file it names, a choice said to have had no
  real alternative, and a section deleted because it was empty.

Testability is a recommendation, not a rule. Wording that is hard
to test goes into the Recommendations section of the report, never
into a finding.

### Sharp and few

Five sharp findings beat twenty trivial ones. The critic never
invents a finding to appear thorough, and never softens one because
its fix is inconvenient. It never edits a chain artefact, and it
never proposes substance: what it proposes is the fix of the
document.

### How the two lenses differ in their reading

`clarity` takes each artefact on its own terms and judges it as a
document.

`essence` takes every adjacent pair of the chain: brief to intent,
intent to assignment, and every later layer against its parent. For
each pair it first distils, blind, the essence of the downstream
artefact in a few sentences; then it distils the upstream artefact
the same way; then it compares the two. A finding of `essence` is a
difference of essences, not a difference of texts.

### What it produces

Each run writes one report into the project's `reviews/` directory,
named `YYYY-MM-DD-critique-<lens>.md`, in English. The report is
immutable once written; a second run on the same day takes the
suffix `-2`. The report opens with front-matter that names the
date, the project, the lens, the target (one artefact with its
version, or the whole chain), every file read with its version, and
the reviewer. Its body holds:

- a delta summary: which findings are new, which were verified
  resolved, which are still open and which became obsolete
- the findings, each under its ID with a severity (high, medium or
  low) and a category from the lens, and each stating where it is,
  what the issue is, why it matters and what fix is suggested
- recommendations: wording that is hard to test, groups that
  overlap, items that could be split; these are not findings and
  not gates, and the principal may ignore them without recording
  anything
- whatever further sections the lens defines for itself

A new finding continues the global `FND` sequence in tens and is
never renumbered.

After the report the critic updates the ledger, the project's one
file of record for state: it adds the new findings to the Findings
table in the state `open`, with the report as their source; it sets
the verified or reopened state on the findings it re-tested; and it
refreshes the document states. It touches no challenge and no other
document.

The report is then settled by walkthrough: the principal and Claude
go through the findings one item per message, and the principal
gives each a verdict.

## Why

**Why the critic is isolated.** The critic and the challenger never
see the working conversation. That blindness is the source of their
value: a reviewer who knows what the drafter meant judges the
intention instead of the document.

**Why two lenses.** One critic hunted formalities and never guarded
the chain. The chain is the sequence of artefacts from brief to
intent and onward; what matters most is that each layer still says
what its parent says. Reading each document on its own cannot find
drift between layers, and so `essence` was separated from
`clarity`.

**Why `essence` compares essences and not texts.** The lens exists
to guard the chain, not to compare wording. The reason the
distillation is done blind, before the comparison, is not recorded
beyond that.

**Why a release offers `critique essence` and nothing else.** It is
the one lens that guards what a release publishes: the drift of the
chain. Everything else stays in the principal's hands.

**Why testability is a recommendation.** Assignments are
deliberately high-level. Delegating the concrete form of an item to
the recipients, through a deliverable item, is a legitimate outcome.
A finding that demanded testable wording would turn a deliberate
delegation into a defect.

**Why deliberate omissions are not defects.** The principal sets the
direction. A section he leaves out may be a delegation to the
recipients, and the critic cannot tell a delegation from an
oversight. So it reports neither, and the choice stays with the
principal.

**Why the findings are advisory.** The principal is the final
authority on content. The critic informs; it never blocks.

## A worked example

A project with the slug `my-project` has a brief, an intent and an
assignment. The principal runs `/critique essence`. The critic reads
the chain, re-tests the two findings of its lens that were marked
resolved since its last run and reports both as verified. Then, for
the pair intent to assignment, it distils the assignment: the
recipients are to deliver a tool that lets a team record its
decisions, on a platform the assignment names. It distils the
intent: the principal wants the team's decisions recorded and
findable, and leaves the choice of platform to the recipients. The
two essences differ in one point. The report carries one new
finding, in this shape:

> **FND.0120** [medium] [<category of the lens>]
>
> - **Location:** `20-assignment.md`, the constraint on the platform
> - **Issue:** The assignment fixes a platform. The intent leaves
>   the platform to the recipients.
> - **Why it matters:** A recipient reads the platform as a
>   boundary he may not challenge, while the principal meant it to
>   be his choice.
> - **Suggested fix:** Either drop the constraint from the
>   assignment, or carry the choice into the intent first, so that
>   the chain says one thing.

The critic adds the finding to the ledger as `open`, with the
report as its source. The principal walks the report through with
Claude and gives the finding a verdict; if he decides the platform
is in fact his choice, the intent changes first and the assignment
follows.

## See also

- [Critique the documents](../use/critique-the-documents.md):
  running a lens.
- [Critic lenses](../reference/critic-lenses.md): the lenses and
  their angles.
- [Add a critic lens](../extend/add-a-critic-lens.md): adding a lens
  of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-14 for version 5.9 from the files the
front-matter names; never edited by hand.
