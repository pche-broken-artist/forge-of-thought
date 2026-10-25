---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 2a762a5cb079ef93
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - .claude/skills/recipe/genres/readme.md
  - .claude/skills/recipe/genres/release-notes.md
  - .claude/skills/recipe/genres/screenplay.md
  - templates/recipe.md
---

# Compose a recipe

`/recipe` composes a render recipe, or iterates an existing one, in a conversation with you. It is for the principal (the person whose thinking is being forged) who wants a new output made from the chain, or wants to change how an existing output is made.

## When to use it

- You want a new render, such as a deck, a README, release notes or a screenplay, and no recipe for it exists yet.
- You want to change an existing recipe: its inputs, its audience, its instructions or its format.
- You are unsure which genres exist or which recipes the project already has.

The render itself is never edited by hand. You iterate the recipe, and the render is regenerated from it.

## The command

```
/recipe [genre-or-recipe] [project-slug]
```

A line that can be typed as it stands:

```
/recipe presentation my-project
```

The project slug is optional when the project is clear from the conversation. If it is ambiguous, Claude asks.

## What happens

1. **Bare `/recipe`: the roster.** Claude lists the available genres, each with a one-line description, and the existing recipes of the project with their versions. Where the conversation suggests a fit, it recommends one. You should now see the genres, the project's recipes and, possibly, a recommendation.
2. **`/recipe <genre>`: a guided composition.** Claude reads the genre's definition and interviews you through its checklist. It offers options and trade-offs, and the decisions are yours. You should now see questions one at a time, each tied to the genre.
3. **The language question.** Every genre ends its checklist with it. The render has one language, or several where the genre allows a primary and its translations. Claude proposes the project's language from its project file and asks. It never assumes. You should now see the language proposed and a request for your choice.
4. **The recipe is composed** from the genre's skeleton. Unused placeholders and all template comments are deleted. You should now see the recipe as a draft to confirm.
5. **The write.** The recipe is written once per round, on your confirmation, into `recipes/<recipe>.md`. A recipe carries a version and no status. It stays at a 0.x version, and its history is kept in a companion file, `recipes/<recipe>.history.md`, created with the recipe. You should now see the recipe file and its history companion named.
6. **The next step.** Claude offers `/render <recipe>`. You should now see that offer.

To iterate, give the name of an existing recipe in place of a genre. Claude iterates that recipe through its genre's definition when one fits, and conversationally otherwise.

A recipe outside any genre is legitimate. Claude composes it conversationally from the base skeleton, which has a purpose, an audience, the inputs, the instructions, an optional format and the template of the render.

## The genres of today

- **presentation:** a slide-by-slide deck definition, from which `/render` makes a plain PowerPoint file and `/publish` a designed one.
- **readme:** the project's README, regenerated at every release.
- **release-notes:** the release notes of a thought project, one section per release.
- **screenplay:** a teaching video of a terminal conversation, cut from session records and made into a video or into the events of the player page.

Each genre's checklist is on [Recipe genres](../reference/recipe-genres.md).

## What you have afterwards

- A recipe at version 0.x in `recipes/`, with its history companion.
- An offer to run `/render <recipe>` ([Render an output](render-an-output.md)).
- For a screenplay, a path onward to a played video: [Make a teaching video from a recipe](make-a-video-from-a-recipe.md).

## If something goes wrong

- If the name you gave is neither a genre nor an existing recipe of the project, Claude lists the genres that exist and stops.
- If the project is ambiguous, Claude asks which one you mean.

## A worked example

You want a short deck for the group, in a project whose slug here is `my-project`.

```
/recipe presentation my-project
```

Claude asks about the audience, the one message, the inputs and the other points of the genre. It then asks for the language of the deck and proposes the project's language. You confirm. Claude writes `recipes/<recipe>.md` at version 0.1 with its history companion, and offers `/render <recipe>`.

A week later you want it shorter. You run `/recipe <recipe> my-project`, answer the questions that change, and confirm. The recipe moves to the next 0.x version, the history records the change, and the render is regenerated from the changed recipe.

## See also

- [Renders and recipes](../about/renders-and-recipes.md): why the recipe is iterated and the render never edited.
- [Recipe genres](../reference/recipe-genres.md): each genre's checklist in full.
- [Render an output](render-an-output.md): generating the render.
- [Make a teaching video from a recipe](make-a-video-from-a-recipe.md): the screenplay genre from recipe to played video.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
