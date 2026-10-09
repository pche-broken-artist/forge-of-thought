---
generated: 2026-10-09
made: mirrored
inputs-hash: 85973edaa2b2f134
inputs:
  - templates/challenger-definition.md
  - .claude/skills/challenger-contract/SKILL.md
  - .claude/skills/challenge/SKILL.md
  - CLAUDE.md
---

# Add a challenger persona

This page is for someone extending the forge who wants a new
challenger persona: another isolated reviewer that tests the substance
of the principal's thinking from a vantage point the existing ones do
not take. A persona is one agent file, and this page says what goes in
it and how to know it works.

## Before you start

A new persona is added only by the principal's decision, and only where
what it finds genuinely differs from the personas already there.
Personas that would say the same thing in different words are noise,
not coverage. Check the existing roster first: bare `/challenge` lists
the personas, and the list of what exists is on
[Challenger personas](../reference/challenger-personas.md).

## Steps

1. **Copy the skeleton.** Start from
   `templates/challenger-definition.md` and save it as
   `.claude/agents/challenger-<persona>.md`. The suffix of the file
   name is the persona's name.

2. **Fill the front-matter.** It has five keys:
   - `name`: `challenger-<persona>`.
   - `description`: one line saying who this persona is, in the form
     the skeleton gives. It ends by saying the persona challenges the
     substance of the principal's thinking and is not a document
     auditor. The description is what the roster shows, so it is how
     the principal picks the persona.
   - `tools`: the skeleton's list, which includes web search and web
     fetch, because a challenge may need to be grounded in how the
     world actually works.
   - `model: inherit`: the whole forge runs on the session model.
   - `skills`: the single entry `challenger-contract`, which loads the
     shared behaviour into the persona.

   If the description contains a colon followed by a space, put the
   whole description in single quotes (an apostrophe inside is
   doubled). Otherwise the agent does not register.

3. **Write the Lens section.** It is the only body the file has, in two
   parts:
   - *Who you are.* A role of its own, such as a CTO or a strategist,
     never a mirror of the principal. It gives the register and the
     vantage point from which the persona reviews the thinking as an
     equal, with no stake in the principal being right.
   - *What to go after.* The blind spots this persona exists to find,
     as a list of concrete angles.

4. **Delete the comment.** The skeleton carries an HTML comment that
   explains itself. Remove it from the persona file.

## What the file must not contain

Nothing of the contract is restated. The contract skill owns the
subject (substance, not document quality), the way of working, the
severity marks, the ban on fabrication and the shape of the report. A
Lens section is a specialisation of it: it may narrow what is read or
make a shared rule stricter, but it never renames, drops or duplicates
a shared rule or field. If the protocol itself should change, that
change is made in the contract alone. What the contract owns is
explained on [About the challenger](../about/the-challenger.md).

## What you do not have to change

A persona costs one file and no edits elsewhere. `/challenge` scans
`.claude/agents/challenger-*.md` for its roster, so the new persona
appears in bare `/challenge` and can be run as
`/challenge <persona> [artefact]` without touching the command.

## Check that it works

- Run `/check engine`, the mechanical conformance check of the engine.
- Run the persona on a target, for example
  `/challenge <persona> intent`. It should write
  `challenges/YYYY-MM-DD-challenge-<persona>.md` in the project and
  add its challenges to the ledger as `open`.

## See also

- [About the challenger](../about/the-challenger.md): what the contract owns.
- [Challenger personas](../reference/challenger-personas.md): the personas that exist.
