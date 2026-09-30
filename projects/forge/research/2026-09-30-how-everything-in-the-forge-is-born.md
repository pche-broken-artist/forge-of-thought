---
project: forge
type: research
topic: how everything in the forge comes into being — the complete typed inventory of what can be created (instance, projects, artefacts, resources, records, recipes and renders, reviewers, extensions of the engine) and, for each kind, the procedure the principal goes through, what he must supply and decide, which commands and skills are involved and what is written where
date: 2026-09-30
derived_from: the engine's own definitions as of commit c95cffe (CLAUDE.md; .claude/skills/*/SKILL.md with the state and genre files; .claude/agents/*.md; templates/*.md; the help headers of scripts/*.ps1; .claude/settings.json); 10-intent.md v4.34 (POS.0120, POS.0300, POS.0540, POS.0700, POS.0960, POS.0970, POS.1020, POS.1130); the principal's question of 2026-09-30
status: immutable
---

# How everything in the forge is born

## Question

What can come into being in the forge, kind by kind — a project, an
artefact of the chain, a recipe, a render, a source, a research note,
a decision, a critic lens, a challenger persona, a check, a layer, a
genre, a script — and for each kind: what must the principal do, in
what order, what must he supply or decide, which command, skill,
script or agent does the work, and what is written where when it is
done? The principal asked for this on 2026-09-30 as research on the
forge itself, so that the way things are born is read from the
definitions once and written down, instead of being rediscovered at
every birth.

## Method and epistemic status

No web source: the subject is the engine, and its definitions are the
primary source. Every skill, state file, genre file, agent file,
template and script header of the engine at commit c95cffe was read
in full; CLAUDE.md and the positions of the forge intent that own the
relevant rules were read for what the skills cite. Where a definition
says how something is born, this note repeats it in short and names
the file. Where no definition says it, the note says so plainly: a
gap in the definitions is a finding of this research, not a rule the
note invents. Everything marked *(Claude)* is Claude's reading beyond
what the definitions say.

## The inventory

Every kind of thing that can be created in the forge, in the groups
of CLAUDE.md, with the door that creates it. "Door" is the command
the principal types, or the act he performs; "by hand" means the
engine has no command for it and the principal or Claude edits files
directly, on the principal's word.

| Group | Kind | Door | Definition |
|---|---|---|---|
| instance | a configured instance of the forge | `/setup` | `.claude/skills/setup/SKILL.md` |
| instance | a git identity per host | `/setup` (offered), or by hand in `~/.gitconfig` | `.claude/skills/setup/SKILL.md`; CLAUDE.md, Persistence |
| project | thought project | `/new-project <slug>` | `.claude/skills/new-project/SKILL.md` |
| project | library (`lib-<name>`) | `/new-project lib-<name>` | same, Library paragraph |
| project | imported project | `/import-project <git-url>` | `.claude/skills/import-project/SKILL.md`, `scripts/forge-clone.ps1` |
| project | spun-off project | `/spinoff <project> <group> <slug>` | `.claude/skills/spinoff/SKILL.md` |
| project | the project's git repository and remote | by hand, one command from CLAUDE.md, Persistence | CLAUDE.md, Persistence |
| project | a branch | `scripts/forge-branch.ps1 <slug> <branch>` | the script's header |
| project | a tag | `/save <slug> -Tag <name>`; `v<major>` by `/release` | `.claude/skills/save/SKILL.md`, `.claude/skills/release/SKILL.md` |
| artefact | brief (`00-brief.md`) | `/new-project` step 3 → `/forge brief` | `.claude/skills/forge/states/brief.md` |
| artefact | later brief (`00-brief-<name>.md`) | `/forge brief <name>` | same |
| artefact | intent (`10-intent.md`) | `/forge intent` | `.claude/skills/forge/states/intent.md` |
| artefact | the intent's threads file (`10-intent.threads.md`) | decided (POS.0120), no door yet | 10-intent.md, POS.0120; THR.0470 |
| artefact | assignment (`20-assignment.md`) | `/forge assignment` | `.claude/skills/forge/states/assignment.md` |
| artefact | a later layer (BRD, …) | no door: a new state file, by the principal's decision | `.claude/skills/forge/SKILL.md` ("adding a layer means adding a file"); POS.0700 |
| record | history row | the write step of every versioned document | CLAUDE.md, Versioning & status; `templates/history.md` |
| record | decision (DEC) | the walkthrough verdict `reject`, or the principal's word | `templates/decisions.md`; `/critique`, `/challenge`, `/spinoff` |
| record | review (FND) | `/critique <lens> [artefact]` | `.claude/skills/critique/SKILL.md`, `critic-contract` |
| record | challenge (CHL) | `/challenge <persona> [artefact]` | `.claude/skills/challenge/SKILL.md`, `challenger-contract` |
| record | check report (nothing filed) | `/check <name> [slug]`; `/save`, `/release` | `.claude/skills/check/SKILL.md`, `check-contract` |
| resource | source (file, pasted text, bundle) | `/ingest [file] [slug]`; bare = sweep | `.claude/skills/ingest/SKILL.md` |
| resource | Markdown extract of a binary | `/ingest`, on the principal's yes → `scripts/doc2md.ps1` | same, step 3 |
| resource | a dependency on a library document | `/ingest` pointed at `projects/lib-<name>/…` | same, step 5; POS.1020 |
| resource | research note | `/research <topic> [slug]` | `.claude/skills/research/SKILL.md` |
| rendering | recipe, by genre | `/recipe <genre> [slug]` | `.claude/skills/recipe/SKILL.md`, `genres/<genre>.md`, `templates/recipe-<genre>.md` |
| rendering | recipe, outside any genre | `/recipe` bare, then conversation from `templates/recipe.md` | same |
| rendering | render (Markdown) | `/render <recipe> [slug]`; README and release notes by `/release` | `.claude/skills/render/SKILL.md` |
| rendering | plain file (`renders/<recipe>.docx\|.pptx`) | `/render`, where the recipe has a Format section | same, step 7; `scripts/md2docx.ps1`, `scripts/md2pptx.ps1` |
| rendering | published file (`published/<recipe>.<ext>`) | `/publish <recipe> [slug]` | `.claude/skills/publish/SKILL.md` |
| reviewer | critic lens | by hand from `templates/critic.md`, by the principal's decision | `.claude/skills/critique/SKILL.md`; CLAUDE.md, Isolated reviewers |
| reviewer | challenger persona | by hand from `templates/challenger.md`, by the principal's decision | `.claude/skills/challenge/SKILL.md`; same |
| reviewer | check | by hand from `templates/check.md`, by the principal's decision | `.claude/skills/check/SKILL.md`; same |
| engine | a state of `/forge` (a layer) | by hand, a file in `.claude/skills/forge/states/` | `.claude/skills/forge/SKILL.md` |
| engine | a genre of `/recipe` | by hand, two files | `.claude/skills/recipe/SKILL.md` |
| engine | a command (skill) | by hand, `.claude/skills/<name>/SKILL.md` and a row in CLAUDE.md, Commands | POS.1130 |
| engine | a script | by hand, `scripts/<name>.ps1` with a help header | CLAUDE.md, Persistence and Portability |
| engine | a template | by hand, `templates/<name>.md` | CLAUDE.md, Templates |
| engine | a working method | by hand, a paragraph in CLAUDE.md, Working methods | CLAUDE.md, prime directive 2 |
| engine | an ID prefix, a convention, a section | by hand, after a decision | CLAUDE.md, prime directive 2 |
| engine | a release of the engine | `/release forge` | `.claude/skills/release/SKILL.md`; POS.0300 |

Nothing in the inventory is born on Claude's own judgement. Every
row is either a command the principal types or a file the principal
has decided to have; the two rules behind that are prime directive 2
(no new convention unilaterally) and the working method Step by step
(the birth of a versioned document is a step on the principal's word).

## What each birth takes

For each kind: what the principal does and in what order, what he
must supply or decide, what is created and registered, and what
follows. The order of the groups is the order in which a new user
meets them.

### 1. The instance

**`/setup`**, once, after cloning the engine and before any other
work. The principal answers two questions, one per message: the
conversation language, then the principal's role. The command copies
`templates/CLAUDE.local.md` to the engine root and fills it; the file
is gitignored. It then asks for the git hosts he will push to with a
name and an e-mail for each, and offers to write, on his word, the
`includeIf` stanzas and the `.gitconfig-<host>` files into the global
git configuration (the file `scripts/forge-status.ps1` names), plus
the guard `user.useConfigOnly = true`; declined, it prints the text
for him to apply by hand. It creates `.claude/settings.local.json`
with the model set to Fable and says so as a notice. It never
overwrites an existing file and runs no git operation. It ends by
pointing at `/new-project` or `/import-project`.

What the principal supplies: the language, his role, the hosts with
identities (may be left for later). What he decides: whether the
stanzas and the guard are written.

### 2. Projects

**A thought project — `/new-project <slug>`.** The slug is
lowercase with hyphens; an existing directory stops the command. The
command asks the kind where the slug leaves it open (`lib-` means
library) and the language of the chain artefacts (English unless he
names another). It creates the folders `sources/`, `reviews/`,
`challenges/`, `research/` with the two `00-INDEX.md` from
`templates/index.md`; `ledger.md` from `templates/ledger.md` with
slug, `kind: thought`, language and date, the brief row as 0.1 draft
pending; `decisions.md` from `templates/decisions.md`;
`recipes/readme.md` and `recipes/release-notes.md` from their genre
skeletons, each with a history companion from `templates/history.md`.
Then it asks for the brief and hands it to `/forge brief` (below). It
creates neither intent nor assignment: those are born by their own
first `/forge <state>`. It ends by proposing `/forge intent` and
reminding him that the project is not under git.

What the principal supplies: the slug, the kind, the language, the
brief text (or the word that it will be composed). What he decides:
whether the brief is finished and locked. `logo.png` is his to add,
optional, never asked for.

**A library — `/new-project lib-<name>`.** Only the ledger (reduced
as `templates/ledger.md` says for `kind: library`), the two indexes,
`recipes/readme.md` with library inputs and its companion. No brief,
no decisions, no reviews, no release notes. The command ends by
proposing `/ingest` for the first documents. A library's documents
are maintained by their owner and may be overwritten (POS.0970).

**The repository and the remote — by hand.** The engine never
initialises a project's repository: the way in is the one line
CLAUDE.md, Persistence, names (`git -C projects/<slug> init -b main`,
then a remote if wanted). This is the principal's one-off act; the
commit identity is git's, resolved per host from the configuration
`/setup` offered. A project "not under git" is a property, not a
defect; `forge-save` skips it with a note. *(Claude)* This is the one
birth the principal performs with raw git, because the scripts carry
no URL and no identity by design (POS.0550); the deny rules of
`.claude/settings.json` forbid it to Claude, not to him.

**An imported project — `/import-project <git-url>`.** The URL is
required; the directory is the repository's name; an existing
directory stops it. On the principal's word the command runs
`scripts/forge-clone.ps1 <url>`, relays the facts the script prints
(last commit, origin, the identity git resolves, whether a ledger
with `kind:` exists) and recommends `/forge <slug>` as the first act.
It writes nothing into the project.

**A spun-off project — `/spinoff <project> <group> <slug>`.** Only
on the principal's explicit instruction. The command lists the items
of the group that will move and lets him adjust the list; creates the
new project by the `/new-project` procedure; derives its `00-brief.md`
from the relevant parts of the source intent as a draft (the one
exception to the verbatim rule), which he approves and locks through
`/forge brief` step 4; mines it into the new intent through `/forge
intent` step 2; marks the moved items superseded in the source
assignment and replaces the group with one link item, with a history
row and a DEC; updates both ledgers. The new repository is his
one-off act afterwards.

**A branch — `scripts/forge-branch.ps1 <slug> <branch>`.** Creates
the branch from the current state when it does not exist; unsaved
changes stop the switch. The branch reaches the remote by the first
`forge-save` on it. Merging is git's, by hand or by merge request; a
release runs from `main` only.

**A tag.** On the principal's word only: `-Tag <name>` on `/save`,
or asked for in words (Claude proposes `v<intent version>`). The one
fixed name, `v<major>` at an approved major of the intent, is
`/release`'s, and a major of the forge intent has a test to pass
first (POS.0300: every check, both lenses, one challenge, settled or
deferred by his word).

### 3. The chain artefacts

**The brief — `/forge brief [name]`.** Born by `/new-project` step 3
for `00-brief.md`, or by `/forge brief <name>` for every later whole
of thinking. If the file does not exist, the command creates it from
`templates/brief.md` (the minimal header only), its history companion
and its Briefs row (Mined: pending). The text arrives one of three
ways, indistinguishable to the forge: pasted whole and locked at
once; begun outside and finished here; born here by elicitation, the
principal's words unmarked and every other block opening with its
origin in italics. Claude clarifies and correlates with reality
(proposing `/research` and `/ingest`), never translates,
restructures or introduces IDs. Written once per round on his
confirmation as a 0.x bump; locked only on his explicit word at 1.0,
immutable from then. It ends by naming the state and, if locked,
proposing `/forge intent`.

What the principal supplies: the text, in whatever language and
shape. What he decides: when it is finished; the lock.

**The intent — `/forge intent`.** Inputs: the locked briefs,
`decisions.md`, the ledger; sources only as he directs. If
`10-intent.md` does not exist, the command creates it from
`templates/intent.md` as 0.1 with its companion, consolidates the
brief into Essence and Positions and derives the first Open threads;
an intent consolidated this way is `in_review` until every position
has been walked through, and no lower layer is derived before that.
Then the elicitation interview: one question per message, briefs
with a `pending` or `partial` row offered for mining first, open
threads first, contradictions and gaps probed, options with
trade-offs where he is unsure. Written once per round on his word:
rewritten for coherence, translated to the project's language,
resolved threads moved into Positions or Rejected directions, the
history row appended, the ledger updated including the Mined column.
It ends by listing what changed, what is open and whether the intent
looks stable enough for `/forge assignment`, as a recommendation.

**The threads file — decided, not yet built.** POS.0120 (intent
4.34) places the open threads in `10-intent.threads.md` beside the
intent, part of it as the history is, its births and closings
recorded in the intent's history. No state file, template or check
carries it yet; THR.0470 carries the order of the work (the threads
cut out first, then the log of the history, then the cleaning of the
intent). Until that step is done the threads stand in the intent.

**The assignment — `/forge assignment`.** Inputs: the intent,
`decisions.md`, the ledger. Claude says whether the intent is ready
to be derived from (never as a gate), drafts from
`templates/assignment.md` under the ID scheme, Requirement style and
prime directives 7 and 8, lists in Terms only what is used, asks
whether success criteria are present, delegated or absent, raises
every silence of the intent as a TBC item or a question, deletes
empty sections and template comments. Written per Versioning &
status into `20-assignment.history.md`, created with the first
draft; the ledger updated. Substance changes go intent-first; a
substance change dictated straight into the assignment gets the
intent update proposed in the same step. It ends with a delta summary
and a recommendation whether a `/critique` run is useful now.

**A later layer — no door today.** The `/forge` dispatcher says
adding a layer means adding a file to `.claude/skills/forge/states/`
named after the artefact it produces, declaring its target, inputs
and working rules; the dispatcher never changes. POS.0700 says the
mechanics of a layer are designed when the layer is actually taken
up, never in advance, and the BRD is certain to come. What the
definitions say a layer needs, gathered from the files that would
carry it: a state file; a template in `templates/`; a file number
with a gap of ten below the assignment (`30-brd.md`) and its line in
CLAUDE.md, Document chain and Repository layout; its ID prefixes,
existing or new (a new one is the principal's decision); a Documents
row in the ledger; the ledger header's `terminal:` where the chain
ends there. What it does not need: the contracts of the reviewers
read "every later layer against its parent" (essence) and take a
target by name (challenger); `check-project` verifies structure from
the layout; recipes may declare it as an input. The research of
2026-09-07 on the colleague's BRD fork adds the anti-pattern "a layer
added without an intent change" and the order it recommends: one
round of `/forge intent` designing the layer, then the state file and
the template, then reviewer calibration, then the first run.
*(Claude)* The birth of a layer is therefore three births in
sequence — a position in the forge intent, the engine files, the
first artefact of the layer in a project — and only the third has a
command.

### 4. Records

**A history row.** Never born on its own: the write step of every
versioned document appends it to `<file>.history.md`, with
`last_change` in the front-matter written by the same step. The row
of an intent, an assignment or a later layer closes with the Notes
block `templates/history.md` owns, from which the release notes are
compiled. POS.0310 (intent 4.34) replaces the table with a log of one
record per change; the operating layer has not followed yet.

**A decision (DEC).** Born by a verdict: `reject` at the walkthrough
of a critique or a challenge writes a DEC in the shape of
`templates/decisions.md` with the principal's reason; `/spinoff`
records one; any decision of the principal that overrules a finding
or settles a matter may be recorded as one on his word. Append-only,
numbered in the global sequence; a later decision supersedes by a new
record that names the old one.

**A review (FND) — `/critique <lens> [artefact] [slug]`.** Bare, the
roster of `.claude/agents/critic-*.md` with a recommended fit. With
a lens, the command invokes the `critic-<lens>` subagent with the
project path and the target and nothing else; the agent reads the
chain and `reviews/`, re-tests its own resolved findings first,
writes `reviews/YYYY-MM-DD-critique-<lens>.md` (immutable) and adds
the FND rows to the ledger. Back in the session Claude verifies the
bookkeeping, presents the delta summary and offers a walkthrough;
`accept` iterates the artefact through `/forge`, `reject` writes a
DEC, `park` and `obsolete` set the state.

**A challenge (CHL) — `/challenge <persona> [artefact] [slug]`.**
The same shape with the `challenger-<persona>` agent, which reads the
chain, `sources/` and `challenges/`, may search the web, writes
`challenges/YYYY-MM-DD-challenge-<persona>.md` and adds the CHL rows.
Best before the next layer is first derived from the target. An
accepted challenge must change the intent.

**A check report — `/check <name> [slug]`.** The `check-<name>`
agent returns its report to the session and writes no file; every
finding carries `file:line`, the rule with its owner and one fix.
Findings marked "immediate fix" are offered at once as one step; the
rest by walkthrough. `/save` runs `light`; `/release` runs `light`
and `project` on a project, `light`, `engine` and `project` on the
engine. No check runs on Claude's own judgement.

### 5. Resources

**A source — `/ingest [file] [slug]`.** Three entries: a file, text
pasted into the conversation (stored as `sources/<slug>.md` with a
two-line header), or bare, which sweeps `sources/` for unregistered
files and reports files changed since registration. Personal matter
stops the command before anything is stored. The file is copied to
`sources/<short-slug>.<ext>` (a set of related files as
`sources/<slug>/` with its own `00-INDEX.md` from
`templates/index-bundle.md`); the date is recorded best effort, never
asked. For every binary one question per file: convert to Markdown?
Yes runs `scripts/doc2md.ps1` and the extract becomes the source, the
original left out of git; no keeps the binary as a functional thing.
The index entry (`sources/00-INDEX.md`: What, Origin, Role, Use for)
and the ledger's Sources row are written; then Claude asks "what is
it for?" and writes the Role from the principal's answer. Nothing is
processed: content enters the intent only by the principal's explicit
act, cited with provenance.

**A dependency on a library document.** The principal points a
project at a document in `projects/lib-<name>/`; `/ingest` stores
nothing, writes an index entry naming the path and a row in the
ledger's Dependencies table (POS.1020). `/check light` verifies the
path exists; the `/forge` map says which libraries the project needs.

**A research note — `/research <topic> [slug]`.** One research, one
question; a topic that turns out to be several questions becomes
several notes. Claude searches, writes
`research/YYYY-MM-DD-<topic-slug>.md` (English, immutable: question,
findings with sources and dates, epistemic status, options with
trade-offs, relevance and a recommendation), adds the index entry
(Question, Answer in short, Consult when) and the ledger's Research
row, summarises for the principal leading with the recommendation,
and proposes changes to the intent or the assignment explicitly,
never silently. The principal supplies the question; a research
proposed by Claude runs on his word.

### 6. Rendering

**A recipe — `/recipe [genre] [slug]`.** Bare, the roster of
`.claude/skills/recipe/genres/` and the project's existing recipes.
With a genre (`presentation`, `readme`, `release-notes`) the genre
file's elicitation checklist runs as an interview — audience,
purpose, inputs, dramaturgy, density, diagram policy, what must not
appear, format, and always the language last, proposed from the
ledger header — and the recipe is composed from
`templates/recipe-<genre>.md`, comments and unused placeholders
deleted; written once per round with version and updated date, no
status, into `recipes/<recipe>.md` and its companion. A recipe
outside any genre is composed conversationally from
`templates/recipe.md`. Registered in the ledger's Renders table when
its first render exists. Every thought project has `readme` and
`release-notes` scaffolded by `/new-project` and iterated here; a
library has `readme` only. The command ends by offering `/render`.

**A render — `/render <recipe> [slug]`.** Only on the principal's
command or by `/release` for the README and the release notes. A
missing recipe is offered through `/recipe` first. The command reads
the recipe's inputs at their current versions and spawns one isolated
subagent on the session model that sees the recipe and its inputs
only, writes `renders/<recipe>.md` or the recipe's `output:` path
with the provenance front-matter (recipe and every input with its
version), and touches nothing else. Back in the session Claude
verifies the file and its provenance, mirrors it in the ledger's
Renders table, and — where the recipe carries a Format section — runs
`scripts/md2docx.ps1` or `scripts/md2pptx.ps1` with `-Engine pandoc`
to make the plain file beside the render; a missing pandoc is said
aloud. A Published row of the same recipe is set to `stale`. A render
is stale when any cited version differs from the current one.

**A published file — `/publish <recipe> [slug]`.** Started by the
principal only, never by `/render`, `/release` or Claude. The command
reads the recipe's Format section (a recipe without one ends at the
Markdown), takes the render as it lies on disk (never renders; a
stale render is named and he says whether to publish as it is), says
in one line what runs and that it takes minutes, and runs the script
of the format with `-Engine claude`, the recipe, the template or
reference document and the model the Format section names, into
`published/<recipe>.<ext>`. Then the Published row: file, recipe with
version, the render it was made from, model, date, state `current`.
What the scripts need installed — pandoc, the `pptx` or `docx`
document skill of Claude Code — is their headers'; the scripts
install nothing.

### 7. Reviewers

**A critic lens, a challenger persona, a check.** All three are born
the same way and by the same authority: only by the principal's
decision, and only where what the new one finds genuinely differs
(CLAUDE.md, Isolated reviewers). There is no command: Claude creates
`.claude/agents/critic-<lens>.md`, `challenger-<persona>.md` or
`check-<name>.md` from `templates/critic.md`, `templates/challenger.md`
or `templates/check.md`, on his word, filling the front-matter (a
description that says what it reads or verifies and, for a check,
when it fits; `model: inherit`; the contract skill in `skills:`) and
the Lens section only — what it reads, what it goes after, its
categories, its own report sections; for a check the rules with
their owners and the cost. The shared conduct, isolation, report
shape and ledger step are the contract's and are never restated. The
dispatchers `/critique`, `/challenge`, `/check` and the manual `/man`
scan the agent files, so the new one appears in every roster without
any edit. The agent registers only when a description carrying a
colon is quoted, as the template comments warn.

*(Claude)* What the definitions do not say is where the decision to
have a new reviewer is recorded: today the existing ones are
positions of the forge intent (POS.0400, POS.0420, POS.1140), which
suggests a round of `/forge intent` before the file, and the check
`engine` would find an agent the intent does not know.

### 8. Extensions of the engine

Everything in this group is born by hand and by decision: the engine
has no command that creates parts of itself. The pattern is the same
every time and is the one CLAUDE.md, The system's own project,
states: a process change is complete only once the forge intent is
updated and the README re-rendered. In the order the definitions
imply:

1. **The decision** — a position of the forge intent, reached by
   `/forge intent` (a walkthrough or an interview, one write per
   round), or a brief when the whole is large (THR.0230 and THR.0360
   are being worked as briefs). Prime directive 2: a new convention,
   prefix or section is proposed, decided, then written.
2. **The files** — the state file (`.claude/skills/forge/states/`),
   the genre pair (`.claude/skills/recipe/genres/<genre>.md` and
   `templates/recipe-<genre>.md`), the skill
   (`.claude/skills/<name>/SKILL.md` with its description and
   argument hint, the row in CLAUDE.md, Commands), the agent file,
   the template, the script (`scripts/<name>.ps1`, cross-platform
   PowerShell 7 with a full help header, nothing Windows-only,
   external tools from PATH), the hook (`.claude/settings.json` and
   `scripts/hook-walkthrough.ps1` are the one instance), the
   paragraph of CLAUDE.md. Each mechanism lives in one place and is
   cited everywhere else (prime directive 10).
3. **The proof** — `/check engine` (the core against itself and
   against the forge intent), `/check single-source-of-truth` before
   a major or after a round on the operating layer, `/check project
   forge`; their findings settled by walkthrough.
4. **The record and the release** — the round's history row with its
   Notes lines for the reader; `/save forge` on the branch, `/release
   forge` from `main`, which re-renders README and release notes and
   tags `v<major>` at an approved major.

What no definition names for an extension: a checklist of the files
a state or a genre touches beyond the dispatcher's one sentence ("a
file", "two files"); the place where a new template is announced
(`/man` reads rosters, not `templates/`); the migration of existing
projects to a new convention, which CLAUDE.md states for two cases
only (the Version History companion, and the threads file once
POS.0120 reaches the operating layer) as "a `/check` finding, fixed on
the principal's word".

## What every birth shares

- **Consent per step.** Every creation that writes a file the
  principal composes is one step with the exact operation, target and
  reason, run on his word; a plan he has seen is not consent
  (CLAUDE.md, Working methods, Step by step). A birth is never a
  by-product of another operation.
- **One write per round.** The content of an artefact, a recipe or a
  brief is carried in the conversation and written once, on `write`;
  the write appends the history row, sets `last_change` and updates
  the ledger. What is only in the conversation is nowhere (prime
  directive 9).
- **Templates are the shape.** Every file the forge creates starts
  from `templates/`; the template owns the shape and the rules are
  cited from CLAUDE.md, never restated in the file.
- **The ledger knows.** Every project-level birth ends with a ledger
  row: Briefs, Documents, Renders, Published, Sources, Dependencies,
  Research, Findings, Challenges. The exceptions are the companions
  and, by POS.0120, the threads file — parts of their document.
- **Isolation for what is generated.** Reviews, challenges, check
  reports and renders are made by subagents that see the project's
  files and never the conversation.
- **Persistence is separate.** Nothing above touches git; `/save`
  and `/release` do, through the scripts alone, on the principal's
  word.

## Gaps found in the definitions

Listed as findings of this research, for the principal to weigh;
none is a rule.

1. **A layer has no birth procedure.** POS.0700 defers it by design;
   the pieces are scattered over the `/forge` dispatcher, CLAUDE.md
   and the fork research. The BRD, "certain to come", will be the
   first to need the list section 3 gathers.
2. **A reviewer's birth is described in three dispatchers with one
   sentence each** and in CLAUDE.md, Isolated reviewers, with the
   authority; where the decision is recorded is not said.
3. **The threads file is decided and not built** (POS.0120,
   THR.0470): the one artefact of the inventory whose door does not
   exist yet.
4. **The project's repository is the one birth outside the scripts**,
   by design (POS.0550); the line the principal types is in CLAUDE.md,
   Persistence, and nowhere else.
5. **A new template has no roster**: `/man` and the bare commands
   read agents, states and genres, not `templates/`; a template is
   known only through the file that cites it.
6. **`/spinoff` is the only composite birth** — project, brief,
   intent and DEC in one procedure — and the only command that
   creates a chain artefact as a by-product of another operation,
   which it reconciles with Step by step by stopping for approval at
   the brief.

## Relevance to this project and recommendation

This note is the map the principal asked for; it stands until the
definitions change, and the engine changes often — a reader should
prefer the definitions where the two differ. Recommendation, offered
once and marked as Claude's:

- Use section 3's list for a later layer and section 8's four steps
  as the checklist of every extension until the forge owns one; the
  first candidate to prove them is the BRD layer through the brief
  `brd` (THR.0360).
- Consider, in a round of `/forge intent`, one position that owns
  how the engine is extended — the four steps of section 8 and where
  the decision is recorded — so that the three dispatchers and
  CLAUDE.md cite it instead of each carrying a sentence (prime
  directive 10). Weighed against it: CLAUDE.md grows (THR.0240), and
  the pattern has worked without a rule so far.
- Nothing in this note changes the chain or any convention.
