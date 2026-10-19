---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: aa673edbfae81955
inputs:
  - .claude/skills/new-artefact/SKILL.md
  - templates/artefact-definition.md
---

# Add an artefact

This page shows how a new kind of artefact is added to the chain with `/new-artefact`, for the extender who wants a project to be able to take one more layer. The command leads to everything a kind needs and decides nothing: Claude proposes, and the principal (the person whose thinking is being forged) decides.

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md). It describes how a change is proved, recorded and released. The addition is recorded and released as any change of the forge.

Check that the kind does not exist yet. The command stops where `.claude/skills/forge/states/<name>.md` already exists: a kind that exists is changed through the forge intent, not added.

Decide how the kind is composed. There are three ways in:

- A brief of the forge project already holds the kind, and Claude mines it.
- You give a few sentences of what you want, and Claude works the kind alone from them and hands back a proposal.
- Neither exists, and Claude walks the Map by interview (see [Elicitation](../about/elicitation.md)).

Every file is born on your word, one step at a time.

## The files

A kind of artefact is a pair of files, and some records around them:

- `.claude/skills/forge/states/<name>.md`: the definition of the kind. It starts from the skeleton `templates/artefact-definition.md`.
- `templates/<name>.md`: the template, the shape of what comes out. It has no skeleton, because each template differs whole.
- A position in the intent of the forge project, `projects/forge`, written first. It says that the kind is wanted and why.
- An item in the solution design of the same project, which names where the kind is realised.
- A row in the ID scheme of `CLAUDE.md`, only if the kind brings a new prefix.
- Optionally, a challenger persona file and a calibration of the critic's contract, where you decide the kind needs its own reviewers.

The rosters need no edit. `/forge`, `/man` and the README read the definitions from disk, so the new kind appears in them by existing.

## Steps

Run the command:

`/new-artefact <name>`

1. Claude reads the forge intent with its threads, the solution design, the existing definitions and their templates, and the ID scheme and reviewer rules of `CLAUDE.md`. You should now see Claude naming which of the three ways in applies.
2. The position comes first. Claude writes it through `/forge intent forge`, before anything is built. You should now see the new position in the intent of the forge project.
3. The definition follows, in the seven blocks the skeleton keeps. Every block is present; one left empty on purpose says so with the reason.
   - Target: the file the artefact lives in and the template that shapes it.
   - Inputs: what the finding starts from.
   - Aim: what is true of the artefact at the end, and when it is complete.
   - Partner: what Claude does beyond the Aim, and what it does not.
   - Map: the areas the finding covers, whatever the order; an area may stay empty when it was considered and found not to apply.
   - Instruments: the mechanisms of the forge the artefact uses in a way of its own.
   - Course: the ways in, and how a session ends.

   You should now see `.claude/skills/forge/states/<name>.md`.
4. The Map of the new kind covers these areas, as the command walks them:
   - what the artefact is and why it is wanted: for whom, what it holds that no other holds, when a project takes it and when it does not;
   - where it stands: what it derives from, what stands above it, its number in the chain;
   - the boundary: what the layer above cites or carries, what the artefact must not hold, what a layer below takes from it;
   - how it is found: the seven blocks themselves;
   - what comes out: the template, its sections and the shape of an item;
   - its items: the prefixes, existing or new, and where each lives;
   - its wording: any rule of style of its own;
   - its reviewers: whether it needs a challenger of its own and what that one hunts, what the critic must know is no defect in it, whether a check must know it;
   - how it reaches a reader: whether a render or the README must show it;
   - where it is realised: the item of the solution design.
5. The template is born next: `templates/<name>.md`. You should now see the sections and the item shape the definition promised.
6. If the kind brings a new prefix, Claude adds its row to the ID scheme in `CLAUDE.md`. You should now see the row there.
7. The reviewers are decided. A challenger persona is added only where what it finds genuinely differs from the existing ones; see [Add a challenger persona](add-a-challenger-persona.md). The skeletons a definition and a persona start from are listed in [Templates](../reference/templates.md).
8. The item of the solution design is written through `/forge solution-design forge`. You should now see it name where the kind is realised.
9. Claude ends by naming what was born and what stays open, offers `/check engine`, and proposes the first `/forge <name>` on a project.

## Prove it

Run the check on the engine. Claude offers it once the kind stands and never runs it on its own judgement:

`/check engine`

The check tells whether the new files conform to the conventions. It does not tell whether the definition works. That is told by the first artefact of the kind made on real work:

`/forge <name> <slug>`

That first run is the trial. If it shows a flaw, the kind is changed through the intent.

## Record and release

The addition is a change of the forge. It is recorded and released as any change; [Make a change to the forge](how-a-change-is-made.md) gives the way. The new files are versioned, and each versioned file keeps its history in a companion beside it.

## A worked example

You want a kind called `<name>`, and you have a few sentences of what it is for.

1. You type `/new-artefact <name>` and give the sentences. Claude checks that `.claude/skills/forge/states/<name>.md` does not exist and takes the handed-over way in.
2. Claude proposes a position for the intent and waits. You accept it, and it is written through `/forge intent forge`.
3. Claude proposes the definition and the template with a short list of what it assumed and what it chose against what. You modify one choice and accept the rest. The two files are born.
4. The items of the new kind need a prefix none of the existing kinds has, so Claude proposes a row for the ID scheme. You accept it.
5. You decide that no new persona is needed, because the existing reviewers cover what the kind holds. Claude notes the decision.
6. The solution design gets its item. Claude lists what was born and what stays open, and offers `/check engine`. You run it, and it reports no finding.
7. You start `/forge <name> <slug>` on a real project. That run is the trial of the definition.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [Elicitation](../about/elicitation.md): the seven blocks and the Map.
- [Where the forge is going](../about/where-it-is-going.md): the layers the forge's owner intends to add.
- [Add a challenger persona](add-a-challenger-persona.md): the persona a kind may need.
- [Templates](../reference/templates.md): the skeletons a definition and a persona start from.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
