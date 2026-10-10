---
generated: 2026-10-10
made: mirrored
inputs-hash: 08a38c73bff8ca34
inputs:
  - .claude/skills/spinoff/SKILL.md
  - CLAUDE.md
---

# Spin off a group

This page is for a user whose project has grown a requirement group that
deserves a project of its own. It says how to split the group off with
`/spinoff`, what you are asked along the way and what you end up with.

## Before you start

A group becomes its own project only on your explicit decision, never
automatically. Claude may tell you a group looks ready to be split off,
but it never runs the split on its own judgement: you give the
instruction, and only then does it start.

## The command

```
/spinoff <project> <group> <slug>
```

- `<project>`: the project that holds the group.
- `<group>`: the name of the requirement group in its assignment.
- `<slug>`: the slug of the new project.

## What happens, step by step

1. **You confirm what moves.** Claude lists the items of the group that
   would move: requirements, out-of-scope items, constraints,
   assumptions, deliverables, open questions and success criteria. You
   may adjust the list.
2. **The new project is created.** It is made the way `/new-project`
   makes a thought project, as files only. No git repository and no
   remote are set up: creating the repository and adding its remote is
   your own one-off act afterwards.
3. **A short brief is drafted.** Claude derives it from the relevant
   parts of the source project's intent: why this became a project of
   its own and what it inherits. It is written in the language settled
   when the project was created. It is presented to you as a draft, and
   on your word it is approved through the usual brief procedure.
4. **The brief is mined into the new intent.** The intent of the new
   project is created through the usual intent procedure, which keeps
   track of what was mined from the brief.
5. **The source project is brought in line.** The intent comes first: it
   records that the group's substance is now delivered by the new
   project. Then the source assignment changes. The moved items are
   marked superseded, never deleted, and the group is replaced by one
   link item saying the group is delivered by the new project, see its
   assignment. The change is recorded in the assignment's history, and
   the command itself writes one decision record in the source
   project's decisions.
6. **Both ledgers are updated** and the result is reported to you.

## What you have afterwards

- A new project with its own brief and intent, ready for you to continue
  with its assignment.
- A source assignment in which the group's items are still visible as
  superseded, with a single link item pointing to the new project.
- A decision record of the split in the source project.
- Your task: initialise the repository of the new project and add its
  remote, if you want it under git.

## See also

- [Start a project](start-a-project.md): what the new project is made of.
