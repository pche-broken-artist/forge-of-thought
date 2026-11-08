---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: ff5f3f538a0ccfae
inputs:
  - .claude/skills/new-artefact/SKILL.md
  - templates/artefact-definition.md
---

# Add an artefact

A new kind of artefact is added to the chain with `/new-artefact
<name>`, and this page is for you, the extender, who wants to add
one. The command leads you to everything a kind needs and decides
nothing: the principal (the person whose thinking is forged) decides,
Claude proposes. The page says which files are born, in which order,
and how you prove the addition. The layers the forge's owner intends
to add are on [Where the forge is going](../about/where-it-is-going.md);
the words of the forge are in the [Glossary](../reference/glossary.md).

## Before you start

The addition is recorded and released as any change of the forge; the
chain is on [Make a change to the forge](how-a-change-is-made.md).

The command stops where the definition `.claude/skills/forge/states/<name>.md`
already exists. A kind that exists is changed through the forge
intent, not added.

Three ways in are open, and the principal chooses:

- a brief of the forge project holds the kind, and Claude mines it
- the principal gives a few sentences of what he wants, and Claude
  works the kind from them and returns a proposal
- neither exists, and Claude walks the Map by interview

Every file is born on the principal's word, one step at a time. The
principal says where the new kind meets an existing one, the layer
above it and the layer below, and raises an overlap as a question.
Nothing is copied from an existing definition: those on disk are
models of the shape, never of the content.

## The files

| File | What it is |
|---|---|
| the position in the forge intent | why the kind is wanted; written first, through the intent's own definition |
| `.claude/skills/forge/states/<name>.md` | the definition, from the skeleton `templates/artefact-definition.md` |
| `templates/<name>.md` | the template, the shape of what comes out; it has no skeleton, each template differs whole |
| a row of the ID scheme in `CLAUDE.md` | only where the kind brings a new prefix |
| a persona file | only where the kind needs a challenger of its own |
| the critic's contract | only where the critic must be told what is no defect in the kind |
| an item of the solution design | where the kind is realised |

The skeletons a definition and a persona start from are listed on
[Templates](../reference/templates.md).

## Steps

1. **Settle the position.** Claude writes the position of the kind
   into the forge intent through `/forge intent forge`, before
   anything is built.

2. **Write the definition.** It has seven blocks, and every block is
   present; a block empty on purpose says so with the reason.
   - Target: the file the kind produces and the template that shapes it
   - Inputs: what the finding starts from
   - Aim: what is true of the artefact at the end, and when it is complete
   - Partner: what Claude does beyond the Aim, and what it does not
   - Map: what is found, whatever the order
   - Instruments: the mechanisms of the forge the kind uses in a way of its own
   - Course: the ways in, and what is offered at the end

   The blocks and the Map are explained on
   [Elicitation](../about/elicitation.md). The Map of the new kind
   covers what the artefact is and why it is wanted, where it stands
   in the chain, its boundary with the layers above and below, how it
   is found, what comes out, its items and prefixes, its wording, its
   reviewers, how it reaches a reader, and where it is realised. An
   area may stay empty when it was considered and found not to apply.

3. **Write the template** `templates/<name>.md`: the sections and the
   shape of an item.

4. **Add the row of a new prefix** to the ID scheme of `CLAUDE.md`,
   where the kind needs a prefix that does not exist yet.

5. **Decide the reviewers.** A challenger of its own is added only
   where what it finds genuinely differs from the others; the way is
   [Add a challenger persona](add-a-challenger-persona.md). A check
   that must know the kind is added as
   [Add a check](add-a-check.md) says. Where the critic must know
   something is no defect in the kind, its contract is calibrated.

6. **Write the item of the solution design** that names how the kind
   is realised, through `/forge solution-design forge`.

Where the kind has a practice outside the forge, Claude proposes
`/research <topic>`, and it runs on the principal's word.

### When the kind needs a trial first

Some kinds cannot hold their position until they have met real work.
Then the order changes:

1. the brief
2. the pair, definition and template, with its reviewers
3. the trial on real work
4. the position in the intent and the item of the solution design

The brief is the authority until then.

### The rosters

The rosters need nothing. `/forge`, `/man` and the README read the
definitions from disk, so the new kind appears in them without an
entry of its own.

## Prove it

```
/check engine
```

Claude offers this check once the kind stands and never runs it on
its own judgement. The check verifies the core against itself and
against the intent.

The first artefact of the kind, made on real work, is the trial:

```
/forge <name>
```

Whether the definition holds is told by that run, and it belongs to
`/forge <name>`, not to `/new-artefact`. At its end `/new-artefact`
names what was born and what stays open, offers `/check engine` and
proposes the first `/forge <name>` on a project.

## Record and release

The addition is recorded and released as any change of the forge:
see [Make a change to the forge](how-a-change-is-made.md).

## A worked example

You add a kind `<name>`, a layer between two existing layers.

```
/new-artefact <name>
```

You tell Claude that `<name>` sits below the layer above it and
above the layer below. Claude walks the Map and proposes, one step at
a time; each file is born on your word:

1. the position of `<name>` in the forge intent
2. `.claude/skills/forge/states/<name>.md`, in the seven blocks
3. `templates/<name>.md`
4. the row of the prefix `<PREFIX>` in the ID scheme of `CLAUDE.md`
5. no persona, because what it would find is not different
6. the item of the solution design

Claude ends by naming what was born and what stays open, then offers
`/check engine`. You run it, and then you run `/forge <name>` on a
project; that first artefact is the trial. Then the change is
recorded and released.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Elicitation](../about/elicitation.md): the seven blocks and the Map.
- [Where the forge is going](../about/where-it-is-going.md): the
  layers the forge's owner intends to add.
- [Add a challenger persona](add-a-challenger-persona.md): the
  persona a kind may need.
- [Add a check](add-a-check.md): the check a kind may need.
- [Templates](../reference/templates.md): the skeletons a definition
  and a persona start from.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-08 for version 6.21 from the files the
front-matter names; never edited by hand.
