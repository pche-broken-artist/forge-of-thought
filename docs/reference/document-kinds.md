---
generated: 2026-10-10
made: mirrored
inputs-hash: 729914386c00049a
inputs:
  - CLAUDE.md
---

# Document kinds

This page lists the kinds a document can have in a Forge of Thought
project, for anyone who needs to know what a file is, who writes it
and how it behaves. "Document" is the word for every file of a
project; "artefact" is reserved for the documents of the chain. Every
document has one kind.

## The kinds

| Group | Kind | Meaning | Written by | Versioned | Behaviour |
|---|---|---|---|---|---|
| artefacts | artefact | a document of the chain; what each is, its definition says | the principal with Claude | yes | rewritten freely |
| records | history | what changed in a versioned document, and why | forge | - | append-only |
| records | decisions | the principal's decisions with reasons | forge | - | append-only |
| records | review, challenge | one dated reviewer run | reviewer agent | - | immutable |
| state | ledger | single source of truth for state | forge | - | freely rewritten |
| state | index | catalogue of a resource directory | forge | - | freely rewritten |
| state | map | the documentation map: one entry per page, everything a page is made from | generated | - | freely rewritten by the documentation run |
| rendering | recipe | how a render is made | Claude, principal iterates | yes | iterated, never approved |
| rendering | render | audience-specific output, never a source of truth | generated | - | overwritten by /render |
| rendering | page | a page of the documentation, or its index; never a source of truth | generated | - | overwritten by the documentation run |
| resources | source | external input as it arrived | external, /ingest | - | immutable |
| resources | research | durable answer to one question | Claude, /research | - | immutable |

## Companions, libraries and wrapping

- Every versioned kind keeps its history in a companion file beside it.
- A library carries no artefacts and no records except its recipe's
  history companion; a functional binary such as a template or a
  graphic is a source, so a library's assets are resources without a
  kind of their own.
- Prose in every document is hard-wrapped at about 72 columns so that
  git diffs stay legible; tables, code blocks and front-matter are
  never wrapped.

## See also

- [About documents and records](../about/documents-and-records.md): why the kinds exist.
