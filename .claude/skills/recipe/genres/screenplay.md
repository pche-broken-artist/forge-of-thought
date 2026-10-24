---
description: Compose a screenplay recipe — a teaching video of a terminal conversation cut from session records, rendered as a screenplay and made into a video or into the events of the player page by a script
---

Genre: screenplay. Skeleton: `templates/recipe-screenplay.md`. What a
screenplay is, its two formats and where a public one lands are
POS.1530 and POS.1540 of the forge intent; the script that makes the
format file is `scripts/md2video.py`, its header says what it needs.

The product is a recipe whose render is a screenplay: a title card, a
card of what the viewer will see, scenes with the real time of day,
each with a caption of two parts (Now: what happens; Why: why the forge
does it this way) and a fenced block of what the terminal shows, and
an end card. The caption is the teaching, the terminal the evidence.
The inputs are session records registered as sources (a transcript
extract, by timestamps) and the brief that says what the videos are
for. The render is never the video: the file is made from it by the
script in the format the recipe names.

Role: interviewer. Elicit the answers below from the principal —
options and trade-offs offered, decisions his (`/recipe`, step 2) —
then compose the recipe from the skeleton.

Elicitation checklist:
1. **Audience and register.** Who watches; whether they have seen
   Claude Code; how the captions speak (plain, factual, no praise of
   the tool).
2. **Purpose and the one message.** What the viewer leaves with —
   the end card says it; which principle of the forge the video
   shows.
3. **Inputs.** The transcript source and the sessions in it; the
   brief of the videos; a document the video shows being born, as a
   dependency by path.
4. **The beats.** The scenes pinned by the time of their first line
   and the lines that must appear, so that every render is the same
   cut; what is left out (the hours of wording, the saves).
5. **The quotes.** The principal's lines as typed, what is corrected
   (gross errors only) and what is kept (no diacritics, the speed);
   which of Claude's answers are shown in full because the scene is
   about them, the rest cut to the sentences that carry the move;
   tool calls as one dim line, tool output and permission prompts
   not at all; the verdict line in today's form.
6. **Length.** Minutes of video, and what is shortened when there is
   too much: Claude's lines, never the principal's and never the
   captions.
7. **The title card.** The disclosure of the composition: real work,
   how many sessions, how many hours, times real, lines verbatim and
   shortened.
8. **What must not appear.** Names, companies, hosts, paths outside
   the forge; the instance's facts are never material.
9. **Languages.** The primary language — the language of the
   sessions — and the translations made from it in the same run
   (POS.1550); the render's notation stays English, the content is in
   the render's language.
10. **Pace and look.** The three reading rates in words a second
    (the principal's lines, Claude's answers, file reports; 4, 8, 16
    unless the principal wants otherwise), the date shown in the tab
    bar, the labels of the captions by language.
11. **Format.** `video` or `html-player`, one of them, never both.
    For `html-player`: whether the file goes out to the engine's
    `docs/videos/` by `output:` (POS.1540), with its number for the
    order of the course, or stays in the project's `renders/` for
    the company; and the course on the player page: the section the
    video belongs to and its name per language, what the viewer will
    learn, listed in place of the title card's title.

The language question is point 9 here; the composition from the
skeleton closes the genre (`/recipe`, step 2).
