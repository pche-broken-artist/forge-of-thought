---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 2c63ae8f69d0d22d
inputs:
  - .claude/skills/new-artefact/SKILL.md
  - templates/artefact-definition.md
---

# Add an artefact

This page shows how a new kind of artefact is added to the chain with `/new-artefact`, for the extender who wants the forge to carry a document it does not yet have. The command leads to everything a kind needs and decides nothing: Claude proposes, and the principal (the person whose thinking is being forged) decides.

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md), which says how a change is proved, recorded and released. The new kind is recorded and released as any change of the forge.

A kind that already has a definition is not added again. If `.claude/skills/forge/states/<name>.md` exists, the command stops: such a kind is changed through the intent of the forge's own project, not added.

Decide how the kind is composed. There are three ways in:

- A brief of the forge's own project already holds the kind, and Claude mines it.
- You give a few sentences of what you want, and Claude works the kind alone from them and hands back a proposal.
- Neither exists, and Claude walks the Map by interview (see [Elicitation](../about/elicitation.md)).

Also know where the new kind meets an existing one: the layer above it and the layer below. Say so to Claude, and raise any overlap as a question. Do not copy an existing definition. The definitions on disk are models of the shape, never of the content.

## The files

The command leads to these files and records:

- A position in the intent of the forge's own project, `projects/forge`. It states that the kind is wanted and why.
- The definition `.claude/skills/forge/states/<name>.md`, made from the skeleton `templates/artefact-definition.md`.
- The template `templates/<name>.md`. It has no skeleton: each template differs whole.
- A row for any new prefix in the ID scheme of `CLAUDE.md`.
- The reviewers, where decided: a persona file, and the calibration of the critic's contract.
- An item of the solution design of the forge's own project, which names where the kind is realised.

The rosters need no edit. `/forge`, `/man` and the README read the definitions from disk, so a new definition appears in them by itself.

## What you do

Type one line, with the name of the new kind in place of `<name>`:

```
/new-artefact <name>
```

## What happens

Every file is born on your word, one step at a time. Claude finds the following, in any order. An area may stay empty when it was considered and found not to apply.

- What the artefact is and why it is wanted: for whom, what it holds that no other artefact holds, and when a project takes it and when it does not.
- Where it stands: what it is derived from, what stands above it, and its number in the chain.
- The boundary: what the layer above it cites or carries, what it must not hold, and what a layer below takes from it.
- How it is found: the seven blocks of its definition, its Map above all.
- What comes out: its template, with the sections and the shape of an item.
- Its items: the prefixes, existing or new, and where each lives.
- Its wording: any rule of style of its own.
- Its reviewers: whether it needs a challenger of its own and what that one hunts, what the critic must know is no defect in it, and whether a check must know it.
- How it reaches a reader: whether a render or the README must show it.
- Where it is realised: the item of the solution design.

The order in which things are born is fixed:

1. The position in the intent is written first, through `/forge intent forge`, before anything is built. You should now see the kind named and reasoned in the intent.
2. The definition is written, then its template. You should now see the file `.claude/skills/forge/states/<name>.md` and the file `templates/<name>.md`.
3. The row of a new prefix is added to the ID scheme in `CLAUDE.md`, where the kind needs one. You should now see the prefix in the table.
4. The reviewers are decided and written where you decide them. A persona starts from the skeleton described in [Add a challenger persona](add-a-challenger-persona.md), and only where what it finds genuinely differs from the existing ones. You should now see a persona file, or a note that none is needed.
5. The item of the solution design is written through `/forge solution-design forge`. You should now see the item naming where the kind is realised.

### The seven blocks of the definition

The skeleton `templates/artefact-definition.md` has seven blocks. Every block is present. A block left empty on purpose says so, with the reason.

- Target: the file of the artefact and the template that gives the shape of the result.
- Inputs: what the finding starts from.
- Aim: what is true of the artefact at the end, and when it is complete.
- Partner: what Claude does beyond the Aim, and what it does not.
- Map: what the artefact finds, in the artefact's own words. A Map is a list of areas, each of which may stay empty (see [Elicitation](../about/elicitation.md)).
- Instruments: the mechanisms of the forge this artefact uses in a way of its own.
- Course: the ways in, what ends a session, and what is offered at completion as a recommendation, never a gate.

The skeleton closes with a paragraph on how the files are made: the first artefact is created from its template as version 0.1, with its history companion and its row in the ledger's Documents table. The skeleton's comments are deleted when the definition is written. Beside the skeleton, [Templates](../reference/templates.md) lists the other skeletons.

## What you have afterwards

The forge has a kind of artefact that a project can take through `/forge <name>`:

- wanted and reasoned in the intent
- defined in the seven blocks, with a template as its pair
- its items named by prefixes
- its reviewers decided
- its realisation named in the solution design

The definition is complete when every area of the Map has been found or knowingly left.

Claude ends by naming what was born and what stays open. It then offers `/check engine` and proposes a first `/forge <name>` on a project.

## Prove it

Run the check of the engine. Claude offers it once the kind stands and never runs it on its own judgement.

```
/check engine
```

You should now see no finding about the new files. This check tests conformance with the conventions, not whether the definition is good.

Whether the definition holds is told by the first artefact of the kind made on real work. That run is the trial:

```
/forge <name> <project-slug>
```

It belongs to `/forge <name>`, not to `/new-artefact`. A definition that fails the trial is changed through the intent.

## Record and release

The addition is recorded and released as any other change of the forge. [Make a change to the forge](how-a-change-is-made.md) gives the steps. The layers the forge's owner intends to add next are described in [Where the forge is going](../about/where-it-is-going.md).

## A worked example

You want a kind called `<name>`. You type:

```
/new-artefact <name>
```

1. Claude checks that `.claude/skills/forge/states/<name>.md` does not exist. It does not, so the work goes on.
2. You hand over three sentences of what you want. Claude works the kind from them and returns a proposal with a short list of what it assumed and what it chose.
3. You say where the kind sits: below the intent, above the layer that takes from it. Claude raises one overlap with an existing kind as a question, and you answer.
4. On your word, Claude writes the position in the intent. You should now see the kind reasoned there.
5. On your word, Claude writes `.claude/skills/forge/states/<name>.md` and `templates/<name>.md`. You decide that the kind needs a new prefix and no persona of its own. Claude adds the prefix row to `CLAUDE.md` and writes the item of the solution design.
6. Claude names what was born, names what stays open, and offers `/check engine`. You accept and run it.
7. You take the first `/forge <name> <project-slug>` on a real project. The result of that run tells you whether the definition holds.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [Elicitation](../about/elicitation.md): the seven blocks and the Map.
- [Where the forge is going](../about/where-it-is-going.md): the layers the forge's owner intends to add.
- [Add a challenger persona](add-a-challenger-persona.md): the persona a kind may need.
- [Templates](../reference/templates.md): the skeletons a definition and a persona start from.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
