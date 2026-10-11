---
generated: 2026-10-11
version: 5.3
made: mirrored
inputs-hash: 7fb111394f64b707
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - .claude/skills/recipe/genres/readme.md
  - .claude/skills/recipe/genres/release-notes.md
  - templates/recipe.md
---

# Compose a recipe

This page shows how you compose or iterate a render recipe with `/recipe`. A recipe is the one versioned file that says how a render is made. It is for the principal (the person whose thinking is being forged) who wants a new render, or wants to change how an existing one comes out.

## When to use it

Use `/recipe` when a project needs a render that does not exist yet, such as a deck, a README or release notes. Use it also when an existing render comes out wrong. The render is never edited by hand, so you change the recipe instead. The reason is given in [Renders and recipes](../about/renders-and-recipes.md).

## The command

```
/recipe presentation my-project
```

The command takes two optional arguments, a genre or the name of an existing recipe, and then a project slug. If the slug is left out, Claude infers the project from the conversation and asks when it is ambiguous.

The forms of the command:

- `/recipe` alone reports the roster.
- `/recipe <genre>` composes a new recipe through that genre.
- `/recipe <recipe>` iterates the recipe of that name, when no genre has that name but the project has such a recipe.

A genre that does not exist and a recipe that does not exist make Claude list the genres and stop.

## The genres

A genre is a guided interview for one kind of render, with its own skeleton. The three genres today:

- `presentation`: a slide-by-slide Markdown deck definition, from which a plain and a designed PowerPoint file can be made.
- `readme`: the project's README, regenerated at every release.
- `release-notes`: the release notes of a thought project, one section per release.

Each genre's checklist is given in full in [Recipe genres](../reference/recipe-genres.md). A recipe that fits no genre is legitimate: Claude composes it conversationally from the base skeleton of a recipe.

## What happens

1. Bare `/recipe` lists the genres, each with its one-line description, and the project's existing recipes with their versions. Claude recommends a fit where the conversation suggests one.
   You should now see the genre roster and the list of recipes of the project.
2. With a genre, Claude reads the genre's definition and interviews you through its checklist. It offers options and trade-offs; the decisions are yours.
   You should now see one question at a time, each with options where there are any.
3. The checklist of every genre closes with the language question. Claude proposes the project's language, as its ledger (the project's state file) records it, and asks. It never assumes.
   You should now see the language proposed and a request to confirm or change it.
4. Claude composes the recipe from the genre's skeleton, with unused placeholders and the template comments deleted. A recipe has inputs, instructions and a template. It may also have a format section, which says which PowerPoint or Word file is made from the render.
   You should now see the composed recipe, shown to you before anything is written.
5. Claude writes once per round, on your confirmation. The recipe is versioned (a version and an updated date, no status) and stays at a 0.x version for life. Its history goes into a companion file beside it, `recipes/<recipe>.history.md`, created with the recipe.
   You should now see the recipe and its history companion named as written.
6. Claude offers `/render <recipe>` as the next step. It is described in [Render an output](render-an-output.md).
   You should now see the offer to render.

When you iterate an existing recipe, the same steps run on the recipe as it stands. Claude goes through the genre's definition where one fits, and otherwise talks the changes through with you.

## What you have afterwards

- The recipe, `recipes/<recipe>.md`, in the project.
- Its history companion, `recipes/<recipe>.history.md`, with the record of the round.
- An offer to run `/render <recipe>`.

## If something goes wrong

- If the genre or recipe name matches nothing, Claude lists the genres that exist and stops. Run the command again with a name from the list.
- If the slug is ambiguous, Claude asks which project you mean.
- If you decline a proposal, nothing is written. Claude reworks the proposal and asks again.

## A worked example

You want a short deck for a team that will carry out an assignment. The project slug is `my-project`.

1. You type `/recipe presentation my-project`.
2. Claude asks who sits in the room and what they must take away. You answer that the audience is technical and that the one message is the scope of the first phase.
3. Claude goes on through the rest of the checklist: which artefacts feed the deck, how many slides, whether speaker notes are wanted, what must not appear. You decide each point.
4. The last question is the language. Claude proposes the language of the project's ledger, and you confirm it.
5. Claude shows the composed recipe. You say to write it.
6. Claude writes `recipes/team-briefing.md` and `recipes/team-briefing.history.md`, then offers `/render team-briefing`.

## See also

- [Renders and recipes](../about/renders-and-recipes.md): why the recipe is iterated and the render never edited.
- [Recipe genres](../reference/recipe-genres.md): each genre's checklist in full.
- [Render an output](render-an-output.md): generating the render.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
