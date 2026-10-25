---
version: 0.48
status: draft
project: forge
audience: whoever realises the solution, a person or an agent
---

# Forge of Thought — Solution design

A proposal, handed over to Claude. The items of 0.1 are a one-off move
(THR.0520, step 4): they stand here as the solution stood in the intent
at 4.55, no choice in them is new, and what they say of a file, a
research note or an open thread beyond the intent was read from that
file by Claude on 2026-10-04. Every item added since carries a date of
its own and names its choices. Every choice below is one the intent
recorded, save where an item says the judgement is Claude's. Where the
intent and its history give no reason for a choice, the item says the
reason is not recorded, and none is invented; where a `Choice` names no
cost, the intent records none. The principal has not judged the design
whole; SOL.0170 he judged on 2026-10-04 (THR.0520, step 5).

This design is the architecture of the forge. The forge cannot yet be
built from its artefacts alone, as POS.1400 asks: the detail of every
part is in the file that realises it, named in `Where`, and the forge
has no technical specification. Whoever rebuilds the forge today needs
the intent, this design and the files of the engine together. A clause
of an older item that cites an item marked "Not built" is not built
either and is built with it: the mark stands once, on the item that owns
the part, and the release's walkthrough turns it over (SOL.0530).

## How the parts work together

The forge is not a program. It is a set of instructions that Claude Code
reads, with deterministic work kept at its edge in scripts. Five ideas
carry it.

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
scripts are the door to a write of git; reading git is open, and the
hook holds the line between the two, putting the few commands that
finish the step of a conflict to the principal (SOL.0520, SOL.0840).

Every file has a way of merging and the forge tells git which
(SOL.0730): composed text and the record files merge as text, a
conflict in a record file two tails kept both; derived state is made
at read time and never kept in git, or made only on main and taken as
ours at a merge; immutable files never conflict. Where git leaves a
conflict, Claude lays both sides out and the principal decides
(SOL.0840); the forge still merges nothing itself.

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
check `light`, unless `--quick`, and commits and pushes through `forge-save`; `/release`
runs its checks, settles them, regenerates the README and the release
notes and then saves with the release message and tag. The release writes the state render
(SOL.0530).

Deliberately not designed here: the wording and the steps of each
command, definition, contract, template and script, which are that
file's; how an artefact is found, which is its definition's; anything
beyond the files the forge makes. No part answers POS.0600, POS.0780, POS.0980, POS.1380 and POS.1780: they state a name, a direction, a
boundary kept by hand or an order of work.

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
  POS.1030, POS.1160, POS.1210, POS.1370, POS.1410, POS.1460,
  POS.1470, POS.1480. Choice: no real
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
  `.claude/settings.json` carries one such hook. It prints two lines on
  the walkthrough, the one-item rule itself, since 2026-09-27 with the
  verdict line that closes a proposition, and a pointer to
  `.claude/skills/walkthrough/SKILL.md` for the full shape when a
  walkthrough or an interview runs, and four lines of conduct, the
  principal's rules, worded in `scripts/hook-walkthrough.py`. The hook's
  command is anchored at the project root: `.claude/settings.json`
  invokes it in exec form, `python` with
  `${CLAUDE_PROJECT_DIR}/scripts/hook-walkthrough.py` as its one
  argument. A relative path is resolved against the session's working
  directory, not the engine root; the placeholder always names the root
  the session started in, and the exec form hands the path to the
  program without a shell. Realises: POS.1170, POS.0850. Choice: a hook
  that repeats the rule against trusting text loaded once; the cost is
  that a hook is context and not enforcement. The gate that would
  enforce the lines of conduct is open, THR.0400, its git half built
  (SOL.0520). Where: `.claude/settings.json`,
  `scripts/hook-walkthrough.py`.
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
  dispatcher plus one definition file per target state, each declaring
  its own inputs: a future layer is added by one file and the dispatcher
  stays untouched. Bare, the dispatcher reports the state map of a
  project, the staleness of renders among it; the map ends with the
  state against the origin (SOL.0780) and refuses a project of the shape
  before the migration (SOL.0800). The Terms section is in
  `templates/assignment.md`. When an artefact is complete is the Aim of
  its definition. When a challenge of the intent and of the solution
  design is offered is its definition's, under Instruments; the
  definitions of the brief and of the assignment name none. Realises:
  POS.0580, POS.1300, POS.1310, POS.1320, POS.1330, POS.1340, POS.1350,
  POS.1360, POS.1390, POS.1400, POS.1420, POS.0100, POS.0130, POS.0140,
  POS.0210, POS.0240, POS.0250, POS.0260, POS.0280, POS.0290, POS.0450.
  Choice: a dispatcher with state files against one command per verb;
  what else it was chosen against is not recorded. Whether `/forge` and
  `/recipe` are one dispatcher or two is open, THR.0460. Where:
  `.claude/skills/forge/SKILL.md`,
  `.claude/skills/forge/states/brief.md`,
  `.claude/skills/forge/states/intent.md`,
  `.claude/skills/forge/states/assignment.md`,
  `.claude/skills/forge/states/brd.md`,
  `.claude/skills/forge/states/solution-design.md`,
  `templates/brief.md`, `templates/intent.md`, `templates/thread.md`,
  `templates/assignment.md`, `templates/brd.md`,
  `templates/solution-design.md`.
- **SOL.0130 The `/recipe` dispatcher and the genres.** The same shape
  as SOL.0120: a thin dispatcher plus one definition file per genre, the
  genre's skeleton in `templates/recipe-<genre>.md`. The genre
  `presentation` has its interview in
  `.claude/skills/recipe/genres/presentation.md` and its render is
  turned into a PowerPoint file by SOL.0430. The genres today are
  `presentation`, `readme`, `release-notes` and `screenplay` (POS.1530),
  each invoked as `/recipe <genre>`. The genre `screenplay` has its
  interview in `.claude/skills/recipe/genres/screenplay.md` and its
  skeleton in `templates/recipe-screenplay.md`; its checklist asks,
  beyond the presentation's audience, purpose, inputs, dramaturgy,
  vocabulary and what must not appear: the sessions and the beats pinned
  by their times, what the viewer leaves with, what is shown in full,
  the rules of the quotes, the languages and the pace, the format
  (`video` or `html-player`) and, for `html-player`, whether the file
  goes out to the engine's `docs/videos/` by `output:` (POS.1540).
  Realises: POS.0770, POS.1000, POS.1530. Choice: no real alternative
  once SOL.0120 stood, Claude's judgement, the intent records none.
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
- **SOL.0150 The first run.** `/setup` fills `CLAUDE.local.md` from its
  template and creates `.claude/settings.local.json` with the session
  model. It closes with the git identity: it asks for the hosts the user
  pushes to and a name and an e-mail for each, and offers to write them
  through `scripts/forge-config.py`: per host `--identity`, the two
  `includeIf` stanzas written by `git config --global` into the file git
  reads, each with `path = .gitconfig-<host>` relative to that file, the
  identity file beside it created with its `[user]` when missing; then
  `--guard`, the global `user.useConfigOnly = true`. An existing key is
  reported and left; a stanza or an identity file that differs is
  reported, and `--replace` offered apart. Where a global `user.name` or
  `user.email` survives, `/setup` says the guard only bites once it is
  removed and offers `--guard --unset-identity`, again only on the
  user's word. Declined, the commands are printed for the user to run by
  hand. The user's global git configuration is the one thing `/setup`
  changes outside the engine, and only through the script. It also
  registers the merge driver `ours` and the git settings it needs through the
  same script (SOL.0740), and writes `author: <handle>` into `CLAUDE.local.md`, the
  author of every record he decides (templates/history.md). On an
  instance made before the `Author` line existed `/setup` offers the
  lines the template has and the file lacks, written on the user's word,
  never touching what is there. Realises: POS.1050, POS.0950. Choice:
  through `git config --global` against a path named by the forge, which
  moves with HOME on a domain machine; against `GIT_CONFIG_GLOBAL` set by
  `/setup` (a change to the user's system) and the registration per
  repository (it reverses SOL.0740) (THR.0720). The registration and
  `author:` built 2026-10-18, the preparation of the cutover plan
  (R1.14); the script built 2026-10-20, the skill brought to it
  2026-10-23 (FND.2260). Where: `.claude/skills/setup/SKILL.md`,
  `scripts/forge-config.py`, `templates/CLAUDE.local.md`,
  `.claude/settings.local.json`, `scripts/forge-status.py`.
- **SOL.0160 A project is born or brought in.** `/new-project` scaffolds
  a project by its kind from `templates/`, asks for the founding brief
  and hands it to the procedure of `/forge brief`, which creates
  `00-brief.md`. `/import-project` calls `scripts/forge-clone.py`, which
  clones into `projects/<repository name>`; a nonconforming name is
  fixed by renaming the directory afterwards. `/spinoff` creates files
  only. None of them touches git beyond the clone. `/new-project`
  validates the slug, and creates the project file, `.gitattributes` and
  `threads/` (SOL.0670, SOL.0730, SOL.0720); `forge-clone` reads the
  project file for the kind and the language. Realises: POS.0110,
  POS.0610, POS.0940, POS.0960, POS.1060. Choice: no real alternative
  recorded. Where: `.claude/skills/new-project/SKILL.md`,
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
- **SOL.0180 Pull and end.** `/pull [slug]` is a skill guarded like
  every command that changes the disk (SOL.0110). It asks `forge-status
  --remote` for the state of its scope against the origin, says it in
  the words of POS.1490 and stops at the offer where a repository has
  unsaved changes or has diverged, at diverged naming the path: `/save`,
  whose rebase leaves a conflict standing for the step of a conflict
  (SOL.0840), or a branch where the work is to stay apart (the roles:
  POS.1690); clean and behind, it runs `forge-pull` (bare: the engine
  and every project with an origin; `forge`: the engine; a slug: that
  project). After a pull of the engine it reads the commit subjects the
  script printed, opens in `RELEASE-NOTES.md` the sections of the
  releases crossed and shows their Action required lines, then offers
  `/check light` and `/check project` on each project, and after a
  release that changes the shape of files says in Action required
  `/migrate <slug>` (SOL.0800); after a pull of a project it reports.
  `/end` is a skill Claude may start, a report (SOL.0110): it names what
  lives only in the conversation and offers the write, runs
  `forge-status` without the remote and offers `/save` where a
  repository has changes, names stale renders by the ledger's Renders
  table as a fact, and closes with one sentence on whether shutting the
  command line loses anything; it writes nothing. Realises: POS.1490,
  POS.1500, POS.0940, POS.1090. Choice: two small commands against
  widening `/save` and `/forge`: a pull runs the other way from a save,
  and the end of a session is another moment than the map; the cost is
  two rows of the Commands table. Decided 2026-10-11. Where:
  `.claude/skills/pull/SKILL.md`, `.claude/skills/end/SKILL.md`,
  `.claude/skills/forge/SKILL.md`.

- **SOL.0630 The history of an item.** `/history <ID> [slug]`
  (`.claude/skills/history/SKILL.md`) is a skill Claude may start, a
  report (SOL.0110): it runs `scripts/forge-history.py <ID> <slug>` and
  prints what the script printed, then adds at most three sentences of
  its own, marked as such: what the item says today, how it moved, what
  hangs on it. The script, read-only, gathers from `projects/<slug>` the
  item's wording today (the reader of a part shared with the
  documentation scripts, `docs_map.part_text`), the records of every
  history log whose subject names the ID, oldest first, the records of
  other items that mention it in their reason, Action or Was, the rows
  of the archives that mention it, and every other citation in the
  project as file and line; the pages, the map, the renders and the
  resources are left out as outputs and inputs. It accepts a short form
  of the ID (`pos580`), prints one timeline of archive rows, records and
  mentions with version and date, wrapped, a Was shortened to its first
  sentence unless `--full` is given. It reads IDs of four or five digits
  with a numeric sort (CLAUDE.md, ID scheme). Realises: POS.1510,
  POS.0310, POS.1090. Choice: a script with a thin skill against a skill
  alone: the gathering is deterministic and was done by hand before,
  differently every time; the cost is one more script. Decided
  2026-10-11. Where: `.claude/skills/history/SKILL.md`, `scripts/forge-
  history.py`, `scripts/docs_map.py`.

### The documents of a project
- **SOL.0200 The history log.** A record is written as a list item, in
  the shape `templates/history.md` owns; its author is the third field.
  A line names several IDs only where the whole line holds for each of
  them, every ID in full and never a range; a line with `Was` names one.
  In `Was` the line breaks of the wrapping become spaces and paragraphs
  are divided by `<br>`. The document's front-matter carries version and
  status; `date` and `last_change` are computed from the records
  (SOL.0700). The way there, for a companion written before the log: its
  table stays untouched, the file moves as it stands to
  `<file>.history.archive.md`, immutable from that moment, and the log
  begins in a new `<file>.history.md` with the next version of the
  document. Nothing is converted: the rows are a record and stay in the
  words they were written in. The history of an item is a search of both
  files. A Version History table, in the body of a document or in its
  companion, is a `/check` finding settled by that move; that is how a
  project migrates (POS.0820), on the principal's word, project by
  project. Realises: POS.0310, POS.0120, POS.0820. Choice: a log beside
  the document against a table in its body; the research behind it is
  `projects/forge/research/2026-09-29-change-history-of-document-items.md`
  and `2026-09-29-change-record-file-format.md`. Where:
  `templates/history.md`, `.claude/agents/check-light.md`,
  `.claude/agents/check-history.md`.
- **SOL.0210 The ledger.** One Markdown file per project, `ledger.md`,
  made at read time by the ledger script and never in git (SOL.0680),
  its tables owned by `templates/ledger.md`. The kind of the project and
  its language are the project file's (SOL.0670). The Briefs table
  carries one row per brief with its mining state, read from the
  intent's history (SOL.0690); `/forge`, `/forge intent` and `/check`
  use it as their definitions say. The Dependencies table carries what
  the project relies on outside its repository; the `/forge` map shows
  them, the README carries a line of them and the ledger script finds
  them as citations (SOL.0690). The check `project` verifies that the
  ledger cites and does not copy. `/new-project`, the `/forge` map and
  `/check` treat each kind of project as their definitions say.
  Realises: POS.0160, POS.0920, POS.0960, POS.1020, POS.0330, POS.0440.
  Choice: Markdown tables; what they were chosen against and why is not
  recorded in the intent. The research of 2026-10-04 names the price,
  tables are a weak store for a script (THR.0530). Where:
  `templates/ledger.md`, `templates/recipe-readme.md`,
  `.claude/skills/ingest/SKILL.md`, `.claude/skills/ledger/SKILL.md`,
  `.claude/skills/forge/SKILL.md`,
  `.claude/skills/forge/states/intent.md`,
  `.claude/agents/check-project.md`.
- **SOL.0220 Sources and their conversion.** Bare, `/ingest` sweeps
  `sources/` and tells a changed file by its modification time against
  the Date of its index entry. It runs `scripts/doc2md.py` file by file
  on every binary the principal chooses to convert, in bundles as well
  as for isolated files; the output is `sources/<slug>.md`, the source
  itself. Realises: POS.0180, POS.1040. Choice: one script for every
  conversion against ad-hoc parsing by the model. Where:
  `.claude/skills/ingest/SKILL.md`, `scripts/doc2md.py`,
  `templates/ledger.md`.
- **SOL.0230 The resource indexes.** `/ingest` and `/research` write the
  entries of `00-INDEX.md`, `/ingest` asking what a source is for before
  the entry is written, an entry carrying the source's date, origin and
  form (SOL.0690); `/new-project` scaffolds the indexes and the check
  `light` verifies index against directory. A bundle's `00-INDEX.md` is
  created by `/ingest` at registration when the bundle lacks one, and a
  supplied one is validated against the contents, origin dates best
  effort, never asked for; a growing bundle (POS.0180) takes a new file
  through `/ingest <file> [slug] --bundle <name>`: the bundle born as
  growing at its first file, its `00-INDEX.md` from the skeleton with
  the paragraph saying it grows, the file stored inside, its entry
  written in the bundle's index after the question of its role, the top
  entry's What kept true, the flag refused where the bundle arrived
  whole; in sweep mode a file inside a bundle without an entry is
  offered for registration there, never reported as a breach, and a new
  subdirectory is asked whether it grows at the question of its role.
  Realises: POS.0840. Choice: no real alternative recorded. Where:
  `templates/index.md`, `templates/index-bundle.md`,
  `.claude/skills/ingest/SKILL.md`, `.claude/skills/research/SKILL.md`,
  `.claude/skills/new-project/SKILL.md`,
  `.claude/agents/check-light.md`.
- **SOL.0640 The work product.** `/work <name> [slug]`
  (`.claude/skills/work/SKILL.md`) is the one door to a work product:
  bare, it lists the project's work products from the ledger; with a
  name, it works the specification `work/<name>.spec.md` with the
  principal, by elicitation or handed over, and makes the file
  `work/<name>.<ext>` from it in the same round on his word. The first
  specification is created from `templates/work.md` as v0.1, with its
  companion `work/<name>.spec.history.md` from `templates/history.md`
  and its row in the Work table, made by the ledger script from its
  first record; the specification's `## Making` section says how the
  file is made from it, and nothing of it is copied into the file. The
  Work table, made by the ledger script from the records of the
  specification's history (SOL.0680, SOL.0690), carries one row per work
  product: the file, the specification with its version, the inputs with
  their versions, when the file was made and its state: `current`, the
  making's record; `stale`, a write of the specification not followed by
  a making; `by hand`, a `changed` record `state: by hand` on the
  principal's word when he has worked the file and does not want it
  remade. `CLAUDE.md` carries the kind in the Document kinds table,
  `work/` in the layout and the command in the Commands table; the check
  `light` verifies the Work table against the directory as it does the
  other tables. Realises: POS.1520. Choice: one command for the
  specification and the file against two, as `/recipe` and `/render`
  are: the making is a step of the round and the specification is
  iterated with the principal, so a second command would only separate
  what one conversation does; the price is a skill that does two things.
  Where: `.claude/skills/work/SKILL.md`, `templates/work.md`,
  `templates/ledger.md`, `CLAUDE.md`, `.claude/agents/check-light.md`.
- **SOL.0670 The project file.** `project.md` in the project's root,
  header `project`, `kind`, `language`, written once at the creation
  from `templates/project.md` and never by a round; read in place of the
  ledger's header by `forge-clone`, `/import-project`, `/new-project`,
  `/forge`, `/recipe`, the ledger script and prime directive 6 of
  CLAUDE.md. Realises: POS.1590, POS.0060, POS.0960. Choice: a file of
  its own against the header of the ledger, which leaves git (SOL.0680);
  no other home was found. Built 2026-10-19 in the first release (the
  cutover plan, R1.03, R1.10). Where: `templates/project.md`,
  `CLAUDE.md` (prime directive 6, Repository layout),
  `scripts/forge-clone.py`, `.claude/skills/new-project/SKILL.md`,
  `.claude/skills/import-project/SKILL.md`,
  `.claude/skills/forge/SKILL.md`, `.claude/skills/recipe/SKILL.md`. A
  fixture project carries `fixture: true` (SOL.0830).
- **SOL.0680 The ledger made at read time.** `scripts/forge-ledger.py
  <slug>` builds `ledger.md` from the documents and writes it gitignored
  (`projects/<slug>/.gitignore`, for the engine `.gitignore` with
  `projects/forge/ledger.md`); the tables stay `templates/ledger.md`'s
  shape. It reads eleven kinds: the project file, the artefacts'
  headers, the histories, the decisions, the resource indexes, the
  reviews and the challenges, the provenance of the recipes and the
  renders, the published companions, the work specifications, the
  threads and `ledger.archive.md`, the archive read for every item
  without a record of the new shape, a newer record overriding. Waiting
  on principal by the rule of POS.1620, a thread's line its first
  sentence and its last dated paragraph. It reports a duplicate ID, a
  closed thread touched by a later commit
  (through `forge_repos`), and a THR cited in any file of the project
  with neither a thread file nor a `closed` record (POS.1640). An
  unparsable file is a finding, not a crash: the row drops aloud, the
  ledger's header carries a line "unparsed: <file>:<line>", the exit is
  zero and `check-light` reports it; the shape one release back is
  tolerated, which for the first release means: over a project of the
  old shape the Findings and Challenges tables, the mining and the work
  states are read from the hand-kept ledger's own tables as the archive.
  The script writes `ledger.md` only on a project of the current shape
  (the project file exists, templates/project.md) whose ledger is out of
  the index where the project is a repository of its own (the mark of
  SOL.0800, met by itself outside git); on a project of the old shape,
  under git or not, it says "shape before the migration, run `/migrate`"
  and does not write, since there `ledger.md` is the hand-kept ledger,
  the archive `/migrate` freezes (POS.1740); where its own repository
  tracks the ledger it refuses the same way, and a repository that is
  not the forge's is asked nothing (POS.0550); either refusal prints to
  stdout or to `--out <path>`, the dry run of a real project going to
  `tmp/` (CHL.0560). Over an old shape with no threads file, Waiting
  says the threads were not read rather than that nothing waits. Called
  by the `/forge` map, `/ledger`, `/end`, `check-light` and `check-
  project`; the readme recipe of a project reads the script's output
  where it read the ledger; the 26 skills that write a ledger row today
  stop. CLAUDE.md, Ledger, ceases to say "freely rewritten, keep it
  current after every operation". Realises: POS.1600, POS.1610,
  POS.1620, POS.1630, POS.1640, POS.0160, POS.0330. Choice: a script
  against the model keeping the file, since the ledger is derived and
  every operation rewrote it; the price is the most complex script of
  the engine, reading dozens of reports at every map, under a second but
  known. Built 2026-10-19 in the first release (the cutover plan, R1.09,
  R1.16). Where: `scripts/forge-ledger.py`, `templates/ledger.md`,
  `templates/recipe-readme.md`, `CLAUDE.md` (Ledger, Document kinds),
  `.claude/skills/ledger/SKILL.md`, `.claude/skills/forge/SKILL.md`,
  `.claude/skills/end/SKILL.md`, `.claude/agents/check-light.md`,
  `.claude/agents/check-project.md`, `.gitignore`.
- **SOL.0690 Where the state lives.** The records that replace the
  ledger's columns: the mining of a brief as a record in the intent's
  history with the brief's file as subject (`00-brief-<name>.md |
  changed | mined: <state>, <note>`), written by the intent's
  definition; the `closed` record of a finding or a challenge in the
  history of the artefact whose version settled it, or of the intent,
  written by the walkthrough's write and named by the three contracts; a
  verdict of the principal on a finding or a challenge in a fixed field
  of its decision, `- **Verdict:** <ID> rejected | parked until <what> |
  obsolete`, one line per ID and as many lines as a decision rules on, a
  partial verdict read as the verdict on the whole ID with the rest in a
  `changed` record of the history, which the script parses; a work
  product's state as records in its specification's history; a published
  file's provenance as `published/<recipe>.md`, written by `/publish`; a
  source's date, origin and form as fields of its index entry; a state
  record carrying the version without raising it. Realises: POS.1610,
  POS.1630. Choice: records in the existing histories and a field in the
  decisions against new kinds of record or a file per item: fewer
  conventions, the same information. Built 2026-10-19 in the first release (the cutover plan, R1.05, R1.17).
  Where: `templates/history.md`, `templates/index.md`,
  `templates/decisions.md`, `.claude/skills/forge/states/intent.md`,
  `.claude/skills/walkthrough/SKILL.md`,
  `.claude/skills/critic-contract/SKILL.md`,
  `.claude/skills/challenger-contract/SKILL.md`,
  `.claude/skills/check-contract/SKILL.md`,
  `.claude/skills/work/SKILL.md`, `.claude/skills/publish/SKILL.md`.
- **SOL.0700 The header without changing fields.** `date` and
  `last_change` leave the artefacts' and the work specifications'
  headers, `updated` and `last_change` the recipes', `updated` the
  indexes', `generated` and `previous` the map's; the templates lose the
  lines, the write step of every artefact stops writing them,
  `forge-history` and the ledger script compute the date and the last
  change from the records, the readme recipe reads them from the script,
  and the documentation run takes the previous map from git through
  `forge_repos` (`git show`). CLAUDE.md, Versioning & status, names the
  fields that stay. Realises: POS.1570. Choice: no real alternative once
  the fields are the certain conflict. Built 2026-10-19 in the first release (the cutover plan, R1.04, R1.11).
  Where: `CLAUDE.md` (Versioning & status), `templates/intent.md`,
  `templates/brief.md`, `templates/assignment.md`,
  `templates/solution-design.md`, `templates/recipe.md` and the genre
  skeletons, `templates/index.md`, `templates/index-bundle.md`,
  `templates/work.md`, `templates/docs-map.md`,
  `.claude/skills/forge/states/*.md`, `scripts/forge-history.py`,
  `scripts/docs_map.py`, `scripts/docs-state.py`,
  `templates/recipe-readme.md`.

- **SOL.0720 Threads as files.** `threads/THR.NNNN.md` from
  `templates/thread.md` (`id`, `concerns`, `origin`, `status`);
  `templates/threads.md` is dropped; the intent's definition creates and
  closes threads as files, the walkthrough's write and `/end`, which
  saves an unfinished conversation into its thread, with it; the ledger
  script makes the list; they merge as text and a thread is never in a
  record file (way 1); a closed thread is immutable and the ledger
  script reports a later touch. The THR row of CLAUDE.md, ID scheme,
  names the directory. Realises: POS.1680, POS.0120, POS.0310. Choice: a
  file per thread against one file with blocks, so that no merge handles
  a block with an inner state; the cost is a directory of many small
  files. Built 2026-10-19 in the first release (the cutover plan, R1.06,
  R1.17, R1.23, R1.29). Where: `templates/thread.md`, `CLAUDE.md` (ID
  scheme, Repository layout), `.claude/skills/forge/states/intent.md`,
  `.claude/skills/walkthrough/SKILL.md`, `.claude/skills/end/SKILL.md`,
  `scripts/forge-ledger.py`, `scripts/forge-migrate.py`.

- **SOL.0850 The BRD.** The pair `states/brd.md` and
  `templates/brd.md` in the shape of SOL.0120, one more definition the
  dispatcher reads from disk; the persona
  `challenger-business-analyst` as SOL.0300 has a persona, reading the
  resource indexes first; the check `check-brd` as SOL.0330 has a
  check, verifying the mechanics of a BRD and, in a BRD from a source,
  that every rule cites the principal's side; a BRD from a file put in
  is a work product of SOL.0640, never `30-brd.md`; the resource
  indexes of SOL.0230 are an input of every BRD. The ledger reads a
  TBC of the principal in the BRD's shape (SOL.0210). Built
  2026-10-23 from the brief `brd` before the positions (POS.1780),
  tried the same day on a vendor transcript into `work/` and on the
  assignment of agentic-platform into its chain, the reviewers run on
  the first. Realises: POS.1800, POS.1810, POS.1820, POS.1830,
  POS.1840, POS.1850, POS.1360, POS.0700. Choice: no critic lens of
  the BRD's own against one, the fork's single critic doing three
  jobs; the cost is that a BRD's quality is read by two lenses that
  know it only through its definition. A persona and a check against
  the lenses alone: the trial showed the persona finding the world
  outside the parent and the check the matrix, which no lens hunts;
  the cost is two more agent files. Where:
  `.claude/skills/forge/states/brd.md`, `templates/brd.md`,
  `.claude/agents/challenger-business-analyst.md`,
  `.claude/agents/check-brd.md`, `scripts/forge-ledger.py`,
  CLAUDE.md (ID scheme, Requirement style).

### The reviewers
- **SOL.0300 Contracts and agent files.** Each kind of reviewer owns one
  skill `.claude/skills/<kind>-contract/SKILL.md` (`critic-contract`,
  `challenger-contract`, `check-contract`; the suffix because `check/`
  is the command), named in the front-matter (`skills:`) of every lens,
  persona or check file of that kind, which then carries its front-
  matter and its Lens section and nothing else; Claude Code injects the
  whole skill at launch. A contract opens by citing `CLAUDE.md`,
  Isolated reviewers, which is the one owner of that division since
  POS.1070, for what the contract owns, what the lens file owns and the
  overlap rule, because the contract lands after the lens's own text and
  the agent must know which yields. The skill is `user-invocable:
  false`, out of the `/` menu, its description staying in the session's
  context (`disable-model-invocation` would also forbid the preload),
  with a description saying it is preloaded. `templates/critic-
  definition.md`, `templates/challenger-definition.md` and
  `templates/check-definition.md` are the skeletons of a lens file. The
  check `engine` verifies that every skill an agent names exists, since
  a missing one is skipped silently. Every agent declares `model:
  inherit` (SOL.0600). What a release offers of the reviewers is
  `.claude/skills/release/SKILL.md`. Regression, the FND sequence, the
  delta report, what is a finding of no lens and the critic's part in
  testability are the critic's contract's. The filing, the IDs and the
  ledger row are the command's, `/critique` and `/challenge` as `/check`
  (POS.1140); the agent returns its report with its findings unnumbered,
  so that reviewers of any kind run in parallel. The three contracts
  name the `closed` record a settled finding or challenge leaves in the
  artefact's history (SOL.0690). Realises: POS.1120, POS.0400, POS.0410,
  POS.0420, POS.0540, POS.0270. Choice: a preloaded skill against a copy
  of the shared text in every agent file. Facts of the mechanism, worked
  out by Claude: the skill arrives at the end of the first user message,
  after the task, not in the system prompt; a headless `--agent` run
  preloads nothing, so reviewers run as subagents only. Decided
  2026-09-06. Where: `.claude/skills/critic-contract/SKILL.md`,
  `.claude/skills/challenger-contract/SKILL.md`, `.claude/skills/check-
  contract/SKILL.md`, `.claude/agents/critic-clarity.md`,
  `.claude/agents/critic-essence.md`, `.claude/agents/challenger-
  cto.md`, `.claude/agents/challenger-architect.md`,
  `.claude/skills/critique/SKILL.md`,
  `.claude/skills/challenge/SKILL.md`,
  `.claude/skills/release/SKILL.md`, `templates/critic-definition.md`,
  `templates/challenger-definition.md`, `templates/check-definition.md`.
- **SOL.0330 The checks.** One contract skill `check-contract`; one
  agent per check, `check-<name>`, front-matter and Lens only, from
  `templates/check-definition.md`; a new check is one file. Composition:
  `/save` runs `light`; `/release` runs `light` and `project`, for the
  engine `engine` too, launched at once; anything else is the
  principal's word. The engine is checked as `/check engine`, the forge
  project as `/check project forge`. The agent stays read-only and
  returns its report; the `/check` procedure files it word for word and
  gives the IDs. What each check verifies is its agent file's: the
  ledger's rules, the kinds and the optional logo in `check-project`;
  front-matter against the companion, what the ledger script reports,
  dependencies, indexes, the one form of a source and a line carrying
  two sentences in `check-light` (SOL.0680); a missing `.gitattributes`
  or project file in `check-project` (SOL.0730, SOL.0670); a document
  against its history in `check-history`. Realises: POS.1140, POS.0540,
  POS.0570, POS.1070, POS.1010, POS.1020, POS.1040. Choice: the session
  files the report, and not the agent, so that the IDs are given at one
  place and a check that every save runs has no right to write, since
  2026-10-17 the rule of every reviewer (POS.1140, SOL.0300); whether a
  script takes the filing over is open, THR.0500. `context: fork` is set
  aside: the field fixes the agent type in a skill's front-matter, so it
  cannot serve a dispatcher that chooses an agent by argument; the
  isolation stays what `/critique` and `/challenge` do, the Agent tool
  with the target path and nothing else. Where:
  `.claude/skills/check/SKILL.md`, `.claude/skills/check-
  contract/SKILL.md`, `.claude/agents/check-*.md`, `templates/check-
  definition.md`.
- **SOL.0810 Unique names of reports.** The filing of `/critique`,
  `/challenge` and `/check` names every report
  `YYYY-MM-DD-<kind>-<name>-HHMM-<4 hex of a content hash>.md`; the
  names given before stay. The command writes the report under its date,
  kind and name into `reviews/` or `challenges/` and
  `scripts/forge-report.py <path>` completes the name in place, the
  local time to the minute and the first four hex characters of the
  SHA-256 of the file's bytes, and prints it; it refuses a name that
  carries the tail already and a target that exists, and touches nothing
  else, no helper directory, no git. Realises: POS.1720. Choice: time
  and hash on every report against a counter or a suffix on the second
  report only, since two branches both make a first report of the day;
  the hash by a script against a one-liner at every filing or a model's
  arithmetic, since what is deterministic is a script's (THR.0530); a
  draft renamed in place against a draft in `tmp/`, which only this
  machine has (the principal's word of 2026-10-18). Built 2026-10-18,
  the preparation of the cutover plan (R1.18). Where:
  `scripts/forge-report.py`, `.claude/skills/critique/SKILL.md`,
  `.claude/skills/challenge/SKILL.md`, `.claude/skills/check/SKILL.md`;
  the shape cited in CLAUDE.md and in the contracts.
- **SOL.0860 The research.** `/research` is the skill
  `.claude/skills/research/SKILL.md`, which owns the course (the
  questions before the plan, the draft, the second engine's review, the
  walkthrough of the plan, the dispatch, the check before filing, the
  synthesis, the index, the report) and the agent's brief, verbatim in
  every packet. The plan and the synthesis have the shape of
  `templates/research-plan.md`, a note that of `templates/research.md`,
  `In short` at its head, Unexpected, Not found, Opened and not used and
  the Search record among its sections. A deep research is a bundle
  `research/YYYY-MM-DD-<topic>/` with `00-plan.md` at its head and one
  note per card per engine, `<card>.<engine>.md`, one entry in
  `research/00-INDEX.md` for the bundle (SOL.0230); a quick research
  stays a single note. A session agent is one `general-purpose` subagent
  per card with web access, its prompt the packet's text and the path of
  its folder; its return is written to `tmp/research/<run>/hold/` and
  moves into the bundle only when the second engine's note of the card
  has returned or the card is closed single-engine. Realises: POS.0050,
  POS.1860, POS.1870, POS.1890, POS.1370, POS.0790. Choice: the plan as
  the unit of consent against the finished note as before, the
  principal's wish; one packet for both engines against a packet per
  engine, so that the answers compare; the hold folder and the order of
  filing against the place of the run, which the probe of 2026-10-24
  showed to lock nothing. Built 2026-10-24 and run once whole (the RFP
  research, twelve notes). Where: `.claude/skills/research/SKILL.md`,
  `templates/research-plan.md`, `templates/research.md`,
  `templates/index.md`.
- **SOL.0870 The engine adapter.** `scripts/forge-engine.py` runs one
  packet on an engine of its table and brings the answer back as a note;
  what it does in full, the version floor, the profile, the fingerprint
  of the folder, the envelope and the flags `--allow-all`, `--sandbox`
  and `--no-profile`, is its header's. The profile is a copy of the
  user's settings file for the engine with `permissions` added: allow
  the web; deny the shell, every write and the reading of every entry of
  the engine root but `tmp/` and of the run's `hold/`, the paths
  computed from where the script lies; the engine started with HOME and
  USERPROFILE pointing at it. Verified 2026-10-24 that a deny rule holds
  under every tool allowed, the shell is refused, the web tools work and
  the login is found. Realises: POS.1880, POS.0800, POS.0790, POS.0950,
  POS.1070. Choice: a CLI against a library and an MCP server
  (REJ.0490), the one-shot shape being shared by four CLIs; a per-run
  profile against the place of the run alone, after the probe showed an
  engine reading CLAUDE.md four levels up without a question; the price
  is one settings shape to know per engine. An engine is a row of the
  table and a pair of functions in `COMMANDS`, one building its command
  and one reading its envelope; the settings path of the profile is
  written for the first engine and moves into its row when a second
  engine comes. Where: `scripts/forge-engine.py`.
- **SOL.0880 The citation check and the measure of independence.**
  `scripts/forge-cite.py` opens every URL of a note or a bundle once
  and classifies it ok, dead, unverifiable or mismatch (an arXiv
  title sharing too few words with the note's entry), writes the
  report to the run folder and exits 1 on anything dead or
  mismatched; `--independence <bundle>` counts, per card with notes
  from more than one engine, the URLs the notes share and the longer
  sentences they have in common, with a verdict, touching no network.
  Nothing is written into a note; what the check finds goes into the
  synthesis. Realises: POS.1890, POS.1870. Choice: resolving the URL
  against a count of agreeing sources (REJ.0460), the one mitigation
  with a measured effect; shared URLs and sentences as the measure of
  independence against trusting the place of the run (the four of six
  of 2026-10-24); a 403 never a failure, since a site that blocks
  bots is the normal case. Built 2026-10-24. Where:
  `scripts/forge-cite.py`.

### Rendering and publishing
- **SOL.0400 Recipe and render.** A recipe is one file,
  `recipes/<recipe>.md`. `/render <recipe>` generates the output in an
  isolated subagent into `renders/<recipe>.md`, or the recipe's optional
  `output:` path, history in git. Every render opens with YAML front-
  matter provenance citing the recipe and every input with their
  versions; the ledger's Renders table mirrors it. The renders of a
  release are made only on main (POS.1690); a project's readme recipe
  reads the ledger script's output where it read the ledger (SOL.0680).
  A recipe may declare `languages:` (POS.1550): the subagent of
  `/render` writes the primary render and then, in the same run, each
  translation as a render of its own, `renders/<recipe>.<lang>.md`,
  scene for scene and line for line, its provenance naming the primary
  render it was made from; one Renders row per file, the format file
  following the name. A recipe without `languages:` renders as before.
  The `output:` path may lie outside the project, in the engine's
  `docs/videos/` (POS.1540); the project's ledger keeps the row, the
  engine none. Realises: POS.0710, POS.0930, POS.1550, POS.1540. Choice:
  visible YAML provenance against an invisible comment: provenance is
  control information, the audience rarely meets raw Markdown, and
  GitLab does not display front-matter. Where:
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
- **SOL.0420 The two steps of an output.** `/render` makes its plain
  file through the script the format names. The two files never share a
  place, or the next render would overwrite the designed file with the
  plain one. The format and what each step needs stand in the recipe's
  `## Format` section, which is never copied into the render: the render
  carries content only, or the plain file would carry the instructions
  as text. A third format, the screenplay's `video` or `html-player`,
  has the plain file only (SOL.0650): `/publish` does nothing with it,
  and the Published table carries no row of it. `/publish` runs on main
  and refuses a repository behind or diverged (POS.1710). The ledger's
  Published table says what each published file was made from and its
  state: `current` set by `/publish`, `stale` by every `/render` of that
  recipe; a date could not tell, since a render may run twice a day.
  `CLAUDE.md` carries the principle of the two steps, which command
  makes which file and who may start each, and the conduct of each step
  is its skill's alone. Realises: POS.0590. Choice: two commands divided
  by cost; what they were chosen against is not recorded. Where:
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
- **SOL.0650 The screenplay conversion.** `scripts/md2video.py` makes
  the format file of a screenplay render by one of two formats, chosen
  by `--format video | html-player`. It reads the render (the
  front-matter for the language, the cards, the scenes with their
  captions and terminal blocks), computes the timeline — typing, the
  stand before Enter, the reveal of an answer, the hold for reading, the
  breath at a scene's end — from the pace given as `--pace
  <principal>,<claude>,<file-report>` words a second, defaults 4, 8, 16,
  and the labels of the captions by language. `video` paints every frame
  with Pillow as a simulated terminal (1280×890, a monospace font for
  the terminal, a sans font for the caption band, with fallbacks where
  the Windows fonts are missing) and pipes them into ffmpeg (H.264, 30
  fps); `html-player` writes the timeline as JSON of events wrapped in a
  script call, `forgeVideo({...})`, in `<name>.html-player.js`, so that
  the page plays it from disk as well as from Pages. The file lands
  beside the render with the render's basename unless `-o` names a
  path; where the path lies under the engine's `docs/videos/`, the
  script writes `docs/videos/index.html` anew from
  `templates/html-player.html` with the folder's files (SOL.0660). What
  it needs — Pillow, ffmpeg on PATH — `forge_tools.py`
  says, as it says for pandoc; the script installs nothing. The pace and
  the look come from the recipe's Format section as arguments; the
  render carries none of it (SOL.0420). Realises: POS.1530, POS.0590,
  POS.0830. Choice: one script with two formats against two scripts: the
  parsing and the pace are one mechanism, and the position says so.
  Pillow and ffmpeg against VHS, asciinema with agg, or a browser driven
  by Playwright: the research of 2026-10-14 (forge-rollout,
  `research/2026-10-14-terminal-video-from-screenplay.md`) found VHS
  broken on Windows, agg ending at GIF and the browser the most code; a
  painter in the language the scripts already are, with one encoder, was
  the least to install and runs on the three platforms. Trial 2026-10-14
  in `tmp/video-trial/`. Where: `scripts/md2video.py`,
  `scripts/forge_tools.py`.
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
  (`.claude/skills/document/SKILL.md`) runs two agents and three
  scripts, asks nothing. The planner `docs-planner` (session model)
  reads the target on disk and writes the map `docs-map.md` beside the
  ledger of the owning project, kind `map`: a Paths section with three
  to five pages per reader in reading order, then one entry per page
  under its path, with title, one line for the index, kind, reader, what
  the page says, its exact inputs as files or as named parts of files (a
  section by its heading, an item by its ID, a block by its bold label),
  the pages it links to with a title and a sentence each, what it must
  not say, `made: mirrored | derived` with the evidence for a derived
  page, and the state new / regenerate / keep / remove. The writer
  `docs-writer` makes one page from its entry alone, handed to it as a
  task file in the engine's `tmp/` that it reads first, in the fixed
  page shape of its definition with one outline per kind of page (a
  how-to, an add page, an artefact page, a concept page, a roster page)
  and the version the page was made for in its front-matter, on a faster
  model for a mirrored page and the session model for a derived one,
  chosen by the entry's `made`. The two agents share their conduct
  through the contract skill `docs-contract`, as the reviewers do, which
  owns beside the isolation the voice and the sentence of a page (one
  voice, one rule per sentence, no image in place of a mechanism, a
  literal copied as its owner has it) and what never reaches a page (a
  real project's content, an unrecorded reason, a date of history, the
  generator speaking of itself). The script `scripts/docs-index.py`
  derives the index `docs/README.md` from the map, the reader paths as
  links and one line per page, with the version of the owning project's
  intent; a run's state is computed by `scripts/docs-state.py` from the
  content hashes of each entry's inputs, a part hashed as that part, and
  of the generator (the writer's definition and the contract), through
  the one reader `scripts/docs_map.py`; the pages are scanned by
  `scripts/docs-check.py` for broken links, long dashes in prose and
  instance facts before they are kept. Pages, kind `page`, live in
  `docs/` of the engine root or of the project, the map never there;
  `docs/videos/` of the engine is not the documentation's: the planner,
  the index, the state and the check read `docs/` without it (SOL.0660).
  The ledger's Renders table carries the index with the map as its
  input. The pinned facts the planner reads as an owner are the section
  "Pinned facts (not rendered)" of the project's readme recipe.
  Realises: POS.1450, POS.1080, POS.0930. Choice: a command of its own
  against `/render`: a page has no recipe to iterate, the map is
  generated. The index named `README.md` against `index.md`: GitHub
  shows a directory's README as its front page. The map beside the
  ledger against `docs/`: a visitor of the documentation would not
  understand it. The pinned facts in the recipe against a file of their
  own: a file would need a kind of its own, and the recipe is read by
  both the README and the planner today; the cost is that a render's
  tool carries facts of the project. Inputs by a named part against
  hashing a file's body without its front-matter: the body changes at
  every round too, and a page citing one position would still be
  regenerated for every other; the cost is that a moved heading or a
  renumbered ID loses the part and regenerates the page, the safe side.
  The generator hashed with the inputs against a switch that forces a
  run: the state stays computed, never judged; the cost is that a change
  of the writer's definition or the contract regenerates every page. The
  outlines per kind and the one-line field of the index against trusting
  the writer's judgement: 106 different headings on 24 how-to pages and
  index entries of 187 words showed the judgement does not converge (the
  documentation audit of 2026-10-11,
  `projects/forge/sources/docs-audit-2026-10-11.md`). Built 2026-10-09
  whole: the skill, the three scripts and the two agents; the first run
  of `/document` the same day regenerated 83 pages and the index, three
  pages once more after the check named a failure in each; redrawn
  2026-10-11 from the audit and run the same day: 86 pages, three new,
  four regenerated once after the check. The map's shape is the skeleton
  `templates/docs-map.md`. `/document` runs only on main and refuses a
  repository behind or diverged (POS.1690, POS.1710); `generated` and
  `previous` leave the map's header and the run takes the previous map
  from git (SOL.0700). After the first and the second release of the
  brief `collaboration` the pages about/persistence-in-git,
  reference/ledger, reference/document-kinds,
  about/versioning-and-history, use/work-on-a-branch, use/save-your-work
  and use/pull-from-the-remote are regenerated and the migration, the
  branches and the step of a conflict get entries of the map; the
  release offers the run (POS.1450). Where:
  `.claude/skills/document/SKILL.md`,
  `.claude/skills/docs-contract/SKILL.md`, `templates/docs-map.md`,
  `.claude/agents/docs-planner.md`, `.claude/agents/docs-writer.md`,
  `scripts/docs-state.py`, `scripts/docs-index.py`,
  `scripts/docs-check.py`, `scripts/docs_map.py`,
  `projects/forge/docs-map.md`, `docs/`.
- **SOL.0660 The player page and the public folder.** `docs/videos/` of
  the engine is the public folder of POS.1540: flat, the
  `html-player.js` files of the projects' screenplays sent there by
  their recipes' `output:`, and one page, `docs/videos/index.html`, that
  plays them. The page is a single file
  with no dependency beyond the browser: a sidebar listing the files in
  the order of their names, by the title of each file's title card; the
  player — the simulated terminal, the caption band, the cards; play and
  pause, speed, the scenes of a video as chapters, the language where a
  file has siblings in other languages, three font sizes remembered in
  the browser. The page is written anew from its skeleton,
  `templates/html-player.html`, by `md2video.py` whenever it writes into
  the folder (SOL.0650), the list of files embedded, since GitHub Pages
  cannot list a folder; what is edited is the skeleton, never the page,
  and no model touches either: the page is tracked in git as a render's
  plain file is. `docs/.nojekyll`, empty, makes Pages
  serve the folder as it lies. The documentation leaves the folder
  alone: `docs-planner`, `docs-index.py`, `docs-state.py` and
  `docs-check.py` read `docs/` without `docs/videos/`, and the index of
  the documentation does not list it. Video files (`.mp4`) are not
  written here: a video goes out as an asset of a release. Realises:
  POS.1540, POS.1530. Choice: a fixed page with the list embedded
  against a generated index file beside it, a course recipe with an
  outline, or folders as sections: the three were weighed on 2026-10-14
  and the principal chose the alphabet of file names for now, the rest
  THR.0660's; the cost is that the script touches a page of the engine.
  A single file against a page with scripts and styles beside it: one
  file is one thing to serve and to copy. Where:
  `templates/html-player.html`, `docs/videos/index.html`, `docs/.nojekyll`,
  `.claude/agents/docs-planner.md`, `scripts/docs-index.py`,
  `scripts/docs-state.py`, `scripts/docs-check.py`,
  `scripts/md2video.py`.

### Persistence
- **SOL.0500 The repositories.** The engine is one git repository,
  `forge-of-thought`, full name Forge of Thought in documents; its
  public home is a pinned fact of the readme recipe, the one place the
  README and the documentation read it from (SOL.0460). The universal
  core in the root (`CLAUDE.md` for the agent, `README.md` for humans,
  `templates/`, `scripts/`, `.claude/`) together with `projects/forge`,
  the system's own project. The engine is a clone; the projects are
  nested git repositories in a gitignored `projects/*` with
  `projects/forge` re-included (`!projects/forge`; the pattern must be
  `projects/*`, not `projects/`, or the re-include fails silently).
  `.gitignore` carries `projects/forge/ledger.md` (SOL.0680). A per-
  project `CLAUDE.md` is polish only where genuinely needed. How the
  scripts recognise a project is in `scripts/forge_repos.py`, which the
  git scripts share. Realises: POS.0760, POS.0940, POS.0990. Choice:
  nested repositories under a gitignored directory against submodules,
  subtree, worktrees, a template repository and a plugin as the only
  shape (REJ.0150). Decided 2026-08-29. Where: `.gitignore`,
  `projects/`, `LICENSE`, `scripts/forge_repos.py`.
- **SOL.0510 The git scripts.** The scripts that serve the engine and
  every project that is a repository of its own: git names its directory
  as the top, one `rev-parse --show-toplevel` in `forge_repos`, resolved
  paths compared, a worktree and a linked directory alike, never a
  `.git` looked for; the engine's own project the one exception, its
  repository the engine. Anything else is a project outside git: the
  scripts skip or refuse it as today and run no git on it, whatever
  repository may lie above it. docs-state's walk up the parents for a
  `.git` goes the same way. Each script is described by its own help
  header: `forge-save.py`, which also pushes a clean repository that is
  ahead, a branch without an upstream counted against the remote's
  branch (SOL.0780), leaves a conflicting rebase standing for the step
  of a conflict and refuses a standing rebase or merge before it stages
  (SOL.0840); `forge-pull.py`; `forge-status.py`, which also reports a
  missing registration (SOL.0740) and a rebase or merge in progress
  (SOL.0840); `forge-clone.py`, which brings an existing project in;
  `forge-branch.py`, which creates a branch or switches to one, `main`
  included, with the slug alone reports the branch and lists the
  branches (TBC.0100); `forge-ledger.py` (SOL.0680); and
  `forge-migrate.py` (SOL.0800). `forge-status --remote` fetches the
  origin of each repository, which changes nothing in the working tree,
  and reports the branch against it: up to date, behind, ahead or
  diverged, with the counts; without the flag it touches no network. The
  state against the origin is one function of `forge_repos.py`, which
  status and pull share. `forge-pull` prints where it moved from and to
  and the subjects of the commits between, so that the releases crossed
  can be read off. Realises: POS.0550, POS.1060, POS.1110, POS.0940,
  POS.1490. Choice: scripts as the only door to a write against git
  typed by the model. Where: `scripts/forge-*.py`,
  `scripts/forge_repos.py`, `scripts/docs-state.py`,
  `.claude/skills/import-project/SKILL.md`.
- **SOL.0520 The wall.** Protection relies on Claude Code's permission
  system, not an OS-level sandbox: commands and file operations run
  under permission prompts and allowlists, shared deny rules in
  `.claude/settings.json` block sensitive paths (`~/.ssh`, `~/.aws`),
  and web access is approved per domain on first use. The line between
  reading git and writing it is a `PreToolUse` hook of the forge's own,
  `scripts/hook-git.py`, registered in the same file on the Bash tool
  and started in exec form like the per-prompt hook (SOL.0030): it
  splits the command at the shell's separators, cuts out heredoc bodies
  as text, finds every call of git past its global options and answers
  allow for a reading verb with reading flags, ask for the commands that
  finish the step of a conflict (SOL.0840: `add` without `--force` and
  the interactive flags, `rebase --continue` and `--abort`, `merge
  --continue` and `--abort`, `merge <branch>` with one name and no flag,
  `checkout --ours` or `--theirs` on a file), deny for everything else
  with the script to use instead, and nothing for a command that is not
  git; over a whole command deny outranks ask and ask outranks allow,
  `$(` marks a substitution whose git is denied whatever it is, and the
  shell's redirections are stripped before a verb is judged. Denied are the writing verbs, a verb it does not know, an alias
  among them, a reading verb with a writing flag (`branch -d`, `tag v1`,
  `config` with a value, `log --output`, `fetch --prune`), a global
  option that changes how git runs (`-c`, `--git-dir`, `--work-tree`,
  `--exec-path`; `-C` and `--no-pager` pass), git behind a wrapper that
  runs what it is given (`sh -c`, `eval`, `xargs`, `env`, `timeout`,
  `find -exec`, an interpreter with `-c` or `-e`) and git inside a
  command substitution; the word git as an argument of any other
  program, a commit message for `forge-save.py` among them, is text and
  left to the harness (the refusal of 2026-09-26, THR.0400). The ask
  holds in the automatic permission mode (tried 2026-10-21, THR.0400;
  seen 2026-10-23 at R6.01). Its cases are its own `--test`, run
  before it is
  registered and after every change; `--judge` prints the verdict of one
  command. The PowerShell tool stays closed to git whole,
  `PowerShell(git *)` under `permissions.deny`, so that there is one
  parser and one door. In the same file `attribution.commit` is empty
  and `attribution.sessionUrl` is false, so Claude Code adds and
  proposes no `Co-Authored-By` or `Claude-Session` trailer. Realises:
  POS.0550, POS.1200, POS.1090. Choice: the permission system against an
  OS-level sandbox, which was tried on 2026-08-04 and deliberately
  dropped: it is unavailable on Windows, where enforcing it meant no
  shell at all; the hook against the deny rule `Bash(git *)` that was
  the wall from 2026-09-21 to 2026-10-21 and against deny rules on the
  writing verbs: a prefix rule matches the text usually typed and `git
  -C . push` passes it, a deny rule cannot be carved by an allow rule
  and is not overridden by a hook, and two walls with one hole read
  worse than one; the cost is a parser of the shell that is a heuristic,
  so what it cannot read it denies. Where: `.claude/settings.json`,
  `scripts/hook-git.py`.
- **SOL.0530 Save and release.** `/release` runs its checks (SOL.0330),
  settles their findings, renders the README and the release notes
  unconditionally, with no staleness test, and ends by running `/save`
  with the release message and tag: not a second procedure. It never
  regenerates the documentation: it reports the age of the index against
  the intent's version and offers `/document` (POS.1450), the detail the
  release skill's. The release writes
  `renders/state.md` from the ledger script (POS.1650), its
  release-notes recipe tolerates a version without content changes
  (POS.1630), and its walkthrough walks the parts of this design marked
  "Not built" for the release made, by its number or deferred and then
  built in it, and turns them over to built, so that the mark does not
  outlive the building (TBC.0020). `/save` saves even when the light
  check cannot build the ledger, and says so, since the save is what
  does not lose work; a rebase that conflicts is left standing by
  `forge-save` for the step of a conflict, and a standing rebase or
  merge is refused before anything is staged (SOL.0840); `/release` refuses a repository that is behind or
  diverged, as do `/document` (SOL.0460) and `/publish` (SOL.0420),
  since `merge=ours` turns round in the rebase of the save (POS.1710).
  The renders come after the check and its walkthrough, not before: a
  render made from the settled sources is current by construction,
  whereas one made before it goes stale whenever a finding bumps the
  intent. The script pushes a tag with the commit and keeps it without
  an origin. `forge-save` checks that git resolves an identity for the
  repository and, where it resolves none, reports it with the command to
  set one and commits nothing until it is. A bare `/save` saves every
  repository with changes; with two windows open the slug narrows it to
  the one the window works in (POS.1700). Realises: POS.1100, POS.0570,
  POS.0730, POS.0810, POS.1070, POS.1710, POS.1650, POS.1700. Choice: two commands against one,
  alternatives REJ.0160 and REJ.0170; the cost is a README stale between
  releases, visibly. Where: `.claude/skills/save/SKILL.md`,
  `.claude/skills/release/SKILL.md`, `scripts/forge-save.py`.
- **SOL.0550 The commit identity.** No roster file and no local
  `git config user.*` at a project's creation or import. The
  identity is resolved per git host by the user's own `includeIf`
  stanzas, which `/setup` offers to write
  (SOL.0150), with the one global guard `user.useConfigOnly = true`
  and no global `user.name`/`user.email`; a surviving global
  identity defeats the guard, and `/setup` says so. Where one host
  serves two roles the user sets a local `git config user.*` of his
  own, which git lets win over the include; `forge-status` reports a
  repository-local identity as a fact, never as a defect (THR.0720).
  Realises: POS.0950, POS.1050. Choice: git's per-host includes
  against an identity kept by the forge; the cost is the two-roles
  case POS.0950 accepts. Reversed 2026-09-16: the identity had been
  a property of the project, set locally in every repository and
  proposed by the command layer from a roster in
  `identities.local.md`, and the per-host include had been rejected
  because a host is only a correlate of the identity and fails where
  one host serves two roles. Where: `.claude/skills/setup/SKILL.md`,
  `scripts/forge-status.py` (the local identity); outside the engine,
  the user's global git configuration file, named by
  `scripts/forge-status.py`.
- **SOL.0730 The ways and the attributes.** `templates/gitattributes`,
  copied by `/new-project` into a project's `.gitattributes`:
  `text=auto`; `merge=ours` on `renders/**`, `README.md`, `RELEASE-
  NOTES.md`, `CONTRIBUTING.md`, `docs/**`, `published/*.md`; `binary` on
  `published/*.pptx` and `published/*.docx`; the record files carry no
  attribute and merge as text (POS.1560). The engine's own
  `.gitattributes` is a list of its own: `merge=ours` on `README.md`,
  `RELEASE-NOTES.md`, `CONTRIBUTING.md` and `docs/**` at the root and on
  `projects/forge/renders/**` and the published companions, `binary` on
  the published files (CHL.0350). `check-project` reports a project
  without the file, with the fix. CLAUDE.md, Persistence, carries the
  ways and the promise. Realises: POS.1560, POS.1690, POS.1750. Choice:
  the attributes per project against a global configuration alone, since
  the attributes travel with the repository and the registration
  (SOL.0740) does not. Built 2026-10-19 in the first release (the
  cutover plan, R1.07, R1.02); the attribute of way 2, `merge=forge-
  records`, let go 2026-10-23 with the driver (REJ.0340). Where:
  `templates/gitattributes`, `.gitattributes`, `CLAUDE.md`
  (Persistence), `.claude/skills/new-project/SKILL.md`,
  `.claude/agents/check-project.md`.
- **SOL.0740 The registration on the machine.** `/setup` registers
  through `scripts/forge-config.py --register` in the global git
  configuration, once per machine and once in each place where git
  reads another global file, on the user's word,
  `merge.ours.driver true`, `rebase.backend merge` (the apply backend
  ignores drivers), `merge.renormalize true` (files committed with CRLF
  before normalisation would conflict whole), sets `rerere.enabled true`
  as a convenience, since a replay never repeats the automerge it keys
  on (CHL.0340), and offers `merge.conflictStyle zdiff3`. `forge-status`
  reports a missing registration, since an unregistered clone silently
  falls back to a conflict on the derived files. Realises: POS.1690,
  POS.1740 (the registration is the machine's, not the project's).
  Choice: one registration per machine against a registration per
  repository, which the migration must not touch. Built 2026-10-18, the
  preparation of the cutover plan: the report of `forge-status` (R1.12),
  the registration by `/setup` of `ours`, the backend, renormalize and
  rerere with the offer of zdiff3 (R1.14); the driver's own key,
  `merge.forge-records.driver`, let go 2026-10-23 with the driver
  (REJ.0340), never registered. Where: `.claude/skills/setup/SKILL.md`,
  `scripts/forge-config.py`, `CLAUDE.md` (Persistence),
  `scripts/forge-status.py`,
  `scripts/forge_repos.py`.

- **SOL.0780 The path through git.** The map ends with the state against
  the origin and its offer (built, `/forge` step 3); the reflection
  before a write reads that state from the last `forge-status --remote`
  and says "behind: pull first" as a recommendation; the write step
  never fetches; `forge-save` pushes a clean repository that is ahead, a
  branch without an upstream counted against `origin/<branch>` after a
  fetch or pushed as new, and leaves a conflicting rebase standing with
  the files and the step printed (SOL.0840). Realises: POS.1710,
  POS.1490. Choice: the state read once at the map and the reflection
  against a fetch at the write, so that the network never fails a round.
  The roles: a contributor's branch and `/save`, the integrator's merge
  and `/save` on main (POS.1770, SOL.0840). Built 2026-10-18, the
  preparation of the cutover plan (R1.12): the ahead counted against the
  upstream without a fetch, a branch with no upstream reaching the
  remote with its first commit; the push of a clean branch without an
  upstream and the conflict left standing 2026-10-23 (R6.02). Where:
  `.claude/skills/forge/SKILL.md`,
  `.claude/skills/walkthrough/SKILL.md`, `scripts/forge-save.py`.
- **SOL.0800 The migration.** `scripts/forge-migrate.py <slug> [--apply
  | --undo]`, door `/migrate [slug]`: a dry run by default; the shape as
  marks (the project file exists, no `date` in the headers, `threads/`
  exists, `.gitattributes` exists, the ledger out of the index); the
  steps in the order of one run: A (the header fields), B0 (the project
  file from the ledger's header), B (the mining and the work state as
  records, the index fields, the published companions, the Findings and
  Challenges tables frozen into `ledger.archive.md`, the ledger out of
  the index by `git rm --cached` through `forge_repos` and into
  `.gitignore`, a Waiting line without an ID printed), C1 (`threads.md`,
  in flow-ba `10-intent.threads.md`, cut by `- **THR.NNNN**` into files,
  `origin` guessed and printed), D (the attributes), then `/check light`
  and `/check project`; for a library A, B0, B and D; each step verifies
  itself; `--undo` restores every changed tracked file from the index
  through `forge_repos`, since the script stages nothing, and the
  created files and the removals from the index from its own manifest;
  refuses an unclean repository, one behind its origin or not on main,
  where the project is a repository of its own; a project outside git
  (SOL.0510) gets none of these: the dry run and `--apply` say that the
  forge runs no git here and that the way back is the user's backup,
  taken before `--apply`; `--undo` refuses there; step B takes the
  ledger out of an index only where the forge's repository has one; a
  run that stops midway is finished by running it again, the marks being
  the memory; commits nothing. `--apply` and `--undo` are tested on the
  fixture (SOL.0830), the migration outside git on the fixture without a
  repository; a real project gets the dry run in place and then its one
  `--apply`, never a clone (DEC.0240). Claude within `/migrate` judges
  the origins of the threads from the script's print. `/pull` of the
  engine says in Action required: `forge-pull` of the engine, `/setup`
  for the registrations, then every project the clone keeps: one already
  migrated elsewhere pulled by `/pull`, one not yet migrated run through
  `/migrate` on that one clone and saved; whose machine or instance the
  clone is makes no difference, every user of the engine migrates his
  own projects (CHL.0540); the map, `check-project` and every writing
  skill say "shape before the migration, run `/migrate`" on a project of
  the old shape and do not write. Realises: POS.1740, POS.0940,
  POS.0820. Choice: one script and one command against the hand
  migration of POS.0940, since every clone must come out the same; marks
  against an engine version in the project, which POS.0940 refuses.
  Built 2026-10-19 in the first release (the cutover plan, R1.13, R1.19,
  R1.23). Where: `scripts/forge-migrate.py`,
  `.claude/skills/migrate/SKILL.md`, `.claude/skills/pull/SKILL.md`,
  `.claude/skills/forge/SKILL.md`, `.claude/agents/check-project.md`,
  `templates/ledger.md` (the archive's shape), `CLAUDE.md` (the Commands
  table, Persistence). The tag before a migration is taken per project
  immediately before its `/migrate` and the engine's before its own; the
  way back from a tag is the principal's hand through git, a reset and a
  forced push or a revert, on a protected main a maintainer's, and
  always the engine and every project together, since the engine refuses
  the old shape once released (CHL.0420).
- **SOL.0830 The fixture.** The test bed of the forge's own tests is one
  project, `projects/fixture`, made by hand once from a bare remote
  `tmp/fixture.git` as a copy of a small real project in the old shape
  and brought to the new shape by the migration, which it thereby
  tested; its project file carries `fixture: true`, written by
  `forge-migrate` for a slug that starts with `fixture` and shown by
  `forge-clone`; nothing skips it: a bare `/save` saves it like any
  repository with changes, and since its origin is the bare remote in
  `tmp/`, nothing of it leaves the machine. On it `--apply`, the test of
  `ours` and the test of the step of a conflict ran, the last with a
  second clone made by hand in `tmp/` and removed after it (R6.03). The
  bare remote is per machine, and its HEAD stands on `master`, so a
  clone opens on the old branch and is switched to `main`. The tests of
  POS.1750 run on it, and on it alone, as rounds of the forge by slug,
  never on a clone of a real project (DEC.0240). Realises: POS.1750,
  POS.1590, POS.0550. Choice: one project made by hand against
  `scripts/fixture.py`, designed 2026-10-17 (CHL.0380, CHL.0520,
  CHL.0610, CHL.0500) and let go with the deferred releases (DEC.0280):
  two projects `fixture-a` and `fixture-b` from a bare remote, born in
  the old shape the script carried, every shape kept by `--shape
  <version>`, a project without git by `--no-git`, and a bare `/save`
  skipping `projects/fixture*` by name; the cost of the hand-made bed is
  that it lives on one machine and is remade by hand where a test needs
  it. Where: `projects/fixture` and `tmp/fixture.git`, not tracked by
  the engine, `templates/project.md` (the flag),
  `scripts/forge_repos.py`.

- **SOL.0840 The step of a conflict.** `forge-save` leaves a conflicting
  rebase standing: the commit is made, the script prints the files in
  conflict (`git diff --name-only --diff-filter=U`) and the step that
  follows, and it refuses a repository with a rebase or a merge already
  standing before it stages anything (`forge_repos.in_progress`, read
  from git's own marks, `rebase-merge`, `rebase-apply`, `MERGE_HEAD`;
  `forge_repos.conflicted`), so that conflict markers are never
  committed; `forge-status` says "rebase in progress, N file(s) in
  conflict". The step itself is the walkthrough
  (`.claude/skills/walkthrough/SKILL.md`): Claude reads both sides
  through the reading git the hook allows, one conflict one question,
  the principal's verdict, Claude writing the chosen wording into the
  file and a `changed` record into the history of the artefact, for a
  record file both tails kept; the commands that finish it run on the
  hook's ask (SOL.0520); `forge-save` then pushes the clean repository
  that is ahead, a branch without an upstream counted against
  `origin/<branch>` after a fetch or pushed as new. A version given
  twice and an ID taken twice are settled as POS.1790 says, the ledger
  script reporting both (SOL.0680). Realises: POS.1710, POS.1750,
  POS.1790, POS.1560, POS.1770. Choice: the help in `/save` and the
  hook's ask against `/merge` with a script of its own and the worktree
  (REJ.0350, REJ.0360); against `forge-save --continue` alone, since the
  ask also serves a merge the integrator makes by hand; against git
  opened to Claude whole, which would leave the commit message, the
  rebase before the push and the check before a save to text; no driver
  and no `merge=union` for the record files (REJ.0340, REJ.0280). Built
  2026-10-23 (the cutover plan, R6.01 to R6.03) and tested on the
  fixture with a second clone: a conflict in a history and in an
  artefact, two verdicts, `add` and `rebase --continue` on the ask,
  pushed and pulled back. Where: `scripts/forge-save.py`,
  `scripts/forge_repos.py`, `scripts/forge-status.py`, `scripts/hook-
  git.py`, `.claude/skills/walkthrough/SKILL.md`,
  `.claude/skills/save/SKILL.md`.

## Across the parts
- **SOL.0600 One model.** The reviewer agents declare `model:
  inherit` explicitly. The session model is chosen in
  `.claude/settings.local.json`, gitignored, which `/setup` creates.
  A command's `effort:` remains the lever for routine turns should
  one ever need it. The headless conversions behind `/publish`,
  `scripts/md2pptx.py` and `scripts/md2docx.py` with `--engine
  claude`, carry the default of their own in `--model`. The model a
  recipe may recommend in its Format section is the headless
  conversion's. A second engine beside the session model is reached
  through the adapter (SOL.0870) and named by its row, never by a
  model; `--model` passes a word to it where the principal asks for
  one and records it in the note.
  Realises: POS.0930, POS.0530, POS.1050, POS.1880. Choice: an explicit
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
  for the three documentation scripts, `forge_docs.py` (the
  front-matter, the records, the ledger tables, the index entries and
  the threads as the scripts read them) for forge-ledger, forge-migrate
  and forge-history, `forge_check.py` (a finding and its report, the
  keys and comments a template owns) for forge-check; `forge_repos.py`
  is shared by the scripts of the brief `collaboration` too (SOL.0510).
  The two hooks are Python scripts too, started by `python` from
  `.claude/settings.json`. Rewritten from PowerShell 7 on 2026-10-09,
  all nine at once, and tested that day against a fixture: a local bare
  remote, an engine cloned from it, a project with a remote and one
  without, 56 cases over every script and its refusals; the `claude`
  engine of the conversions was not run. Realises: POS.0830. Choice:
  Python against PowerShell 7, the principal's decision of 2026-10-02 on
  the feedback of the forge's users; `python` as the one command name
  against `python3`, since Windows has only the first and a Unix system
  gives it by an alias or a package, and the hook can name one. Options
  in the Python spelling (`--tag`, `--engine`, `--recipe`,
  `--reference`, `--template`, `--page-size`, `-o`) against the
  PowerShell ones, since argparse is the convention of the language.
  Portability is verified in part: the git scripts, the ledger and
  docs-state ran on Linux (POS.0830); the conversions and the two hooks
  have not. Where: `scripts/`.
- **SOL.0890 The working folder.** `tmp/` at the engine root, in git
  with `tmp/README.md` and `tmp/.gitignore` (everything but the two
  ignored), its subfolders made by the scripts and commands that need
  them: `tmp/research/<run>/` with a folder per packet, the hold, the
  cite reports, the profile `.home/` and the envelopes; the
  documentation's tasks; a dry ledger; a check's report before it is
  filed; a migration's manifest. Realises: POS.1900. Choice: one
  folder in the engine against the system's temporary directory or
  the session's scratchpad, so that a run is traceable on the machine
  and a profile's deny rules have one path to name; the price is a
  folder to empty by hand. Where: `tmp/README.md`, `tmp/.gitignore`.

## Open
- **TBC.0010** (owner: principal) Mermaid diagrams in a Word file:
  rendering them to pictures needs `mermaid-cli`, a further
  dependency not decided on (THR.0370; Waiting on principal in the
  ledger). Closed by: the principal's
  decision on the dependency. Blocks realisation: no.
- **TBC.0020** (owner: principal) Which check keeps this design true
  against what realises it; POS.1420 wants one and none exists. With
  it, how a layer is told to have fallen behind the intent it was
  brought to, since an artefact names no version of the intent
  (THR.0520, closed 2026-10-22). Closed by: the principal's decision
  on the check. Blocks realisation: no.
- **TBC.0030** (owner: principal) The reviewers on a different model
  family (POS.0800) are not built: the link exists (SOL.0870) and the
  research runs on it; `/challenge` and `/critique` on it, the
  consultation and the spool have no part here (THR.0740). Closed by:
  their design when the principal takes them up. Blocks realisation:
  no.

- **TBC.0100** (owner: Claude) `forge-branch` creates a local branch
  from the current state even when the origin has a branch of that name;
  it should track `origin/<branch>` where it exists (found at R6.03,
  2026-10-23, the second clone of the fixture opening on `master`).
  Closed by: the script changed and tried on the fixture. Blocks
  realisation: no; `forge-pull` brings the branch to the origin's and
  `forge-save` sets the upstream at the push.