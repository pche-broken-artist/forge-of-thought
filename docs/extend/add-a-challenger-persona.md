---
generated: 2026-10-09
made: mirrored
inputs:
  - templates/challenger-definition.md
  - .claude/skills/challenger-contract/SKILL.md
  - .claude/skills/challenge/SKILL.md
  - CLAUDE.md
---

# Add a challenger persona

This page is for someone extending the forge who wants a new
challenger persona: a reviewer that challenges the substance of the
principal's thinking from a vantage point of its own. It says what
the one file is, what goes in it, and how to see that it works.

## Before you start

A persona is added only by the principal's decision, and only where
what it finds genuinely differs from the personas that exist. Two
personas that would say the same thing in different words are noise,
not coverage. If the angle you have in mind is already someone's
blind spot, do not add a persona.

A persona costs one file and no edits. The `/challenge` command does
not change, because the roster is made by scanning the agent files.

## Steps

1. Copy `templates/challenger-definition.md` to
   `.claude/agents/challenger-<persona>.md`, with the persona's name
   in place of `<persona>`.
2. Fill the front-matter:
   - `name`: `challenger-<persona>`.
   - `description`: one line saying who this persona is. The
     skeleton's form is `Challenger persona "<persona>" - <who this
     is, in one line>. Challenges the substance of the principal's
     thinking. Not a document auditor.` The roster shows this line,
     so it is how the persona is recognised.
   - `tools`: keep the skeleton's list. It includes web search and
     fetch, because a persona grounds its claims in how the world
     works.
   - `model`: `inherit`. The whole forge runs on one model.
   - `skills`: `challenger-contract`.
3. If the description contains a colon followed by a space, put the
   whole description in single quotes (an apostrophe inside is
   doubled). Otherwise the agent does not register.
4. Delete the comment block the skeleton carries.
5. Write the Lens section, the only section of the file that is the
   persona's own, in two parts:
   - **Who you are.** A role of its own, not a mirror of the
     principal: the register and the vantage point from which the
     persona reviews the thinking as an equal, with no stake in the
     principal being right.
   - **What to go after.** The blind spots this persona exists to
     find, as a list of concrete angles.

## What the file does not contain

Nothing of the contract is restated. The subject, the way of
working, the severity marks, the report shape and the ledger step
come from the contract skill, which is loaded into the persona
through the `skills` field. A Lens section specialises the contract;
it may narrow what is read or make a shared rule stricter, but it
never renames, drops or duplicates a shared rule or field. A change
to the shared protocol is made in the contract alone. See
[About the challenger](../about/the-challenger.md) for what the
contract owns.

Instance facts such as names, roles, addresses or hosts do not
belong in the file or in any report the persona writes.

## Check that it works

- Run `/check engine`. It verifies the engine against the
  conventions, and the new file is part of what it reads.
- Run bare `/challenge`. The new persona should appear in the
  roster with its description line.
- Run `/challenge <persona> [artefact]` on a target. You should get
  a dated file in the project's `challenges/` directory and new
  open entries in the ledger's Challenges table. The persona's name
  is the suffix of its agent name, and the report is named after it.

## See also

- [About the challenger](../about/the-challenger.md): what the
  contract owns.
- [Challenger personas](../reference/challenger-personas.md): the
  personas that exist.
