---
generated: 2026-10-14
version: 5.9
made: mirrored
inputs-hash: 442e858a96a3f013
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - .claude/skills/recipe/genres/readme.md
  - .claude/skills/recipe/genres/release-notes.md
  - .claude/skills/recipe/genres/screenplay.md
  - templates/recipe.md
---

# Compose a recipe

`/recipe` is the command that composes or iterates a render recipe, the
file that says how one output is generated from the documents of a
project. This page is for you when you want a new render, or want to
change the way an existing one is made. The words used here: the
principal is whoever's thinking is being forged, and Claude is the
assistant that works with the principal.

## When to use it

- You want a new output and one of the genres fits it.
- You want an output that fits no genre.
- You want to change an existing recipe.

The recipe is what you iterate. The render made from it is never
edited by hand; the reason is on [Renders and recipes](../about/renders-and-recipes.md).

## The command

```
/recipe [genre] [slug]
```

Both arguments are optional. A line you can type as it stands:

```
/recipe presentation my-project
```

The slug names the project. Where it is left out, Claude infers the
project from the conversation and asks if that is ambiguous.

## What happens

1. Bare `/recipe` reports the roster. Claude lists the genres with one
   line each, then the project's existing recipes with their versions,
   and recommends a fit where the conversation suggests one.

   You should now see the genres and the recipes of the project, and
   perhaps a recommendation.

2. `/recipe <genre>` starts a guided composition. Claude interviews
   you through the genre's checklist, offers options and trade-offs,
   and leaves every decision to you. The checklist of each genre is on
   [Recipe genres](../reference/recipe-genres.md).

   You should now see Claude asking its questions one genre-specific
   point at a time.

3. The checklist closes with the language question. Claude proposes the
   project's language from its ledger header and asks; it never
   assumes. A recipe declares one language. Where the genre allows it,
   a recipe declares several: the first is the primary and the rest are
   its translations, one render per language.

   You should now see the language proposed and your answer asked.

4. Claude composes the recipe from the genre's skeleton, with unused
   placeholders and template comments removed. A skeleton is the
   template of a file; the recipe has an optional Format section that
   names the file format to produce, and it is covered by the genre's
   checklist.

   You should now see the recipe set out for your confirmation.

5. Claude writes once per round, on your confirmation. The recipe
   carries a version and an updated date, and no status. Its history is
   recorded in `recipes/<recipe>.history.md`, created from
   `templates/history.md` together with the recipe.

   You should now see the written recipe and its history companion named
   as files.

6. Claude offers `/render <recipe>` as the next step. How the render is
   generated is on [Render an output](render-an-output.md).

   You should now see the offer of `/render` with the recipe's name.

Two other ways in:

- With the name of an existing recipe in place of a genre, Claude
  iterates that recipe. It does so through the genre definition when
  one fits, otherwise in conversation.
- A recipe outside any genre is composed in conversation from the base
  skeleton, `templates/recipe.md`. That stays legitimate.

## The genres of today

- **presentation**: a slide-by-slide deck definition, with a plain
  `.pptx` from `/render` and a designed one from `/publish`.
- **readme**: the project's README, regenerated at every release.
- **release-notes**: the release notes of a thought project, one section
  per release, derived from the records of the chain's history logs.
- **screenplay**: a teaching video cut from session records, made into
  a video or into the player page by a script. The path from recipe to
  played video is on [Make a teaching video from a recipe](make-a-video-from-a-recipe.md).

## What you have afterwards

- A recipe in `recipes/<recipe>.md`, versioned 0.x for life, and its
  history companion beside it.
- The offer to render it.

## If something goes wrong

- The argument names neither a genre nor an existing recipe of the
  project: Claude lists the genres that exist and stops. Check the
  spelling against the roster and run the command again.
- The project is ambiguous: Claude asks which one you mean.

## A worked example

You want a short deck for colleagues, in a project called `my-project`.

```
/recipe presentation my-project
```

Claude asks who sits in the room, what they must take away, which
documents feed the deck and how dense the slides may be. You answer,
and Claude states the answers back. At the end it asks which language
the deck is written in and proposes the project's own. You confirm.
Claude writes `recipes/<recipe>.md` at version 0.1 and its history
file, and offers `/render <recipe>`. Next time you want a change, you
run `/recipe <recipe> my-project` with the recipe's name, and Claude
iterates it.

## See also

- [Renders and recipes](../about/renders-and-recipes.md): why the recipe is iterated and the render never edited.
- [Recipe genres](../reference/recipe-genres.md): each genre's checklist in full.
- [Render an output](render-an-output.md): generating the render.
- [Make a teaching video from a recipe](make-a-video-from-a-recipe.md): the screenplay genre from recipe to played video.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
