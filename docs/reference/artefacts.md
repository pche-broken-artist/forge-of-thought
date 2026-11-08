---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 5ea8604d2ed74045
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

This page lists the artefacts of today's chain, one row per definition, with the file, the template, the inputs, the prefixes of the items and the command that works each. It is for the user, the extender and the evaluator who need to look up one artefact quickly. An artefact is a document of the chain, and its definition is the state file that says what it is and how it is found. The principal is the person whose thinking is being forged.

The listing of `.claude/skills/forge/states/` is the one list of artefacts. The rows below follow the order of the file numbers.

## Overview

| Artefact | Description | Template | Inputs | Prefixes | Command |
|---|---|---|---|---|---|
| `00-brief.md`, or `00-brief-<name>.md` for a later whole of thinking | Compose or finish a brief - the principal's idea put together, found with Claude or handed over, approved when done | `templates/brief.md` | The principal's thought; research notes, sources and Claude's proposals gathered around it; the existing intent and the ledger, read only to know what already stands | none (no IDs) | `/forge brief [slug]` |
| `10-intent.md` | Iterate 10-intent.md - the briefs chiselled into what the principal holds | `templates/intent.md` | The briefs the principal says to mine (approved or not); `decisions.md`; the ledger; sources only as the principal directs; the project's `threads/` | POS, FCT, THR, REJ | `/forge intent [slug]` |
| `20-assignment.md` | Iterate 20-assignment.md - the intent's in-scope substance carried to the recipients in a joint pass | `templates/assignment.md` | `10-intent.md` with the project's `threads/`; `decisions.md`; the ledger | REQ, OOS, CON, ASM, DEL, TBC, SCR | `/forge assignment [slug]` |
| `30-brd.md` | Iterate 30-brd.md - the business requirements: the assignment or the intent broken into rules, behaviour and qualities the stakeholders can review and the delivery can estimate; a source put in yields a draft BRD as a work product | `templates/brd.md` | One parent named by the principal: `20-assignment.md` (read with the intent and `threads/`), or `10-intent.md` with `threads/` where there is no assignment; a file put in yields a draft in `work/` instead; around the parent: `decisions.md`, the ledger, the DEL items of an assignment, the roster of the areas of the enterprise a BRD must consider (a library document of the instance, cited by path, or `Roster: none`), the group's standard where the instance has one, the indexes of the resources of the project and of its libraries | BR, UC, DEP, NFR, OOS, ASM, TBC, SCR | `/forge brd [slug]` |
| `35-user-stories.md` | Iterate 35-user-stories.md - the requirements broken into stories of behaviour that the stakeholders approve as a whole, the delivery builds from and the testers test from | `templates/user-stories.md` | One parent named by the principal: `30-brd.md` (read with the layers above it), or, for a small change on the principal's word, `10-intent.md` with `threads/`; a requirements document of someone else yields stories in `work/` instead; around the parent: `decisions.md`, the ledger, the indexes of the resources | US | `/forge user-stories [slug]` |
| `40-solution-design.md` | Iterate 40-solution-design.md: how the things wanted are realised, part by part, with the choices they rest on | `templates/solution-design.md` | The lowest layer the project has above it (the intent alone, the assignment, the BRD or the user stories) and whatever stands above that; `decisions.md`; the ledger; the project's `threads/`; research and sources as the principal directs | SOL, TBC | `/forge solution-design [slug]` |

The prefixes are those of the ID scheme: a prefix of two or three letters, then a four-digit number, global and never renumbered. A prefix such as TBC or OOS appears on more than one layer. The ledger is the state of a project made at read time from its documents, and it reads the header of each artefact.

A layer a project does not have is not missing: `/forge` and the checks say nothing of it.

## See also

- [The document chain](../about/the-document-chain.md): why the listing of that directory is the one list.
- [The BRD](../about/the-brd.md): what the BRD holds and why.
- [The user stories](../about/the-user-stories.md): what the stories hold and why.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
