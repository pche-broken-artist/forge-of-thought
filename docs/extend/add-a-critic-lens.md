---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 8aa44830ae8264aa
inputs:
  - templates/critic-definition.md
  - .claude/skills/critic-contract/SKILL.md
  - .claude/skills/critique/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a critic lens

A critic lens is one agent file that reviews the quality of a project's documents through one angle. This page is for the extender who wants to add a lens: it says which file to write, what goes into it and how to show that it works.

## Before you start

Adding a lens is the principal's decision. The principal is the person whose thinking is being forged. A lens is added only where what it finds genuinely differs from what the existing lenses find. The lenses that exist are listed on [Critic lenses](../reference/critic-lenses.md), and they serve as models of the shape.

A lens does not restate the contract that every lens shares. The contract owns the subject, the way of working and the shape of the report. [The critic](../about/the-critic.md) says what it owns. Your file adds only what is particular to the lens.

The change is made, proved, recorded and released as any change of the forge. [Make a change to the forge](how-a-change-is-made.md) says how. Terms used here are in the [Glossary](../reference/glossary.md).

## The files

One new file is needed, made from a template:

| File | What it is |
|---|---|
| `templates/critic-definition.md` | The template to start from: front-matter and a Lens section, nothing else. |
| `.claude/agents/critic-<lens>.md` | The file you write. The name after `critic-` is the name of the lens. |

The contract that the new agent carries is `.claude/skills/critic-contract/SKILL.md`. You do not edit it. A change to what every lens shares is a change of the contract alone.

The command `/critique` does not change when a lens is added. It finds lenses by scanning `.claude/agents/critic-*.md`.

## Steps

1. Copy `templates/critic-definition.md` to `.claude/agents/critic-<lens>.md`.
2. Fill the front-matter. It has five keys:
   - `name`: `critic-<lens>`.
   - `description`: one line that says what the lens reads and when it fits. Keep the closing sentences of the template (that it reviews the quality of the documents and is not a challenger of the thinking).
   - `tools`: as the template has them.
   - `model`: `inherit`, so that the lens runs on the same model as the rest of the forge.
   - `skills`: a list holding `critic-contract`, which preloads the shared behaviour into the lens.
3. Check the description for a colon followed by a space. If it has one, put the whole description in single quotes. An apostrophe inside the description is doubled. Without the quotes the agent does not register.
4. Delete the comment block of the template.
5. Write the Lens section in four parts:
   - What you read: each artefact on its own, or the chain as a whole, and how a target narrows it.
   - What to go after: the defects this lens exists to find, as a list of concrete angles.
   - Categories: the vocabulary of the category field of a finding.
   - Own report sections: what the lens appends to the shared report shape, if anything.
6. Read the Lens section once against the contract. A lens may narrow what it reads or make a shared rule stricter. It never renames, drops or duplicates a shared rule or a shared field. Anything of that kind is removed from the lens file.

The description is also the roster line. Bare `/critique` and `/man critique` list each lens by its description and recommend one by the fit it states. A vague description therefore weakens the roster.

## Prove it

Run the engine check, which verifies mechanical conformance with the conventions:

```
/check engine
```

You should now see a report with no finding about the new file. A run that finds nothing files nothing.

Then run the lens on a project, so that you see it register and work:

```
/critique
/critique <lens> intent <project-slug>
```

You should now see the new lens in the roster of the bare command. You should then see a review file named `YYYY-MM-DD-critique-<lens>.md` in the project's `reviews/` directory, and its findings entered in the project's ledger. The ledger is the single record of state of a project.

If the lens is missing from the roster, look at the description first: a colon followed by a space in an unquoted description is the usual cause.

## Record and release

Record the addition and release it as any change of the forge, by the steps of [Make a change to the forge](how-a-change-is-made.md).

## A worked example

A lens with the placeholder name `<lens>` that reads the assignment for wording that two recipients could read differently. The file is `.claude/agents/critic-<lens>.md`:

```markdown
---
name: critic-<lens>
description: 'Critic lens "<lens>": reads the assignment for wording that two recipients could read differently. Fits once an assignment exists. Reviews the quality of the documents. Not a challenger of the thinking.'
tools: Read, Edit, Write, Glob, Grep
model: inherit
skills:
  - critic-contract
---

## Lens

### What you read
The assignment. With a target, only the named artefact.

### What to go after
- An item whose subject can be read in two ways.
- An item that says "as appropriate" without saying by whom.

### Categories
`ambiguity`, `vague-actor`

### Own report sections
None.
```

The description holds a colon followed by a space, so it is quoted whole. The Lens section says only what is particular to this lens. The shared report shape, the regression of earlier findings and the ledger step are not mentioned, because the contract owns them.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The critic](../about/the-critic.md): what the contract owns.
- [Critic lenses](../reference/critic-lenses.md): the lenses that exist, as models of the shape.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
