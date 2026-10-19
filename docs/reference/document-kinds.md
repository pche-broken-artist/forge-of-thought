---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: eaaef90e88b21bcb
inputs:
  - CLAUDE.md#Document kinds
---

# Document kinds

This page lists the kinds a document of the forge can have: what each kind is, who writes it, whether it is versioned and how it behaves. It is for the user, the extender and the evaluator who need the table at hand. Every file of a project is a document and has exactly one kind. "Artefact" is the word for the documents of the chain only. The principal is the person whose thinking is being forged.

## The table

| Group | Kind | Meaning | Written by | Versioned | Behaviour |
|---|---|---|---|---|---|
| artefacts | artefact | a document of the chain; what each is, its definition says | the principal with Claude | yes | rewritten freely |
| records | history | what changed in a versioned document, and why | forge | none | append-only |
| records | decisions | the principal's decisions with reasons | forge | none | append-only |
| records | review, challenge | one dated reviewer run | reviewer agent | none | immutable |
| state | ledger | single source of truth for state, made at read time | script | none | never in git |
| state | project | the project file: slug, kind, language | /new-project | none | written once |
| state | thread | one open matter of the intent | the principal with Claude | none | freely rewritten while open, immutable once closed |
| state | index | catalogue of a resource directory | forge | none | freely rewritten |
| state | map | the documentation map: one entry per page, everything a page is made from | generated | none | freely rewritten by the documentation run |
| rendering | recipe | how a render is made | Claude, principal iterates | yes | iterated, never approved |
| rendering | render | audience-specific output, never a source of truth | generated | none | overwritten by /render |
| rendering | page | a page of the documentation, or its index; never a source of truth | generated | none | overwritten by the documentation run |
| work | work | an output of the project made with work of its own: the file holds the content, the specification beside it the way and the why | Claude, the principal judges | yes, the specification | the file remade from the specification; the principal works with it freely |
| resources | source | external input as it arrived | external, /ingest | none | immutable |
| resources | research | durable answer to one question | Claude, /research | none | immutable |

## The companion

Every versioned kind keeps its history in a companion file beside it, not in its own body.

## A library

A functional binary, such as a `.potx` template or a graphic, is a source. A library's assets are therefore resources without a kind of their own. A library carries no artefacts and no records, except the history companion of its recipe.

## Wrapping

Prose in every document is hard-wrapped at about 72 columns so that git diffs stay legible. Tables, code blocks and front-matter are never wrapped.

## See also

- [Documents and records](../about/documents-and-records.md): why the kinds exist.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
