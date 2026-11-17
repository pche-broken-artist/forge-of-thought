---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 9e01c907cd2ad9dc
inputs:
  - templates/critic-definition.md
  - .claude/skills/critic-contract/SKILL.md
  - .claude/skills/critique/SKILL.md
  - CLAUDE.md#Isolated reviewers
  - .claude/agents/check-engine.md
---

# Add a critic lens

This page shows how to add a critic lens, a reviewer of the quality
of a project's documents read through one angle, to the forge. It is
written for the extender. A lens is one agent file, and nothing else
has to change.

## Before you start

A new lens is added only by the principal's decision (the person whose
thinking is being forged), and only where what it finds genuinely
differs from what the existing lenses find. Check the existing ones
first in [Critic lenses](../reference/critic-lenses.md). The shared
behaviour of every lens, its subject, way of working and report shape,
belongs to the contract and is explained in [The critic](../about/the-critic.md);
your file never restates it.

The addition is recorded and released as any change of the forge. How
that goes is in [Make a change to the forge](how-a-change-is-made.md).
Terms of the forge are one line each in the [Glossary](../reference/glossary.md).

## The files

One file is added:

- `.claude/agents/critic-<lens>.md`: the lens agent, made from the
  skeleton `templates/critic-definition.md`.

The command `/critique` does not change. It finds the lenses by
scanning `.claude/agents/critic-*.md`, so the new file appears in the
roster of the bare command as soon as it exists.

## Steps

1. Copy `templates/critic-definition.md` to
   `.claude/agents/critic-<lens>.md`. The suffix of the file name is
   the name of the lens.
2. Fill the front-matter. It has five fields:
   - `name`: `critic-<lens>`.
   - `description`: the roster line. It says what the lens reads in
     one line and when it fits, because `/critique` recommends a lens
     by the fit its description states.
   - `tools`: `Read, Glob, Grep`, as the skeleton has them.
   - `model`: `inherit`.
   - `skills`: a list with one member, `critic-contract`.
3. Check the description for a colon followed by a space. If it has
   one, put the whole description in single quotes, and double any
   apostrophe inside it. Otherwise the agent does not register.
4. Write the Lens section in its four parts:
   - What you read: each artefact on its own, or the chain as a whole,
     and how a target narrows it.
   - What to go after: the defects this lens exists to find, as a list
     of concrete angles.
   - Categories: the vocabulary of the `[category]` field of a finding.
   - Own report sections: what the lens appends to the shared report
     shape, if anything. Leave the part out if there is nothing.
5. Delete the comments of the skeleton. Keep only the line that names
   the skeleton where the skeleton has one.
6. Leave out of the Lens section anything the contract already owns:
   the subject, the rules of isolation, the way of working and the
   report shape. A Lens section may narrow what is read or make a
   shared rule stricter. It never renames, drops or duplicates a
   shared rule or field.

## Prove it

Run the engine check, which compares the agents with the core
documents:

```
/check engine
```

You should now see that the check conforms, or findings that name what
does not fit.

Then run the lens once on a project. Use a project slug of your own in
place of `<slug>`:

```
/critique <lens> <slug>
```

You should now see the lens in the bare roster (`/critique` alone),
and a report with its delta summary after the run. The target is
optional: an artefact, a file path, or nothing for the whole chain.

## Record and release

Record and release the new file as any change of the forge, the way
[Make a change to the forge](how-a-change-is-made.md) describes.

## A worked example

A lens named `<lens>` reading one kind of defect across the chain:

```
---
name: critic-<lens>
description: Critic lens "<lens>" - <what it reads, in one line>. Reviews the quality of the documents. Not a challenger of the thinking.
tools: Read, Glob, Grep
model: inherit
skills:
  - critic-contract
---

## Lens

<What you read: the chain as a whole; a target narrows it to that
file with the files around it.>

<What to go after: a list of concrete angles.>

<Categories: the words of the [category] field.>
```

This description has no colon followed by a space, so it needs no
quotes. A description that did, such as `Critic lens "<lens>": ...`,
would be written whole inside single quotes.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [The critic](../about/the-critic.md): what the contract owns.
- [Critic lenses](../reference/critic-lenses.md): the lenses that exist.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
