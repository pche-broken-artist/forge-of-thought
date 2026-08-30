---
project: forge
render: readme
generated: 2026-08-30
recipe: projects/forge/recipes/readme.md v0.25
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v2.21
---

# Forge of Thought 2.21

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

Technically the forge is a git repository: slash commands and agent
personas for Claude Code, templates, and the conventions binding them.
Today the chain ends at the assignment; it is built to grow further
without reworking anything that exists.

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
- An elicitation interview that forges the intent out of what you
  have not yet articulated.
- Two kinds of blind adversarial reviewers, every verdict recorded.
- Audience-specific renders generated from recipes, including an
  actual PowerPoint file through your own template.
- External sources registered immutably and used only as you direct.
- Everything in files and git — nothing depends on a chat's memory.

## 3. Quickstart

```
git clone <this repository>          # the engine
cp templates/CLAUDE.local.md CLAUDE.local.md   # fill in the two lines
# install Claude Code — see Setup
claude                               # start from the engine root
/new-project <slug>                  # scaffold and capture the brief
/forge intent                        # the elicitation interview
/save                                # check, then commit and push
```

Each project lives inside `projects/<slug>/` as a git repository of
its own, which the engine does not track.

## 4. How it is used

### The flow

A thought arrives — a process you want redesigned, a platform you
want built, a campaign taking shape for your D&D table. You dump it
as it is, alone or in conversation with the forge (`/forge brief`),
and when it says what you meant you lock it: from then on it is the
record against which everything later is measured.

Then the forge interviews you. `/forge intent` asks what you have not
said yet, reflects back what it understood, and writes once per round
into the intent — positions you hold, threads still open, directions
you dropped and why. This goes on over days and sessions; nothing is
lost between them, because everything lives in files.

Material arrives on its own schedule. A downloaded security standard
lands in `sources/` through `/ingest`, registered and catalogued but
not read into anything — weeks later you ask for the intent to be
verified against it, and only then does it matter. Where a topic
deserves grounding, `/research` looks up current practice and files a
note you can consult later.

When the thinking feels solid, you send in the reviewers. `/challenge
cto` attacks the substance without knowing what you meant; `/critique`
audits the documents for gaps and contradictions. Nothing blocks — you
walk through the findings one at a time and rule on each.

Then the handover: `/forge assignment` distils the intent into the
one document the recipients receive. And the audiences beyond them
get renders — a pitch for the group, a slide deck that becomes a real
PowerPoint file, a mail, this very README — each from a recipe you
iterate (a genre interview can guide its composition), each
regenerated whenever the chain moves. `/save` keeps all of it in git.

### What it looks like in practice

A worked example from a real project will appear here once one is
published.

## 5. How the work feels

The forge is as much a way of working as a set of files, and these
are the named methods of that work — the vocabulary you and Claude
share.

- **Walkthrough.** Any list needing your decision — findings,
  challenges, open threads, differences between two requirement sets
  — is worked one item at a time, in order of weight, Claude's
  recommendation and reason first, your verdict in a word. "Leave it
  open" is legitimate, and nothing is written until the round ends.
- **Propose, never decide.** Claude criticises, challenges, inspires
  and lays out options; you compose.
- **Elicitation interview.** Claude draws out by questions what you
  have not yet articulated instead of filling gaps by assumption.
- **Draft early.** An early draft is an elicitation tool, not an
  output: concrete text sharpens your reaction.
- **Reflect back.** Before anything is written, Claude restates what
  it understood, so the write confirms rather than surprises.
- **Intent-first.** Changes of substance go into the intent and
  propagate from there; only wording is fixed downstream directly.
- **Recommend, do not push.** Every option comes with a recommendation
  and reason, stated once; a declined recommendation is not re-argued
  without new facts.

None is a command: you invoke any of them in a word.

## 6. Roles

| Role | What they own |
|---|---|
| Principal | Whoever's thinking is being forged: supplies ideas, answers and decisions, and is the final authority on all content. |
| Claude | The principal's cognitive extension: owns structure, order, process discipline and document hygiene; criticises, challenges, inspires and lays out options; proposes, never decides. |

Standing rules: when unsure, Claude asks and never fills a gap by
assumption; no new convention, prefix or section is introduced
unilaterally; many iterations are the normal mode; key topics are
researched before anything is invented; every critique and checklist
is advisory, and only the principal publishes.

One instance serves one principal; recipients collaborate through the
artefacts. More principals means more instances (see Planned
extensions).

## 7. The document chain

```
00-brief.md (draft → locked)
     │
     ▼
10-intent.md ──────────► renders/<recipe>.md
     │                      (pitch, deck, README …)
     ▼
20-assignment.md ──────► renders/<recipe>.md
     │
     ▼
later layers (30-brd.md, 40-solution-design.md, …)
```

| File | What it is |
|---|---|
| `00-brief.md` | Your idea as you wrote it — draft while composed, verbatim and immutable once locked. |
| `10-intent.md` | The consolidated current state of what you want — rewritten freely, versioned. |
| `20-assignment.md` | The distilled handover for the recipients — versioned, self-contained. |
| `decisions.md` | Append-only record of decisions (DEC). |
| `ledger.md` | Single source of truth for state. |

> A locked brief is immutable — composed, then locked, never touched
> again.

The **brief** is an intent composed and then locked. It is free-form:
any structure you find useful — prose, headings, tables, use cases —
with no required content and no IDs, only a minimal YAML header. It
holds thoughts to be processed rather than decisions, so they may be
changed, reworked or dropped when mined. It is `draft` while being
composed and `approved` (1.0) once you lock it. Three origins are
equally legitimate and indistinguishable to the forge: it arrives
finished and is locked on arrival; it is begun outside and finished
with Claude; it is born in the forge — `/forge brief [name]` is the
door for the latter two. A project may have more than one: every
later whole of thinking that would otherwise land in the intent as a
batch of unproven positions is born as `00-brief-<name>.md` under the
same rules. A locked brief is mined into the single intent, whose
positions cite it as provenance; a whole that dies on the way leaves
the brief locked and one rejected direction with the reason. The
ledger tracks each brief's mining state — pending, partial, mined or
dropped — with a note.

The **intent** is the consolidated *current* state of your thinking
— positions you hold (POS), open threads (THR) and rejected
directions with their reason (REJ), each with a stable ID. It is
rewritten for coherence every round rather than appended to, with a
changelog of what changed and why; its audience is you and Claude
only. It exists because chat context dies and anything of value must
live in a file: it is the document to read when returning to a
project after weeks, instead of excavating old conversations.

The **assignment** is distilled from the intent for the recipients and
is the one document they receive: requirements, out-of-scope items,
constraints, assumptions, deliverables, open questions with an owner
and optional success criteria (REQ, OOS, CON, ASM, DEL, TBC, SCR). It
is complete and precise, assigning rather than solving, and
self-contained.

Iteration: substance changes go into the intent first and propagate
to the assignment; wording-only fixes may edit the assignment
directly. Write cadence: artefacts are written once per iteration
round, on your confirmation — one version bump, one history row.
Feedback from the recipients has no channel of its own: you process
it and feed the conclusions back through `/forge intent`.

> A render is never edited by hand — what is iterated is its recipe.

**Renders and recipes.** A **recipe** (`recipes/<recipe>.md`) holds
inputs, audience, instructions and the output template in one
versioned file; `/render <recipe>` regenerates the output into
`renders/<recipe>.md` — or the recipe's own `output:` path —
overwriting freely, with history in git. Generation runs in an
isolated subagent that sees only the recipe and its inputs. Every
render opens with YAML front-matter provenance citing the recipe and
each input with their versions, and a render may serve as an input of
another render when the citing recipe declares it. A render assigns
nothing and is not part of the chain: the artefacts stay the source
of truth.

**From Markdown to slides.** Everything the forge produces is
Markdown, content only. Composing a recipe may be guided by genre
(`/recipe presentation` for a slide-by-slide deck definition).
`scripts/md2pptx.ps1` turns a deck render into an actual PowerPoint
file through headless Claude Code with the official pptx skill; a
`.potx` template is applied when named by path — typically a document
of a library project — and without one Claude designs the visuals
itself. The generated `.pptx` lands beside its source render and is
tracked like any render output; the Markdown stays the source of
truth. All other format conversion happens outside the forge.

## 8. Two isolated reviewers

Both reviewers run with a clean context: they see the artefacts only,
never the working conversation — they cannot be told what we really
meant. That blindness is the source of their value.

The **challengers** are a growing roster of persona lenses attacking
the substance of the thinking: unstated assumptions, whether the
objective is the real problem, second-order effects, organisational
reality, failure modes, the counter-case.

The **critic** is the auditor of the documents and of the project's
consistency across artefacts: ambiguity, gaps, contradictions,
duplication, divergence between intent and assignment, regression on
past findings.

Isolation is not independence. The author and both reviewers share
one model family: what that family systematically cannot see, none of
them will find, so agreement between the reviewers is never treated
as validation — it only means the artefact is consistent under one
set of priors. The calibration point lies outside the forge: review
by humans or by a different model family, invited at your discretion.

### `/challenge <persona> [artefact]`

One isolated agent per persona (`challenger-<persona>`), each a
distinct lens; the first is `cto` — a peer-CTO register, direct, few
and sharp, no flattery. Further personas are created only by your
decision, and only where their blind spots genuinely differ. Bare
`/challenge` lists the roster and recommends a fit. The target may be
any chain artefact, the intent by default; a layer is best challenged
before the next one is first derived from it. Challenges carry a
severity (dealbreaker, major, minor) and an epistemic status, and
fabrication is banned — uncertainty is stated, not papered over. The
output is a dated, immutable file in `challenges/` with CHL items;
their states are open, accepted, rejected (with a recorded decision),
parked or obsolete. An accepted challenge must change the intent.

### `/critique`

The critic writes a dated, immutable review in `reviews/` with FND
items and reports a delta against earlier runs. Finding states:

- new
- verified resolved
- still open
- newly obsolete

Nothing blocks. Every finding and challenge is either fixed or
explicitly overruled with a recorded reason; silently ignoring is not
an option. Untestable wording is reported as a recommendation, never
as a defect. Both reviewers run on the session model — the whole
forge runs on one model, and speed is bought with context, never with
a weaker reviewer.

## 9. Commands

Commands are entry points into phases, not the only permitted door;
plain conversation follows the same rules.

| Command | Purpose |
|---|---|
| `/new-project <slug>` | Scaffold a project by kind — files only, never git: a thought project with its brief captured verbatim (locked if finished, draft otherwise), or a library (`lib-`) of shared material. |
| `/forge [slug]` | The chain map: which artefacts exist at what versions, which states can be worked from here, which renders are stale, and a recommended next step. |
| `/forge <state> [slug]` | Iterate the target artefact — the command is simply the name of the artefact you want to work on (`brief [name]`, `intent`, `assignment`, …). |
| `/ingest [file] [slug]` | Store and register an external input in `sources/` and index it; bare, sweep `sources/`. |
| `/render <recipe> [slug]` | Regenerate a render from its recipe in `recipes/`. |
| `/recipe [genre] [slug]` | Bare, the genre roster; with a genre (e.g. `presentation`), guided composition or iteration of a render recipe. |
| `/critique [slug]` | Run the isolated critic; review file and ledger updated. |
| `/challenge [persona] [artefact] [slug]` | Bare, the challenger roster; with a persona (e.g. `cto`), run it against the substance of any chain artefact (default the intent). |
| `/research <topic> [slug]` | Best-practices research into `research/`, indexed. |
| `/ledger [slug]` | The quick state readout from the ledger. |
| `/check [slug]` | Conformance of a project against the current conventions; all but forge when bare. |
| `/check-forge` | Consistency check of the core and `projects/forge`. |
| `/save [slug] [-m "message"]` | Pre-save check, findings settled with you, then commit and push. |
| `/spinoff <project> <group> <slug>` | Split a requirement group into its own project — by your explicit decision only. |

`/ingest` stores, registers and catalogues — nothing more: a source's
role (a standard to verify against, inspiration, a counter-example, a
meeting record) is noted in the material index, and you alone direct
how and when it is used. Text extracts of binary sources come from
`scripts/doc2md.ps1`, never from ad-hoc parsing; a set of related
files lives as a bundle `sources/<slug>/` with its own catalogue.
`/save` routes the conformance check by scope, settles the findings
with you, proposes a commit message and only then runs the script;
when the save touches the core it first re-renders this README and
the release notes. `/forge` is the chain map with a recommended next
step; `/ledger` is the quick state readout.

### A typical journey

- You write down what is on your mind, as it is, and lock it (`/forge
  brief`, or `/new-project` with a finished text).
- Over several sessions you are interviewed, and the intent of your
  project takes shape, round by round (`/forge intent`).
- You register the documents you are working from — a standard, an
  offer, a transcript — and ask for a topic to be researched
  (`/ingest`, `/research`).
- You invite pressure: a peer persona attacks the thinking, the critic
  audits the documents, and you rule on each item one at a time
  (`/challenge cto`, `/critique`).
- You compose a recipe for a presentation and render it, including
  the PowerPoint file (`/recipe presentation`, `/render`,
  `scripts/md2pptx.ps1`).
- You distil the assignment for the recipients (`/forge assignment`).
- You save as you go, each save checked before it is committed
  (`/save`).

## 10. Conventions

**IDs.** Format `PREFIX.NNNN`, all prefixes three letters. IDs are
global and stable — never renumbered; items may move between groups
without changing ID. Items are numbered in tens (`REQ.0010`,
`REQ.0020`), each new group starting at the next hundred; overflow
takes the next free number anywhere. Groups are plain headings with no
IDs, no metadata and no lifecycle; depth is at most two levels.

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

**Language.** The forge dictates the output language: all artefacts
are written in English. The briefs are the exception, stored verbatim
in whatever language they were written. The conversation language is
per-instance configuration and lives in `CLAUDE.local.md`.

**Requirement style.** Items use *shall* / *shall not* — never would,
could, should, might, may or MoSCoW wording. No priority column and
no priority tags: everything in an assignment is essential, an
exception carries a note reading *optional*. Each item covers one
idea, is written once, in full, correct UK English sentences, and
must not depend on an external link to be understood, agreed or
tested. Testability is recommended, not required. Illustrative only:

> REQ.0010 The Platform shall record every request and every response
> passing through the Gateway, with the identity of the requesting
> User and the time.

**Completeness over brevity.** An assignment carries the full in-scope
substance of the intent, written as precisely as possible; nothing is
omitted for brevity's sake, and length is whatever fidelity requires.
Leaving a matter out is legitimate only as an explicit delegation (a
DEL or TBC item). The boundary is one of kind, not amount: an
assignment assigns, it does not solve; the machinery of executing
delivery belongs to the recipients.

**Versioning.** Integers denote signed-off versions: `0.1, 0.2, …`
are drafts before first approval, `1.0` is approved, `1.1, 1.2, …`
are changes after approval not yet approved themselves, `2.0` is the
next approved version incorporating everything since `1.0`.
Front-matter carries `version`, `date` and `status` (`draft`,
`in_review`, `approved`, `superseded`), and status must agree with
the number. Every versioned document opens with a Version History
table. Immutable artefacts — a locked brief, reviews, challenges,
research — are never edited: a brief from its lock, the others from
creation; corrections happen downstream.

**Project kinds.** A project is of kind `thought` — the chain — or
`library`: a collection of documents shared across projects, with
only sources, research and a ledger, no chain; its documents are
maintained by their owner. The kind is declared in the ledger header
and defaults to `thought`. Slugs are lowercase and hyphenated on
disk; the engine's own project is `forge`, libraries carry the `lib-`
prefix. Display names may differ and must be legible to the audience,
not only to the principal.

## 11. Repository layout

```
CLAUDE.md                  # universal core — the rules for the agent
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
  sources/00-INDEX.md      # sources and research; documents
  research/00-INDEX.md     # maintained by their owner
```

## 12. Setup

### Prerequisites

- git.
- PowerShell 7 (`pwsh`) — the scripts are PowerShell and run
  unchanged on Windows, macOS and Linux; on macOS and Linux it is one
  install.
- Python 3, for markitdown (document extracts).
- A paid Claude subscription — Claude Code draws on it.

### Getting the forge and Claude Code

1. Clone this repository: it is the engine.
2. Copy `templates/CLAUDE.local.md` to the root as `CLAUDE.local.md`
   and fill in the two lines: who the principal is and the
   conversation language. The file is gitignored and never committed.
3. Create `.claude/settings.local.json` with the model to run on —
   `{"model": "..."}` — gitignored as well; permissions come from the
   shared `.claude/settings.json`.
4. Install Claude Code:
   - Windows: `irm https://claude.ai/install.ps1 | iex`
   - macOS/Linux: `curl -fsSL https://claude.ai/install.sh | bash`
   - or `npm install -g @anthropic-ai/claude-code`
5. Sign in on first run — usage draws from the same pool as Claude
   chat.
6. Always start `claude` from the engine root, so that `CLAUDE.md`
   and `CLAUDE.local.md` load.

Upgrading the engine is `scripts/forge-pull.ps1` — a fast-forward of
`main`; the projects are untouched by it. The engine receives a git
tag at every approved major version.

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
  document of a library project — or omitted, in which case Claude
  designs the visuals.
- `forge-save.ps1`, `forge-pull.ps1` and `forge-status.ps1` need
  nothing beyond git.

### Saving and syncing

The recommended door is `/save`. When the save touches the core or
`projects/forge/` it first re-renders `README.md` and the Unreleased
head of `RELEASE-NOTES.md` from their recipes, then runs the
conformance check routed by scope — `/check-forge` for the core,
`/check <slug>` per touched project — settles the findings with you,
proposes a commit message and only then commits.

Underneath are three scripts, and they are the only intended door to
git — reading state included, no exceptions. Each serves the engine
and every project repository: `scripts/forge-save.ps1` commits and
pushes (bare, every repository with changes, each its own commit,
pushed where it has a remote; with a slug, that one — `forge` meaning
the engine; without an origin the commit is kept and reported; remote
changes are reconciled by rebase); `scripts/forge-pull.ps1`
fast-forwards from the remotes and never touches a repository with
unsaved changes; `scripts/forge-status.ps1` reports unsaved changes,
the last commit and the origin of each without changing anything.
History is linear on `main`, one remote per repository, and no URL
and no identity is written anywhere in the forge — git carries that
itself. Immutability of artefacts is a process rule, not a git
mechanism.

## 13. Scripts

| Script | Purpose | When it runs | Install note |
|---|---|---|---|
| `scripts/forge-save.ps1` | Commits and pushes the engine and every project repository with changes, reconciling remote changes by rebase and printing the commit's file summary. | Under `/save`, or directly from the shell. | git only. |
| `scripts/forge-pull.ps1` | Fast-forwards from the remotes and refuses to run over unsaved changes; on the engine it is the upgrade channel. | When upgrading the engine or syncing a project from its remote. | git only. |
| `scripts/forge-status.ps1` | Reports unsaved changes, the last commit and the origin of each repository without changing anything. | Whenever state is read — it is how `/save` learns its scope. | git only. |
| `scripts/doc2md.ps1` | Produces the text extract of a binary source (document to Markdown) through markitdown. | By `/ingest` for every binary source, file by file. | markitdown — see Setup. |
| `scripts/md2pptx.ps1` | Turns a Markdown deck render into a PowerPoint file through headless Claude Code with the official pptx skill, with an optional `.potx` template named by path. | After a presentation recipe has been rendered. | `document-skills` plugin — see Setup. |

## 14. Planned extensions

The chain is designed to keep growing downward: a BRD layer is
certain to come; solution architecture and integration are intended;
a strategy layer is possible if it proves to make sense. Which layers
are added, and in what order, is open, and the mechanics of a layer —
commands, agents, reviewer calibration — are designed when that layer
is actually taken up, not in advance. The file numbering in tens and
the global ID scheme exist so that this growth reworks nothing.

Independent challengers on a different model family than the
author's are planned, so that `/challenge` can send in a lens with
genuinely different priors.

Multi-principal use is deliberately not being worked on now: today a
second principal receives the forge via git and runs an instance of
their own — more principals, more instances.

`projects/forge/` is the forge itself run through its own process —
brief, intent with positions, open threads and rejected directions,
decisions and ledger — and the one project that travels with the
engine.

## 15. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) — petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit
the author and link to this repository.

## 16. About this README

This file is a render of `projects/forge`: it is regenerated by
`/render readme` whenever the process changes, and by every `/save`
that touches the core, and it is never edited by hand. Fixes go into
its recipe (`projects/forge/recipes/readme.md`) or into its inputs —
`CLAUDE.md` and the forge intent. The YAML provenance at the top is
kept by design: it says which recipe and which input versions produced
this text. Changes to the system itself are recorded in
`projects/forge/`.

_Last updated: 2026-08-30_
