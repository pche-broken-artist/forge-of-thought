---
generated: 2026-10-10
made: mirrored
inputs-hash: cfbb241b75b20725
inputs:
  - .claude/skills/new-artefact/SKILL.md
  - templates/artefact-definition.md
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# Add an artefact

This page is for someone who extends the forge with a new kind of
artefact, a new layer of the chain or a new sort of document in it. It
says what `/new-artefact <name>` leads you through, in what order, and
what is left to other commands.

## What the command is for

A kind of artefact is made of several things that are easy to forget:
a reason for it, a definition, a template, item prefixes, reviewers and
a place in the design. `/new-artefact <name>` leads to all of them and
forgets none. It decides nothing. How the kind is composed is your
choice, as for any artefact, and every file is born on your word, one
step at a time. It adds the kind to the engine, for every user of it.

Types other than an artefact are not this command's: a whole chain, a
reviewer and a genre each have their own way in.

## Before you start

If `.claude/skills/forge/states/<name>.md` already exists, the command
stops. A kind that exists is changed through the intent, not added
again.

The ways in are three:

- A brief of the forge project holds the kind, and the command mines it.
- You give a few sentences of what you want, and the kind is handed
  over: Claude works the definition from them and returns a proposal.
- Neither: the command walks the Map below with you by interview.

## What is found

These areas are found in whatever order the conversation takes. An area
may stay empty when it was considered and found not to apply.

- What the artefact is and why it is wanted: for whom, what it holds
  that no other artefact holds, when a project takes it and when it
  does not.
- Where it stands: what it is derived from, what stands above it, its
  number in the chain.
- Its boundary: what of the layer above it cites or carries, what it
  must not hold, and what a layer below takes from it.
- How it is found: the seven blocks of its definition, its Map above
  all.
- What comes out: its template, the sections and the shape of an item.
- Its items: the prefixes, existing or new, and where each lives.
- Its wording: any rule of style of its own.
- Its reviewers: whether it needs a challenger of its own and what that
  one hunts, what the critic must know is no defect in it, whether a
  check must know it.
- How it reaches a reader: whether a render or the README must show it.
- Where it is realised: the item of the solution design.

You say where the new kind meets an existing one, the layer above and
the layer below, and an overlap is raised as a question. You copy no
existing definition: the definitions on disk are models of the shape,
never of the content.

## What is born, in order

1. **A position in the forge intent.** It is written first, through the
   intent's own definition, before anything is built: what the artefact
   is, for whom, from what it is derived and why. Research is proposed
   where the kind has a practice outside the forge, and run on your
   word.
2. **The definition and its template, as a pair.** The definition is
   `.claude/skills/forge/states/<name>.md`, made from the skeleton
   `templates/artefact-definition.md`, in seven blocks: Target, Inputs,
   Aim, Partner, Map, Instruments and Course. Every block is present; a
   block left empty on purpose says so with the reason. The template is
   `templates/<name>.md`. It has no skeleton: each template differs
   whole.
3. **The row of a new prefix** in the ID scheme of `CLAUDE.md`, where
   the kind needs a prefix of its own. A new prefix is proposed and
   waits for your decision.
4. **The reviewers.** A persona file where you decide one is needed,
   and only where what it finds genuinely differs from the others, and
   the calibration of the critic's contract: what the critic must know
   is no defect in the new kind.
5. **The item of the solution design** that says where the kind is
   realised.

## What needs nothing

The rosters need no entry. `/forge`, `/man` and the README read the
definitions from disk, so the new kind appears in them once its
definition exists.

## At the end

The command names what was born and what stays open, then offers
`/check engine`. The check is offered, never run on Claude's own
judgement. It also proposes the first `/forge <name>` on a project.

That first artefact is not the command's. It is made through
`/forge <name>` on real work, and it is the trial: it tells whether the
definition holds.

## See also

- [About elicitation](../about/elicitation.md): the seven blocks and the Map.
- [Add a challenger persona](add-a-challenger-persona.md): the persona a kind may need.
- [Make a change to the forge](how-a-change-is-made.md): proving and releasing the change.
