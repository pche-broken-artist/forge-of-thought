---
render_of: projects/forge/recipes/readme.md (v0.31)
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md (v3.8)
generated: 2026-09-02
---

# Forge of Thought 3.8

*A workshop where thought is tempered and shaped.* · [Release notes](RELEASE-NOTES.md)

Forge of Thought is an **AI cognitive extension** of a thinking human — the **principal**, whoever's thinking is being forged. It takes a raw, half-formed idea — a process redesign, a platform initiative, an organisational change, a D&D campaign — and tempers it into a precise, self-contained handover for whoever delivers it: a team, a colleague, your future self. It rests on one principle — **the machine carries every part of the work that is not deciding** — in three forms.

- **It thinks with you.** It interviews and probes, criticises, challenges, inspires; it extracts what the principal has not yet articulated and lays out options with their trade-offs. It proposes — you decide.
- **It keeps the work consistent.** Nothing wanders off in forgotten chats: the thinking lives in versioned, templated artefacts, with decisions, state and history keeping themselves in order and consistency guarded across every output.
- **It carries the tedious work.** Audience-facing outputs — a pitch, a deck, even this README — are **renders**: generated from the artefacts through recipes, regenerated whenever the thinking moves, never written by hand twice.

Technically, the forge is a git repository: slash commands and agent personas for Claude Code, templates, and the conventions binding them. The document chain currently ends at the assignment — the frozen, self-contained direction handed to the recipients — and is built to grow downward, layer by layer, without reworking anything that exists.

## 1. Better with AI, or replaced by it?

Forge of Thought is for those who chose to be better. The failure modes it exists to remove:

- Thinking scattered across chat sessions that die, taking their context with them.
- Handovers whose completeness depends on the mood of the day they were written.
- The same thinking retold to every audience — a pitch, a deck, a mail — each version rewritten by hand and drifting from the others.
- Feedback and decisions with no place to land, so the same ground is fought over twice.
- Assumptions nobody attacked before reality did.

## 2. What you get

- A versioned document chain growing from a **brief** — your own text, locked verbatim once it is done — to a self-contained **assignment**.
- An elicitation interview that forges the **intent**: what you want, why, what is open, what was rejected.
- Two kinds of blind adversarial reviewers — one attacking the substance of your thinking, one auditing the documents — with every verdict recorded.
- Audience-specific renders generated from recipes, including an actual PowerPoint file through your own template.
- External sources — transcripts, offers, standards — registered immutably and used only as the principal directs.
- Everything in files and git — nothing depends on a chat's memory.

## 3. Quickstart

First, once per machine:

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
/import-project <project url> # clones into projects/ — the commit identity is proposed from your CLAUDE.local.md roster and confirmed by you
/forge <project-slug>         # the slug is the repository's name; select the project before any work — the forge cannot guess it
```

Each project lives inside `projects/<slug>/` as a git repository of its own, which the engine does not track — that is why you name it first.

## 4. How it is used

### The flow

A thought arrives — a platform initiative, a reorganisation, a campaign taking shape for your D&D table. You dump it exactly as it is in your head into a brief: alone, or in conversation with the forge (`/forge brief`), which clarifies where you are terse but never adds content of its own. When the thought is whole, you lock it, and from that moment it is the untouchable record of where this all began.

Then the real work: the forge interviews you (`/forge intent`) and the intent takes shape — your positions, your open threads, the directions you rejected and why. It is rewritten for coherence round after round, over days and sessions if that is what it takes, and because everything lives in files, you can close the laptop mid-thought and pick up weeks later exactly where you stood.

Material arrives when it arrives. You download a security standard and drop it in (`/ingest`); it sits registered and untouched until the day you say "verify the intent against it". Where a topic deserves grounding, `/research` fetches current best practice and files the findings.

At the moments you choose, you send in the reviewers. A challenger persona attacks the substance — the assumptions you did not state, the problem behind your stated objective; the critic audits the documents for ambiguity, gaps and drift. Nothing they say blocks you: you walk their findings one by one and rule on each.

When the direction is settled, the assignment is distilled — the one document the recipients receive. And whenever an audience needs its own view, you compose a recipe (a genre interview can guide you — `/recipe presentation`) and render it: a pitch for the group, slides including the actual PowerPoint file, a summary, this very README. When the thinking moves, the renders are regenerated — never rewritten by hand.

Along the way, `/save` keeps everything in git: checked for conformance first, committed and pushed after.

### What it looks like in practice

A worked example from a real project will appear here once one is published.

## 5. How the work feels

The forge is as much a way of working as a set of files, and these are the named methods of that work — the vocabulary you and Claude share.

- **Walkthrough.** Any list needing your decision — findings, challenges, open threads, differences between two requirement sets — is worked one item at a time, in order of weight: Claude's recommendation with a one-sentence reason first, your verdict in a word or a counter-proposal, "leave it open" always legitimate. Never a table asking for every verdict at once; everything is written once at the round's end.
- **Propose, never decide.** Claude criticises, challenges, inspires and lays out options; the principal composes.
- **Step by step.** Anything hard to reverse — a write, a commit, a rename — arrives as one step with the exact operation and reason stated, and runs on your word; a plan you have seen is not consent for its steps.
- **Elicitation interview.** Questions draw out what you have not yet articulated; gaps are never filled by assumption.
- **Draft early.** An early draft is an elicitation tool, not an output: concrete text sharpens your reaction.
- **Reflect back.** Before writing, Claude restates what it understood, so the write confirms rather than surprises.
- **Intent-first.** Substance changes go into the intent and propagate from there; only wording is fixed downstream directly.
- **Recommend, do not push.** Every option comes with a recommendation and reason, stated once; a declined recommendation is not re-argued without new facts.

None of these is a command — you invoke any of them in a word.

## 6. Roles

| Role | What they own |
|---|---|
| **Principal** | Whoever's thinking is being forged. Supplies ideas, answers and decisions; final authority on all content. |
| **Claude** | Cognitive extension of the principal. Owns structure, order, process discipline and document hygiene; criticises, challenges, inspires and lays out options; proposes, never decides. |

The standing rules: when unsure, ask — never fill gaps by assumption; never introduce a new convention unilaterally; many iterations are the normal mode; research before inventing; everything is advisory, never blocking — only the principal publishes; artefacts are written once per iteration round, on confirmation. One instance serves one principal, and recipients collaborate through the artefacts; more principals means more instances (see Planned extensions).

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

**Blue = chain artefacts (light = not built yet), green = renders; dashed arrows = growth that does not exist yet.**

Adding a layer is one definition file declaring its inputs — nothing is renumbered and nothing existing is reworked, which is why files are numbered in tens. The boundary between chain and render is authorship: a chain artefact is composed by the principal, a render is generated from artefacts — the article and its translation in the diagram illustrate it.

| File | What it is |
|---|---|
| `00-brief.md` | The idea as the principal wrote it — draft until locked, then verbatim; later wholes as `00-brief-<name>.md`. |
| `10-intent.md` | The working understanding — rewritten freely for coherence, versioned. |
| `20-assignment.md` | Frozen high-level direction for the recipients — versioned, the only document handed over. |
| `decisions.md` | Append-only DEC records. |
| `ledger.md` | Single source of truth for state. |

> A locked brief is immutable — composed, then locked, never touched again.

A **brief** is an intent that is composed and then locked. It is free-form — any structure the principal finds useful: prose, headings, tables, use cases — with no required content and no IDs, because it holds thoughts to be processed, not decisions: they may be changed, reworked or dropped when mined. It is `draft` while being composed and `approved` (1.0) once locked, and three origins are equally legitimate and indistinguishable to the forge: it arrives finished and is locked on arrival, it is begun outside and finished with Claude, or it is born in the forge — `/forge brief [name]` is the door for the latter two. A project may have more than one: every later whole of thinking that would otherwise land in the intent as a batch of unproven positions is born as `00-brief-<name>.md` under the same rules. A locked brief is mined into the single intent — positions cite it as provenance, a whole that dies on the way leaves the brief locked and one REJ with the reason — and the ledger tracks each brief's mining state (`pending | partial | mined | dropped`). Each locked brief is the provenance anchor and drift measure of its whole.

The **intent** (`10-intent.md`) is the consolidated *current* state of the principal's thinking — positions held (POS), open threads (THR) and rejected directions with the reason they were dropped (REJ), each with a stable ID. It exists because chat context dies and anything of value must live in a file: it is the document to read when returning after weeks, instead of excavating old conversations. Its audience is the principal and Claude only, and it is rewritten for coherence every round rather than appended, with the changes recorded in its changelog.

The **assignment** (`20-assignment.md`) is distilled from the intent for the recipients — teams, colleagues, or the principal's future self — and is the one document they receive: requirements, out-of-scope items, constraints, assumptions, deliverables, open questions with an owner, optional success criteria (REQ, OOS, CON, ASM, DEL, TBC, SCR). It carries the full in-scope substance of the intent, written as precisely as fidelity requires — complete and precise, assigning rather than solving, and self-contained: nothing in it depends on an external link to be understood.

Iteration goes intent-first: substance changes land in the intent and propagate to the assignment, while wording-only fixes may edit the assignment directly. Writes happen once per iteration round, on the principal's confirmation — one version bump and one Version History row for the whole round. Feedback from recipients has no channel of its own: the principal processes it and feeds conclusions back through `/forge intent`.

> A render is never edited by hand — what is iterated is its recipe.

**Renders and recipes.** A render is an audience-specific output generated from the chain — a pitch, an architecture picture, an executive summary, this README. The iterated thing is its **recipe** (`recipes/<recipe>.md`): inputs, audience, instructions and the output template in one versioned file. `/render <recipe>` regenerates the output into `renders/<recipe>.md` — or the recipe's own `output:` path — overwriting freely, history in git; generation runs in an isolated subagent that sees only the recipe and its inputs. Every render opens with YAML front-matter provenance citing the recipe and each input with their versions, and a render may serve as an input of another render when the citing recipe declares it. A render assigns nothing and is not part of the chain: the artefacts stay the source of truth. Every project has a README as a render of its own recipe and, if it is a thought project, release notes likewise; every save that touches the project regenerates them.

**From Markdown to slides.** Everything the forge produces is Markdown, renders included — a presentation is a `.md` saying what is on each slide. Composing a recipe may be guided by genre (`/recipe presentation`). The one in-house conversion is `scripts/md2pptx.ps1`: it turns a Markdown deck render into an actual PowerPoint file, applying a `.potx` template when one is named by path — typically a document of a library project — and designing the visuals itself when none is. The generated `.pptx` lands beside its source render; the Markdown stays the source of truth. All other format conversion happens outside the forge.

## 8. Two isolated reviewers

Both reviewers run as isolated subagents with clean contexts: they see the artefacts only, never the working conversation. They cannot be told what we really meant — if the documents do not say it, it is not there. That blindness is the source of their value.

The **challengers** are a growing roster of persona lenses attacking the substance of the thinking: unstated assumptions, whether the objective is the real problem, second-order effects, organisational reality, failure modes, the counter-case.

The **critic** is the auditor of the documents and of the project's consistency across artefacts: ambiguity, gaps, contradictions, duplication, divergence between intent and assignment, regression on past findings.

Isolation is not independence: the two reviewers share the author's model family, so what that family systematically cannot see, none of them will find — their agreement is never validation, only consistency under one set of priors. The calibration point lies outside the forge: review by humans or by a different model family, invited at the principal's discretion.

### /challenge

`/challenge <persona> [artefact]` runs one isolated agent per persona, each a distinct lens; the first is `cto` (peer-CTO register: direct, few and sharp, no flattery), and further personas are created only by the principal's decision, only where their blind spots genuinely differ. The target may be any chain artefact (default the intent); a layer is best challenged before the next one is first derived from it. Bare `/challenge` lists the roster and recommends a fit. Challenges carry a severity (dealbreaker | major | minor) and an epistemic status, and fabrication is banned — uncertainty is stated, not papered over. Results land as CHL items in `challenges/` with states `open`, `accepted`, `rejected` (with a DEC recording the reason), `parked`, `obsolete`. An accepted challenge must change the intent.

### /critique

`/critique` produces FND findings in an immutable review file in `reviews/`, each run a delta report against the last. Finding states:

- new
- verified resolved
- still open
- newly obsolete

Every finding is either fixed or explicitly overruled with a recorded reason (a DEC); silently ignoring is not an outcome. A missing section may be a deliberate delegation, not a defect — the critic informs, the principal decides. Both reviewers end by offering a walkthrough of their findings.

## 9. Commands

Commands are entry points, not the only door — the same rules apply in ordinary conversation.

| Command | Purpose |
|---|---|
| `/setup` | First run after cloning the engine: fills `CLAUDE.local.md` by interview, sets the session model to Fable, and offers one global git guard. Never overwrites, runs no git operation. |
| `/new-project <slug>` | Scaffold a project by kind — files only, never git: a thought project with its brief, or a library of shared material. |
| `/import-project <git-url>` | Bring an existing project into `projects/` by cloning it through `scripts/forge-clone.ps1`; the directory is the repository's name. |
| `/forge [slug]` | The chain map: artefacts, versions, stale renders, and a recommended next step. |
| `/forge <state> [slug]` | Iterate the target artefact (`brief [name]`, `intent`, `assignment`, …). |
| `/ingest [file] [slug]` | Store and register external input in `sources/` and index it; bare, it sweeps `sources/` for unregistered files. |
| `/render <recipe> [slug]` | Regenerate a render from its recipe in `recipes/`. |
| `/recipe [genre] [slug]` | Bare, the genre roster; with a genre (`presentation`, `readme`, `release-notes`), guided composition or iteration of a render recipe. |
| `/critique [slug]` | Run the isolated critic on the project's documents. |
| `/challenge [persona] [artefact] [slug]` | Bare, the challenger roster; with a persona, run that challenger against the substance of any chain artefact (default the intent). |
| `/research <topic> [slug]` | Best-practices research; durable notes stored in `research/` and indexed. |
| `/ledger [slug]` | The quick state readout from the ledger. |
| `/check [slug]` | Conformance of project(s) against the current conventions; all but forge when bare. |
| `/check-forge` | Consistency check of the engine core and `projects/forge` against each other. |
| `/save [slug] [-m "message"]` | Pre-save check, findings settled with the principal, then commit and push. |
| `/spinoff <project> <group> <slug>` | Split a requirement group into its own project — only by the principal's explicit decision. |

The star mechanics of `/forge <state>` are plain: the command is simply the name of the artefact you want to work on, one definition file per state declaring its inputs — so a new layer is a new file, nothing more. `/ingest` stores, registers and catalogues — nothing else: registration does not imply intake, each source's role is individual, and content enters the intent only by the principal's explicit act, with provenance; at ingest, every binary file gets one question — convert to Markdown? — making either the extract or the functional binary the source. `/save` first re-renders the README and release-notes head when the save touches the engine core or `projects/forge/`, then runs the relevant conformance check, settles findings with the principal, proposes a commit message and only then runs the script.

### A typical journey

- You write down the idea exactly as it is in your head and lock it as the brief of your project (`/new-project`, `/forge brief`).
- Over the following days the forge interviews you and your intent takes shape — positions, open threads, rejected directions — rewritten each round (`/forge intent`).
- You send in a challenger to attack the thinking and the critic to audit the documents, then walk their findings one by one, ruling on each (`/challenge cto`, `/critique`).
- The group wants to hear about it, so you compose a presentation recipe and render it — including the actual PowerPoint through your own template (`/recipe presentation`, `/render`).
- When the direction is settled, the assignment is distilled: complete, precise, self-contained — the one document your recipients receive (`/forge assignment`).
- All along you save as you go; every save checks conformance first and re-renders what the change made stale (`/save`).

## 10. Conventions

**IDs.** Format `PREFIX.NNNN`, all prefixes three letters. IDs are global and stable — never renumbered; items may move between groups without ID change. Items are numbered in tens, each new group starting at the next hundred; groups are plain headings with no IDs and no lifecycle, depth capped at two levels.

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

**Terms.** Every assignment carries a Terms section listing the prefixes and domain terms it uses, so it can be forwarded without oral tradition; defined terms are capitalised in item text.

**Language.** The forge dictates the output language: all artefacts are written in English — the briefs are the exception, stored verbatim in whatever language they were written. The conversation language is per-instance configuration; it lives in `CLAUDE.local.md`.

**Requirement style.** Requirements use **shall** / **shall not** — no would, could, should, might, may, no MoSCoW wording. No priority column and no priority tags: everything in an assignment is essential by default, an exception is marked *optional* on the item. Each item covers one idea, is written once, in full, correct UK English sentences, and must not depend on an external link to be understood, agreed or later tested. Testability is recommended, not required — delegating concretisation through a DEL item is legitimate, and the critic reports untestable wording as a recommendation, never a blocking defect. An illustrative item:

> REQ.0010 The Platform shall record every request and every response passing through the Gateway, with the identity of the requesting User and the time.

**Completeness over brevity.** An assignment carries the full in-scope substance of the intent, written as well and as precisely as possible; length is whatever fidelity requires, and leaving a matter out is legitimate only as an explicit delegation (a DEL or TBC item). The boundary is one of kind: an assignment assigns, it does not solve — the machinery of executing delivery belongs to the recipients.

**Versioning.** Integers denote signed-off versions: drafts run `0.1, 0.2, …`; `1.0` is approved; `1.1, 1.2, …` are changes after approval, not yet approved themselves; `2.0` is the next approved version. Front-matter carries `version`, `date` and `status` (`draft | in_review | approved | superseded`), and status must agree with the number. Every versioned document opens with a Version History table stating what changed and why. Reviews, challenges and research notes are immutable from creation; corrections happen downstream.

**Project kinds and naming.** A project is of kind `thought` — the chain — or `library` (`lib-` prefix): shared material with no chain, only a ledger, sources and research, its README a catalogue of what it holds. Slugs are lowercase and hyphenated on disk (the engine's own project is `forge`); display names may differ.

## 11. Repository layout

```
CLAUDE.md                  # universal core — the rules
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

- git
- PowerShell 7 (`pwsh`) — the scripts are PowerShell, needed on macOS/Linux too
- Python 3 (for markitdown)
- A paid Claude subscription

### Getting the forge and Claude Code

Clone this repository — it is the engine. Then install Claude Code:

- Windows: `irm https://claude.ai/install.ps1 | iex`
- macOS/Linux: `curl -fsSL https://claude.ai/install.sh | bash`
- or `npm install -g @anthropic-ai/claude-code`

Sign in on first run — usage draws from the same pool as Claude chat. Always start `claude` from the engine root, so that `CLAUDE.md` and `CLAUDE.local.md` load.

Then run `/setup` once. It creates `CLAUDE.local.md` from its template and fills it with you in a short interview — who the principal is, the conversation language, your git identities per host — gitignored, never committed. It creates `.claude/settings.local.json` with the session model set to Fable, the strongest available model, which the whole forge including the blind reviewers runs on; it tells you so in one sentence, and `/model` or editing that file changes it at any time (permissions come from the shared `.claude/settings.json`). It closes by offering one global git guard — `user.useConfigOnly = true` appended to `~/.gitconfig` — so a repository without a local identity fails aloud instead of committing with a default; declined, it prints the line for you to apply by hand. The identities themselves are set per repository, proposed from your roster at every project creation or import. `/setup` never overwrites existing files.

Upgrading the engine is `scripts/forge-pull.ps1` — a fast-forward of `main`; your projects are untouched by it.

### Your projects

Each project is a directory under `projects/` and a git repository of its own. `/new-project` creates the files; `git init` in that directory and a remote if wanted are a one-off act of yours. The commit identity belongs to the project: it is set locally in the repository, proposed from the identity roster in `CLAUDE.local.md` by the origin's host and confirmed by you. An existing project is brought in with `/import-project <git-url>`, which clones it into `projects/<repository name>` through `scripts/forge-clone.ps1`, sets the identity you confirm and reports the identity the clone ended up with. The engine ignores `projects/*` (except its own `projects/forge`) and the scripts find your project through its `.git`. A project without a repository is reported as "not under git" — a fact, not an error.

### Script prerequisites

- `doc2md.ps1` needs markitdown: `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.
- `md2pptx.ps1` needs the `document-skills` plugin, installed once from an interactive Claude Code session: `/plugin marketplace add anthropics/skills`, then `/plugin install document-skills@anthropic-agent-skills`. A deck template is named by path (`-Template <file.potx>`) — typically a document of a library project — or none, in which case Claude designs the visuals.
- The git scripts need nothing beyond git.

### Saving and syncing

The recommended door for saving is `/save`: when the save touches the engine core or `projects/forge/`, it first re-renders `README.md` and the Unreleased head of `RELEASE-NOTES.md` from their recipes, then runs the conformance check routed by scope, settles the findings with the principal, and only then commits. Underneath, the four scripts are the mechanism — and the only intended door to git, reading state included: `forge-save.ps1`, `forge-pull.ps1`, `forge-status.ps1` and `forge-clone.ps1`, each serving the engine and every project repository. A bare save commits each repository with changes on its own and pushes where it has a remote; history is linear on `main`, one remote per repository, and no URL lives anywhere in the forge — git carries that itself.

## 13. Scripts

| Script | Purpose | When it runs | Install note |
|---|---|---|---|
| `forge-save.ps1` | Commits and pushes — bare, every repository with changes, each its own commit; with a slug, that one (`forge` meaning the engine); reconciles remote changes by rebase and prints the commit's file summary. | Every save, usually through `/save`. | Nothing beyond git. |
| `forge-pull.ps1` | Fast-forwards from the remotes, never touching a repository with unsaved changes; on the engine it is the upgrade channel. | When syncing or upgrading. | Nothing beyond git. |
| `forge-status.ps1` | Reports unsaved changes, the last commit and the origin of each repository without changing anything. | Whenever state is read. | Nothing beyond git. |
| `forge-clone.ps1` | Clones an existing project into `projects/<repository name>`, never overwriting, setting the repository's local commit identity when given `-Name` and `-Email`. | When bringing a project in, through `/import-project`. | Nothing beyond git. |
| `doc2md.ps1` | Converts a binary document to a Markdown extract — the only conversion path for source extracts. | At `/ingest`, for each binary the principal chooses to convert. | markitdown — see Setup. |
| `md2pptx.ps1` | Turns a Markdown deck render into a `.pptx` through headless Claude Code, with a `.potx` template named by path or Claude-designed visuals. | After rendering a presentation, when the actual file is wanted. | `document-skills` plugin — see Setup. |

## 14. Planned extensions

The chain is built to grow downward: a BRD layer is certain to come, solution architecture and integration are intended, a strategy layer is possible. Which layers are added, and in what order, is open — the mechanics of a layer are designed when it is actually taken up, not in advance.

Multi-principal use stays simple by design: one instance serves one principal, and a second principal receives the forge via git and runs their own instance; genuine multi-user operation is deliberately not being worked on now.

The system is its own subject: `projects/forge/` runs Forge of Thought through its own process — its brief, intent, decisions and ledger — and a process change is complete only once that intent is updated and this README re-rendered.

## 15. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) — petr.chlumsky@gmail.com. Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit the author and link to this repository.

## 16. About this README

This file is a render of `projects/forge`: never edited by hand, regenerated by `/render readme` whenever the process changes (and by every `/save` touching the engine core). Fixes go into the recipe (`projects/forge/recipes/readme.md`) or its inputs; system changes are recorded in `projects/forge/`. The YAML front-matter provenance at the top is kept by design.

_Last updated: 2026-09-02_
