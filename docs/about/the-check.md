---
generated: 2026-10-10
made: derived
inputs-hash: 2efbae68e6049fac
inputs:
  - .claude/skills/check-contract/SKILL.md
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# About the check

This page explains what a check is in the forge, how it works and
why it is shaped as it is. It is for the user who sees checks run
at a save or a release, for the extender who wants to add one, and
for the evaluator who wants to know what a check promises and what
it does not. It was put together from the check contract
(`.claude/skills/check-contract/SKILL.md`), from `CLAUDE.md` and
from the forge intent (`projects/forge/10-intent.md`); where those
files differ in wording, the operating layer's wording is used and
the intent's reason.

## What a check is

A check is one of the forge's three isolated reviewers, beside the
critic and the challenger. Its subject is mechanical conformance:
whether the files of its target follow the current conventions of
the engine, as `CLAUDE.md` and the templates state them. It never
judges substance, which is the challenger's job, and never
document quality, which is the critic's. A document that is wrong
or unclear but conforms gets no word from a check. A rule that
seems worth tightening is a matter for the intent, not for a check.

Each check owns one concern and none another's. The forge has
several, each with its own agent file (`check-<name>`), and the
roster is open: a new check comes only by the principal's decision,
and only where what it finds genuinely differs from what the others
find. Which checks exist and what each verifies is on the reference
page linked below.

A check runs as an isolated subagent on the session model. It sees
the target's documents only, never the working conversation. The
target is a project named by its slug, or the engine by its root.

## How it works

**It reads the rules at their owners.** Every rule a check verifies
has an owner: `CLAUDE.md`, a template, or a position of the forge
intent. The check reads the rule there. Its own definition names
the owner of each rule and never restates it, so that a rule lives
in one place and a check cannot drift from it.

**It is read-only.** A check changes nothing: not a document, not
the ledger, not an index. Every fix is applied in the session, on
the principal's word, after the walkthrough. Pure ledger
bookkeeping, such as a stale version, a date or a count, may be
marked as an immediate fix so the session can offer it at once.

**It reports findings only.** What conforms is not reported, under
no label. Every finding is precise: the file and line, or a range
where it spans lines; the rule it breaks with its owner; and one
proposed fix in a sentence. Findings are ranked by severity, by
what would mislead or break first, never by the order they were
found. Where a check's definition says a state is a fact and not a
finding, such as a project without a repository or a missing logo,
it is reported once, in one line, as a fact.

**It is advisory.** Nothing blocks. What becomes of a finding is
decided at the walkthrough that follows the run, never by the
check. A check is a recommended procedure, never a gate.

**A finding decided once is not raised again.** A finding the
project's decisions record as rejected, in an older record, as
overruled or as a state accepted as it is, is not reported again;
at most it is named once as a fact, with the decision cited.

**A known finding keeps its ID.** Before it reports, a check reads
the Findings table of the target's ledger and its own earlier
reports in the target's `reviews/`. A finding already filed is
reported under the ID it has, never as new: still open while it
stands, reopened when the ledger has it resolved and it stands
again. A rejected one is not raised.

**It reads what its definition says.** A check that names a scope
reads that scope and nothing more. A check that names the whole
reads the whole, honestly, however long it takes.

Instance facts, such as names, roles, addresses or hosts, never
enter a check's report, not even where they would explain a
finding: a report is a public file, or may be quoted into one.

## Where the report goes

A check returns its report in its final message and writes no file.
The session files it in the target's `reviews/` as a dated report,
`YYYY-MM-DD-check-<name>.md`, gives each new finding its ID and adds
its row to the ledger. A known finding is named by the ID it has;
a new one arrives without an ID.

Why the session and not the check files the report: the IDs of a
project's findings are then given in one place, and a check that
every save runs would otherwise write into the project at every
save.

A check's findings are filed like a critic's: an FND of the
project's one sequence, a dated report, a row in the ledger, settled
by walkthrough, a rejected one by a decision and then not raised
again. The reason is one mechanism for every reviewer. A finding
without an ID would have no place for its verdict, so a rejected
one would return at the next run, and a user could not tell why one
reviewer's findings are kept and another's are not. A run that
finds nothing files nothing: the reports are immutable, and an
empty one would record nothing worth keeping.

## Who runs it

No check runs on the forge's own judgement. A check is run by hand,
through `/check <check> [slug]`, or by a command that composes
checks into its own procedure. Composition is always the caller's,
and checks never call each other.

Two commands compose checks. `/save` runs the `light` check, the
bookkeeping check fit for a save, and then commits and pushes.
`/release`, from `main` only, runs the project's full conformance
checks and settles their findings with the principal before the
release commit; for the engine that includes the `engine` check,
the core against itself and the forge intent. Which checks each
runs in full is its own definition's. The full check left the save
because it cost minutes and a walkthrough every time; the save is
meant to take seconds.

The rest run on the principal's word. The most expensive one, the
sweep of the whole operating layer for restatements, is run before
a major or after a round on the operating layer, never by a release
on its own.

Two things are deliberately not findings. The staleness of a render
is never a check finding, the README and the release notes
included: the release regenerates those two anyway, so the finding
was void at every release and noise everywhere else; the forge map
shows staleness instead. And a layer below the intent that a
project does not have is not missing: the checks say nothing of it.

## Why it is one mechanism with the critic and the challenger

Mechanical conformance runs on the same mechanism as the critic and
the challenger: its own contract skill, one agent per kind of check,
a roster, a run by hand. The contract owns conduct and isolation,
the subject and its boundary, the way of working and the shape of
the output. A check's own definition owns only its Lens section: a
specialisation of the contract that may narrow what is read or make
a shared rule stricter, never rename, drop or duplicate a shared
rule or field. The protocol changes in the contract alone. The
mechanism takes further kinds of reviewer as they come.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Checks](../reference/checks.md): the checks and what each verifies.
