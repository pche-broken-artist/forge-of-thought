---
project: forge
render: readme
generated: 2026-10-10
recipe: recipes/readme.md v0.60
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v5.0
  - .claude/skills/forge/states/
  - docs/README.md v4.62
---

# Forge of Thought 5.0

*A workshop where thought is tempered and shaped.* · [Documentation](docs/README.md) · [Release notes](RELEASE-NOTES.md)

Forge of Thought is an **AI cognitive extension** of a thinking
human, the **principal**: whoever's thinking is being forged. It
takes a raw, half-formed idea (a process redesign, a platform
initiative, an organisational change, a D&D campaign) and tempers it
into a precise, self-contained handover for whoever delivers it: a
team, a colleague, your future self. It rests on one principle,
**the machine carries every part of the work that is not deciding**,
in three forms.

- **It thinks with you.** It interviews and probes, criticises,
  challenges and inspires; it extracts what the principal has not
  yet articulated and lays out options with their trade-offs. It
  proposes; you decide.
- **It keeps the work consistent.** Nothing wanders off in forgotten
  chats: the thinking lives in versioned, templated artefacts, with
  decisions, state and history keeping themselves in order and
  consistency guarded across every output.
- **It carries the tedious work.** Audience-facing outputs (a pitch,
  a deck, this README, the whole documentation) are **renders**:
  generated from the artefacts, regenerated whenever the thinking
  moves, never written by hand twice.

Technically, Forge of Thought is a git repository: slash commands
and isolated agents (challenger personas and critic lenses) for
Claude Code, templates, and the conventions binding them. Today the
chain runs from a brief through the intent to an assignment and a
solution design; where a project stops along it is the project's to
say, and many stop at the intent.

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
- The same thinking retold to every audience (a pitch, a deck, a
  mail), each version rewritten by hand and drifting from the others.
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
  message, drawing out what you have not yet said
  ([elicitation](docs/about/elicitation.md)).
- Blind adversarial reviewers: critics of the documents, challengers
  of the thinking, checks of the conventions; every verdict recorded
  ([isolated reviewers](docs/about/isolated-reviewers.md)).
- Audience-specific renders generated from **recipes**, including an
  actual PowerPoint file through your own template
  ([renders and recipes](docs/about/renders-and-recipes.md)).
- External sources registered immutably and used only as the
  principal directs
  ([sources and research](docs/about/sources-and-research.md)).
- Everything in files and git: nothing depends on a chat's memory
  ([persistence in git](docs/about/persistence-in-git.md)).

## 3. Quickstart

**First, once per machine**

```text
git clone <this repository>   # you are looking at it
# install Claude Code first: what to install and how is docs/start/install.md
claude                        # always from the engine root
/setup                        # first run only; what it asks is docs/start/setup.md
```

**Starting a new project**

```text
/new-project my-idea
/forge intent
/save
```

**Bringing an existing project**

```text
/import-project <project url>   # clones into projects/
/forge <project-slug>           # the slug is the repository's name; select the project before any work: the forge cannot guess it
```

Each project lives inside `projects/<slug>/` as a git repository of
its own, which the engine does not track: that is why you name it
first. The first sitting from nothing to a saved intent is
[docs/start/first-result.md](docs/start/first-result.md).

## 4. The document chain in one picture

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

- **Brief** (`00-brief.md`): the principal's idea put together, found
  with Claude or handed over, approved when done
  ([the brief](docs/about/the-brief.md)).
- **Intent** (`10-intent.md`): the briefs chiselled into what the
  principal holds ([the intent](docs/about/the-intent.md)).
- **Assignment** (`20-assignment.md`): the intent's in-scope
  substance carried to the recipients in a joint pass
  ([the assignment](docs/about/the-assignment.md)).
- **Solution design** (`40-solution-design.md`): how the things
  wanted are realised, part by part, with the choices they rest on
  ([the solution design](docs/about/the-solution-design.md)).

Below the intent a project takes the layers it needs, none a
condition of another, and many end at the intent.

> A render is never edited by hand: what is iterated is its recipe.

## 5. Documentation

The documentation of the forge is in [`docs/`](docs/README.md):
pages of one topic each, generated from the engine like this README.

- **The user**: begin at [`docs/start/`](docs/start/what-it-is.md),
  then `use/` for every job.
- **The extender**: begin at
  [`docs/extend/`](docs/extend/what-it-is-made-of.md), then
  `reference/` for the shapes.
- **The evaluator**: begin at
  [`docs/about/`](docs/about/what-it-is-and-is-not.md), the concept
  pages, nothing made for him alone.

The documentation was generated on 2026-10-09 for Forge of Thought
at version 4.62; its index says so too.

## 6. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) - petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit
the author and link to this repository.

Feedback, ideas and changes are welcome: see
[CONTRIBUTING.md](CONTRIBUTING.md).

## 7. About this README

This file is a render of `projects/forge`: never edited by hand,
regenerated by `/render readme` whenever the process changes, and by
every `/release` of the engine. Fixes go into the recipe or the
inputs. The documentation in `docs/` is generated the same way, from
the engine, and its index says when and for which version. The YAML
front-matter at the top is the render's provenance, kept by design;
changes to the system are recorded in `projects/forge/`.

_Last updated: 2026-10-10_
