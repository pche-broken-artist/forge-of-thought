---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 9f13b462dcee5190
inputs:
  - .claude/skills/check-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0540
  - projects/forge/10-intent.md#POS.0570
  - projects/forge/10-intent.md#POS.1140
---

# The check

A check is a reviewer that verifies whether the files of a project, or
of the engine, follow the current conventions. This page explains
what a check verifies, why it changes nothing, who files its report
and which command runs which check. It is for anyone who runs checks,
adds one, or wants to judge how the forge keeps its files in order.

## What it is

A check verifies mechanical conformance. It asks whether the files of
its target follow the current conventions of the engine, as they
stand in `CLAUDE.md` and in `templates/`. It never judges substance:
that belongs to the challenger. It never judges document quality:
that belongs to the critic. A document that is wrong or unclear but
conforms gets no word from a check.

Each check owns one concern, and no check owns another's. The
checks there are, and what each verifies, are listed on
[Checks](../reference/checks.md). The roster is open: further checks
may be added as they are needed, as
[Add a check](../extend/add-a-check.md) shows.

A check runs as an isolated subagent (a separate run of Claude that
never sees the working conversation). It is the same mechanism as the
critic and the challenger:

- a contract shared by every check, `.claude/skills/check-contract/SKILL.md`;
- one agent file per check;
- a roster, listed by the bare command;
- a run started by hand.

The target is what the run names: a project by its slug, or the
engine. How to start a run is on
[Check conformance](../use/check-conformance.md).

## How it works

### It reads the rules where they are owned

Every rule a check verifies has an owner: `CLAUDE.md`, a template, or
a position of the forge's own intent. The check reads the rule there.
Its own file names the owner of each rule and never restates the rule.

### It changes nothing

A check is read-only. It changes no document, no ledger (the state
report of a project, made from its documents) and no index. Every fix
is applied afterwards by Claude in the conversation, on the word of
the principal (the person whose thinking is forged, who decides all
content). That happens after a walkthrough, in which the findings are
put to the principal one at a time for a verdict.

A finding that is pure bookkeeping may be marked "immediate fix".
Examples are a comment left behind by its template, or a missing field
of an index entry. Such a finding can be offered for fixing at once.

### It reports findings only

A check reports what breaks a convention and nothing else. What
conforms is not reported, under no label. Where a check's own file
says that a state is a fact and not a finding, the check reports it
as a fact in one line, once. A project without a repository is one
such state.

Every finding is precise:

- where: the file and line, or a range of lines;
- the rule: the rule it breaks and the owner of that rule;
- the fix: one proposed fix in one sentence.

Findings are ranked by severity: what would mislead or break first
comes first. The order in which they were found does not count.

### It is advisory

Nothing a check reports blocks anything. What becomes of a finding is
decided by the principal at the walkthrough, never by the check.

### It does not repeat itself

Before it reports, a check reads the findings table of the target's
ledger and its own earlier reports. A finding already filed is
reported under the ID it already has, never as new. It is "still
open" while it stands. It is "reopened" when the ledger has it as
resolved and it stands again.

A finding the principal rejected by a decision is not raised again.
At most it is named once as a fact, with the decision cited.

### The command files the report, not the check

The check returns its report as its final answer and writes no file.
A new finding carries no ID in that report. The command `/check`
gives each new finding its ID and files the report as a dated file in
the project's `reviews/`. A run that finds nothing files nothing.

A filed finding is settled by walkthrough. Its state is then recorded
in the history of the document that settled it. A rejected one is
recorded by a decision.

### Who runs which check

Which checks run is decided by the caller, and checks never call each
other.

- `/save` runs the `light` check: the bookkeeping check, fit for a
  save.
- `/release` runs the project's full conformance, the `project` check,
  and settles its findings with the principal before the release
  commit.
- The other checks run on the principal's word. The
  `single-source-of-truth` check is the expensive sweep, run before a
  major release or after a round on the operating layer, and never by
  `/release` on its own. The `history` check is run on the principal's
  word as well.

This is the recommended procedure, never a gate: nothing blocks.

Whether a render is out of date is never a finding of a check. The
`/forge` state map shows it instead, and a render is regenerated only
on the principal's word.

## Why

A check is read-only and advisory because the principal decides what
is fixed. The check reports and proposes; it does not decide.

A check stays out of substance and document quality because those are
already covered by the challenger and the critic.

A finding gets an ID because a finding without one has nothing to
attach its verdict to. A rejected finding would then return at the
next run. One mechanism for every reviewer also lets a user see why
one reviewer's findings are kept and another's are not.

The command, not the check, gives the IDs and files the report. This
holds for every kind of reviewer alike, for three reasons:

- the IDs of a project's findings are then given in one place;
- a check that every save runs would otherwise write into the project
  at every save;
- two reviewers run at once would otherwise take the same ID.

Because the reviewer returns its findings unnumbered, reviewers of any
kind may run in parallel.

The full conformance check left the save because it cost minutes and
a walkthrough every time. It now belongs to the release.

The staleness of a render is not a finding because the release
regenerates the README and the release notes anyway. The finding was
void at every release and noise everywhere else.

Why each check owns exactly one concern, and why a check names the
owner of a rule instead of restating it: the reason is not recorded.

## A worked example

A principal saves a project with the slug `example-project`.

1. `/save` launches the `light` check on `example-project`.
2. The check reads the rules at their owners, the findings table of
   the project's ledger, and its own earlier reports in `reviews/`.
3. It finds two things. A front-matter field of a document disagrees
   with the document's history companion. An entry of the resource
   index lacks a field, which is pure bookkeeping and is marked
   "immediate fix". A third breach it finds is already filed and
   still stands, so it reports that one under its existing ID as
   still open.
4. It returns the report, ranked by severity, with no ID on the two
   new findings, and writes nothing.
5. `/check` gives the two new findings their IDs, files the dated
   report in `reviews/`, and offers the walkthrough.
6. The principal accepts the index fix, which Claude applies at once,
   and rejects the other finding by a decision.
7. At the next save the rejected finding is not raised again.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Checks](../reference/checks.md): the checks and what each verifies.
- [Add a check](../extend/add-a-check.md): adding a check of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
