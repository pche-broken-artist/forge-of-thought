---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: bbac2779943b3611
inputs:
  - templates/check-definition.md
  - .claude/skills/check-contract/SKILL.md
  - .claude/skills/check/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a check

A check is one agent file that verifies one concern of the forge's conventions, and this page is for the extender who wants to add one. A check reads files and reports where they do not follow a rule. It judges neither substance nor quality. Terms of the forge are explained in the [Glossary](../reference/glossary.md).

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md). It says how a change is proved, recorded and released. A new check is recorded and released as any other change of the forge.

A new check is added only by the decision of the principal (the person whose thinking is being forged). It is added only where what it finds genuinely differs from what the existing checks find. Each check owns one concern and none another's. The checks that exist are listed in [Checks](../reference/checks.md), and what the shared contract owns is explained in [The check](../about/the-check.md).

## The files

One new file is needed:

- `.claude/agents/check-<name>.md`, made from the skeleton `templates/check-definition.md`.

Nothing else changes. The `/check` command finds checks by scanning the agent files, so it needs no edit. The shared behaviour is not written in the file, because the contract skill named in its front-matter supplies it. The file holds only the front-matter and a Lens section.

## Steps

1. Copy the skeleton to `.claude/agents/check-<name>.md`. Choose `<name>` as the one word for the concern the check owns.
2. Fill the front-matter:
   - `name`: `check-<name>`.
   - `description`: what the check verifies and when it fits, in one line. The roster shows this line, and the line is how a person picks a check.
   - `tools`: read-only tools only (`Read, Glob, Grep` in the skeleton).
   - `model`: `inherit`, so the check runs on the session model, which is the model of the conversation Claude is having with the principal.
   - `skills`: `check-contract`.
3. If the description contains a colon followed by a space, put the whole description in single quotes, and double any apostrophe inside it. Otherwise the agent does not register.
4. Delete the comment that the skeleton carries.
5. Write the Lens section in three parts:
   - What you read: a project, every project or the engine. Say how the target narrows it, and what a library reduces it to.
   - What you verify: the rules, each with its owner cited (a section of `CLAUDE.md`, a template or a position of the intent) and never restated. Say which states are a fact and not a finding, for example a project without a repository. A fact is reported in one line, once.
   - Cost: the scope the check reads. Name the files, or say honestly that it reads the whole.
6. Keep the Lens section a specialisation of the contract. It may narrow what is read or make a shared rule stricter. It must not rename, drop or repeat a shared rule or a field of the report.
7. Leave filing out of the file. The check writes nothing and returns its report, and the `/check` procedure files it. Whether a save or a release runs the new check is said in the definition of that command, so the check file does not say it.

## Prove it

Run the roster, which scans the agent files:

```
/check
```

You should now see the new check among the checks, with its description.

Run the check on the engine, then on a project:

```
/check <name>
/check <name> forge
```

Which of the two a check takes, and what a slug means to it, is said in its Lens section. For a check that takes the engine root, the form is `/check engine`, with no slug. You should now see a report that says "conforms" or lists findings with `file:line`, the rule and its owner, and one proposed fix each. A report that finds nothing is filed nowhere. A report with findings is filed by `/check` into the target project's `reviews/`.

## Record and release

Record the change and release it as [Make a change to the forge](how-a-change-is-made.md) says. The new check is part of the roster from that point on.

## A worked example

A check for one concern, here called `<name>`, begins as this file. The text in angle brackets is yours to fill.

```markdown
---
name: check-<name>
description: Check "<name>" - <what this check verifies, in one line>. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.
tools: Read, Glob, Grep
model: inherit
skills:
  - check-contract
---

## Lens

<What you read: the target, how a slug narrows it, what a library reduces it to.>

<What you verify: each rule with its owner cited, not restated.
What is a fact and not a finding.>

<Cost: the scope you read, named or whole.>
```

You should now see `.claude/agents/check-<name>.md` in the roster after `/check`.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The check](../about/the-check.md): what the contract owns.
- [Checks](../reference/checks.md): the checks that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
