---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: a2acbfd1b9c41379
inputs:
  - .claude/skills/check/SKILL.md
  - .claude/skills/check-contract/SKILL.md#Output
  - .claude/agents/check-engine.md
  - projects/forge/10-intent.md#POS.1980
---

# Check conformance

This page shows how to run `/check`, the command that has one isolated
agent verify that a project or the engine conforms to the conventions.
It is for you when you want to know whether your documents keep the
rules before you save or release them. A subagent is a helper that Claude
starts with a task of its own and no view of your conversation.

## When to use it

- You want a mechanical test of conformance, not a judgement of
  quality or substance. Quality is the job of `/critique` and substance
  the job of `/challenge`.
- You want to know which checks exist: type `/check` alone.
- You have upgraded the engine and want to see that nothing drifted
  (see [Upgrade the engine](upgrade-the-engine.md)).

## The command

```
/check light my-project
```

The general form is `/check [check] [slug]`. Bare `/check` lists the
checks. For the roster itself see [Checks](../reference/checks.md).

The target is a project, named by its slug, or the engine root. Which of
the two a check takes, and what a missing or an added slug means to it,
is stated in that check's own definition. Two typed forms:

- `/check light forge` checks the engine's own project, whose slug is
  `forge`.
- `/check engine` checks the engine root and takes no slug.

The engine check reads the forge intent, so it needs the forge's own
project cloned beside the engine. Whoever develops the engine has it
cloned. A user who only cloned the engine does not have it, and does not
need the engine check (see
[Projects and the engine](../about/projects-and-the-engine.md)).

## What happens

1. Bare `/check` lists the checks, each with the description of when it
   fits, and Claude recommends the one that fits the moment.
   You should now see the roster and a recommendation, which is never a
   gate. No check runs on Claude's own judgement.
2. With a check named, Claude first remakes the target's ledger so that
   the agent reads a current file. The ledger is the file that holds
   the state of a project, made from its documents at the moment it is
   read.
   You should now see the ledger script finish before any check starts.
3. Claude starts the check's agent with the target path and nothing
   else. The agent only reads: it writes nothing. More than one check on
   one target may run at once, and Claude waits for all of them.
   You should now see the agent's report come back.
4. When the report has findings, Claude files it in the target
   project's `reviews/` under a unique dated name. It gives each new
   finding an ID, the next free number of the project, and leaves the
   agent's text otherwise as it came. For the engine the target project
   is `forge`. A report that says "conforms" is filed nowhere.
   You should now see the filed report named, and the ledger remade.
5. Claude presents the report as it came: the one-line verdict, then
   the findings in their ranking with their IDs.
   You should now see the verdict and the ranked findings.
6. Claude offers every finding marked "immediate fix" at once, as one
   step. A finding is marked so when the fix is pure bookkeeping. On your
   word Claude applies the fixes and marks those findings resolved.
   You should now see the fixed findings marked resolved.
7. Claude ends by offering a walkthrough of the remaining findings. A
   walkthrough is one item per message, each closed with a verdict line
   from which you choose (see
   [Walk through a list](walk-through-a-list.md)). An accepted finding
   is fixed, agreed in the conversation and written once at the end of
   the round, and marked resolved. A rule that is worth changing is
   taken to the intent instead.
   You should now see the first finding put to you with the verdict line.

## What you have afterwards

- A filed report in the target's `reviews/`, only if there were
  findings, with an ID on each finding.
- A ledger remade with those findings in it.
- Findings resolved, or parked, as you decided.

Nothing blocks. A release may go ahead with a finding parked. Which
checks a save and a release run is stated by those two commands, not
by `/check`.

## If something goes wrong

- The engine check finds nothing to read for the intent: the forge's own
  project is not cloned beside the engine. Clone it there, or leave this
  check to whoever develops the engine.
- A check asks for a slug it does not take, or lacks one it needs: the
  check's own definition says which, and its description shows when it
  fits. Run bare `/check` to read the descriptions.
- A check is not in the roster: a check exists only as an agent file
  of the engine. Adding one is a change of the engine, not an option of
  this command.

The reasons for these failures and the messages of the ledger script
are not recorded in the inputs of this page.

## A worked example

You have a project `my-project` and want to know whether it keeps the
conventions before a release.

1. You type `/check`. Claude lists the checks and recommends `light` for
   a project.
2. You type `/check light my-project`. Claude remakes the ledger of
   `my-project`, then starts the agent.
3. The agent returns "2 findings". One is marked "immediate fix". Claude
   files the report in `my-project/reviews/` and gives both findings an
   ID.
4. Claude shows the two findings, ranked, and offers the immediate fix
   as one step. You accept, and it is applied and marked resolved.
5. Claude offers a walkthrough of the other finding. You accept it,
   and at the end of the round the fix is written and the finding is
   marked resolved.

## See also

- [Checks](../reference/checks.md): the checks of today.
- [Walk through a list](walk-through-a-list.md): settling the findings.
- [Upgrade the engine](upgrade-the-engine.md): the checks after an
  upgrade.
- [Projects and the engine](../about/projects-and-the-engine.md): why
  the forge's own project is a repository of its own beside the engine.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
