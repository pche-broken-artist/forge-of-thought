---
project: <slug>
purpose: Slide-by-slide source material for <the presentation>
audience: <audience>
version: 0.1
updated: YYYY-MM-DD
# output: <path>   # optional — overrides the default renders/<recipe>.md
---

# Recipe — <presentation name>

<!-- Presentation-genre recipe, composed via /recipe presentation.
A recipe is the iterated thing; its render is generated output. Never
polish a render by hand: change the recipe, run /render <recipe>. The
render is a slide-by-slide deck definition; scripts/md2pptx.ps1 turns
it into an actual PowerPoint file. Recipes are tools: bare version +
updated date in front-matter, no status, no Version History — history
lives in git. -->

## Inputs
<!-- Chain artefacts the deck is generated from. A picture may come
from another render of this project: declare that render here too, so
provenance and staleness track it. -->
- 10-intent.md

## Instructions
- The render is **source material for building a presentation**, not
  the presentation itself: one section per slide, carrying the exact
  on-slide text <and the speaker notes>. Slide count ~<N>; follow the
  Template's slide list.
- Audience: <audience>. Register: <register>. Language: <English>.
- The one message: <what the audience must take away>. Centre of
  gravity: <where the deck dwells>.
- Content comes from the Inputs only — no invention, no softening.
  <Speaker notes cite the underlying <POS/REQ> IDs so a slide can be
  traced back and checked when the input moves.>
- On-slide density: at most <N> bullets per slide, <N> words per
  bullet; everything beyond that belongs to the notes.
- Vocabulary discipline: <terms that must not blur>.
- Must not appear: <what this audience must not see>.
- Diagrams sit on the slides the Template assigns them to, in one of
  two forms: an inline Mermaid block — valid standalone, simple
  enough to survive conversion into native slide shapes — or a
  reference `render: <file>` to a render of this project declared in
  Inputs.
- Copy the Build instructions section verbatim into the render,
  immediately after the front-matter.
- Per-slide format:
  ```
  ## SNN — <slide title>
  **On slide:** <title line and bullets exactly as they should appear>
  **Diagram:** <mermaid block | render: <file> — only where the
  Template assigns one>
  **Speaker notes:** <what the presenter says>
  ```

## Build instructions
<!-- For the LLM that converts the render into a .pptx via
scripts/md2pptx.ps1. Copied verbatim into the render. -->
- Template: <path to a .potx, e.g. projects/lib-<name>/sources/<file>.potx | none — design freely>.
- Model: <recommended md2pptx -Model value; default opus>.
- <Overflow handling, diagram redraw expectations, visual accents —
  anything else the builder must know.>

## Template
Front-matter provenance per the render convention, then the Build
instructions, then one section per slide:

| # | Slide | Content | Diagram |
|---|---|---|---|
| S01 | <title & frame> | <content, with source IDs> | — |
| S02 | <slide> | <content, with source IDs> | <diagram subject \| render: <file>> |
| S<NN> | <closing> | <content> | — |
