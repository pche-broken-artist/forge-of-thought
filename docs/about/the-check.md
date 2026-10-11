---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: 701c8f344089357f
inputs:
  - .claude/skills/check-contract/SKILL.md
  - projects/forge/10-intent.md#POS.0540
  - projects/forge/10-intent.md#POS.0570
  - projects/forge/10-intent.md#POS.1140
---

# The check

A check is a reviewer that verifies whether the files of a project,
or of the engine, follow the current conventions of the forge. This
page says what a check verifies and what it leaves alone, how a run
works, why it changes nothing and why its report is filed by Claude
rather than by the check itself. It is for the person who runs a
check, the person who wants to add one, and the person who judges
whether the mechanism is sound. How to run one is on
[Check conformance](../use/check-conformance.md); what each check
verifies is on [Checks](../reference/checks.md).

## What it is

A check is one of the three isolated reviewers of the forge, beside
the critic and the challenger. It runs as a subagent: a separate run
of Claude that sees nothing of the working conversation and reads
every file it needs from disk. The three reviewers share one
mechanism: a contract that owns the shared behaviour, one agent file
per member, a roster, and a run by hand. For the check, the contract
is `.claude/skills/check-contract/SKILL.md`, and each check is an
agent file `check-<name>`. The agent file adds only a Lens section,
which says what that check reads and which rules it verifies; the
contract owns the subject, the way of working and the shape of the
report.

The subject of a check is mechanical conformance: whether the files
follow the current conventions of the engine, as they stand in
`CLAUDE.md` and in `templates/`. A check never judges substance,
which belongs to the challenger, and never judges document quality,
which belongs to the critic. A document that is wrong or unclear but
conforms draws no finding. A rule that seems worth tightening is a
matter for the forge intent, not for a check.

Each check owns one concern, and no two checks own the same one. The
word for every member is "check": the light check, the project
check, the mechanism's name serving for its members. The roster is
open. The checks the forge has today, by the concern each owns, are
listed on [Checks](../reference/checks.md); the one command is
`/check <check> [slug]`, and bare `/check` prints the roster.

## How it works

A check is given a target: a project by its path, or the engine by
its root. How the target narrows the work is said in the check's
Lens section.

The rules a check verifies have owners: `CLAUDE.md`, a template, or
a position of the forge intent. The check reads each rule at its
owner. Its Lens section names the owner of every rule and never
restates the rule.

A check is read-only. It changes nothing: not a document, not the
ledger (the one file that holds the state of a project), not an
index. Every fix is applied afterwards, in the session, on the
word of the principal (the person whose thinking is forged), after
the walkthrough (the method by which a list of findings is worked
one item per message, each closed with a verdict). Pure
bookkeeping in the ledger, such as a stale version, a date or a
count, may be marked by the check as an immediate fix, so that
Claude can offer it at once.

A check reports findings only. What conforms is not reported, under
no label. Where the Lens section says that a state is a fact and not
a finding, such as a project without a repository or a missing
logo, the check names it as a fact in one line, once.

Every finding is precise: it names the file and the line, or the
range of lines; the rule it breaks together with the owner of that
rule; and one proposed fix in a sentence. Findings are ranked by
severity, by what would mislead or break first, never by the order
in which they were found.

A check is advisory. Nothing blocks. What becomes of a finding is
decided at the walkthrough, never by the check.

A finding is decided once. Where the decisions record of the
project (`decisions.md`) holds a DEC that rejected the finding, in
an older record, as overruled, or as a state accepted as it is, the
check does not raise it again; at most it names it once as a fact,
with the DEC cited.

A known finding keeps its ID. Before it reports, the check reads
the Findings table of the target's ledger (for the engine, the
ledger of the forge's own project) and its own earlier reports in
`reviews/` (`*-check-<name>.md`). A finding already filed is
reported under the ID it has, never as new: still open while it
stands, reopened where the ledger has it resolved and it stands
again. A rejected one is not raised.

A check is as cheap as its Lens section says. A check that names a
scope reads that scope and nothing more. A check that names the
whole reads the whole, honestly, however long it takes.

The check returns its report in its final message and writes no
file. Claude, in the session that launched the check (the working
conversation in which the command was given), files the report as
a dated file in `reviews/`, gives each new finding its FND ID from
the project's one sequence, adds a row to the ledger, presents the
report and offers the walkthrough. The check gives a new finding no
ID and names a known one by the ID it has. The report holds the
findings and, where the Lens section defines one, the facts; it
holds no summary of what conforms, no recommendations and no
questions. A run that finds nothing files nothing.

Which checks run together, and when, is decided by the caller, and
checks never call each other. The save runs the bookkeeping check,
the light check, which verifies fitness for a save: the front-matter
against the history companion and the form of its log, the ledger
against the files, the dependencies and the resource indexes. The
full conformance of a project, the project check, belongs to the
release, which settles the findings of its checks with the principal
before the release commit. The expensive sweep of the whole
operating layer, the single-source-of-truth check, runs only on the
principal's word, before a major version or after a round of work on
the operating layer, never by the release on its own. The history
check runs on the principal's word as well.

The staleness of a render is never a finding of a check, the README
and the release notes included. The state map of a project, printed
by `/forge`, shows staleness, and a render is regenerated only on
the principal's word.

## Why

The check runs on the same mechanism as the critic and the
challenger because one mechanism is wanted for every reviewer. The
mechanism takes further kinds of reviewer as they come, and whether
a check is called a review does not matter to it.

A check's findings are filed like a critic's: an FND of the
project's one sequence, a dated report in `reviews/`, a row in the
ledger, settled by walkthrough, a rejected one closed by a DEC and
then not raised again. The reason is the same: one mechanism for
every reviewer. A finding without an ID has no place for its
verdict, so a rejected one would return at the next run, and a user
could not tell why one reviewer's findings are kept and another's
are not.

Claude files the report and gives the IDs, never the check itself,
so that the IDs of a project's findings are given in one place.
Besides, a check runs at every save; if it wrote its own report, it
would write into the project at every save.

The check is read-only and advisory because the principal decides
what is fixed: the check reports and proposes, nothing more.

The full conformance check left the save because it cost minutes
and a walkthrough every time. Bookkeeping, which is quick, stayed
with the save.

The staleness of a render is never a finding because the release
regenerates the README and the release notes anyway, so the finding
was void at every release and noise everywhere else.

Why a run that finds nothing files nothing is not recorded in the
inputs of this page. Why a check reads a rule at its owner rather
than restating it is likewise not recorded here.

## A worked example

The principal of a project with the slug `my-project` asks Claude to
save. Before the commit, Claude launches the light check on the
project. The check reads the ledger, the front-matter of every
versioned document and its history companion, the dependencies and
the resource indexes, and nothing else; the owners of the rules it
verifies are read from disk in that run. It finds that the ledger's
Documents table gives the intent as version 0.7 while the intent's
front-matter says 0.8, and that the history companion's newest
record carries a version the front-matter does not. It reports two
findings, the version mismatch first because it misleads the state
of the project, each with the file and line, the rule and its
owner, and one proposed fix; the ledger row is marked as an
immediate fix. It reports nothing of the pages that conform.

Claude files the report as `reviews/2026-10-11-check-light.md`,
gives the two findings the next IDs of the project's FND sequence,
adds two rows to the Findings table of the ledger, and offers the
walkthrough. The principal accepts the immediate fix of the ledger
row and accepts the second finding as well. Claude applies both
fixes, records them, marks the findings fixed in the ledger and
then saves. Had the check found nothing, it would have reported
"conforms", nothing would have been filed, and the save would have
run straight away.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Checks](../reference/checks.md): the checks and what each
  verifies.
- [Add a check](../extend/add-a-check.md): adding a check of one's
  own.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-11 for version 5.3 from the files the
front-matter names; never edited by hand.
