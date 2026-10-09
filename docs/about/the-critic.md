---
generated: 2026-10-09
made: derived
inputs-hash: 9ce04537ec0765cd
inputs:
  - .claude/skills/critic-contract/SKILL.md
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About the critic

This page explains what the critic is, how it works and why it is
built the way it is. It is for anyone who runs a critique on a
project, anyone who wants to add a lens, and anyone judging whether
the critic does its job. It was put together from the critic's
contract (`.claude/skills/critic-contract/SKILL.md`), the Isolated
reviewers section of `CLAUDE.md` and the positions of the forge
intent (`projects/forge/10-intent.md`) that give the reasons behind
the design.

## What the critic is

The critic is one of the forge's isolated reviewers. Its subject is
the quality of a project's artefacts as documents, read through a
lens: whether the brief, the intent, the assignment and any later
layer say what they say clearly and completely. It never judges the
substance of the thinking. Whether the objective is the real
problem, what the plan rests on, what it would do to the
organisation: that is the challenger's work, and the critic does not
duplicate it. If a document is sound but the thinking behind it is
wrong, the critic says nothing.

Like every reviewer in the forge, the critic runs as an isolated
subagent. It sees the project's documents only, never the working
conversation in which they were drafted, and it must not be told
what the drafter intended. That blindness is the source of its
value: it judges only what the documents say. It runs on the same
model as the rest of the forge, because speed is bought with
context, never with a weaker reviewer.

The critic is invoked by hand, with `/critique <lens> [artefact]`.
It never runs on Claude's own judgement, and a save runs no
critique. A release offers the `essence` lens once, because that is
the lens that guards what a release publishes; it runs no reviewer
of its own accord.

Its findings are advisory. The principal decides what to do with
each one, and a rejected finding is a legitimate outcome, not a
failure. Findings are settled by walkthrough, one item per message.

## Why two lenses

The critic has two lenses because one critic, in the forge's
experience, hunted formalities and never guarded the chain. The two
lenses look at different things:

- `clarity` reads each artefact on its own, as a document that has
  to stand by itself.
- `essence` reads the chain. For every adjacent pair of artefacts,
  the brief and the intent, the intent and the assignment, and every
  later layer against its parent, it first distils, blind, the
  essence of the downstream artefact in a few sentences, then the
  upstream's in the same way, and compares the two. A finding is a
  difference of essences, not of texts.

A target narrows the lens. Named with an artefact, as `/forge` names
it (`brief`, `brief-<name>`, `intent`, `assignment`, later layers),
`clarity` reads that artefact alone and `essence` reads that
artefact against its parent. A transition is addressed by its
downstream artefact: every layer has exactly one parent, so no arrow
ever has to be typed. Without a target, a lens reads everything it
is meant to read.

The behaviour the two lenses share is written once, in a contract
skill preloaded into each lens agent. The contract owns the subject
and its boundary, the conduct and isolation, the way of working and
the shape of the output. A lens file owns only its Lens section,
which specialises the contract: it may narrow what is read or make a
shared rule stricter, but never renames, drops or duplicates a
shared rule or field. New lenses come only by the principal's
decision, and only where what they would find genuinely differs from
what the existing lenses find.

## How it works

A critique reads the whole chain of the project: the briefs, the
intent, the open threads, every layer below the intent that exists,
the decisions and the ledger, together with every earlier report in
`reviews/`. It reads and never modifies; it never edits a chain
artefact.

Regression comes first. Before raising anything new, the lens
re-tests every finding of its own that was marked resolved since its
last run and reports each as verified or reopened. Findings of the
retired single critic, from reports without a lens suffix, count as
the lens's own where they fall under its categories; findings of a
check, which share the same numbering, are never the critic's.
Rejected findings are respected: a lens does not raise them again
unless the document has changed in a way that materially alters the
situation, and then it cites the decision that rejected them.

Each artefact is judged against its own definition, the state file
that says what that artefact is, and never against another's. The
calibration matters: an assignment deliberately stays high-level and
its recipients are assumed competent and senior, so completeness is
the test, not brevity. Because the principal sets direction, a
number of things are never reported as defects: a missing
stakeholder list, RACI, impact analysis, MECE decomposition or table
of contents, absent priorities, or a missing section that may be a
deliberate delegation to the recipients. A solution design holds
only what cannot be read off the thing itself, so a part whose
detail is left to the file it names, a choice said to have had no
real alternative, or a section deleted because it was empty are not
defects either.

Testability is a recommendation, not a rule. The forge holds that
assignments are deliberately high-level and that delegating
concretisation to the recipients is a legitimate outcome, so wording
that is hard to test goes into the report's recommendations, never
into a finding.

Sharp and few beats thorough and long: five sharp findings beat
twenty trivial ones. The critic never invents findings to appear
thorough and never softens one because the fix is inconvenient. And
it never proposes substance; what it proposes is the fix of the
document.

## What it produces

Each run writes one dated report into the project's `reviews/`
directory, named `YYYY-MM-DD-critique-<lens>.md`, in English and
immutable from the moment it is written; a second run on the same
day takes a suffix. The report records which files were read, with
their versions, and which target the run had.

The report opens with a delta summary: which findings are new, which
earlier ones were verified as resolved, which are still open and
which have become obsolete. The findings follow. Each is an FND item
with a global, stable number that continues the project's sequence
and is never renumbered; each carries a severity (high, medium or
low) and a category from the lens's own list, and says where the
issue is, what it is, why it matters and how the document could be
fixed. A recommendations section closes the shared part of the
report: wording that is hard to test, groups that overlap, items
that could be split. These are neither findings nor gates, and the
principal may ignore them without recording anything. A lens may add
sections of its own after that.

After the report, the critic updates the project's ledger: new
findings enter the Findings table as open, with the report as their
source; re-tested ones get their verified or reopened state; the
document states are refreshed. It touches no challenge and no other
document.

Instance facts, such as the names, roles, addresses or hosts of
those who run a forge, never enter a report, not even where they
would explain a finding: a report is a public file, or may be
quoted into one.

## See also

- [Critique the documents](../use/critique-the-documents.md): running a lens.
- [Critic lenses](../reference/critic-lenses.md): the lenses and their angles.
