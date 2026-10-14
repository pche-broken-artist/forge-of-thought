---
project: forge
render: readme
generated: 2026-10-14
recipe: recipes/readme.md v0.66
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v5.9
  - .claude/skills/forge/states/
  - docs/README.md v5.9
  - RELEASE-NOTES.md
---

# Forge of Thought 5.9

*A workshop where thought is tempered and shaped.* · [Documentation](docs/README.md) · [Videos](https://pche-broken-artist.github.io/forge-of-thought/videos/) · [Release notes](RELEASE-NOTES.md)

**New here? Watch first.** Eight short videos of real sessions, seven
to fifteen minutes each, in two languages, show the forge at work
before you read a word of this README: [Videos](https://pche-broken-artist.github.io/forge-of-thought/videos/).

Forge of Thought is an **AI cognitive extension** of a thinking human,
the **principal**: the one whose thinking is being forged, who
supplies the ideas, the answers and the decisions, and who has the
final word on all content. It takes a raw, half-formed idea (a process
redesign, a platform initiative, an organisational change, a D&D
campaign) and tempers it into a precise, self-contained handover for
whoever delivers it: a team, a colleague, your future self. It rests
on one principle, **the machine carries every part of the work that
is not deciding**, in three forms.

- **It thinks with you.** It interviews and probes, criticises,
  challenges and inspires; it extracts what you have not yet
  articulated and lays out options with their trade-offs. It
  proposes; you decide.
- **It keeps the work consistent.** Nothing wanders off in forgotten
  chats: the thinking lives in versioned, templated artefacts, with
  decisions, state and history keeping themselves in order and
  consistency guarded across every output.
- **It carries the tedious work.** Audience-facing outputs, a pitch, a
  deck, this README, the whole documentation, are **renders**:
  generated from the artefacts, regenerated whenever the thinking
  moves, never written by hand twice.

Technically, Forge of Thought is a git repository: slash commands and
isolated agents, challenger personas and critic lenses, for Claude
Code, templates, and the conventions binding them. Today the chain
runs from a brief through the intent to an assignment and a solution
design; that is where it ends at this version, and a project ends it
wherever it needs to.

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
- the same thinking retold to every audience, a pitch, a deck, a
  mail, each version rewritten by hand and drifting from the others;
- feedback and decisions with no place to land, so the same ground is
  fought over twice;
- assumptions nobody attacked before reality did.

## 2. Watch it work

Every video is a real session of the forge, cut to a few minutes and
played in the browser as a simulated terminal with captions, in two
languages, nothing staged.

- **How a brief is born.** A brief found by questions, a critique
  from outside, research, the lock, the mining.
  [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#01-brief-elicitation) ·
  [read](docs/use/write-a-brief.md)
- **One item, one verdict.** A list settled one item per message, the
  verdict line, one write at the end of the round.
  [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#02-walkthrough) ·
  [read](docs/use/walk-through-a-list.md)
- **From the brief to the intent.** The brief mined into positions,
  rejections and threads, cited at its version.
  [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#03-brief-to-intent) ·
  [read](docs/use/forge-the-intent.md)
- **A critic and walking its findings.** An isolated reviewer of
  document quality, its findings mended or rejected with a reason.
  [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#04-critique) ·
  [read](docs/use/critique-the-documents.md)
- **A check at a save.** A save runs the check, conformance findings
  settled before the commit, a release with more.
  [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#05-check-at-save) ·
  [read](docs/use/save-your-work.md)
- **A challenger: peer review of the substance.** A persona attacks
  the thinking; accepted goes into the intent, rejected keeps its
  reason.
  [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#06-challenger) ·
  [read](docs/use/challenge-the-thinking.md)
- **A layer below the intent and a new artefact.** The chain grows by
  a definition and a template, the first solution design.
  [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#07-new-artefact) ·
  [read](docs/extend/add-an-artefact.md)
- **History and threads.** Why an item changed, one command away; the
  open threads as the project's memory.
  [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#08-history-threads) ·
  [read](docs/use/read-the-history-of-an-item.md)

The whole course is at the [course page](https://pche-broken-artist.github.io/forge-of-thought/videos/),
where each video has its scenes as chapters and the language is a
switch.

## 3. What you get

- A versioned document chain growing from a **brief**, your idea put
  together, yours by your approval, through the **intent** to the
  layers your project needs, an assignment to hand over and a
  solution design among them
  ([The document chain](docs/about/the-document-chain.md)).
- An elicitation interview that forges the intent: one question per
  message, drawing out what you have not yet articulated
  ([Elicitation](docs/about/elicitation.md)).
- Blind adversarial reviewers, critics of the documents, challengers
  of the thinking, checks of the conventions, none of them seeing the
  conversation, every verdict recorded
  ([The isolated reviewers](docs/about/isolated-reviewers.md)).
- Audience-specific renders generated from **recipes**, including an
  actual PowerPoint file through your own template
  ([Renders and recipes](docs/about/renders-and-recipes.md)).
- External sources registered immutably and used only as the
  principal directs
  ([Sources and research](docs/about/sources-and-research.md)).
- Everything in files and git: nothing depends on a chat's memory
  ([Persistence in git](docs/about/persistence-in-git.md)).

## 4. What is new in 5.0

**How a thought is found.** Every artefact of the chain now has a
definition of its elicitation, in the state files of `/forge`, and
the working methods stand named with their reasons; the chain grew
below the intent to the solution design, with the cut between what is
wanted and what realises it, and the history of a document became a
log the release notes derive from. You can find an artefact together
by questions or hand it over in a word, and read in its state file
what holds for it ([Elicitation](docs/about/elicitation.md)).

**How the forge is read.** The forge explains itself from its own
definitions: the documentation is generated by `/document`, the
scripts are in Python, and `CONTRIBUTING.md` says how to give
feedback. What you read about the engine is made from the engine as
it stands, never from an account that may have drifted from it
([The documentation](docs/about/the-documentation.md)).

**`/new-artefact <name>`** adds a new kind of artefact to the forge
and leads to everything a kind needs: its position in the forge
intent, its definition and template, its prefixes, its reviewers and
its place in the solution design. You alone start it, and it decides
nothing ([Add an artefact](docs/extend/add-an-artefact.md)).

**`/document`** generates the documentation of the engine or of a
project: pages of one topic each, for the user, the extender and the
evaluator, from a map it writes itself. A page mirrors its owner or
is derived from the project's documents, and is never a source of
truth
([Generate the documentation](docs/use/generate-the-documentation.md)).

**`/publish <recipe>`** makes the designed Word or PowerPoint file
from a render through a model, into `published/`. You alone start
it; it converts the Markdown you have read and renders nothing
([Publish a designed file](docs/use/publish-a-designed-file.md)).

**`/man [command or method]`**, alias `/manual`, is the forge's
manual, read from its own definitions: bare, it lists the commands
and the working methods; with a command, it shows what that command
does and its roster ([Look up a command](docs/use/look-up-a-command.md)).

The full account, with what each release changed and what to do after
an upgrade, is in [RELEASE-NOTES.md](RELEASE-NOTES.md).

## 5. Quickstart

**First, once per machine**

```
# git, Python and Claude Code must be installed first: docs/start/install.md
git clone <this repository>    # you are looking at it
cd forge-of-thought            # the engine root
claude                         # always start it from the engine root
/setup                         # first run only; what it asks: docs/start/setup.md
```

**Starting a new project**

```
/new-project my-idea
/forge intent
git -C projects/my-idea init -b main   # in your own terminal, at the engine root:
                                       # Claude is not allowed to run git; a remote may follow
/save                                  # a save that commits nothing names its cause (no repository,
                                       # or no git identity for the host); docs/start/first-result.md says what to do
```

**Bringing an existing project**

```
/import-project <project url>   # clones into projects/
/forge <project-slug>           # the slug is the repository's name; select the project
                                # before any work: the forge cannot guess it
```

Each project lives inside `projects/<slug>/` as a git repository of
its own, which the engine does not track: that is why you name it
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
  handed over, approved when done ([The brief](docs/about/the-brief.md)).
- **Intent**: the briefs chiselled into what the principal holds
  ([The intent](docs/about/the-intent.md)).
- **Assignment**: the intent's in-scope substance carried to the
  recipients in a joint pass
  ([The assignment](docs/about/the-assignment.md)).
- **Solution design**: how the things wanted are realised, part by
  part, with the choices they rest on
  ([The solution design](docs/about/the-solution-design.md)).

Below the intent a project takes the layers it needs, none a
condition of another, and many end at the intent.

> A render is never edited by hand: what is iterated is its recipe.

## 7. Documentation

The documentation of the forge is in [`docs/`](docs/README.md):
pages of one topic each, generated from the engine like this README.

- **The user**: [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#01-brief-elicitation) how a brief is born, then begin at [What Forge of Thought is](docs/start/what-it-is.md).
- **The extender**: [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#07-new-artefact) a new artefact being added, then begin at [What the forge is made of](docs/extend/what-it-is-made-of.md).
- **The evaluator**: [watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#06-challenger) a challenger at work, then begin at [What the forge is and is not](docs/about/what-it-is-and-is-not.md).

The documentation was generated on 2026-10-14 for Forge of Thought at
version 5.9, and its index says so too.

- [Start](docs/README.md#start): what the forge is, what to install,
  what `/setup` asks, and the first sitting to a saved intent.
- [Use](docs/README.md#use): one page per command and per working
  situation, from starting a project to ending a session.
- [About](docs/README.md#about): what the forge is and is not, how a
  thought travels through it, and why each of its mechanisms is as it
  is.
- [Extend](docs/README.md#extend): how a change to the forge is made,
  and how an artefact, a lens, a persona, a check, a genre, a command
  or a script is added.
- [Reference](docs/README.md#reference): the commands, the artefacts,
  the reviewers, the scheme of IDs and versions, the layouts and the
  templates, exactly.

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

This file is a render of `projects/forge`: never edited by hand,
regenerated by `/render readme` whenever the process changes, and by
every `/release` of the engine. Fixes go into the recipe
(`projects/forge/recipes/readme.md`) or into the inputs it reads. The
documentation in `docs/` is generated the same way, from the engine,
and its index says when and for which version. The YAML front-matter
at the top is the render's provenance and is kept by design. Changes
to the system itself are recorded in `projects/forge/`.

_Last updated: 2026-10-14_
