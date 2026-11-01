---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: 85b4faccdcf09d29
inputs:
  - .claude/skills/recipe/genres/screenplay.md
  - templates/recipe-screenplay.md
  - .claude/skills/render/SKILL.md
  - scripts/md2video.py
  - projects/forge/10-intent.md#POS.1540
---

# Make a teaching video from a recipe

A teaching video of the forge is a cut of real sessions: the
principal (the person whose thinking is being forged) and Claude in
the terminal, shown scene by scene with a caption that says what
happens and why. This page is for you, the user who has the session
records and wants the video or the player file at the end. It takes
you through the whole job in the order you do it: the sources and
the brief, the recipe composed by `/recipe screenplay`, the
screenplay written by `/render`, and the format file the script
makes from it. What a screenplay is and why one script makes both
formats is explained in
[The screenplay and its player](../about/the-screenplay-and-its-player.md);
every term of the forge is in one line in the
[Glossary](../reference/glossary.md).

## When to use it

Use this job when you have the records of one or more sessions and
want to show how the forge works to someone who was not there: a
colleague, a team, a viewer of a public course. The product is a
recipe whose render is a screenplay, and from the screenplay a file
in one of two formats:

- `video`: an MP4 of a simulated terminal, kept in the project's
  `renders/`.
- `html-player`: the timed events of the video as a script file,
  played by the engine's player page `docs/videos/index.html`; the
  file stays in the project's `renders/` or goes out to the
  engine's `docs/videos/`, where it is public once the engine is
  saved.

One recipe names one format, never both. `/publish` has no part in
this job: a screenplay has no designed file.

## The command

Two commands, in this order, with a placeholder slug for the
project:

```
/recipe screenplay
/render <recipe>
```

`<recipe>` is the name you gave the recipe in the interview; its
file is `recipes/<recipe>.md`. Claude infers the project from the
context of the conversation and asks when it is ambiguous.

## What happens

### 1. Register the session records and write the brief

The inputs of a screenplay recipe are the session records and a
brief. The session records are a transcript extract, registered as
a source with `/ingest`: how that is done is
[Register a source](register-a-source.md). The lines of the
terminal are found in it by timestamps. The brief, `00-brief-<videos>.md`,
says who the videos are for, what they are for and which principles
of the forge they show. A document the video shows being born may
be named as a third input, a dependency by path.

You should now see the transcript under `sources/`, listed in
`sources/00-INDEX.md`, and the brief of the videos in the project
root.

### 2. Compose the recipe with `/recipe screenplay`

`/recipe screenplay` runs the genre interview: Claude is the
interviewer, offers options and trade-offs, and the decisions are
yours. How every genre interview runs is
[Compose a recipe](compose-a-recipe.md). The checklist of this
genre has eleven points:

1. Audience and register: who watches, whether they have seen
   Claude Code, how the captions speak (plain, factual, no praise
   of the tool).
2. Purpose and the one message: what the viewer leaves with, said
   on the end card, and which principle of the forge the video
   shows.
3. Inputs: the transcript source and the sessions in it, the brief
   of the videos, a document the video shows being born.
4. The beats: the scenes pinned by the time of day of their first
   line and the lines that must appear, so that every render is the
   same cut; what is left out (the hours of wording, the saves).
5. The quotes: the principal's lines as typed, what is corrected
   (gross errors only) and what is kept; which of Claude's answers
   are shown in full because the scene is about them, the rest cut
   to the sentences that carry the move; tool calls as one dim
   line, tool output and permission prompts not at all; the verdict
   line in today's form.
6. Length: minutes of video, and what is shortened when there is
   too much (Claude's lines, never the principal's and never the
   captions).
7. The title card: the disclosure of the composition (real work,
   how many sessions, how many hours, times real, lines verbatim
   and shortened).
8. What must not appear: names, companies, hosts, paths outside the
   forge.
9. Languages: the primary language, which is the language of the
   sessions, and the translations made from it in the same run; the
   notation of the render stays English, the content is in the
   render's language.
10. Pace and look: three reading rates in words a second (the
    principal's lines, Claude's answers, file reports; 4, 8, 16
    unless you want otherwise), the date shown in the tab bar, the
    labels of the captions by language.
11. Format: `video` or `html-player`. For `html-player`: whether the
    file goes out to the engine's `docs/videos/` by `output:`, with
    its number for the order of the course, or stays in the
    project's `renders/` for the company; the section of the course
    on the player page the video belongs to; and its name per
    language, what the viewer will learn, listed in place of the
    title card's title.

Claude then composes the recipe from the skeleton
`templates/recipe-screenplay.md`. Its front-matter carries
`languages:` with the primary first; for `html-player` sent out of
the project it carries `output:` with the public path, such as
`docs/videos/<NN>-<recipe>.<lang>.html-player.js`. Its body has four
sections: Inputs, Instructions, Format and Template. The Format
section holds what the script needs: the format, the pace, the date
in the tab bar, the labels of the captions, and for `html-player`
the section of the course and the name per language.

You should now see `recipes/<recipe>.md` at version 0.1, with its
history companion beside it.

### 3. Write the screenplay with `/render <recipe>`

`/render <recipe>` reads the recipe's inputs at their current
versions and generates in isolation: one subagent (an agent that
sees only the recipe and its inputs, never your conversation)
writes the render following the Instructions and the Template. How
a render is made and what its plain file is, in general, is
[Render an output](render-an-output.md). For a screenplay recipe
with `languages:` the subagent writes the primary render first and
then each translation as a file of its own, scene for scene and
line for line; nothing is re-cut in a translation. The renders land
in the project's `renders/`, one per language,
`renders/<recipe>.<lang>.md`, whatever `output:` says: the
`output:` path is the place of the format file only.

Each render opens with its provenance: the project, the recipe and
its version, the inputs and their versions, `language: <lang>`,
and in a translation `translated_from: renders/<recipe>.<primary>.md`.
The Format section of the recipe is never copied into the render.

Back in the session Claude scans the written files mechanically
for the instance's facts, verifies the provenance and remakes the
ledger (the state report built from the documents at read time),
whose Renders table reads that provenance as its rows.

You should now see one Markdown file per language in `renders/`,
each with its provenance front-matter, and Claude's report of what
was rendered from what.

### 4. The format file

In the same run `/render` makes the format file through
`python scripts/md2video.py`, on each language's render, with the
format, the pace, the date and, for `html-player`, the section of
the course and that language's name from the Format section. The
script, its options and what it needs are listed in
[Scripts](../reference/scripts.md). The script computes the
timeline from the pace (typing, the stand before Enter, the reveal
of an answer, the hold for reading, the breath at a scene's end)
and writes one of the two formats:

- `video`: every frame painted as a simulated terminal and piped
  into ffmpeg; the same file from the same render every time. The
  file is `renders/<recipe>.<lang>.mp4`, beside the render.
- `html-player`: the timeline as events wrapped in a script file,
  `<recipe>.<lang>.html-player.js`, so that the player page can load
  it from a file on disk as well as from GitHub Pages. The file
  lands beside the render, or at the recipe's `output:` path in the
  engine's `docs/videos/`. Where it lands in `docs/videos/`, the
  script writes the player page `docs/videos/index.html` anew from
  `templates/html-player.html` with the folder's files listed and
  loaded. The page groups the videos by section, sections and
  videos alike in the order of the file names; so the number in the
  recipe's `output:` is the place of the video in the course. A
  file without a section and a name is listed under its title,
  after the sections.

You should now see the script's lines: a grey line with the count
of parts and events, the length in seconds and the language; for
`video` a grey line with the number of frames; for a file in
`docs/videos/` a grey line `player page renewed with N file(s)`;
and a green line `written <path> (<N> kB)` for each language.

### 5. Read the file before the engine is saved

A file sent to `docs/videos/` is public once the engine is saved.
Before that save you read the file yourself: that is the clearing
of a public version, one step. The player page on disk loads the
file by a script tag, so you can open `docs/videos/index.html` and
play it. The engine carries the file only; its recipe, its render,
its provenance and its history stay in the project, and whoever has
the project regenerates it. A video kept for the company names no
`output:` and stays in the project's `renders/`. An MP4 never
enters the engine's tree: it goes out as an asset of a release.

You should now see the video in the player page, in its section
and under its name per language, as the viewer will see it.

## What you have afterwards

- `recipes/<recipe>.md` with its history companion: the recipe,
  iterated by you; the render is never edited by hand.
- `renders/<recipe>.<lang>.md` for each language: the screenplay,
  the source of truth of the video, with its provenance.
- For `video`: `renders/<recipe>.<lang>.mp4` beside each render.
- For `html-player`: `<recipe>.<lang>.html-player.js` beside each
  render, or `docs/videos/<NN>-<recipe>.<lang>.html-player.js` in
  the engine, with `docs/videos/index.html` renewed.
- A row per render in the ledger's Renders table, read from the
  provenance.

A change of the cut goes into the recipe, and `/render <recipe>`
regenerates everything from it.

## If something goes wrong

- Pillow or ffmpeg is missing. The render stands, the format file is
  not made, and Claude says so aloud. The script prints
  `Pillow not found - install it with `pip install pillow`.` or
  `ffmpeg not found on PATH`, followed by where to install it from.
  Pillow and ffmpeg are needed for `video` only; the script installs
  nothing.
- `ffmpeg failed.`: ffmpeg returned an error while encoding; the
  MP4 is not usable.
- `--pace takes three numbers, e.g. 4,8,16.`: the pace in the
  recipe's Format section is not three rates; correct the recipe.
- `<render> has no cards or scenes of a screenplay.`: the render
  does not have the shape of the Template (a title card, a card of
  what the viewer will see, scenes with the time of day, an end
  card); the recipe's Template or Instructions are at fault, not
  the render, which is regenerated.
- `the player's template templates/html-player.html is missing.`:
  the engine's skeleton of the player page is not there; the engine
  is incomplete.
- The scan after the render finds an instance's fact. Claude says
  it aloud and you judge it: an instance fact is regenerated out,
  never edited by hand; a fact of the engine's own history stands.
- The recipe names both formats. One recipe names one format,
  never both; correct the recipe.
- You want to check the look without the whole video. The script's
  `--frame <seconds> <file.png>` paints one frame of the video at
  the given second to a PNG and stops.

## A worked example

A project `<slug>` has two sessions of one day in a transcript
registered as `sources/<transcript>.md` and a brief
`00-brief-<videos>.md`. The videos are to be public, in the primary
language `<pl>`, the language of the sessions, with one translation
`<tl>`.

```
/recipe screenplay
```

In the interview you choose: a viewer who has not seen Claude Code;
one message, said on the end card; five beats, each pinned by the
time of day of its first line; the pace 4, 8, 16; the format
`html-player`, sent out to the engine as video 01 of the course,
in the section `<section>`, named per language. Claude composes
`recipes/<recipe>.md`, version 0.1. Its front-matter:

```yaml
languages: <pl>, <tl>
output: docs/videos/01-<recipe>.<lang>.html-player.js
```

```
/render <recipe>
```

Claude's subagent writes `renders/<recipe>.<pl>.md` first and then
`renders/<recipe>.<tl>.md` as its translation, scene for scene. The
provenance of the translation says `translated_from:
renders/<recipe>.<pl>.md`. Claude scans both for instance facts,
remakes the ledger and runs the script on each render as the Format
section says:

```
python scripts/md2video.py projects/<slug>/renders/<recipe>.<pl>.md --format html-player --pace 4,8,16 --date "28. 9. 2026" --section "<section>" --name "<name in pl>" -o docs/videos/01-<recipe>.<pl>.html-player.js
python scripts/md2video.py projects/<slug>/renders/<recipe>.<tl>.md --format html-player --pace 4,8,16 --date "28. 9. 2026" --section "<section>" --name "<name in tl>" -o docs/videos/01-<recipe>.<tl>.html-player.js
```

Each run ends with `written docs/videos/01-<recipe>.<xx>.html-player.js
(<N> kB)`, preceded by `player page renewed with 2 file(s)`. You
open `docs/videos/index.html` on disk, find the section
`<section>` with the video under its name, play both languages, and
only then save the engine. Had you chosen `video` instead, the two
files would be `renders/<recipe>.<pl>.mp4` and
`renders/<recipe>.<tl>.mp4`, with no `output:` in the recipe and
nothing in `docs/videos/`.

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

Generated on 2026-11-01 for version 6.8 from the files the
front-matter names; never edited by hand.
