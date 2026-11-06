---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 2903d58973205eba
inputs:
  - .claude/agents/critic-clarity.md
  - .claude/agents/critic-essence.md
---

# Critic lenses

This page lists the critic lenses of the forge, the ways a critic
reviews the quality of the documents of a project, and says what each
lens reads and goes after. It is for the reader who picks a lens to
run and for the extender who writes a new one. Terms of the forge are
in the [Glossary](glossary.md).

## The lenses

| Name | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `clarity` | Reads each artefact on its own for ambiguity, contradiction, duplication, scope hygiene and requirement style | Before a handover | `.claude/agents/critic-clarity.md` |
| `essence` | Reads the chain for drift: distils each layer's essence blind and compares it with the layer above | As soon as a second layer exists | `.claude/agents/critic-essence.md` |

Both lenses review the quality of the documents. Neither challenges
the thinking.

## clarity

**Description.** Reads each artefact on its own for ambiguity,
contradiction, duplication, scope hygiene and requirement style. Fit
before a handover. Reviews the quality of the documents. Not a
challenger of the thinking.

**What it reads.** Each artefact of the chain on its own, as its
recipients will:

- a brief, as the principal's text
- the intent, as the record of current intent
- the assignment, as the one document handed over
- the solution design, as the description of the solution as it stands

While reading one artefact the lens has no memory of the others.
Whether the layers agree with each other is the work of the `essence`
lens.

**Target.** One artefact alone. Without a target, every artefact of
the chain.

**What it goes after.**

- Ambiguity: a sentence that two competent readers would act on
  differently, or an undefined or inconsistently used term.
- Internal contradiction: two items or passages of the same artefact
  that cannot both hold.
- Duplication: the same idea written twice, in one item or across
  items, or two items that differ only in wording.
- Scope hygiene: content that belongs to another artefact, judged by
  the aim stated in that artefact's own definition. The finding names
  the artefact the passage belongs to and proposes the move in full.
- Requirement style: every breach of the rule set in the assignment's
  definition is a finding, except testability.
- Self-containment: a section that the artefact's own template
  requires and the document lacks without a stated reason.

**Categories.**

- `ambiguity`
- `contradiction`
- `duplication`
- `scope-creep`
- `style`
- `gap`

A gap is a hole within the artefact, such as a promised section that is
missing or an item that refers to a group that does not exist. It is
never substance missing from the layer above, which belongs to
`essence`.

## essence

**Description.** Reads the chain for drift: distils each layer's
essence blind and compares it with the layer above. Fit as soon as a
second layer exists. Reviews the quality of the documents. Not a
challenger of the thinking.

**What it reads.** The chain as a whole. It measures whether each
layer kept the essence of the one above it: the briefs against the
intent, the intent against the assignment, and every later layer
against its parent. Wording, style and the internal quality of a single
artefact belong to the `clarity` lens.

**Target.** One artefact against its parent, one pair. Without a
target, every adjacent pair of the chain.

**Method.** For every adjacent pair from the top of the chain:

1. Distil the downstream artefact blind. Read it alone, before opening
   its parent, and write its essence in a few sentences: what it
   wants, why, what it rules out, what it delegates or leaves open.
2. Distil the upstream artefact the same way. A brief is read verbatim
   in whatever language it was written, and its essence is written in
   English.
3. Compare the two essences in both directions. Look for the trace of
   every difference: a rejected direction or a decision for something
   dropped, a deliverable or an open question for something delegated,
   the mining record of the intent's history for what of a brief is
   still pending. The ledger's Briefs table shows that record as a
   mining state and a note.

A finding is a difference of essences, never a difference of texts.
That the intent does not repeat a sentence of the brief is nothing.
That the intent no longer wants what the brief wanted, without a
trace, is a finding. Where the chain has no brief, or no assignment
yet, the report says so in its Distillations and reviews the pairs that
exist. A placeholder brief is not a defect.

**What it goes after.**

- Lost: substance of the upstream artefact that is absent downstream
  with no rejected direction, decision, deliverable, open question or
  mining note accounting for it.
- Added: substance downstream that the upstream does not carry and that
  names no provenance. Examples are a position citing a brief that does
  not say it, an assignment item with no position behind it, and a
  meeting's view promoted silently to the principal's own.
- Shifted: the same words with a different aim, such as an objective
  that narrowed or widened, a boundary that moved, or an emphasis
  inverted.
- Provenance that does not hold: a citation of a brief, a source or a
  decision that, read at its target, does not support the claim.

**Categories.**

- `lost`
- `added`
- `shifted`
- `provenance`

**Own report section.** After Recommendations, a section named
Distillations. It holds one subsection per artefact in the order
distilled, each a few sentences long and written before its parent was
opened. Then it holds one subsection per pair with the comparison the
findings rest on. The subsections are headed as follows:

```markdown
## Distillations

### <artefact> vX.Y — essence
…

### <upstream> → <downstream> — comparison
…
```

## See also

- [Critique the documents](../use/critique-the-documents.md): running a lens.
- [Add a critic lens](../extend/add-a-critic-lens.md): adding a lens.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
