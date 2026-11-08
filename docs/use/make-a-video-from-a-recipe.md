---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: d8a4d08f03839461
inputs:
  - .claude/skills/recipe/genres/screenplay.md
  - templates/recipe-screenplay.md
  - .claude/skills/render/SKILL.md
  - scripts/md2video.py
  - projects/forge/10-intent.md#POS.1540
---

# Make a teaching video from a recipe

A teaching video is a cut of real working sessions, shown as a
simulated terminal with a caption that explains each move. This page
is for you, the user who has the session records of a project and
wants a video or a browser player file out of them. It takes you
through the whole job in the order you do it: registering the
records, composing the screenplay recipe, rendering the screenplay
and making the format file. The principal (the person whose thinking
is forged) decides every answer of the recipe; Claude asks, proposes
and composes.

## When to use it

Use this job when a project's sessions are worth showing: a thing
was born in them that a viewer can learn from. The product is a
recipe of the genre `screenplay` ([Compose a recipe](compose-a-recipe.md)),
a render that is the screenplay, and from it one of two files:

- `video`: an MP4 of a simulated terminal, no voice-over
- `html-player`: the timed events of the screenplay, played by the
  player page of the engine, `docs/videos/index.html`

A recipe names one of the two, never both. The render is never the
video: the file is made from the render by the script
`scripts/md2video.py`. `/publish` has no part in this job: a
screenplay has no designed file.

## The command

The job is three commands, each on its own line, in this order:

```
/ingest <file> <slug>
/recipe screenplay <slug>
/render <recipe> <slug>
```

`<slug>` is the project the sessions belong to; `<recipe>` is the
name of the recipe the interview composes. `/render` runs the script
itself; you type it only where you want a check of the look or a
file made again by hand:

```
python scripts/md2video.py projects/<slug>/renders/<recipe>.<lang>.md --format video --date "<date>"
```

## What happens

1. **Register the session records as sources.** The inputs of a
   screenplay are session records registered as sources, that is a
   transcript extract found by timestamps, and the brief of the
   videos that says what they are for. You register each record with
   `/ingest` ([Register a source](register-a-source.md)); the brief
   is a file `00-brief-<videos>.md` of the project. A document the
   video shows being born is a third input, named as a dependency by
   its path. You should now see the records in `sources/` with an
   entry each in `sources/00-INDEX.md`, and the brief beside the
   project's other briefs.

2. **Compose the recipe through its checklist.** `/recipe
   screenplay <slug>` runs the genre interview: Claude is the
   interviewer, offers options and trade-offs, and the principal
   decides. The checklist, in its order:

   - the audience and the register: who watches, whether they have
     seen Claude Code, how the captions speak (plain, factual, no
     praise of the tool)
   - the purpose and the one message: what the viewer leaves with,
     said on the end card, and which principle of the forge the
     video shows
   - the inputs: the transcript source and the sessions in it, the
     brief of the videos, a document the video shows being born
   - the beats: the scenes pinned by the time of day of their first
     line and the lines that must appear, so that every render is
     the same cut; what is left out (the hours of wording, the saves)
   - the quotes: the principal's lines as typed, gross errors
     corrected and nothing else touched; which of Claude's answers
     are shown in full because the scene is about them, the rest cut
     to the sentences that carry the move; a tool call as one dim
     line; tool output and permission prompts not at all; the
     verdict line in today's form
   - the length: minutes of video, and what is shortened when there
     is too much (Claude's lines, never the principal's and never
     the captions)
   - the title card: the disclosure of the composition (real work,
     how many sessions, how many hours, the times real, the lines
     verbatim and shortened)
   - what must not appear: names, companies, hosts, paths outside
     the forge; the instance's facts are never material
   - the languages: the primary language, the language of the
     sessions, first; the translations made from it in the same run
     after it
   - the pace and the look: three reading rates in words a second
     for the principal's lines, Claude's answers and the lines that
     only report a file (4, 8 and 16 unless the principal wants
     otherwise); the date shown in the tab bar; the labels of the
     captions by language
   - the format: `video` or `html-player`; for `html-player`,
     whether the file goes out to the engine's `docs/videos/` by an
     `output:` line, with a number that gives its place in the
     course, or stays in the project's `renders/` for the company;
     and the course on the player page: the section the video
     belongs to and its name per language, what the viewer will
     learn, listed in place of the title card's title

   Claude then composes the recipe from the skeleton
   `templates/recipe-screenplay.md`. You should now see
   `recipes/<recipe>.md` with `languages:` in its front-matter, the
   primary first, an `output:` line only where a player file goes
   public, and the sections Inputs, Instructions, Format and
   Template, the Format section holding the pace, the date, the
   labels and, for a player file, the section and the name.

3. **Render the screenplay, one file per language.** `/render
   <recipe> <slug>` ([Render an output](render-an-output.md)) reads
   the recipe and its inputs from disk and generates in isolation:
   one subagent (a separate run of Claude that sees nothing of your
   conversation) reads the recipe and its inputs and writes the
   primary render first, then each translation as a file of its own,
   scene for scene and line for line, nothing re-cut. Each render is
   `renders/<recipe>.<lang>.md`; the Markdown render always stays in
   the project's `renders/`, even where the recipe's `output:` points
   into the engine. The render carries no instruction for the
   conversion: the Format section is never copied into it. Back in
   the session Claude scans each file mechanically for the
   instance's facts, verifies the provenance and remakes the ledger
   (the project's state report, made at read time). You should now
   see one render per language, opening with a provenance block
   that names the recipe, its inputs, a `language:` and, on a
   translation, `translated_from:` with the primary render.

4. **Make the format file.** Where the recipe carries a Format
   section, `/render` runs `python scripts/md2video.py` on each
   language's render with the format, the pace, the date and, for
   `html-player`, the section of the course and that language's
   name. The script reads the render, computes the timeline from the
   pace (the typing, the stand before Enter, the reveal of an answer,
   the hold for reading, the breath at a scene's end) and writes one
   of the two files:

   - `video`: `renders/<recipe>.<lang>.mp4` beside the render, every
     frame painted as a simulated terminal, the same file from the
     same render every time
   - `html-player`: `<recipe>.<lang>.html-player.js` beside the
     render, or at the recipe's `output:` path in the engine's
     `docs/videos/`; where the file lands in that folder, the script
     writes the player page `docs/videos/index.html` anew from
     `templates/html-player.html` with the folder's files listed, so
     that the page groups the videos by section in the order of the
     file names

   Where Pillow or ffmpeg is missing, the render stands, the file is
   not made, and Claude says so. You should now see the script's
   lines: one of the shape `N parts, M events, S s, language <lang>`,
   one of the shape `written <file> (<size> kB)` and, for a file in
   `docs/videos/`, `player page renewed with N file(s): <path>`.

5. **Read the public file before the engine is saved.** A file sent
   to `docs/videos/` is public once the engine is saved and served
   by GitHub Pages. The principal reads it first: that is the
   clearing of a public version, one step. A video kept for the
   company names no `output:` and stays in the project's `renders/`.
   An MP4 never enters the tree of the engine: it goes out as an
   asset of a release. You should now see the player file in
   `docs/videos/` beside the renewed `index.html`, ready to be saved
   with the engine.

## What you have afterwards

- the session records in `sources/`, immutable, and the brief of the
  videos
- `recipes/<recipe>.md`, the screenplay recipe, versioned, with its
  history companion
- `renders/<recipe>.<lang>.md` per language, the primary and its
  translations, each with provenance
- one format file per language: an MP4 beside the render, or a
  `<recipe>.<lang>.html-player.js` beside the render or in the
  engine's `docs/videos/`
- for a public player file, the renewed `docs/videos/index.html`
  listing the folder's files

The engine carries the public file only. Its recipe, its render,
its provenance and its history stay in the project, and whoever has
the project regenerates it. Why the engine hosts it is said on
[The screenplay and its player](../about/the-screenplay-and-its-player.md).

## If something goes wrong

- `/render` finds no `recipes/<recipe>.md`: it offers to compose
  one through `/recipe` and stops.
- The scan after the render hits an instance fact: Claude says it
  aloud and the principal judges it; an instance fact is regenerated
  out, never edited by hand.
- Pillow or ffmpeg is missing: the render stands, the format file is
  not made, and Claude says so. The script's own words are
  `Pillow not found - install it with `pip install pillow`.` and
  `ffmpeg not found on PATH`, with where to get it; what the script
  needs on each platform is on [Scripts](../reference/scripts.md).
- `ffmpeg failed.`: ffmpeg returned an error while the video was
  written; the file is not usable.
- `--pace takes three numbers, e.g. 4,8,16.`: the pace of the Format
  section is not three rates separated by commas.
- `<render> has no cards or scenes of a screenplay.`: the file given
  is not a screenplay render of the genre's shape; the script reads
  the title card, the card of what the viewer will see, the scenes
  with their time of day and the end card, and found none.
- `the player's template <path> is missing.`: the engine's
  `templates/html-player.html` is not where the script expects it;
  the player page cannot be renewed.
- The render file named does not exist: the script stops before it
  reads anything.
- The look is wrong before the whole video is made: paint one frame
  with `--frame <seconds> <file.png>` and look at it; the script
  paints that one frame and stops.

## A worked example

A project `<slug>` has two sessions on record and a brief of the
videos. The recipe is to be called `<recipe>`, in two languages,
`<primary>` of the sessions and `<second>` translated from it, as a
player file for the course.

1. You register the transcript extract: `/ingest
   <transcript>.md <slug>`. It is in `sources/`, catalogued in
   `sources/00-INDEX.md`. The brief `00-brief-<videos>.md` is in the
   project.

2. You run `/recipe screenplay <slug>`. Claude asks the checklist
   one point at a time; the principal answers that the viewer has
   not seen Claude Code, names the one message, pins four beats by
   their time of day, keeps the default pace, names the format
   `html-player`, sends the file to the engine as
   `docs/videos/<NN>-<recipe>.<lang>.html-player.js` and names the
   section of the course and the name per language. Claude composes
   `recipes/<recipe>.md`; its front-matter reads
   `languages: <primary>, <second>` and carries the `output:` line.

3. You run `/render <recipe> <slug>`. The subagent writes
   `renders/<recipe>.<primary>.md` and then
   `renders/<recipe>.<second>.md`, the second a translation of the
   first scene for scene. Claude scans both, remakes the ledger and
   reports what was rendered from what.

4. `/render` runs the script on each render, as it stands here for
   the primary:

   ```
   python scripts/md2video.py projects/<slug>/renders/<recipe>.<primary>.md --format html-player --pace 4,8,16 --date "<date>" --section "<section>" --name "<name>" -o docs/videos/<NN>-<recipe>.<primary>.html-player.js
   ```

   The terminal shows `4 parts, ... events, ... s, language
   <primary>`, then `player page renewed with 2 file(s):
   docs/videos/index.html` after the second language, and `written
   docs/videos/<NN>-<recipe>.<primary>.html-player.js (... kB)`.

5. The principal opens `docs/videos/index.html` and plays both
   files. They read as agreed; the engine is saved, and the videos
   are public on the player page.

Had the format been `video`, step 4 would have written
`renders/<recipe>.<primary>.mp4` and `renders/<recipe>.<second>.mp4`
beside the renders, no `output:` line in the recipe, nothing in the
engine, and the MP4s would go out as assets of a release.

## See also

- [The screenplay and its player](../about/the-screenplay-and-its-player.md): what a screenplay is, why one script makes both formats, and why the engine hosts the public files.
- [Compose a recipe](compose-a-recipe.md): the genre interview every recipe runs through.
- [Render an output](render-an-output.md): the render and its plain file.
- [Register a source](register-a-source.md): registering the session records.
- [Scripts](../reference/scripts.md): `md2video.py`, its options and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
