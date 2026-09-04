---
project: forge
render: readme
generated: 2026-09-04
recipe: recipes/readme.md v0.35
inputs:
  - CLAUDE.md
  - projects/forge/10-intent.md v3.23
---

# Forge of Thought 3.23

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
Code, templates, and the conventions binding them. Today the chain runs
from a brief through an intent to an assignment, and ends there; the
numbering of its files leaves room for layers below.

## 1. Better with AI, or replaced by it?

Forge of Thought is for those who chose to be better. The failure modes
it exists to remove:

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

- A versioned document chain growing from a **brief** — your own text,
  locked verbatim once it is done — to a self-contained **assignment**.
- An elicitation interview that forges the **intent**: what you want,
  why, what is open and what you rejected.
- Two kinds of blind adversarial reviewers — one on the thinking, one
  on the documents — with every verdict recorded.
- Audience-specific renders generated from recipes, including an
  actual PowerPoint file through your own template.
- External sources registered immutably and used only as the principal
  directs.
- Everything in files and git — nothing depends on a chat's memory.

## 3. Quickstart

**First, once per machine**

```
git clone <this repository>   # you are looking at it
# install Claude Code — see Setup below
claude                        # always from the engine root
/setup                        # first run only — fills CLAUDE.local.md,
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
                                # CLAUDE.local.md roster and confirmed
                                # by you
/forge <project-slug>           # the slug is the repository's name;
                                # select the project before any work —
                                # the forge cannot guess it
```

Each project lives inside `projects/<slug>/` as a git repository of its
own, which the engine does not track — that is why you name it first.

## 4. How it is used

### The flow

A thought arrives — a process you want redesigned, a platform you want
built, a campaign taking shape for your D&D table. You dump it as it
is, in whatever shape it came, into a brief: alone, or in conversation
with the forge (`/forge brief`) until it says what you mean. Then you
lock it, and from that moment it is the fixed point everything later is
measured against.

From the brief the intent is forged. The forge interviews you
(`/forge intent`), one question at a time, reflects back what it
understood, and writes only when you confirm. This runs over days and
sessions; everything lives in files, so you can close the terminal
mid-thought and the next session picks up from the ledger (`/ledger`)
rather than from a scrollback that no longer exists.

Material arrives whenever it arrives. You drop a downloaded security
standard into `sources/` and `/ingest` registers and catalogues it —
nothing more. Weeks later you say "verify the intent against that
standard", and only then is it read. Where a topic deserves grounding,
`/research` looks up current practice and leaves a dated note in the
project.

Before the next layer is derived, two blind reviewers press on the
work: a challenger persona on the thinking (`/challenge cto`), a critic
lens on the documents (`/critique essence`). Neither has seen your
conversation; neither can block anything. You walk through their
verdicts one item at a time, and each one lands somewhere — a fix, a
decision with its reason, or "leave it open".

When the intent holds, the assignment is distilled from it
(`/forge assignment`): the one document the recipients receive,
complete enough to be read without you in the room.

Then the audiences. A pitch for the group is a recipe — composed, if
you like, through a genre interview (`/recipe presentation`) — and
`/render` generates it; `scripts/md2pptx.ps1` turns the deck into a
PowerPoint file through your own template. When the intent moves, you
render again instead of rewriting three documents by hand. `/save`
keeps all of it — engine and project alike — in git.

### What it looks like in practice

A worked example from a real project will appear here once one is
published.

## 5. How the work feels

The forge is as much a way of working as a set of files, and these are
the named methods of that work — the vocabulary you and Claude share.

- **Walkthrough.** Any list that needs your decision — critique
  findings, challenges, open threads, the differences between two
  requirement sets — is worked one item per message, in order of
  weight: Claude's recommendation with a one-sentence reason, then your
  verdict in a word or a counter-proposal, and "leave it open" is a
  legitimate answer. Never a table asking for every verdict at once,
  and an interview runs the same way — one question, one answer, then
  the next.
- **Propose, never decide.** Claude criticises, challenges, inspires
  and lays out options; you compose.
- **Step by step.** Anything needing your consent — a write, a
  commit, a push, a rename — arrives as one step with the exact
  operation, its target and the reason, and runs on your word; a plan
  you have seen is not consent for its steps.
- **Elicitation interview.** Claude draws out by questions what you
  have not yet articulated, never filling gaps by assumption.
- **Draft early.** An early draft is an elicitation tool, not an
  output: concrete text sharpens your reaction.
- **Reflect back.** Before anything is written, Claude restates what
  it understood, so the write confirms rather than surprises.
- **Intent-first.** A change of substance goes into the intent and
  propagates from there; only wording is fixed downstream.
- **Recommend, do not push.** Every option comes with a
  recommendation and its reason, stated once; a declined
  recommendation is not re-argued without new facts.

None of these is a command: you invoke any of them in a word.

## 6. Roles

| Role | What they own |
|---|---|
| Principal | Whoever's thinking is being forged: supplies ideas, answers and decisions, and is the final authority on all content. |
| Claude | The principal's cognitive extension: owns structure, order, process discipline and document hygiene; criticises, challenges, inspires and lays out options — proposes, never decides. |

The standing rules of the collaboration: when unsure, ask — never fill
a gap by assumption; never introduce a new convention, prefix or
section unilaterally — propose it, wait for the decision, then write
it down; many iterations are the normal mode; research before
inventing; everything is advisory, nothing blocks — only the principal
publishes, and a missing section may be a deliberate delegation rather
than a defect; structure over prose, with stable IDs even at very high
abstraction; write once per iteration round, on confirmation; and one
mechanism lives in one place — a procedure stated twice is a defect.

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

**Blue = chain artefacts (light = not built yet), green = renders;
dashed arrows = growth that does not exist yet.**

Adding a layer is one definition file declaring its inputs — nothing
is renumbered and nothing existing is reworked, which is why files are
numbered in tens. The boundary between chain and render is authorship:
a chain artefact is composed by the principal, a render is generated
from artefacts — the article and its translation in the diagram
illustrate it.

| File | What it is | Behaviour |
|---|---|---|
| `00-brief.md` | The idea as the principal wrote it. | Draft until locked, then verbatim; later wholes as `00-brief-<name>.md`. |
| `10-intent.md` | The working understanding of principal and Claude. | Rewritten freely for coherence; versioned. |
| `20-assignment.md` | The direction handed to the recipients. | Versioned; the only document handed over. |
| `<file>.history.md` | The Version History of a versioned document. | Append-only companion beside it. |
| `decisions.md` | The principal's decisions with their reasons (DEC). | Append-only. |
| `ledger.md` | Single source of truth for state. | Freely rewritten; kept current after every operation. |

> A locked brief is immutable — composed, then locked, never touched
> again.

The brief is an intent that is composed and then locked. It is
free-form — any structure you find useful: prose, headings, tables, use
cases — with no required content and no IDs, because a required
structure would force premature tidiness and destroy the diagnostic
value of how the idea was actually dumped. It holds thoughts to be
processed, not decisions: they may be changed, reworked or dropped when
mined. Only a minimal YAML header (project, title, date, author,
version, status, last_change) is fixed. It is `draft` while being
composed and `approved` (1.0) once you lock it. Three origins are
equally legitimate and indistinguishable to the forge: it arrives
finished and is locked on arrival; it is begun outside and finished
with Claude; it is born in the forge — `/forge brief [name]` is the
door for the latter two. A project may have more than one: every later
whole of thinking that would otherwise land in the intent as a batch of
unproven positions is born as `00-brief-<name>.md` under the same
rules. A locked brief is mined into the single intent — positions cite
it as provenance; a whole that dies on the way leaves the brief locked
and one REJ with the reason — and the ledger's Briefs table tracks how
far each is mined (`pending | partial | mined | dropped`) with a
free-text note. Each locked brief is the provenance anchor and drift
measure of its whole.

The intent is the consolidated *current* state of what you want: the
positions you hold (POS), the open threads still to elicit (THR) and
the directions you rejected with the reason (REJ), each with a stable
ID. It is rewritten for coherence every round rather than appended to,
with the changes recorded in its history companion. Its audience is
you and Claude only. It exists because chat context dies and anything
of value must live in a file: it is the document to read when returning
to a project after weeks, instead of excavating old conversations.

The assignment is distilled from the intent for the recipients — a
team, a colleague, your future self — and is the one document they
receive: requirements, out-of-scope, constraints, assumptions,
deliverables, open questions with an owner and optional success
criteria (REQ, OOS, CON, ASM, DEL, TBC, SCR). It carries the full
in-scope substance of the intent, written as well and as precisely as
possible; it assigns rather than solves, and it is self-contained —
readable, agreeable and testable without you in the room. Its Terms
section lets it be forwarded without oral tradition.

Substance changes go intent-first and propagate to the assignment;
wording-only fixes may edit the assignment directly. Artefacts are
written once per iteration round, on your confirmation — one version
bump and one history row however many answers the round contained.
Feedback from recipients has no channel of its own: you process it and
feed the conclusions back through `/forge intent`.

> A render is never edited by hand — what is iterated is its recipe.

**Renders and recipes.** A render is an audience-specific output
generated from the chain — a pitch for the group, an architecture
picture, an executive summary, this README. Its **recipe**
(`recipes/<recipe>.md`) holds inputs, audience, instructions and the
output template in one versioned file; more than one input is
legitimate, and a render may itself serve as an input of another
render — a deck slide citing an architecture picture — when the citing
recipe declares it. `/render <recipe>` regenerates the output into
`renders/<recipe>.md`, or the recipe's optional `output:` path,
overwriting freely with history in git; generation runs in an isolated
subagent that sees only the recipe and its inputs, never the working
conversation. Every render opens with YAML front-matter provenance
citing the recipe and each input with their versions, mirrored in the
**ledger**'s Renders table. Because regeneration is stochastic, a
regenerated render passes under your eyes: a recipe pins load-bearing
wording, and a save that regenerated renders reports what materially
changed; a render is regenerated only by `/save` or by your explicit
`/render`, never on Claude's own judgement. A render assigns nothing
and is not part of the chain: the artefacts stay the source of truth.
Every project has a README rendered from its own `recipes/readme.md`
and, if it is a thought project, release notes from
`recipes/release-notes.md`, regenerated by every save that touches the
project; a library has a README only.

**From Markdown to slides.** Everything the forge produces is
Markdown, content only: a presentation is a `.md` saying what is on
each slide, with mermaid for pictures. Composing its recipe may be
guided by a genre interview (`/recipe presentation`) covering audience
and register, the one message, inputs including renders as picture
sources, dramaturgy, speaker notes and on-slide density.
`scripts/md2pptx.ps1` then turns the deck render into an actual
PowerPoint file through headless Claude Code with the official pptx
skill — an LLM conversion by design, because deck definitions are
free-form and may carry instructions for the model. A `.potx` template
is applied when named by path (`-Template <path>`), typically a
document of a library project; without it, Claude designs the visuals
itself. The `.pptx` lands beside its source render and is tracked in
git like any render output; the Markdown render stays the source of
truth. All other format conversion happens outside the forge.

## 8. Two isolated reviewers

Both reviewers run as isolated subagents that see the artefacts and
nothing else — never the working conversation. They cannot be told what
we really meant; they read what is written, and that blindness is the
source of their value.

The **challengers** attack the substance of the thinking through a
growing roster of persona lenses: unstated assumptions, whether the
objective is the real problem, second-order effects, organisational
reality, failure modes, the serious counter-case. The first persona is
`cto` — peer-CTO register: direct, few and sharp, no flattery.

The **critic** reads the documents through a roster of lenses:
`clarity` reads each artefact on its own — ambiguity, internal
contradiction, duplication, scope hygiene, requirement style — while
`essence` reads the chain for drift, distilling each layer's essence
blind and comparing it with the layer above. Challengers and critic are
one shape — personas and lenses, one agent file each, the shared
behaviour carried from one skeleton with only the Lens section its
own — with two outputs: CHL in `challenges/`, FND in `reviews/`. New
personas and lenses come only by the principal's decision, and only
where their blind spots genuinely differ.

Isolation is not independence. The author, the critic and the
challengers share one model family; what that family systematically
cannot see, none of them will find, so agreement between the reviewers
is never treated as validation — it only means the artefact is
consistent under one set of priors. The calibration point lies outside
the forge: review by humans or by a different model family, invited at
the principal's discretion.

Both run on the session model — the whole forge runs on one model, and
speed is bought with context, never with a weaker reviewer. Both are
invoked by hand, both reports are immutable and dated, and both are
settled by walkthrough. Both take an optional target, an artefact named
as `/forge` names it (`brief`, `brief-<name>`, `intent`, `assignment`,
later layers); without one, the whole chain. Bare `/challenge` and
bare `/critique` list the roster and recommend a fit for the project.

### `/challenge <persona> [artefact]`

The challenger reads the whole chain for context and challenges the
substance of the target; with no target, every challenge names the
artefact it concerns. A layer is best challenged before the next one is
first derived from it — the intent before the first assignment — while
accepted challenges are still cheap to absorb. It has no stake in your
being right and delivers three to seven sharp challenges, each with a
severity (dealbreaker, major, minor — ordered by it, so a fatal flaw is
never buried among cosmetics), a falsifiable "what would change my
mind" and an epistemic status (consensus, active debate, emerging
practice, its own judgement). Fabrication is banned: a precise "I don't
know" beats an invented figure, and anything reconstructed from memory
is flagged. The report lands as
`challenges/YYYY-MM-DD-challenge-<persona>.md`, its CHL rows in the
ledger. A challenge is open, accepted, rejected (with a DEC recording
the reason), parked or obsolete; an accepted challenge must change the
intent, otherwise it was not accepted. A challenge may inspire, but
nothing enters the intent because a reviewer wrote it — only because
you composed it, by subtraction as readily as by addition.

### `/critique <lens> [artefact]`

A target narrows `clarity` to that artefact and `essence` to that
artefact against its parent — every layer has exactly one parent, so
a transition is addressed by naming its downstream artefact. For every
adjacent pair (brief → intent, intent → assignment, every later layer)
`essence` first distils the downstream artefact's essence blind, then
the upstream's, and compares: substance lost without a trace (no REJ,
DEC, DEL, TBC or mining state accounting for it), substance added
without provenance, meaning shifted. A finding is a difference of
essences, not of texts, and the report carries both distillations.
Regression against resolved findings is every lens's first step, and
each run produces a delta: new, verified resolved, still open, newly
obsolete. Untestable wording is reported as a recommendation, never as
a defect. The report lands as `reviews/YYYY-MM-DD-critique-<lens>.md`,
its FND rows in the ledger. A finding is in one of four states:

- open
- resolved — an iteration of the artefact concerned
- overruled — a DEC with its reason
- obsolete — the passage no longer exists

Nothing blocks: every finding and challenge is either fixed or
explicitly overruled with a recorded reason; overruling and parking are
legitimate outcomes, silently ignoring is not.

## 9. Commands

Commands are the doors into the forge's phases; the same rules apply in
plain conversation, and the `/forge` star means the name of the
artefact you want to work on is the command.

| Command | Purpose |
|---|---|
| `/setup` | First run after cloning the engine: fills `CLAUDE.local.md` by interview, sets the session model to Fable and offers the global git identity guard. Never overwrites, runs no git operation. |
| `/new-project <slug>` | Scaffolds a project by kind, files only and never git: a thought project with its brief captured verbatim (locked if finished, draft otherwise), or a library (`lib-`) of shared material. |
| `/import-project <git-url>` | Brings an existing project into `projects/` by cloning it — the directory is the repository's name; the commit identity is proposed from `CLAUDE.local.md` by the URL's host. |
| `/forge [slug]` | The chain map: which artefacts exist at what versions, which renders are stale, which steps are possible from here, and a recommended next step. |
| `/forge <state> [slug]` | Iterates the named artefact — `brief [name]`, `intent`, `assignment`, later layers as they come; one definition file per state, each declaring its inputs. |
| `/ingest [file] [slug]` | Stores and registers external input in `sources/` and indexes it; bare, sweeps `sources/` for unregistered files. |
| `/render <recipe> [slug]` | Regenerates a render from its recipe in `recipes/`. |
| `/recipe [genre] [slug]` | Bare: the genre roster. With a genre (`presentation`, `readme`, `release-notes`): guided composition — or iteration — of a render recipe from the genre's checklist and skeleton. |
| `/critique [lens] [artefact] [slug]` | Bare: the lens roster. With a lens (`clarity`, `essence`): runs that critic on the documents — one artefact, or one against its parent, when named, else all. |
| `/challenge [persona] [artefact] [slug]` | Bare: the persona roster. With a persona (e.g. `cto`): runs that challenger against the substance of the named artefact, else the whole chain. |
| `/research <topic> [slug]` | Best-practice research into `research/`, indexed. |
| `/ledger [slug]` | The quick state readout from the ledger — where things stand, nothing more. |
| `/check [slug]` | Conformance of a project against the current conventions; bare, every project but forge. |
| `/check-forge` | Consistency check of the core and `projects/forge`. |
| `/save [slug] [-m "message"]` | Pre-save check, findings settled with you, then commit and push. |
| `/spinoff <project> <group> <slug>` | Splits a requirement group into a project of its own — on your explicit decision only. |

`/ingest` stores, registers and catalogues — nothing more. A source
has one form: text, or a functional binary. Every binary gets one
question at ingest — convert to Markdown? Yes makes the extract
`sources/<slug>.md` the source (through `scripts/doc2md.ps1`, never
by ad-hoc parsing), with the original not copied or gitignored where it
already lies; no keeps the binary itself as the source — a template, a
graphic — with no extract. A set of related files lives as a bundle
`sources/<slug>/` with its own `00-INDEX.md`: one source, one ledger
entry. Registration does not imply intake: a source's role — a
standard to verify against, inspiration, a counter-example, a meeting
record — is free text in the resource index, and you alone direct how
and when it is used; when its content enters the intent, that is your
explicit act, cited with provenance.

`/save` routes the conformance check by scope — `/check-forge` when
core files are touched, `/check <slug>` for a project's changes —
walks you through the findings, records what is deferred in the
ledger, proposes a commit message for your confirmation and only then
runs the save script; the check is a recommended procedure, never a
gate. Every command is an entry point, not the only door: the core
rules apply in ordinary conversation too.

### A typical journey

- You write down what you want — as you would in an e-mail, in any
  shape — and lock it as the brief of your project (`/new-project`).
- Over a few sessions the forge interviews you and the intent takes
  shape: positions, open threads, rejected directions (`/forge
  intent`); material you gathered is registered as it arrives
  (`/ingest`) and consulted when you say so.
- Before going further you send in a challenger and a critic
  (`/challenge cto`, `/critique essence`) and walk through their
  verdicts one at a time; what you accept changes the intent, what you
  overrule gets a decision with its reason.
- You compose a presentation recipe through the genre interview
  (`/recipe presentation`), render it (`/render`) and turn the deck
  into a PowerPoint file with your template (`scripts/md2pptx.ps1`).
- When the intent holds, you distil the assignment (`/forge
  assignment`), run the critic once more and hand over one document.
- All along you save (`/save`): each save re-renders your project's
  README and release notes, checks conformance and commits.

## 10. Conventions

**IDs.** Every item carries an ID of the form `PREFIX.NNNN` with a
three-letter prefix. IDs are global and stable — never renumbered;
items may move between groups without changing ID. Items are numbered
in tens (`REQ.0010, REQ.0020`), each new group starting at the next
hundred (`REQ.0100, REQ.0110`); overflow takes the next free number
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
prefixes and any domain terms it actually uses, so it can be forwarded
without oral tradition; defined Terms are capitalised in item text to
signal they appear there.

**Language.** The forge dictates the output language: all documents
are written in English — translated on write — with one exception, the
briefs, stored verbatim in whatever language they were written. The
conversation language is per-instance configuration and lives in
`CLAUDE.local.md`.

**Requirement style.** Requirements use *shall* / *shall not* — never
would, could, should, might, may or MoSCoW wording. There is no
priority column and no priority tag: everything in an assignment is
essential by default, and an exception is marked by a note reading
*optional* on that item. Each item covers one idea, is written once,
and is written in full, correct UK English sentences. Testability is
recommended, not required — assignments are deliberately high-level,
and delegating concretisation through a DEL item is a legitimate
outcome. No item may depend on an external link to be understood,
agreed or later tested. For illustration only:

> REQ.0010 The Platform shall record every request and every response
> passing through the Gateway, with the identity of the requesting
> User and the time.

**Completeness over brevity.** An assignment carries the full in-scope
substance of the intent, written as well and as precisely as possible;
nothing is omitted for brevity's sake, and length is whatever fidelity
requires. Leaving a matter out is legitimate only as an explicit
delegation — a DEL or TBC item. An assignment assigns, it does not
solve: the machinery of executing delivery belongs to the recipients,
while any apparatus may appear where the principal judges it part of
setting direction.

**Versioning.** Integers denote signed-off versions: `0.1, 0.2, …`
are drafts before first approval; `1.0` is approved; `1.1, 1.2, …` are
changes made after approval, not yet approved themselves; `2.0` is the
next approved version, incorporating all changes since 1.0.
Front-matter carries `version`, `date`, `status` (`draft | in_review |
approved | superseded`) and `last_change`, and status must agree with
the number: an integer version is `approved`, anything else is not; a
recipe carries no status and stays 0.x.

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

Every versioned kind keeps its Version History (Version | Modification
| Author | Date — human-readable, what changed and why) in an
append-only companion `<file>.history.md` beside it, never in its
body, and the document's `last_change` line in the front-matter
summarises the newest row, written by the same step that appends it.
An integer version is approved, and a recipe never is. Immutable
documents — a locked brief, reviews, challenges, sources, research —
are never edited: corrections happen downstream.

**Project kinds.** A project has a kind, declared in the header of its
ledger: `thought` (the default) carries the chain; `library` carries no
chain — only a ledger, `sources/` and `research/` with their indexes,
and a README that catalogues what it holds. A library collects material
shared across projects — a deck template, a writing convention —
maintained by its owner, who may overwrite or version as he sees fit;
another project cites a library document by path, a cross-repository
dependency taken knowingly and registered in its ledger's Dependencies
table. Every `sources/` and `research/` directory carries a
`00-INDEX.md` — a light catalogue of what is there and what it is for
(sources: What / Origin / Role / Use for; research: Question / Answer
in short / Consult when), freely rewritten and an automatic input of
no command.

**Naming.** Project slugs are lowercase and hyphenated on disk;
display names may differ. The system's own project is `forge`;
libraries carry the `lib-` prefix. Names must be legible to the
audience, not only to the principal.

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
- PowerShell 7 (`pwsh`) — the scripts are PowerShell, and they are
  needed on macOS and Linux too; `pwsh` is one install there, and the
  scripts run on it unchanged
- Python 3 — for markitdown, which `doc2md.ps1` runs
- a paid Claude subscription — Claude Code draws on it

### Getting the forge and Claude Code

Clone this repository: it is the engine. Then install Claude Code —
Windows: `irm https://claude.ai/install.ps1 | iex`; macOS/Linux:
`curl -fsSL https://claude.ai/install.sh | bash`; or, with Node
installed, `npm install -g @anthropic-ai/claude-code`. Sign in on
first run; usage draws from the same pool as Claude chat.

Always start `claude` from the engine root, so that `CLAUDE.md` and
`CLAUDE.local.md` load. Then run `/setup` once. It creates
`CLAUDE.local.md` from its template and fills it with you in a short
interview — who the principal is, the conversation language, your git
identities per host — gitignored, never committed. It creates
`.claude/settings.local.json` with the session model set to Fable, the
strongest available model, which the whole forge including the blind
reviewers runs on; it tells you so in one sentence, and `/model` or
editing that file changes it at any time (permissions come from the
shared `.claude/settings.json`). It closes by offering one global git
guard — `user.useConfigOnly = true` appended to `~/.gitconfig` — so
that a repository without a local identity fails aloud instead of
committing with a default; declined, it prints the line for you to
apply by hand, and where a global `user.name` or `user.email` exists
it says the guard only bites once that is removed. The identities
themselves are set per repository, proposed from your roster at every
project creation or import. `/setup` never overwrites existing files.

Upgrading the engine is `scripts/forge-pull.ps1` — a fast-forward of
`main`; your projects are untouched by it, and the engine carries a
git tag at every approved major of its own intent.

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
error; a project with a repository and no remote is a legitimate shape
for something kept local.

### Script prerequisites

- `doc2md.ps1` needs markitdown:
  `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`.
- `md2pptx.ps1` needs the `document-skills` plugin, installed once from
  an interactive Claude Code session: `/plugin marketplace add
  anthropics/skills`, then `/plugin install
  document-skills@anthropic-agent-skills`. A deck template is named by
  path (`-Template <file.potx>`) — typically a document of a library
  project — or none, in which case Claude designs the visuals.
- The git scripts need nothing beyond git.

### Saving and syncing

The recommended door for saving is `/save`. When the save touches the
core or `projects/forge/`, it first re-renders `README.md` and the
Unreleased head of `RELEASE-NOTES.md` from their recipes —
unconditionally, reporting what materially changed — then runs the
conformance check routed by scope, settles the findings with you,
proposes a commit message, and only then commits.

Underneath, the scripts in `scripts/` are the mechanism and the only
intended door to git — reading state included, no exceptions; saves
made directly from the shell are legitimate and unaffected by the
ceremony above. Three of them serve the engine and every project
repository alike: `forge-save.ps1` commits and pushes — bare, every
repository with changes, each its own commit; with a slug, that one
(`forge` meaning the engine); without an origin the commit is kept and
reported; remote changes are reconciled by rebase — `forge-pull.ps1`
fast-forwards from the remotes and never touches a repository with
unsaved changes, and `forge-status.ps1` reports without changing
anything. History is linear on `main`, one remote per repository, and
no URL is configured anywhere in the forge: git carries that itself.

## 13. Scripts

| Script | Purpose | When it is run | Install note |
|---|---|---|---|
| `scripts/forge-save.ps1` | Commits and pushes the engine and every project with changes, each its own commit — or one repository by slug — reconciling remote changes by rebase and printing the commit's file summary. | At every save, by `/save` or directly from the shell. | git only. |
| `scripts/forge-pull.ps1` | Fast-forwards from the remotes, never touching a repository with unsaved changes; on the engine it is the upgrade channel. | To upgrade the engine or sync a project. | git only. |
| `scripts/forge-status.ps1` | Reports unsaved changes, the last commit and the origin of the engine and each project, changing nothing. | Whenever you want to know where things stand. | git only. |
| `scripts/forge-clone.ps1` | Clones an existing project into `projects/<repository name>`, never overwriting, and sets its local commit identity when given `-Name` and `-Email`. | By `/import-project`. | git only. |
| `scripts/doc2md.ps1` | Converts a document to Markdown — the only way extracts of binary sources are produced, never by ad-hoc parsing. | By `/ingest`, per binary you choose to convert. | markitdown — see Setup. |
| `scripts/md2pptx.ps1` | Turns a Markdown deck render into a `.pptx` through headless Claude Code with the official pptx skill, applying a `.potx` template named by path. | After rendering a presentation recipe. | `document-skills` plugin — see Setup. |

## 14. Planned extensions

The chain is meant to keep growing downward: thoughts are forged as
far as the principal needs them taken. A BRD layer is certain to come;
solution architecture and integration are intended; a strategy layer
is possible if it proves to make sense. Which layers are added, and in
what order, is open, and nothing is approved for construction: the
mechanics of a layer — its command, its reviewer calibration — are
designed when that layer is actually taken up, never in advance. The
numbering in tens and the star-shaped `/forge <state>` mechanism exist
so that each such layer is one definition file, with nothing existing
reworked.

The forge is a single-user tool per instance. A second principal
receives it via git and runs an instance of their own; genuine
multi-user operation is a matter for the future and deliberately not
worked on now.

`projects/forge/` is Forge of Thought itself run through its own
process — its brief, intent (design positions, open threads, rejected
directions), decisions and ledger. A change to the process is complete
only once that intent is updated and this README re-rendered.

## 15. Author and licence

Forge of Thought © Petr Chlumsky (PCHe) — petr.chlumsky@gmail.com.
Licensed under [CC BY 4.0](LICENSE): use and adapt it freely; credit
the author and link to this repository.

## 16. About this README

This file is a render of the `projects/forge` project: it is generated
by `/render readme` from `projects/forge/recipes/readme.md` and its
inputs — `CLAUDE.md` and the forge intent — whenever the process
changes, and by every `/save` that touches the core. It is never
edited by hand: fixes go into the recipe or the inputs, and the file is
regenerated. The YAML front-matter at the top is its provenance, kept
by design. Changes to the system itself are recorded in
`projects/forge/`.

_Last updated: 2026-09-04_
