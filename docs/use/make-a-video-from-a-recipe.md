---
generated: 2026-10-25
version: 6.0
made: derived
inputs-hash: 29744a52a2f9c74f
inputs:
  - .claude/skills/recipe/genres/screenplay.md
  - templates/recipe-screenplay.md
  - .claude/skills/render/SKILL.md
  - scripts/md2video.py
  - projects/forge/10-intent.md#POS.1540
---

# Make a teaching video from a recipe

A teaching video in the forge is a cut of real terminal sessions with
Claude, written as a screenplay and turned into a video file or into a
file for the player page in the browser. This page takes you through
the whole job, from the session records to the finished file. It is
for the principal, that is the person whose thinking is forged in the
project, and for anyone who makes such a video for him. What a
screenplay is and why one script makes both formats is explained in
[The screenplay and its player](../about/the-screenplay-and-its-player.md).

## When to use it

Use it when you want to show how the forge is used, with real work
rather than a demo. The material is one or more sessions: a session is
one working conversation with Claude in the terminal, and its record is
a transcript of what was typed and answered.

## The command

The recipe is composed once, then rendered as often as you like:

```
/recipe screenplay <slug>
/render <recipe> <slug>
```

`<slug>` is your project, `<recipe>` the name of the screenplay recipe.

## What happens

1. **Register the session records and write the brief.** Store the
   transcript of the sessions as a source of the project with
   `/ingest`, as [Register a source](register-a-source.md) shows; a
   source is an external input, kept unchanged once registered. Write
   the brief of the videos: who they are for, what they are for, which
   principles of the forge they show.
   You should now see the transcript in `sources/` with its entry in
   `sources/00-INDEX.md`, and the brief in the project.

2. **Compose the recipe.** Run `/recipe screenplay <slug>`. A recipe
   is the versioned file that says how a render is made; the render is
   the generated output. Claude interviews you through the genre's
   checklist, as [Compose a recipe](compose-a-recipe.md) describes, and
   the decisions are yours. It asks about:
   - the audience and the register: who watches, whether they have
     seen Claude Code, how the captions speak (plain, factual, no
     praise of the tool);
   - the one message: what the viewer leaves with, said on the end
     card;
   - the inputs: the transcript, the brief, and any document the video
     shows being born, named by its path;
   - the beats: the scenes pinned by the time of day of their first
     line, and the lines that must appear, so that every render is the
     same cut;
   - the quotes: your lines as typed, with gross errors only corrected;
     which of Claude's answers are shown in full and which are cut to
     the sentences that carry the move;
   - the length in minutes, and what is shortened when there is too
     much (Claude's lines, never yours and never the captions);
   - the title card: the disclosure that this is real work, how many
     sessions and hours, the times real, the lines verbatim and
     shortened;
   - what must not appear: names, companies, hosts, paths outside the
     forge;
   - the languages: the primary first (the language of the sessions),
     then the translations made from it;
   - the pace and the look: three reading rates in words a second (your
     lines, Claude's answers, lines that only report a file; 4, 8, 16
     unless you want otherwise), the date shown in the tab bar, the
     labels of the captions by language;
   - the format: `video` or `html-player`, one of them, never both.

   For `html-player` it asks two things more:
   - whether the file goes out to the engine's public folder
     `docs/videos/` by an `output:` line in the recipe, with a number
     that sets its place in the course, or stays in the project's
     `renders/`;
   - the section of the course the video belongs to, and its name per
     language: what the viewer will learn, listed on the player page in
     place of the title.

   You should now see `recipes/<recipe>.md`, with its inputs, its
   instructions, a `## Format` section and the template of the
   screenplay.

3. **Render the screenplay.** Run `/render <recipe> <slug>`. Claude
   hands the work to a subagent, that is a separate Claude that sees
   only the recipe and its inputs and never your conversation. It
   writes the screenplay in the primary language first, then each
   translation as a file of its own, scene for scene and line for line.
   The Markdown render always stays in the project's `renders/`, one
   file per language. Claude then scans each file for the instance's
   facts and says aloud any hit; you judge it.
   You should now see `renders/<recipe>.<lang>.md` for each language,
   each opening with its provenance; a translation names the primary
   render it was made from.

4. **Make the format file.** In the same run, `/render` runs
   `python scripts/md2video.py` on each language's render with the
   format, the pace and the date the recipe's `## Format` section
   names, and for `html-player` that section of the course and that
   language's name. The script prints the number of parts, events and
   seconds and the language, then `written <file>` with its size.
   You should now see one of these:
   - for `video`: `renders/<recipe>.<lang>.mp4` beside the render;
   - for `html-player` without `output:`:
     `renders/<recipe>.<lang>.html-player.js` beside the render;
   - for `html-player` with `output:`: the file in `docs/videos/`, and
     the line `player page renewed with <n> file(s)`, because the
     script writes the player page `docs/videos/index.html` anew with
     every file of the folder listed.

5. **Read a public file before the engine is saved.** A file sent to
   `docs/videos/` becomes public once the engine is saved. Read it
   yourself first: that reading is the clearing of the public version.
   A video kept for the company names no `output:` and stays in the
   project's `renders/`.
   You should now see the video in the player page and be content to
   publish it.

`/publish` has no part in this job: a screenplay has no designed file.

## What you have afterwards

- The recipe `recipes/<recipe>.md` with its history, iterated and
  rendered again whenever you like.
- One screenplay render per language in `renders/`, the source of the
  video and never edited by hand.
- One format file per language: an MP4, or a player file in `renders/`
  or in the engine's `docs/videos/`.

The engine carries only the public player file. The recipe, the
render, the provenance and the history stay in the project, and
whoever has the project can make the file again. The same render gives
the same video every time.

## If something goes wrong

- **Pillow or ffmpeg is missing.** The render stands, the video is not
  made, and Claude says so. The script says
  ``Pillow not found - install it with `pip install pillow`.`` or
  `ffmpeg not found on PATH - install it from https://ffmpeg.org.`
  Install what it names; the script installs nothing. What it needs in
  full is listed under `md2video.py` in [Scripts](../reference/scripts.md).
- **`ffmpeg failed.`** The video encoder stopped with an error; the
  file is not made.
- **`--pace takes three numbers, e.g. 4,8,16.`** The pace in the
  recipe's `## Format` section is not three numbers separated by
  commas. Correct the recipe and render again.
- **`<file> has no cards or scenes of a screenplay.`** The render does
  not have the screenplay's shape: no title card, cards or scenes the
  script can read. Check that the recipe is of the screenplay genre and
  render again.
- **`the player's template ... is missing.`** The skeleton of the
  player page, `templates/html-player.html`, is not in the engine; the
  page cannot be renewed.
- **The look is wrong.** You can paint one frame without the whole
  video: `python scripts/md2video.py renders/<recipe>.<lang>.md
  --format video --frame <seconds> check.png`.

## A worked example

A project `<slug>` has a recipe `<recipe>` in two languages, `<xx>`
primary and `<yy>` its translation, format `html-player`, sent out to
the course with this line in its front-matter:

```
output: docs/videos/<NN>-<recipe>.<lang>.html-player.js
```

Its `## Format` section names the pace 4,8,16, the date for the tab
bar, the section of the course and the name per language. You run:

```
/render <recipe> <slug>
```

The run writes `renders/<recipe>.<xx>.md` and then
`renders/<recipe>.<yy>.md`. For each, it runs a line of this shape:

```
python scripts/md2video.py renders/<recipe>.<xx>.md --format html-player --pace 4,8,16 --date "<date>" --section "<section>" --name "<name>" -o docs/videos/<NN>-<recipe>.<xx>.html-player.js
```

Each run ends with `written ...` and `player page renewed with <n>
file(s)`. You open `docs/videos/index.html`, watch both files, and only
then save the engine. Had the recipe named `video` and no `output:`,
the same run would have left `renders/<recipe>.<xx>.mp4` and
`renders/<recipe>.<yy>.mp4` beside the renders.

## See also

- [The screenplay and its player](../about/the-screenplay-and-its-player.md):
  what a screenplay is, why one script makes both formats, and why the
  engine hosts the public files.
- [Compose a recipe](compose-a-recipe.md): the genre interview every
  recipe runs through.
- [Render an output](render-an-output.md): the render and its plain
  file.
- [Register a source](register-a-source.md): registering the session
  records.
- [Scripts](../reference/scripts.md): `md2video.py`, its options and
  what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.0 from the files the
front-matter names; never edited by hand.
