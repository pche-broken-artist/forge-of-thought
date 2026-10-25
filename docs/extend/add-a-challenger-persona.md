---
generated: 2026-10-25
version: 6.1
made: mirrored
inputs-hash: 9072d03c025ec65c
inputs:
  - templates/challenger-definition.md
  - .claude/skills/challenger-contract/SKILL.md
  - .claude/skills/challenge/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a challenger persona

This page shows how to add a new challenger persona to the forge. A persona is a reviewer that attacks the substance of the principal's thinking from a vantage point of its own. The principal is the person whose thinking is being forged. The page is for the extender who wants one more such vantage point.

## Before you start

A persona is added only by the principal's decision, and only where what it would find genuinely differs from what the existing personas find. Check the personas that exist first: [Challenger personas](../reference/challenger-personas.md) lists them.

The shared behaviour of every persona (what it reads, how it works, the shape of its report) is owned by the challenger contract. A persona file does not restate it. [The challenger](../about/the-challenger.md) explains what the contract owns.

The addition is a change of the forge like any other. How a change is proved, recorded and released is described in [Make a change to the forge](how-a-change-is-made.md). The addition is recorded and released in that way.

Terms of the forge that appear here are defined in the [Glossary](../reference/glossary.md).

## The files

You write one file:

- `.claude/agents/challenger-<persona>.md`, made from the skeleton `templates/challenger-definition.md`.

You edit nothing else. The `/challenge` command finds personas by scanning `.claude/agents/challenger-*.md`, so the new file joins the roster by existing. The command, the contract and the other personas do not change.

## Steps

1. Copy the skeleton `templates/challenger-definition.md` to `.claude/agents/challenger-<persona>.md`. The suffix of the file name is the persona's name.

   You should now see the new file beside the other `challenger-*.md` files.

2. Fill the front-matter:

   - `name`: `challenger-<persona>`.
   - `description`: one line saying who this persona is and what blind spots it exists to find. This line is what the roster shows, so it is how the persona is recognised and chosen.
   - `tools`: `Read, Glob, Grep, WebSearch, WebFetch`. The persona reads files and may search the web.
   - `model: inherit`. The persona runs on the model of the session.
   - `skills`: a list holding `challenger-contract`. This loads the shared behaviour into the persona.

   If the description holds a colon followed by a space, put the whole description in single quotes, and double any apostrophe inside it. Otherwise the agent does not register.

   You should now see a front-matter whose `name` matches the file name.

3. Delete the comment in the skeleton. The persona file holds the front-matter and the Lens section, nothing else.

4. Write the Lens section in two parts:

   - Who you are. Give the persona a role of its own, such as a CTO or a strategist, never a mirror of the principal. State the register and the vantage point from which it reviews the thinking as an equal, with no stake in the principal being right.
   - What to go after. List the blind spots this persona exists to find, as concrete angles.

   The Lens may narrow what is read or make a shared rule stricter. It never renames, drops or duplicates a rule or a field of the contract.

   You should now see a Lens section with two parts and no sentence that restates the contract.

### A worked example

The file below shows the shape with the placeholder `<persona>`. The angles are generic stand-ins that show the form, not a real persona's.

```markdown
---
name: challenger-<persona>
description: Challenger persona "<persona>" - <who this is, in one line>. Challenges the substance of the principal's thinking. Not a document auditor.
tools: Read, Glob, Grep, WebSearch, WebFetch
model: inherit
skills:
  - challenger-contract
---

## Lens

You are <a role of its own>, reviewing the thinking as an equal from
<its vantage point>, with no stake in the principal being right.

Go after:

- <a concrete angle: a kind of blind spot this role sees>
- <another concrete angle>
- <another concrete angle>
```

## Prove it

Run the checks on the engine:

```
/check engine
```

You should now see the check report no finding about the new file. A run that finds nothing files nothing.

Then see that the roster lists the persona:

```
/challenge
```

You should now see `challenger-<persona>` with its description, among the others.

Then run the persona on a target. The target is an artefact named as `/forge` names it, or any file of the project by its path:

```
/challenge <persona> 10-intent.md <slug>
```

You should now see the persona's report: an overall read, then challenges ordered by severity. The command files the report in the project's `challenges/` folder and offers a walkthrough of the challenges.

## Record and release

Record and release the addition as any change of the forge, by the steps in [Make a change to the forge](how-a-change-is-made.md).

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The challenger](../about/the-challenger.md): what the contract owns.
- [Challenger personas](../reference/challenger-personas.md): the personas that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.1 from the files the front-matter names; never edited by hand.
