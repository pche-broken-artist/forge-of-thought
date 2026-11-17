---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: b3288c15668ca49c
inputs:
  - .claude/skills/check-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0540
  - projects/forge/10-intent.md#POS.0570
  - projects/forge/10-intent.md#POS.1140
---

# The check

A check is a read-only verification that the files of a project, or
of the [engine](../reference/glossary.md) itself, follow the current
conventions of Forge of Thought (the forge). This page explains what
a check verifies, why it changes nothing and who files its report. It
serves whoever runs a check, adds one or weighs how the forge keeps
its files in order.

## What it is

A check verifies mechanical conformance. It reads the files of its
target and reports where they do not follow the current conventions
of the engine. The conventions are written in `CLAUDE.md` and in the
[templates](../reference/glossary.md) of `templates/`. The target is
named by the run: a project, or the engine itself.

A check never judges substance and never judges the quality of a
document. Substance is the subject of the
[challenger](../reference/glossary.md), and quality is the subject of
the [critic](../reference/glossary.md). Where a document is wrong or
unclear but conforms, a check says nothing. A rule worth tightening
is a matter for the forge's own [intent](../reference/glossary.md),
not for a check.

The staleness of a [render](../reference/glossary.md) is never a
finding of a check. This holds for the README and the release notes
too.

Each check owns one concern, and no check owns the concern of
another. The word "check" names the mechanism and each of its
members: the light check, the project check. Which checks exist and
what each verifies is listed on the page
[Checks](../reference/checks.md).

A check runs on the same mechanism as the critic and the challenger.
The mechanism consists of:

- a contract (one skill that holds what every check shares: the
  subject, the way of working and the shape of the report), kept in
  `.claude/skills/check-contract/SKILL.md`
- one agent per check (`check-<name>`), whose own part is its Lens
  section (which rules this check verifies and in what scope)
- a roster (the list of the checks the forge has), which is open:
  further checks join it as they come, as
  [Add a check](../extend/add-a-check.md) describes
- a run by hand, through the command `/check <check> [slug]`; typed
  bare, the command prints the roster, and
  [Check conformance](../use/check-conformance.md) describes a run

## How it works

A command launches a check as an isolated subagent (a separate run
of Claude that sees nothing of the conversation and reads every
input from disk). The check returns its report to that command. The
[principal](../reference/glossary.md) (the person whose thinking is
forged) decides what becomes of each finding, in a
[walkthrough](../reference/glossary.md) (the findings taken one at a
time, the principal giving a verdict on each).

```
/check, /save or /release
        |
        v
the check             an isolated subagent, read-only
        |
        |             its report, new findings without an ID
        v
the command           no finding: nothing is filed
        |             findings: the report goes to reviews/,
        |             each new finding receives its ID
        v
the walkthrough       the principal decides each finding
        |
        v
Claude                applies what was decided, on the principal's word
```

### It reads each rule where the rule is written

Every rule a check verifies has an owner, which is one of:

- `CLAUDE.md`
- a template
- a position of the forge's own intent

The Lens section of a check names the owner of each rule and never
restates the rule. The check reads the rule at its owner, in the run
itself.

The Lens section also says how much a check reads. A check that
names a scope reads that scope and nothing more. A check that names
the whole reads the whole, however long that takes.

Before it reports, a check reads what is already known about its
target. It reads the Findings table of the target's
[ledger](../reference/glossary.md) (the file that holds the state of
a project, made anew whenever it is read). It also reads its own
earlier reports in the `reviews/` directory beside that ledger.

### It changes nothing

A check is read-only. It changes no document, no ledger and no
index, and it writes no file of its own. Every fix is applied by
Claude, on the principal's word, after the walkthrough.

A check may mark a fix of pure bookkeeping as an "immediate fix".
Pure bookkeeping is, for example, a header field the template does
not have or a missing field of an index entry. Claude can then offer
that fix at once.

### It reports findings only

What conforms is not reported, under any label. Every finding
carries:

- the place, as file and line, or as a range where it spans lines
- the rule it breaks, with the owner of that rule
- one proposed fix, in a sentence

Findings are ranked by severity, that is by what would mislead or
break first. They are never listed in the order the check met them.

Where the Lens section says that a state is a fact and not a
finding, the check reports that state as a fact, in one line, once.
Examples are a project without a repository and a missing logo.

A finding that is already filed is reported under the ID it has, as
still open or as reopened. A new finding receives no ID from the
check. A finding the principal has rejected is not raised again. At
most the check names it once as a fact and cites the decision that
rejected it. A state the principal has accepted as it is counts as
rejected.

### The command files the report

The check returns its report in its final message. The procedure of
`/check` then files the report and numbers its findings:

- the report is a dated file in the `reviews/` directory of the
  project
- each new finding receives an ID with the prefix `FND`, from the
  one sequence the project keeps for its findings

A run that finds nothing files nothing.

Claude presents the report and offers the walkthrough. Nothing
blocks. A check is advisory: what becomes of a finding is decided at
the walkthrough, never by the check. A settled finding is closed by
a `closed` record in the history (the record of changes kept beside
a document) where it was settled. A rejected finding is settled by a
decision.

### Which check runs when

Which checks run together is decided by the command that calls them.
Checks never call each other.

- `/save` runs the light check, which reads the bookkeeping of a
  project and is fit for a save.
- `/release` runs the project check, which reads the full
  conformance of the project. The release settles the findings of
  its checks with the principal before the release commit. That
  order is the recommended procedure, never a gate.
- The other checks run on the principal's word. One of them is
  `single-source-of-truth`, which sweeps the whole operating layer
  (`CLAUDE.md`, the skills, the agents, the templates and the
  scripts) for rules stated in more than one place. It is expensive
  by design, and a release never runs it on its own. The checks that
  read one document against another, such as a document against its
  history, run on the principal's word too.

## Why

**One mechanism for every reviewer.** A check runs on the mechanism
of the critic and the challenger, and its findings are filed as the
findings of a critic are. A finding without an ID has no place for
its verdict. A rejected finding would then return at the next run.
Nobody could tell why the findings of one reviewer are kept and
those of another are not.

**The command numbers and files, never the agent.** The rule holds
for every kind of reviewer. The reasons recorded are:

- the IDs of a project's findings and challenges are given in one
  place
- a check that every save runs would otherwise write into the
  project at every save
- two reviewers run at once would otherwise take the same ID

Reviewers of any kind can therefore run in parallel.

**A check proposes, the principal decides.** What is fixed is
decided by the principal. A check therefore reports and proposes,
and changes nothing itself.

**Conformance only.** Substance and the quality of a document remain
the territory of the challenger and the critic.

**The full check belongs to the release.** At a save the full check
would cost minutes and a walkthrough every time. The bookkeeping
check stays with the save.

**Staleness is shown elsewhere.** A release regenerates the README
and the release notes anyway. A finding on their staleness would be
void at every release and noise everywhere else. The staleness of a
render is shown by the [state map](../reference/glossary.md) of
`/forge`, and a render is regenerated only on the principal's word.

**Not recorded.** For these rules the reason is not recorded:

- each check owns one concern, and checks never call each other
- a check reads a rule at its owner, and its Lens section never
  restates the rule
- what conforms is not reported

## A worked example

A project with the placeholder slug `my-project` keeps an index of
its sources. One entry of that index lacks a field that the template
of the index has. The principal runs the light check:

```
/check light my-project
```

The light check runs as an isolated subagent. It reads the rule at
the template, reads the index and changes nothing. It returns a
report with one finding, which carries:

- the place: `sources/00-INDEX.md:12`
- the rule and its owner: an entry carries the fields the template
  of the index shows
- the fix: one sentence that names the field to add, marked
  "immediate fix"

A missing field of an index entry is pure bookkeeping. The fix
therefore carries the mark.

The finding has no ID yet. The procedure of `/check` files the
report in the `reviews/` directory of the project and gives the
finding its ID, with the prefix `FND`. Claude presents the report,
offers the fix at once and offers the walkthrough. What follows
depends on the principal's verdict:

- The principal accepts the fix. Claude adds the field on that word.
  The next run of the light check finds nothing and files nothing.
- The principal leaves the finding for later. The next run reports
  it again under the ID it already has, as still open, and gives it
  no new ID.
- The principal rejects the finding, and the rejection is recorded
  as a decision. The next run does not raise the finding again. At
  most it names the state once as a fact and cites the decision.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Checks](../reference/checks.md): the checks and what each
  verifies.
- [Add a check](../extend/add-a-check.md): adding a check of one's
  own.
- [The documentation](the-documentation.md): the documentation run,
  which files what it cannot place as a check's report.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
