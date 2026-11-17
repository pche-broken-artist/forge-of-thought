---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: 08e6a09630998d67
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - .claude/skills/recipe/genres/readme.md
  - .claude/skills/recipe/genres/release-notes.md
  - .claude/skills/recipe/genres/screenplay.md
  - .claude/skills/recipe/genres/user-stories-export.md
  - templates/recipe.md
  - CLAUDE.md#Versioning & status
---

# Compose a recipe

This page shows how you compose a render recipe, or iterate one that
exists, with the command `/recipe`. A recipe is the file that says how
one render is made. It is written for the principal, the person whose
thinking is being forged. Terms of the forge are explained in the
[Glossary](../reference/glossary.md).

## When to use it

Use `/recipe` when you want a new render of a project, such as a deck,
a README or a screenplay. Use it also when an existing recipe needs to
change. You change the recipe and never the render, as
[Renders and recipes](../about/renders-and-recipes.md) explains.

## The command

```
/recipe [genre] [slug]
```

The three forms:

- Bare `/recipe` reports the roster: the genres with a line each, and
  the recipes the project already has with their versions.
- `/recipe <genre> <slug>` composes a recipe through that genre.
- `/recipe <recipe-name> <slug>` iterates an existing recipe. This
  form is taken when the name is not a genre but a file
  `recipes/<recipe-name>.md` exists in the project.

The slug names the project. Where it cannot be told from the
context, Claude asks.

The five genres today:

- `presentation`: a slide-by-slide deck definition, with a plain
  `.pptx` from `/render` and a designed one from `/publish`.
- `readme`: the project's README, regenerated at every release.
- `release-notes`: the project's release notes, one section per
  release in six fixed groups.
- `screenplay`: a teaching video of a terminal conversation, cut from
  session records.
- `user-stories-export`: the project's user stories as an export, one
  heading per story, for pasting elsewhere.

Each genre has its own checklist of questions. The checklists are
in [Recipe genres](../reference/recipe-genres.md).

A recipe that fits no genre is legitimate. Claude composes it with
you in conversation from the base skeleton of a recipe.

## What happens

1. Claude finds the genre, or the existing recipe of that name. You
   should now see either the genre's first question or the recipe
   opened for iteration.
2. Claude asks the genre's questions as an interviewer. It offers
   options and trade-offs, and the decisions are yours. You should
   now see one question at a time, each with Claude's
   recommendation.
3. The checklist closes with the language question. The render is
   made in one language, or in several where the genre allows it: the
   first is the primary and the rest are its translations. Claude
   proposes the project's language from its project file and asks. It
   never assumes. You should now see the proposed language and a
   request to confirm or change it.
4. Claude composes the recipe from the genre's skeleton. Unused
   placeholders and the skeleton's comments are deleted. Only the one
   line that names the skeleton stays. You should now see the
   composed recipe, shown before it is written.
5. On your confirmation Claude writes it, once per round. You should
   now see the recipe in `recipes/` and its history companion beside
   it.
6. Claude offers `/render <recipe>` as the next step. You should now
   see that offer. The generation is described in
   [Render an output](render-an-output.md).

## What you have afterwards

- The recipe `recipes/<recipe>.md`, with a version and no status.
- Its history companion `recipes/<recipe>.history.md`, created with
  the recipe.

A recipe is versioned 0.x. It becomes an integer only where you name
one.

## If something goes wrong

- The argument is neither a genre nor the name of an existing recipe:
  Claude lists the genres that exist and stops. Give a genre from the
  list or the name of a recipe in `recipes/`.
- The project cannot be told from the context: Claude asks which
  project is meant.

## A worked example

You want a README for a project with the slug `<slug>`.

```
/recipe readme <slug>
```

Claude asks who the primary reader is, which ledger and chain facts
the README shows, and what must not appear. It then asks whether the
README is in the project's language, proposing the language from the
project file. You confirm. Claude shows the recipe, you confirm, and
it writes `recipes/readme.md` at version 0.1 with its history. Claude
then offers `/render readme`.

Related pages for two genres:
[Make a teaching video from a recipe](make-a-video-from-a-recipe.md)
takes the screenplay genre from recipe to played video.
[Write user stories](write-user-stories.md) covers the stories that
the export genre renders.

## See also

- [Renders and recipes](../about/renders-and-recipes.md): why the recipe is iterated and the render never edited.
- [Recipe genres](../reference/recipe-genres.md): each genre's checklist in full.
- [Render an output](render-an-output.md): generating the render.
- [Make a teaching video from a recipe](make-a-video-from-a-recipe.md): the screenplay genre from recipe to played video.
- [Write user stories](write-user-stories.md): the stories the export genre renders.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
