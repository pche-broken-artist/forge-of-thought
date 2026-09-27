---
project: forge
purpose: A short public pitch of Forge of Thought to a CTO or head of engineering
audience: technical leadership arriving at the repository - a CTO, a head of engineering or architecture, a peer of the author who does not know him
version: 0.5
updated: 2026-09-27
last_change: 0.5 (2026-09-27): the build line of Instructions becomes the Format section the base skeleton now has - docx, the plain file on A4 without a reference, the published file not set; the render's content is unchanged.
---

# Recipe — CTO pitch (public)

## Inputs
- projects/forge/10-intent.md
- CLAUDE.md

## Instructions
- The render is a short document the reader reads alone: about one
  A4 page, a page and a half at most - a feel for length, not a word
  count; six blocks with short headings; bullets only in blocks 2
  and 4, elsewhere sentences. First person: the author speaks as
  "I". Language: English.
- Register: one technical leader writing to another whom he does not
  know - direct, plain, collegial; no pitch language, no
  superlatives, no corporate register, no familiarity that assumes
  acquaintance.
- The aim: show and inspire. The ask is a look and feedback - could
  this be useful to you, and if not, why. Nothing is sold; the forge
  is published openly under an attribution licence.
- Centre of gravity, block 2: the benefit for the people who do the
  work - how an AI framework changes the daily work of those who
  formulate and receive assignments today, and of business analysts,
  UX/UI and test analysts as the chain grows: productivity and
  quality, with the AI as a cognitive extension and a human fully
  responsible for the output. Among the benefits: common standards
  not only of the output but of its quality - for example an
  assignment analysed against shared security requirements, so that
  every project gets a consistent result. Shared material through
  libraries is today (POS.0970); shared reviewers come with the user
  extensions of block 4 (THR.0300) - the bullet says so, in a few
  words, and never presents shared reviewers as today's state. The
  mechanism gets three sentences in block 1 (a framework for
  structured, versioned documents; the AI elicits, criticises, holds
  structure; the person decides) and no more: no command names, no
  file names, no IDs, no method names.
- Block 3, where it works today and where it goes, as facts of the
  author (not in the Inputs), anonymised: two pieces of work in one
  company were written with the forge, each named by its kind in one
  clause and never by a name - the building of an agentic platform,
  the company's one governed way to run AI and automation in
  production, and the transformation of an IT department into one
  that works with AI by design. What follows holds for both alike,
  never for one of them only: both are already handed over to the
  people who take them further, and on both, teams work with the
  forge themselves. Then the author's own daily use for further
  work, an AI strategy among it. All of this is one flowing
  paragraph of connected sentences, never a row of one-sentence
  paragraphs. Then, as a second paragraph, one or two sentences on
  where it goes: in that company the forge is a foundational
  building block of a large part of the IT transformation ahead;
  today a handful of people work with it, after the next feature
  (block 4) ten to twenty, and the end game is about fifty people
  who will use it daily as their main tool - stated as what is to
  come, never as a state. No other numbers.
- Nothing hidden. Block 4 states the status in three steps, as
  facts of the author: today the chain ends at the intent and the
  assignment; a BRD layer is in development and testing; a modified
  variant of the forge for test analysts and UX/UI is at the plan
  stage. No dates and no "within days": a public document ages. Then
  one short bullet: user extensions - one's own reviewer, say a
  challenger, kept and developed in one's personal repository (the
  intent's THR.0300) - are what has to be finished before a wider
  rollout; one sentence, no gloss on what holds until then, no
  numbers here. The main limitation today: one person works one
  document; sharing across projects through libraries works. Long
  work ahead, said plainly.
- Block 5, the ask: tell me whether this could be useful to you,
  and if not, why. Then the link to the public repository and an
  invitation to read its README, where the forge is described more
  broadly and a first run is a matter of minutes - one or two
  sentences, never a how-to.
- Block 6, headed "About me", as facts of the author, who appears
  under his full identity (his own public profile, in his words,
  not in the Inputs): he is Petr Chlumský; CTO by profession,
  builder by nature - programming since the 8-bit era; two decades
  as a CTO, first of some of the largest Czech online companies,
  today within a global group that is the second largest in the
  world in its field - the group is described so and never named;
  and he never stopped writing code; what draws him to AI is not
  automation but cognition, AI as a cognitive extension of the
  human - the old arts of knowing (scholastic disputation, the
  Socratic method) reforged with AI: a machine that interviews you
  like Socrates and keeps every decision on the record. Then: he
  built the forge himself; he shares it openly, collecting feedback
  and inspiration, and the feedback so far is very positive; the
  reader's feedback would move it further, and he will gladly work
  on it with whoever finds it useful. Two short paragraphs: who he
  is, then the forge and the offer. It closes with the contact as
  one line, exactly: petr.chlumsky@gmail.com -
  https://www.linkedin.com/in/petrchlumsky/ -
  https://github.com/pche-broken-artist. No employer is named and
  nothing is said about when or where the forge was built.
- Must not appear: any company name, project name, product or
  vendor name, any person other than the author; no operating model
  and no internal programme by name; nothing from the intent's
  rejected directions.
- Content comes from the Inputs and the facts above - no invention,
  no softening.
- No long dash anywhere in the render, neither the em-dash nor the
  en-dash. Where a thought wants a dash, it is a plain hyphen with a
  space on each side.
- Hard-wrap prose at about 72 columns.

## Format
- Format: docx
- Plain file, made by `/render` through pandoc: reference none,
  page size A4.
- Published file, made by `/publish` through a model: not set;
  `/publish` asks before its first run.

## Template
    ---
    project: forge
    render: cto-pitch
    generated: <date>
    recipe: recipes/cto-pitch.md v<version>
    inputs:
      - projects/forge/10-intent.md v<version>
      - CLAUDE.md
    ---

    # Forge of Thought
    *A workshop where thought is tempered and shaped.*

    ## What it is
    <three sentences>

    ## What it changes in daily work
    - <benefit 1>
    - <benefit 2>
    - <benefit 3>
    - <benefit 4>
    - <shared standards of quality>

    ## Where it works today, and where it goes
    <one flowing paragraph on today: the two pieces of work, each
    named by its kind in a clause, both handed over and both worked
    on by teams with the forge; then the author's own use>

    <a second paragraph: the building block and the people: a
    handful, ten to twenty, about fifty>

    ## Where it honestly stands
    - <done today>
    - <in development and testing>
    - <planned>
    - <user extensions: to finish before a wider rollout>
    - <the limitation>

    ## What I am asking of you
    <feedback, and why not; the link and the README>

    ## About me
    <who I am: name, CTO and builder, what draws me to AI>

    <the forge: built it myself; shared openly, feedback; glad to
    work together>

    <the contact line: e-mail - LinkedIn - GitHub>
