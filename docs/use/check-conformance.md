---
generated: 2026-10-09
made: mirrored
inputs-hash: 9ca7bc50eeee551b
inputs:
  - .claude/skills/check/SKILL.md
  - .claude/skills/check-contract/SKILL.md
  - CLAUDE.md
---

# Check conformance

This page is for the person who wants to know whether a project, or
the engine itself, follows the conventions of the forge. `/check`
runs a check that verifies this and nothing else, and it settles
what the check finds with you.

## What a check is

A check verifies mechanical conformance: whether the files of a
target follow the current conventions. It never judges substance
(that is `/challenge`) or document quality (that is `/critique`). A
document that is wrong or unclear but conforms is not its business.

Each check owns one concern and none another's. It runs as an
isolated agent that sees the project's documents only, never your
conversation, and it is read-only: it changes no document, no
ledger and no index. It returns a report, and the session does the
rest.

## See the roster

Type `/check` with nothing after it. You get the list of available
checks, each with a line saying when it fits, and a recommendation
of which one suits the moment. The recommendation is never a gate,
and no check runs unless you ask for it. The checks of today and
what each verifies are on [Checks](../reference/checks.md).

## Run a check

Type `/check <check> [slug]`.

- The target is a project, named by its slug, or the engine root.
  The engine's own project is `forge`.
- Which of the two a check takes, and what a missing or an added
  slug means to it, is that check's own to say.
- More than one check on the same target may be launched at once and
  awaited together.

## What happens when the check returns

1. **Filing.** If the report has findings, the session files it in
   the target project under `reviews/`, as a dated file named for
   the check (for the engine, in `projects/forge`). It gives each
   new finding its next free `FND` number and adds a row for it to
   the ledger's Findings table, state `open`. A finding the report
   names as already known keeps its number; one that had been
   resolved and stands again goes back to `open`. A report that says
   the target conforms is filed nowhere. Reports of several checks
   on one target are filed one after another, so no number is given
   twice.
2. **Presenting.** You get the one-line verdict, then the findings
   in their ranking with their numbers, compactly.
3. **Immediate fixes.** Every finding marked "immediate fix" (pure
   bookkeeping such as a stale version, a date or a count) is
   offered at once as a single step. It is applied on your word and
   its state becomes `resolved`.
4. **The rest.** The session ends by offering a walkthrough of the
   remaining findings. Accepting a finding means the fix is agreed
   in the walkthrough and written once at the round's end, state
   `resolved`. How a walkthrough runs is on
   [Walk through a list](walk-through-a-list.md).

A finding already decided in the project's decision record is not
raised again, and a finding already filed is reported under the
number it has.

## When a rule itself is wrong

A check enforces the rules as they stand. If a rule is worth
changing or tightening, that is a matter for the intent, not for the
check: the fix goes there.

## Nothing blocks

Checks are advisory. A release may proceed with a finding parked.
Which checks a save runs and which a release runs is for those
commands to say, not for `/check`; a check on its own never runs on
Claude's initiative. After an upgrade of the engine the checks also
serve to find what no longer conforms; see
[Upgrade the engine](upgrade-the-engine.md).

## See also

- [Checks](../reference/checks.md): the checks of today and what each verifies.
- [Walk through a list](walk-through-a-list.md): settling the findings.
- [Upgrade the engine](upgrade-the-engine.md): the checks as the migration tool after an upgrade.
