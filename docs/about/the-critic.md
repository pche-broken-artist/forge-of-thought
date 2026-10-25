---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 6ddadbff800c54b8
inputs:
  - .claude/skills/critic-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0400
  - projects/forge/10-intent.md#POS.0410
  - projects/forge/10-intent.md#POS.0270
---

# The critic

The critic is the reviewer that judges the quality of a project's
artefacts as documents, through one lens at a time. This page
explains what a lens judges and what it leaves alone, why there are
two lenses, how a run works and what it produces. It is for anyone
who uses the critic, adds a lens to it or weighs whether the forge
reviews its documents well.

## What it is

The critic reviews the artefacts of a project. An artefact is a
document of the chain, such as the brief, the intent or the
assignment (see the [Glossary](../reference/glossary.md) for every
term of the forge in one line). The critic reads them for their
quality as documents. It never judges the substance of the
principal's thinking. The principal is the person whose thinking is
being forged and who has the final word on all content.

Whether the objective is the real problem, which assumptions a plan
rests on and what it does to an organisation are questions for the
challenger, the other kind of reviewer. The critic does not repeat
that work. Where a document is sound but the thinking behind it is
wrong, the critic says nothing.

The critic runs as an isolated subagent. A subagent is a separate
Claude that gets one task and never sees the working conversation in
which the documents were drafted. It is not told what the drafter
intended: it judges only what the documents say. You start it by
hand with one lens, as
[Critique the documents](../use/critique-the-documents.md) shows.

There are two lenses:

- `clarity`: reads each artefact on its own.
- `essence`: reads the chain. For every adjacent pair (brief to
  intent, intent to assignment, every later layer to its parent) it
  first distils, blind, the essence of the downstream artefact in a
  few sentences. It then distils the upstream artefact the same way
  and compares the two. A finding of `essence` is a difference of
  essences, not of texts.

What each lens goes after in detail is listed in
[Critic lenses](../reference/critic-lenses.md).

### The target

A run may name a target, and the target narrows it:

- An artefact as a target narrows `clarity` to that artefact.
- An artefact as a target narrows `essence` to that artefact against
  its parent. A transition is named by its downstream artefact,
  because every layer has exactly one parent.
- Any file of the project may be a target, named by its path. It is
  read with the chain around it.
- A work product as a target is read with its specification.

Where the file gives the lens nothing to work on, the report says so
and carries nothing else. Without a target, the lens reads the whole
chain.

## How it works

Every lens shares one contract. The contract owns the subject, the
way of working and the shape of the report. A lens adds only its own
angle on top of it, and never replaces a shared rule. How to write
such a lens is shown in
[Add a critic lens](../extend/add-a-critic-lens.md).

### What it reads

A lens reads the whole chain and changes none of it:

- the briefs
- the intent
- the threads (the open matters of the intent, one file each)
- every layer below the intent that exists
- the decisions
- the ledger (the table of the project's state, made from its
  documents)
- every earlier report in `reviews/`

### The way of working

**Regression first.** A lens first re-tests every finding of its own
lens that was marked resolved since its last run. It reports each one
as verified or as reopened. Findings filed by a check share the same
numbering but never belong to a lens.

**Rejected findings are respected.** A finding the principal rejected
is not raised again. The exception is a document that has changed in
a way that materially alters the situation. Then the lens may raise
it again and cites the decision that rejected it.

**Each artefact is judged against its own definition.** Every
artefact has a definition that says what it is and what rules it
keeps. A lens measures an artefact against that definition, never
against the definition of another artefact.

**Deliberate omissions are never defects.** The principal sets the
direction. An assignment stays high-level on purpose, and its
recipients are assumed to be competent and senior. For an assignment
the test is completeness, not brevity. A lens never reports these as
defects:

- a missing list of stakeholders
- a missing RACI or impact analysis
- a missing MECE decomposition
- a missing table of contents
- absent priorities
- a missing section that may be a deliberate delegation to the
  recipients

A solution design holds what cannot be read off the built thing
itself. So a lens never reports these as defects in it:

- a part whose detail is left to the file it names
- a choice said to have had no real alternative
- a section deleted because it was empty

**Testability is a recommendation.** Wording that is hard to test
goes into the report's recommendations, never into its findings.

**Sharp and few.** Five sharp findings beat twenty trivial ones. A
lens never invents findings to look thorough. It never softens a
finding because the fix is inconvenient.

**The document's fix, never new substance.** A lens never edits an
artefact. What it proposes is the fix of the document, not a change
to what the principal thinks.

### What it produces

A lens returns one report and writes no file itself. The report
holds:

- a summary of what changed since the last run: the new findings and
  the findings verified resolved, still open or newly obsolete
- the findings, each with a severity (high, medium or low), a
  category its lens defines, the place it concerns, the issue, why it
  matters and a suggested fix
- recommendations, which are not findings and which the principal may
  ignore without recording anything
- any further sections the lens defines for itself

The `/critique` command then gives each new finding the next number
of the project's finding sequence and files the report in `reviews/`
under a dated name. The report is never changed afterwards. Claude
then offers a walkthrough. A walkthrough is the way a list needing
the principal's decision is worked: one item per message, each closed
with a verdict.

The findings are advisory. The principal decides on each, and
"rejected" is a legitimate outcome, not a failure.

## Why

**Why the critic never judges substance.** Document quality and the
substance of the thinking are separate jobs. The challenger owns the
substance, and the critic does not duplicate it.

**Why it is isolated.** The critic never sees the working
conversation. That blindness is the source of its value: it can only
judge what the documents actually say.

**Why two lenses.** One single critic hunted formalities and never
guarded the chain. `clarity` keeps the look at each artefact on its
own. `essence` guards what the single critic missed: whether each
layer still says, in essence, what its parent says. Because
`essence` guards the drift of the chain, it is the one lens a release
offers to run, since the drift is what a release publishes.

**Why any file may be a target.** What Claude composes and the
principal judges deserves the same isolated look as the chain, and a
work product above all. The cost is a report that sometimes says
there was nothing to find.

**Why testability is only a recommendation.** Assignments are
deliberately high-level. Handing the concretisation to the recipients
as a deliverable is a legitimate outcome. So untestable wording is
not a defect in itself.

**Why sharp and few.** The reason is not recorded beyond the rule
itself: findings must not be invented to look thorough.

## A worked example

Suppose a `clarity` run on the intent of a project with the
placeholder slug `example-project`. The lens finds that one word
carries two meanings in two positions. One finding in its report
could read, in substance:

- **Severity:** medium
- **Category:** one of the lens's own categories
- **Location:** `10-intent.md`, the two positions that use the word
- **Issue:** "customer" means the paying organisation in one
  position and the end user in the other.
- **Why it matters:** a recipient cannot tell which of the two a
  requirement derived from either position is meant for.
- **Suggested fix:** use one word for each of the two meanings.

The finding says nothing about whether serving end users is the
right aim. That would be substance, and it belongs to the challenger.
`/critique` numbers the finding and files the report, and the
principal accepts, modifies or rejects it in the walkthrough.

## See also

- [Critique the documents](../use/critique-the-documents.md):
  running a lens.
- [Critic lenses](../reference/critic-lenses.md): the lenses and
  their angles.
- [Add a critic lens](../extend/add-a-critic-lens.md): adding a lens
  of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
