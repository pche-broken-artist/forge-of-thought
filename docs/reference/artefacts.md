---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 227c43c06a588ec7
inputs:
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/solution-design.md
  - CLAUDE.md#ID scheme
  - CLAUDE.md#Ledger
---

# Artefacts

This page lists the artefacts of today's chain, one row per definition: the file each one is, what it is for, the template that shapes it, what it is made from, the prefixes of its items and the command that works it. The list is the content of the directory `.claude/skills/forge/states/`, one definition per artefact, in the order of the file numbers. A reader who wants to know which documents a project can carry finds them here. The principal is whoever's thinking is being forged.

## Overview

| Artefact | File | Description | Template | Command |
|---|---|---|---|---|
| Brief | `00-brief.md` or `00-brief-<name>.md` | "Compose or finish a brief: the principal's idea put together, found with Claude or handed over, approved when done" | `templates/brief.md` | `/forge brief` |
| Intent | `10-intent.md` | "Iterate 10-intent.md: the briefs chiselled into what the principal holds" | `templates/intent.md` | `/forge intent` |
| Assignment | `20-assignment.md` | "Iterate 20-assignment.md: the intent's in-scope substance carried to the recipients in a joint pass" | `templates/assignment.md` | `/forge assignment` |
| Solution design | `40-solution-design.md` | "Iterate 40-solution-design.md: how the things wanted are realised, part by part, with the choices they rest on" | `templates/solution-design.md` | `/forge solution-design` |

## Inputs and prefixes

### Brief

- File: `00-brief.md` (bare), or `00-brief-<name>.md` for a later whole of thinking born during the project's life.
- Inputs: the principal's thought, however it arrives. Around it, gathered during the elicitation: research notes (`research/`), sources (`sources/`) and Claude's own proposals. The existing intent and ledger are read only to know what already stands, never to shape the text.
- Prefixes: none. A brief has a YAML header, then free form, with no IDs.
- Command: `/forge brief [slug]`.

### Intent

- File: `10-intent.md`, with the project's threads in `threads.md`.
- Inputs: the briefs the principal says to mine (`00-brief.md` and any `00-brief-<name>.md`, approved or not), `decisions.md` and the ledger. Sources are read only as the principal directs. The intent as it stands is read with `threads.md`.
- Prefixes:

| Prefix | Meaning |
|---|---|
| POS | position the principal currently holds |
| FCT | fact: what is the case, as the principal states it or as a source states it |
| REJ | rejected direction, with the reason it was dropped |
| THR | open thread, in `threads.md`; names the artefact it concerns |

- Command: `/forge intent [slug]`.

### Assignment

- File: `20-assignment.md`.
- Inputs: `10-intent.md`, `decisions.md` and the ledger. The intent is read with the project's threads, `threads.md`.
- Prefixes:

| Prefix | Meaning |
|---|---|
| REQ | requirement |
| OOS | out of scope or do-not |
| CON | constraint: deliberate boundary, not to be challenged |
| ASM | assumption |
| DEL | deliverable, which may delegate work |
| TBC | open question or to be confirmed, with owner |
| SCR | success criterion, optional or delegated |

- Command: `/forge assignment [slug]`.

### Solution design

- File: `40-solution-design.md`.
- Inputs: the lowest layer the project has above it (the intent alone, the assignment or the BRD, and whatever stands above that), `decisions.md` and the ledger. The intent is read with the project's threads, `threads.md`. Where the thing already exists, what realises it is read as it stands. Research and sources as the principal directs.
- Prefixes:

| Prefix | Meaning |
|---|---|
| SOL | part of the solution: what is built or done, what it realises, the choice it rests on |
| TBC | open question or to be confirmed, with owner |

- Command: `/forge solution-design [slug]`.

A layer below the intent that a project does not have is not missing: the state map and the checks say nothing of it.

## See also

- [The document chain](../about/the-document-chain.md): why the listing of that directory is the one list.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
