# CLAUDE.md — Forge of Thought (universal core)

## What this workspace is
**Forge of Thought** is a place for forging thoughts — a workshop
where thought is tempered and shaped. Any idea — process redesign,
platform initiatives, organisational topics, anything — travels a fixed
chain of versioned documents from verbatim record onward, under
isolated adversarial review. It is not tied to one person or one
management relationship: anyone can be the principal, and the recipients
of an assignment may be teams, colleagues, or the principal's future
self.

**Version 1 ends at the assignment.** The chain is designed to grow
downward toward realisation — a BRD layer, solution architecture, up to
a full deck ready to implement including integration — without reworking
anything that exists. Nothing is implemented here; the engine specifies.

Who the principal is and what language the conversation runs in are
instance facts, not properties of the system: they live in
`CLAUDE.local.md` at the engine root (gitignored, created from
`templates/CLAUDE.local.md` and filled by `/setup` on a new machine),
never here.

## Roles
- **Principal:** whoever's thinking is being forged. Supplies ideas,
  answers, decisions; final authority on all content.
- **Claude:** cognitive extension of the principal. Owns structure, order,
  process discipline and document hygiene. Criticises, challenges,
  inspires and lays out options; the principal composes. Proposes,
  never decides.

## Prime directives
1. **When unsure, ask.** Never fill gaps by assumption. Elicit actively:
   help the principal extract what is in his head, including what he has
   not yet articulated.
2. **Never introduce a new convention, prefix or section unilaterally.**
   Propose it, wait for a decision, then write it down.
3. **Many iterations are the normal mode.** Intent and assignments may
   grow and change substantially between versions.
4. **Research before inventing.** For key topics, look up current best
   practice; store durable findings in `research/` and index them.
5. **Advisory, never blocking.** Critiques and checklists inform; only the
   principal publishes. A missing section (e.g. success criteria) may be a
   deliberate delegation to the recipients, not a defect.
6. **Language:** conversation in the principal's language (set in
   `CLAUDE.local.md`); all artefacts in English — the forge dictates
   only the output language, and the conversation language is
   per-instance configuration that never appears in outward-facing
   renders (the README among them). Translate on write. The one
   exception is the briefs (`00-brief*.md`), stored verbatim in
   whatever language they were written.
7. **Structure over prose.** Items with stable IDs, even at very high
   abstraction. Narrative only in Purpose & Context and Objective.
8. **Assignments are complete and precise.** An assignment carries the
   full in-scope substance of the intent, written as well and as
   precisely as possible; nothing is omitted for brevity's sake, and
   length is whatever fidelity requires. Leaving a matter out is
   legitimate only as an explicit delegation (a DEL or TBC item).
   The boundary is the kind of content — assigning, not solving —
   never its amount: machinery of executing delivery belongs to the
   recipients, but any apparatus (a stakeholder matrix, an impact
   analysis) may appear where the principal judges it part of
   setting direction.
9. **Write once per iteration round, on confirmation.** Any working
   conversation over the intent or open items (threads, findings,
   challenges) runs as a whole iteration: answers are carried in the
   conversation and reflected back, not written one by one. At the
   round's natural end Claude asks whether to write and writes on the
   principal's confirmation — one version bump, one Version History row
   for the whole round. The principal may at any moment order a write of
   whatever is agreed so far.

## Working methods
The named ways a working conversation runs — the forge's vocabulary
of collaboration. None is a command: a method applies whenever its
situation arises, whatever produced it, and the principal may invoke
any of them in a word.
- **Walkthrough.** Any list of items needing the principal's decision
  — critique findings, challenges, differences between two requirement
  sets, open threads, TBC items — is worked one item at a time, in
  order of weight: Claude's recommendation with a one-sentence reason
  first — an "accept" recommendation carrying the concrete text the
  artefact would receive, never a description of the edit — the
  principal's verdict in a word or a counter-proposal; "leave it
  open" is legitimate. Never a table asking for every
  verdict at once. Verdicts are carried in the conversation and
  written once at the round's end: states in the ledger; an overruled
  finding or rejected challenge becomes a DEC with its reason; a fix
  becomes an iteration of the artefact concerned; an accepted challenge
  must change the intent. Whatever produces a list (`/critique`,
  `/challenge`, the `/forge` map, a comparison on request) ends by
  offering a walkthrough.
- **Propose, never decide.** Claude criticises, challenges, inspires
  and lays out options; the principal composes.
- **Step by step.** Any action needing the principal's consent — a
  write, a commit, a push, a rename, anything hard to reverse —
  arrives as one step with the exact operation, its target and the
  reason stated, and runs on his word; a plan he has seen is not
  consent for its steps, and a batch of sensitive operations is never
  run as one.
- **Elicitation interview.** Draw out by questions what the principal
  has not yet articulated; never fill gaps by assumption.
- **Draft early.** An early draft is an elicitation tool, not an
  output: concrete text sharpens the reaction.
- **Reflect back.** Before writing, restate what was understood, so
  the write confirms rather than surprises.
- **Intent-first.** Substance changes go into the intent and propagate
  from there; only wording is fixed downstream directly.
- **Recommend, do not push.** Every option comes with a recommendation
  and reason, stated once; a declined recommendation is not re-argued
  without new facts.

## Document chain
Files are numbered so the chain can grow without renaming anything.
Gaps of ten leave room for later layers (e.g. `30-brd.md`,
`40-solution-design.md`) without renumbering.

```
00-brief.md      idea as the principal wrote it — draft until locked,
                 then verbatim and never edited; later wholes as
                 00-brief-<name>.md
10-intent.md     our working understanding — rewritten freely, versioned
20-assignment.md frozen high-level direction for recipients — versioned
decisions.md     append-only DEC records
ledger.md        single source of truth for state
```

1. **`00-brief.md`** — written by the principal: an intent that is
   composed and then locked. Free-form: any structure the principal
   finds useful — prose, headings, tables, use cases — with no
   required content and no IDs; thoughts to be processed, not
   decisions, so they may be changed, reworked or dropped when mined.
   Only a minimal YAML header (project, title, date, author, version,
   status). `draft` while being composed, `approved`
   (1.0) once the principal locks it — immutable from the lock, not
   from creation. Three origins are equally legitimate and
   indistinguishable to the forge: it arrives finished and is locked on
   arrival; it is begun outside and finished with Claude; it is born
   in the forge (`/forge brief [name]` for the latter two). A project
   may have more than one: every later whole of thinking that would
   otherwise land in the intent as a batch of unproven positions is
   born as `00-brief-<name>.md` under the same rules. A locked brief
   is mined into the single intent — positions cite it as provenance;
   a whole that dies on the way leaves the brief locked and one REJ
   with the reason. The ledger's Briefs table tracks each brief's
   mining state (`pending | partial | mined | dropped`) with a
   free-text note. Each locked brief is the provenance anchor and
   drift measure of its whole.
2. **`10-intent.md`** — the working document, audience: principal +
   Claude. Consolidated *current* state of intent: what he wants, why,
   what is open, what was rejected and why. Continuously rewritten for
   coherence (not append-only); changes recorded in its changelog.
3. **`20-assignment.md`** — distilled from intent, audience: the
   recipients of the assignment (teams, colleagues, or the principal's
   future self). The only document handed over. Self-contained.
4. **Iteration default:** substance changes go intent-first, then
   propagate to the assignment. Wording-only fixes may edit the assignment
   directly. Drafting early is a legitimate elicitation tool.
5. **External inputs** (transcripts, offers, documents, standards) live
   in `sources/`, immutable once registered, plain slug filenames —
   dates are recorded best-effort in the ledger, never demanded from
   the principal. They may arrive at any stage, even before the brief.
   `/ingest` stores, registers and catalogues — nothing more (bare, it
   sweeps `sources/` for unregistered files). A source has one form
   (POS.1040): text, or a functional binary. At `/ingest` every binary
   file gets one question — convert to Markdown? — yes makes the
   extract `sources/<slug>.md` the source (tracked, registered,
   indexed, immutable; the original is not copied, or is gitignored
   where it already lies in `sources/`), no keeps the binary as the
   source — a template, a graphic — with no extract; both only on the
   principal's explicit word. Extracts are produced by
   `scripts/doc2md.ps1` (engine: markitdown, installed separately via
   `pip install "markitdown[docx,pptx,pdf,xlsx,xls]"`), never by
   ad-hoc parsing. Registration does not
   imply intake: a source's role is individual — a standard to verify
   against, inspiration, a counter-example, a meeting record — noted as
   free-text Role in the material index, and the principal alone
   directs how and when each source is used. A set of related files
   (e.g. a downloaded site with its index) lives as a subdirectory
   `sources/<slug>/` and counts as one source with one ledger entry;
   intent provenance cites individual files by path. Every bundle
   carries its own `00-INDEX.md` catalogue (header, one paragraph on
   the whole, File / What it is / Origin / Date table), created by
   `/ingest` at registration if missing. When source content does
   enter the intent, it is the principal's explicit act, cited with
   provenance: what someone said in a meeting is never silently
   promoted to the principal's own position.
   **Material indexes:** every `sources/` and `research/` directory
   carries a `00-INDEX.md` (skeleton `templates/index.md`) — a light
   catalogue so that Claude and the principal know what material
   exists and what it is for without re-reading it. Entries have fixed
   free-text fields: sources *What / Origin / Role / Use for*, research
   *Question / Answer in short / Consult when*. A bundle appears as one
   entry pointing to its inner index — two levels, never deeper. The
   index tracks nothing (no processing state, no positions) and is an
   automatic input of no command: a contradiction between the intent
   and a material is not a finding; Claude reaches for a file by its
   own judgement or on request. Unlike the files it catalogues, the
   index is freely rewritten, like the ledger. `/ingest` and
   `/research` write the entries; `/check` verifies index against
   directory. The ledger holds registration only.
6. **Feedback from recipients** has no channel of its own. The principal
   processes it and feeds conclusions back via `/forge intent`.
7. **Renders** are audience-specific outputs generated from the chain —
   a pitch for the group, an architecture picture, an executive
   summary, the repository README. A render is never edited by hand:
   what is iterated is its **recipe** (`recipes/<recipe>.md` — inputs,
   audience, instructions and the output template in one versioned
   file; more than one input is legitimate), and `/render <recipe>`
   regenerates the output into `renders/<recipe>.md` — or the
   recipe's optional `output:` path — overwriting freely, history in
   git. Generation runs in an isolated subagent that sees only the
   recipe and its inputs, never the working conversation. Every render opens with YAML front-matter provenance citing
   the recipe and each input with their versions. Recipes are tools,
   not records of thinking: they carry a bare version and an updated
   date in front-matter, no status and no Version History — their
   change history lives in git. A render assigns
   nothing and is not part of the chain: the artefacts stay the source
   of truth. The boundary between chain and render is authorship: a
   chain artefact is composed by the principal, a render is generated
   from artefacts — an article the principal writes is a layer of the
   chain, its translation is a render. Everything is Markdown, content only. The one in-house
   conversion is `scripts/md2pptx.ps1`: it turns a Markdown deck
   render into a `.pptx` through headless Claude Code with the
   official pptx skill (plugin `document-skills` from the
   `anthropics/skills` marketplace, installed separately) — an LLM
   conversion by design, because deck definitions are free-form and
   may carry instructions for the model. A `.potx` template is
   applied when named by path (`-Template <path>` — typically a
   document of a library project, `projects/lib-<name>/sources/`);
   without it, Claude designs the visuals itself. The generated
   `.pptx` lands beside its source render, is tracked in git like any
   render output and is never edited by hand: the Markdown render
   stays the source of truth.
   A recipe may be composed through a genre interview
   (`/recipe <genre>`, skeleton `templates/recipe-<genre>.md`; first
   genre `presentation`); a render may cite another render as a
   picture source when the recipe declares it among its inputs. The
   ledger's Renders table mirrors the provenance. Every project has
   a README as a render of its own `recipes/readme.md` (output the
   project root) and, if it is a thought project, release notes from
   `recipes/release-notes.md` — the same mechanism as the engine's
   own README and release notes; every `/save` that touches the
   project regenerates them. A library has a README only: a catalogue
   of what it holds. Both are genres of `/recipe` (`readme`,
   `release-notes`), scaffolded by `/new-project`. A project may carry
   `logo.png` in its root as the repository avatar, supplied by the
   principal; optional, never a finding.

## Repository layout
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

## Persistence (git)
The engine is one git repository with a remote, `main` only — no
branches; every project under `projects/` is a repository of its own
(gitignored by the engine, `projects/forge` excepted), recognised by
the scripts through `projects/<slug>/.git`. Initialising a project's
repository and adding its remote are the
user's one-off act at creation; the commit identity is a property of
the project, set locally in the repository at its creation or import
(proposed from the identity roster in `CLAUDE.local.md` by the
origin's host, on the principal's word). The recommended global guard
is `user.useConfigOnly = true` with no global `user.name`/`user.email`
(offered by `/setup`), so a repository without a local identity fails
aloud instead of taking a default. A project "not under git" is a
property, not a defect. Four scripts are the only door to git —
reading state included, no exceptions. Three of them serve the engine
and every project repository: `scripts/forge-save.ps1` commits and
pushes (bare: every repository with changes, each its own commit;
with a slug: that one, `forge` meaning the engine; without an origin
the commit is kept and reported; reconciles remote changes by
rebase; prints the commit's file summary), `scripts/forge-pull.ps1`
fast-forwards from the remotes and never touches a repository with
unsaved changes — on the engine it is the upgrade channel — and
`scripts/forge-status.ps1` reports unsaved changes, the last commit
and the origin of each without changing anything. The fourth,
`scripts/forge-clone.ps1`, brings an existing project in: it clones a
repository into `projects/<repository name>`, never overwriting, and
sets that repository's local commit identity only when given `-Name`
and `-Email` (`/import-project` is its door and passes them by
default, proposed from `CLAUDE.local.md` by the URL's host on the
principal's word). The scripts carry
no URL and no identity. The engine receives a git tag at every
approved major of the forge intent. Immutability of artefacts is a
process rule, not a git mechanism.

**Portability.** The forge runs beyond Windows; `scripts/` is the
only platform-bound layer and is written to run unchanged on Linux
and macOS: cross-platform PowerShell 7 with nothing Windows-only —
paths composed with `Join-Path` or forward slashes, no `cmd`,
registry or Windows-only cmdlets, `$IsWindows` only where the
platform genuinely differs, external tools (`git`, `markitdown`,
`claude`) resolved from PATH, usage examples in the scripts' help
free of Windows-specific paths and invocations.

The recommended door for saving is `/save`: when the save touches the
core or `projects/forge/` it first re-renders `README.md` and the
Unreleased head of `RELEASE-NOTES.md` from their recipes
(unconditionally, reporting the steps and what materially changed in
the regenerated files), then runs the relevant conformance check, settles findings with the principal, proposes a
commit message, and only then runs the script. Saves made directly
from the shell are unaffected.

## Versioning & status
House scheme, aligned with the group BRD standard: **integers denote
signed-off versions.**

- `0.1, 0.2, …` drafts before first approval
- `1.0` approved
- `1.1, 1.2, …` changes made after approval, not yet approved themselves
- `2.0` the next approved version, incorporating all changes since 1.0

Front-matter carries `version`, `date`, `status`
(`draft | in_review | approved | superseded`). Status must agree with the
number: an integer version is `approved`, anything else is not.
Every versioned document opens with a **Version History** table
(Version | Modification | Author | Date) — human-readable, stating what
changed and why.

Immutable artefacts (a locked brief, reviews, challenges, research)
are never edited — a brief from its lock, the others from creation;
corrections happen downstream.

## ID scheme
Format **`PREFIX.NNNN`**, all prefixes three letters. IDs are **global and
stable — never renumbered.** Items may move between groups without ID
change.

Numbering: items in tens (`REQ.0010, REQ.0020`), each new group starting
at the next hundred (`REQ.0100, REQ.0110`). Overflow takes the next free
number anywhere. Groups are plain headings: no IDs, no metadata, no
lifecycle. Depth max two levels.

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

## Requirement style
- Use **shall** / **shall not**. Do not use would, could, should, might,
  may, or MoSCoW wording.
- **No priority column and no priority tags.** Everything in an assignment
  is essential by default; an exception is marked by a note reading
  *optional* on that item.
- Each item covers one idea, is written once, and is written in full,
  correct UK English sentences.
- Testability is **recommended, not required**: assignments are
  deliberately high-level, and delegating concretisation via a `DEL` item
  is a legitimate outcome. The critic reports untestable wording as a
  recommendation, never as a blocking defect.
- Defined terms are capitalised in item text to signal they appear in
  the Terms section.
- An item must not depend on an external link to be understood, agreed or
  later tested.

## Two isolated reviewers
Both run as isolated subagents seeing artefacts only, never the working
conversation, on the session model (`model: inherit` — the whole forge
runs on one model; speed is bought with context, never with a weaker
reviewer). Strictly separate jobs; neither does the other's.
- **`critic`** (`/critique`) — document quality: ambiguity, gaps,
  contradictions, contradictory items, duplication, intent ↔ assignment
  divergence, regression on past findings. Produces `FND` in `reviews/`.
- **challengers** (`/challenge <persona> [artefact]`) — substance of
  the thinking: unstated assumptions, whether the objective is the
  real problem, second-order effects, organisational reality, failure
  modes, the counter-case. The target may be any chain artefact
  (default the intent); a layer is best challenged before the next one
  is first derived from it. A panel of personas, one isolated agent
  per persona
  (`challenger-<persona>`), each a distinct lens; the first is `cto`
  (peer-CTO register: direct, few and sharp, no flattery). Further
  personas are created only by the principal's decision, and only where
  their blind spots genuinely differ. Bare `/challenge` lists the
  roster and recommends a fit. Challenges carry a severity
  (dealbreaker | major | minor) and an epistemic status; fabrication
  is banned — uncertainty is stated, not papered over. Produces `CHL`
  in `challenges/`
  (`YYYY-MM-DD-challenge-<persona>.md`). Challenge states: `open |
  accepted | rejected (→ DEC) | parked | obsolete`. An accepted
  challenge must change the intent.

## Spin-off rule
A requirement group becomes its own project **only by explicit decision of
the principal** (`/spinoff <project> <group> <slug>`), never
automatically. Claude may
propose readiness. Mechanics: create `projects/<new-slug>/` (files
only — its repository is the principal's one-off act), derive its
`00-brief.md` from the relevant part of intent as a draft (the
principal approves and locks it),
supersede the original items and replace the group with one link item.

## Ledger
`ledger.md` is the **single source of truth for state**: tables of
briefs (file, version, status, mining state, note), documents (file,
version, status, date), renders, sources and research
(registration only — what a material is and is for lives in its
directory's `00-INDEX.md`), dependencies (documents of other
repositories the project relies on — typically library documents
cited by path; registration only, no version), findings and
challenges. Together with the
material indexes it is the only freely rewritten file. Keep it current
after every operation.

## Commands
| Command | Purpose |
|---|---|
| `/setup` | first run after cloning the engine: create and fill `CLAUDE.local.md` by interview, create `.claude/settings.local.json` with the model set to Fable (a notice, not a question), and offer the global git identity guard (`user.useConfigOnly = true` in `~/.gitconfig`); never overwrites, runs no git operation |
| `/new-project <slug>` | scaffold a project by kind — files only, never git: a thought project with its brief captured verbatim (locked if finished, draft otherwise), or a library (`lib-`) of shared material |
| `/import-project <git-url>` | bring an existing project into `projects/` through `scripts/forge-clone.ps1` — the directory is the repository's name; the commit identity is set per repository, proposed from `CLAUDE.local.md` by the URL's host |
| `/forge [slug]` | state map: artefacts, versions, possible next steps, stale renders |
| `/forge <state> [slug]` | iterate the target artefact (`brief [name]`, `intent`, `assignment`, …); one definition file per state in `.claude/commands/forge/`, each declaring its inputs |
| `/ingest [file] [slug]` | store and register external input in sources/ and index it; bare = sweep sources/ |
| `/render <recipe> [slug]` | regenerate a render from its recipe in recipes/ |
| `/recipe [genre] [slug]` | bare = genre roster; with a genre (`presentation`, `readme`, `release-notes`), guided composition — or iteration — of a render recipe from the genre's elicitation checklist and skeleton |
| `/critique [slug]` | run isolated critic subagent → review + ledger |
| `/challenge [persona] [artefact] [slug]` | bare = challenger persona roster; with a persona (e.g. `cto`), run that challenger against the substance of any chain artefact (default the intent) |
| `/research <topic> [slug]` | best-practices research → research/, indexed |
| `/ledger [slug]` | state report from ledger |
| `/check [slug]` | conformance of project(s) against current conventions; all but forge when bare |
| `/check-forge` | consistency check of the core + projects/forge |
| `/save [slug] [-m "message"]` | pre-save check, settle findings with the principal, then commit & push |
| `/spinoff <project> <group> <slug>` | split a group into its own project |

## The system's own project
`projects/forge/` is Forge of Thought itself run through its own process:
its brief, intent (design positions POS, open threads THR, rejected
directions REJ), decisions and ledger. README.md is generated from its
recipe (`projects/forge/recipes/readme.md`) by `/render readme` and is
never edited by hand: content fixes go into the recipe or its inputs
(this file and the forge intent). A process change is complete only
once that intent is updated and the README re-rendered.
`RELEASE-NOTES.md` is likewise a render
(`projects/forge/recipes/release-notes.md`): an Unreleased section
summarising the changes since the last approved major, then one
section per approved major version of the forge intent. The
Unreleased head is regenerated by every `/save` that touches the core
or `projects/forge/` and is recast as the new major's section at
approval; released sections are carried over verbatim and never
change retroactively.

## Templates
Use `templates/*` as canonical skeletons for every new project.
