---
project: forge
render: readme
generated: 2026-09-05
recipe: recipes/readme.md v0.35
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v3.32
---

# Forge of Thought 3.32

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
  articulated and lays out the options with their trade-offs. It
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
isolated agents — challenger personas and critic lenses — for Claude
Code, templates, and the conventions binding them. Today the chain of
artefacts runs from the brief to the assignment; nothing is
implemented here — the forge specifies.

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

- A versioned document chain growing from a **brief** — your own
  text, locked verbatim once it is done — to a self-contained
  assignment.
- An elicitation interview that forges the intent.
- Two kinds of blind adversarial reviewers, every verdict recorded.
- Audience-specific renders generated from recipes, including an
  actual PowerPoint file through your own template.
- External sources registered immutably and used only as the
  principal directs.
- Everything in files and git — nothing depends on a chat's memory.

## 3. Quickstart

**First, once per machine**

```
git clone …          # this repository — you are looking at it
                     # install Claude Code first — see Setup
claude               # always from the engine root
/setup               # first run only — fills CLAUDE.local.md,
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
                                # select the project before any
                                # work — the forge cannot guess it
```

Each project lives inside `projects/<slug>/` as a git repository of
its own, which the engine does not track — that is why you name it
first.

## 4. How it is used

### The flow

A thought arrives — a process you want redesigned, a platform you
want built, a campaign taking shape for your D&D table. You dump it
as it is, in whatever language and shape it comes, into a brief; or
you begin it outside and finish it in conversation with the forge
(`/forge brief`), which clarifies where you are terse and asks whether
someone has already solved the same thing. When it says what you
mean, you lock it, and from then on it is the record everything else
is measured against.

Then the interview begins (`/forge intent`). The forge asks one
question at a time, reflects back what it understood, drafts early so
that you have something concrete to react to, and writes the intent
once per round on your word. You come back after a week, in a fresh
session, and the intent is exactly where you left it — the file is
the memory, not the chat.

Material arrives as it will. A colleague sends the transcript of a
meeting; you download a security standard the intent must later be
verified against; you drop both into `sources/` and `/ingest`
registers them, untouched from that moment. Nothing in them enters
your intent unless you put it there, cited. Where a topic deserves
grounding, `/research` looks up current practice and files a note
you can consult again.

Before the assignment is first drawn from the intent, you send in the
reviewers. A challenger persona (`/challenge cto`) attacks the
thinking — the assumption you never stated, the objective that may
not be the real problem. A critic lens (`/critique essence`) reads
the chain for drift between the brief and the intent. Both work
blind, never seeing your conversation; you walk their findings one
at a time and rule on each, and nothing they say stops you.

When the intent holds, the assignment is distilled from it
(`/forge assignment`): the one document the recipients receive,
complete enough to be handed over without a word of explanation.
And because the same thinking has to reach other audiences, you
compose a recipe — a genre interview (`/recipe presentation`) walks
you through audience, message and dramaturgy — and `/render` turns
it into the pitch for the group; a script turns the deck render into
a real PowerPoint file. When the intent moves, the pitch is
regenerated, never patched by hand. `/save` keeps all of it in git as
you go.

### What it looks like in practice

A worked example from a real project will appear here once one is
published.

## 5. How the work feels

The forge is as much a way of working as a set of files, and these
are the named methods of that work — the vocabulary you and Claude
share.

- **Walkthrough.** Any list of items needing your decision — critique
  findings, challenges, open threads, differences between two
  requirement sets — is worked one item per message, in order of
  weight: Claude's recommendation with a one-sentence reason first,
  your verdict in a word or a counter-proposal, "leave it open" a
  legitimate answer. A table asking for every verdict at once is
  never put in front of you; the verdicts are carried in the
  conversation and written once at the round's end.
- **Propose, never decide.** Claude criticises, challenges, inspires
  and lays out options; you compose.
- **Step by step.** Anything that needs your consent — a write, a
  commit, a push, a rename — arrives as one step with the exact
  operation, its target and the reason, and runs on your word; a
  plan you have seen is not consent for its steps.
- **Elicitation interview.** Claude draws out by questions what you
  have not yet articulated, one question per message, and never
  fills a gap by assumption.
- **Draft early.** An early draft is an elicitation tool, not an
  output: concrete text sharpens your reaction.
- **Reflect back.** Before writing, Claude restates what it
  understood, so the write confirms rather than surprises.
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
| **Claude** | The principal's cognitive extension: structure, order, process discipline and document hygiene; it criticises, challenges, inspires and lays out options — it proposes, never decides. |

Standing rules: when unsure, Claude asks and never fills a gap by
assumption; it never introduces a new convention, prefix or section
on its own — it proposes, waits for the decision, then writes it
down; many iterations are the normal mode, and the intent and the
assignment may change substantially between versions; for key topics
it looks up current best practice before inventing; and everything
it produces is advisory — critiques and checklists inform, only the
principal publishes, and a missing section may be a deliberate
delegation to the recipients rather than a defect.

One instance serves one principal; the recipients collaborate through
the artefacts, and more principals means more instances (see Planned
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

**Blue = chain artefacts (light = not built yet), green = renders; dashed arrows = growth that does not exist yet.**

Adding a layer is one definition file declaring its inputs — nothing
is renumbered and nothing existing is reworked, which is why files
are numbered in tens. The boundary between chain and render is
authorship: a chain artefact is composed by the principal, a render
is generated from artefacts — the article and its translation in the
diagram illustrate it.

| File | What it is |
|---|---|
| `00-brief.md` | The idea as the principal wrote it — draft until locked, then verbatim and never edited; later wholes as `00-brief-<name>.md`. |
| `10-intent.md` | The working understanding of principal and Claude — rewritten freely, versioned. |
| `20-assignment.md` | The direction handed to the recipients — versioned. |
| `<file>.history.md` | The Version History of each versioned document — an append-only companion beside it. |
| `decisions.md` | Append-only DEC records: the principal's decisions with their reasons. |
| `ledger.md` | The single source of truth for state. |
| `sources/`, `research/` | External inputs and research notes, each directory catalogued by its `00-INDEX.md`. |
| `reviews/`, `challenges/` | The dated reports of the two reviewers. |
| `recipes/`, `renders/` | How each render is made, and the generated outputs. |

> A locked brief is immutable — composed, then locked, never touched
> again.

The brief is an intent that is composed and then locked. It is
free-form: any structure you find useful — prose, headings, tables,
use cases — with no required content and no IDs, only a minimal YAML
header. It holds thoughts to be processed, not decisions: they may be
changed, reworked or dropped when they are mined. It is `draft` while
being composed and `approved` (1.0) once you lock it. Three origins
are equally legitimate and indistinguishable to the forge: it arrives
finished and is locked on arrival; it is begun outside and finished
with Claude; it is born in the forge — `/forge brief [name]` is the
door for the latter two. A project may have more than one: every
later whole of thinking that would otherwise land in the intent as a
batch of unproven positions is born as `00-brief-<name>.md` under the
same rules. A locked brief is mined into the single intent —
positions cite it as provenance; a whole that dies on the way leaves
the brief locked and one rejected direction with its reason — and the
ledger tracks how far each brief is mined (`pending | partial | mined
| dropped`) with a free-text note. Each locked brief is the provenance
anchor and drift measure of its whole.

The **intent** (`10-intent.md`) is the consolidated *current* state of
what the principal wants and why: the positions he holds (POS), the
open threads still to elicit (THR) and the directions rejected with
their reason (REJ), each with a stable ID. It is rewritten for
coherence every round rather than appended to, every change recorded
in its history companion, and its audience is the principal and
Claude only. It exists because chat context dies and anything of
value must live in a file: it is the document to read when returning
to a project after weeks, instead of excavating old conversations.

The **assignment** (`20-assignment.md`) is distilled from the intent
for the recipients — teams, colleagues, or the principal's future
self — and is the one document they receive. It holds requirements,
out-of-scope items, constraints, assumptions, deliverables, open
questions with an owner and optional success criteria (REQ, OOS, CON,
ASM, DEL, TBC, SCR): complete and precise, assigning rather than
solving, self-contained.

Iteration: substance changes go into the intent first and propagate
to the assignment, and only wording-only fixes edit the assignment
directly. Write cadence: a working round is written once, on the
principal's confirmation — one version bump and one history row for
the whole round, however many answers it held. Feedback from the
recipients has no channel of its own: the principal processes it and
feeds the conclusions back through `/forge intent`.

The **ledger** (`ledger.md`) is the single source of truth for state —
tables of briefs, documents, renders, sources, research, dependencies
on documents of other repositories, findings and challenges — kept
current after every operation and, together with the resource
indexes, the only freely rewritten file. External inputs
(transcripts, offers, documents, standards) live in `sources/`,
research notes in `research/`; each directory carries a `00-INDEX.md`
saying what each resource is and is for. Registration does not imply
intake: a source's role is individual — a standard to verify against,
inspiration, a counter-example, a meeting record — and the principal
alone directs how and when each is used; when source content does
enter the intent, it is his explicit act, cited with provenance.

> A render is never edited by hand — what is iterated is its recipe.

**Renders and recipes.** A render is an audience-specific output
generated from the chain — a pitch for the group, an architecture
picture, an executive summary, the repository README. Its **recipe**
(`recipes/<recipe>.md`) carries inputs, audience, instructions and
the output template in one versioned file, and `/render <recipe>`
regenerates the output into `renders/<recipe>.md` — or the recipe's
optional `output:` path — overwriting freely, history in git.
Generation runs in an isolated subagent that sees only the recipe
and its inputs. Every render opens with YAML front-matter provenance
citing the recipe and each input with their versions, mirrored in
the ledger's Renders table; a render may cite another render as a
picture source when the recipe declares it among its inputs. A
render assigns nothing and is not part of the chain: the artefacts
stay the source of truth. A recipe is a tool, not a record of
thinking — it carries a version and an updated date and is never
approved. Every project has a README rendered from its own
`recipes/readme.md` and, if it is a thought project, release notes
from `recipes/release-notes.md`; a library has a README only.

**From Markdown to slides.** Everything the forge produces is
Markdown, content only: a presentation is a `.md` saying what is on
each slide. Composing a recipe may be guided by genre —
`/recipe presentation` interviews you on audience and register, the
one message, inputs, dramaturgy, speaker notes and on-slide density,
and fills the genre's skeleton. At the edge sits one conversion:
`scripts/md2pptx.ps1` turns a Markdown deck render into an actual
PowerPoint file through headless Claude Code with the official pptx
skill — a model does the conversion, because deck definitions are
free-form and may carry instructions for it. A `.potx` template is
applied when named by path (`-Template <path>`), typically a document
of a library project; without it Claude designs the visuals itself.
The `.pptx` lands beside its source render, tracked in git and never
edited by hand: the Markdown render stays the source of truth. All
other format conversion happens outside the forge.

## 8. Two isolated reviewers

They cannot be told what we really meant. Both reviewers run as
isolated subagents on the session model and see the artefacts only,
never the working conversation — that blindness is the source of
their value: what the artefact does not say, they do not know, exactly
like the recipients.

**Challengers** attack the substance of the thinking: a growing roster
of persona lenses — the first is `cto`, a peer-CTO register, direct,
few and sharp, no flattery — hunting unstated assumptions, whether
the objective is the real problem, second-order effects,
organisational reality, failure modes and the serious counter-case.

The **critic** reviews the quality of the documents through a roster
of lenses: `clarity` reads each artefact on its own — ambiguity,
internal contradiction, duplication, scope hygiene, requirement
style; `essence` reads the chain for drift, distilling each layer's
essence blind and comparing it with the layer above. The two are one
shape — personas and lenses, one agent file each from a shared
skeleton; challenges (CHL) and findings (FND); both invoked by hand,
both reports immutable and dated, both settled by walkthrough.

Isolation is not independence. The author, the critic and the
challengers share one model family; what that family systematically
cannot see, none of them will find, so agreement between the
reviewers is never treated as validation — it only means the
artefact is consistent under one set of priors. The calibration
point lies outside the forge: review by humans or by a different
model family, invited at the principal's discretion. A challenge may
inspire, but nothing enters the intent because a reviewer wrote it —
only because the principal composed it.

### `/challenge <persona> [artefact]`

Bare `/challenge` lists the roster and recommends a fit for the
project's subject. With a persona, the challenger reads the whole
chain for context and challenges the substance of the named
artefact — or, without one, the whole chain, each challenge naming
the artefact it concerns. It delivers three to seven sharp
challenges, each with a severity (dealbreaker, major or minor, ordered
by it so that a fatal flaw is never buried among cosmetics), a
falsifiable "what would change my mind" and an epistemic status
(consensus, active debate, emerging practice or my judgement);
fabrication is banned — uncertainty is stated, not papered over. The
report lands as `challenges/YYYY-MM-DD-challenge-<persona>.md` with
CHL rows in the ledger. Challenge states: open, accepted, rejected
(a DEC with its reason), parked, obsolete. An accepted challenge must
change the intent — otherwise it was not accepted. An artefact is
best challenged before the next layer is first derived from it,
while accepted challenges are still cheap to absorb. New personas are
created only by the principal's decision, and only where their blind
spots genuinely differ: personas that would say the same things in
different words are noise.

### `/critique <lens> [artefact]`

Bare `/critique` lists the lens roster. `clarity` takes one artefact
(or each in turn) and reports ambiguity, internal contradiction,
duplication, scope hygiene and departures from the requirement style.
`essence` takes one artefact against its parent (or every adjacent
pair — brief → intent, intent → assignment, every later layer): it
distils the downstream artefact's essence blind, then the upstream's,
and compares — substance lost without a trace (a REJ, DEC, DEL or
TBC, the ledger's mining state), added without provenance, or shifted
in meaning; a finding is a difference of essences, not of texts, and
the report carries both distillations. Regression against resolved
findings is every lens's first step. Untestable wording is reported
as a recommendation, never as a defect. The report lands as
`reviews/YYYY-MM-DD-critique-<lens>.md` with FND rows in the ledger.
Finding states:

- open
- resolved — an iteration of the artefact concerned
- overruled — a DEC with its reason
- obsolete — the passage no longer exists

## 9. Commands

Commands are entry points into phases, not the only permitted door:
the core rules apply in ordinary conversation too, and plain
conversation works.

| Command | Purpose |
|---|---|
| `/setup` | First run after cloning the engine: creates and fills `CLAUDE.local.md` by interview, sets the session model to Fable, offers the global git identity guard. Never overwrites, runs no git operation. |
| `/new-project <slug>` | Scaffolds a project by kind — files only, never git: a thought project with its brief captured verbatim, or a library (`lib-`). |
| `/import-project <git-url>` | Brings an existing project into `projects/` through `scripts/forge-clone.ps1`; the commit identity is proposed from `CLAUDE.local.md` by the URL's host. |
| `/forge [slug]` | The chain map: artefacts, versions, possible next steps, stale renders — with a recommended next step. |
| `/forge <state> [slug]` | Iterates the named artefact (`brief [name]`, `intent`, `assignment`, …). |
| `/ingest [file] [slug]` | Stores and registers external input in `sources/` and indexes it; bare, sweeps `sources/`. |
| `/render <recipe> [slug]` | Regenerates a render from its recipe in `recipes/`. |
| `/recipe [genre] [slug]` | Bare, the genre roster; with a genre (`presentation`, `readme`, `release-notes`), guided composition or iteration of a recipe. |
| `/critique [lens] [artefact] [slug]` | Bare, the lens roster; with a lens (`clarity`, `essence`), runs that critic on one artefact or on all. |
| `/challenge [persona] [artefact] [slug]` | Bare, the persona roster; with a persona (e.g. `cto`), runs that challenger against the named artefact or the whole chain. |
| `/research <topic> [slug]` | Best-practice research into `research/`, indexed. |
| `/ledger [slug]` | The quick state readout from the ledger. |
| `/check [slug]` | Conformance of a project against the current conventions; all projects but forge when bare. |
| `/check-forge` | Consistency check of the core and `projects/forge`. |
| `/save [slug] [-m "message"]` | Pre-save check, findings settled with the principal, renders regenerated, then commit and push. |
| `/spinoff <project> <group> <slug>` | Splits a requirement group into a project of its own — only by the principal's explicit decision. |

`/forge <state>` is simply the name of the artefact you want to work
on: `/forge intent` iterates the intent, `/forge assignment` the
assignment, `/forge brief` a brief — one definition file per state,
each declaring its own inputs, so the chain is a star rather than a
line and a future layer is one more file. Bare `/forge` shows where
the chain stands and what can be worked from here; `/ledger`
re-orients you from the ledger alone, which is why a session can end
at any point without loss. `/check` and `/check-forge` are the
mechanical guard, distinct from the two reviewers: read-only and
advisory, they check conformance, never substance.

`/ingest` stores a file in `sources/`, registers it in the ledger and
catalogues it in the directory's index — nothing more; bare, it
sweeps `sources/` for unregistered files. Every binary file gets one
question — convert to Markdown? — yes makes the extract, produced by
`scripts/doc2md.ps1`, the source; no keeps the binary itself, a
template or a graphic, with no extract. A set of related files lives
as a subdirectory `sources/<slug>/` and counts as one source. `/save`
is the recommended door to saving: it routes the conformance check by
scope (`/check-forge` for core changes, `/check <slug>` per touched
project), settles the findings with you in a walkthrough, then — from
the settled sources — re-renders the README and the Unreleased head
of the release notes, reporting what materially changed in them,
proposes a commit message, and only then commits and pushes.

### A typical journey

- You write down the idea as it is in your head — or dictate it to
  the forge — and lock it as the brief of your project
  (`/new-project`, `/forge brief`).
- Over several sessions you answer the forge's questions one at a
  time; the intent grows and is rewritten for coherence each round
  (`/forge intent`).
- Material arrives — a transcript, a standard — and is registered
  untouched, used only when you say so (`/ingest`); a key topic gets
  a research note (`/research`).
- Before the first assignment you send in the reviewers: a persona
  attacks the thinking, a lens reads the documents; you walk their
  findings one by one and give your verdict on each
  (`/challenge cto`, `/critique essence`).
- You want to present the idea to the group: a genre interview
  composes the deck recipe, the render is generated, and a script
  turns it into a real PowerPoint through your own template
  (`/recipe presentation`, `/render`, `scripts/md2pptx.ps1`).
- The assignment is distilled from the intent, complete and
  self-contained, and handed over by a link into git
  (`/forge assignment`).
- You save as you go; each save checks your project, settles what it
  finds with you and regenerates the project's README and release
  notes (`/save`).

## 10. Conventions

**IDs and numbering.** Format `PREFIX.NNNN`, all prefixes three
letters. IDs are global and stable — never renumbered; items may move
between groups without ID change. Items are numbered in tens
(`REQ.0010, REQ.0020`), each new group starting at the next hundred
(`REQ.0100, REQ.0110`); overflow takes the next free number anywhere.
Groups are plain headings: no IDs, no metadata, no lifecycle; depth
max two levels.

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
prefixes and the domain terms it actually uses, so it can be
forwarded without oral tradition; defined terms are capitalised in
item text to signal they appear there.

**Language.** The forge dictates the output language: all documents
are written in English. The briefs are the exception, stored verbatim
in whatever language they were written. The conversation language is
per-instance configuration and lives in `CLAUDE.local.md`.

**Requirement style.** Shall / shall not — no would, could, should,
might or may, and no MoSCoW wording. No priority column and no
priority tags: everything in an assignment is essential by default,
and an exception is marked by a note reading *optional* on that item.
Each item covers one idea, is written once, and is written in full,
correct UK English sentences. Testability is recommended, not
required: assignments are deliberately high-level, and delegating
concretisation through a DEL item is a legitimate outcome. An item
must not depend on an external link to be understood, agreed or
later tested. One illustrative item:

> REQ.0010 The Platform shall record every request and every response
> passing through the Gateway, with the identity of the requesting
> User and the time.

**Completeness over brevity.** An assignment carries the full
in-scope substance of the intent, written as well and as precisely
as possible; nothing is omitted for brevity's sake, and length is
whatever fidelity requires — leaving a matter out is legitimate only
as an explicit delegation (a DEL or TBC item). An assignment assigns,
it does not solve: the machinery of executing delivery belongs to
the recipients, but any apparatus may appear where the principal
judges it part of setting direction.

**Versioning and status.** Integers denote signed-off versions:
`0.1, 0.2, …` are drafts before first approval; `1.0` is approved;
`1.1, 1.2, …` are changes made after approval, not yet approved
themselves; `2.0` is the next approved version, incorporating all
changes since `1.0`. Front-matter carries `version`, `date`, `status`
(`draft | in_review | approved | superseded`) and `last_change`, and
status must agree with the number.

**Document kinds.** "Document" is the word for every file of a
project; "artefact" is reserved for the documents of the chain — the
ones the principal composes, the reviewers read and the renders are
generated from. Every document has one kind, and the kind says what
it is, who writes it, whether it is versioned and how it behaves:

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
companion `<file>.history.md` beside it, with `last_change` in the
front-matter summarising the newest row. An integer version is
approved, and a recipe never is. Immutable documents are never
edited — a brief from its lock, a source from its registration, the
others from creation; corrections happen downstream.

**Project kinds and naming.** A project has a kind: `thought` — the
chain — or `library` (prefix `lib-`): material shared across
projects, with no chain — only a ledger, sources and research with
their indexes, and a README that catalogues what it holds. Project
slugs are lowercase and hyphenated on disk — `forge` is the system's
own project, a library is `lib-<name>` — and display names may
differ.

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
- PowerShell 7 (`pwsh`) — the scripts are PowerShell, needed on
  macOS and Linux too
- Python 3 — for markitdown
- a paid Claude subscription

### Getting the forge and Claude Code

Clone this repository — it is the engine. Then install Claude Code:

```
irm https://claude.ai/install.ps1 | iex             # Windows
curl -fsSL https://claude.ai/install.sh | bash      # macOS / Linux
npm install -g @anthropic-ai/claude-code            # or via npm
```

Sign in on first run — usage draws from the same pool as Claude chat.
Always start `claude` from the engine root, so that `CLAUDE.md` and
`CLAUDE.local.md` load.

Then run `/setup` once. It creates `CLAUDE.local.md` from its template
and fills it with you in a short interview — who the principal is,
the conversation language, your git identities per host — gitignored,
never committed; and it creates `.claude/settings.local.json` with
the session model set to Fable, the strongest available model, which
the whole forge including the blind reviewers runs on. It tells you
so in one sentence; `/model` or editing that file changes it at any
time, while permissions come from the shared `.claude/settings.json`.
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
the origin's host and confirmed by you. An existing project is
brought in with `/import-project <git-url>`, which clones it into
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
- The git scripts need nothing beyond git.

### Saving and syncing

`/save` is the recommended door: before the commit it runs the
scope-routed conformance check, settles its findings with the
principal, and re-renders the README and the Unreleased head of the
release notes when the save touches the core. The scripts are the
underlying mechanism and the only intended door to git — reading
state included, no exceptions — each serving the engine and every
project repository: a bare `forge-save.ps1` commits each repository
with changes on its own and pushes where it has a remote,
reconciling remote changes by rebase; without an origin the commit is
kept and reported. History is linear on `main`, one remote per
repository, and no URL is written anywhere in the forge — git carries
that itself. Immutability of documents is a process rule, not a git
mechanism.

## 13. Scripts

| Script | Purpose | When it is run | Install note |
|---|---|---|---|
| `scripts/forge-save.ps1` | Commits and pushes — bare, every repository with changes, each its own commit; with a slug, that one (`forge` meaning the engine); prints the commit's file summary. | By `/save`, or directly from the shell. | git only. |
| `scripts/forge-pull.ps1` | Fast-forwards from the remotes and never touches a repository with unsaved changes; on the engine it is the upgrade channel. | When upgrading the engine or syncing a project. | git only. |
| `scripts/forge-status.ps1` | Reports unsaved changes, the last commit and the origin of each repository without changing anything. | Whenever you want to know where things stand. | git only. |
| `scripts/forge-clone.ps1` | Clones a repository into `projects/<repository name>`, never overwriting, and sets its local commit identity when given `-Name` and `-Email`. | By `/import-project`. | git only. |
| `scripts/doc2md.ps1` | Converts a binary document to a Markdown extract in `sources/`. | By `/ingest`, for every binary you choose to convert. | markitdown — see Setup. |
| `scripts/md2pptx.ps1` | Turns a Markdown deck render into a `.pptx` through headless Claude Code with the official pptx skill, with an optional `.potx` template named by path. | After rendering a presentation recipe. | `document-skills` plugin — see Setup. |

## 14. Planned extensions

The chain grows downward, as far as its owner needs thoughts taken. A
BRD layer is certain to come; solution architecture and integration
are intended; a strategy layer is possible if it proves to make
sense. Which layers are added, and in what order, is open, and
nothing is approved for construction: the mechanics of a layer —
commands, agents, reviewer calibration — are designed when that
layer is actually taken up, not in advance. Independent challengers
are planned: personas running on a different model family than the
author's, so that `/challenge` can send in a lens with genuinely
different priors.

More principals means more instances: a second principal receives
the forge via git and runs an instance of their own; genuine
multi-user operation is a question for the future, deliberately not
worked on now.

`projects/forge/` is Forge of Thought itself run through its own
process — its brief, intent, decisions and ledger — and every process
change is complete only once that intent is updated and this README
re-rendered.

## 15. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) — petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit
the author and link to this repository.

## 16. About this README

This file is a render of `projects/forge`: it is never edited by hand
and is regenerated by `/render readme` whenever the process changes,
and by every `/save` touching the core. Fixes go into the recipe
(`projects/forge/recipes/readme.md`) or its inputs — `CLAUDE.md` and
the forge intent. The YAML front-matter provenance at the top is kept
by design; changes to the system are recorded in `projects/forge/`.

_Last updated: 2026-09-05_
