---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/recipe/genres/presentation.md
  - .claude/skills/recipe/genres/readme.md
  - .claude/skills/recipe/genres/release-notes.md
  - .claude/skills/recipe/SKILL.md
---

# Recipe genres

This page lists the genres that `/recipe` composes a render recipe
through: for each, its description, its skeleton and output, and the
checklist of questions the interview works through. It is for the
person who composes a recipe and for the one who extends the forge.
The checklists are what `/man recipe` prints.

Each genre is one file in `.claude/skills/recipe/genres/`, with its
skeleton in `templates/recipe-<genre>.md`. In every genre the role is
interviewer: the questions below are put to the principal, options and
trade-offs are offered, and the decisions are his.

## presentation

- **Description:** Compose a presentation recipe, a slide-by-slide deck
  definition, with a plain .pptx from `/render` and a designed one
  from `/publish`.
- **Skeleton:** `templates/recipe-presentation.md`
- **Output:** a slide-by-slide Markdown deck definition, which is
  source material for a presentation and never the presentation
  itself. The PowerPoint files are made from it in two steps, plain by
  `/render` and designed by `/publish`. What each step needs is in the
  recipe's Format section, and the render carries content only.

Elicitation checklist:

1. **Audience and register.** Who sits in the room; technical or
   executive; how direct.
2. **Purpose and the one message.** What the audience must take away;
   the deck's centre of gravity is built around it.
3. **Inputs.** Which chain artefacts feed the deck (default the
   intent). A picture may come from another render of the project: a
   slide references it as `render: <file>`, and that render is
   declared among Inputs so provenance and staleness track it.
4. **Dramaturgy.** Slide count; opening and closing slides; agenda
   slide yes/no; section dividers; the arc from first slide to last.
5. **Speaker notes.** Wanted at all? If yes, whether they carry
   traceability citations (position and requirement IDs) back to the
   inputs.
6. **On-slide density.** Maximum bullets and words per slide; what is
   banished to the notes.
7. **Diagram policy.** Which slides carry a diagram; inline Mermaid
   (valid standalone, simple enough to survive conversion into native
   slide shapes) or a reference to an existing render.
8. **Vocabulary discipline.** Terms that must not blur (defined
   Terms, house distinctions); the recipe states them explicitly.
9. **What must not appear.** Confidentiality toward this audience:
   internal figures, vendor names, anything the room must not see.
10. **Format.** Always `pptx`. For the plain file: a template or none.
    For the published file, read by the model that designs the deck:
    the template, the model, overflow handling, diagram redraw
    expectations (the placeholders of the skeleton's Format section).
    How a template is named and what the model defaults to is in the
    header of `scripts/md2pptx.ps1`. These stay in the recipe and are
    never copied into the render.

## readme

- **Description:** Compose or iterate a project's readme recipe; the
  render is the project's README.md, regenerated at every release.
- **Skeleton:** `templates/recipe-readme.md`
- **Output:** `README.md` in the project root.

When the principal asks for a first version without an interview, the
recipe is drafted from the inputs (the ledger, the brief, the intent's
essence) and presented as a draft to iterate.

Elicitation checklist:

1. **Primary reader.** The recipients of the assignment, colleagues
   browsing the repository, or the principal returning; the README is
   written for the first of them.
2. **Inputs.** A thought project: ledger, brief, intent, and the
   layers below it once they exist. A library: ledger and the two
   `00-INDEX.md` catalogues; its README is a catalogue of what the
   library holds, with Role / Use for each document, and how to use it
   (for example the path a deck template is named by).
3. **What the essence must say** and how much of it: the problem, the
   direction, the recipients; one screen, not the intent.
4. **State.** Which ledger facts appear: chain versions and statuses,
   briefs and mining state, renders, what is waiting on the principal.
5. **What must not appear.** Confidentiality toward whoever can reach
   the repository; internal figures; nothing from other projects.

## release-notes

- **Description:** Compose or iterate a thought project's
  release-notes recipe: one section per release in six fixed groups,
  derived from the records of the chain's history logs.
- **Skeleton:** `templates/recipe-release-notes.md`
- **Output:** `RELEASE-NOTES.md` in the project root. Thought projects
  only: a library has no intent and therefore no release notes; its
  history is git.

The role is interviewer, lightly, because this genre has few degrees of
freedom. The skeleton owns the shape of the notes.

Elicitation checklist:

1. **Which companions feed the notes.** The default is every chain
   artefact but the brief: the intent, the assignment, later layers as
   they appear. A project may narrow it (the forge itself reads the
   intent alone).
2. **The reader.** The recipients tracking the project by default; a
   different reader changes what Action required means.

## The closing shared by every genre

Every genre ends the same way. The checklist closes with the language
question: the render's language is what the recipe declares. The
project's language is proposed from its ledger header and the principal
is asked; it is never assumed. The recipe is then composed from the
genre's skeleton, with unused placeholders and all template comments
deleted.

## See also

- [Compose a recipe](../use/compose-a-recipe.md): composing through a
  genre.
