---
project: forge
render: readme
generated: 2026-10-14
recipe: recipes/readme.md v0.65
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v5.9
  - .claude/skills/forge/states/
  - docs/README.md v5.9
  - RELEASE-NOTES.md
---

# Forge of Thought 5.9

*A workshop where thought is tempered and shaped.* · [Documentation](docs/README.md) · [Videos](https://pche-broken-artist.github.io/forge-of-thought/videos/) · [Release notes](RELEASE-NOTES.md)

Forge of Thought is an **AI cognitive extension** of a thinking
human, the **principal**: whoever's thinking is being forged. It
takes a raw, half-formed idea, a process redesign, a platform
initiative, an organisational change, a D&D campaign, and tempers it
into a precise, self-contained handover for whoever delivers it: a
team, a colleague, your future self. It rests on one principle: **the
machine carries every part of the work that is not deciding**, in
three forms.

- **It thinks with you.** It interviews and probes, criticises,
  challenges, inspires; it extracts what the principal has not yet
  articulated and lays out options with their trade-offs. It
  proposes; you decide.
- **It keeps the work consistent.** Nothing wanders off in forgotten
  chats: the thinking lives in versioned, templated artefacts, with
  decisions, state and history keeping themselves in order and
  consistency guarded across every output.
- **It carries the tedious work.** Audience-facing outputs, a pitch,
  a deck, this README, the whole documentation, are **renders**:
  generated from the artefacts, regenerated whenever the thinking
  moves, never written by hand twice.

Technically the forge is a git repository: slash commands and
isolated agents, challenger personas and critic lenses, for Claude
Code, templates, and the conventions binding them. Today the chain is
built from the brief through the intent and the assignment to the
solution design; where it ends is the project's choice, and many
projects end at the intent.

Short on time? Two one-page notes say it briefly:
[for a CTO](projects/forge/renders/cto-pitch.md) and
[for a CEO](projects/forge/renders/ceo-pitch.md). Each has a Word
version beside it.

## 1. Better with AI, or replaced by it?

Forge of Thought is for those who chose to be better. The failure
modes it exists to remove:

- Thinking scattered across chat sessions that die, taking their
  context with them.
- Handovers whose completeness depends on the mood of the day they
  were written.
- The same thinking retold to every audience, a pitch, a deck, a
  mail, each version rewritten by hand and drifting from the others.
- Feedback and decisions with no place to land, so the same ground is
  fought over twice.
- Assumptions nobody attacked before reality did.

## 2. What you get

- A versioned document chain growing from a **brief**, your idea put
  together, yours by your approval, through the **intent** to the
  layers your project needs, an assignment to hand over and a
  solution design among them
  ([the document chain](docs/about/the-document-chain.md)).
- An elicitation interview that forges the intent: one question per
  message, drawing out what you have not yet articulated
  ([elicitation](docs/about/elicitation.md)).
- Blind adversarial reviewers that never see the working
  conversation: critics of the documents, challengers of the
  thinking, checks of the conventions; every verdict recorded
  ([the isolated reviewers](docs/about/isolated-reviewers.md)).
- Audience-specific renders generated from **recipes**, including an
  actual PowerPoint file through your own template
  ([renders and recipes](docs/about/renders-and-recipes.md)).
- External sources registered immutably and used only as the
  principal directs
  ([sources and research](docs/about/sources-and-research.md)).
- Everything in files and git: nothing depends on a chat's memory
  ([persistence in git](docs/about/persistence-in-git.md)).

## 3. What is new in 5.0

**Every artefact has a definition of how it is found.** Brief,
intent, assignment and solution design each carry a definition of
their elicitation in seven blocks, paired with the artefact's
template, and `/forge` works each artefact by it. What holds for an
artefact is read in one place and mended where it lives
([elicitation](docs/about/elicitation.md)).

**The working methods stand named, with their reasons.** The
walkthrough, step by step, in pieces, one write per round, plain
speech and the rest are the forge's vocabulary of collaboration: you
invoke any of them in a word, and Claude applies them whenever their
situation arises
([the working methods](docs/about/working-methods.md)).

**The chain grew below the intent to the solution design.** An
intent says what is wanted and why; how it is realised, part by
part with the choices it rests on, is the solution design's, whoever
said it. A project takes the layers it needs, and many end at the
intent ([the solution design](docs/about/the-solution-design.md)).

**The history of a document is a log.** Every versioned document
keeps its changes as one record each in a companion beside it, and
the release notes derive from that log; the way to an item, why it
changed and what was tried, is found there and never in the item
([versioning and history](docs/about/versioning-and-history.md)).

**The forge explains itself from its own definitions.** The
documentation is generated from the engine, the scripts are Python
and run from `python` on PATH, and `CONTRIBUTING.md` says how to give
feedback or send a change
([the documentation](docs/about/the-documentation.md)).

**`/new-artefact <name>`** adds a new kind of artefact to the chain
and leads to everything a kind needs: its position, its definition
and template, its prefixes, its reviewers. You alone start it, and
it decides nothing ([add an artefact](docs/extend/add-an-artefact.md)).

**`/document [slug]`** generates the documentation of the engine or
of a project into `docs/`: pages of one topic each with an index,
for the user, the extender and the evaluator, in one run that asks
nothing and regenerates only what changed
([generate the documentation](docs/use/generate-the-documentation.md)).

**`/publish <recipe>`** makes the designed Word or PowerPoint file
from a render through a model, into `published/`, only on your
command. It converts the Markdown you have read and renders nothing
([publish a designed file](docs/use/publish-a-designed-file.md)).

**`/man [command or method]`** prints the forge's manual, read from
its own definitions: bare, the commands and the working methods;
with a command, its purpose, arguments and roster
([look up a command](docs/use/look-up-a-command.md)).

The full account, version by version, is in
[RELEASE-NOTES.md](RELEASE-NOTES.md).

## 4. Quickstart

**First, once per machine**

```
# git, Python and Claude Code must be installed first:
# what and how is docs/start/install.md
git clone <this repository>      # you are looking at it
cd forge-of-thought
claude                           # always from the engine root
/setup                           # first run only; what it asks
                                 # is docs/start/setup.md
```

**Starting a new project**

```
/new-project my-idea
/forge intent
# in your own terminal, at the engine root: Claude is not allowed
# to run git; a remote may follow
git -C projects/my-idea init -b main
/save                            # a save that commits nothing names
                                 # its cause: no repository, or no
                                 # git identity for the host;
                                 # docs/start/first-result.md says
                                 # what to do
```

**Bringing an existing project**

```
/import-project <project url>    # clones into projects/
/forge <project-slug>            # the slug is the repository's name;
                                 # select the project before any
                                 # work: the forge cannot guess it
```

Each project lives inside `projects/<slug>/` as a git repository of
its own, which the engine does not track: that is why you name it
first. `projects/forge` is the forge's own project, the exemplar
every render and page of the documentation derives from, and the one
directory under `projects/` the engine tracks; a user never needs to
open it. The forge is developed and run on Windows; its scripts are
written to run unchanged on Linux and macOS and have not yet been run
there. The first sitting from nothing to a saved intent is
[docs/start/first-result.md](docs/start/first-result.md).

## 5. The document chain in one picture

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

**Blue = chain artefacts (light = not built yet), green = renders;
dashed arrows = growth that does not exist yet.**

- **Brief**: the principal's idea put together, found with Claude or
  handed over, approved when done
  ([the brief](docs/about/the-brief.md)).
- **Intent**: the briefs chiselled into what the principal holds
  ([the intent](docs/about/the-intent.md)).
- **Assignment**: the intent's in-scope substance carried to the
  recipients in a joint pass
  ([the assignment](docs/about/the-assignment.md)).
- **Solution design**: how the things wanted are realised, part by
  part, with the choices they rest on
  ([the solution design](docs/about/the-solution-design.md)).

Below the intent a project takes the layers it needs, none a
condition of another, and many end at the intent.

> A render is never edited by hand: what is iterated is its recipe.

## 6. Documentation

The documentation of the forge is in [`docs/`](docs/README.md),
pages of one topic each, generated from the engine like this README.

- **The user** begins at
  [What Forge of Thought is](docs/start/what-it-is.md).
- **The extender** begins at
  [What the forge is made of](docs/extend/what-it-is-made-of.md).
- **The evaluator** begins at
  [What the forge is and is not](docs/about/what-it-is-and-is-not.md).

The documentation was generated on 2026-10-14 for Forge of Thought
at version 5.9, and its index says so too.

- [Start](docs/README.md#start): what the forge is, what to install,
  what `/setup` asks, and a first result in one sitting.
- [Use](docs/README.md#use): one how-to per command, from starting a
  project to ending a session.
- [About](docs/README.md#about): what each part of the forge is and
  why it is so, for the reader who wants to judge it.
- [Extend](docs/README.md#extend): how a change is made and how an
  artefact, a reviewer, a genre, a command or a script is added.
- [Reference](docs/README.md#reference): the commands, the
  conventions, the layouts and the terms, exactly.

The teaching videos are real sessions of the forge cut to a few
minutes each and played in the browser as a simulated terminal with
captions, in Czech and in English, at the course page
[Videos](https://pche-broken-artist.github.io/forge-of-thought/videos/).
There is one per principle of working with the forge: how a brief is
born, the walkthrough, from the brief to the intent, a critic, a
check at a save, a challenger, a new artefact, history and threads.
The files live in `docs/videos/` and are made from the screenplay
renders of the principal's rollout project by `scripts/md2video.py`.

## 7. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) - petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit
the author and link to this repository.

Feedback, ideas and changes are welcome: see
[CONTRIBUTING.md](CONTRIBUTING.md).

## 8. About this README

This file is a render of `projects/forge`: never edited by hand,
regenerated by `/render readme` whenever the process changes, and by
every `/release` of the engine. Fixes go into the recipe or the
inputs. The documentation in `docs/` is generated the same way, from
the engine, and its index says when and for which version. The YAML
front-matter provenance at the top is kept by design; changes of the
system are recorded in `projects/forge/`.

_Last updated: 2026-10-14_
