---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: f23bc78e965fd21d
inputs:
  - .claude/skills/recipe/genres/screenplay.md
  - templates/recipe-screenplay.md
  - .claude/skills/render/SKILL.md
  - scripts/md2video.py
  - projects/forge/10-intent.md#POS.1540
---

# Make a teaching video from a recipe

A teaching video is a cut of real sessions in the terminal, shown
scene by scene with a caption that says what happens and why. This
page is for you, the user of the forge, when you want to turn the
records of such sessions into a screenplay and from the screenplay
into a video file or into a file the player page in the browser
plays. The job runs through two commands, `/recipe screenplay` and
`/render`, and one script, `scripts/md2video.py`, which `/render`
runs for you. What a screenplay is and why one script makes both
formats is on [The screenplay and its
player](../about/the-screenplay-and-its-player.md); the terms of the
forge are in the [Glossary](../reference/glossary.md).

## When to use it

Use this job when you have one or more sessions worth showing: a
transcript of what was typed and answered, with the time of day of
every line, and a purpose the video serves for its viewers. The
video is never recorded live. It is composed from the transcript as
a screenplay (a recipe's render, in the sense the forge gives the
word: an output generated from documents, never edited by hand) and
then made into its file by the script.

Two formats exist, and a recipe names one of them, never both:

- `video`: an MP4 of a simulated terminal, with no voice-over.
- `html-player`: a file of timed events that the engine's player
  page, `docs/videos/index.html`, plays in the browser.

A player file may stay in the project for the company, or go out
to the engine's `docs/videos/` to be public. That choice is made in
the recipe, video by video.

## The command

```
/recipe screenplay <slug>
/render <recipe> <slug>
```

`<slug>` is the project's slug; `<recipe>` is the name the recipe
gets when it is composed, for example `first-steps`. `/render` runs
the script itself; you type it by hand only to check a frame of the
look (see "If something goes wrong").

## What happens

### 1. Register the session records as sources

The transcript of the sessions is an external input of the project.
Register it with `/ingest`, so that it lies in `sources/` as a
Markdown file; every line of the terminal the video shows is later
found in it by its timestamp. How registering runs is on [Register
a source](register-a-source.md).

You should now see the transcript under `sources/<transcript>.md` of
the project.

### 2. Write the brief of the videos

The recipe needs a brief that says what the videos are for: who
watches, what the series is meant to teach, which principles of the
forge it shows. It is a brief of the project like any other, named
`00-brief-<videos>.md`.

You should now see the brief beside the project's other briefs.

### 3. Compose the recipe with `/recipe screenplay`

Claude takes the role of an interviewer. It asks you, one question
at a time with options and trade-offs, and you decide; then it
composes the recipe from the skeleton `templates/recipe-screenplay.md`.
How every genre interview runs is on [Compose a
recipe](compose-a-recipe.md). The questions of this genre are:

1. Audience and register: who watches, whether they have seen Claude
   Code, how the captions speak (plain, factual, no praise of the
   tool).
2. Purpose and the one message: what the viewer leaves with, which
   the end card says; which principle of the forge the video shows.
3. Inputs: the transcript source and the sessions in it; the brief of
   the videos; a document the video shows being born, named as a
   dependency by path.
4. The beats: the scenes, each pinned by the time of day of its
   first line, with the lines that must appear; what is left out
   (the hours of wording, the saves).
5. The quotes: the principal's lines as typed, with gross errors
   corrected and nothing else touched; which of Claude's answers are
   shown in full because the scene is about them, the rest cut to the
   sentences that carry the move; tool calls as one dim line; tool
   output and permission prompts not at all; the verdict line in
   today's form.
6. Length: minutes of video, and what is shortened when there is too
   much. Claude's lines are shortened, never the principal's and
   never the captions.
7. The title card: the disclosure of the composition (real work, how
   many sessions, how many hours, times real, lines verbatim and
   shortened).
8. What must not appear: names, companies, hosts, paths outside the
   forge.
9. Languages: the primary language, which is the language of the
   sessions, and the translations made from it in the same run.
10. Pace and look: the three reading rates in words a second (the
    principal's lines, Claude's answers, the lines that only report
    a file; 4, 8 and 16 unless you want otherwise), the date shown in
    the tab bar, the labels of the captions by language.
11. Format: `video` or `html-player`. For `html-player`, whether the
    file goes out to the engine's `docs/videos/` by an `output:` line
    with its number for the order of the course, or stays in the
    project's `renders/` for the company.

Here "the principal" is the person whose thinking the forge works on,
the one who typed the lines of the sessions; in this job that is
you. The beats are pinned by time so that every render is the same
cut.

You should now see `recipes/<recipe>.md` in the project, with
`languages:` in its front-matter (the primary first), an `output:`
line where the player file goes out, and the sections Inputs,
Instructions, Format and Template.

### 4. Render the screenplay with `/render`

Claude reads the recipe and its declared inputs from disk and hands
the writing to a subagent (a separate run of Claude that sees only
the recipe and its inputs, never your conversation). The subagent
writes the primary render first, `renders/<recipe>.<primary>.md`,
and then each translation as a file of its own,
`renders/<recipe>.<lang>.md`, scene for scene and line for line;
nothing is re-cut in a translation. Every render opens with
provenance front-matter naming the recipe and the inputs with their
versions; a render in one of several languages carries
`language: <lang>`, and a translation carries `translated_from:`
with the primary render's path. The recipe's Format section is never
copied into the render. Back in the session Claude scans each file
mechanically for the instance's facts, writes the render's row in
the ledger (the project's one file of state) and reports what was
rendered from what. The general job is on [Render an
output](render-an-output.md).

You should now see one Markdown render per language in `renders/`
and Claude's report of what was rendered from what.

### 5. The format file is made by the script

Where the recipe carries a Format section, `/render` runs
`python scripts/md2video.py` on each language's render with the
format, the pace and the date that section names. The script reads
the screenplay, computes the timeline from the pace (typing, the
stand before Enter, the reveal of an answer, the hold for reading,
the breath at a scene's end) and writes one of the two formats:

- `video`: an MP4 beside the render, `renders/<recipe>.<lang>.mp4`,
  every frame painted as a simulated terminal and piped into ffmpeg.
  The same render gives the same file every time.
- `html-player`: `<recipe>.<lang>.html-player.js`, beside the render
  when the recipe names no `output:`, or at the recipe's `output:`
  path in the engine's `docs/videos/`. Where the file lands in that
  folder, the script writes the player page `docs/videos/index.html`
  anew with the folder's files listed in the order of their names.
  Because GitHub Pages cannot list a folder, the page must carry the
  list itself.

The Markdown render always stays in the project's `renders/`, even
where the format file goes out to the engine. `/publish` has no part
in this job: a screenplay has no designed file.

You should now see the script's lines in the terminal, grey then
green: `<N> parts, <N> events, <N> s, language <lang>`, for a video
`<N> frames, <N> s`, for a public player file `player page renewed
with <N> file(s): docs/videos/index.html`, and last `written <path>
(<N> kB)`.

### 6. Read a public file before the engine is saved

Where the file went out to `docs/videos/`, read it before the engine
is saved: open `docs/videos/index.html` from disk in the browser and
play the video in each language. That reading is the clearing of a
public version, one step. Once the engine is saved, the file is
public, served by GitHub Pages from `docs/`. The engine carries the
file only; the recipe, the render, the provenance and the history
stay in the project, and whoever has the project regenerates it.

A video kept for the company names no `output:` and stays in the
project's `renders/`. An MP4 never enters the engine's tree; a video
file goes out as an asset of a release.

You should now see your file listed on the player page, in the
place its number gives it.

## What you have afterwards

- In the project: `recipes/<recipe>.md` with its history companion
  `recipes/<recipe>.history.md`; one render per language,
  `renders/<recipe>.<lang>.md`, with provenance; a row per render in
  the ledger's Renders table, a translation citing its primary.
- Beside the renders: `renders/<recipe>.<lang>.mp4` for the video
  format, or `renders/<recipe>.<lang>.html-player.js` for a player
  file kept for the company.
- In the engine, for a public player file: `docs/videos/<NN>-<recipe>.<lang>.html-player.js`
  and the renewed `docs/videos/index.html`, public once the engine is
  saved. `/document` and its checks leave `docs/videos/` alone.

## If something goes wrong

- `/render` finds no `recipes/<recipe>.md`: it offers to compose the
  recipe through `/recipe` and stops.
- Pillow or ffmpeg is missing: the render stands, the format file is
  not made, and Claude says so. The script's own messages are
  `Pillow not found - install it with \`pip install pillow\`.` and
  `ffmpeg not found on PATH - install it from https://ffmpeg.org.`
  Pillow and ffmpeg are needed for the `video` format only; a player
  file needs neither. The script installs nothing.
- `ffmpeg failed.`: ffmpeg stopped while the frames were piped in;
  the MP4 is not complete.
- `<render> has no cards or scenes of a screenplay.`: the render does
  not follow the screenplay's shape, which is the Template section
  of the recipe (cards and scenes as `##` headings, a scene heading
  as `## Scene <N> — <HH:MM> — <title>`, captions as `**Now:**` and
  `**Why:**`, the terminal in a fenced block). Iterate the recipe and
  render again; never edit the render by hand.
- `--pace takes three numbers, e.g. 4,8,16.`: the pace in the
  recipe's Format section is not three rates.
- `the player's template <path> is missing.`: the engine's
  `templates/html-player.html` is not there; the player page cannot
  be renewed.
- The scan after rendering reports an instance's fact in the render
  (a name, a host, an address): Claude says it aloud and you judge
  it. Such a fact is regenerated out through the recipe, never
  edited by hand.
- You want to check the look before a whole video is made: run the
  script by hand with `--frame <seconds> <file.png>`; it paints one
  frame at that second to a PNG and stops.

The script's options and what it needs are on
[Scripts](../reference/scripts.md).

## A worked example

A project `<slug>` has a transcript of two sessions registered as
`sources/<transcript>.md` and a brief `00-brief-<videos>.md`. You
type:

```
/recipe screenplay <slug>
```

Claude asks the eleven questions, one per message. You choose the
format `html-player`, two languages with `<primary>` first and
`<second>` as its translation, and a public file with the number
`01`. Claude composes `recipes/<recipe>.md`; its front-matter opens
like this:

```yaml
---
project: <slug>
purpose: Screenplay of <the video> — <what it shows>
audience: <who watches; whether they have seen Claude Code>
version: 0.1
updated: 2026-10-14
languages: <primary>, <second>
output: docs/videos/01-<recipe>.<lang>.html-player.js
---
```

Its Format section names the format, the pace `4,8,16`, the date
shown in the tab bar and the labels of the captions by language. You
type:

```
/render <recipe> <slug>
```

The subagent writes `renders/<recipe>.<primary>.md` and then
`renders/<recipe>.<second>.md`, the second with
`translated_from: renders/<recipe>.<primary>.md`. Claude scans both,
writes two rows in the ledger's Renders table, and runs the script
on each render; what you see in the terminal, in effect, is:

```
python scripts/md2video.py projects/<slug>/renders/<recipe>.<primary>.md --format html-player --pace 4,8,16 --date "<the date>" -o docs/videos/01-<recipe>.<primary>.html-player.js
<N> parts, <N> events, <N> s, language <primary>
player page renewed with 2 file(s): docs/videos/index.html
written docs/videos/01-<recipe>.<primary>.html-player.js (<N> kB)
```

and the same for `<second>`. You open `docs/videos/index.html` from
disk, play both, and only then save the engine. Had you chosen the
`video` format instead, no `output:` would stand in the recipe and
the files would be `renders/<recipe>.<primary>.mp4` and
`renders/<recipe>.<second>.mp4`, kept in the project.

## See also

- [The screenplay and its player](../about/the-screenplay-and-its-player.md): what a screenplay is, why one script makes both formats, and why the engine hosts the public files.
- [Compose a recipe](compose-a-recipe.md): the genre interview every recipe runs through.
- [Render an output](render-an-output.md): the render and its plain file.
- [Register a source](register-a-source.md): registering the session records.
- [Scripts](../reference/scripts.md): `md2video.py`, its options and what it needs.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
