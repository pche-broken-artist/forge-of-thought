---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 2e491727030c8ec8
inputs:
  - templates/challenger-definition.md
  - .claude/skills/challenger-contract/SKILL.md
  - .claude/skills/challenge/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a challenger persona

This page shows an extender how to add a new challenger persona, a reviewer that attacks the substance of the principal's thinking from a vantage point of its own. The principal is the person whose thinking is being forged. A persona is one agent file and nothing else.

## Before you start

A persona is added only by the principal's decision, and only where what it finds genuinely differs from the personas that exist. Check the list on [Challenger personas](../reference/challenger-personas.md) first. What a challenger is, and what the shared contract owns, is explained on [The challenger](../about/the-challenger.md).

The addition is a change of the forge like any other. How a change is proved, recorded and released is on [Make a change to the forge](how-a-change-is-made.md). Terms of the forge are one line each in the [Glossary](../reference/glossary.md).

## The files

You write one file:

- `.claude/agents/challenger-<persona>.md`: the agent file of the persona. Its name is the suffix `<persona>`.

You start from the skeleton `templates/challenger-definition.md`. You edit no other file. The `/challenge` command does not change, because it finds the personas by scanning `.claude/agents/challenger-*.md`. The roster that bare `/challenge` prints is that scan, built from the `description` of each file.

## Steps

1. Copy the skeleton to `.claude/agents/challenger-<persona>.md`.
   You should now see a file whose front-matter still holds the placeholder `<persona>`.
2. Fill the front-matter. It has these fields:
   - `name`: `challenger-<persona>`.
   - `description`: who the persona is, in one line, and that it challenges the substance of the principal's thinking and does not audit documents. The roster shows this line.
   - `tools`: `Read, Glob, Grep, WebSearch, WebFetch`. The web search is there because a challenger may check how the world works.
   - `model`: `inherit`, so that the persona runs on the model of the session. The whole forge runs on one model.
   - `skills`: the list holding `challenger-contract`, which loads the shared behaviour into the persona.

   If the description holds a colon followed by a space, put the whole description in single quotes, and double any apostrophe inside it. Otherwise the agent does not register.

   You should now see a front-matter with no placeholder left.
3. Write the `## Lens` section. It has two parts:
   - Who the persona is: a role of its own, such as a strategist or a CTO, and never a mirror of the principal. State its register and the vantage point from which it reviews the thinking as an equal with no stake in the principal being right.
   - What to go after: the blind spots this persona exists to find, as a list of concrete angles.

   You should now see a Lens section of those two parts.
4. Delete the comment block that the skeleton carries. The file holds the front-matter and the Lens section, nothing else.
   You should now see a file with no comment left.

Do not restate the contract. The contract owns conduct and isolation, the subject and its boundary, the way of working and the shape of the report. A Lens section specialises the contract: it may narrow what is read or make a shared rule stricter. It never renames, drops or repeats a shared rule or field. A change of the protocol is made in the contract alone. Do not copy the angles of an existing persona either: a new persona is justified by what it finds that they do not.

## A worked example

The file below is the shape with a placeholder persona. The bracketed lines stand for text you write.

```markdown
---
name: challenger-<persona>
description: Challenger persona "<persona>" — [who this is, in one line]. Challenges the substance of the principal's thinking. Not a document auditor.
tools: Read, Glob, Grep, WebSearch, WebFetch
model: inherit
skills:
  - challenger-contract
---

## Lens

[Who you are: the role, the register and the vantage point.]

[What to go after: the list of concrete blind spots.]
```

Once the file is saved, bare `/challenge` lists `<persona>` with its description, and `/challenge <persona>` runs it.

## Prove it

Run the check of the engine, which verifies the engine's conformance with its conventions:

```
/check engine
```

You should now see no finding that names your file. Then run the persona on a target, an artefact of a project or any file of it by path:

```
/challenge <persona> <artefact> <project-slug>
```

You should now see a report in the shape of the contract, filed in the project's `challenges/` folder, and an offer of a walkthrough of its challenges. A walkthrough is the method where each item needing a decision is worked one at a time.

## Record and release

Record the addition and release it as any change of the forge is recorded and released, as [Make a change to the forge](how-a-change-is-made.md) describes. The persona is part of the engine from the release that carries its file.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The challenger](../about/the-challenger.md): what the contract owns.
- [Challenger personas](../reference/challenger-personas.md): the personas that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
