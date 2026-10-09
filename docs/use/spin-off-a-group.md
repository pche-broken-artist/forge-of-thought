---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/spinoff/SKILL.md
  - CLAUDE.md
---

# Spin off a group

This page is for the person who runs a project in the forge and finds
that one requirement group of its assignment has grown into a matter
of its own. It shows how `/spinoff` moves that group into a new
project, what you are asked along the way and what changes in the
project you started from.

## Before you start

A group becomes its own project only when you decide it, never
automatically. Claude may tell you that a group looks ready to stand
alone, but it never runs the spin-off on that proposal: the command
runs only on your explicit instruction, and proposing and running are
never one step.

A group is a plain heading in the assignment, under which its items
stand: requirements (`REQ`), out-of-scope items (`OOS`), constraints
(`CON`), assumptions (`ASM`), deliverables (`DEL`), open questions
(`TBC`) and success criteria (`SCR`).

## Run the command

```
/spinoff <project> <group> <slug>
```

- `<project>` is the slug of the project that holds the assignment.
- `<group>` is the name of the requirement group to move.
- `<slug>` is the slug of the new project.

For example, `/spinoff my-project "Group name" new-project`.

## What happens, step by step

1. **You confirm what moves.** Claude lists the items of the group
   that will move to the new project. You may adjust the list before
   anything is written.
2. **The new project is created.** It is made by the same procedure as
   `/new-project`, as a thought project, with its files only. It is
   not put under git: creating its repository and adding a remote are
   yours to do afterwards, once.
3. **You approve a short brief.** Claude derives the new project's
   brief, `00-brief.md`, from the relevant parts of the source
   project's intent: why this became a project of its own and what it
   inherits. It is written in the language settled when the project
   was created. Because Claude wrote it, you see it first as a draft;
   it is approved only on your word, through the same procedure as
   `/forge brief`.
4. **The brief is mined into the new intent.** Through the procedure
   of `/forge intent`, the brief is worked into the new project's
   `10-intent.md`, and the brief keeps track of what has been mined.
5. **The source assignment is updated.** The moved items are marked
   superseded, not deleted, and the group is replaced by one link
   item of the form "REQ.NNNN: Delivered by project *new-project*,
   see its assignment." The change is recorded in the assignment's
   history companion, and the decision is recorded in the source
   project's `decisions.md`.
6. **Both ledgers are updated** and Claude reports the result.

## What you end up with

- A new project with a brief you approved and an intent mined from it.
- A source assignment that still shows the moved items, marked
  superseded, with one item pointing to the new project.
- A history record and a decision record of the move in the source
  project, and both projects' ledgers current.

## See also

- [Start a project](start-a-project.md): what the new project is made
  of.
