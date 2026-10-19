---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 370b810ddb55ade9
inputs:
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/solution-design.md
  - CLAUDE.md#ID scheme
  - CLAUDE.md#Ledger
---

# Artefacts

This page lists the artefacts of the chain as it stands today, one row per definition, for anyone who needs to see at a glance which documents a project can have, what each is made from and which command works it. An artefact is a document of the chain; its definition is the state file that says what it is and how it is found. The directory of definitions is the one list of artefacts (see [The document chain](../about/the-document-chain.md)), so this page follows it in the order of the file numbers. Terms of the forge are explained in the [Glossary](glossary.md). The principal is the person whose thinking is being forged.

## Overview

| Artefact | What it is for | When it fits | Where it lives |
|---|---|---|---|
| Brief | The principal's idea put together: what he wants, why and what not | A thought is new and still rough | `00-brief.md`, later ones `00-brief-<name>.md` |
| Intent | The briefs chiselled into what the principal holds | One or more briefs are to be mined into positions | `10-intent.md` |
| Assignment | The in-scope substance of the intent carried to the recipients | The recipients are to act without the principal in the room | `20-assignment.md` |
| Solution design | How the things wanted are realised, part by part, with the choices they rest on | A realisation is worth writing down | `40-solution-design.md` |

## Brief

- **File:** `00-brief.md`, or `00-brief-<name>.md` for a later whole of thinking born during the project's life.
- **Description:** Compose or finish a brief: the principal's idea put together, found with Claude or handed over, approved when done.
- **Template:** `templates/brief.md`.
- **Target:** the brief file. Its shape is a short YAML header, then free form: any headings, tables or lists the principal finds useful.
- **Inputs:** the principal's thought, however it arrives. Around it, gathered during the elicitation: research notes in `research/`, sources in `sources/` and Claude's own proposals. The existing intent and the ledger are read only to know what already stands, never to shape the text.
- **Prefixes of its items:** none. A brief carries no IDs and no conventions of the chain.
- **Command:** `/forge brief [slug]`.

## Intent

- **File:** `10-intent.md`.
- **Description:** Iterate the intent: the briefs chiselled into what the principal holds.
- **Template:** `templates/intent.md`.
- **Target:** the intent file.
- **Inputs:** the briefs the principal says to mine (`00-brief.md` and any `00-brief-<name>.md`, approved or not), `decisions.md` and the ledger. Sources enter only as the principal directs. The intent as it stands is read with the project's threads in `threads/`.
- **Prefixes of its items:**
  - `POS`: a position the principal currently holds
  - `FCT`: a fact, what is the case as the principal or a source states it
  - `REJ`: a rejected direction, with the reason it was dropped
  - `THR`: an open thread, kept as one file per thread in `threads/`, part of the intent
- **Command:** `/forge intent [slug]`.

## Assignment

- **File:** `20-assignment.md`.
- **Description:** Iterate the assignment: the intent's in-scope substance carried to the recipients in a joint pass.
- **Template:** `templates/assignment.md`.
- **Target:** the assignment file.
- **Inputs:** `10-intent.md`, `decisions.md` and the ledger. The intent is read with the project's threads in `threads/`.
- **Prefixes of its items:**
  - `REQ`: a requirement
  - `OOS`: out of scope, or a do-not
  - `CON`: a constraint, a deliberate boundary not to be challenged
  - `ASM`: an assumption
  - `DEL`: a deliverable, which may delegate work
  - `TBC`: an open question to be confirmed, with an owner
  - `SCR`: a success criterion, optional or delegated
- **Command:** `/forge assignment [slug]`.

## Solution design

- **File:** `40-solution-design.md`.
- **Description:** Iterate the solution design: how the things wanted are realised, part by part, with the choices they rest on.
- **Template:** `templates/solution-design.md`.
- **Target:** the solution design file.
- **Inputs:** the lowest layer the project has above it (the intent alone, the assignment or the BRD, and whatever stands above that), `decisions.md` and the ledger. The intent is read with the project's threads in `threads/`. Where the thing already exists, what realises it is read as it stands. Research and sources enter as the principal directs.
- **Prefixes of its items:**
  - `SOL`: a part of the solution, what is built or done, what it realises and the choice it rests on
  - `TBC`: an open question to be confirmed, with an owner
- **Command:** `/forge solution-design [slug]`.

A layer a project does not have is not missing: `/forge` and the checks say nothing of it.

## See also

- [The document chain](../about/the-document-chain.md): why the listing of that directory is the one list.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
