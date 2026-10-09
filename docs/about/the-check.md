---
generated: 2026-10-09
made: derived
inputs:
  - .claude/skills/check-contract/SKILL.md
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About the check

This page explains what a check in Forge of Thought is, how it works
and why it is built the way it is. It is for anyone who runs checks on
a project, anyone who wants to add a check of their own, and anyone
weighing what the forge's checks can be trusted to do. It was put
together from the check contract (`.claude/skills/check-contract/SKILL.md`),
the sections Isolated reviewers and Persistence of `CLAUDE.md`, and the
positions of the forge's own intent that give the reasons.

## What a check looks at

A check verifies mechanical conformance: whether the files of its
target follow the current conventions of the engine, as they stand in
`CLAUDE.md` and in `templates/`. Its target is a project, named by its
slug, or the engine itself.

A check never judges substance and never judges document quality.
Substance is the challenger's territory and quality the critic's. If a
document is wrong or unclear but follows the conventions, a check says
nothing about it. A rule that ought to be tighter is a matter for the
forge's intent, not for a check to enforce on its own.

There is more than one check, and each owns one concern and none
another's. A rule belongs to the one check whose concern it is, never
to two: bookkeeping, the ledger, dependencies and the resource indexes
belong to the `light` check; structure, recipes and renders to the
`project` check. Checks never call each other.

The rules a check verifies have owners: `CLAUDE.md`, a template, a
position of the forge intent. A check reads each rule where its owner
keeps it and never restates it, so a rule is stated in one place only.

## How a check is built

A check runs on the same mechanism as the critic and the challenger.
There is one shared contract for all checks, and one agent file per
check, named `check-<name>`. The contract owns what every check shares:
its subject and the boundary of that subject, its way of working and
the shape of its report. The agent file adds only a Lens section, which
says what that one check verifies. A Lens may narrow what is read or
make a shared rule stricter; it never renames, drops or duplicates a
shared rule, and the shared protocol changes in the contract alone.

Like every reviewer, a check runs as an isolated subagent: it sees the
project's documents only, never the working conversation, and runs on
the same model as the session. It is run by hand. Running `/check`
with no name lists the available checks and recommends one. New checks
are added only on the principal's decision, and only where what they
find genuinely differs from what the existing checks find. The roster
is open to further kinds as they come.

## How a check works

**Read-only.** A check changes nothing: not a document, not the ledger,
not an index. It returns its report, and the `/check` procedure in the
session files it and gives each new finding its ID. Every fix is
applied afterwards in the session, on the principal's word, after the
findings have been worked through one by one. A pure bookkeeping fix,
such as a stale version, a date or a count, may be marked as an
immediate fix so that the session can offer it at once. The reason is
that checks report and propose, and the principal decides what is
fixed.

**Findings only.** What conforms is not reported, under any label. Where
a check's Lens says that a state is a fact and not a finding, such as a
project without a repository or a missing logo, the check reports it
once, in one line, as a fact.

**Precise.** Every finding names the file and line (a range where it
spans lines), the rule it breaks together with the owner of that rule,
and one proposed fix. Findings are ranked by severity, what would
mislead or break first, never by the order in which they were found.

**Advisory.** Nothing blocks. What becomes of a finding is decided when
the findings are worked through, never by the check.

**Decided once.** A finding that the project's `decisions.md` records
as rejected by a decision is not raised again; at most it is named once
as a fact, with the decision cited.

**Known findings keep their ID.** Before reporting, a check reads the
findings in the target's ledger and its own earlier reports. A finding
already filed is reported under the ID it has, never as new: still
open while it stands, reopened when the ledger has it resolved and it
stands again.

## Who runs which check

Composition is the caller's. A check does not decide when it runs and
no reviewer runs on Claude's own judgement; the commands that save and
release say what they run.

- `/save` runs the `light` check, then commits and pushes. The light
  check is the bookkeeping check, fit for a save.
- `/release` runs its checks and settles their findings with the
  principal before the release commit. The project's full conformance
  belongs to the release. Which checks it runs is the release's own
  definition.
- The other checks run on the principal's word. The
  `single-source-of-truth` check, which sweeps the whole operating
  layer for restatements, is expensive by design and is never run by a
  release on its own.

The full check left the save because it cost minutes and a round of
decisions every time; the save keeps the bookkeeping check and the
release takes the full one. Even at a release the checks are the
recommended procedure, never a gate.

## Why findings are filed like a critic's

A check's findings are filed the same way as a critic's: each new
finding gets an ID of the `FND` kind from the project's one sequence,
the report is kept as a dated file in `reviews/`
(`YYYY-MM-DD-check-<name>.md`), the finding gets a row in the ledger,
and it is settled by working through the findings with the principal.
A rejected finding is recorded by a decision and then not raised
again.

The reason is one mechanism for every reviewer. A finding without an
ID has no place to hold its verdict, so a rejected one would return at
the next run, and a user could not tell why one reviewer's findings
are kept and another's are not.

A run that finds nothing files nothing: its report is the one line
"conforms", presented in the session, and no file is made.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Checks](../reference/checks.md): the checks and what each verifies.
