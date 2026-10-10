---
generated: 2026-10-10
made: mirrored
inputs-hash: 4eeac4a2fd54ca47
inputs:
  - templates/critic-definition.md
  - .claude/skills/critic-contract/SKILL.md
  - .claude/skills/critique/SKILL.md
  - CLAUDE.md
---

# Add a critic lens

This page is for someone extending the forge with a new critic lens: a
new way of reviewing the quality of a project's documents. It says
what the file is made of, what you write in it and what you leave to
the contract.

## Before you start

A new lens is added only by the principal's decision, and only where
what it finds genuinely differs from what the existing lenses find. If
the angle you have in mind is already covered, do not add a lens.

A critic reviews the documents as documents, never the substance of
the thinking behind them. A lens that goes after substance belongs to
the challengers, not here.

## What a lens is

A lens is one agent file, `.claude/agents/critic-<lens>.md`. You make
it from the skeleton `templates/critic-definition.md`. The file has
two things and nothing else: front-matter and a Lens section. The
behaviour every lens shares lives in the contract skill
`critic-contract`, which the front-matter names and which is loaded
into the lens when it runs.

## Steps

1. Copy the skeleton to `.claude/agents/critic-<lens>.md`, with the
   lens's name in place of `<lens>`.
2. Fill the front-matter:
   - `name`: `critic-<lens>`.
   - `description`: one line saying what the lens reads and when it
     fits the project.
   - `tools`: as the skeleton gives them.
   - `model: inherit`, so the lens runs on the session's model.
   - `skills:` with `critic-contract` as its entry.
3. Write the Lens section in four parts:
   1. What the lens reads: each artefact on its own, or the chain as a
      whole, and how a target narrows the read.
   2. What it goes after: the defects the lens exists to find, as a
      list of concrete angles.
   3. Its categories: the vocabulary of the category field of a
      finding.
   4. Its own report sections: whatever it appends to the shared
      report shape, if anything.
4. Delete the comments the skeleton carries, in the front-matter's
   neighbourhood and in the Lens section.

## The description

The description does double duty. It is the line the roster shows when
you run bare `/critique` and in `/man critique`, and the fit it states
is what the roster uses to recommend a lens for the project's state.
Write it so a reader can choose the lens from that line alone.

If the description contains a colon followed by a space, put the whole
description in single quotes, doubling any apostrophe inside it.
Otherwise the agent does not register.

## What the lens does not restate

The contract owns the subject and its boundary, the way of working,
the shape of the report and the ledger step. Do not write any of that
into the lens. A lens is a specialisation of the contract: it may
narrow what is read, or make a shared rule stricter, but it never
renames, drops or duplicates a shared rule or a shared field. If the
protocol must change, it changes in the contract, for every lens at
once.

## Check that it works

- Run `/check engine`. It verifies that the contract skill the lens
  names exists.
- Run bare `/critique` and see that your lens appears in the roster
  with its description.
- Run the lens on a project with `/critique <lens> [artefact]`. The
  run should write a review file and update the project's ledger, as
  the contract says.

Adding the lens does not change the `/critique` command: it finds
lenses by scanning the agent files.

## See also

- [About the critic](../about/the-critic.md): what the contract owns.
- [Critic lenses](../reference/critic-lenses.md): the lenses that exist, as models of the shape.
