---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 521ab03f7ba35dca
inputs:
  - .claude/skills/new-artefact/SKILL.md
  - templates/artefact-definition.md
  - projects/forge/10-intent.md#POS.1980
---

# Add an artefact

This page shows how a new kind of artefact is added to the chain with
`/new-artefact <name>`, for someone who extends the forge. The command
leads to everything a kind needs and decides nothing: Claude proposes,
the principal (whoever's thinking is being forged) decides, and every
file is born on the principal's word.

## Before you start

- Clone the forge's own project beside the engine. The command reads
  and writes it, and whoever develops the engine clones it there.
  A user who only runs the forge never needs it.
- Read [Make a change to the forge](how-a-change-is-made.md). The
  addition is recorded and released as any change of the forge.
- Check that the kind does not exist yet. If
  `.claude/skills/forge/states/<name>.md` is present, the command
  stops, because a kind that exists is changed through the intent and
  not added.
- Decide how the kind is composed. Three ways in are open:
  - a brief written for the kind, which Claude mines;
  - a few sentences of what you want, with which Claude hands back a
    proposal;
  - neither, and the Map below is walked by interview.
- Know where the kind meets an existing one: the layer above it and
  the layer below. An overlap is raised as a question.

## The files

The command leads to these, in the order they are born:

1. A position in the forge intent, which lives in the forge's own
   project.
2. The definition `.claude/skills/forge/states/<name>.md`, written
   from the skeleton `templates/artefact-definition.md`.
3. The template `templates/<name>.md`. It has no skeleton, because
   each template differs whole.
4. The row of a new prefix in CLAUDE.md, in the ID scheme, where the
   kind has items that no existing prefix names.
5. The reviewers where decided: a persona file, and the calibration
   of the critic's contract.
6. The item of the solution design, which names where the kind is
   realised.

The skeleton gives a definition seven blocks, and every block is
present. A block left empty on purpose says so, with the reason. The
blocks are:

- Target
- Inputs
- Aim
- Partner
- Map
- Instruments
- Course

[Elicitation](../about/elicitation.md) says what the blocks and the
Map are. [Templates](../reference/templates.md) lists the skeletons a
definition and a persona start from.

## Steps

1. Run `/new-artefact <name>`. Claude names the target pair and the
   inputs it reads.
2. Walk the Map. An area may stay empty when it was considered and
   found not to apply. The areas are:
   - what the artefact is and why it is wanted: for whom, what it
     holds that no other artefact holds, when a project takes it and
     when it does not;
   - where it stands: what it is derived from, what stands above it,
     its number in the chain;
   - the boundary: what the layer above cites or carries, what the
     artefact must not hold, what a layer below takes from it;
   - how it is found: the seven blocks of its definition, its Map
     above all;
   - what comes out: its template, the sections and the shape of an
     item;
   - its items: the prefixes, existing or new, and where each lives;
   - its wording: any rule of style of its own;
   - its reviewers: whether it needs a challenger of its own and what
     that one hunts, what the critic must know is no defect in it,
     whether a check must know it;
   - how it reaches a reader: whether a render or the README must
     show it;
   - where it is realised: the item of the solution design.
3. Write the position in the intent first, through the intent's own
   definition (`/forge intent forge`). Nothing is built before it.
   You should now see the position in the forge intent.
4. Write the definition and then its template. You should now see
   `.claude/skills/forge/states/<name>.md` and `templates/<name>.md`.
5. Add the row of a new prefix to the ID scheme of CLAUDE.md, where
   the kind needs one.
6. Decide the reviewers. A persona is added only where what it finds
   genuinely differs, and only by your decision; see
   [Add a challenger persona](add-a-challenger-persona.md). A check
   that must know the kind is described in [Add a check](add-a-check.md).
7. Write the item of the solution design (`/forge solution-design
   forge`). You should now see the item that names where the kind is
   realised.
8. Claude ends by naming what was born and what stays open, offers
   `/check engine` and proposes the first `/forge <name>` on a
   project.

### When the kind needs a trial first

Some kinds need a trial on real work before their position can hold.
Then the order changes:

1. the brief;
2. the pair, definition and template, with its reviewers;
3. the trial;
4. the position and the item of the solution design.

Until then the brief is the authority.

### What needs no change

The rosters need nothing. `/forge`, `/man` and the README read the
definitions from disk, so the new kind appears in them as soon as its
definition exists.

## Prove it

```
/check engine
```

Claude offers this check once the kind stands and never runs it on its
own judgement. The proof of the definition itself is the first
artefact of the kind made on real work:

```
/forge <name>
```

That first run is the trial. Whether the definition holds is told
there and not by `/new-artefact`.

## Record and release

The addition is recorded and released as any change of the forge,
with its history, a save and a release; the way is in
[Make a change to the forge](how-a-change-is-made.md). The layers the
forge's owner intends to add next are in
[Where the forge is going](../about/where-it-is-going.md).

## A worked example

A placeholder kind, `<name>`, added without a trial first.

1. You run `/new-artefact <name>`. No definition of that name exists,
   so the command goes on.
2. You hand over three sentences of what the kind is for. Claude
   proposes a position and lists what it assumed and chose.
3. You accept. The position is written in the forge intent.
4. Claude writes `.claude/skills/forge/states/<name>.md` from the
   skeleton and `templates/<name>.md`. You should now see both files.
5. The items of the kind need a prefix no existing one covers. You
   accept a new row in the ID scheme.
6. You decide that no persona is needed. The solution design gets its
   item.
7. Claude names what was born, offers `/check engine` and proposes
   `/forge <name>` on a project. You run the check, then the first
   artefact of the kind.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [Elicitation](../about/elicitation.md): the seven blocks and the Map.
- [Where the forge is going](../about/where-it-is-going.md): the layers the forge's owner intends to add.
- [Add a challenger persona](add-a-challenger-persona.md): the persona a kind may need.
- [Add a check](add-a-check.md): the check a kind may need.
- [Templates](../reference/templates.md): the skeletons a definition and a persona start from.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
