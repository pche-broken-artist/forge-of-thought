---
version: 0.1
status: draft            # draft | approved | superseded
project: <slug>
parent: 20-assignment.md   # 20-assignment.md | 10-intent.md; a BRD from a source is a work product (states/brd.md, Inputs)
---

# <Title> — BRD

<!-- The history lives in the companion 30-brd.history.md
(templates/history.md), never here. The rules of every section:
`.claude/skills/forge/states/brd.md`. Items are lists with IDs; a
table only where columns carry data. No value anywhere in this
skeleton stands as a requirement: a value comes from the
stakeholders or is a TBC with an owner. -->

## Purpose & Context
<!-- Two to four paragraphs, from the parent's. Why this exists and
what the reader needs in order to review and estimate. The related
documents, listed by path or name, without IDs. No solutioning
below the line the Aim draws. -->

## Objective
<!-- What must be true at the end. One to three sentences. -->

## Stakeholders
<!-- Roles, never names: who is responsible for the ask on the
business side, who approves, who reviews, who is consulted, who is
informed. The sign-off itself is recorded outside the forge. -->
| Role | Involvement |
|---|---|
| … | responsible / approves / reviews / consulted / informed |

## Scope
**In scope:** <!-- short list, plain text -->

**Out of scope:**
- **OOS.0010** …

**Scope of the document:** <!-- what this BRD does not cover that a
reader would expect, and where it is covered -->

**Impacted systems:** <!-- plain list; what the BRD relies on is a
DEP below -->

## Dependencies
<!-- What the BRD relies on outside itself: another system, project
or document. What must be supplied from outside the forge — the
supplier's or the systems' documentation, a standard, a regulation —
is a DEP with the role that brings it. -->
- **DEP.0010** …

## Assumptions
<!-- What the requirements rest on and would change if it stopped
holding. -->
- **ASM.0010** …

## Use cases
<!-- UC.NNNN at user-goal level. The header and the main scenario
suffice where the behaviour is not contested; the exceptions where
failure, compliance or contract matter. Steps in the active voice,
present tense; a step names a BR only where that rule governs it.
The parent of a use case is its Carries line. -->

### UC.0010 <name>
- **Actor:** …
- **Trigger:** …
- **Preconditions:** …
- **Success outcome:** …
- **Minimal guarantee:** <!-- what holds even when the scenario fails -->
- **Carries:** REQ.NNNN
- **Exercises:** BR.NNNN, BR.NNNN

| Step | Action | BR (where a rule governs the step) |
|---|---|---|
| 1 | … | |

**Exceptions:**
| At step | Condition | Outcome |
|---|---|---|
| … | … | … |

## Business requirements
<!-- BR.NNNN. Numbering: CLAUDE.md, ID scheme; wording: the
Requirement style of `.claude/skills/forge/states/brd.md`. Groups
by capability or process, so that every stakeholder finds theirs
and nothing is twice; a TBC under its group where a rule is not
known. Every item ends with its parent: (REQ.NNNN) or (POS.NNNN).
A TBC whose owner is not yet named carries `owner: unassigned`. -->

### <Group>
- **BR.0010** … (REQ.NNNN)
- **BR.0020** … (REQ.NNNN)
- **TBC.0010** (owner: <role> | unassigned) …

### <Group>
- **BR.0100** … (REQ.NNNN)

## Touched areas of the enterprise
<!-- The roster of the instance, cited by path; each area found (the
items that carry it) or not applicable with the reason; a mandatory
area is never silent. A project with no enterprise around it writes
`Roster: none` and one row saying so. -->
Roster: <path> | none

| Area | Found in / not applicable, because |
|---|---|
| … | … |

## Qualities
<!-- NFR.NNNN, one per category that applies; the categories are the
skeleton's (ISO/IEC 25010 and the practice of a regulated business),
the values the stakeholders'. No value from here: a category without
a value is a TBC with an owner. The same rules as a BR. An NFR ends
with the REQ or POS it follows from, or with its category where the
parent named none. Delete the categories found not to apply, with
the reason in the Touched areas or here. -->
- **NFR.0010** Reliability (service hours, availability, fault
  tolerance, recovery point, recovery time): … (TBC.NNNN, owner:
  <role>) (category: reliability)
- **NFR.0020** Performance (response, throughput, capacity under
  peak, scalability): …
- **NFR.0030** Security and privacy (authentication, authorisation,
  encryption, audit, retention, residency): …
- **NFR.0040** Compliance and regulatory: …
- **NFR.0050** Safety (harm to people, fail-safe behaviour, the
  protection the business owes its users): …
- **NFR.0060** Usability and accessibility: …
- **NFR.0070** Localisation: …
- **NFR.0080** Maintainability and operability (monitoring, support,
  service levels): …
- **NFR.0090** Compatibility and interoperability: …
- **NFR.0100** Data integrity: …

## Transition
<!-- Data to migrate, people to train, the cut-over, where the change
replaces something: BR items in their own group. Delete if nothing is
replaced, with the reason in the Touched areas. -->
- **BR.NNNN** … (REQ.NNNN)

## Phasing
<!-- Mandatory (POS.1360): what each phase of the delivery brings,
in what order, with what dependencies — even as "everything in the
first phase". A phase is a release of the thing, never a version of
this document. -->
| Phase | Delivers | Items carried | Depends on |
|---|---|---|---|
| 1 | … | BR.NNNN, UC.NNNN | … |

## Success criteria
<!-- How the stakeholders will know the ask was met. May be delegated
by the parent. -->
- **SCR.0010** …

## Open questions
<!-- Each with an owner (a role), and whether it blocks estimation.
Questions whose answer must come from outside the forge — the
supplier, the systems' owners, a standard — stand here with that
owner. -->
- **TBC.0010** (owner: <role> | unassigned; blocks estimation: yes | no) …

**To be supplied from outside:** <!-- the list the pass ends with:
what the analyst brings that neither the parent nor the forge holds,
each pointing at its DEP or TBC -->

## Terms
<!-- Every capitalised term of the items; only prefixes and terms
actually used. A term that is a thing the business handles — an
entity — also says the states it may be in and the system it is
taken from; how it is taken is the solution design's, and no
attribute stands here. -->
BR business requirement · UC use case · DEP dependency · NFR
non-functional requirement · OOS out of scope · ASM assumption ·
TBC open question · SCR success criterion

| Term | Meaning | States (entities only) | Source system (entities only) |
|---|---|---|---|
| … | … | … | … |

## Appendix: traceability
<!-- Compiled by Claude at every write from the items, never edited
on its own; verified by /check brd: every parent item mapped, every
mapped ID existing. -->
| Parent | Carried by |
|---|---|
| REQ.NNNN | BR.NNNN, UC.NNNN |
