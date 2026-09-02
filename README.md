---
project: forge
render: readme
generated: 2026-09-02
recipe: projects/forge/recipes/readme.md v0.31
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v3.10
---

# Forge of Thought 3.10

*A workshop where thought is tempered and shaped.* · [Release notes](RELEASE-NOTES.md)

Forge of Thought is an **AI cognitive extension** of a thinking human,
the **principal** — whoever's thinking is being forged. It takes a raw,
half-formed idea — a process redesign, a platform initiative, an
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
agent personas for Claude Code, templates, and the conventions binding
them. Today the chain runs from a brief through an intent to an
assignment; that is where it currently ends.

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
- An elicitation interview that forges the intent: questions that draw
  out what you have not yet put into words.
- Two kinds of blind adversarial reviewers — one on the documents, one
  on the thinking — with every verdict recorded.
- Audience-specific renders generated from recipes, including an
  actual PowerPoint file through your own template.
- External sources registered immutably and used only as you direct.
- Everything in files and git — nothing depends on a chat's memory.

## 3. Quickstart

**First, once per machine**

```
git clone …            # this repository — you are looking at it
                       # install Claude Code first — see Setup
claude                 # always from the engine root
/setup                 # first run only — fills CLAUDE.local.md,
                       # sets the model (Fable)
```

**Starting a new project**

```
/new-project my-idea
/forge intent
/save
```

**Bringing an existing project**

```
/import-project <project url>   # clones into projects/ — the commit
                                # identity is proposed from your
                                # CLAUDE.local.md roster and
                                # confirmed by you
/forge <project-slug>           # the slug is the repository's name;
                                # select the project before any work
                                # — the forge cannot guess it
```

Each project lives inside `projects/<slug>/` as a git repository of
its own, which the engine does not track — that is why you name it
first.

## 4. How it is used

### The flow

A thought arrives — a process you want redesigned, a platform you
want built, a campaign taking shape for your D&D table. You dump it
as it is: a page of prose, a few headings, a table if that is how it
came out. That is your brief. You may write it alone and hand it over
finished, or think it through with the forge (`/forge brief`) until
it says what you mean; then you lock it, and from that moment it is
never touched again.

From the brief the forge interviews you (`/forge intent`). It asks
what you have not said, reflects back what it understood, drafts
early so you have something concrete to react to, and writes the
intent once per round on your word. The intent is rewritten for
coherence every time; nothing lives only in the conversation, so you
can stop tonight and pick up in three weeks by reading one file. When
you need to know where things stand, `/forge` draws the map and
`/ledger` reads the state.

Material arrives whenever it arrives. A downloaded security standard,
a meeting transcript, an offer from a vendor: `/ingest` stores and
registers it, and it sits there until you say what it is for — later,
perhaps, you ask for the intent to be verified against that standard,
and only then is it read. Where a topic needs grounding, `/research`
looks up current practice and files what it found.

Before the next layer is derived, you send in the reviewers. A
challenger persona (`/challenge cto`) attacks the thinking; the critic
(`/critique`) audits the documents. Neither has seen your
conversation, so neither knows what you meant to say — only what you
wrote. Their findings come back one at a time for your verdict, and
nothing they say blocks you: you accept, you overrule with a reason,
or you leave it open.

When the intent is ready, `/forge assignment` distils it into the one
document the recipients receive, self-contained and complete. And
whenever someone else needs the thinking in their shape — a pitch for
the group, a deck for the board, a mail, this very README — you write
a recipe, guided by a genre interview if you like (`/recipe
presentation`), and `/render` generates the output. When the intent
moves, the render is regenerated; you never rewrite the pitch by
hand. `/save` keeps all of it in git as you go.

### What it looks like in practice

A worked example from a real project will appear here once one is
published.

## 5. How the work feels

The forge is as much a way of working as a set of files, and these
are the named methods of that work — the vocabulary you and Claude
share.

- **Walkthrough.** Any list that needs your decision — critique
  findings, challenges, the differences between two requirement sets,
  open threads — is worked one item at a time, in order of weight:
  Claude's recommendation with a one-sentence reason first, your
  verdict in a word or a counter-proposal, and "leave it open" is a
  legitimate answer. You are never handed a table asking for every
  verdict at once; verdicts are written once at the round's end, and
  whatever produces a list ends by offering a walkthrough.
- **Propose, never decide.** Claude criticises, challenges, inspires
  and lays out options; you compose.
- **Step by step.** Anything that needs your consent — a write, a
  commit, a push, a rename, anything hard to reverse — arrives as one
  step with the exact operation, its target and the reason, and runs
  on your word; a plan you have seen is not consent for its steps.
- **Elicitation interview.** Claude draws out by questions what you
  have not yet articulated, never filling a gap by assumption.
- **Draft early.** An early draft is an elicitation tool, not an
  output: concrete text sharpens your reaction.
- **Reflect back.** Before anything is written, Claude restates what
  it understood, so the write confirms rather than surprises.
- **Intent-first.** A change of substance goes into the intent and
  propagates from there; only wording is fixed downstream directly.
- **Recommend, do not push.** Every option comes with a
  recommendation and its reason, stated once; a declined
  recommendation is not re-argued without new facts.

None of these is a command: you invoke any of them in a word.

## 6. Roles

| Role | What they own |
|---|---|
| **Principal** | Whoever's thinking is being forged: supplies ideas, answers and decisions, and is the final authority on all content. |
| **Claude** | The principal's cognitive extension: owns structure, order, process discipline and document hygiene; criticises, challenges, inspires and lays out options; proposes, never decides. |

The standing rules of the collaboration: when unsure, Claude asks and
never fills a gap by assumption; it never introduces a new convention,
prefix or section unilaterally — it proposes, waits for a decision,
then writes it down; many iterations are the normal mode; for key
topics it researches current practice before inventing and stores
durable findings in `research/`; critiques and checklists are
advisory, never blocking — a missing section may be a deliberate
delegation, not a defect; structure with stable IDs beats prose, with
narrative confined to purpose and objective; assignments are complete
and precise; artefacts are written once per iteration round, on the
principal's confirmation; and one mechanism lives in one place —
whatever the forge has a procedure for is used through its own
definition, never re-described or improvised, and a procedure stated
in two places is a defect. One instance serves one principal; the
recipients collaborate through the artefacts, not inside the
instance — more principals means more instances (see Planned
extensions).

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
is renumbered and nothing existing is reworked, which is why the files
are numbered in tens. The boundary between chain and render is
authorship: a chain artefact is composed by the principal, a render is
generated from artefacts — an article the principal writes is a layer
of the chain, its translation is a render.

| File | What it is |
|---|---|
| `00-brief.md` | The idea as the principal wrote it — draft until locked, then verbatim and never edited; later wholes as `00-brief-<name>.md`. |
| `10-intent.md` | The working understanding — rewritten freely for coherence, versioned. |
| `20-assignment.md` | The frozen high-level direction for the recipients — versioned, the only document handed over. |
| `decisions.md` | Append-only DEC records. |
| `ledger.md` | The single source of truth for state. |

> A locked brief is immutable — composed, then locked, never touched
> again.

The **brief** is an intent that is composed and then locked. It is
free-form: any structure the principal finds useful — prose,
headings, tables, use cases — with no required content and no IDs,
only a minimal YAML header. It holds thoughts to be processed, not
decisions: they may be changed, reworked or dropped when mined. It is
`draft` while being composed and `approved` (1.0) once the principal
locks it. Three origins are equally legitimate and indistinguishable
to the forge: it arrives finished and is locked on arrival; it is
begun outside and finished with Claude; it is born in the forge —
`/forge brief [name]` is the door for the latter two. A project may
have more than one: every later whole of thinking that would
otherwise land in the intent as a batch of unproven positions is born
as `00-brief-<name>.md` under the same rules. A locked brief is mined
into the single intent — positions cite it as provenance, a whole that
dies on the way leaves the brief locked and one rejected direction
with the reason — and the ledger tracks how far each brief is mined
(`pending | partial | mined | dropped`). Each locked brief is the
provenance anchor and drift measure of its whole.

The **intent** (`10-intent.md`) is the working document, for the
principal and Claude only: the consolidated *current* state of what he
wants, why, what is open and what was rejected — positions (POS), open
threads (THR) and rejected directions with their reason (REJ), each
with a stable ID. It is rewritten for coherence every round rather
than appended to, with its changes recorded in a changelog. It exists
because chat context dies and anything of value must live in a file:
it is the document to read when returning to a project after weeks,
instead of excavating old conversations.

The **assignment** (`20-assignment.md`) is distilled from the intent
for the recipients — teams, colleagues, or the principal's future
self — and is the one document they receive: requirements,
out-of-scope items, constraints, assumptions, deliverables, open
questions with an owner and optional success criteria (REQ, OOS, CON,
ASM, DEL, TBC, SCR). It carries the full in-scope substance of the
intent, complete and precise; it assigns rather than solves; and it
is self-contained.

Substance changes go intent-first and propagate to the assignment;
only wording is fixed in the assignment directly. Artefacts are
written once per iteration round, on the principal's confirmation —
one version bump, one Version History row for the whole round.
Feedback from the recipients has no channel of its own: the principal
processes it and feeds conclusions back through `/forge intent`.

> A render is never edited by hand — what is iterated is its recipe.

**Renders and recipes.** A render is an audience-specific output
generated from the chain — a pitch for the group, an architecture
picture, an executive summary, the repository README. Its **recipe**
(`recipes/<recipe>.md`) carries inputs, audience, instructions and the
output template in one versioned file, and more than one input is
legitimate; `/render <recipe>` regenerates the output into
`renders/<recipe>.md` — or the recipe's `output:` path — overwriting
freely, with history in git. Generation runs in an isolated subagent
that sees only the recipe and its inputs. Every render opens with YAML
front-matter provenance citing the recipe and each input with their
versions, and the ledger's Renders table mirrors it. A render assigns
nothing and is not part of the chain; it may itself serve as an input
of another render — a slide citing an architecture picture — when the
citing recipe declares it among its inputs. Every project has a README
as a render of its own `recipes/readme.md` and, if it is a thought
project, release notes from `recipes/release-notes.md`; every `/save`
that touches the project regenerates them.

**From Markdown to slides.** Everything the forge produces is
Markdown, content only. Composing a recipe may be guided by genre
(`/recipe presentation` for a slide-by-slide deck definition). The one
in-house conversion is `scripts/md2pptx.ps1`: it turns a deck render
into an actual PowerPoint file through headless Claude Code with the
official pptx skill — an LLM conversion by design, because deck
definitions are free-form and may carry instructions for the model. A
`.potx` template is applied when named by path (`-Template <path>`,
typically a document of a library project); without it, Claude
designs the visuals itself. The generated `.pptx` lands beside its
source render and is tracked like any render output; the Markdown
render stays the source of truth. All other format conversion happens
outside the forge.

## 8. Two isolated reviewers

Both reviewers run as isolated subagents with a clean context: they
see the artefacts only, never the working conversation — they cannot
be told what we really meant, and that blindness is the source of
their value. They run on the same session model as the author: speed
is bought with context, never with a weaker reviewer.

The **challengers** are a growing roster of persona lenses attacking
the substance of the thinking: unstated assumptions, whether the
objective is the real problem, second-order effects, organisational
reality, failure modes, the counter-case.

The **critic** is the auditor of the documents and of the project's
consistency across artefacts: ambiguity, gaps, contradictions,
duplication, divergence between intent and assignment, regression on
past findings.

Isolation is not independence. The author, the critic and the
challengers share one model family; what that family systematically
cannot see, none of them will find, so agreement between the
reviewers is never treated as validation — it only means the artefact
is consistent under one set of priors. The calibration point lies
outside the forge: review by humans or by a different model family,
invited at the principal's discretion.

### `/challenge <persona> [artefact]`

One isolated agent per persona (`challenger-<persona>`), each a
distinct lens defined by the blind spots it exists to find. The
behaviour shared by every persona lives in `templates/challenger.md`
and is carried verbatim by each persona file; only its Lens section is
its own. The first persona is `cto` — peer-CTO register: direct, few
and sharp, no flattery. Further personas are created only by the
principal's decision, and only where their blind spots genuinely
differ. Bare `/challenge` lists the roster and recommends a fit. The
target may be any chain artefact (default the intent); a layer is best
challenged before the next one is first derived from it. A run yields
three to seven sharp challenges, each with a severity (dealbreaker,
major, minor), a falsifiable "what would change my mind" and an
epistemic status; fabrication is banned — uncertainty is stated, not
papered over. Output: `CHL` items in
`challenges/YYYY-MM-DD-challenge-<persona>.md`, immutable once
written. Challenge states: `open | accepted | rejected (→ DEC) | parked
| obsolete`; an accepted challenge must change the intent, a rejected
one is recorded as a decision with its reason. The run ends by
offering a walkthrough.

### `/critique`

The critic reviews the chain artefacts for document quality and
produces `FND` items in `reviews/YYYY-MM-DD-critique.md`, immutable
once written, as a delta against the previous run: new, verified
resolved, still open, newly obsolete. Style violations — modal verbs
instead of shall, multi-idea items, dependence on an external link —
are findings; untestable wording is a recommendation, never a defect.
Finding states:

- open — reported, not yet ruled on;
- fixed — an iteration of the artefact concerned;
- overruled — recorded as a decision (DEC) with its reason;
- deferred — waiting on the principal, recorded in the ledger;
- obsolete — the passage it concerned no longer exists.

The run ends by offering a walkthrough.

## 9. Commands

Commands are the doors into the forge's phases; each is defined in
`.claude/commands/`.

| Command | Purpose |
|---|---|
| `/setup` | First run after cloning the engine: creates and fills `CLAUDE.local.md` by interview, creates `.claude/settings.local.json` with the model set to Fable (a notice, not a question), and offers the global git identity guard. Never overwrites, runs no git operation. |
| `/new-project <slug>` | Scaffolds a project by kind — files only, never git: a thought project with its brief captured verbatim (locked if finished, draft otherwise), or a library (`lib-`) of shared material. |
| `/import-project <git-url>` | Brings an existing project into `projects/` through `scripts/forge-clone.ps1`; the directory is the repository's name, and the commit identity is set per repository, proposed from `CLAUDE.local.md` by the URL's host. |
| `/forge [slug]` | The chain map: which artefacts exist at what versions, which renders are stale, which states can be worked next — with a recommended next step. |
| `/forge <state> [slug]` | Works on the named artefact (`brief [name]`, `intent`, `assignment`, …): the command is simply the name of the artefact you want to work on. |
| `/ingest [file] [slug]` | Stores and registers external input in `sources/` and indexes it; bare, sweeps `sources/` for unregistered files. |
| `/render <recipe> [slug]` | Regenerates a render from its recipe in `recipes/`. |
| `/recipe [genre] [slug]` | Bare, the genre roster; with a genre (`presentation`, `readme`, `release-notes`), guided composition — or iteration — of a render recipe. |
| `/critique [slug]` | Runs the isolated critic; review file plus ledger. |
| `/challenge [persona] [artefact] [slug]` | Bare, the persona roster; with a persona (e.g. `cto`), runs that challenger against any chain artefact (default the intent). |
| `/research <topic> [slug]` | Best-practice research into `research/`, indexed. |
| `/ledger [slug]` | The quick state readout from the ledger. |
| `/check [slug]` | Conformance of a project against the current conventions; all but forge when bare. |
| `/check-forge` | Consistency check of the core and `projects/forge`. |
| `/save [slug] [-m "message"]` | Pre-save check, findings settled with the principal, then commit and push. |
| `/spinoff <project> <group> <slug>` | Splits a requirement group into its own project — on the principal's explicit decision only. |

`/forge <state>` is a star, not a line: a thin dispatcher plus one
definition file per state in `.claude/commands/forge/`, each declaring
its own inputs, so a new layer branches from any artefact by adding
one file. `/ingest` stores, registers and catalogues — nothing more.
Sources may arrive at any stage, even before the brief; a source has
one form, so every binary file gets one question — convert to
Markdown? — and becomes either a text extract `sources/<slug>.md`
produced by `scripts/doc2md.ps1` (the original not copied, or
gitignored where it already lies) or a functional binary kept as is —
a template, a graphic. A set of related files lives as a bundle
`sources/<slug>/` with its own catalogue and counts as one source.
What a source is for is noted as a free-text role in the directory's
`00-INDEX.md`, and the principal alone directs how and when it is
used — nothing from a source enters the intent without his explicit
act and a citation. `/save` is the recommended door for saving: when
the save touches the engine's core or `projects/forge/`, it first
regenerates `README.md` and the Unreleased head of `RELEASE-NOTES.md`
from their recipes (the two renders run in parallel) and reports what
materially changed; then it runs the conformance check in scope —
`/check-forge` for core changes, `/check <slug>` for a project's —
settles the findings with the principal, proposes a commit message,
and only then runs the script. Plain conversation works too: the
commands are entry points into phases, not the only permitted door,
and the core rules apply in ordinary conversation.

### A typical journey

- You have an idea and write it down as it comes; the forge captures
  it verbatim as the brief of your project and locks it
  (`/new-project`), or you compose it with the forge first
  (`/forge brief`).
- You are interviewed until the intent says what you actually want,
  over several sessions and days; each round is written once, on your
  word (`/forge intent`).
- A vendor's offer and a standard you downloaded are stored beside the
  project and used only when you say so (`/ingest`); a topic you are
  unsure about gets researched (`/research`).
- You send in a peer to attack the thinking and an auditor to attack
  the documents; you rule on every challenge and finding, one at a
  time, and each verdict is recorded (`/challenge cto`, `/critique`).
- You want to pitch it to the group: you compose a presentation recipe
  through the genre interview, render the deck and generate the
  PowerPoint through your own template (`/recipe presentation`,
  `/render`, `scripts/md2pptx.ps1`).
- When the intent is right, you distil the assignment the recipients
  will get — complete, precise, self-contained (`/forge assignment`).
- You save as you go; every save re-renders your project's README and
  release notes, checks the project against the conventions and lets
  you settle what it finds before it commits (`/save`).

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
prefixes and the domain terms it actually uses, so it can be forwarded
without oral tradition; defined terms are capitalised in item text to
signal that they appear there.

**Language.** The forge dictates the output language: all artefacts
are written in English. The briefs are the exception, stored verbatim
in whatever language they were written. The language of the working
conversation is per-instance configuration and lives in
`CLAUDE.local.md`.

**Requirement style.** Items use *shall* / *shall not* — never would,
could, should, might, may, or MoSCoW wording. There is no priority
column and no priority tags: everything in an assignment is essential
by default, and an exception carries a note reading *optional* on that
item. Each item covers one idea, is written once, and is written in a
full, correct UK English sentence. Testability is recommended, not
required: assignments are deliberately high-level, and delegating
concretisation through a `DEL` item is a legitimate outcome — the
critic reports untestable wording as a recommendation, never as a
blocking defect. An item must not depend on an external link to be
understood, agreed or later tested. For illustration only:

> REQ.0010 The Platform shall record every request and every response
> passing through the Gateway, with the identity of the requesting
> User and the time.

**Completeness over brevity.** An assignment carries the full
in-scope substance of the intent, written as well and as precisely as
possible; nothing is omitted for brevity's sake, and length is
whatever fidelity requires. Leaving a matter out is legitimate only as
an explicit delegation — a DEL or TBC item. The boundary is the kind
of content, never its amount: an assignment assigns, it does not
solve; the machinery of executing delivery belongs to the recipients,
while any apparatus the principal judges part of setting direction
may appear.

**Versioning.** Integers denote signed-off versions, aligned with the
group BRD standard:

- `0.1, 0.2, …` drafts before first approval
- `1.0` approved
- `1.1, 1.2, …` changes made after approval, not yet approved
  themselves
- `2.0` the next approved version, incorporating all changes since 1.0

Front-matter carries `version`, `date` and `status`
(`draft | in_review | approved | superseded`), and status must agree
with the number: an integer version is `approved`, anything else is
not. Every versioned document opens with a Version History table
(Version | Modification | Author | Date) stating what changed and why.
Immutable artefacts — a locked brief, reviews, challenges, research —
are never edited: a brief from its lock, the others from creation;
corrections happen downstream.

**Project kinds and naming.** A project has a kind, declared in the
header of its ledger: `thought` — the chain — or `library`, a
collection of material shared across projects with no chain, only a
ledger, sources, research and a README that catalogues what it holds.
Slugs are lowercase and hyphenated on disk; display names may differ.
The engine's own project is `forge`; libraries carry the `lib-`
prefix (`lib-<name>`).

## 11. Repository layout

```
CLAUDE.md                  # the universal core — rules for the agent
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
  decisions.md  ledger.md             # ledger header carries kind:
  sources/00-INDEX.md                 # material index (rewritten):
                                      # What / Origin / Role / Use for
  sources/<name>.<ext>                # immutable external inputs, one
                                      # form each: <slug>.md extract of
                                      # a binary, or the binary itself
  sources/.gitignore                  # originals converted in place
  sources/<slug>/                     # bundle of related files = one
                                      # source, one ledger entry;
                                      # catalogued by its 00-INDEX.md
  research/00-INDEX.md                # material index (rewritten):
                                      # Question / Answer / Consult when
  recipes/<recipe>.md                 # render recipes: inputs, audience,
                                      # instructions, template — iterated
  renders/<recipe>.md                 # generated outputs, overwritten by
                                      # /render, provenance front-matter
  renders/<recipe>.pptx               # optional deck generated from the
                                      # md render by scripts/md2pptx.ps1
  reviews/YYYY-MM-DD-critique.md      # immutable critique runs
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

- git.
- PowerShell 7 (`pwsh`) — the scripts are PowerShell and run
  unchanged on Windows, macOS and Linux; on macOS and Linux it is one
  install.
- Python 3 — for markitdown, the document-to-Markdown engine behind
  `scripts/doc2md.ps1`.
- A paid Claude subscription — Claude Code draws on the same pool as
  Claude chat.

### Getting the forge and Claude Code

Clone this repository: it is the engine. Then install Claude Code —
on Windows `irm https://claude.ai/install.ps1 | iex`, on macOS or
Linux `curl -fsSL https://claude.ai/install.sh | bash`, or on any
platform `npm install -g @anthropic-ai/claude-code` — and sign in on
first run. Always start `claude` from the engine root, so that
`CLAUDE.md` and `CLAUDE.local.md` load.

Then run `/setup` once. It creates `CLAUDE.local.md` from its
template and fills it with you in a short interview — who the
principal is, the conversation language, your git identities per
host; the file is gitignored and never committed. It creates
`.claude/settings.local.json` with the session model set to Fable,
the strongest available model, which the whole forge including the
blind reviewers runs on; it tells you so in one sentence, and
`/model` or editing that file changes it at any time (permissions
come from the shared `.claude/settings.json`). It closes by offering
one global git guard — `user.useConfigOnly = true` appended to
`~/.gitconfig` — so that a repository without a local identity fails
aloud instead of committing with a default; declined, it prints the
line for you to apply by hand, and where your `~/.gitconfig` still
carries a global `user.name` or `user.email` it tells you the guard
only bites once that identity is removed. The identities themselves
are set per repository, proposed from your roster at every project
creation or import. `/setup` never overwrites existing files.

Upgrading the engine is `scripts/forge-pull.ps1` — a fast-forward of
`main`; the projects are untouched by it.

### Your projects

Each project is a directory under `projects/` and a git repository of
its own. `/new-project` creates the files; `git init` in that
directory, and a remote if you want one, are a one-off act of yours.
The commit identity belongs to the project: it is set locally in the
repository, proposed from the identity roster in `CLAUDE.local.md` by
the origin's host and confirmed by you, and `forge-save` commits
nothing in a repository where git resolves no identity — it reports
the command to set one instead. An existing project is brought in with
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
  from an interactive Claude Code session:
  `/plugin marketplace add anthropics/skills`, then
  `/plugin install document-skills@anthropic-agent-skills`. A deck
  template is named by path (`-Template <file.potx>`) — typically a
  document of a library project — or omitted, in which case Claude
  designs the visuals.
- The git scripts need nothing beyond git.

### Saving and syncing

`/save` is the recommended door. Before it commits, it regenerates
`README.md` and the Unreleased head of `RELEASE-NOTES.md` from their
recipes whenever the save touches the engine's core or
`projects/forge/` — unconditionally, the two renders launched in
parallel, reporting what materially changed — then runs the
conformance check routed by scope (`/check-forge` for the core,
`/check <slug>` per touched project) in an isolated subagent, settles
the findings with the principal, proposes a commit message, and only
then runs the script.

The scripts are the underlying mechanism and the only intended door
to git — reading state included, no exceptions. Three of them serve
the engine and every project repository: `forge-save.ps1` commits and
pushes — bare, every repository with changes, each its own commit;
with a slug, that one, `forge` meaning the engine; without an origin
the commit is kept and reported; remote changes are reconciled by
rebase — `forge-pull.ps1` fast-forwards from the remotes and never
touches a repository with unsaved changes, and `forge-status.ps1`
reports without changing anything. The fourth, `forge-clone.ps1`,
brings an existing project in. History is linear on `main`, one
remote per repository, and no URL is written anywhere in the forge —
git carries that itself. The engine receives a git tag at every
approved major of the forge intent. Saves made directly from the
shell are unaffected by the `/save` procedure.

## 13. Scripts

| Script | Purpose | When it runs | Install |
|---|---|---|---|
| `scripts/forge-save.ps1` | Commits and pushes: bare, every repository with changes, each its own commit; with a slug, that one (`forge` meaning the engine); reconciles remote changes by rebase; without an origin keeps the commit and reports; prints the commit's file summary. | At every save — through `/save` or directly from the shell. | git only. |
| `scripts/forge-pull.ps1` | Fast-forwards from the remotes and never touches a repository with unsaved changes; on the engine it is the upgrade channel. | To upgrade the engine or bring a project up to date. | git only. |
| `scripts/forge-status.ps1` | Reports unsaved changes, the last commit and the origin of each repository without changing anything. | Whenever state is read — `/save` determines its scope through it. | git only. |
| `scripts/forge-clone.ps1` | Clones an existing project into `projects/<repository name>`, never overwriting, and sets that repository's local commit identity only when given `-Name` and `-Email`. | Through `/import-project`. | git only. |
| `scripts/doc2md.ps1` | Converts a binary document into the Markdown extract that becomes the source. | By `/ingest`, on every binary the principal chooses to convert. | markitdown — see Setup. |
| `scripts/md2pptx.ps1` | Turns a Markdown deck render into a `.pptx` through headless Claude Code with the official pptx skill; a `.potx` template applies when named by path. | After a presentation is rendered, on request. | `document-skills` plugin — see Setup. |

## 14. Planned extensions

The chain is meant to keep growing downward: thoughts are forged as
far as the principal needs them taken. A BRD layer is certain to come;
solution architecture and integration are intended; a strategy layer
is possible if it proves to make sense. Which layers are added, and in
what order, is open, and nothing is approved for construction: the
mechanics of a layer — commands, agents, reviewer calibration — are
designed when that layer is actually taken up, not in advance.
Independent challengers on a different model family than the author's
are planned, so that a lens with genuinely different priors can be
sent in.

More principals means more instances: a second principal receives the
forge via git and runs an instance of their own. Genuine multi-user
operation is an open point for the future, deliberately not being
worked on now.

`projects/forge/` is Forge of Thought itself run through its own
process: its brief, its intent (design positions, open threads,
rejected directions), its decisions and its ledger. This README and
the release notes are renders of that project.

## 15. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) — petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit
the author and link to this repository.

## 16. About this README

This file is a render of the forge's own project: it is never edited
by hand, and `/render readme` regenerates it from its recipe
(`projects/forge/recipes/readme.md`) whenever the process changes —
every `/save` that touches the core does so. Fixes go into the recipe
or its inputs, `CLAUDE.md` and the forge intent. The YAML provenance
at the top is kept by design. Changes to the system are recorded in
`projects/forge/`.

_Last updated: 2026-09-02_
