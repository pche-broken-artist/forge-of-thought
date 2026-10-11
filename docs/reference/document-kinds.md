---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 4385c7b1bf1aaa15
inputs:
  - CLAUDE.md#Document kinds
---

# Document kinds

This page is the table of the kinds a document of the forge can
have, for the user, the extender and the evaluator. Every document
has one kind, and the kind says what it is, who writes it, whether
it is versioned and how it behaves. "Document" is the word for every
file of a project; "artefact" is reserved for the documents of the
chain.

## The table

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

The principal is the person whose thinking is being forged.

## Rules beside the table

- Companion: every versioned kind keeps its history in a companion
  file beside it.
- Library: a library carries no artefacts and no records except its
  recipe's history companion, and a functional binary (such as a
  `.potx` template or a graphic) is a source, so a library's assets
  are resources without a kind of their own.
- Wrapping: prose in every document is hard-wrapped at about 72
  columns so that git diffs stay legible; tables, code blocks and
  front-matter are never wrapped.

## See also

- [Documents and records](../about/documents-and-records.md): why the kinds exist.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
