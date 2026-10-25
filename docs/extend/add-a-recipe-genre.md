---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 77fbf1b70fb968bb
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - templates/recipe.md
  - templates/recipe-presentation.md
---

# Add a recipe genre

A recipe genre is one kind of render that `/recipe <genre>` can
compose through a guided interview. This page is for the extender who
wants to add a new genre. It shows the two files a genre consists of,
what each holds, and how to prove that the new genre works. A recipe
is the versioned file that says how a render is made (see
[Renders and recipes](../about/renders-and-recipes.md)). The genres
that exist today are listed in
[Recipe genres](../reference/recipe-genres.md).

## Before you start

- A new genre is a change to the forge. It is proved, recorded and
  released as any change of the forge is, as described in
  [Make a change to the forge](how-a-change-is-made.md).
- The `/recipe` command itself does not change. It acts as a
  dispatcher: it finds a genre by its file and follows what that file
  says. Adding a genre means adding two files and nothing else.
- Bare `/recipe` and `/man recipe` list the genres by scanning the
  genre directory. A new genre appears there as soon as its file
  exists.
- A recipe outside any genre stays legitimate. It is composed in
  conversation from the base recipe template. A genre is worth adding
  where one kind of render recurs and its questions can be fixed in
  advance.

## The files

A genre is two files, named by the same `<genre>` word:

- `.claude/skills/recipe/genres/<genre>.md`: the genre definition,
  which says what to ask the principal and which skeleton to use. The
  principal is the person whose thinking is being forged.
- `templates/recipe-<genre>.md`: the skeleton of a recipe of this
  genre.

### The genre definition

The presentation genre is the model of this shape. Its definition
holds, in this order:

- A front-matter with one field, `description`: one line that says
  what the genre composes. Bare `/recipe` shows this line in its
  roster.
- One line naming the genre and its skeleton, in the form
  `Genre: <genre>. Skeleton: templates/recipe-<genre>.md.`
- A short paragraph on the product: what the render of such a recipe
  is, and what files are made from it, if any.
- A role: the role Claude takes while composing. In the presentation
  genre the role is interviewer. Claude offers options and trade-offs,
  and the decisions are the principal's.
- A numbered elicitation checklist: the questions Claude asks the
  principal, one numbered item each, with a bold name and what the
  item covers.
- A closing line saying that the language question and the
  composition from the skeleton close every genre.

The checklist does not carry the language question itself. That
question belongs to the frame every genre shares (see Steps).

### The skeleton

The skeleton extends the base recipe shape, which is owned by
`templates/recipe.md`. The base shape has:

- a front-matter with `project`, `purpose`, `audience` and `version`
  (starting at `0.1`), and two optional, commented lines: `output:`
  to override where the render lands, and `languages:` to declare a
  primary language and its translations, one render per language;
- `## Inputs`: the artefacts the render is generated from, by path,
  one per line;
- `## Instructions`: everything the renderer must know beyond the
  template, such as audience, tone, emphasis, omissions and length;
- `## Format`: optional; it names the file made beside the Markdown
  render and what each step needs to make it;
- `## Template`: the literal skeleton of the render, always Markdown,
  with placeholders.

A genre skeleton keeps this shape and fills it for its kind of
render:

- It keeps the front-matter, with a `purpose` worded for the genre.
- It adds the `languages:` line where the genre allows translations.
- It gives `## Instructions` the bullets that turn the checklist's
  answers into rules for the renderer, with placeholders where an
  answer goes.
- It keeps `## Format` where the render has a file beside it. The
  presentation skeleton fixes `Format: pptx` and leaves placeholders
  for the plain file (made by `/render`) and the published file (made
  by `/publish` through a model).
- It leaves `## Format` out where the render ends at the Markdown.
- It gives `## Template` the structure of the render for this genre.
  The presentation skeleton gives a table of slides.

Template comments in the skeleton are guidance only. They are deleted
when a recipe is composed from it.

## Steps

1. Choose the genre word. It names both files and is what the person
   types after `/recipe`.
   You should now see no existing file of that name in
   `.claude/skills/recipe/genres/`.
2. Write `templates/recipe-<genre>.md` from `templates/recipe.md`.
   Fill the Instructions with placeholders, keep or drop
   `## Format`, add `languages:` where translations are allowed, and
   shape the Template.
   You should now see a skeleton whose sections are those of the base
   shape.
3. Write `.claude/skills/recipe/genres/<genre>.md`: the one-line
   `description`, the genre and skeleton line, the product paragraph,
   the role and the numbered checklist. Where the skeleton has a
   `## Format` section, give the checklist an item that asks for what
   that section needs.
   You should now see a checklist with one item for each placeholder
   of the skeleton that the principal must decide.
4. Close the definition with the line that the language question and
   the composition from the skeleton close every genre. Do not add
   the language question to the checklist.
   You should now see the definition end with that line.

Every genre runs in the same frame, which `/recipe` supplies. After
the checklist, Claude asks the language question. It proposes the
project's language from the project file (`project.md`) and asks,
never assumes. Where the genre allows it, the answer may be a primary
language and its translations (`languages:`). The recipe is then
composed from the skeleton, with unused placeholders and all template
comments deleted. It is written once per round, on the principal's
confirmation, with a version and no status, and its history file is
created beside it. Afterwards `/recipe` offers `/render <recipe>`.

## Prove it

Run the check on the engine:

```
/check engine
```

Then compose one recipe through the new genre on a project:

```
/recipe <genre> <slug>
```

Type bare `/recipe` as well:

```
/recipe
```

The new genre should appear in its roster with its one-line
description.

## Record and release

The two new files are recorded and released as any change of the
forge is. How that is done is described in
[Make a change to the forge](how-a-change-is-made.md).

## A worked example

Suppose a genre `<genre>` is added whose render is a Markdown
document with no file beside it, and which allows translations.

The definition `.claude/skills/recipe/genres/<genre>.md`:

```
---
description: Compose a <genre> recipe — <what the render is>
---

Genre: <genre>. Skeleton: `templates/recipe-<genre>.md`.

The product is a recipe whose render is <what the render is>.

Role: interviewer. Elicit the answers below from the principal —
options and trade-offs offered, decisions his (`/recipe`, step 2) —
then compose the recipe from the skeleton.

Elicitation checklist:
1. **<First matter>.** <What is asked.>
2. **<Second matter>.** <What is asked.>

The language question and the composition from the skeleton close
every genre (`/recipe`, step 2).
```

The skeleton `templates/recipe-<genre>.md`:

```
---
project: <slug>
purpose: <purpose of a <genre> render>
audience: <audience>
version: 0.1
# output: <path>   # optional
# languages: <primary, translation>   # optional
---

# Recipe — <name>

## Inputs
- 10-intent.md

## Instructions
- <rule filled from the first matter>
- <rule filled from the second matter>

## Template
<the literal skeleton of the render>
```

This skeleton has no `## Format` section, because its render ends at
the Markdown. Once both files exist, `/recipe <genre> <slug>` asks the
two questions, then the language question, and composes
`recipes/<recipe>.md` in the project.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Recipe genres](../reference/recipe-genres.md): the genres that
  exist.
- [Renders and recipes](../about/renders-and-recipes.md): what a
  recipe is.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
