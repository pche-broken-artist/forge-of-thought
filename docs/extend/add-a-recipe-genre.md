---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: e3d3c430faebde3c
inputs:
  - .claude/skills/recipe/SKILL.md
  - .claude/skills/recipe/genres/presentation.md
  - templates/recipe.md
  - templates/recipe-presentation.md
  - .claude/skills/man/SKILL.md
---

# Add a recipe genre

A recipe genre is one kind of
[recipe](../about/renders-and-recipes.md) that the command `/recipe`
composes by guided questions, such as a presentation. A recipe is the
versioned file that says what a render is generated from, for which
audience and in what shape. A render is the output generated from it.
This page is for the extender who wants `/recipe` to offer a kind of
render it does not offer yet. It names the two files a genre consists
of, the order in which you write them and the run that proves the
genre.

## Before you start

- A genre is a change of the forge. It is proved, recorded and
  released as any change of the forge, in the way
  [Make a change to the forge](how-a-change-is-made.md) describes.
- The genres that exist are listed in
  [Recipe genres](../reference/recipe-genres.md).
- A recipe that fits no genre does not need one. `/recipe` composes
  such a recipe in conversation from the base template
  `templates/recipe.md`.
- The presentation genre is the pattern of the two shapes this page
  describes. Its two files are
  `.claude/skills/recipe/genres/presentation.md` and
  `templates/recipe-presentation.md`.
- The proof needs a project to compose on. How a composition runs is
  described in [Compose a recipe](../use/compose-a-recipe.md).

## The files

A genre is two files. The command `/recipe` itself is not edited.

| File | What it is | What reads it |
|---|---|---|
| `.claude/skills/recipe/genres/<genre>.md` | the definition of the genre: what Claude asks before it composes | `/recipe` typed alone, `/recipe <genre>`, `/man recipe` |
| `templates/recipe-<genre>.md` | the template of the genre: what a recipe of the genre looks like | `/recipe <genre>`, when it composes the recipe |

### The definition

The definition holds these parts, in the order the presentation
genre has them:

- **The description**: one line in the front-matter, under the key
  `description`, that says what the genre composes. `/recipe` typed
  alone lists every genre with this line, and `/man recipe` prints
  it.
- **The genre and its template**: one line of the form
  ``Genre: <genre>. Skeleton: `templates/recipe-<genre>.md`.`` The
  genre files call the template of a genre its skeleton.
- **The product**: a paragraph that says what the render of such a
  recipe is and which files are made from it.
- **The role**: a paragraph that makes Claude the interviewer. Claude
  draws the answers out of the principal (the person whose thinking
  is forged) and then composes the recipe from the template.
- **The [elicitation](../reference/glossary.md) checklist**: a
  numbered list of the questions by which the answers are drawn out,
  under the line `Elicitation checklist:`. Each item has a name in
  bold and says what is asked.
- **The closing line**: one sentence that says the language question
  and the composition from the template close every genre.

Whatever is typed after the genre name reaches the definition as its
arguments.

### The template

The template is the base recipe shape of `templates/recipe.md`. What
every recipe of the genre shares is filled in. What one recipe
decides is a placeholder in angle brackets.

| Part | What stands there |
|---|---|
| front-matter `project` | a placeholder for the slug of the project |
| front-matter `purpose` | what a recipe of the genre is for |
| front-matter `audience` | a placeholder for the audience |
| front-matter `version` | `0.1` |
| front-matter `output:` | optional, a commented line: a path that overrides the default place of the render, `renders/<recipe>.md` |
| front-matter `languages:` | only where the genre allows translations: the first language is the primary one, the rest are its translations, and every language gets a render of its own, `renders/<recipe>.<lang>.md` |
| the title | `# Recipe — <name>` |
| the line that names the template | `<!-- Shape: templates/recipe-<genre>.md -->` |
| `## Inputs` | the documents the render is generated from, by path, one per line; the base shape starts with `10-intent.md` |
| `## Instructions` | what must be known to make the render beyond the `## Template` section: the instructions every recipe of the genre shares, with placeholders for the answers of the checklist |
| `## Format` | only where the render has a file beside it: the format, what the plain file needs and what the published file needs |
| `## Template` | the literal shape of the render, with placeholders, always Markdown |

A recipe without a `## Format` section ends at the Markdown render.
The section itself is never copied into the render. The base shape
names the formats and says how the file of each is made:

- `pptx` and `docx`: the plain file is made by `/render` through
  pandoc. The published file is made by `/publish` through a model.
- `video` and `html-player`: the file is made through
  `scripts/md2video.py`, with the pace, the date and the look stated
  in the section. There is no published file.
- `png`: the picture is drawn in the run of the render, beside a
  render that carries the provenance and a link to the picture. The
  width in pixels is stated in the section. There is no plain file
  made through a script and no published file.

The template of the presentation genre carries a `## Format` section
for `pptx`. It carries no `languages:` line and names the one
language of the render in its `## Instructions`.

### What `/recipe` does for every genre

Every genre runs in the same frame. None of the following is written
into a genre:

- **The language question.** The checklist closes with it. Claude
  proposes the language of the project from its project file
  (`project.md`) and asks. The answer is one language, or several
  where the template carries `languages:`. The recipe declares it.
- **The composition.** The recipe is composed from the template of
  the genre. Unused placeholders and the comments of the template are
  deleted. The line that names the template stays.
- **The conversation.** Claude offers options and trade-offs. The
  decisions belong to the principal.
- **The write.** The recipe is written once per round of the
  conversation, on the principal's confirmation.
- **The history.** The history of the recipe is kept in
  `recipes/<recipe>.history.md`. That file is created with the
  recipe from `templates/history.md`.
- **The version.** A recipe carries a version and no status.
- **The next step.** After the write Claude offers
  `/render <recipe>`.

## Steps

1. Choose the name of the genre. It is the word typed after `/recipe`
   and it stands in both file names. `/recipe <name>` looks for a
   genre of that name first. It looks for a recipe of that name in
   the project only where no genre has the name, and then iterates
   that recipe.
2. Write the template `templates/recipe-<genre>.md`. Start from
   `templates/recipe.md` and keep its sections in their order. Let
   the line that names the template name the new file. Fill in what
   every recipe of the genre shares and leave a placeholder for the
   rest. Keep `## Format` only where the render has a file beside
   it. Carry `languages:` only where the genre allows translations.
3. Write the definition `.claude/skills/recipe/genres/<genre>.md`,
   in the order of the parts above. Name the template on the
   `Skeleton:` line. Let the checklist ask for what the template
   leaves as a placeholder: in the presentation genre every answer
   of the checklist has its place in the template. Where the
   template has a `## Format` section, let the checklist ask for
   what that section needs. Leave the language question out of the
   checklist. The presentation genre does not carry it and closes
   with the one line that names it.
4. Leave the command alone. `.claude/skills/recipe/SKILL.md` is not
   edited for a new genre. `/recipe` typed alone lists the directory
   `.claude/skills/recipe/genres/`, and `/recipe <genre>` resolves
   the definition by its file name.

## Prove it

The proof of a genre is a run of it: a composition on a project,
then a render of what was composed. In this run you are the
principal. The slug `my-project` stands for the project you compose
on.

1. Type `/recipe`. Claude lists the directory of the genres.

   You should now see the new genre in the list, with the one-line
   description of its definition.

2. Type `/man recipe`. The manual reads the definitions and runs
   nothing. It prints in the language of the conversation.

   You should now see the description of the genre and its
   elicitation checklist in full.

3. Type `/recipe <genre> my-project`. Claude asks the questions of
   the checklist, closes with the language question and composes the
   recipe from the template. It writes the recipe on your
   confirmation. Open the recipe: it keeps the line that names your
   template, and no other comment and no unused placeholder of the
   template is left.

   You should now see the recipe `recipes/<recipe>.md` in the
   project, its history file beside it and the offer of
   `/render <recipe>`.

4. Type `/render <recipe>`, with the name the recipe was written
   under.

   You should now see the render `renders/<recipe>.md`, or one
   render per language where the recipe declares languages, and
   beside it the file of the format where the recipe has a
   `## Format` section.

A published file is made by `/publish`, not by this run.

If `/recipe <genre>` lists the genres that exist and stops, it found
neither a definition nor a recipe of that name. The definition then
does not lie at `.claude/skills/recipe/genres/<genre>.md` under the
name you typed.

## Record and release

The two files are recorded and released as any change of the forge.
[Make a change to the forge](how-a-change-is-made.md) gives the way.

## A worked example

A genre named `<genre>`, whose render has a file beside it and no
translations.

The definition `.claude/skills/recipe/genres/<genre>.md`:

```
---
description: Compose a <genre> recipe — <what the render is, in one line>
---

Genre: <genre>. Skeleton: `templates/recipe-<genre>.md`.

The product is a recipe whose render is <what the render is>. <Which
files are made from the render, and by which command.>

Role: interviewer. <What is drawn out of the principal, and that the
recipe is then composed from the skeleton.>

Elicitation checklist:
1. **<Name of the first question>.** <What is asked.>
2. **<Name of the next question>.** <What is asked.>
3. **Format.** <What the Format section of the skeleton needs.>

The language question and the composition from the skeleton close
every genre (`/recipe`, step 2).
```

The template `templates/recipe-<genre>.md`:

```
---
project: <slug>
purpose: <what a recipe of the genre is for>
audience: <audience>
version: 0.1
# output: <path>   # templates/recipe.md
---

# Recipe — <name>

<!-- Shape: templates/recipe-<genre>.md -->

<!-- <What a recipe of this genre is and which command composes it.> -->

## Inputs
- 10-intent.md

## Instructions
- <What every render of the genre is.>
- Audience: <audience>. Language: <language>.
- <One line per answer of the checklist, the answer a placeholder.>

## Format
- Format: <the format of the genre>
- Plain file, made by `/render` through pandoc: reference
  <path | none>.
- Published file, made by `/publish` through a model: template
  <path | none>, model <name>, <anything else the model must know>.

## Template
<The literal shape of the render, with placeholders.>
```

A genre whose render ends at the Markdown leaves out the `## Format`
section and the question that asks for it. A genre that allows
translations carries the `languages:` line of `templates/recipe.md`
in the front-matter of its template.

The proof, on the project `my-project`:

```
/recipe
/man recipe
/recipe <genre> my-project
/render <recipe>
```

Afterwards the project holds the recipe `recipes/<recipe>.md`, its
history `recipes/<recipe>.history.md` and the render
`renders/<recipe>.md` with the file of the format beside it.

## See also

- [Make a change to the forge](how-a-change-is-made.md): proving,
  recording and releasing the change.
- [Recipe genres](../reference/recipe-genres.md): the genres that
  exist.
- [Renders and recipes](../about/renders-and-recipes.md): what a
  recipe is.
- [Compose a recipe](../use/compose-a-recipe.md): the composition
  that proves a genre.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
