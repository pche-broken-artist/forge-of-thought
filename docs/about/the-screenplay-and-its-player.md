---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 9bb61e38056f81be
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

A screenplay is a render that shows a real terminal conversation with
Claude as a teaching video, cut from the records of the working
sessions. This page explains what such a video is made of, why one
script makes both of its formats, and why the engine hosts the files a
project shows in public. It is written for the user who wants to make
a video, the extender who wants to know how the parts fit, and the
evaluator who wants to know what the forge promises about it.

## What it is

A screenplay is the render of a recipe of the genre `screenplay`. A
recipe is the versioned file that says how a render is made; a render
is the output generated from it and never edited by hand (see
[Renders and recipes](renders-and-recipes.md)). The principal is the
person whose thinking is being forged and who has the final word on
every document. A session is one working conversation between the
principal and Claude in the terminal.

The render is never the video itself. It is a Markdown screenplay in a
fixed order:

- a title card: it discloses how the video was composed (real work,
  how many sessions, how many hours, times real, lines verbatim or
  shortened);
- a card of what the viewer will see;
- the scenes: each with the real time of day, a caption and a fenced
  block of what the terminal shows;
- an end card: it says the one message the viewer leaves with.

The caption of a scene has two parts:

- Now: what happens in the scene;
- Why: why the forge does it this way.

The caption is the teaching and the terminal is the evidence.

The inputs of the recipe are two kinds of file:

- session records registered as sources (a transcript extract, cut by
  timestamps);
- the brief that says what the videos are for.

A document the video shows being born may be named as a further input
by its path.

The video file is made from the render by a script, in one of two
formats that the recipe's Format section names:

- `video`: an MP4, painted frame by frame as a simulated terminal;
- `html-player`: the timed events of the video, played by the player
  page of the engine.

A recipe names one format, never both.

## How it works

### From the recipe to the render

The recipe is composed through an interview of the genre. The
questions it asks are listed in full in
[Recipe genres](../reference/recipe-genres.md). They settle, among
other things:

- the audience and the register of the captions;
- the beats: the scenes pinned by the time of their first line, so
  that every render is the same cut;
- the quotes: the principal's lines as typed, Claude's answers shown
  in full or cut to the sentences that carry the move, a tool call as
  one dim line, no tool output and no permission prompt;
- the length, and what is shortened when there is too much: Claude's
  lines, never the principal's and never the captions;
- what must not appear: names, companies, hosts, paths outside the
  forge;
- the languages, the pace and look, and the format.

### Several languages

A recipe may declare several output languages. The first is the
primary; it is the language of the sessions. The others are its
translations. One run of the render generates the primary screenplay
and then translates it into every other language, scene for scene and
line for line. A translation is not generated afresh. This is because
the quotes, the beats and the captions are chosen once, and a second
generation would choose them again differently. Each language has its
own render file, and the format file follows that file's name. The
notation of the render stays English; its content is in the render's
language.

### One script, two formats

Both formats are made by one script, `scripts/md2video.py` (see
[Scripts](../reference/scripts.md)). The script reads the render: the
language from its front-matter, the cards, and the scenes with their
captions and terminal blocks. It then computes the timeline of the
video:

- the typing of a line;
- the stand before Enter;
- the reveal of an answer;
- the hold for reading;
- the breath at the end of a scene.

The timeline is computed from the pace of reading, given in words a
second for three kinds of line:

- the principal's lines (4 by default);
- Claude's answers (8 by default);
- lines that only report a file (16 by default).

For `video`, the script paints every frame as a simulated terminal
with a caption band and encodes the frames into an MP4. For
`html-player`, it writes the timeline as timed events in a small
script file. That file is wrapped so that the player page can play it
from a file on disk as well as from the public site.

The script is deterministic: the same render gives the same file every
time. No model takes part. The file it makes is the plain file of the
render and lands beside the render, unless the recipe sends it
elsewhere. A screenplay has no designed step and no published file.
The command that makes designed files through a model has no part in
it. This is because there is no designed step a model could add.

The pace of reading, the look of the terminal and the labels of the
captions stand in the recipe's Format section. They reach the script
as its arguments and never appear in the render. The reason they are
kept out of the render is not recorded. The parsing of the screenplay
and the pace live in the script alone; the player page plays what the
script computed.

The script installs nothing. What it needs installed is said in
`scripts/forge_tools.py`.

### The player page

The player page is one fixed file of the engine,
`docs/videos/index.html`. It is a single file with no dependency
beyond the browser. It holds:

- a sidebar of the videos: each by the title of its title card, in the
  order of the file names, grouped under the section of the course
  that each file names;
- the player: the simulated terminal, the caption band and the cards;
- play and pause, and the speed;
- the scenes of a video as chapters;
- the choice of language, where a video has siblings in other
  languages;
- three font sizes, remembered in the browser.

The page is written anew by the script from its template,
`templates/html-player.html`, whenever the script writes a file into
the public folder. The script embeds the list of the folder's files
into the page. This is because the public site cannot list a folder.
The page is never edited by hand, and no model touches it or its
template. What is changed is the template, and the script writes the
page again.

### The public folder

A recipe of a project may send its `html-player` file out of the
project, by its `output:` path, into the engine's folder
`docs/videos/`. The engine carries the file only. The recipe, the
render, the provenance and the history stay in the project, and
whoever has the project can regenerate the file. A video kept for a
closed audience names no `output:` and stays in the project's
`renders/`.

What goes out is chosen in the recipe, video by video. The principal
reads the file before the engine is saved. That reading is the one
step that clears a public version.

The folder is flat: its files lie side by side, in the order of their
names. It is foreign to the documentation. The commands and checks
that generate and verify the documentation in `docs/` leave the folder
alone, and the index of the documentation does not list it. Video
files (`.mp4`) never enter the repository tree. They go out as assets
of a release. The public site is served from `docs/` of the engine
once the principal has switched it on by hand. An empty
`docs/.nojekyll` makes the site serve the files as they lie.

## Why

### Why the caption has two parts

The caption is the teaching and the terminal is the evidence. The
viewer sees what really happened in the terminal. The caption says
what happens and why the forge works so.

### Why one script makes both formats

The parsing of the screenplay and the pace of reading are one
mechanism. For that reason one script with two formats was chosen
against two scripts.

The script paints its frames itself, in the language the other scripts
are written in, with one encoder. It was chosen against three other
ways of turning a terminal into a video:

- a terminal recorder that was found broken on Windows;
- a recording tool whose converter ends at an animated GIF;
- a browser driven by a test tool, which needed the most code.

The painter was the least to install and runs on Windows, Linux and
macOS.

### Why the engine hosts the public files

The engine is public and its `docs/` is served as a public site. It is
the one public place of an instance (one installation of the forge).
The project that made a video stays where its sources require, such as
a private repository. The engine therefore carries only the finished
file, and everything the file was made from stays in the project. See
[Projects and the engine](projects-and-the-engine.md) for why the
engine is public and each project is a repository of its own.

### Why a fixed page with the list embedded

A fixed page with the list of files embedded was chosen against three
other shapes:

- a generated index file beside the page;
- a course recipe with an outline;
- folders as sections.

The order of the file names was chosen for now. The price is that the
script touches a page of the engine.

A single file was chosen against a page with its scripts and styles
beside it. This is because one file is one thing to serve and to copy.

### Reasons not recorded

- Why video files are kept out of the tree and go out as release
  assets: the reason is not recorded.
- Why the public folder is kept out of the documentation and its
  checks: the reason is not recorded.

## A worked example

One generic scene of a screenplay, taken from no project. It shows the
parts the genre names; the exact layout of the lines is illustrative.

````markdown
### 09:42

**Now:** The principal asks for a write; Claude restates the round
before it touches the file.

**Why:** A write confirms what was agreed rather than surprising the
principal.

```
> write

● Before I write, here is the round as I understood it:
  the intent goes to 0.4, two positions changed, one thread closed.
  Shall I write it?
  (a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark
```
````

The time is the real time of day of the scene's first line. The
caption carries the teaching. The fenced block carries what the
terminal showed, cut to the lines that carry the move.

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

Generated on 2026-11-01 for version 6.4 from the files the
front-matter names; never edited by hand.
