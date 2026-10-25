---
project: forge
purpose: CONTRIBUTING.md of the engine's repository - how a visitor gives feedback, brings an idea or sends a change
audience: a visitor of the repository on GitHub who has used the forge or read about it and wants to say, ask or change something; he arrives from the Contributing tab, the sidebar, or the page where an issue or a pull request is created
version: 0.4
output: /CONTRIBUTING.md
---

# Recipe — CONTRIBUTING (repository root)

## Inputs
- projects/forge/10-intent.md
- CLAUDE.md
- docs/README.md                 # the documentation index: the three
                                 # readers and where each begins

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
- The reader may never have taken part in an open-source project on
  GitHub: many come from a rollout among colleagues. Every step a
  newcomer needs is said once, plainly, where he needs it, and never
  more than he needs: a GitHub account is the one thing needed to say
  something, a free one is enough; how to reach Discussions and
  Issues from the repository's page (the tab at the top, then "New
  discussion" or "New issue"), the category the one that fits, and
  that choosing wrong does no harm, since I move it.
- A report has a short skeleton the reader fills in, said as a list
  in the file, never a GitHub template the repository does not have:
  what you ran, what you expected, what happened, the version of the
  forge you run (the top section of `RELEASE-NOTES.md`) and your
  operating system. Say once that everything posted there is public:
  no names, no company content, nothing of a project that is not
  yours to show; for that, the private way at the end.
- Before the reader reports anything, point him to where a start is
  made: install, setup and the first result in `docs/start/`, as
  relative links, so that a report of a setup problem cites the page
  he followed.
- The way to a pull request for a newcomer, only in steps the forge
  and GitHub have: fork the repository on GitHub; clone your fork as
  your engine, as `docs/start/install.md` clones the public one; work
  through the forge (`/forge intent forge` for a change of
  behaviour); `/save`, which pushes to your fork; on your fork's page
  on GitHub, "Contribute", then "Open pull request". Say plainly that
  whoever is unsure stops at a discussion and I make the change.
- Right after the opening, before the reader says anything, one
  short section "Find your way" says where things are: the
  documentation in `docs/` (link to docs/README.md), pages of one
  topic each, generated from the engine; the three readers and where
  each begins, from the index's "Where to start", as relative links;
  and for the reader who wants to change something, the two pages
  that say what the forge is made of and how a change is made
  (`docs/extend/what-it-is-made-of.md`,
  `docs/extend/how-a-change-is-made.md`). Five sentences at most;
  the file still reads as one page.
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
- Say in one sentence who decides what: in your own clone you
  decide everything, the forge there is yours; what is merged into
  the public engine its author decides (POS.0070). For a change of
  behaviour say what the pull request carries: the position in
  `projects/forge/10-intent.md` saying what is wanted and why, with
  its record in the history beside it; the item in
  `projects/forge/40-solution-design.md` where the change solves
  something; the change itself; and one line on what you ran. Say
  what it does not carry: no release, no regenerated README, release
  notes or documentation, which the author makes at the next
  release. A brief may come first and need not. Say that the easiest
  way is to open a discussion first, and that the forge's own
  commands do this work (`/forge intent forge`).
- For a document say that `README.md`, `RELEASE-NOTES.md` and this
  file are generated and are never edited by hand: a change goes into
  the recipe in `projects/forge/recipes/` or into what the recipe
  reads. The pages of `docs/` are generated the same way, by
  `/document` from the files that own each topic, never edited by
  hand: a fix goes into the file the page mirrors
  (`docs/extend/change-a-documentation-page.md`).
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

## Before you start
<A GitHub account, free; nothing else is needed to say something.
Where a start is made: docs/start/ (install, setup, first result),
as relative links.>

## Find your way
<The documentation in docs/, pages of one topic each, generated from
the engine; the three readers and where each begins, as relative
links; the two pages for whoever wants to change something.>

## Tell me what you found
<What worked, what did not, what was missing, where you got lost.
How to get there: the Discussions tab, "New discussion", the category
that fits, a wrong one does no harm. Fixed: the channel is
Discussions,
https://github.com/pche-broken-artist/forge-of-thought/discussions>

## Something is broken
<A command does something other than it says, a file is missing, a
link is dead. How to get there: the Issues tab, "New issue". The
skeleton to fill in: what you ran, what you expected, what happened,
the forge's version, your operating system. Everything here is
public: no names, no company content. Fixed: the channel is Issues,
https://github.com/pche-broken-artist/forge-of-thought/issues>

## You have an idea
<An idea needs nothing but itself. Discussions again. What happens to
it: I take it into the intent or I say why not.>

## You want to send a change
<The two kinds of change and the line between them; the kind that
alters no behaviour is settled here: send the pull request.>

### A change of how the forge behaves
<Who decides what, in one sentence; why the chain comes first, in two
sentences; what the pull request carries and what it does not; talk
first.>

### The way to a pull request
<For whoever has never sent one: fork, clone your fork as your
engine, work through the forge, /save to your fork, "Contribute",
"Open pull request". Unsure: stop at a discussion, I make the
change.>

### A change of a document
<Generated files and their recipes; the pages of docs/ generated by
/document, a fix going into the file the page mirrors.>

## Try it first
<Try your change yourself before you send it; AI named.>

## Privately
<Fixed: for anything that should not be public, write to me; my
contacts are on my profile, https://github.com/pche-broken-artist>
