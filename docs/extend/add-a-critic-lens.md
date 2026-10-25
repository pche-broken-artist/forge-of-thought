---
generated: 2026-10-25
version: 6.1
made: mirrored
inputs-hash: bf6a7a0e0cdd29e9
inputs:
  - templates/critic-definition.md
  - .claude/skills/critic-contract/SKILL.md
  - .claude/skills/critique/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a critic lens

This page is for the extender who wants a new critic lens. A critic lens is one agent file that reviews the quality of a project's documents from one angle. The page says which file to write, what goes in it, and how to prove that it works.

## Before you start

A new lens is added only by the decision of the principal (the person whose thinking is forged), and only where what it finds genuinely differs from what the existing lenses find. The lenses that exist are listed on [Critic lenses](../reference/critic-lenses.md). Read that page first, so that the new lens does not repeat one of them.

The addition is recorded and released as any change of the forge. How a change is made, proved, recorded and released is on [Make a change to the forge](how-a-change-is-made.md).

A lens does not restate what every lens shares. The shared behaviour (the subject, the way of working, the shape of the report) belongs to one contract, described on [The critic](../about/the-critic.md). Each lens agent (a subagent, that is an isolated Claude run that does not see the working conversation) receives that contract when it starts. The lens file adds only its own section.

## The files

- `.claude/agents/critic-<lens>.md`: the new lens, the only file you write. `<lens>` is the short name of the lens.
- `templates/critic-definition.md`: the skeleton you start from. You read it and do not change it.

The command `/critique` needs no change. It finds lenses by scanning the files `.claude/agents/critic-*.md`.

## Steps

1. Copy `templates/critic-definition.md` to `.claude/agents/critic-<lens>.md`.
2. Fill the front-matter. It has these keys:
   - `name`: `critic-<lens>`.
   - `description`: one line that says what this lens reads, what it reviews and when it fits.
   - `tools`: `Read, Glob, Grep`, as the skeleton has it.
   - `model`: `inherit`, so that the lens runs on the model of the session.
   - `skills`: a list with one entry, `critic-contract`.
3. Quote the description if it needs it. When the description carries a colon followed by a space, put the whole description in single quotes. An apostrophe inside it is doubled. Without the quotes the agent does not register.
4. Delete the comment block of the skeleton.
5. Write the `## Lens` section. It has four parts and nothing else:
   - What you read: each artefact on its own, or the chain as a whole, and how a target narrows the run.
   - What to go after: the defects this lens exists to find, as a list of concrete angles.
   - Categories: the vocabulary of the `[category]` field of a finding.
   - Own report sections: what this lens appends to the shared report shape, if anything.
6. Check the file against the contract. A Lens section specialises the contract and never replaces it. It may narrow what is read or make a shared rule stricter. It never renames, drops or duplicates a shared rule or a shared field. If the protocol itself should change, the change belongs in the contract and not in the lens.

The description is the line that the roster shows. Bare `/critique` lists the lenses from their descriptions and recommends the one that fits the project's state by the fit the description states. Write it so that a reader can choose the lens from that line alone.

## Prove it

Run the engine check on the change:

```
/check engine
```

Then run the new lens on a project, so that you see it register and report:

```
/critique <lens> [artefact] [slug]
```

You should see the lens in the roster that bare `/critique` prints, and a report in the shared shape from the run. If the lens does not appear in the roster, look first at the description for an unquoted colon followed by a space.

## Record and release

Record the change and release it as any other change of the forge. The steps are on [Make a change to the forge](how-a-change-is-made.md).

## A worked example

This is the shape of a lens file, with `<lens>` as a placeholder. The text in angle brackets is for you to fill.

```
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
- <a concrete angle>
- <another concrete angle>

### Categories
<the words allowed in the [category] field of a finding>

### Own report sections
<what this lens appends to the shared report, or nothing>
```

The description in this example is quoted because it carries a colon followed by a space.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The critic](../about/the-critic.md): what the contract owns.
- [Critic lenses](../reference/critic-lenses.md): the lenses that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.1 from the files the front-matter names; never edited by hand.
