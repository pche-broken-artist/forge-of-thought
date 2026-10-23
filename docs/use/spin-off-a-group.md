---
generated: 2026-10-23
version: 5.34
made: mirrored
inputs-hash: 83c410ef54e57ade
inputs:
  - .claude/skills/spinoff/SKILL.md
---

# Spin off a group

This page shows how `/spinoff` turns one requirement group of an assignment into a project of its own. It is for you, the principal (the person whose thinking is being forged), when a group has grown big enough to deserve its own chain.

## When to use it

Use it when you have decided that a group of requirements should be delivered by a separate project. Claude may tell you that a group looks ready. It never runs the command on its own: the command runs only on your explicit instruction.

## The command

```
/spinoff <project> <group> <slug>
```

- `<project>` is the source project that holds the group.
- `<group>` is the name of the requirement group to move.
- `<slug>` is the short name of the new project.

## What happens

1. Claude lists the items of the group that will move. The items can be requirements, out-of-scope items, constraints, assumptions, deliverables, open questions and success criteria. You may adjust the list.

   You should now see the list of items, and the move waits for your confirmation.

2. Claude creates the new project by the same procedure as `/new-project`, as a project of kind `thought`. It creates files only and no git repository. Setting up the repository and its remote is your own one-off act afterwards. What a new project is made of is on [Start a project](start-a-project.md).

   You should now see the new project's directory with its project file.

3. Claude derives a short brief for the new project from the relevant parts of the source project's intent. The brief says why the group became its own project and what it inherits, in the language settled when the project was created. Claude presents it as a draft. On your word it is approved by the same procedure as `/forge brief`.

   You should now see the draft brief, and after your word the approved brief.

4. Claude mines the brief into the new project's intent by the same procedure as `/forge intent`. That procedure creates the intent and records the mining in the intent's history.

   You should now see the new intent and a history record of the mining.

5. In the source project the change is made intent-first. The source intent records that project `<slug>` now delivers the group's substance, by the `/forge intent` procedure. Then the change is derived into the source assignment by the `/forge assignment` procedure. The moved items are marked superseded and never deleted. The group is replaced by one link item that reads "Delivered by project `<slug>`, see its assignment." The command itself writes only one thing, the decision record in the source project's decisions file.

   You should now see the source intent with the spin-off recorded, the assignment with its moved items superseded and one link item, and a new decision record.

6. Claude makes both ledgers afresh, one for each project, with `python scripts/forge-ledger.py <slug>`, and reports the result. A ledger is the state record each project builds at read time from its documents.

   You should now see a report of the result, with both ledgers current.

## What you have afterwards

- A new project with an approved brief, an intent that carries the mining record, and no git repository yet.
- A source project whose intent records the spin-off, whose assignment keeps the moved items as superseded and points to the new project with one link item, and whose decisions file holds the decision.
- Two fresh ledgers.

## If something goes wrong

The skill names no failure messages and no stop conditions beyond your confirmation at each step. If you do not confirm the list or the brief, the work does not go on. The terms of the forge are explained in the [Glossary](../reference/glossary.md).

## A worked example

You have a project `<project>` whose assignment has a group called `<group>`. You type:

```
/spinoff <project> <group> <slug>
```

Claude lists the items of `<group>`. You take one out of the list and confirm the rest. Claude creates `projects/<slug>/` and shows you a short draft brief. You approve it. Claude mines it into `projects/<slug>/10-intent.md` and records that in the history. In `<project>`, the intent now says that `<slug>` delivers the group, and the assignment shows the moved items as superseded with one link item in their place. The decision is written to `decisions.md`, both ledgers are made again, and Claude reports. You then initialise the new project's git repository yourself.

## See also

- [Start a project](start-a-project.md): what the new project is made of.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.34 from the files the front-matter names; never edited by hand.
