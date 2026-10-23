---
generated: 2026-10-23
version: 5.34
made: derived
inputs-hash: 7f286129a0bddc7c
inputs:
  - .claude/skills/check-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0540
  - projects/forge/10-intent.md#POS.0570
  - projects/forge/10-intent.md#POS.1140
---

# The check

A check is a reviewer that verifies whether the files of a project, or
of the engine, follow the current conventions. This page explains what
a check verifies, why it changes nothing, who files its report, and
which command runs which check. It is written for anyone who runs the
forge, extends it with checks of their own, or weighs how it keeps
its rules.

## What it is

A check verifies mechanical conformance. It looks at whether the files
of its target follow the current conventions of the engine. Those
conventions are set in `CLAUDE.md` and in the templates (the canonical
skeletons in `templates/`).

A check never judges substance and never judges document quality.
Substance is the challenger's work, and quality is the critic's (both
are other kinds of reviewer, see the [Glossary](../reference/glossary.md)).
A document that is wrong or unclear but conforms gets nothing from a
check. A rule that seems worth tightening is a matter for the forge's
intent, not for a check.

There is not one check but a roster of them, and the roster is open.
Each check owns one concern and no other check owns it. A rule belongs
to the one check that owns its concern, never to two. The checks and
what each verifies are listed in [Checks](../reference/checks.md).

A check runs on the same mechanism as the critic and the challenger:

- a contract of its own: one file that holds what every check shares;
- one agent per check: the agent file adds only what that check reads
  and goes after;
- a roster: the list of checks, shown when the command is given bare;
- a run by hand, through `/check <check> [slug]`.

How a check is run is shown in [Check
conformance](../use/check-conformance.md). How a new check is added is
shown in [Add a check](../extend/add-a-check.md).

## How it works

### It reads the rules at their owners

Every rule a check verifies has an owner: `CLAUDE.md`, a template, or a
position of the forge's intent. The check reads the rule there, in the
same run. Its own agent file names the owner of each rule and never
restates the rule. The reason for this is not recorded on the inputs
of this page.

The target of a check is a project, named by its slug, or the engine.
A check that names a narrow scope reads that scope and nothing more. A
check that names the whole reads the whole, however long it takes.

### It is read-only

A check changes nothing: no document, no ledger (the table of a
project's state, made from its documents at read time), no index. It
returns its report as its final message and writes no file.

Every fix is applied afterwards by Claude, on the principal's word.
The principal is the person whose thinking is being forged, and the
final authority on its content. The fix comes after a walkthrough:
the list of findings is worked one item per message, and the
principal gives a verdict on each.

Some findings are pure bookkeeping, such as a missing field of an
index entry. The check may mark such a finding as an immediate fix.
Claude can then offer it at once.

### It reports findings only, precisely and ranked

What conforms is not reported, under no label. Where a check's own
definition says a state is a fact and not a finding (a project without
a repository, for example), the check reports it as a fact, in one
line, once.

Every finding carries three things:

- where it is: the file and the line, or a range of lines;
- the rule it breaks, with that rule's owner;
- one proposed fix, in one sentence.

Findings are ranked by severity: what would mislead or break first
comes first. The order in which the check found them does not count.

### It does not repeat what is settled

A finding that the project's decisions record as rejected is not raised
again. At most the check names it once as a fact and cites the
decision.

A finding already filed is reported under the ID it already has, never
as new. It is still open while it stands. It is reopened when the
ledger has it resolved and it stands again. To know this, the check
reads the findings table of the target's ledger and its own earlier
reports before it reports.

### The command files the report

The check gives a new finding no ID. The `/check` command numbers the
new findings and files the report in the project's `reviews/`
directory. A run that finds nothing files nothing.

A filed finding is settled by walkthrough, like a critic's. A rejected
one is recorded by a decision and then not raised again.

### It is advisory

Nothing a check reports blocks anything. The check reports and
proposes. The principal decides what is fixed, at the walkthrough.

### Who runs which check

Composition is the caller's. Checks never call each other.

- `/save` runs the `light` check, the bookkeeping check that is fit
  for a save, and then commits and pushes. `/save --quick` leaves the
  `light` check out.
- `/release` runs the checks of the project's full conformance and
  settles their findings with the principal before the release commit.
  Which checks it runs, for a project and for the engine, is defined
  in the release's own definition.
- Some checks run only on the principal's word, never by `/release` on
  its own. The check that sweeps the whole operating layer for
  restated rules is one of them: it is expensive by design.

The staleness of a render is never a check finding. That includes the
README and the release notes.

## Why

**Read-only and advisory.** The principal decides what is fixed. A
check reports and proposes, so that the decision stays with him.

**One mechanism for every reviewer.** A check's findings are filed like
a critic's, with an ID of the project's one sequence. A finding
without an ID has no place for its verdict. A rejected finding would
then return at the next run. A user also could not tell why one
reviewer's findings are kept and another's are not.

**The command gives the IDs, not the check.** The IDs of a project's
findings are given in one place. Otherwise a check that every save
runs would write into the project at every save. Otherwise also two
reviewers run at once could take the same ID. Because the agent
returns its findings unnumbered, reviewers of any kind can run in
parallel.

**The full check belongs to the release, not to the save.** The full
check cost minutes and a walkthrough at every save. The save keeps
only the bookkeeping check.

**Render staleness is not a finding.** The release regenerates the
README and the release notes anyway. A staleness finding on them was
therefore void at every release and noise everywhere else. The state
map of a project (what `/forge` shows) shows staleness instead.

**Findings only, ranked by severity.** The reason is not recorded.

**One concern per check.** The inputs state the rule that no concern
belongs to two checks. The reason is not recorded.

## A worked example

Take a project with the placeholder slug `my-project`. You run the
light check on it before a save.

1. The check reads the project's documents and, at their owners, the
   rules it verifies.
2. It finds a document whose header carries version `1.0` and status
   `draft`. The versioning convention in `CLAUDE.md` says an integer
   version is `approved`. That is a finding.
3. It reads the ledger's findings table and its own earlier reports.
   The finding is not there, and no decision rejected it. So it is
   new, and the check gives it no ID.
4. It returns its report: one finding, with the file and line, the
   rule and its owner (`CLAUDE.md`, versioning), and one fix ("set the
   status to `approved`, or the version back to a draft number").
   Nothing that conforms is mentioned.
5. The `/check` command gives the finding its ID and files the report
   in `reviews/`.
6. The principal walks through the finding and decides. If he accepts
   it, Claude applies the fix on his word. If he rejects it, the
   decision is recorded and the next run does not raise it again.

Had the run found nothing, no report would have been filed.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Checks](../reference/checks.md): the checks and what each verifies.
- [Add a check](../extend/add-a-check.md): adding a check of one's
  own.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-23 for version 5.34 from the files the
front-matter names; never edited by hand.
