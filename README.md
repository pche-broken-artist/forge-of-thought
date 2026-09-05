---
project: forge
render: readme
generated: 2026-09-06
recipe: recipes/readme.md v0.37
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v3.39
---

# Forge of Thought 3.39

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
isolated agents — challenger personas and critic lenses — for Claude
Code, templates, and the conventions binding them. Today the chain
runs from the brief to the assignment; it is built so that further
layers can be added below without reworking anything that exists.

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
- An elicitation interview that forges the intent, one question at a
  time, over as many sessions as it takes.
- Two kinds of blind adversarial reviewers — challengers of the
  thinking, critics of the documents — with every verdict recorded.
- Audience-specific renders generated from recipes, including an
  actual PowerPoint file through your own template.
- External sources registered immutably and used only as the
  principal directs.
- Everything in files and git — nothing depends on a chat's memory.

## 3. Quickstart

**First, once per machine**

```
git clone …                # this repository — you are looking at it
# install Claude Code      # see Setup below
claude                     # always from the engine root
/setup                     # first run only — fills CLAUDE.local.md, sets the model (Fable)
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

A thought arrives — a process you want redesigned, a platform you
want built, a campaign taking shape for your D&D table. You dump it as
it is: pasted in finished, or talked out with the forge (`/forge
brief`) until it says what you mean. Then you lock it, and from that
moment it is the record of where you started.

The intent is forged from it in interviews. You answer one question
at a time, the forge reflects back what it understood, and at the end
of a round it writes — positions, open threads, rejected directions,
each with a stable ID. This runs over days and sessions; everything
lives in files, so you can close the laptop mid-thought and pick up
where the ledger says you left off (`/ledger`).

Material arrives whenever it arrives. A downloaded security standard
goes into `sources/` (`/ingest`) and sits there, registered and
immutable, until you say "check the intent against it". Where you
want ground under a key topic, `/research` stores what current
practice says and indexes it for the next time.

When the thinking has a shape, you send in the reviewers. A
challenger persona attacks the substance (`/challenge cto`); a critic
lens reads the documents (`/critique clarity`, `/critique essence`).
Neither has seen your conversation. You walk through what they found
one item at a time; nothing blocks you, and every verdict is recorded.

The assignment is distilled for the recipients (`/forge assignment`)
— the one document they receive. Everything else the thinking has to
become — a pitch for the group, a deck with speaker notes, a mail,
this very README — is a render: you iterate its recipe, a genre
interview guiding you where one exists (`/recipe presentation`), and
`/render` regenerates the output; the deck goes on to become an
actual PowerPoint file.

You save as you go (`/save`) and release when a state is worth
publishing (`/release`): the project is checked, its README and
release notes regenerate, and git carries it all.

### What it looks like in practice

A worked example from a real project will appear here once one is
published.

## 5. How the work feels

The forge is as much a way of working as a set of files, and these
are the named methods of that work — the vocabulary you and Claude
share.

- **Walkthrough.** Any list of items needing your decision — findings,
  challenges, open threads, differences between two requirement sets
  — is worked one item at a time, in order of weight: Claude's
  recommendation with a one-sentence reason, then your verdict in a
  word or a counter-proposal, and "leave it open" is a legitimate
  answer. Never a table asking for every verdict at once; the verdicts
  are carried in the conversation and written once at the end of the
  round.
- **Propose, never decide.** Claude criticises, challenges, inspires
  and lays out options; you compose.
- **Step by step.** Anything hard to reverse — a write, a commit, a
  push, a rename — arrives as one step naming the exact operation and
  its reason, and runs on your word; a plan you have seen is not
  consent for its steps.
- **Elicitation interview.** Claude draws out by questions what you
  have not yet articulated, never filling a gap by assumption.
- **Draft early.** An early draft is an elicitation tool, not an
  output: concrete text sharpens your reaction.
- **Reflect back.** Before anything is written, Claude restates what
  it understood, so the write confirms rather than surprises.
- **Intent-first.** A change of substance goes into the intent and
  propagates from there; only wording is fixed downstream directly.
- **Recommend, do not push.** Every option comes with a recommendation
  and its reason, stated once; a declined recommendation is not
  re-argued without new facts.

None of these is a command: you invoke any of them in a word.

## 6. Roles

| Role | What they own |
|---|---|
| **Principal** | Whoever's thinking is being forged: supplies ideas, answers and decisions, and is the final authority on all content. |
| **Claude** | The principal's cognitive extension: owns structure, order, process discipline and document hygiene; criticises, challenges, inspires and lays out options; proposes, never decides. |

The standing rules: when unsure, Claude asks and never fills a gap by
assumption; it never introduces a convention, prefix or section on its
own — it proposes, waits for the decision, then writes it down; many
iterations are the normal mode; for key topics it researches current
practice before inventing; every critique and checklist is advisory,
and only the principal publishes; artefacts are written once per
iteration round, on the principal's confirmation; and one mechanism
lives in one place — whatever the forge has a procedure for is used
through its own definition, never improvised.

One instance serves one principal; recipients collaborate through the
artefacts, not through the instance — more principals means more
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

Adding a layer is one definition file declaring its inputs — nothing
is renumbered and nothing existing is reworked, which is why files
are numbered in tens. The boundary between chain and render is
authorship: a chain artefact is composed by the principal, a render
is generated from artefacts — the article and its translation in the
diagram illustrate it.

| File | What it is |
|---|---|
| `00-brief.md` | The idea as the principal wrote it; later wholes as `00-brief-<name>.md`. |
| `10-intent.md` | The working understanding — positions, open threads, rejected directions — rewritten freely. |
| `20-assignment.md` | The direction handed to the recipients, self-contained. |
| `<file>.history.md` | The Version History of each versioned document — an append-only companion beside it. |
| `decisions.md` | The principal's decisions with their reasons, append-only. |
| `ledger.md` | The single source of truth for state, freely rewritten. |
| `sources/`, `research/` | External inputs and research notes, immutable once registered, each directory catalogued by its `00-INDEX.md`. |
| `recipes/`, `renders/` | How each render is made, and the generated outputs. |
| `reviews/`, `challenges/` | One immutable dated report per reviewer run. |

> A locked **brief** is immutable — composed, then locked, never
> touched again.

The brief is an intent that is composed and then locked: the
principal's own text, free-form — prose, headings, tables, use cases,
whatever structure he finds useful, with no required content and no
IDs. It holds thoughts to be processed, not decisions: they may be
changed, reworked or dropped when mined. It is `draft` while being
composed and `approved` (1.0) once the principal locks it, and three
origins are equally legitimate: it arrives finished and is locked on
arrival; it is begun outside and finished with Claude; it is born in
the forge — `/forge brief` is the door for the latter two. A project
may have more than one: every later whole of thinking that would
otherwise land in the intent as a batch of unproven positions is born
as `00-brief-<name>.md` under the same rules. A locked brief is mined
into the single intent — positions cite it as provenance, and a whole
that dies on the way leaves the brief locked and one REJ with the
reason — while the ledger tracks how far each brief is mined
(`pending | partial | mined | dropped`).

The **intent** is the consolidated *current* state of what the
principal wants, why, what is open and what was rejected: positions
(POS), open threads (THR) and rejected directions with their reason
(REJ), each with a stable ID. It is rewritten for coherence every
round rather than appended to, with its changes recorded in its
history companion, and its audience is the principal and Claude only.
It exists because chat context dies and anything of value must live
in a file: it is the document to read when returning to a project
after weeks, instead of excavating old conversations.

The **assignment** is distilled from the intent for the recipients —
teams, colleagues, or the principal's future self — and is the one
document they receive: requirements, out-of-scope items, constraints,
assumptions, deliverables, open questions with an owner and optional
success criteria (REQ, OOS, CON, ASM, DEL, TBC, SCR). It is complete
and precise, assigning rather than solving, and self-contained.

Iteration: substance changes go intent-first and propagate to the
assignment; wording-only fixes may edit the assignment directly.
Write cadence: artefacts are written once per iteration round, on
the principal's confirmation — one version bump, one history row.

Feedback from recipients has no channel of its own: the principal
processes it and feeds conclusions back through `/forge intent`.

External inputs — transcripts, offers, documents, standards — may
arrive at any stage, even before the brief. Registration does not
imply intake: a source's role is individual — a standard to verify
against, inspiration, a counter-example, a meeting record — noted in
the resource index, and the principal alone directs how and when each
source is used; when source content enters the intent, it is his
explicit act, cited with provenance.

> A **render** is never edited by hand — what is iterated is its
> **recipe**.

**Renders and recipes.** A render is an audience-specific output
generated from the chain — a pitch for the group, an architecture
picture, an executive summary, the repository README. Its recipe
carries inputs, audience, instructions and the output template in one
versioned file; `/render <recipe>` regenerates the output in an
isolated subagent that sees only the recipe and its inputs, and every
render opens with YAML front-matter provenance citing the recipe and
each input with their versions. A render assigns nothing and is not
part of the chain — the artefacts stay the source of truth — and a
render may serve as an input of another render when the citing recipe
declares it. Every project has a README as a render of its own
`recipes/readme.md` and, if it is a thought project, release notes
from `recipes/release-notes.md`; every `/release` of the project
regenerates both.

**From Markdown to slides.** Everything is Markdown, content only: a
presentation is a `.md` saying what is on each slide. Composing a
recipe may be guided by a genre interview (`/recipe presentation`).
The one in-house conversion is `scripts/md2pptx.ps1`, which turns a
deck render into an actual PowerPoint file through headless Claude
Code with the official pptx skill, applying a `.potx` template named
by path — typically a document of a library project — or designing
the visuals itself when none is named; the `.pptx` lands beside its
source render and the Markdown stays the source of truth. All other
format conversion happens outside the forge.

## 8. Two isolated reviewers

Both reviewers run as isolated agents that see the artefacts and
nothing else — never the working conversation. They cannot be told
what we really meant: they read what is written, which is exactly
what the recipients will do, and that blindness is the source of their
value.

**Challengers** attack the substance of the thinking. They are a
growing roster of persona lenses — the first is `cto` — each defined
by the blind spots it exists to find: unstated assumptions, whether
the stated objective is the real problem, second-order effects,
organisational reality, failure modes, the serious counter-case.

The **critic** reads the documents through a roster of lenses:
`clarity` reads each artefact on its own; `essence` reads the chain
for drift, distilling each layer's essence blind and comparing it
with the layer above. The two reviewers are one shape — personas and
lenses, one agent file each from one shared skeleton — with two
outputs, CHL and FND: both invoked by hand, both reports immutable and
dated, both settled by walkthrough. Neither runs at a save; `/release`
offers `critique essence` once and runs no reviewer on its own.

Isolation is not independence. The author, the critic and the
challengers share one model family; what that family systematically
cannot see, none of them will find, so agreement between the
reviewers is never treated as validation — it only means the artefact
is consistent under one set of priors. The calibration point lies
outside the forge: review by humans or by a different model family,
invited at the principal's discretion.

### `/challenge <persona> [artefact]`

Reviews the thinking through a chosen persona, in a peer register —
direct, few and sharp, no flattery. A target narrows it to that
artefact; without one it reads the whole chain, each challenge naming
the artefact it concerns. A layer is best challenged before the next
one is first derived from it. Challenges carry a severity
(dealbreaker, major or minor) and an epistemic status; fabrication is
banned — uncertainty is stated, not papered over. The report lands in
`challenges/YYYY-MM-DD-challenge-<persona>.md`; bare `/challenge`
lists the roster and recommends a fit. A challenge is open, accepted,
rejected (with a DEC carrying the reason), parked or obsolete, and an
accepted challenge must change the intent.

### `/critique <lens> [artefact]`

Reviews document quality. `clarity` looks for ambiguity, internal
contradiction, duplication, scope hygiene and Requirement style, plus
an advisory checklist; a target is that artefact. `essence` takes
every adjacent pair of the chain — a target is that artefact against
its parent — distils the downstream artefact's essence blind, then the
upstream's, and compares: substance lost without a trace (a REJ, DEC,
DEL, TBC or the ledger's mining state), added without provenance, or
shifted in meaning; a finding is a difference of essences, not of
texts, and the report carries both distillations. Regression against
resolved findings is every lens's first step. The report lands in
`reviews/YYYY-MM-DD-critique-<lens>.md`; bare `/critique` lists the
roster. A finding is in one of four states:

- open
- resolved (an iteration of the artefact concerned)
- overruled (a DEC with its reason)
- obsolete (the passage no longer exists)

## 9. Commands

Every command is an entry point into a phase, not the only permitted
door; work on the chain is invoked by target state, never by verb.

| Command | Purpose |
|---|---|
| `/setup` | First run after cloning: fills `CLAUDE.local.md` by interview, sets the session model to Fable, offers the global git identity guard; never overwrites, runs no git operation. |
| `/new-project <slug>` | Scaffolds a project by kind — files only, never git: a thought project with its brief captured verbatim, or a library (`lib-`) of shared material. |
| `/import-project <git-url>` | Brings an existing project into `projects/` through `scripts/forge-clone.ps1`; the directory is the repository's name, the commit identity is proposed from `CLAUDE.local.md` by the URL's host. |
| `/forge [slug]` | The chain map: artefacts, versions, possible next steps, stale renders, and a recommended next step. |
| `/forge <state> [slug]` | Iterates the named artefact (`brief [name]`, `intent`, `assignment`, …) — the command is simply the name of the artefact you want to work on. |
| `/ingest [file] [slug]` | Stores and registers external input in `sources/` and indexes it; bare, it sweeps `sources/`. |
| `/render <recipe> [slug]` | Regenerates a render from its recipe in `recipes/`. |
| `/recipe [genre] [slug]` | Bare, the genre roster; with a genre (`presentation`, `readme`, `release-notes`), guided composition or iteration of a recipe. |
| `/critique [lens] [artefact] [slug]` | Bare, the lens roster; with a lens (`clarity`, `essence`), runs the critic on one artefact, one artefact against its parent, or all. |
| `/challenge [persona] [artefact] [slug]` | Bare, the persona roster; with a persona (e.g. `cto`), runs the challenger against the named artefact or the whole chain. |
| `/research <topic> [slug]` | Best-practices research, stored in `research/` and indexed. |
| `/ledger [slug]` | The quick state readout from the ledger. |
| `/check [slug]` | Conformance of a project against the current conventions; all but forge when bare. |
| `/check-forge` | Consistency check of the core and `projects/forge`. |
| `/save [slug] [-m "message"] [-Tag name]` | Commits and pushes on the current branch — no check, no renders; a tag on request. |
| `/release [slug] [-m "message"] [-Tag name]` | From `main` only: check, README and release notes re-rendered, then a save with the release message and the tag `v<major>` at an approved major. |
| `/spinoff <project> <group> <slug>` | Splits a requirement group into a project of its own, on the principal's explicit decision. |

`/forge <state>` works as a star: a thin dispatcher plus one
definition file per state, each declaring its own inputs, so a future
layer branches from any artefact by adding one file. `/ingest` stores,
registers and catalogues — nothing more: every binary file gets one
question, convert to Markdown or keep it as a functional thing, and
extracts are produced by `scripts/doc2md.ps1`, never by ad-hoc
parsing; a set of related files may live as a bundle `sources/<slug>/`
counting as one source with its own catalogue. `/save` proposes a
commit message, you confirm, and the script runs — seconds. `/release`
refuses off `main`, walks you through the check's findings, regenerates
the README and release notes from the settled sources under your eyes,
and then saves with the message `release <version>`; without a slug it
asks which repository. Plain conversation works too: the core rules
apply whether or not a command was typed.

### A typical journey

- You write your idea down as it is, or dictate it into a
  conversation, and lock it as the brief of your project
  (`/new-project`, `/forge brief`).
- Over days and sessions you answer questions one at a time; your
  intent grows in positions, open threads and rejected directions,
  reflected back to you before every write (`/forge intent`).
- You register the material that arrives — an offer, a transcript, a
  standard — and tell the forge when to use it (`/ingest`,
  `/research`).
- You send in a peer to attack the thinking and a critic to read the
  documents, and rule on every challenge and finding one at a time
  (`/challenge cto`, `/critique clarity`).
- You compose a presentation recipe in a guided interview, render the
  deck and turn it into an actual PowerPoint file
  (`/recipe presentation`, `/render`, `scripts/md2pptx.ps1`).
- You distil the assignment and hand its link to the recipients
  (`/forge assignment`).
- You save as you go, and now and then you release: your project's
  README and release notes regenerate with it (`/save`, `/release`).

## 10. Conventions

**IDs and numbering.** Every item carries an ID `PREFIX.NNNN`, all
prefixes three letters. IDs are global and stable — never renumbered;
items may move between groups without changing ID. Items are numbered
in tens (`REQ.0010`, `REQ.0020`), each new group starting at the next
hundred (`REQ.0100`, `REQ.0110`); overflow takes the next free number
anywhere. Groups are plain headings — no IDs, no metadata, no
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
signal they appear there.

**Language.** The forge dictates the output language: all documents
are written in English. The briefs are the exception, stored verbatim
in whatever language they were written. The conversation language is
per-instance configuration — it lives in `CLAUDE.local.md`.

**Requirement style.** Items use *shall* / *shall not* — never would,
could, should, might, may or MoSCoW wording. There is no priority
column and no priority tags: everything in an assignment is essential,
and an exception carries a note reading *optional*. Each item covers
one idea, is written once, in a full, correct UK English sentence, and
must not depend on an external link to be understood, agreed or later
tested. Testability is recommended, not required: assignments are
deliberately high-level, delegating concretisation through a DEL item
is a legitimate outcome, and the critic reports untestable wording as
a recommendation, never as a blocking defect. For illustration only:

> REQ.0010 The Platform shall record every request and every response
> passing through the Gateway, with the identity of the requesting
> User and the time.

**Completeness over brevity.** An assignment carries the full in-scope
substance of the intent, written as well and as precisely as
possible; nothing is omitted for brevity's sake, and length is
whatever fidelity requires. Leaving a matter out is legitimate only as
an explicit delegation — a DEL or TBC item. An assignment assigns, it
does not solve: the machinery of executing delivery belongs to the
recipients, while any apparatus the principal judges part of setting
direction may appear.

**Versioning.** Integers denote signed-off versions: `0.1, 0.2, …`
are drafts before first approval; `1.0` is approved; `1.1, 1.2, …` are
changes made after approval, not yet approved themselves; `2.0` is the
next approved version, incorporating all changes since 1.0.
Front-matter carries `version`, `date`, `status` (`draft | in_review |
approved | superseded`) and `last_change`, and status must agree with
the number. Every versioned document keeps its Version History
(Version | Modification | Author | Date — what changed and why) in its
history companion, never in its body: the body is the current state,
the companion the record. The history row of an intent, an assignment
or a later layer closes with a Notes block — one line per change for
the reader of the release notes, which are compiled from those lines.
The companion is part of its document and is handed over with it by
the link into git. Immutable documents — a locked brief, reviews,
challenges, sources, research — are never edited: corrections happen
downstream.

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

Every versioned kind keeps its Version History in an append-only
companion `<file>.history.md` beside it, with `last_change` in the
front-matter summarising the newest row. An integer version is
approved, and a recipe never is: it carries no status and stays 0.x.

**Project kinds.** A project is of kind `thought` — the chain, as
above — or `library`: shared material with no chain, only a ledger,
`sources/` and `research/` with their indexes, and a README that is
the catalogue of what it holds. A library's documents are maintained
by their owner, who may overwrite them or put a new version beside;
another project cites a library document by path and registers the
citation in its ledger's Dependencies table — a cross-repository
dependency taken knowingly, with no version pinned.

**Naming.** Project slugs are lowercase and hyphenated on disk;
display names may differ, and names must be legible to the audience.
The system's own project is `forge`; libraries carry the `lib-`
prefix.

## 11. Repository layout

```
CLAUDE.md                  # this file — universal core
CLAUDE.local.md            # instance facts (principal, conversation
                           # language) — gitignored, created by
                           # /setup from templates/CLAUDE.local.md
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
                                      # regenerated by every /release
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
- PowerShell 7 (`pwsh`) — the scripts are PowerShell, so it is needed
  on macOS and Linux too
- Python 3 (for markitdown)
- a paid Claude subscription

### Getting the forge and Claude Code

Clone this repository — it is the engine. Install Claude Code:

- Windows: `irm https://claude.ai/install.ps1 | iex`
- macOS/Linux: `curl -fsSL https://claude.ai/install.sh | bash`
- or, with Node: `npm install -g @anthropic-ai/claude-code`

Sign in on first run — usage draws from the same pool as Claude chat.
Always start `claude` from the engine root, so that `CLAUDE.md` and
`CLAUDE.local.md` load.

Then run `/setup` once. It creates `CLAUDE.local.md` from its template
and fills it with you in a short interview — who the principal is, the
conversation language, your git identities per host — gitignored and
never committed. It creates `.claude/settings.local.json` with the
session model set to Fable, the strongest available model, which the
whole forge including the blind reviewers runs on; it tells you so in
one sentence, and `/model` or editing that file changes it at any time
(permissions come from the shared `.claude/settings.json`). It closes
by offering one global git guard — `user.useConfigOnly = true`
appended to `~/.gitconfig` — so that a repository without a local
identity fails aloud instead of committing with a default; declined,
it prints the line for you to apply by hand. The identities themselves
are set per repository, proposed from your roster at every project
creation or import. `/setup` never overwrites existing files.

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
- `md2pptx.ps1` needs the `document-skills` plugin, installed once from
  an interactive Claude Code session
  (`/plugin marketplace add anthropics/skills`, then
  `/plugin install document-skills@anthropic-agent-skills`). Name a
  deck template by path (`-Template <file.potx>`) — typically a
  document of a library project — or none, in which case Claude designs
  the visuals.
- The git scripts need nothing beyond git.

### Saving and syncing

Two doors, two speeds. `/save` commits and pushes on the current
branch — no check, no render. `/release`, from `main` only, runs the
conformance check and settles its findings with you, offers
`critique essence` once, re-renders the README and release notes and
then saves with the release message and, at an approved major, the
tag `v<major>`.

Underneath, the scripts in `scripts/` are the mechanism and the only
intended door to git — reading state included. Each serves the engine
and every project repository: a bare `forge-save` commits each
repository with changes on its own and pushes where it has a remote,
reconciling remote changes by rebase and keeping the commit where
there is no origin; `forge-pull` fast-forwards and never touches a
repository with unsaved changes; `forge-status` reports without
changing anything. `main` is the released line and branches are
voluntary: `forge-branch` creates or switches — `main` switches back —
and merging stays with git, by hand or by merge request. One remote per
repository, no URL anywhere in the forge.

## 13. Scripts

| Script | Purpose | When it runs | Install note |
|---|---|---|---|
| `forge-save.ps1` | Commits and pushes one repository or every repository with changes, each its own commit; `-Tag <name>` tags and pushes the tag. | Behind `/save` and `/release`, or from the shell. | git only |
| `forge-pull.ps1` | Fast-forwards from the remotes, never touching a repository with unsaved changes; on the engine it is the upgrade. | When you want the latest engine or project state. | git only |
| `forge-status.ps1` | Reports unsaved changes, the branch, the last commit and the origin of each repository without changing anything. | Whenever you want to know where things stand. | git only |
| `forge-clone.ps1` | Clones an existing project into `projects/<repository name>`, never overwriting, and sets its local commit identity when given `-Name` and `-Email`. | Behind `/import-project`. | git only |
| `forge-branch.ps1` | Switches one repository to a branch, creating it when it does not exist; `main` switches back; refuses over unsaved changes. | When you choose to work on a branch. | git only |
| `doc2md.ps1` | Converts a binary document to a Markdown extract, which becomes the source. | Behind `/ingest`, on every binary you choose to convert. | markitdown — see Setup |
| `md2pptx.ps1` | Turns a Markdown deck render into a `.pptx` through headless Claude Code, with a `.potx` template named by path or none. | After `/render` of a presentation recipe, on your word. | `document-skills` plugin — see Setup |

## 14. Planned extensions

The chain is meant to keep growing downward: thoughts are forged as
far as the principal needs them taken. A BRD layer is certain to come;
solution architecture and integration are intended; a strategy layer
is possible if it proves to make sense. Which layers are added, and in
what order, is open, and the mechanics of a layer are designed when
that layer is actually taken up, not in advance.

More principals means more instances: a second principal receives the
forge via git and runs an instance of their own. How genuine
multi-user operation would work is an open point for the future.

`projects/forge/` is Forge of Thought itself run through its own
process — its brief, its intent with design positions, open threads
and rejected directions, its decisions and its ledger. A process
change is complete only once that intent is updated and this README
re-rendered.

## 15. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) — petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit
the author and link to this repository.

## 16. About this README

This file is a render of `projects/forge`: never edited by hand,
regenerated by `/render readme` whenever the process changes, and by
every `/release` of the engine. Fixes go into the recipe
(`projects/forge/recipes/readme.md`) or its inputs — `CLAUDE.md` and
the forge intent. The YAML front-matter provenance at the top is kept
by design; changes to the system are recorded in `projects/forge/`.

_Last updated: 2026-09-06_
