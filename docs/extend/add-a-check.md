---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 48fd0608cdba88ad
inputs:
  - templates/check-definition.md
  - .claude/skills/check-contract/SKILL.md
  - .claude/skills/check/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a check

This page is for the extender who wants a new check. A check is an isolated reviewer that verifies one concern of mechanical conformance with the conventions, and a new one is added as a single agent file. The page says which file, what it holds and how to prove it works.

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md). It says how a change is proved, recorded and released. The new check is recorded and released as any other change of the forge.

Decide with the principal (the person whose thinking is forged) that the check is wanted. A new check is added only by the principal's decision, and only where what it finds differs from what the existing checks find. The existing ones are listed in [Checks](../reference/checks.md). Each check owns one concern and none another's, so a concern an existing check already covers is not a reason for a new one.

A check verifies conformance only. It never judges the substance of the thinking (that belongs to the challenger) and never the quality of a document (that belongs to the critic). What the shared behaviour of every check is, is described in [The check](../about/the-check.md). Terms of the forge are explained in [Glossary](../reference/glossary.md).

## The files

One file is added:

- `.claude/agents/check-<name>.md`: the agent file of the check, where `<name>` is the short name of the concern.

The file starts from the skeleton `templates/check-definition.md`. Nothing else changes. The `/check` command does not change: it finds the checks by scanning the agent files, so the new file appears in the roster by existing.

The file holds two things and nothing more: a front-matter and a Lens section. The shared behaviour (subject, way of working, report shape) is not written in the file. It comes from the contract skill `check-contract`, which the front-matter names and which is loaded into the agent when it runs.

## Steps

1. Copy `templates/check-definition.md` to `.claude/agents/check-<name>.md`.

2. Fill the front-matter. It has these fields:

   - `name`: `check-<name>`.
   - `description`: what the check verifies and when it fits, in one line. The roster printed by a bare `/check` is made from these descriptions, so the line must let a reader choose.
   - `tools`: read-only tools, `Read, Glob, Grep`.
   - `model`: `inherit`, so that the check runs on the model of the session.
   - `skills`: a list with `check-contract`.

   If the description contains a colon followed by a space, put the whole description in single quotes, and double any apostrophe inside. Otherwise the agent does not register.

3. Delete the comment that the skeleton carries.

4. Write the Lens section. It is the one section that is the check's own, and it has three parts:

   - What you read: a project, every project, or the engine; how the target narrows the reading; what a library reduces it to.
   - What you verify: the rules, each with its owner cited (a section of `CLAUDE.md`, a template, a position of the intent) and never restated; and what is a fact rather than a finding.
   - Cost: the scope the check reads, either named files or the whole, said honestly.

   The Lens section specialises the contract. It may narrow what is read or make a shared rule stricter. It never renames, drops or duplicates a shared rule or field. A change to the protocol is made in the contract alone.

5. Keep to one concern. A rule belongs in the Lens only if it is mechanical, has an owner elsewhere and fits the concern named in the description.

6. Leave out instance facts such as names, roles, addresses and hosts. A report is a public file, or may be quoted into one.

The check writes nothing. It returns its report in its final message, and the `/check` command files it, numbers each new finding and remakes the ledger. Whether a save or a release runs the new check is not decided in the agent file. It is said in the definition of the caller, that is the save or the release.

### A worked example

For a concern called `<name>`, the front-matter of the new file reads:

```
---
name: check-<name>
description: Check "<name>" — <what this check verifies, in one line>. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.
tools: Read, Glob, Grep
model: inherit
skills:
  - check-contract
---
```

Below it comes the heading `## Lens` with the three parts above, each filled for the concern: what the check reads, the rules it verifies with their owners cited, and the scope it costs.

## Prove it

Run the check on the engine. The engine takes no slug:

```
/check engine
```

Replace `engine` with `<name>` when the new check is the one to run:

```
/check <name>
```

If the Lens says the check takes a project, run it on a project by its slug:

```
/check <name> <slug>
```

You should now see the check in the roster printed by a bare `/check`, and a report of one line, either that the target conforms or how many findings it has. A report with findings is filed in the target's `reviews/` by the command. A report that says it conforms is filed nowhere.

Confirm also that each finding names a file and line, the rule it breaks with its owner, and one fix. A finding without them breaks the shape the contract gives.

## Record and release

The new agent file is a change of the forge. Record it and release it as the page [Make a change to the forge](how-a-change-is-made.md) describes. If a save or a release should run the new check, that is a further change to the definition of that command.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The check](../about/the-check.md): what the contract owns.
- [Checks](../reference/checks.md): the checks that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
