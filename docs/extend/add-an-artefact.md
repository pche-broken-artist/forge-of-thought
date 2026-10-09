---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/new-artefact/SKILL.md
  - templates/artefact-definition.md
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# Add an artefact

This page is for someone who extends the forge and wants a new kind
of artefact in the chain. It says what `/new-artefact <name>` does,
what it leads you to, in what order, and what is yours to decide.

## What the command is for

A kind of artefact is made of several things, and two of them, a
prefix for its items and a challenger, are easily forgotten when the
kind is added by hand. `/new-artefact <name>` leads you to all of
them so that none is missed. It decides nothing: how the kind is
composed is your choice, as for any artefact, and every file is born
on your word, one step at a time.

If the file `.claude/skills/forge/states/<name>.md` already exists,
the command stops. A kind that exists is not added again; it is
changed through the intent.

For now the command adds the kind to the engine, for everyone who
uses it. It adds a kind of artefact only. A whole chain, a reviewer
and a genre are other types and are not its business.

## Ways in

- You have written a brief of the forge project that holds the kind:
  it is mined.
- You give a few sentences of what you want: the kind is handed over,
  and Claude returns a proposal with what he assumed and what he
  chose.
- Neither: the Map below is walked as an interview, one question at a
  time.

You say where the new kind meets an existing one, the layer above it
and the layer below, and you raise any overlap as a question. You
copy no existing definition: the definitions on disk are models of
the shape, never of the content.

## What is found: the Map

The areas may be found in any order. An area may stay empty when it
was considered and found not to apply.

- What the artefact is and why it is wanted: for whom, what it holds
  that no other artefact holds, when a project takes it and when it
  does not.
- Where it stands: what it is derived from, what stands above it,
  its number in the chain.
- The boundary: what of the layer above it cites or carries, what it
  must not hold, and what a layer below takes from it.
- How it is found: the seven blocks of its definition, its Map above
  all.
- What comes out: its template, the sections and the shape of an
  item.
- Its items: the prefixes, existing or new, and where each lives.
- Its wording: any rule of style of its own.
- Its reviewers: whether it needs a challenger of its own and what
  that one hunts, what the critic must know is no defect in it,
  whether a check must know it.
- How it reaches a reader: whether a render or the README must show
  it.
- Where it is realised: the item of the solution design.

## What is born, in order

1. **A position in the forge intent.** First, before anything is
   built, through `/forge intent forge`: what the kind is, for whom,
   from what it is derived and why.
2. **The definition**, `.claude/skills/forge/states/<name>.md`, in
   the seven blocks (Target, Inputs, Aim, Partner, Map, Instruments,
   Course), written from the skeleton
   `templates/artefact-definition.md`. Every block is present; a
   block left empty on purpose says so, with the reason.
3. **The template**, `templates/<name>.md`. It has no skeleton:
   each template differs whole, so it is written from what was found.
4. **The prefix.** If the items of the kind need a prefix of their
   own, a row for it is added to the ID scheme in `CLAUDE.md`.
5. **The reviewers.** A challenger persona file where you decide the
   kind needs one, and the calibration of the critic's contract where
   you decide it must know something about the kind. A persona is
   added only where what it finds genuinely differs; see
   [Add a challenger persona](add-a-challenger-persona.md).
6. **The item of the solution design**, through
   `/forge solution-design forge`, naming where the kind is realised.

If the kind has a practice outside the forge, `/research <topic>` is
proposed and run on your word.

## What you see at the end

The command names what was born and what stays open, then offers
`/check engine`. The check is offered, never run on Claude's own
judgement. It also proposes the first `/forge <name>` on a project.

The rosters need nothing added: `/forge`, `/man` and the README read
the definitions from disk, so the new kind appears in them by itself.

## The trial

The command is complete when every area of the Map has been found or
knowingly left. Whether the definition holds is not told by the
command. It is told by the first artefact of the kind, made through
`/forge <name>` on real work.

For how the elicitation shape that the definition follows is
explained, see [About elicitation](../about/elicitation.md). For
proving and releasing the change, see
[Make a change to the forge](how-a-change-is-made.md).

## See also

- [About elicitation](../about/elicitation.md): the seven blocks and
  the Map.
- [Add a challenger persona](add-a-challenger-persona.md): the
  persona a kind may need.
- [Make a change to the forge](how-a-change-is-made.md): proving and
  releasing the change.
