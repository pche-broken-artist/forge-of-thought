---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: a076b5a4441e9fc2
inputs:
  - .claude/agents/critic-clarity.md
  - .claude/agents/critic-essence.md
---

# Critic lenses

This page lists the critic lenses of the forge and says what each one reads and goes after. It is for the principal (the person whose thinking is forged) who picks a lens to run, and for the extender who wants to see the shape of a lens before adding one. A lens reviews the quality of the documents, never the thinking behind them.

## Overview

| Name | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `clarity` | Reads each artefact on its own for ambiguity, contradiction, duplication, scope hygiene and requirement style. | Before a handover. | `.claude/agents/critic-clarity.md` |
| `essence` | Reads the chain for drift: distils each layer's essence blind and compares it with the layer above. | As soon as a second layer exists. | `.claude/agents/critic-essence.md` |

## clarity

Description: Critic lens "clarity". It reads each artefact on its own for ambiguity, contradiction, duplication, scope hygiene and requirement style. It fits before a handover. It reviews the quality of the documents and is not a challenger of the thinking.

What it reads: each artefact of the chain on its own, as its recipients will. A brief is read as the principal's text, the intent as the record of current intent, the assignment as the one document handed over, the solution design as the description of the solution as it stands. While it reads one artefact it has no memory of the others. Whether the layers agree with each other is the job of the `essence` lens.

Target: that artefact alone. Without one, every artefact of the chain.

What it goes after:

- Ambiguity: a sentence that two competent readers would act on differently, or an undefined or inconsistently used term.
- Internal contradiction: two items or passages of the same artefact that cannot both hold.
- Duplication: the same idea written twice, in one item or across items, or two items that differ only in wording.
- Scope hygiene: content that belongs to another artefact, judged by the Aim of the artefact's own definition (`.claude/skills/forge/states/<artefact>.md`). The finding names the artefact the passage belongs to and proposes the move in full.
- Requirement style: the rule set is the Requirement style section of the assignment's definition (`.claude/skills/forge/states/assignment.md`). Every breach is a finding, testability excepted.
- Self-containment: a section that the artefact's own template requires and the document lacks without a stated reason.

Categories: `ambiguity`, `contradiction`, `duplication`, `scope-creep`, `style`, `gap`. A gap here is a hole within the artefact, such as a promised section that is missing or an item that refers to a group that does not exist. It is never substance missing from the layer above, which belongs to `essence`.

## essence

Description: Critic lens "essence". It reads the chain for drift: it distils each layer's essence blind and compares it with the layer above. It fits as soon as a second layer exists. It reviews the quality of the documents and is not a challenger of the thinking.

What it reads: the chain as a whole. It measures whether each layer kept the essence of the one above it: the briefs against the intent, the intent against the assignment, and every later layer against its parent. Wording, style and the internal quality of a single artefact are the job of the `clarity` lens.

Target: that artefact against its parent, one pair. Without one, every adjacent pair of the chain.

Method, for every adjacent pair from the top of the chain:

1. Distil the downstream artefact blind. Read it alone, before opening its parent, and write its essence in a few sentences: what it wants, why, what it rules out, what it delegates or leaves open.
2. Distil the upstream artefact the same way. A brief is read verbatim in whatever language it was written, and its essence is written in English.
3. Compare the two essences in both directions and look for the trace of every difference. The traces are a rejected direction (REJ) or a decision (DEC) for something dropped, a deliverable (DEL) or an open question (TBC) for something delegated, and the mining record of the intent's history for what of a brief is still pending. The ledger's Briefs table shows that record as a mining state and a note.

A finding is a difference of essences, never a difference of texts. That the intent does not repeat a sentence of the brief is nothing. That the intent no longer wants what the brief wanted, without a trace, is a finding. Where the chain has no brief, or no assignment yet, the report says so in its Distillations and reviews the pairs that exist. A placeholder brief is not a defect.

What it goes after:

- Lost: substance of the upstream artefact that is absent downstream, with no REJ, DEC, DEL, TBC or mining note accounting for it.
- Added: substance downstream that the upstream does not carry and that names no provenance. Examples are a position citing a brief that does not say it, an assignment item with no position behind it, and a meeting's view promoted silently to the principal's own.
- Shifted: the same words with a different aim, such as an objective that narrowed or widened, a boundary that moved, or an emphasis inverted.
- Provenance that does not hold: a citation of a brief, a source or a decision that, read at its target, does not support the claim.

Categories: `lost`, `added`, `shifted`, `provenance`.

Own report section, after Recommendations, named Distillations. It has one subsection per artefact in the order distilled, each a few sentences written before its parent was opened. Then it has one subsection per pair with the comparison the findings rest on.

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

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
