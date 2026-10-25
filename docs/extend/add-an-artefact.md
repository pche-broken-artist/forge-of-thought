---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: a4a9dbe0e4ea20ce
inputs:
  - .claude/skills/new-artefact/SKILL.md
  - templates/artefact-definition.md
---

# Add an artefact

This page is for an extender who wants a new kind of artefact in the chain. The command `/new-artefact <name>` leads Claude through everything a kind needs: it proposes and decides nothing, and every file is born on the word of the principal (the person whose thinking is forged).

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md) first: it says how a change is proved, recorded and released. The new kind is recorded and released as any change of the forge.

Check that the kind does not exist yet. If `.claude/skills/forge/states/<name>.md` is there, the command stops: a kind that exists is changed through the intent, not added.

Decide how the kind is composed. There are three ways in:

- A brief holds the kind, and it is mined.
- The principal gives a few sentences of what he wants, and the kind is handed over to Claude, which returns a proposal with its assumptions and choices.
- Neither exists, and Claude walks the Map by interview.

You are the one who says where the new kind meets an existing one, the layer above and the layer below. Claude raises an overlap as a question. No existing definition is copied: the definitions on disk are models of the shape, never of the content.

## The files

A new kind is a pair of files, and what stands around the pair in the forge's own project.

- `.claude/skills/forge/states/<name>.md`: the definition, made from `templates/artefact-definition.md`.
- `templates/<name>.md`: the template of the artefact. It has no skeleton, because each template differs whole.
- A position in the forge intent: why the kind is wanted.
- The row of a new prefix in the ID scheme of `CLAUDE.md`, where the kind has items with a prefix of their own.
- The reviewers, where decided: a persona file, and the calibration of the critic's contract.
- An item of the solution design: where the kind is realised.

The definition keeps seven blocks, all present. A block that is empty on purpose says so, with the reason.

- Target: the file `NN-<name>.md` and the template that shapes it.
- Inputs: what the finding starts from.
- Aim: what is true of the artefact at the end, and when it is complete.
- Partner: what Claude does beyond the Aim, and what it does not.
- Map: what the finding covers, whatever the order.
- Instruments: the mechanisms of the forge the artefact uses in a way of its own.
- Course: the ways in, and what is offered at the end.

The blocks and the Map are explained in [Elicitation](../about/elicitation.md). The skeletons are listed in [Templates](../reference/templates.md).

## Steps

1. Run `/new-artefact <name>`. Claude walks the Map. An area may stay empty when it was considered and found not to apply. The areas are these:
   - what the artefact is and why it is wanted;
   - where it stands in the chain;
   - its boundary against the layers above and below;
   - how it is found;
   - what comes out;
   - its items and their prefixes;
   - its wording;
   - its reviewers;
   - how it reaches a reader;
   - where it is realised.
2. Write the position in the intent first. Claude uses `/forge intent forge` for it, so the position is written through the intent's own definition before anything is built.
3. Write the definition, then its template. Where the kind has a practice outside the forge, Claude proposes `/research <topic>`, and it runs on your word.
4. Add the row of a new prefix to the ID scheme of `CLAUDE.md`, if the kind needs one.
5. Decide the reviewers. A challenger persona is added only where what it hunts genuinely differs; see [Add a challenger persona](add-a-challenger-persona.md). A check is added only where a check must know the kind; see [Add a check](add-a-check.md). The critic's contract is calibrated where you decide it.
6. Write the item of the solution design, through `/forge solution-design forge`.
7. Claude ends by naming what was born and what stays open, offers `/check engine`, and proposes the first `/forge <name>` on a project.

You should now see the definition and its template on disk, and the position and the item in the forge's own project.

The rosters need nothing. `/forge`, `/man` and the README read the definitions from disk, so the new kind appears in them without an edit.

### When the kind needs a trial first

Some kinds cannot hold a position until they have been tried on real work. For such a kind the order changes:

1. The brief first.
2. The pair of definition and template, with its reviewers.
3. The trial on real work.
4. Then the position and the item of the solution design.

Until then the brief is the authority.

## Prove it

```
python scripts/forge-check.py engine
```

This is the mechanical part of `/check engine`, which Claude offers once the kind stands and never runs on its own judgement. Run `/check engine` in the harness (the program that runs Claude and its commands) if you want the full check.

The real proof is the first artefact of the kind. Run `/forge <name>` on real work: whether the definition holds is told there, and that run is the trial. It belongs to `/forge <name>`, not to `/new-artefact`.

## Record and release

Save and release the addition as any change, as [Make a change to the forge](how-a-change-is-made.md) describes. The history of each versioned file records the change in the same step as the write. Which layers the forge's owner intends to add is told in [Where the forge is going](../about/where-it-is-going.md).

## A worked example

You want a kind called `<name>`, and you have a few sentences of what it should be.

1. You type `/new-artefact <name>`. Nothing exists at `.claude/skills/forge/states/<name>.md`, so the command goes on.
2. You hand the kind over with your sentences. Claude returns a proposal and a short list of what it assumed and what it chose, each choice with what it was chosen against.
3. You judge it. On your word the position is written in the intent, then the definition and `templates/<name>.md`, then the prefix row and the item of the design. Each file is born on its own step.
4. Claude names what is born and what stays open, and offers `/check engine`. You accept.
5. You run `/forge <name>` on a project with real work. The artefact it makes is the trial. If the definition does not hold, you change the kind through the intent.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [Elicitation](../about/elicitation.md): the seven blocks and the Map.
- [Where the forge is going](../about/where-it-is-going.md): the layers the forge's owner intends to add.
- [Add a challenger persona](add-a-challenger-persona.md): the persona a kind may need.
- [Add a check](add-a-check.md): the check a kind may need.
- [Templates](../reference/templates.md): the skeletons a definition and a persona start from.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
