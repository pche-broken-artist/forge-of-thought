---
generated: 2026-10-09
made: derived
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - templates/recipe.md
  - templates/recipe-presentation.md
  - CLAUDE.md
---

# Add a recipe genre

This page is for someone extending the forge who wants a new genre of
render recipe: a guided interview that composes the recipe for one
kind of render. It was put together from the `/recipe` skill, the
presentation genre and its skeleton taken as the model pair, the base
recipe skeleton `templates/recipe.md` and `CLAUDE.md`.

A genre is two files. Nothing else changes: the dispatcher, the
`/recipe` skill itself, stays as it is.

## What you add

| File | What it is |
|---|---|
| `.claude/skills/recipe/genres/<genre>.md` | the genre definition: the interview |
| `templates/recipe-<genre>.md` | the skeleton the composed recipe starts from |

The name `<genre>` is the same in both paths and is what the person
types after `/recipe`.

## Steps

1. **Write the definition** at `.claude/skills/recipe/genres/<genre>.md`.
   Take the presentation genre's file as the model. It has:
   - front-matter with a one-line `description`, the line the roster
     shows;
   - a first line giving the genre name and the path of its skeleton;
   - a short statement of the product: what the recipe's render is,
     and how any file beside it is made;
   - a `Role:` line saying what Claude does in the composition, an
     interviewer who offers options and trade-offs while the decisions
     stay with the principal;
   - a numbered elicitation checklist, each item a bold topic and the
     questions it settles for this kind of render.
2. **Close with the language question.** Every genre runs in the same
   frame: the checklist closes with the language question, and the
   recipe is then composed from the genre's skeleton. The render's
   language is what the recipe declares, so the interview proposes the
   project's language from its ledger header and asks; it never
   assumes. The presentation genre ends with a line saying that the
   language question and the composition from the skeleton close every
   genre.
3. **Write the skeleton** at `templates/recipe-<genre>.md`. It extends
   the base recipe shape in `templates/recipe.md` and never replaces
   it, because the base skeleton owns the shape:
   - the same front-matter fields: `project`, `purpose`, `audience`,
     `version`, `updated`, `last_change`, and the optional `output`;
   - the same sections: Inputs, Instructions, Format, Template;
   - a `## Format` section where the render has a file beside it, a
     `pptx` or `docx`; a recipe without it ends at the Markdown;
   - a Template section holding the literal skeleton of the render,
     always Markdown.

   What the genre adds goes into the existing sections: the
   presentation skeleton fills Instructions with the rules for its kind
   of render and Template with the slide list. Placeholders stand in
   angle brackets, and a comment at the top says which genre composes
   the recipe. When a recipe is composed, unused placeholders and all
   template comments are deleted.
4. **Leave the dispatcher alone.** Bare `/recipe` lists the genres
   directory, each genre with its one-line description, so the new
   genre appears by existing there.

## What the person then gets

When someone runs `/recipe <genre>`, the dispatcher reads your
definition and follows it. The recipe is composed with the principal
from your skeleton and written once per round, on confirmation, with
its version and updated date and no status; its history goes into
`recipes/<recipe>.history.md`. The recipe is registered in the
ledger's Renders table when its first render exists. After writing,
`/render <recipe>` is offered as the next step.

## Prove it

- Run `/check engine` to see that the new files conform to the
  forge's conventions.
- Run `/recipe` bare and see the genre in the roster with its
  one-line description.
- Compose a recipe on a project with `/recipe <genre>` and follow the
  interview through to the written recipe. This is the real test of
  the two files.

## See also

- [Recipe genres](../reference/recipe-genres.md): the genres that
  exist.
- [About renders and recipes](../about/renders-and-recipes.md): what
  a recipe is.
