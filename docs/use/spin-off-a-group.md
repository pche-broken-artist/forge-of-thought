---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: a9bf346fa01a46e6
inputs:
  - .claude/skills/spinoff/SKILL.md
---

# Spin off a group

This page is for the principal (whoever's thinking is being forged) who wants one requirement group of an assignment to become a project of its own. `/spinoff` splits that group out of its source project, creates the new project and leaves a link behind. Claude is the AI that runs the steps.

## When to use it

Use it when a group of requirements has grown into something that deserves its own chain of documents. The command runs only on your explicit instruction. Claude may point out that a group looks ready, but it never proposes and runs the split in one step.

## The command

```
/spinoff <project> <group> <slug>
```

- `<project>`: the source project that holds the assignment.
- `<group>`: the name of the requirement group to move.
- `<slug>`: the short name of the new project.

## What happens

1. Claude lists the items of the group that will move (requirements, out-of-scope items, constraints, assumptions, deliverables, open questions and success criteria). You may adjust the list.
   You should now see the list of items, and the scope confirmed by you.
2. Claude creates the new project as a thought project, in the way `/new-project` creates one. It makes files only. The new project's git repository and its remote are your one-off act afterwards.
   You should now see the new project folder with its files.
3. Claude derives a short brief for the new project from the relevant parts of the source intent. The brief says why this became its own project and what it inherits. It is written in the language settled in step 2. Claude shows it as a draft, and on your word it is approved in the same way as any brief.
   You should now see the approved brief in the new project.
4. Claude mines the brief into the new project's intent in the usual way. This creates the new intent, and the mining is recorded in that intent's history.
   You should now see the new intent and its history record.
5. In the source project the change goes intent first. Claude records the spin-off in the source intent: the group's substance is now delivered by the new project. It then derives the change in the source assignment. The moved items are marked superseded, never deleted. The group is replaced with one link item: "Delivered by project *slug*, see its assignment."
   You should now see the spin-off in the source intent and the link item in the source assignment.
6. The command itself writes only the decision record in the source project's decisions file.
   You should now see a new decision recorded.
7. Claude makes both ledgers (the state records of the two projects) afresh and reports the result.
   You should now see a report on both projects.

## What you have afterwards

- A new thought project with its own brief, intent and history. See [Start a project](start-a-project.md) for what a new project is made of.
- A source assignment whose moved items are superseded and whose group is replaced by one link item.
- A source intent that records the spin-off.
- A decision record of the spin-off.
- Fresh ledgers for both projects.

## If something goes wrong

The inputs name no error messages and no stop conditions beyond these: nothing runs without your explicit instruction, and the brief is not approved without your word. If the list of items is wrong, adjust it at step 1 before anything is created.

## A worked example

You have a project `alpha` whose assignment has a group `reporting`. You type:

```
/spinoff alpha reporting reporting-tool
```

Claude lists the items of `reporting` and you drop one of them from the move. Claude creates `reporting-tool`, shows you a draft brief, and you approve it. Claude mines the brief into the new intent. In `alpha` the intent records that reporting is now delivered by `reporting-tool`, the moved items of the assignment become superseded, and one link item points to the new project. A decision is recorded, and both ledgers are made again.

## See also

- [Start a project](start-a-project.md): what the new project is made of.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
