---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: 4b9c9e5693d767a1
inputs:
  - .claude/skills/check-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0540
  - projects/forge/10-intent.md#POS.0570
  - projects/forge/10-intent.md#POS.1140
---

# The check

A check is a reviewer that verifies whether the files of a project,
or of the engine itself, follow the current conventions of the forge.
This page says what a check looks at, how it works, why it changes
nothing and who files its report. It is for the user who runs one,
for the extender who wants to add one, and for the evaluator who
wants to know what a check can and cannot tell him. How a check is
run is on [Check conformance](../use/check-conformance.md); which
checks exist is on [Checks](../reference/checks.md).

## What it is

A check is one of the three kinds of reviewer of the forge. The
other two are the critic, which judges the quality of a document,
and the challenger, which attacks the substance of the thinking. A
check does neither. Its subject is mechanical conformance: whether
the files of its target follow the conventions of the engine as they
stand today, in `CLAUDE.md` and in `templates/`. A document that is
wrong or unclear but conforms is not the check's business. A rule
that seems worth tightening is not a finding either; that is a
matter for the intent of the forge.

A check runs as an isolated subagent, that is a separate run of
Claude that never sees the working conversation and reads only the
files of its target and the rules of the engine. Every check shares
one contract (`.claude/skills/check-contract/SKILL.md`), which owns
the subject, the way of working and the shape of the report. Each
check has an agent file of its own, `check-<name>`, whose Lens
section says what that one check reads and verifies, and nothing
more. The Lens section may narrow the shared rules or make one
stricter; it never replaces them.

The target is what the run names: a project by its slug, or the
engine. Whether a check is called a review is not decided; the
mechanism does not depend on the word.

Each check owns one concern and none of another's. Some checks are
cheap and read only the scope their Lens names; some read the whole
target, honestly, however long it takes. The roster is open: further
checks are added as they come. The word for a member of the roster
is "check", the mechanism's own name serving for its members: the
light check, the project check.

## How it works

A check reads the rules it verifies at their owners. A rule has an
owner, such as `CLAUDE.md`, a template or a position of the forge
intent, and the Lens section names that owner for each rule instead
of restating the rule. Every file the check cites, `CLAUDE.md`
included, is read from disk in that run.

A check is read-only. It changes nothing: not a document, not the
ledger (the file `ledger.md`, the single source of truth for a
project's state), not an index. Every fix is applied afterwards in
the working conversation, on the word of the principal (the person
whose thinking is forged, who alone decides content), after the
walkthrough: the method by which a list of items is worked one item
per message, each closed by the principal's verdict. Pure ledger
bookkeeping, such as a stale version, a date or a count, may be
marked "immediate fix", so that Claude can offer it at once.

A check reports findings only. What conforms is not reported, under
no label. Where a Lens section says that a state is a fact and not a
finding, such as a project without a repository or a missing logo,
the check names it as a fact in one line, once.

Every finding is precise. It carries the file and the line, or a
range of lines where it spans several; the rule it breaks together
with the rule's owner; and one proposed fix in a sentence. The
findings are ranked by severity, that is by what would mislead or
break first, never by the order in which they were found.

A check is advisory. Nothing blocks. What becomes of a finding is
decided at the walkthrough that follows the run, never by the check.

A finding is decided once. Before it reports, a check reads the
Findings table of the target's ledger and its own earlier reports in
`reviews/`. A finding already filed is reported under the ID it
already has, never as new: still open while it stands, reopened when
the ledger has it resolved and it stands again. A finding the
project's `decisions.md` records as rejected by a decision (a `DEC`
record) is not raised again; at most it is named once as a fact,
with the decision cited.

The check returns its report in its final message and writes no
file. Claude, in the working conversation, files the report as a
dated file in `reviews/`, gives each new finding its ID in the
project's one `FND` sequence, adds a row to the ledger and offers
the walkthrough. A run that finds nothing files nothing. The report
holds the findings and, only where the Lens defines one, the facts;
no summary of what conforms, no recommendations, no questions.

The composition of checks belongs to the caller, and checks never
call each other. The save runs the bookkeeping check, `light`, the
one fit for a save. The project's full conformance belongs to the
release, which settles the findings of its checks with the principal
before the release commit. The one expensive sweep of the whole
operating layer, `single-source-of-truth`, runs only on the
principal's word, never by the release on its own. The staleness of
a render is never a finding of any check, the README and the release
notes included.

## Why

A check runs on the same mechanism as the critic and the
challenger, with a contract of its own, one agent per check, a
roster and a run by hand, because the forge wants one mechanism for
every reviewer.

A check never judges substance or quality because those remain the
territory of the challenger and of the critic.

A check is read-only and advisory because the principal decides
what is fixed. The check reports and proposes; the decision is his,
at the walkthrough.

The report is filed by Claude in the working conversation and never
by the check itself, so that the IDs of a project's findings are
given in one place. A check that every save runs would otherwise
write into the project at every save.

A finding of a check gets an ID like a critic's, because a finding
without an ID has no place for its verdict: a rejected one would
return at the next run, and a user could not tell why one reviewer's
findings are kept and another's are not.

The full check left the save and moved to the release because it
cost minutes and a walkthrough every time.

The staleness of a render is never a finding because the release
regenerates the README and the release notes anyway, so that finding
was void at every release and noise everywhere else; the state map
shown by `/forge` says what is stale, and a render is regenerated
only on the principal's word.

Why each check owns exactly one concern, and why a check reads a
rule at its owner instead of restating it, is not recorded in the
inputs of this page.

## A worked example

A check at a save, on a project with the placeholder slug
`my-project`.

1. The principal says `/save my-project`. Before anything is
   committed, Claude launches the light check as a subagent on the
   project. The check reads the ledger, the front-matter of each
   versioned document and its history companion, the resource
   indexes and the dependencies; it reads `CLAUDE.md` and the
   templates from disk for the rules.
2. The check finds that the ledger's Documents table lists the
   intent at version 1.2 while the front-matter of `10-intent.md`
   says 1.3. It reads the Findings table of the ledger and its
   earlier reports in `reviews/`: this one is new. It writes the
   report in its final message: one finding, with the file and
   line in the ledger, the rule and its owner, and the fix marked
   as an immediate fix. It writes no file.
3. Claude presents the report in the working conversation, gives
   the finding its ID, files the report as a dated file in
   `reviews/`, adds the row to the ledger and offers the
   walkthrough.
4. The principal accepts the finding. Claude corrects the ledger row
   and the save goes on.

Had the principal rejected the finding and recorded a decision for
it, the next light check would find the same mismatch and say
nothing new of it: at most one line naming it as a fact, with the
decision cited.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Checks](../reference/checks.md): the checks and what each verifies.
- [Add a check](../extend/add-a-check.md): adding a check of one's own.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
