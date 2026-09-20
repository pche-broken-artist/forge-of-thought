---
project: forge
render: readme
generated: 2026-09-20
recipe: recipes/readme.md v0.49
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v4.17
---

# Forge of Thought 4.17

*A workshop where thought is tempered and shaped.* · [Release notes](RELEASE-NOTES.md)

Forge of Thought is an **AI cognitive extension** of a thinking human,
the **principal** — whoever's thinking is being forged. It is a place
where thoughts are forged: it takes a raw, half-formed idea — a process
redesign, a platform initiative, an organisational change, a D&D
campaign — and tempers it into a precise, self-contained handover for
whoever delivers it: a team, a colleague, your future self. It rests on
one principle — **the machine carries every part of the work that is
not deciding** — in three forms.

- **It thinks with you.** It interviews and probes, criticises,
  challenges and inspires; it extracts what you have not yet
  articulated and lays out options with their trade-offs. It proposes —
  you decide.
- **It keeps the work consistent.** Nothing wanders off in forgotten
  chats: the thinking lives in versioned, templated artefacts, with
  decisions, state and history keeping themselves in order and
  consistency guarded across every output.
- **It carries the tedious work.** Audience-facing outputs — a pitch, a
  deck, even this README — are **renders**: generated from the
  artefacts through recipes, regenerated whenever the thinking moves,
  never written by hand twice.

Technically, Forge of Thought is a git repository: slash commands and
isolated agents — challenger personas and critic lenses — for Claude
Code, templates, and the conventions binding them. Today the chain ends
at the assignment, the one document handed to whoever delivers; it is
built to grow further down without reworking anything that exists.

Short on time? Two one-page notes say it briefly:
[for a CTO](projects/forge/renders/cto-pitch.md) and
[for a CEO](projects/forge/renders/ceo-pitch.md). Each has a Word
version beside it.

## 1. Better with AI, or replaced by it?

Forge of Thought is for those who chose to be better. The failure modes
it exists to remove:

- Thinking scattered across chat sessions that die, taking their
  context with them.
- Handovers whose completeness depends on the mood of the day they were
  written.
- The same thinking retold to every audience — a pitch, a deck, a
  mail — each version rewritten by hand and drifting from the others.
- Feedback and decisions with no place to land, so the same ground is
  fought over twice.
- Assumptions nobody attacked before reality did.

## 2. What you get

- A versioned document chain growing from a **brief** — your own text,
  locked verbatim once it is done — to a self-contained **assignment**,
  the direction handed to those who deliver.
- An elicitation interview that forges the **intent** — the working
  understanding of what you want, why, what is the case, what is open
  and what was rejected.
- Blind adversarial reviewers, every verdict recorded.
- Audience-specific renders generated from recipes, including an actual
  PowerPoint file through your own template.
- External sources registered immutably and used only as the principal
  directs.
- Everything in files and git — nothing depends on a chat's memory.

## 3. Quickstart

First, once per machine:

```
git clone <this repository>   # you are looking at it
                              # install Claude Code first — see Setup
claude                        # always from the engine root
/setup                        # first run only — fills CLAUDE.local.md,
                              # sets the model, Fable
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
                                # identity is git's, resolved from your
                                # own configuration
/forge <project-slug>           # the slug is the repository's name;
                                # select the project before any work —
                                # the forge cannot guess it
```

Each project lives inside `projects/<slug>/` as a git repository of its
own, which the engine does not track — that is why you name it first.

## 4. How it is used

### The flow

A thought arrives — a platform that needs rethinking, or a campaign
taking shape for your D&D table. You dump it as it is: prose, headings,
a table, whatever shape it has in your head. That is the brief. You can
hand it over finished, or grow it in conversation with the forge
(`/forge brief`), where Claude clarifies where you are terse and checks
the thought against what already exists in the world.

From the brief the intent is forged. `/forge intent` is mostly an
interview: one question at a time, your answers reflected back, and at
the end of the round one write into the file. You come back the next
day, or three weeks later, and nothing has to be excavated from old
chats — the intent says where you stand. Material arrives along the
way: a security standard you downloaded goes in through `/ingest` and
sits there, registered, until you say "now verify the intent against
it". Where a topic deserves it, `/research` looks up how others solve
the same thing, so that you are not reinventing the wheel.

When the thinking feels solid, you let the blind reviewers at it. A
challenger goes after the substance — the assumption you never stated,
the second-order effect you did not see. A critic goes after the
documents — the ambiguity, the drift between what the brief said and
what the intent now claims. They report; you go through their points
one at a time and rule on each. Nothing they say stops you.

Then the assignment is distilled for the people who will deliver
(`/forge assignment`): complete, precise, readable without you in the
room.

Around the chain live the renders. The group wants a pitch? You do not
write a pitch; you compose its **recipe** — one file saying what goes
in, who it is for and what shape comes out, optionally through a genre
interview (`/recipe presentation`) — and `/render` generates it, down
to an actual PowerPoint file. A pitch, slides, a mail: each is
regenerated whenever you ask, and this very README at every release.
`/save` as you go and `/release` when a state deserves a name keep all
of it in git.

### What it looks like in practice

A worked example from a real project will appear here once one is
published.

## 5. How the work feels

The forge is as much a way of working as a set of files, and these are
the named methods of that work — the vocabulary you and Claude share.

- **Walkthrough.** Whenever a list of items needs your decision —
  findings, challenges, open threads — Claude puts one item per message
  in front of you, heaviest first, and your verdicts are written
  together at the round's end. Whatever produces such a list ends by
  offering one, and a small per-prompt hook keeps the one-item rule
  alive through a long conversation.
- **Propose, never decide.** Claude criticises, challenges, inspires
  and lays out options, and you compose what enters the content.
- **Step by step.** Anything that needs your consent — a write, a
  commit, a push, a rename, the birth of a new versioned document —
  arrives as one step naming the exact operation, its target and the
  reason, and runs only on your word.
- **Elicitation interview.** Claude draws out by questions, one per
  message, what you have not yet articulated, instead of filling the
  gaps by assumption.
- **In pieces.** You may send one longer thought as several messages
  and close it with a word such as "done"; until then Claude only
  acknowledges, and afterwards works the pieces as one input.
- **Draft early.** An early draft is a tool for drawing out your
  reaction, not an output, because concrete text sharpens it.
- **Reflect back.** Before anything is written Claude restates what it
  understood, so that the write confirms rather than surprises.
- **Intent-first.** A change of substance goes into the intent and
  propagates from there, while wording alone may be fixed downstream.
- **Recommend, do not push.** Every option comes with a recommendation
  and its reason, stated once, and a declined recommendation is not
  argued again without new facts.

None is a command: you invoke any of them in a word.

## 6. Roles

| Role | What they own |
|---|---|
| Principal | Ideas, answers and decisions; the final authority on all content. |
| Claude | Structure, order, process discipline and document hygiene — an amplifier of the principal's thinking, never its substitute. |
| Recipients | The assignment once handed over, and the machinery of delivering it; they may be teams, colleagues or the principal's future self. |

The standing rules of the collaboration: when unsure, Claude asks and
never fills a gap by assumption — and a contradiction, a gap or a risk
it finds in a source is raised at once, as one question naming what
does not fit. Claude never introduces a new convention, prefix or
section on its own: it proposes, waits for a decision and then writes
it down. Many iterations are the normal mode. For key topics Claude
researches current best practice rather than inventing. Reviews and
checklists advise and never block: only the principal publishes. State
lives in files, never only in conversation, so a session can end at any
point without loss. Whatever the forge has a mechanism for — a command,
a script, an agent — is used through that mechanism, never improvised
beside it.

One instance serves one principal, and the recipients collaborate
through the artefacts; more principals means more instances (see
Planned extensions).

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

Adding a layer is one definition file declaring its inputs — nothing is
renumbered and nothing existing is reworked, which is why files are
numbered in tens. The boundary between the chain and its renders is
authorship: a chain artefact is composed by the principal, a render is
generated from artefacts — the article and its translation in the
diagram illustrate it.

Each project carries its chain in `projects/<slug>/`:

| Document | What it is | Behaviour |
|---|---|---|
| `00-brief.md` | The idea as it emerged, in whatever structure the principal finds useful. | Draft until locked at 1.0. |
| `00-brief-<name>.md` | A later whole of thinking, born under the same rules. | Draft until locked at 1.0. |
| `10-intent.md` | The consolidated current understanding, for principal and Claude only. | Rewritten freely, versioned. |
| `20-assignment.md` | The direction handed to the recipients, self-contained. | Rewritten freely, versioned. |
| `<file>.history.md` | The Version History of the versioned document beside it. | Append-only. |
| `decisions.md` | The principal's decisions with their reasons (DEC). | Append-only. |
| `ledger.md` | The single source of truth for state. | Freely rewritten. |
| `sources/` | External inputs as they arrived, catalogued in `00-INDEX.md`. | Immutable once registered. |
| `research/` | Durable answers to one question each, catalogued in `00-INDEX.md`. | Immutable. |
| `reviews/`, `challenges/` | One dated report per reviewer run. | Immutable. |
| `recipes/`, `renders/` | How a render is made, and the generated output. | Recipe iterated, render overwritten. |

> A locked brief is immutable — composed, then locked, never touched again.

**The brief** is an intent that is composed and then locked: `draft`
while it is being written, `approved` (1.0) once the principal locks
it. It is free-form — prose, headings, tables, use cases — with no
required content and no IDs, because a required structure would force
premature tidiness; it holds thoughts to be processed rather than
decisions, so they may be changed, reworked or dropped on the way.
Three origins are equally legitimate and the forge does not tell them
apart: the brief arrives finished and is locked on arrival; it is begun
outside and finished with Claude; or it is born in the forge from the
first word — `/forge brief [name]` is the door for the latter two. A
brief born by elicitation carries the whole pile — your words unmarked,
every other block opening with its origin, *(Claude)* or *(source:
path)* — since the intent is where the pile is sorted. A project may
have more than one: every later whole of thinking is born as
`00-brief-<name>.md` under the same rules. A locked brief is mined into
the single intent, its positions citing the brief as provenance, and
the ledger tracks how far each brief is mined (`pending | partial |
mined | dropped`).

**The intent** is the consolidated *current* state of what the
principal wants: positions (POS), facts (FCT), open threads (THR) and
rejected directions with their reason (REJ), each with a stable ID. It
is rewritten for coherence every round rather than appended to, with
the changes recorded in its history companion, and its audience is the
principal and Claude only. It exists because chat context dies and
anything of value must live in a file: it is the document to read when
returning to a project after weeks, instead of excavating old
conversations. An intent that Claude consolidated from a conversation,
rather than composed item by item with the principal, stays `in_review`
until every position has been walked through, and no lower layer is
derived before that.

**The assignment** is distilled from the intent for the recipients and
is the one document they receive: requirements, out-of-scope items,
constraints, assumptions, deliverables, open questions with an owner
and optional success criteria (REQ, OOS, CON, ASM, DEL, TBC, SCR). It
is complete and precise, assigning rather than solving, and
self-contained — it carries a Terms section so that it can be forwarded
without oral tradition. It is shaped so because the recipients were not
in the room: whatever they need to understand, agree and later test
must be in the document itself.

The **ledger** holds the state of all of this — briefs, documents,
renders, sources, research, dependencies, findings and challenges — and
is kept current after every operation. It cites and never copies: a
matter with an ID gets one line, and its substance stays in the thread
or the record it belongs to. Reviews, challenges, sources and research
are never edited after they are created or registered; corrections
happen downstream.

Iteration: substance changes go into the intent first and propagate to
the assignment; wording-only fixes may edit the assignment directly.

Write cadence: artefacts are written once per iteration round, on the
principal's confirmation — one version bump and one history row per
round — and "written" always means a named file.

Feedback from recipients has no channel of its own: the principal
processes it and feeds the conclusions back through `/forge intent`.

> A render is never edited by hand — what is iterated is its recipe.

**Renders and recipes.** A render is an audience-specific output
generated from the chain — a pitch for the group, an architecture
picture, an executive summary, this README. Its recipe
(`recipes/<recipe>.md`) holds the inputs, the audience, the
instructions and the output template in one versioned file; `/render
<recipe>` regenerates the output into `renders/<recipe>.md`, or into
the recipe's own `output:` path, in an isolated subagent that sees only
the recipe and its inputs. Every render opens with YAML front-matter
provenance citing the recipe and each input with their versions, and
the ledger mirrors it. A render assigns nothing and is no part of the
chain — the artefacts stay the source of truth — and a render may serve
as an input of another render when the citing recipe declares it. A
regenerated render passes under the principal's eyes: a recipe pins
load-bearing wording as fixed text, and Claude never regenerates on its
own judgement — it reports staleness and offers.

**From Markdown to slides.** Everything the forge produces is Markdown,
content only, and a presentation is a Markdown file saying what is on
each slide. Composing a recipe may be guided by genre (`/recipe
presentation`). `scripts/md2pptx.ps1` turns a deck render into an
actual PowerPoint file, with a `.potx` template named by path —
typically a document of a library project. `scripts/md2docx.ps1` turns
any render into a Word file through pandoc, its styles taken from a
reference `.docx` or Word template named by path, the page A4 by
default, Mermaid diagrams left as blocks of code. The Markdown stays
the source of truth, and all other format conversion happens outside
the forge.

## 8. Isolated reviewers

The reviewers work from a clean context: they run as isolated subagents
that see the project's documents only, never the working conversation —
they cannot be told what we really meant, and that blindness is the
source of their value. Every kind of reviewer is of one shape: one
agent file per lens, persona or check, the behaviour shared by the kind
held in one contract, a run by hand on the session model, and a
walkthrough to settle what it found. Their jobs are strictly separate,
because an agent that audits the document and challenges the thinking
at once does neither properly. Every finding and every challenge is
either fixed or explicitly overruled with a recorded reason; overruling
and parking are legitimate, silently ignoring is not. New lenses,
personas and checks come only by the principal's decision, and only
where what they find genuinely differs.

Isolation is not independence. The author, the critic and the
challengers share one model family: what that family systematically
cannot see, none of them will find, so agreement between the reviewers
is never treated as validation — it only means the artefact is
consistent under one set of priors. The calibration point lies outside
the forge: review by humans, or by a different model family, invited at
the principal's discretion.

### Critic (`/critique`)

The **critic** judges the quality of the documents, never the substance
of the thinking. Command: `/critique <lens> [artefact]` — bare, it
lists the roster and recommends a fit; without an artefact, the whole
chain.

- `clarity` — reads each artefact on its own for ambiguity,
  contradiction, duplication, scope hygiene and Requirement style.
- `essence` — reads the chain for drift: distils each layer's essence
  blind and compares it with the layer above.

Output: an immutable dated report in
`reviews/YYYY-MM-DD-critique-<lens>.md` and findings (`FND`) in the
ledger. A finding is in one of these states:

- `open`
- `resolved`
- `overruled` (→ a DEC record with the reason)
- `obsolete`

### Challenger (`/challenge`)

The **challenger** judges the substance of the thinking, never the
quality of the documents. Command: `/challenge <persona> [artefact]` —
bare, it lists the roster and recommends a fit; without an artefact,
the whole chain. Each run brings three to seven sharp challenges,
ordered by severity, each with a falsifiable "what would change my
mind" and an epistemic status, and nothing fabricated: a precise "I
don't know" beats an invented figure. An artefact is best challenged
before the next layer is first derived from it, while accepted
challenges are still cheap to absorb.

- `cto` — a CTO-level peer reviewer who goes after unstated
  assumptions, blind spots, second-order effects and organisational
  reality.

Output: an immutable dated report in
`challenges/YYYY-MM-DD-challenge-<persona>.md` and challenges (`CHL`)
in the ledger. A challenge is in one of these states, and an accepted
one must change the intent:

- `open`
- `accepted`
- `rejected` (→ a DEC record with the reason)
- `parked`
- `obsolete`

### Checks (`/check`)

A check judges mechanical conformance with the conventions, never
substance or quality. Command: `/check <check> [slug]` — bare, it lists
the roster; it takes a project by its slug, or the engine. Each check
owns one concern and none another's, and checks never call each other:
which of them run at a save or a release is the calling command's
business.

- `light` — verifies a project's bookkeeping: front-matter against the
  history companion, the ledger against the files, dependencies and
  resource indexes against the directories; fit for a save.
- `project` — verifies a project's structure, IDs, assignment style,
  language, immutable documents, recipes and renders.
- `engine` — verifies the core against itself and against the forge's
  own intent.
- `single-source-of-truth` — sweeps the whole operating layer for a
  rule or procedure written in two places and for a direct operation
  where a mechanism exists; expensive by design and run on the
  principal's word.

Output: nothing filed — the report returns to the session, where each
finding is settled in one of these ways:

- fix
- defer
- accept

## 9. Commands

Commands are entry points into phases of the work, addressed to Claude
Code from the engine root.

| Command | Purpose |
|---|---|
| `/setup` | First run after cloning: fills `CLAUDE.local.md` by interview, sets the session model and offers the git identity per host. It never overwrites and runs no git operation. |
| `/new-project <slug>` | Scaffolds a project by kind — a thought project with its brief captured verbatim, or a library (`lib-`) of shared material. Files only, never git. |
| `/import-project <git-url>` | Brings an existing project into `projects/`; the directory is the repository's name. |
| `/forge [slug]` | The chain map: which artefacts exist at what versions, what can be worked from here, which renders are stale — with a recommended next step. |
| `/forge <state> [slug]` | Iterates the named artefact (`brief [name]`, `intent`, `assignment`, …). |
| `/ingest [file] [slug]` | Stores, registers and indexes external input — a file, or text pasted into the conversation. Bare, it sweeps `sources/`. |
| `/render <recipe> [slug]` | Regenerates a render from its recipe in `recipes/`. |
| `/recipe [genre] [slug]` | Bare, the genre roster; with a genre (`presentation`, `readme`, `release-notes`), guided composition — or iteration — of a recipe. |
| `/critique [lens] [artefact] [slug]` | Bare, the lens roster; with a lens (`clarity`, `essence`), runs that critic on the named artefact, else on all. |
| `/challenge [persona] [artefact] [slug]` | Bare, the persona roster; with a persona (e.g. `cto`), runs that challenger against the named artefact, else the whole chain. |
| `/research <topic> [slug]` | Best-practice research, stored in `research/` and indexed. |
| `/ledger [slug]` | The quick state readout, straight from the ledger. |
| `/check [check] [slug]` | Bare, the check roster; with a check (`light`, `project`, `engine`, `single-source-of-truth`), runs it on the named project or on the engine. |
| `/save [slug] [-m "message"] [-Tag name]` | Saves one repository, or every one with changes; a tag on request. |
| `/release [slug] [-m "message"] [-Tag name]` | Releases one repository from `main`. |
| `/spinoff <project> <group> <slug>` | Splits a requirement group into a project of its own — only ever on the principal's explicit decision. |
| `/man [command \| method]` | The forge's manual, read from its own definitions: bare, the commands and working methods; with a name, that command's arguments and roster or that method's paragraph. |
| `/manual …` | Alias of `/man`. |

`/forge <state>` needs no memorising: the command is simply the name of
the artefact you want to work on — `/forge intent`, `/forge
assignment` — and a future layer adds its own name, nothing else. Bare
`/forge` and `/ledger` differ in depth: the first reads the chain and
recommends, the second only reports what the ledger says.

`/ingest` stores, registers and catalogues — nothing more. Registration
does not imply intake: a source's role is individual — a standard to
verify against, inspiration, a counter-example, a meeting record — so
after registering, Claude asks what the source is for and notes the
answer in the directory's index, and the principal alone directs how
and when it is used. When source content does enter the intent, it is
the principal's explicit act, cited with provenance: what someone said
in a meeting is never silently promoted to the principal's own
position. A source has one form: for every binary file `/ingest` asks
whether to convert it to Markdown, and the extract then is the source;
a functional binary such as a deck template is kept as it is. Before
storing anything, personal matter stops the command and asks — store,
redact or drop. `/save` and `/release` are two doors at two speeds —
the first takes seconds, the second minutes, because only a release
renders; what each runs is laid out under Saving and syncing in Setup.
`/save` proposes its commit message for your confirmation. Named
without a slug, `/release` asks which repository and never sweeps; it
reports what materially changed in the renders it regenerated, so that
you rule on the delta before the release commit.

Commands that write, scaffold, commit or regenerate start only on your
word; maps, reports and rosters Claude may propose on its own. Plain
conversation works too: commands are doors, not the only permitted
ones, and the rules of the forge hold in ordinary conversation as well.

### A typical journey

- You write down an idea as it is, or talk it into shape with Claude,
  and lock it as the brief of your project (`/new-project`, `/forge
  brief`).
- You are interviewed until the intent says what you want and why, and
  you come back to it over days, each round ending in one write
  (`/forge intent`).
- You drop in the documents that matter and say what each is for
  (`/ingest`), and ground a key topic in how others solve it
  (`/research`).
- You put the thinking under pressure: a challenger on the substance, a
  critic on the documents (`/challenge cto`, `/critique clarity`), and
  you rule on each of their points, one at a time — accept, overrule
  with a reason, or park.
- You need to present it: you compose a presentation recipe through the
  genre interview, render it and build the PowerPoint file (`/recipe
  presentation`, `/render`, `scripts/md2pptx.ps1`).
- You distil the assignment for the people who will deliver, and have
  it checked against the intent for drift (`/forge assignment`,
  `/critique essence`).
- You save as you go, and release when a state deserves a name
  (`/save`, `/release`).

## 10. Conventions

**IDs and numbering.** Every item carries an ID of the form
`PREFIX.NNNN`, all prefixes three letters. IDs are global and stable —
never renumbered — and items may move between groups without changing
theirs. Items are numbered in tens (`REQ.0010`, `REQ.0020`), each new
group starting at the next hundred (`REQ.0100`, `REQ.0110`); overflow
takes the next free number anywhere. Groups are plain headings with no
IDs, no metadata and no lifecycle, two levels deep at most. Structured
items beat prose even at very high abstraction: narrative is confined
to Purpose & Context and Objective.

| Prefix | Meaning | Lives in |
|---|---|---|
| REQ | requirement | assignment |
| OOS | out of scope / do-not | assignment |
| CON | constraint — a deliberate boundary, not to be challenged | assignment |
| ASM | assumption | assignment |
| DEL | deliverable — may delegate work ("produce NFRs and return") | assignment |
| TBC | open question / to be confirmed, with owner | assignment |
| SCR | success criterion — optional or delegated | assignment |
| POS | position the principal currently holds | intent |
| THR | open thread — an unresolved matter to elicit next | intent |
| REJ | rejected direction, with the reason it was dropped | intent |
| FCT | fact — what is the case, not a stance | intent |
| FND | critique finding (document quality) | ledger, reviews |
| CHL | peer-review challenge (substance) | ledger, challenges |
| DEC | decision, incl. overruled findings and rejected challenges | decisions.md |

A fact is what the principal states or what a source states, cited to
its file where one exists; verification is never demanded. A thread
carries its origin — the principal's word (the default, unmarked), a
source by path, or Claude's synthesis — so that a hypothesis of Claude's
stays visibly his until the principal takes it up.

**Terms.** Every assignment's Terms section lists the prefixes and the
domain terms it actually uses. Defined terms are capitalised in item
text to signal that they appear there.

**Language.** The forge dictates one output language per project: the
artefacts of the chain — intent, assignment, later layers — are written
in the language the project's ledger header declares (`language`,
English when absent). The briefs are the exception, stored verbatim in
whatever language they were written. Everything else a project holds —
ledger, decisions, history, reviews, challenges, indexes, research,
recipes — is always English, as is the notation: ID prefixes, `shall`,
status words, front-matter keys. A render may be in any language its
recipe declares. The language of the working conversation is
per-instance configuration and lives in `CLAUDE.local.md`.

**Requirement style.** Requirements use *shall* and *shall not*; would,
could, should, might, may and MoSCoW wording are not used. There is no
priority column and there are no priority tags: everything in an
assignment is essential, and an exception carries a note reading
*optional*. Each item covers one idea, is written once, and is written
in full, correct UK English sentences. Testability is recommended, not
required: assignments are deliberately high-level, and delegating the
concretisation through a `DEL` item is a legitimate outcome — as is
delegating the success criteria. An item must not depend on an external
link to be understood, agreed or later tested. An illustrative item,
not taken from any project:

> REQ.0010 The Platform shall record every request and every response passing through the Gateway, with the identity of the requesting User and the time.

**Completeness over brevity.** An assignment carries the full in-scope
substance of the intent, written as well and as precisely as possible;
nothing is omitted for brevity's sake, and length is whatever fidelity
requires. Leaving a matter out is legitimate only as an explicit
delegation — a `DEL` or a `TBC` item. An assignment assigns, it does
not solve: the machinery of executing delivery belongs to the
recipients, and the boundary is the kind of content, never its amount.

**Versioning.** Integers denote signed-off versions.

- `0.1, 0.2, …` — drafts before the first approval
- `1.0` — approved
- `1.1, 1.2, …` — changes made after approval, not yet approved
  themselves
- `2.0` — the next approved version, incorporating all changes since
  1.0

Front-matter carries `version`, `date`, `status` (`draft | in_review |
approved | superseded`) and `last_change`, and the status must agree
with the number.

**Document kinds.** "Document" is the word for every file of a project;
"artefact" is reserved for the documents of the chain.

| Group | Kind | Meaning | Written by | Versioned | Behaviour |
|---|---|---|---|---|---|
| artefacts | brief | the idea as it emerged: the principal's words alone when handed over finished, the whole pile of the elicitation when born in the forge | principal, with Claude's part marked | yes | locked at 1.0, then immutable |
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

Every versioned kind keeps its Version History in an append-only
companion `<file>.history.md` beside it, never in its body, and the
`last_change` line of the front-matter summarises the newest row. An
integer version is approved, and a recipe never is: it carries no
status and stays 0.x.

**Project kinds and naming.** A project has a kind, declared in the
header of its ledger: `thought` — the chain, the default — or
`library`, a collection of material shared across projects, with
sources and research but no chain, maintained by its owner and cited by
other projects by path; such a citation is registered in the citing
project's ledger as a dependency. A library's slug carries the prefix
`lib-`. Slugs are lowercase and hyphenated on disk, and display names
may differ: the system's own project has the slug `forge` and the full
name Forge of Thought in documents.

## 11. Repository layout

```
CLAUDE.md                  # the universal core Claude works from
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
                           # PowerPoint), md2docx (render → Word),
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
                                      # recipes
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
  renders/<recipe>.docx               # optional Word file generated from
                                      # the md render by scripts/md2docx.ps1
  reviews/YYYY-MM-DD-critique-<lens>.md  # immutable critique runs
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

- git
- PowerShell 7 (`pwsh`) — the scripts are PowerShell, so it is needed
  on macOS and Linux too
- Python 3 (for markitdown)
- a paid Claude subscription

### Getting the forge and Claude Code

Clone this repository — it is the engine. Then install Claude Code:

```
# Windows
irm https://claude.ai/install.ps1 | iex

# macOS / Linux
curl -fsSL https://claude.ai/install.sh | bash

# or, anywhere
npm install -g @anthropic-ai/claude-code
```

Sign in on the first run — usage draws from the same pool as Claude
chat. Always start `claude` from the engine root, so that `CLAUDE.md`
and `CLAUDE.local.md` load.

Then run `/setup` once. It fills `CLAUDE.local.md` — the conversation
language, who the principal is — from its template with you in a short
interview; the file is gitignored and never committed. It creates
`.claude/settings.local.json` with the session model set to Fable, the
strongest available model, which the whole forge including the blind
reviewers runs on; it tells you so in one sentence, and `/model` or
editing that file changes it at any time (permissions come from the
shared `.claude/settings.json`). It closes with your git identity,
which is git's own: it asks for the hosts you push to, with a name and
an e-mail for each, and offers to write the `includeIf` stanzas into
your `~/.gitconfig` — one identity per host, resolved by git from the
remote's URL — together with one global guard, `user.useConfigOnly =
true`, so that a repository on a host with no stanza fails aloud
instead of committing with a default; declined, it prints the lines for
you to apply by hand. The forge itself sets no identity anywhere.
`/setup` never overwrites existing files.

### Your projects

Each project is a directory under `projects/` and a git repository of
its own. `/new-project` creates the files; `git init` in that directory
(`git -C projects/<slug> init -b main`) and a remote, if you want one,
are a one-off act of yours, and the commit identity is git's, resolved
per host from your own configuration. An existing project is brought in
with `/import-project <git-url>`, which clones it into
`projects/<repository name>` through `scripts/forge-clone.ps1` and
reports the identity git resolves for it. The engine ignores
`projects/*` (except its own `projects/forge`), and the scripts find
your project through its `.git`. A project without a repository is
reported as "not under git" — a fact, not an error.

### Script prerequisites

- `doc2md.ps1` needs markitdown:
  `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.
- `md2pptx.ps1` needs the `document-skills` plugin, installed once from
  an interactive Claude Code session (`/plugin marketplace add
  anthropics/skills`, then `/plugin install
  document-skills@anthropic-agent-skills`). A deck template is named by
  path (`-Template <file.potx>`) — typically a document of a library
  project — or not at all, in which case Claude designs the visuals.
- `md2docx.ps1` needs pandoc (https://pandoc.org/installing.html). A
  reference document is named by path (`-Reference`, a `.docx`, `.dotx`
  or `.dotm`) or not at all, in which case pandoc's built-in styles
  apply on an A4 page (`-PageSize Letter` for US Letter).
- The git scripts need nothing beyond git.

### Saving and syncing

There are two doors. `/save` runs the `light` check, then commits and
pushes on the current branch — no render. `/release`, from `main` only,
runs its checks and settles their findings with the principal, offers
`critique essence` once, re-renders the README and the release notes,
and then saves with the release message and, at an approved major, the
tag `v<major>`.

Underneath, the scripts in `scripts/` are the mechanism and, for Claude
and every command of the forge, the only door to git. Each serves the
engine and every project repository: a bare save commits each
repository with changes on its own and pushes where it has a remote.
`main` is the released line and branches are voluntary — `forge-branch`
creates one or switches to it, and merging stays with git. There is one
remote per repository, and no URL is written anywhere in the forge.

### Upgrading

Upgrading the engine is `scripts/forge-pull.ps1`, a fast-forward of
`main`; your projects are untouched by it and record no engine version.
Read `RELEASE-NOTES.md`, the *Action required* lines first: they say
what a new version expects of your projects and your instance files.
Then, project by project, run `/check project <slug>`: it measures the
project against the current conventions and reports what no longer
conforms, nothing else. Go through the findings with Claude one at a
time and agree what to migrate and how; Claude makes the changes on
your word, in the session, with no migration tool in between — the
check and the release notes are the tool. A project you leave as it is
stays valid under the conventions it was written to; migrating it is
your decision, per project, never assumed.

## 13. Scripts

All scripts are cross-platform PowerShell 7, written to run unchanged
on Windows, Linux and macOS; they carry no URL and no identity.

| Script | Purpose | When it is run | Install note |
|---|---|---|---|
| `forge-save.ps1` | Commits and pushes the engine and every project repository with changes, or the one named. | By `/save` and `/release`, or from the shell. | — |
| `forge-pull.ps1` | Fast-forwards from the remotes; on the engine it is the upgrade channel. | When you upgrade the engine or sync a project. | — |
| `forge-status.ps1` | Reports the state of the engine and every project without changing anything. | Whenever you want to know what is unsaved and where. | — |
| `forge-clone.ps1` | Brings an existing project into `projects/`. | By `/import-project`. | — |
| `forge-branch.ps1` | Switches to a branch or creates it; merging is git's. | When you choose to work on a branch. | — |
| `doc2md.ps1` | Converts a document into the Markdown extract that then is the source. | By `/ingest`, on the principal's word. | markitdown — see Setup |
| `md2pptx.ps1` | Turns a Markdown deck render into a `.pptx` through headless Claude Code. | After rendering a presentation. | `document-skills` plugin — see Setup |
| `md2docx.ps1` | Turns a Markdown render into a `.docx` through pandoc, deterministically. | After rendering a document. | pandoc — see Setup |
| `hook-walkthrough.ps1` | Repeats the one-item walkthrough rule and three lines of conduct. | By Claude Code at every prompt, configured in `.claude/settings.json`. | — |

## 14. Planned extensions

The chain is meant to grow downward: thoughts are forged as far as the
principal needs them taken. A BRD layer is certain to come; solution
architecture and integration are intended; a strategy layer is possible
if it proves to make sense. Which layers are added, and in what order,
is open, and nothing is approved for construction: the mechanics of a
layer are designed when that layer is actually taken up, not in
advance. The layers below the assignment grow in the same project, by
the same principal's hand; the chain never spans two principals — what
a recipient does with an assignment in an instance of his own is his
own forge run, in which the assignment becomes his brief.

More principals means more instances: a second principal receives the
forge through git and runs an instance of their own, coordinating
through git. Genuine multi-user operation is an open point,
deliberately not worked on now. Challengers running on a different
model family than the author's, so that a challenge comes with
genuinely different priors, are a decided direction whose mechanics are
still to be designed.

`projects/forge/` is Forge of Thought itself run through its own
process — its brief, its intent with the design positions, open threads
and rejected directions, its decisions and its ledger. A change to the
process is complete only once that intent is updated and this README
re-rendered.

## 15. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) — petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit
the author and link to this repository.

## 16. About this README

This file is a render of `projects/forge`: never edited by hand,
regenerated by `/render readme` whenever the process changes and by
every `/release` of the engine. Fixes go into the recipe
(`projects/forge/recipes/readme.md`) or into its inputs, never here.
The YAML front-matter at the top is provenance — the recipe and the
inputs with their versions — and is kept by design. Changes to the
system itself are recorded in `projects/forge/`.

_Last updated: 2026-09-20_
