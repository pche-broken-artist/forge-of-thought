---
title: Review of the elicitation brief
project: forge
reviewed_documents:
  - 00-brief-elicitation.md, version 0.2, 2026-09-28
  - 10-intent.md, version 4.31, 2026-09-27
language: en
status: review
---

# Review of the elicitation brief

## Purpose of this review

This document reviews `00-brief-elicitation.md` against the current `10-intent.md`. It is written as material for Forge of Thought to ingest and work through, not as a replacement brief. It therefore:

- identifies what the proposed extension gets right;
- identifies contradictions, ambiguities, missing decisions and likely failure modes;
- separates the elicitation change from adjacent architectural questions;
- recommends concrete changes to the brief;
- proposes complete candidate definitions for brief, intent and assignment, so that the seven-block shape can be tested against all three current artefacts before it is adopted.

The central conclusion is that the extension solves a real and important gap. The proposed distinction between the map of what must be found, the process by which it is found, and the template into which it lands is sound. The seven-block definition is a credible common shape. The brief is not yet ready to mine unchanged, however, because it currently combines three decisions of different maturity:

1. a shared definition contract for artefact elicitation;
2. revised elicitation semantics for brief, intent and assignment;
3. a later engine/framework/local-extension architecture.

The first two belong together and are mature enough to work. The third should remain a consequence and a separate brief, not part of the decision made here.

# 1. What the extension gets right

## 1.1 It identifies the missing contract

The current mechanism already has two parts:

- a state file describing how work over an artefact runs;
- a template describing the shape of the resulting artefact.

What it lacks is an artefact-owned statement of what must have been found before the artefact is ready. Conduct and output shape do not provide a semantic completeness condition. The elicitation brief correctly identifies this as the missing third part.

The strongest formulation in the brief is:

- the **Map** says what must be consciously found;
- the **process** says how it may be found;
- the **template** says where accepted material lands.

This distinction should become the conceptual centre of the proposal.

## 1.2 It correctly broadens elicitation beyond an interview

Elicitation is a process of finding and forming knowledge. An interview is only one instrument. Depending on the artefact and the state of the thought, elicitation may also use:

- research;
- ingestion and examination of sources;
- verification of assumptions;
- comparison with existing practice;
- analogy and counter-example;
- concrete proposals;
- early drafts used to provoke a precise reaction;
- walkthrough of alternatives or unresolved points.

This fits the existing working methods better than treating elicitation as a sequence of questions. It also explains why the current brief state feels too passive when the principal begins with a rough idea.

## 1.3 It preserves artefact-specific elicitation

A common mechanism must not mean a common conversation. A brief, an intent, an assignment and a future BRD need different things to be discovered and different conduct from the partner. The proposal keeps that semantic variation in the artefact definition rather than placing it in the dispatcher.

That is the right extension model: a new artefact adds a definition and a template. The dispatcher should not gain knowledge of the artefact's meaning.

## 1.4 `Partner` is more useful than `Role`

`Role` easily degenerates into a generic persona. `Partner` describes conduct in relation to the principal:

- what Claude actively contributes;
- what Claude guards;
- what Claude must not decide;
- who owns wording, substance and closure.

The proposed distinction between `Aim` and `Partner` is valuable:

- **Aim** describes the state that is true when the elicitation has done enough;
- **Partner** describes Claude's conduct in helping the principal reach that state.

This distinction should remain explicit in the contract.

## 1.5 The proposed assignment pass is strong

The assignment proposal addresses the real danger of deriving a lower layer: completeness can fail silently. Reading a finished assignment shows what is present, but not what disappeared.

The proposed three-part course is sound:

1. ask only the blocking questions the intent leaves unanswered;
2. draft the whole assignment and build a provenance map;
3. walk through the result by group rather than ceremonially item by item.

The provenance map is especially useful:

- assignment group → assignment items → intent positions;
- in-scope intent positions that landed nowhere;
- assignment items that came from no intent position.

The last two sets should be empty or explicitly explained. This operationalises the existing principles of completeness, intent-first change and drift control.

## 1.6 The order of work is correct

Self-contained artefact definitions are a prerequisite for a clean engine/framework split. Moving artefact-specific rules out of always-on context and into definitions can be done within the present engine. Once done, a later split becomes mainly a decision about ownership, roots, loading and installation.

The elicitation shape should therefore be settled before packaging or architecture. The split is not needed to validate the elicitation model.

# 2. Material problems to resolve

## 2.1 The brief mixes three scopes

The document begins as a proposal for artefact elicitation, then expands into:

- the semantics of brief, intent and assignment;
- the location of rules in `CLAUDE.md`, skills, state files and templates;
- user-defined artefacts;
- local extension roots;
- engine/framework separation;
- plugins and installation units;
- BRD horizon semantics.

These subjects are related, but they are not one decision. Keeping them together causes two problems:

1. the elicitation proposal cannot be accepted without apparently accepting an unresolved architecture;
2. architecture choices become biased by the first three artefacts before a second framework has properly tested the boundary.

**Recommendation:** make the decision of this brief narrower:

- define the common artefact-definition contract;
- define the elicitation semantics of brief, intent and assignment;
- identify the consequences for ownership of current rules;
- prove the shape in the current engine.

Keep as explicit follow-ons, not decisions of this brief:

- engine/framework split;
- plugin or installation mechanism;
- user-local extension roots;
- the concrete BRD definition;
- unifying `/recipe` with `/forge`.

A concise dependency statement is enough:

> Self-contained artefact definitions are a prerequisite for a later engine/framework split. This brief does not decide packaging, roots or installation.

## 2.2 “Claude brings as much as the principal” is the wrong invariant

The wording expresses the desired move from a passive clarifier to an active cognitive partner, but it creates an unhelpful quantitative norm. In a mature external brief, Claude may need to contribute little. In a raw idea, Claude may contribute a great deal. Requiring equal contribution encourages unnecessary expansion.

It also sits uneasily beside the existing rule that the principal owns content and decisions.

**Recommended replacement:**

> Claude contributes proactively and proportionately to what the thought needs. He does not wait to be asked where outside knowledge, alternatives, counter-examples or a concrete proposal would materially sharpen the thought.

This preserves initiative without making volume a virtue.

## 2.3 “Claude does not sort” is too broad

The same definition asks the brief to hold together while forbidding Claude to sort or tidy. Those requirements conflict. Once the elicitation includes research, sources, alternatives and proposals, some organisation is necessary to keep the material navigable.

The useful boundary is not organisation versus no organisation. It is organisation versus adjudication.

**Recommended distinction:**

> Claude may organise material so that the brief remains navigable and coherent. He does not resolve, rank, discard or convert it into positions. Organisation is presentation; selection remains the principal's and formal judgement belongs to the intent.

The brief may have headings, clusters, comparisons and summaries when the principal accepts them. It should not silently become a decided model.

## 2.4 “Nothing is sorted by weight” is also too absolute

Every act of inclusion, ordering and emphasis gives some weight. The principal may also reject an avenue during exploration, and preserving that reaction may be useful.

The correct boundary is between exploratory judgement and formal consolidation.

**Recommended wording:**

> The brief preserves material before formal consolidation. It may record reactions, preferences and discarded avenues as part of the exploration, but it does not convert them into the stable positions, facts, threads and rejections of the intent.

## 2.5 The completion condition of a brief is not operational enough

The proposed Aim combines unlimited breadth with closure when the principal has nothing more to add. That works for the principal's own thoughts but not for the external field Claude is expected to explore. No elicitation can establish that every relevant idea or example has been found.

The completion condition should be sufficiency for the next state, not exhaustion of the discoverable world.

**Recommended readiness condition:**

> The brief is ready to lock when the principal judges that the thought has enough breadth, grounding and unresolved material to be sorted into an intent, and explicitly ends the exploration. Locking means “enough to proceed”, never “everything discoverable has been found”.

This remains a principal decision and not a hard quality gate.

## 2.6 The Map of the brief is both necessary and under-specified

The brief itself identifies the tension correctly:

- no map leaves lock resting only on “the principal said enough”;
- a rigid map threatens the free form and diagnostic value of a brief.

The answer is to preserve a **coverage map**, not a content schema. It should identify areas to consider without requiring a section for each, without forcing every area to contain material, and without turning into a questionnaire.

A stronger Map for the brief should cover:

- **Core thought:** what is being explored, why it matters to the principal and what prompted it;
- **Boundaries known so far:** what appears to belong, what may not belong and where the boundary is unclear;
- **Reality:** verified facts, current conditions and assumptions already corrected;
- **Possibilities:** alternatives, analogies, inspirations, proposals and counter-examples worth later judgement;
- **Material:** sources and durable research on which later reasoning may rely;
- **Unresolved questions:** matters not decided or verified during exploration.

These are not required headings. The closing pass asks whether each area was consciously considered, not whether each has text.

## 2.7 Authorship, provenance and epistemic status are conflated

The brief proposes removing authorship marks because the principal approves what remains. That intuition is good: authorship alone has limited value. The current intent, however, uses origin marks to protect a different distinction: principal's substance versus Claude's construction versus external material.

What needs preserving is not literary authorship, but decision and epistemic status.

A lightweight scheme should distinguish:

- unmarked material: entered by the principal or explicitly accepted into the brief as part of his thought;
- `(source: <path>)`: material grounded in a registered source;
- `(proposal)`: a proposal Claude has placed before the principal but which has not yet been accepted;
- `(reservation)`: a risk, contradiction or uncertainty deliberately left open;
- where material claims knowledge, optionally `(verified)`, `(unverified)` or `(hypothesis)` if the status is not already clear from a citation or the prose.

When the principal accepts a proposal as part of the thought, `(proposal)` disappears. A source citation remains because provenance remains relevant after acceptance. A reservation remains until resolved, dropped or carried into the intent as a thread.

This model should replace the unresolved choice between permanently marking all Claude-authored blocks and marking none.

## 2.8 Epistemic status is praised in the evidence but absent from the contract

The external preparation example values verified facts, unverified claims and hypotheses. The proposed definition then relies mainly on research notes and source paths. That is insufficient for statements or proposals that are not formal research outputs.

**Recommendation:** add to the common contract, probably under shared writing mechanics rather than only the brief:

> A material claim must not acquire more certainty when it moves into an artefact. Where citation and wording do not make the status clear, the artefact preserves whether it is verified, unverified or a hypothesis.

This is a useful invariant across the chain, though the marks may differ by artefact.

## 2.9 Research and ingest need one consistent trigger rule

The brief alternates between calling research and ingest steps rather than offers, and saying that they run on the principal's word. The second is consistent with the existing command and permission model.

**Recommended wording:**

> Research and ingest are first-class instruments of elicitation, not exceptional detours. Claude proposes them when they would materially reduce uncertainty or widen the thought; they run only on the principal's word.

“First-class” means they are part of the expected process. It does not mean Claude invokes a writing or ingesting command autonomously.

## 2.10 `Target`, `Aim` and `Course` risk repeating completion

The seven blocks are viable only if their ownership is precise:

- **Target:** file identity and template only;
- **Inputs:** legitimate starting and supporting material;
- **Aim:** the state of knowledge to be reached, including the readiness condition;
- **Partner:** artefact-specific conduct and decision boundary;
- **Map:** areas that must be consciously covered;
- **Instruments:** available mechanisms specific enough to name here;
- **Course:** artefact-specific sequence, branches and transitions.

`Course` should not redefine completeness. It should say, for example, “when the Aim's readiness condition is met, offer lock”, not state a second condition of its own.

## 2.11 `Instruments` can become a ceremonial list

If every definition merely cites `Draft early`, `Reflect back`, `In pieces`, `Walkthrough`, `/research` and `/ingest`, the block adds noise and becomes another restatement surface.

**Recommendation:** define the block as:

> Instruments names only the shared mechanisms that this artefact uses in a distinctive way, including any constraints on when they are proposed or invoked. Shared methods that apply unchanged need not be enumerated.

Alternatively, keep a short `Uses:` line with references, but require a sentence only where the artefact changes the normal use.

## 2.12 The contract needs rules for empty and omitted blocks

The proposal says Map may possibly be empty on purpose. It does not yet define whether any of the seven blocks may be omitted, empty or inherited.

**Recommendation:**

- every definition carries all seven headings, so the shape is inspectable;
- `Map` may say explicitly that it is open or intentionally empty, with a reason;
- `Instruments` may say `Shared methods only`;
- no block is silently omitted;
- a block cites its owner rather than copying a shared rule.

This makes the contract mechanically checkable without forcing content that does not exist.

## 2.13 Questions, proposals and walkthrough items need a clearer relationship

The brief correctly says a Map is not a questionnaire. It also retains the existing one-question-per-message interview. But proposal-led elicitation introduces turns that are neither questions nor walkthrough verdicts.

The shared conversation mechanism should make the forms explicit:

- a **question** asks for information or a decision Claude cannot supply;
- a **proposal** offers a concrete model or wording to provoke reaction;
- a **reflection** checks understanding before a write;
- a **walkthrough item** asks for a formal verdict on one bounded proposition.

A proposal may close with one sharp question. It should not automatically impose the full `(a)/(m)/(r)/(p)` verdict line unless a walkthrough is actually running. Otherwise exploratory brief work will become ceremonially heavy.

## 2.14 The brief needs a rule for source saturation and research stopping

Once active research becomes part of the brief, a stopping rule is needed to prevent unbounded exploration while preserving the principal's control.

**Suggested rule:**

> Claude proposes a research step against a named uncertainty, comparison or inspiration need. After the step, he states what materially changed, what remains uncertain and whether further research is likely to change the thought. The principal decides whether to continue.

This is not a hard gate or an estimated completeness score. It is a disciplined hand-back of the decision.

## 2.15 The brief needs a rule for negative findings

Research may find that an assumed capability does not exist, that examples are not comparable or that evidence is inconclusive. Those are useful findings and must not vanish merely because they do not add a positive idea.

**Recommendation:** allow the brief to carry negative findings with provenance, and require the intent mining pass to decide whether they become a fact, a rejection, a constraint or no lasting item.

## 2.16 Existing artefacts need migration semantics

Moving rules out of `CLAUDE.md` and changing state definitions may alter behaviour for existing projects. The current intent already distinguishes current conventions from the validity of older artefacts.

The brief should state:

- the new definitions govern future work after adoption;
- locked briefs are not rewritten merely to conform;
- existing draft artefacts may continue under the new definition only on the principal's word;
- migration changes mechanism and conduct, not past provenance;
- the reduction of `CLAUDE.md` follows behavioural verification, not line-count success.

## 2.17 The proposal needs behavioural acceptance tests

The current brief estimates a reduction in `CLAUDE.md` lines. That may be a useful consequence, but it is not evidence that the new shape works.

The proposal should be tested behaviourally with at least these scenarios:

1. **Finished external brief:** store verbatim, identify whether anything needs grounding, and lock without forcing an interview.
2. **Partially written brief:** preserve the supplied text and continue from its stopping point.
3. **Raw idea:** Claude researches, proposes and confronts actively without taking decisions from the principal.
4. **No-research brief:** a thought that needs no external work proceeds without ceremonial instruments.
5. **Intent mining:** every material block of a locked brief is consciously converted, rejected, deferred or left as context with a reason.
6. **Well-formed intent to assignment:** zero preliminary questions are asked; the whole draft and provenance map are produced.
7. **Incomplete intent to assignment:** only blocking questions are asked, and substantive answers return to the intent first.
8. **Drift detection:** the provenance map exposes one omitted position and one invented assignment item.
9. **Long conversation:** one-item behaviour, write-once-per-round and the distinction between proposals and decisions continue to hold.
10. **Existing project:** a locked legacy brief remains valid and is not rewritten by the migration.

Line reduction may be measured afterwards, but only as context cost, not as the success criterion.

# 3. Decisions the brief should make explicitly

The following points are currently implied or left in tension. They should become explicit decisions before mining:

1. **Scope:** this brief decides the elicitation definition contract and the three current artefact definitions, not engine packaging.
2. **Common shape:** all chain artefact definitions use the same seven headings.
3. **Coverage, not questionnaire:** Map is a coverage map and never prescribes conversation order or document headings.
4. **Readiness:** Aim owns the readiness condition; the principal alone closes or locks.
5. **Organisation:** Claude may organise a brief but may not adjudicate it into intent semantics.
6. **Contribution:** Claude is proactive and proportionate, not quantitatively equal to the principal.
7. **Research authority:** Claude proposes; the principal invokes or approves any command that gathers or writes durable material.
8. **Status marking:** preserve provenance, acceptance and epistemic status, not permanent literary authorship.
9. **Intent-first:** new substance discovered while drafting an assignment is written into the intent before it remains in the assignment.
10. **Assignment questions:** ask the smallest blocking set; zero is valid and six is a normal ceiling, not a correctness limit.
11. **Shared rules:** definitions cite shared methods and do not restate them.
12. **Migration:** current locked artefacts remain valid; behaviour is validated before always-on rules are removed.
13. **Extension point:** user-defined artefacts are not required to validate this contract and remain a separate decision.

# 4. Proposed contract for an artefact definition

The following wording is proposed as the normative description of the seven-block shape.

## Target

Names the artefact, its file identity and the template that owns the shape of the output. It does not define the artefact's purpose or repeat the template.

## Inputs

Names the material the elicitation may legitimately start from or draw upon. It distinguishes authoritative inputs, contextual inputs and material that may inform but must not silently determine the artefact.

## Aim

States what becomes true when the elicitation has done enough and gives the readiness condition for transition. It describes a state of the artefact and the knowledge behind it, not Claude's conduct and not a procedure. Readiness is advisory until the principal explicitly closes the state.

## Partner

Defines Claude's artefact-specific stance: what he actively contributes, what he guards, what he must not decide and how responsibility is divided between Claude and the principal. It does not repeat the Aim.

## Map

Names the areas that must be consciously covered for the artefact to be ready. It is neither a questionnaire, a sequence nor the document's section structure. An area may end with no content if it was considered and found inapplicable. A deliberately open or empty Map says so explicitly.

## Instruments

Names only the shared mechanisms used distinctively for this artefact and any artefact-specific constraint on their use. It cites their owners and never re-describes their common procedure. Research, ingesting, drafting, comparison and walkthrough are instruments, not mandatory stages unless the definition says why.

## Course

Defines only the artefact-specific flow: valid ways in, necessary branching, the order of material transformations and the transition offered when the Aim's readiness condition is met. It cites common conversation, writing, versioning and ledger mechanisms rather than repeating them.

## Contract rules

- Every artefact definition carries all seven headings.
- A block may be explicitly empty; it is never silently absent.
- The definition owns semantics specific to that artefact.
- The template owns output structure.
- Shared methods own their procedure.
- `CLAUDE.md` carries only principles that must hold across states or must be always on.
- A definition may make a shared rule stricter for its artefact but may not silently rename or weaken it.
- No definition introduces a new convention, mark or prefix without an intent decision.

# 5. Candidate definition: brief

This is a candidate for evaluation and adaptation, not a rewrite of the reviewed brief.

## Target

`00-brief.md` for the founding whole of thought, or `00-brief-<name>.md` for a later whole. The output shape is owned by `templates/brief.md`: minimal front matter followed by free-form content chosen for the thought. The brief uses no chain IDs and no required chapter structure.

## Inputs

The principal's thought in whatever form it arrives: finished text, partial text, fragments or a raw idea. During elicitation it may draw on registered sources, durable research notes, observations from the conversation and concrete proposals placed before the principal.

The existing intent and ledger may be read to avoid duplication and to understand what already stands. They do not determine the wording or silently turn a new whole into an extension of the old intent.

## Aim

The brief gathers one whole of thought with enough breadth, grounding and unresolved material to be sorted into an intent. It preserves what the principal is exploring, the relevant reality around it, possibilities worth later judgement and the material on which they rest, without prematurely converting them into formal positions, facts, threads or rejections.

The brief is ready to lock when the principal judges that it is sufficient to proceed and explicitly ends the exploration. Locking means enough to proceed, not that everything discoverable has been found.

## Partner

Claude and the principal find and form the thought together. Claude contributes proactively and proportionately: he verifies material assumptions, offers alternatives and analogies, brings relevant examples and counter-examples, proposes research or ingestion where it would materially help, and uses concrete proposals to sharpen the principal's reaction.

Claude raises a contradiction, implausible assumption or material uncertainty as soon as he sees it. He may organise accepted material so that the brief remains navigable and coherent. He does not resolve, rank or discard the material on the principal's behalf, and he does not translate it into the formal semantics of the intent.

The principal decides what remains, when exploration stops and when the brief locks. Unmarked content is the principal's input or material he has explicitly accepted into the brief. Sources retain their citations. Unaccepted proposals and reservations remain visibly marked until settled.

Each response does one useful elicitation act and ends with at most the few questions Claude cannot answer. Claude does not manufacture questions when a proposal, verification or reflection is the more useful next act.

## Map

The elicitation consciously considers, without requiring sections for:

- **Core thought:** what is being explored, why it matters to the principal and what prompted it;
- **Boundaries known so far:** what appears to belong, what may not belong and what remains ambiguous;
- **Reality:** relevant verified facts, current conditions, existing approaches and assumptions corrected during the work;
- **Possibilities:** alternatives, analogies, inspirations, proposals and counter-examples worth later judgement;
- **Material:** sources and durable research on which later reasoning may rely;
- **Unresolved questions:** matters still uncertain, disputed or deliberately left for the intent.

The Map is a closing coverage check, not a questionnaire and not a completeness gate. An area may be inapplicable.

## Instruments

- `Elicitation interview`, `Draft early`, `Reflect back` and `In pieces`: shared working methods, used according to the situation rather than as mandatory stages.
- `/research <topic>`: proposed against a named uncertainty, comparison or inspiration need; run only on the principal's word; durable findings stored and cited.
- `/ingest [file]`: proposed where external material should become a registered source; run only on the principal's word.
- Concrete proposal: an elicitation instrument used to provoke a precise reaction; marked until accepted.
- Comparison or outside example: accompanied by enough provenance and epistemic status to prevent a suggestion from being mistaken for a fact.

After a research step Claude states what materially changed, what remains uncertain and whether more research is likely to change the thought. The principal decides whether to continue.

## Course

1. Resolve the project and target brief. Create a new brief only on the principal's word. Stop if the target brief is locked; a new whole requires a new brief.
2. Identify the way in:
   - **finished outside:** store the supplied text verbatim, ask whether any grounding or exploration is wanted, and lock immediately if the principal says it is finished;
   - **begun outside:** preserve the supplied text and continue from where it stops;
   - **born here:** begin from the rough idea and elicit through the Partner and Map.
3. Accumulate accepted material in the form the principal approves. Do not re-narrate verbatim text or an accepted structure merely to make it sound uniform.
4. Preserve source provenance, open proposals, reservations and material epistemic status. Negative or inconclusive findings remain available for later judgement.
5. Write once per round after reflection and confirmation, using the shared writing and history mechanism.
6. When the Aim's readiness condition appears met, reflect the whole and offer either further exploration or lock. Lock only on the principal's explicit word.
7. After lock, name the state and offer `/forge intent` to mine the brief.

# 6. Candidate definition: intent

## Target

`10-intent.md`. Its template owns the current structure for essence, positions, facts, open threads, rejected directions and any staging material required by the current chain conventions. The intent is a living consolidation, not an append-only record.

## Inputs

All locked briefs not yet fully mined, the current intent, registered sources and research cited by the briefs or deliberately brought into the round, existing decisions, relevant review and challenge outcomes, and the principal's current words.

The ledger supplies state and points to records. It does not supply substitute prose for the substance. A source informs the intent only when deliberately used; registration alone does not promote its content.

## Aim

The intent expresses the principal's current coherent stance. It sorts the material into:

- what the principal holds or wants;
- what is taken as the case, with provenance;
- what remains unresolved;
- what was considered and rejected, with the reason;
- what is deferred to a later horizon rather than rejected;
- what a lower layer may need to know about objective, recipients, delegation or success, where these are already part of the principal's position.

Each material idea from a brief has a visible fate. Contradictions are resolved or held as explicit threads. Duplication is consolidated without losing provenance. The horizon is recorded where the principal sees one. The whole receives a final reality check before a lower layer is derived.

The intent is ready for the next layer when no unresolved thread blocks that derivation, all in-scope source material has a conscious fate and the principal recognises the document as his current position. It remains open to later change.

## Partner

Claude owns consolidation, structure, traceability and the discipline of the process. The principal owns every substantive position, fact adopted on his word, rejection, deferral and decision to leave a matter open.

Claude mines each brief whole by whole; identifies candidate positions, facts, threads and rejections; exposes duplication, tension, unstated assumptions and missing provenance; proposes options and trade-offs; and recommends research where outside grounding could materially change a decision.

Claude may draft wording and structure, but does not silently promote a source statement, his own synthesis or an unaccepted brief proposal into the principal's position. A thread closes only on the principal's word. A consolidated intent authored substantially by Claude remains `in_review` until the principal has walked through its positions under the existing authorship rule.

## Map

The elicitation consciously establishes:

- **Purpose and substance:** what the principal is trying to make true and why;
- **Positions:** what he holds, wants or directs, with reasons and provenance sufficient for later derivation;
- **Facts:** what is treated as the case and on whose or which source's authority;
- **Boundaries:** scope, exclusions, constraints and assumptions that materially shape the thought;
- **Alternatives and rejections:** serious directions considered but not taken, with reasons;
- **Threads:** unresolved questions, contradictions, dependencies and decisions still needed;
- **Horizon:** proof of concept, now, first version, later, or deliberately distant, wherever such a distinction matters;
- **Lower-layer substance:** objective, likely recipients, delegation boundaries and success criteria where already known or necessary to the meaning of the intent;
- **Provenance and coverage:** the fate of each material part of every brief and any external material deliberately used;
- **Reality check:** feasibility, external validity, organisational reality and failure modes proportionate to the subject.

The Map does not prescribe headings or force every project to have every category.

## Instruments

- Brief mining: a traceable pass over one locked brief or one coherent part of it, recording the fate of its material.
- Elicitation interview: one question at a time only where the principal's substance is missing.
- Reflect back and Draft early: used before a write or to expose the consequences of a candidate position.
- `/research` and `/ingest`: proposed where a thread requires outside grounding; invoked only on the principal's word.
- Walkthrough: used for candidate positions, unresolved choices, the reality check and any intent consolidated substantially by Claude.
- Challenge and critique: independent instruments offered at the appropriate point, never substitutes for the principal's decision.

## Course

1. Resolve the current intent and identify pending or partially mined briefs and any round explicitly opened by the principal.
2. Select one coherent whole to work. Do not mix unrelated briefs merely because they are pending.
3. Read the whole and reflect its candidate structure before writing: candidate positions, facts, threads, rejections, horizon and provenance.
4. Work the material by proposal, question and walkthrough as appropriate. One blocking question or one bounded proposition at a time.
5. Give every material part of the source whole a conscious fate: retained, transformed, combined, rejected, deferred, held as a thread or left as context with a reason.
6. Where recipients, objective, delegation or success criteria become substantive, carry them in the intent. Do not invent them merely because a later assignment template has fields.
7. Run the final reality check proportionate to the change before declaring the round ready.
8. Reflect and write once per round on the principal's confirmation. Update mining state and provenance through the existing ledger and history mechanisms.
9. When the Aim's readiness condition for a lower layer is met, name remaining non-blocking threads and offer the next state. The intent itself never locks permanently.

# 7. Candidate definition: assignment

## Target

`20-assignment.md`. The assignment template owns the recipient-facing structure, IDs, requirement style, terms and the representation of requirements, exclusions, constraints, assumptions, delegation, open matters and success criteria.

The assignment is a self-contained handover. It is not a solution design merely because it is detailed.

## Inputs

The current intent is the sole source of substantive direction. The assignment may also read records and cited sources for clarification and provenance, but it may not derive new substance from them behind the intent.

The current assignment, where one exists, is an input for wording continuity, stable IDs and change analysis. Recipient feedback enters only after the principal has processed it through the intent-first path.

## Aim

The assignment carries the complete in-scope substance of the intent to its recipients in a form they can act on without the principal in the room. It makes clear:

- who the recipients are;
- what must be true at the end;
- what they must do or must not do;
- what is constrained or assumed;
- what they are delegated to decide or return;
- what remains deliberately open;
- what is later rather than never;
- how success is known, delegated or deliberately unspecified.

Every in-scope intent position has a visible destination or an explicit reason for not appearing. Every substantive assignment item has provenance in the intent. The assignment is ready when no recipient-relevant matter is left to silent assumption and the principal confirms the handover. Delegated, later and explicitly open are complete states; silent is not.

## Partner

Claude acts as drafter, completeness guardian and drift detector. He first tests whether the intent contains the substance the assignment requires. He asks only for blocking information the principal must supply, using the smallest set of questions; zero is valid, and six is a normal ceiling rather than a correctness limit.

Claude drafts the whole assignment from the intent, preserves stable IDs where applicable, applies the requirement style and produces a temporary provenance map. He raises missing substance as a TBC candidate or a question; he does not fill it from convention or from a source outside the intent.

Claude may be autonomous in wording, structure, traceability and formal completeness. The principal owns all substance and the decision that the assignment is ready. Any substantive change discovered during drafting is proposed to the intent first and only then propagated to the assignment.

## Map

The elicitation consciously establishes:

- **Recipients and use:** who receives the assignment and what action or decision it is meant to enable;
- **Objective and context:** the result sought and the minimum context required to act correctly;
- **Complete scope:** all in-scope substance from the intent, including negative mandates and explicit exclusions;
- **Delivery boundary:** what recipients decide, what they return, what is specified and what is deliberately left open;
- **Constraints and assumptions:** conditions that materially shape execution;
- **Success:** success criteria present, delegated or deliberately absent;
- **Horizon:** what is now, what is expressly later and what is out of scope, without importing rationale that belongs only in the intent;
- **Self-containment:** terms, definitions and information needed without external oral explanation;
- **Traceability:** every in-scope intent position accounted for and every substantive assignment item grounded in the intent;
- **Drift:** no new solution or direction introduced merely by drafting.

## Instruments

- Blocking-question pass: only matters the intent does not answer and the principal must decide.
- Whole-draft pass: draft the complete assignment rather than polishing fragments before coverage is visible.
- Provenance map: `group → items → intent positions`, plus unmatched positions and unmatched items; a working control, not part of the assignment.
- Group walkthrough: one assignment group at a time, showing its purpose, provenance, delegated and open items, and horizon notes.
- Intent-first correction: any substantive discovery returns to the intent before remaining in the assignment.
- Critique `essence`: offered as the independent adjacent-layer test after the joint pass, not run automatically.

## Course

1. Resolve the current intent and assignment. Confirm that the intent is in a state from which derivation is permitted.
2. Read the intent against the assignment Map and identify only blocking gaps. Ask the smallest necessary set one question per message; ask none if the intent already answers the Map.
3. If an answer changes substance, update the intent first through the shared round and writing mechanism.
4. Draft the whole assignment from the settled intent. At the same time produce the temporary provenance map.
5. Report before walkthrough:
   - in-scope intent positions that landed nowhere;
   - assignment items with no intent provenance;
   - silent gaps represented as TBC candidates;
   - any likely drift or premature solution.
6. Resolve these defects or make their treatment explicit before the joint pass.
7. Walk through the assignment group by group. One group is one top-level item; a disputed requirement opens as a sub-item and is closed before returning to the group.
8. Reflect and write once per round on the principal's confirmation. Wording-only corrections may land directly; substance returns to intent first.
9. When the Aim's readiness condition is met, offer critique `essence` and the appropriate approval or release step. Do not claim completeness while either unmatched set contains an unexplained item.

# 8. Boundary between the three definitions

The definitions will work only if their semantic boundaries remain explicit.

## Brief → Intent

The brief may contain:

- raw thoughts;
- accepted proposals;
- alternatives;
- contradictory material;
- source findings;
- unresolved reservations;
- exploratory reactions and discarded avenues.

The intent decides their durable fate. It converts this material into positions, facts, threads, rejections and horizon. A clean or structured brief does not become an intent merely because it is well written.

## Intent → Assignment

The intent contains the principal's substance, rationale and unresolved thought. The assignment contains the recipient-facing direction derived from the in-scope part of that substance.

The assignment may expose a missing decision, but it does not become the place where that decision is silently made. New substance returns to the intent first.

## Horizon by layer

A useful boundary is:

- **brief:** possibilities and temporal ideas as they emerge, without a required horizon taxonomy;
- **intent:** the principal's judgement of now, first version, proof of concept, later, distant, deferred or rejected, with reasons;
- **assignment:** the execution boundary visible to recipients, especially now versus expressly later versus out of scope, without repeating all intent rationale;
- **future BRD:** phasing, sequence and dependencies, when that artefact is defined.

The BRD rule should remain provisional here. This brief may establish only that each artefact definition must state whether and how it discovers horizon.

# 9. Risks of the proposed design

## 9.1 Definitions may become mini constitutions

Moving rules out of `CLAUDE.md` can merely relocate the bloat. Each definition should contain only artefact semantics and artefact-specific conduct. Shared procedure must remain cited.

**Control:** apply the single-source-of-truth check after the three definitions are drafted and before deleting their former rules from `CLAUDE.md`.

## 9.2 Map may become a hidden questionnaire

A model may mechanically walk Map bullets one by one, even if the definition says not to.

**Control:** state that the Map is evaluated opportunistically and at closing; conversation order follows the thought. Behavioural tests should include a brief that naturally covers the Map without any direct question for several areas.

## 9.3 Active Claude may take over authorship

Drafting early and proposing whole architectures are powerful, but the principal may end up auditing Claude's thought rather than composing his own.

**Control:** preserve accepted/unaccepted status, reflect back before write, keep the principal's explicit closure, and apply the existing `in_review` rule where Claude has consolidated substantial content.

## 9.4 Research may dominate exploration

The availability of research can produce a literature survey instead of a thought.

**Control:** every research step answers a named need in the Map and ends with what changed in the thought. Research that cannot name its intended decision or uncertainty is not yet justified.

## 9.5 Provenance may become too heavy

Marking every sentence would destroy readability and produce ceremony.

**Control:** mark blocks or claims only where origin, acceptance or certainty could otherwise be misunderstood. Unmarked accepted material remains the normal case.

## 9.6 Assignment completeness may become false precision

A provenance map can prove coverage of positions without proving that the assignment is understandable, executable or at the right layer.

**Control:** provenance is necessary but not sufficient. Keep the recipient-use, self-containment and assignment-versus-solution checks in the Map and retain independent critique.

## 9.7 A universal seven-block shape may not fit future artefacts

Brief, intent and assignment may all fit because they are neighbouring thought artefacts. A BRD, article or test strategy may expose a missing block or a block that is consistently empty.

**Control:** adopt the shape as the current chain-definition contract, not as an irreversible universal ontology. Require the first genuinely different artefact to test the contract and change it at the mechanism level if necessary.

# 10. Recommended implementation sequence

This sequence avoids coupling the semantic change to the later architecture:

1. Settle the scope and the thirteen explicit decisions in section 3.
2. Finalise the normative contract in section 4.
3. Draft all three definitions before changing any dispatcher or deleting rules from `CLAUDE.md`.
4. Compare the three definitions for duplicated procedure and unclear ownership.
5. Run the behavioural scenarios in section 2.17 against the definitions as written.
6. Move artefact-specific rules from `CLAUDE.md` into the definitions one owner at a time, replacing them with a principle and pointer only where always-on context is still needed.
7. Keep templates structural; do not move elicitation semantics into template comments merely because they mention output fields.
8. Keep the dispatcher unchanged unless the definitions prove that a mechanism change is actually required.
9. Use the new definitions on one new brief-to-intent-to-assignment flow before treating the design as settled.
10. Only after that, open the separate engine-split work to decide roots, packages, installation and framework ownership.

# 11. Suggested disposition of the current brief

## Keep and strengthen

- the definition of elicitation as finding rather than conversation;
- Map / process / template as separate concepts;
- the seven-block shape;
- Partner replacing Role;
- research and ingest as first-class instruments;
- active proposal-led exploration in a brief;
- assignment provenance mapping and group walkthrough;
- self-contained definitions as a prerequisite of later splitting;
- line-count reduction as an expected consequence only.

## Modify

- replace equal contribution with proactive and proportionate contribution;
- replace “does not sort” with permission to organise but not adjudicate;
- replace exhaustive breadth with sufficiency to proceed;
- strengthen the brief Map into a coverage map;
- replace permanent authorship marking with provenance, acceptance and epistemic status;
- make assignment question count a soft ceiling that permits zero;
- allow recipients and success criteria to originate during assignment preparation, but require substantive answers to return to the intent first;
- define exact ownership of readiness between Aim and Course;
- define empty-block and citation rules for the seven-block contract;
- add migration semantics and behavioural acceptance tests.

## Move to separate work

- engine/framework split;
- plugin and installation unit;
- location and discovery of user-defined artefacts;
- unification of `/recipe` and `/forge`;
- concrete BRD definition and mandatory BRD phasing;
- detailed packaging consequences for `CLAUDE.md`, frameworks and local roots.

# 12. Final assessment

The elicitation extension is directionally correct and should proceed. Its strongest contribution is not a richer interview but a missing semantic contract for every artefact: what the work begins from, what it seeks to discover, how Claude partners in that discovery, what must be consciously covered and when the principal has enough to move on.

The proposed seven-block shape is credible, provided its blocks receive strict ownership and remain references to shared procedure rather than copies of it. The shape should be validated by complete definitions of brief, intent and assignment before it is declared the mechanism for future artefacts.

The brief definition needs the most correction. It should empower Claude to research, confront, propose and organise without allowing him to decide or prematurely consolidate. Its completion condition should be sufficiency for intent, not exhaustive collection. Its marks should preserve provenance, acceptance and certainty rather than literary authorship.

The intent definition then becomes the place where the pile is formally judged and consolidated. The assignment definition becomes the place where that settled substance is completely and traceably recast for recipients. The temporary provenance map is the most valuable concrete mechanism in the proposed assignment pass and should be retained.

The engine split should not be decided here. The elicitation work should make that later split easier by producing self-contained definitions, but it does not need the split in order to succeed. Keeping those decisions separate will make both of them clearer, cheaper to test and easier to reverse.
