---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: cd405842dff561c5
inputs:
  - .claude/agents/critic-clarity.md
  - .claude/agents/critic-essence.md
---

# Critic lenses

This page lists the critic lenses of the forge, the ways a critic can read the documents of a project, and says for each what it reads and what it goes after. It is for the user who picks a lens and for the extender who wants to see the shape a lens takes. The terms of the forge are in the [Glossary](glossary.md).

A lens judges the quality of the documents, never the substance of the thinking. An artefact here is a document of the chain, such as a brief, the intent, the assignment or the solution design.

## Overview

| Name | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `clarity` | Reads each artefact on its own for ambiguity, contradiction, duplication, scope hygiene and requirement style. | Before a handover. | `.claude/agents/critic-clarity.md` |
| `essence` | Reads the chain for drift: distils each layer's essence blind and compares it with the layer above. | As soon as a second layer exists. | `.claude/agents/critic-essence.md` |

Running a lens is described in [Critique the documents](../use/critique-the-documents.md). Adding one is described in [Add a critic lens](../extend/add-a-critic-lens.md).

## clarity

**Description:** Critic lens "clarity" - reads each artefact on its own for ambiguity, contradiction, duplication, scope hygiene and Requirement style. Fit before a handover. Reviews the quality of the documents. Not a challenger of the thinking.

**What it reads:** each artefact of the chain on its own, as its recipients will: a brief as the principal's text, the intent as the record of current intent, the assignment as the one document handed over, the solution design as the description of the solution as it stands. While reading one artefact it has no memory of the others. Whether the layers agree with each other belongs to the `essence` lens.

**Target:** that artefact alone; without one, every artefact of the chain.

**What it goes after:**

- Ambiguity: a sentence that two competent readers would act on differently; an undefined or inconsistently used term.
- Internal contradiction: two items or passages of the same artefact that cannot both hold.
- Duplication: the same idea written twice, in one item or across items; two items that differ only in wording.
- Scope hygiene: content that belongs to another artefact, judged by the aim of the artefact's own definition (`.claude/skills/forge/states/<artefact>.md`). The finding names the artefact the passage belongs to and proposes the move in full.
- Requirement style: every breach of the rule set in the assignment's definition (`.claude/skills/forge/states/assignment.md`) is a finding, testability excepted.
- Self-containment: a section the artefact's own template requires and the document lacks without a stated reason.

**Categories:** `ambiguity` | `contradiction` | `duplication` | `scope-creep` | `style` | `gap`

A gap here is a hole within the artefact (a promised section missing, an item referring to a group that does not exist). Substance missing from the layer above is not a gap in this sense; it belongs to `essence`.

## essence

**Description:** Critic lens "essence" - reads the chain for drift: distils each layer's essence blind and compares it with the layer above. Fit as soon as a second layer exists. Reviews the quality of the documents. Not a challenger of the thinking.

**What it reads:** the chain as a whole. It measures whether each layer kept the essence of the one above it: the briefs against the intent, the intent against the assignment, and every later layer against its parent. Wording, style and the internal quality of a single artefact belong to the `clarity` lens.

**Target:** that artefact against its parent, one pair; without one, every adjacent pair of the chain.

**Method,** for every adjacent pair from the top of the chain:

1. Distil the downstream artefact blind. It reads the artefact alone, before opening its parent, and writes its essence in a few sentences: what it wants, why, what it rules out, what it delegates or leaves open.
2. Distil the upstream artefact the same way. A brief is read verbatim in whatever language it was written; its essence is written in English.
3. Compare the two essences in both directions and look for the trace of every difference: a rejected direction or a decision for something dropped, a deliverable or an open question for something delegated, the mining record in the intent's history for what of a brief is still pending.

A finding is a difference of essences, never a difference of texts. That the intent does not repeat a sentence of the brief is nothing. That the intent no longer wants what the brief wanted, without a trace, is a finding. Where the chain has no brief, or no assignment yet, the report says so and reviews the pairs that exist; a placeholder brief is not a defect.

**What it goes after:**

- Lost: substance of the upstream artefact absent downstream, with no rejected direction, decision, deliverable, open question or mining note accounting for it.
- Added: substance downstream that the upstream does not carry and that names no provenance, such as a position citing a brief that does not say it, an assignment item with no position behind it, or a meeting's view promoted silently to the principal's own.
- Shifted: the same words with a different aim, such as an objective that narrowed or widened, a boundary that moved, or an emphasis inverted.
- Provenance that does not hold: a citation of a brief, a source or a decision that, read at its target, does not support the claim.

**Categories:** `lost` | `added` | `shifted` | `provenance`

**Own report section,** after Recommendations: Distillations. It holds one subsection per artefact in the order distilled, each a few sentences written before its parent was opened (headed "<artefact> vX.Y - essence"), then one subsection per pair with the comparison the findings rest on (headed "<upstream> -> <downstream> - comparison").

## See also

- [Critique the documents](../use/critique-the-documents.md): running a lens.
- [Add a critic lens](../extend/add-a-critic-lens.md): adding a lens.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
