---
version: 0.7
date: 2026-10-09
status: draft
last_change: 0.7 (2026-10-09): the documentation agents share a contract and the map has a skeleton (SOL.0460).
project: forge
audience: whoever realises the solution, a person or an agent
---

# Forge of Thought — Solution design

A proposal, handed over to Claude and not yet judged by the
principal. It is a one-off move (THR.0520, step 4): the solution
stands here as it stood in the intent at 4.55, and no choice in it is
new. Every choice below is one the intent recorded, save where an
item says the judgement is Claude's. Where the intent
and its history give no reason for a choice, the item says the reason
is not recorded, and none is invented. What an item says of a file,
a research note or an open thread beyond the intent was read from
that file by Claude on 2026-10-04. Where a `Choice` names no cost,
the intent records none.

This design is the architecture of the forge. The forge cannot yet
be built from its artefacts alone, as POS.1400 asks: the detail of
every part is in the file that realises it, named in `Where`, and
the forge has no technical specification. Whoever rebuilds the forge
today needs the intent, this design and the files of the engine
together.

## How the parts work together

The forge is not a program. It is a set of instructions that Claude
Code reads, with deterministic work kept at its edge in scripts. Four
ideas carry it.

One always-on core and everything else read when its situation
arises. `CLAUDE.md` is loaded into every session and every subagent;
a command, a definition, a contract or a template is a file read
when it is invoked. What must hold through a long conversation is
repeated by a hook at every prompt.

State lives in Markdown files of the project, never in the
conversation and never in the assistant's memory. A project is a
directory: the artefacts of the chain, their history logs, the
ledger, the records of the reviewers and the resources.

Isolation is bought with subagents. A reviewer, a check and a render
each run in a subagent that sees the files it is given and never the
working conversation, all on the one session model.

Git, the conversion of documents and the hook are scripts. The
harness denies Claude raw `git`, so the scripts are the only door.

The main courses of events. A round of work: `/forge <state>` reads
the definition of the target artefact, the conversation runs by the
working methods, and one write at the round's end changes the
artefact, appends the records to its history and brings the ledger
current. A review: `/critique`, `/challenge` or `/check` launches
one isolated agent, its report is filed with IDs, the findings are
settled by walkthrough and written in one round. A render: `/render`
generates the Markdown in an isolated subagent from a recipe and its
inputs and writes the provenance; `/publish` makes the designed file
from the render as it lies on disk. Persistence: `/save` runs the
check `light` and commits and pushes through `forge-save`; `/release`
runs its checks, settles them, regenerates the README and the release
notes and then saves with the release message and tag.

Deliberately not designed here: the wording and the steps of each
command, definition, contract, template and script, which are that
file's; how an artefact is found, which is its definition's; anything
beyond the files the forge makes. No part answers POS.0600, POS.0700,
POS.0780, POS.0790, POS.0980 and POS.1380: they state a name, a
direction, a boundary kept by hand or an order of work.

## Parts

### The instruction layer
- **SOL.0010 The universal core.** `CLAUDE.md` in the engine root
  carries what must hold in every session and for every subagent:
  the roles, the prime directives, the working methods in short, the
  document kinds, the chain, the layout, persistence, versioning, the
  ID scheme, the reviewers, the ledger and the list of commands. A
  rule of one artefact is not here but in that artefact's definition
  (SOL.0120).
  Realises: POS.0005, POS.0010, POS.0020, POS.0030, POS.0040,
  POS.0050, POS.0060, POS.0070, POS.0150, POS.0170, POS.0190,
  POS.0200, POS.0220,
  POS.0230, POS.0300, POS.0320, POS.0330, POS.0430, POS.0510,
  POS.0860, POS.0880, POS.0890, POS.0900, POS.0910, POS.1080,
  POS.1030, POS.1160, POS.1210, POS.1370, POS.1410. Choice: no real
  alternative, Claude's judgement, the intent records none: it is
  the file Claude Code loads into every session;
  what it costs is its size, open as THR.0240. Where: `CLAUDE.md`.
- **SOL.0020 The instance facts.** `CLAUDE.local.md` stands at the
  engine root: gitignored, created from `templates/CLAUDE.local.md`
  and filled by `/setup` on a new machine (SOL.0150). The root is
  where Claude Code looks for it. The git identities are SOL.0550's.
  The session model lives in
  `.claude/settings.local.json`, gitignored (SOL.0600). `CLAUDE.md`,
  Isolated reviewers, which every reviewer contract cites, forbids
  instance facts in a report.
  Realises: POS.0950, POS.0060, POS.0005. Choice: one gitignored
  file at the root against instance facts in the engine's own files;
  the cost is that the file reaches the reviewers, so it must stay
  small and harmless. Where: `CLAUDE.local.md`,
  `templates/CLAUDE.local.md`.
- **SOL.0030 The per-prompt hook.** The harness's `UserPromptSubmit`
  hook adds context at every prompt; the engine's
  `.claude/settings.json` carries one such hook. It prints two lines
  on the walkthrough, the one-item rule itself, since 2026-09-27
  with the verdict line that closes a proposition, and a pointer to
  `.claude/skills/walkthrough/SKILL.md` for the full shape when a
  walkthrough or an interview runs, and three lines of conduct, the
  principal's rules, worded in `scripts/hook-walkthrough.py`. The
  hook's command is anchored at the project root:
  `.claude/settings.json` invokes it in exec form, `python` with
  `${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.py` as its one
  argument. A relative path is resolved against the session's working
  directory, not the engine root; the placeholder always names the
  root the session started in, and the exec form hands the path to
  the program without a shell.
  Realises: POS.1170, POS.0850. Choice: a hook that repeats the rule
  against trusting text loaded once; the cost is that a hook is
  context and not enforcement. The gate that would enforce the three
  lines of conduct is open, THR.0400. Where:
  `.claude/settings.json`, `scripts/hook-walkthrough.py`.
- **SOL.0040 The walkthrough skill.** The shape of the walkthrough
  and of the elicitation interview lives in
  `.claude/skills/walkthrough/SKILL.md`, read whenever a walkthrough
  or an interview runs; `CLAUDE.md` carries the rule in short and
  the pointer, and the hook repeats the one-item rule at every
  prompt (SOL.0030). The skill is not a command. What `reject`,
  `park` and `obsolete` write is this skill's; what `accept` writes
  is the skill of the command that produced the list, `critique`,
  `challenge` or `check`.
  Realises: POS.0850, POS.0870. Choice: always-on is one sentence
  and a pointer, the detail a file read when its situation arises,
  against the whole method in `CLAUDE.md`; the first instance of the
  pattern THR.0240 asks for. Where:
  `.claude/skills/walkthrough/SKILL.md`.

### The commands
- **SOL.0100 Commands are skills.** Every command lives as
  `.claude/skills/<name>/SKILL.md`. The state files of `/forge` and
  the genre files of `/recipe` are supporting files of their
  dispatcher (`.claude/skills/forge/states/<state>.md`,
  `.claude/skills/recipe/genres/<genre>.md`): read by path,
  registered as nothing, carrying a description and no registration
  field. The reviewers' contracts (SOL.0300) are skills of the same
  directory, not user-invocable. "Command" stays the word for what
  the user invokes by slash; "skill" names the file shape, commands
  and contracts alike. A skill shadows a command of the same name,
  so a migration is whole, never partial. Every `argument-hint` is
  quoted: a front-matter with CRLF line endings and an unquoted hint
  of two bracketed items fails to parse, and the harness then shows
  the body's first line as the description. No context gain: a
  command's body and a skill's alike load only when invoked, so
  THR.0240 is untouched.
  Realises: POS.0580, POS.0770, POS.1070. Choice: skills
  against command files. Grounds, how Claude Code behaves, worked
  out by Claude: custom commands have been merged into skills, a
  command file and a skill of one name create the same `/name` and
  work the same way, existing command files keep working, skills are
  the recommended form, and a skill adds what this layer wants,
  supporting files without registration, `context: fork` with an
  agent type (set aside, SOL.0330) and named `arguments`. Decided
  2026-09-06. Where: `.claude/skills/`.
- **SOL.0110 The guard against starting a command unasked.** The
  commands POS.1090 names as guarded carry
  `disable-model-invocation: true` in their front-matter. The state
  and genre files are supporting files registered as nothing and
  need no guard. The descriptions of the guarded commands thereby
  leave the always-on context. A guarded command asked for in words
  is followed as the dispatchers follow a state file. The
  commands POS.1090 names as Claude's to start carry no such field
  and stay model-invocable.
  Realises: POS.1090. Choice: the harness's field against conduct
  alone, so that Step by step rests on the harness as well as on
  `CLAUDE.md`. Decided 2026-09-05. Where:
  `.claude/skills/<name>/SKILL.md` of each guarded command.
- **SOL.0120 The `/forge` dispatcher and the definitions.** A thin
  dispatcher plus one definition file per target state, each
  declaring its own inputs: a future layer is added by one file and
  the dispatcher stays untouched. Bare, the dispatcher reports the
  state map of a project, the staleness of renders among it. The
  Terms section is in `templates/assignment.md`. When an artefact is
  complete is the Aim of its definition. When a challenge of the
  intent and of the solution design is offered is its definition's,
  under Instruments; the definitions of the brief and of the
  assignment name none.
  Realises: POS.0580, POS.1300, POS.1310, POS.1320, POS.1330,
  POS.1340, POS.1350, POS.1360, POS.1390, POS.1400, POS.1420,
  POS.0100, POS.0130, POS.0140, POS.0210, POS.0240, POS.0250,
  POS.0260, POS.0280, POS.0290, POS.0450. Choice: a dispatcher with
  state files against one command per verb; what else it was chosen
  against is not recorded. Whether `/forge` and `/recipe` are one
  dispatcher or two is open, THR.0460. Where:
  `.claude/skills/forge/SKILL.md`,
  `.claude/skills/forge/states/brief.md`,
  `.claude/skills/forge/states/intent.md`,
  `.claude/skills/forge/states/assignment.md`,
  `.claude/skills/forge/states/solution-design.md`,
  `templates/brief.md`,
  `templates/intent.md`, `templates/threads.md`,
  `templates/assignment.md`, `templates/solution-design.md`.
- **SOL.0130 The `/recipe` dispatcher and the genres.** The same
  shape as SOL.0120: a thin dispatcher plus one definition file per
  genre, the genre's skeleton in `templates/recipe-<genre>.md`. The
  genre `presentation`
  has its interview in `.claude/skills/recipe/genres/presentation.md`
  and its render is turned into a PowerPoint file by SOL.0430. The
  genres today are `presentation`, `readme` and `release-notes`,
  each invoked as `/recipe <genre>`.
  Realises: POS.0770, POS.1000. Choice: no real alternative once
  SOL.0120 stood, Claude's judgement, the intent records none.
  Where: `.claude/skills/recipe/SKILL.md`,
  `.claude/skills/recipe/genres/`, `templates/recipe.md`,
  `templates/recipe-<genre>.md`.
- **SOL.0140 The manual.** `/man` reads the forge's own definitions
  and prints them. The alias `/manual` is
  a second skill whose whole body invokes the first, since a skill
  has no alias field.
  Realises: POS.1190, POS.1070. Choice: no real alternative for the
  alias. Where:
  `.claude/skills/man/SKILL.md`, `.claude/skills/manual/SKILL.md`.
- **SOL.0150 The first run.** `/setup` fills `CLAUDE.local.md` from
  its template and creates `.claude/settings.local.json` with the
  session model. It closes with the git identity: it offers to write
  the `includeIf` stanzas into the global git configuration file git
  actually reads (named by `scripts/forge-status.py`, the stanza
  paths absolute, since `~` in git's hands and in the shell's may
  differ), each `.gitconfig-<host>` beside that file created with
  its `[user]` when missing, together with the global guard
  `user.useConfigOnly = true`: the file read first, never
  overwriting existing content, an existing stanza or guard reported
  and left. Where the file carries a global `user.name` or
  `user.email`, `/setup` says the guard only bites once that
  identity is removed and offers the removal, again only on the
  user's word.
  Realises: POS.1050, POS.0950. Choice: no real alternative
  recorded. Where: `.claude/skills/setup/SKILL.md`,
  `templates/CLAUDE.local.md`, `.claude/settings.local.json`,
  `scripts/forge-status.py`.
- **SOL.0160 A project is born or brought in.** `/new-project`
  scaffolds a project by its kind from `templates/`, asks for the
  founding brief and hands it to the procedure of `/forge brief`,
  which creates `00-brief.md`. `/import-project` calls
  `scripts/forge-clone.py`. `/spinoff` creates files only. None of
  them touches git beyond the clone. `/new-project` validates the
  slug.
  Realises: POS.0110, POS.0610, POS.0940, POS.0960, POS.1060.
  Choice: no real alternative recorded. Where:
  `.claude/skills/new-project/SKILL.md`,
  `.claude/skills/import-project/SKILL.md`,
  `.claude/skills/spinoff/SKILL.md`, `scripts/forge-clone.py`,
  `templates/`.
- **SOL.0170 A new kind of artefact.** `/new-artefact <name>` is a
  skill written in the seven blocks of a definition and guarded like
  every command that writes (SOL.0110). It makes no file by a
  script. The pair starts from the skeleton
  `templates/artefact-definition.md` for the definition; a template
  has no skeleton, each differing whole. Beside the pair it touches
  the forge intent and this design through their own definitions,
  the row of a new prefix in `CLAUDE.md`, ID scheme, the calibration
  of the critic's contract and, where one is decided, a persona file
  from `templates/challenger-definition.md`. The rosters need
  nothing: `/forge`, `/man` and the README read the definitions from
  disk.
  Realises: POS.1430, POS.0700. Choice: a command of its own against
  a state of `/forge`, which works an artefact of one project while
  this changes the engine; the cost is one more command and one more
  row of the Commands table. A skeleton of the definition against
  the definitions on disk as the only models: a skeleton carries no
  content to copy; the cost is one more file to change with
  POS.1310. Where: `.claude/skills/new-artefact/SKILL.md`,
  `templates/artefact-definition.md`.

### The documents of a project
- **SOL.0200 The history log.** A record is written as a list item,
  in the shape `templates/history.md` owns; its author is the third
  field. A line
  names several IDs only where the whole line holds for each of
  them, every ID in full and never a range; a line with `Was` names
  one. In `Was` the line breaks of the wrapping become spaces and
  paragraphs are divided by `<br>`. The document's front-matter
  carries version, date, status and a machine-written `last_change:`
  line, derived from the records of the newest version by the same
  write step that appends them, never by hand, so the two cannot
  drift. The way there, for a companion written before the log: its
  table stays untouched, the file moves as it stands to
  `<file>.history.archive.md`, immutable from that moment, and the
  log begins in a new `<file>.history.md` with the next version of
  the document. Nothing is converted: the rows are a record and stay
  in the words they were written in. The history of an item is a
  search of both files. A Version History table, in the body of a
  document or in its companion, is a `/check` finding settled by
  that move; that is how a project migrates (POS.0820), on the
  principal's word, project by project.
  Realises: POS.0310, POS.0120, POS.0820. Choice: a log beside the
  document against a table in its body; the research behind it is
  `projects/forge/research/2026-09-29-change-history-of-document-items.md`
  and `2026-09-29-change-record-file-format.md`. `last_change` is
  called machine-written and is written by the model; whether a
  script takes the write over is open, THR.0530. Where:
  `templates/history.md`, `.claude/agents/check-light.md`,
  `.claude/agents/check-history.md`.
- **SOL.0210 The ledger.** One Markdown file per project,
  `ledger.md`, freely rewritten, its tables owned by
  `templates/ledger.md`. Its YAML header carries the kind of the
  project and its language. The Briefs table carries one row per
  brief with its mining state; `/forge`, `/forge intent` and `/check`
  use it as their definitions say. The Dependencies table carries
  what the project relies on outside its repository; the `/forge`
  map shows them, the README carries a line of them and `/ingest`
  registers them. The check `project` verifies that the ledger cites and does not copy.
  `/new-project`, the `/forge` map and `/check` treat each kind of
  project as their definitions say.
  Realises: POS.0160, POS.0920, POS.0960, POS.1020, POS.0330,
  POS.0440. Choice: Markdown tables; what they were chosen against
  and why is not recorded in the intent. The research of 2026-10-04
  names the price, tables are a weak store for a script (THR.0530).
  Where: `templates/ledger.md`, `templates/recipe-readme.md`,
  `.claude/skills/ingest/SKILL.md`,
  `.claude/skills/ledger/SKILL.md`, `.claude/skills/forge/SKILL.md`,
  `.claude/skills/forge/states/intent.md`,
  `.claude/agents/check-project.md`.
- **SOL.0220 Sources and their conversion.** Bare, `/ingest` sweeps
  `sources/` and tells a changed file by its modification time
  against the ledger date.
  It runs `scripts/doc2md.py` file by file on every binary the
  principal chooses to convert, in bundles as well as for isolated
  files; the output is `sources/<slug>.md`, the source itself.
  Realises: POS.0180, POS.1040. Choice: one script for every
  conversion against ad-hoc parsing by the model. Where:
  `.claude/skills/ingest/SKILL.md`, `scripts/doc2md.py`,
  `templates/ledger.md`.
- **SOL.0230 The resource indexes.** `/ingest` and `/research` write
  the entries of `00-INDEX.md`, `/new-project` scaffolds the indexes
  and the check `light` verifies index against directory.
  Realises: POS.0840. Choice: no real alternative recorded. Where:
  `templates/index.md`, `templates/index-bundle.md`,
  `.claude/skills/ingest/SKILL.md`,
  `.claude/skills/research/SKILL.md`,
  `.claude/skills/new-project/SKILL.md`,
  `.claude/agents/check-light.md`.

### The reviewers
- **SOL.0300 Contracts and agent files.** Each kind of reviewer owns
  one skill `.claude/skills/<kind>-contract/SKILL.md`
  (`critic-contract`, `challenger-contract`, `check-contract`; the
  suffix because `check/` is the command), named in the front-matter
  (`skills:`) of every lens, persona or check file of that kind,
  which then carries its front-matter and its Lens section and
  nothing else; Claude Code injects the whole skill at launch. A
  contract opens by citing `CLAUDE.md`, Isolated reviewers, which is
  the one owner of that division since POS.1070, for what the
  contract owns, what the lens file owns and the overlap rule,
  because the contract lands after the lens's own text and the agent
  must know which yields. The skill is `user-invocable: false`, out
  of the `/` menu, its description staying in the session's context
  (`disable-model-invocation` would also forbid the preload), with a
  description saying it is preloaded. `templates/critic-definition.md`,
  `templates/challenger-definition.md` and
  `templates/check-definition.md` are the skeletons of a lens file. The check `engine` verifies that every
  skill an agent names exists, since a missing one is skipped
  silently. Every agent declares `model: inherit` (SOL.0600). What a
  release offers of the reviewers is `.claude/skills/release/SKILL.md`.
  Regression, the FND sequence, the delta report, what is a finding
  of no lens and the critic's part in testability are the critic's
  contract's.
  Realises: POS.1120, POS.0400, POS.0410, POS.0420, POS.0540,
  POS.0270. Choice: a preloaded skill against a copy of the shared text in
  every agent file. Facts of the mechanism, worked out by Claude:
  the skill arrives at the end of the first user message, after the
  task, not in the system prompt; a headless `--agent` run preloads
  nothing, so reviewers run as subagents only. Decided 2026-09-06.
  Where: `.claude/skills/critic-contract/SKILL.md`,
  `.claude/skills/challenger-contract/SKILL.md`,
  `.claude/skills/check-contract/SKILL.md`,
  `.claude/agents/critic-clarity.md`,
  `.claude/agents/critic-essence.md`,
  `.claude/agents/challenger-cto.md`,
  `.claude/agents/challenger-architect.md`,
  `.claude/skills/critique/SKILL.md`,
  `.claude/skills/challenge/SKILL.md`,
  `.claude/skills/release/SKILL.md`,
  `templates/critic-definition.md`,
  `templates/challenger-definition.md`,
  `templates/check-definition.md`.
- **SOL.0330 The checks.** One contract skill `check-contract`; one
  agent per check, `check-<name>`, front-matter and Lens only, from
  `templates/check-definition.md`; a new check is one file. Composition:
  `/save` runs `light`; `/release` runs `light` and `project`, for
  the engine `engine` too, launched at once; anything else is the
  principal's word. The engine is checked as `/check engine`, the
  forge project as `/check project forge`. The agent stays read-only
  and returns its report; the `/check` procedure files it word for
  word and gives the IDs. What each check verifies is its agent
  file's: the ledger's rules, the kinds and the optional logo in
  `check-project`; front-matter against the companion, the ledger
  against the files, dependencies, indexes and the one form of a
  source in `check-light`; a document against its history in
  `check-history`.
  Realises: POS.1140, POS.0540, POS.0570, POS.1070, POS.1010,
  POS.1020, POS.1040. Choice: the session files the report, and not the agent, so that the IDs are
  given at one place and a check that every save runs has no right
  to write; whether a script takes the filing over is open,
  THR.0500. `context: fork` is set aside: the field fixes the agent
  type in a skill's front-matter, so it cannot serve a dispatcher
  that chooses an agent by argument; the isolation stays what
  `/critique` and `/challenge` do, the Agent tool with the target
  path and nothing else. Where: `.claude/skills/check/SKILL.md`,
  `.claude/skills/check-contract/SKILL.md`,
  `.claude/agents/check-*.md`, `templates/check-definition.md`.

### Rendering and publishing
- **SOL.0400 Recipe and render.** A recipe is one file,
  `recipes/<recipe>.md`. `/render <recipe>` generates the output in
  an isolated subagent into `renders/<recipe>.md`, or the recipe's
  optional `output:` path, history in git. Every render opens with
  YAML front-matter provenance citing the recipe and every input
  with their versions; the ledger's Renders table mirrors it.
  Realises: POS.0710, POS.0930. Choice: visible YAML
  provenance against an invisible comment: provenance is control
  information, the audience rarely meets raw Markdown, and GitLab
  does not display front-matter. Where:
  `.claude/skills/render/SKILL.md`, `templates/recipe.md`.
- **SOL.0410 The engine's README.** Its recipe lives at
  `projects/forge/recipes/readme.md` with `output:` pointing at the
  repository root; the natural inputs are the intent and
  `CLAUDE.md`. The release notes are a render of
  `projects/forge/recipes/release-notes.md` in the same way.
  Realises: POS.0720, POS.0730, POS.1000, POS.0620, POS.0990.
  Choice: no real alternative, Claude's judgement, the intent
  records none: the README is a render like any other. Where:
  `projects/forge/recipes/readme.md`,
  `projects/forge/recipes/release-notes.md`,
  `templates/recipe-readme.md`, `templates/recipe-release-notes.md`.
- **SOL.0420 The two steps of an output.** `/render` makes its
  plain file through pandoc. The two files
  never share a place, or the next render would overwrite the
  designed file with the plain one. The format and what each step
  needs stand in the recipe's `## Format` section, which is never
  copied into the render: the render carries content only, or the
  plain file would carry the instructions as text. The ledger's
  Published table says what each published file was made from and
  its state: `current` set by `/publish`, `stale` by every `/render`
  of that recipe; a date could not tell, since a render may run
  twice a day. `CLAUDE.md` carries the principle of the two steps,
  which command makes which file and who may start each, and the
  conduct of each step is its skill's alone.
  Realises: POS.0590. Choice: two commands divided by cost; what
  they were chosen against is not recorded. Where:
  `.claude/skills/render/SKILL.md`, `.claude/skills/publish/SKILL.md`.
- **SOL.0430 The PowerPoint conversion.** `scripts/md2pptx.py`
  makes a PowerPoint file from a Markdown deck render, by one of two
  engines. `--engine claude`, the default and the engine of
  `/publish`, makes the designed deck through headless Claude Code
  (`claude -p`) with Anthropic's official pptx skill. `/publish`
  names the recipe by path (`--recipe`) so that the model reads the
  Format section there. `--template <path>` names a `.potx` or
  `.pptx` file by path, typically a document of a library project,
  e.g. `projects/lib-<name>/sources/<name>.potx`; without the
  parameter Claude designs the visual style itself. There is no
  default template and no bare-name lookup. The headless run's model
  is chosen by `--model`, default opus; a presentation recipe may
  recommend one in its Format section. `--engine pandoc`, the engine
  of `/render`, makes a plain deck for reading, one slide per
  second-level heading. The generated file is tracked in git like
  any render output; where it lands is the script's help.
  Realises: POS.0590, POS.0710, POS.0970. Choice: a model and not a
  deterministic converter for the designed deck, because deck
  definitions are deliberately free-form and may themselves contain
  instructions for the model: slide content, speaker notes, diagrams
  to redraw as native shapes, visual directions; the cost is an
  expensive conversion, which is why it runs only at `/publish`
  (POS.0590). Present shape 2026-09-27. Where:
  `scripts/md2pptx.py`.
- **SOL.0440 The Word conversion.** `scripts/md2docx.py` makes a
  Word file from a Markdown render, by one of two engines. `--engine
  pandoc`, the default and the engine of `/render`, is a
  deterministic conversion: the plain file needs no model. Styles
  come from a reference document named by path (`--reference`, a
  `.docx` or a Word template `.dotx`/`.dotm`, typically a document
  of a library project); without it pandoc's built-in styles apply,
  no default reference and no bare-name lookup. The page is A4 by
  default. Mermaid diagrams land in the document as blocks of code
  (TBC.0010). `--engine claude`, the engine of `/publish`, makes the
  designed document through headless Claude Code and the official
  docx skill, the reference document as the template it starts from,
  the recipe named by path (`--recipe`), the model chosen by `--model`,
  default opus. The machine carries neither the library the docx
  skill expects nor the tools that show the model its pages
  (LibreOffice, Poppler), and the model is told to install nothing:
  it writes the document's XML directly and designs without seeing
  the result, enough for a page of text, untried for tables,
  pictures or a template. The engine runs under whatever
  configuration directory and login the calling shell has. The
  generated file is tracked in git like any render output; where it
  lands is the script's help.
  Realises: POS.0590, POS.0710, POS.0970. Choice: Word is the target
  and PDF is not: pandoc writes Word without a further engine, and a
  PDF is the recipient's one click from Word. Present shape
  2026-09-27. Where: `scripts/md2docx.py`.
- **SOL.0450 The repository's CONTRIBUTING.** `CONTRIBUTING.md` in
  the repository root is a render of
  `projects/forge/recipes/contributing.md`, made on the principal's
  `/render contributing` and not by a release. GitHub links a file of
  that name from the Contributing tab, the sidebar and the pages
  where an issue or a pull request is created. Three channels are
  named in it: Discussions for feedback and ideas, Issues for a
  defect, the author's contacts on his GitHub profile for what is
  not public. Discussions are switched on in the repository's
  settings by the principal.
  Realises: POS.1440, POS.0710. Choice: a render against a file
  written by hand, so that the rule it tells cannot drift from the
  intent; the cost is that it is current only after a render. The
  root against `.github/`, where GitHub would look first: a visitor
  of the file listing sees it. Three channels against Issues alone:
  a discussion is a smaller step for one who only wants to say
  something; the cost is two places to watch. Where:
  `projects/forge/recipes/contributing.md`, `CONTRIBUTING.md`.
- **SOL.0460 The documentation.** `/document [slug]`
  (`.claude/skills/document/SKILL.md`) runs two agents and three scripts,
  asks nothing. The planner `docs-planner` (session model) reads the
  target on disk and writes the map `docs-map.md` beside the ledger of
  the owning project, kind `map`: one entry per page under its path,
  with title, kind, reader, what the page says, its exact inputs as
  whole files, the pages it links to with a title and a sentence each,
  what it must not say, `made: mirrored | derived` with the evidence for
  a derived page, and the state new / regenerate / keep / remove. The
  writer `docs-writer` makes one page from its entry alone, handed to
  it as a task file in the engine's `tmp/` that it reads first, in the fixed
  page shape of its definition, on a faster model for a mirrored page
  and the session model for a derived one, chosen by the entry's `made`.
  The script `scripts/docs-index.py` derives the index `docs/README.md`
  from the map with the version of the owning project's intent; a run's
  state is computed from the content hashes of each entry's inputs and
  the pages are scanned for broken links, long dashes and instance facts
  before they are kept. Pages, kind `page`, live in `docs/` of the
  engine root or of the project, the map never there. The ledger's
  Renders table carries the index with the map as its input. The pinned
  facts the planner reads as an owner are the section "Pinned facts (not
  rendered)" of the project's readme recipe.
  Realises: POS.1450, POS.1080, POS.0930. Choice: a command of its own
  against `/render`: a page has no recipe to iterate, the map is
  generated. The index named `README.md` against `index.md`: GitHub
  shows a directory's README as its front page. The map beside the
  ledger against `docs/`: a visitor of the documentation would not
  understand it. The pinned facts in the recipe against a file of their
  own: a file would need a kind of its own, and the recipe is read by
  both the README and the planner today; the cost is that a render's
  tool carries facts of the project. Built 2026-10-09 whole: the
  skill, the three scripts and the two agents; the first run of
  `/document` the same day regenerated 83 pages and the index, three
  pages once more after the check named a failure in each. The two
  agents share their conduct through the contract skill
  `docs-contract`, as the reviewers do; the map's shape is the
  skeleton `templates/docs-map.md`. Where:
  `.claude/skills/document/SKILL.md`,
  `.claude/skills/docs-contract/SKILL.md`, `templates/docs-map.md`,
  `.claude/agents/docs-planner.md`,
  `.claude/agents/docs-writer.md`, `scripts/docs-state.py`,
  `scripts/docs-index.py`, `scripts/docs-check.py`,
  `scripts/docs_map.py`, `projects/forge/docs-map.md`, `docs/`.

### Persistence
- **SOL.0500 The repositories.** The engine is one git repository,
  `forge-of-thought`, full name Forge of Thought in documents; its
  public home is `https://github.com/pche-broken-artist/forge-of-thought`,
  the address a clone and a project's README point to. The
  universal core in the root (`CLAUDE.md` for the agent, `README.md`
  for humans, `templates/`, `scripts/`, `.claude/`) together with
  `projects/forge`, the system's own project. The engine is a clone;
  the projects are nested git repositories in a gitignored
  `projects/*` with `projects/forge` re-included (`!projects/forge`;
  the pattern must be `projects/*`, not `projects/`, or the
  re-include fails silently). A per-project `CLAUDE.md` is polish
  only where genuinely needed. How the scripts recognise a project
  is in `scripts/forge_repos.py`, which the git scripts share.
  Realises: POS.0760, POS.0940, POS.0990. Choice: nested
  repositories under a gitignored directory against submodules,
  subtree, worktrees, a template repository and a plugin as the only
  shape (REJ.0150). Decided 2026-08-29. Where: `.gitignore`,
  `projects/`, `LICENSE`, `scripts/forge_repos.py`.
- **SOL.0510 The git scripts.** The scripts that serve the engine
  and every project that is a repository (`projects/<slug>/.git`),
  each described by its own help header: `forge-save.py`,
  `forge-pull.py`, `forge-status.py`, `forge-clone.py`, which
  brings an existing project in, and `forge-branch.py`, which
  creates a branch or switches to one, `main` included, with the
  slug alone reports the branch and lists the branches, and nothing
  else.
  Realises: POS.0550, POS.1060, POS.1110, POS.0940. Choice: scripts
  as the only door against git typed by the model. Where:
  `scripts/forge-*.py`, `scripts/forge_repos.py`.
- **SOL.0520 The wall.** Protection relies on Claude Code's
  permission system, not an OS-level sandbox: commands and file
  operations run under permission prompts and allowlists, shared
  deny rules in `.claude/settings.json` block sensitive paths
  (`~/.ssh`, `~/.aws`) and raw `git`, and web access is approved per
  domain on first use. The file denies Claude the `git` command in
  both shells (`Bash(git *)`, `PowerShell(git *)` under
  `permissions.deny`). In the same file `attribution.commit` is
  empty and `attribution.sessionUrl` is false, so Claude Code adds
  and proposes no `Co-Authored-By` or `Claude-Session` trailer.
  Realises: POS.0550, POS.1200, POS.1090. Choice: the permission
  system against an OS-level sandbox, which was tried on 2026-08-04
  and deliberately dropped: it is unavailable on Windows, where
  enforcing it meant no shell at all. Where:
  `.claude/settings.json`.
- **SOL.0530 Save and release.** `/release` runs its checks
  (SOL.0330), settles their findings, renders the README and
  the release notes unconditionally, with no staleness test, and
  ends by running `/save` with the release message and tag: not a
  second procedure. The renders come after the check and its
  walkthrough, not before: a render made from the settled sources is
  current by construction, whereas one made before it goes stale
  whenever a finding bumps the intent. The script pushes a tag with the commit and
  keeps it without an origin. `forge-save` checks that git resolves
  an identity for the repository and, where it resolves none,
  reports it with the command to set one and commits nothing until
  it is.
  Realises: POS.1100, POS.0570, POS.0730, POS.0810, POS.1070.
  Choice: two commands against one, alternatives REJ.0160 and
  REJ.0170; the cost is a README stale between releases, visibly.
  Where: `.claude/skills/save/SKILL.md`,
  `.claude/skills/release/SKILL.md`, `scripts/forge-save.py`.
- **SOL.0550 The commit identity.** No roster file and no local
  `git config user.*` at a project's creation or import. The
  identity is resolved per git host by the user's own `includeIf`
  stanzas, which `/setup` offers to write
  (SOL.0150), with the one global guard `user.useConfigOnly = true`
  and no global `user.name`/`user.email`; a surviving global
  identity defeats the guard, and `/setup` says so. Where one host
  serves two roles the user sets a local `git config user.*` of his
  own, which git lets win over the include.
  Realises: POS.0950, POS.1050. Choice: git's per-host includes
  against an identity kept by the forge; the cost is the two-roles
  case POS.0950 accepts. Reversed 2026-09-16: the identity had been
  a property of the project, set locally in every repository and
  proposed by the command layer from a roster in
  `identities.local.md`, and the per-host include had been rejected
  because a host is only a correlate of the identity and fails where
  one host serves two roles. Where: `.claude/skills/setup/SKILL.md`;
  outside the engine, the user's global git configuration file,
  named by `scripts/forge-status.py`.

## Across the parts
- **SOL.0600 One model.** The reviewer agents declare `model:
  inherit` explicitly. The session model is chosen in
  `.claude/settings.local.json`, gitignored, which `/setup` creates.
  A command's `effort:` remains the lever for routine turns should
  one ever need it. The headless conversions behind `/publish`,
  `scripts/md2pptx.py` and `scripts/md2docx.py` with `--engine
  claude`, carry the default of their own in `--model`. The model a
  recipe may recommend in its Format section is the headless
  conversion's.
  Realises: POS.0930, POS.0530, POS.1050. Choice: an explicit
  `inherit` against per-agent pins, which age. Where:
  `.claude/agents/`, `.claude/settings.local.json`.
- **SOL.0610 One owner for every shape.** Where a shape had no owner
  it has a skeleton: the bundle catalogue
  (`templates/index-bundle.md`), the library reduction of the ledger
  (`templates/ledger.md`'s header), the state vocabularies of
  findings and challenges and the reading of an older state word
  (`templates/ledger.md`'s Findings and Challenges comments), the
  reading of an older recipe's `## Build instructions` as Format
  (`templates/recipe.md`'s Format comment).
  Realises: POS.1070. Choice: a skeleton against a second
  description. Where: `templates/`,
  `.claude/agents/check-single-source-of-truth.md`.
- **SOL.0620 The scripts and their platform.** The scripts are Python
  3.8 or newer, run as `python scripts/<name>.py`, and use nothing
  Windows-only: paths through `pathlib`, processes through `subprocess`
  with argument lists and never a shell, external tools (`git`,
  `markitdown`, `pandoc`, `claude`) resolved from PATH, colour only on a
  terminal, usage examples in the help free of Windows-specific paths.
  Each script carries its help in its module docstring (synopsis, what
  it does, what it needs, examples). What several scripts share lives in
  one module beside them, imported by path: `forge_repos.py` (the engine
  root, the git check, the list of repositories a bare or a slug form
  visits, running git) for the five git scripts, `forge_tools.py` (a
  tool on PATH, resolving paths, the headless Claude Code run) for the
  three conversions, `docs_map.py` (the reader of the documentation map)
  for the three documentation scripts. The per-prompt hook is a Python
  script too, started by `python` from `.claude/settings.json`.
  Rewritten from PowerShell 7 on 2026-10-09, all nine at once, and
  tested that day against a fixture: a local bare remote, an engine
  cloned from it, a project with a remote and one without, 56 cases over
  every script and its refusals; the `claude` engine of the conversions
  was not run.
  Realises: POS.0830. Choice: Python against PowerShell 7, the
  principal's decision of 2026-10-02 on the feedback of the forge's
  users; `python` as the one command name against `python3`, since
  Windows has only the first and a Unix system gives it by an alias or a
  package, and the hook can name one. Options in the Python spelling
  (`--tag`, `--engine`, `--recipe`, `--reference`, `--template`,
  `--page-size`, `-o`) against the PowerShell ones, since argparse is
  the convention of the language. Portability is not verified: the set
  has not been run on Linux. Where: `scripts/`.

## Open
- **TBC.0010** (owner: principal) Mermaid diagrams in a Word file:
  rendering them to pictures needs `mermaid-cli`, a further
  dependency not decided on (THR.0370; Waiting on principal in the
  ledger). Closed by: the principal's
  decision on the dependency. Blocks realisation: no.
- **TBC.0020** (owner: principal) Which check keeps this design true
  against what realises it; POS.1420 wants one and none exists
  (THR.0520, Open). Closed by: a decision in THR.0520. Blocks
  realisation: no.
- **TBC.0030** (owner: principal) The independent challengers of
  POS.0800 are not built and have no part here. Closed by: their
  design when the principal takes them up. Blocks realisation: no.
