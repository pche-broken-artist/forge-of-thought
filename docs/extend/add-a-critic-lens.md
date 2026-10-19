---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 5b7dd71033f628e6
inputs:
  - templates/critic-definition.md
  - .claude/skills/critic-contract/SKILL.md
  - .claude/skills/critique/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a critic lens

This page shows an extender how to add a new critic lens to the forge. A critic lens is one agent file that reviews the quality of a project's documents through one angle, never the substance of the thinking. The page covers the file, the steps, the proof and the release.

## Before you start

A lens is added only by the principal's decision (the principal is whoever's thinking is being forged), and only where what the new lens finds genuinely differs from what the existing lenses find. Check the lenses that exist in [Critic lenses](../reference/critic-lenses.md) first. What the shared contract owns is explained in [The critic](../about/the-critic.md).

The addition is recorded and released as any change of the forge. How a change is made is described in [Make a change to the forge](how-a-change-is-made.md). Terms of the forge are glossed in the [Glossary](../reference/glossary.md).

## The files

One file is added: `.claude/agents/critic-<lens>.md`. It is made from the skeleton `templates/critic-definition.md`.

The command `/critique` does not change. It finds lenses by scanning the agent files, so a new file is a new lens.

The file has two parts.

- The front-matter, which holds these fields:
  - `name`: `critic-<lens>`
  - `description`: the line that the bare `/critique` roster shows, so it says what this lens reads and when it fits
  - `tools`: `Read, Glob, Grep`
  - `model`: `inherit`
  - `skills`: a list with one entry, `critic-contract`
- The Lens section, the only part of the body the lens owns.

The contract skill `critic-contract` is preloaded into the lens at launch. It owns the conduct and isolation, the subject and its boundary, the way of working and the shape of the report. The lens file restates none of it. A Lens section specialises the contract: it may narrow what is read or make a shared rule stricter. It never renames, drops or duplicates a shared rule or field.

## Steps

1. Copy `templates/critic-definition.md` to `.claude/agents/critic-<lens>.md`, with `<lens>` replaced by the lens's name.
2. Set `name` to `critic-<lens>`.
3. Write the `description`: Critic lens "<lens>", one line on what it reads, then that it reviews the quality of the documents and is not a challenger of the thinking.
4. If the description carries a colon followed by a space, put the whole description in single quotes, and double any apostrophe inside. Otherwise the agent does not register.
5. Leave `tools`, `model` and `skills` as the skeleton has them. `model: inherit` keeps the lens on the model of the session, so a lens is never a weaker reviewer.
6. Delete the comment block of the skeleton.
7. Write the Lens section in four parts:
   - What it reads: each artefact on its own, or the chain as a whole, and how a target narrows the reading.
   - What to go after: the defects this lens exists to find, as a list of concrete angles.
   - Categories: the vocabulary of the `[category]` field of a finding.
   - Own report sections: what the lens appends to the shared report shape, if anything. Leave the part out if there is nothing.
8. Take the angles from what only this lens finds. Do not copy the angles of an existing lens.

You should now see one new file in `.claude/agents/`, with front-matter that names the contract skill and a Lens section of its own.

## Prove it

Run the engine check, which verifies the engine against its conventions:

```
/check engine
```

You should now see no finding about the new file, or a finding that names what to correct.

Then run the lens on a project:

```
/critique <lens> <project-slug>
```

You should now see the lens appear in the roster of a bare `/critique`, and a report whose front-matter names `lens: <lens>`. The command files the report in the project's `reviews/` and offers a walkthrough of its findings.

## Record and release

The new file and the record of the decision to add it are saved and released as any change. The steps are on [Make a change to the forge](how-a-change-is-made.md).

## A worked example

A lens named `<lens>`, in `.claude/agents/critic-<lens>.md`. The description contains a colon followed by a space, so it is quoted whole:

```markdown
---
name: critic-<lens>
description: 'Critic lens "<lens>": <what this lens reads, in one line>. Reviews the quality of the documents. Not a challenger of the thinking.'
tools: Read, Glob, Grep
model: inherit
skills:
  - critic-contract
---

## Lens

### What you read
<each artefact on its own, or the chain as a whole; how a target narrows it>

### What to go after
- <a concrete angle only this lens finds>
- <another concrete angle>

### Categories
- <category-one>
- <category-two>

### Own report sections
<what this lens appends to the shared report, or leave the part out>
```

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The critic](../about/the-critic.md): what the contract owns.
- [Critic lenses](../reference/critic-lenses.md): the lenses that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
