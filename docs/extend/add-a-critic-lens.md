---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 400969024d8f66ab
inputs:
  - templates/critic-definition.md
  - .claude/skills/critic-contract/SKILL.md
  - .claude/skills/critique/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a critic lens

A critic lens is one agent file that reviews the quality of a project's documents through one angle. This page is for the extender who wants to add a lens, and it shows how to write that one file.

## Before you start

Add a lens only on the decision of the principal, the person whose thinking is being forged. Add it only where what it finds genuinely differs from what the existing lenses find. The lenses that exist are listed in [Critic lenses](../reference/critic-lenses.md).

Read [The critic](../about/the-critic.md) first. The shared behaviour of every lens belongs to the critic contract, a skill that is loaded into each lens agent when it starts. The contract owns the conduct and isolation, the subject and its boundary, the way of working and the shape of the report. Your file never restates any of it.

The lens is recorded and released as any change of the forge is. How that goes is in [Make a change to the forge](how-a-change-is-made.md). Terms of the forge are in the [Glossary](../reference/glossary.md).

## The files

One file is added:

- `.claude/agents/critic-<lens>.md`: the agent file of the lens. Its name suffix is the lens's name, and the contract reads the lens name from it.

Its skeleton is `templates/critic-definition.md`. No command changes: `/critique` finds a lens by scanning the files `.claude/agents/critic-*.md`.

## Steps

1. Copy `templates/critic-definition.md` to `.claude/agents/critic-<lens>.md`.
2. Fill the front-matter:
   - `name`: `critic-<lens>`
   - `description`: the roster line, see the next step
   - `tools`: `Read, Edit, Write, Glob, Grep`, as the skeleton has it
   - `model`: `inherit`
   - `skills`: a list with one member, `critic-contract`
3. Write the `description`. It is the line that bare `/critique` shows in the roster, and `/critique` recommends a lens by the fit the line states. So it says what the lens reads, in one line, that it reviews the quality of the documents, and that it is not a challenger of the thinking. The skeleton shows the shape.
4. Check the description for a colon followed by a space. If it has one, put the whole description in single quotes, and double any apostrophe inside. Otherwise the agent does not register.
5. Delete the comment block of the skeleton.
6. Fill the `## Lens` section in its four parts:
   - What you read: each artefact on its own, or the chain as a whole, and how a target narrows it.
   - What to go after: the defects this lens exists to find, as a list of concrete angles.
   - Categories: the vocabulary of the `[category]` field of a finding.
   - Own report sections: what the lens appends to the shared report shape, if anything.
7. Keep the Lens section a specialisation of the contract. It may narrow what is read or make a shared rule stricter. It never renames, drops or repeats a shared rule or field. A change of protocol is made in the contract alone.

You should now see a single new file in `.claude/agents/`, whose front-matter names the contract and whose body is the Lens section and nothing else.

## Prove it

Run the check of the engine:

```
/check engine
```

You should now see the report of the check, or no report where it finds nothing.

Then run the lens on a project:

```
/critique <lens> [artefact] [project-slug]
```

The target is optional. Without one, the lens reads everything it reads. You should now see a review file `reviews/YYYY-MM-DD-critique-<lens>.md` in the project, the ledger updated with its findings, and the delta summary offered to you in the conversation.

## Record and release

Record the change and release it as any change of the forge, as [Make a change to the forge](how-a-change-is-made.md) says.

## A worked example

A lens named `<lens>` that reads the intent only. The description holds a colon and a space, so it is quoted whole.

```
---
name: critic-<lens>
description: 'Critic lens "<lens>": reads the intent alone, item by item. Reviews the quality of the documents. Not a challenger of the thinking.'
tools: Read, Edit, Write, Glob, Grep
model: inherit
skills:
  - critic-contract
---

## Lens

### What you read
The intent, `10-intent.md`. A target other than the intent
narrows nothing further: the intent is read whole.

### What to go after
- <a concrete angle, one defect this lens exists to find>
- <another concrete angle>

### Categories
<category-one>, <category-two>

### Own report sections
None.
```

You should now see the lens listed by bare `/critique`, with its description as the roster line.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The critic](../about/the-critic.md): what the contract owns.
- [Critic lenses](../reference/critic-lenses.md): the lenses that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
