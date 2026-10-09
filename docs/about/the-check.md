---
generated: 2026-10-09
made: derived
inputs-hash: f88381d4ede57081
inputs:
  - .claude/skills/check-contract/SKILL.md
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About the check

This page explains what a check is, how it works and why it is built
the way it is: for a user who sees one run at a save, for an extender
who wants to add one, and for an evaluator who wants to judge the
design. It was put together from the contract every check shares
(`.claude/skills/check-contract/SKILL.md`), from the sections
Isolated reviewers and Persistence of `CLAUDE.md`, and from the
positions of the forge intent (`projects/forge/10-intent.md`) that
give the reasons.

## What a check is

A check is one of the forge's three isolated reviewers, beside the
critic and the challenger. Its subject is mechanical conformance:
whether the files of its target follow the current conventions of
the engine, as `CLAUDE.md` and the templates state them. It never
judges substance, which is the challenger's job, and never document
quality, which is the critic's. A document that is wrong or unclear
but conforms gets no remark from a check; a rule that seems worth
tightening is a matter for the intent, not for a check.

Each check owns one concern and none another's. The forge has a
roster of them, open to new members: one check reads a project's
structure, IDs, language, immutables, recipes and renders; one reads
the bookkeeping, that is front-matter against the history companion,
the ledger against the files, dependencies and resource indexes;
one reads the engine's core against itself and the forge intent; one
sweeps the whole operating layer for restatements of a rule that
lives elsewhere; one reads a document with its history and reports
where the division between them does not hold. A rule that an older
text attributes to "the check" as one procedure belongs to the one
check that owns its concern, never to two. Which checks exist and
what each verifies is the page [Checks](../reference/checks.md).

A check takes a project by its slug, or the engine. Bare `/check`
lists the roster and recommends a fit.

## How a check is built

A check runs on the same mechanism as the other reviewers: an
isolated subagent that sees the project's documents only, never the
working conversation, on the session model. Every check is one
agent file, `check-<name>`, and the behaviour all checks share is
preloaded from one contract skill named in the agent's front-matter.
The contract owns the subject and its boundary, the way of working
and the shape of the report; the agent file owns its Lens section
and only that. A Lens is a specialisation of the contract, never a
replacement: it may narrow what is read or make a shared rule
stricter, but it cannot rename, drop or duplicate a shared rule or
field, and any change of protocol happens in the contract alone.

The rules a check verifies have owners: `CLAUDE.md`, a template, a
position of the forge intent. The check reads each rule at its owner
and never restates it; its Lens names the owner of each rule. The
reason is the forge's rule that one mechanism lives in one place: a
rule stated twice is a defect, and a check that carried its own copy
of the conventions would be checking against a copy that could drift
from the original. The check also reads every file it cites from
disk in its run, `CLAUDE.md` included, because the copy of
`CLAUDE.md` in the session's context may be older than the file.

Instance facts never enter a check's report: names, roles, addresses
and hosts are left out even where they would explain a finding,
because a report is a public file or may be quoted into one.

## How a check works

**Read-only.** A check changes nothing: not a document, not the
ledger, not an index. Every fix is applied in the session, on the
principal's word, after the walkthrough. Pure ledger bookkeeping, a
stale version, a date or a count, may be marked as an immediate fix
so the session can offer it at once.

**Findings only.** What conforms is not reported, under no label:
no observations, no notes, no summary of what is fine. Where a Lens
says that a state is a fact and not a finding, for instance a project
without a repository or a missing logo, the check reports it as a
fact in one line, once.

**Precise and ranked.** Every finding carries its file and line, or a
range where it spans lines, the rule it breaks together with the
rule's owner, and one proposed fix in a sentence. Findings are ranked
by severity, by what would mislead or break first, never by the order
in which they were found.

**Advisory.** Nothing blocks. What becomes of a finding is decided at
the walkthrough that follows the run, never by the check.

**Decided once.** A finding the project's `decisions.md` records as
rejected, whether in an older record, as overruled or as a state
accepted as it is, is not raised again; at most the check names it
once as a fact and cites the decision.

**Known findings keep their ID.** Before reporting, a check reads the
Findings table of the target's ledger and its own earlier reports in
the target's `reviews/`. A finding already filed is reported under
the ID it has and never as new: still open while it stands, reopened
when the ledger has it resolved and it stands again.

**Cheap where the Lens says so.** A check that names a scope reads
that scope and nothing more; a check that names the whole reads the
whole, honestly, however long it takes. The sweep of the whole
operating layer is expensive by design and runs only on the
principal's word, before a major release or after a round of work on
the operating layer, never as part of a release on its own.

## Who files the report, and why

The check returns its report in its final message and writes no
file. The `/check` procedure in the session files it as a dated,
immutable report in the project's `reviews/`, gives each new finding
its ID and adds a row to the ledger; the check gives a new finding no
ID and names a known one by the ID it has.

Two reasons stand behind this division. First, the IDs of a
project's findings are given in one place: one sequence for the
project, handed out by the session, so that no two reviewers can
number the same finding differently. Second, a check that every save
runs would otherwise write into the project at every save; an agent
that reports and leaves cannot.

## Why findings are filed like a critic's

A check's findings are filed exactly as a critic's are: as findings
of the project's one sequence, in a dated report in `reviews/`, with
a row in the ledger, settled by walkthrough, a rejected one recorded
by a decision and then not raised again. The reason is one mechanism
for every reviewer. A finding without an ID has no place for its
verdict, so a rejected one would return at the next run, and a user
could not tell why one reviewer's findings are kept and another's
are not.

A run that finds nothing files nothing: there is no finding to give
an ID to, nothing for a walkthrough to settle, and so no report to
keep.

## Who runs what

No check runs on Claude's own judgement; every run is invoked by
hand or by a command whose definition names it. Composition is the
caller's, and checks never call each other.

The forge has two doors into git, at two speeds, and they divide the
checks between them. `/save` runs the bookkeeping check, the one that
reads front-matter against the companion, the ledger against the
files, dependencies and resource indexes, and then commits and pushes
on whatever branch is checked out: seconds, no render. `/release`,
from `main` only, runs the checks of the project's full conformance,
settles their findings with the principal at a walkthrough before the
release commit, re-renders the README and the release notes and then
saves with the release message and tag. Which checks each door runs
is stated in its own definition (`.claude/skills/save/SKILL.md`,
`.claude/skills/release/SKILL.md`). Every other check runs on the
principal's word.

The full check left the save because it cost minutes and a
walkthrough every time. The release is a recommended procedure,
never a gate: nothing blocks. The staleness of a render is never a
check finding, the README and the release notes included: the
release regenerates those two anyway, so the finding was void at
every release and noise everywhere else; the `/forge` map shows
staleness instead, and a render is regenerated only on the
principal's word.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Checks](../reference/checks.md): the checks and what each verifies.
