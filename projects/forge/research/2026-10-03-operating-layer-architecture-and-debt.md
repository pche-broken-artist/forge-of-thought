---
project: forge
type: research
topic: how the operating layer of the forge is built today (CLAUDE.md, the skills with their contracts, state and genre files, the agents, the settings, the templates, the scripts) and where its technical and architectural debt lies - the same kind of thing done in different ways, what CLAUDE.md carries for single commands, rules stated more than once, the parts rewritten most often, naming, duplicated script logic
date: 2026-10-03
derived_from: the engine's own files as they stand on 2026-10-03, read in full (CLAUDE.md; .claude/skills/**; .claude/agents/*.md; .claude/settings.json; templates/*.md; scripts/*.ps1); projects/forge/10-intent.history.md and 10-intent.history.archive.md searched by subject, never loaded whole; 10-intent.md (POS.0830, POS.0940, POS.1070, POS.1090, POS.1130) and 10-intent.threads.md (THR.0150, THR.0240, THR.0320, THR.0400, THR.0460, THR.0480, THR.0500); reviews/2026-09-05-critique-harness.md and reviews/2026-10-02-check-single-source-of-truth.md; research/2026-09-30-adding-a-new-type-to-the-engine.md and research/2026-09-30-how-everything-in-the-forge-is-born.md; the draft brief 00-brief-next-gen.md v0.1, section "A technical clean-up"; no web source
status: immutable
---

# The operating layer: how it is built and where its debt lies

## Question

How is the operating layer of the forge built today, and where is its
technical and architectural debt? The draft brief `next-gen` asks, in
its section "A technical clean-up", to standardise how the single
things are done, to take as much as possible out of CLAUDE.md and to
name the debt of a system that grew step by step. This note is the
inventory and the list of debts with evidence; it gives options and
one recommendation of what a standard architecture of a mechanism
could look like. It is findings and options, not a redesign.

## How it was read

No web source: the subject is the engine, and its files are the
primary source. Every file of the operating layer was read in full on
2026-10-03 and its lines counted (blank lines included). Counts of
citations and of repeated phrases were made by pattern search over
the same files. The history of the forge intent was searched by
subject and by ID, never loaded whole: the log
(`10-intent.history.md`, 138 records, versions 4.42 to 4.50) and the
archive table (`10-intent.history.archive.md`, 150 rows, versions 0.1
to 4.41).

Epistemic marks used below:
- **verified** - read in the named file at the named line;
- **counted** - the result of a pattern search, with the pattern's
  limits said where they matter;
- **hypothesis** - Claude's reading beyond what the files say.

What the two notes of 2026-09-30 already establish is cited and not
repeated: `2026-09-30-how-everything-in-the-forge-is-born.md` (what
can be created and through which door) and
`2026-09-30-adding-a-new-type-to-the-engine.md` (what adding a member
of each type costs, the scanned and the written rosters, the coupling
of a layer to the word "assignment", the ordinal numbering of
Document chain). One correction to the second: the lens, check and
genre names it found written into the Commands table of CLAUDE.md are
gone since intent 4.49 (verified: CLAUDE.md:619-639; ledger FND.0610
and FND.0630, resolved).

## Key findings

### 1. The inventory

The operating layer is 63 files and 4,995 lines (counted).

| Part | Files | Lines | What it is |
|---|---|---|---|
| `CLAUDE.md` | 1 | 650 | always-on context: constitution, catalogue and manual at once |
| command skills `.claude/skills/<name>/SKILL.md` | 18 | 881 | one procedure per command |
| state files `.claude/skills/forge/states/` | 3 | 386 | the definition of each chain artefact's elicitation |
| genre files `.claude/skills/recipe/genres/` | 3 | 108 | the elicitation checklist of a recipe genre |
| contract skills `<kind>-contract` | 3 | 325 | what every reviewer of a kind shares |
| method skill `walkthrough` | 1 | 93 | the shape of a working method |
| agents `.claude/agents/` | 8 | 434 | one reviewer each: front-matter and a Lens section |
| `.claude/settings.json` | 1 | 27 | two git deny rules, two read deny rules, one per-prompt hook |
| `templates/` | 17 | 706 | skeletons of four different kinds of file |
| `scripts/` | 9 | 1,385 | git (5), conversions (3), the hook (1); all PowerShell |

CLAUDE.md by section (verified by heading lines): What this workspace
is 21, Roles 7, Prime directives 63, Working methods 55, Document
kinds 32, Document chain 145, Repository layout 80, Persistence 51,
Versioning & status 48, ID scheme 27, Requirement style 5, Isolated
reviewers 55, Spin-off rule 7, Ledger 16, Commands 26, The system's
own project 8, Templates 2.

The mechanisms the layer implements, and how (all verified in the
named files):

| Mechanism | Where it lives | How it works |
|---|---|---|
| a command | `SKILL.md` with `description`, `argument-hint` | prose procedure read on invocation; nine carry `disable-model-invocation: true` (POS.1090) |
| a dispatcher over members | `forge`, `recipe`, `critique`, `challenge`, `check` | bare = roster by scanning a directory; with a name = read the member's file and follow it |
| an artefact's definition | `states/<state>.md` | seven named blocks in prose (Target, Inputs, Aim, Partner, Map, Instruments, Course) plus "How the files are made" |
| a reviewer | agent file + contract skill preloaded through `skills:` | isolated subagent; the contract owns conduct and output, the agent only its Lens |
| a render | `/render` + recipe | a `general-purpose` subagent prompted by the session writes the file; the session mirrors the ledger |
| a conversion | `/ingest`, `/render`, `/publish` + a script | the skill calls a script; pandoc or headless Claude Code inside |
| persistence | `/save`, `/release` + `forge-*.ps1` | skills compose checks, renders and the script; raw git denied in settings |
| the write of a round | no file of its own | prime directive 9, Working methods, Versioning & status, the walkthrough skill, each state file |
| a rule that must hold every turn | `hook-walkthrough.ps1` | five constant lines printed into every prompt |
| the manual | `/man` | reads the Commands table, the Working methods and the dispatchers' scans |

### 2. The same kind of thing done in different ways

**Rosters: six ways to know what exists.** States and genres are a
scan of a directory inside the dispatcher's skill
(forge/SKILL.md:15, recipe/SKILL.md:15). Reviewers are a scan of
`.claude/agents/` by file-name prefix (critique/SKILL.md:17-18,
challenge/SKILL.md:17-18, check/SKILL.md:19-20). Commands are a
written table in CLAUDE.md:619-639, which `/man` reads (man/SKILL.md:15)
and `check-engine` guards against the skills on disk
(check-engine.md:24-25). Working methods are the bold names of a
CLAUDE.md section (man/SKILL.md:39-41). Scripts are a written comment
in the layout and a written sentence in Persistence (CLAUDE.md:337-344,
424-430). Templates have no roster at all (the 2026-09-30 note on
births, gap 5). Verified.

**Dispatchers: one pattern in five wordings.** The sentence "adding a
member means adding a file; this command does not change" stands in
all five (counted: 5 hits in 5 files; forge/SKILL.md:10,
recipe/SKILL.md:11-12, critique/SKILL.md:8-10, challenge/SKILL.md:9-11,
check/SKILL.md:8-10). Two open with "Role: dispatcher" and numbered
steps, three with a description of where the members live and no
role. The three reviewer dispatchers share the frame "bare, run, when
it returns, offer a walkthrough" and differ in the middle; the
harness critique of 2026-09-05 already called `critique` and
`challenge` near-mirrors
(reviews/2026-09-05-critique-harness.md:268-274). THR.0460 carries
`/forge` and `/recipe` as "one mechanism written twice in different
shapes" (10-intent.threads.md:658-660). Verified.

**How a reviewer's output is filed: two mechanisms for three kinds.**
A critic and a challenger write their own report and edit the ledger
themselves, each taking the next ID (critic-contract/SKILL.md:79-80,
116-119; challenger-contract/SKILL.md:72-73, 107-109); their agents
carry `Write` and `Edit`. A check writes nothing and returns text; the
`/check` command gives the IDs, writes the file and the ledger rows
(check-contract/SKILL.md:73-76; check/SKILL.md:34-48); its agents are
read-only. Both draw on one FND sequence, and the command already
guards against a double ID only for checks (check/SKILL.md:46-48).
The front-matter of the three reports differs in fields: the critic
has `lens` and `reviewed`, the challenger `reviewed` and no field
naming the persona, the check `check` and no `reviewed`. The
same-day suffix `-2` is stated in three places
(critic-contract:80, challenger-contract:73, check/SKILL.md:36) and a
fourth time for sources (ingest/SKILL.md:37). Verified. THR.0500
already holds the wish for one mechanism and names the ID race
(10-intent.threads.md:850-878); this note adds only the evidence by
line.

**Other generated outputs: three more ways.** A render is written by
an ad-hoc `general-purpose` subagent whose prompt the session
composes (render/SKILL.md:18-34), a published file by a script that
starts headless Claude Code (publish/SKILL.md:30-36), a research note
by the session itself (research/SKILL.md:18-21). So "an isolated
generation with a report" has five implementations: a named agent
that files itself, a named agent whose command files, a general
subagent, a headless process, the session. Verified; that these are
one kind of thing is a hypothesis.

**How the project and the arguments are resolved: a rule per
command.** Counted in the bodies, verified by line:
- `/research`: the last token is the slug if it names a directory
  under `projects/` (research/SKILL.md:6-8), the only deterministic
  rule;
- `/forge`, `/recipe`: "$1 may be a slug; if ambiguous, ask"
  (forge/SKILL.md:13-14, recipe/SKILL.md:17-18), while the same `$1`
  is resolved as a state or a genre and an unknown one "lists the
  states and stops" (forge/SKILL.md:43-44, recipe/SKILL.md:25-29): the
  skill does not say which reading wins for `/forge <slug>`;
- `/render`, `/publish`: `$2`, or ask (render/SKILL.md:13,
  publish/SKILL.md:14);
- `/ingest`: the second argument or context (ingest/SKILL.md:7-8);
- `/critique`, `/challenge`: inferred from context, with an optional
  artefact before the slug (critique/SKILL.md:24-28);
- `/ledger`: no slug means every project (ledger/SKILL.md:6);
- `/save`: no slug means every repository with changes; `/release`:
  no slug means ask (release/SKILL.md:12-14).
The argument syntax of a command is written in three places: the
Commands table, the `argument-hint` and the body; they differ in
wording (`/ingest [file]` against `[file-or-path]`, `/recipe [genre]`
against `[genre-or-recipe]`, and the name of `/forge brief [name]`
is in neither the table nor the hint). Whether the `$1` ambiguity
bites in practice is a hypothesis; that no single definition of
"resolve the project" exists is verified.

**How one file cites another: five forms.** Counted over CLAUDE.md,
the skills, the agents, the templates and the scripts:
- by path to a skill file: 43 in 22 files;
- by path to a template: 78 in 30 files;
- by CLAUDE.md section name: 103 in 45 files;
- by ordinal inside CLAUDE.md: "Document chain N" 36 in 23 files,
  "prime directive N" 22 in 13 files;
- by step number of another skill ("`/render` step 5", "`/recipe`,
  step 2"): 12 in 9 files;
- by an ID of the forge project's intent (POS, THR, REJ): 93 in 33
  files, 39 distinct positions.
The ordinal and step forms break silently when the target is
renumbered: FND.0550 was exactly that, `/spinoff` citing numbered
steps of state files that no longer had them
(reviews/2026-10-02-check-single-source-of-truth.md:20-21). The ID
form binds the engine to one project: `release/SKILL.md` alone
carries fourteen such citations and cannot be fully read without
`projects/forge/10-intent.md`. The harness critique counted 59 such
citations on 2026-09-05 and called them inert tokens for the model
(reviews/2026-09-05-critique-harness.md:261-267); the count has
grown since. Verified counts; that the growth is a debt is a
hypothesis, and it bears directly on the brief's wish to keep the
core apart from what a user adds.

**Where the shape of a file is owned: three kinds of place.**
Project documents have skeletons in `templates/`. Report shapes live
in the contract skills. The render's provenance block, the filed
check report and the header of a pasted source live in command
skills (render/SKILL.md:38-49, check/SKILL.md:36-40,
ingest/SKILL.md:12-14). The front-matter of a research note
(`type`, `topic`, `derived_from`, `status`) has no owner anywhere:
the pattern search finds it in no template and no skill, and the
skill names only the sections (research/SKILL.md:18-21). The skill
also says "with current web sources" (research/SKILL.md:6) while
three notes of the forge, this one among them, are read from the
engine. Verified.

**Front-matter and form of the skills.** Only the three contracts
carry `name:`; the walkthrough skill, equally `user-invocable:
false`, does not (walkthrough/SKILL.md:1-4). Four skills open with
"Role:", fourteen do not. Step numbering has a "1a" (save/SKILL.md:23),
a step 0 (ingest/SKILL.md:27) and a library paragraph that excludes
"steps 3-5 below" (new-project/SKILL.md:35-36). Verified; low
weight.

### 3. What CLAUDE.md carries that single commands need

CLAUDE.md is loaded into every turn and, as THR.0240 records, into
every reviewer run: "about 600 lines, the largest block of its
context, several times its own agent body and contract together"
(10-intent.threads.md:247-256). By section, with the commands that
cite it (verified by the citations in the skills; the judgement that
nothing else needs it is a hypothesis):

| CLAUDE.md | Lines | Needed when |
|---|---|---|
| Document chain 5, external inputs and indexes (232-268) | 37 | `/ingest`, `/research`, the check `light` |
| Document chain 7, renders (271-325) | 55 | `/render`, `/publish`, `/recipe`, `/release`, `/new-project` |
| Repository layout (326-405) | 80 | `/new-project`, the checks `project` and `engine` |
| Persistence (406-456) | 51 | `/save`, `/release`, `/setup`, `/import-project`, the scripts |
| Isolated reviewers (537-591) | 55 | `/critique`, `/challenge`, `/check`, the contracts |
| Spin-off rule (592-598) | 7 | `/spinoff` |
| Requirement style (532-536) | 5 | already a pointer to the assignment's definition |
| ID scheme, the seven assignment prefixes (505-531) | 7 of 27 | `/forge assignment`, the lens `clarity` |

The first six rows are 285 lines, 44 per cent of the file. What is
left is what holds in every turn: the workspace, the roles, the
prime directives, the working methods, the document kinds, the chain
in outline, versioning, the ID format, the ledger, the list of
commands.

Three limits the files themselves state. Moving a rule from
always-on to on-demand "is a behaviour change, not a cut", to be
measured "by behaviour, never by line count"
(10-intent.threads.md:240-246). A rule of an artefact leaves
CLAUDE.md only once its definition has been seen to hold (POS.1380,
as the note on adding a type reports it). And the move has already
been made three times by the same pattern, which is the model:
the walkthrough (one sentence, a pointer to a skill and a hook,
10-intent.threads.md:258-262), the Requirement style and prime
directive 8 (now pointers to `states/assignment.md`), the brief
(CLAUDE.md:206-210 points to `states/brief.md`).

### 4. Rules stated in more than one place

The check `single-source-of-truth` ran on 2026-10-02 and filed
nineteen findings, FND.0540 to FND.0720, of which seventeen are
resolved, one rejected (DEC.0170) and one parked (FND.0650, the
genre checklists against their skeletons); what it found is not
repeated here. What stands after it (verified):

- **The identical opening paragraph of each family.** The three
  state files open with the same seven lines (brief.md:5-11,
  intent.md:5-11, assignment.md:5-11); the three contracts with the
  same ten (each SKILL.md:9-18); the three genre files close with
  the same sentence. POS.1120 decided three contracts and no common
  skill, "reopened only if a fourth kind repeats them", so the
  contracts are a decision and not an oversight; the state files have
  no such decision.
- **The walkthrough rule in three places** by design: CLAUDE.md:99-112,
  the skill, and the hook's first line
  (hook-walkthrough.ps1:25), a deliberate repetition (POS.1170).
- **One-line reminders.** "Not a defect" 8 times in 6 files, "never
  a gate" 8 in 8, "own judgement" 10 in 8, "only door" 3 in 3
  (counted). POS.1070 allows a reminder that names its owner
  (10-intent.md:1396-1401); they are legitimate, and they are also
  the measure of how much each skill re-asserts the constitution.
- **Each script describes itself twice.** The comment-based help and
  a hand-written `Show-Usage` text carry the same content in
  `md2docx.ps1` (8-61 against 103-150), `md2pptx.ps1` (8-40 against
  77-116) and `doc2md.ps1` (6-24 against 82-128).
- **Readings of older shapes, scattered.** The alias `## Build
  instructions` is handled in publish/SKILL.md:18-21,
  md2pptx.ps1:198-200, check-project.md:45-48 and
  templates/recipe.md:30-31, and not in md2docx.ps1:211; the state
  word `overruled` in templates/ledger.md:78-79,
  check-contract/SKILL.md:57-58 and critic-contract/SKILL.md:55-56;
  the retired single critic's reports in critic-contract/SKILL.md:49-51;
  `.extract.md` names in ingest/SKILL.md:68-69; dated render names
  in check-project.md:40-41; the history archive in CLAUDE.md:492-500.
  Each is correct where it stands; together they are the forge's
  compatibility layer, and it has no place of its own. POS.0940 says
  so knowingly: "no migration tool exists" (10-intent.md:1301-1302).
- **A dangling reference.** `check-project` promises "assignment
  style" in its description and excludes "Assignment style" for a
  library (check-project.md:3, 30-31), but its list of what it
  verifies has no such item (36-76); the Requirement style is the
  lens `clarity`'s (critic-clarity.md:32-36).

### 5. What the history shows was rewritten most

The intent reached 4.50 through 150 archived rows and 138 log
records (counted). Rows of the archive that mention a subject, out
of 150: CLAUDE.md 84, the README 63, recipes 52, the ledger 47, the
checks 41, save and release 39, the brief 34, the walkthrough 33,
the challenger 33, the critic 31, release notes 30. Positions named
most often in the archive: POS.0950 no instance facts in the engine
(25), POS.0570 what a release checks (23), POS.1070 one mechanism in
one place (22), POS.0550 persistence in git (21), POS.0310 the
history of a document (21), POS.0710 renders (18), POS.0730 release
notes (18), POS.0180 external inputs (18), POS.1100 save and release
(16), POS.0110 the brief (16), POS.0930 one model (16). In the log
of the last nine versions the three definitions lead: POS.1330 (6),
POS.1350 (5), POS.1380 (4).

A mention is not a rewrite: a row may cite a position without
changing it, so the numbers rank attention, not change. Read with
that limit, four areas were reworked again and again (hypothesis
from the counts): persistence with save, release and what they
check; the render line with README and release notes; the history
of a document; and the boundary of CLAUDE.md itself, since more than
half of all rows touch it. These are the areas where "who knows
whether they are right" (the brief's words) applies most, and three
of the four are served by PowerShell scripts or by bookkeeping done
in prose.

### 6. Naming

All verified in the files named; that each is worth changing is the
principal's call.
- **"forge"** is the system, the `/forge` command, the engine as a
  repository in the scripts and in `/save` ("'forge' means the
  engine", forge-save.ps1:13), the project `projects/forge` in
  `/check` (check/SKILL.md:25-26), and the author of records in the
  Document kinds table (CLAUDE.md:162-166).
- **"state"** is an artefact of the chain in `/forge <state>` and
  the directory `states/`, a "definition" in the same files, an
  "elicitor" in the research of 2026-09-30; it is also the state of
  a finding, of a challenge and of a published file, beside the
  "status" of a document.
- **"Lens"** is a member of the critic and also the name of the one
  own section of every persona and every check (`## Lens` in all
  eight agents).
- **"check"** is the kind, the command and the member ("the check
  has checks", CLAUDE.md:546); its reports are filed in `reviews/`
  beside the critic's, under the prefix FND shared with it.
- **Three stems for one family**: command `critique`, agent
  `critic-`, file `critique-<lens>`; command `challenge`, agent
  `challenger-`, file `challenge-<persona>`, directory `challenges/`.
- **`templates/`** holds four kinds of skeleton: project documents,
  agent files (`critic.md`, `challenger.md`, `check.md`), recipe
  genres, and an instance file (`CLAUDE.local.md`); CLAUDE.md:649-650
  still calls them skeletons "for every new project".
- **`hook-walkthrough.ps1`** prints two lines on the walkthrough and
  three on tools, own commands and consent (25-29); its name covers
  the smaller part.
- **Script families** by three patterns: `forge-<verb>`, `<a>2<b>`,
  `hook-<name>`; `md2pptx` defaults to the engine `claude` and
  `md2docx` to `pandoc` (md2pptx.ps1:50, md2docx.ps1:71), and the
  same pandoc option is `-Template` in one and `-Reference` in the
  other.

### 7. Scripts

- **Duplicated preamble.** The function `Fail` and the two
  preconditions stand five times (forge-save.ps1:48-61,
  forge-pull.ps1:26-39, forge-status.ps1:17-30, forge-branch.ps1:39-49,
  forge-clone.ps1:27-37). Verified.
- **Duplicated enumeration of repositories.** The block that turns a
  slug into the list of repositories is the same in
  forge-save.ps1:66-88 and forge-pull.ps1:41-58, a third variant in
  forge-status.ps1:69-72 and a fourth in forge-branch.ps1:52-62.
  Verified.
- **Two conversion scripts that are one.** `md2docx.ps1` (311 lines)
  and `md2pptx.ps1` (225) share parameter handling, the resolution of
  the output (md2docx.ps1:176-186 equals md2pptx.ps1:144-154), the
  check for pandoc, and the whole `claude` engine: the prompt, the
  invocation and its tool list (md2docx.ps1:189-239,
  md2pptx.ps1:185-222). Only the page-size patch
  (md2docx.ps1:252-292) and the slide level are specific. Verified.
- **Two styles of error handling.** The git scripts use `Fail` with
  `exit 1` and no strict mode; the conversions use `throw` and
  `Set-StrictMode`. Verified.
- **A decision not yet carried out.** Scripts are to be written in
  Python since 2026-10-02 and the PowerShell ones rewritten in time
  (POS.0830, 10-intent.md:1279-1281; THR.0150); all nine are
  PowerShell and no Python file exists (verified by listing).
  Portability is "a writing rule, not a claim" until run on Linux
  (10-intent.md:1277-1278).
- **No test.** No test file exists for any script (verified by
  listing); the brief's section on testing behaviour covers the
  instructions, and the scripts are the one part that could be
  tested by ordinary means today.
- **The hook starts a process per prompt** to print five constant
  lines (settings.json:19-21, hook-walkthrough.ps1:25-29). That this
  costs anything worth saving is a hypothesis; not measured.
- **Enforcement is thin.** Raw git is denied by two prefix patterns
  (settings.json:10-11); everything else the hook asks for is text
  in the context. THR.0400 holds the open gate. That a prefix
  pattern can be passed by a compound command is a hypothesis, not
  tried.

## The debts, ranked

Ranked by how much of the brief's next generation each one stands in
the way of (the ranking is Claude's; the evidence is above).

1. **CLAUDE.md is three documents in one**: a constitution, a
   catalogue of files and scripts, and the manual of single
   commands. 285 of 650 lines serve named commands (finding 3), and
   every reviewer run pays for all of it. It is also what a user's
   own addition cannot extend without editing the core.
2. **The write of a round has no definition of its own.** The most
   used mechanism (reflect, bump the version, append the records,
   derive `last_change`, update the ledger) is spread over prime
   directive 9, two working methods, Versioning & status, the
   walkthrough skill's last section, `/recipe` step 2 and the last
   paragraph of each state file; the dispatcher says only that it
   "follows the core conventions" (forge/SKILL.md:46-47). Its area
   is among the most reworked (finding 5), and it is where several
   people on one project collide.
3. **The engine cites its own project.** 93 citations of intent IDs
   in 33 operating files and 70 citations by ordinal or step number
   (finding 2). The first ties the core to `projects/forge`; the
   second breaks on renumbering.
4. **One family, several mechanisms.** Three reviewer kinds with two
   ways of filing and a shared ID sequence; five ways of producing a
   generated file; five dispatchers in five wordings; six kinds of
   roster (finding 2). THR.0500, THR.0460 and THR.0480 each hold a
   part.
5. **No single way to resolve the project and the arguments**
   (finding 2), with one stated ambiguity in the two main
   dispatchers.
6. **The scripts**: five copies of the preamble, the enumeration
   written four times, two conversions that are one, a language
   decision not carried out, no tests (finding 7).
7. **Compatibility has no home.** Readings of older shapes are
   scattered over skills, agents, templates and scripts (finding 4),
   and there is knowingly no migration mechanism.
8. **Shapes without an owner or with an owner of the wrong kind**:
   the research note's front-matter, `templates/` as four kinds in
   one directory, the `/research` skill that knows only the web
   (finding 2).
9. **Overloaded words** (finding 6): cheap to live with for one
   user, dearer in documentation for many.
10. **Small defects**: the dangling "Assignment style" of
    `check-project`, the `Build instructions` alias missing in
    `md2docx.ps1`, the name of the hook, uneven skill front-matter.

## Options with trade-offs

**A. Keep the architecture, keep sweeping.** The check
`single-source-of-truth` after every round on the operating layer,
small defects mended as found. Cheapest, no behaviour risk, and it
works: the sweep of 2026-10-02 settled seventeen findings. It removes
copies; it does not remove the differences of mechanism, and debts 1
to 5 stay.

**B. A standard anatomy, by convention only.** One position that
says what every mechanism consists of and how its parts are named,
and the existing files brought to it family by family as each is
next touched. No new machinery, no rule moves out of the always-on
context by itself. The risk is a convention that is written and not
followed; it needs a check that verifies the anatomy, as
`check-engine` verifies the Commands table today.

**C. Shared steps become definitions of their own.** The write of a
round, the resolution of the project, the filing of a report and the
roster each get one file that the others cite, and CLAUDE.md's
command-serving sections move into the definitions that use them.
This is the direct answer to debts 1, 2, 4 and 5 and continues what
the walkthrough skill, the state files and POS.1380 began. The
price: rules leave the always-on context, which is a change of
behaviour with nothing today to verify it (the brief's "Testing how
the engine behaves"); and a procedure cited through three files is
harder to follow than one written out.

**D. Bookkeeping into scripts.** What is purely mechanical (the next
free ID, a ledger row, a history record with `last_change`, the
roster listing, the engine's own consistency) is done by a script
and no longer by the model following prose. It removes the ID race,
makes a part of the engine testable, and is the natural content of
the Python rewrite already decided. The price is the one THR.0500
names: a script must know the shape of a report and of a ledger
table, which the templates and contracts own today, so the shape
stands in two places unless the script reads it from the skeleton;
and Markdown tables are a poor data store for a program.

The four are not exclusive: A is today's state, B is a decision, C
and D are the work B would order.

## Relevance to this project and recommendation

For the brief `next-gen`: its section "A technical clean-up" can
name the debt by this list, and three of its other sections meet the
same debts from another side. User modifications need debts 1, 3 and
4 answered (a core that a user can extend without editing it, and
members found by scanning). Several people on one project meet debt
2 and the ID sequences. Upgrade and compatibility meets debt 7.
Testing meets the limit of option C. The clean-up is therefore not a
separate tidying but the ground the other sections stand on;
whether it comes first is the principal's to decide.

Recommendation, offered once and marked as Claude's: decide option B
first, as one position, and let C and D follow family by family,
never as one rebuild. What a standard architecture of a mechanism
could look like, drawn only from patterns the forge already has in
at least one place:

1. **One definition file per mechanism**, in a fixed set of named
   blocks, as the state files already have theirs: what it is for
   and when it applies; its arguments; what it reads; the procedure;
   what it writes and where; which other mechanisms it uses.
2. **Members are files in one scanned directory**, each with a
   `description`; a roster is never written. The Commands table and
   the script list are the two written rosters left.
3. **Every file shape has a skeleton**, of the kind of place it
   belongs to: project documents, engine parts (agent, state, genre,
   skill) and generated files (report, render, research note) kept
   apart.
4. **Citation by path and heading name only**, never by an ordinal
   or a step number; the positions a file implements named once, in
   one line apart from the instructions, as the harness critique
   proposed.
5. **Shared steps are mechanisms too**: resolving the project,
   writing a round, filing a generated file, each defined once and
   cited.
6. **What is pure bookkeeping is a script**, reading its shapes from
   the skeletons; what needs judgement stays prose.
7. **CLAUDE.md keeps what must hold in every turn** and an index of
   the mechanisms; a section moves out only together with a way to
   see that behaviour held, in the order POS.1380 already set for
   the artefacts.
8. **Compatibility has one place**: a list of older shapes and how
   each is read, which the checks cite.

A first step that is small and proves the anatomy: the write of a
round (debt 2), because every other mechanism cites it and its rules
are already complete, only scattered. The small defects of debt 10
need no decision of architecture and can be mended at the next round
on the operating layer.

Weighed against all of it: the layer works, the sweep keeps it
honest, and the principal's own word of 2026-09-26 stands against
one tool that does everything; a standard anatomy is worth its
price only if the forge is in fact to be extended by others, which
is the brief's open question, not this note's.

## What stays uncertain

- Whether rules moved out of CLAUDE.md are still followed: untested,
  and nothing in the forge can test it today.
- The history counts rank mentions, not changes; a reading of the
  records themselves, subject by subject, would be needed to say
  what was really redone and why.
- What Claude Code itself offers for these mechanisms today (skill
  arguments, forked context, plugin packaging, hooks at the end of a
  subagent): not looked up here, by the terms of this research; the
  notes `2026-08-29-claude-code-packaging.md` and
  `2026-10-02-running-reviewers-without-the-conversation.md` hold
  what was verified earlier.
- The three hypotheses marked above: the `$1` ambiguity in practice,
  the cost of the per-prompt hook, the reach of the two deny
  patterns.
