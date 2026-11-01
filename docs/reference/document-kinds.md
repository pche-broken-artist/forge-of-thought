---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: 550b42e0a2fdb8c4
inputs:
  - CLAUDE.md#Document kinds
---

# Document kinds

This page lists the kinds of document the forge knows, for the user, the extender and the evaluator. Every file of a project is a document, and every document has exactly one kind. The kind says what the document is, who writes it, whether it is versioned and how it behaves.

"Artefact" is reserved for the documents of the chain. Every other file is a document of another kind.

## The table

| Group | Kind | Meaning | Written by | Versioned | Behaviour |
|---|---|---|---|---|---|
| artefacts | artefact | a document of the chain; what each is, its definition says | the principal with Claude | yes | rewritten freely |
| records | history | what changed in a versioned document, and why | forge | - | append-only |
| records | decisions | the principal's decisions with reasons | forge | - | append-only |
| records | review, challenge | one dated reviewer run | reviewer agent | - | immutable |
| state | ledger | single source of truth for state, made at read time | script | - | never in git |
| state | project | the project file: slug, kind, language | /new-project | - | written once |
| state | thread | one open matter of the intent | the principal with Claude | - | freely rewritten while open, immutable once closed |
| state | index | catalogue of a resource directory | forge | - | freely rewritten |
| state | map | the documentation map: one entry per page, everything a page is made from | generated | - | freely rewritten by the documentation run |
| rendering | recipe | how a render is made | Claude, principal iterates | yes | iterated, never approved |
| rendering | render | audience-specific output, never a source of truth | generated | - | overwritten by /render |
| rendering | page | a page of the documentation, or its index; never a source of truth | generated | - | overwritten by the documentation run |
| work | work | an output of the project made with work of its own: the file holds the content, the specification beside it the way and the why | Claude, the principal judges | yes, the specification | the file remade from the specification; the principal works with it freely |
| resources | source | external input as it arrived | external, /ingest | - | immutable |
| resources | research | durable answer to one question; a research of several questions is a bundle with the plan and the synthesis at its head and one note per question per engine | Claude, /research | - | immutable |

A hyphen in the Versioned column means the kind is not versioned.

## The companion

Every versioned kind keeps its history in a companion file beside it. The companion is the history of that document.

## A library

A functional binary, such as a `.potx` template or a graphic, is a source. A library's assets are therefore resources without a kind of their own. A library carries no artefacts and no records, except the history companion of its recipe.

## The wrapping rule

Prose in every document is hard-wrapped at about 72 columns so that git diffs stay legible. Tables, code blocks and front-matter are never wrapped.

## See also

- [Documents and records](../about/documents-and-records.md): why the kinds exist.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
