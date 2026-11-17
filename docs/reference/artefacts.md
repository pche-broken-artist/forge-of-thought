---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 8137f0753a844544
inputs:
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/brd.md
  - .claude/skills/forge/states/user-stories.md
  - .claude/skills/forge/states/solution-design.md
  - .claude/reference/id-prefixes.md
  - .claude/skills/forge/SKILL.md
---

# Artefacts

This page lists the artefacts of today's chain, one entry per
definition, with the file each is written to, its template, its
inputs, the prefixes of its items and the command that works it. It is
for anyone who needs to know which artefacts the forge has and what
each is made from. The list is the listing of the directory
`.claude/skills/forge/states/`, one definition per artefact, in the
order of the file numbers. In the entries, the principal is whoever's
thinking is being forged, and the ledger is the state of a project
that a script builds from its documents when it is read.

## Overview

| Artefact | File | Template | Prefixes of its items | Command |
|---|---|---|---|---|
| Brief | `00-brief.md`, `00-brief-<name>.md` | `templates/brief.md` | none | `/forge brief` |
| Intent | `10-intent.md` | `templates/intent.md` | POS, FCT, THR, REJ | `/forge intent` |
| Assignment | `20-assignment.md` | `templates/assignment.md` | REQ, OOS, CON, ASM, DEL, TBC, SCR | `/forge assignment` |
| BRD | `30-brd.md` | `templates/brd.md` | BR, UC, DEP, NFR, OOS, ASM, TBC, SCR | `/forge brd` |
| User stories | `35-user-stories.md` | `templates/user-stories.md` | US | `/forge user-stories` |
| Solution design | `40-solution-design.md` | `templates/solution-design.md` | SOL, TBC | `/forge solution-design` |

What each prefix means is in [ID scheme](id-scheme.md). Terms of the
forge are in the [Glossary](glossary.md).

## Brief

- **File:** `00-brief.md`, or `00-brief-<name>.md` for a later whole
  of thinking born during the project's life.
- **Description:** `Compose or finish a brief — the principal's idea put together, found with Claude or handed over, approved when done`
- **Template:** `templates/brief.md`.
- **Inputs:** the principal's thought, however it arrives. Around it,
  gathered during the elicitation: research notes (`research/`),
  sources (`sources/`) and Claude's own proposals. The existing intent
  and the ledger are read only to know what already stands.
- **Prefixes of its items:** none. The brief carries no IDs.
- **Command:** `/forge brief`.

## Intent

- **File:** `10-intent.md`.
- **Description:** `Iterate 10-intent.md — the briefs chiselled into what the principal holds`
- **Template:** `templates/intent.md`.
- **Inputs:** the briefs the principal says to mine (`00-brief.md` and
  any `00-brief-<name>.md`, approved or not), `decisions.md` and the
  ledger. Sources enter only as the principal directs. The intent as
  it stands is read with the project's threads, `threads/`.
- **Prefixes of its items:** POS, FCT, THR, REJ.
- **Command:** `/forge intent`.

## Assignment

- **File:** `20-assignment.md`.
- **Description:** `Iterate 20-assignment.md — the intent's in-scope substance carried to the recipients in a joint pass`
- **Template:** `templates/assignment.md`.
- **Inputs:** `10-intent.md`, `decisions.md` and the ledger. The
  intent is read with the project's threads, `threads/`.
- **Prefixes of its items:** REQ, OOS, CON, ASM, DEL, TBC, SCR.
- **Command:** `/forge assignment`.

## BRD

- **File:** `30-brd.md`.
- **Description:** `Iterate 30-brd.md — the business requirements: the assignment or the intent broken into rules, behaviour and qualities the stakeholders can review and the delivery can estimate; a source put in yields a draft BRD as a work product`
- **Template:** `templates/brd.md`.
- **Inputs:** one parent, named by the principal when he asks for the
  BRD:
  - `20-assignment.md`, read with `10-intent.md` and `threads/`;
  - `10-intent.md` with `threads/`, where the project has no
    assignment.

  Around the parent: `decisions.md`, the ledger and the DEL items of
  an assignment. Also the roster of the instance, a library document
  that names the areas of the enterprise a BRD must consider and
  which of them are mandatory, cited by path; a project with no
  enterprise around it has no roster and says `Roster: none`. Also the
  group's standard where the instance has one, and the indexes of the
  project's resources and of every library it depends on. Sources and
  research as the principal directs. A file the principal puts in,
  such as a transcript, an offer or a document of someone else, yields
  a draft BRD that is always a work product in `work/`, never
  `30-brd.md`.
- **Prefixes of its items:** BR, UC, DEP, NFR, OOS, ASM, TBC, SCR. BR,
  UC, DEP and NFR are the BRD's own.
- **Command:** `/forge brd`.
- **More:** [The BRD](../about/the-brd.md).

## User stories

- **File:** `35-user-stories.md`.
- **Description:** `Iterate 35-user-stories.md — the requirements broken into stories of behaviour that the stakeholders approve as a whole, the delivery builds from and the testers test from`
- **Template:** `templates/user-stories.md`.
- **Inputs:** one parent, named by the principal when he asks for the
  stories:
  - `30-brd.md`, read with the layers above it;
  - `10-intent.md` with `threads/`, where the change is small, the ask
    precise and without further impact, and the principal says so.

  Around the parent: `decisions.md`, the ledger, and the indexes of
  the project's resources, sources and research as the principal
  directs. A requirements document of someone else, put in through
  `/ingest`, yields stories that are a work product in `work/`, never
  `35-user-stories.md`.
- **Prefixes of its items:** US.
- **Command:** `/forge user-stories`.
- **More:** [The user stories](../about/the-user-stories.md).

## Solution design

- **File:** `40-solution-design.md`.
- **Description:** `Iterate 40-solution-design.md: how the things wanted are realised, part by part, with the choices they rest on`
- **Template:** `templates/solution-design.md`.
- **Inputs:** the lowest layer the project has above it (the intent
  alone, the assignment, the BRD or the user stories) and whatever
  stands above that; `decisions.md` and the ledger. The intent is read
  with the project's threads, `threads/`. Where the thing already
  exists, what realises it is read as it stands. Research and sources
  as the principal directs.
- **Prefixes of its items:** SOL, TBC.
- **Command:** `/forge solution-design`.

A layer a project does not have is not missing. A project takes the
layers it needs, and none is a condition of another. Why the listing
of the definitions is the one list is explained in
[The document chain](../about/the-document-chain.md).

## See also

- [The document chain](../about/the-document-chain.md): why the listing of that directory is the one list.
- [The BRD](../about/the-brd.md): what the BRD holds and why.
- [The user stories](../about/the-user-stories.md): what the stories hold and why.
- [ID scheme](id-scheme.md): the table of prefixes, each with what it means and where its items live.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
