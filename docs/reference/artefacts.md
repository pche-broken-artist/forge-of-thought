---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 7e5089c689da32d2
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

This page lists the artefacts of today's chain, one row per definition: the file, the template, what it is made from, the prefixes of its items and the command that works it. It is for anyone who needs to look up which artefact is which. An artefact is a document of the chain; the principal is the person whose thinking is being forged.

The list is the directory `.claude/skills/forge/states/`, one definition each, in the order of the file numbers. A definition is the state file that says what an artefact is and how it is found. The page [The document chain](../about/the-document-chain.md) gives the reason this directory is the one list.

## Overview

| Artefact | File | Template | Prefixes of its items | Command |
|---|---|---|---|---|
| Brief | `00-brief.md`, `00-brief-<name>.md` | `templates/brief.md` | none | `/forge brief [slug]` |
| Intent | `10-intent.md` | `templates/intent.md` | POS, FCT, REJ, THR | `/forge intent [slug]` |
| Assignment | `20-assignment.md` | `templates/assignment.md` | REQ, OOS, CON, ASM, DEL, TBC, SCR | `/forge assignment [slug]` |
| BRD | `30-brd.md` | `templates/brd.md` | BR, UC, DEP, NFR, OOS, ASM, TBC, SCR | `/forge brd [slug]` |
| Solution design | `40-solution-design.md` | `templates/solution-design.md` | SOL, TBC | `/forge solution-design [slug]` |

## The entries

Each entry has the same shape: description, file, template, inputs, prefixes, command.

### Brief

- Description: compose or finish a brief. It is the principal's idea put together, found with Claude or handed over, approved when done.
- File: `00-brief.md` when bare, or `00-brief-<name>.md` with a name, a later whole of thinking born during the project's life.
- Template: `templates/brief.md`. A header, then free form: any headings, tables or lists the principal finds useful.
- Inputs: the principal's thought, however it arrives. Around it, gathered during the elicitation: research notes (`research/`), sources (`sources/`) and Claude's own proposals. The existing intent and the ledger are read only to know what already stands, never to shape the text.
- Prefixes: none. A brief has no IDs and none of the conventions of the chain.
- Command: `/forge brief [slug]`.

### Intent

- Description: iterate the intent. The briefs are chiselled into what the principal holds.
- File: `10-intent.md`, with the project's threads in `threads/`, one file per thread.
- Template: `templates/intent.md`.
- Inputs: the briefs the principal says to mine (`00-brief.md` and any `00-brief-<name>.md`, approved or not), `decisions.md` and the ledger. Sources enter only as the principal directs. The intent as it stands is read with the project's threads.
- Prefixes: POS (position), FCT (fact), REJ (rejected direction) and THR (open thread, which lives in `threads/`).
- Command: `/forge intent [slug]`.

### Assignment

- Description: iterate the assignment. The intent's in-scope substance is carried to the recipients in a joint pass.
- File: `20-assignment.md`.
- Template: `templates/assignment.md`.
- Inputs: `10-intent.md`, `decisions.md` and the ledger. The intent is read with the project's threads.
- Prefixes: REQ (requirement), OOS (out of scope), CON (constraint), ASM (assumption), DEL (deliverable), TBC (open question) and SCR (success criterion).
- Command: `/forge assignment [slug]`.

### BRD

- Description: iterate the BRD, the business requirements. The assignment, the intent or a source put in is broken into rules, behaviour and qualities that the stakeholders can review and the delivery can estimate. The page [The BRD](../about/the-brd.md) says what the BRD holds and why.
- File: `30-brd.md`. A draft made from a file the principal puts in is a work product in `work/`, never this file.
- Template: `templates/brd.md`.
- Inputs: one parent, named by the principal when he asks for the BRD.
  - `20-assignment.md`, read with `10-intent.md` and `threads/`.
  - `10-intent.md` with `threads/`, where the project has no assignment.
  - A file the principal puts in (a transcript, an offer, a document of someone else) is a third way in and not a parent of the chain.
  - Around the parent: `decisions.md`, the ledger, the DEL items of an assignment, the resource indexes of the project and of every library it depends on, and sources and research as the principal directs.
  - The instance's roster of areas, a library document cited by path. A project with no enterprise around it has no roster and says `Roster: none`.
- Prefixes: BR (business requirement), UC (use case), DEP (dependency), NFR (non-functional requirement), OOS, ASM, TBC and SCR. BR, UC, DEP and NFR are the BRD's own.
- Command: `/forge brd [slug]`.

### Solution design

- Description: iterate the solution design. It says how the things wanted are realised, part by part, with the choices they rest on.
- File: `40-solution-design.md`.
- Template: `templates/solution-design.md`.
- Inputs: the lowest layer the project has above it (the intent alone, the assignment or the BRD, and whatever stands above that), `decisions.md` and the ledger. The intent is read with the project's threads. Where the thing already exists, what realises it is read as it stands. Research and sources as the principal directs.
- Prefixes: SOL (part of the solution) and TBC.
- Command: `/forge solution-design [slug]`.

## A layer a project does not have

A layer a project does not have is not missing: the ledger, the single record of state made at read time, and the checks say nothing of it. The page [Glossary](glossary.md) has every term of the forge in one line.

## See also

- [The document chain](../about/the-document-chain.md): why the listing of that directory is the one list.
- [The BRD](../about/the-brd.md): what the BRD holds and why.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
