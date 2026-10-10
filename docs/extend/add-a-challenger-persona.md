---
generated: 2026-10-10
made: mirrored
inputs-hash: fd922b1578b496b1
inputs:
  - templates/challenger-definition.md
  - .claude/skills/challenger-contract/SKILL.md
  - .claude/skills/challenge/SKILL.md
  - CLAUDE.md
---

# Add a challenger persona

This page is for the extender who wants a new challenger persona: a
further reviewer of the substance of the thinking. It says when a
persona is worth adding, what its one file holds, and how to see that
it works.

## Before you start

A persona is added only by the principal's decision, and only where
what it would find genuinely differs from the personas that exist.
Two personas that would say the same thing in different words are
noise. Read the existing roster first (see the list of personas
linked below) and ask what blind spots the new one would see that no
other does.

## What a persona costs

One file and no edits. A persona is an agent file,
`.claude/agents/challenger-<persona>.md`, made from the skeleton
`templates/challenger-definition.md`. The `/challenge` command does
not change: the roster is a scan of the files matching
`.claude/agents/challenger-*.md`, so the new file is found by being
there.

## Steps

1. Copy the skeleton to `.claude/agents/challenger-<persona>.md`,
   with the persona's name as the suffix.
2. Fill the front-matter:
   - `name`: `challenger-<persona>`.
   - `description`: one line saying who this persona is. The
     skeleton's wording is `Challenger persona "<persona>" - <who
     this is, in one line>. Challenges the substance of the
     principal's thinking. Not a document auditor.` This line is
     what the roster shows, so it is how the persona is chosen.
   - `tools`: the skeleton's list, which includes web search and
     fetch, because a persona grounds its challenges in how the
     world actually works.
   - `model: inherit`: the whole forge runs on the one session
     model.
   - `skills: challenger-contract`: the shared behaviour is loaded
     from there.
3. If the description contains a colon followed by a space, put the
   whole description in single quotes (an apostrophe inside is
   doubled). Otherwise the agent does not register.
4. Write the `## Lens` section, in two parts and nothing else:
   - **Who you are.** A role of its own, such as a CTO or a
     strategist, never a mirror of the principal. It gives the
     register and the vantage point from which the persona reviews
     the thinking as an equal, with no stake in the principal being
     right.
   - **What to go after.** The blind spots this persona exists to
     find, as a list of concrete angles.
5. Delete the skeleton's comments from the file.

## What stays out of the file

Nothing of the contract is restated. The contract skill owns the
subject, the way of working, the severity marks, the report shape and
the ledger step for every persona. A Lens section specialises the
contract and never replaces it: it may narrow what is read or make a
shared rule stricter, but it never renames, drops or duplicates a
shared rule or field. If the protocol should change, it changes in
the contract alone.

## Check that it works

- Run `/check engine`, the mechanical check of the engine's
  conformance with its conventions.
- Run bare `/challenge`: the new persona appears in the roster with
  its description.
- Run `/challenge <persona>` on a target in a project. The persona
  writes its report to `challenges/` and adds its challenges to the
  project's ledger, as the other personas do.

## See also

- [About the challenger](../about/the-challenger.md): what the
  contract owns.
- [Challenger personas](../reference/challenger-personas.md): the
  personas that exist.
