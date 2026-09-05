---
project: forge
render: readme
generated: 2026-09-05
recipe: recipes/readme.md v0.37
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v3.34
---

# Forge of Thought 3.34

*A workshop where thought is tempered and shaped.* · [Release notes](RELEASE-NOTES.md)

Forge of Thought is an **AI cognitive extension** of a thinking human,
the **principal** — whoever's thinking is being forged. It takes a
raw, half-formed idea — a process redesign, a platform initiative, an
organisational change, a D&D campaign — and tempers it into a precise,
self-contained handover for whoever delivers it: a team, a colleague,
your future self. It rests on one principle — **the machine carries
every part of the work that is not deciding** — in three forms.

- **It thinks with you.** It interviews and probes, criticises,
  challenges and inspires; it extracts what you have not yet
  articulated and lays out options with their trade-offs. It
  proposes — you decide.
- **It keeps the work consistent.** Nothing wanders off in forgotten
  chats: the thinking lives in versioned, templated artefacts, with
  decisions, state and history keeping themselves in order and
  consistency guarded across every output.
- **It carries the tedious work.** Audience-facing outputs — a pitch,
  a deck, even this README — are **renders**: generated from the
  artefacts through recipes, regenerated whenever the thinking moves,
  never written by hand twice.

Technically, the forge is a git repository: slash commands and
isolated agents — challenger personas and critic lenses — for Claude
Code, templates, and the conventions binding them. Today the chain
ends at the assignment; it is built to grow further without reworking
what exists.

## 1. Better with AI, or replaced by it?

Forge of Thought is for those who chose to be better. The failure
modes it exists to remove:

- Thinking scattered across chat sessions that die, taking their
  context with them.
- Handovers whose completeness depends on the mood of the day they
  were written.
- The same thinking retold to every audience — a pitch, a deck, a
  mail — each version rewritten by hand and drifting from the others.
- Feedback and decisions with no place to land, so the same ground is
  fought over twice.
- Assumptions nobody attacked before reality did.

## 2. What you get

- A versioned document chain growing from a brief — your own text,
  locked verbatim once it is done — to a self-contained assignment.
- An elicitation interview that forges the intent, one question at a
  time.
- Two kinds of blind adversarial reviewers, every verdict recorded.
- Audience-specific renders generated from recipes, including an
  actual PowerPoint file through your own template.
- External sources registered immutably and used only as the
  principal directs.
- Everything in files and git — nothing depends on a chat's memory.

## 3. Quickstart

**First, once per machine**

```
git clone <this repository>      # you are looking at it
# install Claude Code — see Setup below
claude                           # always from the engine root
/setup                           # first run only — fills CLAUDE.local.md, sets the model (Fable)
```

**Starting a new project**

```
/new-project my-idea             # scaffolds the files; your brief is captured verbatim
/forge intent                    # the elicitation interview begins
/save                            # commit and push
```

**Bringing an existing project**

```
/import-project <project url>    # clones into projects/ — the commit identity is proposed
                                 # from your CLAUDE.local.md roster and confirmed by you
/forge <project-slug>            # the slug is the repository's name; select the project
                                 # before any work — the forge cannot guess it
```

Each project lives inside `projects/<slug>/` as a git repository of
its own, which the engine does not track — that is why you name it
first.

## 4. How it is used

### The flow

A thought arrives — a platform initiative you have been turning over
for weeks, or a campaign taking shape for your D&D table. You dump it
as it is, in whatever language and shape it came, into a brief: alone,
or in conversation with the forge (`/forge brief`), which clarifies
where you are terse and asks whether someone has already solved this.
When you are done you lock it, and from that moment it is never
touched again.

Then the forge forges. `/forge intent` interviews you, one question at
a time, and writes what it understood into the intent: positions you
hold, threads still open, directions you rejected and why. You iterate
over days and sessions; nothing lives in the chat, everything lives in
files, so a session can end at any moment and you pick up from the
ledger.

Material arrives as it arrives. A security standard you downloaded
goes into `sources/` through `/ingest` — registered, catalogued, never
edited — and lies there until you say "verify the intent against
section 4 of that standard". Where a topic needs grounding,
`/research` looks up current practice and stores what it found.

Before the next layer is derived, you send in the reviewers. A
challenger persona attacks the substance of the thinking; a critic
lens reads the documents for ambiguity, or distils the essence of each
layer and compares it with the layer above. Neither sees your
conversation, and neither blocks anything: you walk through their
findings one by one and decide.

When the intent holds, `/forge assignment` distils it for the
recipients — the one document they receive, complete and
self-contained. And when the group needs a pitch, you compose a
recipe — optionally guided by a genre interview, `/recipe
presentation` — and `/render` generates the slides from the
artefacts, the actual PowerPoint included; a mail, a summary, this
very README are made the same way and regenerated at every release.
`/save` commits and pushes as you go; `/release` checks, re-renders
and saves from `main`.

### What it looks like in practice

A worked example from a real project will appear here once one is
published.

## 5. How the work feels

The forge is as much a way of working as a set of files, and these are
the named methods of that work — the vocabulary you and Claude share.

- **Walkthrough.** Any list of items needing your decision — findings,
  challenges, open threads, differences between two requirement
  sets — is worked one item at a time, in order of weight: Claude's
  recommendation with a one-sentence reason, then your verdict in a
  word or a counter-proposal, and only then the next item. Never a
  table asking for every verdict at once; "leave it open" is a
  legitimate answer.
- **Propose, never decide.** Claude criticises, challenges, inspires
  and lays out options; you compose.
- **Step by step.** Anything needing your consent — a write, a commit,
  a push, a rename — arrives as one step with the exact operation and
  its reason, and runs on your word; a plan you have seen is not
  consent for its steps.
- **Elicitation interview.** Claude draws out by questions what you
  have not yet articulated; it never fills a gap by assumption.
- **Draft early.** An early draft is an elicitation tool, not an
  output: concrete text sharpens your reaction.
- **Reflect back.** Before anything is written, Claude restates what
  it understood, so the write confirms rather than surprises.
- **Intent-first.** A change of substance goes into the intent and
  propagates from there; only wording is fixed downstream directly.
- **Recommend, do not push.** Every option comes with a recommendation
  and its reason, stated once; a declined recommendation is not
  re-argued without new facts.

None of these is a command: you invoke any of them in a word.

## 6. Roles

| Role | What they own |
|---|---|
| Principal | The thinking being forged: supplies ideas, answers and decisions, and is the final authority on all content. |
| Claude | Structure, order, process discipline and document hygiene: criticises, challenges, inspires and lays out options, but proposes and never decides. |

The standing rules of the collaboration: when unsure, Claude asks
rather than assumes; no new convention, prefix or section is
introduced without your decision; many iterations are the normal
mode; key topics are researched before anything is invented; every
critique and checklist is advisory and only you publish; structure
with stable IDs beats prose even at high abstraction; and every
iteration round is written once, on your confirmation, as one version
bump.

One instance serves one principal, and the recipients collaborate
through the artefacts — more principals means more instances (see
Planned extensions).

## 7. The document chain

```mermaid
flowchart LR
    B["00-brief<br>(draft → locked)"] --> I["10-intent"]
    I --> A["20-assignment"]
    I --> RI(["renders: pitch, deck, summary …"])
    A --> RA(["renders: mail …"])
    A -.-> BRD["30-brd<br>business analysis"]
    A -.-> RFP["an RFP"]
    I -.-> ART["an article"]
    ART -.-> RT(["render: a translation"])
    I -.-> ST["strategy"]
    BRD -.-> SD["40-solution-design"]
    SD -.-> IMP["implementation deck"]

    classDef built fill:#1f6feb,stroke:#1158c7,color:#ffffff
    classDef future fill:#c6dbfa,stroke:#1f6feb,color:#24292f
    classDef render fill:#2da44e,stroke:#1a7f37,color:#ffffff
    class B,I,A built
    class BRD,RFP,ART,ST,SD,IMP future
    class RI,RA,RT render
```

**Blue = chain artefacts (light = not built yet), green = renders;
dashed arrows = growth that does not exist yet.**

Adding a layer is one definition file declaring its inputs — nothing
is renumbered and nothing existing is reworked, which is why files are
numbered in tens. The boundary between chain and render is authorship:
a chain artefact is composed by the principal, a render is generated
from artefacts — the article and its translation in the diagram
illustrate it.

| File | What it is |
|---|---|
| `00-brief.md` | The idea as you wrote it: an intent composed and then locked, free-form, draft until locked. |
| `00-brief-<name>.md` | A later whole of thinking, born under the same rules as the first brief. |
| `10-intent.md` | The working understanding — positions, open threads, rejected directions — rewritten freely, versioned. |
| `20-assignment.md` | The direction handed to the recipients, self-contained and versioned. |
| `<file>.history.md` | The Version History of each versioned document, an append-only companion beside it. |
| `decisions.md` | Append-only DEC records: your decisions with their reasons. |
| `ledger.md` | The single source of truth for state. |

> A locked brief is immutable — composed, then locked, never touched
> again.

The **brief** is your own text: any structure you find useful — prose,
headings, tables, use cases — with no required content and no IDs,
because a required structure would force premature tidiness and
destroy the diagnostic value of how the idea was actually dumped. It
holds thoughts to be processed, not decisions: they may be changed,
reworked or dropped when mined. It is `draft` while being composed and
`approved` (1.0) once you lock it. Three origins are equally legitimate
and indistinguishable to the forge: it arrives finished and is locked
on arrival; it is begun outside and finished with Claude; it is born in
the forge — `/forge brief [name]` is the door for the latter two. A
project may have more than one: every later whole of thinking that
would otherwise land in the intent as a batch of unproven positions is
born as `00-brief-<name>.md`. Every locked brief is mined into the
single intent — positions cite it as provenance, and a whole that dies
on the way leaves the brief locked and one rejected direction with the
reason — with the ledger tracking how far each is mined
(`pending | partial | mined | dropped`).

The **intent** is the consolidated *current* state of what you want,
why, what is open and what was rejected: positions you hold (POS),
open threads to elicit next (THR) and rejected directions with the
reason they were dropped (REJ), each with a stable ID. It is rewritten
for coherence every round rather than appended to, with every change
recorded in its history companion. It exists because chat context dies
and anything of value must live in a file: it is the document to read
when you return to a project after weeks, instead of excavating old
conversations. Its audience is you and Claude only.

The **assignment** is distilled from the intent for the recipients and
is the one document they receive: requirements, out-of-scope items,
constraints, assumptions, deliverables, open questions with an owner
and optional success criteria (REQ, OOS, CON, ASM, DEL, TBC, SCR). It
carries the full in-scope substance of the intent, written as well and
as precisely as possible — complete, assigning rather than solving,
and self-contained, so it can be forwarded without oral tradition.

Substance changes go intent-first and then propagate to the
assignment; only wording is fixed downstream directly. Artefacts are
written once per iteration round, on your confirmation — one version
bump, one history row, however many answers the round contained.
Feedback from the recipients has no channel of its own: you process it
and feed the conclusions back through `/forge intent`.

> A render is never edited by hand — what is iterated is its recipe.

**Renders and recipes.** A render is an audience-specific output
generated from the chain — a pitch for the group, an architecture
picture, an executive summary, the repository README. The iterated
thing is its **recipe** (`recipes/<recipe>.md`): inputs, audience,
instructions and the output template in one versioned file. `/render
<recipe>` regenerates the output into `renders/<recipe>.md` — or the
recipe's own `output:` path — in an isolated subagent that sees only
the recipe and its inputs, overwriting freely, history in git. Every
render opens with YAML front-matter provenance citing the recipe and
each input with their versions, and a render may serve as an input of
another render — a deck citing an architecture picture — when the
recipe declares it. A render assigns nothing and is not part of the
chain: the artefacts stay the source of truth.

**From Markdown to slides.** Everything is Markdown, content only: a
presentation is a `.md` saying what is on each slide. Composing a
recipe may be guided by genre — `/recipe presentation` runs the
interview for a deck, `readme` and `release-notes` are the genres
every project's own README and release notes come from. The one
in-house conversion is `scripts/md2pptx.ps1`, which turns a deck render
into an actual PowerPoint file through headless Claude Code with the
official pptx skill — an LLM conversion by design, because deck
definitions are free-form and may carry instructions for the model. A
`.potx` template is applied when named by path (`-Template <path>`),
typically a document of a library project; without it, Claude designs
the visuals. The `.pptx` lands beside its source render and is never
edited by hand: the Markdown stays the source of truth. All other
format conversion happens outside the forge.

## 8. Two isolated reviewers

Both reviewers run as isolated subagents that see the artefacts only,
never the working conversation — they cannot be told what we really
meant, and that blindness is the source of their value. Both run on
the session model: speed is bought with context, never with a weaker
reviewer.

The **challengers** are a growing roster of persona lenses attacking
the substance of the thinking — unstated assumptions, whether the
objective is the real problem, second-order effects, organisational
reality, failure modes, the counter-case. The first persona is `cto`:
a peer-CTO register, direct, few and sharp, no flattery.

The **critic** is a roster of lenses on the documents: `clarity` reads
each artefact on its own for ambiguity, internal contradiction,
duplication, scope hygiene and Requirement style; `essence` reads the
chain for drift, distilling each layer's essence blind and comparing
it with the layer above — a finding is a difference of essences, not
of texts. The two reviewers are one shape: personas and lenses, one
agent file each carrying a shared skeleton verbatim, CHL and FND as
their outputs; both are invoked by hand, both reports are immutable
and dated, both are settled by walkthrough. Neither runs at a save;
`/release` offers `critique essence` once and runs no reviewer on its
own.

Isolation is not independence. The author, the critic and the
challengers share one model family; what that family systematically
cannot see, none of them will find, so agreement between the reviewers
is never treated as validation — it only means the artefact is
consistent under one set of priors. The calibration point lies outside
the forge: review by humans or by a different model family, invited at
your discretion; challengers running on a different model family are
planned.

### `/challenge <persona> [artefact]`

A target narrows the challenge to that artefact, else the whole chain,
each challenge naming the artefact it concerns; a layer is best
challenged before the next one is first derived from it, while
accepted challenges are still cheap to absorb. Every challenge carries
a severity (dealbreaker, major, minor) and an epistemic status;
fabrication is banned — uncertainty is stated, not papered over. The
report lands in `challenges/YYYY-MM-DD-challenge-<persona>.md`.
Challenge states: open, accepted, rejected (a DEC with its reason),
parked, obsolete. An accepted challenge must change the intent,
otherwise it was not accepted. Bare `/challenge` lists the roster and
recommends a fit.

### `/critique <lens> [artefact]`

With `clarity` a target is that artefact; with `essence` it is that
artefact against its parent; without one, the whole chain. Regression
against resolved findings is every lens's first step. The report lands
in `reviews/YYYY-MM-DD-critique-<lens>.md`. Finding states:

- open
- resolved — an iteration of the artefact concerned
- overruled — a DEC with its reason
- obsolete — the passage no longer exists

Untestable wording is reported as a recommendation, never as a
blocking defect. Bare `/critique` lists the lenses and recommends a
fit.

## 9. Commands

Commands are entry points into phases, not the only permitted door;
the same rules apply in ordinary conversation.

| Command | Purpose |
|---|---|
| `/setup` | First run after cloning the engine: fills `CLAUDE.local.md` by interview, sets the session model to Fable and offers the global git identity guard; never overwrites, runs no git operation. |
| `/new-project <slug>` | Scaffolds a project by kind — files only, never git: a thought project with its brief captured verbatim, or a library (`lib-`) of shared material. |
| `/import-project <git-url>` | Brings an existing project into `projects/` through `scripts/forge-clone.ps1`; the directory is the repository's name and the commit identity is proposed from your roster by the URL's host. |
| `/forge [slug]` | The chain map: which artefacts exist at what versions, which states can be worked from here, which renders are stale, and a recommended next step. |
| `/forge <state> [slug]` | Iterates the named artefact (`brief [name]`, `intent`, `assignment`, …): the command is simply the name of the artefact you want to work on. |
| `/ingest [file] [slug]` | Stores and registers external input in `sources/` and indexes it; bare, it sweeps `sources/` for unregistered files. |
| `/render <recipe> [slug]` | Regenerates a render from its recipe in `recipes/`. |
| `/recipe [genre] [slug]` | Bare, the genre roster; with a genre (`presentation`, `readme`, `release-notes`), guided composition or iteration of a recipe. |
| `/critique [lens] [artefact] [slug]` | Bare, the lens roster; with a lens (`clarity`, `essence`), runs that critic on the named artefact — or, for `essence`, that artefact against its parent — else all. |
| `/challenge [persona] [artefact] [slug]` | Bare, the persona roster; with a persona (e.g. `cto`), runs that challenger against the named artefact, else the whole chain. |
| `/research <topic> [slug]` | Best-practices research stored in `research/` and indexed. |
| `/ledger [slug]` | The quick state readout from the ledger: what exists, in which version and state. |
| `/check [slug]` | Conformance of a project against the current conventions; every project but forge when bare. |
| `/check-forge` | Consistency check of the core and `projects/forge`. |
| `/save [slug] [-m "message"] [-Tag name]` | Commits and pushes on the current branch — no check, no renders; a tag on request. |
| `/release [slug] [-m "message"] [-Tag name]` | From `main` only: check, README and release notes re-rendered, then a save with the release message and the tag `v<major>` at an approved major; asks for the repository when no slug is given. |
| `/spinoff <project> <group> <slug>` | Splits a requirement group into a project of its own — only on your explicit decision. |

`/ingest` stores, registers and catalogues — nothing more: every
binary file gets one question, convert to Markdown or keep the binary
as the source, and registration never implies intake — you alone
direct how and when a source is used. `/save` is the fast door: a
commit message proposed and confirmed, the script run, seconds; it
runs on whatever branch is checked out. `/release` is the slow one:
it refuses off `main`, runs the conformance check and settles its
findings with you, offers `critique essence` once, re-renders the
README and the release notes from the settled sources and reports
what materially changed in them, then saves with the release message
and, at an approved major, the tag. Plain conversation works too — the
commands are doors, not the only way in.

### A typical journey

- You have an idea and write it down as it comes — your project's
  brief — and lock it once it says what you mean (`/new-project`,
  `/forge brief`).
- Over several sessions the forge interviews you and the intent takes
  shape: positions, open threads, rejected directions, each with its
  ID (`/forge intent`).
- A standard you downloaded and a meeting transcript join the
  project's sources; you decide when each is used (`/ingest`).
- Before the assignment is derived you send in the reviewers: a
  peer-CTO challenger attacks the substance, the critic reads the
  documents; you walk through every challenge and finding and record
  your verdicts (`/challenge cto`, `/critique clarity`).
- The group wants a pitch: you compose a presentation recipe through
  its interview, render the deck and turn it into an actual PowerPoint
  through your template (`/recipe presentation`, `/render`,
  `scripts/md2pptx.ps1`).
- The intent holds, and the assignment is distilled from it — the one
  document the recipients receive (`/forge assignment`).
- You save as you go, and release from `main` when a version is worth
  publishing: checked, README and release notes regenerated (`/save`,
  `/release`).

## 10. Conventions

**IDs and numbering.** Every item carries an ID of the form
`PREFIX.NNNN`, all prefixes three letters. IDs are global and stable —
never renumbered — and an item may move between groups without
changing its ID. Items are numbered in tens (`REQ.0010, REQ.0020`),
each new group starting at the next hundred (`REQ.0100, REQ.0110`);
overflow takes the next free number anywhere. Groups are plain
headings — no IDs, no metadata, no lifecycle — and depth is capped at
two levels.

| Prefix | Meaning | Lives in |
|---|---|---|
| REQ | requirement | assignment |
| OOS | out of scope / do-not | assignment |
| CON | constraint — deliberate boundary, not to be challenged | assignment |
| ASM | assumption | assignment |
| DEL | deliverable — may delegate work ("produce NFRs and return") | assignment |
| TBC | open question / to be confirmed, with owner | assignment |
| SCR | success criterion — optional or delegated | assignment |
| POS | position the principal currently holds | intent |
| THR | open thread — unresolved matter to elicit next | intent |
| REJ | rejected direction, with the reason it was dropped | intent |
| FND | critique finding (document quality) | ledger, reviews |
| CHL | peer-review challenge (substance) | ledger, challenges |
| DEC | decision, incl. overruled findings and rejected challenges | decisions.md |

**Terms.** Every assignment carries a Terms section listing the
prefixes and any domain terms it actually uses; defined terms are
capitalised in item text to signal they appear there.

**Language.** The forge dictates the output language: all documents
are written in English. The briefs are the exception, stored verbatim
in whatever language they were written. The conversation language is
per-instance configuration and lives in `CLAUDE.local.md`.

**Requirement style.** Items use *shall* / *shall not* — never would,
could, should, might, may or MoSCoW wording. There is no priority
column and no priority tag: everything in an assignment is essential,
and an exception carries a note reading *optional*. Each item covers
one idea, is written once, in a full, correct UK English sentence, and
must not depend on an external link to be understood, agreed or later
tested. Testability is recommended, not required: delegating
concretisation through a DEL item is a legitimate outcome. An
illustrative item:

> REQ.0010 The Platform shall record every request and every response
> passing through the Gateway, with the identity of the requesting
> User and the time.

**Completeness over brevity.** An assignment carries the full in-scope
substance of the intent; nothing is omitted for brevity's sake, and
length is whatever fidelity requires. Leaving a matter out is
legitimate only as an explicit delegation — a DEL or TBC item. The
boundary is one sentence: an assignment assigns, it does not solve;
the machinery of executing delivery belongs to the recipients, while
any apparatus may appear where you judge it part of setting direction.

**Versioning.** Integers denote signed-off versions: `0.1, 0.2, …` are
drafts before first approval, `1.0` is approved, `1.1, 1.2, …` are
changes made after approval and not yet approved themselves, `2.0` the
next approved version. Front-matter carries `version`, `date`,
`status` (`draft | in_review | approved | superseded`) and
`last_change`, and the status must agree with the number.

**Document kinds.** "Document" is the word for every file of a
project; "artefact" is reserved for the documents of the chain — the
ones the principal composes, the reviewers read and the renders are
generated from. Every document has one kind, and the kind says what it
is, who writes it, whether it is versioned and how it behaves:

| Group | Kind | Meaning | Written by | Versioned | Behaviour |
|---|---|---|---|---|---|
| artefacts | brief | the idea as the principal wrote it | principal | yes | locked at 1.0, then immutable |
| artefacts | intent | current understanding for principal and Claude: positions, threads, rejections | Claude, principal composes | yes | rewritten freely |
| artefacts | assignment | the direction handed to the recipients, self-contained | Claude, principal composes | yes | rewritten freely |
| artefacts | later artefacts (BRD, RFP, article…) | further layers, each derived from the one above | Claude, principal composes | yes | rewritten freely |
| records | history | what changed in a versioned document, and why | forge | — | append-only |
| records | decisions | the principal's decisions with reasons | forge | — | append-only |
| records | review, challenge | one dated reviewer run | reviewer agent | — | immutable |
| state | ledger | single source of truth for state | forge | — | freely rewritten |
| state | index | catalogue of a resource directory | forge | — | freely rewritten |
| rendering | recipe | how a render is made | Claude, principal iterates | yes | iterated, never approved |
| rendering | render | audience-specific output, never a source of truth | generated | — | overwritten by /render |
| resources | source | external input as it arrived | external, /ingest | — | immutable |
| resources | research | durable answer to one question | Claude, /research | — | immutable |

Every versioned kind keeps its Version History in an append-only
companion `<file>.history.md` beside it, never in its body, with
`last_change` in the front-matter summarising the newest row. An
integer version is approved, and a recipe never is: it carries a
version and an updated date, no status, and stays 0.x for life.

**Project kinds.** A project has a kind, declared in the header of its
ledger: `thought` — the chain — or `library`, a collection of material
shared across projects with no chain: a ledger, sources and research
with their indexes, and a README that catalogues what it holds. A
library's slug carries the prefix `lib-`; another project cites a
library document by path and registers the dependency in its ledger.
Slugs are lowercase and hyphenated on disk — `forge` is the system's
own project — and display names may differ.

## 11. Repository layout

```
CLAUDE.md                  # this file — universal core
CLAUDE.local.md            # instance facts (principal, conversation
                           # language) — gitignored, created by
                           # /setup from templates/CLAUDE.local.md
README.md                  # for humans — a render (/render readme)
RELEASE-NOTES.md           # release notes — a render (/render
                           # release-notes): Unreleased head +
                           # one frozen section per approved major
logo.png                   # project avatar
LICENSE                    # CC BY 4.0 — the engine is published
                           # under attribution
scripts/                   # forge-save / forge-pull / forge-status
                           # / forge-clone / forge-branch (git),
                           # doc2md (document →
                           # Markdown), md2pptx (deck render →
                           # PowerPoint)
.claude/                   # commands, agents, settings
                           # (settings.local.json: the session
                           # model — gitignored)
templates/                 # canonical skeletons
projects/                  # gitignored (projects/*) except
                           # projects/forge — every other project is
                           # a git repository of its own, which the
                           # engine does not know
projects/<slug>/           # kind: thought — the chain
  .git/                               # the project's own repository
  README.md  RELEASE-NOTES.md         # renders of recipes/readme.md and
                                      # recipes/release-notes.md,
                                      # regenerated by every /release
  logo.png                            # optional project avatar
  00-brief.md  10-intent.md  20-assignment.md
  00-brief-<name>.md                  # later briefs, one per whole
  <file>.history.md                   # Version History of each
                                      # versioned document (brief,
                                      # intent, assignment, recipe):
                                      # append-only companion
  decisions.md  ledger.md             # ledger header carries kind:
  sources/00-INDEX.md                 # resource index (rewritten):
                                      # What / Origin / Role / Use for
  sources/<name>.<ext>                # immutable external inputs, one
                                      # form each: <slug>.md extract of
                                      # a binary, or the binary itself
  sources/.gitignore                  # originals converted in place
  sources/<slug>/                     # bundle of related files = one
                                      # source, one ledger entry;
                                      # catalogued by its 00-INDEX.md
  research/00-INDEX.md                # resource index (rewritten):
                                      # Question / Answer / Consult when
  recipes/<recipe>.md                 # render recipes: inputs, audience,
                                      # instructions, template — iterated
  recipes/<recipe>.history.md         # the recipe's Version History
  renders/<recipe>.md                 # generated outputs, overwritten by
                                      # /render, provenance front-matter
  renders/<recipe>.pptx               # optional deck generated from the
                                      # md render by scripts/md2pptx.ps1
  reviews/YYYY-MM-DD-critique-<lens>.md  # immutable critique runs
  challenges/YYYY-MM-DD-challenge-<persona>.md  # immutable peer reviews
  research/YYYY-MM-DD-<topic>.md      # immutable research notes
  CLAUDE.md                # optional project-specific polish
projects/lib-<name>/       # kind: library — material shared across
  .git/  ledger.md         # projects, no chain: only the ledger,
  README.md  logo.png      # sources and research; documents
  recipes/readme.md        # maintained by their owner; README =
  sources/00-INDEX.md      # the catalogue, a render of its recipe
  research/00-INDEX.md
```

## 12. Setup

### Prerequisites

- git
- PowerShell 7 (`pwsh`) — the scripts are PowerShell and run
  unchanged on Windows, macOS and Linux, so it is needed on macOS and
  Linux too
- Python 3 — for markitdown, the engine behind `doc2md.ps1`
- A paid Claude subscription — Claude Code's usage draws from the
  same pool as Claude chat

### Getting the forge and Claude Code

Clone this repository: it is the engine. Then install Claude Code:

- Windows: `irm https://claude.ai/install.ps1 | iex`
- macOS/Linux: `curl -fsSL https://claude.ai/install.sh | bash`
- or, with Node: `npm install -g @anthropic-ai/claude-code`

Sign in on first run. Always start `claude` from the engine root, so
that `CLAUDE.md` and `CLAUDE.local.md` load.

Then run `/setup` once. It creates `CLAUDE.local.md` from its template
and fills it with you in a short interview — who the principal is, the
conversation language, your git identities per host — gitignored,
never committed. It creates `.claude/settings.local.json` with the
session model set to Fable, the strongest available model, which the
whole forge including the blind reviewers runs on; it tells you so in
one sentence, and `/model` or editing that file changes it at any time
(permissions come from the shared `.claude/settings.json`). It closes
by offering one global git guard — `user.useConfigOnly = true`
appended to `~/.gitconfig` — so that a repository without a local
identity fails aloud instead of committing with a default; declined,
it prints the line for you to apply by hand. The identities themselves
are set per repository, proposed from your roster at every project
creation or import. `/setup` never overwrites existing files.

Upgrading the engine is `scripts/forge-pull.ps1` — a fast-forward of
`main`; your projects are untouched by it.

### Your projects

Each project is a directory under `projects/` and a git repository of
its own. `/new-project` creates the files; `git init` in that
directory, and a remote if you want one, are a one-off act of yours.
The commit identity belongs to the project: it is set locally in the
repository, proposed from the identity roster in `CLAUDE.local.md` by
the origin's host and confirmed by you.

An existing project is brought in with `/import-project <git-url>`,
which clones it into `projects/<repository name>` through
`scripts/forge-clone.ps1`, sets the identity you confirm and reports
the identity the clone ended up with.

The engine ignores `projects/*` (except its own `projects/forge`), and
the scripts find your project through its `.git`. A project without a
repository is reported as "not under git" — a fact, not an error.

### Script prerequisites

- `doc2md.ps1` needs markitdown:
  `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.
- `md2pptx.ps1` needs the `document-skills` plugin, installed once
  from an interactive Claude Code session:
  `/plugin marketplace add anthropics/skills`, then
  `/plugin install document-skills@anthropic-agent-skills`. A deck
  template is named by path (`-Template <file.potx>`) — typically a
  document of a library project — or left out, in which case Claude
  designs the visuals.
- The git scripts need nothing beyond git.

### Saving and syncing

Two doors, two speeds. `/save` commits and pushes on whatever branch
is checked out — no check, no render. `/release`, from `main` only,
runs the conformance check and settles its findings with you, offers
`critique essence` once, re-renders the README and the release notes
from the settled sources and then saves with the release message and,
at an approved major, the tag `v<major>`.

Underneath both lie the scripts in `scripts/`, the only intended door
to git — reading state included. Each serves the engine and every
project repository alike: a bare `forge-save` commits each repository
with changes on its own and pushes where it has a remote, and without
a remote the commit is kept and reported. `main` is the released line;
branches are voluntary — `forge-branch <name>` creates or switches,
`forge-branch main` switches back, and merging stays with git, by hand
or by merge request. One remote per repository, configured in git
itself: the forge carries no URL anywhere.

## 13. Scripts

| Script | Purpose | When it runs | Install note |
|---|---|---|---|
| `scripts/forge-save.ps1` | Commits and pushes: bare, every repository with changes, each its own commit; with a slug, that one (`forge` meaning the engine); reconciles remote changes by rebase, prints the commit's file summary, and `-Tag <name>` tags the commit and pushes the tag. | Under `/save` and `/release`, or from the shell. | — |
| `scripts/forge-pull.ps1` | Fast-forwards from the remotes and never touches a repository with unsaved changes; on the engine it is the upgrade channel. | When you upgrade the engine or pull a project. | — |
| `scripts/forge-status.ps1` | Reports unsaved changes, the branch, the last commit and the origin of each repository without changing anything. | Whenever you want to know where things stand. | — |
| `scripts/forge-clone.ps1` | Clones an existing project into `projects/<repository name>`, never overwriting, and sets its local commit identity when given `-Name` and `-Email`. | Under `/import-project`. | — |
| `scripts/forge-branch.ps1` | Switches one repository to a branch, creating it when it does not exist (`main` switches back); refuses over unsaved changes and does nothing else. | When you want a branch. | — |
| `scripts/doc2md.ps1` | Converts a binary document into the Markdown extract that becomes the source. | Under `/ingest`, when you say yes to converting a binary. | markitdown — see Setup. |
| `scripts/md2pptx.ps1` | Turns a Markdown deck render into a `.pptx` through headless Claude Code, with a `.potx` template named by path or Claude's own design. | After a presentation render, when the PowerPoint is wanted. | `document-skills` plugin — see Setup. |

## 14. Planned extensions

The chain is meant to grow downward, as far as its owner needs a
thought taken: a BRD layer is certain to come, solution architecture
and integration are intended, a strategy layer is possible if it
proves to make sense. Which layers are added, and in what order, is
open, and nothing is approved for construction: the mechanics of a
layer — its commands, agents and reviewer calibration — are designed
when that layer is actually taken up, not in advance.

One instance serves one principal. A second principal receives the
forge — `projects/forge` included — through git and runs an instance
of their own; how genuine multi-user operation would work is open and
deliberately not being worked on now.

`projects/forge/` is the system's own project: Forge of Thought run
through its own process, with its brief, its intent of design
positions, open threads and rejected directions, its decisions and its
ledger. A process change is complete only once that intent is updated
and this README re-rendered.

## 15. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) — petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit
the author and link to this repository.

## 16. About this README

This file is a render of `projects/forge`: never edited by hand,
regenerated by `/render readme` whenever the process changes — and by
every `/release` of the engine. Fixes go into the recipe
(`projects/forge/recipes/readme.md`) or its inputs, `CLAUDE.md` and
the forge intent. The YAML front-matter provenance at the top is kept
by design. Changes to the system itself are recorded in
`projects/forge/`.

_Last updated: 2026-09-05_
