---
generated: 2026-11-01
version: 6.4
made: derived
inputs-hash: 3483f81b8c282de1
inputs:
  - .claude/skills/recipe/genres/screenplay.md
  - templates/recipe-screenplay.md
  - .claude/skills/render/SKILL.md
  - scripts/md2video.py
  - projects/forge/10-intent.md#POS.1540
---

# Make a teaching video from a recipe

A teaching video in the forge is a cut of real work in the terminal.
It is written as a screenplay from session records, and a script makes
it into a video or into a file for the player page. This page walks
you through the whole job, from registering the records to the
finished file. It is for the principal (the person whose thinking is
forged and who decides everything in it). What a screenplay is and why
one script makes both formats is explained in
[The screenplay and its player](../about/the-screenplay-and-its-player.md).

## When to use it

Use it when you want to show how the forge is used, with real work
rather than a demo. The material is the record of one or more
sessions (a session is one sitting of work with Claude in the
terminal), registered as a source of the project.

The result is one of two formats, never both:

- `video`: an MP4 of a simulated terminal.
- `html-player`: a file of timed events that the engine's player page,
  `docs/videos/index.html`, plays in the browser.

`/publish` has no part in this job. A screenplay has no designed file.

## The command

The job runs through three commands, in this order:

```
/ingest sources/<transcript>.md <slug>
/recipe screenplay <slug>
/render <recipe> <slug>
```

`<slug>` is the short name of your project. `<recipe>` is the name you
give the screenplay recipe.

## What happens

1. **Register the session records and write the brief.** Register the
   transcript of the sessions as a source with `/ingest` (how is said
   in [Register a source](register-a-source.md)). Every line the
   terminal shows in the video comes from this source, found by its
   timestamps. Beside it stands a brief of the videos, such as
   `00-brief-<videos>.md`: who watches, what the videos are for and
   which principles they show.
   You should now see the transcript under the project's `sources/`
   and the brief of the videos in the project's root.

2. **Compose the recipe with `/recipe screenplay`.** The recipe is the
   file a render is made from (see the [Glossary](../reference/glossary.md)).
   Claude runs the genre interview (described in
   [Compose a recipe](compose-a-recipe.md)) and asks you, one point at
   a time, through this checklist:
   - Audience and register: who watches, whether they have seen
     Claude Code, how the captions speak.
   - Purpose and the one message: what the viewer leaves with, said on
     the end card.
   - Inputs: the transcript and its sessions, the brief, and a
     document the video shows being born, cited by path.
   - The beats: the scenes, each pinned by the time of day of its
     first line, and the lines that must appear.
   - The quotes: what is corrected in your lines (gross errors only),
     which of Claude's answers are shown in full and which are cut.
   - Length: minutes of video, and what is shortened when there is too
     much (Claude's lines, never yours and never the captions).
   - The title card: real work, how many sessions and hours, times
     real, lines verbatim and shortened.
   - What must not appear: names, companies, hosts, paths outside the
     forge.
   - Languages: the primary language (the language of the sessions)
     first, then the translations made from it.
   - Pace and look: three reading rates in words a second (your lines,
     Claude's answers, lines that only report a file; 4, 8, 16 unless
     you want otherwise), the date shown in the tab bar, the labels of
     the captions by language.
   - Format: `video` or `html-player`.
   - For `html-player` only: whether the file goes out to the engine's
     `docs/videos/` through the recipe's `output:` (with a number that
     sets its place in the course) or stays in the project's
     `renders/`; and the section of the course on the player page with
     the video's name in each language.
   Claude then composes the recipe from the template
   `templates/recipe-screenplay.md`. The choice of format, the pace,
   the date and the course entries go into its `## Format` section.
   You should now see `recipes/<recipe>.md` with `languages:` in its
   front-matter, the sections Inputs, Instructions, Format and
   Template, and an `output:` line only if the file is to go public.

3. **Render the screenplay with `/render <recipe>`.** A subagent (a
   separate Claude that sees only the recipe and its inputs, never your
   conversation) writes the primary render first and then each
   translation, scene for scene and line for line. The render is
   Markdown only. The `## Format` section is never copied into it. More
   on rendering is in [Render an output](render-an-output.md).
   You should now see one `renders/<recipe>.<lang>.md` per language,
   each with a title card, a card of what the viewer will see, scenes
   with a time of day and a caption of two parts (Now and Why), and an
   end card.

4. **The format file is made.** In the same run Claude calls
   `python scripts/md2video.py` on each language's render, with the
   format, the pace and the date the Format section names. For
   `html-player` it also passes the section of the course and that
   language's name. The script's options and what it needs are listed
   on [Scripts](../reference/scripts.md). Where the file lands depends
   on the format and the recipe:
   - `video`: `renders/<recipe>.<lang>.mp4`, beside the render.
   - `html-player` without `output:`: `renders/<recipe>.<lang>.html-player.js`,
     beside the render.
   - `html-player` with `output:`: the engine's `docs/videos/`, under
     the name `output:` gives. The script then writes the player page
     `docs/videos/index.html` anew, with every player file of the
     folder listed in the order of the file names. The Markdown render
     stays in the project's `renders/`.
   You should now see the script's lines in the terminal: the number
   of parts and events, the length in seconds and the language, then
   `written <file> (<size> kB)`. For a file in `docs/videos/` you also
   see `player page renewed with <n> file(s)`.

5. **Read a public file before the engine is saved.** A file sent to
   `docs/videos/` is public once the engine is saved. Read it yourself
   in the player page before you save the engine. That reading is the
   one step that clears a public version.
   You should now see the video in the player page under its section,
   with the name you gave it.

## What you have afterwards

- The recipe `recipes/<recipe>.md`, which you iterate and render again
  whenever you want the video changed.
- One screenplay render per language in the project's `renders/`.
- One format file per language: an MP4 or a player file in
  `renders/`, or a player file in the engine's `docs/videos/` with the
  player page renewed.

The engine carries only the public file. The recipe, the render and
their history stay in the project. A video kept for the company names
no `output:` and stays in the project's `renders/`.

## If something goes wrong

- Pillow or ffmpeg is missing. The screenplay render stands, the video
  is not made, and Claude says so. The script prints
  ``Pillow not found - install it with `pip install pillow`.`` or
  `ffmpeg not found on PATH - install it from https://ffmpeg.org.`
  Install what is missing and render again. The script installs
  nothing itself.
- `ffmpeg failed.`: ffmpeg stopped while the video was being written.
  The reason is not recorded.
- `--pace takes three numbers, e.g. 4,8,16.`: the pace in the Format
  section is not three numbers. Correct the recipe and render again.
- `<file> has no cards or scenes of a screenplay.`: the render does
  not have the shape of a screenplay. Render it again from the recipe.
- `the player's template <path> is missing.`: the engine's template
  `templates/html-player.html` is not there, so the player page cannot
  be renewed.

## A worked example

Here is one run for a player file that goes public, with the primary
language `<lang-a>` and one translation `<lang-b>`.

The recipe's front-matter after `/recipe screenplay <slug>`:

```yaml
---
project: <slug>
purpose: Screenplay of <the video> — <what it shows>
audience: <who watches>
version: 0.1
languages: <lang-a>, <lang-b>
output: docs/videos/<NN>-<recipe>.<lang>.html-player.js
---
```

Its Format section names `html-player`, the pace `4,8,16`, the date
for the tab bar, the section of the course and the name in each
language.

You type:

```
/render <recipe> <slug>
```

Claude writes `renders/<recipe>.<lang-a>.md` and then
`renders/<recipe>.<lang-b>.md`, translated from the first. For each it
runs a call of this shape:

```
python scripts/md2video.py projects/<slug>/renders/<recipe>.<lang-a>.md --format html-player --pace 4,8,16 --date "<date>" --section "<section>" --name "<name>" -o docs/videos/<NN>-<recipe>.<lang-a>.html-player.js
```

The terminal reports the file written and the player page renewed.
You open `docs/videos/index.html`, watch both language versions, and
only then save the engine.

For a company video, the same recipe would name no `output:`. With
the format `video`, the files would be `renders/<recipe>.<lang-a>.mp4`
and `renders/<recipe>.<lang-b>.mp4`.

## See also

- [The screenplay and its player](../about/the-screenplay-and-its-player.md): what a screenplay is, why one script makes both formats, and why the engine hosts the public files.
- [Compose a recipe](compose-a-recipe.md): the genre interview every recipe runs through.
- [Render an output](render-an-output.md): the render and its plain file.
- [Register a source](register-a-source.md): registering the session records.
- [Scripts](../reference/scripts.md): `md2video.py`, its options and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
