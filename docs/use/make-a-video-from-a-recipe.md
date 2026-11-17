---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 9ac5d64073c475fd
inputs:
  - .claude/skills/recipe/genres/screenplay.md
  - templates/recipe-screenplay.md
  - .claude/skills/render/SKILL.md
  - scripts/md2video.py
  - projects/forge/10-intent.md#POS.1540
---

# Make a teaching video from a recipe

A teaching video of the forge is a terminal conversation cut from the
records of real sessions (working conversations with Claude in the
terminal), shown scene by scene with captions that teach. It is made
in two moves. A [recipe](compose-a-recipe.md) of the genre
`screenplay` says how the conversation is cut, and its
[render](render-an-output.md) is the
[screenplay](../about/the-screenplay-and-its-player.md). A script then
makes the screenplay into an MP4, or into a file that the player page
of the [engine](../reference/glossary.md) plays in the browser. The
engine is the forge's own repository, which is public. This page takes
you through the whole job, from the session records to that file. It
is written for the principal (the person whose thinking is forged) of
a project that has sessions worth showing: on this page that is you.

## When to use it

Use this job when you have records of real sessions and want to teach
from them. Three things say whether it fits:

- The video shows real work. Every line of the terminal comes from a
  registered record, and the title card discloses how the video was
  cut.
- The cut is fixed. The recipe pins each scene by the time of day of
  its first line, and every render is then the same cut.
- The output is one of two formats. A recipe names one of them, never
  both:
  - `video`: an MP4 of a simulated terminal, without voice-over.
  - `html-player`: the timed events of the screenplay as a file that
    the player page plays in the browser.

A screenplay has no designed file. `/publish` has no part in this job.

## The command

```
/recipe screenplay
/render <recipe> <slug>
```

The first line can be typed as it stands: `screenplay` is the genre of
the recipe. In the second line `<recipe>` is the name of the recipe
file in `recipes/` and `<slug>` is your project. The slug may be left
out: Claude takes the project from the conversation and asks where it
is not clear.

Two steps come before the commands. The session records are registered
as [sources](register-a-source.md) (the external inputs of a project),
and the [brief](../reference/glossary.md) of the videos is written.

## What happens

```
session records            the brief of the videos
      |  /ingest                     |
      v                              v
sources/<transcript>.md      00-brief-<videos>.md
       \                            /
        \    /recipe screenplay    /
         v                        v
            recipes/<recipe>.md
                    |  /render <recipe>
                    v
       renders/<recipe>.<lang>.md         one per language
                    |  python scripts/md2video.py
          +---------+-----------+
          v                     v
   Format: video          Format: html-player
   <recipe>.<lang>.mp4    <recipe>.<lang>.html-player.js
   beside the render      beside the render, or in the
                          engine's docs/videos/
```

### 1. Register the session records

Register the records of the sessions as sources with `/ingest`, as
[Register a source](register-a-source.md) describes. A record enters
as a transcript extract whose lines carry timestamps. Every line the
terminal of the video shows comes from that extract, found by the
times the recipe names.

You should now see the transcript extract in the project: a file of
the form `sources/<transcript>.md`.

### 2. Write the brief of the videos

Write the brief of the videos. It says what the videos are for: the
audience, the purpose and the principles they show. The recipe names
it among its inputs.

You should now see a file of the form `00-brief-<videos>.md` in the
project.

### 3. Compose the recipe

Type `/recipe screenplay`. Claude interviews you through the checklist
of the genre, in the way [Compose a recipe](compose-a-recipe.md)
describes for every genre. It offers options and their trade-offs, and
you make the decisions. The checklist asks for:

1. **Audience and register**: who watches, whether they have seen
   Claude Code, and how the captions speak.
2. **Purpose and the one message**: what the viewer leaves with, which
   the end card says.
3. **Inputs**: the transcript source and the sessions in it, the brief
   of the videos, and a document the video shows being born.
4. **The beats**: the scenes, each pinned by the time of day of its
   first line, with the lines that must appear and what is left out.
5. **The quotes**: what is corrected in the lines of the principal,
   and which answers of Claude are shown in full.
6. **Length**: the minutes of video, and what is shortened when there
   is too much.
7. **The title card**: the disclosure of the composition, such as the
   number of sessions and of hours.
8. **What must not appear**: names, companies, hosts and paths outside
   the forge.
9. **Languages**: the language of the sessions as the primary, named
   first, and the translations.
10. **Pace and look**: the three reading rates, the date shown in the
    tab bar and the labels of the captions by language.
11. **Format**: `video` or `html-player`.

The pace is three reading rates in words a second: one for the lines
of the principal, one for the answers of Claude, one for the lines that
only report a file. The default is 4, 8 and 16.

For `html-player` the last point holds three more answers:

- **Where the file lands**: in the engine's `docs/videos/`, by an
  `output:` line in the head of the recipe, or in the project's
  `renders/`. A video kept for the company names no `output:`.
- **The section**: the part of the course (the ordered list of videos
  on the player page) the video belongs to.
- **The name**: what the viewer will learn, one name per language. The
  player page lists it in place of the title of the title card.

The number in the file name of `output:` is the place of the video in
the course.

Claude then composes the recipe from the template
`templates/recipe-screenplay.md`. The head of the recipe carries
`languages:`. Where the player file goes out, it also carries
`output: docs/videos/<NN>-<recipe>.<lang>.html-player.js`.

You should now see `recipes/<recipe>.md` at version `0.1`, with the
sections `Inputs`, `Instructions`, `Format` and `Template`.

### 4. Render the screenplay

Type `/render <recipe>`. Claude reads the recipe and the inputs it
names. The screenplay itself is written by a subagent (a separate run
of Claude that sees only the recipe and its inputs, never your
conversation). The reason: a render is made from the documents, not
from what was said about them.

Where the recipe names several languages, the primary render is
written first. Each translation is then written as a file of its own,
scene for scene and line for line. Nothing is cut again in a
translation. Timestamps, file names, commands and the verdict line
(`(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`) stay
unchanged. The notation of the file (headings, labels, the fence of
the terminal) stays English in every language.

The screenplay always lands in the project's `renders/`. An `output:`
line in the recipe is the place of the format file only (the MP4 or
the player file, made in the next step).

Each file opens with its provenance: the recipe and the inputs it was
made from, with their versions, and its `language:`. A translation
also names the primary render in `translated_from:`. Below the
provenance stands the screenplay:

- a title card
- a card of what the viewer will see
- the scenes, each with the real time of day, a caption of two parts
  (`Now:` what happens, `Why:` why the forge does it this way) and a
  fenced block of what the terminal shows
- an end card

You should now see one file `renders/<recipe>.<lang>.md` for each
language, and Claude's report of what was rendered from what.

### 5. The format file is made

The same `/render` goes on to the format file (the plain file of a
screenplay). The render is never the video itself. Claude runs
`python scripts/md2video.py` once for each language's render and
passes what the `Format` section of the recipe names:

- the format: `video` or `html-player`
- the pace
- the date shown in the tab bar beside the time of the scene
- for `html-player`: the section of the course and the name of the
  video in that language

Where the file lands depends on the format and on `output:`:

- `video`: `renders/<recipe>.<lang>.mp4`, beside the render.
- `html-player` without `output:`:
  `renders/<recipe>.<lang>.html-player.js`, beside the render.
- `html-player` with `output:`:
  `docs/videos/<NN>-<recipe>.<lang>.html-player.js` in the engine. The
  script then writes the player page `docs/videos/index.html` anew,
  with the files of the folder listed.

The script needs Python 3.8 or newer. For `video` it also needs Pillow
and ffmpeg on PATH. It installs nothing. Its options are listed in
[Scripts](../reference/scripts.md).

For each language the script prints:

- always: `<N> parts, <N> events, <N> s, language <lang>`
- for `video`: `<N> frames, <N> s`
- for a player file in `docs/videos/`:
  `player page renewed with <N> file(s): <engine>/docs/videos/index.html`
- last: `written <file> (<N> kB)`

You should now see the line `written <file> (<N> kB)` for each
language, and the file at its place.

### 6. Read the file that goes out

This step applies only where `output:` sent the file into the engine's
`docs/videos/`. That folder is the engine's public folder: the file is
public once the engine is saved. Read the file before that. Open the
player page `docs/videos/index.html` from disk and play the video: the
page loads the files of the folder from disk as well. What goes out is
your choice in the recipe, video by video, and this reading is the
clearing of the public version.

You should now see the video on the player page, listed in its section
under the name you gave it for that language.

## What you have afterwards

| File | Where | What it is |
|---|---|---|
| `recipes/<recipe>.md` | the project | the recipe: what you change when the video is to change |
| `renders/<recipe>.<lang>.md` | the project | the screenplay, one per language |
| `renders/<recipe>.<lang>.mp4` | the project | format `video`: the MP4 |
| `renders/<recipe>.<lang>.html-player.js` | the project | format `html-player`, kept for the company |
| `docs/videos/<NN>-<recipe>.<lang>.html-player.js` | the engine | format `html-player`, sent out by `output:` |
| `docs/videos/index.html` | the engine | the player page, renewed by the script |

- The MP4 has the look of a simulated Windows Terminal (1280x890,
  H.264, 30 frames a second) and no voice-over. The languages differ
  in text only. The same render gives the same file every time.
- The engine carries the player file only. Its recipe, its render, its
  provenance and its history stay in the project, and whoever has the
  project regenerates the file.
- The player page is kept current with its folder by the script, never
  by hand.
- To change the video, change the recipe and type `/render <recipe>`
  again. Claude never renders on its own judgement. Where the version
  of the recipe or of an input differs from the one the render names,
  it reports the render as stale and offers to render.

## If something goes wrong

| What you see | What it means and what you do |
|---|---|
| Claude says `recipes/<recipe>.md` does not exist, offers `/recipe` and stops | There is no recipe of that name. Compose it with `/recipe screenplay`, then render. |
| Claude says the format file was not made | Pillow or ffmpeg is missing. The render stands. Install what is missing and type `/render <recipe>` again. |
| A message that begins `ffmpeg not found on PATH` | The format `video` needs ffmpeg on PATH. Install it by one of the lines below the table. |
| A message that begins `Pillow not found` | The format `video` paints its frames with Pillow. Install it with `pip install pillow`. |
| `ffmpeg failed.` | ffmpeg ended with an error while it encoded the frames. Look at the error lines ffmpeg itself printed. |
| `--pace takes three numbers, e.g. 4,8,16.` | The pace in the `Format` section of the recipe is not three numbers. Correct it there and render again. |
| `<render> has no cards or scenes of a screenplay.` | The script found no title card, card or scene in the file. Check that the recipe is of the genre `screenplay` and render again. |
| `the player's template <path> is missing.` | The engine's `templates/html-player.html` is not in its place. The player file is written; the player page is not renewed. |
| Claude says the render holds a fact of your instance | After rendering, Claude scans the file for facts of your [instance](../reference/glossary.md) (one installation of the forge) and says a hit aloud. You judge it. A fact of the instance is rendered out again, never edited out by hand. |
| The video is listed after the sections, under the title of its title card | The player file carries no section and no name. Name both in the `Format` section of the recipe and render again. |
| The videos of the course stand in the wrong order | The player page orders sections and videos by file name. The number in `output:` is the place in the course. |

ffmpeg is installed by:

- Windows: `winget install Gyan.FFmpeg`
- macOS: `brew install ffmpeg`
- Linux: your package manager

To check the look without making the whole video, paint one frame:

```
python scripts/md2video.py projects/<slug>/renders/<recipe>.<lang>.md --format video --frame 75 check.png
```

The script paints the frame at second 75 into `check.png`, prints
`frame at 75.0 s of <N> -> check.png` and stops.

## A worked example

A project `<slug>` has one day of sessions to show. The video is to be
public, in two languages: `<primary>` (the language of the sessions)
and `<second>`.

1. The record of the day is registered with `/ingest` and lies in the
   project as `sources/<transcript>.md`. The brief of the videos is
   written as `00-brief-<videos>.md`.

2. You type:

   ```
   /recipe screenplay
   ```

   You answer the checklist. You choose the format `html-player` and
   send the file out to the engine. Claude composes
   `recipes/<recipe>.md`. Its head and its `Format` section read:

   ```
   ---
   project: <slug>
   purpose: Screenplay of <the video> — <what it shows>
   audience: <who watches; whether they have seen Claude Code>
   version: 0.1
   languages: <primary>, <second>
   output: docs/videos/<NN>-<recipe>.<lang>.html-player.js
   ---
   ```

   ```
   ## Format
   - Format: html-player
   - Plain file, made by `/render` through `scripts/md2video.py`:
     pace 4,8,16 words a second for the principal's lines, Claude's
     answers and the lines that only report a file; the date in the
     tab bar "<date>"; the labels of the captions by language.
     The section of the course on the player page "<section>", and
     the name the page lists per language, what the viewer will
     learn (<primary> "<name>", <second> "<name>"); the number of
     `output:` is the place in the course.
     `<recipe>.<lang>.html-player.js`, played by the engine's
     `docs/videos/index.html`; where `output:` points into that
     folder, the file is public once the engine is saved.
   ```

3. You type:

   ```
   /render <recipe> <slug>
   ```

   Claude reports `renders/<recipe>.<primary>.md` and
   `renders/<recipe>.<second>.md` as written. It then runs the script
   once for each language. For the primary language the line is:

   ```
   python scripts/md2video.py projects/<slug>/renders/<recipe>.<primary>.md --format html-player --pace 4,8,16 --date "<date>" --section "<section>" --name "<name>" -o docs/videos/<NN>-<recipe>.<primary>.html-player.js
   ```

   The script prints:

   ```
   <N> parts, <N> events, <N> s, language <primary>
   player page renewed with <N> file(s): <engine>/docs/videos/index.html
   written <engine>/docs/videos/<NN>-<recipe>.<primary>.html-player.js (<N> kB)
   ```

4. You open `docs/videos/index.html` from disk, find the video in
   `<section>` under its name and read it in both languages. Then the
   engine is saved, and the file is public.

The same video kept for the company names no `output:` in the head of
its recipe. The player file then lands as
`projects/<slug>/renders/<recipe>.<primary>.html-player.js`, and the
player page is not renewed.

With `Format: video` in the recipe, the line and what it prints are:

```
python scripts/md2video.py projects/<slug>/renders/<recipe>.<primary>.md --format video --pace 4,8,16 --date "<date>"
```

```
<N> parts, <N> events, <N> s, language <primary>
<N> frames, <N> s
written <path>/renders/<recipe>.<primary>.mp4 (<N> kB)
```

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

Generated on 2026-11-17 for version 7.12 from the files the
front-matter names; never edited by hand.
