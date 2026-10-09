---
generated: 2026-10-09
made: mirrored
inputs-hash: 12286338a7125d86
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - .claude/skills/recipe/genres/readme.md
  - .claude/skills/recipe/genres/release-notes.md
  - templates/recipe.md
  - CLAUDE.md
---

# Compose a recipe

This page is for a user who wants a new render, or wants to change how
an existing one is made. A recipe is the file that says how a render is
made, and `/recipe` is the command that composes it with you.

## Run the command

The command is `/recipe [genre] [slug]`. The slug names the project; if
it is not clear from the conversation, you are asked.

- **Bare `/recipe`.** You get the roster: the available genres, each
  with a one-line description, and the recipes the project already has
  with their versions. Where the conversation suggests a fit, a
  recommendation comes with it.
- **`/recipe <genre>`.** A guided composition through that genre. You
  are asked the genre's questions one after another, with options and
  trade-offs offered. The decisions are yours.
- **`/recipe <name of an existing recipe>`.** If the name is not a genre
  but the project has a recipe of that name, that recipe is iterated:
  through its genre where one fits, otherwise in conversation.
- **A name that is neither.** You are shown the genres that exist and
  nothing is composed.

A recipe that fits no genre is still legitimate. It is composed in
conversation from the base skeleton, `templates/recipe.md`, which has
the sections Inputs, Instructions, an optional Format and Template.

## What happens in a guided composition

1. The genre's questions are put to you. Every genre closes with the
   language question: the render's language is whatever the recipe
   declares. The project's language is proposed from its ledger header
   and you are asked; it is never assumed.
2. The recipe is then composed from the genre's skeleton, with unused
   placeholders and template comments removed.
3. The recipe is written once per round, when you confirm. It carries a
   version and an updated date but no status, and it stays at 0.x for
   life, because recipes are tools that are iterated and never
   approved. Its history goes into a companion file,
   `recipes/<recipe>.history.md`, created with the recipe.
4. `/render <recipe>` is offered as the next step. The recipe is
   entered in the ledger's Renders table when its first render exists.

A recipe may name a Format section for a plain or a designed file. That
section exists so the files can be made later; the render itself
carries content only.

## The three genres today

| Genre | What it produces |
|---|---|
| `presentation` | A recipe whose render is a slide-by-slide Markdown deck definition, the source for a PowerPoint file and never the presentation itself. |
| `readme` | A recipe whose render is the project's `README.md` in the project root, regenerated at every release. |
| `release-notes` | A recipe whose render is `RELEASE-NOTES.md` in the project root, for thought projects only. |

The presentation genre has the longest interview. The readme genre asks
a shorter one, and if you ask for a first version without an interview
it is drafted from the project's documents and handed to you as a draft
to iterate. The release-notes genre has few degrees of freedom, so it
asks little: which documents feed the notes and who reads them.

## See also

- [About renders and recipes](../about/renders-and-recipes.md): why the recipe is iterated and the render never edited.
- [Recipe genres](../reference/recipe-genres.md): each genre's checklist in full.
- [Render an output](render-an-output.md): generating the render.
