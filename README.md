---
project: forge
render: readme
generated: 2026-09-04
recipe: recipes/readme.md v0.35
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v3.21
---

# Forge of Thought 3.21

*A workshop where thought is tempered and shaped.* · [Release notes](RELEASE-NOTES.md)

Forge of Thought is an **AI cognitive extension** of a thinking human,
the **principal** — whoever's thinking is being forged. It takes a raw,
half-formed idea — a process redesign, a platform initiative, an
organisational change, a D&D campaign — and tempers it into a precise,
self-contained handover for whoever delivers it: a team, a colleague,
your future self. It rests on one principle — **the machine carries
every part of the work that is not deciding** — in three forms.

- **It thinks with you.** It interviews and probes, criticises,
  challenges, inspires; it extracts what you have not yet articulated
  and lays out options with their trade-offs. It proposes — you decide.
- **It keeps the work consistent.** Nothing wanders off in forgotten
  chats: the thinking lives in versioned, templated artefacts, with
  decisions, state and history keeping themselves in order and
  consistency guarded across every output.
- **It carries the tedious work.** Audience-facing outputs — a pitch,
  a deck, even this README — are **renders**: generated from the
  artefacts through recipes, regenerated whenever the thinking moves,
  never written by hand twice.

Technically, Forge of Thought is a git repository: slash commands and
isolated agents — challenger personas and critic lenses — for Claude
Code, templates, and the conventions binding them. Today the chain of
documents ends at the assignment; it is numbered and shaped to grow
further without reworking anything that exists.

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

- A versioned document chain growing from a **brief** — your own
  text, locked verbatim once it is done — through the **intent**, the
  consolidated current state of what you want, to a self-contained
  **assignment** for whoever delivers it.
- An elicitation interview that forges the intent: one question at a
  time, drawing out what you have not yet articulated.
- Two kinds of blind adversarial reviewers — a **challenger** on the
  substance of the thinking, a **critic** on the quality of the
  documents — with every verdict recorded.
- Audience-specific renders generated from **recipes**, including an
  actual PowerPoint file through your own template.
- External sources registered immutably and used only as you direct.
- Everything in files and git — nothing depends on a chat's memory.

## 3. Quickstart

**First, once per machine**

```
git clone <this repository>   # you are looking at it
                              # install Claude Code first — see Setup
claude                        # always from the engine root
/setup                        # first run only — fills CLAUDE.local.md, sets the model (Fable)
```

**Starting a new project**

```
/new-project my-idea
/forge intent
/save
```

**Bringing an existing project**

```
/import-project <project url>   # clones into projects/ — the commit identity is proposed from your CLAUDE.local.md roster and confirmed by you
/forge <project-slug>           # the slug is the repository's name; select the project before any work — the forge cannot guess it
```

Each project lives inside `projects/<slug>/` as a git repository of
its own, which the engine does not track — that is why you name it
first.

## 4. How it is used

### The flow

A thought arrives — a process you want redesigned, a platform you want
built, a campaign taking shape for your D&D table — and you dump it as
a brief, alone or in conversation with the forge (`/forge brief`), in
whatever shape and language it came. When it says what you meant, you
lock it, and from then on it is the record your later thinking is
measured against.

Then the interview starts. `/forge intent` asks you one question at a
time and reflects back what it heard; over days and sessions the
intent grows into positions you hold, threads still open and
directions you rejected with the reason, every one of them with a
stable ID. Nothing lives in the chat: you can close the session at any
point and `/ledger` re-orients you when you come back.

Material arrives as it will. A security standard you downloaded goes
in through `/ingest`, registered and catalogued but not read into your
thinking until you say so — weeks later you may ask that the intent be
verified against it. Where a topic needs grounding, `/research` looks
up current practice and files what it found.

When the intent feels solid, you send in the reviewers. `/challenge
cto` attacks the substance the way a peer would; `/critique clarity`
and `/critique essence` read the documents for ambiguity and for
drift between the layers. Neither has seen your conversation, and
neither can stop you: you walk through what they found, item by item,
and decide.

Then you distil: `/forge assignment` produces the one document your
recipients receive, complete and self-contained. And from the same
chain come the outputs for everyone else — a pitch for the group, a
deck with slides, a mail, this very README — each generated from a
recipe you iterate rather than from a text you rewrite; composing a
recipe can be guided by a genre interview (`/recipe presentation`),
and a deck render becomes an actual PowerPoint file. Whenever the
chain moves, `/save` checks the project, regenerates what depends on
it and commits.

### What it looks like in practice

A worked example from a real project will appear here once one is
published.

## 5. How the work feels

The forge is as much a way of working as a set of files, and these are
the named methods of that work — the vocabulary you and Claude share.

- **Walkthrough.** Any list of items needing your decision — critique
  findings, challenges, open threads, differences between two
  requirement sets — is worked one item per message, in order of
  weight: Claude's recommendation with a one-sentence reason, then
  your verdict in a word or a counter-proposal, "leave it open"
  included. Never a table asking for every verdict at once, and every
  command that produces a list ends by offering one.
- **Propose, never decide.** Claude criticises, challenges, inspires
  and lays out options; you compose.
- **Step by step.** Anything needing your consent — a write, a
  commit, a push, a rename — arrives as one step with the exact
  operation and reason, and runs on your word; a plan you have seen
  is not consent for its steps.
- **Elicitation interview.** Claude draws out by questions what you
  have not yet articulated, never filling a gap by assumption.
- **Draft early.** An early draft is an elicitation tool, not an
  output: concrete text sharpens your reaction.
- **Reflect back.** Before writing, Claude restates what it
  understood, so the write confirms rather than surprises.
- **Intent-first.** Substance changes go into the intent and
  propagate from there; only wording is fixed downstream directly.
- **Recommend, do not push.** Every option comes with a
  recommendation and its reason, stated once; a declined
  recommendation is not re-argued without new facts.

None of these is a command: a method applies whenever its situation
arises, and you invoke any of them in a word.

## 6. Roles

| Role | What they own |
|---|---|
| **Principal** | Whoever's thinking is being forged: supplies ideas, answers and decisions, and is the final authority on all content. |
| **Claude** | Structure, order, process discipline and document hygiene; it criticises, challenges, inspires and lays out options — the principal composes. |
| **Recipients** | Whoever receives the assignment — a team, a colleague, the principal's future self; they get one self-contained document and nothing else. |

Standing rules: when unsure, Claude asks rather than assumes; it never
introduces a new convention, prefix or section on its own; many
iterations are the normal mode; it researches before inventing;
everything it produces is advisory — only the principal publishes,
and a missing section may be a deliberate delegation, not a defect;
structure with stable IDs beats prose; and one mechanism lives in one
place — whatever the forge has a procedure for is used through its
own definition, never re-described. One instance serves one principal
and recipients collaborate through the artefacts; more principals
means more instances (see Planned extensions).

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
numbered in tens. The boundary between chain and render is
authorship: a chain artefact is composed by the principal, a render
is generated from artefacts — the article and its translation in the
diagram illustrate it.

| File | What it is |
|---|---|
| `00-brief.md` | The idea as the principal wrote it — draft until locked, then verbatim; later wholes as `00-brief-<name>.md`. |
| `10-intent.md` | The working understanding — rewritten freely, versioned. |
| `20-assignment.md` | The direction handed to the recipients — versioned. |
| `<file>.history.md` | The Version History of each versioned document — an append-only companion beside it. |
| `decisions.md` | Append-only DEC records. |
| `ledger.md` | The single source of truth for state. |

> A locked brief is immutable — composed, then locked, never touched
> again.

A brief is an intent that is composed and then locked. It is
free-form: any structure you find useful — prose, headings, tables,
use cases — with no required content and no IDs, only a minimal YAML
header; it holds thoughts to be processed, not decisions, so they may
be changed, reworked or dropped when mined. It is `draft` while being
composed and `approved` (1.0) once you lock it. Three origins are
equally legitimate and indistinguishable to the forge: it arrives
finished and is locked on arrival; it is begun outside and finished
with Claude; it is born in the forge — `/forge brief [name]` is the
door for the latter two. A project may have more than one: every
later whole of thinking that would otherwise land in the intent as a
batch of unproven positions is born as `00-brief-<name>.md` under the
same rules. A locked brief is mined into the single intent — positions
cite it as provenance, and a whole that dies on the way leaves one
rejected direction with the reason — while the **ledger**, the file
that holds all state, tracks how far each brief is mined (`pending |
partial | mined | dropped`).

The intent is the consolidated *current* state of what the principal
wants: positions held (POS), open threads (THR) and rejected
directions with their reason (REJ), each with a stable ID. It is
rewritten for coherence every round rather than appended, with the
changes recorded in its history; its audience is the principal and
Claude only. It exists because chat context dies and anything of
value must live in a file: it is the document to read when returning
to a project after weeks, instead of excavating old conversations.

The assignment is distilled from the intent for the recipients and is
the one document they receive: requirements, out-of-scope items,
constraints, assumptions, deliverables, open questions with an owner
and optional success criteria (REQ, OOS, CON, ASM, DEL, TBC, SCR). It
is complete and precise — it carries the full in-scope substance of
the intent, assigning rather than solving — and self-contained, so it
can be forwarded without oral tradition.

Substance changes go intent-first and propagate to the assignment;
only wording is fixed downstream directly. Claude writes once per
iteration round, on the principal's confirmation — one version bump
and one history row for the whole round, however many answers it
held. Feedback from recipients has no channel of its own: the
principal processes it and feeds the conclusions back through
`/forge intent`.

> A render is never edited by hand — what is iterated is its recipe.

**Renders and recipes.** A **recipe** (`recipes/<recipe>.md`) carries
inputs, audience, instructions and the output template in one
versioned file; `/render <recipe>` regenerates the output into
`renders/<recipe>.md` — or the recipe's own `output:` path —
overwriting freely, with history in git, in an isolated subagent that
sees only the recipe and its inputs. Every render opens with YAML
front-matter provenance citing the recipe and each input with their
versions, and a render may serve as an input of another render — a
deck citing an architecture picture — when the recipe declares it
among its inputs. Every project has a README rendered from its own
`recipes/readme.md` and, if it is a thought project, release notes
from `recipes/release-notes.md`, both regenerated by every `/save`
that touches the project.

**From Markdown to slides.** Everything the forge produces is Markdown,
renders included: a presentation is a `.md` saying what is on each
slide. Composing a recipe may be guided by genre — `/recipe
presentation` interviews you slide by slide — and
`scripts/md2pptx.ps1` turns the deck render into an actual PowerPoint
file, applying a `.potx` template named by path (typically a document
of a library project) or designing the visuals itself; the `.pptx`
lands beside its source render and the Markdown stays the source of
truth. All other format conversion happens outside the forge.

## 8. Two isolated reviewers

Both reviewers run as isolated agents that see the artefacts only,
never the working conversation, on the same model as everything else:
they cannot be told what we really meant, and that blindness is the
source of their value.

The **challengers** are a growing roster of persona lenses attacking
the substance of the thinking — unstated assumptions, whether the
objective is the real problem, second-order effects, organisational
reality, failure modes, the counter-case.

The **critic** is a roster of lenses on the documents: `clarity` reads
each artefact on its own, `essence` reads the chain for drift by
distilling each layer's essence blind and comparing it with the layer
above. The two are one shape — personas and lenses, one agent file
each built from a shared skeleton — with two outputs, CHL and FND,
both invoked by hand, both immutable and dated, both settled by
walkthrough.

Isolation is not independence. The author, the critic and the
challengers share one model family; what that family systematically
cannot see, none of them will find, and agreement between the
reviewers is never treated as validation — it only means the artefact
is consistent under one set of priors. The calibration point lies
outside the forge: review by humans or by a different model family,
invited at the principal's discretion.

Both take an optional target, an artefact named as `/forge` names it
(`brief`, `brief-<name>`, `intent`, `assignment`, later layers);
without one, the whole chain. Bare `/challenge` and bare `/critique`
list the roster and recommend a fit; new personas and lenses come only
by the principal's decision, and only where their blind spots
genuinely differ.

### `/challenge <persona> [artefact]`

The first persona is `cto`: peer-CTO register — direct, few and sharp,
no flattery. A target narrows the challenge to that artefact, else the
whole chain, each challenge naming the artefact it concerns; a layer
is best challenged before the next one is first derived from it. Each
challenge carries a severity (dealbreaker, major, minor) and an
epistemic status; fabrication is banned — uncertainty is stated, not
papered over. The report lands in
`challenges/YYYY-MM-DD-challenge-<persona>.md`. A challenge is open,
accepted, rejected (a DEC with its reason), parked or obsolete; an
accepted challenge must change the intent.

### `/critique <lens> [artefact]`

`clarity` reads one artefact — or each on its own — for ambiguity,
internal contradiction, duplication, scope hygiene, requirement style
and an advisory checklist. `essence` reads one artefact against its
parent — or every adjacent pair of the chain — distilling the
downstream essence blind, then the upstream, and comparing: substance
lost without a trace, added without provenance, or shifted in meaning;
a finding is a difference of essences, not of texts, and the report
carries both distillations. Regression against resolved findings is
every lens's first step. The report lands in
`reviews/YYYY-MM-DD-critique-<lens>.md`. A finding has one of four
states:

- open
- resolved — an iteration of the artefact concerned
- overruled — a DEC with its reason
- obsolete — the passage no longer exists

## 9. Commands

Commands are entry points into phases, not the only door: the same
rules apply in plain conversation, and `/forge <state>` is simply the
name of the artefact you want to work on.

| Command | Purpose |
|---|---|
| `/setup` | First run after cloning: creates and fills `CLAUDE.local.md` by interview, creates `.claude/settings.local.json` with the model set to Fable, and offers the global git identity guard. Never overwrites, runs no git operation. |
| `/new-project <slug>` | Scaffolds a project by kind — files only, never git: a thought project with its brief captured verbatim (locked if finished, draft otherwise), or a library (`lib-`) of shared material. |
| `/import-project <git-url>` | Brings an existing project into `projects/` through `scripts/forge-clone.ps1`; the directory is the repository's name and the commit identity is proposed from `CLAUDE.local.md` by the URL's host. |
| `/forge [slug]` | The chain map: artefacts and versions, possible next steps, stale renders, and a recommended next step. |
| `/forge <state> [slug]` | Iterates the target artefact (`brief [name]`, `intent`, `assignment`, …); one definition file per state, each declaring its inputs. |
| `/ingest [file] [slug]` | Stores and registers external input in `sources/` and indexes it; bare, it sweeps `sources/` for unregistered files. |
| `/render <recipe> [slug]` | Regenerates a render from its recipe in `recipes/`. |
| `/recipe [genre] [slug]` | Bare: the genre roster. With a genre (`presentation`, `readme`, `release-notes`): guided composition or iteration of a recipe from the genre's checklist and skeleton. |
| `/critique [lens] [artefact] [slug]` | Bare: the critic lens roster. With a lens (`clarity`, `essence`): runs that critic on one artefact, or one against its parent, when named, else all — review plus ledger. |
| `/challenge [persona] [artefact] [slug]` | Bare: the challenger persona roster. With a persona (e.g. `cto`): runs it against the substance of the named artefact, else the whole chain. |
| `/research <topic> [slug]` | Best-practices research into `research/`, indexed. |
| `/ledger [slug]` | The quick state readout from the ledger. |
| `/check [slug]` | Conformance of a project against the current conventions; bare, every project except forge. |
| `/check-forge` | Consistency check of the core and `projects/forge`. |
| `/save [slug] [-m "message"]` | Pre-save check, findings settled with the principal, then commit and push. |
| `/spinoff <project> <group> <slug>` | Splits a requirement group into its own project — only by the principal's explicit decision. |

`/ingest` stores, registers and catalogues — nothing more. A source
keeps one form: at ingest every binary file gets one question, convert
to Markdown? — yes makes the extract `sources/<slug>.md` the source,
produced by `scripts/doc2md.ps1`, and the original is not kept in git;
no keeps the binary itself as the source, a template or a graphic,
with no extract. A set of related files lives as `sources/<slug>/`
and counts as one source, catalogued by its own `00-INDEX.md`. What a
source is for is noted as free text in the directory's index, and the
principal alone directs how and when it is used: registration is not
intake, and nothing said in a meeting is silently promoted to the
principal's own position. `/save` is the recommended way to save:
when the save touches the core or `projects/forge/` it first
re-renders `README.md` and the Unreleased head of `RELEASE-NOTES.md`,
reporting what materially changed; it then runs the conformance check
that fits the scope, settles the findings with the principal, proposes
a commit message and only then runs the save script. `/check` and
`/check-forge` run in an isolated subagent that sees only the files
and return their report for the walkthrough.

### A typical journey

- You write down what is in your head, however rough, and lock it as
  the brief of your project (`/new-project`, `/forge brief`).
- Over several sessions you answer questions one at a time and watch
  your intent take shape as positions, threads and rejected
  directions (`/forge intent`), each round written once, on your
  word.
- A standard you downloaded and a meeting transcript are registered
  as they arrive, and you decide when each is brought to bear
  (`/ingest`); a topic you are unsure of gets researched
  (`/research`).
- You send in a peer to attack the thinking and a critic to attack
  the documents, then walk through their findings one by one —
  fixing, overruling with a reason, or leaving open (`/challenge cto`,
  `/critique clarity`, `/critique essence`).
- You compose a presentation recipe through its interview and render
  the deck — including the actual PowerPoint through your own
  template (`/recipe presentation`, `/render`,
  `scripts/md2pptx.ps1`).
- You distil the assignment your recipients receive, complete and
  self-contained, and approve it as 1.0 (`/forge assignment`).
- All along you save as you go, and the project's README and release
  notes regenerate with every save (`/save`).

## 10. Conventions

**IDs.** Every item carries an ID of the form `PREFIX.NNNN`, all
prefixes three letters. IDs are global and stable — never renumbered;
items may move between groups without changing their ID. Items are
numbered in tens (`REQ.0010, REQ.0020`), each new group starting at
the next hundred (`REQ.0100, REQ.0110`); overflow takes the next free
number anywhere. Groups are plain headings — no IDs, no metadata, no
lifecycle — at most two levels deep.

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
prefixes and the domain terms it actually uses; defined terms are
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
concretisation through a DEL item is a legitimate outcome, and the
critic reports untestable wording as a recommendation, never as a
blocking defect. An illustrative item:

> REQ.0010 The Platform shall record every request and every response
> passing through the Gateway, with the identity of the requesting
> User and the time.

**Completeness over brevity.** An assignment carries the full in-scope
substance of the intent, written as well and as precisely as
possible; nothing is omitted for brevity's sake, and length is
whatever fidelity requires — leaving a matter out is legitimate only
as an explicit delegation (a DEL or TBC item). An assignment assigns,
it does not solve: the machinery of executing delivery belongs to the
recipients, but any apparatus may appear where the principal judges it
part of setting direction.

**Versioning.** Integers denote signed-off versions: `0.1, 0.2, …` are
drafts before first approval, `1.0` is approved, `1.1, 1.2, …` are
changes made after approval and not yet approved themselves, `2.0` is
the next approved version incorporating all changes since 1.0.
Front-matter carries `version`, `date`, `status` (`draft | in_review |
approved | superseded`) and `last_change`, and status must agree with
the number: an integer version is `approved`, anything else is not.

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

Every versioned kind keeps its Version History (Version |
Modification | Author | Date — what changed and why) in an append-only
companion `<file>.history.md` beside it, never in its body, and the
document's `last_change` line in the front-matter summarises the
newest row. An integer version is approved, and a recipe never is: it
stays 0.x for life and carries no status.

**Project kinds.** A project is of kind `thought` — the chain — or
`library`: a collection of material shared across projects, prefix
`lib-`, with no chain — only a ledger, sources and research with their
indexes, and a README that catalogues what it holds. A project's kind
is declared in the header of its ledger. Project slugs are lowercase
and hyphenated on disk — `forge` is the system's own project, and
`lib-<name>` a library — while display names may differ.

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
                           # / forge-clone (git), doc2md (document →
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
                                      # regenerated by every /save
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
- PowerShell 7 (`pwsh`) — the scripts are PowerShell, needed on macOS
  and Linux too
- Python 3 — for markitdown
- a paid Claude subscription

### Getting the forge and Claude Code

Clone this repository: it is the engine. Then install Claude Code:

- Windows: `irm https://claude.ai/install.ps1 | iex`
- macOS/Linux: `curl -fsSL https://claude.ai/install.sh | bash`
- or `npm install -g @anthropic-ai/claude-code`

Sign in on first run — usage draws from the same pool as Claude chat.
Always start `claude` from the engine root, so that `CLAUDE.md` and
`CLAUDE.local.md` load.

Then run `/setup` once. It creates `CLAUDE.local.md` from its template
and fills it with you in a short interview — who the principal is, the
conversation language, your git identities per host — a file that is
gitignored and never committed. It creates `.claude/settings.local.json`
with the session model set to Fable, the strongest available model,
which the whole forge including the blind reviewers runs on; it tells
you so in one sentence, and `/model` or editing that file changes it
at any time (permissions come from the shared `.claude/settings.json`).
It closes by offering one global git guard — `user.useConfigOnly =
true` appended to `~/.gitconfig` — so that a repository without a
local identity fails aloud instead of committing with a default;
declined, it prints the line for you to apply by hand. The identities
themselves are set per repository, proposed from your roster at every
project creation or import. `/setup` never overwrites existing files.

Upgrading the engine is `scripts/forge-pull.ps1` — a fast-forward of
`main`; your projects are untouched by it.

### Your projects

Each project is a directory under `projects/` and a git repository of
its own. `/new-project` creates the files; `git init` in that
directory, and a remote if you want one, are a one-off act of yours.
The commit identity belongs to the project: it is set locally in the
repository, proposed from the identity roster in `CLAUDE.local.md` by
the origin's host and confirmed by you. An existing project is brought
in with `/import-project <git-url>`, which clones it into
`projects/<repository name>` through `scripts/forge-clone.ps1`, sets
the identity you confirm and reports the identity the clone ended up
with. The engine ignores `projects/*` (except its own `projects/forge`)
and the scripts find your project through its `.git`. A project
without a repository is reported as "not under git" — a fact, not an
error.

### Script prerequisites

- `doc2md.ps1` needs markitdown:
  `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.
- `md2pptx.ps1` needs the `document-skills` plugin, installed once
  from an interactive Claude Code session
  (`/plugin marketplace add anthropics/skills`, then
  `/plugin install document-skills@anthropic-agent-skills`). A deck
  template is named by path (`-Template <file.potx>`) — typically a
  document of a library project — or omitted, in which case Claude
  designs the visuals.
- The git scripts need nothing beyond git.

### Saving and syncing

`/save` is the recommended door. Before committing it re-renders the
README and the Unreleased head of the release notes when the save
touches the core, runs the conformance check routed by scope, and
settles the findings with the principal; then it runs the script. The
scripts in `scripts/` are the underlying mechanism and the only
intended door to git — reading state included — each serving the
engine and every project repository: a bare save commits each
repository with changes on its own and pushes where it has a remote;
pull fast-forwards and never touches unsaved work; status reports
without changing anything. History is linear on `main`, one remote
per repository, and no URL is stored anywhere in the forge — git
carries that itself.

## 13. Scripts

| Script | Purpose | When it is run | Install note |
|---|---|---|---|
| `forge-save.ps1` | Commits and pushes: bare, every repository with changes, each its own commit; with a slug, that one (`forge` meaning the engine); reconciles remote changes by rebase; without an origin the commit is kept and reported. | At every save — by `/save` as its last step, or directly from the shell. | git only |
| `forge-pull.ps1` | Fast-forwards from the remotes and never touches a repository with unsaved changes. | To upgrade the engine, or to pick up a project's remote changes. | git only |
| `forge-status.ps1` | Reports unsaved changes, the last commit and the origin of each repository, changing nothing. | Whenever you want to know where things stand. | git only |
| `forge-clone.ps1` | Clones an existing repository into `projects/<repository name>`, never overwriting, and sets its local commit identity only when given `-Name` and `-Email`. | Through `/import-project`. | git only |
| `doc2md.ps1` | Converts a binary document to a Markdown extract with markitdown. | By `/ingest`, for every binary you choose to convert. | markitdown — see Setup |
| `md2pptx.ps1` | Turns a Markdown deck render into a `.pptx` through headless Claude Code with the official pptx skill, with an optional `.potx` template named by path. | After a presentation recipe is rendered, on request. | `document-skills` plugin — see Setup |

## 14. Planned extensions

The chain is designed to grow downward toward realisation: a BRD layer
is certain to come, solution architecture and integration are
intended, a strategy layer is possible if it proves to make sense.
Which layers are added, and in what order, is open, and nothing is
approved for construction — the mechanics of a layer are designed when
that layer is actually taken up, not in advance.

More principals means more instances: a second principal receives the
forge via git and runs an instance of their own; genuine multi-user
operation is a question for later, deliberately not worked on now.

The system runs through its own process: `projects/forge/` holds the
forge's brief, intent, decisions and ledger, and the engine receives a
git tag at every approved major of that intent.

## 15. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) — petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit
the author and link to this repository.

## 16. About this README

This file is a render of the `projects/forge` project: it is never
edited by hand and is regenerated by `/render readme` whenever the
process changes — and by every `/save` that touches the core. Fixes
go into the recipe (`projects/forge/recipes/readme.md`) or its inputs;
the YAML front-matter at the top is the render's provenance and is
kept by design. Changes to the system are recorded in
`projects/forge/`.

_Last updated: 2026-09-04_
