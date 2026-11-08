---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: cd94fd8d1f335f3b
inputs:
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/brd.md
  - .claude/skills/forge/states/user-stories.md
  - .claude/skills/forge/states/solution-design.md
  - CLAUDE.md#ID scheme
  - CLAUDE.md#Ledger
---

# Artefacts

This page lists the artefacts of today's chain, one entry per definition, with the file, the template, the inputs, the prefixes of the items and the command that works each. It is for the user, the extender and the evaluator who need to find one artefact's facts quickly. The listing of definitions is the one list of artefacts; the reasons are on [The document chain](../about/the-document-chain.md), and the terms are in the [Glossary](glossary.md).

The commands below are typed as `/forge <state> [slug]`, where the slug names the project. The principal is whoever's thinking is being forged. The ledger is the state file that is made from the documents at read time.

## Overview

| Artefact | What it is for | File | Template | Items | Command |
|---|---|---|---|---|---|
| Brief | The principal's idea put together, found with Claude or handed over | `00-brief.md` or `00-brief-<name>.md` | `templates/brief.md` | none | `/forge brief [slug]` |
| Intent | The briefs chiselled into what the principal holds | `10-intent.md` | `templates/intent.md` | POS, FCT, THR, REJ | `/forge intent [slug]` |
| Assignment | The intent's in-scope substance carried to the recipients | `20-assignment.md` | `templates/assignment.md` | REQ, OOS, CON, ASM, DEL, TBC, SCR | `/forge assignment [slug]` |
| BRD | The business requirements: rules, behaviour and qualities the stakeholders can review | `30-brd.md` | `templates/brd.md` | BR, UC, DEP, NFR, OOS, ASM, TBC, SCR | `/forge brd [slug]` |
| User stories | The requirements broken into stories of behaviour | `35-user-stories.md` | `templates/user-stories.md` | US | `/forge user-stories [slug]` |
| Solution design | How the things wanted are realised, part by part | `40-solution-design.md` | `templates/solution-design.md` | SOL, TBC | `/forge solution-design [slug]` |

## Brief

- File: `00-brief.md` (bare) or `00-brief-<name>.md` (a later whole of thinking born during the project's life).
- Description: Compose or finish a brief. It is the principal's idea put together, found with Claude or handed over, approved when done.
- Template: `templates/brief.md`, a YAML header and then free form.
- Inputs: the principal's thought, however it arrives. Around it come the research notes in `research/`, the sources in `sources/` and Claude's own proposals. The existing intent and the ledger are read only to know what already stands.
- Prefixes: none. A brief carries no IDs.
- Command: `/forge brief [slug]`.

## Intent

- File: `10-intent.md`.
- Description: Iterate the intent. The briefs are chiselled into what the principal holds.
- Template: `templates/intent.md`.
- Inputs: the briefs the principal says to mine (`00-brief.md` and any `00-brief-<name>.md`, approved or not), `decisions.md`, the ledger, and sources only as the principal directs. The intent as it stands is read with the project's `threads/`.
- Prefixes: POS (position), FCT (fact), THR (thread), REJ (rejected direction).
- Command: `/forge intent [slug]`.

## Assignment

- File: `20-assignment.md`.
- Description: Iterate the assignment. The intent's in-scope substance is carried to the recipients in a joint pass.
- Template: `templates/assignment.md`.
- Inputs: `10-intent.md` read with the project's `threads/`, `decisions.md` and the ledger.
- Prefixes: REQ (requirement), OOS (out of scope), CON (constraint), ASM (assumption), DEL (deliverable), TBC (open question), SCR (success criterion).
- Command: `/forge assignment [slug]`.

## BRD

- File: `30-brd.md`.
- Description: Iterate the BRD. The assignment or the intent is broken into rules, behaviour and qualities that the stakeholders can review and the delivery can estimate. A source put in yields a draft BRD as a work product.
- Template: `templates/brd.md`.
- Inputs: one parent, named by the principal when he asks for the BRD.
  - `20-assignment.md`, read with `10-intent.md` and `threads/`. The parent of an item is then a REQ.
  - `10-intent.md` with `threads/`, where the project has no assignment. The parent is then a POS.
  - A file the principal puts in (a transcript, an offer, a document of someone else) is a third way in and not a parent of the chain. It yields a draft BRD as a work product in `work/`, never `30-brd.md`.
- Around the parent: `decisions.md`, the ledger, the DEL items of an assignment, the indexes of the project's resources and of the libraries it depends on, and sources and research as the principal directs.
- From the instance: the roster of areas of the enterprise a BRD must consider and which of them are mandatory, and the group's standard where the instance has one. Both are library documents of the instance, cited by path. A project with no enterprise around it says `Roster: none`.
- Prefixes: BR (business requirement), UC (use case), DEP (dependency), NFR (non-functional requirement), OOS, ASM, TBC, SCR. BR, UC, DEP and NFR are the BRD's own.
- Command: `/forge brd [slug]`.
- More: what the BRD holds and why is on [The BRD](../about/the-brd.md).

## User stories

- File: `35-user-stories.md`.
- Description: Iterate the user stories. The requirements are broken into stories of behaviour that the stakeholders approve as a whole, the delivery builds from and the testers test from.
- Template: `templates/user-stories.md`.
- Inputs: one parent, named by the principal when he asks for the stories.
  - `30-brd.md`, read with the layers above it. A story cites the BR, NFR, UC or DEP it serves.
  - `10-intent.md` with `threads/`, where the change is small, the ask precise and without further impact, and the principal says so. A story then cites the POS it serves.
  - A requirements document of someone else, put in through `/ingest`, yields stories as a work product in `work/`, never `35-user-stories.md`.
- Around the parent: `decisions.md`, the ledger, and the indexes of the project's resources, sources and research as the principal directs.
- Prefixes: US (user story), the layer's own.
- Command: `/forge user-stories [slug]`.
- More: what the stories hold and why is on [The user stories](../about/the-user-stories.md).

## Solution design

- File: `40-solution-design.md`.
- Description: Iterate the solution design. It says how the things wanted are realised, part by part, with the choices they rest on.
- Template: `templates/solution-design.md`.
- Inputs: the lowest layer the project has above it (the intent alone, the assignment, the BRD or the user stories) and whatever stands above that, `decisions.md` and the ledger. The intent is read with `threads/`. Where the thing already exists, what realises it is read as it stands. Research and sources come as the principal directs.
- Prefixes: SOL (part of the solution), TBC.
- Command: `/forge solution-design [slug]`.

A layer a project does not have is not missing: the state map and the checks say nothing of it.

## See also

- [The document chain](../about/the-document-chain.md): why the listing of that directory is the one list.
- [The BRD](../about/the-brd.md): what the BRD holds and why.
- [The user stories](../about/the-user-stories.md): what the stories hold and why.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
