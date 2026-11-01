---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 5f479c16c7c05e97
inputs:
  - .claude/skills/new-artefact/SKILL.md
  - templates/artefact-definition.md
---

# Add an artefact

This page shows how a new kind of artefact is added to the chain with `/new-artefact <name>`. It is for the extender, who wants the forge to carry a layer or a document it does not have yet. The command leads to everything a kind needs and decides nothing: the principal (the person whose thinking is being forged) decides every file, and Claude proposes.

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md). It says how a change is proved, recorded and released. The addition is recorded and released as any change of the forge.

Check that the kind does not exist yet. If `.claude/skills/forge/states/<name>.md` is there, the command stops: a kind that exists is changed through the intent, not added.

Know where the new kind meets an existing one: the layer above it and the layer below. Raise any overlap as a question before anything is written. For the layers the forge's owner intends to add, see [Where the forge is going](../about/where-it-is-going.md).

Decide how the kind is composed. There are three ways in:

- A brief of the forge project already holds the kind. It is mined.
- You give a few sentences of what you want. The kind is handed over to Claude, which returns a proposal.
- Neither exists. The command walks the areas of the Map by interview, one question per message.

## The files

A kind of artefact is a pair of files, plus what stands around the pair in the forge's own project:

| File | What it is |
|---|---|
| `.claude/skills/forge/states/<name>.md` | the definition, from the skeleton `templates/artefact-definition.md` |
| `templates/<name>.md` | the template; it has no skeleton, because each template differs whole |
| a position of the forge intent | why the kind is wanted and what it is to achieve |
| an item of the solution design | where the kind is realised |
| a row in CLAUDE.md, ID scheme | only where the kind brings a new prefix |
| a challenger persona file | only where the principal decides the kind needs its own |
| a calibration of the critic's contract | only where decided: what the critic must know is no defect in the kind |

The skeletons are listed in [Templates](../reference/templates.md).

## Steps

The command finds the kind by a Map. Each area may stay empty when it was considered and found not to apply:

- what the artefact is and why it is wanted: for whom, what it holds that no other artefact holds, when a project takes it and when it does not
- where it stands: what it is derived from, what stands above it, its number in the chain
- the boundary: what of the layer above it cites or carries, what it must not hold, and what a layer below takes from it
- how it is found: the seven blocks of its definition, its Map above all
- what comes out: its template, the sections and the shape of an item
- its items: the prefixes, existing or new, and where each lives
- its wording: any rule of style of its own
- its reviewers: whether it needs a challenger of its own and what that one hunts, what the critic must know is no defect in it, whether a check must know it
- how it reaches a reader: whether a render or the README must show it
- where it is realised: the item of the solution design

The order in which the files are born:

1. The position in the intent, written through `/forge intent forge`, before anything is built. You should now see the position in the intent, with its reason.
2. The definition in the seven blocks of the skeleton (Target, Inputs, Aim, Partner, Map, Instruments, Course). Every block is present; a block empty on purpose says so with the reason. The blocks and the Map are explained in [Elicitation](../about/elicitation.md). You should now see `.claude/skills/forge/states/<name>.md` with no skeleton comments left.
3. The template `templates/<name>.md`. You should now see the file beside the other templates.
4. The row of a new prefix in CLAUDE.md, ID scheme, where the kind brings one. You should now see the prefix in the table.
5. The reviewers, where decided: a persona file ([Add a challenger persona](add-a-challenger-persona.md)), the calibration of the critic's contract, and a check that knows the kind ([Add a check](add-a-check.md)). You should now see the files you decided on, and no others.
6. The item of the solution design, written through `/forge solution-design forge`. You should now see the item naming how the kind is realised.

Every file is born on the principal's word, one step at a time. Research is proposed with `/research <topic>` where the kind has a practice outside the forge, and run only on the principal's word.

### When the kind needs a trial first

Some kinds cannot be reasoned in advance: they need a trial on real work before their position can hold. The order then changes:

1. The brief.
2. The pair (definition and template) with its reviewers.
3. The trial.
4. Then the position in the intent and the item of the solution design.

Until the trial is done, the brief is the authority.

### Rosters

The rosters need nothing. `/forge`, `/man` and the README read the definitions from disk, so the new kind appears in them without an edit.

## Prove it

Run the check of the engine:

```
/check engine
```

Claude offers it once the kind stands and never runs it on its own judgement. Whether the definition holds is told by the first artefact of the kind made on real work, through:

```
/forge <name>
```

That first run is the trial. The command ends by naming what was born and what stays open, and proposes this first run on a project.

## Record and release

The addition is recorded in the history of the files it changes and released as any change of the forge. The steps are in [Make a change to the forge](how-a-change-is-made.md).

## A worked example

You want a new kind `<name>`.

1. You type `/new-artefact <name>`. Claude finds no `.claude/skills/forge/states/<name>.md` and goes on.
2. You hand over a few sentences of what the kind is for. Claude returns a proposal with a short list of what it assumed and what it chose, each choice with what it was chosen against.
3. You judge the proposal. On your word the position is written in the intent, then the definition, then `templates/<name>.md`.
4. The kind needs one new prefix. Claude proposes the row, and on your word it is added to CLAUDE.md, ID scheme.
5. You decide the kind needs no challenger of its own. No persona file is born.
6. The item of the solution design is written.
7. Claude names what was born and what stays open, and offers `/check engine`.
8. You run it, then start `/forge <name>` on a real project. The first artefact made is the trial.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [Elicitation](../about/elicitation.md): the seven blocks and the Map.
- [Where the forge is going](../about/where-it-is-going.md): the layers the forge's owner intends to add.
- [Add a challenger persona](add-a-challenger-persona.md): the persona a kind may need.
- [Add a check](add-a-check.md): the check a kind may need.
- [Templates](../reference/templates.md): the skeletons a definition and a persona start from.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
