---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: aa969cde4ac32857
inputs:
  - .claude/agents/critic-clarity.md
  - .claude/agents/critic-essence.md
  - .claude/skills/critique/SKILL.md
---

# Critic lenses

The critic lenses are the ways the forge reviews the quality of the documents of a project, each defined by what it reads and goes after. This page lists the lenses of today for the user and the extender. A lens reviews documents, never the thinking in them. An artefact is a document of the chain, and the chain is the sequence of versioned documents from the brief onward. For the terms of the forge, see the [Glossary](glossary.md).

The roster is the scan of the files `.claude/agents/critic-*.md`. The fit of each lens is the one its own description states.

## The lenses at a glance

| Name | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `clarity` | Reads each artefact on its own for ambiguity, contradiction, duplication, scope hygiene and requirement style. | Before a handover. | `.claude/agents/critic-clarity.md` |
| `essence` | Reads the chain for drift: distils each layer's essence blind and compares it with the layer above. | As soon as a second layer exists. | `.claude/agents/critic-essence.md` |

## clarity

Description: Critic lens "clarity" - reads each artefact on its own for ambiguity, contradiction, duplication, scope hygiene and Requirement style. Fit before a handover. Reviews the quality of the documents. Not a challenger of the thinking.

Lens:

The lens reads each artefact of the chain on its own, as its recipients will. A brief is read as the principal's text, the intent as the record of current intent, the assignment as the one document handed over, and the solution design as the description of the solution as it stands. The principal is the one whose thinking is forged. While the lens reads one artefact it has no memory of the others. Whether the layers agree with each other is the `essence` lens's work.

Target: that artefact alone. Without one, every artefact of the chain.

What it goes after:

- Ambiguity: a sentence that two competent readers would act on differently, or an undefined or inconsistently used term.
- Internal contradiction: two items or passages of the same artefact that cannot both hold.
- Duplication: the same idea written twice, in one item or across items, or two items that differ only in wording.
- Scope hygiene: content that belongs to another artefact, judged by the aim in that artefact's own definition. The finding names the artefact the passage belongs to and proposes the move in full.
- Requirement style: the rule set is the one in the assignment's definition. Every breach is a finding, except testability. Where an artefact's own definition has a style section (the BRD's requirement style, the user stories' story style), that section is the rule set for that artefact instead.
- Self-containment: a section the artefact's own template requires and the document lacks without a stated reason.

Categories: `ambiguity`, `contradiction`, `duplication`, `scope-creep`, `style`, `gap`. A gap here is a hole within the artefact, such as a promised section missing or an item referring to a group that does not exist. It is never substance missing from the layer above, which belongs to `essence`.

## essence

Description: Critic lens "essence" - reads the chain for drift: distils each layer's essence blind and compares it with the layer above. Fit as soon as a second layer exists. Reviews the quality of the documents. Not a challenger of the thinking.

Lens:

The lens reads the chain as a whole and measures whether each layer kept the essence of the one above it: the briefs to the intent, the intent to the assignment, and every later layer against its parent. Wording, style and the internal quality of a single artefact belong to the `clarity` lens.

Target: that artefact against its parent, one pair. Without one, every adjacent pair of the chain.

Method, for every adjacent pair from the top of the chain:

1. Distil the downstream artefact blind. Read it alone, before opening its parent, and write its essence in a few sentences: what it wants, why, what it rules out, and what it delegates or leaves open.
2. Distil the upstream artefact the same way. A brief is read verbatim in whatever language it was written, and its essence is written in English.
3. Compare the two essences in both directions, and look for the trace of every difference. The traces are a rejected direction or a decision for something dropped, a deliverable or an open question for something delegated, and the mining record of the intent's history for what of a brief is still pending. The ledger's Briefs table shows the mining state and note.

A finding is a difference of essences, never a difference of texts. That the intent does not repeat a sentence of the brief is nothing. That the intent no longer wants what the brief wanted, without a trace, is a finding. Where the chain has no brief, or no assignment yet, the report says so in its distillations and reviews the pairs that exist. A placeholder brief is not a defect.

What it goes after:

- Lost: substance of the upstream artefact absent downstream, with no rejected direction, decision, deliverable, open question or mining note accounting for it.
- Added: substance downstream that the upstream does not carry and that names no provenance. Examples are a position citing a brief that does not say it, an assignment item with no position behind it, and a meeting's view promoted silently to the principal's own.
- Shifted: the same words with a different aim, such as an objective that narrowed or widened, a boundary that moved, or an emphasis inverted.
- Provenance that does not hold: a citation of a brief, a source or a decision that, read at its target, does not support the claim.

Categories: `lost`, `added`, `shifted`, `provenance`.

Own report section, after the recommendations:

```markdown
## Distillations
<!-- One subsection per artefact in the order distilled, each a few
sentences, written before its parent was opened. Then one subsection
per pair with the comparison the findings rest on. -->

### <artefact> vX.Y — essence
…

### <upstream> → <downstream> — comparison
…
```

## See also

- [Critique the documents](../use/critique-the-documents.md): running a lens.
- [Add a critic lens](../extend/add-a-critic-lens.md): adding a lens.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
