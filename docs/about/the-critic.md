---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 77d1c3abc032574d
inputs:
  - .claude/skills/critic-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0400
  - projects/forge/10-intent.md#POS.0410
  - projects/forge/10-intent.md#POS.0270
---

# The critic

The critic is the reviewer that judges the quality of a project's
artefacts as documents, read through a lens, and never the substance
of the thinking they hold. This page says what the critic is, how a
lens works, what a run produces and why there are two lenses. It is
for the user who wants to know what a critique will and will not
tell him, for the extender who wants to add a lens of his own, and
for the evaluator who wants to see what guards the chain.

## What it is

The critic is one of the isolated reviewers of the forge. It runs as
a subagent (a separate Claude process with its own context) that
never sees the working conversation between the principal (the
person whose thinking is being forged) and Claude. Nobody tells it
what the drafter intended. It judges only what the documents say.

Its subject is the quality of the artefacts as documents. Whether
the objective is the real problem, what assumptions a plan rests on,
what it does to the organisation: none of that is the critic's.
Those questions belong to the challenger, the other reviewer of the
same shape. If a document is sound and the thinking behind it is
wrong, the critic says nothing.

The critic reads through a lens. Each lens is one angle on quality
and has an agent file of its own, `critic-<lens>`; what every lens
shares is written once, in the contract
`.claude/skills/critic-contract/SKILL.md`. The forge ships two
lenses:

- `clarity` reads each artefact on its own.
- `essence` reads the chain: for every adjacent pair of artefacts
  (the brief and the intent, the intent and the assignment, every
  later layer and its parent) it first distils the essence of the
  downstream artefact in a few sentences, blind, then distils the
  upstream artefact the same way, and compares the two. A finding of
  this lens is a difference of essences, not a difference of texts.

The lenses and their angles are listed in [Critic
lenses](../reference/critic-lenses.md).

The critic is advisory. Its findings inform; the principal decides,
and a rejected finding is a legitimate outcome, not a failure. No
critic runs on Claude's own judgement: the principal invokes a lens
by hand with `/critique <lens>`, and the way to run one is in
[Critique the documents](../use/critique-the-documents.md). A save
runs no critic. A release offers the `essence` lens once and runs
no reviewer on its own.

## How it works

A lens reads the whole chain of the project: the briefs, the intent,
the project's threads, every layer below the intent that exists, the
decisions, the ledger (the project's single file of state) and every
earlier report in `reviews/`. It reads and never modifies; it never
edits an artefact of the chain.

A run can be narrowed to one target, an artefact named the way the
state map names it (`brief`, `intent`, `assignment` and so on). A
target narrows `clarity` to that one artefact. It narrows `essence`
to that artefact against its parent. A transition between two
layers is therefore addressed by its downstream artefact, and no
arrow is ever typed. Without a target the lens reads everything it
reads.

Regression comes first. Before raising anything new, the lens
re-tests every finding of its own that was marked resolved since
its last run and reports each as verified or reopened. Findings of
the retired single critic, whose reports carry no lens suffix, are
the lens's own where they fall under its categories. Findings of a
check are never the critic's, though they share the same numbering.
A rejected finding is respected: the lens does not raise it again
unless the document changed in a way that materially alters the
situation, and then it cites the decision that rejected it.

Each artefact is judged against its own definition, the state file
that says what that artefact is, and never against another's. The
critic is calibrated to the forge's conventions. An assignment
deliberately stays high-level, and its recipients are assumed
competent and senior; completeness is the test, not brevity. The
principal sets direction, so a deliberate omission is never reported
as a defect: a missing stakeholder list, a RACI, an impact analysis,
a MECE decomposition, a table of contents, absent priorities, or a
missing section that may be a delegation to the recipients. In a
solution design the same holds for a part whose detail is left to
the file it names, a choice said to have had no real alternative, or
a section deleted because it was empty.

Testability is a recommendation, not a rule. Wording that is hard to
test goes into the Recommendations section of the report and never
becomes a finding.

Sharp and few beats thorough and long. The lens never invents
findings to appear thorough and never softens a finding because the
fix is inconvenient. It proposes the fix of the document, never a
change of substance.

A run ends with a report. The report is a dated, immutable file in
`reviews/`, named `YYYY-MM-DD-critique-<lens>.md`, in English,
with a `-2` suffix when the lens has already reported that day. Its
front-matter records the project, the lens, the target and every
file read, with versions where they exist. The body opens with a
delta summary, which lists what is new, what was verified resolved,
what is still open and what became obsolete. Then come the findings.
Each finding carries an ID in the global `FND` sequence, numbered in
tens and never renumbered, a severity (high, medium or low) and a
category from the lens's own set; each names its location, the
issue, why it matters and a suggested fix. A Recommendations section
follows, for what is not a finding and not a gate: wording that is
hard to test, groups that overlap, items that could be split. The
principal may ignore a recommendation without recording anything. A
lens may add sections of its own after that.

After the report the lens updates the ledger: new findings enter the
Findings table as `open`, with the report as their source; re-tested
findings get their verified or reopened state; the document states
are refreshed. The lens touches no challenge and no other document.
The findings are then settled by walkthrough (one item per message,
each closed with the principal's verdict).

## Why

The critic is blind to the conversation because that blindness is
the source of its value: a reviewer who knew what the drafter meant
would read the intention into the text instead of judging what the
text says.

There are two lenses because one critic hunted formalities and never
guarded the chain. Reading each artefact on its own catches what is
unclear within it; it cannot see that an assignment has quietly
drifted from the intent it was made from. The `essence` lens exists
for that drift. It distils each side of a pair blind, before
comparing, so that the comparison is of what each artefact amounts
to and not of its wording. The reason why a difference of essences,
rather than of texts, is the right unit of a finding is not recorded
beyond this.

The `essence` lens is the one a release offers because it is the
one lens that guards what a release publishes: the drift of the
chain.

A target addresses a transition by its downstream artefact because
every layer has exactly one parent. Naming the child names the pair.

Testability is a recommendation because assignments are deliberately
high-level: delegating the concretisation of an item to the
recipients, through a deliverable, is a legitimate outcome. An
untestable sentence may be a choice, and a choice is not a defect.

Deliberate omissions are not defects because the principal sets
direction. A missing section may be a delegation to the recipients
rather than a gap.

The reason why regression is run first, and the reason why few sharp
findings are preferred to many, are not recorded beyond the
contract's own statement that five sharp findings beat twenty
trivial ones.

## A worked example

A project with the slug `my-project` has an intent and an
assignment. The principal runs the `clarity` lens with the
assignment as the target. The lens reads the assignment, its
definition, the earlier reports and the ledger, and re-tests the one
resolved finding of its own from last month, which it reports as
verified. It then raises one new finding, in substance:

- ID and labels: `FND.0230`, severity medium, a category of the
  lens's own.
- Location: `20-assignment.md`, item `REQ.0120`.
- Issue: the item says the recipients "shall keep the current
  interface", and `REQ.0340` says they "shall replace the interface
  with the one chosen in the solution design"; the two items name the
  same interface and the reader cannot tell which holds.
- Why it matters: a recipient reading the assignment on its own
  will pick one of the two and work from it; the assignment is meant
  to be complete and precise.
- Suggested fix: keep the item that states what is wanted and reword
  the other to say which interface it means.

The lens does not say which of the two is right; that is substance,
and it is the principal's. A vague adjective elsewhere in the
assignment ("the service shall be fast") goes into the
Recommendations section, not among the findings. The ledger gains
one row, `FND.0230` as `open`, and the principal settles the report
by walkthrough.

## See also

- [Critique the documents](../use/critique-the-documents.md):
  running a lens.
- [Critic lenses](../reference/critic-lenses.md): the lenses and
  their angles.
- [Add a critic lens](../extend/add-a-critic-lens.md): adding a lens
  of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-11 for version 5.3 from the files the
front-matter names; never edited by hand.
