---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 711f107bc28b2cc3
inputs:
  - .claude/skills/check/SKILL.md
  - .claude/skills/check-contract/SKILL.md#Output
---

# Check conformance

This page shows how to run a check with `/check`: a read-only
verification that a project or the engine follows the conventions of
the forge. It is for anyone who keeps a project or the engine and
wants to know where it departs from those conventions. Terms of the
forge are explained in the [Glossary](../reference/glossary.md).

## When to use it

Use it when you want a mechanical answer to the question "does this
follow the conventions?". A check judges conformance only. It does
not judge the substance of the thinking or the quality of a document;
other commands do that. Nothing runs on Claude's own judgement: a
check runs when you ask for it, or when a save or a release runs it.
Which checks a save and a release run is said by those two commands.
After an upgrade, see [Upgrade the engine](upgrade-the-engine.md).

## The command

Bare, the command lists the checks:

```
/check
```

With a check, it runs that check:

```
/check light my-project
```

The form is `/check [check] [slug]`. The slug names a project. The
engine's own project is `forge`, so `/check light forge` checks it.
The engine itself is checked as `/check engine`, with no slug. Which
of the two targets a check takes, and what a missing or an added slug
means to it, is said by the check itself. The checks that exist today
are in [Checks](../reference/checks.md).

## What happens

1. Bare `/check` lists the available checks, each with the moment it
   fits, and recommends one for now. You should now see the roster
   and one recommendation, which you are free to ignore.
2. With a check, Claude first remakes the target's ledger (the file
   that holds the state of the project), so that the check reads a
   current file. You should now see the ledger refreshed before the
   check starts.
3. Claude starts one isolated subagent for the check (a helper that
   does not see your conversation) and gives it the target path and
   nothing else. The subagent only reads. It returns its report and
   writes no file. Several checks on one target may be started at
   once and awaited together.
4. When the report returns, Claude files it, but only when it has
   findings. It saves the report in the `reviews/` folder of the
   target project (for the engine, the folder of the forge's own
   project) under a unique dated name. Each new finding receives the
   next free finding number of that project. The ledger is remade so
   that the findings appear in it. Reports of several checks on one
   target are filed one after another. A report that says "conforms"
   is filed nowhere. You should now see the name of the filed report,
   or nothing filed if the target conforms.
5. Claude shows you the report as it came: a one-line verdict, then
   the findings in their ranking, each with its number. You should
   now see the verdict and the ranked findings.
6. Claude offers every finding marked "immediate fix" (pure
   bookkeeping) as one step. The fixes are applied on your word, and
   the findings are then marked resolved.
7. Claude closes by offering a walkthrough of the remaining findings
   (a list worked one item per message, with a verdict from you on
   each). See [Walk through a list](walk-through-a-list.md). Accepting
   a finding there writes the fix once, at the end of the round, and
   marks the finding resolved. A rule that is worth changing goes to
   the intent instead.

## What you have afterwards

- A filed, dated report in `reviews/`, when the check found anything.
- Findings with numbers, listed in the ledger.
- Immediate fixes applied, if you agreed to them.
- The remaining findings either settled in a walkthrough or left open.

Nothing blocks. A release may proceed with a finding parked.

## A worked example

You have a project `my-project` and you want to know whether it
follows the conventions.

```
/check
```

Claude lists the checks and recommends one. You pick the light check:

```
/check light my-project
```

Claude remakes the ledger of `my-project` and starts the check. The
report comes back with three findings. Claude files it in
`my-project/reviews/` and gives the findings their numbers. It shows
the verdict "3 findings" and the ranking. One finding is marked
"immediate fix", so Claude offers it as a step. You agree, and it is
applied and marked resolved. Claude then offers a walkthrough of the
other two. If the report had said "conforms", nothing would have been
filed.

## See also

- [Checks](../reference/checks.md): the checks of today.
- [Walk through a list](walk-through-a-list.md): settling the findings.
- [Upgrade the engine](upgrade-the-engine.md): the checks after an upgrade.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
