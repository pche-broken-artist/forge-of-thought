---
project: forge
title: BRD — a layer of business requirements below the assignment
author: PCHe
version: 0.5
status: draft
---

<!-- Only this header is fixed; the text below it is free-form. The
rules: its definition, `.claude/skills/forge/states/brief.md`; the
history companion:
templates/history.md. -->

## What I want

A BRD layer of the forge built on best practice and the standards
(ISO/IEC/IEEE 29148, BABOK, IREB, the group's own BRD standard),
not a copy of anything. The BRD of the fork is the inspiration:
the person who leads business analysis for me built it on an early
version of the forge and put his own view into it, and what held
on real work is distilled from it — the separate lists of what is
out of scope, what is depended on and what is assumed; use cases
with steps and exceptions; open questions with an owner;
testability mandatory; the touched areas of the enterprise each
found or knowingly found not to apply. What did not hold is not
taken, not even rewritten: everything in tables, short
assignments, the company's names in the engine, a value from the
skeleton standing as a requirement.

The BRD is `30-brd.md`, below the assignment. The company's own
content — the stakeholder pillars, the mandatory areas of the
impact analysis, the systems and vendors, the roles of the RACI,
the wiki convention — stays in the library lib-allwyn; the engine
carries a generic map.

Speed over completeness: I want to try making a BRD as soon as
possible and let the real work show what the definition gets
wrong. The first trial is the project agentic-platform, from its
assignment 1.3, automatically.

## How a BRD is started

Three inputs, one way of working:

1. the assignment, read with the intent and the project's threads
   for the reasons the assignment does not carry; the traceability
   leads to REQ;
2. the intent alone, where the project has no assignment; the
   traceability leads to POS;
3. any file I put in — a transcript of a meeting, an offer, a
   document of someone else — ingested as a source and cited by
   path; the traceability leads to its place in the source. What
   comes out of such a file is always a work product in `work/`,
   never an artefact of the chain: a thing someone said does not
   become my position by being run through a skill. Where I want
   that BRD in the chain, the intent is handed over from the same
   file first and the BRD re-parented on it.

On every input the same map is walked, and in one of two ways: on
my word automatically — draft early: Claude walks the map alone,
writes what the input answers, leaves what it does not as a TBC
with an owner or as an ASM, asks nothing and returns the draft with
a short list of what he assumed, so that I see what it shows — or
found together by questions. The result of the first two inputs
lands in the chain as `30-brd.md` 0.1 where the project takes the
BRD as a layer, or in `work/` where it is a quick look; I say which
when I ask for it. This is my mode of operation: run this file
through the BRD skill and let us see.

## The IDs

| ID | Short for | What it marks | In the forge today |
|---|---|---|---|
| BR | business requirement | one requirement of the business: one sentence, testable, citing the REQ or POS it carries | new |
| UC | use case | a use case at user-goal level: actor, preconditions, outcome, the main scenario in steps, the exceptions | new |
| DEP | dependency | what the BRD relies on outside itself: another system, project or document | new |
| NFR | non-functional requirement | a quality: a value, a condition, a population, from the stakeholders or open as a TBC; the same rules as a BR | new |
| OOS | out of scope | what is not done | yes |
| ASM | assumption | what the requirements rest on and would change if it stopped holding | yes |
| TBC | to be confirmed | an open question with a role as its owner; said whether it blocks estimation | yes |
| SCR | success criterion | how the stakeholders will know the ask was met | yes |

REQ is cited in a BRD as the parent of a BR or a UC, never written
there; the matrix REQ → BR/UC is generated from the items. Not
taken from the fork: REF (a reference to a related document —
related documents are listed without IDs, since an item carries no
link), the 0900 number range for the non-functional requirements
(a type is never told by a number; NFR is a prefix instead), and
no FR (functional requirement): a BR carries the functional
substance at the business level, and a functional specification
below it is the next stage's.

## Decided

- **Sign-off.** The stakeholders' approval by the RACI happens
  outside the forge, where the company does it today. The forge
  records what it can: the principal's approval as an integer
  version, and in the BRD's Stakeholders section the roles with
  their involvement (approves, reviews, consulted, informed), no
  names. A decision in `decisions.md` where I want the sign-off
  recorded; not a rule.
- **A report for a third party** is a work product, not a BRD
  (THR.0360, closed 2026-10-22).
- **A coding agent** gets the artefacts that are available; which
  ones is a person's decision.
- The challenge (CHL.0030, under DEC.0060) revisited 2026-10-23 at
  the birth of the BRD definition; the decision stands.

## The first build and its review

The definition, the template, a challenger persona
`business-analyst` and a check `brd` were built on 2026-10-23 from
this brief and the research, before any position of the intent
(POS.1780), and reviewed the same day by another model outside the
forge, its answer filed as a critique
(`reviews/2026-10-23-critique-external-gemini-2153-337a.md`,
FND.2530 to FND.2620) and settled in a walkthrough. What it
changed: the file put in yields a work product only (above); the
persona hunts only what someone who knows the business would see,
drift and mechanics left to the lenses and the check; the use case
carries a trigger and two guarantees and its steps cite a rule only
where one governs them; the terms carry the states and the source
system of an entity, the mechanics of taking it left to the
solution design; ten categories of quality with safety among them;
the phasing names its items; an open question may carry
`owner: unassigned` until the role is named.

## The first trial

The third way in was tried the same evening on the project
agentic-platform: a BRD drafted automatically from the transcript
of a vendor meeting into `work/`, then the clarity and the essence
lens, the `business-analyst` persona and the `brd` check run on it,
and the result compared with the requirements catalogue derived
from the same meeting in August. The catalogue had taken nearly
everything the vendor said as a requirement; the BRD kept the
room's asks as rules and the vendor's descriptions as dependencies,
and carried what the catalogue has not: stakeholders as roles, the
scope of the document, what is out, the phasing, the follow-ups
with owners, what must come from outside. Three faults of the
automatic pass, found by the reviewers and brought into the
definition, the template, the check and the persona on the same
day, the output left as it is: asks of the room lost because the
items were written before the provenance map, so the map is built
first now; the vendor's answers leaking into rules and use cases,
so a rule cites the principal's side only and the check verifies
it; matters called unknown that the libraries already held, so the
resource indexes are an input always and the list of what comes
from outside says what the forge holds. The reviewers' findings on
that file stay parked in the project, the file a trial and not an
artefact.

## Still open

- The roster of the instance as a document of its own in
  lib-allwyn: after the first trial, which cites the fork's
  template in the bundle by path instead.

## The material

- projects/lib-allwyn/sources/fork-brd/ — the fork's BRD: template,
  drafting skill, critic, three BRDs and their critiques, the
  company's standard and tutorial; private, cited by path.
- research/2026-10-13-the-brd-layer-of-the-fork-against-todays-engine.md
  — the fork re-read against today's forge; the seven blocks of the
  definition and the template drafted there.
- research/2026-10-13-what-a-brd-contains-and-how-it-is-found-today.md
  — the standards, and a checklist of what goes wrong in a BRD.
- research/2026-09-07-brd-layer-fork-analysis.md — the first
  reading of the fork.
- research/2026-09-28-artefact-layers-from-idea-to-handover.md —
  where the BRD sits among the layers.
