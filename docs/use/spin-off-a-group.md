---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 14758ff187899452
inputs:
  - .claude/skills/spinoff/SKILL.md
---

# Spin off a group

This page is for you, the principal (the person whose thinking is forged), when a requirement group of an assignment has grown into a project of its own. The command `/spinoff` splits that group out into a new project. The terms of the forge are explained in the [Glossary](../reference/glossary.md).

## When to use it

Use it when you have decided that one group of requirements should be delivered as its own project. Claude may tell you that a group looks ready. It never runs the command on its own judgement and never proposes and runs it in one step: it runs only on your explicit instruction.

## The command

```
/spinoff <project> <group> <slug>
```

- `<project>` is the source project that holds the group.
- `<group>` is the name of the requirement group.
- `<slug>` is the name of the new project.

## What happens

1. Claude lists the items of the group that will move. These are the requirements, out-of-scope items, constraints, assumptions, deliverables, open questions and success criteria of the group. You may adjust the list.

   You should now see the list of items, and you confirm it.

2. Claude creates the new project by the same procedure as `/new-project`, as a thought project. It makes files only and no git repository. Initialising the repository and adding a remote are your own one-off act afterwards. What the new project is made of is on the page [Start a project](start-a-project.md).

   You should now see the new project with its files in place.

3. Claude derives a short brief for the new project from the relevant parts of the source intent. The brief says why this became a project of its own and what it inherits. It is written in the language settled when the project was created. Claude presents it to you as a draft. On your word it is approved through the `/forge brief` procedure.

   You should now see the draft brief, and after your word the approved brief.

4. Claude mines the brief into the new project's intent through `/forge intent`. That creates the intent and keeps its record of what was mined from where.

   You should now see the new project's intent.

5. In the source project Claude records the spin-off in the source intent through `/forge intent`: the group's substance is now delivered by the new project. It then derives the change in the source assignment through `/forge assignment`. The moved items are marked superseded and never deleted. The group is replaced by one link item that says the group is delivered by project `<slug>` and points to its assignment. The command itself writes only one decision record, in the decisions file of the source project.

   You should now see the moved items marked superseded, the one link item and the decision record in the source project.

6. Claude updates both ledgers and reports the result.

   You should now see the report of what was done in each project.

## What you have afterwards

- A new thought project with an approved brief and an intent mined from it.
- The source assignment with the moved items superseded and one link item in their place.
- A decision record of the spin-off in the source project.
- Both ledgers current.

## A worked example

You say `/spinoff alpha reporting-tools reporting`. Claude lists the items of the group `reporting-tools` in project `alpha` and you remove one that stays behind. Claude creates `projects/reporting/`, drafts its brief from the intent of `alpha`, and you approve it. The intent of `reporting` is mined from the brief. In `alpha` the moved items become superseded, and one link item says the group is delivered by project `reporting`. A decision record notes the split. Last, both ledgers are updated and Claude reports.

## See also

- [Start a project](start-a-project.md): what the new project is made of.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
