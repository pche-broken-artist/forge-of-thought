---
project: forge
render: readme
generated: 2026-10-23
recipe: recipes/readme.md v0.68
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v5.35
  - .claude/skills/forge/states/
  - docs/README.md v5.34
  - RELEASE-NOTES.md
---

# Forge of Thought 5.35

*A workshop where thought is tempered and shaped.* · [Documentation](docs/README.md) · [Videos](https://pche-broken-artist.github.io/forge-of-thought/videos/) · [Release notes](RELEASE-NOTES.md)

**New here? Watch first.** Eight short videos of real sessions, seven to fifteen minutes each, in two languages, show the forge at work before you read a word of this README: [Videos](https://pche-broken-artist.github.io/forge-of-thought/videos/).

Forge of Thought is an **AI cognitive extension** of a thinking
human, the **principal**: the person whose thinking is being forged,
who supplies the ideas, the answers and the decisions and holds the
final say on every word of content. It takes a raw, half-formed idea
- a process redesign, a platform initiative, an organisational
change, a D&D campaign - and tempers it into a precise,
self-contained handover for whoever delivers it: a team, a
colleague, your future self. It rests on one principle: **the
machine carries every part of the work that is not deciding**, in
three forms.

- **It thinks with you.** It interviews and probes, criticises,
  challenges and inspires; it extracts what you have not yet
  articulated and lays out options with their trade-offs. It
  proposes; you decide.
- **It keeps the work consistent.** Nothing wanders off in forgotten
  chats: the thinking lives in versioned, templated artefacts, with
  decisions, state and history keeping themselves in order and
  consistency guarded across every output.
- **It carries the tedious work.** Audience-facing outputs - a pitch,
  a deck, this README, the whole documentation - are **renders**:
  generated from the artefacts, regenerated whenever the thinking
  moves, never written by hand twice.

Technically, Forge of Thought is a git repository: slash commands and
isolated agents - challenger personas and critic lenses - for Claude
Code, templates, and the conventions binding them. Today the chain
runs from a brief through the intent to an assignment, a BRD and a
solution design; that is where it ends as of this version, not where
it is meant to stop.

Short on time? Two one-page notes say it briefly:
[for a CTO](projects/forge/renders/cto-pitch.md) and
[for a CEO](projects/forge/renders/ceo-pitch.md). Each has a Word
version beside it.

## 1. Better with AI, or replaced by it?

Forge of Thought is for those who chose to be better. The failure
modes it exists to remove:

- thinking scattered across chat sessions that die, taking their
  context with them;
- handovers whose completeness depends on the mood of the day they
  were written;
- the same thinking retold to every audience - a pitch, a deck, a
  mail - each version rewritten by hand and drifting from the others;
- feedback and decisions with no place to land, so the same ground is
  fought over twice;
- assumptions nobody attacked before reality did.

## 2. Watch it work

Every video is a real session of the forge, cut to a few minutes and
played in the browser as a simulated terminal with captions, in two
languages; nothing is staged.

- **How a brief is born.** A brief found by questions, a critique
  from outside, research, the approval, the mining.
  [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#01-brief-elicitation) · [read](docs/use/write-a-brief.md)
- **One item, one verdict.** A list settled one item per message, the
  verdict line, one write at the end of the round.
  [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#02-walkthrough) · [read](docs/use/walk-through-a-list.md)
- **From the brief to the intent.** The brief mined into positions,
  rejections and threads, cited at its version.
  [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#03-brief-to-intent) · [read](docs/use/forge-the-intent.md)
- **A critic and walking its findings.** An isolated reviewer of
  document quality, its findings mended or rejected with a reason.
  [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#04-critique) · [read](docs/use/critique-the-documents.md)
- **A check at a save.** A save runs the check, conformance findings
  settled before the commit, a release with more.
  [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#05-check-at-save) · [read](docs/use/save-your-work.md)
- **A challenger: peer review of the substance.** A persona attacks
  the thinking; what is accepted goes into the intent, what is
  rejected keeps its reason.
  [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#06-challenger) · [read](docs/use/challenge-the-thinking.md)
- **A layer below the intent and a new artefact.** The chain grows by
  a definition and a template: the first solution design.
  [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#07-new-artefact) · [read](docs/extend/add-an-artefact.md)
- **History and threads.** Why an item changed, one command away; the
  open threads as the project's memory.
  [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#08-history-threads) · [read](docs/use/read-the-history-of-an-item.md)

The whole course is at the
[course page](https://pche-broken-artist.github.io/forge-of-thought/videos/),
where each video has its scenes as chapters and the language is a
switch.

## 3. What you get

- A versioned document chain growing from a **brief** - your idea put
  together, yours by your approval - through the **intent** to the
  layers your project needs, an assignment to hand over and a
  solution design among them
  ([the document chain](docs/about/the-document-chain.md)).
- An elicitation interview that forges the intent: questions that
  draw out what you have not yet articulated, one per message
  ([elicitation](docs/about/elicitation.md)).
- Blind adversarial reviewers that never see the working
  conversation: critics of the documents, challengers of the
  thinking, checks of the conventions, every verdict recorded
  ([the isolated reviewers](docs/about/isolated-reviewers.md)).
- Audience-specific renders generated from **recipes**, including an
  actual PowerPoint file through your own template
  ([renders and recipes](docs/about/renders-and-recipes.md)).
- External sources registered immutably and used only as the
  principal directs
  ([sources and research](docs/about/sources-and-research.md)).
- Everything in files and git: nothing depends on a chat's memory
  ([persistence in git](docs/about/persistence-in-git.md)).

## 4. What is new in 5.0

**Every artefact has a definition of how it is found.** Each artefact
of the chain now has a definition of its elicitation in seven blocks,
paired with its template, and `/forge` works by it; what holds for an
artefact is read in one state file. You can also hand an artefact
over in a word and judge the proposal Claude returns.
([Elicitation](docs/about/elicitation.md))

**The working methods stand named, with their reasons.**
Walkthrough, one write per round, in pieces, step by step, plain
speech and the rest are the forge's vocabulary of collaboration: you
invoke any of them in a word, and a single letter answers a verdict
line. ([The working methods](docs/about/working-methods.md))

**The chain grew below the intent to the solution design.** An
intent says what you want and why and does not solve; how the things
wanted are realised belongs to `40-solution-design.md`, made of parts
with the choices they rest on. A project takes the layers it needs,
and many end at the intent.
([The solution design](docs/about/the-solution-design.md))

**The history of a document is a log.** Every versioned document
keeps a companion of one record per change, the way to every item
with its reasons; the release notes and the commit messages derive
from it, and `/history <ID>` gives you the whole way to an item in
one call.
([Versioning and history](docs/about/versioning-and-history.md))

**The forge explains itself from its own definitions.** `/document`
generates the documentation in `docs/`, pages of one topic each for
the user, the extender and the evaluator, never composed by hand; the
scripts are Python and run from one `python` on PATH; and
`CONTRIBUTING.md` says how to give feedback or send a change.
([The documentation](docs/about/the-documentation.md))

**`/new-artefact <name>` adds a kind of artefact to the chain.** It
leads to everything a kind needs: its position in the intent, its
definition and template, its prefixes, its reviewers and its place in
the solution design. You alone start it and it decides nothing.
([Add an artefact](docs/extend/add-an-artefact.md))

**`/publish <recipe>` makes the designed file.** From a render it
makes the designed Word or PowerPoint file through a model, into
`published/`, only on your command; the cheap plain file stays
`/render`'s. ([Publish a designed file](docs/use/publish-a-designed-file.md))

**`/man` is the forge's manual.** It is read from the forge's own
definitions: bare, it lists the commands and the working methods; with
a command, it shows what the command does and its roster.
([Look up a command](docs/use/look-up-a-command.md))

The full account, release by release, is in
[RELEASE-NOTES.md](RELEASE-NOTES.md).

## 5. Quickstart

**First, once per machine**

```text
# git, Python and Claude Code installed first: docs/start/install.md
git clone <this repository>        # you are looking at it
claude                             # always from the engine root
/setup                             # first run only: docs/start/setup.md
```

The forge is developed and run on Windows; its scripts are written to
run unchanged on Linux and macOS, and a part of them has been
verified on Linux by a user.

**Starting a new project**

```text
/new-project my-idea
/forge intent
git -C projects/my-idea init -b main   # in your own terminal, at the
                                       # engine root: Claude writes
                                       # nothing into git itself; the
                                       # init and a remote are your
                                       # one-off act
/save                                  # a save that commits nothing
                                       # names its cause (no repository,
                                       # or no git identity for the
                                       # host): docs/start/first-result.md
```

**Bringing an existing project**

```text
/import-project <project url>     # clones into projects/
/forge <project-slug>             # the slug is the repository's name;
                                  # select the project before any
                                  # work: the forge cannot guess it
```

Each project lives inside `projects/<slug>/` as a git repository of
its own, which the engine does not track; that is why you name it
first. `projects/forge` is the forge's own project, the exemplar
every render and page of the documentation derives from, and the one
directory under `projects/` the engine tracks; a user never needs to
open it. The first sitting from nothing to a saved intent is
[Get a first result](docs/start/first-result.md).

## 6. The document chain in one picture

```mermaid
flowchart LR
    B["00-brief"] --> I["10-intent"]
    I --> A["20-assignment"]
    I --> SD["40-solution-design"]
    A --> SD
    I --> RI(["renders: pitch, deck, summary …"])
    A --> RA(["renders: mail …"])
    A -.-> BRD["30-brd<br>business analysis"]
    BRD -.-> SD
    A -.-> RFP["an RFP"]
    I -.-> ART["an article"]
    ART -.-> RT(["render: a translation"])
    I -.-> ST["strategy"]
    SD -.-> IMP["implementation deck"]

    classDef built fill:#1f6feb,stroke:#1158c7,color:#ffffff
    classDef future fill:#c6dbfa,stroke:#1f6feb,color:#24292f
    classDef render fill:#2da44e,stroke:#1a7f37,color:#ffffff
    class B,I,A,SD built
    class BRD,RFP,ART,ST,IMP future
    class RI,RA,RT render
```

**Blue = chain artefacts (light = not built yet), green = renders; dashed arrows = growth that does not exist yet.**

- **Brief**: the principal's idea put together, found with Claude or
  handed over, approved when done
  ([The brief](docs/about/the-brief.md)).
- **Intent**: the briefs chiselled into what the principal holds
  ([The intent](docs/about/the-intent.md)).
- **Assignment**: the intent's in-scope substance carried to the
  recipients in a joint pass
  ([The assignment](docs/about/the-assignment.md)).
- **BRD**: the business requirements, the assignment, the intent or a
  source put in, broken into rules, behaviour and qualities the
  stakeholders can review and the delivery can estimate. The BRD is
  built since this version, though the picture above still shows it
  light and dashed, and the documentation at 5.34 has no page for it
  yet; both follow at their next regeneration.
- **Solution design**: how the things wanted are realised, part by
  part, with the choices they rest on
  ([The solution design](docs/about/the-solution-design.md)).

Below the intent a project takes the layers it needs, none a
condition of another, and many end at the intent.

> A render is never edited by hand: what is iterated is its recipe.

## 7. Documentation

The documentation of the forge is in [`docs/`](docs/README.md), pages
of one topic each, generated from the engine like this README.

- **The user**: watch [how a brief is born](https://pche-broken-artist.github.io/forge-of-thought/videos/#01-brief-elicitation) first, then begin at [What Forge of Thought is](docs/start/what-it-is.md).
- **The extender**: watch [a new artefact](https://pche-broken-artist.github.io/forge-of-thought/videos/#07-new-artefact) first, then begin at [What the forge is made of](docs/extend/what-it-is-made-of.md).
- **The evaluator**: watch [a challenger](https://pche-broken-artist.github.io/forge-of-thought/videos/#06-challenger) first, then begin at [What the forge is and is not](docs/about/what-it-is-and-is-not.md).

The documentation was generated on 2026-10-23 for Forge of Thought at
version 5.34, as its index says.

- [Start](docs/README.md#start): what the forge is, what to install,
  what `/setup` asks, and the first sitting to a saved intent.
- [Use](docs/README.md#use): one how-to per command, from starting a
  project to saving, releasing, pulling and ending a session.
- [About](docs/README.md#about): why the forge is built as it is,
  from the principal and Claude to the chain, the reviewers, renders,
  git and where it is going.
- [Extend](docs/README.md#extend): how to add an artefact, a lens, a
  persona, a check, a genre, a command or a script, and how a change
  of the forge is made.
- [Reference](docs/README.md#reference): the commands, artefacts,
  rosters, scheme, shapes, scripts, templates and glossary, exactly.

Each video is a screenplay rendered from the session records of the
principal's rollout project and made into a player file by
`scripts/md2video.py`. The files live in `docs/videos/`, served as
the course page, and the documentation on making one is the page
[Make a teaching video from a recipe](docs/use/make-a-video-from-a-recipe.md).

## 8. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) - petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit
the author and link to this repository.

Feedback, ideas and changes are welcome: see
[CONTRIBUTING.md](CONTRIBUTING.md).

## 9. About this README

This file is a render of the forge's own project, `projects/forge/`:
never edited by hand, regenerated by `/render readme` whenever the
process changes and by every `/release` of the engine. Fixes go into
the recipe or the inputs. The documentation in `docs/` is generated
the same way, from the engine, and its index says when and for which
version. The YAML provenance at the top of this file is kept by
design; changes to the system are recorded in `projects/forge/`.

_Last updated: 2026-10-23_
