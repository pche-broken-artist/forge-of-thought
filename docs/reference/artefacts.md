---
generated: 2026-10-25
version: 6.1
made: mirrored
inputs-hash: c3ba0701dd364288
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

This page lists the artefacts of the chain as it stands today, one
per definition, for anyone who needs to know which file each one is,
what it is made from and which command works it. An artefact is a
document of the chain; a definition is the file in
`.claude/skills/forge/states/` that says what the artefact is and how
it is found. The principal (the person whose thinking is forged)
works each artefact through `/forge <state> [slug]`, where `<state>`
is the name of its definition.

## Overview

| Artefact | File | Template | Prefixes of its items | Command |
|---|---|---|---|---|
| Brief | `00-brief.md` or `00-brief-<name>.md` | `templates/brief.md` | none | `/forge brief` |
| Intent | `10-intent.md` | `templates/intent.md` | POS, FCT, REJ, THR | `/forge intent` |
| Assignment | `20-assignment.md` | `templates/assignment.md` | REQ, OOS, CON, ASM, DEL, TBC, SCR | `/forge assignment` |
| BRD | `30-brd.md` | `templates/brd.md` | BR, UC, DEP, NFR, OOS, ASM, TBC, SCR | `/forge brd` |
| Solution design | `40-solution-design.md` | `templates/solution-design.md` | SOL, TBC | `/forge solution-design` |

The directory `.claude/skills/forge/states/` is the one list of the
artefacts: a definition there is an artefact, and no other list
exists. A layer a project does not have is not missing: `/forge` and
the checks say nothing of it.

## Brief

- **File:** `00-brief.md`, or `00-brief-<name>.md` for a later whole
  of thinking born during the project's life.
- **Description:** Compose or finish a brief. The principal's idea
  put together, found with Claude or handed over, approved when done.
- **Template:** `templates/brief.md`: a YAML header, then free form.
- **Inputs:**
  - the principal's thought, however it arrives
  - research notes in `research/`
  - sources in `sources/`
  - Claude's own proposals
  - the existing intent and the ledger, read only to know what
    already stands, never to shape the text
- **Prefixes:** none. A brief carries no IDs and none of the
  conventions of the chain.
- **Command:** `/forge brief [slug]`.

## Intent

- **File:** `10-intent.md`, with the project's threads in
  `threads/`, one file each.
- **Description:** Iterate `10-intent.md`. The briefs chiselled into
  what the principal holds.
- **Template:** `templates/intent.md`.
- **Inputs:**
  - the briefs the principal says to mine (`00-brief.md` and any
    `00-brief-<name>.md`, approved or not)
  - `decisions.md`
  - the ledger
  - sources, only as the principal directs
  - the intent as it stands, read with `threads/`
- **Prefixes:**
  - POS: a position the principal currently holds
  - FCT: a fact
  - REJ: a rejected direction, with the reason it was dropped
  - THR: an open thread, one file in `threads/`
- **Command:** `/forge intent [slug]`.

## Assignment

- **File:** `20-assignment.md`.
- **Description:** Iterate `20-assignment.md`. The intent's in-scope
  substance carried to the recipients in a joint pass.
- **Template:** `templates/assignment.md`.
- **Inputs:**
  - `10-intent.md`, read with `threads/`
  - `decisions.md`
  - the ledger
- **Prefixes:**
  - REQ: requirement
  - OOS: out of scope, or a do-not
  - CON: constraint
  - ASM: assumption
  - DEL: deliverable, which may delegate work
  - TBC: open question, with an owner
  - SCR: success criterion, optional or delegated
- **Command:** `/forge assignment [slug]`.

## BRD

- **File:** `30-brd.md`. A BRD made from a file the principal puts in
  is a work product in `work/`, not this file.
- **Description:** Iterate `30-brd.md`. The business requirements:
  the assignment, the intent or a source put in, broken into rules,
  behaviour and qualities the stakeholders can review and the
  delivery can estimate.
- **Template:** `templates/brd.md`.
- **Inputs:** one parent, named by the principal when he asks for the
  BRD:
  - `20-assignment.md`, read with `10-intent.md` and `threads/`; or
  - `10-intent.md` with `threads/`, where the project has no
    assignment; or
  - a file the principal puts in, registered through `/ingest`, which
    yields a draft in `work/`.

  Around the parent:
  - `decisions.md`
  - the ledger
  - the DEL items of an assignment, as the list of what the BRD is
    asked to bring back
  - the instance's roster of areas, a library document cited by path;
    a project with no enterprise around it has none and says
    `Roster: none`
  - the indexes of the project's resources and of every library it
    depends on (`sources/00-INDEX.md`, `research/00-INDEX.md`,
    `projects/lib-*/sources/00-INDEX.md`)
  - sources and research, as the principal directs
- **Prefixes:**
  - BR: business requirement
  - UC: use case
  - DEP: dependency
  - NFR: non-functional requirement
  - OOS: out of scope
  - ASM: assumption
  - TBC: open question, with an owner
  - SCR: success criterion

  BR, UC, DEP and NFR are the BRD's own.
- **Command:** `/forge brd [slug]`.

What the BRD holds is on [The BRD](../about/the-brd.md).

## Solution design

- **File:** `40-solution-design.md`.
- **Description:** Iterate `40-solution-design.md`. How the things
  wanted are realised, part by part, with the choices they rest on.
- **Template:** `templates/solution-design.md`.
- **Inputs:**
  - the lowest layer the project has above it: the intent alone, the
    assignment or the BRD, and whatever stands above that
  - `decisions.md`
  - the ledger
  - the intent, read with `threads/`
  - what realises the thing, read as it stands, where the thing
    already exists
  - research and sources, as the principal directs
- **Prefixes:**
  - SOL: a part of the solution
  - TBC: open question, with an owner
- **Command:** `/forge solution-design [slug]`.

## See also

- [The document chain](../about/the-document-chain.md): why the listing of that directory is the one list.
- [The BRD](../about/the-brd.md): what the BRD holds and why.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.1 from the files the front-matter names; never edited by hand.
