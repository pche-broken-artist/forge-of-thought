---
generated: 2026-10-23
version: 5.33
made: mirrored
inputs-hash: 5a8e15e5c05fb9f8
inputs:
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/solution-design.md
  - CLAUDE.md#ID scheme
  - CLAUDE.md#Ledger
---

# Artefacts

This page lists the artefacts of the chain as it stands today, one row per definition: the file each one is, the template it takes its shape from, what it is made from, the prefixes of its items and the command that works it. It is for anyone who needs to look up one artefact quickly.

The artefacts are the listing of the directory `.claude/skills/forge/states/`, one definition (a state file) each, in the order of the file numbers. A project's `00-brief.md` is the principal's first document (the principal is whoever's thinking is being forged).

## Overview

| Artefact | File | Description | Template | Command |
|---|---|---|---|---|
| Brief | `00-brief.md`, `00-brief-<name>.md` | The principal's idea put together, found with Claude or handed over, approved when done | `templates/brief.md` | `/forge brief [slug]` |
| Intent | `10-intent.md` | The briefs chiselled into what the principal holds | `templates/intent.md` | `/forge intent [slug]` |
| Assignment | `20-assignment.md` | The intent's in-scope substance carried to the recipients in a joint pass | `templates/assignment.md` | `/forge assignment [slug]` |
| Solution design | `40-solution-design.md` | How the things wanted are realised, part by part, with the choices they rest on | `templates/solution-design.md` | `/forge solution-design [slug]` |

## Brief

- File: `00-brief.md` when bare, `00-brief-<name>.md` when named (a later whole of thinking born during the project's life).
- Description: the principal's idea put together, found with Claude or handed over, approved when done.
- Template: `templates/brief.md`, a YAML header and then free form.
- Inputs: the principal's thought, however it arrives. Around it, the research notes in `research/`, the sources in `sources/` and Claude's own proposals. The existing intent and the ledger are read only to know what already stands.
- Prefixes of its items: none. A brief carries no IDs.
- Command: `/forge brief [slug]`.

## Intent

- File: `10-intent.md`.
- Description: the briefs chiselled into what the principal holds.
- Template: `templates/intent.md`.
- Inputs: the briefs the principal says to mine (approved or not), `decisions.md` and the ledger. Sources only as the principal directs. The intent as it stands is read with the project's threads in `threads/`.
- Prefixes of its items:
  - `POS`: a position the principal currently holds.
  - `FCT`: a fact.
  - `REJ`: a rejected direction, with the reason.
  - `THR`: an open thread. Each thread is a file in `threads/`, not a line of the intent.
- Command: `/forge intent [slug]`.

## Assignment

- File: `20-assignment.md`.
- Description: the intent's in-scope substance carried to the recipients in a joint pass.
- Template: `templates/assignment.md`.
- Inputs: `10-intent.md`, `decisions.md` and the ledger. The intent is read with the project's threads.
- Prefixes of its items:
  - `REQ`: a requirement.
  - `OOS`: out of scope, or a do-not.
  - `CON`: a constraint, a deliberate boundary not to be challenged.
  - `ASM`: an assumption.
  - `DEL`: a deliverable, which may delegate work.
  - `TBC`: an open question, with an owner.
  - `SCR`: a success criterion, optional or delegated.
- Command: `/forge assignment [slug]`.

## Solution design

- File: `40-solution-design.md`.
- Description: how the things wanted are realised, part by part, with the choices they rest on.
- Template: `templates/solution-design.md`.
- Inputs: the lowest layer the project has above it (the intent alone, the assignment or the BRD, and whatever stands above that), `decisions.md` and the ledger. The intent is read with the project's threads. Where the thing already exists, what realises it is read as it stands. Research and sources as the principal directs.
- Prefixes of its items:
  - `SOL`: a part of the solution, or a matter that holds across parts.
  - `TBC`: an open question, with an owner, what would close it and whether it blocks realisation.
- Command: `/forge solution-design [slug]`.

## A layer a project does not have

A layer below the intent that a project does not have is not missing. `/forge` and the checks say nothing of it.

## See also

- [The document chain](../about/the-document-chain.md): why the listing of that directory is the one list.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-23 for version 5.33 from the files the front-matter names; never edited by hand.
