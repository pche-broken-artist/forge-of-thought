---
generated: 2026-10-09
made: mirrored
inputs-hash: 1412cb140e8f21b2
inputs:
  - .claude/skills/forge/states/brief.md
  - .claude/skills/forge/states/intent.md
  - .claude/skills/forge/states/assignment.md
  - .claude/skills/forge/states/solution-design.md
  - CLAUDE.md
---

# Artefacts

This page lists the artefacts of the chain, one row for each definition
in `.claude/skills/forge/states/`, in the order of the file numbers. It
is for the user who wants to know which file a command works, for the
extender who adds a layer, and for the evaluator who wants the whole
set at a glance.

| Artefact file | Description | Template | Inputs | Item prefixes | Command |
|---|---|---|---|---|---|
| `00-brief.md`, or `00-brief-<name>.md` for a later whole | Compose or finish a brief: the principal's idea put together, found with Claude or handed over, approved when done | `templates/brief.md` | The principal's thought; research notes (`research/`), sources (`sources/`) and Claude's proposals gathered along the way; the existing intent and ledger, read only to know what already stands | none: a brief carries no IDs | `/forge brief` |
| `10-intent.md` | Iterate `10-intent.md`: the briefs chiselled into what the principal holds | `templates/intent.md` | The briefs the principal says to mine (approved or not), `decisions.md`, the ledger; sources only as the principal directs; the intent as it stands, read with the project's threads in `threads.md` | `POS`, `FCT`, `REJ` in the intent; `THR` in `threads.md` | `/forge intent` |
| `20-assignment.md` | Iterate `20-assignment.md`: the intent's in-scope substance carried to the recipients in a joint pass | `templates/assignment.md` | `10-intent.md`, `decisions.md`, the ledger; the intent read with the project's threads, `threads.md` | `REQ`, `OOS`, `CON`, `ASM`, `DEL`, `TBC`, `SCR` | `/forge assignment` |
| `40-solution-design.md` | Iterate `40-solution-design.md`: how the things wanted are realised, part by part, with the choices they rest on | `templates/solution-design.md` | The lowest layer the project has above it (the intent alone, the assignment or the BRD) and whatever stands above that; `decisions.md`, the ledger; the intent read with the project's threads; what realises the thing, read as it stands where it already exists; research and sources as the principal directs | `SOL`, `TBC` | `/forge solution-design` |

Each artefact also keeps a history companion, `<file>.history.md`,
beside it.

A layer a project does not have is not missing.

## See also

- [About the document chain](../about/the-document-chain.md): why the listing of that directory is the one list.
