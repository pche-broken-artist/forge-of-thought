---
project: <slug>
purpose: Screenplay of <the video> — <what it shows>
audience: <who watches; whether they have seen Claude Code>
version: 0.1
updated: YYYY-MM-DD
last_change: <derived from the records of the newest version in recipes/<recipe>.history.md>
languages: <cs, en>      # the first primary, the rest translations of it (POS.1550)
# output: docs/videos/<NN>-<recipe>.<lang>.html-player.js   # html-player only: the engine's public folder (POS.1540); omit to stay in renders/
---

# Recipe — <the video>

<!-- Screenplay-genre recipe, composed via /recipe screenplay; the
render is a screenplay from which scripts/md2video.py makes the
video or the events of the player page (POS.1530). A recipe and
the plain file: CLAUDE.md, Document chain, Renders. -->

## Inputs
<!-- Session records registered as sources, the brief of the videos,
and a document the video shows being born as a dependency by path. -->
- sources/<transcript>.md — the sessions of <dates>; every line of
  the terminal comes from here, found by the timestamps the beats name
- 00-brief-<videos>.md — the audience, the purpose, the principles
- <path of a document the video shows, and its history> (a
  dependency, by path)

## Instructions
- The render is a screenplay, source of a video: a title card, a
  card of what the viewer will see, <N> scenes and an end card. A
  scene has the real time of day, one caption of two parts (Now:
  what happens; Why: why the forge does it this way) and a fenced
  block holding what the terminal shows. The caption is the
  teaching, the terminal the evidence. Notation of the file is
  English (headings, labels, the fence); the content — cards,
  captions, scene titles and the lines of the terminal — is in the
  render's language.
- Audience: <audience>. Register of the captions: <plain, factual,
  short sentences, no praise of the tool>.
- The one message: <what the video shows>. What the viewer leaves
  with, said on the end card: <three or four things>.
- The beats, pinned so that every render is the same cut. Each is a
  scene; the time is the time of the first line shown; the lines
  named are found in the transcript at or after that time:
  1. <HH:MM> — <title>. <the lines that must appear>.
  2. <HH:MM> — <title>. <…>
  Everything between is left out: <the hours of wording, the saves>.
- The quotes. The principal's lines are his words as typed, without
  diacritics, shortened only where long; gross errors of grammar
  and typos corrected, nothing else touched. Claude's answers keep
  the sentences that carry the move; a wording the scene is about
  (<a definition, a preview of a write, a research outcome>) is
  shown in full or nearly so. Tool calls are one dim line each;
  tool output, permission prompts and the expansions of skills not
  at all. The verdict line is shown in today's form, `(a)ccept /
  (m)odify / (q)uestion / (r)eject / (p)ark`. Claude's Markdown is
  flattened to plain terminal lines; a quoted document keeps its
  section headings as plain lines.
- Length: about <N> minutes of video at the pace of the Format,
  about <N> thousand words in all, a guide and not a rule: sense
  comes first. Where there is too much, Claude's lines are
  shortened, never the principal's and never the captions.
- The title card discloses the composition: real work, not a demo;
  <N> sessions of <date>, about <N> hours from <HH:MM> to <HH:MM>;
  a cut, the times real, the lines verbatim and shortened. The card
  of what the viewer will see names <N> things, one line each.
- Must not appear: no name of a person but the principal's handle,
  no company name, no host, no path outside the forge's own
  projects; the instance's facts are not material.
- Translation. The primary language is <cs>, the language of the
  sessions. The <en> render is a translation of the primary render
  scene for scene and line for line: the principal's lines keep
  their register, Claude's keep theirs; timestamps, file names,
  commands, IDs and the verdict line stay unchanged. Nothing is
  re-cut in the translation.

## Format
<!-- One of the two formats, never both (POS.1530). The script and
what it needs: the header of scripts/md2video.py. -->
- Format: <video | html-player>
- Plain file, made by `/render` through `scripts/md2video.py`:
  pace <4,8,16> words a second for the principal's lines, Claude's
  answers and the lines that only report a file; the date in the
  tab bar <"28. 9. 2026">; the labels of the captions by language.
  <video: `renders/<recipe>.<lang>.mp4`, the look of a simulated
  Windows Terminal, no voice-over, the languages differ in text
  only. | html-player: `<recipe>.<lang>.html-player.js`, played by
  the engine's `docs/videos/index.html`; where `output:` points into
  that folder, the file is public once the engine is saved.>

## Template
````
# <title> — screenplay

<one line: video N of the series on using the forge>

## Title card
**<title>.**
<the disclosure of the composition, two short paragraphs>

## Card — What you will see
**<heading>.**
<lines, one per principle shown, separated by blank lines>

## Scene <N> — <HH:MM> — <scene title>
**Now:** <what happens now, two or three sentences>
**Why:** <why the forge does it this way, one or two sentences>
```
> <the principal's line; continuation lines indented two spaces>
<Claude's answer, line by line, hard-wrapped; a blank line inside
it kept; a tool call as `  · <Tool>: <what the call did>`>
```

## End card
**<heading>.**
<the things the viewer leaves with, one line each>
````
