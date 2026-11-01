---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 6258e5c61608fbb4
inputs:
  - .claude/skills/check/SKILL.md
  - .claude/skills/check-contract/SKILL.md#Output
---

# Check conformance

This page shows how to run a check with `/check`, which verifies that a project or the engine follows the conventions of the forge. It is for the principal (whoever's thinking is being forged), who runs the command and settles what it finds. Terms of the forge are explained in the [Glossary](../reference/glossary.md).

## When to use it

Use it when you want to know whether the documents of a project, or the engine itself, still keep the mechanical rules: the conventions of names, headers, records and files. A check judges conformance only. It does not judge substance or the quality of a document; other commands do that.

Use it, for example, after an [upgrade of the engine](upgrade-the-engine.md), or at any moment you doubt the state of a project. No check runs on Claude's own judgement: you start it.

## The command

To see which checks exist and which fits the moment, type it bare:

```
/check
```

To run one check, name it and, for a project, its slug:

```
/check light my-project
```

The engine's own project has the slug `forge`, so its check is `/check light forge`. The engine root is the target of `/check engine`, with no slug.

Which of the two targets a check takes, and what a missing or an added slug means to it, is stated by that check. The [Checks](../reference/checks.md) page lists the checks of today.

## What happens

1. Bare `/check` lists the available checks, each with the line that says when it fits, and Claude recommends one for the moment. The recommendation is advice, never a gate.

   You should now see the roster and a recommended check.

2. With a check named, Claude first remakes the ledger of the target (the file that holds the state of a project, made at read time), so that the check reads a current one.

   You should now see Claude start the check on a freshly made ledger.

3. Claude hands the target to one isolated agent (a subagent that sees nothing of your conversation and only reads). The agent verifies the conformance and returns its report. It writes no file.

   You should now see the agent return its report, which opens with a one-line verdict.

4. If the report has findings, Claude files it in the `reviews/` folder of the target project (`projects/forge` for the engine) under a unique dated name. Each new finding receives its `FND` number there. A report that says the target conforms is filed nowhere.

   You should now see the name under which the report was filed.

5. Claude presents the report: the verdict line, then the findings ranked by severity with their numbers.

   You should now see the ranked findings, compactly.

6. Claude offers every finding marked "immediate fix" (pure bookkeeping) at once, as one step. It applies them on your word and marks them resolved.

   You should now see the immediate fixes applied and marked resolved.

7. Claude ends by offering a [walkthrough](walk-through-a-list.md) of the remaining findings: one finding per message, each closed by the verdict line. What `accept` writes here is the fix, agreed and written once at the end of the round, and the finding is marked resolved. A rule worth changing goes to the intent of the forge. The other verdicts are those of the walkthrough.

   You should now see the first remaining finding, with the verdict line.

Several checks on one target may run at once. Claude launches them together and waits for all of them.

## What you have afterwards

- A report in `reviews/`, only if the check had findings.
- A number for each new finding.
- The ledger remade, so that it shows the findings.
- Fixes applied for the immediate ones, and for those you accepted in the walkthrough.

## If something goes wrong

Nothing blocks. A finding that you park does not stop a release: a release may go ahead with a finding left open.

Which checks a save and a release run is stated by those commands, not by this one.

The sources do not record what the command prints when the ledger cannot be made.

## A worked example

You have changed a few documents of a project with the placeholder slug `my-project` and want to know whether they keep the conventions.

1. You type `/check`. Claude lists the checks and recommends `light` as the fit.
2. You type `/check light my-project`. Claude remakes the ledger of `my-project` and starts the check.
3. The agent returns a report with three findings. Claude files it in `reviews/` of `my-project` and numbers the three findings.
4. Claude shows the verdict line and the three findings, most severe first. One is marked "immediate fix". Claude offers it as one step. You accept, and it is applied and marked resolved.
5. Claude offers a walkthrough of the other two. You accept one and park the other. The parked finding stays open and blocks nothing.

## See also

- [Checks](../reference/checks.md): the checks of today.
- [Walk through a list](walk-through-a-list.md): settling the findings.
- [Upgrade the engine](upgrade-the-engine.md): the checks after an upgrade.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
