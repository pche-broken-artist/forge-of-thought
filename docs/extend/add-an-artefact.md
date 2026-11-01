---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: eb03b274347ba93a
inputs:
  - .claude/skills/new-artefact/SKILL.md
  - templates/artefact-definition.md
---

# Add an artefact

This page is for the extender who wants a new kind of artefact in the chain. The command `/new-artefact <name>` leads Claude through everything a kind needs: its place in the forge's intent, its definition, its template, its prefixes, its reviewers and its item in the solution design. It decides nothing: the principal (whoever's thinking is being forged) decides, and every file is born on the principal's word.

## Before you start

- A change to the forge is made, proved, recorded and released in one way. That way is described in [Make a change to the forge](how-a-change-is-made.md). The new kind is recorded and released as any change of the forge.
- Check that the kind does not exist. If `.claude/skills/forge/states/<name>.md` is there, the command stops, because a kind that exists is changed through the forge intent and not added.
- Decide how the kind is composed. There are three ways in:
  - A brief of the forge project holds the kind, and Claude mines it.
  - The principal gives a few sentences of what he wants, and Claude hands the kind back as a proposal.
  - Neither exists, and Claude walks the Map by interview.
- Know where the new kind meets an existing one: the layer above it and the layer below. The principal says this, and raises any overlap as a question.

A definition is the state file that says how an artefact is found. Its template is the skeleton of what comes out. The seven blocks of a definition and the Map are explained in [Elicitation](../about/elicitation.md).

## The files

The command leads to these, and to nothing else:

- `.claude/skills/forge/states/<name>.md`: the definition, in the seven blocks, started from `templates/artefact-definition.md`.
- `templates/<name>.md`: the template. It has no skeleton, because each template differs whole.
- A position in the forge intent: what the principal holds about the kind and why.
- The row of a new prefix in the ID scheme of `CLAUDE.md`, where the kind's items need one.
- The reviewers, where decided: a persona file and the calibration of the critic's contract.
- An item in the solution design of the forge: where the kind is realised.

The seven blocks of the skeleton are:

- Target: the file the kind produces and the template that gives its shape.
- Inputs: what the finding starts from.
- Aim: what is true of the artefact at the end, and when it is complete.
- Partner: what Claude does beyond the Aim, and what it does not.
- Map: what the artefact finds, whatever the order. An area may stay empty when it was considered and found not to apply.
- Instruments: the mechanisms of the forge the kind uses in a way of its own.
- Course: the ways in, and what is offered at the end.

Every block is present. A block empty on purpose says so, with the reason.

## Steps

1. Run `/new-artefact <name>`. Claude reads the forge intent with its threads, the solution design, the existing definitions and their templates, and the ID scheme and reviewer rules of `CLAUDE.md`.
2. Walk the Map with Claude. It covers:
   - what the artefact is and why it is wanted;
   - where it stands in the chain, with its number;
   - the boundary with the layer above and the layer below;
   - how it is found;
   - what comes out;
   - its items and prefixes;
   - its wording;
   - its reviewers;
   - how it reaches a reader;
   - where it is realised.

   Claude proposes and decides nothing. Research is proposed where the kind has a practice outside the forge and runs on the principal's word.
3. The position comes first. It is written through `/forge intent forge`, before anything is built.
4. The definition is born, then its template. Claude writes them from what was found. The definitions on disk are models of the shape, never of the content, so nothing is copied from them.
5. A new prefix gets its row in the ID scheme of `CLAUDE.md`. A kind that uses existing prefixes needs none.
6. The reviewers are decided. A persona file is made only where what it finds genuinely differs. See [Add a challenger persona](add-a-challenger-persona.md). A check that must know the kind is a separate addition: see [Add a check](add-a-check.md). The skeletons these start from are in [Templates](../reference/templates.md).
7. The item of the solution design is written through `/forge solution-design forge`.
8. Claude ends by naming what was born and what stays open, offers `/check engine`, and proposes the first `/forge <name>` on a project.

You should now see the definition and the template side by side, the position and the design item that stand around them, and a list of what stays open.

### When the kind needs a trial first

Some kinds cannot hold a position until they have been tried on real work. The order then changes:

1. The brief of the forge project.
2. The pair, the definition and its template, with its reviewers.
3. The trial on real work.
4. Then the position and the item of the solution design.

Until the trial is done, the brief is the authority for the kind.

The rosters need no edit. `/forge`, `/man` and the README read the definitions from disk, so the new kind appears in them once its definition exists.

## Prove it

```
/check engine
```

This checks the engine's files against the conventions. Claude offers it once the kind stands and never runs it on its own judgement.

The check does not tell whether the definition holds. That is told by the first artefact of the kind, made on real work:

```
/forge <name>
```

That first run is the trial. If it shows a gap, the kind is changed through the forge intent.

## Record and release

The addition is recorded in the history of each versioned document it touches, and released as any change of the forge. How is described in [Make a change to the forge](how-a-change-is-made.md). The layers the forge's owner intends to add are described in [Where the forge is going](../about/where-it-is-going.md). Terms of the forge are defined in the [Glossary](../reference/glossary.md).

## A worked example

A kind with the placeholder name `<name>` is added.

1. You type `/new-artefact <name>`. Claude finds no `.claude/skills/forge/states/<name>.md` and goes on.
2. You hand over three sentences about what the kind is for. Claude answers with a proposal, its assumptions and what each choice was chosen against.
3. You judge it. On your word Claude writes the position through the forge intent, then `.claude/skills/forge/states/<name>.md` and `templates/<name>.md`.
4. The kind needs one new prefix. Claude proposes its row in the ID scheme, and you accept it.
5. You decide that no persona is needed. Claude writes the item of the solution design.
6. Claude names what was born, lists what stays open, and offers `/check engine`.
7. You run `/check engine`, then `/forge <name>` on a real project. The first artefact is the trial.

You should now see that `/forge` lists the new kind among the states, read from its definition on disk.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving, recording and releasing the change.
- [Elicitation](../about/elicitation.md): the seven blocks and the Map.
- [Where the forge is going](../about/where-it-is-going.md): the layers the forge's owner intends to add.
- [Add a challenger persona](add-a-challenger-persona.md): the persona a kind may need.
- [Add a check](add-a-check.md): the check a kind may need.
- [Templates](../reference/templates.md): the skeletons a definition and a persona start from.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
