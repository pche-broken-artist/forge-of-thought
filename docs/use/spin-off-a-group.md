---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 43cffa43c6d1e53b
inputs:
  - .claude/skills/spinoff/SKILL.md
---

# Spin off a group

`/spinoff` splits one requirement group of an assignment into a project of its own. This page is for you, the principal (the person whose thinking is being forged), when a group has grown into something that deserves its own chain.

## When to use it

Use it when a group of requirements in one project should be delivered by a project of its own. Claude may tell you that a group looks ready. It never runs the command on its own: the spin-off happens only on your explicit instruction.

## The command

```
/spinoff <project> <group> <slug>
```

- `<project>` is the project that holds the group.
- `<group>` is the name of the requirement group.
- `<slug>` is the slug of the new project.

## What happens

1. Claude lists the items of the group that will move. They can be requirements, out-of-scope items, constraints, assumptions, deliverables, open questions and success criteria. You may adjust the list.

   You should now see the list of items, confirmed by you.

2. Claude creates the new project by the same procedure as a new project, as a thought project. It makes files only. The new project's git repository and remote are your one-off act afterwards. What the new project is made of is described in [Start a project](start-a-project.md).

   You should now see the new project's folder with its files, and no repository in it.

3. Claude derives a short brief for the new project from the relevant parts of the source project's intent. The brief says why this became its own project and what it inherits. It is written in the language settled in the previous step. Claude shows it to you as a draft. On your word it is approved through the brief procedure of `/forge`.

   You should now see an approved brief in the new project.

4. Claude mines the brief into the new project's intent through the intent procedure of `/forge`. That creates the intent and writes the mining record in the intent's history.

   You should now see the new intent, and its history holding the record of the mining.

5. Claude turns to the source project and works intent-first. It records the spin-off in the source intent, saying that the group's substance is now delivered by the new project. Then it derives the change in the source assignment. The moved items are marked superseded, never deleted. The group is replaced by one link item that reads "Delivered by project *slug*, see its assignment." The command itself writes only the decision, in the source project's decisions file.

   You should now see the moved items marked superseded, the one link item in their place, and the decision recorded.

6. Claude makes the ledger of each project afresh and reports the result. The ledger is the state report that is made at read time and never kept in git.

   You should now see a report on both projects.

## What you have afterwards

- A new project with an approved brief, an intent and its history.
- In the source project, an intent that records the spin-off, an assignment whose moved items are superseded and replaced by one link item, and a decision.
- A fresh ledger for both projects.

The new project has no git repository yet. Creating it and adding a remote is your step. For terms used here, see the [Glossary](../reference/glossary.md).

## If something goes wrong

The inputs record no error messages for this command. Two stops are stated:

- Without your explicit instruction the command does not run, and Claude never proposes and runs it in one step.
- Nothing is derived from the draft brief until you approve it.

## A worked example

You have a project `alpha` whose assignment holds a group called `Reporting`.

1. You type `/spinoff alpha Reporting reporting-tool`.
2. Claude lists the items of `Reporting`. You remove one item that belongs with the rest of `alpha` and confirm.
3. Claude creates `projects/reporting-tool/` and drafts its brief. You approve the brief.
4. Claude mines the brief into the intent of `reporting-tool`.
5. In `alpha`, the intent records that `Reporting` is delivered by `reporting-tool`. The assignment marks the confirmed items superseded and puts one link item where the group stood. The decision is written.
6. Both ledgers are made afresh and Claude reports. You then create the repository of `reporting-tool` yourself.

## See also

- [Start a project](start-a-project.md): what the new project is made of.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
