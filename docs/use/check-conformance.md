---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: c3a72b0e1797952a
inputs:
  - .claude/skills/check/SKILL.md
  - .claude/skills/check-contract/SKILL.md#Output
---

# Check conformance

This page shows how to run `/check`, the command that has an isolated, read-only agent verify that a project or the engine follows the forge's conventions. It is for you, the principal (the person whose thinking is forged), when you want to know whether the documents are in the shape the conventions ask for. A check judges conformance only. It never judges substance or the quality of the writing.

## When to use it

- You want to see which checks exist and which one fits the moment.
- You want the mechanical conventions of a project verified before you save or release it.
- You have upgraded the engine and want to see that the project still conforms (see [Upgrade the engine](upgrade-the-engine.md)).

Nothing blocks. A release may go ahead with a finding parked, and no check runs unless you ask for it.

## The command

To see the roster of checks and a recommendation for the moment:

```
/check
```

To run one check on the engine's own project:

```
/check light forge
```

To run one on a project of yours, give the check and the slug:

```
/check light my-project
```

To run one on the engine itself, give no slug:

```
/check engine
```

Which of the two targets a check takes, and what a missing or an added slug means to it, is stated by the check itself. The roster says when each check fits, and [Checks](../reference/checks.md) lists the checks of today.

## What happens

1. Bare `/check` lists the checks, each with the line that says when it fits, and recommends one. The recommendation is not a gate.
   You should now see the roster and one recommended check.
2. With a check named, Claude first remakes the target's ledger, so that the agent reads a current file. The ledger is the single source of truth for state, made from the documents at the moment it is read.
   You should now see the ledger rebuilt for the target.
3. Claude starts the check as a subagent, an isolated agent that sees nothing of your conversation. It receives the target path and nothing else. It reads the target, writes no file and returns a report. You may start several checks on one target at once, and Claude waits for all of them.
   You should now see the report come back, headed by one line: either "conforms" or the number of findings.
4. If the report has findings, Claude files it in the `reviews/` folder of the target project (for the engine, that of `projects/forge`) under a unique dated name. It gives each new finding the next free finding number of the project, and a finding that is already known keeps the number it has. A report that says "conforms" is filed nowhere.
   You should now see the filed report, and the ledger rebuilt so that the findings appear in it.
5. Claude presents the report as it came: the one-line verdict, then the findings in their ranking with their numbers, compactly.
   You should now see the ranked findings.
6. Claude offers every finding marked "immediate fix" as one step. These are findings of pure bookkeeping. On your word it applies them and marks the findings `resolved`.
   You should now see those findings resolved.
7. Claude offers a walkthrough of the remaining findings. In a walkthrough Claude takes one item per message and you answer each with a verdict. The method is described in [Walk through a list](walk-through-a-list.md). Here `accept` means that the fix is agreed and is written once at the end of the round, with the finding marked `resolved`. A rule that is worth changing goes to the intent, the document where your positions on the forge are kept. The other verdicts are the walkthrough's.
   You should now see the first remaining finding, with the verdict line.

## What you have afterwards

- A report in `reviews/` under a unique dated name, if there were findings. It is immutable once filed.
- A finding number on every new finding, and the ledger rebuilt so that it lists them.
- Findings resolved, or parked, or under a verdict of the walkthrough.
- Nothing, when the check conforms: no file is written.

## If something goes wrong

- A check does not run on Claude's own judgement. If you did not ask for one, none ran.
- A check cannot repair anything. It writes no file, and fixes happen only on your word, in step 6 or in the walkthrough.
- A finding that concerns substance or the quality of the writing is not a check's business. Those belong to `/critique` and `/challenge`.
- A finding does not stop a save or a release. You may park it and go on.

## A worked example

You have finished a round on a project with the slug `my-project`, and you want to know whether its documents conform.

```
/check
```

Claude lists the checks and recommends `light`, since you want a quick pass over the project. You then type:

```
/check light my-project
```

Claude rebuilds the ledger of `my-project` and hands the target to the `light` check. The report comes back with three findings, one of them an immediate fix. Claude files it in `projects/my-project/reviews/` under a dated name and numbers the three findings. It shows you the verdict "3 findings" and the ranked list, then offers the immediate fix as one step. You answer `accept`, and that finding is resolved. Claude offers a walkthrough of the other two. You take the first, answer `accept`, and park the second. A release now may proceed with the parked finding standing.

## See also

- [Checks](../reference/checks.md): the checks of today.
- [Walk through a list](walk-through-a-list.md): settling the findings.
- [Upgrade the engine](upgrade-the-engine.md): the checks after an upgrade.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
