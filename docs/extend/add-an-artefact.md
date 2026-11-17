---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 13716c4fa4d67a06
inputs:
  - .claude/skills/new-artefact/SKILL.md
  - templates/artefact-definition.md
  - projects/forge/10-intent.md#POS.1980
---

# Add an artefact

This page shows how to add a new kind of artefact to the chain with
`/new-artefact`, for the extender who wants the forge to carry a
layer it does not have. The command leads you to everything a kind
needs and decides nothing: Claude proposes, and the principal (the
person whose thinking is being forged) decides.

## Before you start

- Read [Make a change to the forge](how-a-change-is-made.md). A new
  kind is recorded and released as any change of the forge is.
- Have the forge's own project cloned beside the engine. It is a
  repository of its own, and the command reads and writes it. Whoever
  develops the engine clones it; a user of the engine does not need
  it.
- Check that the kind does not exist yet. The command stops where
  `.claude/skills/forge/states/<name>.md` already exists, because a
  kind that exists is changed through the intent and is not added.
- Decide how the kind is composed. It is the principal's choice, and
  there are three ways in:
  - the principal has written a brief for the kind, and Claude mines
    it;
  - the principal gives a few sentences of what he wants, and Claude
    hands back a proposal for him to judge;
  - neither, and Claude walks the Map of the kind with him by
    interview.

## The files

What a kind consists of:

- A position in the forge intent, which says why the kind is wanted.
  It lives in the forge's own project.
- The definition, `.claude/skills/forge/states/<name>.md`, made from
  the skeleton `templates/artefact-definition.md`.
- The template of the kind, `templates/<name>.md`. It has no
  skeleton, because each template differs whole.
- Where the kind needs a new prefix, a row in the table of prefixes,
  `.claude/reference/id-prefixes.md`. See [ID scheme](../reference/id-scheme.md).
- The reviewers, where the principal decides them: a persona file and
  the calibration of the critic's contract.
- An item of the solution design, in the forge's own project, which
  names where the kind is realised.

The rosters need nothing. `/forge`, `/man` and the README read the
definitions from disk, so the new kind appears in them by itself.

The definition has seven blocks. Every block is present, and a block
left empty on purpose says so with its reason.

- Target: the file the kind produces and the template that shapes it.
- Inputs: what the finding starts from.
- Aim: what is true of the artefact at the end, and when it is
  complete.
- Partner: what Claude does beyond the Aim, and what it does not.
- Map: what the kind finds, whatever the order.
- Instruments: the mechanisms of the forge the kind uses in a way of
  its own.
- Course: how a run begins, the ways in, and what is offered at the
  end.

The blocks and the Map are explained in
[Elicitation](../about/elicitation.md). The skeletons are listed in
[Templates](../reference/templates.md).

## Steps

1. Type the command with the slug of the new kind.

   ```
   /new-artefact <name>
   ```

   You should now see Claude resolve the kind and stop if it exists,
   or name the way in it will take.

2. Walk the Map with Claude. The Map covers these areas, and an area
   may stay empty when it was considered and found not to apply:
   - what the artefact is and why it is wanted;
   - where it stands: what it is derived from, what stands above it,
     its number in the chain;
   - the boundary: what the layer above it cites or carries, what it
     must not hold, what a layer below takes from it;
   - how it is found: the seven blocks;
   - what comes out: the template, its sections and the shape of an
     item;
   - its items: the prefixes, existing or new, and where each lives;
   - its wording: any rule of style of its own;
   - its reviewers: whether it needs a challenger of its own, what the
     critic must know is no defect in it, whether a check must know
     it;
   - how it reaches a reader: whether a render or the README must show
     it;
   - where it is realised: the item of the solution design.

   You say where the new kind meets an existing one, the layer above
   and the layer below, and you raise an overlap as a question. You
   copy no definition. The definitions on disk are models of the shape
   and never of the content.

   You should now see the answers carried and reflected back, and
   nothing written yet. A file is born only on your word.

3. Let the files be born in this order, each on your word:
   1. the position in the forge intent, written through the intent's
      own definition before anything is built;
   2. the definition, then its template;
   3. the row of a new prefix in the table of prefixes;
   4. the reviewers, a persona file and the calibration of the
      critic's contract, where decided;
   5. the item of the solution design.

   You should now see each file named as it is born.

4. Where a persona is wanted, make it only if what it finds genuinely
   differs from the reviewers that exist. See
   [Add a challenger persona](add-a-challenger-persona.md). Where a
   check must know the kind, see [Add a check](add-a-check.md).

   You should now see the persona file in place, or a recorded
   decision that none is needed.

5. Let Claude close by naming what was born and what stays open.

   You should now see an offer of `/check engine` and a proposal for
   the first `/forge <name>` on a project.

### When the kind needs a trial first

Some kinds need a trial on real work before their position can hold.
Then the order changes:

1. the principal's brief for the kind;
2. the pair of definition and template, with its reviewers;
3. the trial;
4. the position in the intent and the item of the solution design.

Until the trial is done, the brief is the authority for the kind. The
reason the position waits is that it cannot hold before the trial
shows the definition holds.

## Prove it

Run the check of the engine. Claude offers it once the kind stands
and never runs it on its own judgement.

```
/check engine
```

The proof that the definition holds is the first artefact of the kind
made on real work. It is not this command's job.

```
/forge <name>
```

That first run is the trial. If it shows the definition wrong, the
kind is changed through the intent.

## Record and release

The addition is recorded and released as any change of the forge:
follow [Make a change to the forge](how-a-change-is-made.md) for
proving, recording and releasing. The definition and the template
carry a history beside them, and the new prefix is read from the
table of prefixes. The glossary has every term of the forge in one
line: [Glossary](../reference/glossary.md).

## A worked example

You want a kind named `<name>`.

1. You type `/new-artefact <name>`. No definition of that name exists,
   so Claude goes on.
2. You give a few sentences of what the kind is to hold. Claude works
   the Map alone from them and returns a proposal, with a short list
   of what it assumed and what it chose.
3. You judge the proposal and correct what is wrong. Claude writes
   once, on your word: the position in the intent, then
   `.claude/skills/forge/states/<name>.md`, then `templates/<name>.md`.
4. The kind needs the prefix `<PREFIX>`, so a row is added to
   `.claude/reference/id-prefixes.md`. You decide that no persona is
   needed.
5. The item of the solution design is written. Claude names what was
   born and what stays open, and offers `/check engine`.
6. You run `/check engine`, then `/forge <name>` on a real project.
   The first artefact of the kind is the trial.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Elicitation](../about/elicitation.md): the seven blocks and the
  Map.
- [Where the forge is going](../about/where-it-is-going.md): the
  layers the forge's owner intends to add.
- [Add a challenger persona](add-a-challenger-persona.md): the
  persona a kind may need.
- [Add a check](add-a-check.md): the check a kind may need.
- [ID scheme](../reference/id-scheme.md): the table of prefixes a new
  prefix gets its row in.
- [Templates](../reference/templates.md): the skeletons a definition
  and a persona start from.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
