---
generated: 2026-10-09
made: mirrored
inputs-hash: 26c71781b47b1432
inputs:
  - .claude/skills/new-artefact/SKILL.md
  - templates/artefact-definition.md
  - CLAUDE.md
  - projects/forge/10-intent.md
---

# Add an artefact

This page is for someone who wants the forge to have a new kind of
artefact in its chain. It says what `/new-artefact <name>` does, what
is found and born in what order, and where the work ends.

## What the command does

`/new-artefact <name>` adds a new kind of artefact to the forge. It
leads you to everything a kind needs, so that you do not have to know
by heart what a kind is made of, and it decides nothing. How the kind
is composed is your choice, as for any artefact, and each file is born
on your word. For now the command adds the kind to the engine, for
every user of it.

If `.claude/skills/forge/states/<name>.md` already exists, the command
stops: a kind that exists is changed through the intent, not added.

## Ways in

- A brief of the forge project already holds the kind, and it is mined.
- You give a few sentences of what you want, and the kind is handed
  over: a proposal comes back, with what was assumed and chosen.
- Neither, and the Map below is walked by interview.

You say where the new kind meets an existing one, the layer above and
the layer below, and an overlap is raised as a question. No existing
definition is copied: the kind is written from what was found, the
definitions on disk being models of the shape and not of the content.

## The Map: what is found

The order is free, and an area may stay empty when it was considered
and found not to apply.

- What the artefact is and why it is wanted: for whom, what it holds
  that no other artefact holds, when a project takes it and when not.
- Where it stands: what it is derived from, what stands above it, its
  number in the chain.
- The boundary: what the layer above cites or carries, what the new
  artefact must not hold, what a layer below takes from it.
- How it is found: the seven blocks of its definition, its Map above
  all.
- What comes out: its template, the sections and the shape of an item.
- Its items: the prefixes, existing or new, and where each lives.
- Its wording: any rule of style of its own.
- Its reviewers: whether it needs a challenger of its own and what
  that one hunts, what the critic must know is no defect in it,
  whether a check must know it.
- How it reaches a reader: whether a render or the README must show it.
- Where it is realised: the item of the solution design.

## What is born, in order

1. **A position in the forge intent**, written through
   `/forge intent forge` before anything is built. It holds what the
   artefact is, for whom, from what it is derived and why.
2. **The definition** `.claude/skills/forge/states/<name>.md`, from the
   skeleton `templates/artefact-definition.md`. It has the seven
   blocks: Target, Inputs, Aim, Partner, Map, Instruments, Course.
   Every block is present; one left empty on purpose says so with the
   reason. The skeleton also fixes how files are made: the first
   artefact is created from its template as v0.1, with a history
   companion and a row in the ledger's Documents table.
3. **The template** `templates/<name>.md`. It has no skeleton, because
   each template differs whole.
4. **The row of a new prefix** in the ID scheme of `CLAUDE.md`, where
   the kind needs its own prefix for its items.
5. **The reviewers**: a challenger persona file where you decide one is
   needed, and the calibration of the critic's contract, so that the
   critic knows what is no defect in the new kind. A persona is added
   only where what it finds genuinely differs.
6. **The item of the solution design**, through
   `/forge solution-design forge`, naming where the kind is realised.

If the kind has a practice outside the forge, `/research <topic>` is
proposed and run on your word.

## What the rosters need

Nothing. `/forge`, `/man` and the README read the definitions from
disk, so the new kind appears in them without further edits.

## At the end

The command names what was born and what stays open, then offers
`/check engine`. The check is offered once the kind stands and is
never run without your word. It also proposes a first `/forge <name>`
on a project.

## The trial

The command does not tell whether the definition holds. The first
artefact of the kind, made through `/forge <name>` on real work, does:
that is the trial. A kind that exists is afterwards changed through
the intent.

## See also

- [About elicitation](../about/elicitation.md): the seven blocks and the Map.
- [Add a challenger persona](add-a-challenger-persona.md): the persona a kind may need.
- [Make a change to the forge](how-a-change-is-made.md): proving and releasing the change.
