---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: c0e52447fdc9e215
inputs:
  - templates/check-definition.md
  - .claude/skills/check-contract/SKILL.md
  - .claude/skills/check/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a check

This page shows how to add a new check to the forge. A check is an isolated reviewer (a subagent: a Claude run that sees nothing of the working conversation) that verifies mechanical conformance with the conventions. A new check is one agent file. The page is for the extender who has decided, together with the principal (the person whose thinking is forged), that a concern needs a check of its own. Terms of the forge are explained in the [Glossary](../reference/glossary.md).

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md). It describes how a change is proved, recorded and released. A new check is recorded and released as any other change of the forge.

Two conditions come first:

- A new check is added only by the principal's decision, and only where what it finds genuinely differs from the existing checks.
- A check owns one concern and none another's. If the rule you have in mind belongs to a concern an existing check already owns, it does not need a new check. The existing ones are listed on [Checks](../reference/checks.md).

What a check is, and what its contract already owns, is explained on [The check](../about/the-check.md). You do not repeat any of it in the new file.

## The files

You add one file:

- `.claude/agents/check-<name>.md`: the agent file of the check. `<name>` is the short name of the concern.

You start from the skeleton `templates/check-definition.md`. Nothing else changes: the `/check` command finds a check by scanning `.claude/agents/` for `check-*.md`, so no list needs an entry.

## Steps

1. Copy `templates/check-definition.md` to `.claude/agents/check-<name>.md`.
2. Fill the front-matter:
   - `name`: `check-<name>`.
   - `description`: what the check verifies, in one line, and when it fits. The roster of `/check` shows this line, so the principal chooses a check by it.
   - `tools`: read-only tools only (the skeleton gives `Read, Glob, Grep`).
   - `model`: `inherit`, so the check runs on the model of the session.
   - `skills`: `check-contract`, which carries the behaviour every check shares.
3. If the description contains a colon followed by a space, put the whole description in single quotes (an apostrophe inside is doubled). Otherwise the agent does not register.
4. Delete the comment in the skeleton.
5. Write the `## Lens` section, the only section of the file that is the check's own. It has three parts:
   - What you read: a project, every project or the engine; how the target narrows it; what a library reduces it to.
   - What you verify: the rules, each with its owner cited (a section of `CLAUDE.md`, a template, a position of the intent) and never restated. It also says what is a fact and not a finding.
   - Cost: the scope the check reads, either named files or the whole, said honestly.
6. Leave out of the file anything the contract already says. A Lens section narrows or tightens a shared rule. It never renames, drops or duplicates one.

The check writes nothing. It returns its report, and the `/check` procedure files it and numbers its findings.

Whether a save or a release runs the new check is not decided in the check file. It is said by the definition of the caller, `/save` or `/release`. Until a caller names it, the check runs only when someone calls it by hand.

## Prove it

Run the check on the engine. The command is typed as it stands:

```
/check <name>
```

For the engine, the command takes no slug. Which targets a check takes, and what a slug means to it, is said in its Lens section. A check that works on a project is run with the slug of that project:

```
/check <name> <slug>
```

You should see the check listed in the roster that bare `/check` prints, with its description. A run should return either one line saying the target conforms, or a ranked list of findings, each with a place, the rule and its owner, and one proposed fix.

## Record and release

Record the change and release it as the page [Make a change to the forge](how-a-change-is-made.md) describes. The check is part of the next release like any other change.

## A worked example

A concern called `<name>` is to verify that every document of a project carries a given header field. The extender:

1. Copies the skeleton to `.claude/agents/check-<name>.md`.
2. Sets `name: check-<name>` and a one-line description that says what the check verifies and when it fits. The tools stay `Read, Glob, Grep`, `model: inherit` and `skills: check-contract` stay as they are.
3. Writes the Lens: it reads one project, and a library reduces the reading to its few files. It verifies the field against the template that defines it, cited by its path and not restated. A project without the field's owner is a fact, not a finding. The cost is the documents of the project, named.
4. Runs `/check <name>` and `/check <name> <slug>`, reads the reports, and brings the principal the file for the decision to release.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The check](../about/the-check.md): what the contract owns.
- [Checks](../reference/checks.md): the checks that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
