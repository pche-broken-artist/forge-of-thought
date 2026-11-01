---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 3eec20f25b3ba254
inputs:
  - .claude/skills/check-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0540
  - projects/forge/10-intent.md#POS.0570
  - projects/forge/10-intent.md#POS.1140
---

# The check

A check is a reviewer that verifies whether the files of a project, or
of the engine, follow the current conventions of the forge. This page
explains what a check looks at, how it works, why it changes nothing,
and who files what it finds. It is written for anyone who runs a check,
adds one, or wants to judge how the forge keeps its files in shape.

## What it is

A check verifies mechanical conformance. It asks whether the files of
its target follow the current conventions of the engine, as they stand
in `CLAUDE.md` and in `templates/`. It never judges substance. It never
judges document quality either. Substance belongs to the challenger,
and document quality belongs to the critic. A document that is wrong or
unclear but conforms gets no word from a check.

Each check owns one concern, and no check owns another's. The
[Checks](../reference/checks.md) page lists the checks and what each
verifies. The roster is open: further checks can be added as they are
needed, as the [Add a check](../extend/add-a-check.md) page shows.

A check runs as an isolated subagent (a separate instance of Claude
that sees nothing of the working conversation and reads every input
from disk in its own run). It runs on the same mechanism as the critic
and the challenger:

- its own contract, shared by every check;
- one agent file per kind of check;
- a roster, listed when the command is given bare;
- a run by hand.

Its target is a project, named by its slug, or the engine.

## How it works

### It reads the rules at their owners

The rules a check verifies have owners: `CLAUDE.md`, a template, a
position of the forge's own intent. The check reads each rule there.
Its own agent file names the owner of each rule and never restates the
rule. The reason is not recorded.

### It changes nothing

A check is read-only. It changes no document, not the ledger (the
single source of truth for a project's state, made by a script at read
time) and not a resource index. Every fix is applied afterwards by
Claude, on the word of the principal (the person whose thinking is
being forged), after a walkthrough (one item per message, each closed
with a verdict from the principal). A fix that is pure bookkeeping,
such as a missing field of an index entry, may be marked "immediate
fix". Claude can then offer it at once.

### It reports findings only

What conforms is not reported, under no label. A state that the check's
own definition calls a fact and not a finding is reported once, in one
line, as a fact.

Every finding carries:

- where it is, as `file:line`, or a range where it spans lines;
- the rule it breaks, with the owner of that rule;
- one proposed fix, in a sentence.

Findings are ranked by severity: what would mislead or break first
comes first, never the order in which they were found.

### It does not raise again what was decided

A finding that the project's decisions record as rejected is not raised
again. At most it is named once as a fact, with the decision cited.

A finding that was already filed is reported under the ID it has, never
as new. It is still open while it stands. It is reopened when the
ledger has it resolved and it stands again. To know which findings are
known, the check reads the findings of the target's ledger and its own
earlier reports in the target's `reviews/`.

### It is advisory

Nothing a check finds blocks anything. What becomes of a finding is
decided by the principal at the walkthrough, never by the check.

### The command files the report

The check returns its report in its final message and writes no file.
It gives a new finding no ID. The command `/check` gives each new
finding its ID, files the report as a dated file in the project's
`reviews/`, and offers the walkthrough. A finding is settled at that
walkthrough. A rejected one is settled by a decision and is then not
raised again. A run that finds nothing files nothing.

### Who runs which check

Composition is the caller's: a check never calls another check. The
callers are these:

- `/save` runs the light check before it commits and pushes, unless it
  is told to leave the check out with `--quick`.
- `/release` runs its checks, the project's full conformance among
  them, and settles their findings with the principal before the
  release commit.
- Any other check runs on the principal's word. The sweep of the whole
  operating layer for restated rules is one of them: it is never run by
  `/release` on its own. So is the check that reads a document beside
  its history.

The [Check conformance](../use/check-conformance.md) page shows how to
run a check by hand.

## Why

One mechanism serves every reviewer. A user should not have to wonder
why one reviewer's findings are kept and another's are not.

A finding needs an ID. A finding without an ID has no place for its
verdict, so a rejected one would return at the next run.

The command gives the IDs and files the report, never the agent. This
holds for the critic and the challenger as much as for the check, for
three reasons:

- the IDs of a project's findings are given in one place;
- a check that every save runs would otherwise write into the project
  at every save;
- two reviewers run at once would otherwise take the same ID.

Because the agent returns its findings unnumbered, reviewers of any
kind may run in parallel.

The full conformance check belongs to the release, not to the save.
Because it cost minutes and a walkthrough every time, it left the save.
The save keeps the cheap bookkeeping check.

The staleness of a render is never a finding of a check. The release
regenerates the README and the release notes anyway, so such a finding
was void at every release and noise everywhere else. The state map of
a project shows staleness instead.

Why a check is read-only, beyond the principal deciding what is fixed,
is not recorded. Why each check owns exactly one concern is not
recorded. Why every finding must name its file and line, and why
findings are ranked by severity, is not recorded.

## A worked example

A check runs on a project with the placeholder slug `my-project`. It
finds two things:

1. A document's header lacks a field its template requires. Other
   tools would misread the document, so this is ranked first. Where:
   the document's file and the line of its header. Rule: the field, as
   the template that owns it shows it. Fix: add the field.
2. An entry of the resource index `sources/00-INDEX.md` lacks one of
   the fields of its template. Where: the file and the line of the
   entry. Rule: the template of the index. Fix, marked as an immediate
   fix: add the missing field.

The second finding was already filed in an earlier run and is still
open, so the check names it by the ID it already has. The first is new
and carries no ID. The check returns the report and stops.

`/check` gives the new finding its ID and files the report in
`reviews/`. Claude then walks the principal through the two findings,
one at a time. The principal accepts the first, and Claude adds the
field on his word.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Checks](../reference/checks.md): the checks and what each verifies.
- [Add a check](../extend/add-a-check.md): adding a check of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter
names; never edited by hand.
