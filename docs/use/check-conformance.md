---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: e1ec550d63395b2f
inputs:
  - .claude/skills/check/SKILL.md
  - .claude/skills/check-contract/SKILL.md#Output
---

# Check conformance

This page shows how to run a check with `/check`: a read-only test that a project or the engine follows the conventions of the forge. It is for the user, that is the principal, the person whose thinking is forged (terms of the forge are in the [Glossary](../reference/glossary.md)).

## When to use it

Use it when you want to know whether a project or the engine still keeps the mechanical rules: names, headers, registrations and the like. A check never judges substance or the quality of a document. Nothing blocks: a finding may stay open and a release may go ahead.

## The command

Bare, it lists the checks:

```
/check
```

With a check and a target, it runs one:

```
/check light forge
```

`forge` is the slug of the engine's own project. For a project of yours, put its slug in its place, for example `/check light my-project`. For the engine itself, there is no slug:

```
/check engine
```

Which target a check takes, and what a missing or an added slug means to it, is said by the check itself. The checks of today are on the [Checks](../reference/checks.md) page.

## What happens

1. Bare `/check` lists the checks, each with the moment it fits, and recommends one. You should now see the roster and a recommendation. No check runs unless you ask for it.
2. With a check named, Claude first makes the target's ledger again (the file that holds the current state of a project, made when it is read), so that the check reads a current file. You should now see the ledger rebuilt.
3. Claude starts the check as a subagent (a helper that runs on its own and never sees your conversation). It gets the target and nothing else. It reads and writes nothing. It returns a report. You should now see the check return a verdict of one line.
4. When the report has findings, Claude files it in the project's `reviews/` folder under a unique dated name and gives each new finding its number. A report that says the target conforms is filed nowhere. You should now see the file name and the numbers.
5. Claude presents the findings to you as they came, the verdict first, then the findings ranked by severity with their numbers.
6. Claude offers every finding marked as an immediate fix (pure bookkeeping) at once, as one step. It applies them on your word and marks them resolved. You should now see those findings resolved.
7. Claude closes by offering a walkthrough of the rest, one finding at a time. How that goes is on the [Walk through a list](walk-through-a-list.md) page. Accepting a finding means the fix is agreed here and written once at the end of the round. If a rule itself is worth changing, the change goes to the intent.

Several checks on one target may run at once. Claude waits for all of them.

## What you have afterwards

- A report in `reviews/`, when there were findings, and a rebuilt ledger that cites it.
- Findings resolved, parked or waiting for your walkthrough.
- No change to any document apart from what you accepted.

A save and a release each run their own checks; which ones is for `/save` and `/release` to say, not for this command. After an upgrade of the engine the checks are offered too: see [Upgrade the engine](upgrade-the-engine.md).

## If something goes wrong

- A check that finds nothing prints that the target conforms and files nothing. That is not an error.
- A library has no `reviews/` folder until its first finding. Claude creates it then.
- A finding you do not want to fix now can be parked. It blocks nothing.

## A worked example

You have just reorganised a project with the slug `my-project` and want to know whether it still conforms.

```
/check light my-project
```

Claude rebuilds the ledger and starts the check. The check returns "2 findings". Claude files the report in `reviews/` and gives the two findings numbers. It shows you a high finding and a low one. The low one is an immediate fix, so Claude offers it as one step. You agree and it is applied. Claude then offers a walkthrough of the high finding. You walk through it and decide.

## See also

- [Checks](../reference/checks.md): the checks of today.
- [Walk through a list](walk-through-a-list.md): settling the findings.
- [Upgrade the engine](upgrade-the-engine.md): the checks after an upgrade.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
