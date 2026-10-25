---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 3eff6194e2f3827e
inputs:
  - projects/forge/10-intent.md#POS.1530
  - projects/forge/10-intent.md#POS.1540
  - projects/forge/10-intent.md#POS.1550
  - projects/forge/40-solution-design.md#SOL.0650
  - projects/forge/40-solution-design.md#SOL.0660
  - .claude/skills/recipe/genres/screenplay.md
  - templates/html-player.html
---

# The screenplay and its player

A screenplay is the render of a teaching video: a written cut of a
real terminal conversation with Claude, from which one script makes
either a video file or the events of a player page. This page explains
what a screenplay is made of, why one script makes both of its
formats, and why the engine (the public repository of the forge
itself) hosts the files a project shows in public. It is for anyone
who uses, extends or evaluates the forge.

## What it is

A screenplay is the output of a recipe of the genre `screenplay`. A
recipe is the versioned file that says how a render is made; a render
is a generated output, never edited by hand
([Renders and recipes](renders-and-recipes.md)). The person whose
thinking is forged is called the principal.

A screenplay is made of these parts, in order:

- a title card: it discloses the composition, that is, that the
  video shows real work, how many sessions and hours it covers, that
  the times are real and the lines verbatim or shortened;
- a card of what the viewer will see;
- scenes, each with the real time of day, a caption and a fenced block
  of what the terminal shows;
- an end card, which says the one message the viewer leaves with.

The caption of a scene has two parts:

- Now: what happens in the scene;
- Why: why the forge does it this way.

The caption is the teaching. The terminal is the evidence.

The inputs of a screenplay recipe are of two kinds:

- session records registered as sources (a transcript extract, cut by
  timestamps); a session here is one working conversation with
  Claude;
- the brief that says what the videos are for.

The render is never the video. The file is made from the render by a
script, in the format the recipe names.

## How it works

### Two formats, one script

The recipe's Format section names one of two formats, never both:

- `video`: an MP4, painted frame by frame as a simulated terminal;
- `html-player`: the timed events for the player page of the engine.

Both are made by one script, `scripts/md2video.py`
([Scripts](../reference/scripts.md)). The script reads the render,
computes the timeline and writes the file. The timeline covers the
typing, the pause before Enter, the reveal of an answer, the hold for
reading and the breath at the end of a scene. The script is
deterministic: the same render gives the same file every time. No
model takes part in it.

The file is the plain file of `/render`, the command that regenerates
a render from its recipe, and it lands beside the render. A
screenplay has no designed step and no published file: `/publish`
has no part in it, because there is no designed step a model could
add.

The `html-player` file is the timeline as events wrapped in a script
call. The wrapping lets the player page play the file from disk as
well as from the web.

### Pace and look

The pace of reading is given in words a second, for three kinds of
line:

- the principal's lines (4 unless the principal wants otherwise);
- Claude's answers (8);
- the lines that only report a file (16).

The pace, the look of the terminal and the labels of the captions
stand in the recipe's Format section. They reach the script as its
arguments, never in the render. The parsing of the screenplay and the
pace live in the script alone; the player page plays what the script
computed.

### Languages

A recipe may declare several output languages. The first is the
primary; the rest are its translations. `/render` generates the
primary render and, in the same run, translates it into every other
language scene for scene and line for line. Each language has its own
render, named `renders/<recipe>.<lang>.md`, and the format file
follows that name. The render's notation stays English; its content is
in the render's language.

### The player page

The player page is one fixed file of the engine,
`docs/videos/index.html`. It is a single file with no dependency
beyond the browser. It holds:

- a sidebar of the videos by the title of each file's title card,
  grouped by the section of the course each file names, sections and
  videos in the order of the file names, a video without a section
  last;
- the simulated terminal with its caption band and cards;
- play and pause, and the speed;
- the scenes of a video as chapters;
- the language, where a video has siblings in other languages;
- three font sizes, remembered in the browser.

The page is written anew by the script from its template,
`templates/html-player.html`, whenever the script writes a file into
`docs/videos/`. The list of files is embedded in the page. What is
edited is the template, never the page, and no model touches either.

### The public folder

A project's recipe may send its `html-player` file out of the project
into the engine's `docs/videos/`, by the recipe's `output:` path.

- The engine carries the file only. The recipe, the render, the
  provenance and the history stay in the project, and whoever has the
  project can regenerate the file.
- A video kept private names no `output:` and stays in the project's
  `renders/`.
- What goes out is chosen in the recipe, video by video.
- The principal reads the file before the engine is saved. That
  reading is the clearing of a public version, in one step.
- `docs/videos/` is flat, its files in the order of their names.
- The documentation and its checks leave the folder alone: they read
  `docs/` without `docs/videos/`, and the index of the documentation
  does not list it.
- Video files (`.mp4`) never enter the repository's tree. They go out
  as assets of a release.
- An empty `docs/.nojekyll` makes GitHub Pages serve the folder as it
  lies.

## Why

**Why the engine hosts the public files.** The engine is public and
is served by GitHub Pages from `docs/`, so it is the one public place
of an instance (one installation of the forge). The project that made
a video stays where its sources require, such as a private repository.
Why the engine is public while a project is a repository of its own
is explained in [Projects and the engine](projects-and-the-engine.md).

**Why one script makes both formats.** The parsing of the screenplay
and the pace are one mechanism, so they live in one script rather than
two.

**Why the video is painted by the script itself.** The script paints
the frames in Python and pipes them into one encoder. The alternatives
weighed were existing terminal recorders and a browser driven by a
program. One recorder was found broken on Windows, another ended at
GIF, and the browser took the most code. A painter in the language
the scripts already are, with one encoder, was the least to install
and runs on Windows, Linux and macOS.

**Why translations are cut from the primary.** The quotes of a
transcript, the beats and the captions are chosen once. A second
generation would choose them again, differently. Translating scene for
scene keeps every language the same cut.

**Why there is no published file.** A model adds a designed step to a
published file, and a screenplay has none it could add.

**Why the list of files is embedded in the page.** GitHub Pages
cannot list a folder.

**Why the page is one fixed file.** One file is one thing to serve and
to copy. A generated index file beside the page, a course recipe with
an outline, and folders as sections were weighed against it; the order
of file names was chosen for now. The price is that the script touches
a page of the engine.

**Why the pace stays out of the render.** The reason is not recorded.

**Why video files go out as release assets rather than into the
tree.** The reason is not recorded.

## A worked example

One generic scene of a screenplay, in the shape the genre defines.
The project and the lines are placeholders.

````markdown
## Scene 2 - 10:42

**Now:** The principal asks for the state map of the project.
**Why:** The forge shows the state before anything is changed.

```
> /forge example-project
  ... the state map of example-project ...
```
````

The heading carries the real time of day. The two-part caption
teaches, and the fenced block is the evidence of what the terminal
showed. The script turns this into frames of a video, or into timed
events the player page plays.

## See also

- [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md):
  the job from the recipe to the played file.
- [Renders and recipes](renders-and-recipes.md): the render and its
  recipe, which a screenplay is one of.
- [Projects and the engine](projects-and-the-engine.md): why the
  engine is public and a project is a repository of its own.
- [Scripts](../reference/scripts.md): the script that makes both
  formats.
- [Recipe genres](../reference/recipe-genres.md): the genre's
  checklist in full.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
