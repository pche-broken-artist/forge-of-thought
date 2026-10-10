---
generated: 2026-10-10
made: mirrored
inputs-hash: 02d0f2c3980074b7
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - .claude/skills/recipe/genres/readme.md
  - .claude/skills/recipe/genres/release-notes.md
  - templates/recipe.md
  - CLAUDE.md
---

# Compose a recipe

This page is for a user who wants a new render, or wants to change
how an existing one is made. It shows how to compose or iterate a
recipe with `/recipe`, what you are asked, and what you see at the
end.

A recipe is the file that says how a render is made: its inputs, its
audience, its instructions and the template of the output. You never
edit a render by hand. You iterate its recipe and regenerate the
render from it.

## What you type

`/recipe [genre] [slug]`. The slug names the project; where it is
ambiguous you are asked.

| You type | What happens |
|---|---|
| `/recipe` | The roster: the available genres, each with a one-line description, and the project's existing recipes with their versions. A fit is recommended where the conversation suggests one. |
| `/recipe <genre>` | A guided composition of a new recipe through that genre's checklist. |
| `/recipe <recipe-name>` | If the name is not a genre but a recipe exists under that name in the project, that recipe is iterated. A genre definition is used where one fits, otherwise the iteration is a conversation. |

If the name is neither a genre nor an existing recipe, you are shown
the genres that exist and nothing else happens.

## Composing through a genre

1. Claude runs the genre's checklist as an interview, one question at
   a time. It offers options and trade-offs; the decisions are yours.
2. Every genre closes with the language question. Claude proposes the
   project's language, read from its ledger header, and asks. It does
   not assume. The render is in the language the recipe declares.
3. The recipe is then composed from the genre's skeleton. Unused
   placeholders and all template comments are deleted.
4. The recipe is written once per round, when you confirm. It carries
   a version and an updated date, and no status.
5. Claude then offers `/render <recipe>` as the next step.

## A recipe outside any genre

A recipe that fits no genre is legitimate. Compose it in conversation
from the base skeleton. That skeleton has these parts: a header
naming the project, purpose and audience; **Inputs**, the chain
artefacts the render is made from, one per line; **Instructions**,
what the renderer must know beyond the template; an optional
**Format** section, for a recipe that goes beyond Markdown to a
PowerPoint or Word file; and **Template**, the literal skeleton of
the render, always in Markdown.

## Versions and history

A recipe is versioned 0.x for life: it is iterated and never
approved. Its history lives in a companion file beside it,
`recipes/<recipe>.history.md`, created with the recipe. Each round
you confirm is one version and adds its records there.

## The three genres of today

- **presentation**: a recipe whose render is a slide-by-slide
  Markdown deck definition, source material for a presentation. A
  plain PowerPoint file comes from `/render` and a designed one from
  `/publish`.
- **readme**: a project's README. The render is `README.md` in the
  project root, regenerated at every release.
- **release-notes**: the release notes of a thought project. The
  render is `RELEASE-NOTES.md` in the project root, one section per
  release in six fixed groups, derived from the history records of
  the chain. A library has no release notes.

Each genre's checklist in full is in
[Recipe genres](../reference/recipe-genres.md).

## See also

- [About renders and recipes](../about/renders-and-recipes.md): why the recipe is iterated and the render never edited.
- [Recipe genres](../reference/recipe-genres.md): each genre's checklist in full.
- [Render an output](render-an-output.md): generating the render.
