---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: ad588dbbfae71b21
inputs:
  - projects/forge/10-intent.md#POS.1530
  - projects/forge/10-intent.md#POS.1540
  - projects/forge/10-intent.md#POS.1550
  - projects/forge/40-solution-design.md#SOL.0420
  - projects/forge/40-solution-design.md#SOL.0650
  - projects/forge/40-solution-design.md#SOL.0660
  - .claude/skills/recipe/genres/screenplay.md
  - templates/html-player.html
---

# The screenplay and its player

A screenplay is a render of the forge that tells a terminal
conversation as a teaching video: scenes cut from the records of real
sessions, each with a caption that teaches and a block of terminal
that proves. This page explains what such a video is made of, how one
script turns the same screenplay into either of its two formats, what
the player page of the engine is, and why the engine, not the project,
hosts the files a project shows in public. It is for the user who
wants to understand what he is making, for the extender who meets the
script and the skeleton, and for the evaluator who wants to know why
the pieces lie where they do. How the job is done, from the recipe to
the played file, is the how-to
[Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md).

## What it is

A screenplay is one render among the [renders and
recipes](renders-and-recipes.md) of a project: a recipe of the genre
`screenplay` names its inputs, its audience and its format, and
`/render` generates the screenplay from it. The render is never the
video. The video, or the events the player page plays, is a plain
file made from the render by a script.

The screenplay has a fixed composition:

- a title card, which discloses how the video was composed: real
  work, how many sessions, how many hours, the times real, the lines
  verbatim and shortened
- a card of what the viewer will see
- scenes, each pinned to the real time of day of its first line
- in every scene a caption of two parts: what happens now, and why
  the forge does it this way
- in every scene a fenced block of what the terminal shows
- an end card, which says the one message the viewer leaves with

The caption is the teaching; the terminal is the evidence.

Its inputs are of two kinds. The session records are registered as
sources of the project, as a transcript extract cut by timestamps.
The brief of the videos says what the videos are for. A document the
video shows being born may stand beside them as a dependency, cited
by path.

A recipe may declare several languages. The first is the primary
language, the language of the sessions. The rest are its
translations, made in the same run, scene for scene and line for
line, so that every language shows the same cut. One render is
written per language, `renders/<recipe>.<lang>.md`, each with its own
provenance; a translation cites the primary render it was made from.
The notation of the render stays English; its content is in the
render's language. A recipe with one language keeps
`renders/<recipe>.md`.

The Format section of the recipe names one of two formats, never
both:

- `video`: an MP4, painted frame by frame as a simulated terminal
- `html-player`: the timed events for the player page of the engine,
  written as a script file, `renders/<recipe>.<lang>.html-player.js`

Both are the plain file of `/render`. There is no designed step and
no published file: `/publish` does nothing with a screenplay, and the
Published table of the ledger (the state report of a project, made at
read time) carries no row of it.

## How it works

One script makes both formats, `scripts/md2video.py` (its place in
the roster is [Scripts](../reference/scripts.md)). It is
deterministic: the same render gives the same file every time, and
no model takes part. It installs nothing. What it needs, Pillow and
ffmpeg on the PATH, is said by the shared tools module beside it, as
it is said for pandoc.

The script reads the render: the front-matter for the language, the
cards, and the scenes with their captions and terminal blocks. From
them it computes a timeline:

- the typing of a line
- the stand before Enter
- the reveal of an answer
- the hold for reading
- the breath at a scene's end

The pace of reading is three rates in words a second: one for the
principal's lines (the principal is the person whose thinking is
forged), one for Claude's answers, one for the lines that only report
a file. The defaults are 4, 8 and 16. The pace, the look of the
terminal, the date shown in the tab bar and the labels of the captions
by language stand in the recipe's Format section. They reach the
script as its arguments and never appear in the render. The parsing
of the screenplay and the pace live in the script alone; the player
page plays what the script computed.

For `video` the script paints every frame with Pillow as a simulated
terminal, 1280 by 890 pixels, with a monospace font for the terminal
and a sans font for the caption band, and fallbacks where the Windows
fonts are missing. It pipes the frames into ffmpeg, which encodes
H.264 at 30 frames a second.

For `html-player` the script writes the timeline as JSON events,
wrapped in a script call, so that the page plays the file from disk
as well as from GitHub Pages. The file lands beside the render with
the render's basename, unless the recipe's `output:` names another
path. Where that path lies under the engine's `docs/videos/`, the
script also writes the player page, `docs/videos/index.html`, anew
from its skeleton, `templates/html-player.html`, with the list of the
folder's files embedded. The list is embedded because GitHub Pages
cannot list a folder. The skeleton holds two placeholders, one for the
list of files and one for a script tag per file; the served page is
never edited by hand and never by a model. What is edited is the
skeleton.

The player page is a single file with no dependency beyond the
browser. It offers:

- a sidebar listing the videos by title, in the order of their file
  names, grouped under the section of the course each file names,
  with the section's name in each language; a recipe may give, in
  place of the title, one line of what the viewer will learn
- the simulated terminal with its caption band and its cards
- play and pause
- speed
- the scenes of a video as chapters
- the language, where a video has siblings in other languages
- three font sizes, remembered in the browser

The public folder `docs/videos/` is flat. Its files lie in the order
of their names, and a recipe that sends a file there gives it a
number for the order of the course. Video files (`.mp4`) never enter
the tree: a video goes out as an asset of a release. The reason is
not recorded. GitHub Pages is switched on once by the principal, by
hand, on `main` and the `/docs` folder; an empty `docs/.nojekyll`
makes Pages serve the files as they lie. The documentation keeps
being read in the repository view as before.

A video kept for the company names no `output:` and stays in the
project's `renders/`.

## Why

**Why the caption and the terminal are two parts.** The caption is
the teaching and the terminal the evidence: the viewer sees what the
forge does and reads, at the same moment, why it does it so.

**Why one script makes both formats.** The parsing of the screenplay
and the pace are one mechanism. Two scripts would carry that
mechanism twice; one script with two formats was chosen against two
scripts for that reason.

**Why the Format section never reaches the render.** The render
carries content only. If the pace and the look stood in the render,
the plain file would carry the instructions as text.

**Why no model in it, and no published file.** The plain file of a
screenplay is made by a deterministic script, so that the same render
gives the same file every time. There is no designed step a model
could add, so `/publish` has no part. The two steps of an output in
general, a plain file by a script and a designed file by a model, are
divided by cost; what that division was chosen against is not
recorded.

**Why Pillow and ffmpeg.** The alternatives weighed were VHS,
asciinema with agg, and a browser driven by Playwright. VHS was found
broken on Windows; agg ends at a GIF; the browser was the most code.
A painter in the language the scripts already are, with one encoder,
was the least to install and runs on the three platforms the forge
runs on.

**Why the translations are cut from the primary.** The quotes of a
transcript, the beats and the captions are chosen once. A second
generation would choose them again, differently, and the languages
would show different videos.

**Why the engine hosts what a project shows in public.** The engine
is public on GitHub and served by GitHub Pages from `docs/`, so it is
the one public place of an instance (one installation of the forge).
The project that made the file stays where its sources require, in a
private repository; why that is so is explained in
[Projects and the engine](projects-and-the-engine.md). The engine
carries the file only. The recipe, the render, the provenance and the
history stay in the project, and whoever has the project regenerates
the file. What goes out is chosen in the recipe, video by video, and
the file is read by the principal before the engine is saved. That
reading is the clearing of a public version, one step.

**Why the folder is foreign to the documentation.** `docs/videos/` is
not a page of the documentation. The documentation's planner, its
index, its state and its check read `docs/` without `docs/videos/`,
generate and verify the documentation around it and leave it alone,
and the index of the documentation does not list it.

**Why a fixed page with the list embedded.** It was weighed against a
generated index file beside the page, against a course recipe with an
outline, and against folders as sections. The principal chose the
order of file names for now; the shape of a course beyond that is
still open. The price is that the script touches a page of the
engine.

**Why a single file.** A page with scripts and styles beside it was
the alternative. One file is one thing to serve and to copy.

## A worked example

One scene of a screenplay, generic, from no project. The scene is
pinned to the time of day of its first line. The caption carries its
two parts. The fenced block shows what the terminal showed: the
principal's line as typed, a tool call as one dim line, and Claude's
answer cut to the sentences that carry the move.

```
## 14:32

Now: The principal asks for the state map of the project and Claude
reads it from the documents, not from memory.
Why: The ledger is made at read time, so what the map says is what
the files say.

~~~
> /forge my-project

  Read projects/my-project/ledger.md

  The intent is at 0.4, two threads open. The assignment is not
  started. Shall we work the oldest thread first?
~~~
```

The same scene, in a second language of the recipe, is the same
scene: the same time, the same lines of the terminal, the caption
translated. The script computes the same timeline for both, from the
same pace.

## See also

- [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md): the job from the recipe to the played file.
- [Renders and recipes](renders-and-recipes.md): the render and its recipe, which a screenplay is one of.
- [Projects and the engine](projects-and-the-engine.md): why the engine is public and a project is a repository of its own.
- [Scripts](../reference/scripts.md): the script that makes both formats.
- [Recipe genres](../reference/recipe-genres.md): the genre's checklist in full.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
