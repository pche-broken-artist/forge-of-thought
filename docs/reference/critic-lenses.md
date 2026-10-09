---
generated: 2026-10-09
made: mirrored
inputs-hash: 80b3a30ae409059f
inputs:
  - .claude/agents/critic-clarity.md
  - .claude/agents/critic-essence.md
---

# Critic lenses

This page lists the critic lenses the forge has, one entry each: the lens name, its description and what its Lens section says. It is for the person who chooses a lens to run and for the one who extends the forge with a new lens.

## clarity

Agent file: `.claude/agents/critic-clarity.md`

**Description.** Critic lens "clarity" - reads each artefact on its own for ambiguity, contradiction, duplication, scope hygiene and Requirement style. Fit before a handover. Reviews the quality of the documents. Not a challenger of the thinking.

**What it reads.** Each artefact of the chain on its own, as its recipients will: a brief as the principal's text, the intent as the record of current intent, the assignment as the one document handed over, the solution design as the description of the solution as it stands. While reading one artefact it has no memory of the others. Whether the layers agree with each other is the `essence` lens's job.

**Target.** That artefact alone; without one, every artefact of the chain.

**What it goes after.**

- Ambiguity: a sentence that two competent readers would act on differently; an undefined or inconsistently used term.
- Internal contradiction: two items or passages of the same artefact that cannot both hold.
- Duplication: the same idea written twice, in one item or across items; two items that differ only in wording.
- Scope hygiene: content that belongs to another artefact, judged by the Aim of the artefact's own definition (`.claude/skills/forge/states/<artefact>.md`). Examples are an intent that solves, an assignment that solves or carries machinery of delivery, and a solution design that restates the layer above or copies what realises it. The finding names the artefact the passage belongs to and proposes the move in full.
- Requirement style: the rule set is the Requirement style section of the assignment's definition (`.claude/skills/forge/states/assignment.md`). Every breach is a finding, testability excepted.
- Self-containment: a section the artefact's own template requires and the document lacks without a stated reason.

**Categories.**

| Category | Meaning |
|---|---|
| `ambiguity` | as under ambiguity above |
| `contradiction` | as under internal contradiction above |
| `duplication` | as under duplication above |
| `scope-creep` | as under scope hygiene above |
| `style` | as under requirement style above |
| `gap` | a hole within the artefact: a promised section missing, an item referring to a group that does not exist; never substance missing from the layer above, which belongs to `essence` |

**Own report sections.** None.

## essence

Agent file: `.claude/agents/critic-essence.md`

**Description.** Critic lens "essence" - reads the chain for drift: distils each layer's essence blind and compares it with the layer above. Fit as soon as a second layer exists. Reviews the quality of the documents. Not a challenger of the thinking.

**What it reads.** The chain as a whole. It measures whether each layer kept the essence of the one above it: the briefs to the intent, the intent to the assignment, and every later layer against its parent. Wording, style and the internal quality of a single artefact are the `clarity` lens's job.

**Target.** That artefact against its parent, one pair; without one, every adjacent pair of the chain.

**Method.** For every adjacent pair from the top of the chain:

1. Distil the downstream artefact blind. Read it alone, before opening its parent, and write its essence in a few sentences: what it wants, why, what it rules out, what it delegates or leaves open.
2. Distil the upstream artefact the same way. A brief is read verbatim in whatever language it was written; its essence is written in English.
3. Compare the two essences in both directions, and look for the trace of every difference: a rejected direction or a decision for something dropped, a deliverable or an open question for something delegated, the ledger's Briefs table (mining state and note) for what of a brief is still pending.

A finding is a difference of essences, never a difference of texts. That the intent does not repeat a sentence of the brief is nothing; that the intent no longer wants what the brief wanted, without a trace, is a finding. Where the chain has no brief, or no assignment yet, the report says so in the Distillations and reviews the pairs that exist; a placeholder brief is not a defect.

**What it goes after.**

- Lost: substance of the upstream artefact absent downstream with no rejected direction, decision, deliverable, open question or mining note accounting for it.
- Added: substance downstream that the upstream does not carry and that names no provenance. Examples are a position citing a brief that does not say it, an assignment item with no position behind it, and a meeting's view promoted silently to the principal's own.
- Shifted: the same words with a different aim: an objective that narrowed or widened, a boundary that moved, an emphasis inverted.
- Provenance that does not hold: a citation of a brief, a source or a decision that, read at its target, does not support the claim.

**Categories.**

| Category | Meaning |
|---|---|
| `lost` | as under lost above |
| `added` | as under added above |
| `shifted` | as under shifted above |
| `provenance` | as under provenance that does not hold above |

**Own report section.** After Recommendations, a section named Distillations. It has one subsection per artefact in the order distilled, each a few sentences, written before its parent was opened, headed `<artefact> vX.Y - essence`. Then it has one subsection per pair with the comparison the findings rest on, headed `<upstream> -> <downstream> - comparison`.

## See also

- [Critique the documents](../use/critique-the-documents.md): running a lens.
