---
generated: 2026-11-01
version: 6.8
made: mirrored
inputs-hash: 03aa40e76c5e6421
inputs:
  - CLAUDE.md#Document kinds
---

# Document kinds

The document kinds are the table that says, for every file of a project, what it is, who writes it, whether it is versioned and how it behaves. This page is for the user, the extender and the evaluator who need the table and its rules in one place. The principal is whoever's thinking is being forged.

"Document" is the word for every file of a project. "Artefact" is reserved for the documents of the chain. Every document has one kind.

## The table

In the Versioned column, a hyphen means the kind is not versioned.

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
| rendering | recipe | how a render is made | Claude, principal iterates | yes | iterated; an integer only on the principal's word, his own mark, not an approval |
| rendering | render | audience-specific output, never a source of truth | generated | - | overwritten by /render |
| rendering | page | a page of the documentation, or its index; never a source of truth | generated | - | overwritten by the documentation run |
| work | work | an output of the project made with work of its own: the file holds the content, the specification beside it the way and the why | Claude, the principal judges | yes, the specification | the file remade from the specification; the principal works with it freely |
| resources | source | external input as it arrived | external, /ingest | - | immutable |
| resources | research | durable answer to one question; a research of several questions is a bundle with the plan and the synthesis at its head and one note per question per engine | Claude, /research | - | immutable |

## The companion of a versioned kind

- Every versioned kind keeps its history in a companion beside it: the artefact, the recipe and the specification of a work product.
- The companion is a file named `<file>.history.md`.
- The body of the document is the current state. The companion is the record.

## A library's reduced set

A library carries no artefacts and no records. The one record it has is the history companion of its recipe.

A functional binary, such as a `.potx` template or a graphic, is a source. A library's assets are therefore resources without a kind of their own.

## Files that have no kind

The forge reads none of these as a document:

- a file of `tmp/`
- the player page of `docs/videos/`
- the principal's own file in `renders/` or `published/`

## The wrapping rule

Prose in every document is hard-wrapped at about 72 columns, so that git diffs stay legible. Tables, code blocks and front-matter are never wrapped.

## See also

- [Documents and records](../about/documents-and-records.md): why the kinds exist.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
