---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: ea910923a65072b1
inputs:
  - templates/challenger-definition.md
  - .claude/skills/challenger-contract/SKILL.md
  - .claude/skills/challenge/SKILL.md
  - CLAUDE.md#Isolated reviewers
  - .claude/agents/check-engine.md
---

# Add a challenger persona

A challenger persona is one agent file that reviews the substance of
the principal's thinking from a vantage point of its own. This page
is for the extender who wants to add one. The principal is whoever's
thinking is being forged, and a persona is added only on the
principal's decision, and only where what it finds genuinely differs
from what the personas that exist already find.

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md). It says
how a change is proved, recorded and released. A new persona is
recorded and released as any change of the forge.

Read [The challenger](../about/the-challenger.md) for what the shared
contract owns, and [Challenger personas](../reference/challenger-personas.md)
for the personas that exist, so that the new one finds something they
do not. Terms of the forge are one line each in the
[Glossary](../reference/glossary.md).

## The files

A persona costs one file and no edits:

- `.claude/agents/challenger-<persona>.md` is the new agent file. It
  is made from `templates/challenger-definition.md`.

Nothing else changes. The roster is the scan of
`.claude/agents/challenger-*.md`, so bare `/challenge` lists the new
persona as soon as the file exists. The `/challenge` command itself
does not change.

## Steps

1. Copy `templates/challenger-definition.md` to
   `.claude/agents/challenger-<persona>.md`. The suffix is the
   persona's name.
2. Fill the front-matter:
   - `name`: `challenger-<persona>`.
   - `description`: the persona in one line, then that it challenges
     the substance of the principal's thinking and is not a document
     auditor. The roster shows this line, so it says the blind spots
     the persona exists to find.
   - `tools`: `Read, Glob, Grep, WebSearch, WebFetch`. A challenger may
     search the web, so the web tools stay.
   - `model`: `inherit`. The whole forge runs on one model.
   - `skills`: one entry, `challenger-contract`. It preloads the
     shared behaviour into the persona.
3. If the description holds a colon followed by a space, put the whole
   description in single quotes, with an apostrophe inside doubled.
   Otherwise the agent does not register.
4. Delete the comment the template carries.
5. Write the `## Lens` section, the persona's own, in two parts:
   - Who you are: a role of its own, such as a CTO or a strategist,
     never a mirror of the principal. It names the register and the
     vantage point from which the persona reviews the thinking as an
     equal, with no stake in the principal being right.
   - What to go after: the blind spots this lens exists to find, as a
     list of concrete angles.
6. Restate nothing of the contract. The Lens section may narrow what
   is read or make a shared rule stricter. It never renames, drops or
   duplicates a shared rule or a field of the report, because the
   protocol changes in the contract alone. Subject, way of working
   and report shape are the contract's.
7. Keep instance facts out of the file: names, roles, addresses and
   hosts never enter a persona or its reports.

## Prove it

Check the engine against itself. The check verifies, among other
things, that every skill an agent names in its `skills:` field exists
as `.claude/skills/<name>/SKILL.md`, because Claude Code skips a
missing one silently.

```
/check engine
```

Then run the persona on a target. The target is an artefact of the
chain or any file of the project by its path:

```
/challenge <persona> <artefact> <slug>
```

You should now see the persona in the roster, and a report that
carries its challenges, each with a severity, filed in the project's
`challenges/` folder.

## Record and release

Record the change and release it as any change of the forge, in the
way [Make a change to the forge](how-a-change-is-made.md) describes.

## A worked example

The persona is called `<persona>`, and the file is
`.claude/agents/challenger-<persona>.md`:

```
---
name: challenger-<persona>
description: Challenger persona "<persona>" — <who this is, in one line>. Challenges the substance of the principal's thinking. Not a document auditor.
tools: Read, Glob, Grep, WebSearch, WebFetch
model: inherit
skills:
  - challenger-contract
---

## Lens

<Who you are: a role of its own, the register and the vantage point.>

<What to go after: a list of concrete blind spots.>
```

After `/check engine` passes, `/challenge` with no argument lists
`<persona>` beside the others, and `/challenge <persona>` runs it.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The challenger](../about/the-challenger.md): what the contract owns.
- [Challenger personas](../reference/challenger-personas.md): the personas that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
