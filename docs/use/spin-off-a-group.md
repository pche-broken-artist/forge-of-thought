---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: a943e08381b6f43e
inputs:
  - .claude/skills/spinoff/SKILL.md
---

# Spin off a group

This page shows how `/spinoff` turns one requirement group of a project's assignment into a project of its own. It is for you, the principal (the person whose thinking is forged), when a group has grown large enough to stand alone. Terms of the forge are in the [Glossary](../reference/glossary.md).

## When to use it

Use it when you have decided that a requirement group of an assignment should be delivered by a separate project. The command runs only on your explicit instruction. Claude may point out that a group looks ready to leave, but it never runs the split on its own judgement, and it never proposes and runs in one step.

## The command

```
/spinoff <project> <group> <slug>
```

- `<project>`: the project that holds the group today.
- `<group>`: the name of the requirement group to move.
- `<slug>`: the short name of the new project.

## What happens

1. Claude lists the items of the group that will move (requirements, out-of-scope items, constraints, assumptions, deliverables, open questions and success criteria). You may adjust the list.

   You should now see the list confirmed by you, item by item.

2. Claude creates the new project by the same procedure as `/new-project`, as a thought project. It makes files only. The project's git repository and its remote are your one-off act afterwards. What the new project is made of is on [Start a project](start-a-project.md).

   You should now see the folder `projects/<slug>/` with its files.

3. Claude derives a short brief for the new project from the relevant parts of the source project's intent. The brief says why the group became its own project and what it inherits. It is written in the language settled when the project was created. Claude presents it to you as a draft, and on your word it is approved through the `/forge brief` procedure.

   You should now see an approved `00-brief.md` in the new project.

4. Claude mines the brief into the new project's intent through the `/forge intent` procedure. That procedure creates the intent and keeps its record of what was mined.

   You should now see `10-intent.md` in the new project.

5. In the source project, the change goes intent first. Claude records the spin-off in the source intent through the `/forge intent` procedure: the group's substance is now delivered by the new project. Then it derives the change in the source assignment through the `/forge assignment` procedure. The moved items are marked superseded, never deleted. The group is replaced by one link item saying that the group is delivered by the new project and pointing to its assignment. The command itself writes only the decision record, in the source project's decisions file.

   You should now see the intent recording the spin-off, the moved items marked superseded, one link item in their place, and a new decision record.

6. Claude remakes the ledger (the file that holds the state of a project) of both projects with `python scripts/forge-ledger.py <slug>`, once for each, and reports the result.

   You should now see a report for both projects.

## What you have afterwards

- A new project with a brief, an intent and its own ledger, ready for its repository and remote, which you add yourself.
- A source project whose intent records the spin-off, whose assignment keeps the moved items as superseded and shows one link item for the group, and whose decisions file holds the decision.
- Both ledgers made afresh.

## If something goes wrong

The definition of the command names no stop conditions and prints no messages of its own. If a step does not look right, say so before the next one: the items, the brief and the changes to the source project all wait for your word.

## A worked example

You have a project `acme` whose assignment holds a group called `reporting`, and you want it delivered by a project named `acme-reporting`.

```
/spinoff acme reporting acme-reporting
```

Claude lists the items of `reporting` and you drop one that should stay. It creates `projects/acme-reporting/`, drafts the brief from the intent of `acme`, and you approve it. It mines the brief into the new intent. In `acme`, the intent records that `acme-reporting` now delivers the group, the assignment marks the moved items superseded and shows one link item in their place, and the decision is written. Both ledgers are remade. Last, you initialise the git repository of `acme-reporting` and add its remote yourself.

## See also

- [Start a project](start-a-project.md): what the new project is made of.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
