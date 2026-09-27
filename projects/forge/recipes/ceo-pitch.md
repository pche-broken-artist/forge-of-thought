---
project: forge
purpose: A short public pitch of Forge of Thought to a CEO - what it can mean for a company, not how it works
audience: a CEO or another C-level executive whose experience of AI is chatting with it, arriving at the repository or handed the document by their technology lead
version: 0.5
updated: 2026-09-27
last_change: 0.5 (2026-09-27): the build line of Instructions becomes the Format section the base skeleton now has - docx, the plain file on A4 without a reference, the published file not set; the render's content is unchanged.
---

# Recipe — CEO pitch (public)

## Inputs
- projects/forge/10-intent.md
- CLAUDE.md

## Instructions
- The render is a short document the reader reads alone: about one
  A4 page, a page and a half at most - a feel for length, not a word
  count; six blocks with short headings; bullets only in blocks 2
  and 4, elsewhere sentences. First person: the author speaks as
  "I". Language: English.
- Audience: a CEO who knows AI as a chat window - they have asked it
  questions and received good answers, and that is the whole of
  their mental model. Register: plain, short sentences, the language
  of running a company - cost, quality, speed, accountability,
  people; no technology, no process description, no tooling, no
  method names. One executive writing to another whom he does not
  know: direct and respectful, no pitch language, no superlatives.
- The centre of gravity is not what the forge is but what it can
  mean for the reader's company. Block 1 says what it is in three
  sentences and no more, built on the one contrast this reader can
  feel: a chat gives you an answer; the forge gives you a decision
  you can stand behind. Everything else is about meaning.
- Block 2, the heart, five bullets, each opening with the business
  word it is about and each saying what changes and why it pays:
  - Efficiency: the questions come before the writing, so an
    assignment is complete and precise the first time and the rounds
    of clarification between the one who assigns and the team shrink;
    one forged substance is cast into an output for every audience,
    and when the idea changes every output follows, so nobody
    rewrites five documents.
  - Quality: before any person sees a document, opponents that never
    saw the conversation attack it - one the clarity of the text,
    another the substance of the thinking - and every objection ends
    in a recorded verdict; this is review nobody would run by hand on
    every document.
  - Accountability: the AI proposes and never decides; a named
    person composes every sentence and answers for the result; every
    decision carries a date and a reason, readable a year later.
  - One standard for everyone: the same discipline from the CEO to
    the analyst, and shared requirements - security is the example -
    applied to every project in the same way, so quality stops
    depending on who happened to write the document.
  - The IT department's way into AI: instead of each person chatting
    on their own, whole professions - those who assign work, business
    analysts, UX/UI, test analysts as the chain grows - work with AI
    by design, in one governed way, with the AI as a cognitive
    extension of the person and never a substitute for them.
  The benefits are stated as what the mechanism changes and why that
  should pay, never as measured gains: nothing here has been
  measured, and the render says no percentage and no saving in
  money or time as a figure.
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
  work, an AI strategy among it. One flowing paragraph of connected
  sentences, never a row of one-sentence paragraphs. Then, as a
  second paragraph, one or two sentences on where it goes: in that
  company the forge is a foundational building block of a large part
  of the IT transformation ahead; today a handful of people work
  with it, the next step is ten to twenty, and the end game is about
  fifty people who will use it daily as their main tool - stated as
  what is to come, never as a state. No other numbers.
- Nothing hidden. Block 4, in a CEO's terms: it is not a product and
  there is nothing to buy - it is a published way of working that
  runs on an AI coding assistant a company already licenses or can
  license; today it carries an idea as far as the assignment handed
  to a team, and the layers beyond that, toward requirements and
  solution design, are in development; one person works one document
  at a time; it is young, the work of one author, and there is long
  work ahead. Four or five short bullets, said plainly.
- Block 5, the suggestion: if this speaks to you, hand it to your
  technology lead - the public repository carries a note written for
  them and a README that describes the forge more broadly; and tell
  me whether this could be useful to you, and if not, why. The link
  to the repository is given once. One short paragraph, never a
  how-to.
- Block 6, headed "About me", as facts of the author, who appears
  under his full identity (his own public profile, in his words,
  not in the Inputs): he is Petr Chlumský; CTO by profession,
  builder by nature - two decades as a CTO, first of some of the
  largest Czech online companies, today within a global group that
  is the second largest in the world in its field - the group is
  described so and never named; he assigns work to teams every
  day; what draws him to AI is not automation but cognition,
  AI as a cognitive extension of the human. For this reader the
  career comes first and the craft is one clause; nothing on
  programming eras or the history of philosophy. Then: he built the
  forge himself; he shares it openly, collecting feedback and
  inspiration, and the feedback so far is very positive; he will
  gladly work on it with whoever finds it useful. Two short
  paragraphs: who he is, then the forge and the offer. It closes
  with the contact as one line, exactly: petr.chlumsky@gmail.com -
  https://www.linkedin.com/in/petrchlumsky/ -
  https://github.com/pche-broken-artist. No employer is named and
  nothing is said about when or where the forge was built.
- Vocabulary discipline: "chat" always means the question-and-answer
  use of AI the reader knows; "the forge" is the system; "the idea"
  is what enters and "the output" is what leaves; "assignment" is
  allowed as the business word it is. Never "brief", "intent",
  "ledger", "recipe", "render", "critic", "challenger", never any ID
  or prefix, no command and no file name. The reviewers are
  "opponents that never saw the conversation", never a count.
- Must not appear: any company name, project name, product, vendor
  or model name, any person other than the author; no operating
  model and no internal
  programme by name; nothing from the intent's open threads or
  rejected directions beyond the status facts given above.
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
    render: ceo-pitch
    generated: <date>
    recipe: recipes/ceo-pitch.md v<version>
    inputs:
      - projects/forge/10-intent.md v<version>
      - CLAUDE.md
    ---

    # Forge of Thought
    *A chat gives you an answer. The forge gives you a decision you
    can stand behind.*

    ## What it is
    <three sentences>

    ## What it can mean for your company
    - **Efficiency.** <what changes, why it pays>
    - **Quality.** <what changes, why it pays>
    - **Accountability.** <what changes, why it pays>
    - **One standard for everyone.** <what changes, why it pays>
    - **Your IT department's way into AI.** <what changes, why it pays>

    ## Where it works today, and where it goes
    <one flowing paragraph on today: the two pieces of work, each
    named by its kind in a clause, both handed over and both worked
    on by teams with the forge; then the author's own use>

    <a second paragraph: the building block and the people: a
    handful, ten to twenty, about fifty>

    ## Where it honestly stands
    - <not a product, nothing to buy>
    - <how far it carries an idea today, and what is in development>
    - <one person, one document>
    - <young, one author, long work ahead>

    ## What I would suggest
    <hand it to your technology lead; the link, the note for them and
    the README; tell me whether it could be useful, and if not, why>

    ## About me
    <who I am: name, two decades a CTO, one who assigns work every
    day, what draws me to AI>

    <the forge: built it myself; shared openly, feedback; glad to
    work together>

    <the contact line: e-mail - LinkedIn - GitHub>
