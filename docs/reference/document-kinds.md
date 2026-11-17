---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: f819898819b7c470
inputs:
  - CLAUDE.md#Document kinds
---

# Document kinds

This page is the table of the kinds a document of the forge can have,
with the files that have no kind and the rule that wraps prose. It is
for the user, the extender and the evaluator who need to know what a
file is, who writes it and how it behaves. In the table, the
principal is the person whose thinking is being forged, and Claude is
the machine that works with the principal.

## The kinds

Every document has one kind. The kind says what the document is, who
writes it, whether it is versioned and how it behaves. "Document" is
the word for every file of a project. "Artefact" is reserved for the
documents of the chain. A dash in a cell of the Versioned column,
shown as `—`, means the kind is not versioned.

| Group | Kind | Meaning | Written by | Versioned | Behaviour |
|---|---|---|---|---|---|
| artefacts | artefact | a document of the chain; what each is, its definition says | the principal with Claude | yes | rewritten freely |
| records | history | what changed in a versioned document, and why | forge | `—` | append-only |
| records | decisions | the principal's decisions with reasons | forge | `—` | append-only |
| records | review, challenge | one dated reviewer run | reviewer agent | `—` | immutable |
| state | ledger | single source of truth for state, made at read time | script | `—` | never in git |
| state | project | the project file: slug, kind, language | /new-project | `—` | written once |
| state | thread | one matter of a project set aside to be taken up later | the principal with Claude | `—` | freely rewritten while open, immutable once closed |
| state | index | catalogue of a resource directory | forge | `—` | freely rewritten |
| state | map | the documentation map: one entry per page, everything a page is made from | generated | `—` | freely rewritten by the documentation run |
| rendering | recipe | how a render is made | Claude, principal iterates | yes | iterated; an integer only on the principal's word, his own mark, not an approval |
| rendering | render | audience-specific output, never a source of truth | generated | `—` | overwritten by /render |
| rendering | page | a page of the documentation, or its index; never a source of truth | generated | `—` | overwritten by the documentation run |
| work | work | an output of the project made with work of its own: the file holds the content, the specification beside it the way and the why | Claude, the principal judges | yes, the specification | the file remade from the specification; the principal works with it freely |
| resources | source | external input as it arrived | external, /ingest | `—` | immutable |
| resources | research | durable answer to one question; a research of several questions is a bundle with the plan and the synthesis at its head and one note per question per engine | Claude, /research | `—` | immutable |

## Files that have no kind

The forge reads none of these as a document.

- A file of `tmp/`.
- The player page of `docs/videos/`.
- The principal's own file in `renders/` or `published/`.

## The wrapping rule

Prose in every document is hard-wrapped at about 72 columns so that
git diffs stay legible. Tables, code blocks and front-matter are never
wrapped.

## See also

- [Documents and records](../about/documents-and-records.md): why the kinds exist.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
