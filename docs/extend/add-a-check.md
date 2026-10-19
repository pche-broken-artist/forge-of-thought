---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: a83ffcab8964a651
inputs:
  - templates/check-definition.md
  - .claude/skills/check-contract/SKILL.md
  - .claude/skills/check/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a check

This page shows an extender how to add a new check to the forge. A check is a reviewer that verifies one kind of mechanical conformance with the conventions, and it is added as one agent file.

## Before you start

A change to the forge is made, proved, recorded and released in one way, described in [Make a change to the forge](how-a-change-is-made.md). The new check is recorded and released as any change of the forge.

A new check is added only by the decision of the principal (the person whose thinking is being forged). It is added only where what it finds genuinely differs from what the existing checks find. [Checks](../reference/checks.md) lists the ones that exist, so read it first.

Each check owns one concern and none another's. If your idea mixes two concerns, it is two checks. If it judges whether a document is wrong, unclear or badly written, it is not a check at all: a check never judges substance or document quality.

Terms of the forge are explained in [Glossary](../reference/glossary.md). What the shared contract of every check holds is described in [The check](../about/the-check.md).

## The files

You add one file and change no other.

- `.claude/agents/check-<name>.md`: the agent file of the new check. Its skeleton is `templates/check-definition.md`.

The command `/check` does not change. It finds the roster by scanning the agent files `.claude/agents/check-*.md` and reading their `description` fields.

## Steps

1. Choose the name. The file is `check-<name>.md` and the name is the suffix of the agent name.
2. Copy `templates/check-definition.md` to `.claude/agents/check-<name>.md`.
3. Fill the front-matter.
   - `name`: `check-<name>`.
   - `description`: what the check verifies and when it fits, in one line. The roster shows this line, so it is how a person picks the check. If the description contains a colon followed by a space, put the whole description in single quotes (an apostrophe inside is doubled), or the agent does not register.
   - `tools`: read-only tools (`Read, Glob, Grep` in the skeleton). A check changes nothing.
   - `model`: `inherit`, so the check runs on the model of the session.
   - `skills`: `check-contract`, the contract that carries the behaviour every check shares.
4. Delete the comments of the skeleton.
5. Write the Lens section, the only part of the file that is the check's own. It has three parts.
   - What the check reads: a project, every project, or the engine. Say how the target narrows it, and what a library reduces it to.
   - What the check verifies: the rules. Name the owner of each rule (a section of `CLAUDE.md`, a template, a position of the intent) and never restate the rule. Say which states are a fact and not a finding, if any.
   - Cost: the scope the check reads, either named files or the whole, stated honestly.
6. Leave the shared behaviour to the contract. The Lens section may narrow what is read or make a shared rule stricter. It may not rename, drop or duplicate a shared rule or field.

The check writes nothing. It returns its report, and the `/check` procedure files the report and gives each new finding its number. Whether a save or a release runs the new check is for the definition of that caller to say, so the check file does not decide it. Checks never call each other.

## Prove it

Run the check on the engine, which takes no slug:

```
/check engine
```

Then run the new check on a project, with a placeholder slug:

```
/check <name> <slug>
```

You should now see a report that opens with one line, either "conforms" or a count of findings. Each finding names a file and line, the rule with its owner, and one proposed fix. A run that finds nothing files nothing.

Which of the two targets a check takes, and what a missing or an added slug means to it, is said in its Lens section, so test the target your Lens names.

## Record and release

Record and release the new file as any change of the forge, as [Make a change to the forge](how-a-change-is-made.md) describes.

## A worked example

This example is generic. The check `<name>` verifies one concern, for instance that a kind of file carries a field its template requires.

1. Copy the skeleton to `.claude/agents/check-<name>.md`.
2. Set the front-matter:

```
---
name: check-<name>
description: Check "<name>" - <what it verifies, in one line>. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.
tools: Read, Glob, Grep
model: inherit
skills:
  - check-contract
---
```

3. Write the Lens section: the project it reads, the owner of the rule it verifies (cited, not restated), and the cost of its scope.
4. Run `/check engine`, then `/check <name> <slug>`.

You should now see the check in the bare `/check` roster, and its report on the target.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The check](../about/the-check.md): what the contract owns.
- [Checks](../reference/checks.md): the checks that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
