---
project: forge
render: readme
generated: 2026-09-03
recipe: recipes/readme.md v0.33
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v3.19
---

# Forge of Thought 3.19

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

Technically, Forge of Thought is a git repository: slash commands and
agent personas for Claude Code, templates, and the conventions that
bind them. Today the chain of documents ends at the assignment.

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
- An elicitation interview that forges the intent: what you want, why,
  what is open, what you rejected and why.
- Two kinds of blind adversarial reviewers — one on the substance of
  the thinking, one on the quality of the documents — with every
  verdict recorded.
- Audience-specific renders generated from recipes, including an
  actual PowerPoint file through your own template.
- External sources registered immutably and used only as you direct.
- Everything in files and git — nothing depends on a chat's memory.

## 3. Quickstart

**First, once per machine**

```
git clone <this repository>   # you are looking at it
# install Claude Code — see Setup
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

A thought arrives — a platform you want built, a process that needs
redesigning, a campaign taking shape for your D&D table. You dump it
as it is, in whatever language and shape it comes, alone or in
conversation with the forge (`/forge brief`), and lock it. That text
is your brief, and it never changes again.

From the brief the forge interviews you (`/forge intent`) — one
question at a time, drawing out what you have not yet said — and
writes the intent: what you want, why, what is still open, what you
have already rejected and why. You iterate it over days and sessions;
everything lives in files, so a session can end at any point without
loss and you pick up where you left off.

Along the way material arrives: a downloaded security standard you
will later verify the intent against, a meeting transcript, an offer.
You register it (`/ingest`) and it sits immutably in `sources/` until
you decide how it is used; where a topic deserves grounding,
`/research` stores what current practice says. When the intent feels
solid, you send in the blind reviewers: a challenger presses on the
thinking (`/challenge cto`), a critic on the documents
(`/critique clarity`, `/critique essence`) — and you decide, item by
item, what to accept. Nothing blocks you.

Then you distil the assignment (`/forge assignment`) — the one
document the recipients receive — and the audience-facing outputs: a
pitch for the group is a render, generated from a recipe you compose
(guided by a genre interview if you like, `/recipe presentation`) and
regenerated whenever the chain moves; a deck render becomes an actual
PowerPoint file. Even this README is one. Throughout, `/save` keeps it
all in git.

### What it looks like in practice

A worked example from a real project will appear here once one is
published.

## 5. How the work feels

The forge is as much a way of working as a set of files, and these
are the named methods of that work — the vocabulary you and Claude
share.

- **Walkthrough.** Any list needing your decision — critique
  findings, challenges, open threads, differences between two
  requirement sets — is worked one item per message, in order of
  weight: Claude's recommendation with a one-sentence reason first,
  your verdict in a word or a counter-proposal, "leave it open" a
  legitimate answer. Verdicts are carried in the conversation and
  written once at the round's end; whatever produces a list ends by
  offering a walkthrough.
- **Propose, never decide.** Claude criticises, challenges, inspires
  and lays out options; you compose.
- **Step by step.** Anything needing your consent — a write, a
  commit, a push, a rename — arrives as one step with the exact
  operation, its target and the reason, and runs on your word; a plan
  you have seen is not consent for its steps.
- **Elicitation interview.** Claude draws out by questions what you
  have not yet articulated, one question per message, never filling
  gaps by assumption.
- **Draft early.** An early draft is an elicitation tool, not an
  output: concrete text sharpens your reaction.
- **Reflect back.** Before writing, Claude restates what it
  understood, so the write confirms rather than surprises.
- **Intent-first.** Substance changes go into the intent and
  propagate from there; only wording is fixed downstream directly.
- **Recommend, do not push.** Every option comes with a
  recommendation and reason, stated once; a declined recommendation
  is not re-argued without new facts.

None is a command: you invoke any of them in a word.

## 6. Roles

| Role | What they own |
|---|---|
| **Principal** | Whoever's thinking is being forged: supplies ideas, answers and decisions, and is the final authority on all content. |
| **Claude** | The principal's cognitive extension: structure, order, process discipline and document hygiene; criticises, challenges, inspires and lays out options — proposes, never decides. |

Standing rules for Claude: when unsure, ask — never fill gaps by
assumption; never introduce a new convention, prefix or section
unilaterally; research before inventing; advise, never block — only
the principal publishes, and a missing section may be a deliberate
delegation rather than a defect; structure over prose; write once per
iteration round, on confirmation; and one mechanism lives in one
place — whatever the forge has a procedure for is used through its
own definition, never re-described.

One instance serves one principal; recipients collaborate through the
artefacts, and more principals means more instances (see Planned
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
is renumbered and nothing existing is reworked, which is why files are
numbered in tens. The boundary between chain and render is
authorship: a chain artefact is composed by the principal, a render is
generated from artefacts — the article and its translation in the
diagram illustrate it.

| File | What it is |
|---|---|
| `00-brief.md` | The idea as the principal wrote it — draft until locked, then verbatim and never edited. |
| `00-brief-<name>.md` | A later whole of thinking, born under the same rules as the first brief. |
| `10-intent.md` | The working understanding — rewritten freely, versioned; audience principal and Claude. |
| `20-assignment.md` | The frozen high-level direction for the recipients — versioned, the only document handed over. |
| `decisions.md` | Append-only DEC records, including overruled findings and rejected challenges. |
| `ledger.md` | The single source of truth for state. |
| `sources/`, `research/` | Immutable external inputs and research notes, each directory catalogued by its `00-INDEX.md`. |
| `reviews/`, `challenges/` | Immutable, dated reports of the two reviewers. |
| `recipes/`, `renders/` | Iterated render recipes and the outputs generated from them. |

> A locked brief is immutable — composed, then locked, never touched
> again.

The **brief** is an intent that is composed and then locked. It is the
principal's own text, free-form: any structure he finds useful —
prose, headings, tables, use cases — with no required content and no
IDs, only a minimal YAML header. It holds thoughts to be processed,
not decisions, so they may be changed, reworked or dropped when mined.
It is `draft` while being composed and `approved` (1.0) once locked.
Three origins are equally legitimate and indistinguishable to the
forge: it arrives finished and is locked on arrival; it is begun
outside and finished with Claude; it is born in the forge —
`/forge brief [name]` is the door for the latter two. A project may
have more than one: every later whole of thinking that would otherwise
land in the intent as a batch of unproven positions is born as
`00-brief-<name>.md`. A locked brief is mined into the single intent —
positions cite it as provenance, a whole that dies on the way leaves
one REJ with the reason — and the ledger tracks how far each is mined
(`pending | partial | mined | dropped`).

The **intent** is the consolidated *current* state of what the
principal wants: positions he holds (POS), open threads still to
elicit (THR) and rejected directions with the reason they were dropped
(REJ), each with a stable ID. It is rewritten for coherence every
round rather than appended to, with a changelog recording what changed
and why, and its audience is the principal and Claude only. It exists
because chat context dies and anything of value must live in a file:
it is the document to read when returning to a project after weeks,
instead of excavating old conversations.

The **assignment** is distilled from the intent for the recipients and
is the one document they receive: requirements, out-of-scope items,
constraints, assumptions, deliverables, open questions with an owner
and optional success criteria (REQ, OOS, CON, ASM, DEL, TBC, SCR). It
is complete and precise — it carries the full in-scope substance of
the intent, assigning rather than solving — and self-contained.

Substance changes go intent-first and then propagate to the
assignment; only wording-only fixes may edit the assignment directly.
Artefacts are written once per iteration round, on the principal's
confirmation — one version bump and one Version History row for the
whole round.

External inputs — transcripts, offers, documents, standards — live in
`sources/`, immutable once registered, and may arrive at any stage,
even before the brief. Registration does not imply intake: a source's
role is individual, and the principal alone directs how and when each
is used; when source content enters the intent, it is his explicit
act, cited with provenance. Feedback from recipients has no channel of
its own: the principal processes it and feeds conclusions back through
`/forge intent`.

> A render is never edited by hand — what is iterated is its recipe.

**Renders and recipes.** A render is an audience-specific output
generated from the chain — a pitch, an architecture picture, an
executive summary, the repository README. Its **recipe**
(`recipes/<recipe>.md`) carries inputs, audience, instructions and
the output template in one versioned file; `/render <recipe>`
regenerates the output into `renders/<recipe>.md` — or the recipe's
optional `output:` path — overwriting freely, with history in git.
Generation runs in an isolated subagent that sees only the recipe and
its inputs. Every render opens with YAML front-matter provenance
citing the recipe and each input with their versions, and a render may
serve as an input of another render when the recipe declares it. A
render assigns nothing and is not part of the chain: the artefacts
stay the source of truth.

**From Markdown to slides.** Everything is Markdown, content only.
Composing a recipe may be guided by genre (`/recipe presentation`,
`/recipe readme`, `/recipe release-notes`). The one in-house
conversion is `scripts/md2pptx.ps1`: it turns a Markdown deck render
into an actual PowerPoint file through headless Claude Code with the
official pptx skill — a model does the conversion, because deck
definitions are free-form and may carry instructions for it. A
`.potx` template is applied when named by path (`-Template <path>`),
typically a document of a library project; without one, Claude
designs the visuals itself. The generated `.pptx` lands beside its
source render and is tracked like any render output; the Markdown
render stays the source of truth. All other format conversion happens
outside the forge.

## 8. Two isolated reviewers

The reviewers run as isolated subagents that see the artefacts only,
never the working conversation: they cannot be told what we really
meant. That blindness is the source of their value. Both run on the
session model — speed is bought with context, never with a weaker
reviewer.

The **challengers** are a growing roster of persona lenses attacking
the substance of the thinking: unstated assumptions, whether the
objective is the real problem, second-order effects, organisational
reality, failure modes, the counter-case.

The **critic** is a roster of lenses on the documents: `clarity` reads
each artefact on its own; `essence` reads the chain for drift by
distilling each layer's essence blind and comparing it with the layer
above. The two reviewers are one shape — personas and lenses, one
agent file each, the shared behaviour carried verbatim from one
skeleton — with strictly separate outputs: challenges (CHL) in
`challenges/`, findings (FND) in `reviews/`. Both are invoked by hand,
both reports are immutable and dated, both are settled by walkthrough.

Isolation is not independence. The author, the critic and the
challengers share one model family; what that family systematically
cannot see, none of them will find, so agreement between the
reviewers is never treated as validation — it only means the artefact
is consistent under one set of priors. The calibration point lies
outside the forge: review by humans or by a different model family,
invited at the principal's discretion; challengers on a different
model family are planned.

### `/challenge [persona] [artefact]`

Bare `/challenge` lists the roster and recommends a fit; the first
persona is `cto` — peer-CTO register, direct, few and sharp, no
flattery. With an artefact named as `/forge` names it (`brief`,
`brief-<name>`, `intent`, `assignment`, later layers) the challenge
narrows to that artefact; without one it takes the whole chain, each
challenge naming the artefact it concerns. A layer is best challenged
before the next one is first derived from it. Challenges carry a
severity (dealbreaker | major | minor) and an epistemic status;
fabrication is banned — uncertainty is stated, not papered over. The
report is `challenges/YYYY-MM-DD-challenge-<persona>.md`. Challenge
states: open, accepted, rejected (a DEC with its reason), parked,
obsolete. An accepted challenge must change the intent. New personas
only by the principal's decision, and only where their blind spots
genuinely differ.

### `/critique [lens] [artefact]`

Bare `/critique` lists the lenses and recommends a fit. `clarity`
reads one artefact (or each artefact when none is named) on its own:
ambiguity, internal contradiction, duplication, scope hygiene,
Requirement style, the advisory checklist. `essence` reads the named
artefact against its parent (or every adjacent pair of the chain):
substance lost without a trace, added without provenance, or shifted
in meaning — a finding is a difference of essences, not of texts, and
the report carries both distillations. Regression against resolved
findings is every lens's first step. The report is
`reviews/YYYY-MM-DD-critique-<lens>.md`. Finding states:

- open
- resolved — an iteration of the artefact concerned
- overruled — a DEC with its reason
- obsolete — the passage no longer exists

## 9. Commands

Commands are entry points into phases; the core rules apply in
ordinary conversation too.

| Command | Purpose |
|---|---|
| `/setup` | First run after cloning the engine: fills `CLAUDE.local.md` by interview, sets the session model to Fable, offers the global git identity guard. Never overwrites, runs no git operation. |
| `/new-project <slug>` | Scaffolds a project by kind — a thought project with its brief, or a library (`lib-`). Files only, never git. |
| `/import-project <git-url>` | Brings an existing project into `projects/` through `scripts/forge-clone.ps1`; the commit identity is proposed from `CLAUDE.local.md` by the URL's host. |
| `/forge [slug]` | The chain map: artefacts, versions, stale renders and a recommended next step. |
| `/forge <state> [slug]` | Iterates the named artefact (`brief [name]`, `intent`, `assignment`, …). |
| `/ingest [file] [slug]` | Stores and registers external input in `sources/` and indexes it; bare, sweeps `sources/`. |
| `/render <recipe> [slug]` | Regenerates a render from its recipe. |
| `/recipe [genre] [slug]` | Bare, the genre roster; with a genre (`presentation`, `readme`, `release-notes`), guided composition or iteration of a recipe. |
| `/critique [lens] [artefact] [slug]` | Bare, the lens roster; with a lens, runs the critic on one artefact (`clarity`) or one artefact against its parent (`essence`), else on all. |
| `/challenge [persona] [artefact] [slug]` | Bare, the persona roster; with a persona, runs that challenger against the named artefact, else the whole chain. |
| `/research <topic> [slug]` | Best-practices research into `research/`, indexed. |
| `/ledger [slug]` | The quick state readout from the ledger. |
| `/check [slug]` | Conformance of project(s) against the current conventions; all but forge when bare. |
| `/check-forge` | Consistency check of the core and `projects/forge`. |
| `/save [slug] [-m "message"]` | Pre-save check, findings settled with the principal, then commit and push. |
| `/spinoff <project> <group> <slug>` | Splits a requirement group into its own project — by the principal's explicit decision only. |

`/forge <state>` is simply the name of the artefact you want to work
on: one definition file per state declares its inputs, so the chain
is a star, not a line, and knowing the target is knowing the command.
`/forge` shows the map with a recommended next step; `/ledger` reads
the state back from the ledger. `/ingest` stores, registers and
catalogues — nothing more: every binary file gets one question,
convert to Markdown?, and yes makes the extract (`scripts/doc2md.ps1`)
the source while no keeps the binary as it is; a set of related files
lives as one bundle with its own index; a source's role is noted as
free text in the directory's `00-INDEX.md`. `/save`, when it touches
the core or `projects/forge/`, first re-renders `README.md` and the
Unreleased head of `RELEASE-NOTES.md` from their recipes and reports
what materially changed; it then runs the relevant conformance check
in an isolated subagent, settles the findings with the principal,
proposes a commit message and only then runs the script — bare, for
every repository with changes, each its own commit.

### A typical journey

- You dump your idea into your project's brief and lock it
  (`/new-project`, `/forge brief`).
- Over several sessions the forge interviews you and rewrites the
  intent until it holds what you actually want (`/forge intent`).
- You register the documents that inform the work as they arrive and
  let research ground the key topics (`/ingest`, `/research`).
- You send in a challenger and the critic, then walk through their
  challenges and findings one at a time, recording every verdict
  (`/challenge cto`, `/critique clarity`, `/critique essence`).
- You compose a presentation recipe through the genre interview and
  render the deck, PowerPoint included (`/recipe presentation`,
  `/render`, `scripts/md2pptx.ps1`).
- You distil the assignment and hand it over — the one document the
  recipients receive (`/forge assignment`).
- You save as you go; every save regenerates your project's README
  and release notes (`/save`).

## 10. Conventions

**IDs.** Format `PREFIX.NNNN`, three-letter prefixes. IDs are global
and stable — never renumbered; items may move between groups without
an ID change. Items are numbered in tens (`REQ.0010, REQ.0020`), each
new group starting at the next hundred (`REQ.0100, REQ.0110`);
overflow takes the next free number anywhere. Groups are plain
headings with no IDs, no metadata and no lifecycle; depth is at most
two levels.

| Prefix | Meaning | Lives in |
|---|---|---|
| REQ | requirement | assignment |
| OOS | out of scope / do-not | assignment |
| CON | constraint — deliberate boundary, not to be challenged | assignment |
| ASM | assumption | assignment |
| DEL | deliverable — may delegate work | assignment |
| TBC | open question / to be confirmed, with owner | assignment |
| SCR | success criterion — optional or delegated | assignment |
| POS | position the principal currently holds | intent |
| THR | open thread — unresolved matter to elicit next | intent |
| REJ | rejected direction, with the reason it was dropped | intent |
| FND | critique finding (document quality) | ledger, reviews |
| CHL | peer-review challenge (substance) | ledger, challenges |
| DEC | decision, incl. overruled findings and rejected challenges | decisions.md |

**Terms.** Defined terms are capitalised in item text to signal that
they appear in the assignment's Terms section, so the document can be
forwarded without oral tradition.

**Language.** The forge dictates the output language: all artefacts
are written in English. The briefs are the exception, stored verbatim
in whatever language they were written. The conversation language is
per-instance configuration and lives in `CLAUDE.local.md`.

**Requirement style.** Items use *shall* / *shall not* — never would,
could, should, might, may, or MoSCoW wording. There is no priority
column and no priority tags: everything in an assignment is essential
by default, and an exception carries a note reading *optional*. Each
item covers one idea, is written once, in a full, correct UK English
sentence, and must not depend on an external link to be understood,
agreed or tested. Testability is recommended, not required: delegating
concretisation through a DEL item is a legitimate outcome. Illustrative
example:

> REQ.0010 The Platform shall record every request and every response
> passing through the Gateway, with the identity of the requesting
> User and the time.

**Completeness over brevity.** An assignment carries the full in-scope
substance of the intent, written as well and as precisely as
possible; nothing is omitted for brevity's sake, and length is
whatever fidelity requires. Leaving a matter out is legitimate only as
an explicit delegation (a DEL or TBC item). An assignment assigns, it
does not solve: the machinery of executing delivery belongs to the
recipients.

**Versioning.** Integers denote signed-off versions: `0.1, 0.2, …`
drafts before first approval; `1.0` approved; `1.1, 1.2, …` changes
after approval, not yet approved themselves; `2.0` the next approved
version. Front-matter carries `version`, `date` and `status`
(`draft | in_review | approved | superseded`); an integer version is
`approved`, anything else is not. Every versioned document opens with
a Version History table (Version | Modification | Author | Date).
Immutable artefacts — a locked brief, reviews, challenges, research —
are never edited; corrections happen downstream.

**Project kinds and naming.** A project has a kind, declared in its
ledger header: `thought` — the chain — or `library` — material shared
across projects, no chain: only the ledger, sources and research with
their indexes, and a README as a catalogue of what it holds.
Project slugs are lowercase and hyphenated on disk; libraries carry the
`lib-` prefix; the system's own project is `forge`.

## 11. Repository layout

```
CLAUDE.md                  # universal core — the agent's instructions
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

- git.
- PowerShell 7 (`pwsh`) — the scripts are PowerShell and are needed
  on macOS and Linux too.
- Python 3 — for markitdown, the engine behind `doc2md.ps1`.
- A paid Claude subscription.

### Getting the forge and Claude Code

Clone this repository — it is the engine. Install Claude Code:

- Windows: `irm https://claude.ai/install.ps1 | iex`
- macOS/Linux: `curl -fsSL https://claude.ai/install.sh | bash`
- or `npm install -g @anthropic-ai/claude-code`

Sign in on first run — usage draws from the same pool as Claude chat.
Always start `claude` from the engine root so that `CLAUDE.md` and
`CLAUDE.local.md` load.

Then run `/setup` once. It creates `CLAUDE.local.md` from its template
and fills it with you in a short interview — who the principal is,
the conversation language, your git identities per host — gitignored,
never committed. It creates `.claude/settings.local.json` with the
session model set to Fable, the strongest available model, which the
whole forge including the blind reviewers runs on; it tells you so in
one sentence, and `/model` or editing that file changes it at any
time (permissions come from the shared `.claude/settings.json`). It
closes by offering one global git guard — `user.useConfigOnly = true`
appended to `~/.gitconfig` — so that a repository without a local
identity fails aloud instead of committing with a default; declined,
it prints the line for you to apply by hand. The identities themselves
are set per repository, proposed from your roster at every project
creation or import. `/setup` never overwrites existing files.

Upgrading the engine is `scripts/forge-pull.ps1` — a fast-forward of
`main`; the projects are untouched by it.

### Your projects

Each project is a directory under `projects/` and a git repository of
its own. `/new-project` creates the files; `git init` in that directory
and a remote, if wanted, are a one-off act of yours. The commit
identity belongs to the project: it is set locally in the repository,
proposed from the identity roster in `CLAUDE.local.md` by the origin's
host and confirmed by you. An existing project is brought in with
`/import-project <git-url>`, which clones it into
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
  from an interactive Claude Code session:
  `/plugin marketplace add anthropics/skills`, then
  `/plugin install document-skills@anthropic-agent-skills`. A deck
  template is named by path (`-Template <file.potx>`) — typically a
  document of a library project — or none, in which case Claude
  designs the visuals.
- The git scripts need nothing beyond git.

### Saving and syncing

`/save` is the recommended door. When the save touches the core or
`projects/forge/`, it first re-renders `README.md` and the Unreleased
head of `RELEASE-NOTES.md`; it then runs the conformance check routed
by scope (`/check-forge` for the core, `/check <slug>` per touched
project), settles the findings with the principal, and only then
commits. Underneath, four scripts are the only intended door to git —
reading state included, no exceptions — each serving the engine and
every project repository: `forge-save.ps1` commits and pushes (bare,
every repository with changes, each its own commit; with a slug, that
one, `forge` meaning the engine; without a remote the commit is kept
and reported; remote changes reconciled by rebase), `forge-pull.ps1`
fast-forwards from the remotes and never touches a repository with
unsaved changes, `forge-status.ps1` reports unsaved changes, the last
commit and the origin of each without changing anything, and
`forge-clone.ps1` brings an existing project in. Linear history on
`main`, one remote per repository, no URL anywhere in the forge.

## 13. Scripts

| Script | Purpose | When it runs | Install |
|---|---|---|---|
| `scripts/forge-save.ps1` | Commits and pushes the engine and every project repository with changes, each its own commit. | At every `/save`, or directly from the shell. | Needs git only. |
| `scripts/forge-pull.ps1` | Fast-forwards the engine and the projects from their remotes, never touching a repository with unsaved changes. | To upgrade the engine or sync a project. | Needs git only. |
| `scripts/forge-status.ps1` | Reports unsaved changes, the last commit and the origin of each repository without changing anything. | Whenever the state of the repositories is needed, including by `/save`. | Needs git only. |
| `scripts/forge-clone.ps1` | Clones an existing project into `projects/<repository name>`, never overwriting, setting its local commit identity when given `-Name` and `-Email`. | At `/import-project`. | Needs git only. |
| `scripts/doc2md.ps1` | Converts a binary document to a Markdown extract that becomes the source. | At `/ingest`, on every binary the principal chooses to convert. | markitdown — see Setup. |
| `scripts/md2pptx.ps1` | Turns a Markdown deck render into a `.pptx` through headless Claude Code with the official pptx skill, applying a `.potx` template named by path. | After rendering a deck, on request. | `document-skills` plugin — see Setup. |

## 14. Planned extensions

The chain is meant to grow downward: a BRD layer is certain to come,
solution architecture and integration are intended, a strategy layer
is possible if it proves to make sense. Which layers are added, and in
what order, is open; the mechanics of a layer — commands, agents,
reviewer calibration — are designed when that layer is actually taken
up, never in advance, and nothing that exists is reworked when one is
added.

One instance serves one principal today. A second principal receives
the forge via git and runs their own instance; genuine multi-user
operation is an open point for the future, deliberately not being
worked on now.

`projects/forge/` is Forge of Thought itself run through its own
process: its brief, intent, decisions and ledger. A process change is
complete only once that intent is updated and this README re-rendered.

## 15. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) — petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit
the author and link to this repository.

## 16. About this README

This file is a render of `projects/forge`: it is never edited by hand
and is regenerated by `/render readme` whenever the process changes,
and by every `/save` touching the core. Fixes go into its recipe
(`projects/forge/recipes/readme.md`) or its inputs (`CLAUDE.md` and
the forge intent). The YAML front-matter provenance at the top is
kept by design. Changes to the system itself are recorded in
`projects/forge/`.

_Last updated: 2026-09-03_
