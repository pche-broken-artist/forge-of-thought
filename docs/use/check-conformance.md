---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: c611006cfa966f69
inputs:
  - .claude/skills/check/SKILL.md
  - .claude/skills/check-contract/SKILL.md#Output
---

# Check conformance

This page shows how you run a check with `/check`: a read-only test that a project or the engine follows the conventions of the forge. It is for the user who wants to know what a check does, what Claude does with its result and what stays up to you. The principal is the person whose thinking is being forged, and the one who decides on every finding.

## When to use it

Use it when you want to know whether a project or the engine conforms to the conventions, for example before a save or a release, or after [upgrading the engine](upgrade-the-engine.md). A check looks at mechanical conformance only. It never judges substance or the quality of a document. Claude never runs a check on its own judgement: you ask for it.

## The command

Bare, `/check` lists the checks:

```
/check
```

To run one check on a project, give its name and the project's slug:

```
/check light my-project
```

The engine's own project is `forge`, so its check is typed `/check light forge`. To check the engine itself, give no slug:

```
/check engine
```

Which of the two targets a check takes, and what a missing or an added slug means to it, is stated by that check. The page [Checks](../reference/checks.md) lists the checks of today and what each verifies.

## What happens

1. **The roster.** Bare `/check` lists the available checks, each with the moment it fits, and Claude recommends one for the present moment. The recommendation is never a gate.
   You should now see a list of checks and one recommended.
2. **The run.** With a check and a target, Claude starts one subagent (an isolated agent that does not see your conversation) for that check. It gets the target path and nothing else. The agent only reads and writes no file. More than one check on one target may run at once and are awaited together.
   You should now see the checking agent's report come back.
3. **Filing.** When the report has findings, Claude files it in the `reviews/` directory of the target project (for the engine, in the `forge` project), as a dated file. If one exists for today, the name gets the suffix `-2`. The agent's text is kept word for word. Only the finding IDs are added: each new finding gets the next free `FND` number of the project. Claude also adds a row per new finding to the ledger (the file that holds the state of the project) with the category `conformance` and the state `open`. A finding the report names as reopened goes back to `open`. Reports of several checks on one target are filed one after another so that no ID is given twice. A report that says "conforms" is filed nowhere.
   You should now see the new report file in `reviews/` and the new rows in the ledger, or nothing filed if the target conforms.
4. **The report to you.** Claude presents the report as it came: the one-line verdict, then the findings in their ranking with their IDs.
   You should now see the verdict and the ranked findings.
5. **The immediate fixes.** Claude offers every finding marked "immediate fix" at once, as one step. It applies them on your word and sets their state to `resolved`.
   You should now see the offer of one step with the fixes, and after your word the fixes applied.
6. **The rest.** Claude ends by offering a walkthrough of the remaining findings. A walkthrough works a list one item per message, and you give a verdict on each. See [Walk through a list](walk-through-a-list.md). On `accept` the fix is agreed in the conversation and written once at the end of the round, with the state `resolved`. The other verdicts are those of the walkthrough.
   You should now see the first remaining finding, with the verdict line.

## What you have afterwards

- A dated report in `reviews/`, if there were findings.
- A row per finding in the ledger, with the state you settled it to.
- Fixes applied for what you accepted.

Nothing blocks. A release may go ahead with a finding parked. When a finding shows that a rule itself is worth changing, the rule goes to the intent, not to a fix.

A save and a release each run their own checks. Which ones is stated by `/save` and `/release`, not here.

## If something goes wrong

- A check that takes only a project given the engine, or the reverse, is answered by that check as its own description says. Read it on the page [Checks](../reference/checks.md).
- Two checks that finish on one target are filed one after another. This is done to keep the IDs unique, not because of an error.
- A report that says "conforms" produces no file. This is the normal result, not a failure.

## A worked example

You have a project `my-project` and want to know whether it conforms.

1. You type `/check light my-project`.
2. Claude starts the check agent. The agent returns a report: "2 findings".
3. Claude files it as `reviews/2026-10-11-check-light.md` in `my-project`, gives the findings `FND` numbers in the project's sequence, and adds two `open` rows to the ledger.
4. Claude presents the verdict and the two findings in ranking. One is marked "immediate fix".
5. Claude offers that fix as one step. You say yes, and its state becomes `resolved`.
6. Claude offers a walkthrough of the second finding. You accept it, and at the end of the round the fix is written and the state set to `resolved`.

## See also

- [Checks](../reference/checks.md): the checks of today and what each verifies.
- [Walk through a list](walk-through-a-list.md): settling the findings.
- [Upgrade the engine](upgrade-the-engine.md): the checks as the migration tool after an upgrade.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
