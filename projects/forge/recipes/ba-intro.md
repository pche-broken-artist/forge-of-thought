---
project: forge
purpose: Slide-by-slide source material for an introduction of Forge of Thought to business analysts, followed by a live demonstration and a homework
audience: business analysts meeting the forge for the first time, in one room with the author, who shows it live after the slides and sets them a task to try it themselves
version: 0.1
---

# Recipe — BA introduction

<!-- Presentation-genre recipe (`/recipe presentation`); the render
is a slide-by-slide deck definition, from which /render makes a plain
PowerPoint file and /publish the designed one (CLAUDE.md, Document
chain, Renders).

Handed over 2026-10-11, not yet judged (CLAUDE.md, Working methods,
Handing over). What Claude assumed: the room knows requirements
work and the words brief, requirement and BRD, and nothing of the
forge; English, by the principal's word; about twenty minutes of
slides before a live demonstration by the author. What Claude chose,
each against what it was chosen against: fourteen slides with
speaker notes rather than a shorter deck without them, so that the
author need not prepare; the chain picture as one inline diagram
rather than a reference to another render, so that the deck stands
alone; the assignment as the slide where the room's own work meets
the forge, chosen against a slide on the BRD layer, which is not
built; a "What you will see now" slide naming four things of the
live demonstration, chosen against leaving the demonstration
unframed; the homework as the closing slide, in the words of
CONTRIBUTING.md. -->

## Inputs
- CLAUDE.md
- projects/forge/10-intent.md
- .claude/skills/forge/states/   # the definitions of the artefacts:
                                 # what each is, one line each
- docs/start/what-it-is.md
- docs/about/what-it-is-and-is-not.md
- docs/about/how-a-thought-travels.md
- docs/about/the-document-chain.md
- docs/about/the-principal-and-claude.md
- docs/about/elicitation.md
- docs/about/working-methods.md
- docs/about/the-brief.md
- docs/about/the-intent.md
- docs/about/the-assignment.md
- docs/reference/requirement-style.md
- docs/about/isolated-reviewers.md
- docs/about/documents-and-records.md
- docs/about/renders-and-recipes.md
- docs/start/install.md
- docs/start/first-result.md
- CONTRIBUTING.md

## Instructions
- The render is **source material for building a presentation**, not
  the presentation itself: one section per slide, carrying the exact
  on-slide text and the speaker notes. Slide count 14; follow the
  Template's slide list.
- Audience: business analysts who write and receive requirements
  for a living and see the forge for the first time. Register: a
  colleague explaining a tool he built and uses, direct and plain;
  no pitch language, no superlatives, no corporate register.
  Language: English.
- The one message: the forge is a workshop where a thought is
  tempered into documents someone can act on, with an AI that asks,
  criticises and keeps order, and a person who decides and answers
  for every word. Centre of gravity: the document chain and how a
  working session feels (S05 to S09), because that is what the room
  will do themselves.
- The deck is understanding first: the room must grasp what the
  forge is, what it is not, how complex it is and how one works in
  it. It is not an installation guide and not a sales deck. The
  author shows the forge live after the slides; S13 frames that and
  S14 sets the task.
- Content comes from the Inputs only, no invention, no softening.
  Speaker notes cite the page or the section of the Inputs the slide
  rests on, by path, so that a slide can be traced back and checked
  when the input moves. Where a slide names a command, it names the
  command as the Inputs name it and says what it does in one clause.
- On-slide density: at most five bullets per slide, at most twelve
  words per bullet; everything beyond that belongs to the notes.
  Each slide closes with one bold line of at most ten words, the
  thing to remember from it.
- Vocabulary discipline: principal (whose thinking is forged) and
  recipients (who receive the result); brief, intent, assignment and
  solution design as the artefacts of the chain, never "document"
  where one of them is meant; position, thread, rejected direction;
  render (generated, never edited) against recipe (iterated); the
  three reviewers kept apart, critic (quality of the documents),
  challenger (substance of the thinking), check (conformance with
  the conventions); the engine (the forge's repository) against a
  project (a repository of its own). "Cognitive extension" is said
  once with its meaning: an amplifier of the person's thinking, never
  a substitute.
- Must not appear: the name of any company, programme, product or
  vendor; the name of any project made with the forge; any person
  other than the author; any date, deadline or number of people;
  anything of the intent's rejected directions; nothing of instance
  facts (who runs this instance, in what language, on which host).
  The author appears by his public GitHub profile only, as
  CONTRIBUTING.md carries it.
- The BRD: the room knows it; the deck says once, on S08, that a
  BRD layer below the assignment is foreseen and not built, as a
  fact and never as a promise with a date.
- Diagrams sit on the slides the Template assigns them to, as inline
  Mermaid blocks, valid standalone and simple enough to survive
  conversion into native slide shapes: S05 the chain, S10 the three
  reviewers around the chain.
- No long dash anywhere in the render, neither the em-dash nor the
  en-dash; where a thought wants a dash, it is a plain hyphen with a
  space on each side.
- Hard-wrap prose at about 72 columns; the Mermaid blocks are never
  wrapped.
- Per-slide format:
  ```
  ## SNN - <slide title>
  **On slide:** <title line and bullets exactly as they should appear,
  the bold closing line last>
  **Diagram:** <mermaid block, only where the Template assigns one>
  **Speaker notes:** <what the presenter says; the citation of the
  Inputs at the end in brackets>
  ```

## Format
- Format: pptx
- Plain file, made by `/render` through pandoc: reference none.
- Published file, made by `/publish` through a model: template
  none, the model designs the visual style itself: light background,
  one accent colour, generous whitespace, a clean sans-serif; model
  opus. Never let text overflow: if a slide's lines do not fit at
  the body size, shorten nothing, move the last bullet to the notes
  and say so in the build log. Redraw the Mermaid diagrams as native
  shapes with the same node labels; no rendered images of Mermaid.
  The bold closing line of each slide is set apart visually (accent
  colour, bottom of the slide). The speaker notes go into the notes
  pane of each slide. No slide numbers, no footer, no logo.

## Template
Front-matter provenance per the render convention, then one section
per slide:

| # | Slide | Content | Diagram |
|---|---|---|---|
| S01 | Forge of Thought | title; the subtitle "A workshop where thought is tempered and shaped"; one line on what the room will know in twenty minutes: what it is, what it is not, how one works in it, what their task is | - |
| S02 | A chat gives you an answer | the problem the forge answers: thinking in a chat dies with the session; what the forge does instead in three bullets: the idea travels a chain of versioned documents, reviewers that never saw the conversation attack it, who decided what and why is on record (what-it-is, what-it-is-and-is-not) | - |
| S03 | What it is not | four bullets: not a program (nothing is implemented, the engine specifies); not a delivery tool (a run ends where its owner is satisfied); not a chat (state lives in files); not one domain (the same machinery forges a platform assignment or a game campaign) (what-it-is-and-is-not, What it is not) | - |
| S04 | Two roles | the principal: ideas, answers, decisions, final authority on content; Claude: structure, order, process discipline, document hygiene; proposes and never decides; "cognitive extension" said with its meaning; prime directive 1: when unsure, ask, never fill a gap by assumption (CLAUDE.md Roles and Prime directives, the-principal-and-claude) | - |
| S05 | The document chain | the picture: brief, intent, below it assignment and solution design, each a versioned file with its history; the chain ends where the project needs it, many end at the intent; stable IDs, numbered in tens, never renumbered (the-document-chain, how-a-thought-travels, the definitions) | mermaid: 00-brief --> 10-intent --> 20-assignment; 10-intent --> 40-solution-design; 20-assignment -.-> 40-solution-design; a note that the chain grows by adding a layer |
| S06 | The brief: rough on purpose | what the brief is: the idea put together, free-form, thoughts to be processed and not decisions; three origins; mined into the intent and not polished (the-brief) | - |
| S07 | The intent: what you want and why | positions with their reason, facts, rejected directions with the reason they were dropped, open threads beside it; rewritten for coherence every round, the way to a position in its history; the document to read after weeks instead of old conversations (the-intent, how-a-thought-travels) | - |
| S08 | The assignment: where your work meets the forge | complete and precise, nothing left out in silence; it assigns and does not solve; items with shall and shall not, no priorities, one idea each; the prefixes REQ, OOS, CON, ASM, DEL, TBC, SCR in one bullet; a BRD layer below it is foreseen and not built (the-assignment, requirement-style, the-document-chain) | - |
| S09 | How a session feels | the working methods the room will meet: the elicitation interview, one question at a time; the walkthrough, one item per message, a verdict each; draft early, reflect back; one write per round, on the word write; step by step, nothing hard to reverse without a word (working-methods, elicitation) | - |
| S10 | Reviewers that never saw the conversation | the three kinds kept apart: critic, quality of the documents; challenger, substance of the thinking; check, conformance with the conventions; isolated, blind to the conversation; every finding settled by walkthrough, fixed or rejected with a recorded reason (isolated-reviewers) | mermaid: the chain in the middle, critic, challenger and check around it, each with its one word |
| S11 | Everything is a file | the history beside every versioned document; decisions; the ledger as the single source of truth; sources and research with their indexes; renders generated from recipes and never edited by hand, the README among them; git through scripts (documents-and-records, renders-and-recipes) | - |
| S12 | How complex is it | technically a git repository of slash commands, isolated agents and templates, run in Claude Code; one command per situation, the map of a project on one command; a first result in one sitting: a project, a brief, an intent, a save; what must be installed in one bullet (what-it-is, first-result, install) | - |
| S13 | What you will see now | the live demonstration framed in four bullets: the map of a project; the interview that forges an intent; a reviewer run and its walkthrough; a render made from the chain (first-result, isolated-reviewers, renders-and-recipes) | - |
| S14 | Your task | five bullets, in this order: a GitHub account; follow the author's profile, https://github.com/pche-broken-artist; install the forge on your own machine by the documentation; make a project of your own in it, any idea, to the first intent; bring one improvement, by CONTRIBUTING.md: an idea in Discussions first, a change through the chain; the closing line: come back with what did not work (CONTRIBUTING.md, install, first-result) | - |
