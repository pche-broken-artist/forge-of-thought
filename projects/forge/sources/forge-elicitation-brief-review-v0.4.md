---
title: Second review of the elicitation brief
project: forge
reviewed_document: 00-brief-elicitation.md, version 0.4, 2026-09-28
previous_review: sources/forge-elicitation-brief-review.md
language: en
status: review
---

# Second review of the elicitation brief

## Purpose

This review assesses version 0.4 of `00-brief-elicitation.md` after the first review was worked into it. It is an incremental review, not a repetition of the first one. It identifies what version 0.4 resolved and what still deserves attention before the brief is mined into the intent.

## Overall assessment

Version 0.4 is materially stronger. It has incorporated most of the important criticism correctly:

- the scope of the decision is now explicit;
- the engine split and extension mechanism are consequences and later material rather than decisions of this brief;
- all three artefacts now have Aim, Partner, Map, Instruments and Course;
- the seven blocks have clearer ownership and completion belongs to Aim alone;
- the brief is no longer described as the whole pile produced by elicitation, but as the principal's choice from the finding;
- Map is explicitly a coverage map rather than a questionnaire or document structure;
- research has a named need and a stopping hand-back;
- assignment questions may be zero and the provenance map remains central;
- behavioural validation replaces line count as proof.

The brief is now suitable material for mining into the intent. The remaining issues do not invalidate the direction, but several of them affect the core semantics and should be decided consciously rather than inherited from the present wording.

# 1. What version 0.4 resolved well

## 1.1 The brief now distinguishes finding from the resulting brief

The strongest change is the distinction between:

- the broad finding process, which may include the principal's ideas, Claude's proposals, research, sources, alternatives and counter-examples; and
- the brief, which contains what the principal chooses from that finding.

This is more precise than both earlier extremes. A brief is neither the principal's untouched initial words nor a transcript-like pile of everything that happened during elicitation. It is a deliberately rough composition of the idea, selected by the principal and left with work for the intent to do.

The note that the current elicitation brief itself is an exception is also useful. It prevents this unusually long and worked-through document from becoming the accidental exemplar of the new brief definition.

## 1.2 Scope is now explicit

The document clearly states that it decides:

- the shape of an artefact definition;
- the definitions of brief, intent and assignment.

It also states that user-defined definitions, the engine split, installation and `/recipe` unification remain later material. This is sufficient to avoid the earlier conceptual coupling, provided mining respects the boundary.

## 1.3 The seven-block contract is substantially clearer

Version 0.4 resolves several ambiguities:

- Aim owns completion;
- Course only says what is offered when completion is reached;
- every definition carries every block;
- an intentionally empty block says so;
- Instruments lists only mechanisms used distinctively by the artefact;
- shared mechanics are cited rather than repeated.

This is a workable contract. It can now be evaluated through real definitions rather than only in the abstract.

## 1.4 The brief's Map is now a closing coverage pass

The Map is no longer presented as required brief content. It is a map of the finding and is walked once before lock. An area may leave nothing in the brief.

This is the correct defence against turning the Map into either a questionnaire or a template. It preserves free form while still requiring conscious coverage.

## 1.5 Research has a disciplined stopping rule

Research is proposed against a named uncertainty, comparison or inspiration need. After the step, Claude reports:

- what changed in the thought;
- what remains uncertain;
- whether more research is likely to change anything.

The principal then decides whether to continue. This gives research a useful place in elicitation without turning the brief into an open-ended survey.

## 1.6 The assignment definition is now operational

The assignment's three phases are now properly supported by its Map, Instruments and Course. Important improvements include:

- zero preliminary questions is explicitly valid;
- the questions concern only what the intent does not answer;
- the provenance map remains outside the assignment;
- changed intent can trigger a delta pass rather than requiring a complete recast every time;
- wording fixes remain downstream while substantive changes return to the intent.

The assignment definition is the most implementation-ready of the three.

# 2. Remaining material issues

## 2.1 The brief's Partner may now be too restrictive about who formulates the text

The definition says that after the active opening, the principal writes and Claude records his words, not a summary and not Claude's prose. Claude may translate and mend grammar, but may not restyle, tidy or add.

This protects the principal's authorship, but it risks reintroducing the original problem in a different form. During active elicitation Claude may produce a useful synthesis, architecture, analogy or formulation which the principal accepts as exactly what he means. Under the current wording, the idea may be accepted but the resulting brief still cannot carry Claude's well-formed text unless the principal effectively dictates it back.

The meaningful boundary should be ownership of substance, not authorship of sentences.

**Recommendation:** allow Claude to formulate accepted substance when the principal explicitly approves the meaning. For example:

> The brief carries the principal's chosen thought. The principal may write it himself or ask Claude to formulate what they have agreed. Claude never substitutes his wording or synthesis without the principal's explicit acceptance of the substance; where he formulates it, he reflects it back before the write.

This would preserve the principal as composer while allowing the active elicitation model to produce usable text.

## 2.2 “What he does not take is gone with the conversation” is too absolute

The rule is correct for incidental ideas. A brief should not become a log of everything considered. However, a significant alternative may need to remain visible when its rejection defines the chosen idea or prevents the same question from reopening immediately during intent work.

Research findings and sources already have durable homes, but a rejected proposal created in conversation may have none.

This does not justify a new record kind or a fate map for every idea. It does justify an exception under the principal's control.

**Recommendation:**

> What the principal does not take normally leaves no record. Where an alternative materially defines the chosen thought, he may keep a short note of it and why it was left behind; this remains exploratory material, not an intent rejection.

## 2.3 “What and why” versus “how exactly” is useful but too categorical

The Partner says that a brief says what and why; once the conversation turns to how exactly, Claude identifies it as intent work and does not develop it.

This is a good warning against doing the intent inside the brief, but the form of a mechanism can itself be part of the idea. In this very project, “one dispatcher with a definition and template pair” is partly a how, yet without it the thought would be materially different.

The boundary should depend on whether the mechanism is part of the idea or whether it is being elaborated into a settled specification.

**Recommended wording:**

> A brief may carry a concrete mechanism where that mechanism is part of the idea being proposed. It stops before the mechanism is systematically decomposed, normalised or agreed block by block; that chiselling belongs to the intent.

## 2.4 The Aim of intent still imposes a two-axis ceremony on every idea

The wording says every idea is weighed twice: good or bad, feasible or not.

Not every material idea needs both judgements. Some are framing observations, some are factual, some are mutually compatible, and some need a choice for reasons other than abstract value. “Good or bad” is also less precise than value in relation to the aim.

**Recommendation:** replace the universal two-pass rule with:

> Each material idea is judged for its value to the intent and for feasibility wherever either distinction matters.

The Map already contains weight and reality, so the process retains both concerns without manufacturing a verdict pair for every item.

## 2.5 Intent mining has lost an explicit whole-brief coverage check

It is correct to drop the requirement that every part of a brief receive an individually recorded fate. That would be heavy and would turn mining into bookkeeping.

The current definition, however, no longer states explicitly that the material substance of each brief must survive, be rejected or be knowingly left behind. `Mined` state alone does not prove semantic coverage.

A lighter whole-level control is enough.

**Recommendation:** add to the intent Map:

> the briefs as wholes: whether the material substance of each is represented, rejected or deliberately left behind.

This should not require paragraph-level traceability. It is an essence-level check before a brief is marked mined.

## 2.6 The definition of Map no longer fully matches the assignment Map

The common definition describes Map as what must be found. The assignment Map includes “the words: what must be defined so that the assignment is read without the principal in the room.” This is partly a property to verify in the resulting document rather than knowledge to discover.

The point belongs in the assignment, but its name and the common Map definition should align.

**Recommendation:** rename the item to **Self-containment**:

> self-containment: which terms, context and distinctions must be explicit for the recipients to act without the principal in the room.

Also broaden the common definition slightly:

> Map names what must be found or consciously verified for the artefact to be complete.

This accommodates both knowledge discovery and conscious coverage without turning Map into acceptance criteria.

## 2.7 The number of assignment questions should not decide whether intent is ready

The joint pass says questions are rarely more than six, and if more are needed the intent is not ready and work returns to it.

The number is a useful warning against an assignment interview becoming a second intent elicitation, but count is not the semantic boundary. Seven simple handover details may be less serious than one missing substantive decision.

**Recommended wording:**

> Questions are one per message and limited to what the intent does not answer. Where the missing answers amount to unresolved substance rather than handover detail, the work returns to the intent. A large question set is evidence of that problem, not its definition.

A normal soft ceiling may remain as guidance, but should not govern the state transition.

## 2.8 Later architectural material still creates mining noise

The scope disclaimer is now sufficient to prevent accidental decision in principle. In practice, the sections on user-defined mechanisms and the split still occupy a large part of the document and contain mature-sounding propositions.

A mining pass may still promote them unless they have a distinct declared status.

**Recommendation:** mark both later sections explicitly:

> Status: material for later briefs; not to be mined into the elicitation decision except for the dependency that self-contained definitions come first.

The content may stay because this brief is deliberately preserved as the record of the work. Its mining treatment should nevertheless be unambiguous.

## 2.9 The behavioural tests need an intentionally imperfect brief

Version 0.4 correctly says that a brief polished until the intent has nothing left to do has gone too far. The cited behavioural scenarios do not directly test that claim.

**Recommendation:** add this scenario:

> **Intentionally imperfect brief:** a brief contains a meaningful tension, an unresolved alternative and an imprecise boundary. It can still lock when the principal judges it ready for chiselling; the closing Map must not force those matters to be resolved prematurely.

This test is important because a conscientious implementation may otherwise use the Map to over-complete the brief.

## 2.10 The role of citations in a brief remains unresolved and should not remain implicit

The brief correctly rejects authorship marks and retains source paths and plain-language epistemic status. It then leaves open whether a brief born in the forge carries marks and citations at all.

The source path is not merely an authorship mark. It lets intent mining distinguish a principal's claim from a proposition grounded in external material and later preserve provenance in a fact.

**Recommendation:** decide that a material external claim retains a source citation when it enters the brief. Do not require citation on every inspiration or sentence. Use it where the later intent would otherwise lose the ground of the statement.

A useful rule would be:

> A source is cited in the brief where its identity materially supports, limits or contradicts the thought. Mere inspiration need not interrupt the prose when its source remains discoverable through the research note.

## 2.11 `(remark: …)` combines too many states

The proposed mark covers a reservation, uncertainty or suggestion not adopted by the principal. Those states do not behave alike:

- a reservation challenges material that remains;
- an uncertainty records lack of knowledge;
- an unadopted suggestion is normally omitted under the new brief model.

Putting all three under `remark` may preserve ambiguity rather than remove it.

**Recommendation:** keep `remark` only for something that must remain visible beside accepted material, such as a material reservation or unresolved uncertainty. An unadopted suggestion should normally disappear unless the principal chooses to preserve it as a significant alternative under section 2.2 above.

## 2.12 The definitions still repeat some shared mechanism

Version 0.4 greatly improves citation, but the brief Course still restates several shared actions: create companion and ledger row, write once per round, lock on the principal's word and end by naming the state. The common shape says these mechanisms live outside definitions.

Some repetition may be needed at the action point, but ownership should be consistent.

**Recommendation:** in the implementation state files, reduce Course to artefact-specific branching and transition. Keep shared write, versioning, ledger and end-state rules in their owner and cite them once. The longer wording may remain in this source brief as design material, but should not automatically become the final state files.

# 3. The central decision still required

The largest unresolved design choice is:

> May Claude formulate the text of a brief after the principal has accepted the substance, or must a forge-born brief consist almost entirely of the principal's own sentences?

Version 0.4 chooses the second model. That choice protects against Claude taking over the thought, but it weakens the active-partner model and may make the result depend on the principal's willingness to rewrite a synthesis he already accepts.

The recommended model is:

- the principal owns selection, substance and lock;
- Claude may formulate accepted substance when asked or explicitly authorised;
- the formulation is reflected back before write;
- the brief remains deliberately rough and is not normalised into intent semantics;
- unaccepted Claude material does not enter the brief;
- source provenance and material uncertainty remain visible regardless of who wrote the sentence.

This makes authorship a working choice while preserving the principal's composition of the thought.

# 4. Suggested amendments

The following are concise candidate amendments for mining or walkthrough.

## Brief Partner: formulation

> The brief carries the principal's chosen thought. He may write it himself or ask Claude to formulate what they have agreed. Claude never substitutes his wording or synthesis without the principal's explicit acceptance of the substance; where he formulates it, he reflects it back before the write. Translation and grammatical correction do not change substance or style unless the principal asks.

## Brief Partner: boundary with intent

> A brief says what the idea is and why it matters. It may carry a concrete mechanism where that mechanism is part of the idea. Once the work turns to systematic decomposition, normalisation or wording to be agreed block by block, Claude names it as the intent's work and does not continue it inside the brief.

## Brief Aim: omitted alternatives

> What the principal does not take normally leaves no record. Where an alternative materially defines the chosen thought, he may keep a short note of it and why it was left behind; this remains exploratory material, not an intent rejection.

## Intent Aim: judgement

> Each material idea is judged for its value to the intent and for feasibility wherever either distinction matters, and placed on a horizon where the principal sees one.

## Intent Map: whole-brief coverage

> the briefs as wholes: whether the material substance of each is represented, rejected or deliberately left behind.

## Common Map definition

> Map names what must be found or consciously verified for the artefact to be complete, in the artefact's own vocabulary. It is not a questionnaire, a sequence, acceptance criteria or the document's section structure.

## Assignment Map: self-containment

> self-containment: which terms, context and distinctions must be explicit for the recipients to act without the principal in the room.

## Assignment questions

> Questions are one per message and limited to what the intent does not answer. Where the missing answers amount to unresolved substance rather than handover detail, the work returns to the intent. A large question set is evidence of that problem, not its definition.

## Later architectural material

> Status of the remainder of this section: material for later briefs; not to be mined into the elicitation decision except for the dependency that self-contained definitions come first.

## Additional behavioural scenario

> **Intentionally imperfect brief:** a brief contains a meaningful tension, an unresolved alternative and an imprecise boundary. It can still lock when the principal judges it ready for chiselling; the closing Map must not force those matters to be resolved prematurely.

# 5. Recommended disposition

## Ready to mine

- the seven-block definition contract;
- the distinction between finding and the selected brief;
- the brief's closing coverage Map;
- research and ingest as first-class but principal-authorised instruments;
- the intent's Map, Instruments and Course, subject to the amendments above;
- the assignment's provenance map and three-phase joint pass;
- behavioural validation before rules leave `CLAUDE.md`;
- the explicit separation of this decision from the later engine split.

## Decide during mining

- whether Claude may formulate accepted brief substance;
- whether significant unchosen alternatives may remain briefly visible;
- how concrete a mechanism may become before work has crossed into intent;
- whether whole-brief essence coverage is added to intent mining;
- exact citation and `remark` rules for a forge-born brief;
- whether Map covers both finding and conscious verification.

## Keep out of this decision

- local extension roots;
- user-defined artefact discovery;
- plugin and installation mechanism;
- `/recipe` and `/forge` unification;
- final BRD horizon rules;
- the final engine/framework packaging boundary.

# 6. Final assessment

Version 0.4 is ready to be used as input to the intent. It is no longer blocked by the structural issues identified in the first review. Its primary model is coherent: elicitation is broad finding; the brief is the principal's rough choice from it; the intent chisels that choice into a coherent stance; the assignment derives the in-scope stance into a complete, traceable handover.

The largest remaining risk is that the new brief definition overcorrects authorship. If Claude may inspire and synthesise but may not formulate accepted substance, the process may throw away useful wording and quietly return to passive note-taking. The better safeguard is explicit acceptance and reflection before write, not a ban on Claude's prose.

The other remaining changes are narrower: preserve essence-level coverage without recording the fate of every fragment, judge ideas only where the distinctions matter, separate substantive gaps from the number of questions, make later architectural material visibly non-minable, and test that an intentionally imperfect brief can still lock.
