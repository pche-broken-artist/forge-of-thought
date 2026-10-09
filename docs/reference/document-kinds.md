---
generated: 2026-10-09
made: mirrored
inputs:
  - CLAUDE.md
---

# Document kinds

This page lists the kinds of document the forge knows, for anyone who
uses, extends or evaluates it. Every document has exactly one kind,
and the kind says what the document is, who writes it, whether it is
versioned and how it behaves.

"Document" is the word for every file of a project; "artefact" is
reserved for the documents of the chain.

| Group | Kind | Meaning | Written by | Versioned | Behaviour |
|---|---|---|---|---|---|
| artefacts | artefact | a document of the chain; what each is, its definition says | the principal with Claude | yes | rewritten freely |
| records | history | what changed in a versioned document, and why | forge | - | append-only |
| records | decisions | the principal's decisions with reasons | forge | - | append-only |
| records | review, challenge | one dated reviewer run | reviewer agent | - | immutable |
| state | ledger | single source of truth for state | forge | - | freely rewritten |
| state | index | catalogue of a resource directory | forge | - | freely rewritten |
| rendering | recipe | how a render is made | Claude, principal iterates | yes | iterated, never approved |
| rendering | render | audience-specific output, never a source of truth | generated | - | overwritten by /render |
| resources | source | external input as it arrived | external, /ingest | - | immutable |
| resources | research | durable answer to one question | Claude, /research | - | immutable |

## Companions of versioned kinds

- Every versioned kind (artefact and recipe) keeps its history in a
  companion `<file>.history.md` beside it.

## A library's reduced set

- A library carries no artefacts and no records but its recipe's
  history companion. A functional binary such as a `.potx` template
  or a graphic is a source, so a library's assets are resources
  without a kind of their own.

## Wrapping

- Prose in every document is hard-wrapped at about 72 columns so that
  git diffs stay legible; tables, code blocks and front-matter are
  never wrapped.

## See also

- [About documents and records](../about/documents-and-records.md): why the kinds exist.
