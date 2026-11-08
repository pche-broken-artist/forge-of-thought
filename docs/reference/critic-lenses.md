---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 39cd60a8d1616882
inputs:
  - .claude/agents/critic-clarity.md
  - .claude/agents/critic-essence.md
---

# Critic lenses

This page lists the critic lenses of the forge, the reviewers of the quality of the documents, and says what each one reads and goes after. It is for a reader who wants to pick a lens and for one who wants to see what a lens covers before adding another. Terms of the forge are in the [Glossary](glossary.md).

A critic lens reviews the quality of the documents, never the substance of the thinking. Each lens is one agent file in `.claude/agents/`. A lens is run on the chain, or on one artefact of it (a document of the chain, such as a brief or an intent). How to run one is in [Critique the documents](../use/critique-the-documents.md). How to add one is in [Add a critic lens](../extend/add-a-critic-lens.md).

## Overview

| Name | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `clarity` | Reads each artefact on its own for ambiguity, contradiction, duplication, scope hygiene and requirement style | Before a handover | `.claude/agents/critic-clarity.md` |
| `essence` | Reads the chain for drift: distils each layer's essence blind and compares it with the layer above | As soon as a second layer exists | `.claude/agents/critic-essence.md` |

## clarity

**Description.** Critic lens "clarity" - reads each artefact on its own for ambiguity, contradiction, duplication, scope hygiene and Requirement style. Fit before a handover. Reviews the quality of the documents. Not a challenger of the thinking.

**Lens.** It reads each artefact of the chain on its own, as its recipients will: a brief as the principal's text, the intent as the record of current intent, the assignment as the one document handed over, the solution design as the description of the solution as it stands. While reading one artefact it has no memory of the others. Whether the layers agree with each other is the work of the `essence` lens. (The principal is whoever's thinking is being forged.)

**Target.** That artefact alone; without one, every artefact of the chain.

**What it goes after:**

- Ambiguity: a sentence that two competent readers would act on differently; an undefined or inconsistently used term.
- Internal contradiction: two items or passages of the same artefact that cannot both hold.
- Duplication: the same idea written twice, in one item or across items; two items that differ only in wording.
- Scope hygiene: content that belongs to another artefact, judged by the Aim of the artefact's own definition (`.claude/skills/forge/states/<artefact>.md`). The finding names the artefact the passage belongs to and proposes the move in full.
- Requirement style: the rule set is the Requirement style section of the assignment's definition (`.claude/skills/forge/states/assignment.md`). Every breach is a finding, testability excepted. Where the artefact's own definition carries a style section of its own (the BRD's Requirement style, the user stories' Story style), that section is the rule set for that artefact instead.
- Self-containment: a section the artefact's own template requires and the document lacks without a stated reason.

**Categories.** `ambiguity`, `contradiction`, `duplication`, `scope-creep`, `style`, `gap`. A gap here is a hole within the artefact (a promised section missing, an item referring to a group that does not exist), never substance missing from the layer above, which belongs to `essence`.

## essence

**Description.** Critic lens "essence" - reads the chain for drift: distils each layer's essence blind and compares it with the layer above. Fit as soon as a second layer exists. Reviews the quality of the documents. Not a challenger of the thinking.

**Lens.** It reads the chain as a whole and measures whether each layer kept the essence of the one above it: the briefs to the intent, the intent to the assignment, and every later layer against its parent. Wording, style and the internal quality of a single artefact are the work of the `clarity` lens.

**Target.** That artefact against its parent, one pair; without one, every adjacent pair of the chain.

**Method**, for every adjacent pair from the top of the chain:

1. Distil the downstream artefact blind. Read it alone, before opening its parent, and write its essence in a few sentences: what it wants, why, what it rules out, what it delegates or leaves open.
2. Distil the upstream artefact the same way. A brief is read verbatim in whatever language it was written; its essence is written in English.
3. Compare the two essences, in both directions, and look for the trace of every difference: a rejected direction or a decision for something dropped, a deliverable or an open question for something delegated, the mining record of the intent's history (the ledger's Briefs table reads it: mining state and note) for what of a brief is still pending.

A finding is a difference of essences, never a difference of texts. That the intent does not repeat a sentence of the brief is nothing. That the intent no longer wants what the brief wanted, without a trace, is a finding. Where the chain has no brief, or no assignment yet, the report says so in its Distillations and reviews the pairs that exist. A placeholder brief is not a defect.

**What it goes after:**

- Lost: substance of the upstream artefact absent downstream with no rejected direction, decision, deliverable, open question or mining note accounting for it.
- Added: substance downstream that the upstream does not carry and that names no provenance. Examples are a position citing a brief that does not say it, an assignment item with no position behind it, a meeting's view promoted silently to the principal's own.
- Shifted: the same words with a different aim. Examples are an objective that narrowed or widened, a boundary that moved, an emphasis inverted.
- Provenance that does not hold: a citation of a brief, a source or a decision that, read at its target, does not support the claim.

**Categories.** `lost`, `added`, `shifted`, `provenance`.

**Own report section**, after Recommendations, one subsection per artefact in the order distilled (each a few sentences, written before its parent was opened), then one subsection per pair with the comparison the findings rest on:

```markdown
## Distillations

### <artefact> vX.Y - essence
...

### <upstream> -> <downstream> - comparison
...
```

## See also

- [Critique the documents](../use/critique-the-documents.md): running a lens.
- [Add a critic lens](../extend/add-a-critic-lens.md): adding a lens.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
