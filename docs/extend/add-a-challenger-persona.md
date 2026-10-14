---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: a61f0bc179941a4a
inputs:
  - templates/challenger-definition.md
  - .claude/skills/challenger-contract/SKILL.md
  - .claude/skills/challenge/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a challenger persona

A challenger persona is one reviewer that reads the substance of the principal's thinking from a vantage point of its own, and this page shows an extender how to add one as a single agent file. The principal is the person whose thinking is forged. Challengers are isolated subagents: Claude runs each in its own context, and the subagent never sees the working conversation.

## Before you start

- Add a persona only on the principal's decision, and only where what it finds genuinely differs from what the existing personas find. The list of those that exist is in [Challenger personas](../reference/challenger-personas.md).
- Know what the shared contract already owns, so that you do not restate it. [The challenger](../about/the-challenger.md) explains it, and the terms of the forge are in the [Glossary](../reference/glossary.md).
- Read [Make a change to the forge](how-a-change-is-made.md). The persona is recorded and released as any change of the forge.

## The files

A persona is one file and no other edit:

- `.claude/agents/challenger-<persona>.md`: the agent file, made from `templates/challenger-definition.md`.

The command `/challenge` does not change. The roster is the scan of `.claude/agents/challenger-*.md`, so a new file is in the roster as soon as it exists.

## Steps

1. Copy `templates/challenger-definition.md` to `.claude/agents/challenger-<persona>.md`. The file name and the `name` field carry the same persona name.
2. Fill the front-matter:
   - `name`: `challenger-<persona>`.
   - `description`: who the persona is, in one line, then that it challenges the substance of the principal's thinking and is not a document auditor. The roster shows this line. If it holds a colon followed by a space, put the whole description in single quotes (an apostrophe inside is doubled). Otherwise the agent does not register.
   - `tools`: keep the skeleton's list, which includes `WebSearch` and `WebFetch`, because a challenger may search the web.
   - `model: inherit`: the whole forge runs on the session model.
   - `skills`: the entry `challenger-contract`.
3. Delete the comment that the skeleton carries.
4. Write the `## Lens` section in two parts:
   - Who you are: a role of its own (for example a CTO or a strategist), never a mirror of the principal. It gives the register and the vantage point from which the persona reviews the thinking as an equal, with no stake in the principal being right.
   - What to go after: the blind spots this lens exists to find, as a list of concrete angles.
5. Leave the rest to the contract. The file holds the front-matter and the Lens section and nothing else. The contract owns the subject and its boundary, the way of working, the report shape and the ledger step. The Lens may narrow what is read or make a shared rule stricter. It never renames, drops or repeats a shared rule or field.

You should now see one new file, with the front-matter filled, no skeleton comment, and a Lens section of two parts.

## Prove it

Run the check of the engine:

```
/check engine
```

You should now see the check report that the engine conforms to its conventions, or findings that name what to correct in the file.

Then list the roster and run the persona on a target:

```
/challenge
/challenge <persona> intent
```

You should now see `<persona>` in the roster with its description. After the run you should see a file `challenges/YYYY-MM-DD-challenge-<persona>.md` in the project and the new challenges in the ledger's Challenges table, in state `open`.

## Record and release

The persona is recorded and released as any change of the forge. [Make a change to the forge](how-a-change-is-made.md) gives the steps for proving, recording and releasing it.

## A worked example

The persona is `<persona>`. The file is `.claude/agents/challenger-<persona>.md`:

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

<Who you are: the role, the register and the vantage point, as an
equal with no stake in the principal being right.>

<What to go after: the blind spots this lens exists to find, one
concrete angle to a line.>
```

You should now see the file in the roster after `/challenge` is typed bare, and a run of `/challenge <persona>` on a project writes its report as the contract's shape says.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The challenger](../about/the-challenger.md): what the contract owns.
- [Challenger personas](../reference/challenger-personas.md): the personas that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
