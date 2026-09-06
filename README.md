---
project: forge
render: readme
generated: 2026-09-06
recipe: recipes/readme.md v0.41
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v4.0
---

# Forge of Thought 4.0

*A workshop where thought is tempered and shaped.* · [Release notes](RELEASE-NOTES.md)

Forge of Thought is an **AI cognitive extension** of a thinking human,
the **principal** — the person whose thinking is being forged. It takes
a raw, half-formed idea — a process redesign, a platform initiative, an
organisational change, a D&D campaign — and tempers it into a precise,
self-contained handover for whoever delivers it: a team, a colleague,
your future self. It rests on one principle — **the machine carries
every part of the work that is not deciding** — in three forms.

- **It thinks with you.** It interviews and probes, criticises,
  challenges and inspires; it extracts what you have not yet
  articulated and lays out options with their trade-offs. It proposes
  — you decide.
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
Code, templates, and the conventions binding them. Today the chain
runs from the brief through the intent to the assignment; nothing is
implemented here — the engine specifies.

## 1. Better with AI, or replaced by it?

Forge of Thought is for those who chose to be better. The failure
modes it exists to remove:

- thinking scattered across chat sessions that die, taking their
  context with them;
- handovers whose completeness depends on the mood of the day they
  were written;
- the same thinking retold to every audience — a pitch, a deck, a
  mail — each version rewritten by hand and drifting from the others;
- feedback and decisions with no place to land, so the same ground is
  fought over twice;
- assumptions nobody attacked before reality did.

## 2. What you get

- A versioned document chain growing from a brief — your own text,
  locked verbatim once it is done — to a self-contained assignment.
- An elicitation interview that forges the intent.
- Blind adversarial reviewers, every verdict recorded.
- Audience-specific renders generated from recipes, including an
  actual PowerPoint file through your own template.
- External sources registered immutably and used only as the
  principal directs.
- Everything in files and git — nothing depends on a chat's memory.

## 3. Quickstart

**First, once per machine**

```
git clone <this repository>   # you are looking at it
# install Claude Code — see Setup below
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
/import-project <project url>   # clones into projects/ — the commit identity is proposed
                                # from your identities.local.md roster and confirmed by you
/forge <project-slug>           # the slug is the repository's name; select the project
                                # before any work — the forge cannot guess it
```

Each project lives inside `projects/<slug>/` as a git repository of
its own, which the engine does not track — that is why you name it
first.

## 4. How it is used

### The flow

A thought arrives — a platform initiative that will not leave you
alone, a reorganisation you keep sketching on napkins, a campaign
taking shape for your D&D table. You dump it verbatim as a brief:
alone, in one sitting, or in conversation with the forge
(`/forge brief`). When it says what you meant, you lock it, and from
then on it stays as it was — the record of where the thinking started.

Then the forge interviews you. Over days and sessions
(`/forge intent`), one question at a time, it draws out what you
want, why, what is open and what you have already rejected, and writes
it into the intent — positions, threads, rejections, each with an ID
you can point at. Everything lives in files; a session that ends loses
nothing.

Material arrives along the way. A security standard you downloaded is
registered with `/ingest` and sits in `sources/` untouched until you
say what it is for — later the intent is verified against it. Where a
key topic needs grounding, `/research` looks up current practice and
files a note you can cite.

When the intent feels settled you ask for pressure. `/challenge cto`
sends a peer reviewer at the thinking; `/critique clarity` sends a
critic at the documents. Neither has seen your conversation; both
return numbered findings you go through one at a time — accept,
overrule, park — and every verdict lands where it can be found again.
Nothing blocks you: you publish when you decide to.

Then you distil the assignment (`/forge assignment`): the one document
the recipients receive, complete and self-contained. And the group
needs a pitch — so you compose a recipe (`/recipe presentation` guides
you through it with a genre interview), `/render pitch` generates the
slides, and `scripts/md2pptx.ps1` turns them into an actual PowerPoint
on your template. When the intent moves next month, you regenerate;
you never rewrite the pitch by hand. This README is such a render too.

`/save` commits and pushes as you go; `/release` marks a version you
stand behind and regenerates the README and release notes with it.

### What it looks like in practice

A worked example from a real project will appear here once one is
published.

## 5. How the work feels

The forge is as much a way of working as a set of files, and these
are the named methods of that work — the vocabulary you and Claude
share.

- **Walkthrough.** Any list needing your decision — findings,
  challenges, differences between two requirement sets, open threads
  — is worked one item per message, in order of weight: Claude's
  recommendation with a one-sentence reason first, your verdict in a
  word or a counter-proposal; "leave it open" is legitimate. Never a
  table asking for every verdict at once, and never a questionnaire
  of several questions — the verdicts are carried in the conversation
  and written once, at the round's end.
- **Propose, never decide.** Claude criticises, challenges, inspires
  and lays out options; you compose.
- **Step by step.** Anything needing your consent — a write, a
  commit, a push, a rename, anything hard to reverse — arrives as one
  step with the exact operation, its target and the reason, and runs
  on your word; a plan you have seen is not consent for its steps.
- **Elicitation interview.** Questions draw out what you have not yet
  articulated; a gap is never filled by assumption.
- **Draft early.** An early draft is an elicitation tool, not an
  output: concrete text sharpens your reaction.
- **Reflect back.** Before writing, Claude restates what it
  understood, so that the write confirms rather than surprises.
- **Intent-first.** Substance changes go into the intent and
  propagate from there; only wording is fixed downstream directly.
- **Recommend, do not push.** Every option comes with a recommendation
  and its reason, stated once; a declined recommendation is not
  re-argued without new facts.

None is a command: each applies whenever its situation arises,
whatever produced it, and you invoke any of them in a word.

## 6. Roles

| Role | What they own |
|---|---|
| **Principal** | Whoever's thinking is being forged: supplies ideas, answers and decisions, and is the final authority on all content. |
| **Claude** | Cognitive extension of the principal: structure, order, process discipline and document hygiene; criticises, challenges, inspires and lays out options — proposes, never decides. |

Some rules stand in every session. When unsure, Claude asks and never
fills a gap by assumption. No new convention, prefix or section
appears unilaterally: it is proposed, decided, then written down. Many
iterations are the normal mode, and intent and assignments may grow
and change substantially between versions. Key topics are researched
before anything is invented. Everything a reviewer or checklist says
is advisory: only the principal publishes, and a missing section may
be a deliberate delegation to the recipients, not a defect. Structure
beats prose — items with stable IDs, narrative only where purpose,
context and objective are explained. Every mechanism of the forge
lives in one place and is used through its own definition, never
re-described or improvised.

One instance serves one principal; the recipients of an assignment
collaborate through the artefacts, not through the instance — more
principals means more instances (see Planned extensions).

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
from artefacts — an article the principal writes is a layer of the
chain, its translation is a render, as the diagram shows.

| File | What it is |
|---|---|
| `00-brief.md` | The idea as the principal wrote it — draft until locked, then verbatim; later wholes as `00-brief-<name>.md`. |
| `10-intent.md` | The working understanding of principal and Claude — rewritten freely, versioned. |
| `20-assignment.md` | The direction handed to the recipients — versioned, self-contained. |
| `<file>.history.md` | The Version History of each versioned document — an append-only companion beside it. |
| `decisions.md` | Append-only DEC records: the principal's decisions with their reasons. |
| `ledger.md` | The **ledger** — the single source of truth for state, kept current after every operation. |
| `sources/`, `research/` | External inputs and research notes, immutable, each directory catalogued by its `00-INDEX.md`. |
| `recipes/`, `renders/` | Render recipes and the outputs generated from them. |
| `reviews/`, `challenges/` | Dated, immutable reviewer runs. |

> A locked brief is immutable — composed, then locked, never touched
> again.

The **brief** is an intent that is composed and then locked.
Free-form: any structure the principal finds useful — prose,
headings, tables, use cases — with no required content and no IDs; it
holds thoughts to be processed, not decisions, so they may be
changed, reworked or dropped when mined. It is `draft` while being
composed and `approved` (1.0) once the principal locks it. Three
origins are equally legitimate and indistinguishable to the forge: it
arrives finished and is locked on arrival; it is begun outside and
finished with Claude; it is born in the forge — `/forge brief [name]`
is the door for the latter two. A project may have more than one:
every later whole of thinking that would otherwise land in the intent
as a batch of unproven positions is born as `00-brief-<name>.md`
under the same rules. A locked brief is mined into the single intent
— positions cite it as provenance; a whole that dies on the way
leaves the brief locked and one REJ with the reason. The ledger
tracks each brief's mining state (`pending | partial | mined |
dropped`), and each locked brief is the provenance anchor and drift
measure of its whole.

The **intent** is the consolidated *current* state of what the
principal wants and why: the positions he holds (POS), the open
threads to elicit next (THR) and the directions he rejected, with the
reason each was dropped (REJ), every item with a stable ID. Its
audience is the principal and Claude only. It exists because thinking
grows and changes substantially between versions, and a record that
only appends buries the current state under its own history: the
intent is rewritten for coherence every round, and what changed and
why is recorded in its history companion.

The **assignment** is distilled from the intent for the recipients —
teams, colleagues, or the principal's future self — and is the one
document they receive, so it is self-contained. It holds
requirements, out-of-scope items, constraints, assumptions,
deliverables, open questions with an owner and optional success
criteria (REQ, OOS, CON, ASM, DEL, TBC, SCR). It is complete and
precise: it carries the full in-scope substance of the intent at
whatever length fidelity requires, and it assigns rather than solves.

Substance changes go intent-first and propagate to the assignment;
wording-only fixes may edit the assignment directly. A working round
is written once, on the principal's confirmation — one version bump,
one history row for the whole round. Feedback from recipients has no
channel of its own: the principal processes it and feeds the
conclusions back into the intent (`/forge intent`).

> A render is never edited by hand — what is iterated is its recipe.

**Renders and recipes.** A **recipe** (`recipes/<recipe>.md`) holds
inputs, audience, instructions and the output template in one
versioned file; more than one input is legitimate, and a render may
itself be declared an input of another render — as a picture source,
for instance. `/render <recipe>` regenerates the output into
`renders/<recipe>.md` — or the recipe's optional `output:` path —
overwriting freely, history in git; generation runs in an isolated
subagent that sees only the recipe and its inputs, never the working
conversation. Every render opens with YAML front-matter provenance
citing the recipe and each input with their versions, mirrored in the
ledger's Renders table. A recipe carries a version and an updated
date and no status, since it is never approved. A render assigns
nothing and is not part of the chain: the artefacts stay the source
of truth. Every project has a README as a render of its own
`recipes/readme.md`, and a thought project release notes from
`recipes/release-notes.md`; every `/release` regenerates them.

**From Markdown to slides.** Everything is Markdown, content only.
Composing a recipe may be guided by a genre interview —
`/recipe presentation` for a deck, `readme` and `release-notes` being
the other genres. The one in-house conversion is
`scripts/md2pptx.ps1`: it turns a Markdown deck render into an actual
PowerPoint file through headless Claude Code — an LLM conversion by
design, because deck definitions are free-form and may carry
instructions for the model — with a `.potx` template named by path,
typically a document of a library project. The generated `.pptx` is
tracked in git like any render output; the Markdown render stays the
source of truth. All other format conversion happens outside the
forge.

## 8. Isolated reviewers

Reviewers run as isolated subagents that see the project's documents
only, never the working conversation: they cannot be told what we
really meant, so they read what is actually written. Every kind of
reviewer is of one shape — one agent file per lens, persona or check,
the behaviour shared by its kind preloaded from one contract — and
all run on the session model: the whole forge runs on one model, and
speed is bought with context, never with a weaker reviewer. Each is
invoked by hand and settled by walkthrough; no reviewer runs on
Claude's own judgement. New personas, lenses and checks come only by
the principal's decision, and only where what they find genuinely
differs.

Isolation is not independence. The author, the critic and the
challengers share one model family; what that family systematically
cannot see, none of them will find, and agreement between the
reviewers is therefore never treated as validation — it only means
the artefact is consistent under one set of priors. The calibration
point lies outside the forge: review by humans or by a different
model family, invited at the principal's discretion.

### Critic (`/critique`)

The **critic** judges document quality, never substance.
`/critique <lens> [artefact]` runs one lens on the named artefact
(`brief`, `brief-<name>`, `intent`, `assignment`, later layers) or,
without one, on the whole chain; bare `/critique` lists the roster.

- `clarity` — reads each artefact on its own for ambiguity,
  contradiction, duplication, scope hygiene and Requirement style.
- `essence` — reads the chain for drift: distils each layer's essence
  blind and compares it with the layer above.

Output: `FND` findings in a dated, immutable review,
`reviews/YYYY-MM-DD-critique-<lens>.md`, tracked in the ledger.
Finding states:

- open
- resolved
- overruled (→ DEC)
- obsolete

### Challenger (`/challenge`)

The **challenger** judges the substance of the thinking, never
document quality. `/challenge <persona> [artefact]` runs one persona
against the named artefact or, without one, the whole chain; bare
`/challenge` lists the roster.

- `cto` — a CTO-level peer reviewer: challenges the substance of the
  principal's thinking — assumptions, blind spots, second-order
  effects, organisational reality; not a document auditor.

Output: `CHL` challenges in a dated, immutable report,
`challenges/YYYY-MM-DD-challenge-<persona>.md`, tracked in the
ledger; an accepted challenge must change the intent. Challenge
states:

- open
- accepted
- rejected (→ DEC)
- parked
- obsolete

### Checks (`/check`)

A check judges mechanical conformance with the conventions, never
substance or quality; each owns one concern and none another's.
`/check <check> [slug]` runs one check on the named project or on the
engine; bare `/check` lists the roster.

- `light` — verifies a project's bookkeeping: front-matter against
  the history companion, ledger tables against the files,
  dependencies and resource indexes against the directories; fit for
  a save.
- `project` — verifies a project's structure, IDs, assignment style,
  language, immutables, recipes and renders against the conventions.
- `engine` — verifies the core (CLAUDE.md, templates, skills, agents,
  scripts) against itself and against the forge intent: every
  position honoured, nothing withdrawn still advertised, every
  decision reflected.
- `single-source-of-truth` — verifies that every rule, procedure and
  file shape is written in one place and cited everywhere else: no
  restatement across CLAUDE.md, skills, agents, templates and
  scripts, no direct operation where a mechanism exists; the honest
  sweep, expensive by design.

Output: nothing filed — the report returns to the session and each
finding is settled there:

- fix
- defer
- accept

Composition is the caller's (`/save`, `/release`); checks never call
each other.

## 9. Commands

Every command is a slash command in a Claude Code session started
from the engine root.

| Command | Purpose |
|---|---|
| `/setup` | First run after cloning the engine: creates and fills `CLAUDE.local.md` and `identities.local.md` by interview, creates `.claude/settings.local.json` with the model set to Fable, and offers the global git identity guard. Never overwrites, runs no git operation. |
| `/new-project <slug>` | Scaffolds a project by kind — files only, never git: a thought project with its brief captured verbatim (locked if finished, draft otherwise), or a library (`lib-`) of shared material. |
| `/import-project <git-url>` | Brings an existing project into `projects/` through `scripts/forge-clone.ps1`; the directory is the repository's name, the commit identity is proposed from `identities.local.md` by the URL's host. |
| `/forge [slug]` | The chain map: artefacts, versions, stale renders, and a recommended next step. |
| `/forge <state> [slug]` | Iterates the named artefact — the command is simply the name of the artefact you want to work on (`brief [name]`, `intent`, `assignment`, …). |
| `/ingest [file] [slug]` | Stores and registers an external input in `sources/` and indexes it; bare, it sweeps `sources/` for unregistered files. |
| `/render <recipe> [slug]` | Regenerates a render from its recipe in `recipes/`. |
| `/recipe [genre] [slug]` | Bare, the genre roster; with a genre (`presentation`, `readme`, `release-notes`), guided composition or iteration of a render recipe from the genre's checklist and skeleton. |
| `/critique [lens] [artefact] [slug]` | Bare, the critic lens roster; with a lens (`clarity`, `essence`), runs that critic on the quality of the documents — one artefact, or one against its parent, when named, else all → review + ledger. |
| `/challenge [persona] [artefact] [slug]` | Bare, the challenger persona roster; with a persona (e.g. `cto`), runs that challenger against the substance of the named artefact, else the whole chain. |
| `/research <topic> [slug]` | Best-practices research, stored in `research/` and indexed. |
| `/ledger [slug]` | The quick state readout from the ledger. |
| `/check [check] [slug]` | Bare, the check roster; with a check (`light`, `project`, `engine`, `single-source-of-truth`), runs it on the named project or on the engine — report to the session, nothing filed. |
| `/save [slug] [-m "message"] [-Tag name]` | Saves one repository, or every one with changes: the `light` check, then commit and push on the current branch, no render; a tag on request. |
| `/release [slug] [-m "message"] [-Tag name]` | Releases one repository from `main`: its checks, the README and release notes re-rendered, then a save with the release message and the tag `v<major>` at an approved major. |
| `/spinoff <project> <group> <slug>` | Splits a requirement group into its own project — only by your explicit decision, never automatically. |

`/ingest` stores, registers and catalogues — nothing more. A source
has one form, text or a functional binary; a binary is converted to a
Markdown extract by `scripts/doc2md.ps1` only on your explicit word,
and the extract then is the source. A set of related files lives as a
subdirectory `sources/<slug>/`, counts as one source and carries its
own `00-INDEX.md`. Registration does not imply intake: what a source
is for is noted as its Role in the resource index, and you alone
direct how and when it is used — what someone said in a meeting is
never silently promoted to your own position. `/save` and `/release`
are the two doors to git — the `light` check, then commit and push on
the current branch, for the one; the release checks, the README and
release notes and the major's tag, from `main`, for the other — and
their mechanics are in Saving and syncing below. Plain conversation
works too: the commands are doors, and a working method applies
whenever its situation arises, whatever produced it.

### A typical journey

- You write down the idea as it is in your head and lock it as the
  brief of your project (`/new-project`, `/forge brief`).
- Over several sessions you answer questions, one at a time, and
  watch the intent take shape and change — positions, open threads,
  what you rejected and why (`/forge intent`).
- You register the documents you were sent and the standard you
  found, and say what each is for (`/ingest`).
- You ask for pressure: a peer reviewer attacks the thinking, a
  critic the documents; you give your verdict on each finding and
  every verdict is recorded (`/challenge cto`, `/critique clarity`).
- You compose a presentation recipe through a short interview and get
  the pitch rendered — as Markdown and as an actual PowerPoint on
  your template (`/recipe presentation`, `/render`,
  `scripts/md2pptx.ps1`).
- You distil the assignment your recipients will receive — complete,
  precise, self-contained — and hand it over (`/forge assignment`).
- You save as you go, and release when you stand behind a version
  (`/save`, `/release`).

## 10. Conventions

**IDs and numbering.** Every item carries a stable ID of the form
`PREFIX.NNNN`, all prefixes three letters. IDs are global and never
renumbered; an item may move between groups without changing its ID.
Numbering runs in tens (`REQ.0010`, `REQ.0020`), each new group
starting at the next hundred (`REQ.0100`, `REQ.0110`); overflow takes
the next free number anywhere. Groups are plain headings — no IDs, no
metadata, no lifecycle — at most two levels deep.

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

**Terms.** Defined terms are capitalised in item text to signal that
they appear in the Terms section.

**Language.** The forge dictates the output language: all documents
are written in English, translated on write. The briefs are the
exception, stored verbatim in whatever language they were written.
The conversation language is per-instance configuration — it lives in
`CLAUDE.local.md` — and never appears in outward-facing renders.

**Requirement style.** Requirements use *shall* / *shall not* — never
would, could, should, might, may or MoSCoW wording. There is no
priority column and no priority tag: everything in an assignment is
essential by default, and an exception is marked by a note reading
*optional* on that item. Each item covers one idea, is written once,
in full, correct UK English sentences, and must not depend on an
external link to be understood, agreed or later tested. Testability
is recommended, not required: assignments are deliberately
high-level, and delegating concretisation through a DEL item is a
legitimate outcome — the critic reports untestable wording as a
recommendation, never as a blocking defect. An illustrative item:

> REQ.0010 The Platform shall record every request and every response
> passing through the Gateway, with the identity of the requesting
> User and the time.

**Completeness over brevity.** An assignment carries the full
in-scope substance of the intent, written as well and as precisely as
possible; nothing is omitted for brevity's sake, and length is
whatever fidelity requires. Leaving a matter out is legitimate only
as an explicit delegation — a DEL or TBC item. The boundary is the
kind of content, never its amount: an assignment assigns, it does not
solve — the machinery of executing delivery belongs to the
recipients, while any apparatus the principal judges part of setting
direction may appear.

**Versioning.** Integers denote signed-off versions: `0.1, 0.2, …`
are drafts before first approval, `1.0` is approved, `1.1, 1.2, …`
are changes made after approval and not yet approved themselves,
`2.0` the next approved version, incorporating all changes since 1.0.
Front-matter carries `version`, `date`, `status` (`draft | in_review
| approved | superseded`) and `last_change`; status must agree with
the number — an integer version is `approved`, anything else is not,
and a recipe carries no status and stays 0.x. Immutable documents — a
locked brief, reviews, challenges, sources, research — are never
edited: a brief from its lock, a source from its registration, the
others from creation; corrections happen downstream.

**Document kinds.** "Document" is the word for every file of a
project; "artefact" is reserved for the documents of the chain — the
ones the principal composes, the reviewers read and the renders are
generated from. Every document has one kind:

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
companion `<file>.history.md` beside it, never in its body — the body
is the current state, the companion the record — and `last_change` in
the front-matter summarises the newest row, written by the same step
that appends it. An integer version is approved, and a recipe never
is.

**Project kinds and naming.** A project has a kind, recorded in its
ledger header: `thought` carries the chain; `library` (slug prefix
`lib-`) holds material shared across projects — sources and research
maintained by their owner, with a ledger and a README as its
catalogue, and no chain. A project is named by its slug, the name of
its directory under `projects/` and of its repository: the engine's
own project is `forge`, a library is `lib-<name>`.

## 11. Repository layout

```
CLAUDE.md                  # this file — universal core
CLAUDE.local.md            # instance facts (principal, conversation
                           # language) — gitignored, created by
                           # /setup from templates/CLAUDE.local.md
identities.local.md        # git identities — gitignored, loaded by
                           # nobody, read by path by /setup,
                           # /new-project and /import-project
README.md                  # for humans — a render (/render readme)
RELEASE-NOTES.md           # release notes — a render (/render
                           # release-notes): one section per
                           # release, compiled from the Notes of
                           # the intent's history rows; minors
                           # fold into a major
logo.png                   # project avatar
LICENSE                    # CC BY 4.0 — the engine is published
                           # under attribution
scripts/                   # forge-save / forge-pull / forge-status
                           # / forge-clone / forge-branch (git),
                           # doc2md (document →
                           # Markdown), md2pptx (deck render →
                           # PowerPoint)
.claude/                   # skills (the commands and the reviewers'
                           # contracts), agents, settings
                           # (settings.local.json: the session
                           # model — gitignored)
templates/                 # canonical skeletons
projects/                  # gitignored (projects/*) except
                           # projects/forge — every other project is
                           # a git repository of its own, which the
                           # engine does not know
projects/<slug>/           # kind: thought — the chain
  .git/                               # the project's own repository
  README.md  RELEASE-NOTES.md         # renders (Document chain 7)
  logo.png                            # optional project avatar
  00-brief.md  10-intent.md  20-assignment.md
  00-brief-<name>.md                  # later briefs, one per whole
  <file>.history.md                   # Version History of each
                                      # versioned document (brief,
                                      # intent, assignment, recipe):
                                      # append-only companion
  decisions.md  ledger.md             # ledger header carries kind:
  sources/00-INDEX.md                 # resource index (rewritten)
  sources/<name>.<ext>                # immutable external inputs, one
                                      # form each: <slug>.md extract of
                                      # a binary, or the binary itself
  sources/.gitignore                  # originals converted in place
  sources/<slug>/                     # bundle of related files = one
                                      # source, one ledger entry;
                                      # catalogued by its 00-INDEX.md
  research/00-INDEX.md                # resource index (rewritten)
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

Written for a reader who has never used Claude Code.

### Prerequisites

- git
- PowerShell 7 (`pwsh`) — the scripts are PowerShell and run
  unchanged on Windows, macOS and Linux, so it is needed there too
- Python 3 — for markitdown, which `doc2md.ps1` uses
- a paid Claude subscription

### Getting the forge and Claude Code

Clone this repository: it is the engine. Install Claude Code and sign
in on first run — usage draws from the same pool as Claude chat:

```
irm https://claude.ai/install.ps1 | iex                  # Windows
curl -fsSL https://claude.ai/install.sh | bash            # macOS / Linux
npm install -g @anthropic-ai/claude-code                  # or, via npm
```

Always start `claude` from the engine root, so that `CLAUDE.md` and
`CLAUDE.local.md` load.

Then run `/setup` once. In a short interview it fills
`CLAUDE.local.md` (who the principal is, the conversation language)
and `identities.local.md` (your git identities per host) from their
templates — both gitignored, never committed — and creates
`.claude/settings.local.json` with the session model set to Fable,
the strongest available model, which the whole forge including the
blind reviewers runs on; it tells you so in one sentence, and
`/model` or editing that file changes it at any time (permissions
come from the shared `.claude/settings.json`). It closes by offering
one global git guard — `user.useConfigOnly = true` appended to
`~/.gitconfig` — so that a repository without a local identity fails
aloud instead of committing with a default; declined, it prints the
line for you to apply by hand. The identities themselves are set per
repository, proposed from your roster at every project creation or
import. `/setup` never overwrites existing files.

### Your projects

Each project is a directory under `projects/` and a git repository of
its own. `/new-project` creates the files; `git init` in that
directory (`git -C projects/<slug> init -b main`) and a remote, if
wanted, are a one-off act of yours, while the commit identity belongs
to the project: it is set locally in the repository, proposed from
the identity roster in `identities.local.md` by the origin's host and
confirmed by you. An existing project is brought in with
`/import-project <git-url>`, which clones it into
`projects/<repository name>` through `scripts/forge-clone.ps1`, sets
the identity you confirm and reports the identity the clone ended up
with. The engine ignores `projects/*` (except its own
`projects/forge`) and the scripts find your project through its
`.git`. A project without a repository is reported as "not under
git" — a fact, not an error.

### Script prerequisites

- `doc2md.ps1` needs markitdown:
  `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.
- `md2pptx.ps1` needs the `document-skills` plugin, installed once
  from an interactive Claude Code session
  (`/plugin marketplace add anthropics/skills`, then
  `/plugin install document-skills@anthropic-agent-skills`), and a
  deck template named by path (`-Template <file.potx>`) — typically a
  document of a library project — or none, in which case Claude
  designs the visuals.
- The git scripts (`forge-save`, `forge-pull`, `forge-status`,
  `forge-clone`, `forge-branch`) need nothing beyond git.

### Saving and syncing

Two doors, two speeds. `/save` runs the `light` check, then commits
and pushes on the current branch — no render. `/release`, from `main`
only, runs its checks, settled with you by walkthrough, offers
`critique essence` once, re-renders the README and release notes and
then saves with the release message and, at an approved major, the
tag `v<major>`. Underneath both are the scripts in `scripts/`, the
only intended door to git — reading state included: each serves the
engine and every project repository, so a bare save commits each
repository with changes on its own and pushes where it has a remote.
`main` is the released line; branches are voluntary and left to git —
`forge-branch` creates or switches, merging stays with git, by hand or
by merge request. One remote per repository; the scripts carry no URL
and no identity. Saves made directly from the shell are unaffected.

### Upgrading

Upgrading the engine is `scripts/forge-pull.ps1`, a fast-forward of
`main`; your projects are untouched by it and record no engine
version. Read `RELEASE-NOTES.md`, the *Action required* lines first:
they say what a new version expects of your projects and your
instance files. Then, project by project, run `/check project <slug>`:
it measures the project against the current conventions and reports
what no longer conforms, nothing else. Go through the findings with
Claude one at a time and agree what to migrate and how; Claude makes
the changes on your word, in the session, with no migration tool in
between — the check and the release notes are the tool. A project you
leave as it is stays valid under the conventions it was written to;
migrating it is your decision, per project, never assumed.

## 13. Scripts

| Script | Purpose | When it runs | Needs |
|---|---|---|---|
| `scripts/forge-save.ps1` | Commits and pushes — the engine and every project repository with changes. | Under `/save` and `/release`, or by hand from the shell. | git |
| `scripts/forge-pull.ps1` | Fast-forwards from the remotes; on the engine, the upgrade channel. | When you upgrade the engine or sync a project. | git |
| `scripts/forge-status.ps1` | Reports the state of the repositories without changing anything. | Whenever you want to know where things stand. | git |
| `scripts/forge-clone.ps1` | Brings an existing project repository into `projects/`. | Under `/import-project`. | git |
| `scripts/forge-branch.ps1` | Switches to or creates a branch; merging stays with git. | When you choose to work on a branch. | git |
| `scripts/doc2md.ps1` | Converts a functional binary source into the Markdown extract that then is the source. | Under `/ingest`, on your explicit word. | markitdown — see Setup |
| `scripts/md2pptx.ps1` | Turns a Markdown deck render into a `.pptx` through headless Claude Code. | After `/render` of a deck recipe. | `document-skills` plugin — see Setup |

## 14. Planned extensions

The chain is designed to grow downward toward realisation, in the
same project and by the same principal's hand, when he chooses to
take his own thought further: a BRD layer is certain to come,
solution architecture and integration are intended, a strategy layer
is possible if it proves to make sense. Which layers are added, and
in what order, is open, and nothing is approved for construction —
the mechanics of a layer are designed when that layer is actually
taken up, not in advance. The chain never spans two principals: what
a recipient does with an assignment in his own instance is his own
forge run, the assignment becoming his brief.

More principals means more instances: a second principal receives the
forge via git and runs their own instance, and genuine multi-user
operation is open and deliberately not worked on now. Independent
challengers on a different model family are planned, as the
calibration point the isolated reviewers lack on their own.

Forge of Thought is itself run through its own process:
`projects/forge/` holds its brief, intent, decisions and ledger, and
this README and the release notes are renders from that project's
recipes. A process change is complete only once that intent is
updated and the README re-rendered.

## 15. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) — petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit
the author and link to this repository.

## 16. About this README

This file is a render of `projects/forge`: never edited by hand,
regenerated by `/render readme` whenever the process changes, and by
every `/release` of the engine. Fixes go into the recipe
(`projects/forge/recipes/readme.md`) or into its inputs, never here.
The YAML front-matter provenance at the top is kept by design. Changes
to the system itself are recorded in `projects/forge/`.

_Last updated: 2026-09-06_
