---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: f0862a828f85737b
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

A teaching video of the forge is a screenplay of a real terminal
conversation, cut from the records of working sessions, and made
into a watchable file by one script. This page says what a
screenplay is made of, how its two formats come out of one script,
what the player page of the engine is, and why the engine hosts what
a project shows in public. It is written for the user who wants to
understand what he is making, for the extender who touches the
script or the page, and for the evaluator who wants to see why it is
built this way. The job itself, from the recipe to the played file,
is [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md).

## What it is

A screenplay is a [render](renders-and-recipes.md) of a recipe of
the genre `screenplay`. A render is an output generated from a
recipe, and the recipe is what is iterated, never the output. A
screenplay renders a terminal conversation between the principal
(the person whose thinking is being forged) and Claude as a sequence
of cards and scenes:

- a title card, which discloses the composition: real work, how many
  sessions, how many hours, the times real, the lines verbatim and
  shortened
- a card of what the viewer will see
- scenes, each with the real time of day, a caption of two parts and
  a fenced block of what the terminal shows
- an end card, which says the one message the viewer leaves with

The caption of a scene has two parts. "Now" says what happens in the
scene. "Why" says why the forge does it this way. The caption is the
teaching; the terminal block is the evidence.

The inputs of a screenplay are session records registered as sources
and the brief that says what the videos are for. A session is one
working conversation with Claude; its record is a transcript extract,
cut by timestamps. A document the video shows being born may be named
as a dependency by path.

The render is never the video. The recipe's Format section names one
of two formats, never both:

- `video`: an MP4, painted frame by frame as a simulated terminal
- `html-player`: the timed events of the screenplay, written as a
  file the player page of the engine loads,
  `renders/<recipe>.<lang>.html-player.js`

Both formats are made by one script, `scripts/md2video.py`
([Scripts](../reference/scripts.md)). The script is deterministic:
the same render gives the same file every time, with no model in it.
The file is the plain file of `/render`. There is no designed step
and no published file: `/publish` has no part in a screenplay.

The player page is one fixed file of the engine,
`docs/videos/index.html`. It is a single file with no dependency
beyond the browser. It shows a sidebar of the videos by title, the
simulated terminal with its caption band and its cards, play and
pause, a choice of speed, the scenes of a video as chapters, a choice
of language where a video has siblings in other languages, and three
font sizes, remembered in the browser. The page is written anew from
its skeleton, `templates/html-player.html`, by the script; it is never
edited by hand and never written by a model.

## How it works

### The recipe and the cut

The recipe is composed through the genre interview of `/recipe`
([Recipe genres](../reference/recipe-genres.md) carries the checklist
in full). The interview fixes the audience and the register of the
captions, the one message of the end card, the inputs, the beats, the
quotes, the length, the title card, what must not appear, the
languages, the pace and the look, and the format.

The beats are pinned by the time of their first line and by the lines
that must appear. So every render is the same cut. The principal's
lines are shown as typed; only gross errors are corrected, and the
speed and the missing diacritics are kept. Claude's answers are shown
in full where the scene is about them. The rest are cut to the
sentences that carry the move. A tool call is one dim line. Tool
output and permission prompts do not appear. Where there is too much
for the length, Claude's lines are shortened, never the principal's
and never the captions. Names, companies, hosts and paths outside the
forge never appear: the facts of an instance (one installation of the
forge) are never material.

### Languages

A recipe declares its output languages in `languages:`. The first is
the primary language, that is the language of the sessions; the rest
are its translations. `/render` generates the primary render and, in
the same run, translates it into every other language, scene for
scene and line for line. One render per language is written,
`renders/<recipe>.<lang>.md`, each with its own provenance and its own
row in the Renders table of the ledger (the project's one file of
state). A translation cites the primary render it was made from. The
format file follows the name of its render. A recipe with one
language keeps `renders/<recipe>.md`. The notation of a render stays
English; its content is in the render's language.

### The script

The script reads the render: the front-matter for the language, the
cards, the scenes with their captions and their terminal blocks. From
them it computes the timeline: the typing of a line, the stand before
Enter, the reveal of an answer, the hold for reading, the breath at a
scene's end. The pace is three reading rates in words a second, one
for the principal's lines, one for Claude's answers and one for the
lines that only report a file; the defaults are 4, 8 and 16. The
labels of the captions are given by language. The pace, the date
shown in the tab bar and the labels stand in the recipe's Format
section and reach the script as its arguments. The render carries
none of it.

For `video` the script paints every frame as a simulated terminal, a
monospace font for the terminal and a sans font for the caption band,
with fallbacks where the usual fonts are missing, and pipes the
frames into ffmpeg as H.264 at 30 frames a second. For `html-player`
it writes the timeline as events in a file the player page loads.
What the script needs installed, Pillow and ffmpeg on PATH, is said
by the shared module `scripts/forge_tools.py`, as it says for pandoc;
the script installs nothing.

The file lands beside the render with the render's basename, unless
the recipe's `output:` names another path. Where that path lies under
the engine's `docs/videos/`, the script also renews the list of files
in `docs/videos/index.html`, by writing the page anew from its
skeleton with the list of the folder's player files in it.

### The player page and the public folder

The player page groups the files of the folder by video: a video has
one player file per language, told apart by the language in the file
name. The sidebar lists the videos in the order of their file names,
each by the title of its title card. Under a title the scenes of the
video fold out as chapters; choosing one jumps to it. Where a video
has siblings in other languages, the page offers the language; the
chosen language is kept while another video is opened. A video can be
opened by its name in the address, so one video can be linked. The
data of each video arrive with the player file itself, so the page
plays from a file on disk as well as from GitHub Pages.

The engine's `docs/videos/` is the public folder. It is flat. It is
foreign to `/document` and its scripts: the planner, the index, the
state and the check of the documentation read `docs/` without
`docs/videos/`, and the index of the documentation does not list it.
An empty `docs/.nojekyll` makes GitHub Pages serve the folder as it
lies. GitHub Pages is switched on by the principal once, by hand, on
`main` and `/docs`; the documentation keeps being read in the
repository view as before. Video files (`.mp4`) are never written
into the folder: a video goes out as an asset of a release.

### Going public

A project's recipe may send its format file out of the project into
the engine's repository by its `output:` path, into `docs/videos/`.
The engine carries the file only. The recipe, the render, the
provenance and the history stay in the project, and whoever has the
project regenerates the file. A video kept inside the company names
no `output:` and stays in the project's `renders/`. What goes out is
chosen in the recipe, video by video. The file is read by the
principal before the engine is saved; that reading is the clearing of
a public version, one step.

## Why

The caption carries the teaching and the terminal shows the evidence:
the captions are what the viewer learns from, the terminal block is
the real work they speak of, shortened but never composed. Why the
title card discloses the composition is not recorded.

One script makes both formats, against two scripts, because the
parsing of the screenplay and the pace are one mechanism. The player
page plays what the script computed; it computes nothing of the cut
itself.

The script has no model in it, and `/publish` has no part, because
there is no designed step a model could add: the same render must
give the same file every time.

The pace and the look stand in the recipe's Format section and not in
the render. The reason for this placement is not recorded in the
inputs of this page.

The translations are made in the same run as the primary, scene for
scene and line for line, because the quotes of a transcript, the
beats and the captions are chosen once; a second generation would
choose them again, differently, and the cut would no longer be the
same.

The painter is written in Python with Pillow and encoded by ffmpeg,
against VHS, asciinema with agg, or a browser driven by Playwright.
The research behind the choice found VHS broken on Windows, agg
ending at a GIF and the browser the most code to write. A painter in
the language the scripts already are, with one encoder, was the least
to install and runs on the three platforms the forge runs on.

The engine hosts what a project shows in public, because the engine,
public on GitHub and served by GitHub Pages from `docs/`, is the one
public place of an instance, while the project that made the file
stays in a private repository where its sources require
([Projects and the engine](projects-and-the-engine.md) says why the
engine is public and a project is a repository of its own). The
engine carries the file only, so that the recipe, the provenance and
the history stay with the project that owns them.

The list of files is embedded in the page and renewed by the script,
because GitHub Pages cannot list a folder. A fixed page with the list
embedded was chosen against a generated index file beside it, a
course recipe with an outline, or folders as sections. The principal
chose the order of file names for now; sections and the order of a
course are an open matter. The price is that the script touches a
page of the engine.

The page is a single file, against a page with scripts and styles
beside it, because one file is one thing to serve and to copy. It is
never edited by hand, so that the skeleton stays the one place it is
made from; it is a file of the engine, versioned by git like a
script.

Video files never enter the tree. The reason is not recorded beyond
that a video goes out as an asset of a release.

## A worked example

One scene of a screenplay, as the render would carry it. The exact
headings and labels are the skeleton's; the shape is this: the time
of day, the two-part caption, the terminal block.

````markdown
## Scene 3 (09:41)

Now: The principal asks for the state map of his project. Claude
reads the ledger and answers with the artefacts the project has and
where each stands.

Why: The forge keeps the state of a project in one file, the ledger,
so that a question of "where are we" is answered from a file and
never from memory.

```
> /forge my-project

  Read ledger.md                                               ok

my-project has a brief (0.2, draft) and an intent (1.0, approved).
Two threads are open, both on the intent. No layer below the intent
exists; none is missing.

Shall I iterate the intent on the open threads?
```
````

In the `video` format this scene becomes a run of frames: the line is
typed into the box at the principal's reading rate, the dim tool line
appears, the answer is revealed paragraph by paragraph at Claude's
rate, and the frame holds for reading. In the `html-player` format the
same run is a list of timed events, and the player page plays them
with the caption in its band and `09:41` in the tab bar.

## See also

- [Make a teaching video from a recipe](../use/make-a-video-from-a-recipe.md): the job from the recipe to the played file.
- [Renders and recipes](renders-and-recipes.md): the render and its recipe, which a screenplay is one of.
- [Projects and the engine](projects-and-the-engine.md): why the engine is public and a project is a repository of its own.
- [Scripts](../reference/scripts.md): the script that makes both formats.
- [Recipe genres](../reference/recipe-genres.md): the genre's checklist in full.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
