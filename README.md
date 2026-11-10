---
project: forge
render: readme
generated: 2026-11-10
recipe: recipes/readme.md v0.81
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v7.3
  - .claude/skills/forge/states/
  - docs/README.md v7.0
  - RELEASE-NOTES.md
---

# Forge of Thought 7.3

*A workshop where thought is tempered and shaped.* · [Documentation](docs/README.md) · [Videos](https://pche-broken-artist.github.io/forge-of-thought/videos/) · [Release notes](RELEASE-NOTES.md)

**New here? Watch first.** Ten videos and eight short clips of real
sessions, in two languages, show the forge at work before a word of
this README is read: [Videos](https://pche-broken-artist.github.io/forge-of-thought/videos/).

Forge of Thought is an **AI cognitive extension** of a thinking human,
the **principal**: whoever's thinking is being forged. It takes a raw,
half-formed idea - a process redesign, a platform initiative, an
organisational change, a D&D campaign - and tempers it into a precise,
self-contained handover for whoever delivers it: a team, a colleague,
your future self. It rests on one principle - **the machine carries
every part of the work that is not deciding** - in three forms.

- **It thinks with you.** It interviews and probes, criticises,
  challenges and inspires; it extracts what the principal has not yet
  articulated; it lays out options with their trade-offs. It proposes;
  you decide.
- **It keeps the work consistent.** Nothing wanders off in forgotten
  chats: the thinking lives in versioned, templated artefacts, with
  decisions, state and history keeping themselves in order and
  consistency guarded across every output.
- **It carries the tedious work.** Audience-facing outputs - a pitch,
  a deck, this README, the whole documentation - are **renders**:
  generated from the artefacts, regenerated whenever the thinking
  moves, never written by hand twice.

The forge is a place where thoughts are forged. Technically it is a
git repository: slash commands and isolated agents - challenger
personas and critic lenses - for Claude Code, templates, and the
conventions binding them. Today its chain of artefacts is built down
to a solution design.

Short on time? Two one-page notes say it briefly:
[for a CTO](https://github.com/pche-broken-artist/forge/blob/main/renders/cto-pitch.md)
and
[for a CEO](https://github.com/pche-broken-artist/forge/blob/main/renders/ceo-pitch.md).
Each has a Word version beside it.

## 1. Better with AI, or replaced by it?

Forge of Thought is for those who chose to be better. The failure
modes it exists to remove:

- Thinking scattered across chat sessions that die, taking their
  context with them.
- Handovers whose completeness depends on the mood of the day they
  were written.
- The same thinking retold to every audience - a pitch, a deck, a
  mail - each version rewritten by hand and drifting from the others.
- Feedback and decisions with no place to land, so the same ground is
  fought over twice.
- Assumptions nobody attacked before reality did.

## 2. Watch it work

Every video is a real session of the forge, cut to a few minutes and
played in the browser as a simulated terminal with captions, in two
languages, nothing staged.

- **How a brief is born.** A brief found by questions, a critique from
  outside, research, the approval and the mining.
  ([watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#01-brief-elicitation),
  [read](docs/use/write-a-brief.md))
- **One item, one verdict.** A list settled one item per message, with
  the verdict line and one write at the end of the round.
  ([watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#02-walkthrough),
  [read](docs/use/walk-through-a-list.md))
- **From the brief to the intent.** The brief mined into positions,
  rejections and threads, cited at its version.
  ([watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#03-brief-to-intent),
  [read](docs/use/forge-the-intent.md))
- **A critic and walking its findings.** An isolated reviewer of
  document quality, its findings mended or rejected with a reason.
  ([watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#04-critique),
  [read](docs/use/critique-the-documents.md))
- **A check at a save.** A save runs the check, conformance findings
  are settled before the commit, and a release runs more.
  ([watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#05-check-at-save),
  [read](docs/use/save-your-work.md))
- **A challenger: peer review of the substance.** A persona attacks
  the thinking; what is accepted goes into the intent, what is
  rejected keeps its reason.
  ([watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#06-challenger),
  [read](docs/use/challenge-the-thinking.md))
- **History and threads.** Why an item changed is one command away,
  and the open threads are the project's memory.
  ([watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#07-history-threads),
  [read](docs/use/read-the-history-of-an-item.md))
- **Solution design: a new layer of the chain.** The chain grows by a
  definition and a template, up to the first solution design.
  ([watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#08-new-artefact),
  [read](docs/extend/add-an-artefact.md))
- **The BRD, a new artefact.** A new artefact from its definition to
  its first document.
  ([watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#12-brd),
  [read](docs/use/write-a-brd.md))
- **Research: a plan, two LLMs and a synthesis.** The plan confirmed
  before the search, the same cards on two model families, then the
  synthesis.
  ([watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#13-deep-research),
  [read](docs/use/research-a-topic.md))

The whole course is at the
[course page](https://pche-broken-artist.github.io/forge-of-thought/videos/),
where each video has its scenes as chapters and the language is a
switch, and where eight short clips stand in the order of a talk:
the wall between reading git and writing it, the principal deciding
by a letter, a mistake becoming a rule, research planned first,
elicitation one question at a time, handing over, reviewers that
never saw the conversation, and GitHub from an issue to an answer.

## 3. What you get

- A versioned document chain growing from a **brief** - your idea put
  together, yours by your approval - through the **intent**, what you
  hold, to the layers your project needs, an assignment to hand over
  and a solution design among them
  ([the document chain](docs/about/the-document-chain.md)).
- An elicitation interview that forges the intent, one question at a
  time ([elicitation](docs/about/elicitation.md)).
- Blind adversarial reviewers - critics of the documents, challengers
  of the thinking, checks of the conventions - every verdict recorded
  ([the isolated reviewers](docs/about/isolated-reviewers.md)).
- Audience-specific renders generated from a **recipe** each,
  including an actual PowerPoint file through your own template
  ([renders and recipes](docs/about/renders-and-recipes.md)).
- External sources registered immutably and used only as the
  principal directs
  ([sources and research](docs/about/sources-and-research.md)).
- Everything in files and git: nothing depends on a chat's memory
  ([persistence in git](docs/about/persistence-in-git.md)).

## 4. What is new in 7.0

**The forge's own project stands apart.** The project in which the
forge is designed by its own process is now a repository of its own
beside the engine. You clone the engine alone and nothing you run
reads that project
([projects and the engine](docs/about/projects-and-the-engine.md)).

**The scripts are under test.** The scripts have tests with pytest on
a synthetic fixture, a made-up thought project that no real content
enters, in proportion: enough to catch what a change of a script
breaks. A change to a script or a template is proved before it
reaches you ([the tests](docs/about/the-tests.md)).

**User stories are a layer of the chain.** Between a BRD and a
solution design a project may now carry user stories: behaviour seen
from the outside that the stakeholders approve as a whole, the
delivery builds from and the testers test from. The layer was built
by another person in a clone of their own and taken in from the first
merge request of two people, pull request #8
([the user stories](docs/about/the-user-stories.md)).

**The requirement verb is a rule of kind.** An item of an assignment
or a BRD is an obligation in the indicative, never a conditional, a
permission or a wish. An artefact in another language than English
takes that language's own verb of obligation, so `shall` is said only
in English
([requirement style](docs/reference/requirement-style.md)).

**What waits on GitHub is in the map.** With `gh` installed and
signed in, the `/forge` map and `/pull` tell you that a pull request
or an unanswered discussion waits on your repository, before anything
is written into the project. The forge only reads it: it merges,
answers and closes nothing
([see where a project stands](docs/use/see-where-a-project-stands.md)).

**Two fixed files at the root.** The security policy and the code of
conduct stand at the root as fixed texts, derived from nothing and
rendered by nothing. A security problem is reported privately, never
in a public issue
([the security policy and the code of conduct](docs/about/the-security-policy-and-the-code-of-conduct.md)).

**`/test` runs the engine's tests.** One command runs the whole suite,
or the part you name, and gives back the sum, or a red test word for
word as pytest printed it. It fixes nothing and writes nothing, so a
change to a script can be checked at any moment
([run the tests](docs/use/run-the-tests.md)).

The full account is in [RELEASE-NOTES.md](RELEASE-NOTES.md).

## 5. Quickstart

**First, once per machine**

```
# git, Python and Claude Code installed first (docs/start/install.md)
git clone <this repository>      # you are looking at it
claude                           # always from the engine root
/setup                           # first run only (docs/start/setup.md)
```

The forge is developed on Windows; its tests run in CI on Linux and
Windows at every push, and the conversions and the two hooks are
written to run unchanged on Linux and macOS.

**Starting a new project**

```
/new-project my-idea
/forge intent
# in your own terminal, at the engine root: Claude writes nothing
# into git itself; the init and a remote are your one-off act
git -C projects/my-idea init -b main
/save    # a save that commits nothing names its cause (no repository,
         # or no git identity for the host): docs/start/first-result.md
```

**Bringing an existing project**

```
/import-project <project url>    # clones into projects/
/forge <project-slug>            # the slug is the repository's name;
                                 # select the project before any work,
                                 # the forge cannot guess it
```

Each project lives inside `projects/<slug>/` as a git repository of
its own, which the engine does not track: that is why you name it
first. `projects/forge` is the forge's own project, the exemplar every
render and page of the documentation derives from, a public
repository of its own at github.com/pche-broken-artist/forge, cloned
beside the engine by whoever develops it; a user never needs it. The
first sitting from nothing to a saved intent is
[docs/start/first-result.md](docs/start/first-result.md).

## 6. The document chain in one picture

```mermaid
flowchart LR
    B["00-brief"] --> I["10-intent"] --> A["20-assignment"] --> BRD["30-brd"] --> US["35-user-stories"] --> SD["40-solution-design"]
    WP["any document (/work)"] --> RT(["renders: a translation, a summary, a video …"])
    I --> RI(["renders: a pitch, a deck, a summary, a video, a README …"])
    A --> RA(["renders: a mail, a handover deck, a video …"])
    A -.-> RFP["an RFP"]
    I -.-> ST["strategy"]
    SD -.-> IMP["implementation deck"]

    classDef built fill:#1f6feb,stroke:#1158c7,color:#ffffff
    classDef future fill:#c6dbfa,stroke:#1f6feb,color:#24292f
    classDef render fill:#2da44e,stroke:#1a7f37,color:#ffffff
    class B,I,A,BRD,US,SD,WP built
    class RFP,ST,IMP future
    class RI,RA,RT render
```

**Blue = chain artefacts and a work product (light = not built yet),
green = renders, the dots saying the list is open; dashed arrows =
growth that does not exist yet.**

- **Brief:** the principal's idea put together, found with Claude or
  handed over, approved when done ([the brief](docs/about/the-brief.md)).
- **Intent:** the briefs chiselled into what the principal holds
  ([the intent](docs/about/the-intent.md)).
- **Assignment:** the intent's in-scope substance carried to the
  recipients in a joint pass
  ([the assignment](docs/about/the-assignment.md)).
- **BRD:** the business requirements, the assignment or the intent
  broken into rules, behaviour and qualities the stakeholders can
  review and the delivery can estimate ([the BRD](docs/about/the-brd.md)).
- **User stories:** the requirements broken into stories of behaviour
  that the stakeholders approve as a whole, the delivery builds from
  and the testers test from
  ([the user stories](docs/about/the-user-stories.md)).
- **Solution design:** how the things wanted are realised, part by
  part, with the choices they rest on
  ([the solution design](docs/about/the-solution-design.md)).

Below the intent a project takes the layers it needs, none a
condition of another, and many end at the intent.

> A render is never edited by hand: what is iterated is its recipe.

## 7. Planned architecture

![From a monolith to a family of forges](https://raw.githubusercontent.com/pche-broken-artist/forge/main/renders/forge-evolution.png)

Forge of Thought grows in four steps.

1. **Up to 7.0, one monolith.** The general base, the operating layer
   of Forge of Thought and the project that designs it lived in one
   repository.
2. **At 7.0, the definition separated.** The forge's own project, in
   which the forge is designed by its own process, is a repository of
   its own.
3. **Next, the AI engine separated.** The general base, Anvil, with the
   histories, the ledger, research and the mechanics of critique,
   challenge and check, becomes a plugin of Claude Code apart from the
   operating layer of Forge of Thought.
4. **Then further forges.** One forge for everything makes no sense:
   each field needs its own elicitation, lenses and checks. Further
   forges grow on the same base, Forge of Proof for tests and Forge of
   Form for UX/UI and the web prototype, each with its own framework
   and its own definition, an ecosystem rather than one forge.

Anvil, Forge of Proof and Forge of Form are working names.

## 8. Documentation

The documentation of the forge is in [`docs/`](docs/README.md), pages
of one topic each, generated from the engine like this README.

- **The user:** watch how a brief is born
  ([watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#01-brief-elicitation)),
  then begin with [What Forge of Thought is](docs/start/what-it-is.md).
- **The extender:** watch a new artefact
  ([watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#08-new-artefact)),
  then begin with [What the forge is made of](docs/extend/what-it-is-made-of.md).
- **The evaluator:** watch a challenger
  ([watch](https://pche-broken-artist.github.io/forge-of-thought/videos/#06-challenger)),
  then begin with [What the forge is and is not](docs/about/what-it-is-and-is-not.md).

The documentation was generated on 2026-11-08 for version 7.0, and
its index says so too.

- [Start](docs/README.md#start): what the forge is, what to install,
  the first run and a first result.
- [Use](docs/README.md#use): one page per task, from starting a
  project to releasing a version.
- [About](docs/README.md#about): why the forge is as it is, concept by
  concept.
- [Extend](docs/README.md#extend): how an artefact, a lens, a persona,
  a check, a genre, a command, a script or an engine is added.
- [Reference](docs/README.md#reference): the exact shapes, tables and
  rosters, from the commands to the glossary.

Each video is a screenplay rendered from the session records of the
principal's rollout project and made into a player file by
`scripts/md2video.py`. The files live in `docs/videos/`, served as the
course page, and the documentation on making one is the page
[Make a teaching video from a recipe](docs/use/make-a-video-from-a-recipe.md).

## 9. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) - petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit the
author and link to this repository. The code of conduct,
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), is the Contributor Covenant
3.0 under CC BY-SA 4.0.

Feedback, ideas and changes are welcome: see
[CONTRIBUTING.md](CONTRIBUTING.md).

## 10. About this README

This file is a render of `projects/forge`: never edited by hand,
regenerated by `/render readme` whenever the process changes and by
every `/release` of the engine. Fixes go into the recipe or the
inputs. The documentation in `docs/` is generated the same way, from
the engine, and its index says when and for which version. The YAML
front-matter provenance is kept by design; system changes are
recorded in `projects/forge/`.

_Last updated: 2026-11-10_
