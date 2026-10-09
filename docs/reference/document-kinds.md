---
generated: 2026-10-09
made: mirrored
inputs-hash: ba5c0977c510f4cd
inputs:
  - CLAUDE.md
---

# Document kinds

This page lists the kinds a document of the forge can have, with what
each kind is, who writes it, whether it is versioned and how it
behaves. It is for anyone who needs to look up a kind: a user, an
extender or an evaluator.

"Document" is the word for every file of a project. "Artefact" is
reserved for the documents of the chain: the ones the principal
composes, the reviewers read and the renders are generated from. Every
document has exactly one kind.

## The kinds

| Group | Kind | Meaning | Written by | Versioned | Behaviour |
|---|---|---|---|---|---|
| artefacts | artefact | a document of the chain; what each is, its definition says | the principal with Claude | yes | rewritten freely |
| records | history | what changed in a versioned document, and why | forge | no | append-only |
| records | decisions | the principal's decisions with reasons | forge | no | append-only |
| records | review, challenge | one dated reviewer run | reviewer agent | no | immutable |
| state | ledger | single source of truth for state | forge | no | freely rewritten |
| state | index | catalogue of a resource directory | forge | no | freely rewritten |
| state | map | the documentation map: one entry per page, everything a page is made from | generated | no | freely rewritten by the documentation run |
| rendering | recipe | how a render is made | Claude, principal iterates | yes | iterated, never approved |
| rendering | render | audience-specific output, never a source of truth | generated | no | overwritten by /render |
| rendering | page | a page of the documentation, or its index; never a source of truth | generated | no | overwritten by the documentation run |
| resources | source | external input as it arrived | external, /ingest | no | immutable |
| resources | research | durable answer to one question | Claude, /research | no | immutable |

## Companions, libraries and wrapping

- Every versioned kind keeps its history in a companion file beside it.
- A library carries no artefacts and no records except its recipe's
  history companion; a functional binary, such as a `.potx` template
  or a graphic, is a source, so a library's assets are resources
  without a kind of their own.
- Prose in every document is hard-wrapped at about 72 columns; tables,
  code blocks and front-matter are never wrapped.

## See also

- [About documents and records](../about/documents-and-records.md): why the kinds exist.
