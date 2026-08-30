---
project: forge
render: readme
generated: 2026-08-30
recipe: projects/forge/recipes/readme.md v0.26
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v3.4
---

# Forge of Thought 3.4

*A workshop where thought is tempered and shaped.* · [Release notes](RELEASE-NOTES.md)

Forge of Thought is an **AI cognitive extension** of a thinking human,
the **principal** — whoever's thinking is being forged. It takes a
raw, half-formed idea — a process redesign, a platform initiative, an
organisational change, a D&D campaign — and tempers it into a precise,
self-contained handover for whoever delivers it: a team, a colleague,
your future self. It rests on one principle — **the machine carries
every part of the work that is not deciding** — in three forms.

- **It thinks with you.** It interviews and probes, criticises,
  challenges, inspires; it extracts what you have not yet articulated
  and lays out options with their trade-offs. It proposes — you
  decide.
- **It keeps the work consistent.** Nothing wanders off in forgotten
  chats: the thinking lives in versioned, templated artefacts, with
  decisions, state and history keeping themselves in order and
  consistency guarded across every output.
- **It carries the tedious work.** Audience-facing outputs — a pitch,
  a deck, even this README — are **renders**: generated from the
  artefacts through recipes, regenerated whenever the thinking moves,
  never written by hand twice.

Technically, the forge is a git repository: slash commands and agent
personas for Claude Code, templates, and the conventions binding them.
Today the chain of documents ends at the assignment; it is built to
grow downward toward realisation without reworking anything that
exists.

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
- An elicitation interview that forges the intent.
- Two kinds of blind adversarial reviewers, every verdict recorded.
- Audience-specific renders generated from recipes, including an
  actual PowerPoint file through your own template.
- External sources registered immutably and used only as you direct.
- Everything in files and git — nothing depends on a chat's memory.

## 3. Quickstart

```
git clone <this repository>
cp templates/CLAUDE.local.md CLAUDE.local.md   # fill in the two lines
# install Claude Code (see Setup)
claude                                         # from the engine root
/new-project <slug>
/forge intent
/save
```

Each project lives inside `projects/<slug>/` as a git repository of
its own, which the engine does not track.

## 4. How it is used

### The flow

A thought arrives — a process you want redesigned, a platform you
want built, a campaign taking shape for your D&D table. You dump it
as it is: a page written alone at the kitchen table, or a few lines
finished in conversation with the forge (`/forge brief`). Once it
says what you mean, you lock it, and from that moment it is never
touched again.

Then the interview begins. `/forge intent` asks what you actually
want, why, what you are unsure about and what you have already
rejected, and keeps a consolidated picture of it in a working
document that is rewritten every round rather than appended to. This
takes days and sessions, not one sitting, and nothing depends on a
chat surviving — everything lives in files.

Along the way material accumulates. A transcript of the meeting where
the topic came up, an offer from a vendor, a security standard you
downloaded and later want the intent verified against — each is
registered as it arrives (`/ingest`) and stays untouched; you decide
when and how each one is used. Where a key topic deserves grounding,
`/research` looks up current practice and files what it found.

When the picture holds, you let two blind reviewers at it. One
attacks the thinking itself — is this the real problem, what happens
in the second order, what does the organisation actually do with it
(`/challenge cto`). The other audits the documents — ambiguity, gaps,
contradictions (`/critique`). Neither has seen your conversation, so
neither can be talked round. You walk through their findings one at a
time; nothing blocks you, every verdict is written down.

From the intent you distil the assignment (`/forge assignment`) — the
one document the recipients receive, complete and self-contained. And
because the same thinking has to reach other audiences, you write
recipes rather than documents: a pitch for the group as a render, a
deck for the board as another, the actual PowerPoint generated from
it. Composing a recipe can be guided by a genre interview
(`/recipe presentation`). When the intent moves, `/render` regenerates
each output — this README is one of them. `/save` keeps it all in git,
one commit at a time.

### What it looks like in practice

A worked example from a real project will appear here once one is
published.

## 5. How the work feels

The forge is as much a way of working as a set of files, and these
are the named methods of that work — the vocabulary you and Claude
share.

- **Walkthrough.** Any list needing your decision — findings,
  challenges, open threads — is worked one item at a time in order of
  weight: Claude's recommendation with a one-sentence reason first,
  an "accept" carrying the concrete text the artefact would receive,
  then your verdict in a word or a counter-proposal. Verdicts are
  carried in the conversation and written once at the round's end,
  never asked for in a table all at once.
- **Propose, never decide.** Claude criticises, challenges, inspires
  and lays out options; you compose.
- **Step by step.** Anything needing your consent — a write, a commit,
  a push, a rename — arrives as one step with the exact operation and
  its reason, and runs on your word; a plan you have seen is not
  consent for its steps.
- **Elicitation interview.** Claude draws out by questions what you
  have not yet articulated, and never fills a gap by assumption.
- **Draft early.** An early draft is an elicitation tool, not an
  output: concrete text sharpens your reaction.
- **Reflect back.** Before writing, Claude restates what it
  understood, so the write confirms rather than surprises.
- **Intent-first.** Substance changes go into the intent and propagate
  from there; only wording is fixed downstream directly.
- **Recommend, do not push.** Every option comes with a recommendation
  and a reason, stated once; a declined recommendation is not
  re-argued without new facts.

None is a command: you invoke any of them in a word.

## 6. Roles

| Role | What they own |
|---|---|
| **Principal** | Whoever's thinking is being forged: supplies ideas, answers and decisions; final authority on all content. |
| **Claude** | Cognitive extension of the principal: structure, order, process discipline and document hygiene; criticises, challenges, inspires, lays out options; proposes, never decides. |

Standing rules: when unsure, Claude asks rather than assumes; it
never introduces a new convention, prefix or section without your
decision; many iterations are the normal mode; it researches before
inventing; critiques and checklists advise and never block — only the
principal publishes, and a missing section may be a deliberate
delegation rather than a defect; it writes once per iteration round,
on your confirmation. One instance serves one principal; the
recipients collaborate through the artefacts, and more principals
means more instances (see Planned extensions).

## 7. The document chain

```
00-brief.md (draft → locked)
      │
      ▼
10-intent.md ──────────────▶ renders/  (pitch, deck, summary …)
      │
      ▼
20-assignment.md ──────────▶ renders/
      │
      ▼
later layers (30-brd.md, 40-solution-design.md, …)
```

| File | What it is |
|---|---|
| `00-brief.md` | The idea as you wrote it — draft until locked, then verbatim and never edited; later wholes as `00-brief-<name>.md`. |
| `10-intent.md` | Our working understanding — rewritten freely for coherence, versioned. |
| `20-assignment.md` | Frozen high-level direction for the recipients — versioned, self-contained. |
| `decisions.md` | Append-only DEC records. |
| `ledger.md` | Single source of truth for state. |

> A locked brief is immutable — composed, then locked, never touched
> again.

The **brief** is an intent that is composed and then locked. It is
free-form: any structure you find useful — prose, headings, tables,
use cases — with no required content and no IDs, and only a minimal
YAML header. Its content is thoughts to be processed, not decisions,
so it may be changed, reworked or dropped when mined. It is `draft`
while being composed and `approved` (1.0) once you lock it. Three
origins are equally legitimate and indistinguishable to the forge: it
arrives finished and is locked on arrival; it is begun outside and
finished with Claude; it is born in the forge — `/forge brief [name]`
is the door for the latter two. A project may have more than one:
every later whole of thinking that would otherwise land in the intent
as a batch of unproven positions is born as `00-brief-<name>.md`
under the same rules. A locked brief is mined into the single intent
— positions cite it as provenance; a whole that dies on the way
leaves the brief locked and one REJ with the reason — and the
ledger's Briefs table tracks each brief's mining state (`pending |
partial | mined | dropped`).

The **intent** exists because the brief is raw and the assignment is
frozen: something in between has to hold the consolidated *current*
state of what you want, why, what is open and what was rejected. It
holds positions (POS), open threads (THR) and rejected directions
with their reason (REJ), each with a stable ID, and is rewritten for
coherence every round rather than appended to, with a changelog. Its
audience is you and Claude only.

The **assignment** is distilled from the intent for the recipients
and is the one document they receive. It holds requirements,
out-of-scope items, constraints, assumptions, deliverables, open
questions with an owner and optional success criteria (REQ, OOS, CON,
ASM, DEL, TBC, SCR). It is complete and precise, assigning rather
than solving, and self-contained.

Iteration rule: substance changes go intent-first and propagate to
the assignment; wording-only fixes may edit the assignment directly.
Write cadence: a working round is written once, on your
confirmation — one version bump, one Version History row for the
whole round. Feedback from the recipients has no channel of its own:
you process it and feed conclusions back through `/forge intent`.

> A render is never edited by hand — what is iterated is its recipe.

**Renders and recipes.** A render is an audience-specific output
generated from the chain — a pitch for the group, an architecture
picture, an executive summary, the repository README. What you
iterate is its **recipe** (`recipes/<recipe>.md`: inputs, audience,
instructions and the output template in one versioned file; more than
one input is legitimate), and `/render <recipe>` regenerates the
output into `renders/<recipe>.md` — or the recipe's own `output:`
path — overwriting freely, history in git. Generation runs in an
isolated subagent that sees only the recipe and its inputs. Every
render opens with YAML front-matter provenance citing the recipe and
each input with their versions, and a render may cite another render
as a picture source when the recipe declares it among its inputs. A
render assigns nothing and is not part of the chain. Every project
has a README as a render of its own `recipes/readme.md` and, if it is
a thought project, release notes from `recipes/release-notes.md`;
every `/save` that touches the project regenerates them.

**From Markdown to slides.** Everything is Markdown, content only.
Composing a recipe may be guided by genre (`/recipe presentation`).
The one in-house conversion is `scripts/md2pptx.ps1`: it turns a
Markdown deck render into an actual PowerPoint file through headless
Claude Code with the official pptx skill — an LLM conversion by
design, because deck definitions are free-form and may carry
instructions for the model. A `.potx` template is applied when named
by path — typically a document of a library project; without it,
Claude designs the visuals itself. The generated `.pptx` lands beside
its source render and is tracked in git like any render output; the
Markdown stays the source of truth. All other format conversion
happens outside the forge.

## 8. Two isolated reviewers

Both reviewers run in a clean context: they see the artefacts and
nothing else, so they cannot be told what we really meant. If a
document only works with the conversation behind it, they will say
so.

The **challengers** are a growing roster of persona lenses, one
isolated agent per persona, attacking the substance of the thinking:
unstated assumptions, whether the objective is the real problem,
second-order effects, organisational reality, failure modes, the
counter-case.

The **critic** is the auditor of the documents and of the project's
consistency across artefacts: ambiguity, gaps, contradictions,
duplication, divergence between intent and assignment, regression on
past findings.

Isolation is not independence. The author, the critic and the
challengers share one model family; what that family systematically
cannot see, none of them will find, and agreement between the
reviewers is therefore never treated as validation — it only means
the artefact is consistent under one set of priors. The calibration
point lies outside the forge: review by humans or by a different
model family, invited at the principal's discretion.

Both run on the session model — the whole forge runs on one model;
speed is bought with context, never with a weaker reviewer. Their
jobs are strictly separate; neither does the other's.

### `/challenge <persona> [artefact]`

The target may be any chain artefact (default the intent); a layer is
best challenged before the next one is first derived from it. The
first persona is `cto` — peer-CTO register: direct, few and sharp, no
flattery. Further personas are created only by your decision, and
only where their blind spots genuinely differ. Bare `/challenge`
lists the roster and recommends a fit. Challenges carry a severity
(dealbreaker, major, minor) and an epistemic status; fabrication is
banned — uncertainty is stated, not papered over. Output is CHL items
in `challenges/YYYY-MM-DD-challenge-<persona>.md`, immutable once
written. Challenge states: `open`, `accepted`, `rejected` (with a
DEC), `parked`, `obsolete`. An accepted challenge must change the
intent.

### `/critique`

Produces FND items in `reviews/YYYY-MM-DD-critique.md`, immutable
once written, and records them in the ledger. Untestable wording is
reported as a recommendation, never as a blocking defect. Each
finding ends in one of these states:

- open
- fixed — an iteration of the artefact concerned
- overruled — a DEC record with the reason

Whatever produces a list ends by offering a walkthrough.

## 9. Commands

Commands are the doors to the forge; plain conversation works too.

| Command | Purpose |
|---|---|
| `/new-project <slug>` | Scaffold a project by kind — files only, never git: a thought project with its brief captured verbatim, or a library (`lib-`) of shared material. |
| `/forge [slug]` | The chain map: artefacts, versions, stale renders, possible next steps with a recommendation. |
| `/forge <state> [slug]` | Iterate the named artefact — `brief [name]`, `intent`, `assignment`, … |
| `/ingest [file] [slug]` | Store, register and index an external input in `sources/`; bare, sweep `sources/` for unregistered files. |
| `/render <recipe> [slug]` | Regenerate a render from its recipe in `recipes/`. |
| `/recipe [genre] [slug]` | Bare, the genre roster; with a genre (`presentation`, `readme`, `release-notes`), guided composition or iteration of a recipe. |
| `/critique [slug]` | Run the isolated critic — review plus ledger. |
| `/challenge [persona] [artefact] [slug]` | Bare, the persona roster; with a persona, run that challenger against any chain artefact (default the intent). |
| `/research <topic> [slug]` | Best-practices research into `research/`, indexed. |
| `/ledger [slug]` | The quick state readout from the ledger. |
| `/check [slug]` | Conformance of project(s) against current conventions; all but forge when bare. |
| `/check-forge` | Consistency check of the core and `projects/forge`. |
| `/save [slug] [-m "message"]` | Pre-save check, findings settled with you, then commit and push. |
| `/spinoff <project> <group> <slug>` | Split a requirement group into its own project — your explicit decision only. |

`/forge <state>` is simply the name of the artefact you want to work
on: one definition file per state, each declaring its inputs. `/forge`
bare is the map with a recommended next step; `/ledger` is the state
readout. `/ingest` stores a file in `sources/` under a plain slug
name, registers it in the ledger with a best-effort date, and
catalogues it in the material index — nothing more; a set of related
files lives as a subdirectory and counts as one source, catalogued by
its own index. Registration does not imply intake: what a source is
for is noted as its role, and you alone direct when and how it is
used; when its content enters the intent it is your explicit act,
cited with provenance. `/save`, when it touches the core or
`projects/forge/`, first re-renders `README.md` and the Unreleased
head of `RELEASE-NOTES.md`, then runs the relevant conformance check,
settles findings with you, proposes a commit message, and only then
runs the script.

### A typical journey

- You have an idea and write it down as it comes; the forge captures
  it verbatim as the brief of your project and, once you are happy,
  locks it (`/new-project`, `/forge brief`).
- Over several sessions you are interviewed about what you actually
  want; the intent grows, is rewritten for coherence and versioned as
  it goes (`/forge intent`).
- A vendor document and a standard arrive; you register them and
  decide later how each is used (`/ingest`).
- You let a challenger press on the thinking and the critic audit the
  documents, then walk through their findings one by one, recording
  every verdict (`/challenge cto`, `/critique`).
- You compose a presentation recipe through the genre interview and
  render the deck, including the actual PowerPoint through your own
  template (`/recipe presentation`, `/render`, `scripts/md2pptx.ps1`).
- You distil the assignment for the recipients — the one document
  they receive (`/forge assignment`).
- You save as you go, one commit per step (`/save`).

## 10. Conventions

**IDs and numbering.** Every item has an ID `PREFIX.NNNN` — three
letters, four digits — that is global and stable and never renumbered;
items may move between groups without changing their ID. Items are
numbered in tens (`REQ.0010, REQ.0020`), each new group starting at
the next hundred; overflow takes the next free number anywhere. Groups
are plain headings with no IDs, no metadata and no lifecycle; depth is
at most two levels.

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
they appear in the Terms section.

**Language.** The forge dictates the output language: all artefacts
are written in English. The briefs are the exception, stored verbatim
in whatever language they were written. The conversation language is
per-instance configuration and lives in `CLAUDE.local.md`.

**Requirement style.** Use *shall* / *shall not* — no would, could,
should, might, may, and no MoSCoW wording. No priority column and no
priority tags: everything in an assignment is essential by default,
and an exception is marked by a note reading *optional* on that item.
Each item covers one idea, is written once, and is written in full,
correct UK English sentences. Testability is recommended, not
required; delegating concretisation through a DEL item is a legitimate
outcome. An item must not depend on an external link to be understood,
agreed or later tested. One illustrative item:

> REQ.0010 The Platform shall record every request and every response
> passing through the Gateway, with the identity of the requesting
> User and the time.

**Completeness over brevity.** An assignment carries the full in-scope
substance of the intent, written as well and as precisely as possible;
nothing is omitted for brevity's sake, and length is whatever fidelity
requires. Leaving a matter out is legitimate only as an explicit
delegation (a DEL or TBC item). An assignment assigns, it does not
solve: the machinery of executing delivery belongs to the recipients,
while any apparatus you judge part of setting direction may appear.

**Versioning.** Integers denote signed-off versions: `0.1, 0.2, …`
are drafts before first approval, `1.0` is approved, `1.1, 1.2, …` are
changes after approval not yet approved themselves, `2.0` the next
approved version incorporating all changes since 1.0. Front-matter
carries `version`, `date` and `status` (`draft | in_review | approved
| superseded`); an integer version is `approved`, anything else is
not. Every versioned document opens with a Version History table
(Version | Modification | Author | Date). Immutable artefacts — a
locked brief, reviews, challenges, research — are never edited;
corrections happen downstream.

**Project kinds and naming.** A project is of kind `thought` — the
chain — or `library` — shared material with no chain, only a ledger,
sources and research, named with the `lib-` prefix. Projects are
identified by slugs; the engine's own project is `forge`.

## 11. Repository layout

```
CLAUDE.md                  # universal core
CLAUDE.local.md            # instance facts (principal, conversation
                           # language) — gitignored, from
                           # templates/CLAUDE.local.md
README.md                  # for humans — a render (/render readme)
RELEASE-NOTES.md           # release notes — a render (/render
                           # release-notes): Unreleased head +
                           # one frozen section per approved major
logo.png                   # project avatar
LICENSE                    # CC BY 4.0 — the engine is published
                           # under attribution
scripts/                   # forge-save / forge-pull / forge-status
                           # (git), doc2md (document → Markdown),
                           # md2pptx (deck render → PowerPoint)
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
  sources/<name>.<ext>                # immutable external inputs
                                      # (+ .extract.md for binaries)
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
- PowerShell 7 (`pwsh`) — the scripts are PowerShell, needed on macOS
  and Linux too
- Python 3 (for markitdown)
- a paid Claude subscription

### Getting the forge and Claude Code

1. Clone this repository — it is the engine.
2. Copy `templates/CLAUDE.local.md` to the root as `CLAUDE.local.md`
   and fill in the two lines: who the principal is, and the
   conversation language. It is gitignored and never committed.
3. Create `.claude/settings.local.json` with the model to run on —
   `{"model": "..."}` — gitignored; permissions come from the shared
   `.claude/settings.json`.
4. Install Claude Code:
   - Windows: `irm https://claude.ai/install.ps1 | iex`
   - macOS/Linux: `curl -fsSL https://claude.ai/install.sh | bash`
   - or `npm install -g @anthropic-ai/claude-code`
5. Sign in on first run — usage draws from the same pool as Claude
   chat.
6. Always start `claude` from the engine root so that `CLAUDE.md` and
   `CLAUDE.local.md` load.

Upgrading the engine is `scripts/forge-pull.ps1` — a fast-forward of
`main`; your projects are untouched by it.

### Your projects

Each project is a directory under `projects/` and a git repository of
its own. `/new-project` creates the files; `git init` in that
directory, a remote if you want one and the commit identity for that
host are a one-off act of yours. The engine ignores `projects/*`
(except its own `projects/forge`), and the scripts find your project
through its `.git`. A project without a repository is reported as
"not under git" — a fact, not an error.

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

`/save` is the recommended door. Before committing it re-renders the
README and the Unreleased head of the release notes when the save
touches the core, runs the conformance check routed by scope, and
settles the findings with you; then it runs the script. The scripts
are the underlying mechanism and the only intended door to git —
reading state included — and each serves the engine and every project
repository: `forge-save.ps1` commits and pushes (bare, every
repository with changes, each its own commit; with a slug, that one,
`forge` meaning the engine; without an origin the commit is kept and
reported; remote changes reconciled by rebase; the commit's file
summary printed), `forge-pull.ps1` fast-forwards from the remotes and
never touches a repository with unsaved changes, `forge-status.ps1`
reports unsaved changes, the last commit and the origin of each
without changing anything. History is linear on `main` with no
branches, one remote per repository, and the scripts carry no URL and
no identity. The engine receives a git tag at every approved major of
the forge intent.

## 13. Scripts

| Script | Purpose | When it runs | Install note |
|---|---|---|---|
| `scripts/forge-save.ps1` | Commits and pushes the engine or a project repository, reconciling remote changes by rebase. | At every save — through `/save` or directly from the shell. | git only. |
| `scripts/forge-pull.ps1` | Fast-forwards from the remotes, never touching a repository with unsaved changes; the engine's upgrade channel. | When upgrading the engine or syncing a project from another machine. | git only. |
| `scripts/forge-status.ps1` | Reports unsaved changes, the last commit and the origin of each repository without changing anything. | Whenever you want to know the state of git. | git only. |
| `scripts/doc2md.ps1` | Produces the text extract of a binary source through markitdown, never by ad-hoc parsing. | At ingest of a binary document. | markitdown — see Setup. |
| `scripts/md2pptx.ps1` | Turns a Markdown deck render into a `.pptx` through headless Claude Code with the official pptx skill, optionally through a `.potx` template named by path. | After rendering a presentation recipe. | `document-skills` plugin — see Setup. |

## 14. Planned extensions

The chain is meant to keep growing downward: a BRD layer is certain to
come, solution architecture and integration are intended, a strategy
layer is possible if it proves to make sense. Which layers are added,
and in what order, is open, and the mechanics of a layer are designed
when that layer is actually taken up, not in advance. One instance
serves one principal; more principals means more instances. The
system's own design runs through its own process in
`projects/forge/` — its brief, intent, decisions and ledger.

## 15. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) — petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit
the author and link to this repository.

## 16. About this README

This file is a render of `projects/forge`: never edited by hand,
regenerated by `/render readme` whenever the process changes and by
every `/save` touching the core. Fixes go into the recipe
(`projects/forge/recipes/readme.md`) or its inputs. The YAML
front-matter provenance at the top is kept by design. Changes to the
system itself are recorded in `projects/forge/`.

_Last updated: 2026-08-30_
