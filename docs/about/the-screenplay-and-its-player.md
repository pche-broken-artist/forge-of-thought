---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: a5af6a043a676c3e
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

A screenplay is the render of a teaching video: a terminal
conversation with Claude, cut from real session records and written
out as cards and scenes. This page explains what a screenplay is made
of, how one script turns it into a video or into a file for the
player page, and why the engine hosts the files a project shows in
public. It is for anyone who uses, extends or evaluates the forge.

## What it is

A screenplay is the render of a recipe of the genre `screenplay`. A
render is an output generated from a recipe, and a recipe is the
versioned file that says how the render is made (see
[Renders and recipes](renders-and-recipes.md)). The screenplay shows
a conversation between the principal and Claude in a terminal. The
principal is the person whose thinking is forged.

A screenplay holds these parts, in this order:

- a title card: it discloses how the video was composed (real work,
  how many sessions, how many hours, the times real, the lines
  verbatim or shortened);
- a card of what the viewer will see;
- the scenes, each with the real time of day;
- an end card: it says the one message the viewer leaves with.

Each scene carries two things:

- a caption of two parts: "Now" (what happens now) and "Why" (why
  the forge does it this way);
- a fenced block of what the terminal shows.

The caption is the teaching. The terminal is the evidence.

The inputs of a screenplay recipe are two:

- session records registered as sources (a transcript extract, cut
  by timestamps); a session is one conversation with Claude, and a
  source is an external input stored in the project as it arrived;
- the brief that says what the videos are for.

The render is never the video. The playable file is made from the
render by a script, in the format the recipe names.

## How it works

### One recipe, several languages

A recipe may declare several output languages in `languages:`. The
first is the primary; the rest are its translations. `/render`
generates the primary render and, in the same run, translates it into
every other language scene for scene and line for line. Each language
gets its own render, `renders/<recipe>.<lang>.md`, with its own
provenance. The translation cites the primary render it was made
from. A recipe with one language keeps `renders/<recipe>.md`.

### Two formats, one script

The recipe's Format section names one of two formats, never both:

- `video`: an MP4 painted frame by frame as a simulated terminal;
- `html-player`: the timed events for the player page of the engine,
  written as `renders/<recipe>.<lang>.html-player.js`.

Both are made by one script, `scripts/md2video.py` (see
[Scripts](../reference/scripts.md)). The script reads the render: its
language, its cards, its scenes with their captions and terminal
blocks. From the render it computes a timeline: the typing, the pause
before Enter, the reveal of an answer, the hold for reading and the
breath at the end of a scene. For `video` it paints every frame and
hands the frames to an encoder. For `html-player` it writes the
timeline as events wrapped in a script call. The wrapping lets the
player page play the file from disk as well as from the web.

The script is deterministic: the same render gives the same file
every time. No model runs in it. The file is the plain file of
`/render` and lands beside the render. `/publish` has no part in a
screenplay, and a screenplay has no published file.

The pace of reading and the look stand in the recipe's Format section
and reach the script as its arguments. They never stand in the render.
The pace is three reading rates in words a second:

- the principal's lines (4 by default);
- Claude's answers (8 by default);
- the lines that only report a file (16 by default).

The look covers the terminal and the labels of the captions by
language. The parsing of the screenplay and the pace live in the
script alone. The player page plays what the script computed.

What the script needs installed (Pillow, and ffmpeg on the PATH) is
said in `scripts/forge_tools.py`. The script installs nothing.

### Where a public file goes

A project's recipe may send its `html-player` file out of the project
into the engine's repository, by its `output:` path, into
`docs/videos/`. The engine carries the file only. The recipe, the
render, the provenance and the history stay in the project. Whoever
has the project can regenerate the file. A video that is not meant
for the public names no `output:` and stays in the project's
`renders/`.

What goes out is chosen in the recipe, video by video. The principal
reads the file before the engine is saved. That reading is the whole
clearing of a public version: one step.

`docs/videos/` is flat. Its files stand in the order of their names.
The folder is foreign to the documentation: `/document` and its
checks generate and verify the pages around it and leave it alone,
and the index of the documentation does not list it. Video files
(`.mp4`) never enter the repository tree. A video goes out as an
asset of a release instead. An empty `docs/.nojekyll` makes GitHub
Pages serve the folder as it lies.

### The player page

The player page is `docs/videos/index.html`, one fixed file of the
engine. It is a single file with no dependency beyond the browser. It
offers:

- a sidebar of the videos, by the title on each file's title card, in
  the order of the file names;
- the player: the simulated terminal, the caption band and the cards;
- play and pause;
- speed;
- the scenes of a video as chapters;
- the language, where a video has siblings in other languages;
- three font sizes, remembered in the browser.

The page is written anew by `scripts/md2video.py` from its template,
`templates/html-player.html`, whenever the script writes a file into
the folder. The script embeds the list of the folder's files in the
page, because GitHub Pages cannot list a folder. What is edited is the
template, never the page. No model touches either of them. The page
is tracked in git as the plain file of a render is.

## Why

**Why one script makes both formats.** The parsing of the screenplay
and the pace are one mechanism. Two scripts would hold it twice.

**Why the script paints the frames itself.** Other ways of making a
terminal video were weighed: dedicated terminal recorders and a
browser driven by a test tool. A painter in the language the scripts
are already written in, with one encoder, was the least to install
and runs on Windows, Linux and macOS.

**Why no model and no designed step.** The script makes the same file
from the same render every time. There is no designed step a model
could add, so `/publish` has no part.

**Why the pace and the look stay out of the render.** The reason is
not recorded.

**Why translations are cut from the primary.** The quotes of a
transcript, the beats and the captions are chosen once. A second
generation would choose them again, and differently. The translation
keeps the same cut, scene for scene.

**Why the engine hosts what a project shows in public.** The engine
is public and is served by GitHub Pages from `docs/`. It is the one
public place of an instance. The project that made the file stays
where its sources require it to be, such as a private repository (see
[Projects and the engine](projects-and-the-engine.md)).

**Why the list of files is embedded in a fixed page.** A generated
index file beside the page, a course recipe with an outline, and
folders as sections were weighed against it. For now the order is the
order of the file names. The price is that the script writes a page
of the engine.

**Why the page is a single file.** One file is one thing to serve and
to copy.

## A worked example

A sketch of one scene of a screenplay, generic and taken from no
project. It shows the parts a scene holds: the real time of day, the
caption of two parts and the block of what the terminal shows. The
exact layout of a scene in the render is not shown here.

```
Scene at 10:42

Now: the principal asks for the state map of a project.
Why: <why the forge does it this way, in one or two sentences>

    > /forge example-project
    <Claude's answer, cut to the sentences that carry the move>
```

The video or the player shows the terminal block typed and revealed
at the pace the recipe gives, with the caption in the caption band.

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

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
