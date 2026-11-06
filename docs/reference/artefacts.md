---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 540a4be16428cc33
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

This page lists the artefacts of the chain as it stands today, one row per definition, with the file each is kept in, its template, what it is made from, the prefixes of its items and the command that works it. It is for anyone who needs to look up which artefact a project can have and what it reads. The reason the listing of definitions is the one list is on [The document chain](../about/the-document-chain.md).

A definition is a state file in `.claude/skills/forge/states/`. The artefacts are listed here in the order of the file numbers. The principal is the person whose thinking is being forged. The ledger is the state report that is made from the documents when it is read.

## Overview

| Artefact | What it is for | When it fits | File |
|---|---|---|---|
| Brief | The principal's idea put together | Every project starts here; a later whole of thinking is a later brief | `00-brief.md` or `00-brief-<name>.md` |
| Intent | The briefs chiselled into what the principal holds | Every project has one; it is the trunk of the chain | `10-intent.md` |
| Assignment | The intent's in-scope substance carried to the recipients | When recipients must act without the principal in the room | `20-assignment.md` |
| BRD | The business requirements | When stakeholders must review and delivery must estimate | `30-brd.md` |
| Solution design | How the things wanted are realised | When a design is worth writing | `40-solution-design.md` |

The descriptions below are quoted as the definitions have them, with their long dash rendered as a spaced hyphen.

## Brief

- File: `00-brief.md` (bare) or `00-brief-<name>.md` (with a name: a later whole of thinking born during the project's life).
- Description: "Compose or finish a brief - the principal's idea put together, found with Claude or handed over, approved when done".
- Template: `templates/brief.md`.
- Inputs: the principal's thought, however it arrives. Around it, gathered during the work: research notes (`research/`), sources (`sources/`) and Claude's own proposals. The existing intent and the ledger are read only to know what already stands.
- Prefixes of its items: none. A brief has no IDs and no conventions of the chain.
- Command: `/forge brief`.

## Intent

- File: `10-intent.md`, with the project's threads in `threads/`.
- Description: "Iterate 10-intent.md - the briefs chiselled into what the principal holds".
- Template: `templates/intent.md`.
- Inputs: the briefs the principal says to mine (`00-brief.md` and any `00-brief-<name>.md`, approved or not), `decisions.md` and the ledger. Sources only as the principal directs. The intent as it stands is read with the threads.
- Prefixes of its items: POS (position), FCT (fact), REJ (rejected direction) and THR (open thread, one file each in `threads/`).
- Command: `/forge intent`.

## Assignment

- File: `20-assignment.md`.
- Description: "Iterate 20-assignment.md - the intent's in-scope substance carried to the recipients in a joint pass".
- Template: `templates/assignment.md`.
- Inputs: `10-intent.md` read with the project's threads, `decisions.md` and the ledger.
- Prefixes of its items: REQ (requirement), OOS (out of scope), CON (constraint), ASM (assumption), DEL (deliverable), TBC (open question) and SCR (success criterion).
- Command: `/forge assignment`.

## BRD

- File: `30-brd.md`.
- Description: "Iterate 30-brd.md - the business requirements: the assignment or the intent broken into rules, behaviour and qualities the stakeholders can review and the delivery can estimate; a source put in yields a draft BRD as a work product".
- Template: `templates/brd.md`.
- Inputs: one parent, named by the principal when he asks for the BRD.
  - `20-assignment.md`, read with `10-intent.md` and `threads/`.
  - `10-intent.md` with `threads/`, where the project has no assignment.
  - A file the principal puts in (a transcript, an offer, a document of someone else) is a third way in. It is registered through `/ingest` and yields a draft BRD that is a work product in `work/`, never `30-brd.md`.
- Inputs around the parent:
  - `decisions.md` and the ledger.
  - The DEL items of an assignment, as the list of what the BRD is asked to bring back.
  - The roster of the instance, the areas of the enterprise a BRD must consider and which of them are mandatory: a library document of the instance, cited by path. A project with no enterprise around it has no roster and says `Roster: none`.
  - The group's standard, where the instance has one: a library document likewise.
  - The indexes of the project's resources and of every library it depends on (`sources/00-INDEX.md`, `research/00-INDEX.md`, `projects/lib-*/sources/00-INDEX.md`).
  - Sources and research as the principal directs.
- Prefixes of its items: BR (business requirement), UC (use case), DEP (dependency) and NFR (non-functional requirement), which are the BRD's own; also OOS, ASM, TBC and SCR.
- Command: `/forge brd`.

What the BRD holds and why is on [The BRD](../about/the-brd.md).

## Solution design

- File: `40-solution-design.md`.
- Description: "Iterate 40-solution-design.md: how the things wanted are realised, part by part, with the choices they rest on".
- Template: `templates/solution-design.md`.
- Inputs: the lowest layer the project has above it (the intent alone, the assignment or the BRD) and whatever stands above that, `decisions.md` and the ledger. The intent is read with the project's threads. Where the thing already exists, what realises it is read as it stands. Research and sources as the principal directs.
- Prefixes of its items: SOL (a part of the solution) and TBC (open question).
- Command: `/forge solution-design`.

## A layer a project does not have

A layer a project does not have is not missing: none of the layers below the intent is a condition of another, and the ledger and the checks say nothing of an absent one.

## See also

- [The document chain](../about/the-document-chain.md): why the listing of that directory is the one list.
- [The BRD](../about/the-brd.md): what the BRD holds and why.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
