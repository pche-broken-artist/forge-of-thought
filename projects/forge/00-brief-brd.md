---
project: forge
title: BRD — a layer of business requirements below the assignment
author: PCHe
version: 0.2
status: draft
---

<!-- Only this header is fixed; the text below it is free-form. The
rules: its definition, `.claude/skills/forge/states/brief.md`; the
history companion:
templates/history.md. -->

## What I want

Start from the BRD of the fork, which a colleague already built on
an early version of the forge and which works: its template, its
drafting skill, its critic. Check it against the standards for what
is missing. Improve it where it is worth it. The base is there; the
work is to bring it into today's forge, not to design a BRD layer
from nothing.

The BRD is `30-brd.md`, below the assignment.

## The IDs the fork uses

From `projects/lib-allwyn/sources/fork-brd/template-brd.md`:

| ID | What it marks | In the forge today |
|---|---|---|
| BR | business requirement; the non-functional requirements are BR too, in the 0900 range | no, new |
| UC | use case | no, new |
| DEP | dependency on another system or document | no, new |
| REF | reference to a related document (assignment, intent, ledger) | no, new |
| OOS | out of scope | yes |
| ASM | assumption | yes |
| SCR | success criterion | yes |
| TBC | open question, with the role that is to answer it | yes |
| REQ | requirement of the assignment, which a BR points to in the traceability matrix | yes |

Being decided, one at a time:
- BR, UC and DEP taken over from the fork as they are, as new
  prefixes of the forge valid in the BRD. (remark: proposed;
  ISO 29148 and BABOK divide requirements the same way; no verdict
  yet.)
- REF: whether it stays a prefix of its own.
- The non-functional requirements: BR in the 0900 range as in the
  fork, or an ID of their own.

## Still open

1. **How the fork is taken over.** Rewritten into the forge's
   format, with the company's content moved to the library
   lib-allwyn, since the engine is public: the checklist of six
   areas with the vendors' names, the gambling law and the company's
   systems. The other ways were copying the fork one to one (the
   company's content would land in the public engine) and
   generating the BRD from the assignment (not possible, the BRD
   adds content the assignment does not have).
2. **A BRD without an assignment.** The chain is intent, then
   assignment, then BRD. May a project skip the assignment and
   write the BRD straight from the intent?
3. **Who signs the BRD.** In the company the stakeholders approve a
   BRD by the RACI (who approves, who is consulted, who is
   informed). Does the forge record that approval, for instance as
   a decision of the project, or does it happen outside the forge,
   in Confluence?
4. **A report for a third party.** The first newcomer to try the
   forge needed a report for an outside party at the end, not an
   assignment. Where such a report belongs is open: a BRD, a layer
   of its own, or something generic. (remark: proposed that it is
   not a BRD and stays open on its own.)
5. **CHL.0030.** In August the CTO reviewer objected that a forge
   growing down to the BRD and the architecture would push out the
   analysts and architects whose work that is; the objection was
   rejected then. To be revisited: if the analyst decides the BRD,
   the forge helps the analyst and does not replace him.
6. **A coding agent.** When Claude takes a whole chain alone and
   hands it to a coding agent (THR.0670), does the agent get the
   BRD or the solution design?

## The material

- projects/lib-allwyn/sources/fork-brd/ — the fork's BRD: template,
  drafting skill, critic, three BRDs and their critiques, the
  company's standard and tutorial; private, cited by path.
- research/2026-10-13-the-brd-layer-of-the-fork-against-todays-engine.md
  — the fork re-read against today's forge.
- research/2026-10-13-what-a-brd-contains-and-how-it-is-found-today.md
  — the standards, and a checklist of what goes wrong in a BRD.
- research/2026-09-07-brd-layer-fork-analysis.md — the first
  reading of the fork.
- research/2026-09-28-artefact-layers-from-idea-to-handover.md —
  where the BRD sits among the layers.
