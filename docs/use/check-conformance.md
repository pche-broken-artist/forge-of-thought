---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 086e3f1d255d8bce
inputs:
  - .claude/skills/check/SKILL.md
  - .claude/skills/check-contract/SKILL.md#Output
  - .claude/agents/check-engine.md
  - projects/forge/10-intent.md#POS.1980
---

# Check conformance

`/check` runs one check, an isolated read-only agent, against a project or against the engine and tells you where they depart from the conventions. This page is for you, the user, when you want to know whether a project or the engine still follows its own rules. A check verifies mechanical conformance only. It does not judge the substance of the thinking or the quality of the documents.

## When to use it

- You want to know which checks exist and which one fits the moment.
- You have changed a project or the engine and want its conformance verified.
- You have upgraded the engine and want to see that nothing drifted (see [Upgrade the engine](upgrade-the-engine.md)).

A save and a release run certain checks of their own. Which ones is defined by those two commands, not here. Running `/check` by hand is always your choice: Claude never runs a check on its own judgement.

## The command

To see the roster of checks and a recommendation of which fits:

```
/check
```

To run one check on a project, give the check and the project's slug:

```
/check light forge
```

To run the engine check on the engine itself, give no slug:

```
/check engine
```

Here `forge` is the slug of the forge's own project. Which of the two targets a check takes, and what a missing or an added slug means to it, is stated by the check itself. The checks of today are listed on [Checks](../reference/checks.md).

The engine check reads the forge intent, so it needs the forge's own project cloned beside the engine. Whoever develops the engine has it cloned there. See [Projects and the engine](../about/projects-and-the-engine.md) for why it is a repository of its own.

## What happens

1. **Bare `/check` lists the roster.** Claude shows each check with the line that says when it fits and recommends one. The recommendation is never a gate.
   You should now see the list of checks and one named as the fit.
2. **With a check, Claude first makes the target's ledger.** The ledger is the single record of a project's state, built from its documents each time it is read. Claude remakes it so that the agent reads a current file. For the engine the ledger is the one of the forge's own project.
   You should now see the ledger rebuilt without an error.
3. **One agent verifies the target.** Claude invokes the check's isolated subagent (a helper that sees none of your conversation) with the target path and nothing else. It reads only, writes nothing and returns its report. You may launch several checks on one target at once, and Claude awaits them together.
   You should now see the agent's report come back to Claude.
4. **Claude files the report, only when it has findings.** The report goes into the `reviews/` folder of the target project under a unique dated name. For the engine that is the forge's own project. Each new finding receives its own finding number from the project's sequence. A report that says the target conforms is filed nowhere.
   You should now see the path of the filed report, or the plain verdict that the target conforms.
5. **Claude presents the result.** It gives the one-line verdict, then the findings in their ranking with their numbers, compactly.
   You should now see the ranked findings.
6. **Claude offers the immediate fixes.** A finding marked "immediate fix" is pure bookkeeping. Claude offers all of them at once as one step and applies them on your word, marking them resolved.
   You should now see one proposal that holds every immediate fix.
7. **Claude offers a walkthrough of the rest.** A walkthrough takes the remaining findings one per message. See [Walk through a list](walk-through-a-list.md). What `accept` writes here is the fix, agreed during the round and written once at its end, with the finding resolved. A rule worth changing goes to the intent instead. The other verdicts are the walkthrough's own.
   You should now see the first remaining finding with the verdict line.

## What you have afterwards

- A filed report in the project's `reviews/` folder, when there were findings. The report is immutable once filed.
- The findings as rows of the ledger, remade after the filing.
- The immediate fixes applied and the findings you accepted resolved, once you have said so.

Nothing blocks. A release may go ahead with a finding parked.

## If something goes wrong

- **The engine check cannot read the forge intent.** The forge's own project is not cloned beside the engine. The check needs it, and only whoever develops the engine has it there.
- **The report says the target conforms.** Nothing is filed. This is the intended result, not a failure.
- **You expected a judgement of substance or style.** A check does not give one. The critique and challenge commands exist for that.

The inputs record no other stop conditions or messages for this command.

## A worked example

You have edited a project with the slug `my-project` and want to verify it with the check named `light`.

```
/check light my-project
```

Claude rebuilds the ledger of `my-project`, then runs the `light` check as an isolated agent. The agent returns a report of two findings. Claude files it in `my-project/reviews/` under a unique dated name and gives each finding its number. It presents the verdict "2 findings" and the two findings ranked by severity. One is marked "immediate fix". Claude offers that fix as one step, and you accept it. Claude then offers a walkthrough of the other finding, and you settle it with a verdict.

## See also

- [Checks](../reference/checks.md): the checks of today.
- [Walk through a list](walk-through-a-list.md): settling the findings.
- [Upgrade the engine](upgrade-the-engine.md): the checks after an upgrade.
- [Projects and the engine](../about/projects-and-the-engine.md): why the forge's own project is a repository of its own beside the engine.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
