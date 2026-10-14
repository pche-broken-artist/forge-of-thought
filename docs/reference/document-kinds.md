---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 4dc3094155998f41
inputs:
  - CLAUDE.md#Document kinds
---

# Document kinds

This page is the table of document kinds: every file of a project has exactly one kind, and the kind says what the file is, who writes it, whether it is versioned and how it behaves. It is for anyone who needs to know what a given file is allowed to do.

"Document" is the word for every file of a project. "Artefact" is reserved for the documents of the chain.

## The table

A cell with a hyphen means the kind is not versioned.

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
| work | work | an output of the project made with work of its own: the file holds the content, the specification beside it the way and the why | Claude, the principal judges | yes, the specification | the file remade from the specification; the principal works with it freely |
| resources | source | external input as it arrived | external, /ingest | - | immutable |
| resources | research | durable answer to one question | Claude, /research | - | immutable |

The principal is the person whose thinking is being forged.

## The companion of a versioned kind

- Every versioned kind keeps its history in a companion beside it.
- The versioned kinds are the artefact, the recipe and the specification of a work product.

## A library's reduced set

- A functional binary, such as a `.potx` template or a graphic, is a source. A library's assets are therefore resources without a kind of their own.
- A library carries no artefacts and no records, except the history companion of its recipe.

## The wrapping rule

- Prose in every document is hard-wrapped at about 72 columns, so that git diffs stay legible.
- Tables, code blocks and front-matter are never wrapped.

## See also

- [Documents and records](../about/documents-and-records.md): why the kinds exist.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
