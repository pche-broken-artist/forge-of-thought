---
project: forge
type: research
topic: how a new type is added to the forge — a fourth artefact of the chain with its elicitor, a challenger persona, a critic lens, a check, a render genre, a command, a script, a template, an ID prefix, a document kind, a working method, a project kind, a kind of reviewer — and for each what the principal decides, which files are created, which existing files must be touched, what appears on its own, how the addition is proved and where it is recorded
date: 2026-09-30
derived_from: the engine's own definitions at commit c95cffe, every place that names an existing member of each type found by search (CLAUDE.md; .claude/skills/**; .claude/agents/*.md; templates/*.md; the help headers of scripts/*.ps1; .claude/settings.json; projects/forge/recipes/readme.md); 10-intent.md v4.34 (POS.0120, POS.0400, POS.0410, POS.0420, POS.0540, POS.0580, POS.0700, POS.0960, POS.1000, POS.1070, POS.1120, POS.1130, POS.1140, POS.1170, POS.1300 to POS.1380); research/2026-09-07-brd-layer-fork-analysis.md; the principal's question of 2026-09-30, sharpened after a first note answered the wrong question; the elicitor added and the layer section rewritten to POS.1310 on 2026-09-30, on the principal's word, before the note's first save
status: immutable
---

# Adding a new type to the engine

## Question

The forge has three artefacts of the chain today: brief, intent,
assignment. What must be done to add a fourth? And the same for every
other type the engine is made of: a new elicitor (the definition of
how an artefact is found, POS.1310), a new challenger persona, a new
critic lens, a new check, a new render genre, a new command, a new
script, a new template, a new ID prefix, a new document kind, a new
working method, a new project kind, a new kind of reviewer. Not how a
brief or a review is made in a project — how the engine gains a new
member of a type. For each: what the principal decides, which files
are created and from which skeleton, which existing files name the
type's members and must be touched, what appears on its own once the
file exists, how the addition is proved, and where it is recorded.

## Method and epistemic status

The engine's definitions at commit c95cffe are the source. For each
type, every existing member was searched by name across CLAUDE.md,
the skills with their state and genre files, the agents, the
templates, the script headers, `.claude/settings.json` and the forge
README recipe; every hit is a place a new member would have to
appear, or a place that names members generically and needs nothing.
The lists below are those hits. Where the definitions state the
procedure ("adding a lens means adding an agent file"), the note
repeats it in short and names the file; where they do not, the list
is what the search found and is marked as such. Everything marked
*(Claude)* is Claude's reading beyond what the definitions say.

## The spine every addition follows

The definitions state the same five steps for every type, in
different files; gathered here once.

1. **Decision.** Prime directive 2: no new convention, prefix or
   section unilaterally — proposed, decided, then written. For
   reviewers CLAUDE.md, Isolated reviewers, adds the test: only where
   what the new one finds genuinely differs. The decision is the
   principal's word in a round of `/forge intent`; it lands as a
   position of the forge intent (every existing type has one: layers
   POS.0700, lenses POS.0410, personas POS.0420, checks POS.1140,
   commands POS.1130, contracts POS.1120, project kinds POS.0960,
   README and release-notes genres POS.1000).
2. **Files.** Created from the type's skeleton where one exists
   (`templates/critic.md`, `templates/challenger.md`,
   `templates/check.md`, `templates/recipe.md` for a genre skeleton);
   for a state file, a skill, a script or a template there is no
   skeleton and the existing members are the model. Every file
   describes only its own job and cites the owner of every rule it
   needs (prime directive 10, POS.1070).
3. **Rosters.** Two kinds exist. Scanned rosters need nothing: the
   dispatchers list `.claude/skills/forge/states/`,
   `.claude/skills/recipe/genres/` and `.claude/agents/critic-*`,
   `challenger-*`, `check-*` at the call, `/man` reads the same scans,
   and the forge README recipe builds its reviewer rosters from the
   agents' descriptions at the next release. Written rosters must be
   edited: the Commands table of CLAUDE.md names the lenses, the
   checks and the genres in its cells; Isolated reviewers names the
   two lenses; Repository layout names every script. Which type has
   which is listed per type below.
4. **Proof.** `/check engine` verifies the Commands table against the
   skills, the described agents against `.claude/agents/`, every
   `skills:` entry of an agent against an existing skill, every
   script against CLAUDE.md, the templates against the conventions,
   and the core against the forge intent. `/check
   single-source-of-truth` after a round on the operating layer finds
   a restatement. One real run of the new member — a lens on a
   project, a state file on a first artefact — is the test the
   definitions imply and none prescribes.
5. **Record and release.** CLAUDE.md, The system's own project: a
   process change is complete only once the forge intent is updated
   and the README re-rendered. The round's history row carries the
   Notes line for the reader (`Added — … For you: …`); `/save forge`
   commits; `/release forge` re-renders README and release notes.

The type-by-type lists below give steps 2 and 3 for each type, and
what of steps 1, 4 and 5 is specific to it.

## Type by type

### A fourth artefact of the chain (a layer)

The definitions: the `/forge` dispatcher — "adding a layer means
adding a file" to `.claude/skills/forge/states/`, named after the
artefact it produces; POS.0580 and POS.1310 — that file is the
definition of the artefact's elicitation in seven blocks and stands
beside the artefact's template as a pair, how we get there and what
is to come out; POS.0700 — the mechanics of a layer are designed
when it is taken up, never in advance; POS.1380 — the BRD is the
first instance of the shape of POS.1310; the research of 2026-09-07
on the BRD fork — a layer added without an intent change is an
anti-pattern, and its recommended order is one round of `/forge
intent`, then the state file and the template, then reviewer
calibration, then the first run.

An artefact and its elicitor are one birth: an artefact type without
a definition of its elicitation does not exist in the forge (POS.1300:
every artefact type has a definition of its own), and a definition
defines nothing without the template it lands in. What the elicitor
is and what its seven blocks take is the next section; this one
lists everything else a layer touches.

**Decide** (in the round of `/forge intent`): what the layer is and
for whom; what of the parent it carries and what it must not (the
assigning-not-solving boundary has an owner for the assignment, prime
directive 8, and none for a layer below it); the seven blocks of its
elicitation (next section), written whole in the intent as
POS.1330 to POS.1350 are for the three artefacts of today; its file
number, a multiple of ten below the parent (`30-<layer>.md`); its ID
prefixes, existing or new; whether every project gets it or only
those whose ledger header names it as `terminal:`; which reviewer
needs calibration; how its horizon is carried (POS.1360 gives the
BRD the phasing); the position that records all this and the update
of POS.0700.

**Create:**
- `.claude/skills/forge/states/<layer>.md` — the elicitor: the
  front-matter `description` (what `/forge` bare and `/man` print)
  and the seven blocks of POS.1310 in reading order — Target, Inputs,
  Aim, Partner, Map, Instruments, Course — every block present, a
  block empty on purpose saying so with the reason; the shared
  mechanisms (the form of the conversation, one write per round,
  versioning with history and ledger, creation from the template, the
  language question, ending by naming the state) cited and never
  repeated. The three definitions POS.1330 to POS.1350 are the
  models; the two state files of today, `intent.md` and
  `assignment.md`, predate the shape and are to be derived from
  their definitions (POS.1310: "the state files are derived from
  them"), so a new layer is born into the seven blocks and does not
  copy today's files.
- `templates/<layer>.md` — the Target's other half: front-matter
  `version`, `date`, `status`, `last_change`, `project`, `audience`
  (CLAUDE.md, Versioning & status; `check-engine` verifies the
  fields); a comment citing the rules' owners; the sections with
  their prefixes; a Terms line if the layer carries IDs. The Map
  (POS.1320) prescribes neither the template's headings nor the
  conversation's order: the two are written as a pair, not as one
  copied from the other.

**Touch** (found by search for `assignment`):
- CLAUDE.md, Document chain: the file block gains a line
  `30-<layer>.md`; the numbered list gains an item after item 3 —
  which renumbers items 4 to 7, and "Document chain 5" and "Document
  chain 7" are cited 31 times in 24 files of the engine (skills,
  templates, scripts, the README recipe). *(Claude)* Either the item
  is added without renumbering (an item "3a", or the layers listed
  inside item 3) or every citation is edited; the definitions do not
  say which.
- CLAUDE.md, Repository layout: the file on the line
  `00-brief.md  10-intent.md  20-assignment.md`.
- CLAUDE.md, ID scheme: a row per new prefix with "Lives in"; an
  existing prefix reused across layers gets its "Lives in" widened.
- CLAUDE.md, Requirement style, or the template: the style rules of
  the layer where they differ from the assignment's (the fork research
  found the BRD wants testability mandatory where the assignment has
  it recommended).
- `templates/ledger.md`, Documents table: a row `30-<layer>.md | — |
  not started | —`; existing projects add it on the principal's word.
- `.claude/skills/forge/states/<parent>.md`, closing step: the
  recommendation "stable enough for `/forge <layer>`" — today
  `intent.md` names `/forge assignment` only.
- `.claude/skills/new-project/SKILL.md`, step 4: "Do NOT create
  10-intent.md or 20-assignment.md yet" — the layer joins the list.
- `.claude/skills/challenger-contract/SKILL.md`, Inputs: names
  `20-assignment.md if it exists` and no later layer; the critic
  contract already reads "any later layer".
- `.claude/agents/critic-clarity.md`, Lens: names the three artefacts
  and carries an assignment-shaped Advisory checklist; a layer with
  its own style gets its angles here (reviewer calibration).
- The project's recipes: the readme recipe's Inputs ("the assignment
  once it exists") and the release-notes recipe's Inputs (the
  template's comment reserves "one line per later layer") — iterated
  through `/recipe` in each project that takes the layer.
- The forge README recipe (`projects/forge/recipes/readme.md`): "the
  three chain artefacts get paragraphs of equal weight" and the
  journey story — iterated so the README shows the fourth.
- The forge intent: POS.0700 and the new position.

**Needs nothing:** the Document kinds table ("later artefacts");
Versioning & status and prime directive 6 ("later layers"); the
Isolated reviewers target list ("later layers"); the Commands table
row of `/forge <state>` (`…`); `templates/history.md` (Notes block
for every later layer); `critic-essence` ("every later layer against
its parent"); `check-project` (structure from the layout, IDs from
the scheme, `terminal:` from the ledger); the release-notes genre
("later layers as they appear"); `/render` inputs; `/forge` bare and
`/man` (scan the states).

**Prove:** `/check engine`, `/check project forge`; the
`single-source-of-truth` sweep over the new definition for
restatement (POS.1380); the first `/forge <layer>` in a project on
real work, then `/critique clarity <layer>` and `/critique essence
<layer>` on the result. POS.1380 adds the rule for the rules that
move: a rule of the artefact leaves CLAUDE.md only once its definition
has been seen to hold.

**Count:** 2 files created (the pair), about 11 places touched, one
numbering question open.

### An elicitor

The definitions: POS.1300 — elicitation is the process by which the
principal and Claude find an artefact together; it differs by
artefact, and every artefact type has a definition of its own;
composing a recipe, `/setup` and the walkthrough of findings are not
elicitation. POS.1310 — the shape of a definition, seven blocks:
**Target** (the artefact's file and its template), **Inputs**,
**Aim** (what the elicitation achieves and when the artefact is
complete — the one place completion is stated), **Partner** (Claude's
stance: what he does, what he does not, who steers and who decides),
**Map** (what must be found, POS.1320: a map of areas in the
artefact's vocabulary, walked at the moments the definition names,
never a questionnaire), **Instruments** (only the forge mechanisms
this artefact uses in a way of its own, cited), **Course** (the ways
in, the order, what is offered at completion). The definition lives
in the state file of `/forge` and stands beside the template as a
pair. POS.1330 to POS.1350 — the three definitions of today's
artefacts, written whole in the intent. POS.1380 — the state files
are derived from the definitions once these have been written whole,
swept and tried; not yet done.

**When it is a birth of its own.** Never separately from an artefact:
one elicitor per artefact type, so a new elicitor is either half of a
new layer (previous section) or the rewriting of an existing
artefact's definition into the seven blocks — which is exactly the
work POS.1380 orders first for the brief, the intent and the
assignment. The genre files of `/recipe` map onto the shape (Genre
and Skeleton to Target, Role to Partner, the checklist to Map) but
are not elicitors: composing a recipe is configuration, not the
finding of knowledge (POS.1300).

**Decide:** each of the seven blocks, in the intent, whole — above
all the Aim (the only statement of completion) and the Map (what must
have been consciously considered before completion is offered);
which shared mechanisms the Instruments cite; which rules of the
artefact that CLAUDE.md carries today move into the definition
(Document chain 1 to 3, Requirement style, prime directive 8 are the
ones POS.1310 names), and in what order (POS.1380).

**Create:** the state file `.claude/skills/forge/states/<artefact>.md`
in the seven blocks, derived from the definition in the intent; where
the artefact is new, its template beside it.

**Touch:**
- CLAUDE.md, where a rule of the artefact leaves for the definition —
  Document chain 1 to 3, Requirement style, prime directive 8 — only
  after the definition has been tried (POS.1380); until then the
  rule stands in both places and the `single-source-of-truth` check
  names the owner.
- The forge intent: the definition itself as a position (POS.1330 to
  POS.1350 are the models); POS.1310's list of the definitions.
- Nothing in `/forge` (it reads the state files), `/man` (it prints
  the description and the file), the walkthrough skill or the hook
  (shared instruments, cited by the definition, never changed by it).

**Prove** (POS.1380): the definition written whole first; the
`single-source-of-truth` sweep; then tried on real work, one run from
a brief through the intent to an assignment, in the named
situations — a finished brief locked without an interview, a raw
idea, a brief that needs no research, a brief locked with a tension
left unresolved, an assignment drafted with no question asked, a
drift the provenance map catches. The proof is conduct, not the
number of lines CLAUDE.md loses.

**Count:** 1 file created (2 with a new artefact's template), 1 to 3
places of CLAUDE.md emptied later, 1 intent position. The cheapest
type to add and the one the forge has not yet added once: the three
definitions stand in the intent and no state file has the shape.

### A challenger persona

The definitions: `/challenge` — adding a persona means adding an
agent file from `templates/challenger.md`; CLAUDE.md, Isolated
reviewers — by the principal's decision, where the blind spots it
hunts genuinely differ; POS.0420 — one agent per persona, defined by
its blind spots, the contract invariant.

**Decide:** who the persona is to the principal (a role of its own,
never his mirror), its register, the blind spots that no existing
persona hunts.

**Create:** `.claude/agents/challenger-<persona>.md` from
`templates/challenger.md`: `name`, `description` (in single quotes
where it carries a colon, or the agent does not register — the
template's warning), `tools`, `model: inherit`, `skills:
challenger-contract`; the Lens section with the two parts, who you
are and what to go after. Nothing the contract owns.

**Touch** (search for `cto`): nothing is required. CLAUDE.md names
the first persona as an example only ("Personas, the first `cto`";
Commands table "e.g. `cto`"). The forge intent gets the decision —
*(Claude)* a line in POS.0420 or a position of the persona's own,
since check `engine` reads "every position honoured", not "every
agent known".

**Needs nothing:** `/challenge` bare, `/man`, the README roster
(bullets from the descriptions at the next release).

**Prove:** one run on a project; `/check single-source-of-truth` for
a Lens that restates the contract.

**Count:** 1 file created, 0 files touched, 1 intent entry.

### A critic lens

The definitions: `/critique` — an agent file from
`templates/critic.md`; Isolated reviewers — by the principal's
decision, where what it finds genuinely differs; POS.0410 — the
critic has two lenses, and why.

**Decide:** what the lens reads (each artefact alone, the chain as a
whole, or a scope of its own), what it goes after that neither
`clarity` nor `essence` does, its finding categories, when it fits
(the sentence `/critique` bare says per lens).

**Create:** `.claude/agents/critic-<lens>.md` from
`templates/critic.md`: front-matter as above with `skills:
critic-contract`; the Lens section's four parts — what you read, what
to go after, categories, own report sections.

**Touch** (search for `clarity|essence`):
- CLAUDE.md, Isolated reviewers: "Lenses `clarity` (each artefact on
  its own) and `essence` (each layer against its parent)" — a written
  roster.
- CLAUDE.md, Commands table, row `/critique`: "(`clarity`,
  `essence`)" and the parenthesis on what each narrows to.
- `.claude/skills/critique/SKILL.md`, bare form: the fit sentence
  ("`essence` as soon as a second layer exists, `clarity` before a
  handover") gains the new lens's moment.
- The forge intent: POS.0410 ("two lenses").

**Needs nothing:** the contract (regression first works over the
lens's own reports, of which there are none yet), `/man`, the README
roster.

**Prove:** one run; `/check engine` (the Commands table names it now);
`/check single-source-of-truth`.

**Count:** 1 file created, 3 places touched, 1 intent position.

### A check

The definitions: `/check` — an agent file from `templates/check.md`;
POS.1140 — the roster open, a new check one file, each owning one
concern and none another's; composition is `/save`'s and `/release`'s;
checks never call each other.

**Decide:** the one concern; which existing check gives it up (each
check names its neighbours' concerns as "never yours"); whether it
runs at a save, at a release, or on the principal's word only; when it
fits (its description says so).

**Create:** `.claude/agents/check-<name>.md` from `templates/check.md`:
front-matter with `skills: check-contract`, a description that says
what it verifies and when it fits; the Lens section's three parts —
what you read, what you verify with the owner of every rule cited and
never restated, cost.

**Touch** (search for the four check names):
- CLAUDE.md, Commands table, row `/check`: "(`light`, `project`,
  `engine`, `single-source-of-truth`)" — a written roster.
- `.claude/skills/save/SKILL.md` step 1a or
  `.claude/skills/release/SKILL.md` step 2, where the check joins a
  composition.
- The neighbouring checks' Lens sections that hand a concern to
  another by name (`check-light` → `project`; `check-project` →
  `light`; `check-engine` → `project`, `light`,
  `single-source-of-truth`) — where the new check takes a concern
  from one of them.
- The forge intent: POS.1140 lists the checks and their concerns.

**Needs nothing:** `/check` bare, `/man`, the README roster.

**Prove:** one run on its target; `/check engine`.

**Count:** 1 file created, 1 to 3 places touched, 1 intent entry.

### A render genre

The definitions: `/recipe` — adding a genre means adding two files,
`.claude/skills/recipe/genres/<genre>.md` and
`templates/recipe-<genre>.md`; the genre skeleton extends
`templates/recipe.md`, never replaces it (`check-project` bullet 5);
every genre closes with the language question and the composition
from the skeleton (`/recipe` step 2).

**Decide:** the kind of render and its output; the elicitation
checklist; whether every project carries a recipe of this genre (as
`readme` and `release-notes` do, POS.1000) or only those that ask;
its format section if any.

**Create:**
- `.claude/skills/recipe/genres/<genre>.md` — `description`; the line
  "Genre: … Skeleton: …" (and "Output: …" where fixed); Role; the
  elicitation checklist; the closing line citing `/recipe` step 2.
- `templates/recipe-<genre>.md` — the front-matter of
  `templates/recipe.md` (`project`, `purpose`, `audience`, `version`,
  `updated`, `last_change`, optional `output`), a comment citing
  Document chain 7, Inputs, Instructions, Format where the genre has
  one, Template.

**Touch** (search for the three genre names):
- CLAUDE.md, Commands table, row `/recipe`: "(`presentation`,
  `readme`, `release-notes`)" — a written roster.
- Only if every project carries it: CLAUDE.md, Document chain 7 (the
  sentence naming the two mandatory recipes), Repository layout,
  `.claude/skills/new-project/SKILL.md` step 2 (scaffold), the
  `check-project` Structure bullet ("the README and release-notes
  recipes … exist").
- The forge intent: a position (POS.1000 owns the two mandatory
  genres; `presentation` has none of its own).

**Needs nothing:** `/recipe` bare, `/man`, `/render`, `/publish`
(they read the recipe's Format section, not the genre).

**Prove:** one recipe composed through it and rendered; `/check
engine` (templates against the conventions: recipe templates carry no
status).

**Count:** 2 files created, 1 place touched (4 more if mandatory), 1
intent position.

### A command

The definitions: POS.1130 — every command is a skill,
`.claude/skills/<name>/SKILL.md`; supporting files (states, genres)
are read by path and registered as nothing; a contract is a skill of
the same directory, not user-invocable. `check-engine` verifies the
Commands table against the skills on disk, contracts excepted.

**Decide:** the purpose in one line; the arguments; whether only the
user may start it (`disable-model-invocation: true` — nine commands
carry it today: `/setup`, `/new-project`, `/import-project`,
`/ingest`, `/render`, `/publish`, `/save`, `/release`, `/spinoff`;
the reviewers, `/forge`, `/recipe`, `/research`, `/ledger`, `/check`
and `/man` do not); whether it needs a script or an agent.

**Create:** `.claude/skills/<name>/SKILL.md` — front-matter
`description` and `argument-hint`; the procedure, citing every
mechanism it uses by path and adding nothing to how it runs
(POS.1070). An alias is a two-line skill that names the original
(`manual` → `man`).

**Touch:**
- CLAUDE.md, Commands table: one row (the README's Commands table
  mirrors it one to one at the next release).
- The forge intent: the command's position.
- `.claude/settings.json` only where the command must be denied a
  raw tool (the git deny rules are the one instance).

**Needs nothing:** `/man` (reads the table and the skill).

**Prove:** `/check engine` (table ↔ skills); one run.

**Count:** 1 file created, 1 place touched, 1 intent position.

### A script

The definitions: CLAUDE.md, Persistence — the scripts are the only
door to git, each described in full by its help header; Portability
— cross-platform PowerShell 7, nothing Windows-only, external tools
from PATH, help examples free of Windows paths; `check-engine` —
every file in `scripts/` is described in CLAUDE.md (layout comment and
governing rule) and nothing described is missing.

**Decide:** what the script does that no existing one does; which
command is its door (a script is used through its command, never
directly, POS.1070 — `doc2md` through `/ingest`, `md2pptx` and
`md2docx` through `/render` and `/publish`, `forge-clone` through
`/import-project`); what it may never carry (a URL, an identity —
POS.0550).

**Create:** `scripts/<name>.ps1` — `#Requires -Version 7`; a help
header with `.SYNOPSIS`, `.DESCRIPTION` (what it does, what it needs
installed, what it never does) and `.EXAMPLE`; the Portability rules
in the body; installs nothing.

**Touch:**
- CLAUDE.md, Repository layout: the `scripts/` comment lists every
  script by name and job.
- CLAUDE.md, the governing rule: Persistence for a git script (the
  sentence listing the five), Document chain 5 or 7 for a conversion.
- The command that calls it, by path, with what it passes.
- `.gitignore` where the script writes local files.
- The forge intent: the position of the mechanism it serves.

**Prove:** `/check engine` (scripts ↔ CLAUDE.md); one run on each
platform the principal has.

**Count:** 1 file created, 3 to 4 places touched.

### A template

The definitions: CLAUDE.md, Templates — canonical skeletons for every
new project; `check-engine` — templates agree with the conventions
(front-matter fields including `last_change`, the history companion,
prefixes, numbering, statuses, no Version History table in the body,
no status on a recipe template); every template comment cites the
owner of the rule and never restates it.

**Decide:** which file the template instantiates and which command or
state creates it; whether the document is versioned (then the
front-matter of Versioning & status and a companion from
`templates/history.md`) or freely rewritten (then `project` and
`updated`, as the ledger and the indexes have).

**Create:** `templates/<name>.md` — the front-matter, a comment
citing the owners, the sections with placeholders in angle brackets
and one sample item where IDs are used.

**Touch:**
- The command, state or agent that creates the file from it — a
  template no file cites is dead; there is no roster of templates
  (`/man` reads agents, states and genres, not `templates/`).
- CLAUDE.md where the skeleton is named beside its rule (Document
  chain 1 names `templates/brief.md`, Isolated reviewers the three
  reviewer skeletons, Ledger `templates/ledger.md`).

**Prove:** `/check engine`; one file made from it.

**Count:** 1 file created, 2 places touched.

### An ID prefix

The definitions: CLAUDE.md, ID scheme — three letters, `PREFIX.NNNN`,
the table with "Lives in"; `check-project` verifies ID hygiene against
the scheme in every document that carries IDs; prime directive 2.

**Decide:** what the item is that needs an identity of its own and
which document carries it; whether it has states (then it is a record
with a ledger table, as FND and CHL) or none (as POS, REQ).

**Touch** (no file is created):
- CLAUDE.md, ID scheme: the row.
- The template of the document that carries it: a sample item; for
  the assignment the Terms line lists the prefixes used.
- Where the items have states: `templates/ledger.md` gains a table
  (`check-light` verifies the ledger's shape against the template),
  the producing contract or command gains the ledger step, and the
  README's conventions section reproduces the prefix table on its
  own.

**Count:** 0 files created, 2 to 4 places touched.

### A document kind

The definitions: CLAUDE.md, Document kinds — every document has one
kind, the table says what it is, who writes it, whether it is
versioned and how it behaves; the layout and the chain block list the
files.

**Decide:** the row of the kinds table (group, kind, meaning, written
by, versioned, behaviour); which command or state writes it; whether
it has a ledger row; whether the reviewers read it.

**Touch:** the kinds table; Document chain (the file block and the
item of the document it belongs to); Repository layout; the template
and the command or state that creates it; the ledger template if it
has a row; `check-light` (bookkeeping of a versioned or unversioned
file) and `check-project` (structure); the contracts' Inputs if the
reviewers read it.

The live example is the intent's threads file, decided in POS.0120
(intent 4.34) and not yet built: the analysis of 2026-09-30 for
THR.0470 found the places it touches — CLAUDE.md Document chain 2, the
file block, Repository layout, the ID scheme row of THR ("Lives in"),
the Ledger paragraph; `templates/intent.md` and a new
`templates/intent.threads.md`; `.claude/skills/forge/states/intent.md`;
the Inputs of both reviewer contracts; `check-light` and
`check-project`; `.claude/skills/new-project/SKILL.md` step 4; the
forge README recipe. Fourteen places for one unversioned file.

**Count:** 1 to 2 files created, about 10 places touched.

### A working method

The definitions: CLAUDE.md, Working methods — the forge's vocabulary
of collaboration, none a command, each a bold name with a paragraph;
the walkthrough shows a method with a shape kept in a skill
(`.claude/skills/walkthrough/SKILL.md`, `user-invocable: false`) and a
rule repeated by the per-prompt hook (POS.1170: a rule that must hold
in a long conversation is not trusted to CLAUDE.md alone); `/man
<method>` prints the paragraph and the skill; the forge README's "How
the work feels" section lists every method in CLAUDE.md's order under
its name.

**Decide:** the name; when the method applies; whether it has a shape
worth a skill; whether it must be repeated by the hook; the word the
principal types, if any (`write`, `??`, the verdict letters).

**Create:** the paragraph in CLAUDE.md, Working methods; a skill
where there is a shape.

**Touch:** `scripts/hook-walkthrough.ps1` where the hook must carry
it; the forge intent (the Working methods group of positions, from
POS.0850).

**Needs nothing:** `/man`, the README section.

**Count:** 0 to 1 file created, 2 to 3 places touched.

### A project kind

The definitions: POS.0960 — a project has a kind declared in its
ledger header, the rules of a kind live in the engine and the project
carries only the marker; two kinds today, `thought` and `library`.

**Touch** (found by following `library` through the engine): the
`templates/ledger.md` header comment (which tables the kind keeps);
`.claude/skills/new-project/SKILL.md` (scaffold by kind);
`.claude/skills/forge/SKILL.md` step 3 (what the map reports for the
kind); `.claude/agents/check-project.md` bullet 0 (what the kind
reduces the checks to); `.claude/skills/ingest/SKILL.md` (what a
changed source means in the kind); CLAUDE.md, Repository layout (a
block per kind) and the Document kinds paragraph; the README recipe's
conventions ("project kinds — `thought` and `library`"); the forge
intent (POS.0960, POS.0970).

**Count:** 0 files created, about 8 places touched. The heaviest
type after the layer.

### A kind of reviewer

The definitions: POS.1120 — each kind owns one contract skill
`.claude/skills/<kind>-contract/SKILL.md`, named in the front-matter
of every agent of the kind; three contracts and no common skill,
"reopened only if a fourth kind repeats them"; CLAUDE.md, Isolated
reviewers, enumerates the three kinds with their outputs.

**Create:** the contract skill (`user-invocable: false`; subject, way
of working, output shape, ledger step); the agent skeleton
`templates/<kind>.md`; the command `.claude/skills/<command>/SKILL.md`
(bare = roster, with a name = run, the walkthrough verdicts and what
each writes); the first agent.

**Touch:** CLAUDE.md, Isolated reviewers (the sentence enumerating
the kinds and their outputs; the skeleton list; the contract list);
the Commands table; the ID scheme and `templates/ledger.md` if it
files records; `check-single-source-of-truth` (its "Reviewer files
carry only their own" bullet names the three agent prefixes); the
forge intent (POS.1120, and a position for the kind).

**Needs nothing:** the README's reviewer section ("every kind that
comes after").

**Count:** 4 files created, about 6 places touched.

## What the search shows across the types

| Type | Skeleton exists | Files created | Written rosters to edit | Scanned rosters (free) |
|---|---|---|---|---|
| artefact (layer) with its elicitor | the seven blocks (POS.1310), the three definitions as models | 2 (the pair) | 0, but ~11 coupling points | `/forge`, `/man`, `critic-essence`, `check-project` |
| elicitor of an existing artefact | the seven blocks; its definition in the intent | 1 (the state file rewritten) | 0; CLAUDE.md emptied of the artefact's rules later | `/forge`, `/man` |
| challenger persona | yes | 1 | 0 | `/challenge`, `/man`, README |
| critic lens | yes | 1 | 3 | `/critique`, `/man`, README |
| check | yes | 1 | 1 to 3 | `/check`, `/man`, README |
| render genre | partly (`templates/recipe.md`) | 2 | 1 (4 more if mandatory) | `/recipe`, `/man` |
| command | no | 1 | 1 | `/man`, README table |
| script | no | 1 | 3 to 4 | — |
| template | no | 1 | 2 | — |
| ID prefix | — | 0 | 2 to 4 | README table |
| document kind | no | 1 to 2 | ~10 | — |
| working method | no | 0 to 1 | 2 to 3 | `/man`, README |
| project kind | — | 0 | ~8 | — |
| kind of reviewer | partly | 4 | ~6 | README |

Four observations, from the table:

1. **The reviewers are the cheapest to extend and the layer the
   dearest.** A persona is one file and touches nothing; a layer is
   two files and eleven places, because "assignment" is written into
   the operating layer where "the last layer" was meant. *(Claude)*
   The definitions could name the parent and the terminal instead of
   the assignment in the places listed above; then a layer would cost
   what a persona costs.
2. **Written rosters are the friction.** Every place that had to be
   edited for a lens, a check or a genre is a list of names inside a
   sentence of CLAUDE.md, while the same names are read from disk by
   the dispatchers. The engine check would find the drift; the
   definitions do not say why the Commands table names the members
   at all.
3. **The numbering of Document chain couples the chain's growth to
   thirty-one citations.** The first fourth layer will meet it.
4. **An artefact and its elicitor are one birth, and the shape for
   it exists before any file has it.** The seven blocks are decided
   (POS.1310), the three definitions are written (POS.1330 to
   POS.1350), and every state file on disk still has the older
   shape; the first layer added will be born into the new shape while
   its neighbours wait for POS.1380's rewrite. *(Claude)* Adding the
   BRD before the three state files are derived means two shapes on
   disk at once; POS.1380's order — the elicitation first, then
   `brd` — avoids that and is the reason to keep it.

## Relevance to this project and recommendation

This note is the checklist the principal asked for; it stands until
the definitions change, and the engine changes often — where the two
differ, the definitions win. Recommendation, offered once and marked
as Claude's:

- **For the BRD layer** (THR.0360, the brief `brd`): use the layer
  and elicitor sections above as the list of the round's decisions
  and edits — the seven blocks written whole in the intent first, the
  pair of state file and template derived from them — and settle the
  Document chain numbering question before the state file is
  written, since every later layer will inherit the answer. Keep
  POS.1380's order: the three definitions into their state files
  first, so that the BRD is not the only file of the new shape.
- **For the operating layer**, one position in a round of `/forge
  intent` that owns how a type is added — the five-step spine above
  and the rule that a roster is scanned, never written — so that the
  three dispatchers, CLAUDE.md and the contracts cite it instead of
  each carrying its own sentence (prime directive 10). Weighed
  against it: CLAUDE.md grows (THR.0240), and the pattern has held so
  far without a rule. The check `engine` already guards the written
  rosters; a rule would remove them rather than guard them.
- Nothing in this note changes the chain or any convention; the
  first note of today (`2026-09-30-how-everything-in-the-forge-is-born.md`)
  answers the wider question of how the members of every type are
  made in a project, and this one how the types themselves are added.
