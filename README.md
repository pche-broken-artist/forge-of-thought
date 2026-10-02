---
project: forge
render: readme
generated: 2026-10-02
recipe: recipes/readme.md v0.54
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v4.49
  - .claude/agents/
  - .claude/skills/forge/states/
  - .claude/skills/
  - scripts/
  - templates/ledger.md
---

# Forge of Thought 4.49

*A workshop where thought is tempered and shaped.* · [Release notes](RELEASE-NOTES.md)

Forge of Thought is an **AI cognitive extension** of a thinking human,
the **principal**: whoever's thinking is being forged. It takes a raw,
half-formed idea — a process redesign, a platform initiative, an
organisational change, a D&D campaign — and tempers it into a precise,
self-contained handover for whoever delivers it: a team, a colleague,
your future self. It rests on one principle — **the machine carries
every part of the work that is not deciding** — in three forms.

- **It thinks with you.** It interviews and probes, criticises,
  challenges and inspires; it draws out what you have not yet
  articulated and lays out options with their trade-offs. It
  proposes — you decide.
- **It keeps the work consistent.** Nothing wanders off in forgotten
  chats: the thinking lives in versioned, templated artefacts, while
  decisions, state and history keep themselves in order and
  consistency is guarded across every output.
- **It carries the tedious work.** Audience-facing outputs — a pitch,
  a deck, even this README — are **renders**: generated from the
  artefacts through recipes, regenerated whenever the thinking moves,
  never written by hand twice.

Technically, the forge is a git repository: slash commands and
isolated agents — challenger personas and critic lenses — for Claude
Code, templates, and the conventions binding them. Today the chain of
documents ends at the assignment; it is built to grow further down
without reworking anything that exists.

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
- The same thinking retold to every audience — a pitch, a deck, a
  mail — each version rewritten by hand and drifting from the others.
- Feedback and decisions with no place to land, so the same ground is
  fought over twice.
- Assumptions nobody attacked before reality did.

## 2. What you get

- A versioned document chain growing from a brief — your idea put
  together, yours by your approval and locked once it is done — to a
  self-contained assignment.
- An elicitation interview that forges the intent.
- Blind adversarial reviewers, every verdict recorded.
- Audience-specific renders generated from recipes, including an
  actual PowerPoint file through your own template.
- External sources registered immutably and used only as the
  principal directs.
- Everything in files and git — nothing depends on a chat's memory.

## 3. Quickstart

First, once per machine:

```
git clone <this repository>      # you are looking at it
# install Claude Code first — see Setup
claude                           # always from the engine root
/setup                           # first run only — fills CLAUDE.local.md, sets the model, Fable
```

**Starting a new project**

```
/new-project my-idea
/forge intent
/save
```

**Bringing an existing project**

```
/import-project <project url>    # clones into projects/ — the commit identity is git's, resolved from your own configuration
/forge <project-slug>            # the slug is the repository's name; select the project before any work — the forge cannot guess it
```

Each project lives inside `projects/<slug>/` as a git repository of
its own, which the engine does not track — that is why you name it
first.

## 4. How it is used

### The flow

A thought arrives: a reorganisation you keep turning over, a platform
nobody has quite described yet, a campaign taking shape for your D&D
table. You put it together as a brief, alone or in conversation with
the forge (`/forge brief`): what you want, why, and what you do not
want. Claude brings what exists elsewhere, proposes a research step
here and there, and writes down what the two of you arrived at. When
it says what you mean, you lock it.

From the brief the intent is forged (`/forge intent`). Claude mines
the brief with you, probes the contradictions, asks what you have not
said yet, and over days and sessions the intent becomes what you
actually hold. You close the laptop mid-thought; next week the files
are still there, and `/ledger` tells you where you stopped.

Material arrives as it will. You drop a downloaded security standard
into the project and `/ingest` registers it; weeks later you ask
Claude to verify the intent against it, and only then does it play a
part. Where a topic needs grounding, `/research` writes a durable
note instead of a chat answer.

When the thinking feels solid, you set the reviewers on it. A
challenger who never saw your conversation attacks the substance
(`/challenge cto`); a critic reads the documents for ambiguity and
drift (`/critique clarity`). You go through what they found one item
at a time, and nothing blocks: you decide what changes.

Then the assignment is distilled for the people who will deliver it
(`/forge assignment`). Meanwhile the group needs a pitch: you compose
a recipe, guided by a genre interview if you like
(`/recipe presentation`), and `/render` produces the deck — Markdown
first, a plain PowerPoint beside it, and `/publish` makes the
designed one when you ask. The next time the intent moves, the pitch
is regenerated, not rewritten.

Along the way `/save` puts everything into git, and `/release`
checks the whole, regenerates the README and the release notes and
marks the version. This very README is produced the same way.

### What it looks like in practice

A worked example from a real project will appear here once one is
published.

## 5. How the work feels

The forge is as much a way of working as a set of files, and these are
the named methods of that work — the vocabulary you and Claude share:

- **Walkthrough.** Any list of items that needs your decision —
  findings, challenges, open threads, a comparison — is worked one
  item per message, in order of weight, each proposition closed with
  the verdict line `(a)ccept / (m)odify / (r)eject / (p)ark`. You
  answer with the single letter as your whole message, the verdicts
  are carried to one write at the end of the round, and an item that
  no longer applies can be declared obsolete.
- **Propose, never decide.** Claude criticises, challenges, inspires
  and lays out options; you compose, and `??` asks for its honest
  opinion of what you have just written.
- **Step by step.** Anything that needs your consent — a write, a
  commit, a rename, the birth of a new document — arrives as one step
  with its operation, target and reason, and runs on your word.
- **Elicitation interview.** Claude draws out by questions, one per
  message, what you have not yet articulated.
- **In pieces.** You may send one long thought as several messages and
  close it with a word such as "done"; until then Claude only
  acknowledges.
- **Draft early.** An early draft is a tool for drawing out your
  reaction, not an output.
- **Reflect back.** Before anything is written, Claude restates what it
  understood, so that the write confirms rather than surprises.
- **One write per round.** What is agreed in a working conversation is
  carried and written once at its end, when you type `write`.
- **Intent-first.** A change of substance goes into the intent and
  propagates from there; only wording is fixed downstream directly.
- **Recommend, do not push.** Every option comes with a recommendation
  and its reason, stated once and not re-argued without new facts.

None of these is a command: you invoke any of them in a word.

| You type | What it does |
|---|---|
| `a`, `m`, `r` or `p` | Answers the verdict line `(a)ccept / (m)odify / (r)eject / (p)ark`, as your whole message. |
| `write` | Orders the write of everything agreed in the round. Claude shows you the round first and writes on your yes. |
| `??` | Asks for Claude's honest opinion of what you have just written. Three points at most, nothing written. |

## 6. Roles

| Role | What they own |
|---|---|
| Principal | Whoever's thinking is being forged: supplies ideas, answers and decisions, and has final authority on all content. |
| Claude | The principal's cognitive extension: owns structure, order, process discipline and document hygiene, and proposes, never decides. |

Some rules stand throughout. When unsure, Claude asks rather than
assumes, and a contradiction, gap or risk it finds is raised at once
as a question; it says in plain words whether what it brings is
verified, unverified or a hypothesis. It never introduces a new
convention, prefix or section without your decision, researches key
topics before inventing, and treats critiques and checklists as
advice: only the principal publishes.

One instance of the forge serves one principal; recipients
collaborate through the artefacts handed to them, and more principals
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
is renumbered and nothing existing is reworked, which is why files
are numbered in tens. The boundary between chain and render is
authorship: a chain artefact is composed by the principal, a render
is generated from artefacts — an article you write is a layer of the
chain, its translation is a render.

| File | What it is | Audience | Behaviour |
|---|---|---|---|
| `00-brief.md` | The idea put together: what you want and why. | Principal | Draft while composed, then locked at 1.0. |
| `00-brief-<name>.md` | A later whole of thinking, born as a brief of its own. | Principal | Same states and rules as the founding brief. |
| `10-intent.md` | The consolidated current state of your intent. | Principal and Claude | Rewritten freely, versioned. |
| `10-intent.threads.md` | The intent's open threads and their working debate. | Principal and Claude | Freely rewritten, part of the intent. |
| `20-assignment.md` | The direction handed to the recipients. | Recipients | Rewritten freely, versioned. |
| `<file>.history.md` | What changed in a versioned document, and why. | Principal and Claude | Append-only log. |
| `decisions.md` | Your decisions with their reasons (DEC). | Principal and Claude | Append-only. |
| `ledger.md` | The single source of truth for state. | Principal and Claude | Freely rewritten. |

> A locked brief is immutable — composed, then locked, never touched again.

**The brief** is free-form: any structure you find useful, no
required content and no IDs, only a minimal YAML header. It holds
thoughts to be processed rather than decisions, so they may be
changed, reworked or dropped when they are mined, and it is rough on
purpose: the chiselling is the intent's. It is yours by your approval,
whoever first said a thought. Three origins are equally legitimate: it
arrives finished from outside and is locked on arrival, it is begun
outside and finished with Claude, or it is born in the forge from the
first word; `/forge brief [name]` is the door for the latter two. A
project may have more than one: every later whole of thinking that
would otherwise land in the intent as a batch of unproven positions is
born as `00-brief-<name>.md`. Each locked brief is mined into the one
intent, its positions citing the brief as provenance, and the ledger's
Briefs table tracks how far (`pending`, `partial`, `mined`,
`dropped`); a whole that dies on the way leaves its brief locked and
one rejected direction with the reason.

**The intent** is the consolidated *current* state of what you want:
positions (POS), facts (FCT), open threads (THR) kept beside it in
`10-intent.threads.md`, and rejected directions with their reason
(REJ), each with a stable ID. It is rewritten for coherence every
round rather than appended to, and every change is recorded in its
history companion. Its audience is you and Claude only. It exists
because chat context dies and anything of value must live in a file:
it is the document to read when you return after weeks, instead of
excavating old conversations — and it replaced an append-only log of
questions and answers that left the current state scattered.

**The assignment** is distilled from the intent for the recipients and
is the one document they receive: requirements, out of scope,
constraints, assumptions, deliverables, open questions with an owner
and optional success criteria (REQ, OOS, CON, ASM, DEL, TBC, SCR). It
is complete and precise, it assigns rather than solves, and it is
self-contained, so that the recipients can act rightly without you in
the room. It is found in a joint pass: questions up front only for
what the intent does not answer, a recast of the whole with a
provenance map, and a walkthrough by group.

Iteration runs intent-first, with drafting early as a legitimate
tool. Each working round is written once, at its end, on your word.

Feedback from recipients has no channel of its own: you process it
and feed your conclusions back through `/forge intent`.

> A render is never edited by hand — what is iterated is its recipe.

**Renders and recipes.** A recipe (`recipes/<recipe>.md`) holds the
inputs, the audience, the instructions and the output template in one
versioned file; it is a tool, not a record of thinking, carrying a
version and an updated date but no status. `/render <recipe>`
regenerates the output in an isolated agent that sees only the recipe
and its inputs, never the working conversation, and every render
opens with YAML front-matter citing the recipe and each input with its
version; the ledger's Renders table mirrors it. A render may serve as
an input of another render — a deck slide citing an architecture
picture — when the citing recipe declares it among its inputs. A
render assigns nothing and is not part of the chain: the artefacts
stay the source of truth.

**From Markdown to slides.** Everything the forge produces is
Markdown, content only. Composing a recipe may be guided by genre
(`/recipe presentation`). An output is made in two steps, each with
its own command. `/render` makes the Markdown and, where the recipe
names a format in its `Format` section, the plain `.docx` or `.pptx`
beside it through pandoc — cheap, the same every time, Mermaid
diagrams landing as blocks of code. `/publish` makes the designed file
through a model into `published/` — expensive, started by the
principal only, from the Markdown as it lies on disk; it never renders
and sends nothing anywhere. A recipe without a format ends at the
Markdown. A deck template or a reference document is named by path,
typically a document of a library project, and the page is A4 by
default. The Markdown stays the source of truth, and all other format
conversion happens outside the forge.

## 8. Isolated reviewers

The reviewers run with a clean context: they see the project's
documents only, never the working conversation, so they cannot be
told what we really meant — that blindness is where their value comes
from. Every kind of reviewer is of one shape: an agent file per lens,
persona or check, its shared behaviour preloaded from one contract,
invoked by hand, producing an immutable dated report and settled by
walkthrough. All run on the session model; nothing they find blocks
anything.

Isolation is not independence. The author, the critics and the
challengers share one model family, so what that family systematically
cannot see none of them will find, and agreement between the reviewers
is never treated as validation — it only means the artefact is
consistent under one set of priors. The calibration point lies outside
the forge: review by humans or by a different model family, at the
principal's discretion; independent challengers on a different model
family are planned.

### Critic (`/critique`)

The critic judges the quality of the documents, never the substance.
Command: `/critique <lens> [artefact] [slug]`; bare, it lists the
lenses and recommends a fit. Lenses:

- `clarity` — reads each artefact on its own for ambiguity,
  contradiction, duplication, scope hygiene and Requirement style; fit
  before a handover.
- `essence` — reads the chain for drift: distils each layer's essence
  blind and compares it with the layer above; fit as soon as a second
  layer exists.

Output: findings (`FND`) in `reviews/YYYY-MM-DD-critique-<lens>.md`
and the ledger. Finding states:

- `open`
- `resolved`
- `rejected`
- `parked`
- `obsolete`

### Challenger (`/challenge`)

The challenger judges the substance of the thinking, never the quality
of the documents. Command: `/challenge <persona> [artefact] [slug]`;
bare, it lists the personas and recommends a fit. Personas:

- `cto` — a CTO-level peer reviewer challenging assumptions, blind
  spots, second-order effects and organisational reality; not a
  document auditor.

Output: challenges (`CHL`) in
`challenges/YYYY-MM-DD-challenge-<persona>.md` and the ledger; an
accepted challenge must change the intent. Challenge states:

- `open`
- `accepted`
- `rejected`
- `parked`
- `obsolete`

### Checks (`/check`)

A check judges mechanical conformance with the conventions, never
substance or quality; each check owns one concern and none another's.
Command: `/check <check> [slug]`, on a project by its slug or on the
engine; bare, it lists the checks and recommends a fit. Checks:

- `light` — verifies a project's bookkeeping: front-matter against the
  history companion, ledger tables against the files, dependencies and
  resource indexes against the directories; fit for a save.
- `project` — verifies a project's structure, IDs, assignment style,
  language, immutables, recipes and renders against the conventions.
- `engine` — verifies the core (CLAUDE.md, templates, skills, agents,
  scripts) against itself and the forge intent: every position
  honoured, nothing withdrawn still advertised, every decision
  reflected.
- `single-source-of-truth` — verifies that every rule, procedure and
  file shape is written in one place and cited everywhere else; the
  honest sweep, expensive by design, fit before a major or after a
  round on the operating layer.
- `history` — reads a document with its history and reports where the
  division between them does not hold, proposing each move in full;
  fit when a document is cleaned, never at a save or a release.

Output: the agent returns its report and the command files it as
findings (`FND`) in `reviews/YYYY-MM-DD-check-<name>.md` and the
ledger — only when it finds something; a clean run files nothing.
Checks never call each other. Finding states:

- `open`
- `resolved`
- `rejected`
- `parked`
- `obsolete`

## 9. Commands

Every command is a skill of Claude Code; `/man <command>` prints what
it does in full.

| Command | Purpose |
|---|---|
| `/setup` | First run after cloning the engine: prepares the instance. |
| `/new-project <slug>` | Scaffolds a project from templates, a thought project or a library; files only, never git. |
| `/import-project <git-url>` | Brings an existing project into `projects/` by cloning it. |
| `/forge [slug]` | The chain map of a project: artefacts, versions, stale renders and the recommended next step. |
| `/forge <state> [slug]` | Works on the artefact you name — `brief`, `intent`, `assignment` — through its definition. |
| `/ingest [file] [slug]` | Stores, registers and indexes external input in `sources/`; bare, sweeps `sources/`. |
| `/render <recipe> [slug]` | Regenerates a render from its recipe, with its plain file where the recipe names a format. |
| `/publish <recipe> [slug]` | Makes the designed `.pptx` or `.docx` from a render, through a model; started by the principal only. |
| `/recipe [genre] [slug]` | Composes or iterates a render recipe by genre; bare, lists the genres. |
| `/critique [lens] [artefact] [slug]` | Runs a critic lens on the quality of the documents; bare, lists the lenses. |
| `/challenge [persona] [artefact] [slug]` | Runs a challenger persona against the substance; bare, lists the personas. |
| `/research <topic> [slug]` | Researches current best practice and stores a durable, indexed note in `research/`. |
| `/ledger [slug]` | A quick state readout from the ledger. |
| `/check [check] [slug]` | Runs a check on a project or on the engine; bare, lists the checks. |
| `/save [slug] [-m "message"] [-Tag name]` | Saves one repository, or every one with changes. |
| `/release [slug] [-m "message"] [-Tag name]` | Releases one repository from `main`. |
| `/spinoff <project> <group> <slug>` | Splits a requirement group into its own project, on the principal's explicit decision only. |
| `/man [command \| method]` | The forge's manual, read from its own definitions. |
| `/manual …` | Alias of `/man`. |

`/forge <state>` needs nothing memorised: the state is simply the name
of the artefact you want to work on, so a new layer of the chain
brings its command with it. `/forge` shows the whole chain and what
to do next; `/ledger` only reads the state back.

`/ingest` takes a file or text pasted into the conversation; before
storing it stops on personal matter and asks, it asks of every binary
whether to convert it to Markdown (yes makes the extract the source),
records an origin date only where it can be found for free, writes an
index entry and then asks what the source is for — and carries nothing
into the intent. `/save` drafts a one-line commit message from the
records the round appended to the histories and commits with the
wording you confirm; a tag is set only on your word. `/release` names
one repository, offers `/critique essence` once, reports what
materially changed in the regenerated README and release notes so you
can rule on the delta, and commits as `release <intent version>`; at
an approved major it proposes the tag `v<major>`.

Commands are entry points, not the only door: the same rules hold in
plain conversation, and you can simply ask.

### A typical journey

- You have an idea and put it together as a brief, then lock it when
  it says what you mean (`/forge brief`).
- You work the intent over several sessions, answering questions,
  dropping directions and keeping open what is still open
  (`/forge intent`).
- You put pressure on it: a challenger attacks the substance, a critic
  the documents, and you give your verdict on each point
  (`/challenge`, `/critique`).
- You need to present it, so you compose a presentation recipe and
  render it, including the PowerPoint file (`/recipe presentation`,
  `/render`, `/publish`).
- You distil the assignment for the people who will deliver it
  (`/forge assignment`).
- You save as you go, and release when a version is worth marking
  (`/save`, `/release`).

## 10. Conventions

**IDs.** Every item carries an ID of the format `PREFIX.NNNN`, all
prefixes three letters. IDs are global and stable, never renumbered;
items may move between groups without changing their ID. Items are
numbered in tens (`REQ.0010`, `REQ.0020`), each new group starting at
the next hundred (`REQ.0100`); overflow takes the next free number
anywhere. Groups are plain headings with no IDs, metadata or
lifecycle, at most two levels deep.

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
| THR | open thread — unresolved matter to elicit next; carries its origin: the principal's word (the default, unmarked), a source by path, or Claude's synthesis | intent (its threads file) |
| REJ | rejected direction, with the reason it was dropped | intent |
| FCT | fact — what is the case, as the principal states it or as a source states it; not a stance; a source's fact cites its file, the principal's needs none; verification is never demanded | intent |
| FND | finding of a critic (document quality) or of a check (conformance) | ledger, reviews |
| CHL | peer-review challenge (substance) | ledger, challenges |
| DEC | decision, incl. rejected findings and challenges | decisions.md |

**Terms.** Every assignment carries a Terms section, so that it can be
forwarded without oral tradition; defined Terms are capitalised in
item text.

**Language.** The forge dictates one output language per project: the
artefacts of the chain — intent, assignment, later layers — are
written in the language the project's ledger header declares
(`language`, English when absent). The briefs are the exception, kept
in whatever language they are written in. Everything else a project
holds — ledger, decisions, history, reviews, challenges, indexes,
research, recipes — is always English, as is the notation (ID
prefixes, `shall`, status words, front-matter keys). A render may be
in any language its recipe declares. The conversation language is
per-instance configuration and lives in `CLAUDE.local.md`.

**Requirement style.** Items use **shall** / **shall not**, never
would, could, should, might, may or MoSCoW wording. There is no
priority column and there are no priority tags: everything is
essential, and an exception carries a note reading *optional*. Each
item covers one idea, is written once, and is written in full, correct
sentences. Testability is recommended, not required — delegating
concretisation through a `DEL` item is a legitimate outcome — and no
item may depend on an external link to be understood, agreed or later
tested. Illustrative:

> REQ.0010 The Platform shall record every request and every response passing through the Gateway, with the identity of the requesting User and the time.

**Completeness over brevity.** An assignment carries the full in-scope
substance of the intent; nothing is omitted for brevity's sake, length
is whatever fidelity requires, and leaving a matter out is legitimate
only as an explicit delegation (a `DEL` or `TBC` item).

**Assigning, not solving.** An assignment assigns, it does not solve:
the machinery of executing delivery belongs to the recipients.

**Versioning.** Integers denote signed-off versions: `0.1, 0.2, …`
are drafts, `1.0` is approved, `1.1, 1.2, …` are changes since that
are not yet approved themselves, and `2.0` is the next approved
version incorporating them all. Front-matter carries `version`,
`date`, `status` (`draft | approved | superseded`) and `last_change`,
and the status must agree with the number.

**Document kinds.** "Document" is every file of a project; "artefact"
is reserved for the documents of the chain — the ones the principal
composes, the reviewers read and the renders are generated from.

| Group | Kind | Meaning | Written by | Versioned | Behaviour |
|---|---|---|---|---|---|
| artefacts | brief | the idea put together: what the principal wants and why, with what he chose from the finding | principal; Claude may work on the text | yes | locked at 1.0, then immutable |
| artefacts | intent | current understanding for principal and Claude: positions, facts, threads, rejections | Claude, principal composes | yes | rewritten freely |
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

Every versioned document keeps its history in an append-only
companion `<file>.history.md` beside it, one record per change, and
its `last_change` front-matter line is derived from the newest
records, never written by hand. An integer version is approved, and a
recipe never is: it carries `updated` in place of `date`, no status,
and stays 0.x.

**Project kinds.** A project declares its kind in its ledger header:
`thought` (the default) travels the chain; `library` holds shared
material used across projects — a ledger, sources and research with
their indexes, and a README cataloguing them — with no chain, and its
slug carries the `lib-` prefix.

**Naming.** Project slugs are lowercase and hyphenated on disk;
display names may differ and must be legible to the audience. The
system's own project is `forge`; a library is `lib-<name>`.

## 11. Repository layout

```
CLAUDE.md                  # the universal core, for the agent
CLAUDE.local.md            # instance facts (who the principal is, the
                           # conversation language) — gitignored,
                           # created by /setup from
                           # templates/CLAUDE.local.md
README.md                  # for humans — a render (/render readme)
RELEASE-NOTES.md           # release notes — a render (/render
                           # release-notes); the shape:
                           # templates/recipe-release-notes.md
logo.png                   # project avatar
LICENSE                    # CC BY 4.0 — the engine is published
                           # under attribution
scripts/                   # forge-save / forge-pull / forge-status
                           # / forge-clone / forge-branch (git),
                           # doc2md (document →
                           # Markdown), md2pptx (deck render →
                           # PowerPoint), md2docx (render → Word),
                           # each by pandoc or by a model,
                           # hook-walkthrough (the per-prompt hook
                           # of .claude/settings.json)
.claude/                   # skills (the commands, the reviewers'
                           # contracts and the walkthrough method),
                           # agents, settings
                           # (settings.local.json: the session
                           # model — gitignored)
templates/                 # canonical skeletons
projects/                  # gitignored (projects/*) except
                           # projects/forge — every other project is
                           # a git repository of its own, which the
                           # engine does not know
projects/<slug>/           # kind: thought — the chain
  .git/                               # the project's own repository
  README.md  RELEASE-NOTES.md         # renders of the project's own
                                      # readme and release-notes recipes
  logo.png                            # optional project avatar
  00-brief.md  10-intent.md  20-assignment.md
  10-intent.threads.md                # the intent's open threads,
                                      # part of the intent
  00-brief-<name>.md                  # later briefs, one per whole
  <file>.history.md                   # history of each versioned
                                      # document: append-only
                                      # companion, a log
  <file>.history.archive.md           # a history table before the
                                      # log, immutable
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
  recipes/<recipe>.history.md         # the recipe's history
  renders/<recipe>.md                 # generated outputs, overwritten by
                                      # /render, provenance front-matter
  renders/<recipe>.pptx               # the plain file of a render, made
  renders/<recipe>.docx               # by /render through pandoc where
                                      # the recipe names a format
  published/<recipe>.pptx             # the designed file, made by
  published/<recipe>.docx             # /publish through a model
  reviews/YYYY-MM-DD-critique-<lens>.md  # immutable critique runs
  reviews/YYYY-MM-DD-check-<name>.md     # immutable check reports,
                                      # filed when a check finds
                                      # something
  challenges/YYYY-MM-DD-challenge-<persona>.md  # immutable peer reviews
  research/YYYY-MM-DD-<topic>.md      # immutable research notes
  CLAUDE.md                # optional project-specific polish; note
                           # that Claude Code's /export writes into
                           # the working directory — export outside
                           # the project or gitignore it
projects/lib-<name>/       # kind: library — material shared across
  .git/  ledger.md         # projects, no chain: only the ledger,
  README.md  logo.png      # sources and research; documents
  recipes/readme.md        # maintained by their owner; README =
  recipes/readme.history.md  # the catalogue, a render of its recipe
  sources/00-INDEX.md
  research/00-INDEX.md
```

## 12. Setup

### Prerequisites

- git.
- PowerShell 7 (`pwsh`) — the scripts are PowerShell, needed on macOS
  and Linux too.
- Python 3, for markitdown.
- A paid Claude subscription.

### Getting the forge and Claude Code

Clone this repository: it is the engine. Then install Claude Code:

- Windows: `irm https://claude.ai/install.ps1 | iex`
- macOS/Linux: `curl -fsSL https://claude.ai/install.sh | bash`
- or: `npm install -g @anthropic-ai/claude-code`

Sign in on the first run; usage draws from the same pool as Claude
chat. Always start `claude` from the engine root, so that `CLAUDE.md`
and `CLAUDE.local.md` load.

Then run `/setup` once. It fills `CLAUDE.local.md` — the conversation
language and who the principal is — from its template with you in a
short interview; the file is gitignored and never committed. It
creates `.claude/settings.local.json` with the session model set to
Fable, the strongest available model, which the whole forge including
the blind reviewers runs on; it tells you so in one sentence, and
`/model` or editing that file changes it at any time (permissions come
from the shared `.claude/settings.json`). It closes with your git
identity, which is git's own: it asks for the hosts you push to, with
a name and an e-mail for each, and offers to write the `includeIf`
stanzas into your `~/.gitconfig` — one identity per host, resolved by
git from the remote's URL — together with one global guard,
`user.useConfigOnly = true`, so that a repository on a host with no
stanza fails aloud instead of committing with a default. Declined, it
prints the lines for you to apply by hand. The forge itself sets no
identity anywhere, and `/setup` never overwrites existing files.

### Your projects

Each project is a directory under `projects/` and a git repository of
its own. `/new-project` creates the files; `git init` in that
directory and a remote, if you want one, are a one-off act of yours,
and the commit identity is git's, resolved per host from your own
configuration. An existing project is brought in with
`/import-project <git-url>`, which clones it into
`projects/<repository name>` through `scripts/forge-clone.ps1` and
reports the identity git resolves for it. The engine ignores
`projects/*` (except its own `projects/forge`), and the scripts find
your project through its `.git`. A project without a repository is
reported as "not under git" — a fact, not an error.

### Script prerequisites

- `doc2md.ps1` needs markitdown:
  `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.
- `md2pptx.ps1` has two engines (`-Engine pandoc | claude`). The
  `pandoc` engine, behind `/render`, needs pandoc
  (https://pandoc.org/installing.html). The `claude` engine, behind
  `/publish`, needs the `document-skills` plugin, installed once from
  an interactive Claude Code session
  (`/plugin marketplace add anthropics/skills`, then
  `/plugin install document-skills@anthropic-agent-skills`). A deck
  template is named by path (`-Template <file.potx>`), typically a
  document of a library project; without one the model designs the
  visuals.
- `md2docx.ps1` has the same two engines with the same needs. A
  reference document is named by path (`-Reference`, a `.docx`,
  `.dotx` or `.dotm`), typically a document of a library project;
  without one pandoc's built-in styles apply on an A4 page
  (`-PageSize Letter` for US Letter).
- `hook-walkthrough.ps1` needs nothing beyond PowerShell 7.
- The git scripts (`forge-save`, `forge-pull`, `forge-status`,
  `forge-clone`, `forge-branch`) need nothing beyond git.

### Saving and syncing

There are two doors. `/save` runs the light check, then commits and
pushes on the current branch, with no render. `/release`, from `main`
only, runs its checks and settles them with the principal, offers
`critique essence` once, re-renders the README and the release notes,
and then saves with the release message and, at an approved major, the
tag `v<major>`. Underneath are the scripts in `scripts/`: for Claude
and every command of the forge they are the only door to git, reading
state included — enforced for Claude by the deny rules of
`.claude/settings.json`. Each serves the engine and every project
repository: a bare save commits each repository with changes on its
own and pushes where it has a remote. `main` is the released line;
branches are voluntary (`forge-branch` creates or switches, merging
stays with git, by hand or by merge request). There is one remote per
repository and no URL anywhere in the forge.

### Upgrading

Upgrading the engine is `scripts/forge-pull.ps1`, a fast-forward of
`main`; your projects are untouched by it and record no engine
version. Read `RELEASE-NOTES.md`, the *Action required* lines first:
they say what a new version expects of your projects and your instance
files. Then, project by project, run `/check project <slug>`: it
measures the project against the current conventions and reports what
no longer conforms, nothing else. Go through the findings with Claude
one at a time and agree what to migrate and how; Claude makes the
changes on your word, in the session, with no migration tool in
between — the check and the release notes are the tool. A project you
leave as it is stays valid under the conventions it was written to;
migrating it is your decision, per project, never assumed.

## 13. Scripts

| Script | Purpose | When it is run | Install |
|---|---|---|---|
| `forge-save.ps1` | Commits and pushes the engine and every project that is a repository of its own. | By `/save` and `/release`. | — |
| `forge-pull.ps1` | Fast-forwards the engine and every project with an origin from their remotes. | To upgrade the engine or bring projects up to date. | — |
| `forge-status.ps1` | Reports the git state of the engine and every project, changing nothing. | Whenever git state is read, by `/save`, `/release` and `/setup`. | — |
| `forge-clone.ps1` | Clones an existing project's repository into `projects/`. | By `/import-project`. | — |
| `forge-branch.ps1` | Switches one repository to a branch, creating it if needed, or reports its branch. | When you want a branch, or to return to `main`. | — |
| `doc2md.ps1` | Converts Word, PowerPoint, PDF and Excel documents to Markdown through markitdown. | By `/ingest`, for a binary you choose to convert. | markitdown, see Setup |
| `md2pptx.ps1` | Makes a PowerPoint deck from a Markdown deck render, plain through pandoc or designed through a model. | By `/render` (pandoc) and `/publish` (model). | pandoc or the document-skills plugin, see Setup |
| `md2docx.ps1` | Makes a Word document from a Markdown render, plain through pandoc or designed through a model. | By `/render` (pandoc) and `/publish` (model). | pandoc or the document-skills plugin, see Setup |
| `hook-walkthrough.ps1` | Repeats the one-item walkthrough rule and three lines of conduct at every prompt. | By Claude Code on every prompt, configured in `.claude/settings.json`. | — |

`scripts/` is the only platform-bound layer of the forge, and it is
written to run unchanged on Linux and macOS: cross-platform
PowerShell 7 with nothing Windows-only, external tools (`git`,
`markitdown`, `pandoc`, `claude`) resolved from PATH. New scripts are
written in Python, and the PowerShell scripts are rewritten to it in
time.

## 14. Planned extensions

The chain is meant to keep growing downward, as far as a thought
needs taking: a BRD layer is certain to come, solution architecture
and integration are intended, and a strategy layer is possible if it
proves to make sense. Which layers are added, and in what order, is
open; the mechanics of a layer are designed when it is taken up, not
in advance. The layers grow in the same project by the same
principal's hand: the chain never spans two principals, and what a
recipient does with an assignment in an instance of their own is
their own forge run.

The forge stays a single-user tool per instance: more principals means
more instances, coordinated through git.

The forge develops itself through its own process: `projects/forge/`
is Forge of Thought run through its own chain, and a change to the
process is complete only once its intent is updated and this README
re-rendered.

## 15. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) — petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit
the author and link to this repository.

## 16. About this README

This file is a render of `projects/forge`: it is never edited by hand
and is regenerated by `/render readme` whenever the process changes,
and by every `/release` of the engine. Fixes go into the recipe or its
inputs. The YAML front-matter at the top is the render's provenance,
kept by design. Changes to the system itself are recorded in
`projects/forge/`.

_Last updated: 2026-10-02_
