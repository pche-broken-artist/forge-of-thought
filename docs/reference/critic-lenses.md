---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 3e483759a670e81f
inputs:
  - .claude/agents/critic-clarity.md
  - .claude/agents/critic-essence.md
---

# Critic lenses

This page lists the critic lenses of the forge and says what each one reads and goes after. A lens is one way the critic, an isolated subagent (a helper that never sees the working conversation), reviews the quality of the documents of a project. It is for the principal (the person whose thinking is forged) who picks a lens, and for the extender who writes a new one. Terms of the forge are one line each in the [Glossary](glossary.md).

## Overview

| Name | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `clarity` | Reads each artefact on its own for ambiguity, contradiction, duplication, scope hygiene and Requirement style. | Before a handover. | `.claude/agents/critic-clarity.md` |
| `essence` | Reads the chain for drift: distils each layer's essence blind and compares it with the layer above. | As soon as a second layer exists. | `.claude/agents/critic-essence.md` |

Both lenses review the quality of the documents. Neither challenges the thinking.

## clarity

Description: Critic lens "clarity" - reads each artefact on its own for ambiguity, contradiction, duplication, scope hygiene and Requirement style. Fit before a handover. Reviews the quality of the documents. Not a challenger of the thinking.

Lens:

The lens reads each artefact of the chain on its own, as its recipients will:

- a brief as the principal's text
- the intent as the record of current intent
- the assignment as the one document handed over
- the solution design as the description of the solution as it stands

While reading one artefact it has no memory of the others. Whether the layers agree with each other is the job of the `essence` lens.

Target: that artefact alone. Without one, every artefact of the chain.

What it goes after:

- Ambiguity: a sentence that two competent readers would act on differently, or an undefined or inconsistently used term.
- Internal contradiction: two items or passages of the same artefact that cannot both hold.
- Duplication: the same idea written twice, in one item or across items, or two items that differ only in wording.
- Scope hygiene: content that belongs to another artefact, judged by the Aim of the artefact's own definition (`.claude/skills/forge/states/<artefact>.md`). The finding names the artefact the passage belongs to and proposes the move in full.
- Requirement style: every breach of the rule set in the assignment's definition (`.claude/skills/forge/states/assignment.md`) is a finding, testability excepted.
- Self-containment: a section the artefact's own template requires and the document lacks without a stated reason.

Categories: `ambiguity`, `contradiction`, `duplication`, `scope-creep`, `style`, `gap`. A gap here is a hole within the artefact, such as a promised section that is missing or an item that refers to a group that does not exist. It is never substance missing from the layer above, which belongs to `essence`.

## essence

Description: Critic lens "essence" - reads the chain for drift: distils each layer's essence blind and compares it with the layer above. Fit as soon as a second layer exists. Reviews the quality of the documents. Not a challenger of the thinking.

Lens:

The lens reads the chain as a whole and measures whether each layer kept the essence of the one above it: the briefs to the intent, the intent to the assignment, and every later layer against its parent. Wording, style and the internal quality of a single artefact belong to the `clarity` lens.

Target: that artefact against its parent, one pair. Without one, every adjacent pair of the chain.

Method, for every adjacent pair from the top of the chain:

1. Distil the downstream artefact blind. Read it alone, before opening its parent, and write its essence in a few sentences: what it wants, why, what it rules out, what it delegates or leaves open.
2. Distil the upstream artefact the same way. A brief is read verbatim in whatever language it was written, and its essence is written in English.
3. Compare the two essences in both directions, and look for the trace of every difference: a REJ or DEC for something dropped, a DEL or TBC for something delegated, the ledger's Briefs table (mining state and note) for what of a brief is still pending.

A finding is a difference of essences, never a difference of texts. That the intent does not repeat a sentence of the brief is nothing. That the intent no longer wants what the brief wanted, without a trace, is a finding. Where the chain has no brief, or no assignment yet, the report says so in its Distillations and reviews the pairs that exist. A placeholder brief is not a defect.

What it goes after:

- Lost: substance of the upstream artefact absent downstream, with no REJ, DEC, DEL, TBC or mining note accounting for it.
- Added: substance downstream that the upstream does not carry and that names no provenance, such as a position citing a brief that does not say it, an assignment item with no position behind it, or a meeting's view promoted silently to the principal's own.
- Shifted: the same words with a different aim, such as an objective that narrowed or widened, a boundary that moved, or an emphasis inverted.
- Provenance that does not hold: a citation of a brief, a source or a DEC that, read at its target, does not support the claim.

Categories: `lost`, `added`, `shifted`, `provenance`.

Own report section, after Recommendations:

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

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
