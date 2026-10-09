---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/solution-design.md
  - CLAUDE.md
---

# Artefacts

This page lists the artefacts of the chain, one row for each
definition in `.claude/skills/forge/states/`, in the order of the
file numbers. It is for the person who works an artefact, the person
who extends the forge with a new one, and the person who wants to see
what the chain holds.

| Artefact file | Description | Template | Inputs | Prefixes of its items | Command |
|---|---|---|---|---|---|
| `00-brief.md`, or `00-brief-<name>.md` for a later whole of thinking | Compose or finish a brief - the principal's idea put together, found with Claude or handed over, approved when done | `templates/brief.md` | The principal's thought, however it arrives; research notes (`research/`), sources (`sources/`) and Claude's own proposals gathered during the elicitation. The existing intent and ledger are read only to know what already stands | none; a brief carries no IDs | `/forge brief` |
| `10-intent.md` | Iterate 10-intent.md - the briefs chiselled into what the principal holds | `templates/intent.md` | The briefs the principal says to mine (`00-brief.md` and any `00-brief-<name>.md`, approved or not), `decisions.md`, the ledger; sources only as the principal directs. The intent as it stands is read with the project's threads, `threads.md` | POS, FCT, REJ; THR for the threads, which live in `threads.md` | `/forge intent` |
| `20-assignment.md` | Iterate 20-assignment.md - the intent's in-scope substance carried to the recipients in a joint pass | `templates/assignment.md` | `10-intent.md`, `decisions.md`, the ledger. The intent is read with the project's threads, `threads.md` | REQ, OOS, CON, ASM, DEL, TBC, SCR | `/forge assignment` |
| `40-solution-design.md` | Iterate 40-solution-design.md: how the things wanted are realised, part by part, with the choices they rest on | `templates/solution-design.md` | The lowest layer the project has above it (the intent alone, the assignment or the BRD, and whatever stands above that); `decisions.md`, the ledger. The intent is read with the project's threads, `threads.md`. Where the thing already exists, what realises it is read as it stands. Research and sources as the principal directs | SOL, TBC | `/forge solution-design` |

A layer a project does not have is not missing.

## See also

- [About the document chain](../about/the-document-chain.md) - why the listing of that directory is the one list.
