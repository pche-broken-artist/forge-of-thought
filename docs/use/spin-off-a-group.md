---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: dcca2b9c8bcb43c3
inputs:
  - .claude/skills/spinoff/SKILL.md
---

# Spin off a group

`/spinoff` splits one requirement group of a project's assignment into a project of its own, so that the group's substance is delivered there. This page is for you, the principal (the person whose thinking is being forged), when a group has grown big enough to stand alone.

## When to use it

Use it when you have decided that a group of requirements should become its own project. The command runs only on your explicit instruction. Claude may point out that a group looks ready, but it never proposes and runs the split in one step.

## The command

```
/spinoff <project> <group> <slug>
```

A concrete line, with placeholders:

```
/spinoff my-project onboarding-group my-new-project
```

The three arguments are the source project, the name of the group to move, and the slug of the new project.

## What happens

1. Claude lists the items of the group that will move. These can be requirements, out-of-scope items, constraints, assumptions, deliverables, open questions and success criteria. You may adjust the list.

   You should now see the list of items, and the moved set is the one you confirmed.

2. Claude creates the new project by the same procedure as `/new-project`, as a thought project. It makes files only. It does not set up git: the new project's repository and its remote are your own one-off act afterwards. See [Start a project](start-a-project.md) for what the new project is made of.

   You should now see the new project's folder under `projects/`.

3. Claude derives a short brief for the new project from the relevant parts of the source intent. The brief says why this became its own project and what it inherits. It is written in the language settled in step 2. Claude shows it to you as a draft, and on your word it is approved through the `/forge brief` procedure.

   You should now see an approved brief in the new project.

4. The brief is mined into the new project's intent through the `/forge intent` procedure. This creates the intent and writes the mining record in the intent's history.

   You should now see the new intent and, in its history, the record of the mining.

5. In the source project the change is made intent first. The source intent records that the group's substance is now delivered by the new project. Then the source assignment is changed through the `/forge assignment` procedure. The moved items are marked superseded and never deleted. The group is replaced by one link item that says the group is delivered by the new project and points to its assignment. The command itself writes only the decision, in the source project's decisions file.

   You should now see the intent's record of the spin-off, the superseded items, the one link item and the new decision.

6. Claude remakes the ledger of both projects and reports the result. The ledger is the state of a project, made afresh each time it is read.

   You should now see a report with both ledgers remade.

## What you have afterwards

- A new thought project with an approved brief and an intent.
- In the source project, the intent recording the spin-off, the moved items marked superseded, one link item in place of the group, and a decision.
- Both ledgers made afresh.
- A new project that is not yet under git. Its repository and remote are yours to set up.

## A worked example

You decide that the group `reporting` of project `my-project` should stand alone as `my-reports`.

1. You type `/spinoff my-project reporting my-reports`.
2. Claude lists the items of `reporting`. You drop one item from the list and confirm the rest.
3. Claude creates `projects/my-reports/`, drafts its brief from the intent of `my-project`, and you approve the brief.
4. Claude mines the brief into the intent of `my-reports`.
5. In `my-project`, the intent records the spin-off, the moved items become superseded, and the group is replaced by one item that reads "Delivered by project *my-reports*, see its assignment."
6. Claude writes the decision, remakes both ledgers and reports.

Afterwards you initialise git for `my-reports` yourself.

## See also

- [Start a project](start-a-project.md): what the new project is made of.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
