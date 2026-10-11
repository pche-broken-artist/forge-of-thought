---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 4f0094e0ce87b510
inputs:
  - .claude/skills/new-artefact/SKILL.md
  - templates/artefact-definition.md
---

# Add an artefact

This page says how a new kind of artefact is added to the chain with
`/new-artefact`, for someone who extends the forge. The command leads
to everything a kind needs and decides nothing: the principal (the
person whose thinking is forged) decides, and Claude proposes.

## Before you start

Read [Make a change to the forge](how-a-change-is-made.md), which
says how a change is proved, recorded and released. An added kind is
recorded and released as any change of the forge.

Check that the kind does not exist yet. If
`.claude/skills/forge/states/<name>.md` is there, the command stops:
an existing kind is changed through the forge intent, never added.

Decide how the kind is composed. There are three ways in:

- A brief of the forge's own project already holds the kind, and the
  command mines it.
- You give a few sentences of what you want, and the kind is handed
  over: Claude works it alone and returns a proposal.
- Neither exists, and the command walks the Map by interview.

You say where the new kind meets an existing one, the layer above it
and the layer below, and you raise an overlap as a question. You copy
no existing definition: the definitions on disk are models of the
shape, never of the content.

## The files

A kind is a pair of files, and what stands around them in the forge's
own project and in the engine.

| What | Where | Made from |
|---|---|---|
| The position of the intent | the forge intent of the forge's own project | written through `/forge intent forge` |
| The definition | `.claude/skills/forge/states/<name>.md` | `templates/artefact-definition.md` |
| The template | `templates/<name>.md` | no skeleton: each template differs whole |
| The row of a new prefix | the ID scheme in `CLAUDE.md` | only where the kind has items of a prefix that does not exist |
| The reviewers | a persona file, and the calibration of the critic's contract | only where decided |
| The item of the solution design | the solution design of the forge's own project | written through `/forge solution-design forge` |

The definition has seven blocks, all present: Target, Inputs, Aim,
Partner, Map, Instruments and Course. A block left empty on purpose
says so, with the reason. [Elicitation](../about/elicitation.md)
says what each block holds and what a Map is. The skeleton also ends
with the way the files of the first artefact are made: from the
template as version 0.1, with its history companion and its row in
the ledger (the single source of truth for state).

## Steps

Every file is born on the principal's word, one step at a time.

1. State what the artefact is and why it is wanted. Say for whom,
   what it holds that no other artefact holds, and when a project
   takes it and when it does not.
2. Place it in the chain. Say what it is derived from, what stands
   above it and its number.
3. Draw the boundary. Say what the layer above carries or cites, what
   the artefact must not hold, and what a layer below takes from it.
4. Write the position in the forge intent with `/forge intent forge`,
   before anything is built.
5. Write the definition, then its template. The Map of the definition
   holds what is found: how the kind is found, what comes out, its
   items, its own rules of wording, its reviewers, how it reaches a
   reader, and where it is realised. An area may stay empty when it
   was considered and found not to apply.
6. Add the row of a new prefix to the ID scheme in `CLAUDE.md`, if the
   kind needs one.
7. Decide the reviewers. A challenger persona is added only where
   what it finds genuinely differs; see
   [Add a challenger persona](add-a-challenger-persona.md). Add the
   calibration of the critic's contract where the critic must know
   something is no defect in the kind. Say whether a check must know
   the kind.
8. Write the item of the solution design with
   `/forge solution-design forge`.

The rosters need nothing. `/forge`, `/man` and the README read the
definitions from disk, so the new kind appears in them by itself.

The skeletons a definition and a persona start from are listed in
[Templates](../reference/templates.md).

## Prove it

Run the check of the engine:

```
/check engine
```

The command offers it at the end and never runs it on its own. The
kind itself is tried by its first artefact on real work, through
`/forge <name>`. That is the trial, and it belongs to `/forge`, not
to `/new-artefact`.

## Record and release

The addition is recorded and released as any change of the forge. The
steps are on [Make a change to the forge](how-a-change-is-made.md).

## A worked example

You want a kind called `<name>`. You type:

```
/new-artefact <name>
```

Claude finds no `.claude/skills/forge/states/<name>.md`, so it goes
on. It asks how you want to compose the kind. You hand it over with
two sentences. Claude proposes the position for the intent and, on
your word, writes it. It then drafts the definition from the
skeleton and the template `templates/<name>.md`, each on your word.
It asks whether the items need a new prefix, and you say they do; the
row is added. You decide that no persona is needed and that the
critic needs one calibration. Claude writes the item of the solution
design. It ends by naming what was born and what stays open, offers
`/check engine`, and proposes the first `/forge <name>` on a project.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [Elicitation](../about/elicitation.md): the seven blocks and the Map.
- [Where the forge is going](../about/where-it-is-going.md): the layers the forge's owner intends to add.
- [Add a challenger persona](add-a-challenger-persona.md): the persona a kind may need.
- [Templates](../reference/templates.md): the skeletons a definition and a persona start from.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
