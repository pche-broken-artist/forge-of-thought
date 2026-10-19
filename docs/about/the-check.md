---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 53dd49ff7ebd831b
inputs:
  - .claude/skills/check-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0540
  - projects/forge/10-intent.md#POS.0570
  - projects/forge/10-intent.md#POS.1140
---

# The check

A check is a reviewer that verifies whether the files of a project, or
of the engine, follow the current conventions of the forge. This page
explains what a check looks at, how it works, why it changes nothing
itself and who files what it finds. It is written for anyone who runs
checks, adds one or wants to judge the mechanism.

## What it is

A check verifies mechanical conformance. It asks whether the files of
its target follow the current conventions of the engine, as they stand
in `CLAUDE.md` and in `templates/`. It never judges substance, which
belongs to the challenger. It never judges document quality, which
belongs to the critic. A document that is wrong or unclear but follows
the conventions gets no word from a check. A rule that seems worth
tightening is a matter for the forge's intent (the document of the
positions the forge's design rests on), not for a check.

Each check owns one concern, and no check owns another's. A concern
such as the bookkeeping of a save belongs to one check only, never to
two. The reason for one concern per check is not recorded. The checks
and what each verifies are listed on [Checks](../reference/checks.md).

A check runs on the same mechanism as the other reviewers:

- a contract shared by every check (`.claude/skills/check-contract/SKILL.md`);
- one agent file per check, which holds only that check's own part;
- a roster, which bare `/check` lists;
- a run by hand, `/check <check> [slug]`, where the slug names a
  project and its absence the engine.

An agent here is a subagent: a separate run of Claude that sees
nothing of the working conversation and reads its inputs from disk.
The roster is open, so further checks can be added as they are
needed. How to add one is on [Add a check](../extend/add-a-check.md).

## How it works

### It reads the rules where they are owned

Every rule a check verifies has an owner. The owner is `CLAUDE.md`, a
template or a position of the forge's intent. The check reads the rule
at its owner. Its own agent file names the owner of each rule and never
restates the rule. The reason is not recorded in the inputs of this
page.

A check reads as much as its own definition says. One that names a
scope reads that scope and nothing more. One that names the whole
reads the whole, however long it takes.

### It changes nothing

A check is read-only. It changes no document, no ledger (the file that
holds the state of a project) and no index. It returns its report in
its final message and writes no file. Every fix is applied afterwards
by Claude in the working conversation, on the word of the principal
(the person whose thinking is being forged), after the walkthrough
(the review of the findings one item at a time, each closed by the
principal's verdict).

A fix that is pure bookkeeping may be marked "immediate fix". Such a
fix is, for example, a comment restored behind its template or a
missing field of an index entry. The mark lets Claude offer the fix at
once.

### It reports findings only

What conforms is not reported, under no label. There is no
"observation" and no "note". Where a check's own definition says that
a state is a fact and not a finding, the check reports it as a fact in
one line, once. A project without a repository and a missing logo are
such states.

Every finding is precise. It carries:

- where it is: the file and the line, or a range of lines;
- the rule it breaks, with the owner of that rule;
- one proposed fix, in a sentence.

The findings are ranked by severity: what would mislead or break first
comes first. They are never listed in the order the check found them.

### It is advisory

Nothing a check reports blocks anything. What becomes of a finding is
decided at the walkthrough that `/check` offers, never by the check.
The check reports and proposes. The principal decides what is fixed.

### It does not repeat itself

Before it reports, a check reads two things:

- the Findings table of the target's ledger, which the command that
  launches the check makes at read time;
- its own earlier reports in the target's `reviews/`.

A finding already filed is reported under the ID it has, never as new.
It is still open while it stands. It is reopened when the ledger has it
resolved and it stands again.

A finding that the project's `decisions.md` records as rejected by a
decision is not raised again. At most it is named once as a fact, with
the decision cited.

### The command files the report

The check gives a new finding no ID. The `/check` command gives each
new finding its ID and files the report. A finding becomes an FND of
the project's one sequence, in a dated report in `reviews/`. Its state
is a `closed` record in the history that settled it. A run that finds
nothing files nothing. How to run a check and settle its findings is
on [Check conformance](../use/check-conformance.md).

### Who runs which check

Composition belongs to the caller, and checks never call each other.

- `/save` runs the `light` check, the bookkeeping check that is fit for
  a save.
- `/release` runs the checks of the project's full conformance and
  settles their findings with the principal before the release commit.
- The `single-source-of-truth` check, which sweeps the whole operating
  layer and is expensive by design, is never run by `/release` on its
  own. It runs on the principal's word, before a major or after a round
  on the operating layer, and on a project on request.
- The `history` check runs on the principal's word.

The staleness of a render is never a check finding. That holds for the
README and the release notes as well.

## Why

**Read-only, and the command files.** There is one mechanism for every
reviewer. The IDs of a project's findings and challenges are given in
one place. A check that every save runs would otherwise write into the
project at every save. Two reviewers run at once would otherwise take
one ID. Because the agent returns its findings unnumbered and the
command numbers and files them, reviewers of any kind may run in
parallel.

**Findings carry an ID.** A finding without an ID has no place for its
verdict. A rejected one would then return at the next run. A user
could also not tell why one reviewer's findings are kept and another's
are not.

**Conformance only.** Substance and document quality remain the
territory of the challenger and of the critic.

**The full check at the release, not at the save.** The full check
cost minutes and a walkthrough every time it ran at a save. The save
keeps the bookkeeping check, and the release takes the full one. This
is the recommended procedure, never a gate.

**No staleness findings.** The release regenerates the README and the
release notes anyway, so a staleness finding was void at every release
and noise everywhere else. The state map of `/forge` shows staleness
instead, and a render is regenerated only on the principal's word.

**Advisory.** The principal decides what is fixed. Why nothing blocks
is not recorded in the inputs of this page.

## A worked example

A project `<slug>` holds a document whose front-matter says version
0.3, while the newest record of its history companion says 0.2. The
principal runs `/check light <slug>`.

1. The `light` check reads the rule at its owner and compares the
   front-matter with the companion.
2. It reads the Findings table of the project's ledger and its own
   earlier reports. The mismatch is not among them, and no decision
   rejects it.
3. It returns one finding, unnumbered: the file and the line of the
   front-matter, the rule with its owner, and one fix in a sentence.
4. The `/check` command gives the finding the next ID, `FND.NNNN`, and
   files the report in `reviews/` under a dated name.
5. The walkthrough offers the finding to the principal. He accepts it,
   and Claude applies the fix.

Had he rejected it instead, a decision would record the rejection, and
the next run of the check would not raise the finding again.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Checks](../reference/checks.md): the checks and what each verifies.
- [Add a check](../extend/add-a-check.md): adding a check of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
