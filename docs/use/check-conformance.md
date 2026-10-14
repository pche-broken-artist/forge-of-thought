---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: d704dc9abf6fc244
inputs:
  - .claude/skills/check/SKILL.md
  - .claude/skills/check-contract/SKILL.md#Output
---

# Check conformance

This page shows how you run a check with `/check`: an isolated agent that verifies, mechanically, that a project or the engine follows the conventions. It is for you, the person who runs the forge and wants to know whether the documents conform. A check never judges substance or the quality of a document.

## When to use it

- You want to know whether a project, or the engine, conforms with the conventions.
- You have upgraded the engine and want the checks to show what needs migrating (see [Upgrade the engine](upgrade-the-engine.md)).
- You are about to save or release and want a check beforehand. A save and a release run their own checks, and what each runs is defined by those commands.

Nothing blocks: a release may proceed with a finding parked.

## The command

Bare, the command lists the roster of checks and recommends which fits the moment:

```
/check
```

With a check name, it runs that check. The target is a project by its slug, or the engine root. Which of the two a check takes is stated in the check's own definition.

```
/check light forge
/check engine
```

The first line checks the engine's own project (slug `forge`). The second checks the engine itself and takes no slug. The checks of today are listed in [Checks](../reference/checks.md). A term you do not know is in the [Glossary](../reference/glossary.md).

## What happens

1. Bare `/check`: Claude lists the checks, each with the line saying when it fits, and recommends one. It runs none on its own judgement.

   You should now see the roster and one recommendation.

2. `/check <name> [slug]`: Claude starts the check as a subagent (an isolated agent that does not see your conversation). It receives the target path and nothing else. The agent is read-only: it writes no file and returns its report.

   You should now see Claude waiting for the report. Several checks on one target may be started at once.

3. The report comes back. When it has findings, Claude files it in the target project as a file in `reviews/`, named `YYYY-MM-DD-check-<name>.md`, with `-2` added if one exists for today. The text is the agent's, word for word. Each new finding is given its next free `FND` number, and a row is added to the ledger's Findings table with the state `open`. A finding the report names as reopened goes back to `open`. A report that says "conforms" is filed nowhere.

   You should now see a new file in `reviews/` and new rows in the ledger, or no file at all if the report said "conforms".

4. Claude presents the report as it came: the one-line verdict, then the findings in their ranking with their numbers, compactly.

   You should now see the verdict and the ranked findings.

5. Claude offers every finding marked "immediate fix" at once, as one step. It applies them on your word and sets them to `resolved`.

   You should now see one offer covering all the immediate fixes.

6. Claude ends by offering a walkthrough of the remaining findings. A walkthrough settles a list one item per message (see [Walk through a list](walk-through-a-list.md)). An accepted finding is fixed as agreed, written once at the end of the round, and set to `resolved`. A rule that is worth changing goes to the intent. The other verdicts are the walkthrough's.

   You should now see the offer of a walkthrough, or nothing more if every finding was an immediate fix.

## What you have afterwards

- The verdict and the ranked findings, presented in the conversation.
- When there were findings, a report in the project's `reviews/` and a row per finding in the ledger.
- Fixes applied and findings set to `resolved` where you agreed them.
- Findings you parked stay in the ledger.

## If something goes wrong

- A check that finds nothing says "conforms" and files nothing. That is the normal result, not a failure.
- If you name a check that does not exist, run bare `/check` for the roster.
- A missing or an added slug can mean something different to each check. Read the check's definition, or its line in [Checks](../reference/checks.md).
- A library has no Findings table and no `reviews/` folder until its first finding. Claude adds both then.

## A worked example

You have edited a project, `my-project`, and want to know whether it conforms. You type:

```
/check light my-project
```

Claude starts the check agent on `projects/my-project`. The agent returns "2 findings". Claude files the report as `projects/my-project/reviews/YYYY-MM-DD-check-light.md`, giving the findings the next free numbers in the project's sequence, and adds two rows to the ledger with the state `open`.

Claude presents the verdict and the two findings in rank. One is marked "immediate fix", a pure bookkeeping correction. Claude offers it as one step. You agree, and Claude applies it and sets the finding to `resolved`.

Claude then offers a walkthrough of the other finding. You park it. It stays `open` in the ledger, and you may save or release with it parked.

## See also

- [Checks](../reference/checks.md): the checks of today.
- [Walk through a list](walk-through-a-list.md): settling the findings.
- [Upgrade the engine](upgrade-the-engine.md): the checks as the migration tool after an upgrade.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
