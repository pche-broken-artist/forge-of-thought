---
project: forge
render: readme
generated: 2026-10-10
recipe: recipes/readme.md v0.62
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v5.0
  - .claude/skills/forge/states/
  - docs/README.md v5.0
  - RELEASE-NOTES.md
---

# Forge of Thought 5.0

*A workshop where thought is tempered and shaped.* · [Documentation](docs/README.md) · [Release notes](RELEASE-NOTES.md)

Forge of Thought is an **AI cognitive extension** of a thinking
human, the **principal**: the one whose thinking is being forged, who
supplies the ideas, the answers and the decisions, and who alone has
the final word on content. It takes a raw, half-formed idea (a
process redesign, a platform initiative, an organisational change, a
D&D campaign) and tempers it into a precise, self-contained handover
for whoever delivers it: a team, a colleague, your future self. It
rests on one principle, **the machine carries every part of the work
that is not deciding**, in three forms.

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

Technically the forge is a git repository: slash commands and
isolated agents (challenger personas and critic lenses) for Claude
Code, templates, and the conventions binding them. The chain today
runs from a brief through the intent to an assignment and a solution
design; many projects end at the intent.

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
- feedback and decisions with no place to land, so the same ground is
  fought over twice;
- assumptions nobody attacked before reality did.

## 2. What you get

- A versioned document chain growing from a **brief**, your idea put
  together, yours by your approval, through the **intent**, the
  consolidated current state of what you hold, to the layers your
  project needs, an assignment to hand over and a solution design
  among them ([the document chain](docs/about/the-document-chain.md)).
- An elicitation interview that forges the intent: one question per
  message, drawing out what you have not yet articulated, written
  once per round on your word ([elicitation](docs/about/elicitation.md)).
- Blind adversarial reviewers that never see the working
  conversation: critics of the documents, challengers of the
  thinking, checks of the conventions; every verdict is recorded
  ([isolated reviewers](docs/about/isolated-reviewers.md)).
- Audience-specific renders generated from **recipes**, a recipe
  being the iterated thing: inputs, audience, instructions and the
  output template in one versioned file; among the outputs an actual
  PowerPoint or Word file through your own template
  ([renders and recipes](docs/about/renders-and-recipes.md)).
- External sources registered immutably, catalogued, and used only
  as the principal directs
  ([sources and research](docs/about/sources-and-research.md)).
- Everything in files and git: nothing depends on a chat's memory
  ([persistence in git](docs/about/persistence-in-git.md)).

## 3. What is new in 5.0

**Every artefact has a definition of how it is found.** For the
brief, the intent, the assignment and the solution design there is a
state file in `.claude/skills/forge/states/` saying what the artefact
is to achieve, what Claude does and what you do, what the
conversation must cover and how it runs. `/forge brief`,
`/forge intent`, `/forge assignment` and `/forge solution-design` run
by those definitions, so what holds for an artefact is read in one
place and mended there ([elicitation](docs/about/elicitation.md)).

**The working methods stand named, with their reasons.**
Walkthrough, propose never decide, step by step, in pieces, one write
per round, handing over, plain speech, kind not count: each is a word
you can say, and Claude applies it whenever its situation arises. You
can send a long thought in several messages and close with "done",
hand an artefact over in a sentence and judge the proposal that comes
back, or end a message with `??` for an honest opinion
([working methods](docs/about/working-methods.md)).

**The chain grew below the intent to the solution design.** An
intent says what you want and why and does not solve;
`40-solution-design.md` says how the things wanted are realised,
part by part, with the choice each part rests on and what is still
open, so that whoever builds it can do so without you in the room. A
project takes the layers it needs, and many end at the intent
([the solution design](docs/about/the-solution-design.md)).

**The history of a document is a log.** Every versioned document
keeps a companion with one record per change: the reason, what the
text was, and what you must do after it. The release notes and the
commit messages are derived from that log, so the way to every item
is on record and the document itself reads as the current state
([versioning and history](docs/about/versioning-and-history.md)).

**The forge explains itself from its own definitions.** The
documentation in `docs/` is generated from the engine as it stands,
pages of one topic each for the user, the extender and the
evaluator; the scripts are Python and run unchanged on Windows,
Linux and macOS; and `CONTRIBUTING.md` says how to give feedback,
bring an idea or send a change
([the documentation](docs/about/the-documentation.md)).

**`/new-artefact <name>`** adds a new kind of artefact to the forge
and leads to everything a kind needs: its position in the forge
intent, its definition and template, its prefixes, its reviewers and
its place in the solution design. You alone start it, and it decides
nothing ([add an artefact](docs/extend/add-an-artefact.md)).

**`/document [slug]`** generates the documentation of the engine or
of a project into `docs/` in one run that asks nothing: a planner
writes the map, a writer makes each page, and only what changed is
regenerated. Your own project gets its documentation the same way,
when you want it
([generate the documentation](docs/use/generate-the-documentation.md)).

**`/publish <recipe>`** makes the designed Word or PowerPoint file
from a render through a model and its document skills, into
`published/`. It runs only on your command, never by `/render` or by
a release, because it is expensive and takes minutes
([publish a designed file](docs/use/publish-a-designed-file.md)).

**`/man [command | method]`** is the forge's manual, read from its
own definitions at the moment you ask: the commands with their
arguments and purposes, a command's roster and what each entry looks
for, a method's paragraph
([look up a command](docs/use/look-up-a-command.md)).

The full account, with what to do after an upgrade, is in
[RELEASE-NOTES.md](RELEASE-NOTES.md).

## 4. Quickstart

**First, once per machine**

```
git clone <this repository>   # you are looking at it
# install Claude Code first: what to install and how is docs/start/install.md
claude                        # always from the engine root
/setup                        # first run only; what it asks is docs/start/setup.md
```

**Starting a new project**

```
/new-project my-idea
/forge intent
/save
```

**Bringing an existing project**

```
/import-project <project url>   # clones into projects/
/forge <project-slug>           # the slug is the repository's name; select the
                                # project before any work: the forge cannot guess it
```

Each project lives inside `projects/<slug>/` as a git repository of
its own, which the engine does not track: that is why you name it
first. `projects/forge` is the forge's own project, the exemplar
every render and page of the documentation derives from, and the one
directory under `projects/` the engine tracks; a user never needs to
open it. The first sitting from nothing to a saved intent is
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

**Blue = chain artefacts (light = not built yet), green = renders; dashed arrows = growth that does not exist yet.**

- **Brief** (`00-brief.md`): the principal's idea put together,
  composed or finished with Claude or handed over, approved when done
  ([about the brief](docs/about/the-brief.md)).
- **Intent** (`10-intent.md`): the briefs chiselled into what the
  principal holds ([about the intent](docs/about/the-intent.md)).
- **Assignment** (`20-assignment.md`): the intent's in-scope
  substance carried to the recipients in a joint pass
  ([about the assignment](docs/about/the-assignment.md)).
- **Solution design** (`40-solution-design.md`): how the things
  wanted are realised, part by part, with the choices they rest on
  ([about the solution design](docs/about/the-solution-design.md)).

Below the intent a project takes the layers it needs, none a
condition of another, and many end at the intent.

> A render is never edited by hand: what is iterated is its recipe.

## 6. Documentation

The documentation of the forge is in [`docs/`](docs/README.md), pages
of one topic each, generated from the engine like this README.

- **the user**: [`start/`](docs/start/what-it-is.md), then `use/` for every job.
- **the extender**: [`extend/`](docs/extend/what-it-is-made-of.md), then `reference/` for the shapes.
- **the evaluator**: [`about/`](docs/about/what-it-is-and-is-not.md), the concept pages, nothing made for him alone.

It was generated on 2026-10-10 for Forge of Thought at version 5.0,
as its index says too.

**Start**

- [About what the forge is](docs/start/what-it-is.md)
- [Install what the forge needs](docs/start/install.md)
- [Set up the forge](docs/start/setup.md)
- [Get a first result](docs/start/first-result.md)

**Use**

- [Start a project](docs/use/start-a-project.md)
- [Bring in an existing project](docs/use/bring-in-an-existing-project.md)
- [See where a project stands](docs/use/see-where-a-project-stands.md)
- [Write a brief](docs/use/write-a-brief.md)
- [Forge the intent](docs/use/forge-the-intent.md)
- [Distil an assignment](docs/use/distil-an-assignment.md)
- [Design the solution](docs/use/design-the-solution.md)
- [Register a source](docs/use/register-a-source.md)
- [Research a topic](docs/use/research-a-topic.md)
- [Compose a recipe](docs/use/compose-a-recipe.md)
- [Render an output](docs/use/render-an-output.md)
- [Publish a designed file](docs/use/publish-a-designed-file.md)
- [Generate the documentation](docs/use/generate-the-documentation.md)
- [Critique the documents](docs/use/critique-the-documents.md)
- [Challenge the thinking](docs/use/challenge-the-thinking.md)
- [Check conformance](docs/use/check-conformance.md)
- [Walk through a list](docs/use/walk-through-a-list.md)
- [Save your work](docs/use/save-your-work.md)
- [Release a version](docs/use/release-a-version.md)
- [Work on a branch](docs/use/work-on-a-branch.md)
- [Upgrade the engine](docs/use/upgrade-the-engine.md)
- [Spin off a group](docs/use/spin-off-a-group.md)
- [Look up a command](docs/use/look-up-a-command.md)
- [Share material through a library](docs/use/share-material-through-a-library.md)

**About**

- [About what the forge is and is not](docs/about/what-it-is-and-is-not.md)
- [About how a thought travels](docs/about/how-a-thought-travels.md)
- [About the principal and Claude](docs/about/the-principal-and-claude.md)
- [About the working methods](docs/about/working-methods.md)
- [About elicitation](docs/about/elicitation.md)
- [About the document chain](docs/about/the-document-chain.md)
- [About the brief](docs/about/the-brief.md)
- [About the intent](docs/about/the-intent.md)
- [About the assignment](docs/about/the-assignment.md)
- [About the solution design](docs/about/the-solution-design.md)
- [About documents and records](docs/about/documents-and-records.md)
- [About versioning and history](docs/about/versioning-and-history.md)
- [About stable IDs](docs/about/stable-ids.md)
- [About the isolated reviewers](docs/about/isolated-reviewers.md)
- [About the critic](docs/about/the-critic.md)
- [About the challenger](docs/about/the-challenger.md)
- [About the check](docs/about/the-check.md)
- [About renders and recipes](docs/about/renders-and-recipes.md)
- [About the documentation](docs/about/the-documentation.md)
- [About sources and research](docs/about/sources-and-research.md)
- [About projects and the engine](docs/about/projects-and-the-engine.md)
- [About persistence in git](docs/about/persistence-in-git.md)
- [About how the rules are held](docs/about/how-the-rules-are-held.md)
- [About languages](docs/about/languages.md)
- [About where the forge is going](docs/about/where-it-is-going.md)

**Extend**

- [About what the forge is made of](docs/extend/what-it-is-made-of.md)
- [Make a change to the forge](docs/extend/how-a-change-is-made.md)
- [Add an artefact](docs/extend/add-an-artefact.md)
- [Add a critic lens](docs/extend/add-a-critic-lens.md)
- [Add a challenger persona](docs/extend/add-a-challenger-persona.md)
- [Add a check](docs/extend/add-a-check.md)
- [Add a recipe genre](docs/extend/add-a-recipe-genre.md)
- [Add a command](docs/extend/add-a-command.md)
- [Add a script](docs/extend/add-a-script.md)
- [Change a documentation page](docs/extend/change-a-documentation-page.md)

**Reference**

- [Commands](docs/reference/commands.md)
- [Artefacts](docs/reference/artefacts.md)
- [Critic lenses](docs/reference/critic-lenses.md)
- [Challenger personas](docs/reference/challenger-personas.md)
- [Checks](docs/reference/checks.md)
- [Recipe genres](docs/reference/recipe-genres.md)
- [ID scheme](docs/reference/id-scheme.md)
- [Versioning and front-matter](docs/reference/versioning-and-front-matter.md)
- [History companion](docs/reference/history-companion.md)
- [Requirement style](docs/reference/requirement-style.md)
- [Document kinds](docs/reference/document-kinds.md)
- [Ledger](docs/reference/ledger.md)
- [Render provenance](docs/reference/render-provenance.md)
- [Documentation map](docs/reference/documentation-map.md)
- [Verdict words](docs/reference/verdict-words.md)
- [Repository layout](docs/reference/repository-layout.md)
- [Scripts](docs/reference/scripts.md)
- [Templates](docs/reference/templates.md)
- [Configuration](docs/reference/configuration.md)
- [Glossary](docs/reference/glossary.md)

## 7. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) - petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit
the author and link to this repository.

Feedback, ideas and changes are welcome: see
[CONTRIBUTING.md](CONTRIBUTING.md).

## 8. About this README

This file is a render of `projects/forge`: never edited by hand,
regenerated by `/render readme` whenever the process changes and by
every `/release` of the engine. Fixes go into the recipe
(`projects/forge/recipes/readme.md`) or the inputs it reads. The
documentation in `docs/` is generated the same way, from the engine,
and its index says when and for which version. The YAML provenance
at the top of this file is kept by design; changes to the system
itself are recorded in `projects/forge/`.

_Last updated: 2026-10-10_
