---
generated: 2026-10-09
made: mirrored
inputs-hash: 118123a4ed1ca22f
inputs:
  - .claude/skills/spinoff/SKILL.md
  - CLAUDE.md
---

# Spin off a group

This page is for a user who wants a requirement group of an
assignment to become a project of its own. It says how to run
`/spinoff`, what you are asked to confirm and what changes in the
source project and in the new one.

## When it happens

A group becomes its own project only by your explicit decision. Claude
may tell you that a group looks ready to be split off, but it never
runs the command on its own judgement and never proposes and runs it
in one step. You start it yourself:

```
/spinoff <project> <group> <slug>
```

- `<project>` is the project whose assignment holds the group.
- `<group>` is the name of the requirement group.
- `<slug>` is the slug of the new project.

## Steps

1. **Confirm the scope.** Claude lists the items of the group that
   will move: requirements, out-of-scope items, constraints,
   assumptions, deliverables, open questions and success criteria.
   You may adjust the list before anything is done.
2. **The new project is created.** Claude creates the project with
   the same procedure as `/new-project`, as a thought project. Only
   files are made, no git. The repository of the new project and its
   remote are your one-off act afterwards.
3. **A short brief is drafted.** Claude derives the new project's
   `00-brief.md` from the relevant parts of the source intent. It says
   why the group became its own project and what it inherits, in the
   language settled when the project was created. Claude presents it
   as a draft. On your word it is approved through the `/forge brief`
   procedure.
4. **The brief is mined into the new intent.** Claude runs the
   `/forge intent` procedure, which creates the new project's
   `10-intent.md` and keeps its Mined column.
5. **The source assignment is changed.** The moved items are marked
   superseded and not deleted. The group is replaced by one link item
   saying that the group is delivered by the new project, see its
   assignment. The change is written as the rules for versioning say,
   into the assignment's history companion, and recorded as a
   decision in the source project's `decisions.md`.
6. **Both ledgers are updated** and Claude reports the result.

## What you end with

- A new project holding the brief and the intent derived from it,
  ready to be worked on its own. What a new project is made of is
  described in [Start a project](start-a-project.md).
- The source assignment with the moved items kept as superseded and
  one link item pointing to the new project.
- A history record and a decision recording the split.
- Both ledgers current.

## See also

- [Start a project](start-a-project.md): what the new project is made of.
