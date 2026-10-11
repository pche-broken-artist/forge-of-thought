---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 577d6ed44c4de220
inputs:
  - templates/challenger-definition.md
  - .claude/skills/challenger-contract/SKILL.md
  - .claude/skills/challenge/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a challenger persona

This page says how a new challenger persona is added to the forge, and it is for the extender. A challenger persona is one isolated reviewer (a subagent, that is a helper Claude starts in a context of its own) that tests the substance of the principal's thinking, the principal being whoever's thinking is being forged. A persona is one agent file, written from a template.

## Before you start

- A persona is added only by the principal's decision. It is added only where the blind spots it hunts genuinely differ from those of the personas that exist. The list of those is in [Challenger personas](../reference/challenger-personas.md).
- What every persona shares is owned by the challenger's contract, not by the persona file. Read what the contract owns in [The challenger](../about/the-challenger.md).
- The addition is recorded and released as any change of the forge. How that goes is in [Make a change to the forge](how-a-change-is-made.md).
- Terms of the forge are explained in the [Glossary](../reference/glossary.md).

## The files

A persona costs one file and no edits elsewhere.

- Create `.claude/agents/challenger-<persona>.md` from `templates/challenger-definition.md`.
- The command `/challenge` does not change. The roster of personas is made by scanning the files `.claude/agents/challenger-*.md`, so the new file is found by itself.

## Steps

1. Copy `templates/challenger-definition.md` to `.claude/agents/challenger-<persona>.md`. The name of the persona is the suffix of the file name.
2. Fill the front-matter:
   - `name`: `challenger-<persona>`.
   - `description`: one line saying who this persona is, then that it challenges the substance of the principal's thinking and is not a document auditor. The roster shows this line, and a recommendation of a fit is made from it.
   - `tools`: as the template has them, web search included, because a challenger may search the web.
   - `model`: `inherit`. The whole forge runs on one model.
   - `skills`: `challenger-contract`, the one contract every persona carries.
3. If the description holds a colon followed by a space, put the whole description in single quotes. An apostrophe inside it is doubled. Otherwise the agent does not register.
4. Write the `## Lens` section, the only section that is the persona's own. It has two parts:
   - Who you are: a role of its own, never a mirror of the principal. It gives the register and the vantage point from which the persona reviews the thinking as an equal, with no stake in the principal being right.
   - What to go after: the blind spots this persona exists to find, as a list of concrete angles.
5. Delete the comment of the template from the file.
6. Restate nothing of the contract in the Lens section. The subject, the way of working, the severity marks, the report shape and the ledger step belong to the contract. A Lens section may narrow what is read or make a shared rule stricter. It never renames, drops or duplicates a shared rule or field.

You should now see one new file with the front-matter and the Lens section and nothing else.

## Prove it

Run the check of the engine:

```
/check engine
```

You should now see the check report no finding about the new file. A run that finds nothing files nothing.

Then run the persona on a target:

```
/challenge <persona> <artefact> <project-slug>
```

You should now see Claude invoke the `challenger-<persona>` subagent on the project, a file `challenges/YYYY-MM-DD-challenge-<persona>.md` written, and the new challenges added to the ledger (the single table of state of the project) as open. Bare `/challenge` lists the roster, and the new persona stands in it.

## Record and release

The new file is saved and released as any change of the forge, by the steps of [Make a change to the forge](how-a-change-is-made.md).

## A worked example

The persona is named `<persona>`. The file `.claude/agents/challenger-<persona>.md` has this shape, the words in angle brackets being placeholders:

```
---
name: challenger-<persona>
description: Challenger persona "<persona>" - <who this is, in one line>. Challenges the substance of the principal's thinking. Not a document auditor.
tools: Read, Edit, Glob, Grep, WebSearch, WebFetch, Write
model: inherit
skills:
  - challenger-contract
---

## Lens

<Who you are: the role of this persona and the vantage point from
which it reviews the thinking as an equal.>

<What to go after: a list of concrete blind spots this persona exists
to find.>
```

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The challenger](../about/the-challenger.md): what the contract owns.
- [Challenger personas](../reference/challenger-personas.md): the personas that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
