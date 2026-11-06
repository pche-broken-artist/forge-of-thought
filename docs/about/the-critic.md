---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 59962cdf7a754f60
inputs:
  - .claude/skills/critic-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0400
  - projects/forge/10-intent.md#POS.0410
  - projects/forge/10-intent.md#POS.0270
  - CLAUDE.md#Isolated reviewers
---

# The critic

The critic is the reviewer that judges the quality of a project's
[artefacts](../reference/glossary.md) as documents, read through a
[lens](../reference/critic-lenses.md), and never the substance of the
thinking in them. This page explains what a critic lens judges, how a
run works, why there are two lenses and what a run produces. It is
for the user who wants to know what a critique will and will not tell
him, for the extender who wants to add a lens, and for the evaluator
who wants to understand why the critic is built as it is. How to run
a lens is on [Critique the documents](../use/critique-the-documents.md).

## What it is

The critic is one of the forge's isolated kinds of review. It reads
the documents of a project and reports on their quality as documents:
whether an artefact says what it means, whether the chain of
artefacts still carries one essence from layer to layer. Whether the
objective is the real problem, what assumptions a plan rests on, what
it would do to an organisation: that is the substance of the
thinking, and it belongs to the challenger, not to the critic. If a
document is sound and the thinking in it is wrong, the critic says
nothing.

The critic has lenses. A lens is one angle of reading, with one agent
file of its own (`critic-<lens>`). What every lens shares, the
subject and its boundary, the way of working and the shape of the
report, is written once in a contract, the skill
`.claude/skills/critic-contract/SKILL.md`, and preloaded into every
lens agent at launch. A lens owns only its Lens section: what it
reads and what it goes after. A Lens section specialises the
contract and never replaces it. It may narrow what is read or make a
shared rule stricter. It never renames, drops or duplicates a shared
rule or field. The lenses the forge has today, and the angle of each,
are listed on [Critic lenses](../reference/critic-lenses.md). Adding
one is described on [Add a critic lens](../extend/add-a-critic-lens.md).

There are two lenses:

- `clarity` reads each artefact on its own.
- `essence` reads the chain. For every adjacent pair of artefacts (the
  brief and the intent, the intent and the assignment, every later
  layer and its parent) it first distils, blind, the essence of the
  downstream artefact in a few sentences, then the essence of the
  upstream artefact the same way, and compares the two. A finding of
  `essence` is a difference of essences, not a difference of texts.

Every lens runs as an isolated subagent (an agent run of its own that
sees nothing of the working conversation). It did not take part in
drafting and is not told what the drafter intended. It judges only
what the documents say. Its findings are advisory: the principal (the
person whose thinking is being forged) decides, and a rejected
finding is a legitimate outcome, not a failure.

## How it works

**The target.** A run may take a target, or none.

- Without a target, the lens reads everything its angle covers: the
  whole chain.
- An artefact as target, named as the state map names it (`brief`,
  `intent`, `assignment`, later layers as they come), narrows the run
  to that artefact. For `clarity` that is the artefact alone. For
  `essence` it is that artefact against its parent. A transition
  between two layers is addressed by its downstream artefact, because
  every layer has exactly one parent, so no arrow is ever typed.
- Any file of the project as target, named by its path, is read with
  the chain around it. A work product is read with its specification.
  Where the file gives the lens nothing to work on, the report says
  so and carries nothing else.

**What the lens reads.** The whole chain of the project: the briefs,
the intent, the threads, every layer below the intent that exists,
the decisions and the ledger (the project's single source of truth
for state, made at read time), and every file in `reviews/`. It reads
every input from disk in its own run, and it never modifies any of
them.

**Regression first.** Before anything new, the lens re-tests every
finding of its own lens that was marked resolved since its last run,
and reports each as verified or reopened. A report from the retired
single critic, one named without a lens suffix, belongs to the lens
whose categories its findings fall under. A check's report, one named
`*-check-<name>*.md`, shares the finding sequence but is never the
critic's. A rejected finding is respected: it is not raised again
unless the document changed in a way that materially alters the
situation, and then the decision that rejected it is referenced.

**Calibration.** Each artefact is judged against its own definition
(its state file under `.claude/skills/forge/states/`), never against
another's. The assignment deliberately stays high-level and its
recipients are assumed competent and senior, so completeness is the
test, not brevity. Because the principal sets direction, the critic
never reports as defects:

- a missing stakeholder list, RACI, impact analysis or MECE
  decomposition;
- a missing table of contents;
- absent priorities on the items of an assignment;
- a missing section that may be a deliberate delegation to the
  recipients;
- in a solution design: a part whose detail is left to the file it
  names, a choice said to have had no real alternative, or a section
  deleted because it was empty.

**Testability is a recommendation, not a rule.** Wording that is hard
to test goes into the Recommendations part of the report, never in as
a finding.

**Sharp and few.** Five sharp findings beat twenty trivial ones. The
lens never invents a finding to appear thorough, and never softens one
because the fix is inconvenient. It never edits a chain artefact and
never proposes substance: it proposes the fix of the document.

**The report and its filing.** The lens returns its report in its
final message and writes no file. Its new findings carry no ID; a
known finding is named by the ID it already has. The `/critique`
command then gives each new finding the next number of the project's
finding sequence, in tens, never renumbering, and files the report as
`reviews/YYYY-MM-DD-critique-<lens>-HHMM-<hash>.md`, the name
completed by `scripts/forge-report.py`. The report is immutable from
then on. Claude files the report and offers a walkthrough (the
findings worked one per message, in order of weight, each closed with
a verdict). The report is written in English; the reason is not
recorded in the inputs of this page.

**What the report holds.** A delta summary first: how many findings
are new, which earlier ones are verified resolved, which are still
open and which have become obsolete. Then the findings, each with a
severity (high, medium or low), a category from the lens's own
section, a one-line headline, a location in the documents, the issue,
why it matters and a suggested fix. Then recommendations: not
findings and not gates, such as wording that is hard to test, groups
that overlap or items that could be split; the principal may ignore
them without recording anything. A lens may add sections of its own
after these, as its Lens section defines them. The states a finding
passes through afterwards are those the ledger template defines, and
the ledger is made from them.

**On the principal's word.** No lens runs on Claude's own judgement.
A critique runs when the principal invokes it, or where a command's
definition names it, as `/release` does when it offers `essence`
once.

## Why

**Why the critic sees nothing of the conversation.** That blindness
is the source of its value. A reviewer that knew what the drafter
intended would read the intention into the text instead of judging
what the text says.

**Why two lenses.** One critic hunted formalities and never guarded
the chain. The two lenses split the work: `clarity` guards each
artefact as a document, `essence` guards what passes from one layer
to the next. Comparing distilled essences rather than texts is what
makes a drift of the chain visible as a finding.

**Why a file may be a target.** What Claude composes and the
principal judges, a work product above all, deserves the isolated
look as much as the chain does. The cost is a report that sometimes
says there was nothing to find, and that cost is accepted.

**Why the lens does not number its findings.** Every agent returns
its findings unnumbered and writes nothing; the command numbers and
files one report at a time, so that no ID is given twice.

**Why testability is only recommended.** Assignments are deliberately
high-level. Delegating the concretisation to the recipients through a
deliverable item is a legitimate outcome, so wording that is not yet
testable is not a defect.

**Why omissions are not defects.** The principal sets direction, and a
missing section may be a deliberate delegation to the recipients
rather than a gap. The critic reads what the documents say, not what
a checklist would expect of them.

**Why a run happens only on the principal's word.** A run costs
tokens, and what is spent is his to decide. There is no other reason.
The word may be given once, in a command's definition that names what
it runs; what is ruled out is a run on Claude's own judgement.

**Why one contract for every lens.** A contract owns the conduct, the
isolation, the subject and its boundary, the way of working and the
shape of the output, so that the protocol changes in one place and a
new lens is only its own angle. New lenses are added only by the
principal's decision, and only where what they find genuinely
differs.

**Why findings never carry an instance fact.** A report is a public
file, or may be quoted into one. Names, roles, addresses and hosts of
the installation never enter it, not even where they would explain a
finding.

**Why regression comes first.** The inputs of this page record the
rule and not its reason; the reason is not recorded.

**Why the same model as the rest of the forge.** Speed is bought with
context, never with a weaker reviewer.

## A worked example

A project with the placeholder slug `my-project` has an intent and an
assignment. The principal runs the `essence` lens with the assignment
as target. The lens distils the essence of the assignment in a few
sentences, then the essence of the intent the same way, and compares.
It finds that the intent wants a service the recipients can run
without the principal's team, while the assignment reads as a service
the principal's team keeps operating. That is a difference of
essences, and it becomes one finding, returned without an ID:

- severity: high
- category: the one the lens's own section names for a drift
- headline: the assignment keeps what the intent hands over
- location: the assignment, the group of requirements on operation
- issue: the intent places the running of the service with the
  recipients; the requirements of the assignment describe the
  principal's team as the operator, and no item hands the operation
  over
- why it matters: the recipients would build for the wrong operator,
  and the layer below the intent no longer carries the intent's
  essence
- suggested fix: reword the requirements on operation so that the
  recipients are the operator, or add one item that hands the
  operation over; the substance stays the principal's to decide

The command gives the finding the next free number of the project's
finding sequence, files the report under `reviews/` with the day, the
lens, the time and a hash in its name, and offers a walkthrough.
Whether the assignment is wrong or the intent has moved on is the
principal's call: if he rejects the finding, the rejection is
recorded as a decision, and the lens will not raise it again unless
the documents change materially.

## See also

- [Critique the documents](../use/critique-the-documents.md): running
  a lens.
- [Critic lenses](../reference/critic-lenses.md): the lenses and their
  angles.
- [Add a critic lens](../extend/add-a-critic-lens.md): adding a lens
  of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
