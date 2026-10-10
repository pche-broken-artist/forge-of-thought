---
generated: 2026-10-10
made: derived
inputs-hash: 561dc8494237052c
inputs:
  - .claude/skills/critic-contract/SKILL.md
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About the critic

This page explains what the critic is, how it works and why it is
built the way it is: for the user who runs it on a project, the
extender who wants to add a lens, and the evaluator who wants to
know what its reports are worth. It was put together from the
critic's contract (`.claude/skills/critic-contract/SKILL.md`), the
Isolated reviewers section of `CLAUDE.md` and the review positions
of the forge's own intent (`projects/forge/10-intent.md`).

## What the critic is

The critic is one of the three isolated reviewers of the forge,
beside the challenger and the check. Its subject is the quality of a
project's artefacts as documents, read through a lens: never the
substance of the principal's thinking. Whether the objective is the
real problem, what assumptions a plan rests on, what it does to the
organisation: that belongs to the challenger. If a document is sound
but the thinking behind it is wrong, the critic says nothing; that is
not its job. Mechanical conformance with the conventions is the
check's, not the critic's either.

The critic runs as an isolated subagent on the session model. It
sees the project's documents only, never the working conversation,
and it is never told what the drafter intended: it judges only what
the documents say. That blindness is the source of its value. It is
invoked by hand, with `/critique <lens>`; no reviewer runs on
Claude's own judgement. A save runs no critic; a release offers the
`essence` lens once and runs nothing on its own.

The critic's findings are advisory. The principal decides, and a
rejected finding is a legitimate outcome, not a failure. Findings
are settled by walkthrough.

## Why two lenses

There are two lenses because one critic hunted formalities and never
guarded the chain. The lenses split the work by what they read:

- **`clarity`** reads each artefact on its own.
- **`essence`** reads the chain. For every adjacent pair, brief to
  intent, intent to assignment, and every later layer, it first
  distils, blind, the essence of the downstream artefact in a few
  sentences, then the upstream's the same way, and compares. A
  finding is a difference of essences, not of texts.

What makes the two lenses one critic is the contract: the shared
behaviour of every lens is written once, in the contract skill, and
preloaded into each lens agent at launch. The contract owns conduct
and isolation, the subject and its boundary, the way of working and
the shape of the report. A lens file owns only its Lens section: a
specialisation of the contract, never a replacement. It may narrow
what is read or make a shared rule stricter; it may never rename,
drop or duplicate a shared rule or field. The protocol changes in the
contract alone. A new lens comes only by the principal's decision,
and only where what it finds genuinely differs.

## What a target does

The critic takes an optional target: an artefact named as `/forge`
names it, by its state file (`brief`, `brief-<name>`, `intent`,
`assignment`, later layers as they come). Without a target, the lens
reads everything it reads: the whole chain.

A target narrows `clarity` to that one artefact and `essence` to
that artefact against its parent. A transition is addressed by its
downstream artefact, since every layer has exactly one parent, so no
arrow is ever typed. This is what lets one file or one transition be
reviewed alone.

## How it works

The critic reads the whole chain of the project, never modifying it:
the briefs, the intent, the open threads, every layer below the
intent that exists, the decisions, the ledger, and every earlier
report in `reviews/`. From there it works in a fixed way.

**Regression first.** Before anything new, the critic re-tests every
finding of its own lens that was marked resolved since its last run,
and reports each as verified or reopened. A report from the retired
single critic counts as its own where the findings fall under its
categories; a check's report never does, though the two share one
numbering of findings. Rejected findings are respected: the critic
does not raise them again unless the document changed in a way that
materially alters the situation, and then it references the decision
that rejected them.

**Each artefact against its own definition.** An artefact is judged
against its own definition and never against another's. The
assignment deliberately stays high-level and its recipients are
assumed competent and senior; completeness is the test, not brevity.
Because the principal sets direction, the critic never reports as
defects what he may have left out on purpose: missing stakeholder
lists, RACI, impact analysis, MECE decomposition, a table of
contents, absent priorities, or a missing section that may be a
delegation to the recipients. For a solution design, which holds
what cannot be read off the thing itself, the same goes for a part
whose detail is left to the file it names, a choice said to have had
no real alternative, or a section deleted because it was empty.

**Testability is a recommendation, not a rule.** The forge's
position is that testability is recommended, never required:
assignments are deliberately high-level, and delegating the
concretisation to the recipients is a legitimate outcome. So wording
that is hard to test goes into the report's recommendations, never
into a finding.

**Sharp and few.** Five sharp findings beat twenty trivial ones. The
critic never invents findings to appear thorough and never softens a
finding because the fix is inconvenient. It never edits a chain
artefact and never proposes substance: it proposes the fix of the
document.

## What it produces

Each run writes one dated, immutable report into the project's
`reviews/` directory, named `YYYY-MM-DD-critique-<lens>.md` (with a
`-2` suffix if the lens already reported that day). Its front-matter
records the date, the project, the lens, the target or `all`, every
file read with its version, and the reviewer. The report carries:

- a **delta summary**: which findings are new, which earlier ones
  were verified resolved, which are still open, which have become
  obsolete;
- the **findings**, each a `FND.NNNN` item continuing the project's
  global sequence in tens and never renumbered, with a severity
  (high, medium or low), a category from the lens, a location in the
  documents, the issue, why it matters and a suggested fix;
- **recommendations**: not findings, not gates. Wording that is hard
  to test, groups that overlap, items that could be split; the
  principal may ignore these without recording anything;
- whatever further sections the lens defines for itself.

The critic then updates the project's ledger: new findings enter the
Findings table as `open` with this report as their source, re-tested
ones get their verified or reopened state, and the document states
are refreshed. It touches no challenge and no other document. The
finding states themselves are those of the ledger template
(`templates/ledger.md`).

Instance facts never enter a report: no names, roles, addresses or
hosts, not even where they would explain a finding, because a report
is a public file or may be quoted into one.

## See also

- [Critique the documents](../use/critique-the-documents.md): running a lens.
- [Critic lenses](../reference/critic-lenses.md): the lenses and their angles.
