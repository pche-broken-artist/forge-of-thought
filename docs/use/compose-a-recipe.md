---
generated: 2026-10-09
made: mirrored
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - .claude/skills/recipe/genres/readme.md
  - .claude/skills/recipe/genres/release-notes.md
  - templates/recipe.md
  - CLAUDE.md
---

# Compose a recipe

This page is for a user who wants to make or change a recipe, the
file a render is generated from. It says what `/recipe` does, how a
composition runs and what you see at the end.

## Run the command

The command is `/recipe [genre] [slug]`. The slug names the project;
leave it out and the command infers the project from the
conversation, asking if that is ambiguous. What happens depends on the
first word.

### Bare: see what exists

`/recipe` alone prints the roster. It lists the available genres with
a one-line description each, and the project's existing recipes with
their versions. Where the conversation suggests a fit, it recommends
one.

### With a genre: a guided composition

`/recipe <genre>` starts an interview for that genre. You do this:

1. Answer the genre's checklist of questions. Options and trade-offs
   are offered, and the decisions are yours.
2. Answer the last question, which is always the language. The render's
   language is whatever the recipe declares. The command proposes the
   project's language, taken from its ledger header, and asks. It does
   not assume.
3. Read the recipe composed from the genre's skeleton, with unused
   placeholders and template comments removed.
4. Confirm. The recipe is written once per round, on your
   confirmation, together with its history record.

### With the name of an existing recipe: iterate it

If the word is not a genre but names a recipe in the project's
`recipes/` directory, the command iterates that recipe. It goes
through the genre's interview when a genre fits, and conversationally
otherwise. If the word matches neither a genre nor a recipe, the
command lists the genres and stops.

### A recipe outside any genre

A recipe that fits no genre stays legitimate. It is composed
conversationally from the base skeleton, `templates/recipe.md`.

## What gets written

A recipe is versioned, and it stays at 0.x for life. It carries a
version and an `updated` date, and has no status. Its history lives in
a companion file, `recipes/<recipe>.history.md`, created with the
recipe. One round of work is one version bump, with one history
record per change.

The recipe is entered in the ledger's Renders table once its first
render exists.

## The next step

After writing, the command offers `/render <recipe>` as the natural
next step. A recipe has a section for the output format, which is
optional. A recipe without it ends at the Markdown.

## The three genres

| Genre | What it produces |
|---|---|
| `presentation` | A recipe whose render is a slide-by-slide Markdown deck definition, the source material for a presentation. PowerPoint files are made from it in a later step. |
| `readme` | A project's readme recipe. Its render is the project's `README.md`, regenerated at every release. |
| `release-notes` | A thought project's release-notes recipe. Its render is `RELEASE-NOTES.md`, one section per release. |

## See also

- [About renders and recipes](../about/renders-and-recipes.md): why the recipe is iterated and the render never edited.
- [Recipe genres](../reference/recipe-genres.md): each genre's checklist in full.
- [Render an output](render-an-output.md): generating the render.
