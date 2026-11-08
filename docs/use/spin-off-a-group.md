---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 2f017382fa815f9a
inputs:
  - .claude/skills/spinoff/SKILL.md
---

# Spin off a group

`/spinoff` splits one requirement group of a project's assignment into a project of its own. This page is for you, the principal (the person whose thinking is being forged), when a group has grown into work that deserves its own chain. Terms of the forge are in the [Glossary](../reference/glossary.md).

## When to use it

Use it when you have decided that a group of requirements should be delivered by a project of its own. Claude may point out that a group looks ready. It never runs the command on its own: the spin-off happens only on your explicit instruction, and never as a proposal and a run in one step.

## The command

```
/spinoff <source-project> <group-name> <new-slug>
```

The three arguments are the project that holds the group, the name of the group, and the slug of the new project.

## What happens

1. Claude lists the items of the group that will move: the requirements, the out-of-scope items, the constraints, the assumptions, the deliverables, the open questions and the success criteria. You may adjust the list.
   You should now see the list of items, confirmed by you.
2. Claude creates the new project by the same procedure as `/new-project`, as a thought project. It makes files only and no git. The new project's repository and remote are your own one-off act afterwards. What the new project is made of is on the page [Start a project](start-a-project.md).
   You should now see the folder of the new project with its files.
3. Claude derives a short brief for the new project from the relevant parts of the source intent. The brief says why this became a project of its own and what it inherits, in the language settled at step 2. Claude shows it to you as a draft. On your word it is approved through the procedure of `/forge brief`.
   You should now see the approved brief in the new project.
4. Claude mines the brief into the new project's intent through the procedure of `/forge intent`. That creates the intent and writes the mining record in the intent's history.
   You should now see the new intent and its history record.
5. In the source project, Claude works intent-first. It records the spin-off in the source intent through the procedure of `/forge intent`: the group's substance is now delivered by the new project. Then it derives the change in the source assignment through the procedure of `/forge assignment`. That marks the moved items superseded, never deleted, and replaces the group with one link item: "Delivered by project *new-slug*, see its assignment."
   You should now see the intent with the spin-off recorded and the assignment with the group replaced by the link item.
6. The command itself writes the decision into the source project's decisions record. This is the only thing it writes directly.
   You should now see the new decision at the end of the decisions record.
7. Claude makes both ledgers afresh, one for each project, and reports the result.
   You should now see the report of both projects' state.

## What you have afterwards

- A new project with an approved brief, an intent and a history record of the mining.
- A source project whose intent records the spin-off, whose assignment marks the moved items superseded and carries one link item in place of the group, and whose decisions record holds the decision.
- Two ledgers made afresh.

The new project's own git repository and remote are not made. They remain your step.

## If something goes wrong

The skill names no stop conditions and prints no messages of its own. Each procedure it calls (`/new-project`, `/forge brief`, `/forge intent`, `/forge assignment`) works under its own rules, and the step you adjust or refuse is the one you decide about.

## A worked example

You decide that the group "reporting" of the project `source-project` should become the project `reporting-tool`.

```
/spinoff source-project reporting reporting-tool
```

Claude lists the items of the group "reporting" and you remove one that stays behind. It creates `projects/reporting-tool/`, drafts the brief, and you approve it. It mines the brief into the new intent. In `source-project` it records the spin-off in the intent, marks the moved items superseded in the assignment and puts one link item in their place. It writes the decision and makes both ledgers afresh.

## See also

- [Start a project](start-a-project.md): what the new project is made of.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
