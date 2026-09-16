---
description: Compose a presentation recipe — a slide-by-slide deck definition, convertible to pptx by scripts/md2pptx.ps1
---

Genre: presentation. Skeleton: `templates/recipe-presentation.md`.

The product is a recipe whose render is a slide-by-slide Markdown deck
definition — source material for a presentation, never the
presentation itself. The render is convertible into an actual
PowerPoint file by `scripts/md2pptx.ps1`, which hands it to an LLM:
the definition therefore carries its own Build instructions.

Role: interviewer. Elicit the answers below from the principal —
options and trade-offs offered, decisions his — then compose the
recipe from the skeleton.

Elicitation checklist:
1. **Audience and register.** Who sits in the room; technical or
   executive; how direct.
2. **Purpose and the one message.** What the audience must take away —
   the deck's centre of gravity is built around it.
3. **Inputs.** Which chain artefacts feed the deck (default the
   intent). A picture may come from another render of the project: a
   slide references it as `render: <file>`, and that render is
   declared among Inputs so provenance and staleness track it.
4. **Dramaturgy.** Slide count; opening and closing slides; agenda
   slide yes/no; section dividers; the arc from first slide to last.
5. **Speaker notes.** Wanted at all? If yes, whether they carry
   traceability citations (POS/REQ IDs) back to the inputs.
6. **On-slide density.** Maximum bullets and words per slide; what is
   banished to the notes.
7. **Diagram policy.** Which slides carry a diagram; inline Mermaid
   (valid standalone, simple enough to survive conversion into native
   slide shapes) or a reference to an existing render.
8. **Vocabulary discipline.** Terms that must not blur (defined
   Terms, house distinctions); the recipe states them explicitly.
9. **What must not appear.** Confidentiality toward this audience:
   internal figures, vendor names, anything the room must not see.
10. **Build instructions.** For the deck-builder LLM: recommended
    `.potx` template (named by path, typically a document of a
    library project: `projects/lib-<name>/sources/<file>.potx`),
    recommended model for
    `md2pptx.ps1 -Model` (default opus), overflow handling, diagram
    redraw expectations. Copied verbatim into the render so the
    builder sees them.

The language question and the composition from the skeleton close
every genre (`/recipe`, step 2).
