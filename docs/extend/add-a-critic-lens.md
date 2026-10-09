---
generated: 2026-10-09
made: mirrored
inputs:
  - templates/critic-definition.md
  - .claude/skills/critic-contract/SKILL.md
  - .claude/skills/critique/SKILL.md
  - CLAUDE.md
---

# Add a critic lens

This page is for someone extending the forge who wants a new critic
lens: a new way of reading the documents of a project for quality. It
says what the file is, how to write it and how to see that it works.

A lens is added only by the principal's decision, and only where what
it would find genuinely differs from what the existing lenses find.
If the principal has not decided, propose the lens and wait.

## What a lens is

A lens is one agent file, `.claude/agents/critic-<lens>.md`, made from
the skeleton `templates/critic-definition.md`. It holds the
front-matter and a Lens section, and nothing else. Everything the
lenses share (subject, way of working, report shape, ledger step) is
owned by the contract skill that the front-matter names. The lens file
restates none of it.

A lens may narrow what the contract says or make a shared rule
stricter. It never renames, drops or duplicates a shared rule or
field. If the shared protocol itself needs to change, it changes in
the contract, not in a lens.

## Steps

1. **Copy the skeleton** to `.claude/agents/critic-<lens>.md` and
   replace `<lens>` with the lens's name. The name of the agent is
   `critic-<lens>`, and the lens name is the suffix.
2. **Fill the front-matter.**
   - `name`: `critic-<lens>`.
   - `description`: one line saying what the lens reads and when it
     fits the state of a project. Keep the skeleton's closing
     sentences that say it reviews document quality and does not
     challenge the thinking.
   - `tools`: as the skeleton has them.
   - `model: inherit`: the whole forge runs on the session model.
   - `skills`: the list holding `critic-contract`.
3. **Mind the colon.** If the description contains a colon followed by
   a space, put the whole description in single quotes (an apostrophe
   inside is doubled). Otherwise the agent does not register.
4. **Write the Lens section** in four parts:
   1. *What you read.* Each artefact on its own, or the chain as a
      whole, and how a target narrows the run. Without a target the
      lens reads everything it reads.
   2. *What to go after.* The defects this lens exists to find, as a
      list of concrete angles.
   3. *Categories.* The vocabulary of the `[category]` field of a
      finding.
   4. *Own report sections.* What the lens appends to the shared
      report shape, if anything.
5. **Delete the skeleton's comments** from the lens file.

## What you see afterwards

The description is the lens's line in the roster. Bare `/critique`
scans `.claude/agents/critic-*.md`, lists the lenses and recommends
the one that fits the project's state by the fit each description
states. `/man critique` shows the same roster. The `/critique` command
itself does not change when a lens is added.

## Prove that it works

- Run `/check engine`. It verifies, among other things, that the
  contract skill the lens names exists.
- Run the lens on a project with `/critique <lens> [artefact] [slug]`.
  It should return a review file in the project's `reviews/` and
  update the ledger, and the command presents the delta summary. If
  the lens is missing from bare `/critique`, look first at the colon
  in the description.

Every run of a lens is the principal's word; none runs on its own
judgement.

## See also

- [About the critic](../about/the-critic.md): what the contract owns.
- [Critic lenses](../reference/critic-lenses.md): the lenses that
  exist, as models of the shape.
