---
project: forge
purpose: CONTRIBUTING.md of the engine's repository - how a visitor gives feedback, brings an idea or sends a change
audience: a visitor of the repository on GitHub who has used the forge or read about it and wants to say, ask or change something; he arrives from the Contributing tab, the sidebar, or the page where an issue or a pull request is created
version: 0.1
updated: 2026-10-04
last_change: 0.1 (2026-10-04): the recipe born (POS.1440).
output: /CONTRIBUTING.md
---

# Recipe — CONTRIBUTING (repository root)

## Inputs
- projects/forge/10-intent.md
- CLAUDE.md

## Instructions
- The render is one file a visitor reads whole before he acts: no
  section he would skip, nothing that describes a thing the forge
  does not have. Language: English.
- Voice: the author speaks as "I" to "you", plain and warm, short
  sentences. Open by thanking the reader for wanting to contribute,
  in plain words and without saying how far he has come. One person
  wrote the forge and reads every word sent to him; say so once. No
  pitch language. No em dash and no en dash anywhere: a comma, a
  colon or a new sentence. A term of the
  forge (intent, solution design, recipe, render) is said with a few
  words of what it is at its first use.
- The order is the order a visitor would act: say something, bring
  an idea, then send a change. Feedback and ideas come first and get
  the most room, because they are what is wanted most (POS.1440).
- From the intent: POS.1440 is the stance the whole file says;
  POS.1390 for what the intent and the solution design each hold;
  POS.0720 and POS.0710 for a render and its recipe; POS.0070 for who
  decides. From CLAUDE.md: the names of the files of the chain and
  where they stand. The wording is derived anew at each render; what
  is marked fixed below is carried word for word.
- The line between the two kinds of change is drawn by what the
  change does, never by its size. A change of how the forge behaves,
  a command, a rule, a convention, what a reviewer looks for, goes
  through the chain. A change that alters no behaviour, a wording, a
  broken path, a slip, does not, and is sent as it is.
- For a change of behaviour say what the pull request carries: the
  position in `projects/forge/10-intent.md` saying what is wanted and
  why, with its record in the history beside it; the item in
  `projects/forge/40-solution-design.md` where the change solves
  something; and the change itself. A brief may come first and need
  not. Say that the easiest way is to open a discussion first, and
  that the forge's own commands do this work (`/forge intent forge`).
- For a document say that `README.md`, `RELEASE-NOTES.md` and this
  file are generated and are never edited by hand: a change goes into
  the recipe in `projects/forge/recipes/` or into what the recipe
  reads.
- The rule on trying is one short section, said to "you" in the
  same warm voice as the rest and never as a prohibition in the third
  person: try your change yourself before you send it. It names AI
  plainly: a change written with an AI is welcome on the same rule,
  and the pull request says what was run.
- The change that alters no behaviour gets no section of its own: it
  is settled where the two kinds are told apart, in a sentence that
  says to send the pull request and that nothing else is needed.
- Never promise a time of answer. Never invent a channel, a label, a
  template or a rule the inputs and these instructions do not give.
- Omit: code of conduct, security policy, commit message rules,
  branch names, tests and build. The forge has none of them to
  describe.

## Template
# Contributing to Forge of Thought

<Two or three sentences: thanks; what I want most is feedback and
ideas; I wrote the forge alone and I read everything.>

## Tell me what you found
<What worked, what did not, what was missing, where you got lost.
Fixed: the channel is Discussions,
https://github.com/pche-broken-artist/forge-of-thought/discussions>

## Something is broken
<A command does something other than it says, a file is missing, a
link is dead: what you ran, what you expected, what happened. Fixed:
the channel is Issues,
https://github.com/pche-broken-artist/forge-of-thought/issues>

## You have an idea
<An idea needs nothing but itself. Discussions again. What happens to
it: I take it into the intent or I say why not.>

## You want to send a change
<The two kinds of change and the line between them; the kind that
alters no behaviour is settled here: send the pull request.>

### A change of how the forge behaves
<Why the chain comes first, in two sentences; what the pull request
carries; talk first.>

### A change of a document
<Generated files and their recipes.>

## Try it first
<Try your change yourself before you send it; AI named.>

## Privately
<Fixed: for anything that should not be public, write to me; my
contacts are on my profile, https://github.com/pche-broken-artist>
