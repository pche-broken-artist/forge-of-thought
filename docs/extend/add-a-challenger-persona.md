---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 0bde1371de3a8843
inputs:
  - templates/challenger-definition.md
  - .claude/skills/challenger-contract/SKILL.md
  - .claude/skills/challenge/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a challenger persona

This page shows an extender how to add a new challenger persona to the forge. A persona is one agent file: an isolated reviewer (a subagent, that is, a helper Claude runs in a context of its own) that tests the substance of the principal's thinking from a vantage point of its own. The principal is the person whose thinking is being forged.

## Before you start

A new persona is added only by the principal's decision, and only where what it would find genuinely differs from what the existing personas find. Look at the existing ones first: [Challenger personas](../reference/challenger-personas.md) lists them.

What every persona shares is owned by one contract (conduct, isolation, the subject, the way of working and the shape of the report), and a persona file never restates it. [The challenger](../about/the-challenger.md) explains what the contract owns.

How a change is proven, recorded and released is described in [Make a change to the forge](how-a-change-is-made.md). The new persona is recorded and released as any change of the forge.

Terms of the forge are explained in the [Glossary](../reference/glossary.md).

## The files

One file is added and none is edited:

- `.claude/agents/challenger-<persona>.md`: the persona, made from the skeleton `templates/challenger-definition.md`.

The command `/challenge` does not change. Its roster is made by scanning the agent files named `challenger-*.md`, so the new file appears in it by existing.

## Steps

1. Copy the skeleton `templates/challenger-definition.md` to `.claude/agents/challenger-<persona>.md`. The name of the persona is the suffix of the file name.
2. Fill the front-matter:
   - `name`: `challenger-<persona>`.
   - `description`: the persona in one line, saying who it is and what blind spots it exists to find. The roster shows this line, and the recommendation of a fit is made from it.
   - `tools`: the skeleton's list, which includes web search (`WebSearch`, `WebFetch`) so that the persona can ground a claim in how the world works.
   - `model`: `inherit`, so that the persona runs on the model of the session.
   - `skills`: the list holding `challenger-contract`, which loads the shared contract into the persona.
3. If the description holds a colon followed by a space, put the whole description in single quotes (an apostrophe inside is doubled). Otherwise the agent does not register.
4. Delete the comment in the skeleton.
5. Write the `## Lens` section, the only section that is the persona's own. It has two parts:
   - Who you are: a role of its own, never a mirror of the principal. It gives the register and the vantage point from which the persona reviews the thinking as an equal, with no stake in the principal being right.
   - What to go after: the blind spots this persona exists to find, as a list of concrete angles.
6. Leave out anything the contract already says. The Lens section may narrow what is read or make a shared rule stricter. It never renames, drops or duplicates a shared rule or field.

You should now see one new file, with front-matter and a Lens section, and nothing else changed.

## Prove it

Check the engine against its conventions:

```
/check engine
```

You should now see no finding about the new file. A run that finds nothing files nothing.

List the roster:

```
/challenge
```

You should now see `<persona>` among the personas, with its description.

Run the persona on a target, an artefact named as `/forge` names it or any file of a project by its path:

```
/challenge <persona> <artefact> <slug>
```

You should now see a report in the shape of the contract. The command files it in the project's `challenges/` folder and offers a walkthrough of its challenges.

## Record and release

The new file is recorded and released as any change of the forge, by the steps in [Make a change to the forge](how-a-change-is-made.md).

## A worked example

The principal decides that a new persona, `<persona>`, is wanted, for a vantage point none of the existing personas takes.

1. You copy the skeleton to `.claude/agents/challenger-<persona>.md`.
2. You set `name: challenger-<persona>` and a one-line `description` starting `Challenger persona "<persona>"` and naming who this is. The description holds no colon followed by a space, so it needs no quotes.
3. You keep `tools`, `model: inherit` and the `challenger-contract` skill as the skeleton has them.
4. Under `## Lens` you write, first, a short paragraph of who `<persona>` is and the register it speaks in, and second, a list of the concrete blind spots it goes after.
5. You run `/check engine`, then `/challenge`, which lists `<persona>`, then `/challenge <persona> <artefact> <slug>` on a project of yours.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The challenger](../about/the-challenger.md): what the contract owns.
- [Challenger personas](../reference/challenger-personas.md): the personas that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
