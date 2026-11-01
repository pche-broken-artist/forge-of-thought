---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: ca5de09916fbef6b
inputs:
  - templates/challenger-definition.md
  - .claude/skills/challenger-contract/SKILL.md
  - .claude/skills/challenge/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a challenger persona

This page shows how to add a new challenger persona to the forge. A persona is one agent file that reviews the substance of the principal's thinking (the principal is the person whose thinking is being forged) from a vantage point of its own. The page is for an extender who has decided that a new set of blind spots needs its own reviewer.

## Before you start

A new persona is added only by the principal's decision, and only where what it would find genuinely differs from what the existing personas find. Look at the personas that exist first: [Challenger personas](../reference/challenger-personas.md). If one of them already covers the blind spots you have in mind, you do not need a new file.

The persona shares its behaviour with every other persona through one contract, so your file does not restate it. What the contract owns is explained in [The challenger](../about/the-challenger.md). Terms of the forge are defined in [Glossary](../reference/glossary.md).

The addition is a change like any other: it is proved, recorded and released as the page [Make a change to the forge](how-a-change-is-made.md) describes.

## The files

You add one file and edit none:

- `.claude/agents/challenger-<persona>.md`: the agent file of the persona. `<persona>` is the persona's short name.

The command `/challenge` finds personas by scanning `.claude/agents/challenger-*.md`. Bare `/challenge` lists what the scan finds, so the new persona appears in the roster without any other file being touched, and the command itself does not change.

## Steps

1. Copy `templates/challenger-definition.md` to `.claude/agents/challenger-<persona>.md`.

   You should now see a file with front-matter, a comment and an empty `## Lens` heading.

2. Fill the front-matter. It has five fields:

   - `name`: `challenger-<persona>`. The persona's name is the suffix.
   - `description`: who this persona is, in one line. It is what the roster shows, so it says what blind spots the persona exists to find. If the description contains a colon followed by a space, put the whole description in single quotes, and double any apostrophe inside it. Otherwise the agent does not register.
   - `tools`: keep `Read, Glob, Grep, WebSearch, WebFetch`. The persona reads files and may search the web to ground a claim in how the world works.
   - `model`: keep `inherit`. The whole forge runs on the session model, so the persona uses the same one.
   - `skills`: keep the single entry `challenger-contract`. The contract is loaded into the persona when it starts.

   You should now see the front-matter complete, with the skeleton's values kept except `name` and `description`.

3. Write the `## Lens` section in two parts. This section is the only thing the persona file owns.

   - Who you are: a role of its own (for example an officer of some function, or a strategist), never a mirror of the principal. State the register and the vantage point from which the persona reviews the thinking as an equal, with no stake in the principal being right.
   - What to go after: the blind spots this lens exists to find, as a list of concrete angles.

   You should now see a Lens section with these two parts and nothing else under it.

4. Delete the skeleton's comment from the file.

   You should now see a file that holds only front-matter and the Lens section.

5. Keep the contract out of the file. The Lens may narrow what is read or make a shared rule stricter. It never renames, drops or repeats a shared rule or field of the contract, such as the subject, the way of working or the shape of the report. A change to that protocol is made in the contract alone.

## Prove it

Run the engine check, which verifies the engine's files against the conventions:

```
/check engine
```

You should see no finding about the new file. A run that finds nothing files nothing.

Then run the persona on a target, that is, an artefact of a project or a file named by its path:

```
/challenge <persona> <artefact> <slug>
```

You should see the persona's report presented, with the overall read first, and the report filed in the project's `challenges/` folder. Bare `/challenge` should list the new persona in the roster.

## Record and release

Record and release the new file as any change of the forge, following [Make a change to the forge](how-a-change-is-made.md).

## A worked example

The persona is called `<persona>`. Its file `.claude/agents/challenger-<persona>.md` reads, in outline:

```
---
name: challenger-<persona>
description: Challenger persona "<persona>" - <who this is, in one line>. Challenges the substance of the principal's thinking. Not a document auditor.
tools: Read, Glob, Grep, WebSearch, WebFetch
model: inherit
skills:
  - challenger-contract
---

## Lens

<Who you are: the role, the register and the vantage point, as an
equal with no stake in the principal being right.>

<What to go after: a list of concrete angles, the blind spots this
lens exists to find.>
```

After the file is saved, `/check engine` finds nothing, bare `/challenge` lists `<persona>`, and `/challenge <persona>` runs it on a target.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The challenger](../about/the-challenger.md): what the contract owns.
- [Challenger personas](../reference/challenger-personas.md): the personas that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
