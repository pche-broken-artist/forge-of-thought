---
project: forge
date: 2026-09-07
topic: the BRD layer as built in a colleague's fork of the engine — what it contains, how good it is, what the forge's own BRD layer should borrow
derived_from: 10-intent.md v4.0 (POS.0700 growth path, POS.0210, POS.0760, POS.0780, POS.1140); a fork of the engine at intent 2.8 read from a local clone on 2026-09-07
status: immutable research note
---

# The BRD layer in a colleague's fork — analysis and lessons

## Question

A colleague forked the engine at intent 2.8 (mid-August 2026), ported it
to a second agent runtime, and added the layer the forge has always
named as its next one: a Business Requirements Document, `30-brd.md`.
Three BRDs were drafted with it and one was taken through three rounds
of an isolated BRD critic. What ideas does that layer carry, which of
them are sound, and what should the forge's own BRD layer (POS.0700,
"certain to come") borrow, and what must it not?

The fork is a private company repository; this note describes its
mechanisms and judges them, and carries nothing company-specific by
name (POS.0760, THR.0210).

## What the fork contains

Read in full on 2026-09-07: the fork's core file, its BRD template and
BRD-critique template, the `draft-brd` and `critique-brd` skills, the
`brd-critic` agent, the three BRDs (a platform initiative at 0.4 after
three critique rounds, a process initiative at 0.2, and a BRD of the
forge itself at 0.1), the three critique reports, the group's BRD
Standards & Guidelines (v0.3, December 2023) ingested as a source, and
the git history since the fork point.

| Element | What the fork did |
|---|---|
| Chain | `00-brief → 10-intent → 20-assignment → 30-brd → (solution design)`; the BRD is "distilled and decomposed from the assignment", audience stakeholders, solution architecture, delivery teams |
| Template `brd.md` | nine fixed chapters: document control (Version History in the body, stakeholder RACI, a six-pillar stakeholder coverage checklist, references), context and objective, scope (scope table, OOS, DEP, ASM, impacted systems), use cases, core business requirements, stakeholder-domain and NFR requirements, success criteria, terminology, appendix with a REQ → BR traceability matrix |
| Prefixes | `BR` business requirement (atomic, testable), `UC` use case, `DEP` dependency (added to the assignment too), a document code `<BRD>.<instance>.NNNN` for the company wiki |
| Drafting rule | "non-duplication": the BRD transforms the assignment into contract-grade requirements and process flows, never copies it |
| Reviewer | a third reviewer kind, `brd-critic`, with its own template: regression of earlier findings first, then findings with location / issue / why it matters / suggested fix, then a pass-fail checklist of the group standard's rules (DS, SIBR), of "what to avoid", of stakeholder-domain coverage and of NFR coverage |
| Core rules changed | prime directive 7 became "structure over prose (all in tables)"; a new directive "assignments stay short and airy (≤ 3 pages)", pushing RACI, impact analysis and MECE decomposition to the BRD; a "wiki publishing standard" section with the company space, hub page id and title convention; "three independent reviewers" |
| Process | the layer arrived through the core file, templates, skills and the README — the forge intent of the fork was not touched: no position, no thread, no decision records the layer |

## Key findings

Epistemic tags: **[C]** consensus in the field, **[S]** one standard or
one organisation's convention, **[F]** the fork's own invention,
**[M]** my judgement from reading the material.

### What is sound and worth borrowing

1. **The BRD as a transformation of the assignment, not a copy.** [F,
   and [C] in substance] The fork's "non-duplication principle" states
   exactly what the forge's essence lens (POS.0410) verifies between
   layers: the child carries the parent's essence in a different kind
   of content. The critic caught the opposite failure twice — a
   traceability matrix mapping BR items to wrong parent REQ ids
   (findings in rounds one and two, fixed only in round three). The
   principle holds; the forge already owns the lens for it.

2. **A 100 % traceability appendix, REQ → BR, verified mechanically.**
   [C] ISO/IEC/IEEE 29148 and BABOK both make traceability between
   requirement levels a property of the set, not a nicety. In the fork
   it was the single most defect-prone artefact of the BRD and the
   critic's most valuable catch. It is a mechanical concern — every
   parent id exists, every parent id is mapped, every child id
   exists — which in the forge's architecture belongs to a check
   (POS.1140), not to a critic.

3. **Stakeholder-domain coverage as an explicit checklist.** [F] Each
   of a fixed roster of enterprise domains ("pillars") receives a row:
   applicable or not, and either the impact in one line or the OOS
   item that excludes it. This forces the author to *enumerate who is
   touched* and permits an explicit "no" — the same move the forge's
   Working methods make for success criteria (absence is a decision,
   not a gap). The idea is sound; its roster is not (see the
   anti-patterns: the fork wrote one company's pillars, statutes and
   vendors into the engine).

4. **Separate tables for dependencies and assumptions.** [S] The group
   standard asks for assumptions (DS.023) and related documents
   (DS.024); the fork separates external-system dependencies (`DEP`)
   from business assumptions (`ASM`) and from out-of-scope items
   (`OOS`) after a critique round found them mixed. Three distinct
   questions — what we rely on, what we take as true, what we refuse —
   deserve three lists. `DEP` is a prefix the forge does not have.

5. **Use cases with traced steps and exception flows.** [C] A header
   (actor, pre- and post-conditions, traced BR items), a step table
   whose every step names the requirement it exercises, and an
   alternate-flow table. The group standard asks only for "diagrams
   and process flows where they give context" (GR.010); the use case
   is the fork's addition and the right one: it is the process view
   the assignment deliberately does not carry and the solution design
   needs.

6. **Discovery questions inline, with an owner.** [F] `TBC` items sit
   as a quoted line directly under the requirement group they belong
   to, addressed to a role ("Compliance lead: confirm retention
   period"). The forge has the `TBC` prefix; the inline placement and
   the role-as-owner are worth keeping. One lesson learned in the
   fork: TBC ids that mirrored BR numbers collided (finding in round
   two) — the forge's global, per-prefix numbering already prevents
   that.

7. **Testability mandatory at this layer.** [S] The forge makes
   testability recommended for the assignment (CLAUDE.md, Requirement
   style) because an assignment is high-level and may delegate; the
   fork makes it mandatory for the BRD. That distinction is correct:
   the BRD is where "produce NFRs and return" (a `DEL` item) is
   answered, and the group standard (SIBR.0020) and 29148 (verifiable
   as a characteristic of every requirement) agree.

8. **Regression-first review with a delta summary.** [F] Every critique
   run opens with new / verified resolved / still open, then re-tests
   every earlier finding in a table before raising new ones. The
   forge's critic contract already runs regression; the fork's compact
   delta head is a good shape to keep.

9. **A dedicated NFR section by category.** [C] Availability,
   recovery, latency, throughput, encryption, auditability,
   multi-tenancy, localisation — the categories are standard and a
   BRD without them is incomplete. The *values* are another matter
   (anti-pattern 4).

10. **The group standard's own process clause.** [S] AP.010: the BRD
    "must be treated as an analysis process to uncover further
    requirements", "should not hand over ambiguity to the solution
    design", and "is often not agnostic of the solution: teams come
    together to break the back of the project ask with architects and
    SMEs". This is looser than the fork's absolute "no solutioning"
    rule: the standard tolerates high-level solution input and
    justified system changes (its section 7) as long as the *how* is
    left to design. The forge's BRD boundary should follow the
    standard, not the fork's stricter reading.

### What is weak or an anti-pattern

1. **"All in tables" as a prime directive.** [F] Two-column tables
   whose second column is a full sentence (`| BR.0010 | The system
   shall … |`) carry no more structure than the forge's `- **BR.0010**
   …` list, read worse in raw Markdown, and make every diff noisy.
   The motive was a wiki publishing target — a render concern, not an
   artefact concern (Document chain 7: a recipe can tabulate). Tables
   earn their place where columns carry data: the traceability
   matrix, the coverage checklist, use-case steps, the NFR categories.
   [M]

2. **"Assignments stay short and airy (≤ 3 pages)", RACI and impact
   analysis pushed down to the BRD.** [F] The fork froze the engine's
   earlier reading; the forge revised it on 2026-08-17 (POS.0210,
   prime directive 8: completeness over brevity, any apparatus may
   appear where it sets direction). Do not re-import.

3. **Instance facts in the engine.** [F] The template, the critic
   agent and the core file carry one company's stakeholder pillars,
   national statutes, ERP and vendor names, wiki space, hub page id,
   document-code prefix and named persons in RACI rows. That is the
   exact boundary POS.0760 and POS.0950 draw: the engine carries no
   instance fact. The forge's BRD layer must be generic in the engine
   and take its roster and publishing target from the instance — a
   library document (POS.1020) or the project's own front-matter.

4. **Requirement values pre-filled in the skeleton.** [F] The template
   states 99.9 % availability, RPO 0, RTO under 15 minutes, 2.5 s at
   the 95th percentile, a TPS figure and native-language support as
   its example rows — and all three BRDs carry them verbatim,
   including the BRD of the forge itself ("conformance checks return
   in under 5 seconds", "review subagents finish in under 90
   seconds"), figures nobody decided. A skeleton that contains a value
   writes the requirement. The forge's rule must be: no value in a
   template, a `TBC` with an owner instead. [M]

5. **A BRD of the forge itself.** [F] Derived from the intent (there
   is no assignment), it invents SLAs, a scale target, wiki badges and
   model tiering, and cites the critic's third-round report as a
   reference named "independent quality critique, 100 % passed". This
   is what happens when a layer is applied because it exists, not
   because the owner needs it — POS.0780's rule that a forge run ends
   where its owner is satisfied, and the ledger's own note that the
   forge project's handover artefact is the core itself. A review used
   as a certificate also contradicts prime directive 5 (advisory,
   never a gate). [M]

6. **A third reviewer kind.** [F] The fork added `brd-critic` beside
   `critic` and `challenger`. In the forge's architecture (POS.1120,
   POS.1140) the reviewer *kinds* are fixed — critic, challenger,
   check — and a new document gets a lens, a persona or a check, not a
   kind. The fork's BRD critique is, read closely, two things: a
   quality review (atomicity, testability, vague words, solutioning)
   that is the clarity lens with layer-specific rules, and a pass-fail
   checklist (ToC present, ids in tens, terms defined, matrix
   complete, no external links) that is a check. [M]

7. **The layer arrived without an intent change.** [F] Nine commits,
   a new document kind, a new reviewer, three new prefixes and a
   rewritten prime directive — and the fork's forge intent records
   none of it; its own core rule says a process change is complete
   only once the intent is updated. POS.0700 says the mechanics of a
   layer are designed when it is taken up: in the forge that design
   is a round of `/forge intent` first, then the operating layer. [M]

8. **A separate drafting command.** [F] `draft-brd` mirrors the fork's
   old `/draft`; the forge's dispatcher is a star (POS.0580) — the BRD
   is one more file in `.claude/skills/forge/states/`, nothing else.

9. **Version History in the body, named persons, a repository link in
   the references.** [S/F] The forge moved history to the companion
   (POS.0310) on 2026-09-04; named persons and links belong to a
   private project, never to a template or to `projects/forge`.

### What the layer actually is, in the field's terms

- **ISO/IEC/IEEE 29148:2018** [C] defines a family of information
  items — Business Requirements Specification (BRS), Stakeholder
  Requirements Specification (StRS), System (SyRS) and Software (SRS)
  requirements specifications — with nine quality characteristics of
  a single requirement (necessary, appropriate, unambiguous, complete,
  singular, feasible, verifiable, correct, conforming) and five of the
  set. Mapped onto the forge: the assignment is a BRS-level document
  (business or mission requirements, why and what at the level of
  direction); the fork's BRD is an StRS-level one — stakeholder
  requirements traceable to the business ones, with solution-level
  functional and non-functional requirements beginning to appear.
- **BABOK v3** [C] classifies requirements as business, stakeholder,
  solution (functional and non-functional) and transition
  (data conversion, training, business continuity). The fork's BRD
  spans stakeholder + solution; its "data migration" pillar is the
  transition class. The forge's assignment ≈ business requirements.
- **The group standard** [S] says of itself that "what we mean by a
  BRD may not be consistent with the wider industry, where user
  requirements, functional requirements and system changes may be
  excluded from a BRD"; it uses the BRD as the place to "do the
  analysis, solve problems and document what is needed, and worry
  about where it belongs later". So the group's BRD is deliberately a
  broad StRS-plus document, and that is the convention the forge's
  versioning and requirement style already follow (POS.0230,
  POS.0300).

## Options for the forge's BRD layer

| Option | What it means | Trade-off |
|---|---|---|
| A. Adopt the fork's layer as is | copy template, skills and critic | fastest; imports every anti-pattern above, breaks POS.0760 (instance facts), POS.0210 (short assignment), POS.1120 (reviewer kinds), and lands a layer nobody designed in the intent |
| B. Design the layer in the forge's own terms, borrowing the sound ideas | a round of `/forge intent` (what a BRD is, its boundary, its prefixes, its reviewers), then `states/brd.md`, `templates/brd.md`, one critic rule set, one check, a library-held roster | slower by one intent round; consistent with every position the forge holds; the fork's three BRDs remain useful as test material and as a worked example of the transformation |
| C. Do nothing yet | the assignment stays the last layer | POS.0700 says the BRD is certain; a colleague has already shown the need and the shape; waiting costs the forge the chance to define the layer before the company's instances define it by accretion |

## Relevance to this project — recommendation

**Take option B.** Open the BRD layer as a thread of the forge intent
and design it in one round of `/forge intent` before any file is
written; borrow from the fork the eight sound ideas and refuse the
nine anti-patterns. Concretely, the round would settle:

1. **What the BRD is.** An StRS-level artefact derived from the
   approved assignment: stakeholder and solution-level requirements,
   process view (use cases), boundaries (OOS, DEP, ASM), NFRs,
   transition requirements, terms, and a traceability appendix;
   audience solution architecture and delivery; readable in isolation
   (DS.010). The boundary of kind follows the group standard's AP.010
   — analysis that breaks the back of the ask with architects, no
   design of the how — rather than the fork's absolute ban.
2. **Prefixes.** `BR` and `UC` new; `DEP` new and BRD-only unless the
   principal wants it in the assignment too; `OOS`, `ASM`, `TBC`,
   `SCR` reused. Testability mandatory at this layer (a rule of the
   layer, stated once in Requirement style).
3. **Template.** Chapters as the fork has them minus the anti-patterns:
   lists not tables except where columns carry data; no values in any
   row; no Version History in the body (companion); no names, no
   links; the stakeholder table lists roles and their involvement.
4. **Coverage roster.** The checklist mechanism in the engine; the
   roster of domains a library document of the instance (POS.1020),
   cited from the project's front-matter, optional — a project with no
   enterprise around it (POS.0780's campaign) simply has none.
5. **Reviewers.** No new kind. The clarity lens receives the BRD's
   rules (atomicity, testability, vague words, solutioning, terms);
   the essence lens verifies BRD against assignment as it does
   assignment against intent; a `check-brd` (or a section of
   `check-project`) verifies the mechanics: ToC, ids in tens, every
   `REQ` of the parent mapped, every mapped id existing, no external
   link in an item, every capitalised term defined. The challenger
   takes the BRD as any other target.
6. **Sign-off.** A BRD is the first artefact whose approval has a
   counterparty other than the principal — the stakeholders of its
   RACI (DS.022) — which CHL.0190's question "what does an approved
   major mean" asks afresh at this layer; the principal decides
   whether the forge records that sign-off (a DEC, a ledger note) or
   leaves it to the instance.
7. **Publishing.** The company wiki is a render target: a recipe of
   genre `brd-page` or a plain recipe with `output:`, never a chain
   mechanism, and its space and page ids live in the instance's
   library, not in the engine.
8. **First run.** The platform initiative's assignment (approved 1.0
   in the principal's own project) is the natural first BRD; the
   fork's 0.4 of the same initiative is a worked comparison for the
   essence lens, and its three critique rounds a calibration set for
   the BRD rules of the clarity lens.

**Proposed change to the intent** (not written; for `/forge intent`):
one new thread, "the BRD layer — taken up", citing POS.0700, this
note, and the eight points above as its agenda; POS.0700's sentence
"the BRD layer is certain to come" then closes into positions of its
own when the round ends. DEC.0060 marked CHL.0030 to be revisited when
the layer is taken up — that revisit belongs to the same round.

## Sources

- ISO/IEC/IEEE 29148:2018 — the information-item family (BRS, StRS,
  SyRS, SRS) and requirement quality characteristics:
  [ReqView: 29148 templates](https://www.reqview.com/doc/iso-iec-ieee-29148-templates/),
  [Modern Requirements: ISO 29148 explained](https://www.modernrequirements.com/blogs/iso-29148-explained/),
  [ISO catalogue entry](https://standards.iteh.ai/catalog/standards/iso/8cf2bc2b-8b5e-4907-a82a-d1c5676c9e85/iso-iec-ieee-29148-2018)
  (read 2026-09-07).
- BABOK v3 requirement classification (business, stakeholder,
  solution, transition):
  [IIBA requirement types infographic](https://www.iiba.org/contentassets/38e412c7b77d456297d953de5bf5ca61/requirement-types-infograph.pdf),
  [Modern Analyst: how BABOK categorises requirements](https://modernanalyst.com/Careers/InterviewQuestions/tabid/128/ID/2033/Explain-how-BABOK-categorizes-requirements.aspx)
  (read 2026-09-07).
- The group's BRD Standards & Guidelines, v0.3 (December 2023) — DS,
  AP, SIBR, RT, GR rules; ingested in the fork as a source; to be
  ingested into the company library of this instance on the
  principal's word.
- The fork itself, read from a local clone on 2026-09-07 (private;
  not cited by path).
- Earlier note `2026-08-25-comparable-projects-landscape.md` for the
  standards family (29148, INCOSE, BABOK) already surveyed.
