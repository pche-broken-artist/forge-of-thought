---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 39ac5336057a37dd
inputs:
  - .claude/skills/critic-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0400
  - projects/forge/10-intent.md#POS.0410
  - projects/forge/10-intent.md#POS.0270
---

# The critic

The critic is an isolated reviewer that judges the quality of a
project's artefacts as documents, through one of two lenses. This
page explains what it judges and what it leaves alone, how a run
works, what it produces and why there are two lenses. It is written
for anyone who runs a critique, adds a lens or weighs whether the
review is worth trusting.

## What it is

The critic reads the artefacts of the chain (the brief, the intent
and every layer below it that a project has) and judges them as
documents. It never judges the substance of the thinking. Whether
the objective is the real problem, what a plan rests on and what it
does to an organisation belong to the challenger, the other kind of
reviewer. If a document is sound but the thinking behind it is wrong,
the critic says nothing.

The critic runs as a subagent, that is, a separate instance of Claude
started for one job, which never sees the working conversation. It
is not told what the drafter intended: it judges only what the
documents say. It is started by hand by the principal (the person
whose thinking is being forged), never by Claude on its own and never
at a save. See [Glossary](../reference/glossary.md) for every term
of the forge in one line.

The critic comes in two lenses. A lens is one way of reading, with
its own agent file:

- `clarity`: reads each artefact on its own.
- `essence`: reads the chain, one adjacent pair of artefacts at a
  time.

What each lens goes after in detail is on
[Critic lenses](../reference/critic-lenses.md). How a lens is run is
on [Critique the documents](../use/critique-the-documents.md). How a
lens of one's own is added is on
[Add a critic lens](../extend/add-a-critic-lens.md).

Every lens shares one contract: the subject, the way of working and
the shape of the report are written once for all of them. A lens
adds only its own angle on top.

## How it works

### What a run reads

Without a target, a lens reads everything it covers: the briefs, the
intent, the threads, every layer below the intent, the decisions,
the ledger (the record of the project's state) and every earlier
report in `reviews/`. It reads and never modifies.

A target narrows the run. The target can be one of two things:

- An artefact, named as `/forge` names it. `clarity` then reads that
  artefact. `essence` reads that artefact against its parent.
- Any file of the project, named by its path. The critic reads it
  with the chain around it, and a work product with its
  specification. The report names the file.

A transition between two artefacts is addressed by its downstream
artefact. Every layer has exactly one parent, so the pair is never
typed as an arrow. Where a file gives the lens nothing to work on,
the report says so and carries nothing else.

### How `essence` compares

For every adjacent pair (brief and intent, intent and assignment,
every later layer and its parent), `essence` first distils the
essence of the downstream artefact in a few sentences, blind. It then
distils the upstream artefact the same way and compares the two. A
finding of `essence` is a difference of essences, not of texts.

### The way of working

Every lens works the same way:

- **Regression first.** A run first re-tests every finding of its
  own lens marked resolved since its last run. It reports each one
  as verified or reopened.
- **Rejected findings are respected.** A rejected finding is not
  raised again. The exception is a document that has changed in a
  way that materially alters the situation. Then the new finding
  refers to the decision that rejected the old one.
- **Each artefact against its own definition.** An artefact is
  judged against its own definition (the file that says what that
  artefact is and owns its rules), never against another
  artefact's.
- **Deliberate omissions are never defects.** The principal sets
  direction. A missing stakeholder list, a missing table of contents
  or absent priorities are not reported. A missing section may be a
  deliberate delegation to the recipients, so it is not reported
  either. In a solution design, a detail left to the file it names, a
  choice said to have had no real alternative and a section deleted
  because it was empty are not reported.
- **Testability is a recommendation.** Wording that is hard to test
  goes into the report's Recommendations, never in as a finding.
- **Sharp and few.** A handful of sharp findings is worth more than
  many trivial ones. A lens never invents findings to look thorough.
  It never softens a finding because the fix is inconvenient.
- **The fix of the document, never substance.** A finding proposes
  how to mend the document. It proposes no new content of the
  thinking. The critic never edits an artefact.

### What it produces

A run returns one report and writes no file itself. The `/critique`
command files the report in `reviews/` under a dated name, and the
report is never edited after that. The command also gives each new
finding its ID, the next free one of the project's `FND` sequence.
A finding found earlier keeps the ID it has.

The report opens with a summary of what changed since the last run:

- the count of new findings;
- the findings verified as resolved;
- the findings still open;
- the findings that have become obsolete.

The findings follow, each with a severity (high, medium or low) and
a category from the lens. Recommendations come after them. The
principal may ignore a recommendation without recording anything.

Every finding is advisory. The principal decides each one in a
walkthrough (a conversation that takes the findings one at a time,
each closed by the principal's verdict). "Rejected" is a legitimate
outcome, not a failure of the review.

## Why

- **Why isolated.** The critic never sees the working conversation.
  That blindness is the source of its value: it reads only what the
  documents say, not what anyone meant them to say.
- **Why two lenses.** One critic hunted formalities and never
  guarded the chain. `clarity` keeps the look at each document;
  `essence` watches whether meaning drifts from one artefact to the
  next.
- **Why a file may be the target.** What Claude composes and the
  principal judges deserves the isolated look as much as the chain
  does. This holds for a work product above all. The cost is a report
  that sometimes says there was nothing to find.
- **Why a target at all.** A target lets one file or one transition
  be reviewed alone.
- **Why testability is only a recommendation.** Assignments are
  deliberately high-level. Delegating their concretisation to the
  recipients through a deliverable is a legitimate outcome.
- **Why deliberate omissions are not defects.** The principal sets
  direction, and a missing section may be a delegation rather than a
  gap.
- **Why regression comes first.** The reason is not recorded.
- **Why sharp and few.** The reason beyond the rule itself is not
  recorded.

## A worked example

A generic finding of the `clarity` lens, as it might stand in a
report. It is not taken from any project:

```markdown
### [medium] [ambiguity] — "the team" names no team
- **Location:** 20-assignment.md, REQ.0130
- **Issue:** The item says "the team shall review the design" but
  the assignment names two teams.
- **Why it matters:** A recipient cannot tell who is bound by the
  item.
- **Suggested fix:** Name the team the item binds.
```

The finding carries no ID in the report the lens returns. The
`/critique` command gives it the next `FND` number when it files the
report. The category `ambiguity` stands here for any category the
lens defines.

## See also

- [Critique the documents](../use/critique-the-documents.md): running
  a lens.
- [Critic lenses](../reference/critic-lenses.md): the lenses and
  their angles.
- [Add a critic lens](../extend/add-a-critic-lens.md): adding a lens
  of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
