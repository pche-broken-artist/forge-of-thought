---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 205bd32c288db29a
inputs:
  - templates/critic-definition.md
  - .claude/skills/critic-contract/SKILL.md
  - .claude/skills/critique/SKILL.md
  - CLAUDE.md#Isolated reviewers
---

# Add a critic lens

This page tells an extender how to add a new critic lens to the forge. A lens is one agent file that makes an isolated reviewer (a subagent, that is a helper Claude starts in a context of its own) look at the quality of a project's documents from one angle. The reader is someone who has decided, or been told by the principal (the person whose thinking is forged), that a new angle is needed.

## Before you start

A lens is added only by the principal's decision. It is added only where what it finds genuinely differs from what the existing lenses find. The lenses that exist are listed in [Critic lenses](../reference/critic-lenses.md); read that list first, so that the new lens does not repeat one.

A lens judges the quality of the documents, never the substance of the thinking. Substance belongs to the challenger personas. What every lens shares is owned by the critic contract, described in [The critic](../about/the-critic.md). Your lens file does not restate it.

The addition is a change of the forge like any other: it is proved, recorded and released as one. How that goes is described in [Make a change to the forge](how-a-change-is-made.md).

## The files

You add one file:

- `.claude/agents/critic-<lens>.md`: the agent file of the lens, made from the skeleton `templates/critic-definition.md`.

The command `/critique` does not change. It finds lenses by scanning `.claude/agents/critic-*.md`, so the new file is on the roster as soon as it exists.

## Steps

1. Copy `templates/critic-definition.md` to `.claude/agents/critic-<lens>.md`. The name after `critic-` is the lens name.
2. Fill the front-matter:
   - `name`: `critic-<lens>`.
   - `description`: one line saying what the lens reads and when it fits. This line is the lens's entry on the roster, and `/critique` recommends a lens by the fit it states there.
   - `tools`: `Read, Glob, Grep`, as the skeleton has them.
   - `model`: `inherit`, so that the lens runs on the model of the session.
   - `skills`: the single entry `critic-contract`, which loads the shared behaviour into the lens.
3. Quote the description whole if it contains a colon followed by a space. Use single quotes, and double any apostrophe inside. Without the quotes the agent does not register.
4. Delete the comment block of the skeleton from the lens file.
5. Write the `## Lens` section. It has four parts:
   - What you read: each artefact on its own, or the chain as a whole, and how a named target narrows the work.
   - What to go after: the defects this lens exists to find, as a list of concrete angles.
   - Categories: the vocabulary of the `[category]` field of a finding.
   - Own report sections: what this lens appends to the shared report shape, if anything.
6. Leave out everything the contract owns: the subject, the way of working, the calibration and the report shape. The Lens section may narrow what is read or make a shared rule stricter. It never renames, drops or duplicates a shared rule or field.

## Prove it

Run the engine check, which verifies the engine's files against the conventions:

```
/check engine
```

Then list the roster and see that the new lens appears with its description:

```
/critique
```

Then run the lens on a project, naming an artefact if you want to test how a target narrows the run:

```
/critique <lens> intent <slug>
```

You should now see a report with the delta summary, its findings in your categories, and any own sections your lens defines. The lens writes no file. The command files the report in the project's `reviews/` folder and offers a walkthrough (a one-item-at-a-time pass over the findings, closed by the principal's verdict on each).

## Record and release

Record the addition in the history of the engine and release it, as [Make a change to the forge](how-a-change-is-made.md) describes.

## A worked example

The lens name here is the placeholder `<lens>`. The file `.claude/agents/critic-<lens>.md` reads:

```markdown
---
name: critic-<lens>
description: 'Critic lens "<lens>": reads <what it reads, in one line>. Reviews the quality of the documents. Not a challenger of the thinking.'
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
- <category>

### Own report sections
<what this lens appends to the report, or nothing>
```

The description carries a colon followed by a space, so it is quoted whole in single quotes. Without them the agent would not register.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The critic](../about/the-critic.md): what the contract owns.
- [Critic lenses](../reference/critic-lenses.md): the lenses that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
