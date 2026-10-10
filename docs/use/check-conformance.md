---
generated: 2026-10-10
made: mirrored
inputs-hash: d8728b342ae3cf82
inputs:
  - .claude/skills/check/SKILL.md
  - .claude/skills/check-contract/SKILL.md
  - CLAUDE.md
---

# Check conformance

This page is for a user who wants to know whether a project, or the
engine itself, follows the conventions of the forge. It says how to
run `/check`, what comes back and what you do with it.

## What a check is for

A check verifies mechanical conformance: whether the files of a
target follow the current conventions of the engine. It never judges
substance (that is the challenger's work) and never document quality
(that is the critic's). If a document is wrong or unclear but
conforms, a check says nothing.

Each check is one isolated agent. It sees the target's documents only,
never your conversation, and it is read-only: it changes no document,
no ledger, no index. It returns its report, and the session files and
presents it.

## See the roster

Run `/check` with nothing after it. You get the list of available
checks, each with a line saying when it fits, and a recommendation of
which fits the moment. The recommendation is never a gate, and no
check runs unless you ask for it.

## Run a check

Run `/check <check> [slug]`.

- The target is a project, named by its slug, or the engine. The
  engine's own project is `forge`.
- Which of the two a check accepts, and what a missing or an added
  slug means to it, is stated by that check itself.
- More than one check may be launched on one target at once and
  awaited together.

## What happens when it returns

1. **Filing.** If the report has findings, the session files it in the
   project's `reviews/` folder as `YYYY-MM-DD-check-<name>.md` (a
   `-2` suffix if one exists for today), with the agent's text word
   for word. Each new finding is given its next `FND` number, and a
   row is added to the ledger's Findings table with the category
   `conformance` and the state `open`. A finding the report names as
   reopened goes back to `open`. Reports of several checks are filed
   one after another, so that no number is given twice. A report that
   says "conforms" is filed nowhere.
2. **Presentation.** You see the one-line verdict, then the findings
   in their ranking, each with its number, compactly.
3. **Immediate fixes.** Every finding marked "immediate fix" (pure
   bookkeeping such as a stale version, a date or a count) is offered
   to you at once as one step. It is applied on your word and its
   state becomes `resolved`.
4. **Walkthrough.** The session then offers a walkthrough of the
   remaining findings. Accepting a finding there means the fix,
   agreed during the round and written once at its end, with the
   state `resolved`. If a rule itself is worth changing, the change
   goes to the intent, not into a check.

## Nothing blocks

A check is advisory. A release may proceed with a finding parked.
Which checks a save runs and which a release runs is for those
commands to say.

## See also

- [Checks](../reference/checks.md): the checks of today and what each verifies.
- [Walk through a list](walk-through-a-list.md): settling the findings.
- [Upgrade the engine](upgrade-the-engine.md): the checks as the migration tool after an upgrade.
