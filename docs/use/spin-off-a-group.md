---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 701e35f6a8f0c654
inputs:
  - .claude/skills/spinoff/SKILL.md
---

# Spin off a group

`/spinoff` splits one requirement group of an assignment into a project of its own. This page is for the principal, the person whose thinking is forged, who has decided that a group has outgrown the project it sits in. The terms of the forge are explained in the [Glossary](../reference/glossary.md).

## When to use it

Use it when you have decided that a group of requirements should be delivered by a project of its own. The decision is yours alone. Claude may say that a group looks ready to be split off, but it never runs the command on its own and never proposes and runs it in one step.

## The command

```
/spinoff <project> <group> <slug>
```

- `<project>`: the slug of the project the group comes from.
- `<group>`: the name of the requirement group.
- `<slug>`: the slug of the new project.

## What happens

1. Claude lists the items of the group that will move. These are the requirements, out-of-scope items, constraints, assumptions, deliverables, open questions and success criteria of the group. You may adjust the list. You should now see the list of items and a request for your confirmation.
2. Claude creates the new project by the `/new-project` procedure, as a project of the kind that holds a chain of documents. It makes files only. You should now see the new project's directory, made as [Start a project](start-a-project.md) describes. The new project's git repository and its remote are not made. They are your one-off act afterwards.
3. Claude derives a short brief for the new project from the relevant parts of the source project's intent. The brief says why the group became its own project and what the new project inherits. It is written in the language settled when the project was created. Claude presents it as a draft. You should now see the draft brief. On your word it is approved through the `/forge brief` procedure.
4. Claude mines the approved brief into the new project's intent through the `/forge intent` procedure. You should now see a new intent file in the new project.
5. Claude changes the source project, starting with its intent. It records there that the group's substance is now delivered by the new project. Then it derives the change in the source assignment through the `/forge assignment` procedure. That procedure marks the moved items superseded and never deletes them. It replaces the group with one link item that reads "Delivered by project *slug*, see its assignment." You should now see the moved items marked superseded and the one link item in their place. The command itself writes only one decision record in the source project's decisions file.
6. Claude updates the ledger of both projects and reports the result. You should now see the report.

## What you have afterwards

- A new project with its own brief and intent, created from the source project's intent.
- A source assignment in which the moved items are superseded and one link item points to the new project.
- A decision record in the source project that records the spin-off.
- Both ledgers up to date.
- Nothing committed. The new project has no git repository until you make one.

## A worked example

You have a project `site-rebuild` whose assignment has a group named `search`. You decide it should be a project of its own, called `site-search`.

You type:

```
/spinoff site-rebuild search site-search
```

Claude lists the items of the group `search` and asks you to confirm. You drop one item from the list and confirm. Claude creates `projects/site-search/`, shows you a draft brief, and you approve it. Claude mines the brief into the new intent, records the spin-off in the intent of `site-rebuild`, marks the moved items of its assignment superseded, and adds the one link item. It writes the decision record, updates both ledgers and reports. You then initialise the repository of `site-search` yourself if you want one.

## See also

- [Start a project](start-a-project.md): what the new project is made of.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
