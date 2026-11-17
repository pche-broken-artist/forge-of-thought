---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: d08950b36ee8a217
inputs:
  - .claude/skills/spinoff/SKILL.md
---

# Spin off a group

`/spinoff` splits one requirement group of an assignment into a project
of its own. This page is for you, the principal (the person whose
thinking is being forged), when a group has grown into something that
deserves its own chain of documents.

## When to use it

Use it when you have decided that a requirement group of an assignment
should be delivered by a separate project. The command runs only on your
explicit instruction. Claude may propose that a group is ready, but it
never runs the command as a step after its own proposal: the decision is
yours.

## The command

```
/spinoff <project> <group> <slug>
```

- `<project>`: the source project that holds the assignment.
- `<group>`: the name of the requirement group to move.
- `<slug>`: the slug of the new project.

For example: `/spinoff my-project "Reporting" my-reporting`.

## What happens

1. Claude lists the items of the group that will move: requirements,
   out-of-scope items, constraints, assumptions, deliverables, open
   points and scope items. You may adjust the list.

   You should now see the list confirmed by you, item by item.

2. Claude creates the new project under `projects/<slug>/` by the
   procedure of `/new-project`, as a project of the kind `thought`. It
   makes files only, no git: creating the repository and its remote is
   your one-off act afterwards. How a project is made is described in
   [Start a project](start-a-project.md).

   You should now see the new project's folder with its project file.

3. Claude derives a short brief for the new project from the relevant
   parts of the source intent. The brief says why this became its own
   project and what it inherits, and it is written in the language
   settled in step 2. Claude shows it to you as a draft. On your word it
   is approved through the procedure of `/forge brief`.

   You should now see the approved brief in the new project.

4. Claude mines the brief into the new project's intent through the
   procedure of `/forge intent`. That procedure creates the intent and
   writes the mining record in the intent's history.

   You should now see the new intent and, in its history, the record of
   the mining.

5. In the source project the change goes intent first. Claude records
   the spin-off in the source intent through `/forge intent`: the
   group's substance is now delivered by the new project. Then it
   derives the change in the source assignment through `/forge
   assignment`. That marks the moved items superseded, never deleted,
   and replaces the group with one link item that reads "Delivered by
   project *<slug>*, see its assignment." The command itself writes
   only the decision, in the source project's decisions file.

   You should now see the spin-off in the source intent, the moved items
   marked superseded, one link item in place of the group and a new
   decision.

6. Claude remakes the ledger of both projects with `python
   scripts/forge-ledger.py <slug>`, once for each, and reports the
   result.

   You should now see a report with both ledgers made afresh.

## What you have afterwards

- A new project of the kind `thought`, with an approved brief and an
  intent mined from it, but no git repository yet.
- A source intent that records the spin-off.
- A source assignment whose moved items are marked superseded and whose
  group is replaced by one link item.
- A decision in the source project's decisions file.
- A fresh ledger for each of the two projects (the ledger is the state
  of a project, made from its documents at read time).

## If something goes wrong

The command has no stop conditions or error messages of its own. It
stops where you do not confirm: an item list you reject, a brief you do
not approve. Nothing further is written in that case.

## A worked example

You decide that the group "Reporting" of the project `my-project`
should become its own project `my-reporting`.

1. You type `/spinoff my-project "Reporting" my-reporting`.
2. Claude lists the items of "Reporting". You remove one that belongs
   to the parent and confirm the rest.
3. Claude creates `projects/my-reporting/`, shows you a draft brief and
   approves it on your word.
4. Claude mines the brief into the intent of `my-reporting`.
5. In `my-project` the intent records the spin-off, the assignment
   marks the moved items superseded and gets one link item "Delivered
   by project *my-reporting*, see its assignment.", and the decision is
   written.
6. Both ledgers are remade and Claude reports.

You then create the git repository and remote of `my-reporting`
yourself.

## See also

- [Start a project](start-a-project.md): what the new project is made of.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
