---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 07e27ca3de1b5af0
inputs:
  - templates/check-definition.md
  - .claude/skills/check-contract/SKILL.md
  - .claude/skills/check/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a check

A check is a reviewer that verifies one concern of mechanical conformance with the conventions, and it is added as one agent file. This page is for the extender who wants a new check on the roster that `/check` lists.

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md). It says how a change is proved, recorded and released. The new check is recorded and released as any other change of the forge.

A new check is added only by the decision of the principal (the person whose thinking is forged). It is added only where what it finds genuinely differs from what an existing check finds. See [Checks](../reference/checks.md) for the checks that exist. See [The check](../about/the-check.md) for what the shared contract owns, so that your file does not repeat it.

One check owns one concern and no other check's concern.

## The files

You add one file and change none.

- `.claude/agents/check-<name>.md` is the agent file of the new check. The suffix after `check-` is the name of the check.
- `templates/check-definition.md` is the skeleton you start from.

The `/check` command is not changed. It finds the new check by scanning the agent files, so the roster grows by itself.

## Steps

1. Copy `templates/check-definition.md` to `.claude/agents/check-<name>.md`.
2. Fill the front-matter.
   - `name` is `check-<name>`.
   - `description` says what the check verifies and when it fits. The roster shows this line, so it is what lets a reader choose the check.
   - `tools` stays read-only: `Read, Glob, Grep`. A check changes nothing.
   - `model` is `inherit`, so that the check runs on the session model.
   - `skills` lists `check-contract`, which brings in the shared behaviour.
3. Quote the description if it holds a colon followed by a space. Put the whole description in single quotes and double any apostrophe inside it. Otherwise the agent does not register.
4. Delete the comment that the skeleton carries.
5. Write the Lens section in its three parts.
   - What you read: a project, every project or the engine. Say how the target narrows it and what a library reduces it to.
   - What you verify: the rules, each with its owner cited (a section of `CLAUDE.md`, a template or a position) and never restated. Say which states are a fact to report and not a finding.
   - Cost: the scope the check reads, either named files or the whole, stated honestly.
6. Leave out of the Lens section anything the contract already says. A Lens section may narrow what is read or make a shared rule stricter. It never renames, drops or repeats a shared rule or field.

The check does not write its report to a file. It returns the report, and the `/check` procedure files it, gives each new finding its number and adds it to the ledger.

Whether a save or a release runs the new check is for the definition of that caller to say. Adding the agent file does not put the check into either of them.

## Prove it

Run the check on the engine:

```
/check engine
```

Run it on a project, with a placeholder slug here:

```
/check <name> <project-slug>
```

Which of the two targets the check takes, and what a missing or an added slug means to it, is said in its Lens section. Use the one it declares.

You should now see a one-line verdict, either "conforms" or the number of findings. Findings come ranked, each with a place, the rule and its owner, and one proposed fix. A report that says "conforms" is filed nowhere.

Run bare `/check` as well. You should now see your check in the roster with its description.

## A worked example

This example is generic and invented. It shows the shape of a file, not a check that exists. The check `naming` verifies that the files of a target follow one naming convention.

File: `.claude/agents/check-naming.md`

```
---
name: check-naming
description: Check "naming" — verifies that file names follow the naming convention. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.
tools: Read, Glob, Grep
model: inherit
skills:
  - check-contract
---

## Lens

### What you read
The file names of one project, named by its path. Given the
engine root, the file names of the engine. A library is reduced to
its sources and research directories.

### What you verify
Each file name against the naming convention, which belongs to
its owner (<the section of CLAUDE.md that states it>). A project
with no sources directory is a fact, reported once in one line,
and not a finding.

### Cost
Directory listings only; no file is opened.
```

Then prove it with `/check naming <project-slug>`.

## Record and release

Record the addition and release it as any change of the forge, by the steps in [Make a change to the forge](how-a-change-is-made.md).

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The check](../about/the-check.md): what the contract owns.
- [Checks](../reference/checks.md): the checks that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
