---
project: forge
render: readme
generated: 2026-10-11
recipe: recipes/readme.md v0.63
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v5.3
  - .claude/skills/forge/states/
  - docs/README.md v5.3
  - RELEASE-NOTES.md
---

# Forge of Thought 5.3

*A workshop where thought is tempered and shaped.* · [Documentation](docs/README.md) · [Release notes](RELEASE-NOTES.md)

Forge of Thought is an **AI cognitive extension** of a thinking
human, the **principal**: the person whose thinking is being forged.
It takes a raw, half-formed idea (a process redesign, a platform
initiative, an organisational change, a D&D campaign) and tempers it
into a precise, self-contained handover for whoever delivers it: a
team, a colleague, your future self. It rests on one principle, **the
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
- **It carries the tedious work.** Audience-facing outputs (a pitch,
  a deck, this README, the whole documentation) are **renders**:
  generated from the artefacts, regenerated whenever the thinking
  moves, never written by hand twice.

Technically, Forge of Thought is a git repository: slash commands and
isolated agents (challenger personas and critic lenses) for Claude
Code, templates, and the conventions binding them. Today the chain
runs from the brief through the intent to the assignment and the
solution design, where it currently ends. It is developed and run on
Windows; its scripts are written to run unchanged on Linux and macOS
and have not yet been run there.

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
- the same thinking retold to every audience (a pitch, a deck, a
  mail), each version rewritten by hand and drifting from the others;
- feedback and decisions with no place to land, so the same ground
  is fought over twice;
- assumptions nobody attacked before reality did.

## 2. What you get

- A versioned document chain growing from a **brief**, your idea put
  together and yours by your approval, through the **intent** to the
  layers your project needs, an assignment to hand over and a
  solution design among them
  ([The document chain](docs/about/the-document-chain.md)).
- An elicitation interview that forges the intent: one question per
  message, drawing out what you have not yet articulated
  ([Elicitation](docs/about/elicitation.md)).
- Blind adversarial reviewers, never shown the working conversation:
  critics of the documents, challengers of the thinking, checks of
  the conventions, every verdict recorded
  ([The isolated reviewers](docs/about/isolated-reviewers.md)).
- Audience-specific renders generated from **recipes**, including an
  actual PowerPoint file through your own template
  ([Renders and recipes](docs/about/renders-and-recipes.md)).
- External sources registered immutably and used only as the
  principal directs
  ([Sources and research](docs/about/sources-and-research.md)).
- Everything in files and git: nothing depends on a chat's memory
  ([Persistence in git](docs/about/persistence-in-git.md)).

## 3. What is new in 5.0

**Every artefact has a definition of its elicitation.** The brief,
the intent, the assignment and the solution design are each found by
their own definition: what the artefact is for, what it reads, how
Claude partners you and in what order the questions come. You can
read, in one file per artefact, how a conversation about it will run
([Elicitation](docs/about/elicitation.md)).

**The working methods stand named, with their reasons.** Walkthrough,
one write per round, in pieces, handing over, plain speech and the
rest are the vocabulary of a working conversation; you invoke any of
them in a word, and Claude is held to them at every prompt
([The working methods](docs/about/working-methods.md)).

**The chain grew below the intent to the solution design.** An intent
says what you want and why and does not solve; how the thing is
realised, part by part with the choices it rests on, is the solution
design's. The cut between the two is now a rule, and a project takes
the layers it needs
([The solution design](docs/about/the-solution-design.md)).

**The history of a document is a log.** Every versioned document
keeps its changes as one record per change in a companion beside it,
with the reason, the old wording and what you must do after; the
release notes and the commit messages derive from it
([Versioning and history](docs/about/versioning-and-history.md)).

**The forge explains itself from its own definitions.** The
documentation is generated from the engine as it stands, the scripts
are Python so that the forge runs beyond Windows, and
`CONTRIBUTING.md` says how to give feedback or bring a change
([The documentation](docs/about/the-documentation.md)).

**`/new-artefact <name>`** adds a new kind of artefact to the chain
and leads to everything a kind needs: its position in the intent, its
definition and template, its prefixes, its reviewers. The chain grows
without reworking what exists
([Add an artefact](docs/extend/add-an-artefact.md)).

**`/document [slug]`** generates the documentation of the engine or
of a project into `docs/`: pages of one topic each and their index,
regenerated only where something changed, never composed by hand
([Generate the documentation](docs/use/generate-the-documentation.md)).

**`/publish <recipe>`** makes the designed Word or PowerPoint file
from a render through a model, only on your command; the cheap plain
file stays with `/render`
([Publish a designed file](docs/use/publish-a-designed-file.md)).

**`/man [command | method]`**, alias `/manual`, prints the forge's
manual from its own definitions: bare, the commands and the working
methods; with a name, what that command or method does
([Look up a command](docs/use/look-up-a-command.md)).

The full account, with what each change asks of you, is in
[RELEASE-NOTES.md](RELEASE-NOTES.md).

## 4. Quickstart

**First, once per machine**

```
# git, Python and Claude Code must be installed first: docs/start/install.md
git clone <this repository>   # you are looking at it
claude                        # always start it from the engine root
/setup                        # first run only; what it asks: docs/start/setup.md
```

**Starting a new project**

```
/new-project my-idea
/forge intent
git -C projects/my-idea init -b main   # in your own terminal, at the engine root:
                                       # Claude is not allowed to run git; a remote may follow
/save                                  # a save that commits nothing names its cause (no repository,
                                       # or no git identity for this host): docs/start/first-result.md says what to do
```

**Bringing an existing project**

```
/import-project <project url>   # clones into projects/
/forge <project-slug>           # the slug is the repository's name; select the project
                                # before any work: the forge cannot guess it
```

Each project lives inside `projects/<slug>/` as a git repository of
its own, which the engine does not track: that is why you name it
first. `projects/forge` is the forge's own project, the exemplar every
render and page of the documentation derives from, and the one
directory under `projects/` the engine tracks; a user never needs to
open it. The first sitting, from nothing to a saved intent, is
[Get a first result](docs/start/first-result.md).

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

**Blue = chain artefacts (light = not built yet), green = renders; dashed arrows = growth that does not exist yet.**

- **Brief** (`00-brief.md`): the principal's idea put together, found
  with Claude or handed over, approved when done
  ([The brief](docs/about/the-brief.md)).
- **Intent** (`10-intent.md`): the briefs chiselled into what the
  principal holds ([The intent](docs/about/the-intent.md)).
- **Assignment** (`20-assignment.md`): the intent's in-scope
  substance carried to the recipients in a joint pass
  ([The assignment](docs/about/the-assignment.md)).
- **Solution design** (`40-solution-design.md`): how the things
  wanted are realised, part by part, with the choices they rest on
  ([The solution design](docs/about/the-solution-design.md)).

Below the intent a project takes the layers it needs, none a
condition of another, and many end at the intent.

> A render is never edited by hand: what is iterated is its recipe.

## 6. Documentation

The documentation of the forge is in [`docs/`](docs/README.md), pages
of one topic each, generated from the engine like this README.

- **The user** begins with
  [What Forge of Thought is](docs/start/what-it-is.md), then installs,
  sets up, gets a first result and forges the intent.
- **The extender** begins with
  [What the forge is made of](docs/extend/what-it-is-made-of.md), then
  how a change is made, how the rules are held, the templates and how
  a documentation page is changed.
- **The evaluator** begins with
  [What the forge is and is not](docs/about/what-it-is-and-is-not.md),
  then how a thought travels, elicitation, the isolated reviewers and
  the documentation.

The documentation was generated on 2026-10-11 for Forge of Thought at
version 5.3; its index says so too.

- [Start](docs/README.md#start): what the forge is, what to install,
  what `/setup` asks and how to get a first result in one sitting.
- [Use](docs/README.md#use): one page per command and per working
  situation, from starting a project to ending a session.
- [About](docs/README.md#about): what the forge is and why it is
  built as it is, artefact by artefact and mechanism by mechanism.
- [Extend](docs/README.md#extend): how a change to the forge is
  made, and how an artefact, a lens, a persona, a check, a genre, a
  command or a script is added.
- [Reference](docs/README.md#reference): the exact shapes, tables,
  words and layouts, from the commands to the glossary.

## 7. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) - petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit
the author and link to this repository.

Feedback, ideas and changes are welcome: see
[CONTRIBUTING.md](CONTRIBUTING.md).

## 8. About this README

This file is a render of `projects/forge`: never edited by hand,
regenerated by `/render readme` whenever the process changes, and by
every `/release` of the engine. Fixes go into the recipe
(`projects/forge/recipes/readme.md`) or into the inputs it reads. The
documentation in `docs/` is generated the same way, from the engine,
and its index says when and for which version. The YAML front-matter
at the top of this file is the render's provenance, kept by design;
changes to the system are recorded in `projects/forge/`.

_Last updated: 2026-10-11_
