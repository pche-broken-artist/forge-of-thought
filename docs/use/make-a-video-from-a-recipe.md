---
generated: 2026-10-19
version: 5.26
made: derived
inputs-hash: 5ef24764c8e52478
inputs:
  - .claude/skills/recipe/genres/screenplay.md
  - templates/recipe-screenplay.md
  - .claude/skills/render/SKILL.md
  - scripts/md2video.py
  - projects/forge/10-intent.md#POS.1540
---

# Make a teaching video from a recipe

A teaching video of the forge is a cut of a real terminal
conversation with Claude. It is written first as a screenplay and
then made by a script into a video or into a file for the player
page in the browser. This page takes you through the job from end
to end: from the records of your sessions to the finished file. It
is for the principal (the person whose thinking is forged, here
you) who wants to show how the work went.

## When to use it

Use it when you want to show real work with the forge to people who
watch rather than read. A session here means one sitting of work in
the terminal with Claude, and its record is the transcript of what
was typed and answered. The video shows that work as it happened,
with a caption under each scene that says what happens and why.

## The command

The job runs in three commands, one after the other:

```
/ingest <file> <slug>
/recipe screenplay <slug>
/render <recipe> <slug>
```

`<slug>` stands for your project and `<recipe>` for the name of the
recipe you compose. `/publish` has no part in this job: a screenplay
has no designed file.

## What happens

1. **Register the session records as sources.** Run `/ingest` on
   the transcript of the sessions you want to show (see
   [Register a source](register-a-source.md)). A source is an
   external input, stored as it arrived and never edited. Every line
   the terminal shows in the video comes from this source, found by
   its timestamps. Write also the brief of the videos: the text that
   says who they are for, what they are for and which principles of
   the forge they show.
   You should now see the transcript in the project's `sources/`,
   with its entry in the resource index.

2. **Compose the recipe.** Run `/recipe screenplay <slug>`. A recipe
   is the versioned file that says how a render is made: its inputs,
   its instructions, its format and its template. Claude runs the
   genre interview (see [Compose a recipe](compose-a-recipe.md)): it
   asks, offers options with their trade-offs, and you decide. The
   questions follow this checklist:
   - **Audience and register:** who watches, whether they have seen
     Claude Code, and how the captions speak.
   - **Purpose and the one message:** what the viewer leaves with,
     said on the end card.
   - **Inputs:** the transcript and the sessions in it, the brief of
     the videos, and a document the video shows being born, named by
     its path.
   - **The beats:** the scenes, each pinned by the time of day of its
     first line, and the lines that must appear, so that every render
     is the same cut; and what is left out.
   - **The quotes:** your lines as typed, with gross errors only
     corrected; which of Claude's answers are shown in full; tool
     calls as one dim line, tool output and permission prompts not at
     all.
   - **Length:** the minutes of video, and what is shortened when
     there is too much (Claude's lines, never yours and never the
     captions).
   - **The title card:** the disclosure that this is real work, how
     many sessions and hours, the times real, the lines verbatim and
     shortened.
   - **What must not appear:** names, companies, hosts and paths
     outside the forge.
   - **Languages:** the primary language first (the language of the
     sessions), then the translations made from it in the same run.
   - **Pace and look:** the three reading rates in words a second
     (your lines, Claude's answers, the lines that only report a
     file; 4, 8 and 16 unless you want otherwise), the date shown in
     the tab bar, and the labels of the captions by language.
   - **Format:** `video` or `html-player`, one of them, never both.
     For `html-player` you also decide whether the file goes out to
     the engine's public folder `docs/videos/` by an `output:` line,
     with a number in its name for the order of the course, or stays
     in the project's `renders/`.

   Claude then composes the recipe from the screenplay template.
   You should now see `recipes/<recipe>.md` with `languages:` in its
   front-matter, the beats under Instructions and a `## Format`
   section naming the format, the pace and the date.

3. **Render the screenplay.** Run `/render <recipe> <slug>` (see
   [Render an output](render-an-output.md)). Claude writes the
   screenplay in isolation, that is, by a separate agent that reads
   only the recipe and its inputs. The primary language comes first,
   then each translation as a file of its own, scene for scene and
   line for line; nothing is re-cut. The screenplay holds a title
   card, a card of what the viewer will see, the scenes with their
   time of day, a caption of two parts (Now and Why) and a block of
   what the terminal shows, and an end card. Claude then scans each
   file for the facts of your instance (one installation of the
   forge, with its names and hosts); a hit is said aloud and you
   judge it.
   You should now see one render per language,
   `renders/<recipe>.<lang>.md`, each opening with its provenance;
   a translation names the primary render it was made from.

4. **The format file is made.** In the same run Claude runs
   `python scripts/md2video.py` on each language's render, with the
   format, the pace and the date the Format section names (see
   [Scripts](../reference/scripts.md)). The script prints how many
   parts, events and seconds the render holds, and its language.
   - For `video` it paints every frame as a simulated terminal and
     writes an MP4 beside the render: `renders/<recipe>.<lang>.mp4`.
   - For `html-player` it writes the timed events as
     `<recipe>.<lang>.html-player.js`, beside the render or at the
     recipe's `output:` path in `docs/videos/`. Where the file lands
     in `docs/videos/`, the script also writes the player page
     `docs/videos/index.html` anew, with every player file of the
     folder listed in the order of their names.

   You should now see a line `written <file> (<size> kB)`, and for a
   file in `docs/videos/` also `player page renewed with <n>
   file(s)`.

5. **Read a public file before you save the engine.** A player file
   in `docs/videos/` is public once the engine is saved. Read it
   first: that reading is the clearing of the public version, one
   step. A video kept for the company names no `output:` and stays
   in the project's `renders/`.
   You should now have read the file and either saved the engine or
   changed the recipe and rendered again.

## What you have afterwards

- `recipes/<recipe>.md`, the recipe you iterate whenever the video
  should change.
- `renders/<recipe>.<lang>.md`, one screenplay per language. It is
  never edited by hand; you change the recipe and render again.
- The format file of each language: `renders/<recipe>.<lang>.mp4`,
  or `<recipe>.<lang>.html-player.js` in `renders/` or in the
  engine's `docs/videos/`.
- For a file in `docs/videos/`: the player page
  `docs/videos/index.html`, renewed with the folder's files. The
  engine carries the file only; the recipe, the render and their
  history stay in the project.

## If something goes wrong

- **Pillow or ffmpeg is missing.** The render stands, the video is
  not made, and Claude says so aloud. The script prints
  ``Pillow not found - install it with `pip install pillow`.`` or a
  message that begins `ffmpeg not found on PATH` and says where to
  install it from. The script installs nothing itself.
- **`ffmpeg failed.`** ffmpeg stopped while writing the video.
- **`<render> has no cards or scenes of a screenplay.`** The file
  the script was given is not a screenplay of the genre: its
  headings do not match the template.
- **`--pace takes three numbers, e.g. 4,8,16.`** The pace in the
  Format section is not three numbers separated by commas.
- **`the player's template ... is missing.`** The player page could
  not be renewed because `templates/html-player.html` is not in the
  engine.
- **The look is wrong.** Paint a single frame to check it without
  making the whole video:
  `python scripts/md2video.py renders/<recipe>.<lang>.md --format video --frame <seconds> check.png`.

## A worked example

You have a transcript of two sessions and want a player file in two
languages, `<primary>` and `<other>`, published as the first video of
the course.

1. `/ingest <transcript>.md <slug>` registers the transcript; you
   write the brief of the videos.
2. `/recipe screenplay <slug>` runs the interview. You choose
   `html-player`, the languages `<primary>, <other>`, the default
   pace and the date for the tab bar. The recipe's front-matter
   carries:

   ```
   languages: <primary>, <other>
   output: docs/videos/01-<recipe>.<lang>.html-player.js
   ```

3. `/render <recipe> <slug>` writes `renders/<recipe>.<primary>.md`
   and `renders/<recipe>.<other>.md`, then runs for each:

   ```
   python scripts/md2video.py renders/<recipe>.<primary>.md --format html-player --pace 4,8,16 --date "<date>" -o docs/videos/01-<recipe>.<primary>.html-player.js
   ```

   The script reports `written ...` and `player page renewed with 2
   file(s)`.
4. You read both files in `docs/videos/` and then save the engine.

## See also

- [The screenplay and its player](../about/the-screenplay-and-its-player.md):
  what a screenplay is, why one script makes both formats, and why
  the engine hosts the public files.
- [Compose a recipe](compose-a-recipe.md): the genre interview every
  recipe runs through.
- [Render an output](render-an-output.md): the render and its plain
  file.
- [Register a source](register-a-source.md): registering the session
  records.
- [Scripts](../reference/scripts.md): `md2video.py`, its options and
  what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-19 for version 5.26 from the files the
front-matter names; never edited by hand.
