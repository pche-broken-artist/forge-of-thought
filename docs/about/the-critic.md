---
generated: 2026-10-09
made: derived
inputs:
  - .claude/skills/critic-contract/SKILL.md
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About the critic

This page explains what the critic is, what it judges, how it works
and what it leaves behind. It is for the person who runs it, the one
who extends the forge with a new lens, and the one who is deciding
whether the review is worth trusting. It was put together from the
critic's contract (`.claude/skills/critic-contract/SKILL.md`), from
the section of `CLAUDE.md` on isolated reviewers, and from the
positions in the forge intent that say why the critic has two lenses
and why testability is only recommended.

## What the critic judges

The critic judges the quality of the artefacts as documents, read
through a lens. It does not judge the substance of the thinking.
Whether the objective is the real problem, what a plan assumes, what
it does to an organisation: that belongs to the challenger, a
separate reviewer. If a document is sound but the thinking behind it
is wrong, the critic says nothing.

The critic is one of the forge's isolated reviewers. It runs as a
subagent that sees the project's documents only, never the working
conversation, and it is told nothing of what the author meant. That
blindness is where its value comes from: it judges only what the
documents say. It runs on the same model as the rest of the forge, is
started by hand by the principal with `/critique <lens>`, and never
runs on Claude's own judgement. Its findings are advisory. The
principal decides, and "rejected" is a legitimate outcome, not a
failure.

## Two lenses

The critic has two lenses because a single critic hunted formalities
and never guarded the chain. Each lens is a separate reviewer with
its own angle on the same documents.

- **clarity** reads each artefact on its own.
- **essence** reads the chain. For every adjacent pair (a brief and
  the intent, the intent and the assignment, and so on down every
  later layer) it first distils, blind, the essence of the downstream
  artefact in a few sentences. It then distils the upstream one the
  same way and compares the two. A finding is a difference of
  essences, not a difference of texts.

A target narrows a lens. Given one artefact, clarity reads that
artefact alone, and essence compares that artefact with its parent.
Because every layer has exactly one parent, a pair is named by its
downstream artefact, so no arrow is ever typed. Without a target, the
lens reads the whole chain. Bare `/critique` lists the lenses and
recommends one that fits.

For someone extending the forge: each lens is one agent file,
`critic-<lens>`, and what every lens shares is written once, in the
critic's contract, which is loaded into each lens at launch. The
contract owns the conduct, the subject and its boundary, the way of
working and the shape of the report. A lens's own section only
specialises it: it may narrow what is read or make a shared rule
stricter, but never rename, drop or duplicate a shared rule. A new
lens comes only by the principal's decision, and only where what it
finds genuinely differs from the lenses that exist.

## How it works

The critic's way of working has these parts.

- **Regression first.** Before anything new, the critic re-tests each
  earlier finding of its own lens that was marked resolved, and
  reports it as verified or reopened.
- **Respect for rejected findings.** A finding the principal rejected
  is not raised again unless the document has changed in a way that
  materially alters the situation. In that case the critic refers to
  the decision that rejected it.
- **Sharp and few.** A handful of sharp findings is worth more than
  many trivial ones. The critic does not invent findings to look
  thorough and does not soften one because the fix is inconvenient.
- **Each artefact against its own definition.** The critic measures
  an artefact by the definition of that artefact, never by another's.
  The assignment, for instance, stays deliberately high-level for
  competent, senior recipients, and completeness is its test, not
  brevity.
- **The principal's deliberate omissions are not defects.** The
  critic does not report a missing stakeholder list, a missing
  responsibility matrix, impact analysis, a table of contents, absent
  priorities, or a section that may be a deliberate delegation to the
  recipients. In a solution design it does not report a part whose
  detail is left to the file it names, a choice said to have had no
  real alternative, or a section deleted because it was empty.
- **Testability is a recommendation.** Wording that is hard to test
  is reported among the recommendations, never as a finding. The
  reason is that assignments are deliberately high-level, and handing
  the concretisation to the recipients as a deliverable is a
  legitimate outcome.
- **The critic fixes the document, not the thinking.** It never edits
  an artefact and never proposes substance; it proposes how the
  document should change.

## What it produces

Each run writes a dated report in the project's `reviews/` directory,
named after the date and the lens, which is never edited afterwards.
The report holds:

- findings, each with a number in the project's FND sequence, a
  severity (high, medium or low), a category from the lens, its
  location, the issue, why it matters and a suggested fix;
- a delta summary against earlier runs: what is new, what was
  verified as resolved, what is still open and what has become
  obsolete;
- recommendations, which are neither findings nor gates and which the
  principal may ignore without recording anything;
- any sections the lens adds for itself.

The critic then updates the project's ledger: new findings enter its
findings table as open, re-tested ones get their verified or reopened
state, and the states of the documents are refreshed. The findings
are afterwards settled with the principal in a walkthrough.

## See also

- [Critique the documents](../use/critique-the-documents.md): running a lens.
- [Critic lenses](../reference/critic-lenses.md): the lenses and their angles.
