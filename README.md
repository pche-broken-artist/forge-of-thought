---
project: forge
render: readme
generated: 2026-09-01
recipe: recipes/readme.md v0.28
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v3.6
---

# Forge of Thought 3.6

*A workshop where thought is tempered and shaped.* · [Release notes](RELEASE-NOTES.md)

Forge of Thought is an **AI cognitive extension** of a thinking
human, the **principal** — whoever's thinking is being forged. It
takes a raw, half-formed idea — a process redesign, a platform
initiative, an organisational change, a D&D campaign — and tempers
it into a precise, self-contained handover for whoever delivers it:
a team, a colleague, your future self. It rests on one principle —
**the machine carries every part of the work that is not deciding**
— in three forms.

- **It thinks with you.** It interviews and probes, criticises,
  challenges and inspires; it extracts what you have not yet
  articulated and lays out options with their trade-offs. It
  proposes — you decide.
- **It keeps the work consistent.** Nothing wanders off in
  forgotten chats: the thinking lives in versioned, templated
  artefacts, with decisions, state and history keeping themselves
  in order and consistency guarded across every output.
- **It carries the tedious work.** Audience-facing outputs — a
  pitch, a deck, even this README — are **renders**: generated from
  the artefacts through recipes, regenerated whenever the thinking
  moves, never written by hand twice.

Technically, Forge of Thought is a git repository: slash commands
and agent personas for Claude Code, templates, and the conventions
binding them. Today the chain of documents ends at the assignment.

## 1. Better with AI, or replaced by it?

Forge of Thought is for those who chose to be better. The failure
modes it exists to remove:

- thinking scattered across chat sessions that die, taking their
  context with them;
- handovers whose completeness depends on the mood of the day they
  were written;
- the same thinking retold to every audience — a pitch, a deck, a
  mail — each version rewritten by hand and drifting from the
  others;
- feedback and decisions with no place to land, so the same ground
  is fought over twice;
- assumptions nobody attacked before reality did.

## 2. What you get

- A versioned document chain growing from a **brief** — your own
  text, locked verbatim once it is done — to a self-contained
  **assignment**.
- An elicitation interview that forges the **intent** — the
  consolidated, current state of what you want and why.
- Two kinds of blind adversarial reviewers — one attacking the
  substance, one auditing the documents — with every verdict
  recorded.
- Audience-specific renders generated from recipes, including an
  actual PowerPoint file through your own template.
- External sources registered immutably and used only as the
  principal directs.
- Everything in files and git — nothing depends on a chat's memory.

## 3. Quickstart

**First, once per machine**

```
git clone …        # you are looking at it — this repository is the engine
# install Claude Code — see Setup below
claude             # always from the engine root
/setup             # first run only — fills CLAUDE.local.md, sets the model (Fable)
```

**Starting a new project**

```
/new-project my-idea
/forge intent
/save
```

**Bringing an existing project**

```
/import-project <project url>   # clones into projects/ — your git configuration supplies the identity
/forge my-idea                  # select the project before any work — the forge cannot guess it
```

Each project lives inside `projects/<slug>/` as a git repository of
its own, which the engine does not track — that is why you name it
first.

## 4. How it is used

### The flow

A thought arrives — a platform initiative half-formed on the way
home, or a campaign taking shape for your D&D table. You dump it
verbatim as a brief and lock it, or you compose it with the forge
(`/forge brief`) until it says what you mean; either way it becomes
the fixed record the later work is measured against.

From the brief the intent is forged. You sit in interviews
(`/forge intent`) where the forge asks rather than assumes,
reflects back what it heard, and consolidates your positions, open
threads and rejected directions into one living document. This runs
over days and sessions; everything lives in files, so a session can
end at any moment without loss.

Material arrives as it arrives. A downloaded security standard is
registered (`/ingest`) and sits untouched until you say "verify the
intent against it"; a meeting transcript is registered the same way
and never silently becomes your own position. For key topics
`/research` grounds the thinking in current practice instead of
invention.

When the thinking firms up, you send in the reviewers. A challenger
attacks the substance through a chosen lens; the critic audits the
documents. Both are blind to your conversations, nothing they say
blocks you, and every finding is walked through one by one — fixed,
overruled with a recorded reason, or left open.

Then the thinking travels. The assignment is distilled for its
recipients (`/forge assignment`). A pitch for the group is a render:
you compose its recipe — optionally guided by a genre interview
(`/recipe presentation`) — and regenerate the output whenever the
chain moves, up to an actual PowerPoint file. This very README is a
render. `/save` keeps it all in git.

### What it looks like in practice

A worked example from a real project will appear here once one is
published.

## 5. How the work feels

The forge is as much a way of working as a set of files, and these
are the named methods of that work — the vocabulary you and Claude
share.

- **Walkthrough.** Any list needing your decision — critique
  findings, challenges, open threads, the differences between two
  requirement sets — is worked one item at a time, in order of
  weight: Claude's recommendation with a one-sentence reason first,
  your verdict in a word or a counter-proposal, and "leave it open"
  always legitimate. Whatever produces a list ends by offering one,
  and verdicts are written once at the round's end.
- **Propose, never decide.** Claude criticises, challenges,
  inspires and lays out options; you compose.
- **Step by step.** Any action needing your consent — a write, a
  commit, a rename — arrives as one step with the exact operation
  and its reason, and runs on your word.
- **Elicitation interview.** Questions draw out what you have not
  yet articulated; gaps are never filled by assumption.
- **Draft early.** An early draft is an elicitation tool, not an
  output: concrete text sharpens your reaction.
- **Reflect back.** Before writing, Claude restates what it
  understood, so the write confirms rather than surprises.
- **Intent-first.** Substance changes go into the intent and
  propagate from there; only wording is fixed downstream directly.
- **Recommend, do not push.** Every option comes with a
  recommendation and its reason, stated once; a declined
  recommendation is not re-argued without new facts.

None of these is a command — you invoke any of them in a word.

## 6. Roles

| Role | What they own |
|---|---|
| Principal | The content: ideas, answers, decisions; final authority on everything published. |
| Claude | The machinery: structure, order, process discipline, document hygiene; criticism, challenge, inspiration and options. |

The standing rules of the pairing: when unsure, Claude asks — never
fills gaps by assumption; no new convention, prefix or section is
introduced unilaterally; many iterations are the normal mode; for
key topics current best practice is researched rather than
invented; everything Claude produces is advisory — nothing blocks,
and a missing section may be a deliberate delegation, not a defect;
artefacts are written once per iteration round, on the principal's
confirmation. One instance serves one principal — recipients
collaborate through the artefacts, and more principals means more
instances (see Planned extensions).

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

Adding a layer is one definition file declaring its inputs —
nothing is renumbered and nothing existing is reworked, which is
why the files are numbered in tens. The boundary between chain and
renders is authorship: a chain artefact is composed by the
principal, a render is generated from artefacts — an article you
write is a layer, its translation is a render.

| File | What it is |
|---|---|
| `00-brief.md` | The idea as you wrote it: an intent composed and then locked (draft → approved); later wholes as `00-brief-<name>.md`. |
| `10-intent.md` | The consolidated current state of your intent — rewritten freely, versioned. |
| `20-assignment.md` | The frozen, self-contained handover for the recipients. |
| `decisions.md` | Append-only DEC records. |
| `ledger.md` | The **ledger** — single source of truth for state. |

> **A locked brief is immutable** — composed, then locked, never
> touched again.

The **brief** is the principal's own text and the birthplace of one
whole of thinking. It is free-form — any structure you find useful:
prose, headings, tables, use cases — because it holds thoughts to
be processed, not decisions; only a minimal YAML header is
required. It is a draft while being composed and approved (1.0)
once you lock it, and three origins are equally legitimate: it
arrives finished and is locked on arrival, it is begun outside and
finished with Claude, or it is born in the forge — `/forge brief`
is the door for the latter two. A project may have more than one:
every later whole of thinking is born as `00-brief-<name>.md` under
the same rules. A locked brief is mined into the single intent —
positions cite it as provenance, the ledger's Briefs table tracks
how far each is mined (`pending | partial | mined | dropped`), and
a whole that dies on the way leaves the brief locked and one REJ
with the reason.

The **intent** (`10-intent.md`) is the working document and the
consolidated *current* state of what you want: positions you hold
(POS), open threads to elicit next (THR) and rejected directions
with the reason they were dropped (REJ), each with a stable ID. It
is rewritten for coherence every round rather than appended, with
changes recorded in its changelog, and its audience is the
principal and Claude only. It exists because chat context dies and
anything of value must live in a file: it is the document to read
when returning to a project after weeks, instead of excavating old
conversations.

The **assignment** (`20-assignment.md`) is distilled from the
intent for the recipients and is the one document they receive:
requirements, out-of-scope, constraints, assumptions, deliverables,
open questions with an owner and optional success criteria (REQ,
OOS, CON, ASM, DEL, TBC, SCR). It is complete and precise — it
carries the full in-scope substance of the intent — and it assigns
rather than solves, standing entirely on its own.

Substance changes go intent-first and propagate to the assignment;
only wording is fixed downstream directly. Artefacts are written
once per iteration round, on the principal's confirmation — one
version bump for the whole round. Feedback from recipients has no
channel of its own: the principal processes it and feeds
conclusions back through `/forge intent`.

> **A render is never edited by hand** — what is iterated is its
> **recipe**.

**Renders and recipes.** A render is an audience-specific output
generated from the chain — a pitch, an architecture picture, an
executive summary, this README. Its recipe
(`recipes/<recipe>.md`) holds the inputs (one artefact or several),
audience, instructions and the output template in one versioned
file; `/render <recipe>` regenerates the output, overwriting
freely, with history in git, and only `/save` or your explicit
`/render` ever regenerates one. Every render opens with YAML
front-matter provenance citing the recipe and each input with their
versions, and a render may itself serve as an input of another
render — a deck slide citing an architecture picture — when the
citing recipe declares it. Every project carries its own README
(and, for a thought project, release notes) as renders of its own
recipes, regenerated by every save that touches it.

**From Markdown to slides.** Everything the forge produces is
Markdown. Composing a recipe may be guided by genre
(`/recipe presentation`), and `scripts/md2pptx.ps1` turns a deck
render into an actual PowerPoint file through headless Claude Code
with the official pptx skill — a `.potx` template named by path,
typically a document of a library project, or none, in which case
Claude designs the visuals itself. The generated `.pptx` lands
beside its source render; the Markdown stays the source of truth,
and all other format conversion happens outside the forge.

## 8. Two isolated reviewers

Both reviewers run isolated, with clean contexts: they see the
artefacts only, never the working conversation — they cannot be
told what we really meant. That blindness is the source of their
value.

The **challengers** are a growing roster of persona lenses
attacking the substance of the thinking: unstated assumptions,
whether the stated objective is the real problem, second-order
effects, organisational reality, failure modes, the serious
counter-case.

The **critic** is the auditor of the documents and of the project's
consistency across artefacts: ambiguity, gaps, contradictions,
duplication, divergence between intent and assignment, regression
on past findings.

Isolation is not independence: both reviewers share the author's
model family, so what that family systematically cannot see, none
of them will find — their agreement is never treated as validation,
only as consistency under one set of priors, and the calibration
point lies outside the forge, in review by humans or by a different
model family.

### `/challenge <persona> [artefact]`

The target may be any chain artefact (default the intent); a layer
is best challenged before the next one is first derived from it.
Bare `/challenge` lists the roster and recommends a fit. The first
persona is `cto` — peer-CTO register: direct, few and sharp, no
flattery; further personas are created only by the principal's
decision, and only where their blind spots genuinely differ.
Challenges carry a severity (dealbreaker | major | minor) and an
epistemic status; fabrication is banned — uncertainty is stated,
not papered over. Output is CHL items in
`challenges/YYYY-MM-DD-challenge-<persona>.md`, with states open,
accepted, rejected (→ DEC), parked or obsolete — and an accepted
challenge must change the intent.

### `/critique`

The critic produces FND items in
`reviews/YYYY-MM-DD-critique.md`; each run is a delta report, and
every finding lands in one state:

- new
- verified resolved
- still open
- newly obsolete

Untestable wording is reported as a recommendation, never as a
blocking defect. Every finding is either fixed or explicitly
overruled with a recorded reason (a DEC); silently ignoring is not
an outcome.

## 9. Commands

Commands are the entry points into the process; each maps to one
job.

| Command | Purpose |
|---|---|
| `/setup` | First run after cloning the engine: creates and fills `CLAUDE.local.md` by interview and creates `.claude/settings.local.json` with the model set to Fable — a notice, not a question. Never overwrites, never touches git. |
| `/new-project <slug>` | Scaffold a project by kind — files only, never git: a thought project with its brief, or a library (`lib-`) of shared material. |
| `/import-project <git-url>` | Bring an existing project into `projects/` through `scripts/forge-clone.ps1` — the directory is the repository's name; your git configuration supplies the commit identity (offered from `CLAUDE.local.md` as a fallback). |
| `/forge [slug]` | The chain map: artefacts, versions, stale renders and a recommended next step. |
| `/forge <state> [slug]` | Work on the named artefact — the command is simply the name of what you want to work on (`brief [name]`, `intent`, `assignment`, …). |
| `/ingest [file] [slug]` | Store and register an external input in `sources/` and index it; bare, it sweeps `sources/` for unregistered files. |
| `/render <recipe> [slug]` | Regenerate a render from its recipe in `recipes/`. |
| `/recipe [genre] [slug]` | Bare, the genre roster; with a genre (`presentation`, `readme`, `release-notes`), guided composition or iteration of a render recipe. |
| `/critique [slug]` | Run the isolated critic — review file plus ledger. |
| `/challenge [persona] [artefact] [slug]` | Bare, the challenger roster; with a persona, challenge the substance of any chain artefact (default the intent). |
| `/research <topic> [slug]` | Best-practices research into `research/`, indexed. |
| `/ledger [slug]` | The quick state readout from the ledger. |
| `/check [slug]` | Conformance of project(s) against the current conventions; all but forge when bare. |
| `/check-forge` | Consistency check of the core and `projects/forge`. |
| `/save [slug] [-m "message"]` | Pre-save check, findings settled with the principal, then commit and push. |
| `/spinoff <project> <group> <slug>` | Split a requirement group into its own project — by the principal's explicit decision only. |

`/ingest` stores, registers and catalogues — nothing more. Every
binary file gets one question — convert to Markdown? — yes makes
the extract `sources/<slug>.md` the source, no keeps the binary as
the source (a template, a graphic); a set of related files lives as
one bundle with one ledger entry. Registration never implies
intake: a source's role is recorded in the material index, and its
content enters the intent only by your explicit act, with
provenance. `/save`, when it touches the core or `projects/forge/`,
first re-renders the README and the Unreleased head of the release
notes, then runs the conformance check routed by scope, settles the
findings with you, proposes a commit message and only then commits
and pushes. And commands are doors, not walls: plain conversation
works too, under the same rules.

### A typical journey

- You dump the idea into a brief — your own words, kept verbatim —
  and lock it (`/new-project`, `/forge brief`).
- Over days and sessions the intent is forged from it in
  interviews: positions firm up, open threads are worked, rejected
  directions keep their reasons (`/forge intent`).
- You invite pressure: a challenger attacks the thinking, the
  critic audits the documents, and you walk the findings one by
  one, every verdict yours (`/challenge cto`, `/critique`).
- You compose a presentation recipe and render the deck for your
  audience, up to the actual PowerPoint file
  (`/recipe presentation`, `/render`).
- The assignment is distilled — complete, precise, self-contained —
  and handed to its recipients (`/forge assignment`).
- You save as you go; every artefact and every verdict survives the
  session (`/save`).

## 10. Conventions

**IDs.** Format `PREFIX.NNNN`, all prefixes three letters. IDs are
global and stable — never renumbered; items may move between groups
without ID change. Items are numbered in tens, each new group
starting at the next hundred; groups are plain headings with no IDs
and no lifecycle, at most two levels deep.

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
prefixes and any domain terms it actually uses, so it can be
forwarded without oral tradition; defined Terms are capitalised in
item text to signal they appear there.

**Language.** The forge dictates the output language: all artefacts
are written in English, with one exception — the briefs, stored
verbatim in whatever language they were written. The conversation
language is per-instance configuration and lives in
`CLAUDE.local.md`.

**Requirement style.** Requirements use shall / shall not — never
would, could, should, might, may or MoSCoW wording. There are no
priorities: everything in an assignment is essential, and an
exception carries a note reading *optional*. Each item covers one
idea, is written once, in full, correct UK English sentences, and
must not depend on an external link to be understood, agreed or
later tested. Testability is recommended, not required —
delegating concretisation through a DEL item is legitimate. An
illustrative example:

> REQ.0010 The Platform shall record every request and every response passing through the Gateway, with the identity of the requesting User and the time.

**Completeness over brevity.** An assignment carries the full
in-scope substance of the intent, written as well and as precisely
as possible; nothing is omitted for brevity's sake, and length is
whatever fidelity requires — leaving a matter out is legitimate
only as an explicit delegation (a DEL or TBC item). The boundary is
the kind of content: an assignment assigns, it does not solve — the
machinery of executing delivery belongs to the recipients.

**Versioning.** Integers denote signed-off versions: `0.1, 0.2, …`
are drafts before first approval, `1.0` is approved, `1.1, 1.2, …`
are changes made after approval and not yet approved themselves,
`2.0` is the next approved version. Status
(`draft | in_review | approved | superseded`) must agree with the
number, and every versioned document opens with a Version History
table (Version | Modification | Author | Date).

**Project kinds and naming.** A project is of kind `thought` — the
chain — or `library`: shared material with no chain, only sources,
research and a ledger. Slugs are lowercase and hyphenated on disk —
the system's own project is `forge`, libraries carry the `lib-`
prefix — and display names may differ.

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

- git
- PowerShell 7 (`pwsh`) — the scripts are PowerShell; needed on
  macOS and Linux too
- Python 3 — for markitdown, the document-conversion engine
- a paid Claude subscription

### Getting the forge and Claude Code

Clone this repository — it is the engine. Then install Claude Code:

- Windows: `irm https://claude.ai/install.ps1 | iex`
- macOS/Linux: `curl -fsSL https://claude.ai/install.sh | bash`
- or `npm install -g @anthropic-ai/claude-code`

Sign in on first run — usage draws from the same pool as Claude
chat. Always start `claude` from the engine root, so that
`CLAUDE.md` and `CLAUDE.local.md` load. Then run `/setup` once: it
creates `CLAUDE.local.md` from its template and fills it with you
in a short interview — who the principal is, the conversation
language, your git identities per host — gitignored, never
committed; and it creates `.claude/settings.local.json` with the
session model set to Fable, the strongest available model, which
the whole forge including the blind reviewers runs on. It tells you
so in one sentence, and `/model` or editing that file changes it at
any time (permissions come from the shared `.claude/settings.json`).
`/setup` never overwrites existing files. Upgrading the engine is
`scripts/forge-pull.ps1` — a fast-forward of `main`; your projects
are untouched by it.

### Your projects

Each project is a directory under `projects/` and a git repository
of its own: `/new-project` creates the files, and `git init` in
that directory and a remote if you want one are a one-off act of
yours. The commit identity follows the host, resolved by your own
git configuration — per-host conditional includes recommended —
with a per-repository local identity as a legitimate override. An
existing project is brought in with `/import-project <git-url>`,
which clones it into `projects/<repository name>` through
`scripts/forge-clone.ps1`; the script reports which identity git
resolves for the fresh clone, and where none resolves, the matching
identity from `CLAUDE.local.md` is offered as the fallback. The
engine ignores `projects/*` (except its own `projects/forge`), and
the scripts find your project through its `.git`. A project without
a repository is reported as "not under git" — a fact, not an error.

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

`/save` is the recommended door. When the save touches the core or
`projects/forge/`, it first re-renders `README.md` and the
Unreleased head of `RELEASE-NOTES.md` from their recipes, then runs
the conformance check routed by scope, settles the findings with
the principal, and only then commits. Underneath sit the scripts —
the only intended door to git, reading state included, each serving
the engine and every project repository: a bare save commits each
repository with changes on its own and pushes where it has a
remote. History is linear on `main`, one remote per repository, and
no URL lives anywhere in the forge — git carries that itself.

## 13. Scripts

| Script | What it does | When it runs |
|---|---|---|
| `forge-save.ps1` | Commits and pushes — bare, every repository with changes, each its own commit; with a slug, that one (`forge` meaning the engine); reconciles remote changes by rebase and prints the commit's file summary. | At every save, normally through `/save`. |
| `forge-pull.ps1` | Fast-forwards from the remotes, never touching a repository with unsaved changes; on the engine it is the upgrade channel. | When syncing a machine or upgrading the engine. |
| `forge-status.ps1` | Reports unsaved changes, the last commit and the origin of each repository, changing nothing. | Whenever state is read. |
| `forge-clone.ps1` | Clones an existing project into `projects/<repository name>`, never overwriting, reporting the commit identity git resolves; sets a local identity only when given one. | Through `/import-project`. |
| `doc2md.ps1` | Converts a binary document to a Markdown extract (engine: markitdown — install note in Setup). | Through `/ingest`, on binaries the principal chooses to convert. |
| `md2pptx.ps1` | Turns a Markdown deck render into a `.pptx` through headless Claude Code with the official pptx skill (install note in Setup). | After rendering a deck, when the actual file is wanted. |

## 14. Planned extensions

The chain grows downward: a BRD layer is certain to come, solution
architecture and integration are intended, and a strategy layer is
possible if it proves to make sense. Which layers are added, and in
what order, is open; the mechanics of a layer are designed when it
is taken up, never in advance.

One instance serves one principal. A second principal receives the
forge via git and runs an instance of their own; genuine multi-user
operation is an open point for the future, deliberately not being
worked on now.

Forge of Thought is its own first project: `projects/forge/`
carries the system's brief, intent, decisions and ledger — the
forge run through its own process.

## 15. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) — petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely;
credit the author and link to this repository.

## 16. About this README

This file is a render: it is never edited by hand and is
regenerated by `/render readme` whenever the process changes — and
by every `/save` touching the core. Fixes go into the recipe
(`projects/forge/recipes/readme.md`) or its inputs, and changes to
the system itself are recorded in `projects/forge/`. The YAML
front-matter provenance at the top is kept by design.

_Last updated: 2026-09-01_
