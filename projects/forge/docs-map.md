---
target: engine
owner: projects/forge
---

# Documentation map - the engine

Paths under `inputs` are relative to the engine root. Every page of the previous map keeps its path and is `keep`; three pages are `new`: `docs/use/migrate-a-project.md`, `docs/about/the-ledger.md` and `docs/about/upgrades-and-migration.md`. None is `remove`. `docs/videos/` is not a section of the documentation and is not mapped. For every entry at least one other entry names it under `links`.

## Paths
- user: docs/start/what-it-is.md, docs/start/install.md, docs/start/setup.md, docs/start/first-result.md, docs/use/forge-the-intent.md
- extender: docs/extend/what-it-is-made-of.md, docs/extend/how-a-change-is-made.md, docs/about/how-the-rules-are-held.md, docs/reference/templates.md, docs/extend/change-a-documentation-page.md
- evaluator: docs/about/what-it-is-and-is-not.md, docs/about/how-a-thought-travels.md, docs/about/elicitation.md, docs/about/isolated-reviewers.md, docs/about/the-documentation.md

## start

### docs/start/what-it-is.md
- title: What Forge of Thought is
- line: What is this thing, in one paragraph, before you install anything?
- kind: explanation
- reader: user, evaluator
- says: One paragraph in plain words: Forge of Thought is a workshop in which a thought is tempered into a chain of versioned documents under review by agents that never saw the conversation; it runs in Claude Code, Anthropic's AI assistant for the command line; the person who uses it is the principal, whose thinking is forged and who decides everything, while Claude proposes and keeps order. One person starts from a rough brief, works it into an intent by interview, takes the layers the project needs, has the thinking attacked by blind reviewers and gets outputs for every audience generated from the documents. One closing sentence says what it technically is: a git repository of slash commands, isolated agents, templates, scripts and conventions, bound to no domain. One sentence then points at the course page of the teaching videos (the address the pinned facts give): real sessions cut to a few minutes and played in the browser, the place to see the forge at work before reading on.
- inputs:
  CLAUDE.md#What this workspace is
  CLAUDE.md#Roles
  projects/forge/10-intent.md#Essence
  projects/forge/10-intent.md#POS.0780
  projects/forge/10-intent.md#POS.0600
  projects/forge/recipes/readme.md#Pinned facts (not rendered)
- links:
  `docs/start/install.md`: what must be on the machine and how it gets there.
  `docs/about/what-it-is-and-is-not.md`: the longer explanation of what the forge is, is not, and why.
  `docs/about/the-screenplay-and-its-player.md`: what the teaching videos are made of and where they are played.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no commands, no file names, no conventions, no history of the project, no name of a person, no instance fact, no version number; no address but the course page's and none of the other pinned facts.
- made: derived
- evidence: CLAUDE.md, What this workspace is, gives the identity sentence; Roles the two roles; the Essence "runs in Claude Code", the reviewers and the domain; POS.0780 where a run ends; POS.0600 the name; the pinned facts the course page and what is played there. The technical sentence is composed from the Essence's last paragraph.
- state: keep

### docs/start/install.md
- title: Install what the forge needs
- line: What must be on your machine, and in what order, before the forge runs?
- kind: how-to
- reader: user
- says: Steps in the order a newcomer needs them, each with what you see when it worked: git; Python 3.8 or newer on PATH as a real executable named `python` (the scripts and the per-prompt hook are Python and the hook is started without a shell; the package or symlink the pinned facts name for Linux and macOS); Claude Code with a paid subscription, installed by the lines the pinned facts give, signed in on first run; clone the engine from its public home (never copy it: the scripts refuse an engine that is not a repository); always start `claude` from the engine root. The optional tools last, each resolved from PATH and installed by no script: markitdown through pip for `/ingest`'s conversions, pandoc for the plain Word and PowerPoint files of `/render`, Pillow and ffmpeg for the video format of a screenplay (the player format needs nothing beyond Python), the document-skills plugin for `/publish` unless Claude Code already brings the docx and pptx skills. Closes by pointing at the first setup. One worked example: the sequence as typed, with placeholders.
- inputs:
  projects/forge/recipes/readme.md#Pinned facts (not rendered)
  CLAUDE.md#Persistence (git)
  .claude/settings.json
  scripts/hook-walkthrough.py
  scripts/forge_repos.py
  scripts/doc2md.py
  scripts/forge_tools.py
  scripts/md2video.py
- links:
  `docs/start/what-it-is.md`: what you are installing, in one paragraph.
  `docs/start/setup.md`: the first run, `/setup`.
  `docs/reference/scripts.md`: every script with what it needs and its options.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no account, no author line, no e-mail; no address other than the engine's public home and the course page as the pinned facts give them; nothing of the readme recipe beyond its pinned facts; no platform-specific path; no claim that the scripts have been run on Linux or macOS; nothing on git identity or the registration of merge drivers (the setup page's); no mention of PowerShell; nothing of the script bodies below their headers.
- made: derived
- evidence: the pinned facts own the prerequisites, the `python` remedies, the Claude Code install lines, "clone, not copy", "start from the engine root", the script prerequisites and the addresses; CLAUDE.md, Persistence (Portability) gives Python 3.8 or newer and the tools resolved from PATH; `.claude/settings.json` starts the hook through `python`; `forge_repos.py` refuses an engine that is not a clone; `doc2md.py` gives the pip line; `forge_tools.py` owns what pandoc and the claude engine need; `md2video.py`'s header what the video and the player formats need. The order is the writer's, by when each piece is first needed.
- state: keep

### docs/start/setup.md
- title: Set up the forge
- line: What does `/setup` ask and write on the first run after cloning?
- kind: how-to
- reader: user
- says: The first run, before any other work: `/setup`. What you see, step by step: `CLAUDE.local.md` created from its template by a short interview, one question at a time, the conversation language first, then who the principal is by role, then the principal's short handle, which stands as the author of every history record he decides; the file is gitignored and never committed, and on an instance that already has it `/setup` only offers the lines it lacks. `.claude/settings.local.json` created with the session model set to Fable, the strongest model, on which the whole forge including the blind reviewers runs, or the strongest model the account lists, changeable with `/model` or by editing the file. The git identity, which is git's: the hosts you push to with a name and an e-mail for each, and the offer to write, on your word, the per-host `includeIf` stanzas with absolute paths and the global guard `user.useConfigOnly = true` into the global git configuration file the status script names, never overwriting. Then, once per machine and on your word, the registration of the merge drivers and the git settings they need in the same file (`[merge "ours"]`, `renormalize`, `rebase` backend `merge`, `rerere`, and `conflictStyle = zdiff3` offered apart), every key already set reported and left; declined, the lines are printed for you to apply by hand; `python scripts/forge-status.py` reports the registration afterwards. It never overwrites an existing file and runs no git operation; it ends by pointing at `/new-project` or `/import-project`. One sentence says that the course page of the teaching videos (the pinned address) shows a first run before you make your own. One worked example with placeholder values. Prerequisite: the install page.
- inputs:
  .claude/skills/setup/SKILL.md
  templates/CLAUDE.local.md
  scripts/forge-status.py
  projects/forge/recipes/readme.md#Pinned facts (not rendered)
- links:
  `docs/start/install.md`: what must be on the machine first.
  `docs/start/first-result.md`: from a new project to a saved intent in one sitting.
  `docs/about/persistence-in-git.md`: why the identity is git's, why the scripts are the only door and what the merge settings are for.
  `docs/reference/configuration.md`: the instance files and settings, field by field.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no example host, name, handle or e-mail that could be real; no instance value; no date of a finding; nothing of the skill copied as an instruction to Claude; no address but the course page's and none of the other pinned facts; no driver of the forge's own for record files, which is not registered today.
- made: mirrored
- state: keep

### docs/start/first-result.md
- title: Get a first result
- line: How do you go from nothing to a saved intent in one sitting?
- kind: how-to
- reader: user
- says: One sitting, every act outside Claude a step of its own: `/new-project my-idea` scaffolds the files; when asked, paste a brief (a five-line sample brief, generic and invented, is given on the page) and say it is finished, so it is approved; `/forge intent` mines the brief into the first intent through an interview, one question per message, written once at the round's end on the word `write`; in your own terminal at the engine root, `git -C projects/my-idea init -b main`, the one-off act Claude is not allowed to run, a remote optional; `/save`, which runs the light check and commits and pushes, and which names its cause when it commits nothing. One line that "not under git" until then is a fact, not an error. The other door: `/import-project <git-url>` then `/forge <project-slug>`. One sentence points at the course page of the teaching videos (the pinned address), where this sitting is shown on real work. Prerequisite: setup.
- inputs:
  projects/forge/recipes/readme.md#Instructions
  projects/forge/recipes/readme.md#Pinned facts (not rendered)
  .claude/skills/new-project/SKILL.md
  .claude/skills/forge/states/brief.md#Course
  .claude/skills/forge/states/intent.md#Course
  .claude/skills/save/SKILL.md
  .claude/skills/import-project/SKILL.md
  CLAUDE.md#Persistence (git)
- links:
  `docs/start/setup.md`: the first run that comes before.
  `docs/use/start-a-project.md`: the full job of starting a project.
  `docs/use/bring-in-an-existing-project.md`: a project you already have, cloned into `projects/`.
  `docs/use/forge-the-intent.md`: the full job of iterating the intent.
  `docs/use/save-your-work.md`: what a save does and asks.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no explanation of what a brief or an intent is beyond one clause each; no instance slug (use `my-idea`); no theory of elicitation; no address but the course page's; nothing of the readme recipe but its Quickstart instruction (Section 5) and the pinned course address; no author line.
- made: derived
- evidence: the sequence and the git step are the readme recipe's Quickstart instruction; what each step does for the person is read from the skills and the two Courses; "not under git" is CLAUDE.md, Persistence; the course page is the pinned facts'. The sample brief is invented by the writer as a generic shape.
- state: keep

## use

### docs/use/start-a-project.md
- title: Start a project
- line: How do you scaffold a thought project or a library with `/new-project`?
- kind: how-to
- reader: user
- says: `/new-project <slug>`: a thought project (the chain) or a library (`lib-` prefix, material only); the kind and the language of the chain artefacts are asked where your words leave them open and written once into the project file `project.md`. What the command creates for each kind, files only, never git: for every project the project file, `.gitattributes` from its template and a `.gitignore` that keeps the ledger out of git; for a thought project beside them `sources/`, `reviews/`, `challenges/`, `research/` and `threads/`, the two resource indexes, `decisions.md` and the readme and release-notes recipes with their history companions; for a library only the indexes and the readme recipe. The founding brief is asked for at once and handed to the brief procedure; the intent and lower layers are born at their first `/forge <state>`; the ledger is made once by its script; `logo.png` is optional. The one-off act that is yours: `git -C projects/<slug> init -b main`, then a remote if wanted. One worked example with `<slug>`.
- inputs:
  .claude/skills/new-project/SKILL.md
  templates/project.md
  CLAUDE.md#Persistence (git)
- links:
  `docs/use/write-a-brief.md`: composing the founding brief.
  `docs/use/share-material-through-a-library.md`: what a library is for.
  `docs/about/projects-and-the-engine.md`: why a project is a repository of its own and what its project file declares.
  `docs/about/languages.md`: why a project declares one output language.
  `docs/reference/repository-layout.md`: every file of a thought project and of a library.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no instance slug; nothing of the brief procedure; no git beyond the one way in CLAUDE.md names; no file of ID reservations, which the command does not create.
- made: mirrored
- state: keep

### docs/use/bring-in-an-existing-project.md
- title: Bring in an existing project
- line: How do you clone a project you already have into `projects/` with `/import-project`?
- kind: how-to
- reader: user
- says: `/import-project <git-url>` clones the repository through the clone script into `projects/<repository name>`, never overwriting, and relays the script's facts: the last commit, the origin, the identity git resolves (none means the save script will commit nothing), and the project file with its kind and language, or, where the project has no project file, that it is of the shape before the migration and the one remedy is `/migrate`; a project with neither a project file nor a ledger was not made by the forge, a fact, not a defect. Nothing is written into the project. Work starts by selecting it, `/forge <slug>`. The script's messages under "If something goes wrong". One worked example with `<git-url>`.
- inputs:
  .claude/skills/import-project/SKILL.md
  scripts/forge-clone.py
  templates/project.md
- links:
  `docs/use/see-where-a-project-stands.md`: the `/forge` map that follows.
  `docs/use/migrate-a-project.md`: what to do with a project of the shape before the migration.
  `docs/use/upgrade-the-engine.md`: what to check when a project was written to older conventions.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no URL with a real host (`<git-url>`; the script's `example.com` may stand); no identity example.
- made: mirrored
- state: keep

### docs/use/see-where-a-project-stands.md
- title: See where a project stands
- line: What does the bare `/forge` map tell you about a project, and what does `/ledger` tell you?
- kind: how-to
- reader: user
- says: Bare `/forge [slug]` first makes the project's ledger with its script, then reports the state map: the kind and the language from the project file, and whether the project is under git, as a fact; a library stops after its material and the git line; the artefacts with versions and status, the briefs with their mining state; which target states can be worked from here; stale renders and stale published files; the libraries it needs and whether each is cloned alongside; what waits on the principal, the few live matters named in words with the ID in brackets and the rest as a count; a recommended next step and, where more than one matter waits, the offer of a walkthrough. The last word is the state of the engine and of the project against the origin (up to date, behind, ahead, diverged, no origin) with that state's one offer; the map runs none of it. A project of the shape before the migration is said so and nothing more. `/ledger [slug]` makes the ledger and gives the same report from it, for one project or all; the lines the ledger script could not parse and its Reports section are read aloud, and fixing them is the light check's. One worked example of a map, generic.
- inputs:
  .claude/skills/forge/SKILL.md
  .claude/skills/ledger/SKILL.md
  templates/project.md
  templates/ledger.md#Reports
- links:
  `docs/about/the-ledger.md`: what the ledger is made from and why nobody writes it.
  `docs/use/pull-from-the-remote.md`: the offer the map makes when a repository is behind.
  `docs/use/migrate-a-project.md`: what to do when the map says a project is of the old shape.
  `docs/use/walk-through-a-list.md`: how the matters waiting on the principal are worked.
  `docs/reference/ledger.md`: the ledger's tables and state words.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no description of `/forge <state>`; no staleness definition beyond a pointer; no content of a real project; no worktree or branch suffix of a slug, which is not built.
- made: mirrored
- state: keep

### docs/use/write-a-brief.md
- title: Write a brief
- line: How do you compose or finish a brief with `/forge brief`?
- kind: how-to
- reader: user
- says: `/forge brief [name] [slug]` composes or finishes `00-brief.md`, or `00-brief-<name>.md` for a later whole. The three ways the text arrives and what happens with each: pasted whole, begun outside, born in the forge from a rough idea with Claude active at the opening, research and ingest proposed and run on your word. What you can ask for: a structure given to the text without a word changed; `??` for Claude's opinion. Free form, no IDs, approved only on your explicit word, mined by `/forge intent` when you say so; how far each brief is mined is shown in the ledger's Briefs table. One worked example of the exchange, generic.
- inputs:
  .claude/skills/forge/states/brief.md
  templates/brief.md
- links:
  `docs/about/the-brief.md`: what a brief is and why it is rough on purpose.
  `docs/use/research-a-topic.md`: the research step the brief's finding uses.
  `docs/use/register-a-source.md`: the ingest step the brief's finding uses.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no restatement of the Map's areas; nothing of the Partner block as instruction to Claude; no language rule beyond "kept in the language it is written in".
- made: mirrored
- state: keep

### docs/use/forge-the-intent.md
- title: Forge the intent
- line: How do you iterate the intent with `/forge intent`, round by round?
- kind: how-to
- reader: user
- says: `/forge intent [slug]` iterates `10-intent.md`: the briefs mined whole by whole, briefs offered before threads; or a round from an open thread, a new word of yours or what the recipients sent back. One theme at a time, the reality check last; answers carried in the conversation and written once per round on `write`, Claude reflecting the round back first; resolved threads move into positions or rejections and are closed. The open threads are files in `threads/`, one per thread, each saying what it concerns, where it came from and whether it is open; an unfinished conversation is saved into its thread before the session ends. The round ends by naming what changed and what stays open, naming the layers that can follow or offering the approval. `/challenge <persona> intent` is offered as the independent reality check. One worked example of a round, generic.
- inputs:
  .claude/skills/forge/states/intent.md
  templates/intent.md
  templates/thread.md
- links:
  `docs/about/the-intent.md`: what the intent holds and why it is rewritten for coherence.
  `docs/about/working-methods.md`: the named ways the conversation runs.
  `docs/use/challenge-the-thinking.md`: running the independent reality check.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no ID scheme; no restatement of the Map; no Partner text as instruction to Claude; no position or thread of the forge project; no renumbering of a thread at a merge, which is not built.
- made: mirrored
- state: keep

### docs/use/distil-an-assignment.md
- title: Distil an assignment
- line: How do you derive the assignment from the intent with `/forge assignment`?
- kind: how-to
- reader: user
- says: `/forge assignment [slug]` derives `20-assignment.md` from the intent in a joint pass of three phases: questions up front, one per message; the recast with a provenance map; the walkthrough by group, one verdict per group. A substance change goes to the intent first; a wording fix is made directly. After the pass `/critique essence` is offered, then the approval. Items in the Requirement style. One worked example of a group's walkthrough item, generic.
- inputs:
  .claude/skills/forge/states/assignment.md
  templates/assignment.md
- links:
  `docs/about/the-assignment.md`: what makes an assignment complete.
  `docs/reference/requirement-style.md`: the rule set of the items.
  `docs/use/critique-the-documents.md`: running the essence lens.
  `docs/use/spin-off-a-group.md`: a requirement group that becomes a project of its own.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no restatement of the Requirement style rules; no ID numbering rules; no item of a real project.
- made: mirrored
- state: keep

### docs/use/design-the-solution.md
- title: Design the solution
- line: How do you iterate the solution design with `/forge solution-design`?
- kind: how-to
- reader: user
- says: `/forge solution-design [slug]` iterates `40-solution-design.md` from the lowest layer above it. Whether one is worth writing is yours to say; the ways in: no design yet, a layer above that moved, the thing changed below, a wording fix. Every pass makes the coverage map. What cannot be realised goes back to the intent as a thread. `/challenge <persona> solution-design` is offered once the design stands; the persona `architect` exists for it. One worked example, generic.
- inputs:
  .claude/skills/forge/states/solution-design.md
  templates/solution-design.md
- links:
  `docs/about/the-solution-design.md`: what a solution design holds.
  `docs/use/challenge-the-thinking.md`: the challenge of the design.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no shape of a SOL item beyond one sentence; no item of the forge's own design.
- made: mirrored
- state: keep

### docs/use/work-a-work-product.md
- title: Work a work product
- line: How do you make an output of the project with work of its own, a model, an analysis, a worked task, with `/work`?
- kind: how-to
- reader: user
- says: `/work [name] [slug]`: bare, the roster of the project's work products from the ledger's Work table, made by its script, each with its file, its specification and version, its inputs, when it was made and its state (`current`, `stale`, `by hand`); with a name, the specification `work/<name>.spec.md` is born on your word from its template with its history companion, worked with you (handed over, or found together by interview), reflected back and written once per round; the file `work/<name>.<ext>` is made from it on your word, as its `## Making` section says, and the making is recorded in the specification's history, from which the Work table reads `current`. A file you have worked by hand and do not want remade is `by hand` on your word; Claude never remakes it on its own. A conclusion that is to hold goes into the intent first. One worked example with `<name>`.
- inputs:
  .claude/skills/work/SKILL.md
  templates/work.md
  templates/ledger.md#Work
- links:
  `docs/about/the-work-product.md`: what a work product is and why it is neither an artefact nor a render.
  `docs/use/forge-the-intent.md`: where a conclusion that is to hold goes.
  `docs/reference/ledger.md`: the Work table and its state words.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no work product of a real project; no ID numbering rules beyond naming ASM and TBC; nothing of the skill as an instruction to Claude; no record line copied from the history template.
- made: mirrored
- state: keep

### docs/use/register-a-source.md
- title: Register a source
- line: How do you store, register and catalogue external input with `/ingest`?
- kind: how-to
- reader: user
- says: `/ingest [file] [slug]`: with a file, that document; with text pasted into the conversation, the text as `sources/<slug>.md`; bare, a sweep for unregistered files and a report of files changed since registration. Personal matter stops the command before storing. Every binary gets one question, convert to Markdown? Yes: `scripts/doc2md.py` makes the extract, which is then the source; no: the binary is the source as a functional thing. A related set is a bundle with its own index. Before the index entry is written Claude asks what the source is for; the answer is its Role, or Claude infers it on your word and marks it so. The entry carries the source's date, best effort and never asked, and its form. A library document is cited by path in an entry and not copied; the ledger finds the citation by itself. Registration is not intake. The reply is two lines at most. One worked example, generic.
- inputs:
  .claude/skills/ingest/SKILL.md
  scripts/doc2md.py
  templates/index.md
  templates/index-bundle.md
- links:
  `docs/about/sources-and-research.md`: why sources are immutable and why registration is not intake.
  `docs/use/share-material-through-a-library.md`: citing a library's document.
  `docs/reference/scripts.md`: `doc2md.py`, its formats and what it needs.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no example file with a real name; no ledger column detail; nothing of the skill as an instruction to Claude; no merge driver of the index.
- made: mirrored
- state: keep

### docs/use/research-a-topic.md
- title: Research a topic
- line: How do you get a durable, indexed research note with `/research`?
- kind: how-to
- reader: user
- says: `/research <topic> [slug]` looks up current best practice on one question with web sources, marks consensus, emerging and contested, and writes an immutable dated note into `research/` with the question, findings with sources, options with trade-offs and a recommendation; several questions become several notes. Indexed in `research/00-INDEX.md`; the ledger's Research table reads the note itself. The summary leads with the recommendation; a change to an artefact is proposed through `/forge <state>`. One worked example, generic.
- inputs:
  .claude/skills/research/SKILL.md
  templates/index.md
- links:
  `docs/about/sources-and-research.md`: what research is for and why it is immutable.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no topic of the forge project; no index field detail beyond naming the three fields.
- made: mirrored
- state: keep

### docs/use/compose-a-recipe.md
- title: Compose a recipe
- line: How do you compose or iterate a render recipe by genre with `/recipe`?
- kind: how-to
- reader: user
- says: `/recipe [genre] [slug]`: bare, the roster of genres with the project's existing recipes; with a genre, a guided composition through its checklist, closing with the language question (one language, or several where the genre allows a primary and its translations; the project's language is proposed from its project file and never assumed), the recipe composed from the genre's skeleton; with the name of an existing recipe, an iteration. A recipe outside any genre is composed from the base skeleton. Versioned 0.x for life with its history companion; `/render <recipe>` offered next. The four genres of today in one line each. One worked example, generic.
- inputs:
  .claude/skills/recipe/SKILL.md
  .claude/skills/recipe/genres/presentation.md
  .claude/skills/recipe/genres/readme.md
  .claude/skills/recipe/genres/release-notes.md
  .claude/skills/recipe/genres/screenplay.md
  templates/recipe.md
- links:
  `docs/about/renders-and-recipes.md`: why the recipe is iterated and the render never edited.
  `docs/reference/recipe-genres.md`: each genre's checklist in full.
  `docs/use/render-an-output.md`: generating the render.
  `docs/use/make-a-video-from-a-recipe.md`: the screenplay genre from recipe to played video.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no checklist reproduced; no Format section detail beyond its existence; not the parenthesis of the release-notes genre that the forge's own recipe reads the intent alone.
- made: mirrored
- state: keep

### docs/use/render-an-output.md
- title: Render an output
- line: How do you regenerate a render, and its plain file, with `/render`?
- kind: how-to
- reader: user
- says: `/render <recipe> [slug]` regenerates a render from its recipe: the inputs read from disk (the ledger made first by its script where the recipe reads it), the Markdown generated in isolation from the recipe and its inputs alone, written to `renders/<recipe>.md` or the recipe's `output:` path, opening with provenance front-matter; where the recipe declares `languages:`, the primary render first and then one translation per language as a file of its own, `renders/<recipe>.<lang>.md`, scene for scene, nothing re-cut. Back in the session the file is scanned mechanically for instance facts (`python scripts/docs-check.py --file <render>`) and a hit is said aloud for you to judge; then the provenance is verified, and the ledger's Renders table reads it, nobody writing a row. Where the recipe has a `## Format` section the plain `.docx` or `.pptx` is made beside the render through pandoc, or for a screenplay the video or the player file through `scripts/md2video.py`, at the render or at the recipe's `output:`; a missing tool is said aloud and the render stands. Where a published file of the recipe exists, you are told it is now older than its render. Regenerated only on this command or by `/release`. One worked example, generic.
- inputs:
  .claude/skills/render/SKILL.md
  scripts/docs-check.py
- links:
  `docs/reference/render-provenance.md`: the front-matter block and the one definition of stale.
  `docs/use/publish-a-designed-file.md`: the designed file, made through a model.
  `docs/use/make-a-video-from-a-recipe.md`: the screenplay's formats in full.
  `docs/about/renders-and-recipes.md`: why a render is generated and never a source of truth.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no subagent prompt text; no provenance block (reference); no script options beyond `--file`; no render of the forge project named; no version on a branch in a provenance, which is not built.
- made: mirrored
- state: keep

### docs/use/make-a-video-from-a-recipe.md
- title: Make a teaching video from a recipe
- line: How do you turn real sessions into a screenplay and into a video or a player file with `/recipe screenplay` and `/render`?
- kind: how-to
- reader: user
- says: The job from end to end: register the session records as sources (`/ingest`) and write the brief of the videos; `/recipe screenplay` composes the recipe through its checklist (audience, the one message, the beats pinned by time of day, the quotes, the length, the title card, what must not appear, the languages with the primary first, the pace and the look, the format `video` or `html-player`, and for the player format whether the file goes out to the engine's `docs/videos/` by `output:` with its number for the order); `/render <recipe>` writes the screenplay, one render per language, and makes the format file through `python scripts/md2video.py` with the pace and the date the Format section names: an MP4 beside the render, or a `<recipe>.<lang>.html-player.js` beside the render or in `docs/videos/`, where the script renews the player page's list of files. A file sent to `docs/videos/` is read by you before the engine is saved; a video kept for the company names no `output:`. `/publish` has no part. What you see at each step; the script's messages under "If something goes wrong". One worked example with `<recipe>` and placeholder languages.
- inputs:
  .claude/skills/recipe/genres/screenplay.md
  templates/recipe-screenplay.md
  .claude/skills/render/SKILL.md
  scripts/md2video.py
  projects/forge/10-intent.md#POS.1540
- links:
  `docs/about/the-screenplay-and-its-player.md`: what a screenplay is, why one script makes both formats, and why the engine hosts the public files.
  `docs/use/compose-a-recipe.md`: the genre interview every recipe runs through.
  `docs/use/render-an-output.md`: the render and its plain file.
  `docs/use/register-a-source.md`: registering the session records.
  `docs/reference/scripts.md`: `md2video.py`, its options and what it needs.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no recipe, render or video of a real project; no course address (the start pages carry it); no name of a person; no reasons beyond one sentence each; no project slug from the script's examples (use `<slug>`).
- made: derived
- evidence: the genre file gives the checklist and the product; the skeleton the recipe's shape, the Format section and where the player file lands; the render skill steps 3, 4 and 7 the languages, the `output:` into `docs/videos/` and the run of the script; the script's header its synopsis, the two formats, where the output lands, the renewal of the player page and what it needs; POS.1540 that the file is read by the principal before the engine is saved and that a company video stays in `renders/`. The page joins them into one job in the order the person does it.
- state: keep

### docs/use/publish-a-designed-file.md
- title: Publish a designed file
- line: How do you make the designed Word or PowerPoint file with `/publish`?
- kind: how-to
- reader: user
- says: `/publish <recipe> [slug]` makes the designed `.pptx` or `.docx` from the render as it lies on disk, through a model and its document skills, into `published/`: started by you only, never by `/render`, `/release` or Claude's own judgement; on `main` only, and refused for a repository behind or diverged from its origin, with `/pull` offered; expensive and minutes long, said in one line before it runs. It never renders: a stale render is named first and the word is yours. A recipe without a `## Format` section ends at the Markdown; a screenplay has no published file. After the run a companion `published/<recipe>.md` records what the file was made from; the ledger's Published table reads it and shows the file `current`, or `stale` once its render is newer. A failed run writes no companion. One worked example, generic.
- inputs:
  .claude/skills/publish/SKILL.md
  templates/ledger.md#Published
- links:
  `docs/use/render-an-output.md`: the Markdown and the plain file that come first.
  `docs/reference/render-provenance.md`: the published companion and the definition of a stale render.
  `docs/reference/scripts.md`: `md2pptx.py` and `md2docx.py`, the `claude` engine and what it needs.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no model name as a recommendation; no script options beyond `--engine claude`.
- made: mirrored
- state: keep

### docs/use/generate-the-documentation.md
- title: Generate the documentation
- line: How does `/document` make the pages and the index, and what do you get at the end?
- kind: how-to
- reader: user, extender
- says: `/document [slug]` generates the documentation in one run that asks nothing: bare, the engine's into `docs/` with the map beside the ledger of `projects/forge`; with a slug, that project's into `projects/<slug>/docs/`. It runs on `main` only and refuses a repository behind or diverged from its origin, offering `/pull`. The steps in the person's terms: the previous map is taken from git; a planner reads the target on disk and writes the map; a script computes every page's state from the content of its inputs and of the rule the pages are made by (new, regenerate, keep, remove) and writes one task per page; pages that lost their entry are deleted; one writer per page makes it from its entry and inputs alone; a script derives the index; a script checks every page, a failing page regenerated once and one that fails twice left out. `docs/videos/` of the engine is not the documentation's and is left alone. What you get at the end: the counts, the Unowned list, what did not fit, what the writers left out, the places where a reason is not recorded, the check's result, the ledger remade so that its Renders table carries the index. A release never runs it: it reports the index's age and offers the command. One worked example of the closing report, generic.
- inputs:
  .claude/skills/document/SKILL.md
  scripts/docs-state.py
  scripts/docs-index.py
  scripts/docs-check.py
- links:
  `docs/about/the-documentation.md`: what the documentation is, for whom, and why it is generated.
  `docs/extend/change-a-documentation-page.md`: how a page is changed through its owners.
  `docs/reference/scripts.md`: the three documentation scripts with their options.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no agent prompt or task text; no model name; no field of the map; no page count or date of a run; nothing of the check script's `--file` mode.
- made: mirrored
- state: keep

### docs/use/critique-the-documents.md
- title: Critique the documents
- line: How do you run a critic lens on document quality with `/critique`?
- kind: how-to
- reader: user
- says: `/critique [lens] [artefact|path] [slug]`: bare, the roster of lenses with a recommended fit; with a lens, the ledger is made first, then one isolated agent reads the project's documents and judges document quality through that lens, never substance. The optional target narrows the run to one artefact, named as `/forge` names it, or to any file of the project by its path, read with the chain around it. The report comes back with its findings unnumbered; Claude gives each new finding its FND and files the report, word for word, in `reviews/` under a name of its date, kind, lens, time and a short content hash. What you see: the delta summary and the offer of a walkthrough; `accept` means an iteration of the artefact through `/forge`. No lens runs at a save; a release offers `essence` once. One worked example, generic.
- inputs:
  .claude/skills/critique/SKILL.md
  .claude/skills/critic-contract/SKILL.md#Output
- links:
  `docs/reference/critic-lenses.md`: the lenses of today.
  `docs/use/walk-through-a-list.md`: settling the findings one by one.
  `docs/about/the-critic.md`: what the critic judges and why it is blind.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no report shape; no severity or category vocabulary beyond naming that they exist; no finding of the forge project; no naming script options.
- made: mirrored
- state: keep

### docs/use/challenge-the-thinking.md
- title: Challenge the thinking
- line: How do you have a persona attack the substance with `/challenge`?
- kind: how-to
- reader: user
- says: `/challenge [persona] [artefact|path] [slug]`: bare, the roster of personas with a recommended fit; with a persona, the ledger is made first, then one isolated agent attacks the substance of the target, an artefact or any file of the project by its path, or the whole chain, never document quality, and returns a report with three to seven challenges ordered by severity, what is strong and the questions it cannot answer. Claude gives each challenge its CHL and files the report word for word in `challenges/` under a unique dated name. Best run before the next layer is first derived. What you see: the overall read, each challenge compressed, Claude's own disagreement marked as its own, the offer of a walkthrough; `accept` means the challenge is mended through `/forge`. A rejected challenge is a healthy outcome. One worked example, generic.
- inputs:
  .claude/skills/challenge/SKILL.md
  .claude/skills/challenger-contract/SKILL.md#Output
- links:
  `docs/reference/challenger-personas.md`: the personas of today.
  `docs/use/walk-through-a-list.md`: settling the challenges one by one.
  `docs/about/the-challenger.md`: what the challenger judges and why it may be wrong.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no report shape; no persona text; no challenge of the forge project.
- made: mirrored
- state: keep

### docs/use/check-conformance.md
- title: Check conformance
- line: How do you run a check against the conventions with `/check`?
- kind: how-to
- reader: user
- says: `/check [check] [slug]`: bare, the roster of checks; with a check, the target's ledger is made first, then one read-only isolated agent verifies mechanical conformance of a project (`/check light forge` for the engine's own project) or of the engine (`/check engine`) and returns its report. Claude files it in `reviews/` under a unique dated name only when it has findings, gives each new finding its FND, presents the ranked findings, offers every "immediate fix" at once and a walkthrough of the rest. Several checks on one target may run at once. Nothing blocks. Which checks a save and a release run is theirs. One worked example, generic.
- inputs:
  .claude/skills/check/SKILL.md
  .claude/skills/check-contract/SKILL.md#Output
- links:
  `docs/reference/checks.md`: the checks of today.
  `docs/use/walk-through-a-list.md`: settling the findings.
  `docs/use/upgrade-the-engine.md`: the checks after an upgrade.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no report shape; no Lens text; no finding of the forge project.
- made: mirrored
- state: keep

### docs/use/walk-through-a-list.md
- title: Walk through a list
- line: How is a list of findings, challenges or threads worked one item at a time?
- kind: how-to
- reader: user
- says: How any list that needs your decision is worked: one item per message, in order of weight; what an item carries; the proposition closing with `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`, answered with a single letter or the word; `question` asks about the open item and changes nothing, Claude answers and closes the item again; `obsolete` as a further verdict. The verdicts are carried and written once at the round's end on `write`, Claude reflecting the whole round back first; `accept` writes what the producing command says and a closing record; `reject`, `park` and `obsolete` each write a decision with your reason and its verdict line, and a rejected item is not raised again; the ledger is made afresh after the write. The elicitation interview runs the same way. One worked example of one item, generic.
- inputs:
  .claude/skills/walkthrough/SKILL.md
- links:
  `docs/reference/verdict-words.md`: the words and letters, exactly.
  `docs/about/working-methods.md`: why the one-item rule exists and how a hook holds it.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no hook text; nothing addressed to Claude; no record or decision line copied from a template.
- made: mirrored
- state: keep

### docs/use/save-your-work.md
- title: Save your work
- line: What does `/save` check, ask and commit?
- kind: how-to
- reader: user
- says: `/save [slug] [-m "message"] [--tag name] [--quick]`: the scope from the status script, each repository with the branch it is on; the `light` check on every repository in scope, settled through `/check`, a save never waiting on a finding you have not asked to fix, and going on, said aloud, where the ledger script cannot read a file; `--quick` leaves the check out and nothing else; a one-line commit message drafted from the round's history records and confirmed, or `-m`; a tag only on your word, any name git accepts; then the save script, which commits, rebases your commits onto the remote and pushes on whatever branch is checked out, no render. It pushes a clean repository that is ahead of its origin; a rebase that conflicts is aborted with nothing lost and the steps to finish it by hand printed; without an origin the commit stays local; where git resolves no identity it commits nothing. One worked example, generic.
- inputs:
  .claude/skills/save/SKILL.md
  scripts/forge-save.py
  scripts/forge-status.py
- links:
  `docs/use/release-a-version.md`: the other door, from `main`, with the renders.
  `docs/use/end-a-session.md`: the end of a session, which names what is unsaved.
  `docs/about/persistence-in-git.md`: why there are two doors and two speeds.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no git command typed by you beyond what the script prints for a conflicting rebase; no example message from the forge project; no slug from the script's examples (use `<slug>`; `forge` may stand); no landing of branch records, which is not built.
- made: mirrored
- state: keep

### docs/use/release-a-version.md
- title: Release a version
- line: What does `/release` run, render and tag, in what order?
- kind: how-to
- reader: user
- says: `/release [slug] [-m "message"] [--tag name]` releases one repository from `main` only, refusing another branch with the way back and a repository behind or diverged from its origin with the offer of `/pull`: the checks (`light` and `project` for a project; `engine`, `light` and `project` for the engine) settled by walkthrough; `critique essence` offered once; the README and the release notes regenerated through `/render` with a summary of what materially changed; then the state render, the ledger written as the tracked file `renders/state.md`; the age of the documentation reported and `/document` offered; then `/save` with the message `release <intent version>: <one line>` and, at an integer version, the tag `v<major>` on your word, Claude first naming what the forge's own intent asks a major to pass. The check is advisory. One worked example, generic.
- inputs:
  .claude/skills/release/SKILL.md
- links:
  `docs/use/save-your-work.md`: the save the release ends with.
  `docs/use/check-conformance.md`: the checks and how their findings are settled.
  `docs/about/renders-and-recipes.md`: why the README and the release notes are renders.
  `docs/use/generate-the-documentation.md`: the command the release offers.
  `docs/about/versioning-and-history.md`: what a major approves.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no version number of the forge; no description of what a major must pass beyond the pointer; no claim that the release regenerates the documentation on its own.
- made: mirrored
- state: keep

### docs/use/pull-from-the-remote.md
- title: Pull from the remote
- line: How does `/pull` look at the remote, and what does it pull and refuse?
- kind: how-to
- reader: user
- says: `/pull [slug]` (bare: the engine and every project with an origin; `forge`: the engine). First the state of each repository against its origin as a fact (up to date, behind, ahead, diverged, no origin, not under git); a repository with unsaved changes or a diverged history stops with its one offer, `/save` first, nothing pulled. For what is clean and behind the pull script fast-forwards and reports where each repository moved from and to and the commits between. After a pull of the engine the Action required lines of the releases crossed are shown and the two checks offered per project; where an Action required line names a migration, `/migrate <slug>` is offered for each project of the old shape. The forge never pulls or merges on its own. The scripts' refusals under "If something goes wrong". One worked example, generic.
- inputs:
  .claude/skills/pull/SKILL.md
  scripts/forge-pull.py
  scripts/forge-status.py
- links:
  `docs/use/upgrade-the-engine.md`: what to do after a pull of the engine.
  `docs/use/migrate-a-project.md`: the migration a release may ask for.
  `docs/use/save-your-work.md`: the save that must come first on unsaved work.
  `docs/about/persistence-in-git.md`: why the forge looks at the remote and offers.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no git command; no slug from the script's examples; no version numbers; no `/merge` command, which does not exist.
- made: mirrored
- state: keep

### docs/use/upgrade-the-engine.md
- title: Upgrade the engine
- line: How do you take a new version of the engine and bring your projects to its conventions?
- kind: how-to
- reader: user
- says: The job after a pull of the engine: read the Action required lines `/pull` showed, which stand first in every section of the release notes; then, project by project, `/check light <slug>` and `/check project <slug>` measure the project against the current conventions, the findings are walked one at a time and Claude brings the project current on your word. Where a release changed the shape of files, its Action required line says so: each project of the old shape is migrated once with `/migrate <slug>` on one clone and saved, and a project migrated elsewhere is pulled. Projects record no engine version and the pull does not touch them; a project left as it is stays valid under the conventions it was written to, though one of the old shape is read and not written until it is migrated. One worked example, generic.
- inputs:
  .claude/skills/pull/SKILL.md
  projects/forge/10-intent.md#POS.0940
  projects/forge/10-intent.md#POS.0820
  projects/forge/recipes/release-notes.md#Template
- links:
  `docs/use/pull-from-the-remote.md`: the pull itself.
  `docs/use/check-conformance.md`: running a check and settling its findings.
  `docs/use/migrate-a-project.md`: the migration of a project to a new shape of files.
  `docs/about/upgrades-and-migration.md`: why a project records no engine version and when a migration comes with a release.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no version numbers; no history of past migrations; no repository address; nothing of the release-notes recipe beyond its reader and that Action required stands first; no reasons beyond the link.
- made: derived
- evidence: the pull skill's step 3 gives what follows a pull of the engine and the offer of `/migrate`; POS.0940 that a project records no engine version, the migration path through the two checks with Claude migrating on the user's word and a migration for a release that changes the shape of files; POS.0820 that an artefact stays valid under the conventions it was written to and that a project of the old shape is read, not written; the recipe's Template that Action required stands first. The page joins them into one job.
- state: keep

### docs/use/migrate-a-project.md
- title: Migrate a project
- line: How do you bring a project to the shape of files a new release expects, with `/migrate`?
- kind: how-to
- reader: user
- says: `/migrate [slug]` (`forge` is the engine's own project) runs once per project, on one clone, on `main`, when a release changed the shape of files; everyone else pulls the migrated project. What happens, step by step: Claude runs the dry run, `python scripts/forge-migrate.py <slug>`, and shows its print as it came: the marks of the shape, the steps that would run and what each would change; a project already in shape ends there. On your word, and only then, the script runs with `--apply`: the fields that change with a round leave the headers, the project file is written, what only the ledger knew becomes records and index fields, the hand-kept ledger is kept as an immutable archive and the ledger leaves git, the threads file is cut into one file per thread, the `.gitattributes` is written; a library takes fewer steps. The script commits nothing. Then Claude walks through what the script printed for your judgement, above all the origin it guessed for each thread, as a walkthrough written into the thread files at the round's end; text that was not a thread goes where it belongs. Then the ledger is made and `/save <slug>` proposed; the migrated shape reaches the remote by that save. The way back before the save is `python scripts/forge-migrate.py <slug> --undo`; after it, the tag taken before the migration. The refusals under "If something goes wrong": not a repository, a working tree that is not clean, a branch behind or diverged from its origin, any branch but `main`, an instance file without the `Author` line. One worked example with `my-idea`.
- inputs:
  .claude/skills/migrate/SKILL.md
  scripts/forge-migrate.py
  templates/project.md
- links:
  `docs/use/upgrade-the-engine.md`: the upgrade a migration belongs to.
  `docs/about/upgrades-and-migration.md`: why a shape change comes with a migration and why it runs once.
  `docs/use/save-your-work.md`: the save that carries the migrated shape to the remote.
  `docs/use/walk-through-a-list.md`: how the guessed thread origins are judged.
  `docs/reference/scripts.md`: `forge-migrate.py`, its forms and what it needs.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no slug from the script's examples (`fixture` and the like; use `<slug>` or `my-idea`); no name of a release or of a brief of the forge project; no conversion to one sentence per line, which is not built; no manifest path or file name of the script's internals; no reasons beyond the link.
- made: mirrored
- state: keep

### docs/use/end-a-session.md
- title: End a session
- line: How does `/end` tell you what a shutdown would lose?
- kind: how-to
- reader: user
- says: `/end` says what lives only in this conversation (a round not written, verdicts carried, anything promised and not done) and offers the write; runs the status script without the remote and names every repository with unsaved changes, offering `/save`; makes the ledger and names stale renders as a fact; closes with one sentence: nothing lives only in this conversation and shutting the command line loses nothing, or the list of what it would lose. It writes nothing and runs nothing but its scripts. One worked example of the closing, generic.
- inputs:
  .claude/skills/end/SKILL.md
  scripts/forge-status.py
- links:
  `docs/use/save-your-work.md`: the save it offers.
  `docs/about/documents-and-records.md`: why state lives in files and never in the conversation.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no git command; no content of a real session.
- made: mirrored
- state: keep

### docs/use/read-the-history-of-an-item.md
- title: Read the history of an item
- line: How do you see the whole history of one position, requirement or part with `/history`?
- kind: how-to
- reader: user
- says: `/history <ID> [slug]` (a short form such as `pos580` is accepted; `forge` is the engine's own project) runs the history script and prints what it printed: the item as it stands today, its timeline oldest first and every other citation in the project; `--full` prints every Was whole. Claude adds at most three sentences of its own, marked as such; nothing is written. An ID nothing in the project knows is said so, never guessed. Read-only. One worked example with a placeholder ID.
- inputs:
  .claude/skills/history/SKILL.md
  scripts/forge-history.py
- links:
  `docs/about/versioning-and-history.md`: why the history is a log beside the document and is searched, never loaded whole.
  `docs/reference/history-companion.md`: the shape of a record the script reads.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no item of the forge project quoted; no script internals below the docstring.
- made: mirrored
- state: keep

### docs/use/work-on-a-branch.md
- title: Work on a branch
- line: How do you switch a repository to a branch without typing git?
- kind: how-to
- reader: user
- says: Branches are voluntary: `python scripts/forge-branch.py <slug> <branch>` switches the repository to the branch, creating it when it does not exist, `main` switching back; with the slug alone it reports the branch and lists the branches (`forge` means the engine). Unsaved changes stop a switch. Merging, deleting and pushing branches stay with git; a new branch reaches the remote by the first save made on it; a release, a documentation run and a publish are made from `main` only. One worked example with `<slug>` and `<branch>`.
- inputs:
  scripts/forge-branch.py
  .claude/skills/release/SKILL.md
- links:
  `docs/use/save-your-work.md`: the save that carries a branch to the remote.
  `docs/about/persistence-in-git.md`: why merging is left to git.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no git command other than through the script; no branch name or slug from the script's examples other than `forge` and `main`; no worktree, `--done` or `/merge`, which are not built.
- made: mirrored
- state: keep

### docs/use/spin-off-a-group.md
- title: Spin off a group
- line: How does `/spinoff` make a requirement group a project of its own?
- kind: how-to
- reader: user
- says: `/spinoff <project> <group> <slug>` splits a requirement group of an assignment into a project of its own, only on your explicit instruction: the items to move confirmed; the new project created by the `/new-project` procedure; a short brief derived from the source intent, approved on your word; mined into the new intent; in the source project the intent records the spin-off first and the assignment marks the moved items superseded and replaces the group with one link item; the command itself writes the decision; both ledgers are made afresh. Claude may propose readiness, never run it. One worked example, generic.
- inputs:
  .claude/skills/spinoff/SKILL.md
- links:
  `docs/use/start-a-project.md`: what the new project is made of.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no group or slug of an instance project.
- made: mirrored
- state: keep

### docs/use/look-up-a-command.md
- title: Look up a command
- line: How does `/man` print the manual of a command or a working method?
- kind: how-to
- reader: user
- says: `/man [command | method]`, alias `/manual`, is the forge's manual, read at the moment of the call from the files that own it: bare, the commands and the working methods; with a command, its purpose, arguments, the roster it dispatches over with what each entry looks for, and the skill file; with a method, its paragraph and the skill that holds its shape. It runs nothing and prints in the conversation language, the notation staying English. The word `help` is Claude Code's own. One worked example, generic.
- inputs:
  .claude/skills/man/SKILL.md
  .claude/skills/manual/SKILL.md
- links:
  `docs/reference/commands.md`: the same table, as a page.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no copy of the Commands table.
- made: mirrored
- state: keep

### docs/use/share-material-through-a-library.md
- title: Share material through a library
- line: How do you keep material shared across projects in a library and cite it?
- kind: how-to
- reader: user
- says: A library is a project of kind `library`, prefix `lib-`, with no chain: the project file, its `.gitattributes` and `.gitignore`, `sources/` and `research/` with their indexes, and a readme recipe whose render is a catalogue; its ledger is made by the script like every project's. Born by `/new-project lib-<name>`; documents enter by `/ingest`; a changed document is the owner's maintenance. A project uses a library document by citing its path: `/ingest` adds an index entry that names the path, and the ledger finds the citation and lists it under Dependencies; a deck template or a Word reference document is named by path in a recipe's Format section. The `/forge` map says which libraries a project needs and whether each is cloned alongside; a missing one is brought in with `/import-project`. One worked example with `lib-<name>`.
- inputs:
  .claude/skills/new-project/SKILL.md
  .claude/skills/ingest/SKILL.md
  .claude/skills/forge/SKILL.md
  .claude/agents/check-light.md
  CLAUDE.md#Repository layout
- links:
  `docs/about/projects-and-the-engine.md`: why a library is a kind of project.
  `docs/use/register-a-source.md`: the ingest the library shares with every project.
  `docs/use/bring-in-an-existing-project.md`: cloning a library that is missing alongside.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no library name of an instance; no template file name of a company.
- made: derived
- evidence: the library's file set is CLAUDE.md, Repository layout; what `/new-project` creates is its Every project and Library paragraphs; a changed document as maintenance is `/ingest`'s sweep paragraph; citation by path, found by the ledger as a dependency, is `/ingest` step 6; the map's Dependencies line is `/forge` step 3; the missing-library finding is the light check's Dependencies clause.
- state: keep

## about

### docs/about/what-it-is-and-is-not.md
- title: What the forge is and is not
- line: What is Forge of Thought, what is it not, and why?
- kind: explanation
- reader: user, extender, evaluator
- says: What the forge is: a general engine for forging any thought, bound to no person or management relationship; the principal is whoever's thinking is forged; Claude is a cognitive extension, an amplifier never a substitute, who proposes and never decides. What it is not: not a program; not a delivery tool, a run ends where its owner is satisfied; not a chat, state lives in files; not tied to one domain. Why the name, why "thought" and not "assignment", why the chain ends where the project needs it to. One worked example: one invented thought and where its run ends.
- inputs:
  CLAUDE.md#What this workspace is
  projects/forge/10-intent.md#Essence
  projects/forge/10-intent.md#POS.0005
  projects/forge/10-intent.md#POS.0010
  projects/forge/10-intent.md#POS.0070
  projects/forge/10-intent.md#POS.0780
  projects/forge/10-intent.md#POS.0330
  projects/forge/10-intent.md#POS.0600
  projects/forge/10-intent.md#POS.0620
  projects/forge/10-intent.md#REJ.0125
  projects/forge/10-intent.md#REJ.0130
- links:
  `docs/about/how-a-thought-travels.md`: the course of one thought through the forge.
  `docs/about/the-principal-and-claude.md`: the two roles and the rule between them.
  `docs/about/where-it-is-going.md`: the direction the forge is developed in.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no name or handle of the first principal or author; no company; no origin story beyond "it began as one person's tool, an instance fact"; no commands.
- made: derived
- evidence: CLAUDE.md gives the identity; the Essence and the positions the general engine, the amplifier, where a run ends, state in files, the name; the two REJ what was rejected.
- state: keep

### docs/about/how-a-thought-travels.md
- title: How a thought travels through the forge
- line: What happens to one idea from a rough brief to a saved release?
- kind: explanation
- reader: user, extender, evaluator
- says: One invented, generic thought followed through: it arrives as a brief; is chiselled into the intent by elicitation, rewritten for coherence every round; below the intent the project takes the layers it needs, an assignment, a solution design, many ending at the intent; at every layer blind reviewers press on the documents and the thinking; outputs for every audience are generated through recipes, work products made beside them where the project needs work of its own, the documentation generated the same way; everything saved to git and released. Sources and research arrive at any stage. The main courses of events in one sentence each.
- inputs:
  CLAUDE.md#Document chain
  projects/forge/40-solution-design.md#How the parts work together
  projects/forge/10-intent.md#POS.0110
  projects/forge/10-intent.md#POS.0120
  projects/forge/10-intent.md#POS.0130
  projects/forge/10-intent.md#POS.1400
  projects/forge/10-intent.md#POS.0400
  projects/forge/10-intent.md#POS.0710
  projects/forge/10-intent.md#POS.0180
  projects/forge/10-intent.md#POS.1100
  projects/forge/10-intent.md#POS.1520
- links:
  `docs/about/the-document-chain.md`: the chain as a star.
  `docs/about/isolated-reviewers.md`: why the reviewers never see the conversation.
  `docs/about/renders-and-recipes.md`: how an output is generated from the artefacts.
  `docs/about/the-work-product.md`: an output made with work of its own.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no command syntax beyond names in passing; no forge project detail; no version numbers; no landing of branch records or merge driver, which the design head names and which are not built.
- made: derived
- evidence: CLAUDE.md, Document chain gives the chain; the solution design's head the main courses of events; the positions what each station is for, POS.1520 the work product. The page tells it in the order a thought meets it.
- state: keep

### docs/about/the-principal-and-claude.md
- title: The principal and Claude
- line: Who decides, who proposes, and which rules bind Claude?
- kind: explanation
- reader: user, evaluator
- says: The two roles and the prime directives that follow, each with its reason: when unsure ask, raising what does not fit as a question and saying in words how sure a claim is; never introduce a convention unilaterally; many iterations are normal; research before inventing; advisory never blocking; structure over prose; one write per round and "written" means a file; one mechanism in one place. Why: nothing enters content because Claude proposed it; the rules bind Claude, not the principal. Authorship is the principal's whether an artefact is found together or handed over. One worked example of a question raised, generic.
- inputs:
  CLAUDE.md#Roles
  CLAUDE.md#Prime directives
  projects/forge/10-intent.md#POS.0005
  projects/forge/10-intent.md#POS.0010
  projects/forge/10-intent.md#POS.0020
  projects/forge/10-intent.md#POS.0030
  projects/forge/10-intent.md#POS.0040
  projects/forge/10-intent.md#POS.0050
  projects/forge/10-intent.md#POS.0070
  projects/forge/10-intent.md#POS.0190
  projects/forge/10-intent.md#POS.0200
  projects/forge/10-intent.md#POS.0430
  projects/forge/10-intent.md#POS.1070
  projects/forge/10-intent.md#POS.1370
  projects/forge/10-intent.md#POS.1410
- links:
  `docs/about/working-methods.md`: the named ways the two work together.
  `docs/about/how-the-rules-are-held.md`: how the harness backs the principal's word.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no name, role or handle of an instance's principal; no directive as an instruction to Claude beyond what it means for the person; no decision record cited; no project the reasons were learnt on.
- made: derived
- evidence: CLAUDE.md, Roles and Prime directives give the rules; the positions their reasons. A directive whose reason no position gives is said to have its reason not recorded.
- state: keep

### docs/about/working-methods.md
- title: The working methods
- line: What are the named ways a working conversation runs, and why each exists?
- kind: explanation
- reader: user, evaluator
- says: The forge's vocabulary of collaboration, none a command: Walkthrough, Propose never decide (and `??`), Step by step, Elicitation interview, In pieces, Draft early, Reflect back, One write per round (`write`), Intent-first, Handing over, Recommend do not push, Plain speech, Kind not count. For each, what it is in the operating layer's wording and why in the intent's: the one-item rule because text loaded once dissolves in a long conversation, which is why a hook repeats it; `question` as a verdict so that a question is never mistaken for a yes; one write per round; step by step because consent is given to a concrete operation; handing over because the principal's attention is the scarce thing; plain speech; kind not count. Every list that needs a decision ends by offering a walkthrough. One worked example of a method invoked, generic.
- inputs:
  CLAUDE.md#Working methods
  .claude/skills/walkthrough/SKILL.md
  projects/forge/10-intent.md#Working methods
  projects/forge/10-intent.md#POS.1410
- links:
  `docs/use/walk-through-a-list.md`: the walkthrough as a procedure.
  `docs/about/elicitation.md`: the process the elicitation interview is one instrument of.
  `docs/reference/verdict-words.md`: the words the principal types.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no hook text; no dates or incidents of the intent's reasons; no project the methods were learnt on; nothing of the assistant's memory.
- made: derived
- evidence: CLAUDE.md, Working methods gives every method's name and wording; the walkthrough skill the shape and the verdicts; the intent's group Working methods and POS.1410 the reasons. The page keeps CLAUDE.md's order.
- state: keep

### docs/about/elicitation.md
- title: Elicitation
- line: How are the principal and Claude meant to find an artefact together, and what is a definition?
- kind: explanation
- reader: user, extender, evaluator
- says: Elicitation is the process by which the principal and Claude find an artefact together: the conversation is the medium, the interview one instrument, research and sources others. Three things kept apart: the map of what must be found, the process by which it is walked, the template where the result lands. Every kind of artefact has a definition in seven blocks, Target, Inputs, Aim, Partner, Map, Instruments, Course, paired with its template; a Map is a map of what must be found, not a questionnaire. What is not elicitation: composing a recipe, `/setup`, a walkthrough of findings. Found together or handed over, authorship is the principal's. One worked example: a Map walked for an invented artefact.
- inputs:
  projects/forge/10-intent.md#Elicitation
  templates/artefact-definition.md
  CLAUDE.md#Document chain
- links:
  `docs/about/the-document-chain.md`: how the definitions make the chain a star.
  `docs/extend/add-an-artefact.md`: writing a definition of one's own.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no block of a particular artefact's definition; no brief of the forge project named; nothing of the Elicitation group's history beyond the reasons.
- made: derived
- evidence: the intent's group Elicitation states what elicitation is, the seven blocks and the Map; the skeleton shows the blocks; CLAUDE.md, Document chain says every artefact has a definition paired with its template.
- state: keep

### docs/about/the-document-chain.md
- title: The document chain
- line: Why is the chain a star of definitions, and how does it grow?
- kind: explanation
- reader: user, extender, evaluator
- says: The chain starts at a brief and its trunk is the intent; below the intent a project takes the layers it needs, none a condition of another. The chain is a star: each definition declares its own inputs, so a layer branches from any artefact by adding one definition, and the dispatcher never changes. Files numbered in tens. Which artefacts exist is the listing of the definitions directory. Substance changes go into the intent first. The chain never spans two principals. The diagram: the artefacts of today's chain with their inputs as the definitions declare them. One worked example, generic.
- inputs:
  CLAUDE.md#What this workspace is
  CLAUDE.md#Document chain
  .claude/skills/forge/SKILL.md
  .claude/skills/forge/states/brief.md#Inputs
  .claude/skills/forge/states/intent.md#Inputs
  .claude/skills/forge/states/assignment.md#Inputs
  .claude/skills/forge/states/solution-design.md#Inputs
  projects/forge/10-intent.md#POS.0100
  projects/forge/10-intent.md#POS.0140
  projects/forge/10-intent.md#POS.0580
  projects/forge/10-intent.md#POS.0700
  projects/forge/10-intent.md#POS.1400
- links:
  `docs/about/the-brief.md`: the first artefact.
  `docs/about/the-intent.md`: the trunk.
  `docs/about/elicitation.md`: what a definition is.
  `docs/reference/artefacts.md`: the definitions of today, one row each.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no planned layer drawn as if it existed; no forge project history.
- made: derived
- evidence: CLAUDE.md gives the trunk, the growth and the numbering; the `/forge` skill the star; the Inputs blocks the arrows of the diagram; the positions the reasons. Where no input gives a reason, the page says the reason is not recorded.
- state: keep

### docs/about/the-brief.md
- title: The brief
- line: What is a brief, who writes it, and why is it rough on purpose?
- kind: explanation
- reader: user, evaluator
- says: An artefact page: a brief is the principal's text of one whole of thinking, free form, no IDs, rough on purpose because the chiselling is the intent's. Not the record of the finding. Nothing marks authorship; `(source: <path>)` and `(remark: ...)` carry something else. Three origins equally legitimate. A project may have more than one, mined into the single intent when the principal says so; how far each is mined is recorded in the intent's history, since the mining changes the intent and not the brief. Approved on his word, never locked. Kept in the language it is written in. One worked example: a generic five-line brief.
- inputs:
  .claude/skills/forge/states/brief.md
  templates/brief.md
  projects/forge/10-intent.md#POS.0110
  projects/forge/10-intent.md#POS.0920
  projects/forge/10-intent.md#REJ.0040
  projects/forge/10-intent.md#REJ.0180
  projects/forge/10-intent.md#REJ.0220
  CLAUDE.md#Prime directives
- links:
  `docs/use/write-a-brief.md`: composing one.
  `docs/about/the-intent.md`: where the brief is mined.
  `docs/about/languages.md`: why a brief keeps its language.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no brief of the forge project named or quoted; no Course steps; no author field value; nothing of the prime directives but directive 6's language exception.
- made: derived
- evidence: the definition gives the wording and how the files are made; the template the header; the positions what a brief is and why, POS.0920 the mining record; the three REJ what was rejected; prime directive 6 the language exception.
- state: keep

### docs/about/the-intent.md
- title: The intent
- line: What does the intent hold, why is it rewritten every round, and where does solving go instead?
- kind: explanation
- reader: user, evaluator
- says: An artefact page: the intent is the consolidated current state of what the principal holds, rewritten for coherence every round, never a log. It holds positions with reasons and provenance, facts, rejected directions; what is being worked lives in threads, one file per thread beside it, each saying what it concerns, where it came from and whether it is open, rewritten freely while open and immutable once closed, so that two people on different threads never meet and Claude reads only the threads he needs. An intent says what is wanted and why and does not solve: the test of a sentence is whether it would still hold if the thing were realised wholly differently. Complete for now when no thread blocks the next layer, never finished. One worked example: a generic position with its reason.
- inputs:
  .claude/skills/forge/states/intent.md
  templates/intent.md
  templates/thread.md
  projects/forge/10-intent.md#POS.0120
  projects/forge/10-intent.md#POS.1680
  projects/forge/10-intent.md#POS.0230
  projects/forge/10-intent.md#POS.1390
  projects/forge/10-intent.md#REJ.0010
- links:
  `docs/use/forge-the-intent.md`: iterating it.
  `docs/about/elicitation.md`: how the intent is found.
  `docs/about/versioning-and-history.md`: the history companion a position's past lives in.
  `docs/about/the-solution-design.md`: where the solution goes instead.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no position or thread of the forge project quoted; no numbering rules beyond naming the prefixes; no renumbering of a thread at a merge, which is not built.
- made: derived
- evidence: the definition gives the wording and the Threads and files block; the template and the thread template the shapes; the positions what a position, a fact and a thread carry, POS.1680 why threads are files, and the intent/solution test; REJ.0010 why a Q&A log was rejected.
- state: keep

### docs/about/the-assignment.md
- title: The assignment
- line: What makes an assignment complete, and where does assigning end and solving begin?
- kind: explanation
- reader: user, evaluator
- says: An artefact page: the assignment carries the in-scope substance of the intent to the recipients, complete and precise. Complete means nothing left to assumption: delegated or open on purpose is complete, silent is not. It assigns and does not solve, the boundary being the kind of content never its amount. Items with stable IDs and shall/shall not, no priorities, testability recommended, success criteria wanted not compulsory; why shall and not MoSCoW. Why a joint pass of three phases. Why the name. One worked example: a generic requirement item.
- inputs:
  .claude/skills/forge/states/assignment.md
  templates/assignment.md
  projects/forge/10-intent.md#POS.0130
  projects/forge/10-intent.md#Structure and style of an assignment
  projects/forge/10-intent.md#POS.1350
  projects/forge/10-intent.md#REJ.0050
  projects/forge/10-intent.md#REJ.0060
  projects/forge/10-intent.md#REJ.0120
- links:
  `docs/use/distil-an-assignment.md`: the joint pass as a procedure.
  `docs/about/stable-ids.md`: why every item carries an ID.
  `docs/reference/requirement-style.md`: the rule set.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no rule set reproduced; no item of an instance project; no spin-off mechanics; nothing of the ID group's merge clash or blocks of IDs, which are not built.
- made: derived
- evidence: the definition gives the wording and the two "why not"; the positions the reasons; the three REJ what was rejected.
- state: keep

### docs/about/the-solution-design.md
- title: The solution design
- line: What does a solution design hold, and why does it restate nothing above it?
- kind: explanation
- reader: user, extender, evaluator
- says: An artefact page: the solution design says how the things wanted are realised, kept current, read by whoever realises it without the principal in the room. Derived from the lowest layer above it; worth writing where the way is not obvious or a choice has a price. It holds why, against what, at what price, how the parts fit; it cites the layer above by ID and names what realises a part by path. The shape of a SOL item; a TBC with its owner. One worked example: a generic SOL item.
- inputs:
  .claude/skills/forge/states/solution-design.md
  templates/solution-design.md
  projects/forge/10-intent.md#POS.1390
  projects/forge/10-intent.md#POS.1400
  projects/forge/10-intent.md#POS.1420
- links:
  `docs/use/design-the-solution.md`: iterating it.
  `docs/about/the-intent.md`: the layer whose "what" this answers.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no item of the forge's own design quoted; no check named that does not exist.
- made: derived
- evidence: the definition gives the wording; the three positions the reasons.
- state: keep

### docs/about/the-work-product.md
- title: The work product
- line: What is a work product, why is it two files, and why is it neither an artefact nor a render?
- kind: explanation
- reader: user, extender, evaluator
- says: A concept page: a work product is an output of the project made with work of its own, a model, an analysis, a worked task, in whatever form the work needs; it takes its inputs from the chain and the resources, is iterated, is handed over, and what it shows flows back into the intent. It is two files in `work/`: the file, named by the work alone, holds the content; the specification beside it holds the way and the why (the task, the inputs cited by ID and path and never copied, the method, assumptions as ASM, open matters as TBC, how the file is made), versioned with its history companion and approvable. The specification is in the project's language, the file in the language the work needs. The principal works with the file freely; whether the file is current, stale or worked by hand is recorded in the specification's history, and the ledger's Work table shows it. Why it is not a render (a render carries no content of its own and is never edited by hand), not a research note, not an artefact of the chain; why stretching the render was dropped. One worked example: a generic specification.
- inputs:
  projects/forge/10-intent.md#POS.1520
  projects/forge/40-solution-design.md#SOL.0640
  templates/work.md
  CLAUDE.md#Document kinds
- links:
  `docs/use/work-a-work-product.md`: working one with `/work`.
  `docs/about/renders-and-recipes.md`: the render, which a work product is not.
  `docs/about/documents-and-records.md`: the kinds of document a project holds.
  `docs/reference/templates.md`: the specification's skeleton.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no work product of a real project; no command steps beyond one sentence; nothing of the design's group beyond SOL.0640.
- made: derived
- evidence: POS.1520 gives what a work product is, the two files, its neighbours and the reason the render was not stretched; SOL.0640 the one command, the Work table read from the records and its choice; the template the shape of the specification; CLAUDE.md, Document kinds the row of the kind.
- state: keep

### docs/about/documents-and-records.md
- title: Documents and records
- line: What kinds of document does a project hold, and why does state live in files?
- kind: explanation
- reader: user, extender, evaluator
- says: "Document" is every file of a project; "artefact" is reserved for the documents of the chain. Every document has one kind, in six groups: artefacts; records (history and decisions append-only; reviews and challenges immutable); state (the ledger made at read time, the project file written once, the threads, the indexes, the documentation map); rendering (recipes, renders, pages); work (the work product); resources (sources and research). Why state lives in files and never in the conversation. The ledger is the single source of truth for state, made from the other files and never written by hand, said in one sentence with a link. Why immutability is a process rule. Prose hard-wrapped at about 72 columns. One worked example, generic.
- inputs:
  CLAUDE.md#Document kinds
  templates/decisions.md
  projects/forge/10-intent.md#POS.1080
  projects/forge/10-intent.md#POS.0160
  projects/forge/10-intent.md#POS.0320
  projects/forge/10-intent.md#POS.0330
  projects/forge/10-intent.md#POS.0550
- links:
  `docs/reference/document-kinds.md`: the table of kinds, verbatim.
  `docs/about/the-ledger.md`: what the ledger is made from and why nobody writes it.
  `docs/use/end-a-session.md`: the command that says what lives only in the conversation.
  `docs/about/versioning-and-history.md`: the history companion of every versioned kind.
  `docs/about/the-documentation.md`: the map and the pages.
  `docs/about/the-work-product.md`: the work kind.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no table reproduced; no forge project ledger content; no merge driver of the record files, which is not built; no "one sentence per line", which is not built.
- made: derived
- evidence: CLAUDE.md, Document kinds gives the groups and kinds; the decisions skeleton the shape of a record; the positions the reasons. Where no input gives a reason, the page says the reason is not recorded.
- state: keep

### docs/about/the-ledger.md
- title: The ledger, made from the records
- line: Why is the ledger made at read time from the other files, and where does the state it shows really live?
- kind: explanation
- reader: user, extender, evaluator
- says: A concept page. What it is: the ledger is the single source of truth for a project's state (its briefs, documents, renders, published files, work products, sources, research, dependencies, findings, challenges and what waits on the principal), made at read time by a script from the project's documents and never kept in git; nobody writes a row, and every command that changes state makes it afresh. How it works: what only the ledger once knew lives in records and fields where it belongs: the mining of a brief as a record in the intent's history, the settling of a finding or a challenge as a closing record or a decision's verdict line, a work product's state in its specification's history, a source's date and form in its index entry, a published file's provenance in its companion; a record of state only carries the current version and does not raise it. Waiting on the principal is a rule, not a list: the open threads, the open questions he owns, the open findings of a critic and the open challenges, and the parked ones under a heading of their own. The Reports section says what the files cannot say by themselves (an ID defined twice, a closed thread touched later, a thread cited with no file), and a file the script cannot read is named in the header instead of breaking the run. The hand-kept ledger of a migrated project stays as an immutable archive, read for every item with no newer record. Where the state is wanted on the remote, a release writes it as a tracked render. Why: the ledger was the one file present at every collision of two people or two windows on one project, since every operation wrote it; made at read time it stops being a thing to merge; a hand-kept list of what waits differed from any rule in both directions. One worked example: a generic closing record and the ledger row it yields.
- inputs:
  CLAUDE.md#Ledger
  templates/ledger.md
  templates/history.md
  scripts/forge-ledger.py
  projects/forge/10-intent.md#POS.1600
  projects/forge/10-intent.md#POS.1610
  projects/forge/10-intent.md#POS.1620
  projects/forge/10-intent.md#POS.1630
  projects/forge/10-intent.md#POS.1650
- links:
  `docs/reference/ledger.md`: the tables, their columns and the state words, exactly.
  `docs/use/see-where-a-project-stands.md`: the map and `/ledger`, which read it.
  `docs/about/documents-and-records.md`: the kinds of document the ledger is made from.
  `docs/about/upgrades-and-migration.md`: the migration that turned a hand-kept ledger into an archive.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no landing of branch records, no `+` version token, no "merged unseen" or unlanded-records report, no version on a branch, which are not built; no row of a real project's ledger; no project named at whose merges the reason was found; no count of documents or reports.
- made: derived
- evidence: CLAUDE.md, Ledger gives the made-at-read-time rule, that nobody writes a row and where what only the ledger knew lives; the ledger skeleton the tables, the Waiting rule, the Reports and the archive; the history skeleton the records of state; the script's header the kinds of document it reads and that an unparsable file is a header line; POS.1600 to POS.1630 and POS.1650 the reasons and the state render.
- state: keep

### docs/about/versioning-and-history.md
- title: Versioning and history
- line: What does a version number mean, what is a major, and where does a document's history live?
- kind: explanation
- reader: user, extender, evaluator
- says: Integers denote signed-off versions, drafts 0.x; status agrees with the number; a recipe stays 0.x for life. A header carries nothing that changes with a round: the date and the last change of a document are computed from its history by whatever reads them, so that no field asks for a write at every round. What a major of an intent is and what its test attests. Every versioned document, a work specification included, keeps its history in an append-only companion beside it, a log of one record per change with the reason, Action and Was; a record of state only (a mining, a closing, a work product's state) carries the current version and does not raise it. Why: the way to an item does not belong in the item; the log is the single primary from which commit messages and release notes derive; a history is searched by `/history`, never loaded whole. A companion written before the log moves to an archive. One worked example: a generic record.
- inputs:
  CLAUDE.md#Versioning & status
  templates/history.md
  projects/forge/10-intent.md#POS.0300
  projects/forge/10-intent.md#POS.0310
  projects/forge/10-intent.md#POS.1570
  projects/forge/10-intent.md#POS.1630
  projects/forge/10-intent.md#POS.0730
  projects/forge/10-intent.md#POS.1510
  projects/forge/10-intent.md#REJ.0110
- links:
  `docs/reference/versioning-and-front-matter.md`: the fields and the scheme, exactly.
  `docs/reference/history-companion.md`: the record's shape.
  `docs/use/read-the-history-of-an-item.md`: reading one item's history by command.
  `docs/use/release-a-version.md`: where the tag of a major is proposed.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no record of the forge project; no version number of the forge; no list of the checks a major of the forge ran; no `landed` kind, `+` token, landing on main or version written on main only, which are not built.
- made: derived
- evidence: CLAUDE.md gives the scheme, the header rule and the companion rule; the template the record and the records of state; the positions the reasons, POS.1570 the header and POS.1630 the state records; REJ.0110 the rejected scheme.
- state: keep

### docs/about/stable-ids.md
- title: Stable IDs
- line: Why does every item carry an ID that is never renumbered?
- kind: explanation
- reader: user, extender, evaluator
- says: Every item carries `PREFIX.NNNN`, four digits as long as the number fits and a fifth only beyond 9999, numbered in tens with each group at the next hundred, global and stable, never renumbered, every sorting numeric. Why structure over prose: an item with a stable ID can be cited, reviewed, traced and changed one at a time. Why a fact, a position and a thread have prefixes of their own; why a thread carries its origin. One worked example, generic.
- inputs:
  CLAUDE.md#ID scheme
  projects/forge/10-intent.md#POS.0200
  projects/forge/10-intent.md#POS.0230
  projects/forge/10-intent.md#REJ.0020
  projects/forge/10-intent.md#REJ.0100
- links:
  `docs/reference/id-scheme.md`: the prefix table and the numbering rules.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no table; no ID of an instance project; no group name of a company standard; no renumbering at a merge clash, no blocks of IDs per author, no allocation over branches, which are not built.
- made: derived
- evidence: CLAUDE.md gives the rules, the fifth digit and the numeric sort; POS.0200 and POS.0230 the reasons; the two REJ what was rejected. The reason for the fifth digit given in the intent rests on the blocks of IDs, which are not built; the page says the fifth digit and gives no reason for it beyond what CLAUDE.md says.
- state: keep

### docs/about/isolated-reviewers.md
- title: The isolated reviewers
- line: Why do three kinds of reviewer never see the conversation, and what does their agreement mean?
- kind: explanation
- reader: user, extender, evaluator
- says: Three kinds of reviewer of one shape: the critic, the challenger, the check. All run as isolated subagents that see the project's documents and never the working conversation, on the session model; their blindness is the source of their value. All invoked by hand, settled by walkthrough, reports immutable and dated, each named by its date, the time and a short content hash so that two branches never make the same name; nothing blocks. Every agent returns its report with its findings unnumbered and writes nothing; the command numbers it and files it, so that the IDs are given in one place and reviewers may run in parallel. The shared behaviour of each kind is one contract, the agent file owns only its Lens. Isolation is not independence: their agreement is never validation. Instance facts never enter a report. One worked example, generic.
- inputs:
  CLAUDE.md#Isolated reviewers
  projects/forge/10-intent.md#POS.0400
  projects/forge/10-intent.md#POS.1120
  projects/forge/10-intent.md#POS.1140
  projects/forge/10-intent.md#POS.1720
  projects/forge/10-intent.md#POS.0430
  projects/forge/10-intent.md#POS.0440
  projects/forge/10-intent.md#POS.0450
  projects/forge/10-intent.md#POS.0540
  projects/forge/10-intent.md#POS.0790
  projects/forge/10-intent.md#REJ.0080
- links:
  `docs/about/the-critic.md`: what the critic judges.
  `docs/about/the-challenger.md`: what the challenger judges.
  `docs/about/the-check.md`: what a check verifies.
  `docs/use/walk-through-a-list.md`: how findings are settled.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no roster; no contract text; no planned challengers on another model family presented as built; the documentation agents are not reviewers; no version on a branch in a report, which is not built.
- made: derived
- evidence: CLAUDE.md gives the mechanism and the filing by the command; POS.1140 why the command numbers and files; POS.1720 why the names are unique; the other positions the reasons; REJ.0080 why review and challenge are two reviewers.
- state: keep

### docs/about/the-critic.md
- title: The critic
- line: What does a critic lens judge, and why two lenses?
- kind: explanation
- reader: user, extender, evaluator
- says: The critic judges the quality of the artefacts as documents through a lens, never the substance; two lenses because one critic hunted formalities and never guarded the chain: `clarity` reads each artefact on its own, `essence` distils every adjacent pair blind and compares. A target narrows a run to one artefact, or to any file of the project read with the chain around it, a work product with its specification, so that what Claude composes gets the isolated look as well. How it works: regression first, respect for rejected findings, sharp and few, each artefact judged against its own definition, deliberate omissions never defects. What it produces. One worked example of a finding, generic.
- inputs:
  .claude/skills/critic-contract/SKILL.md
  projects/forge/10-intent.md#POS.0400
  projects/forge/10-intent.md#POS.0410
  projects/forge/10-intent.md#POS.0270
- links:
  `docs/use/critique-the-documents.md`: running a lens.
  `docs/reference/critic-lenses.md`: the lenses and their angles.
  `docs/extend/add-a-critic-lens.md`: adding a lens of one's own.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no report template; no instruction to the agent copied as such; no finding of the forge project.
- made: derived
- evidence: the contract gives subject, target, way of working and output; the positions why two lenses, why a file may be the target and why testability is a recommendation.
- state: keep

### docs/about/the-challenger.md
- title: The challenger
- line: What does a challenger persona attack, and why may it be wrong?
- kind: explanation
- reader: user, extender, evaluator
- says: The challenger attacks the substance through a persona with a register and blind spots of its own, as an equal with no stake in the principal being right. Its target is an artefact, any file of the project read with the chain around it, or the whole chain. How it works: reads for what is not there, grounds itself externally, never fabricates, three to seven challenges by severity with an epistemic status, never proposing edits; it may be wrong. What it produces. Why best run before the next layer; why a rejected challenge is healthy; why an accepted one is mended where it needs to be. One worked example, generic.
- inputs:
  .claude/skills/challenger-contract/SKILL.md
  projects/forge/10-intent.md#POS.0420
  projects/forge/10-intent.md#POS.0440
  projects/forge/10-intent.md#POS.0450
  projects/forge/10-intent.md#POS.0790
- links:
  `docs/use/challenge-the-thinking.md`: running a persona.
  `docs/reference/challenger-personas.md`: the personas and what each hunts.
  `docs/extend/add-a-challenger-persona.md`: adding a persona of one's own.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no report template; no challenge of the forge project; no persona text.
- made: derived
- evidence: the contract gives subject, target, way of working and output; the positions the reasons.
- state: keep

### docs/about/the-check.md
- title: The check
- line: What does a check verify, why is it read-only, and who files its report?
- kind: explanation
- reader: user, extender, evaluator
- says: A check verifies mechanical conformance with the current conventions, never substance or quality, each check owning one concern; it reads the rules at their owners. Read-only: it returns its report and the command files it, only when it has findings. Findings only, precise to file and line, ranked; a finding decided once by a decision is not raised again, and a known one is reported under the ID it has. Advisory. Composition is the caller's: `/save` runs `light` unless told otherwise, `/release` runs `light` and `project`, for the engine `engine` too. One worked example, generic.
- inputs:
  .claude/skills/check-contract/SKILL.md
  projects/forge/10-intent.md#POS.0540
  projects/forge/10-intent.md#POS.0570
  projects/forge/10-intent.md#POS.1140
- links:
  `docs/use/check-conformance.md`: running a check.
  `docs/reference/checks.md`: the checks and what each verifies.
  `docs/extend/add-a-check.md`: adding a check of one's own.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no report template; no Lens text; no finding of the forge project; no overlap check of ID reservations, which is not built.
- made: derived
- evidence: the contract gives subject, way of working and output; the positions the composition and the reasons. Where no input gives a reason, the page says the reason is not recorded.
- state: keep

### docs/about/renders-and-recipes.md
- title: Renders and recipes
- line: Why is an output generated from a recipe and never edited by hand?
- kind: explanation
- reader: user, extender, evaluator
- says: A render is an audience-specific output generated from the chain, never a source of truth; what is iterated is its recipe; never edited by hand. The boundary between chain and render is authorship. Every render opens with provenance and is stale when a cited version differs; regenerated only on the principal's word or by a release, because regeneration is stochastic. A recipe may declare several languages, the first primary and the rest translated from it in the same run, one render per language, because a second generation would choose the quotes and the cut again differently. An output is made in two steps divided by cost: the plain file with the render through pandoc, or through the screenplay script, and the designed file by `/publish` through a model, whose provenance stands in a companion beside it; a screenplay has no designed step. Every project's README and release notes are renders; recipes may be composed by genre. A page of the documentation and a work product are not renders. One worked example: a generic recipe's shape.
- inputs:
  CLAUDE.md#Document chain
  templates/recipe.md
  templates/recipe-readme.md#Instructions
  projects/forge/10-intent.md#POS.0710
  projects/forge/10-intent.md#POS.0720
  projects/forge/10-intent.md#POS.0730
  projects/forge/10-intent.md#POS.0590
  projects/forge/10-intent.md#POS.0770
  projects/forge/10-intent.md#POS.0810
  projects/forge/10-intent.md#POS.1000
  projects/forge/10-intent.md#POS.1550
  projects/forge/10-intent.md#REJ.0160
  projects/forge/10-intent.md#REJ.0240
- links:
  `docs/use/compose-a-recipe.md`: composing a recipe.
  `docs/use/render-an-output.md`: generating a render.
  `docs/use/publish-a-designed-file.md`: the designed file.
  `docs/about/the-screenplay-and-its-player.md`: the screenplay, its two formats and where a public one lands.
  `docs/about/the-work-product.md`: the output that is not a render.
  `docs/reference/render-provenance.md`: the provenance block and the definition of stale.
  `docs/about/the-documentation.md`: the pages, generated without a recipe.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no recipe of the forge project quoted; no author line; no pitch content; no script options; not the readme skeleton's fixed closing sentence; no version on a branch in a provenance, which is not built.
- made: derived
- evidence: CLAUDE.md, Document chain (Renders) gives the mechanism, the languages, the published table and the three conversions; the recipe skeleton the sections; the readme skeleton's Instructions what a README carries; the positions the reasons, POS.1550 the languages and POS.0590 the two steps; the two REJ what was rejected.
- state: keep

### docs/about/the-screenplay-and-its-player.md
- title: The screenplay and its player
- line: What is a teaching video of the forge made of, why does one script make both of its formats, and why does the engine host the public files?
- kind: explanation
- reader: user, extender, evaluator
- says: A concept page: a recipe of the genre `screenplay` renders a screenplay of a terminal conversation cut from session records: a title card that discloses the composition, a card of what the viewer will see, scenes with the real time of day, each with a caption of two parts (what happens now, why the forge does it this way) and a fenced block of what the terminal shows, and an end card; the caption is the teaching, the terminal the evidence. Its inputs are session records registered as sources and the brief of the videos; a recipe may render in several languages, the translations cut scene for scene from the primary. Its Format names one of two formats: `video`, an MP4 painted frame by frame as a simulated terminal, or `html-player`, the timed events for the player page of the engine; both made by one script, deterministic, no model in it, the plain file of `/render`, no designed step and no published file; the pace of reading and the look stand in the recipe's Format section and reach the script as arguments, never in the render. The player page is one fixed file of the engine, a single file with no dependency beyond the browser: a sidebar of the videos by title, the simulated terminal with its caption band and cards, play and pause, speed, the scenes as chapters, the language where a video has siblings, three font sizes; it is written anew from its skeleton by the script, never by hand and never by a model. Why the engine hosts what a project shows in public: the engine, public and served by GitHub Pages from `docs/`, is the one public place of an instance, while the project that made the file stays private; the engine carries the file only, the recipe, render, provenance and history stay in the project; what goes out is chosen in the recipe, video by video, and read by the principal before the engine is saved; the folder is flat, in the order of file names, foreign to the documentation and its checks; video files never enter the tree. The choices and their price as the solution design records them. One worked example: a generic scene of a screenplay.
- inputs:
  projects/forge/10-intent.md#POS.1530
  projects/forge/10-intent.md#POS.1540
  projects/forge/10-intent.md#POS.1550
  projects/forge/40-solution-design.md#SOL.0650
  projects/forge/40-solution-design.md#SOL.0660
  .claude/skills/recipe/genres/screenplay.md
  templates/html-player.html
- links:
  `docs/use/make-a-video-from-a-recipe.md`: the job from the recipe to the played file.
  `docs/about/renders-and-recipes.md`: the render and its recipe, which a screenplay is one of.
  `docs/about/projects-and-the-engine.md`: why the engine is public and a project is a repository of its own.
  `docs/reference/scripts.md`: the script that makes both formats.
  `docs/reference/recipe-genres.md`: the genre's checklist in full.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no video, recipe or project of an instance named; no course address; no name of a person; no sections or order of a course beyond "in the order of file names" (open); nothing of the page's styles or code; no research or trial of a project named.
- made: derived
- evidence: POS.1530 gives the screenplay, the two formats and the one script with its reason; POS.1540 the engine as the public host, what goes out, the clearing, the flat folder and the player page; POS.1550 the languages; SOL.0650 the script's choices and their price; SOL.0660 what the page does, that the script renews its list, that the documentation leaves the folder alone, and the choice of the alphabet of file names; the genre file the product and the inputs; the skeleton's head comment that the page is written from it by the script and never edited.
- state: keep

### docs/about/the-documentation.md
- title: The documentation
- line: What is the documentation, who reads it, and why is it generated rather than written?
- kind: explanation
- reader: user, extender, evaluator
- says: The documentation of a project is a set of pages of one topic each in `docs/`, with an index that names each reader's path. Three readers in order of weight. Five sections by the reader's journey, filled only where the project has material; each page of one kind (how-to, explanation, reference), the kind saying what content belongs on it; one rule has one home page; every page is reached from another page. Generated and never composed by hand: a page mirrors the files that own its topic or is derived from named evidence; the map lies beside the owning project's ledger, carries only its target and owner in its header, and is never shown to the reader; the previous map is taken from git. Two agents make it under one contract, a planner and a writer per page; a run regenerates only pages whose inputs changed, an input hashed as the named part of a file, the rule the pages are made by hashed with them; a run is made on `main` only; a release reports the index's age and offers the command. The public folder of the videos under `docs/` is not the documentation's. Why: the README was the whole documentation and poor as one; why not a recipe per page, a site, a hand-kept philosophy. The diagram: one documentation run. One worked example: a generic entry of the map.
- inputs:
  CLAUDE.md#Document chain
  .claude/skills/document/SKILL.md
  .claude/skills/docs-contract/SKILL.md
  .claude/agents/docs-planner.md
  .claude/agents/docs-writer.md
  templates/docs-map.md
  projects/forge/10-intent.md#POS.1450
  projects/forge/10-intent.md#POS.0930
  projects/forge/10-intent.md#REJ.0240
  projects/forge/10-intent.md#REJ.0250
  projects/forge/10-intent.md#REJ.0260
  projects/forge/40-solution-design.md#SOL.0460
- links:
  `docs/use/generate-the-documentation.md`: running `/document`.
  `docs/extend/change-a-documentation-page.md`: changing a page through its owners.
  `docs/reference/documentation-map.md`: the map's entry and the page's front-matter, field by field.
  `docs/about/renders-and-recipes.md`: the renders, which the pages are not.
  `docs/about/the-screenplay-and-its-player.md`: the videos folder under `docs/` that the documentation leaves alone.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no count of pages or date of a run; no model name; no entry of the engine's map quoted; no name of a project other than `forge`; nothing of the contract as an instruction to Claude; no list of pages the design says are to be regenerated after a release.
- made: derived
- evidence: CLAUDE.md, Document chain (Documentation) gives what the documentation is and where the map lies; the `/document` skill the one run, the main-only rule and the previous map from git; the contract what the two agents share and the kinds of a page; the planner the readers, the outline and the videos folder left alone; the writer the page's shape; the map's skeleton its header; POS.1450 the position whole with its reason, POS.0930 the faster model for a mirrored page; the three REJ what was rejected; SOL.0460 the choices and the parts of a run the diagram draws. Where no input gives a reason, the page says the reason is not recorded.
- state: keep

### docs/about/sources-and-research.md
- title: Sources and research
- line: Why are sources immutable, why is registration not intake, and what is a research note for?
- kind: explanation
- reader: user, evaluator
- says: External inputs live in `sources/`, immutable once registered, one form each; a related set is a bundle. Registration is not intake: what a source is for is the principal's word, asked before its index entry is written so that the entry carries it from its birth, its Role in the index; source content enters the intent only by his explicit act with provenance. Research is a durable answer to one question, immutable and dated. Every `sources/` and `research/` directory carries an index that tracks nothing and is an automatic input of no command; a source's date, origin and form are fields of its entry. Why personal matter stops an ingest before the store. One worked example: a generic index entry.
- inputs:
  CLAUDE.md#Document chain
  templates/index.md
  templates/index-bundle.md
  projects/forge/10-intent.md#POS.0050
  projects/forge/10-intent.md#POS.0180
  projects/forge/10-intent.md#POS.0840
  projects/forge/10-intent.md#POS.1040
- links:
  `docs/use/register-a-source.md`: the ingest procedure.
  `docs/use/research-a-topic.md`: the research procedure.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no source of the forge project; no index entry reproduced; no merge driver of the index, which is not built.
- made: derived
- evidence: CLAUDE.md gives the rules; the skeletons the fields; the positions the reasons. Where no input gives a reason, the page says the reason is not recorded.
- state: keep

### docs/about/projects-and-the-engine.md
- title: Projects and the engine
- line: Why is every project a repository of its own that the engine does not know?
- kind: explanation
- reader: user, extender, evaluator
- says: The engine is one public repository, the core together with its own project `projects/forge`; every other project is a repository of its own under a gitignored `projects/`, recognised by its `.git`; any remote and visibility, or none. Why: publication with nothing sensitive, access per project, seamless work inside. A project has a project file, written once at its creation, that declares its slug, its kind (thought or library) and the language of its artefacts; a library is shared material cited by path as a dependency taken knowingly. Instance facts live in `CLAUDE.local.md`; the forge's behaviour lives in the engine, never in the assistant's memory. A project records no engine version, said in one sentence with a link. The engine is the one public place of an instance: what a project shows in public goes out as a file into the engine, said in one sentence with a link. The shapes rejected. The diagram: the engine root with its own project and the nested project repositories. One worked example, generic.
- inputs:
  CLAUDE.md#Repository layout
  CLAUDE.md#Persistence (git)
  templates/project.md
  projects/forge/10-intent.md#POS.0760
  projects/forge/10-intent.md#POS.0940
  projects/forge/10-intent.md#POS.0950
  projects/forge/10-intent.md#POS.0960
  projects/forge/10-intent.md#POS.1590
  projects/forge/10-intent.md#POS.0970
  projects/forge/10-intent.md#POS.1020
  projects/forge/10-intent.md#POS.1030
  projects/forge/10-intent.md#POS.1540
  projects/forge/10-intent.md#REJ.0140
  projects/forge/10-intent.md#REJ.0150
  projects/forge/40-solution-design.md#SOL.0500
- links:
  `docs/use/share-material-through-a-library.md`: using a library.
  `docs/about/upgrades-and-migration.md`: why a project records no engine version and how it follows the engine.
  `docs/about/the-screenplay-and-its-player.md`: the public files a project sends into the engine.
  `docs/reference/repository-layout.md`: the layout, file by file.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no host, company or project name other than `forge`; no repository address; no history of the split as a story; no fixture project; no second working tree of the engine, which is not built.
- made: derived
- evidence: CLAUDE.md gives the shape; the project file skeleton its fields; the positions the reasons, POS.1590 why the project file exists, POS.1540 the engine as the public place in one sentence; the two REJ what was rejected; SOL.0500 the gitignore pattern and the parts the diagram draws.
- state: keep

### docs/about/persistence-in-git.md
- title: Persistence in git
- line: Why are the scripts the only door to git, and why two doors, two speeds?
- kind: explanation
- reader: user, extender, evaluator
- says: The scripts in `scripts/` are the only door to git, reading state included, for Claude a wall of the harness. Two doors, two speeds: `/save` with the light check, on any branch; `/release` from `main` only with its checks, the README and release notes, the release message and the major's tag. `/pull` is the door inward: the forge looks at the remote, pulls only a clean repository that is behind, and never merges on its own. `main` is the released line, branches voluntary, merging git's. The files made for a reader (the renders, the README, the release notes, the documentation, the published companions) are made only on `main` and are taken as `ours` at a merge, a published file being binary; so a release, a documentation run and a publish refuse a repository behind or diverged, since the rebase of a save would otherwise let an older file win. Neither way is built into git: `/setup` registers them once per machine and the status script says when the registration is missing, since an unregistered clone silently falls back to a conflict. The ledger is not in git at all. The commit identity is git's, resolved per host, with a guard. Immutability is a process rule. The scripts are Python, `python` on PATH their one prerequisite, written to run unchanged on Linux and macOS as a writing rule, not a verified claim. One worked example, generic.
- inputs:
  CLAUDE.md#Persistence (git)
  templates/gitattributes
  projects/forge/10-intent.md#POS.0550
  projects/forge/10-intent.md#POS.0830
  projects/forge/10-intent.md#POS.0950
  projects/forge/10-intent.md#POS.1100
  projects/forge/10-intent.md#POS.1200
  projects/forge/10-intent.md#POS.1490
  projects/forge/10-intent.md#POS.1710
  projects/forge/40-solution-design.md#SOL.0730
  projects/forge/10-intent.md#REJ.0160
  projects/forge/10-intent.md#REJ.0170
- links:
  `docs/use/save-your-work.md`: the save.
  `docs/use/release-a-version.md`: the release.
  `docs/use/pull-from-the-remote.md`: the pull.
  `docs/use/work-on-a-branch.md`: branches.
  `docs/about/the-ledger.md`: why the ledger is made at read time and kept out of git.
  `docs/reference/scripts.md`: the scripts themselves.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no host, identity example or incident story; no git command; no mention of PowerShell; no driver of the forge's own for record files, no `/merge`, no worktree, no landing of branch records, no blocks of IDs, which are not built; no project named at whose merges a reason was found.
- made: derived
- evidence: CLAUDE.md, Persistence gives the rules, the registration and the migration door; the attributes template which files are taken as `ours` and which are binary; SOL.0730 that `ours` and `binary` are built and the record driver deferred; POS.1710 why derived files are made on main and the refusals; the other positions the reasons; the two REJ what was rejected. Where no input gives a reason, the page says the reason is not recorded.
- state: keep

### docs/about/upgrades-and-migration.md
- title: Upgrades and migration
- line: How does a project follow a new release of the engine, and why does a change of the shape of files come with a migration?
- kind: explanation
- reader: user, extender, evaluator
- says: A concept page. What it is: an upgrade is a fast-forward pull of the engine; a project records no engine version, and the checks measure it against the current conventions; the release notes say in Action required what to do. Artefacts do not expire with the conventions: a finished or dormant project that no longer conforms is a fact to report, never a defect to chase, and bringing it current is the principal's decision per project. How it works: an upgrade of a few lines is brought in by Claude on the user's word after the checks have named it; a release that changes the shape of files comes with a migration, one command with a script for every deterministic step and Claude for what needs judgement. The script recognises a project's shape as a set of marks, one per step, never by an engine version, and runs only the steps missing; it commits nothing and can be undone before the save. A migration runs once per project, on one clone, on `main`, and everyone else pulls; until a project is migrated nothing writes into it, since the engine cannot write two shapes. Why: an upgrade that rewrites files of every project, in every clone, must come out the same everywhere, which a hand migration cannot promise; an engine version in the project would be one more thing to keep. One worked example: a generic project going from the old shape to the new.
- inputs:
  projects/forge/10-intent.md#POS.0940
  projects/forge/10-intent.md#POS.0820
  projects/forge/10-intent.md#POS.1740
  CLAUDE.md#Persistence (git)
  templates/project.md
  scripts/forge-migrate.py
- links:
  `docs/use/upgrade-the-engine.md`: the steps after a pull of the engine.
  `docs/use/migrate-a-project.md`: running `/migrate`.
  `docs/about/projects-and-the-engine.md`: why the engine does not know the projects.
  `docs/about/the-ledger.md`: what the first migration made of the hand-kept ledger.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no version numbers or names of releases; no conversion to one sentence per line, no refusal over unmerged branches, which are not built; no git command for the way back; no project other than `forge` named.
- made: derived
- evidence: POS.0940 the upgrade path and the narrowing to a migration for a shape change; POS.0820 that artefacts do not expire and that a project of the old shape is read, not written; POS.1740 the one command, the marks, once per project on one clone and the reason; CLAUDE.md, Persistence the migration door as the operating layer says it; the project file skeleton what a project without the file is; the script's header the marks, the dry run, `--apply`, `--undo` and the refusals.
- state: keep

### docs/about/how-the-rules-are-held.md
- title: How the rules are held
- line: How does the forge keep its rules in force across a long conversation and inside a subagent?
- kind: explanation
- reader: extender, evaluator
- says: One always-on core, `CLAUDE.md`, loaded into every session and subagent; everything else a file read when its situation arises. One mechanism lives in one place and is cited by path everywhere else. A rule that must hold through a long conversation is repeated at every prompt by a hook; what the hook prints. The harness enforces what it can: deny rules keep Claude from raw git and sensitive paths; a command that changes files the moment it runs is guarded against being started on Claude's own judgement. A subagent may take the session's copy of a file for the file on disk, so every agent that writes an outward-facing file reads its inputs from disk, and generated files are scanned mechanically. One model for the whole forge. The forge's behaviour never lives in the assistant's memory. The forge explains itself through `/man`. One worked example, generic.
- inputs:
  CLAUDE.md#Prime directives
  CLAUDE.md#Working methods
  .claude/settings.json
  scripts/hook-walkthrough.py
  projects/forge/10-intent.md#POS.0930
  projects/forge/10-intent.md#POS.0950
  projects/forge/10-intent.md#POS.1030
  projects/forge/10-intent.md#POS.1070
  projects/forge/10-intent.md#POS.1090
  projects/forge/10-intent.md#POS.1170
  projects/forge/10-intent.md#POS.1190
  projects/forge/10-intent.md#POS.1200
  projects/forge/40-solution-design.md#The instruction layer
- links:
  `docs/extend/what-it-is-made-of.md`: the files of the operating layer.
  `docs/reference/configuration.md`: the settings, exactly.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no claim that a hook or a deny rule guarantees behaviour; no incident story or date; no thread of the forge project; nothing of the hook's docstring beyond what it prints.
- made: derived
- evidence: prime directive 10 and the Walkthrough method give the one-place rule and the hook; the settings the deny rules; the hook's `LINES` what it prints; the positions the reasons; the design's group how the core, the instance file, the hook and the walkthrough skill are realised.
- state: keep

### docs/about/languages.md
- title: Languages
- line: Which language does each kind of document carry, and why only one output language per project?
- kind: explanation
- reader: user, evaluator
- says: The forge dictates one output language per project: the artefacts in the language the project file declares, English when absent; records, state, research and recipes always English; English the notation throughout; the briefs the one exception; a work specification follows the artefacts and its file the language its Making section says; a render in any language, or languages, its recipe declares, the first primary and the rest its translations, said in one sentence with a link; the documentation English only. The conversation language is an instance fact, never shown outward. Translate on write. One worked example, generic.
- inputs:
  CLAUDE.md#Prime directives
  projects/forge/10-intent.md#POS.0060
  projects/forge/10-intent.md#POS.1450
- links:
  `docs/start/setup.md`: where the conversation language is set.
  `docs/about/renders-and-recipes.md`: a recipe in several languages.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no language value of an instance; no example project; nothing of the prime directives but directive 6; nothing of POS.1450 but the documentation's language.
- made: derived
- evidence: prime directive 6 gives the rule, the project file as its source, the work specification and the languages of a render; POS.0060 the reason; POS.1450 that the documentation is English only. Where no input gives a reason, the page says the reason is not recorded.
- state: keep

### docs/about/where-it-is-going.md
- title: Where the forge is going
- line: In which direction is the forge developed, and what is deliberately not promised?
- kind: explanation
- reader: user, extender, evaluator
- says: Direction without destination: the chain is to be extended downward as far as the principal needs a thought taken, a BRD layer certain, a strategy layer possible; nothing approved for construction. A new kind of artefact is added by one command; a user is to be able to add one of his own at his own place, which is open. Independent challengers on another model family are planned. One principal per instance for now. Developed at its owner's discretion and pace; feedback and ideas are wanted most.
- inputs:
  projects/forge/10-intent.md#POS.0700
  projects/forge/10-intent.md#POS.0780
  projects/forge/10-intent.md#POS.0800
  projects/forge/10-intent.md#POS.1430
  projects/forge/10-intent.md#POS.1440
- links:
  `docs/about/the-document-chain.md`: how a layer is added.
  `docs/extend/how-a-change-is-made.md`: how a change reaches the forge.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no thread quoted; no date; no version; no company rollout; no name; no vendor or product of the planned challengers.
- made: derived
- evidence: positions only. Where no input gives a reason, the page says the reason is not recorded.
- state: keep

## extend

### docs/extend/what-it-is-made-of.md
- title: What the forge is made of
- line: Which files make up the operating layer, what is each, and when is it loaded?
- kind: how-to
- reader: extender
- says: Opens with a table (path, what it is, loaded when): `CLAUDE.md`, the always-on core; `.claude/skills/<name>/SKILL.md`, one per command, with the `/forge` state files and the `/recipe` genre files as supporting files, and the skills that are not commands (the three reviewer contracts, the documentation contract, the walkthrough skill); `.claude/agents/`, one file per lens, persona and check, and the documentation's planner and writer; `.claude/settings.json`; `templates/`, the skeletons, the player page's skeleton among them; `scripts/`, Python with the shared modules beside them; `.gitattributes`, the engine's own ways of merging its derived files; `projects/forge`, the forge's own project; `docs/`, the generated documentation, with `docs/videos/` the public folder of the videos, not the documentation's. Then one line of flow. Then the ideas that carry it. One worked example: one command traced through the layer.
- inputs:
  CLAUDE.md#Repository layout
  CLAUDE.md#Templates
  CLAUDE.md#Persistence (git)
  projects/forge/40-solution-design.md#How the parts work together
  projects/forge/40-solution-design.md#The instruction layer
  projects/forge/40-solution-design.md#The commands
  projects/forge/40-solution-design.md#SOL.0300
  projects/forge/40-solution-design.md#SOL.0330
  projects/forge/40-solution-design.md#Across the parts
- links:
  `docs/reference/repository-layout.md`: the layout block.
  `docs/reference/templates.md`: every skeleton.
  `docs/about/how-the-rules-are-held.md`: why the core is small and the rest on demand.
  `docs/extend/how-a-change-is-made.md`: changing any of it.
  `docs/about/the-documentation.md`: what `docs/` and the map are.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no listing of individual commands or agents; no file of an instance; no repository address; no count of pages or date of a run; no script, command or template the design names that does not exist on disk (the record driver, the landing script, the merge command, the fixture script, the ID reservations).
- made: derived
- evidence: CLAUDE.md, Repository layout and Templates give the directories and the `<type>-definition.md` rule; Persistence the shared modules; the design's head the ideas and its groups what each kind of file is and when the harness loads it; SOL.0300 and SOL.0330 the reviewer files. The table and the line of flow are the writer's join.
- state: keep

### docs/extend/how-a-change-is-made.md
- title: Make a change to the forge
- line: How is a change of the forge's behaviour made, proved, recorded and released?
- kind: how-to
- reader: extender
- says: A change of how the forge behaves goes through the chain before it is built: a position in the forge intent through `/forge intent forge`; the item of the solution design through `/forge solution-design forge`; then the operating layer. Proved by `/check engine` and, before a major or after a round on the operating layer, `/check single-source-of-truth`; recorded in the history companions; released by `/release forge`; a process change is complete only once the intent is updated and the README re-rendered. A change that alters no behaviour is made directly. The README, the release notes and CONTRIBUTING are renders: a change goes into their recipes. A visitor's way to send feedback, an idea or a change is `CONTRIBUTING.md`, the channels by kind, a pull request carrying the position, the item, the change and one line on what was run; in a clone the user decides everything, what is merged into the public engine its author decides. One worked example: one invented change traced through.
- inputs:
  CLAUDE.md#The system's own project
  CLAUDE.md#Versioning & status
  projects/forge/10-intent.md#POS.0720
  projects/forge/10-intent.md#POS.0900
  projects/forge/10-intent.md#POS.1440
  .claude/agents/check-engine.md
  .claude/agents/check-single-source-of-truth.md
  .claude/skills/release/SKILL.md
  projects/forge/recipes/contributing.md#Instructions
- links:
  `docs/use/forge-the-intent.md`: iterating an intent.
  `docs/use/check-conformance.md`: running the checks.
  `docs/use/release-a-version.md`: the release.
  `docs/use/generate-the-documentation.md`: regenerating the pages.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no channel URL, account, profile or name; no pull-request mechanics beyond what the recipe gives; no claim that the release regenerates the documentation on its own.
- made: derived
- evidence: CLAUDE.md gives the completeness rule and the `operating layer` subject; the positions intent-first and the open rule; the contributing recipe's Instructions the line between the two kinds of change, who decides what and the channels by kind; the two check agents what proves a change; the release skill what a release re-renders.
- state: keep

### docs/extend/add-an-artefact.md
- title: Add an artefact
- line: How is a new kind of artefact added to the chain with `/new-artefact`?
- kind: how-to
- reader: extender
- says: An add page: `/new-artefact <name>` leads to everything a kind needs and decides nothing: a position in the forge intent first; the definition in the seven blocks from `templates/artefact-definition.md` and its template `templates/<name>.md`; the row of a new prefix; the reviewers; the item of the solution design. The rosters need nothing: `/forge`, `/man` and the README read the definitions from disk. Prove it: `/check engine`; the first artefact of the kind through `/forge <name>` on real work is the trial. Recorded and released as any change. One worked example with `<name>`.
- inputs:
  .claude/skills/new-artefact/SKILL.md
  templates/artefact-definition.md
- links:
  `docs/extend/how-a-change-is-made.md`: proving, recording and releasing the change.
  `docs/about/elicitation.md`: the seven blocks and the Map.
  `docs/about/where-it-is-going.md`: the layers the forge's owner intends to add.
  `docs/extend/add-a-challenger-persona.md`: the persona a kind may need.
  `docs/reference/templates.md`: the skeletons a definition and a persona start from.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no planned artefact named as if being added; no brief of the forge project.
- made: mirrored
- state: keep

### docs/extend/add-a-critic-lens.md
- title: Add a critic lens
- line: How is a new critic lens added as one agent file?
- kind: how-to
- reader: extender
- says: An add page: a lens is one agent file `.claude/agents/critic-<lens>.md` from `templates/critic-definition.md`: front-matter (name, description, tools, `model: inherit`, `skills: critic-contract`) and a Lens section in four parts. Nothing the contract owns is restated. The description is the roster line; a description carrying a colon followed by a space is quoted whole or the agent does not register. Only by the principal's decision and only where what it finds genuinely differs. Prove it: `/check engine`; a run on a project. Recorded and released as any change. One worked example with `<lens>`.
- inputs:
  templates/critic-definition.md
  .claude/skills/critic-contract/SKILL.md
  .claude/skills/critique/SKILL.md
  CLAUDE.md#Isolated reviewers
- links:
  `docs/extend/how-a-change-is-made.md`: proving, recording and releasing the change.
  `docs/about/the-critic.md`: what the contract owns.
  `docs/reference/critic-lenses.md`: the lenses that exist.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no contract text copied; no existing lens's angles copied as content.
- made: mirrored
- state: keep

### docs/extend/add-a-challenger-persona.md
- title: Add a challenger persona
- line: How is a new challenger persona added as one agent file?
- kind: how-to
- reader: extender
- says: An add page: a persona is one agent file `.claude/agents/challenger-<persona>.md` from `templates/challenger-definition.md`: front-matter (name, description, tools including web search, `model: inherit`, `skills: challenger-contract`) and a Lens section in two parts. Nothing of the contract restated. Only by the principal's decision. A persona costs one file and no edits: the roster is scanned. Prove it: `/check engine`; a run on a target. Recorded and released as any change. One worked example with `<persona>`.
- inputs:
  templates/challenger-definition.md
  .claude/skills/challenger-contract/SKILL.md
  .claude/skills/challenge/SKILL.md
  CLAUDE.md#Isolated reviewers
- links:
  `docs/extend/how-a-change-is-made.md`: proving, recording and releasing the change.
  `docs/about/the-challenger.md`: what the contract owns.
  `docs/reference/challenger-personas.md`: the personas that exist.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no contract text copied; no existing persona's angles copied as content.
- made: mirrored
- state: keep

### docs/extend/add-a-check.md
- title: Add a check
- line: How is a new check added as one agent file?
- kind: how-to
- reader: extender
- says: An add page: a check is one agent file `.claude/agents/check-<name>.md` from `templates/check-definition.md`: front-matter (name, description with when it fits, read-only tools, `model: inherit`, `skills: check-contract`) and a Lens section in three parts. One concern per check. It writes nothing: the `/check` procedure files its report. Whether a save or a release runs it is the caller's definition to say. Prove it: `/check engine`; a run on a project. Recorded and released as any change. One worked example with `<name>`.
- inputs:
  templates/check-definition.md
  .claude/skills/check-contract/SKILL.md
  .claude/skills/check/SKILL.md
  CLAUDE.md#Isolated reviewers
- links:
  `docs/extend/how-a-change-is-made.md`: proving, recording and releasing the change.
  `docs/about/the-check.md`: what the contract owns.
  `docs/reference/checks.md`: the checks that exist.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no contract text copied; no existing check's clauses copied as content.
- made: mirrored
- state: keep

### docs/extend/add-a-recipe-genre.md
- title: Add a recipe genre
- line: How is a new genre of `/recipe` added as two files?
- kind: how-to
- reader: extender
- says: An add page: a genre is two files: `.claude/skills/recipe/genres/<genre>.md`, a definition with a one-line description, the skeleton and output, a role and a numbered elicitation checklist, and `templates/recipe-<genre>.md`, the skeleton that extends the base recipe shape, with a `## Format` section where the render has a file beside it and `languages:` where the genre allows translations. Every genre runs in the same frame: the checklist closes with the language question and the recipe is composed from the skeleton. The dispatcher never changes; bare `/recipe` and `/man recipe` scan the directory. Prove it: `/check engine`; a composition on a project. Recorded and released as any change. One worked example with `<genre>`.
- inputs:
  .claude/skills/recipe/SKILL.md
  .claude/skills/recipe/genres/presentation.md
  templates/recipe.md
  templates/recipe-presentation.md
- links:
  `docs/extend/how-a-change-is-made.md`: proving, recording and releasing the change.
  `docs/reference/recipe-genres.md`: the genres that exist.
  `docs/about/renders-and-recipes.md`: what a recipe is.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no checklist copied as content; no genre named as planned.
- made: derived
- evidence: the `/recipe` skill says a genre is two files, that the dispatcher never changes and gives the shared frame with the language question; the presentation genre file and its skeleton are the model of the two shapes; `templates/recipe.md` owns the base shape, `languages:` among it.
- state: keep

### docs/extend/add-a-command.md
- title: Add a command
- line: How is a new command added as a skill, and when is it guarded?
- kind: how-to
- reader: extender
- says: An add page: a command is a skill `.claude/skills/<name>/SKILL.md`: front-matter with `description`, a quoted `argument-hint`, and `disable-model-invocation: true` where the command changes files the moment it runs, so that Claude cannot start it on its own judgement; a body that says what the command does and cites every mechanism of another by path; supporting files beside it where it dispatches over a roster. A row in the Commands table of `CLAUDE.md`. Named so that it does not collide with a built-in of Claude Code. Prove it: `/check engine`; `/check single-source-of-truth`. Recorded and released as any change. One worked example with `<name>`.
- inputs:
  CLAUDE.md#Commands
  .claude/skills/ledger/SKILL.md
  .claude/skills/end/SKILL.md
  .claude/agents/check-engine.md
  projects/forge/10-intent.md#POS.1090
  projects/forge/10-intent.md#POS.1070
  projects/forge/10-intent.md#POS.1050
  projects/forge/10-intent.md#POS.1190
  projects/forge/40-solution-design.md#SOL.0100
  projects/forge/40-solution-design.md#SOL.0110
- links:
  `docs/extend/how-a-change-is-made.md`: the chain the change goes through.
  `docs/reference/commands.md`: the commands that exist.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no skill body copied; no harness detail beyond what the solution design states.
- made: derived
- evidence: SOL.0100 and SOL.0110 give the skill shape, the quoted hint and the guard; POS.1090 the criterion of a guarded command; POS.1070 citation over restatement; CLAUDE.md, Commands the table; the `ledger` and `end` skills the smallest models; the `check-engine` agent that the table is verified against the skills; POS.1050 and POS.1190 the naming rule.
- state: keep

### docs/extend/add-a-script.md
- title: Add a script
- line: How is a new script written so that it is portable, documented in its docstring and the one owner of its facts?
- kind: how-to
- reader: extender
- says: An add page: a script is Python 3.8 or newer, run as `python scripts/<name>.py`, with its help in its module docstring: synopsis, what it does, what it needs, options, where the output lands, examples; the docstring owns those facts and commands cite it. Rules: nothing Windows-only, `pathlib`, `subprocess` with argument lists, external tools resolved from PATH and never installed, colour only on a terminal, examples free of platform paths, no URL and no identity. What several scripts share lives in one module beside them: `forge_repos.py`, `forge_tools.py`, `forge_docs.py`, `docs_map.py`. Named in the layout comment of `CLAUDE.md`. Prove it: `/check engine`. Recorded and released as any change. One worked example: a generic docstring.
- inputs:
  CLAUDE.md#Persistence (git)
  CLAUDE.md#Repository layout
  scripts/forge-status.py
  scripts/forge_repos.py
  .claude/agents/check-engine.md
  projects/forge/10-intent.md#POS.0830
  projects/forge/40-solution-design.md#SOL.0620
- links:
  `docs/extend/how-a-change-is-made.md`: proving, recording and releasing the change.
  `docs/reference/scripts.md`: the scripts that exist.
  `docs/about/persistence-in-git.md`: why the scripts are the only door.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no claim that the set has been run on Linux or macOS; no instance path; no mention of PowerShell; no script body; nothing of SOL.0620 beyond how the scripts are written and what they share.
- made: derived
- evidence: CLAUDE.md gives the writing rules, the four shared modules and the layout comment; POS.0830 the reason; SOL.0620 how the scripts are written; `forge-status.py` the smallest model of a docstring, `forge_repos.py` of a shared module; the `check-engine` agent that scripts on disk are verified against the layout comment.
- state: keep

### docs/extend/change-a-documentation-page.md
- title: Change a documentation page
- line: How do you change what a page says, which pages exist, or what the check refuses, without editing a page?
- kind: how-to
- reader: extender
- says: A page is never edited by hand; what is wrong is mended in the file that owns the matter and the page regenerated. Finding the owner: the page's front-matter lists its inputs. To change what a page says: change the owning file and run `/document`, which remakes only the pages whose inputs, entry or generating rule changed. To change the shape every page has, or what kind of content a page of each kind carries: the writer's definition and the documentation contract are hashed with the inputs. To change which pages exist or who reads it: the map is written by the planner from the target at every run, the readers and the outline are the planner's definition and a position of the forge intent. A fact a page needs and no file owns is reported under Unowned; the readme skeleton's "Pinned facts (not rendered)" is that home. What the check refuses. An agent's definition is loaded once per session. One worked example: one invented fix traced through.
- inputs:
  .claude/skills/document/SKILL.md
  .claude/skills/docs-contract/SKILL.md
  .claude/agents/docs-planner.md
  .claude/agents/docs-writer.md
  scripts/docs-state.py
  scripts/docs-check.py
  templates/recipe-readme.md#Pinned facts (not rendered)
- links:
  `docs/use/generate-the-documentation.md`: running the command.
  `docs/reference/documentation-map.md`: the fields of an entry and of a page's front-matter.
  `docs/extend/how-a-change-is-made.md`: the chain a change of the forge goes through.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no model name; no agent text as an instruction to Claude; no address; no page named as an example that may not exist; no instance fact; nothing of the check script's `--file` mode.
- made: derived
- evidence: the `/document` skill gives "mended in the file that owns the matter", the state computed from the inputs, the twice-failing page and the harness note; the contract what must never reach a page and the kinds of a page; the writer the page's front-matter; the planner that the map is written from the target at every run and Unowned; the state script's docstring the parts and the generator hashed; the check script's docstring what it looks for; the readme skeleton's comment the home of pinned facts.
- state: keep

## reference

### docs/reference/commands.md
- title: Commands
- line: Every command with its signature, purpose, arguments and whether it is guarded.
- kind: reference
- reader: user, extender, evaluator
- says: A roster page: one overview table first (command, purpose, arguments, guarded or not), then one entry per command in the order of the Commands table of `CLAUDE.md`: the row's signature and purpose, the skill's `description` and `argument-hint`, and whether it carries `disable-model-invocation: true`; `/work`, `/pull`, `/end`, `/history`, `/migrate`, `/man` and `/manual` included.
- inputs:
  CLAUDE.md#Commands
  .claude/skills/setup/SKILL.md
  .claude/skills/new-project/SKILL.md
  .claude/skills/new-artefact/SKILL.md
  .claude/skills/import-project/SKILL.md
  .claude/skills/forge/SKILL.md
  .claude/skills/ingest/SKILL.md
  .claude/skills/render/SKILL.md
  .claude/skills/publish/SKILL.md
  .claude/skills/document/SKILL.md
  .claude/skills/recipe/SKILL.md
  .claude/skills/work/SKILL.md
  .claude/skills/critique/SKILL.md
  .claude/skills/challenge/SKILL.md
  .claude/skills/research/SKILL.md
  .claude/skills/ledger/SKILL.md
  .claude/skills/history/SKILL.md
  .claude/skills/check/SKILL.md
  .claude/skills/save/SKILL.md
  .claude/skills/release/SKILL.md
  .claude/skills/pull/SKILL.md
  .claude/skills/end/SKILL.md
  .claude/skills/spinoff/SKILL.md
  .claude/skills/migrate/SKILL.md
  .claude/skills/man/SKILL.md
  .claude/skills/manual/SKILL.md
- links:
  `docs/use/look-up-a-command.md`: the same, printed in the session by `/man`.
  `docs/extend/add-a-command.md`: adding a command of one's own.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no procedure of any command; no explanation.
- made: mirrored
- state: keep

### docs/reference/artefacts.md
- title: Artefacts
- line: The artefacts of today's chain, one row per definition, with template, inputs, prefixes and command.
- kind: reference
- reader: user, extender, evaluator
- says: A roster page: one overview table first, then one row per definition in `.claude/skills/forge/states/` in the order of the file numbers: the artefact's file, its `description`, its template, its inputs (Target and Inputs blocks), the prefixes of its items, and the command that works it. One line below: a layer a project does not have is not missing.
- inputs:
  .claude/skills/forge/states/brief.md
  .claude/skills/forge/states/intent.md
  .claude/skills/forge/states/assignment.md
  .claude/skills/forge/states/solution-design.md
  CLAUDE.md#ID scheme
  CLAUDE.md#Ledger
- links:
  `docs/about/the-document-chain.md`: why the listing of that directory is the one list.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no Aim, Partner, Map or Course text; no explanation.
- made: mirrored
- state: keep

### docs/reference/critic-lenses.md
- title: Critic lenses
- line: The critic lenses of today and what each reads and goes after.
- kind: reference
- reader: user, extender
- says: A roster page: one overview table first (name, what it is for, when it fits, where it lives), then one entry per `.claude/agents/critic-*.md`: the lens name, its `description`, and its Lens section, as `/man critique` prints them.
- inputs:
  .claude/agents/critic-clarity.md
  .claude/agents/critic-essence.md
- links:
  `docs/use/critique-the-documents.md`: running a lens.
  `docs/extend/add-a-critic-lens.md`: adding a lens.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no contract text; no explanation.
- made: mirrored
- state: keep

### docs/reference/challenger-personas.md
- title: Challenger personas
- line: The challenger personas of today and what each hunts.
- kind: reference
- reader: user, extender
- says: A roster page: one overview table first, then one entry per `.claude/agents/challenger-*.md`: the persona name, its `description`, and its Lens section, as `/man challenge` prints them.
- inputs:
  .claude/agents/challenger-cto.md
  .claude/agents/challenger-architect.md
- links:
  `docs/use/challenge-the-thinking.md`: running a persona.
  `docs/extend/add-a-challenger-persona.md`: adding a persona.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no contract text; no explanation.
- made: mirrored
- state: keep

### docs/reference/checks.md
- title: Checks
- line: The checks of today, what each verifies, its cost, and which a save and a release run.
- kind: reference
- reader: user, extender
- says: A roster page: one overview table first, then one entry per `.claude/agents/check-*.md`: the check name, its `description`, and its Lens section (what it reads, what it verifies with the owner of each rule, its cost), as `/man check` prints them; one line on which a save and a release run, from the two skills.
- inputs:
  .claude/agents/check-light.md
  .claude/agents/check-project.md
  .claude/agents/check-engine.md
  .claude/agents/check-history.md
  .claude/agents/check-single-source-of-truth.md
  .claude/skills/save/SKILL.md
  .claude/skills/release/SKILL.md
- links:
  `docs/use/check-conformance.md`: running a check.
  `docs/extend/add-a-check.md`: adding a check.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no contract text; no explanation; nothing of the save and release skills beyond which checks each runs.
- made: mirrored
- state: keep

### docs/reference/recipe-genres.md
- title: Recipe genres
- line: The genres of `/recipe` with their skeletons, outputs and checklists in full.
- kind: reference
- reader: user, extender
- says: A roster page: one overview table first, then one entry per `.claude/skills/recipe/genres/*.md`: the genre, its `description`, its skeleton and output, and its elicitation checklist in full, as `/man recipe` prints them; the shared closing once.
- inputs:
  .claude/skills/recipe/genres/presentation.md
  .claude/skills/recipe/genres/readme.md
  .claude/skills/recipe/genres/release-notes.md
  .claude/skills/recipe/genres/screenplay.md
  .claude/skills/recipe/SKILL.md
- links:
  `docs/use/compose-a-recipe.md`: composing through a genre.
  `docs/use/make-a-video-from-a-recipe.md`: the screenplay genre from recipe to played file.
  `docs/extend/add-a-recipe-genre.md`: adding a genre.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no skeleton reproduced; no explanation; not the parenthesis of the release-notes genre that the forge's own recipe reads the intent alone.
- made: mirrored
- state: keep

### docs/reference/id-scheme.md
- title: ID scheme
- line: The format, the numbering rules and the prefix table, exactly.
- kind: reference
- reader: user, extender, evaluator
- says: The format `PREFIX.NNNN` with the fifth digit beyond 9999 and the numeric sort, the numbering rules, and the prefix table with meaning and where each lives (threads in `threads/`, one file per thread), as the ID scheme of `CLAUDE.md` has them.
- inputs:
  CLAUDE.md#ID scheme
- links:
  `docs/about/stable-ids.md`: why IDs are never renumbered.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no explanation; no example from a project.
- made: mirrored
- state: keep

### docs/reference/versioning-and-front-matter.md
- title: Versioning and front-matter
- line: The version scheme and the header fields of an artefact, a brief, a recipe, a work specification and an index, exactly.
- kind: reference
- reader: user, extender, evaluator
- says: The version scheme; the rule that a header carries nothing that changes with a round, the date and the last change computed from the history; the header fields of an artefact (`version`, `status`, `project`, `audience`), of a brief (`project`, `title`, `author`, `version`, `status`), of a recipe (`version` and no status, optional `output:` and `languages:`), of a work specification (`file:`), of a resource index (`directory`); the status rule; the companion and archive file names, as `CLAUDE.md` and the templates have them.
- inputs:
  CLAUDE.md#Versioning & status
  templates/intent.md
  templates/brief.md
  templates/recipe.md
  templates/work.md
  templates/index.md
- links:
  `docs/reference/history-companion.md`: the record's shape.
  `docs/about/versioning-and-history.md`: why.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no explanation; no example values from a project; no author value.
- made: mirrored
- state: keep

### docs/reference/history-companion.md
- title: History companion
- line: The shape of `<file>.history.md`, record by record, exactly.
- kind: reference
- reader: user, extender
- says: The shape of `<file>.history.md` as `templates/history.md` owns it: the front-matter, the record line with its fields in order, the five kinds, what the subject may be, when a field is left out, `Was` last, the two records at a document's birth; the records of state (the mining of a brief, a finding or a challenge settled, a work product's state) and that they do not raise the version; that `rejected`, `parked` and `obsolete` are a decision's verdict, never a record; and the archive rule as `CLAUDE.md` has it.
- inputs:
  templates/history.md
  CLAUDE.md#Versioning & status
- links:
  `docs/reference/versioning-and-front-matter.md`: the fields the companion feeds.
  `docs/use/read-the-history-of-an-item.md`: reading one item's records by command.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no record from a project; no explanation.
- made: mirrored
- state: keep

### docs/reference/requirement-style.md
- title: Requirement style
- line: The rule set of the items of an assignment, exactly.
- kind: reference
- reader: user, extender
- says: The rule set as the Requirement style of the assignment's definition has it.
- inputs:
  .claude/skills/forge/states/assignment.md#Requirement style
- links:
  `docs/about/the-assignment.md`: why the items are written so.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no example item; no explanation.
- made: mirrored
- state: keep

### docs/reference/document-kinds.md
- title: Document kinds
- line: The table of document kinds, verbatim, with the companion, library and wrapping rules.
- kind: reference
- reader: user, extender, evaluator
- says: The table of document kinds of `CLAUDE.md`, verbatim, six columns and every row, the ledger, the project file, the thread and the work kind among them; one line each on the companion of every versioned kind, on a library's reduced set, and on the wrapping rule.
- inputs:
  CLAUDE.md#Document kinds
- links:
  `docs/about/documents-and-records.md`: why the kinds exist.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no explanation; no position ID from the table's cells (the table's bracketed IDs are left out).
- made: mirrored
- state: keep

### docs/reference/ledger.md
- title: Ledger
- line: The ledger's header, tables, columns, state words and reports, exactly, with where each column is read from.
- kind: reference
- reader: user, extender
- says: The ledger as `templates/ledger.md` owns it: the header (the slug and the day it was made, the kind and the language echoed from the project file); every table with its columns (Briefs, Documents, Renders, Published, Work, Sources, Dependencies, Research, Findings, Challenges) and, for each, which header, record, field or report its columns are read from; the state words of briefs, published files, work products, findings and challenges; the row of the documentation index in Renders; the rule of Waiting on principal; the Reports section and the `unparsed:` header line; which tables a library keeps; `ledger.archive.md` read for items without a newer record. That it is made by `python scripts/forge-ledger.py <slug>` and never kept in git.
- inputs:
  templates/ledger.md
  CLAUDE.md#Ledger
  scripts/forge-ledger.py
- links:
  `docs/use/see-where-a-project-stands.md`: reading the ledger through `/ledger`.
  `docs/about/the-ledger.md`: why the ledger is made from the records.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no row from a project; no explanation; no slug from the script's examples.
- made: mirrored
- state: keep

### docs/reference/render-provenance.md
- title: Render provenance
- line: The provenance block every render opens with, the definition of stale, the published companion, and where the files land.
- kind: reference
- reader: user, extender
- says: The YAML front-matter every render opens with, verbatim as `/render` step 5 gives it, with `language:` and `translated_from:` for a render in several languages, and the one definition of a stale render; the file places (`renders/<recipe>.md`, `renders/<recipe>.<lang>.md`, or the recipe's `output:`), the plain file beside the render or in the engine's `docs/videos/` for a screenplay's player file; the `published/` place and the companion `published/<recipe>.md` with its fields as `/publish` step 6 gives them; the state `current | stale` the ledger computes for a published file.
- inputs:
  .claude/skills/render/SKILL.md
  .claude/skills/publish/SKILL.md
  templates/ledger.md#Published
- links:
  `docs/use/render-an-output.md`: the command.
  `docs/use/publish-a-designed-file.md`: the command that writes the companion.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no explanation; no example from a project; nothing of the scan a render passes.
- made: mirrored
- state: keep

### docs/reference/documentation-map.md
- title: Documentation map
- line: The fields of the map, of a writer's task, of a page's front-matter and of the index, exactly.
- kind: reference
- reader: extender
- says: The shape of the map `docs-map.md` as its skeleton, the planner, the writer and the scripts own it: the front-matter (`target`, `owner`; the previous map taken from git, never named in the header); the `## Paths` section; one section per section of the outline, in each one entry with the fields in order (`title`, `line`, `kind`, `reader`, `says`, `inputs` with a part named after `#`, a section by its heading, an item by its ID or a block by its bold label, `links`, `must-not`, `made`, `evidence`, `state`); then Unowned and Did not fit. The task file. The page's front-matter and shape. The index: derived from the map, with the intent's version.
- inputs:
  templates/docs-map.md
  .claude/agents/docs-planner.md#The map
  .claude/agents/docs-writer.md#The shape
  scripts/docs_map.py
  scripts/docs-state.py
  scripts/docs-index.py
- links:
  `docs/about/the-documentation.md`: what the map and the pages are for.
  `docs/extend/change-a-documentation-page.md`: changing a page through its owners.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no entry of the engine's map quoted; no explanation; no model name; nothing of the agents' conduct beyond the shapes.
- made: mirrored
- state: keep

### docs/reference/verdict-words.md
- title: Verdict words
- line: The words and letters the principal types in a walkthrough, exactly.
- kind: reference
- reader: user
- says: The words and what each does, as the walkthrough skill owns them: the verdict line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark` and the single letters `a`, `m`, `q`, `r`, `p` as a whole message; `obsolete`; `write`; `??`; a closing word such as "done" for a thought sent in pieces; that no other word of the forge has a letter and every command is typed in full.
- inputs:
  .claude/skills/walkthrough/SKILL.md
  CLAUDE.md#Working methods
- links:
  `docs/use/walk-through-a-list.md`: the procedure the words belong to.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no explanation; no reason; nothing of the Working methods beyond `??`, `write` and the closing word of In pieces.
- made: mirrored
- state: keep

### docs/reference/repository-layout.md
- title: Repository layout
- line: The layout of the engine root, a thought project and a library, file by file.
- kind: reference
- reader: user, extender, evaluator
- says: The layout block of `CLAUDE.md`, Repository layout, in full: the engine root with `.gitattributes` and `docs/videos/` as the comments have them; a thought project with its project file, `.gitattributes`, `.gitignore`, `threads/`, `ledger.archive.md`, `renders/state.md`, the published companions, `work/` and the renders per language; a library; each comment kept as a fact.
- inputs:
  CLAUDE.md#Repository layout
- links:
  `docs/about/projects-and-the-engine.md`: why projects are repositories of their own.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no explanation; no value of an instance file; no position ID from the comments.
- made: mirrored
- state: keep

### docs/reference/scripts.md
- title: Scripts
- line: Every script with its synopsis, options, forms, what it needs and the command that runs it.
- kind: reference
- reader: user, extender
- says: A roster page: one overview table first (script, what it is for, the command that runs it, what it needs), then one entry per file in `scripts/` from its module docstring: what it does, its synopsis and options, its forms, what it needs installed, where its output lands; for `forge-ledger.py` the ledger it writes and its `--out` form; for `forge-migrate.py` the dry run, `--apply` and `--undo`, the marks and the refusals; for `forge-report.py` the name it completes; for `md2pptx.py` and `md2docx.py` the two engines; for `md2video.py` the two formats, the pace, `--frame`, where the file lands and that it renews the player page under `docs/videos/`; for the three documentation scripts their place in the run of `/document`, `docs-state.py`'s `--previous` form and `docs-check.py`'s one-file scan; the four shared modules each in one line. Below, the portability rule in one line.
- inputs:
  scripts/forge-save.py
  scripts/forge-pull.py
  scripts/forge-status.py
  scripts/forge-clone.py
  scripts/forge-branch.py
  scripts/forge-history.py
  scripts/forge-report.py
  scripts/forge-ledger.py
  scripts/forge-migrate.py
  scripts/forge_repos.py
  scripts/forge_docs.py
  scripts/doc2md.py
  scripts/md2pptx.py
  scripts/md2docx.py
  scripts/md2video.py
  scripts/forge_tools.py
  scripts/hook-walkthrough.py
  scripts/docs-state.py
  scripts/docs-index.py
  scripts/docs-check.py
  scripts/docs_map.py
  CLAUDE.md#Persistence (git)
- links:
  `docs/start/install.md`: installing what the scripts need.
  `docs/use/generate-the-documentation.md`: the run the documentation scripts serve.
  `docs/use/render-an-output.md`: the render that runs the conversions and the one-file scan.
  `docs/use/make-a-video-from-a-recipe.md`: the job `md2video.py` serves.
  `docs/use/read-the-history-of-an-item.md`: the command behind the history script.
  `docs/use/migrate-a-project.md`: the command behind the migration script.
  `docs/extend/add-a-script.md`: writing a script of one's own.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: nothing below a docstring; no example path or slug of a project (the docstrings carry `platform-strategy`, `agentic-platform`, `acme`, `flow-ba`, `fixture`, a `lib-acme` path, a path into the forge project's renders and a forge report's name, replaced by `<slug>` and `<path>`; `forge`, `main`, `my-idea` and `example.com` may stand); no date, thread number or brief name from a docstring; no explanation; no version tag from an example.
- made: mirrored
- state: keep

### docs/reference/templates.md
- title: Templates
- line: Every skeleton in `templates/`, what it is the skeleton of, and which procedure creates from it.
- kind: reference
- reader: extender
- says: A roster page: one overview table first, then one entry per file in `templates/`: what it is the skeleton of, which command or procedure creates from it, and its fields or sections in one line; the `<type>-definition.md` naming rule; the project file's skeleton and what a project without the file is; the thread's skeleton; the attributes template a project's `.gitattributes` is copied from; the map's skeleton; the work specification's skeleton; the screenplay recipe's skeleton; the player page's skeleton, from which the script writes the served page; the readme skeleton's "Pinned facts (not rendered)" section; the fields of a resource index entry and of a bundle index; the decision's Verdict line.
- inputs:
  templates/CLAUDE.local.md
  templates/project.md
  templates/gitattributes
  templates/brief.md
  templates/intent.md
  templates/thread.md
  templates/assignment.md
  templates/solution-design.md
  templates/work.md
  templates/ledger.md
  templates/decisions.md
  templates/history.md
  templates/index.md
  templates/index-bundle.md
  templates/recipe.md
  templates/recipe-readme.md
  templates/recipe-release-notes.md
  templates/recipe-presentation.md
  templates/recipe-screenplay.md
  templates/html-player.html
  templates/docs-map.md
  templates/artefact-definition.md
  templates/critic-definition.md
  templates/challenger-definition.md
  templates/check-definition.md
  CLAUDE.md#Templates
- links:
  `docs/extend/what-it-is-made-of.md`: where the templates sit in the whole.
  `docs/reference/documentation-map.md`: the map's fields in full.
  `docs/about/the-work-product.md`: the kind the work skeleton serves.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no skeleton reproduced whole; no explanation; not the readme skeleton's fixed closing sentence; nothing of the player page's styles or code beyond its head comment; no position or design ID from the comments.
- made: mirrored
- state: keep

### docs/reference/configuration.md
- title: Configuration
- line: The files that configure an instance and a project, and what each holds, field by field.
- kind: reference
- reader: user, extender
- says: `.claude/settings.json` (shared: `attribution` with an empty commit trailer and `sessionUrl` false, the deny rules for sensitive paths and raw git in both shells, the `UserPromptSubmit` hook running `scripts/hook-walkthrough.py` through `python`); `.claude/settings.local.json` (gitignored, the session model, created by `/setup`); `CLAUDE.local.md` (gitignored: the principal by role, the conversation language and the author handle); the `.gitignore` of the engine (the instance files, `projects/*` with `projects/forge` re-included, the forge project's ledger); the `.gitattributes` of the engine and the template a project's own is copied from (which files are taken as `ours` at a merge and which are binary); a project's file `project.md` (slug, kind, language); the configuration outside the engine as `/setup` writes it: the git identity per host with the guard, and the registration of the merge settings.
- inputs:
  .claude/settings.json
  .gitignore
  .gitattributes
  templates/gitattributes
  templates/project.md
  templates/CLAUDE.local.md
  .claude/skills/setup/SKILL.md
  CLAUDE.md#What this workspace is
- links:
  `docs/start/setup.md`: the command that fills the instance files.
  `docs/about/how-the-rules-are-held.md`: why the deny rules and the hook exist.
  `docs/about/persistence-in-git.md`: what the merge settings and the attributes are for.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no value of an instance; no host; no explanation beyond one clause per item; nothing of the `.gitignore`'s entry for a local launcher; no mention of PowerShell beyond the deny rule's shell name; no position or design ID from the comments; no driver for record files, which is not registered today.
- made: mirrored
- state: keep

### docs/reference/glossary.md
- title: Glossary
- line: Every term of the forge in one line, with the file that defines it.
- kind: reference
- reader: user, extender, evaluator
- says: The terms in one line each, with the file that defines each: principal, recipients, Claude as cognitive extension, session, harness, document, artefact, brief, intent, position, fact, thread, thread file, rejected direction, assignment, solution design, layer, definition, template, Map, elicitation, walkthrough, verdict, round, write, history companion, record, record of state, archive, ledger, made at read time, Waiting on principal, Reports, decision, Verdict line, source, bundle, extract, research, resource index, Role, project file, kind, recipe, render, plain file, published file, published companion, format file, genre, screenplay, player page, public folder, primary render, translation, provenance, stale, state render, work product, specification, critic, lens, challenger, persona, check, finding, challenge, contract, Lens section, subagent, isolation, project, thought project, library, dependency, engine, instance, instance fact, session model, save, release, pull, migration, shape of a project, major, tag, branch, immutable, mined, documentation, documentation map, page, index, mirrored, derived, how-to, explanation, reference, pinned fact, Unowned, guarded command, working method, prime directive.
- inputs:
  CLAUDE.md
  projects/forge/10-intent.md#POS.0120
  projects/forge/10-intent.md#POS.0230
  projects/forge/10-intent.md#POS.0300
  projects/forge/10-intent.md#POS.0950
  projects/forge/10-intent.md#POS.1090
  projects/forge/10-intent.md#POS.1450
  projects/forge/10-intent.md#POS.1520
  projects/forge/10-intent.md#POS.1530
  projects/forge/10-intent.md#POS.1540
  projects/forge/10-intent.md#POS.1550
  projects/forge/10-intent.md#POS.1590
  projects/forge/10-intent.md#POS.1600
  projects/forge/10-intent.md#POS.1610
  projects/forge/10-intent.md#POS.1740
  projects/forge/10-intent.md#Elicitation
  .claude/skills/forge/states/brief.md
  .claude/skills/forge/states/intent.md
  .claude/skills/forge/states/assignment.md
  .claude/skills/forge/states/solution-design.md
  .claude/skills/walkthrough/SKILL.md
  .claude/skills/render/SKILL.md
  .claude/skills/publish/SKILL.md
  .claude/skills/document/SKILL.md
  .claude/skills/pull/SKILL.md
  .claude/skills/work/SKILL.md
  .claude/skills/migrate/SKILL.md
  .claude/skills/critic-contract/SKILL.md
  .claude/skills/challenger-contract/SKILL.md
  .claude/skills/check-contract/SKILL.md
  .claude/skills/docs-contract/SKILL.md
  .claude/agents/docs-planner.md
  .claude/agents/docs-writer.md
  templates/ledger.md
  templates/history.md
  templates/decisions.md
  templates/project.md
  templates/thread.md
  templates/recipe-readme.md#Pinned facts (not rendered)
- links:
  `docs/about/what-it-is-and-is-not.md`: the forge in prose.
- must-not: no term invented; no definition longer than a sentence; no name, handle or instance value; no address; no term of a mechanism that is not built (landing, `+` token, record driver, `/merge`, worktree, ID blocks).
- made: derived
- evidence: each term is defined where a file first defines it: the roles, the document kinds, the chain, the reviewers, the ledger, persistence, the commands in CLAUDE.md (whole, since the terms span its sections); the artefacts in their definitions, the thread file in the intent's definition and its template; position, fact, thread, rejection in POS.0120 and POS.0230; elicitation, Map, definition in the Elicitation group; walkthrough, verdict, round, write in the walkthrough skill; render, provenance, stale, primary render, translation in the render skill and POS.1550; published companion in the publish skill; the work product and its specification in POS.1520 and the work skill; screenplay, format file, player page, public folder in POS.1530 and POS.1540; the states against the origin in the pull skill; the migration and the shape of a project in the migrate skill, the project file skeleton and POS.1740; the project file and kind in POS.1590 and its skeleton; made at read time, record of state, Waiting on principal, Reports and the archive in POS.1600, POS.1610 and the ledger and history skeletons; the Verdict line in the decisions skeleton; lens, persona, check, finding, challenge, contract, Lens section, isolation in the three contracts; session, harness, instance, subagent, how-to, explanation, reference, mirrored, derived in the docs contract; the ledger's state words in its template; engine, instance fact in POS.0950; major in POS.0300; guarded command in POS.1090; documentation, map, page, index in POS.1450, the `/document` skill and the two agents; pinned fact in the readme skeleton's section. A term no file defines is left out.
- state: keep

## Unowned

- Whether the forge runs on Linux and macOS as a verified fact, needed by `docs/start/install.md`, `docs/about/persistence-in-git.md` and `docs/extend/add-a-script.md`: CLAUDE.md, POS.0830 and SOL.0620 say it is a writing rule until verified. The pages state the rule and no claim.
- What `/document <slug>` reads for a project other than the engine beyond the planner's paragraph, and in which language a project's pages are written when its artefacts are not English: open in the intent's thread on project documentation; needed by `docs/about/the-documentation.md` and `docs/use/generate-the-documentation.md`, which say nothing of it.
- What `/forge <state>` does on a project of kind `library`: not needed by any page; recorded so that no page invents it.
- What Claude Code is beyond "the engine runs in Claude Code": `docs/start/what-it-is.md` says what the Essence says and nothing beyond it.
- What document kind the player page `docs/videos/index.html` is: no row of CLAUDE.md, Document kinds names it; `docs/about/the-screenplay-and-its-player.md` says it is a file of the engine written by the script and names no kind.
- The sections and the order of the course of videos beyond the alphabet of file names: open in the intent's thread on the course; `docs/about/the-screenplay-and-its-player.md` and `docs/use/make-a-video-from-a-recipe.md` say "in the order of their names" and no more.
- How the tag before a migration is taken and how the way back from it runs: the migrate skill names "the tag before the migration" as the way back after the save, POS.1740 says it is taken per project immediately before `/migrate` and that the way back is the principal's own hand through git; no skill takes the tag or describes the way back. `docs/use/migrate-a-project.md` names the tag as the way back and nothing more.
- The reason for the fifth digit of an ID that holds without the blocks of IDs: POS.0220 gives the blocks as the reason and they are not built; `docs/about/stable-ids.md` states the rule without a reason beyond CLAUDE.md.

## Did not fit

- The intent and the solution design describe mechanisms of the brief `collaboration` that are not built: the forge's own driver for record files, `/merge`, the worktree and the second root of the engine, the version as a boundary (`+`, `landed`, the landing on main), the blocks of IDs and the allocation over the local branches, `ids.md`, the renumbering of an item at a merge clash, the fixture script, and the conversion to one sentence per line. The design marks each "Not built" or deferred and CLAUDE.md, the skills and the scripts carry none of them. The pages follow the operating layer: every entry whose inputs touch one of them forbids it in `must-not`.
- POS.1580 says prose is written one sentence per line; CLAUDE.md, Document kinds still says hard-wrapped at about 72 columns, and the design marks the conversion not built. The operating layer wins: `docs/about/documents-and-records.md` and `docs/reference/document-kinds.md` say 72 columns.
- POS.1110 and POS.1490 offer `/merge` at the state diverged and write the branch command as `forge-branch <name>`; the pull skill offers `/save` first or a merge by hand, and the script takes `<slug> [branch]`. The operating layer wins.
- SOL.0220 says the sweep of `/ingest` tells a changed file against the ledger date; the ingest skill says against the Date of the index entry. SOL.0420 says `/publish` sets `current` and every `/render` sets `stale`; the publish skill, the render skill and the ledger template say the state is computed from the dates. SOL.0160 says `/new-project` creates `ids.md`; the skill does not. The operating layer wins in each.
- In the solution design the heading "### Rendering and publishing" stands inside the text of SOL.0810, so the section "The reviewers" runs on to "### Persistence" and carries the rendering items; `docs/extend/what-it-is-made-of.md` names SOL.0300 and SOL.0330 instead of that section. SOL.0670's sentence on when it was built is garbled ("R1.10).0620)"); no page reads it.
- The scripts' header says an item is found by the line that carries `**POS.1450**`; titled items carry the ID and a title in bold (`**SOL.0640 The work product.**`). The history script's docstring cites `sol460`, a titled item, through the same reader, so the map cites titled items by ID; should the reader miss one, the state script reports the input missing and the page is regenerated.
- The contract allows no address but the target's public home; the start pages carry the course page of the teaching videos, which the pinned facts name as the engine's own repository served by GitHub Pages. Kept on the four start pages from the pinned facts and forbidden on every other page.
- `docs/start/what-it-is.md` is an explanation in a section the outline marks how-to; kept in `start/` with `kind: explanation`.
- The skeleton's heading `# Documentation map — <target>` carries a long dash; this map's heading carries a spaced hyphen.
- `use/` never names a subagent or a model; `docs/use/generate-the-documentation.md` says "a planner" and "a writer" because the skill's steps are nothing without them; no agent file and no model name reaches the page.
- The release-notes genre file says the forge itself reads the intent alone, while the forge's recipe reads the solution design's history as well; the pages leave the parenthesis out.
- CLAUDE.md, Isolated reviewers speaks of three contracts; the documentation agents share a fourth and are not reviewers; the pages say so.
- The owning project's recipes carry facts no page may carry: the readme recipe's author line with a name and an e-mail, the contributing recipe's channels as addresses and the author's profile; the pages that read either name the section they read and keep those off the page. The pitch recipes and `ba-intro` own nothing a page needs.
- The scripts' docstrings carry example slugs and paths (`platform-strategy`, `agentic-platform`, `acme`, `lib-acme`, `flow-ba`, `fixture`, a path into the forge project's renders, a forge report name), and the migration script's header names the brief `collaboration` and "the first release"; the pages replace them by placeholders and say "a release that changes the shape of files". The hook's docstring carries dates and a thread number; the pages take what it prints. The setup skill carries a date of a finding; the setup page leaves it out.
- The forge intent names its first principal by handle in POS.0005, POS.0990 names the licence holder; the briefs carry an `author` field; every page that reads the intent has "no name, no handle" in its `must-not` or reads no such item.
- `00-brief.md` says no brief exists for the forge; the other briefs were read and their substance stands in the intent, so the reasons of the `about/` pages come from the intent and no brief is an input. The threads, `decisions.md` and the research index were read for orientation and are the input of no page; the pull skill reads `RELEASE-NOTES.md`, a render, which the map never names as an input.
- The reasons the writers wanted and no file records stay unrecorded; the entries say the page says the reason is not recorded.
- The three new pages are each named under `links` by at least one other entry: the migration how-to by the upgrade, pull, scripts and bring-in pages and the migration concept; the ledger concept by the map how-to, the documents page, the persistence page, the migration concept and the ledger roster; the migration concept by the upgrade and migration how-tos, the projects page and the ledger concept.
- The renders, the README, `CONTRIBUTING.md`, `RELEASE-NOTES.md`, `docs/` and `docs/videos/` of the target were not read, as the definition says.
