---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/check/SKILL.md
  - .claude/skills/check-contract/SKILL.md
  - CLAUDE.md
---

# Check conformance

This page is for a user who wants to know whether a project, or the
engine itself, follows the conventions of the forge. It says how to
run `/check`, what you see and what you do with the result.

A check verifies mechanical conformance only: whether the files
follow the conventions. It never judges substance (that is
`/challenge`) or the quality of a document (that is `/critique`). A
document that is wrong or unclear but conforms is not a finding.

## See which checks exist

Type `/check` with nothing after it. You get the roster: every
available check, each with a line saying when it fits, and a
recommendation of which fits the moment. The recommendation is
advice, not a gate. No check runs unless you ask for it.

## Run a check

Type `/check <check> [slug]`.

- The target is a project, named by its slug, or the engine. The
  engine's own project is `forge`.
- Which of the two a check takes, and what a missing or an added
  slug means to it, is stated by that check. The roster tells you
  when each fits.
- More than one check on the same target may be started together.

The check runs as one isolated agent. It sees only the target's
files, never your conversation, and it is read-only: it changes no
document, no ledger and no index. It returns its report to the
session.

## What you see

1. **The report is filed, if it has findings.** It goes into the
   target project's `reviews/` folder, named
   `YYYY-MM-DD-check-<name>.md`. A report that says "conforms" is
   filed nowhere.
2. **Each new finding gets its number**, the next free `FND.NNNN` of
   the project, and a row in the ledger's Findings table in state
   `open`. A finding that was filed before and stands again is
   reported under its old number; if it had been resolved, it goes
   back to `open`.
3. **The findings are presented**, as they came: a one-line verdict,
   then the findings ranked by severity, each with its place in the
   files, the rule it breaks and one proposed fix.
4. **Every "immediate fix" is offered at once** as a single step.
   These are pure bookkeeping, such as a stale version, a date or a
   count. They are applied on your word and marked `resolved`.
5. **A walkthrough of the rest is offered.** Findings are settled one
   at a time. Accepting one means the fix is agreed and written once
   at the end of the round, then marked `resolved`. The other
   verdicts are those of the walkthrough.

## What to do with a finding

- Settle it in the walkthrough, as above.
- If the rule itself is worth changing, the change goes to the
  intent. A check does not tighten rules.
- A finding already decided as rejected is not raised again.

Nothing blocks. A release may go ahead with a finding left parked.

## Checks inside a save and a release

`/save` and `/release` each run certain checks themselves. Which ones
is stated by those commands, not by `/check`.

## See also

- [Checks](../reference/checks.md): the checks of today and what each verifies.
- [Walk through a list](walk-through-a-list.md): settling the findings.
- [Upgrade the engine](upgrade-the-engine.md): the checks as the migration tool after an upgrade.
