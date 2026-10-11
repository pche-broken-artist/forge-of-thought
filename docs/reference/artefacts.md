---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 8abff7b34e76cd67
inputs:
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/solution-design.md
  - CLAUDE.md#ID scheme
  - CLAUDE.md#Ledger
---

# Artefacts

This page lists the artefacts of the chain as it stands today, one row per definition, with the file each is kept in, its template, what it is made from, the prefixes of its items and the command that works it. It is for anyone who wants to see at a glance which documents a project can carry. An artefact is a document of the chain (a versioned document the principal forms with Claude); a definition is the state file in `.claude/skills/forge/states/` that says what the artefact is and how it is found.

The rows follow the order of the file numbers. The listing of that directory is the one list of artefacts.

## The artefacts

| Artefact file | What it is | Template | Inputs | Prefixes of its items | Command |
|---|---|---|---|---|---|
| `00-brief.md`, or `00-brief-<name>.md` for a later whole of thinking | Compose or finish a brief: the principal's idea put together, found with Claude or handed over, approved when done | `templates/brief.md` | The principal's thought, however it arrives. Around it, gathered during the elicitation: research notes (`research/`), sources (`sources/`) and Claude's own proposals. The existing intent and ledger are read only to know what already stands, never to shape the text. | None. A brief has no IDs and no conventions of the chain. | `/forge brief [slug]` |
| `10-intent.md` | Iterate the intent: the briefs chiselled into what the principal holds | `templates/intent.md` | The briefs the principal says to mine (`00-brief.md` and any `00-brief-<name>.md`, approved or not), `decisions.md` and the ledger. Sources only as the principal directs. The intent as it stands is read with the project's threads, `threads.md`. | POS (position), FCT (fact), REJ (rejected direction). THR (open thread) lives in the project's `threads.md`. | `/forge intent [slug]` |
| `20-assignment.md` | Iterate the assignment: the intent's in-scope substance carried to the recipients in a joint pass | `templates/assignment.md` | `10-intent.md`, `decisions.md` and the ledger. The intent is read with the project's threads, `threads.md`. | REQ (requirement), OOS (out of scope or do-not), CON (constraint), ASM (assumption), DEL (deliverable), TBC (open question), SCR (success criterion) | `/forge assignment [slug]` |
| `40-solution-design.md` | Iterate the solution design: how the things wanted are realised, part by part, with the choices they rest on | `templates/solution-design.md` | The lowest layer the project has above it, the intent alone, the assignment or the BRD, and whatever stands above that. Also `decisions.md` and the ledger. The intent is read with the project's threads, `threads.md`. Where the thing already exists, what realises it is read as it stands. Research and sources as the principal directs. | SOL (part of the solution), TBC (open question) | `/forge solution-design [slug]` |

The meaning of each prefix, and where it lives, is set by the ID scheme: REQ is a requirement, OOS an out-of-scope or do-not item, CON a constraint that is a deliberate boundary and not to be challenged, ASM an assumption, DEL a deliverable that may delegate work, TBC an open question with an owner, SOL a part of the solution with the choice it rests on, SCR a success criterion that is optional or delegated, POS a position the principal currently holds, THR an open thread, REJ a rejected direction with its reason, and FCT a fact.

The numbers of the files leave gaps of ten, so that a layer can be added without renaming anything.

A layer that a project does not have is not missing. The ledger and the checks say nothing of it.

## See also

- [The document chain](../about/the-document-chain.md): why the listing of that directory is the one list.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
