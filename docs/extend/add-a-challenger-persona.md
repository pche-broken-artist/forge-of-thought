---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 5b45ed8ba44867bb
inputs:
  - templates/challenger-definition.md
  - .claude/skills/challenger-contract/SKILL.md
  - .claude/skills/challenge/SKILL.md
  - CLAUDE.md#Isolated reviewers
  - .claude/agents/check-engine.md
---

# Add a challenger persona

This page is for the extender who wants a new challenger persona. A
challenger persona is one isolated reviewer (a subagent, that is, an
agent that runs in its own context and sees nothing of the
conversation) that challenges the substance of the thinking of the
principal, the person whose thinking is being forged. A persona is
added as one agent file made from a template. Terms of the forge are
one line each in the [Glossary](../reference/glossary.md).

## Before you start

A new persona is added only by the principal's decision, and only
where what it finds genuinely differs from what the existing personas
find. The personas that exist are listed in
[Challenger personas](../reference/challenger-personas.md). What the
shared contract of every persona owns is explained in
[The challenger](../about/the-challenger.md).

The addition is recorded and released as any change of the forge. How
a change is proved, recorded and released is described in
[Make a change to the forge](how-a-change-is-made.md).

## The files

A persona costs one file and no edits elsewhere.

- `.claude/agents/challenger-<persona>.md` is the new file. Its
  skeleton is `templates/challenger-definition.md`.

Nothing else changes. The `/challenge` command does not change,
because the roster of personas is the scan of the files
`.claude/agents/challenger-*.md`.

## Steps

1. Copy `templates/challenger-definition.md` to
   `.claude/agents/challenger-<persona>.md`. The suffix of the file
   name is the persona's name.
2. Fill the front-matter:
   - `name` is `challenger-<persona>`.
   - `description` says who the persona is in one line and states
     that it challenges the substance of the thinking and is not a
     document auditor. If the description holds a colon followed by a
     space, put the whole description in single quotes, with an
     apostrophe inside doubled. Otherwise the agent does not register.
   - `tools` stays `Read, Glob, Grep, WebSearch, WebFetch`. Web search
     is part of it, because a persona grounds its claims in how the
     world works.
   - `model` is `inherit`.
   - `skills` lists `challenger-contract`.
3. Delete the comment of the skeleton from the file.
4. Write the section `## Lens` in two parts:
   - Who you are: a role of its own, never a mirror of the principal.
     It gives the register and the vantage point from which the
     persona reviews the thinking as an equal, with no stake in the
     principal being right.
   - What to go after: the blind spots this lens exists to find, as a
     list of concrete angles.
5. Add nothing else. Subject, way of working and shape of the report
   belong to the contract, which is loaded into every persona after
   its Lens section. Restating any of it in the persona file is a
   defect, because the contract changes in one place only.

## Prove it

Check the engine against itself. The check verifies, among other
things, that every skill an agent names in its front-matter exists,
and that the described agents agree with `.claude/agents/`.

```
/check engine
```

Then run the persona once on a target, so that the file is shown to
register and to return a report:

```
/challenge <persona> <artefact-or-path> <project-slug>
```

The target and the slug are optional. Without a target, the whole
chain is challenged. A bare `/challenge` lists the roster, and the new
persona should stand in it.

## Record and release

The new file is recorded and released as any change of the forge, by
the way [Make a change to the forge](how-a-change-is-made.md)
describes.

## A worked example

The persona is called `<persona>`, and its file is
`.claude/agents/challenger-<persona>.md`:

```markdown
---
name: challenger-<persona>
description: Challenger persona "<persona>" — <who this is, in one line>. Challenges the substance of the principal's thinking. Not a document auditor.
tools: Read, Glob, Grep, WebSearch, WebFetch
model: inherit
skills:
  - challenger-contract
---

## Lens

<Who you are: a role of its own, its register and its vantage point.>

<What to go after: the blind spots of this lens, one concrete angle
per item.>
```

You should now see `challenger-<persona>` in the list printed by a
bare `/challenge`, and `/check engine` should report no finding about
the new file.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The challenger](../about/the-challenger.md): what the contract owns.
- [Challenger personas](../reference/challenger-personas.md): the personas that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
