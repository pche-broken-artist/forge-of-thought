---
generated: 2026-10-09
made: mirrored
inputs-hash: 8d6efcce72ecbd61
inputs:
  - templates/critic-definition.md
  - .claude/skills/critic-contract/SKILL.md
  - .claude/skills/critique/SKILL.md
  - CLAUDE.md
---

# Add a critic lens

This page is for someone extending the forge with a new critic lens: a
further way of reading the quality of a project's documents. It says
what the lens file is made of, what it must leave alone and how to
tell that it works.

## When a lens is warranted

A new lens is added only by the principal's decision, and only where
what it finds genuinely differs from what the existing lenses find.
If the principal has not decided, propose it and wait.

## What a lens is

A lens is one agent file, `.claude/agents/critic-<lens>.md`, made from
the skeleton `templates/critic-definition.md`. The file holds the
front-matter and a Lens section, and nothing else. The behaviour every
lens shares is not in the file: the front-matter names the contract
skill, which is loaded into the lens when it runs (see
[About the critic](../about/the-critic.md) for what the contract owns).

## Steps

1. **Copy the skeleton** to `.claude/agents/critic-<lens>.md` and
   replace `<lens>` with the lens's name. Delete the comments of the
   skeleton in the new file.
2. **Fill the front-matter.** It has these keys:
   - `name`: `critic-<lens>`.
   - `description`: one line saying what the lens reads and when it
     fits the project's state. The skeleton's wording ends with the
     statement that the lens reviews the quality of the documents and
     is not a challenger of the thinking.
   - `tools`: as the skeleton gives them (`Read, Edit, Write, Glob,
     Grep`).
   - `model: inherit`: the whole forge runs on the session model.
   - `skills`: a list holding `critic-contract`.
3. **Quote the description if it needs it.** If the description
   carries a colon followed by a space, put the whole description in
   single quotes, with any apostrophe inside doubled. Otherwise the
   agent does not register.
4. **Write the Lens section** in four parts:
   1. What the lens reads: each artefact on its own, or the chain as
      a whole, and how a target narrows that reading.
   2. What it goes after: the defects the lens exists to find, as a
      list of concrete angles.
   3. Its categories: the vocabulary of the `[category]` field of a
      finding.
   4. Its own report sections: what the lens appends to the shared
      report shape, if anything.

## What the lens must not do

Nothing the contract owns is restated in the lens file. A Lens section
specialises the contract and never replaces it: it may narrow what is
read or make a shared rule stricter, but it may not rename, drop or
duplicate a shared rule or a field. If the protocol needs to change, it
changes in the contract alone.

## Where the description shows

The description is the lens's line in the roster. Bare `/critique`
scans `.claude/agents/critic-*.md`, lists the lenses and recommends the
one that fits the project's state by the fit each description states.
`/man critique` shows the same. The command itself does not change when
a lens is added.

## Check that it works

- Run `/check engine`. It verifies, among other things, that the
  contract skill the lens names exists.
- Run bare `/critique` and see that the new lens appears in the roster
  with its description.
- Run `/critique <lens>` on a project and see that it writes its review
  file in `reviews/` and updates the ledger.

## See also

- [About the critic](../about/the-critic.md): what the contract owns.
- [Critic lenses](../reference/critic-lenses.md): the lenses that exist, as models of the shape.
