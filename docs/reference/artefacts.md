---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 6303a92b255b4680
inputs:
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/brd.md
  - .claude/skills/forge/states/solution-design.md
  - CLAUDE.md#ID scheme
  - CLAUDE.md#Ledger
---

# Artefacts

This page lists the artefacts of today's chain, one row per definition, with the file each produces, its template, what it reads, the prefixes of its items and the command that works it. It is for the user who wants to know which layers exist, the extender who adds one, and the evaluator who checks what the forge covers. The chain is the set of versioned documents a thought travels through, from the brief downward. Terms of the forge are in the [Glossary](glossary.md); why the listing of the definitions directory is the one list is in [The document chain](../about/the-document-chain.md).

Each artefact has one definition: a file in `.claude/skills/forge/states/`. The artefacts are the files of that directory, in the order of the file numbers. Every artefact is worked by `/forge <state> [slug]`, where `<state>` is the name of its definition and `slug` names the project. A project is a repository of its own; the principal is whoever's thinking is being forged.

## Overview

| Artefact | File | Template | Prefixes of its items | Command |
|---|---|---|---|---|
| Brief | `00-brief.md`, `00-brief-<name>.md` | `templates/brief.md` | none | `/forge brief` |
| Intent | `10-intent.md` | `templates/intent.md` | POS, REJ, FCT, THR | `/forge intent` |
| Assignment | `20-assignment.md` | `templates/assignment.md` | REQ, OOS, CON, ASM, DEL, TBC, SCR | `/forge assignment` |
| BRD | `30-brd.md` | `templates/brd.md` | BR, UC, DEP, NFR, OOS, ASM, TBC, SCR | `/forge brd` |
| Solution design | `40-solution-design.md` | `templates/solution-design.md` | SOL, TBC | `/forge solution-design` |

## Brief

- **File:** `00-brief.md`, or `00-brief-<name>.md` for a later whole of thinking born during the project's life.
- **Description:** Compose or finish a brief: the principal's idea put together, found with Claude or handed over, approved when done.
- **Template:** `templates/brief.md`. A YAML header, then free form: any headings, tables or lists the principal finds useful, no IDs, no conventions of the chain.
- **Inputs:** the principal's thought, however it arrives. Around it, gathered during the elicitation: research notes (`research/`), sources (`sources/`) and Claude's own proposals. The existing intent and the ledger (the state of a project, made at read time by `python scripts/forge-ledger.py <slug>`) are read only to know what already stands, never to shape the text.
- **Prefixes of its items:** none.
- **Command:** `/forge brief [slug]`.

## Intent

- **File:** `10-intent.md`, with the project's threads in `threads/`, one file per thread.
- **Description:** Iterate 10-intent.md: the briefs chiselled into what the principal holds.
- **Template:** `templates/intent.md`.
- **Inputs:** the briefs the principal says to mine (`00-brief.md` and any `00-brief-<name>.md`, approved or not), `decisions.md` and the ledger; sources only as the principal directs. The intent as it stands is read with the project's threads.
- **Prefixes of its items:** POS (position), REJ (rejected direction), FCT (fact), THR (open thread, kept in `threads/`).
- **Command:** `/forge intent [slug]`.

## Assignment

- **File:** `20-assignment.md`.
- **Description:** Iterate 20-assignment.md: the intent's in-scope substance carried to the recipients in a joint pass.
- **Template:** `templates/assignment.md`.
- **Inputs:** `10-intent.md`, `decisions.md` and the ledger. The intent is read with the project's threads.
- **Prefixes of its items:** REQ (requirement), OOS (out of scope), CON (constraint), ASM (assumption), DEL (deliverable), TBC (open question), SCR (success criterion).
- **Command:** `/forge assignment [slug]`.

## BRD

- **File:** `30-brd.md`. A draft made from a file the principal puts in is a work product in `work/`, never `30-brd.md`.
- **Description:** Iterate 30-brd.md: the business requirements: the assignment or the intent broken into rules, behaviour and qualities the stakeholders can review and the delivery can estimate; a source put in yields a draft BRD as a work product.
- **Template:** `templates/brd.md`.
- **Inputs:** one parent, named by the principal when he asks for the BRD:
  - `20-assignment.md`, read with `10-intent.md` and `threads/`; or
  - `10-intent.md` with `threads/`, where the project has no assignment.
  - Around the parent: `decisions.md`, the ledger, the DEL items of an assignment, the instance's roster of areas (a library document cited by path; a project with no enterprise around it says `Roster: none`), the group's standard where the instance has one (a library document likewise), the resource indexes of the project and of every library it depends on, and sources and research as the principal directs.
- **Prefixes of its items:** BR (business requirement), UC (use case), DEP (dependency), NFR (non-functional requirement), OOS, ASM, TBC, SCR. BR, UC, DEP and NFR are the BRD's own.
- **Command:** `/forge brd [slug]`.

What the BRD holds and why is in [The BRD](../about/the-brd.md).

## Solution design

- **File:** `40-solution-design.md`.
- **Description:** Iterate 40-solution-design.md: how the things wanted are realised, part by part, with the choices they rest on.
- **Template:** `templates/solution-design.md`.
- **Inputs:** the lowest layer the project has above it (the intent alone, the assignment or the BRD, and whatever stands above that), `decisions.md` and the ledger. The intent is read with the project's threads. Where the thing already exists, what realises it is read as it stands. Research and sources as the principal directs.
- **Prefixes of its items:** SOL (part of the solution), TBC.
- **Command:** `/forge solution-design [slug]`.

## A layer a project does not have

A layer a project does not have is not missing: `/forge` and the checks say nothing of it.

## See also

- [The document chain](../about/the-document-chain.md): why the listing of that directory is the one list.
- [The BRD](../about/the-brd.md): what the BRD holds and why.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
