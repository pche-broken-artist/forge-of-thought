---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 4725da43c48b18fa
inputs:
  - CLAUDE.md#Document kinds
---

# Document kinds

This page is the table of the kinds a document of the forge can have, for the user, the extender and the evaluator. Every file of a project is a document, and every document has exactly one kind. The kind says what the document is, who writes it, whether it is versioned and how it behaves. A short explanation of why the kinds exist is on [Documents and records](../about/documents-and-records.md); the terms used here are in the [Glossary](glossary.md).

## The words

- "Document" is the word for every file of a project.
- "Artefact" is reserved for the documents of the chain.

## The table

In the column "Versioned", "no" stands where the owner has no version for the kind.

| Group | Kind | Meaning | Written by | Versioned | Behaviour |
|---|---|---|---|---|---|
| artefacts | artefact | a document of the chain; what each is, its definition says | the principal with Claude | yes | rewritten freely |
| records | history | what changed in a versioned document, and why | forge | no | append-only |
| records | decisions | the principal's decisions with reasons | forge | no | append-only |
| records | review, challenge | one dated reviewer run | reviewer agent | no | immutable |
| state | ledger | single source of truth for state, made at read time | script | no | never in git |
| state | project | the project file: slug, kind, language | /new-project | no | written once |
| state | thread | one open matter of the intent | the principal with Claude | no | freely rewritten while open, immutable once closed |
| state | index | catalogue of a resource directory | forge | no | freely rewritten |
| state | map | the documentation map: one entry per page, everything a page is made from | generated | no | freely rewritten by the documentation run |
| rendering | recipe | how a render is made | Claude, principal iterates | yes | iterated, never approved |
| rendering | render | audience-specific output, never a source of truth | generated | no | overwritten by /render |
| rendering | page | a page of the documentation, or its index; never a source of truth | generated | no | overwritten by the documentation run |
| work | work | an output of the project made with work of its own: the file holds the content, the specification beside it the way and the why | Claude, the principal judges | yes, the specification | the file remade from the specification; the principal works with it freely |
| resources | source | external input as it arrived | external, /ingest | no | immutable |
| resources | research | durable answer to one question; a research of several questions is a bundle with the plan and the synthesis at its head and one note per question per engine | Claude, /research | no | immutable |

## The companion of a versioned kind

Every versioned kind keeps its history in a companion beside it, never in its body. The companion is a file named `<file>.history.md`. The body is the current state; the companion is the record.

## A library's reduced set

A library carries no artefacts and no records but its recipe's history companion.

## A functional binary

A functional binary, such as a `.potx` template or a graphic, is a source. A library's assets are therefore resources without a kind of their own.

## The wrapping rule

Prose in every document is hard-wrapped at about 72 columns, so that git diffs stay legible. Tables, code blocks and front-matter are never wrapped.

## See also

- [Documents and records](../about/documents-and-records.md): why the kinds exist.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
