---
target: engine
owner: projects/forge
---

# Documentation map - the engine

Paths under `inputs` are relative to the engine root. Every page of the previous map keeps its path and is `keep`; five pages are `new` (the user stories as a job and as an artefact, the tests as a job and as a concept, the two fixed files of the root); none is `remove`. Entries whose material did not change are carried over word for word, so that only the pages whose entry or inputs changed are made again. `docs/videos/` is not a section of the documentation and is not mapped. For every entry at least one other entry names it under `links`. Every input stands on a line of its own, a part named only where its heading, its ID or its bold label exists on disk.

## Paths
- user: docs/start/what-it-is.md, docs/start/install.md, docs/start/setup.md, docs/start/first-result.md, docs/use/forge-the-intent.md
- extender: docs/extend/what-it-is-made-of.md, docs/extend/how-a-change-is-made.md, docs/about/how-the-rules-are-held.md, docs/about/the-tests.md, docs/extend/change-a-documentation-page.md
- evaluator: docs/about/what-it-is-and-is-not.md, docs/about/how-a-thought-travels.md, docs/about/elicitation.md, docs/about/isolated-reviewers.md, docs/about/the-documentation.md

## start

### docs/start/what-it-is.md
- title: What Forge of Thought is
- line: What is this thing, in one paragraph, before you install anything?
- kind: explanation
- reader: user, evaluator
- says: One paragraph in plain words: Forge of Thought is a workshop in which a thought is tempered into a chain of versioned documents under review by agents that never saw the conversation; it runs in Claude Code, Anthropic's agent for the command line, whose slash commands, skills, agents and hooks are the forge's mechanisms; the person who uses it is the principal, whose thinking is forged and who decides everything, while Claude proposes and keeps order. One person starts from a rough brief, works it into an intent by interview, takes the layers the project needs, has the thinking attacked by blind reviewers and gets outputs for every audience generated from the documents. One closing sentence says what it technically is: a git repository of slash commands, isolated agents, templates, scripts and conventions, bound to no domain. One sentence then points at the course page of the teaching videos (the address the pinned facts give): real sessions cut to a few minutes and played in the browser, the place to see the forge at work before reading on.
- inputs:
  CLAUDE.md#What this workspace is
  CLAUDE.md#Roles
  projects/forge/10-intent.md#Essence
  projects/forge/10-intent.md#POS.0780
  projects/forge/10-intent.md#POS.0600
  projects/forge/recipes/readme.md#Pinned facts (not rendered)
  CLAUDE.md#Repository layout
- links:
  `docs/start/install.md`: what must be on the machine and how it gets there.
  `docs/about/what-it-is-and-is-not.md`: the longer explanation of what the forge is, is not, and why.
  `docs/about/the-screenplay-and-its-player.md`: what the teaching videos are made of and where they are played.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no commands, no file names, no conventions, no history of the project, no name of a person, no instance fact, no version number; no address but the course page's and none of the other pinned facts.
- made: derived
- evidence: CLAUDE.md, What this workspace is, gives the identity sentence, that the forge runs in Claude Code, Anthropic's agent for the command line, and that the slash commands, the skills, the agents and the hooks are its mechanisms; Roles the two roles; the Essence the reviewers blind to the conversation and the unconstrained subject matter; POS.0780 where a run ends and that the mechanics are domain-agnostic; POS.0600 the name; the pinned facts the course page and what is played there. The technical sentence is composed from CLAUDE.md, What this workspace is (the mechanisms of Claude Code the forge is told through) and Repository layout (templates, scripts, the conventions of the core), with the Essence's domain sentence.
- state: regenerate

### docs/start/install.md
- title: Install what the forge needs
- line: What must be on your machine, and in what order, before the forge runs?
- kind: how-to
- reader: user
- says: Steps in the order a newcomer needs them, each with what you see when it worked: git, version 2.36 or newer where `/setup` is to write the identity per host; Python 3.8 or newer on PATH as a real executable named `python` (the scripts and the two hooks are Python and the hooks are started without a shell; the package or symlink the pinned facts name for Linux and macOS); Claude Code with a paid subscription, installed by the lines the pinned facts give, signed in on first run; clone the engine from its public home (never copy it: the scripts refuse an engine that is not a repository); always start `claude` from the engine root. One line on platforms, as the owners say it: the scripts are written to run unchanged on Linux and macOS; the engine's tests run in CI on Linux and Windows at every push, the git scripts, the ledger, the light check and the git hook's judgement among them; the conversions are tested only for their failure without the tool, the per-prompt hook is a writing rule until a run says otherwise, and nothing has run on macOS, where the whole set is the writing rule alone. The optional tools last, each resolved from PATH and installed by no script: markitdown through pip for `/ingest`'s conversions; pandoc for the plain Word and PowerPoint files of `/render`; Pillow and ffmpeg for the video format of a screenplay (the player format needs nothing beyond Python); the document-skills plugin for `/publish` unless Claude Code already brings the docx and pptx skills; the command-line tool of a second engine for a research on two model families (today `agy`, the row `antigravity`, at version 1.1.1 or newer): the forge asks only that it is on PATH and signed in once, how it is installed and signed in being the tool's own documentation's, the forge carrying no key or account; GitHub's command-line tool `gh`, on PATH and logged in, for the line of the state map that says what waits on GitHub outside git, without which that line says it could not read and why; pytest, `python -m pip install pytest`, the one thing a contributor installs beyond `python` to run the engine's tests, which a user never runs. Closes by pointing at the first setup. One worked example: the sequence as typed, with placeholders.
- inputs:
  projects/forge/recipes/readme.md#Pinned facts (not rendered)
  CLAUDE.md#Persistence (git)
  projects/forge/10-intent.md#POS.0830
  projects/forge/10-intent.md#POS.1880
  projects/forge/10-intent.md#POS.1930
  .claude/settings.json
  scripts/hook-walkthrough.py
  scripts/hook-git.py
  scripts/forge-config.py
  scripts/forge_repos.py
  scripts/forge-status.py
  scripts/doc2md.py
  scripts/forge_tools.py
  scripts/md2video.py
  scripts/forge-engine.py
  .claude/skills/test/SKILL.md
- links:
  `docs/start/what-it-is.md`: what you are installing, in one paragraph.
  `docs/start/setup.md`: the first run, `/setup`.
  `docs/use/research-a-topic.md`: the research that uses a second engine.
  `docs/use/run-the-tests.md`: the tests a contributor runs with `/test`.
  `docs/reference/scripts.md`: every script with what it needs and its options.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no account, no author line, no e-mail; no address other than those the pinned facts give: the engine's public home, the course page and the install lines of Claude Code, which carry the tool's own addresses and may stand; nothing of the readme recipe beyond its pinned facts; no platform-specific path; no claim of a run on macOS and none on Linux beyond what CLAUDE.md, Portability, and POS.0830 say; no issue, pull request or user the intent cites for the run on Linux; nothing on the identity per host or the registration of the merge driver beyond the git version they need (the setup page's); no mention of PowerShell; nothing of the script bodies below their headers; no install line for the second engine's tool, which is its own documentation's; no vendor or model family named for the second engine beyond `antigravity` and `agy`; no date or probe from the engine script's header; no count of tests; no discussion or pull request of the forge project.
- made: derived
- evidence: the pinned facts own the prerequisites, the `python` remedies, the Claude Code install lines, "clone, not copy", "start from the engine root", the script prerequisites and the addresses; CLAUDE.md, Persistence (Portability) gives Python 3.8 or newer, the tools resolved from PATH, the tests in CI on Linux and Windows and what of the rest is a writing rule; POS.0830 the same with the reason and that nothing has run on macOS; POS.1880 that the installation and the login of an engine's tool are the tool's own documentation's and the forge asks only that it is on PATH; POS.1930 and the `/test` skill that pytest is the one thing a contributor installs, by `python -m pip install pytest`, and that a user never runs the tests; `.claude/settings.json` starts both hooks through `python`, and the two hook headers say what each needs; `forge-config.py`'s header that the identity stanzas need git 2.36 or newer; `forge_repos.py` refuses an engine that is not a clone; `forge-status.py`'s header that `gh` on PATH and logged in serves the line on what waits on GitHub and that the line says so without it; `doc2md.py` gives the pip line; `forge_tools.py` owns what pandoc and the claude engine need; `md2video.py`'s header what the video and the player formats need; `forge-engine.py`'s header that the engine's tool is found on PATH, the version floor of the one row, and that the login is the user's, made once outside the forge. The order is the writer's, by when each piece is first needed.
- state: regenerate

### docs/start/setup.md
- title: Set up the forge
- line: What does `/setup` ask and write on the first run after cloning?
- kind: how-to
- reader: user
- says: The first run, before any other work: `/setup`. What you see, step by step: `CLAUDE.local.md` created from its template by a short interview, one question at a time, the conversation language first, then who the principal is by role, then the principal's short handle, which stands as the author of every history record he decides; the file is gitignored and never committed, and on an instance that already has it `/setup` only offers the lines it lacks. Then the git identity, which is git's: `python scripts/forge-config.py` first shows what the global git configuration holds; you name the hosts you push to with a name and an e-mail for each, or leave it for later; on your word one call per host, `python scripts/forge-config.py --identity <host> <name> <email>`, writes the per-host stanzas and the identity file beside the global file, and a stanza or identity file that differs is reported and left unless you accept `--replace`; then the global guard, `--guard`, and where a global name or e-mail survives, `--guard --unset-identity`, since the guard only bites once that identity is gone. Where git reads another global file in another place (a network home at work, a local profile at home), `/setup` runs once in each. Then, once per machine and once in each such place, on your word, the registration of the merge driver `ours` and the git settings it needs, `python scripts/forge-config.py --register`, with `--zdiff3` offered apart; they hold for every repository on the machine, and renormalize only evens line endings at a merge. Declined, the commands are printed for you to run by hand; nothing already set is overwritten; `python scripts/forge-status.py` reports the registration afterwards. The identity is verified by git at the first `/import-project`. Then `.claude/settings.local.json`, created with the session model set to Fable, the strongest model, on which the whole forge including the blind reviewers runs, or the strongest model the account lists, changeable with `/model` or by editing the file. It ends by pointing at `/new-project` or `/import-project`. One sentence says that the course page of the teaching videos (the pinned address) shows a first run before you make your own. One worked example with placeholder values. Prerequisite: the install page.
- inputs:
  .claude/skills/setup/SKILL.md
  templates/CLAUDE.local.md
  scripts/forge-config.py
  scripts/forge-status.py
  projects/forge/recipes/readme.md#Pinned facts (not rendered)
- links:
  `docs/start/install.md`: what must be on the machine first.
  `docs/start/first-result.md`: from a new project to a saved intent in one sitting.
  `docs/about/persistence-in-git.md`: why the identity is git's, why the scripts are the only door and what the merge driver `ours` is for.
  `docs/reference/configuration.md`: the instance files and settings, field by field.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no example host, name, handle or e-mail that could be real (the script's example name and address become `<name>` and `<email>`); no instance value; no path of a machine's global git configuration file; nothing of the skill copied as an instruction to Claude; no address but the course page's and none of the other pinned facts; no merge driver of the forge's own for record files, which the forge does not have; nothing of the status script's line on GitHub, which is the state map's.
- made: mirrored
- state: regenerate

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
- must-not: no explanation of what a brief or an intent is beyond one clause each; no instance slug (use `my-idea`); no theory of elicitation; no address but the course page's; nothing of the readme recipe but its Quickstart instruction (Section 5) and the pinned course address; no author line; nothing of the forge's own project beyond that a user never needs to open it.
- made: derived
- evidence: the sequence and the git step are the readme recipe's Quickstart instruction; what each step does for the person is read from the skills and the two Courses; "not under git" is CLAUDE.md, Persistence; the course page is the pinned facts'. The sample brief is invented by the writer as a generic shape.
- state: regenerate

## use

### docs/use/start-a-project.md
- title: Start a project
- line: How do you scaffold a thought project or a library with `/new-project`?
- kind: how-to
- reader: user
- says: `/new-project <slug>`: a thought project (the chain) or a library (`lib-` prefix, material only); the kind and the language of the chain artefacts are asked where your words leave them open and written once into the project file `project.md`. What the command creates for each kind, files only, never git: for every project the project file, `.gitattributes` from its template and `.gitignore` from its template, which keeps the ledger and the lock files of an open Office document out of git; for a thought project beside them `sources/`, `reviews/`, `challenges/`, `research/` and `threads/`, the two resource indexes, `decisions.md` and the readme and release-notes recipes with their history companions; for a library only the indexes and the readme recipe. The founding brief is asked for at once and handed to the brief procedure; the intent and lower layers are born at their first `/forge <state>`; the ledger is made once by its script; `logo.png` is optional. The one-off act that is yours: `git -C projects/<slug> init -b main`, then a remote if wanted. One worked example with `<slug>`.
- inputs:
  .claude/skills/new-project/SKILL.md
  templates/project.md
  templates/gitignore
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
- state: regenerate

### docs/use/bring-in-an-existing-project.md
- title: Bring in an existing project
- line: How do you clone a project you already have into `projects/` with `/import-project`?
- kind: how-to
- reader: user
- says: `/import-project <git-url>` clones the repository through the clone script into `projects/<repository name>`, never overwriting, and relays the script's facts: the last commit, the origin, the identity git resolves (none means the save script will commit nothing; the script names the way out, `/setup` or `python scripts/forge-config.py --identity <host> <name> <email>`), and the project file with its kind and language, or, where the project has no project file, that it is of the shape before the migration and the one remedy is `/migrate`; a project with neither a project file nor a ledger was not made by the forge, a fact, not a defect. Nothing is written into the project. Work starts by selecting it, `/forge <slug>`. A project already on this machine, in a repository of its own, in another's or in none, is not cloned: you copy or link it into `projects/<slug>` by hand, and the forge knows it from `/forge <slug>` on. The script's messages under "If something goes wrong". One worked example with `<git-url>`.
- inputs:
  .claude/skills/import-project/SKILL.md
  scripts/forge-clone.py
  templates/project.md
- links:
  `docs/use/see-where-a-project-stands.md`: the `/forge` map that follows.
  `docs/use/migrate-a-project.md`: what to do with a project of the shape before the migration.
  `docs/use/upgrade-the-engine.md`: what to check when a project was written to older conventions.
  `docs/start/setup.md`: the identity step, when git resolves no identity for the clone.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no URL with a real host (`<git-url>`; the script's `example.com` may stand); no identity example beyond the placeholders `<host>`, `<name>` and `<email>`; nothing of the fixture flag the script prints.
- made: mirrored
- state: regenerate

### docs/use/see-where-a-project-stands.md
- title: See where a project stands
- line: What does the bare `/forge` map tell you about a project, and what does `/ledger` tell you?
- kind: how-to
- reader: user
- says: Bare `/forge [slug]` first makes the project's ledger with its script, then reports the state map: the kind and the language from the project file, and whether the project is under git, as the status script reports it and as a fact; a library stops after its material and the git line; the artefacts with versions and status, the briefs with their mining state; which target states can be worked from here; stale renders and stale published files; the libraries it needs and whether each is cloned alongside; what waits on the principal, the few live matters named in words with the ID following in brackets as an address, and the rest as a count; a recommended next step and, where more than one matter waits, the offer of a walkthrough. The last word is the state of the engine and of the project against the origin (up to date, behind, ahead, diverged, no origin) with that state's one offer, and, from the same run of the status script, what waits on GitHub outside git: the open pull requests and the discussions nobody of the repository has answered, one line each, or the one line saying it could not read them and why (no `gh`, an origin that is not GitHub, no login, no network); the offer is to look at it before anything is written into the project, and the map runs none of it. A project of the shape before the migration is said so and nothing more. `/ledger [slug]` makes the ledger and gives the same report from it, for one project or all; the lines the ledger script could not parse and its Reports section are read aloud, and fixing them is the light check's. One worked example of a map, generic: the matters waiting on the principal shown as sentences in words, the place of the ID left as the bracket a reader would see and never a number, since no ID of any project may stand on a page.
- inputs:
  .claude/skills/forge/SKILL.md
  .claude/skills/ledger/SKILL.md
  scripts/forge-status.py
  templates/project.md
  templates/ledger.md#Reports
- links:
  `docs/about/the-ledger.md`: what the ledger is made from and why nobody writes it.
  `docs/use/pull-from-the-remote.md`: the offer the map makes when a repository is behind.
  `docs/use/migrate-a-project.md`: what to do when the map says a project is of the old shape.
  `docs/use/walk-through-a-list.md`: how the matters waiting on the principal are worked.
  `docs/reference/ledger.md`: the ledger's tables and state words.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no description of `/forge <state>`; no staleness definition beyond a pointer; no content of a real project; no ID of the chain, not even a placeholder one, in the example; no worktree or branch suffix of a slug, which is not built; no pull request, discussion or number of the forge project; no slug from the status script's examples.
- made: mirrored
- state: regenerate

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
  `docs/use/write-a-brd.md`: the business requirements that may be broken out of the assignment next.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no restatement of the Requirement style rules; no ID numbering rules; no item of a real project.
- made: mirrored
- state: regenerate

### docs/use/write-a-brd.md
- title: Write a BRD
- line: How do you break an assignment, an intent or a document someone gave you into business requirements with `/forge brd`?
- kind: how-to
- reader: user
- says: `/forge brd [slug]` iterates `30-brd.md`, the business requirements. When asking for it you name its parent: the assignment (read with the intent and the threads), or the intent where the project has no assignment. A file someone else gave you (a transcript, an offer, a document) is registered first with `/ingest` and yields a draft that is always a work product in `work/`, never `30-brd.md`; to have it in the chain, an intent is first handed over from the same file. Around the parent the forge reads the decisions, the ledger, the resource indexes of the project and of every library it depends on, and the instance's roster of areas: a library document of the instance, cited by path, that names the areas of the enterprise a BRD must consider and which of them are mandatory; a project with no enterprise around it has no roster, writes `Roster: none` and walks the area against nothing. The ways in, and what you see in each: found together, questions up front one per message on the stakeholders, the scope of the document and the phasing, then the whole draft with its provenance map, then a walkthrough by group with the touched areas of the enterprise one per item; on your word drafted automatically, Claude asking nothing and returning the draft with the provenance map, what he assumed and the list of what must be supplied from outside, in two parts, what the forge already holds by path and what must be fetched, an open question with no owner marked `owner: unassigned` until you name a role; a parent that moved, and the pass runs on what changed; a wording fix, made directly. Where a draft of the first two ways lands, in the chain or as a quick look in `work/`, is your word when you ask. The round ends by naming what changed, what stays open and what must come from outside, and offers the approval; the stakeholders' sign-off is your organisation's act, recorded outside the forge or as a decision where you want it kept. The reviewers offered for it: `/critique essence` and `/critique clarity`, `/challenge business-analyst`, `/check brd`. One worked example with `<slug>`, generic.
- inputs:
  .claude/skills/forge/states/brd.md
  templates/brd.md
- links:
  `docs/about/the-brd.md`: what a BRD is, what it holds and why the forge names what it cannot know.
  `docs/use/work-a-work-product.md`: the work product a BRD from someone else's file becomes.
  `docs/use/register-a-source.md`: registering the file put in.
  `docs/use/share-material-through-a-library.md`: the library a roster of areas is kept in and cited from.
  `docs/use/write-user-stories.md`: the stories that may be broken out of a BRD next.
  `docs/use/challenge-the-thinking.md`: running the business-analyst persona.
  `docs/use/check-conformance.md`: running the `brd` check.
  `docs/reference/requirement-style.md`: the rule set of a BRD's items.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no library path, company, group standard or fork of an instance; no item of a real project; no trial, transcript or vendor; nothing of the Partner block as an instruction to Claude; no restatement of the Map's areas or of the Requirement style; no thread number.
- made: mirrored
- state: regenerate

### docs/use/write-user-stories.md
- title: Write user stories
- line: How do you break a BRD, or a small change of the intent, into user stories with `/forge user-stories`, and hand the stakeholders their export?
- kind: how-to
- reader: user
- says: `/forge user-stories [slug]` iterates `35-user-stories.md`. When asking for it you name its parent: the BRD, read with the layers above it, or the intent where the change is small, the ask precise and without further impact and you say so; whether the ask suffices is your word, and Claude may say why he thinks it does not. A requirements document of someone else, registered first with `/ingest`, yields stories that are a work product in `work/`, never `35-user-stories.md`. What you see, step by step, in the default way, handing over: Claude walks the Map alone and returns first the cut, the name of every story with a short description of what it covers and the items of the parent no story serves, named by what they say, for your word; only on the cut agreed he drafts the whole stories, asks nothing and returns the draft; the stories are then walked story by story, one per message with the verdict line; a story whose parent does not suffice turns the walk into an interview on that story, one question at a time; a parent that moved runs the pass on what changed; a wording fix is made directly. Nothing is derived from the draft before you have judged it. The round ends by naming what changed and what stays open and offers the approval; the stakeholders' approval of the whole is your organisation's act, recorded in the decisions where you want it kept. The reviewers offered: `/check user-stories` for the mechanics, `/critique clarity` with the Story style, `/critique essence` for drift from the parent. The export the stakeholders receive is a render and never the artefact: `/recipe user-stories-export` composes its recipe through a short interview (the input, the section heading and the purpose line), `/render user-stories-export` writes `renders/user-stories-export.md`, one heading per story with its parts on lines of their own, no table, no line wrapped, every reference to a POS left out since the stakeholders never see the intent, ready to be pasted into a wiki or a tracker. One worked example with `<slug>`, generic: the cut, one story walked, the export of that story.
- inputs:
  .claude/skills/forge/states/user-stories.md
  templates/user-stories.md
  .claude/skills/recipe/genres/user-stories-export.md
  templates/recipe-user-stories-export.md
- links:
  `docs/about/the-user-stories.md`: what the stories are, what a story holds and why the export leaves the intent out.
  `docs/use/write-a-brd.md`: the usual parent of the stories.
  `docs/use/work-a-work-product.md`: the work product stories from someone else's document become.
  `docs/use/walk-through-a-list.md`: the walk of the draft, one story per message.
  `docs/use/compose-a-recipe.md`: the genre interview every recipe runs through.
  `docs/use/render-an-output.md`: the render that makes the export.
  `docs/use/check-conformance.md`: running the `user-stories` check.
  `docs/reference/requirement-style.md`: the Story style of a story's parts.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no restatement of the Story style or of the Map's areas; no story of a real project; no product name of a wiki or a tracker; no source file of the forge project named; nothing of the Partner block as an instruction to Claude; no thread number.
- made: mirrored
- state: new

### docs/use/design-the-solution.md
- title: Design the solution
- line: How do you iterate the solution design with `/forge solution-design`?
- kind: how-to
- reader: user
- says: `/forge solution-design [slug]` iterates `40-solution-design.md` from the lowest layer above it, the intent alone, the assignment, the BRD or the user stories. Whether one is worth writing is yours to say; the ways in: no design yet, a layer above that moved, the thing changed below, a wording fix. Every pass makes the coverage map. What cannot be realised goes back to the intent as a thread. `/challenge <persona> solution-design` is offered once the design stands; the persona `architect` exists for it. One worked example, generic.
- inputs:
  .claude/skills/forge/states/solution-design.md
  templates/solution-design.md
- links:
  `docs/about/the-solution-design.md`: what a solution design holds.
  `docs/use/challenge-the-thinking.md`: the challenge of the design.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no shape of a SOL item beyond one sentence; no item of the forge's own design.
- made: mirrored
- state: regenerate

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
- says: `/ingest [file] [slug] [--bundle name]`: with a file, that document; with text pasted into the conversation, the text as `sources/<slug>.md`; with `--bundle <name>`, the file into a bundle of one origin that keeps arriving, born at its first file, each file immutable from its own registration; bare, a sweep for unregistered files and a report of files changed since registration. Personal matter stops the command before storing. Every binary gets one question, convert to Markdown? Yes: `scripts/doc2md.py` makes the extract, which is then the source; no: the binary is the source as a functional thing. A related set that arrives whole is a bundle with its own index. Before the index entry is written Claude asks what the source is for; the answer is its Role, or Claude infers it on your word and marks it so. The entry carries the source's date, best effort and never asked, and its form. A document of another project, a library's among them, is cited by path in an entry and not copied; the ledger finds the citation by itself. Registration is not intake. The reply is two lines at most. One worked example, generic.
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
- must-not: no example file with a real name; no ledger column detail; nothing of the skill as an instruction to Claude; no example of a real bundle (issues, minutes of a named body).
- made: mirrored
- state: regenerate

### docs/use/research-a-topic.md
- title: Research a topic
- line: How do you get a planned, checked and indexed research with `/research`, quick or deep, on one model family or two?
- kind: how-to
- reader: user
- says: `/research [--quick | --deep [--engine <name>]] <topic> [slug]`. Two depths: `--deep` is a plan of several cards and a bundle `research/YYYY-MM-DD-<topic>/` with the plan and the synthesis at its head and one note per card per engine; `--deep --engine antigravity` adds a second engine of another model family, which reads the draft plan and answers every card on the same packet; `--quick` is one card answered on the session model alone and filed as one note. Without the word Claude proposes the depth with its reason, and you decide. What happens, step by step: Claude asks what the research serves and what you already know or want left out, one question per message, and names the notes and sources it will build on; it drafts the plan (purpose, perspectives, assumptions with a premortem, what is left out, the cards, each one question with why it matters, what would answer it, where to look, a disconfirming query and a stop rule); with a second engine, its additions to the plan are shown beside the draft and marked as the engine's; a walkthrough of the plan, perspectives first, then the cards, `(m)odify` the normal verdict on a card; nothing is searched and nothing written until you confirm, and on your word the bundle is born with its plan; Claude tells you the models and the number of runs before it dispatches; each card is searched apart from the conversation; every note is checked against its shape, scanned for instance facts and has every URL it cites opened by `python scripts/forge-cite.py <note>` before it is filed, a note with a dead or mismatched citation sent back once; with two engines, how independent the two notes of each card are is measured by `python scripts/forge-cite.py --independence <bundle>`; the synthesis follows, with Claude's own view last and apart; a second round only for gaps the notes name, on your word, no third; one index entry for the bundle, the ledger remade. A quick research shows its one card with the verdict line before anything is searched. An engine named but unusable (not on PATH, not signed in, quota spent) is said in one sentence with the script's reason and the research goes on without it. What you see at the end: a report leading with what the research says and where the engines differ; a change to an artefact proposed through `/forge <state>`, never made silently. The run folder `tmp/research/<run>/` stays for inspection and is no source of truth. One worked example, generic.
- inputs:
  .claude/skills/research/SKILL.md
  templates/research-plan.md
  templates/research.md
  templates/index.md
  scripts/forge-engine.py
  scripts/forge-cite.py
- links:
  `docs/about/the-research.md`: why a research is planned before it is searched and how what it found is kept honest.
  `docs/about/another-model-family.md`: what the second engine is, how it is reached and how its independence is measured.
  `docs/reference/research-bundle.md`: the shape of a note, a bundle and its plan.
  `docs/about/sources-and-research.md`: what research is for and why it is immutable.
  `docs/start/install.md`: what a second engine needs on the machine.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no agent's brief copied; no subagent, agent type or model named; no profile, envelope or hold folder internals beyond one clause; no topic, bundle or note of the forge project; no date, probe or trial from the headers; no script flags beyond the two forms of `forge-cite.py` named; no vendor or model family named beyond the engine `antigravity`.
- made: mirrored
- state: regenerate

### docs/use/compose-a-recipe.md
- title: Compose a recipe
- line: How do you compose or iterate a render recipe by genre with `/recipe`?
- kind: how-to
- reader: user
- says: `/recipe [genre] [slug]`: bare, the roster of genres with the project's existing recipes; with a genre, a guided composition through its checklist, closing with the language question (one language, or several where the genre allows a primary and its translations; the project's language is proposed from its project file and never assumed), the recipe composed from the genre's skeleton; with the name of an existing recipe, an iteration. A recipe outside any genre is composed from the base skeleton. Versioned 0.x with its history companion, an integer only where you name one; `/render <recipe>` offered next. The five genres of today in one line each: presentation, readme, release-notes, screenplay, user-stories-export. One worked example, generic.
- inputs:
  .claude/skills/recipe/SKILL.md
  .claude/skills/recipe/genres/presentation.md
  .claude/skills/recipe/genres/readme.md
  .claude/skills/recipe/genres/release-notes.md
  .claude/skills/recipe/genres/screenplay.md
  .claude/skills/recipe/genres/user-stories-export.md
  templates/recipe.md
  CLAUDE.md#Versioning & status
- links:
  `docs/about/renders-and-recipes.md`: why the recipe is iterated and the render never edited.
  `docs/reference/recipe-genres.md`: each genre's checklist in full.
  `docs/use/render-an-output.md`: generating the render.
  `docs/use/make-a-video-from-a-recipe.md`: the screenplay genre from recipe to played video.
  `docs/use/write-user-stories.md`: the stories the export genre renders.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no checklist reproduced; no Format section detail beyond its existence; not the parenthesis of the release-notes genre that the forge's own recipe reads the intent alone; nothing of Versioning & status beyond the sentence on a recipe's version; no product name of a wiki or a tracker; no source file of the forge project named.
- made: mirrored
- state: regenerate

### docs/use/render-an-output.md
- title: Render an output
- line: How do you regenerate a render, and its plain file, with `/render`?
- kind: how-to
- reader: user
- says: `/render <recipe> [slug]` regenerates a render from its recipe: the inputs read from disk (the ledger made first by its script where the recipe reads it), the Markdown generated in isolation from the recipe and its inputs alone, written to `renders/<recipe>.md` or the recipe's `output:` path, opening with provenance front-matter; where the recipe declares `languages:`, the primary render first and then one translation per language as a file of its own, `renders/<recipe>.<lang>.md`, scene for scene, nothing re-cut. Back in the session the file is scanned mechanically for instance facts (`python scripts/docs-check.py --file <render>`) and a hit is said aloud for you to judge; then the provenance is verified, and the ledger's Renders table reads it, nobody writing a row. Where the recipe has a `## Format` section the plain `.docx` or `.pptx` is made beside the render through pandoc, or for a screenplay the video or the player file through `scripts/md2video.py`, at the render or at the recipe's `output:`; a missing tool is said aloud and the render stands. Where a published file of the recipe exists, you are told it is now older than its render. Regenerated only on this command or by `/release`. The render and its plain file are never edited by hand; a file you make yourself from them and keep in `renders/` under a name of its own (an edited copy, a PDF saved by hand) is yours, kept in git and left alone by the forge (one sentence, link). One worked example, generic.
- inputs:
  .claude/skills/render/SKILL.md
  scripts/docs-check.py
  projects/forge/10-intent.md#POS.1910
- links:
  `docs/reference/render-provenance.md`: the front-matter block and the one definition of stale.
  `docs/use/publish-a-designed-file.md`: the designed file, made through a model.
  `docs/use/make-a-video-from-a-recipe.md`: the screenplay's formats in full.
  `docs/about/renders-and-recipes.md`: why a render is generated and never a source of truth, and what becomes of the principal's own files beside it.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no subagent prompt text; no provenance block (reference); no script options beyond `--file`; no render of the forge project named; no version on a branch in a provenance, which is not built; no reasons for the principal's own files beyond the link.
- made: mirrored
- state: regenerate

### docs/use/make-a-video-from-a-recipe.md
- title: Make a teaching video from a recipe
- line: How do you turn real sessions into a screenplay and into a video or a player file with `/recipe screenplay` and `/render`?
- kind: how-to
- reader: user
- says: The job from end to end: register the session records as sources (`/ingest`) and write the brief of the videos; `/recipe screenplay` composes the recipe through its checklist (audience, the one message, the beats pinned by time of day, the quotes, the length, the title card, what must not appear, the languages with the primary first, the pace and the look, the format `video` or `html-player`, and for the player format whether the file goes out to the engine's `docs/videos/` by `output:`, its section of the course and its name); `/render <recipe>` writes the screenplay, one render per language, and makes the format file through `python scripts/md2video.py` with the pace, the date and, for the player, the section and the name the Format section names: an MP4 beside the render, or a `<recipe>.<lang>.html-player.js` beside the render or in `docs/videos/`, where the script renews the player page's list of files. A file sent to `docs/videos/` is read by you before the engine is saved; a video kept for the company names no `output:`. `/publish` has no part. What you see at each step; the script's messages under "If something goes wrong". One worked example with `<recipe>` and placeholder languages.
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
- must-not: no recipe, render or video of a real project; no course address (the start pages carry it); no name of a person; no reasons beyond one sentence each; no project slug from the script's examples (use `<slug>`); no section name of the forge's own course.
- made: derived
- evidence: the genre file gives the checklist and the product; the skeleton the recipe's shape, the Format section and where the player file lands; the render skill steps 3, 4 and 7 the languages, the `output:` into `docs/videos/`, the section and the name for the player and the run of the script; the script's header its synopsis, the two formats, where the output lands, the renewal of the player page and what it needs; POS.1540 that the file is read by the principal before the engine is saved and that a company video stays in `renders/`. The page joins them into one job in the order the person does it.
- state: regenerate

### docs/use/publish-a-designed-file.md
- title: Publish a designed file
- line: How do you make the designed Word or PowerPoint file with `/publish`?
- kind: how-to
- reader: user
- says: `/publish <recipe> [slug]` makes the designed `.pptx` or `.docx` from the render as it lies on disk, through a model and its document skills, into `published/`: started by you only, never by `/render`, `/release` or Claude's own judgement; on `main` only, and refused for a repository behind or diverged from its origin, with `/pull` offered; expensive and minutes long, said in one line before it runs. It never renders: a stale render is named first and the word is yours. A recipe without a `## Format` section ends at the Markdown; a screenplay has no published file. After the run a companion `published/<recipe>.md` records what the file was made from; the ledger's Published table reads it and shows the file `current`, or `stale` once its render is newer. A failed run writes no companion. The designed file is never edited by hand: what you want to change you copy first under a name of your own, and that copy, or a PDF you save from Word or PowerPoint, is yours, kept in `published/` with no companion and no check (one sentence, link). One worked example, generic.
- inputs:
  .claude/skills/publish/SKILL.md
  templates/ledger.md#Published
  projects/forge/10-intent.md#POS.1910
- links:
  `docs/use/render-an-output.md`: the Markdown and the plain file that come first.
  `docs/reference/render-provenance.md`: the published companion and the definition of a stale render.
  `docs/reference/scripts.md`: `md2pptx.py` and `md2docx.py`, the `claude` engine and what it needs.
  `docs/about/renders-and-recipes.md`: why the forge's files are never edited by hand and what the principal's own files beside them are.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no model name as a recommendation; no script options beyond `--engine claude`; no reasons for the principal's own files beyond the link.
- made: mirrored
- state: regenerate

### docs/use/generate-the-documentation.md
- title: Generate the documentation
- line: How does `/document` make the pages and the index, and what do you get at the end?
- kind: how-to
- reader: user, extender
- says: `/document [slug]` generates the documentation in one run that asks nothing: bare, the engine's into `docs/` with the map beside the ledger of `projects/forge`; with a slug, that project's into `projects/<slug>/docs/`, the map beside the project's ledger, the planner reading the project's briefs, intent, threads, the layers below the intent, its ledger, the indexes of `sources/` and `research/`, its recipes and whatever its documents point to on disk, and nothing a project would set for itself; the pages are written in the project's language, as its artefacts are. It runs on `main` only and refuses a repository behind or diverged from its origin, offering `/pull`. The steps in the person's terms: the previous map is taken from git into the engine's working folder `tmp/`; a planner reads the target on disk and writes the map, its task naming the open findings of the last documentation report that concern the map; a script computes every page's state from the content of its inputs and of the rule the pages are made by (new, regenerate, keep, remove) and writes one task per page; pages that lost their entry are deleted; Claude says how many pages it is about to make and on which models before it launches the writers; one writer per page makes it from its entry and inputs alone; a script derives the index; a script checks every page, a failing page regenerated once and one that fails twice left out. `docs/videos/` of the engine is not the documentation's and is left alone. What you get at the end: the counts, the check's result, the ledger remade so that its Renders table carries the index, and what the run could not place filed as a report of the run in `reviews/` under the name of a check, one finding per matter: a fact no file owns, a matter the map and an owner disagree on, a claim the map asked for and no input carried, every place where a writer wanted a reason and none is recorded; its findings are settled by walkthrough as a check's are, a mend landing in the file that owns the matter and never on a page, and a run that leaves nothing files nothing. A release never runs it on its own judgement: by hand it reports the index's age against the intent's version and offers the command; with `--auto` it asks once before anything runs, the default yes. One worked example of the closing report, generic.
- inputs:
  .claude/skills/document/SKILL.md
  .claude/agents/docs-planner.md#What you read
  .claude/skills/docs-contract/SKILL.md#What must never reach a page or the map
  .claude/skills/release/SKILL.md
  scripts/docs-state.py
  scripts/docs-index.py
  scripts/docs-check.py
  projects/forge/10-intent.md#REJ.0500
- links:
  `docs/about/the-documentation.md`: what the documentation is, for whom, and why it is generated.
  `docs/extend/change-a-documentation-page.md`: how a page is changed through its owners.
  `docs/use/check-conformance.md`: how a report's findings are settled by walkthrough.
  `docs/use/release-a-version.md`: the release that reports the documentation's age and offers the run.
  `docs/reference/scripts.md`: the three documentation scripts with their options.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no agent prompt or task text; no model name; no field of the map; no page count or date of a run; no finding of the forge project; nothing of the check script's `--file` mode; nothing of the release skill beyond what it does with the documentation; nothing of the contract beyond the language of the pages; nothing of REJ.0500 beyond what a project's planner reads, not the help command it rejects; no thread number.
- made: mirrored
- state: regenerate

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
- says: How any list that needs your decision is worked: one item per message, in order of weight; what an item carries; the proposition closing with `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark`, answered with a single letter or the word; `question` asks about the open item and changes nothing, Claude answers and closes the item again; `obsolete` as a further verdict. The verdicts are carried and written once at the round's end on `write`, Claude reflecting the whole round back first; `accept` writes what the producing command says and a closing record; `reject`, `park` and `obsolete` each write a decision with your reason and its verdict line, and a rejected item is not raised again; the ledger is made afresh after the write. The elicitation interview runs the same way. The same line closes every question of Claude's that asks you to decide, in a walkthrough or outside it (a step that needs your consent, a choice between options, an either/or, whether to write): it is one proposition with Claude's recommendation as what `accept` means, and a yes that carries a question is `question`; only a question for information Claude lacks ends with the question alone. One worked example of one item, generic.
- inputs:
  .claude/skills/walkthrough/SKILL.md
  CLAUDE.md#Working methods
- links:
  `docs/reference/verdict-words.md`: the words and letters, exactly.
  `docs/about/working-methods.md`: why the one-item rule exists and how a hook holds it.
  `docs/use/settle-a-conflict.md`: the conflict of a save, laid out one conflict per message in the same way.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no hook text; nothing addressed to Claude; no record or decision line copied from a template; nothing of the Working methods beyond the Walkthrough, the Elicitation interview and the verdict line of Step by step; no date the skill carries.
- made: mirrored
- state: regenerate

### docs/use/save-your-work.md
- title: Save your work
- line: What does `/save` check, ask and commit?
- kind: how-to
- reader: user
- says: `/save [slug] [-m "message"] [--tag name] [--quick]`: the scope from the status script, each repository with the branch it is on; the `light` check on every repository in scope, settled through `/check`, a save never waiting on a finding you have not asked to fix, and going on, said aloud, where the ledger script cannot read a file; `--quick` leaves the check out and nothing else; a one-line commit message drafted from the round's history records and confirmed, or `-m`; a tag only on your word, any name git accepts; then the save script, which commits and pushes on whatever branch is checked out, no render. Where the remote's branch has moved on as well, the histories diverged, the script integrates the remote changes first by rebasing your commits onto them; a branch that is merely ahead, a merge you made by hand among its commits, is pushed as it stands, so that the merge keeps its merge commit. It pushes a clean repository that is ahead of its origin, a branch with no upstream yet included; a rebase that conflicts is left standing, the commit made and nothing lost, the files in conflict and the step that follows printed, and the session goes on with the step of a conflict and saves again (one sentence, link); a repository with a rebase or a merge already in progress is refused before anything is staged, and the refusal names the step; without an origin the commit stays local; where git resolves no identity it commits nothing. A bare save commits every repository with changes, so with two windows open the slug narrows it to the one you work in. A save never runs the engine's tests. One worked example, generic.
- inputs:
  .claude/skills/save/SKILL.md
  scripts/forge-save.py
  scripts/forge-status.py
  projects/forge/40-solution-design.md#SOL.0530
  .claude/skills/test/SKILL.md
- links:
  `docs/use/release-a-version.md`: the other door, from `main`, with the renders.
  `docs/use/settle-a-conflict.md`: what to do when the save stops on a conflict.
  `docs/use/end-a-session.md`: the end of a session, which names what is unsaved.
  `docs/about/persistence-in-git.md`: why there are two doors and two speeds.
  `docs/about/working-together.md`: why a merge made by hand is pushed as it stands.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no git command typed by you (the finishing commands of a conflict are the conflict page's); no example message from the forge project; no slug from the script's examples (use `<slug>`; `forge` may stand); no tag name from the script's examples; no pull request or contributor the script's comments cite; nothing of the tests beyond that a save never runs them.
- made: mirrored
- state: regenerate

### docs/use/settle-a-conflict.md
- title: Settle a conflict
- line: What do you do when `/save` stops on a conflict with the remote, or a merge leaves one?
- kind: how-to
- reader: user
- says: When to use it: a save whose rebase of your commits onto the remote conflicts, or a merge of a branch that git leaves in conflict; the merge itself is git's, made by hand on your own clone outside the forge's scripts, or by a merge request where it needs no hand. What you see first: the save script has made the commit, left the rebase standing, and printed the files in conflict and the step that follows; `python scripts/forge-status.py` says a rebase or a merge is in progress and how many files are in conflict; a further save is refused before anything is staged until the step is finished, so that conflict markers are never committed. The step, as a walkthrough: Claude reads both sides and puts one conflict per message in front of you with its proposition, and you give the verdict; at the round's end Claude writes the chosen wording into the file, and for an artefact a `changed` record into its history as for any change; a conflict in a history, in `decisions.md` or in a resource index is two tails appended after one last line and is settled by keeping both. The commands that finish the step, `git add <file>` and `git rebase --continue` (`git rebase --abort` to give it up; `git merge --continue` or `--abort` after a merge; `git merge <branch>` with one name for a merge Claude is asked to start), are put to you by the hook and run on your yes. Then `/save` again, which pushes the clean repository that is ahead. Where both sides raised one document to the same version, git merges the header's `version:` line silently when both wrote the same number and shows the clash at the end of the history, where both sides appended records, and the merged document takes the next number with one `changed` record naming the merge, the records of both sides keeping their numbers; an item number taken twice is renumbered as the stable IDs page says (one sentence, link). One worked example: a generic conflict in one artefact and in one history.
- inputs:
  CLAUDE.md#Persistence (git)
  scripts/forge-save.py
  scripts/forge-status.py
  scripts/hook-git.py
  .claude/skills/walkthrough/SKILL.md
  projects/forge/40-solution-design.md#SOL.0840
  projects/forge/10-intent.md#POS.1790
- links:
  `docs/use/save-your-work.md`: the save that stops on the conflict and the save that follows it.
  `docs/use/walk-through-a-list.md`: the one-item-per-message shape the step runs in.
  `docs/about/working-together.md`: what the forge promises two people on one project and how each kind of file merges.
  `docs/about/stable-ids.md`: how an item number taken twice is settled.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no git command beyond the finishing commands the hook asks for and the step the save script prints; no `/merge` command and no merge driver of the forge's own, which the forge does not have; no test, plan, fixture or brief of the forge project; no slug from the scripts' examples (use `<slug>`); no date; no claim that the ledger reports a version given twice; no pull request or contributor the script's comments cite.
- made: derived
- evidence: CLAUDE.md, Persistence gives the conflict left standing, the merge as git's made by the integrator on his own clone outside the forge's scripts, the step with Claude laying both sides out and the principal deciding, the finishing commands on the hook's ask and the record files merged as text with two tails kept; the save script's header what is printed, the refusal of a standing rebase or merge and the push of a clean repository that is ahead; the status script what it says of a rebase in progress; the hook's header which commands are asked, `merge <branch>` with one name among them; the walkthrough skill the shape of the step; SOL.0840 the `changed` record into the artefact's history and the step as a walkthrough; POS.1790 the version given twice, found by git as a conflict of the two history tails, the version line merging silently. The page joins them into one job in the order the person meets it.
- state: regenerate

### docs/use/release-a-version.md
- title: Release a version
- line: What does `/release` run, render and tag, in what order, and what does `--auto` decide on its own?
- kind: how-to
- reader: user
- says: `/release [slug] [-m "message"] [--tag name] [--auto]` releases one repository from `main` only, refusing another branch with the way back and a repository behind or diverged from its origin with the offer of `/pull`. The order of every release: for the engine the tests first, through `/test`, before any check or agent runs, a red test stopping the release with the failures as `/test` reports them, and pytest missing said so and passed only on your word, a project's release running no tests; then the checks (`light` and `project` for a project; `engine`, `light` and `project` for the engine) settled by walkthrough, a finding you have not settled when you order the release to go on parked by that word; `critique essence` offered once; the age of the documentation reported against the intent's version and `/document` offered, run on your word before the renders so that the README reads the current index; the README and the release notes regenerated through `/render` with a summary of what materially changed; then the state render, the ledger written as the tracked file `renders/state.md`; then `/save --quick`, without a second light check, with the message `release <intent version>: <one line>` and, at an integer version, the tag `v<major>` on your word, Claude first naming what the forge's own intent asks a major to pass. With `--auto` the release runs through and stops only at a serious thing: it asks once, before anything runs, whether the documentation runs, the default yes; it stops at a red test and at a missing pytest alike; the checks and every run of agents run without asking, the model and the size said as information; a finding whose fix lies in the operating layer or in bookkeeping and changes no position and no rule's meaning is fixed and recorded by Claude, while a finding of severity high, one that would change a position or a rule's meaning, or one the report calls a decision stops the release; `critique essence` is neither offered nor run; the regenerated files are taken as they came, the one stop a hit of the instance-fact scan the released version did not already carry; the drafted message is used and said aloud; the tag of a major is never taken by `--auto`, the release stopping before it and asking. The check is advisory. One worked example, generic.
- inputs:
  .claude/skills/release/SKILL.md
- links:
  `docs/use/save-your-work.md`: the save the release ends with.
  `docs/use/run-the-tests.md`: the tests a release of the engine runs first.
  `docs/use/check-conformance.md`: the checks and how their findings are settled.
  `docs/about/renders-and-recipes.md`: why the README and the release notes are renders.
  `docs/use/generate-the-documentation.md`: the command the release offers and, with `--auto`, asks about once.
  `docs/about/versioning-and-history.md`: what a major approves.
  `docs/about/persistence-in-git.md`: why there are two doors and two speeds, and why a release is made on `main` only.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no version number of the forge; no description of what a major must pass beyond the pointer; no claim that the release regenerates the documentation on its own judgement; no sample release or date; no brief of the forge project named.
- made: mirrored
- state: regenerate

### docs/use/pull-from-the-remote.md
- title: Pull from the remote
- line: How does `/pull` look at the remote, and what does it pull and refuse?
- kind: how-to
- reader: user
- says: `/pull [slug]` (bare: the engine and every project with an origin; `forge`: the engine). First the state of each repository against its origin as a fact (up to date, behind, ahead, diverged, no origin, not under git), and beside it what waits on GitHub outside git, the open pull requests and the unanswered discussions, or the one line saying it could not read them and why, nothing of it pulled, merged or answered; a repository with unsaved changes or a diverged history stops with its one offer, nothing pulled: `/save` first, or a merge by hand, or `/save`, which rebases your commits onto the remote. For what is clean and behind the pull script fast-forwards and reports where each repository moved from and to and the commits between. After a pull of the engine the Action required lines of the releases crossed are shown and the two checks offered per project; where an Action required line names a migration, `/migrate <slug>` is offered for each project of the old shape. The forge never pulls or merges on its own. The scripts' refusals under "If something goes wrong". One worked example, generic.
- inputs:
  .claude/skills/pull/SKILL.md
  scripts/forge-pull.py
  scripts/forge-status.py
- links:
  `docs/use/upgrade-the-engine.md`: what to do after a pull of the engine.
  `docs/use/migrate-a-project.md`: the migration a release may ask for.
  `docs/use/save-your-work.md`: the save that must come first on unsaved work.
  `docs/use/settle-a-conflict.md`: what to do when the save of a diverged repository meets a conflict.
  `docs/about/persistence-in-git.md`: why the forge looks at the remote and offers.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no git command; no slug from the script's examples; no version numbers; no `/merge` command, which does not exist; no pull request, discussion or number of the forge project.
- made: mirrored
- state: regenerate

### docs/use/upgrade-the-engine.md
- title: Upgrade the engine
- line: How do you take a new version of the engine and bring your projects to its conventions?
- kind: how-to
- reader: user
- says: The job after a pull of the engine: read the Action required lines `/pull` showed, which stand first in every section of the release notes; then, project by project, `/check light <slug>` and `/check project <slug>` measure the project against the current conventions, the findings are walked one at a time and Claude brings the project current on your word. Where a release changed the shape of files, its Action required line says so: each project of the old shape is migrated once with `/migrate <slug>` on one clone, on `main`, and saved, the migrated shape reaching the remote by that save, and everyone else pulls the migrated project. Projects record no engine version and the pull does not touch them; a project left as it is stays valid under the conventions it was written to, though one of the old shape is read and not written until it is migrated. One worked example, generic.
- inputs:
  .claude/skills/pull/SKILL.md
  .claude/skills/migrate/SKILL.md
  projects/forge/10-intent.md#POS.0940
  projects/forge/10-intent.md#POS.0820
  projects/forge/recipes/release-notes.md#Instructions
  CLAUDE.md#Persistence (git)
- links:
  `docs/use/pull-from-the-remote.md`: the pull itself.
  `docs/use/check-conformance.md`: running a check and settling its findings.
  `docs/use/migrate-a-project.md`: the migration of a project to a new shape of files.
  `docs/about/upgrades-and-migration.md`: why a project records no engine version and when a migration comes with a release.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no version numbers; no history of past migrations; no repository address; nothing of the release-notes recipe beyond that Action required stands first in every section and carries a record's Action word for word; no reasons beyond the link.
- made: derived
- evidence: the pull skill's step 3 gives what follows a pull of the engine and the offer of `/migrate`; the migrate skill that a migration runs once per project, on one clone, on `main`, everyone else pulling, and that the migrated shape reaches the remote by the save it proposes; POS.0940 that a project records no engine version, the migration path through the two checks with Claude migrating on the user's word and a migration for a release that changes the shape of files; POS.0820 that an artefact stays valid under the conventions it was written to and that a project of the old shape is read, not written; CLAUDE.md, Persistence the one-clone rule as the operating layer has it; the recipe's Instructions that Action required stands first among the groups and carries the Action of a record. The page joins them into one job.
- state: regenerate

### docs/use/migrate-a-project.md
- title: Migrate a project
- line: How do you bring a project to the shape of files a new release expects, with `/migrate`?
- kind: how-to
- reader: user
- says: `/migrate [slug]` (`forge` is the engine's own project) runs once per project, on one clone, on `main`, when a release changed the shape of files; everyone else pulls the migrated project. What happens, step by step: Claude runs the dry run, `python scripts/forge-migrate.py <slug>`, and shows its print as it came: the marks of the shape, the steps that would run and what each would change; a project already in shape ends there. Before the migration a tag is taken, `/save <slug> --tag <name>`, the way back once the migrated project is saved. On your word, and only then, the script runs with `--apply`: the fields that change with a round leave the headers, the project file is written, what only the ledger knew becomes records and index fields, the hand-kept ledger is kept as an immutable archive and the ledger leaves git, the threads file is cut into one file per thread, the `.gitattributes` is written; a library takes fewer steps. The script commits nothing. Then Claude walks through what the script printed for your judgement, above all the origin it guessed for each thread, as a walkthrough written into the thread files at the round's end; text that was not a thread goes where it belongs. Then the ledger is made and `/save <slug>` proposed; the migrated shape reaches the remote by that save. The way back before the save is `python scripts/forge-migrate.py <slug> --undo`; after it, the tag taken before. A project outside git is migrated the same, with none of git's refusals: you take a backup before `--apply`, as the dry run tells you, that backup is its way back, `--undo` refuses there, and a run that stops midway is finished by running it again. The refusals under "If something goes wrong": for a project that is a repository of its own, unsaved changes to tracked files, a branch behind or diverged from its origin, any branch but `main`; for every project, an instance file without the `Author` line. One worked example with `my-idea`.
- inputs:
  .claude/skills/migrate/SKILL.md
  scripts/forge-migrate.py
  templates/project.md
- links:
  `docs/use/upgrade-the-engine.md`: the upgrade a migration belongs to.
  `docs/about/upgrades-and-migration.md`: why a shape change comes with a migration and why it runs once.
  `docs/use/save-your-work.md`: the save that takes the tag before and carries the migrated shape to the remote after.
  `docs/use/walk-through-a-list.md`: how the guessed thread origins are judged.
  `docs/reference/scripts.md`: `forge-migrate.py`, its forms and what it needs.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no slug from the script's examples (`fixture` and the like; use `<slug>` or `my-idea`); no name of a release or of a brief of the forge project; no conversion to one sentence per line, which is not built; no manifest path or file name of the script's internals; no git command for the way back from the tag after the save; no reasons beyond the link.
- made: mirrored
- state: regenerate

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
- must-not: no git command; no content of a real session; nothing of the status script's line on GitHub, which `/end` does not ask for.
- made: mirrored
- state: regenerate

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
- state: regenerate

### docs/use/work-on-a-branch.md
- title: Work on a branch
- line: How do you switch a repository to a branch without typing git?
- kind: how-to
- reader: user
- says: Branches are voluntary: `python scripts/forge-branch.py <slug> <branch>` switches the repository to the branch, creating it when it does not exist, `main` switching back; with the slug alone it reports the branch and lists the branches (`forge` means the engine). Unsaved changes stop a switch. Merging, deleting and pushing branches stay with git: a new branch reaches the remote by the first save made on it; a release, a documentation run and a publish are made from `main` only. One worked example with `<slug>` and `<branch>`.
- inputs:
  scripts/forge-branch.py
  .claude/skills/release/SKILL.md
- links:
  `docs/use/save-your-work.md`: the save that carries a branch to the remote.
  `docs/about/persistence-in-git.md`: why merging is left to git.
  `docs/about/working-together.md`: how a contributor's branch reaches the integrator.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no git command other than through the script; no branch name or slug from the script's examples other than `forge` and `main`; no worktree, `--done` or `/merge`, which are not built.
- made: mirrored
- state: regenerate

### docs/use/spin-off-a-group.md
- title: Spin off a group
- line: How does `/spinoff` make a requirement group a project of its own?
- kind: how-to
- reader: user
- says: `/spinoff <project> <group> <slug>` splits a requirement group of an assignment into a project of its own, only on your explicit instruction: the items to move confirmed; the new project created by the `/new-project` procedure; a short brief derived from the source intent, approved on your word; mined into the new intent, the mining recorded in that intent's history; in the source project the intent records the spin-off first and the assignment marks the moved items superseded and replaces the group with one link item; the command itself writes the decision; both ledgers are made afresh. Claude may propose readiness, never run it. One worked example, generic.
- inputs:
  .claude/skills/spinoff/SKILL.md
- links:
  `docs/use/start-a-project.md`: what the new project is made of.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no group or slug of an instance project.
- made: mirrored
- state: regenerate

### docs/use/look-up-a-command.md
- title: Look up a command, or ask how to do something
- line: How does `/man` print the manual of a command or a working method, and answer a need you say in your own words?
- kind: how-to
- reader: user
- says: `/man [command | method | question]`, alias `/manual`, is the forge's manual, read at the moment of the call from the files that own it; it runs nothing, writes nothing and decides nothing. Bare, it lists the commands and the working methods. With a command, its purpose, arguments, the roster it dispatches over with what each entry looks for, and the skill file. With a method, its paragraph and the skill that holds its shape. With anything that is neither, it takes your words as a need: Claude reads the documentation's index, where every page carries the one question it answers, chooses the pages that meet the need, asks once in one sentence where the need can be read two ways that lead to different pages, reads those pages (and the skill they name where the detail matters) and answers in plain sentences: the way the forge has first, with what you type; then what matters on that way; where several ways fit, one recommended with its reason; and plainly where the way leaves the forge (a repository to initialise, a program to install). The pages read are named by path at the end. Where the forge has nothing for the need, it says so, names an open thread of the forge's own project if one carries the need, and marks what Claude would do without a mechanism as his own. It prints in the conversation language, the notation staying English. The word `help` is Claude Code's own. One worked example of a command page and one of a question, generic.
- inputs:
  .claude/skills/man/SKILL.md
  .claude/skills/manual/SKILL.md
- links:
  `docs/reference/commands.md`: the same table of commands, as a page.
  `docs/use/generate-the-documentation.md`: the run that makes the index the manual reads to answer a question.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no copy of the Commands table; no thread of the forge project named; no second help command, which the forge does not have; nothing of the skill as an instruction to Claude.
- made: mirrored
- state: regenerate

### docs/use/share-material-through-a-library.md
- title: Share material through a library
- line: How do you keep material shared across projects in a library and cite it?
- kind: how-to
- reader: user
- says: A library is a project of kind `library`, prefix `lib-`, with no chain: the project file, its `.gitattributes` and `.gitignore`, `sources/` and `research/` with their indexes, and a readme recipe whose render is a catalogue; its ledger is made by the script like every project's. Born by `/new-project lib-<name>`; documents enter by `/ingest`; a changed document is the owner's maintenance; `/forge <state>` on a library says that it has no chain and stops. A project uses a library document by citing its path: `/ingest` adds an index entry that names the path, and the ledger finds the citation and lists it under Dependencies; a deck template or a Word reference document, typically a document of a library project, is named by path in a recipe's Format section and reaches the conversion scripts as the path they are given; the roster of areas a BRD walks is such a library document too (one sentence, link). The `/forge` map says which libraries a project needs and whether each is cloned alongside; a missing one is brought in with `/import-project`. One worked example with `lib-<name>`.
- inputs:
  .claude/skills/new-project/SKILL.md
  .claude/skills/ingest/SKILL.md
  .claude/skills/forge/SKILL.md
  .claude/agents/check-light.md
  CLAUDE.md#Repository layout
  templates/recipe.md
  scripts/md2pptx.py
  scripts/md2docx.py
  .claude/skills/forge/states/brd.md#Inputs
- links:
  `docs/about/projects-and-the-engine.md`: why a library is a kind of project.
  `docs/use/register-a-source.md`: the ingest the library shares with every project.
  `docs/use/bring-in-an-existing-project.md`: cloning a library that is missing alongside.
  `docs/use/write-a-brd.md`: the BRD that walks the instance's roster of areas, a library document.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no library name of an instance; no template file name of a company; nothing of the conversion scripts beyond that a template or a reference document is named by path.
- made: derived
- evidence: the library's file set is CLAUDE.md, Repository layout; what `/new-project` creates is its Every project and Library paragraphs; a changed document as maintenance is `/ingest`'s sweep paragraph; that `/forge <state>` on a library says so and stops is the forge skill's; citation by path, found by the ledger as a dependency, is `/ingest` step 6; the Format section's `template <path | none>` and `reference <path | none>` are `templates/recipe.md`'s, and that such a file is typically a document of a library project the headers of `md2pptx.py` and `md2docx.py`; the map's Dependencies line is `/forge` step 3; the missing-library finding is the light check's Dependencies clause; that the roster of areas a BRD walks is a library document of the instance, cited by path, is the BRD definition's Inputs block. The roster is the BRD page's; this page says one sentence.
- state: regenerate

### docs/use/run-the-tests.md
- title: Run the tests
- line: How do you run the engine's tests with `/test`, and what do you see when one is red?
- kind: how-to
- reader: extender, user
- says: `/test [pytest arguments]` runs the engine's tests from the engine root, `python -m pytest -q` over `tests/`, with whatever you give passed to pytest as it stands: `/test` the whole suite, `/test -k conflict` the tests whose name carries the word, `/test tests/test_git_scripts.py` one file, `/test -x` stopping at the first red test. The tests are the engine's, beside the scripts they test; a project has none, so the command takes no slug. What you see: the sum as pytest prints it, a line of the shape "N passed in M s"; a red test word for word as pytest printed it, the failing assertion included, and nothing fixed on this command's word: the fix is a round of its own, the script changed with its test. The tests run on copies of the fixture `tests/fixture` in a temporary directory and on no repository of the forge, so nothing of the engine or of a project changes. If something goes wrong: pytest not installed (`No module named pytest`) is said so, with the one thing a contributor installs beyond `python`, `python -m pip install pytest`. The same suite runs in CI at every push and pull request, on Linux and Windows, Python 3.8 and the newest; a release of the engine runs the tests before anything else and a red test stops it; a save never runs them. One worked example: one run with a placeholder sum, one red test as the shape pytest prints.
- inputs:
  .claude/skills/test/SKILL.md
  pytest.ini
  .github/workflows/tests.yml
- links:
  `docs/about/the-tests.md`: what is tested, what the fixture is and why the tests are in proportion.
  `docs/use/release-a-version.md`: the release that runs the tests first.
  `docs/use/save-your-work.md`: the save, which never runs them.
  `docs/extend/add-a-script.md`: changing a script with its test.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no count of tests as a fact (the sum is a shape with placeholder numbers); no content of a test file; no brief, decision or thread of the forge project named; no account or address of the CI.
- made: mirrored
- state: new

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
- must-not: no name or handle of the first principal or author; no company; no origin story beyond "it began as one person's tool, an instance fact"; no commands; no company rollout.
- made: derived
- evidence: CLAUDE.md gives the identity; the Essence and the positions the general engine, the amplifier, where a run ends, state in files, the name; the two REJ what was rejected.
- state: regenerate

### docs/about/how-a-thought-travels.md
- title: How a thought travels through the forge
- line: What happens to one idea from a rough brief to a saved release?
- kind: explanation
- reader: user, extender, evaluator
- says: One invented, generic thought followed through: it arrives as a brief; is chiselled into the intent by elicitation, rewritten for coherence every round; below the intent the project takes the layers it needs, an assignment, a BRD, user stories, a solution design, many ending at the intent; at every layer blind reviewers press on the documents and the thinking; research is planned and run where a position will rest on what the world already knows; outputs for every audience are generated through recipes, work products made beside them where the project needs work of its own, the documentation generated the same way; everything saved to git and released. Sources and research arrive at any stage. The main courses of events in one sentence each.
- inputs:
  CLAUDE.md#Document chain
  projects/forge/40-solution-design.md#How the parts work together
  projects/forge/10-intent.md#POS.0110
  projects/forge/10-intent.md#POS.0120
  projects/forge/10-intent.md#POS.0130
  projects/forge/10-intent.md#POS.1800
  projects/forge/10-intent.md#POS.1990
  projects/forge/10-intent.md#POS.1400
  projects/forge/10-intent.md#POS.0400
  projects/forge/10-intent.md#POS.1860
  projects/forge/10-intent.md#POS.0710
  projects/forge/10-intent.md#POS.0180
  projects/forge/10-intent.md#POS.1100
  projects/forge/10-intent.md#POS.1520
- links:
  `docs/about/the-document-chain.md`: the chain as a star.
  `docs/about/the-user-stories.md`: the stories, the layer between the BRD and the solution design.
  `docs/about/isolated-reviewers.md`: why the reviewers never see the conversation.
  `docs/about/the-research.md`: how a research is planned before it is searched.
  `docs/about/renders-and-recipes.md`: how an output is generated from the artefacts.
  `docs/about/the-work-product.md`: an output made with work of its own.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no command syntax beyond names in passing; no forge project detail; no version numbers; nothing of merging and conflicts beyond "saved to git" (the working-together page's); no position the design's head lists as answered by no part; nothing of the BRD or the stories beyond one clause each; no pull request or user the intent cites.
- made: derived
- evidence: CLAUDE.md, Document chain gives the chain; the solution design's head the main courses of events; the positions what each station is for, POS.1800 the BRD and POS.1990 the user stories among the layers, POS.1860 the research, POS.1520 the work product. The page tells it in the order a thought meets it.
- state: regenerate

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
- state: regenerate

### docs/about/working-methods.md
- title: The working methods
- line: What are the named ways a working conversation runs, and why each exists?
- kind: explanation
- reader: user, evaluator
- says: The forge's vocabulary of collaboration, none a command: Walkthrough, Propose never decide (and `??`), Step by step, Elicitation interview, In pieces, Draft early, Reflect back, One write per round (`write`), Intent-first, Handing over, Recommend do not push, Plain speech, Kind not count. For each, what it is in the operating layer's wording and why in the intent's: the one-item rule because text loaded once dissolves in a long conversation, which is why a hook repeats it with four lines of conduct at every prompt; `question` as a verdict so that a question is never mistaken for a yes; one write per round, because writing after every exchange buries the substantive change under churn; intent-first, because a lower layer that takes a change the intent does not carry drifts from it; step by step because consent is given to a concrete operation, a run of several agents arriving with the model and the size said, every such step closing with the verdict line so that the word is a letter and a yes that carries a question is a question; the same line closing every question that asks the principal to decide (a choice between options, an either/or, whether to write), only a question for information Claude lacks ending bare; handing over because the principal's attention is the scarce thing; plain speech; kind not count. Every list that needs a decision ends by offering a walkthrough. One worked example of a method invoked, generic.
- inputs:
  CLAUDE.md#Working methods
  .claude/skills/walkthrough/SKILL.md
  projects/forge/10-intent.md#Working methods
  projects/forge/10-intent.md#POS.1410
  projects/forge/10-intent.md#POS.0190
  projects/forge/10-intent.md#POS.0140
- links:
  `docs/use/walk-through-a-list.md`: the walkthrough as a procedure.
  `docs/about/elicitation.md`: the process the elicitation interview is one instrument of.
  `docs/reference/verdict-words.md`: the words the principal types.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no hook text; no dates or incidents of the intent's reasons; no project the methods were learnt on; nothing of the assistant's memory.
- made: derived
- evidence: CLAUDE.md, Working methods gives every method's name and wording, the verdict line of Step by step, the run of several agents and the questions that ask for a decision among it; the walkthrough skill the shape and the verdicts; the intent's group Working methods and POS.1410 the reasons, POS.0190 the reason of one write per round, POS.0140 the rule intent-first names. Where a method's reason no position gives, the page says the reason is not recorded. The page keeps CLAUDE.md's order.
- state: regenerate

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
- state: regenerate

### docs/about/the-document-chain.md
- title: The document chain
- line: Why is the chain a star of definitions, and how does it grow?
- kind: explanation
- reader: user, extender, evaluator
- says: The chain starts at a brief and its trunk is the intent; below the intent a project takes the layers it needs, none a condition of another. The chain is a star: each definition declares its own inputs, so a layer branches from any artefact by adding one definition, and the dispatcher never changes. Files numbered in tens. Which artefacts exist is the listing of the definitions directory. Substance changes go into the intent first. The chain never spans two principals. The diagram: the artefacts of today's chain with their inputs as the definitions declare them (the brief; the intent from the briefs; the assignment from the intent; the BRD from the assignment, or from the intent where there is none, a file someone gave yielding a work product instead; the user stories from the BRD, or from the intent for a small change, a requirements document of someone else yielding a work product; the solution design from the lowest layer above it, the intent alone, the assignment, the BRD or the user stories). One worked example, generic.
- inputs:
  CLAUDE.md#What this workspace is
  CLAUDE.md#Document chain
  .claude/skills/forge/SKILL.md
  .claude/skills/forge/states/brief.md#Inputs
  .claude/skills/forge/states/intent.md#Inputs
  .claude/skills/forge/states/assignment.md#Inputs
  .claude/skills/forge/states/brd.md#Inputs
  .claude/skills/forge/states/user-stories.md#Inputs
  .claude/skills/forge/states/solution-design.md#Inputs
  projects/forge/10-intent.md#POS.0100
  projects/forge/10-intent.md#POS.0140
  projects/forge/10-intent.md#POS.0580
  projects/forge/10-intent.md#POS.0700
  projects/forge/10-intent.md#POS.1400
- links:
  `docs/about/the-brief.md`: the first artefact.
  `docs/about/the-intent.md`: the trunk.
  `docs/about/the-brd.md`: the business requirements below the assignment.
  `docs/about/the-user-stories.md`: the stories below the BRD.
  `docs/about/elicitation.md`: what a definition is.
  `docs/reference/artefacts.md`: the definitions of today, one row each.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no planned layer drawn as if it existed; no forge project history; no library path or company of an instance; no thread number from a definition's Inputs.
- made: derived
- evidence: CLAUDE.md gives the trunk, the growth and the numbering; the `/forge` skill the star; the Inputs blocks the arrows of the diagram; the positions the reasons. Where no input gives a reason, the page says the reason is not recorded.
- state: regenerate

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
- state: regenerate

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
- state: regenerate

### docs/about/the-assignment.md
- title: The assignment
- line: What makes an assignment complete, and where does assigning end and solving begin?
- kind: explanation
- reader: user, evaluator
- says: An artefact page: the assignment carries the in-scope substance of the intent to the recipients, complete and precise. Complete means nothing left to assumption: delegated or open on purpose is complete, silent is not. It assigns and does not solve, the boundary being the kind of content never its amount. Items with stable IDs, each an obligation in the indicative, no priorities, testability recommended, success criteria wanted not compulsory; in English the obligation is shall and shall not, strictly, and an artefact in another language uses that language's own verb of obligation under the same rule of kind, the forge naming no word of any other language; why an obligation in the indicative and not a conditional, a permission, a wish or MoSCoW, and why the verb follows the language of the artefact rather than being kept in English and translated by a render. Why a joint pass of three phases. Why the name. One worked example: a generic requirement item.
- inputs:
  .claude/skills/forge/states/assignment.md
  templates/assignment.md
  projects/forge/10-intent.md#POS.0130
  projects/forge/10-intent.md#Structure and style of an assignment
  projects/forge/10-intent.md#POS.0250
  projects/forge/10-intent.md#POS.1350
  projects/forge/10-intent.md#REJ.0050
  projects/forge/10-intent.md#REJ.0060
  projects/forge/10-intent.md#REJ.0120
  projects/forge/10-intent.md#REJ.0540
- links:
  `docs/use/distil-an-assignment.md`: the joint pass as a procedure.
  `docs/about/stable-ids.md`: why every item carries an ID.
  `docs/about/languages.md`: which language an artefact is written in.
  `docs/reference/requirement-style.md`: the rule set.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no rule set reproduced; no item of an instance project; no spin-off mechanics; nothing of the ID group's merge clash or blocks of IDs, which are not built; no group or company standard named; no language, project or wording the position cites as the case that changed the verb rule; no thread number or date.
- made: derived
- evidence: the definition gives the wording, the Requirement style and the two "why not"; the positions the reasons, POS.0250 the obligation in the indicative, shall in English, the language's own verb elsewhere and why; the four REJ what was rejected, REJ.0540 why the verb is not kept in English and translated by a render.
- state: regenerate

### docs/about/the-brd.md
- title: The BRD
- line: What does a BRD hold, how does it start, and why does the forge name what it cannot know instead of writing it?
- kind: explanation
- reader: user, extender, evaluator
- says: An artefact page. What it is: the business requirements, `30-brd.md`, below the assignment and above the solution design; it breaks its parent into rules the stakeholders of each area review on their own, behaviour that must be agreed as a sequence, and qualities with values from the stakeholders, so that the delivery can estimate and the solution design can start. Who writes and reads it: an analyst working as the principal of his own project, with Claude as partner doing the recast; the stakeholders and the delivery teams read it. Made from: the assignment, read with the intent and the threads, or the intent alone where there is none; a file someone else gave is a third way in and yields a work product, never the artefact, since what someone said does not become the principal's position by being run through a command; around the parent the decisions, the ledger, the resource indexes of the project and of its libraries, and the roster of the instance, a library document cited by path that names the areas of the enterprise a BRD must consider and which of them are mandatory, a project with no enterprise around it having none and writing `Roster: none`. What it holds: four prefixes of its own (BR a business requirement, UC a use case at user-goal level, DEP a dependency, NFR a quality by category) beside OOS, ASM, TBC and SCR; the stakeholders as roles, the scope of the document, the touched areas of the enterprise walked against the roster, the phasing always stated, the terms, a traceability appendix; every BR and UC cites its parent; an open question is defined once, in Open questions, and an item whose rule is not known cites it in brackets; the Requirement style is the assignment's made stricter. Complete when nothing of the parent is left out in silence, every matter that must come from outside has its owner, and no open question that blocks estimation remains. How it is found: found together or drafted automatically on the principal's word, from a provenance map first. What the forge cannot know, it names: the suppliers' and systems' documentation, the standards and regulation, what the operations know are brought by the analyst; Claude writes none of it from imagination and puts a DEP or a TBC with an owner in its place, and the pass ends with the list of what must be supplied from outside. The reviewers: no lens of its own, `clarity` and `essence` read it as they read an assignment, a persona `business-analyst` hunts the world outside the parent, a check `brd` the mechanics. The stakeholders' sign-off is the organisation's act outside the forge. Why: each, as the positions give it; why the company's content lives in the instance's library and the engine carries a generic Map; why no prefix REF, no range of numbers for qualities, no FR, no lens of its own, no BRD of the chain from someone else's file. One worked example: a generic BR item with its parent and a generic NFR with a TBC for its value.
- inputs:
  .claude/skills/forge/states/brd.md
  templates/brd.md
  projects/forge/10-intent.md#POS.1800
  projects/forge/10-intent.md#POS.1810
  projects/forge/10-intent.md#POS.1820
  projects/forge/10-intent.md#POS.1830
  projects/forge/10-intent.md#POS.1840
  projects/forge/10-intent.md#POS.1850
  projects/forge/10-intent.md#REJ.0390
  projects/forge/10-intent.md#REJ.0400
  projects/forge/10-intent.md#REJ.0410
  projects/forge/10-intent.md#REJ.0420
  projects/forge/10-intent.md#REJ.0430
- links:
  `docs/use/write-a-brd.md`: iterating it with `/forge brd`.
  `docs/about/the-assignment.md`: the usual parent of a BRD.
  `docs/about/the-user-stories.md`: the layer that may follow a BRD.
  `docs/about/the-work-product.md`: what a BRD from someone else's file becomes.
  `docs/about/sources-and-research.md`: why what someone said is never silently the principal's position.
  `docs/about/projects-and-the-engine.md`: the library, a project of its own, where an instance keeps its roster of areas.
  `docs/reference/requirement-style.md`: the rule set of its items.
  `docs/reference/challenger-personas.md`: the business-analyst persona.
  `docs/reference/checks.md`: the `brd` check.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no company, group standard, colleague, fork, library path or instance roster named (the public standards the position names may stand); no trial, transcript, vendor, date, challenge or decision the positions cite; no thread number; no item of a real project; nothing of the Partner block as an instruction to Claude.
- made: derived
- evidence: the definition gives the target, the three ways in, the inputs around the parent with the roster as a library document of the instance cited by path and `Roster: none`, the Aim and its completion, the Partner's line of what Claude does not do, the Map's areas and the Requirement style with the TBC defined once and cited in brackets; the template the sections, `parent:` and the appendix; POS.1800 what the BRD is, where it stands, the analyst as the principal of a project of his own and that the company's content lives in the instance's library while the engine carries a generic Map; POS.1810 the ways in and the reason for the work product; POS.1820 what the forge names; POS.1830 the prefixes and the stricter style; POS.1840 the reviewers; POS.1850 the sign-off; the five REJ what was rejected and why. Where the definition and the positions differ in wording, the definition's wording and the position's reason stand.
- state: regenerate

### docs/about/the-user-stories.md
- title: The user stories
- line: What are the user stories, what does one story hold, and why does the export the stakeholders get leave the intent out?
- kind: explanation
- reader: user, extender, evaluator
- says: An artefact page. What it is: the user stories, `35-user-stories.md`, below the BRD and above the solution design: the parent broken into behaviour seen from the outside, what the user or the business sees happen and under which conditions it is accepted, so that the stakeholders approve them as a whole, the delivery makes its technical analysis and builds from them without an empty place, and the testers write their test cases from them; one item of the parent may be served by several stories and one story may serve several items, and the solution design cites the stories, never the reverse. Who writes and reads it: the principal with Claude, handed over by default; the stakeholders, the delivery and the testers read it. Made from: the BRD, read with the layers above it for the reasons it does not carry; or the intent with its threads where the change is small, the ask precise and without further impact, on the principal's word; a requirements document of someone else, registered and cited by path, yields stories that are a work product, never the artefact; around the parent the decisions, the ledger and the resource indexes. What it holds: stories only, under one prefix of its own, US; a story is a heading `US.NNNN — <name>`, a free sentence carrying who or what wants it, what happens and why (the form "As a... I want... so that..." neither required nor forbidden), its acceptance criteria as bullets in the indicative, one behaviour each, and then only the parts it has, under fixed English labels, `Edge cases` (situation and what happens), `Risks` (each with its mitigation or its consequences), `Note` (a link to an attachment or a technical analysis with what lies behind it), `Questions` (question and owner), `Reference`, the one part every story has, the BR, NFR, UC or DEP it serves, or in a small change the POS; a story is one function as the one who uses it meets it, its variants by condition, its qualities and its transitions being its criteria and edge cases, never stories of their own; a quality cutting across the whole is a story of its own; no vague word in a criterion, no priority, no estimate, no technical solution, no section of notes, dependencies or introduction; the labels English, the content in the project's language. Complete when every in-scope item of the parent is served by at least one story or said not to be, every criterion can be tested, no two stories contradict each other or describe one function twice, every open question has an owner and none that blocks the delivery is open; the stakeholders' approval of the whole is the instance's act. How it is found: handed over by default, Claude returning first the cut, the name of every story with a short description and the items of the parent no story serves, and only on the cut agreed the whole draft, walked story by story, an interview where the parent does not suffice for a story; what is missing stands as a question with an owner, never an assumption, and a change of substance goes to the parent first. The reviewers: no new critic and no new persona, `clarity` reads the stories with their Story style, `essence` compares them with their parent, a challenger of the roster may be sent where the principal wants the substance tried, and a check `user-stories` verifies the mechanics, coverage counted and never judged. The export the instance hands over is a render of the genre `user-stories-export`, one heading per story with its parts on lines of their own, pasted into a wiki or a tracker, which leaves out every reference to a POS since the stakeholders never see the intent, so that the artefact keeps its references and the export changes without touching it. Why: each, as the positions give it; why a section of dependencies was rejected, the Reference carrying them; why no persona of its own, the business-analyst persona hunting in the BRD above what a persona would hunt in stories. One worked example: one generic story with two criteria, one edge case, one question and its Reference, and the same story as the export shows it.
- inputs:
  .claude/skills/forge/states/user-stories.md
  templates/user-stories.md
  .claude/skills/recipe/genres/user-stories-export.md
  projects/forge/10-intent.md#POS.1990
  projects/forge/10-intent.md#POS.2000
  projects/forge/10-intent.md#POS.2010
  projects/forge/10-intent.md#POS.2020
  projects/forge/40-solution-design.md#SOL.0920
- links:
  `docs/use/write-user-stories.md`: iterating them with `/forge user-stories` and making the export.
  `docs/about/the-brd.md`: the usual parent of the stories.
  `docs/about/the-solution-design.md`: the layer that cites the stories.
  `docs/about/the-work-product.md`: what stories from someone else's document become.
  `docs/about/renders-and-recipes.md`: the render, which the export is and the artefact is not.
  `docs/reference/requirement-style.md`: the Story style, rule by rule.
  `docs/reference/checks.md`: the `user-stories` check.
  `docs/reference/recipe-genres.md`: the export genre and its checklist.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no pull request, user, clone, trial, project or date the positions and the design cite; no story of a real project; no product name of a wiki or a tracker; no source file of the forge project named; no brief of the forge project named; nothing of the Partner block as an instruction to Claude; no restatement of the Story style beyond what the shape of a story needs; nothing of the scripts' pattern of prefixes, which is the stable IDs page's.
- made: derived
- evidence: the definition gives the target, the inputs with the three ways in, the Aim and its completion, the Partner's line of what Claude does not do, the Map, the Instruments, the Course and the Story style; the template the heading, the parts and their order, the fixed labels and `parent:`; the genre file the shape of the export and that it is a render and never the artefact; POS.1990 what the stories are, where they stand, the many-to-many relation to the parent and the export without a POS, with the reason; POS.2000 how they are made with the reason; POS.2010 the shape of a story and why the section of dependencies was rejected; POS.2020 the reviewers with the reason; SOL.0920 the check without a persona and the export as a render of its own genre, each with what it was chosen against and its price. Where the definition and the positions differ in wording, the definition's wording and the position's reason stand.
- state: new

### docs/about/the-solution-design.md
- title: The solution design
- line: What does a solution design hold, and why does it restate nothing above it?
- kind: explanation
- reader: user, extender, evaluator
- says: An artefact page: the solution design says how the things wanted are realised, kept current, read by whoever realises it without the principal in the room. Derived from the lowest layer above it, the intent alone, the assignment, the BRD or the user stories; worth writing where the way is not obvious or a choice has a price. It holds why, against what, at what price, how the parts fit; it cites the layer above by ID and names what realises a part by path. The shape of a SOL item; a TBC with its owner. One worked example: a generic SOL item.
- inputs:
  .claude/skills/forge/states/solution-design.md
  templates/solution-design.md
  projects/forge/10-intent.md#POS.1390
  projects/forge/10-intent.md#POS.1400
  projects/forge/10-intent.md#POS.1420
- links:
  `docs/use/design-the-solution.md`: iterating it.
  `docs/about/the-intent.md`: the layer whose "what" this answers.
  `docs/about/the-user-stories.md`: the stories, which a design cites and never the reverse.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no item of the forge's own design quoted; no check named that does not exist.
- made: derived
- evidence: the definition gives the wording; the three positions the reasons. Where no input gives a reason, the page says the reason is not recorded.
- state: regenerate

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
- evidence: POS.1520 gives what a work product is, the two files, its neighbours and the reason the render was not stretched; SOL.0640 the one command, the Work table made by the ledger script from the records and its choice; the template the shape of the specification; CLAUDE.md, Document kinds the row of the kind.
- state: keep

### docs/about/documents-and-records.md
- title: Documents and records
- line: What kinds of document does a project hold, and why does state live in files?
- kind: explanation
- reader: user, extender, evaluator
- says: "Document" is every file of a project; "artefact" is reserved for the documents of the chain. Every document has one kind, in six groups: artefacts; records (history and decisions append-only; reviews and challenges immutable); state (the ledger made at read time, the project file written once, the threads, the indexes, the documentation map); rendering (recipes, renders, pages); work (the work product); resources (sources and research, a research of several questions being a bundle). Three files have no kind and are read by the forge as no document: a file of the engine's working folder `tmp/`, the player page of the videos, and the principal's own file beside the forge's in `renders/` or `published/`. Why state lives in files and never in the conversation. The ledger is the single source of truth for state, made from the other files and never written by hand, said in one sentence with a link. Why immutability is a process rule. Prose hard-wrapped at about 72 columns. One worked example, generic.
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
  `docs/about/renders-and-recipes.md`: the principal's own files beside the forge's, which have no kind.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no table reproduced; no forge project ledger content; no merge driver of the record files, which is not built; no "one sentence per line", which is not built.
- made: derived
- evidence: CLAUDE.md, Document kinds gives the groups and kinds and the three files that have no kind; the decisions skeleton the shape of a record; the positions the reasons. Where no input gives a reason, the page says the reason is not recorded.
- state: keep

### docs/about/the-ledger.md
- title: The ledger, made from the records
- line: Why is the ledger made at read time from the other files, and where does the state it shows really live?
- kind: explanation
- reader: user, extender, evaluator
- says: A concept page. What it is: the ledger is the single source of truth for a project's state (its briefs, documents, renders, published files, work products, sources, research, dependencies, findings, challenges and what waits on the principal), made at read time by a script from the project's documents and never kept in git; nobody writes a row, and every command that changes state makes it afresh. How it works: what only the ledger once knew lives in records and fields where it belongs: the mining of a brief as a record in the intent's history, the settling of a finding or a challenge as a closing record or a decision's verdict line, a work product's state in its specification's history, a source's date and form in its index entry, a published file's provenance in its companion; a record of state only carries the current version and does not raise it. Waiting on the principal is a rule, not a list: the open threads, the open questions he owns, the open findings of a critic and the open challenges, and the parked ones under a heading of their own. The Reports section says what the merged files cannot say by themselves (an ID defined twice, a closed thread touched later, a thread cited with no file), and a file the script cannot read is named in the header instead of breaking the run. The hand-kept ledger of a migrated project stays as an immutable archive, read for every item with no newer record. Where the state is wanted on the remote, a release writes it as a tracked render. Why: the ledger was the one file present at every collision of two people or two windows on one project, since every operation wrote it; made at read time it stops being a thing to merge; a hand-kept list of what waits differed from any rule in both directions. One worked example: a generic closing record and the ledger row it yields.
- inputs:
  CLAUDE.md#Ledger
  templates/ledger.md
  templates/history.md
  scripts/forge-ledger.py
  projects/forge/10-intent.md#POS.1600
  projects/forge/10-intent.md#POS.1610
  projects/forge/10-intent.md#POS.1620
  projects/forge/10-intent.md#POS.1630
  projects/forge/10-intent.md#POS.1640
  projects/forge/10-intent.md#POS.1650
- links:
  `docs/reference/ledger.md`: the tables, their columns and the state words, exactly.
  `docs/use/see-where-a-project-stands.md`: the map and `/ledger`, which read it.
  `docs/about/documents-and-records.md`: the kinds of document the ledger is made from.
  `docs/about/upgrades-and-migration.md`: the migration that turned a hand-kept ledger into an archive.
  `docs/about/working-together.md`: why the ledger never conflicts when two people work on one project.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no landing of branch records, no `+` version token, no version on a branch, which the forge does not have; no report the ledger template does not list (a version given twice among them); no row of a real project's ledger; no project named at whose merges the reason was found; no count of documents or reports; no slug from the script's examples.
- made: derived
- evidence: CLAUDE.md, Ledger gives the made-at-read-time rule, that nobody writes a row and where what only the ledger knew lives; the ledger skeleton the tables, the Waiting rule, the Reports and the archive; the history skeleton the records of state; the script's header the kinds of document it reads and that an unparsable file is a header line; POS.1600 to POS.1650 the reasons and the state render, POS.1640 and the skeleton's Reports agreeing on the three reports.
- state: regenerate

### docs/about/versioning-and-history.md
- title: Versioning and history
- line: What does a version number mean, what is a major, and where does a document's history live?
- kind: explanation
- reader: user, extender, evaluator
- says: Integers denote signed-off versions, drafts 0.x; status agrees with the number; a recipe carries no status and stays 0.x unless the principal names an integer, from which the count goes on, the number his own mark and not an approval, because approval has a meaning only where someone receives the document and a recipe is received by nobody. A header carries nothing that changes with a round: the date and the last change of a document are computed from its history by whatever reads them, so that no field asks for a write at every round. What a major of an intent is and what its test attests. Every versioned document, a work specification included, keeps its history in an append-only companion beside it, a log of one record per change with the reason, Action and Was; a record of state only (a mining, a closing, a work product's state) carries the current version and does not raise it. Why: the way to an item does not belong in the item; the log is the single primary from which commit messages and release notes derive; a history is searched by `/history`, never loaded whole. A companion written before the log moves to an archive. One worked example: a generic record.
- inputs:
  CLAUDE.md#Versioning & status
  templates/history.md
  projects/forge/10-intent.md#POS.0300
  projects/forge/10-intent.md#POS.0310
  projects/forge/10-intent.md#POS.0710
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
  `docs/about/renders-and-recipes.md`: the recipe, the one versioned kind that is never approved.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no record of the forge project; no version number of the forge; no list of the checks a major of the forge ran; no `landed` kind, `+` token, landing on main or version written on main only, which are not built; nothing of POS.0710 beyond the recipe's version and its reason.
- made: derived
- evidence: CLAUDE.md gives the scheme, the header rule, the recipe's integer on the principal's word and the companion rule; the template the record and the records of state; the positions the reasons, POS.0710 why a recipe stays 0.x and what an integer means on it, POS.1570 the header and POS.1630 the state records; REJ.0110 the rejected scheme.
- state: keep

### docs/about/stable-ids.md
- title: Stable IDs
- line: Why does every item carry an ID that is never renumbered, and what happens when two items share one number?
- kind: explanation
- reader: user, extender, evaluator
- says: Every item carries `PREFIX.NNNN`, a prefix of two or three letters, four digits as long as the number fits and a fifth only beyond 9999, numbered in tens with each group at the next hundred, global and stable, never renumbered, every sorting numeric. The one exception: two items with one number in one project, however they came to it (a merge of two branches, a hand's edit, documents born apart), are settled the same way: the older keeps its number, the younger takes a new one with a `changed` record naming the clash, its citations corrected and a thread's file renamed with it; a finding of a filed report that clashes is renumbered in the report itself, the one exception to a report's immutability, since the ID lives in the report's heading and the ledger reads it there; the ledger script reports the clash and writes nothing, and the renumbering is Claude's with the principal, never Claude's alone. IDs stay one sequence per project, taken at the write, with no blocks per author. Why structure over prose: an item with a stable ID can be cited, reviewed, traced and changed one at a time. Why the fifth digit: a prefix may outgrow four digits on use alone. Why two letters are allowed beside three: the BRD's prefixes had two already and the scripts' pattern was the one limit. Why a fact, a position and a thread have prefixes of their own; why a thread carries its origin. Why detection and the existing remedy over blocks of IDs: a clash is rare on a project of one or two people. One worked example, generic.
- inputs:
  CLAUDE.md#ID scheme
  projects/forge/10-intent.md#POS.0200
  projects/forge/10-intent.md#POS.0220
  projects/forge/10-intent.md#POS.0230
  projects/forge/10-intent.md#POS.1790
  projects/forge/10-intent.md#REJ.0020
  projects/forge/10-intent.md#REJ.0100
- links:
  `docs/reference/id-scheme.md`: the prefix table and the numbering rules.
  `docs/use/settle-a-conflict.md`: where a number taken twice usually shows up, after a merge.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no table; no ID of an instance project; no group name of a company standard; no decision, challenge, report name or date the positions cite; no count of the forge's own positions; no blocks of IDs, allocation over branches or hashed IDs presented as anything but a rejected direction; no project named at which a clash occurred.
- made: derived
- evidence: CLAUDE.md gives the rules, the two or three letters, the fifth digit, the numeric sort and the one exception; POS.0220 the exception's procedure, the renumbering of a filed report's finding with its reason, the reason for the fifth digit and why two letters are allowed; POS.1790 the one sequence, no blocks, and the reason detection was chosen; POS.0200 and POS.0230 the reasons for structure and the prefixes; the two REJ what was rejected.
- state: regenerate

### docs/about/isolated-reviewers.md
- title: The isolated reviewers
- line: Why do three kinds of reviewer never see the conversation, and what does their agreement mean?
- kind: explanation
- reader: user, extender, evaluator
- says: Three kinds of reviewer of one shape: the critic, the challenger, the check. All run as isolated subagents that see the project's documents and never the working conversation, on the session model; their blindness is the source of their value. What holds for every isolated subagent of the forge (a reviewer, a renderer, a documentation agent, a research agent) in one sentence: it sees nothing of the conversation, reads every input from disk in its own run because the copy of the core file in its context may be older, and lets no instance fact into what it returns. All reviewers run on the principal's word alone, because a run costs tokens, some checks a great deal, and what is spent is his to decide; the word may be given once in a command's definition that names the checks it runs, and what is ruled out is a run on Claude's own judgement. Settled by walkthrough, reports immutable and dated, each named by its date, the time and a short content hash so that two branches never make the same name; nothing blocks. Every agent returns its report with its findings unnumbered and writes nothing; the command numbers it and files it, one report at a time, so that no ID is given twice and reviewers may run in parallel. The shared behaviour of each kind is one contract, the agent file owns only its Lens. Isolation is not independence: the reviewers share one model family with the author, so their agreement is never validation; the calibration lies outside, in people or another model family, said in one sentence with a link. Instance facts never enter a report. One worked example, generic.
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
  `docs/about/another-model-family.md`: the link to a model of another family, and why its reviewers are not built yet.
  `docs/use/walk-through-a-list.md`: how findings are settled.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no roster; no contract text; no reviewer on another model family presented as built; the documentation agents and the research agent are not reviewers; no version on a branch in a report, which is not built; no date the positions cite.
- made: derived
- evidence: CLAUDE.md, Isolated reviewers gives what holds for every isolated subagent, the mechanism and the filing by the command one report at a time; POS.0400 why a reviewer runs on the principal's word alone and where that word may be given once; POS.1140 why the command numbers and files; POS.1720 why the names are unique; POS.0790 that isolation is not independence and that another family is reached over the link, the research first; the other positions the reasons; REJ.0080 why review and challenge are two reviewers.
- state: keep

### docs/about/the-critic.md
- title: The critic
- line: What does a critic lens judge, and why two lenses?
- kind: explanation
- reader: user, extender, evaluator
- says: The critic judges the quality of the artefacts as documents through a lens, never the substance; two lenses because one critic hunted formalities and never guarded the chain: `clarity` reads each artefact on its own, `essence` distils every adjacent pair blind and compares. A target narrows a run to one artefact, or to any file of the project read with the chain around it, a work product with its specification, so that what Claude composes gets the isolated look as well. How it works: regression first, respect for rejected findings, sharp and few, each artefact judged against its own definition, deliberate omissions never defects; the lens returns its report with its findings unnumbered and the command numbers and files it, so that no ID is given twice. What it produces. One worked example of a finding, generic.
- inputs:
  .claude/skills/critic-contract/SKILL.md
  projects/forge/10-intent.md#POS.0400
  projects/forge/10-intent.md#POS.0410
  projects/forge/10-intent.md#POS.0270
  CLAUDE.md#Isolated reviewers
- links:
  `docs/use/critique-the-documents.md`: running a lens.
  `docs/reference/critic-lenses.md`: the lenses and their angles.
  `docs/extend/add-a-critic-lens.md`: adding a lens of one's own.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no report template; no instruction to the agent copied as such; no finding of the forge project.
- made: derived
- evidence: the contract gives subject, target, way of working and output; the positions why two lenses, why a file may be the target and why testability is a recommendation; CLAUDE.md, Isolated reviewers why the lens returns its report and the command files it. Where no input gives a reason, the page says the reason is not recorded.
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
- evidence: the contract gives subject, target, way of working and output; the positions the reasons. Where no input gives a reason, the page says the reason is not recorded.
- state: keep

### docs/about/the-check.md
- title: The check
- line: What does a check verify, why is it read-only, and who files its report?
- kind: explanation
- reader: user, extender, evaluator
- says: A check verifies mechanical conformance with the current conventions, never substance or quality, each check owning one concern; it reads the rules at their owners. Read-only: it returns its report and the command files it, only when it has findings. Findings only, precise to file and line, ranked; a finding decided once by a decision is not raised again, and a known one is reported under the ID it has. Advisory. Composition is the caller's: `/save` runs `light` unless told otherwise, `/release` runs `light` and `project`, for the engine `engine` too; any other check, such as one for a single kind of artefact, runs on the principal's word. One worked example, generic.
- inputs:
  .claude/skills/check-contract/SKILL.md
  projects/forge/10-intent.md#POS.0540
  projects/forge/10-intent.md#POS.0570
  projects/forge/10-intent.md#POS.1140
- links:
  `docs/use/check-conformance.md`: running a check.
  `docs/reference/checks.md`: the checks and what each verifies.
  `docs/extend/add-a-check.md`: adding a check of one's own.
  `docs/about/the-documentation.md`: the documentation run, which files what it cannot place as a check's report.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no report template; no Lens text; no finding of the forge project; no overlap check of ID reservations, which is not built; no check run as a program, which is a trial run by no command.
- made: derived
- evidence: the contract gives subject, way of working and output; the positions the composition and the reasons. Where no input gives a reason, the page says the reason is not recorded.
- state: keep

### docs/about/renders-and-recipes.md
- title: Renders and recipes
- line: Why is an output generated from a recipe and never edited by hand?
- kind: explanation
- reader: user, extender, evaluator
- says: A render is an audience-specific output generated from the chain, never a source of truth; what is iterated is its recipe; never edited by hand. The boundary between chain and render is authorship. Every render opens with provenance and is stale when a cited version differs; regenerated only on the principal's word or by a release, because regeneration is stochastic. A recipe is a tool, not a record of thinking: it carries a version and no status, stays 0.x unless the principal names an integer, and that integer is his own mark and not an approval, since a recipe is received by nobody. A recipe may declare several languages, the first primary and the rest translated from it in the same run, one render per language, because a second generation would choose the quotes and the cut again differently. An output is made in two steps divided by cost: the plain file with the render through pandoc, or through the screenplay script, and the designed file by `/publish` through a model, whose provenance stands in a companion beside it; a screenplay has no designed step. The forge owns in `renders/` and `published/` only the files its recipes name; any other file there is the principal's own, made by hand from the forge's files (a copy under a new name that he edits, a PDF saved from Word or PowerPoint, an HTML of a diagram), kept in git beside them with no companion, no row and no check, never read, overwritten or raised by the forge; what is to change in a forge's file is copied first. Every project's README and release notes are renders; recipes may be composed by genre. A page of the documentation and a work product are not renders. One worked example: a generic recipe's shape.
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
  projects/forge/10-intent.md#POS.1910
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
  `docs/about/the-security-policy-and-the-code-of-conduct.md`: the two fixed files of the root, which are no render either.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no recipe of the forge project quoted; no author line; no pitch content; no script options; not the readme skeleton's fixed closing sentence; no version on a branch in a provenance, which is not built; no project, file or decision named at which the principal's own files came up.
- made: derived
- evidence: CLAUDE.md, Document chain (Renders) gives the mechanism, the languages, the published table, the three conversions and the principal's own files; the recipe skeleton the sections; the readme skeleton's Instructions what a README carries; the positions the reasons, POS.0710 the recipe as a tool with a version and no status, its integer on the principal's word and why, POS.1550 the languages, POS.0590 the two steps and POS.1910 the principal's own files with the rule that the forge's file is copied first; the two REJ what was rejected.
- state: regenerate

### docs/about/the-screenplay-and-its-player.md
- title: The screenplay and its player
- line: What is a teaching video of the forge made of, why does one script make both of its formats, and why does the engine host the public files?
- kind: explanation
- reader: user, extender, evaluator
- says: A concept page: a recipe of the genre `screenplay` renders a screenplay of a terminal conversation cut from session records: a title card that discloses the composition, a card of what the viewer will see, scenes with the real time of day, each with a caption of two parts (what happens now, why the forge does it this way) and a fenced block of what the terminal shows, and an end card; the caption is the teaching, the terminal the evidence. Its inputs are session records registered as sources and the brief of the videos; a recipe may render in several languages, the translations cut scene for scene from the primary. Its Format names one of two formats: `video`, an MP4 painted frame by frame as a simulated terminal, or `html-player`, the timed events for the player page of the engine; both made by one script, deterministic, no model in it, the plain file of `/render`, no designed step and no published file; the pace of reading and the look stand in the recipe's Format section and reach the script as arguments, never in the render, so that the render carries content only and the plain file would not carry the instructions as text. The player page is one fixed file of the engine, a single file with no dependency beyond the browser: a sidebar of the videos by title, grouped by the section of the course each file names, the simulated terminal with its caption band and cards, play and pause, speed, the scenes as chapters, the language where a video has siblings, three font sizes; it is written anew from its skeleton by the script, never by hand and never by a model. Why the engine hosts what a project shows in public: the engine, public and served by GitHub Pages from `docs/`, is the one public place of an instance, while the project that made the file stays private; the engine carries the file only, the recipe, render, provenance and history stay in the project; what goes out is chosen in the recipe, video by video, and read by the principal before the engine is saved; the folder is flat, foreign to the documentation and its checks, which generate and verify the documentation around it and leave it alone; video files never enter the tree and go out as assets of a release. The choices and their price as the solution design records them. One worked example: a generic scene of a screenplay.
- inputs:
  projects/forge/10-intent.md#POS.1530
  projects/forge/10-intent.md#POS.1540
  projects/forge/10-intent.md#POS.1550
  projects/forge/40-solution-design.md#SOL.0420
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
- must-not: no video, recipe or project of an instance named; no course address; no name of a person; no section name or order of the forge's own course; nothing of the page's styles or code; no research or trial of a project named.
- made: derived
- evidence: POS.1530 gives the screenplay, the two formats and the one script with its reason; POS.1540 the engine as the public host, what goes out, the clearing, the flat folder, the player page and that video files never enter the tree; POS.1550 the languages; SOL.0420 why the Format section is never copied into the render; SOL.0650 the script's choices and their price; SOL.0660 what the page does, its grouping, that the script renews its list and that the documentation leaves the folder alone; the genre file the product and the inputs; the skeleton's head comment that the page is written from it by the script and never edited.
- state: keep

### docs/about/the-documentation.md
- title: The documentation
- line: What is the documentation, who reads it, and why is it generated rather than written?
- kind: explanation
- reader: user, extender, evaluator
- says: The documentation of a project is a set of pages of one topic each in `docs/`, with an index that names each reader's path. Three readers in order of weight. Five sections by the reader's journey, filled only where the project has material; each page of one kind (how-to, explanation, reference), the kind saying what content belongs on it; one rule has one home page; every page is reached from another page. Generated and never composed by hand: a page mirrors the files that own its topic or is derived from named evidence; the map lies beside the owning project's ledger, carries only its target and owner in its header, and is never shown to the reader; the previous map is taken from git, since the map's header carries no field that changes with a run. Two agents make it under one contract, a planner and a writer per page; for the engine the planner reads the core, the skills, the agents, the settings, the templates, the scripts' headers and the owning project's briefs, intent, threads, design, decisions and recipes, for a project its briefs, intent, threads, the layers below the intent, its ledger, its indexes and its recipes and whatever they point to, and nothing a project would set for itself; the pages are written in the project's language, as its artefacts are, the README staying English. A run regenerates only pages whose inputs changed, an input hashed as the named part of a file, the rule the pages are made by hashed with them, its whitespace normalised so that a re-wrap of the rule regenerates nothing; a run is made on `main` only, since the pages are taken as `ours` at a merge and that turns round in the rebase of a save; a release by hand reports the index's age and offers the command, with `--auto` it asks once before anything runs. A page is never mended by hand, because the next run writes it again from its owners and the mend is gone; only a mend in the file that owns the matter survives. What a run cannot place, a fact with no owner, a matter the map and an owner disagree on, a reason a page wants and no file records, is a finding of the run, filed in `reviews/` as a check's report and settled as a check's findings are, since the documentation finds what no other check does. The index is also what the manual `/man` reads to answer a need said in free words, since every page carries the one question it answers. The public folder of the videos under `docs/` is not the documentation's, left alone by the planner, the index, the state and the check. Why: the README was the whole documentation and poor as one; why not a recipe per page, a site, a hand-kept philosophy. The diagram: one documentation run. One worked example: a generic entry of the map.
- inputs:
  CLAUDE.md#Document chain
  .claude/skills/document/SKILL.md
  .claude/skills/docs-contract/SKILL.md
  .claude/agents/docs-planner.md
  .claude/agents/docs-writer.md
  templates/docs-map.md
  .claude/skills/man/SKILL.md
  scripts/docs-state.py
  projects/forge/10-intent.md#POS.1450
  projects/forge/10-intent.md#POS.0930
  projects/forge/10-intent.md#POS.1540
  projects/forge/10-intent.md#POS.1690
  projects/forge/10-intent.md#POS.1710
  projects/forge/10-intent.md#REJ.0240
  projects/forge/10-intent.md#REJ.0250
  projects/forge/10-intent.md#REJ.0260
  projects/forge/10-intent.md#REJ.0500
  projects/forge/40-solution-design.md#SOL.0460
  projects/forge/40-solution-design.md#SOL.0700
- links:
  `docs/use/generate-the-documentation.md`: running `/document`.
  `docs/extend/change-a-documentation-page.md`: changing a page through its owners.
  `docs/reference/documentation-map.md`: the map's entry and the page's front-matter, field by field.
  `docs/about/renders-and-recipes.md`: the renders, which the pages are not.
  `docs/about/the-check.md`: the check, whose report shape and settling the documentation run borrows.
  `docs/about/the-screenplay-and-its-player.md`: the videos folder under `docs/` that the documentation leaves alone.
  `docs/about/languages.md`: which language each kind of document carries, the pages among them.
  `docs/use/look-up-a-command.md`: the manual that reads the index to answer a question.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no count of pages or date of a run; no model name; no entry of the engine's map quoted; no name of a project other than `forge`; nothing of the contract as an instruction to Claude; no list of pages the design says are to be regenerated after a release; no finding of the forge project; nothing of REJ.0500 beyond what a project's planner reads; no thread number.
- made: derived
- evidence: CLAUDE.md, Document chain (Documentation) gives what the documentation is and where the map lies; the `/document` skill the one run, the main-only rule, the previous map from git and the filing of what the run cannot place as a check's report; the contract what the two agents share, the kinds of a page and the language of the pages; the planner the readers, the outline, what it reads for the engine and for a project, and the videos folder left alone; REJ.0500 that what a project wants documented beyond what the planner reads is not a setting of its own; the writer the page's shape; the map's skeleton its header; the `/man` skill that a question is answered from the index, every page carrying the question it answers; the state script's header that the generator is hashed with its whitespace normalised and why; POS.1450 the position whole with its reason, the pages in the project's language, why a page is never mended by hand, the report of the run and what a release does by hand and with `--auto`; POS.0930 the faster model for a mirrored page; POS.1540 why the videos folder is kept apart; POS.1690 and POS.1710 why the run is on `main` only; SOL.0700 why the previous map comes from git; the three REJ what was rejected; SOL.0460 the choices and the parts of a run the diagram draws. Where no input gives a reason, the page says the reason is not recorded.
- state: regenerate

### docs/about/sources-and-research.md
- title: Sources and research
- line: Why are sources immutable, why is registration not intake, and what is a research for?
- kind: explanation
- reader: user, evaluator
- says: External inputs live in `sources/`, immutable once registered, one form each; a related set is a bundle. Registration is not intake: what a source is for is the principal's word, asked before its index entry is written so that the entry carries it from its birth, its Role in the index; source content enters the intent only by his explicit act with provenance, so that what someone said is never silently promoted to his position. Research is a durable answer to a question: a single note for one card on one engine, or a bundle of a plan, one note per card per engine and a synthesis; immutable from its filing and dated; how it is planned and checked is said in one sentence with a link. A source and a research note are immutable because they record a moment, a state of the world the forge did not make and has no business editing; a newer state is a new file, a research run again, a document that arrives in a new version a further file of a bundle of one origin, whose index says which is the newest, so that every citation of the intent keeps pointing at the text it was made from. Every `sources/` and `research/` directory carries an index that tracks nothing and is an automatic input of no command; a source's date, origin and form are fields of its entry. Why personal matter stops an ingest before the store. One worked example: a generic index entry.
- inputs:
  CLAUDE.md#Document chain
  CLAUDE.md#Document kinds
  templates/index.md
  templates/index-bundle.md
  projects/forge/10-intent.md#POS.0050
  projects/forge/10-intent.md#POS.0180
  projects/forge/10-intent.md#POS.0840
  projects/forge/10-intent.md#POS.1040
- links:
  `docs/use/register-a-source.md`: the ingest procedure.
  `docs/use/research-a-topic.md`: the research procedure.
  `docs/about/the-research.md`: how a research is planned before it is searched and kept honest.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no source of the forge project; no index entry reproduced; no merge driver of the index, which is not built; nothing of the research's course beyond the one sentence and the link.
- made: derived
- evidence: CLAUDE.md, Document chain gives the rules of sources and indexes; Document kinds the research row with the bundle; the skeletons the fields; the positions the reasons, POS.1040 why a source and a research note are immutable and why personal matter stops the command before the store. Where no input gives a reason, the page says the reason is not recorded.
- state: keep

### docs/about/the-research.md
- title: How a research is made
- line: Why is a research planned before it is searched, and how is what it found kept honest?
- kind: explanation
- reader: user, extender, evaluator
- says: A concept page. What it is: a research grounds the principal's artefacts in what the world has already solved, so that he does not reinvent it; its quality is made by its plan, not by the searching. How it works: the plan comes first and is confirmed in a walkthrough before anything is searched or costs anything: the purpose, the perspectives each with its cards or none, the assumptions with a premortem marked as Claude's, what is left out on purpose, and the cards, each one question answered by one kind of evidence from one kind of source, with why it matters, where to look, a disconfirming query and a stop rule; a card that needs two kinds is two cards, a card with nothing under why it matters is cut. Two depths: deep, a bundle with one note per card per engine and a synthesis; quick, one card filed as one note, still shown before the search. Every card is searched by an agent that sees a packet made from the forge's own definition and nothing of the conversation, the agent's brief the same in every packet: start wide, open a page or do not cite it, go upstream to the first publisher, exclude sources by kind, name conflicts and what was not found, never fabricate. Before a note is filed it is read against its shape, scanned for instance facts and every URL it cites opened by a script; a dead page or an identifier that names another paper sends it back once, an unanswered page is unverifiable and never a failure. The synthesis is Claude's from the notes alone: completeness card by card, the answers side by side, the unexpected gathered before any judgement, what was not found, Claude's own view last and apart. A second round only for gaps the notes name, never a third. Why: each, as the positions give it; why no recursive deep-dive to a fixed depth, no fact verified by a count of agreeing sources, no saturation as a percentage. The research on a second model family is said in one sentence with a link. One worked example: a generic card.
- inputs:
  projects/forge/10-intent.md#POS.0050
  projects/forge/10-intent.md#POS.1860
  projects/forge/10-intent.md#POS.1890
  projects/forge/10-intent.md#POS.1370
  projects/forge/10-intent.md#REJ.0450
  projects/forge/10-intent.md#REJ.0460
  projects/forge/10-intent.md#REJ.0470
  projects/forge/40-solution-design.md#SOL.0860
  .claude/skills/research/SKILL.md
  templates/research-plan.md
- links:
  `docs/use/research-a-topic.md`: running `/research`.
  `docs/about/another-model-family.md`: the second engine, how it is reached and how its independence is measured.
  `docs/about/sources-and-research.md`: research as a resource of the project.
  `docs/reference/research-bundle.md`: the shape of a note, a bundle and its plan.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no agent's brief copied as an instruction to an agent; no topic, bundle or note of the forge project; no date, trial or count of notes the positions or the design cite; no brief named; no subagent type; no model name; nothing of the second engine beyond the sentence and the link.
- made: derived
- evidence: POS.0050 gives the purpose; POS.1860 the plan before the search, the cards, the two depths, the packet, the synthesis and the second round, with the reason; POS.1890 the check before filing and its reason; POS.1370 Claude's own view apart; the three REJ what was rejected and why; SOL.0860 the choice of the plan as the unit of consent; the research skill the course and the agent's brief in the operating layer's wording; the plan skeleton the sections of a plan and a card. Where the skill and the positions differ, the skill's wording and the position's reason stand.
- state: regenerate

### docs/about/another-model-family.md
- title: Another model family
- line: Why does the forge reach a model of another family, how is it reached, and how is its answer kept independent?
- kind: explanation
- reader: user, extender, evaluator
- says: A concept page. What it is: the author, the critic and the challengers share one model family, so what that family cannot see none of them finds; a model of another family is a calibration point outside. How it is reached: one script runs one packet on an engine of its table, one row per engine, over that engine's own command-line tool; the login is the user's, made once in the engine's own tool, how the tool is installed and signed in being the tool's own documentation's, the forge asking only that it is on PATH and carrying no key, no account and no configuration; the forge names engines and tiers, never models or versions, so that a name always means the newest of its kind and nothing in the forge changes when a new version arrives. The engine works in a packet folder under the engine's working folder `tmp/`, never at the forge's root, whose hooks and instance file it must not see; because the place alone locks nothing, the script gives the engine a profile of its own for the run, which denies the forge's tree and the shell and allows the web, the user's own settings untouched and the profile kept in the run folder as its record. Every tool call is allowed and the engine's sandbox contains it, since a run that cannot ask returns nothing; read-only is verified by comparing the folder before and after, and a run that changed anything is refused. The answer comes back as a note with the engine, the model word, the usage and the run in its front-matter, and the command files it. Where it is used today: a deep research may take a second engine by name; it reads the draft plan and answers every card in full on the same packet, so that two whole answers lie side by side; agreement is consistency, never validation, and difference is spelled out. Independence is measured, never assumed: the first engine's notes are held out of reach until the second's note of the card has returned, and the URLs and the sentences the two notes share are counted before filing; a note written from the other's goes back once or is said to be no second voice. An engine's quota is spent one or two runs at a time. The reviewers on this link are intended and not built. Why: each, as the positions give it; why both engines do the whole work rather than a split of roles; why no skill on the other engine's side; why a command-line tool and not a library or a server. One worked example: one generic card answered by two engines and the measure of their independence.
- inputs:
  projects/forge/10-intent.md#POS.0790
  projects/forge/10-intent.md#POS.0800
  projects/forge/10-intent.md#POS.1870
  projects/forge/10-intent.md#POS.1880
  projects/forge/10-intent.md#REJ.0440
  projects/forge/10-intent.md#REJ.0480
  projects/forge/10-intent.md#REJ.0490
  projects/forge/40-solution-design.md#SOL.0870
  projects/forge/40-solution-design.md#SOL.0880
  scripts/forge-engine.py
  scripts/forge-cite.py
- links:
  `docs/about/the-research.md`: the research, the first job on this link.
  `docs/about/isolated-reviewers.md`: the reviewers of one family and why their agreement is not validation.
  `docs/use/research-a-topic.md`: a research with `--engine`.
  `docs/extend/add-an-engine.md`: adding an engine as one row of the table.
  `docs/reference/scripts.md`: the engine script and the citation script, their options.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no vendor, product or model family named beyond the table's row `antigravity` and its tool `agy`; no date, probe, trial, count of notes or research of the forge project; no path of the user's settings file or of the profile beyond "in the run folder"; no thread or challenge number; no consultation or spool; no reviewer on the link presented as built; no flags beyond naming that every tool call is allowed and the sandbox is on.
- made: derived
- evidence: POS.0790 gives isolation not independence and the calibration outside; POS.0800 the reviewers intended on the link and not built; POS.1870 the second engine on one plan, the side-by-side answers, the measured independence, the unusable engine and the quota; POS.1880 the one script, the login and the installation as the tool's own documentation's, no key and no configuration, the packet folder, the profile, the verified read-only, the returned note, and that the forge names engines and tiers and never versions, with the reason; the three REJ what was rejected; SOL.0870 the profile's allow and deny and its price; SOL.0880 the counts of independence; the two scripts' headers what each does in the operating layer's wording. Where a header and a position differ, the header's wording and the position's reason stand.
- state: keep

### docs/about/projects-and-the-engine.md
- title: Projects and the engine
- line: Why is every project a repository of its own that the engine does not know?
- kind: explanation
- reader: user, extender, evaluator
- says: The engine is one public repository, the core together with its own project `projects/forge`; every other project is a repository of its own under a gitignored `projects/`, with any remote and visibility, or none. A project is under git when git names its directory as the top of a repository, the one question the scripts ask; a project whose top lies elsewhere, or that has none, is a project outside git: the forge writes its files and runs no git on it, the repository above it asked nothing, and it comes in by hand, a copy or a link into `projects/`. Why: publication with nothing sensitive, access per project, seamless work inside. A project has a project file, written once at its creation, that declares its slug, its kind (thought or library) and the language of its artefacts; a library is shared material cited by path as a dependency taken knowingly. Instance facts live in `CLAUDE.local.md`; the forge's behaviour lives in the engine, never in the assistant's memory. A project records no engine version, said in one sentence with a link. The engine is the one public place of an instance: what a project shows in public goes out as a file into the engine, said in one sentence with a link. The shapes rejected. The diagram: the engine root with its own project and the nested project repositories. One worked example, generic.
- inputs:
  CLAUDE.md#Repository layout
  CLAUDE.md#Persistence (git)
  templates/project.md
  projects/forge/10-intent.md#POS.0550
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
  `docs/about/where-it-is-going.md`: the forge's own project as a repository of its own, a direction decided and not yet built.
  `docs/reference/repository-layout.md`: the layout, file by file.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no host, company or project name other than `forge`; no repository address; no history of the split as a story; no issue, challenge or date the positions cite; no fixture project; no second working tree of the engine, which is not built; no claim that the forge's own project is already a repository of its own.
- made: derived
- evidence: CLAUDE.md gives the shape and, in Persistence, how a project is recognised and what a project outside git is; POS.0550 the same with its reason; the project file skeleton its fields; the positions the reasons, POS.1590 why the project file exists, POS.1540 the engine as the public place in one sentence; the two REJ what was rejected; SOL.0500 the gitignore pattern and the parts the diagram draws. Where no input gives a reason, the page says the reason is not recorded.
- state: regenerate

### docs/about/persistence-in-git.md
- title: Persistence in git
- line: Why are the scripts the only door to a write of git, and why two doors, two speeds?
- kind: explanation
- reader: user, extender, evaluator
- says: The scripts in `scripts/` are the door to a write of git; reading git directly is open, since reading changes nothing. The line between the two is held for Claude by a hook of the harness (the program Claude runs in, glossed once): it allows a reading command, denies every write and names the script to use instead, and puts the few commands that finish the step of a conflict to the principal, which run on his yes; the other shell tool is closed to git whole, so that there is one door; the rule binds the forge, not the principal's own shell. A commit carries the message the principal confirmed and no attribution line. Two doors, two speeds: `/save` with the light check, on any branch; `/release` from `main` only with its checks, for the engine the tests first, the documentation offered, the README and release notes, the release message and the major's tag, its closing save without a second light check. `/pull` is the door inward: the forge looks at the remote, says what waits on GitHub outside git beside the state of the branch, pulls only a clean repository that is behind, and never merges on its own. `main` is the released line, branches voluntary, merging git's, made by the integrator on his own clone outside the forge's scripts. Every file has a way of merging, said in one sentence with a link; the files made for a reader are made only on `main` and taken as `ours` at a merge, so whatever makes a derived file or migrates a project (`/release`, `/publish`, `/document`, `/migrate`) runs on `main` only and refuses a repository behind or diverged, since the rebase of a save turns `ours` round and would let an older file win. `ours` is a merge driver not built into git: `/setup` registers it once per machine with the git settings it needs, and the status script says when the registration is missing, since an unregistered clone silently falls back to a conflict. The ledger is not in git at all. The commit identity is git's, resolved per host, with a guard. Immutability is a process rule. The scripts are Python, `python` on PATH their one prerequisite, written to run unchanged on Linux and macOS: the engine's tests run in CI on Linux and Windows at every push, the conversions are tested for their failure without the tool alone, the per-prompt hook stays a writing rule until a run says otherwise, and nothing has run on macOS, where the whole set is the writing rule alone; the tests themselves are said in one sentence with a link. One worked example, generic.
- inputs:
  CLAUDE.md#Persistence (git)
  .claude/settings.json
  scripts/hook-git.py
  projects/forge/10-intent.md#POS.0550
  projects/forge/10-intent.md#POS.0830
  projects/forge/10-intent.md#POS.0950
  projects/forge/10-intent.md#POS.1100
  projects/forge/10-intent.md#POS.1200
  projects/forge/10-intent.md#POS.1490
  projects/forge/10-intent.md#POS.1710
  projects/forge/10-intent.md#POS.1970
  projects/forge/40-solution-design.md#SOL.0520
  projects/forge/40-solution-design.md#SOL.0740
  projects/forge/10-intent.md#REJ.0160
  projects/forge/10-intent.md#REJ.0170
- links:
  `docs/use/save-your-work.md`: the save.
  `docs/use/release-a-version.md`: the release.
  `docs/use/pull-from-the-remote.md`: the pull.
  `docs/use/work-on-a-branch.md`: branches.
  `docs/use/settle-a-conflict.md`: the step of a conflict, the one place Claude's git asks the principal.
  `docs/about/working-together.md`: the three ways of merging and what the forge promises two people on one project.
  `docs/about/the-ledger.md`: why the ledger is made at read time and kept out of git.
  `docs/about/the-tests.md`: the tests that make the portability rule a run.
  `docs/reference/scripts.md`: the scripts themselves.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no host, identity example or incident story; no git command but the finishing commands named in passing; the other shell named as "the other shell tool", no product name; no list of the hook's verbs and flags; no date of a decision or a test; no issue, pull request, discussion or user the intent cites; no claim of a run on macOS; no `/merge`, worktree, merge driver of the forge's own for record files, landing of branch records or blocks of IDs, which the forge does not have; no project named at whose merges a reason was found; no count of tests.
- made: derived
- evidence: CLAUDE.md, Persistence gives the door, the hook's three answers, the conflict left standing, the integrator's merge with git itself outside the scripts, the registration of the driver `ours`, the main-only rule of whatever makes a derived file or migrates a project, the migration door and, in Portability, the tests in CI and what of the rest is a writing rule; the settings and the hook's header the two shells and the hook; SOL.0520 the wall and the commit with no trailer; SOL.0740 the registration; POS.1710 why derived files are made on main and the refusals; POS.1200 why a hook and not deny rules; POS.0830 the portability rule, the runs in CI and that nothing has run on macOS; POS.1100 the two doors, the order of a release with the tests first and its save without a second light check; POS.1970 what the map and the pull say of the remote beside the state, in one sentence; the other positions the reasons; the two REJ what was rejected. Where no input gives a reason, the page says the reason is not recorded.
- state: regenerate

### docs/about/working-together.md
- title: Working together on one project
- line: What does the forge promise when two people, or two branches, work on one project, and how does each kind of file merge?
- kind: explanation
- reader: user, extender, evaluator
- says: A concept page. What it is: every file of a project has one of three ways of merging, and the forge tells git which through the project's `.gitattributes`. Text: the artefacts, the recipes, the work specifications, the threads, the project file, and the record files (the histories, the decisions, the resource indexes, the documentation map), merged by git, what git leaves in conflict settled by a person. Derived: the ledger, never in git and made at read time; the documents for a reader (the renders, the README, the release notes, CONTRIBUTING, the documentation, the state render, the published companions), made only on `main`, taken as `ours` at a merge and made again, the published files binary; the three root files anchored with a leading slash in the attributes, since a bare name matches at every depth and, where the file system ignores case, in every case. Immutable and unique: reviews, challenges, research, sources and closed threads, which never conflict, a report's name unique across branches. What the forge promises: one person on one project saves and pulls; with two people or two branches, derived state never conflicts, a conflict in a record file is two tails appended after one last line and settled by keeping both, a conflict in an artefact is the same item or sentence changed on both sides and settled by a person with Claude's help in the step of a conflict; IDs stay one sequence and a number taken twice is settled after the merge; a version given twice is found by git as a conflict of the two history tails, the header's version line merging silently when both sides wrote the same number, and is settled in the same step. How it works with several people: one integrator and contributors; a contributor works on a branch and saves it; the integrator, typically the principal, merges it, on the server where the merge request has no conflict, on his own clone with git itself, outside the forge's scripts, through the step of a conflict where it has, since the server merges with no attribute of the forge's; the save rebases one's own commits onto the remote only where both sides moved on, so that the integrator's merge of a branch and a contributor's merge of the upstream keep their merge commit and nothing of the other side is replayed. Two windows of one person on one project are not solved: the person arranges it through git, a branch or a second clone. Why: the ledger was the one file present at every collision, and made at read time it stopped being a thing to merge; two people on one project are the exception and the exception is handled with git; why no merge driver of the forge's own for the record files, no union merge and no merge command of the forge. One worked example: a generic contributor's branch merged by the integrator.
- inputs:
  CLAUDE.md#Persistence (git)
  templates/gitattributes
  projects/forge/10-intent.md#POS.1560
  projects/forge/10-intent.md#POS.1690
  projects/forge/10-intent.md#POS.1700
  projects/forge/10-intent.md#POS.1750
  projects/forge/10-intent.md#POS.1770
  projects/forge/10-intent.md#POS.1790
  projects/forge/10-intent.md#REJ.0280
  projects/forge/10-intent.md#REJ.0340
  projects/forge/10-intent.md#REJ.0350
- links:
  `docs/use/settle-a-conflict.md`: the step of a conflict, done.
  `docs/about/persistence-in-git.md`: the doors to git and why the files for a reader are made on `main` only.
  `docs/use/work-on-a-branch.md`: switching a repository to a branch.
  `docs/use/save-your-work.md`: the save, which pushes a merge made by hand as it stands.
  `docs/about/the-ledger.md`: why the ledger is made at read time.
  `docs/about/stable-ids.md`: how an item number taken twice is settled.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no project named but `forge`, no merge evidenced on a real project named; no fixture, test, plan row, brief version, decision, challenge, pull request, contributor or date the positions cite; no account or hosting address; no GitHub issue or pull request of the forge project; nothing of the rejected mechanisms beyond the reasons they were let go; no attribute or driver that the attributes template does not carry; no claim that the ledger reports a version given twice; no git command the integrator types, which no file gives.
- made: derived
- evidence: POS.1560 gives the three ways and the reason; POS.1690 the attributes, the engine's own list, the server merging with no attribute, and the rebase only where both sides moved on with its reason; POS.1750 the promise; POS.1770 the integrator and the contributors; POS.1790 the number and the version taken twice, the version found by git as a conflict of the two history tails; POS.1700 the two windows; CLAUDE.md, Persistence the record files as text with two tails kept, the integrator's merge with git itself outside the scripts and the step of a conflict as the operating layer has them; the attributes template which paths carry `ours` and `binary` and why the root files are anchored; REJ.0280, REJ.0340 and REJ.0350 what was let go and why. Where the operating layer and the intent differ, the operating layer's wording stands.
- state: regenerate

### docs/about/upgrades-and-migration.md
- title: Upgrades and migration
- line: How does a project follow a new release of the engine, and why does a change of the shape of files come with a migration?
- kind: explanation
- reader: user, extender, evaluator
- says: A concept page. What it is: an upgrade is a fast-forward pull of the engine; a project records no engine version, and the checks measure it against the current conventions; the release notes say in Action required what to do. Artefacts do not expire with the conventions: a finished or dormant project that no longer conforms is a fact to report, never a defect to chase, and bringing it current is the principal's decision per project. How it works: an upgrade of a few lines is brought in by Claude on the user's word after the checks have named it; a release that changes the shape of files comes with a migration, one command with a script for every deterministic step and Claude for what needs judgement. The script recognises a project's shape as a set of marks, one per step, never by an engine version, and runs only the steps missing; it commits nothing and can be undone before the save. A migration runs once per project, on one clone, on `main`, and everyone else pulls; a project outside git is migrated the same, its way back the backup taken before, a run that stops midway finished by running it again, the marks being its memory. Until a project is migrated nothing writes into it, since the engine cannot write two shapes. Why: an upgrade that rewrites files of every project, in every clone, must come out the same everywhere, which a hand migration cannot promise; why a project records no engine version is not recorded. One worked example: a generic project going from the old shape to the new.
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
- must-not: no version numbers or names of releases; no conversion to one sentence per line, no refusal over unmerged branches, which are not built; no git command for the way back; no thread, challenge or date the positions cite; no project other than `forge` named; no reason invented for the missing engine version.
- made: derived
- evidence: POS.0940 the upgrade path and the narrowing to a migration for a shape change, the rule that a project records no engine version with no reason given; POS.0820 that artefacts do not expire and that a project of the old shape is read, not written; POS.1740 the one command, the marks, once per project on one clone, a project outside git, and the reason; CLAUDE.md, Persistence the migration door as the operating layer says it; the project file skeleton what a project without the file is; the script's header the marks, the dry run, `--apply`, `--undo`, the refusals and a project outside git.
- state: regenerate

### docs/about/how-the-rules-are-held.md
- title: How the rules are held
- line: How does the forge keep its rules in force across a long conversation and inside a subagent?
- kind: explanation
- reader: extender, evaluator
- says: One always-on core, `CLAUDE.md`, loaded into every session and subagent; everything else a file read when its situation arises. One mechanism lives in one place and is cited by path everywhere else. A rule that must hold through a long conversation is repeated at every prompt by a hook; what the hook prints (the one-item rule, the pointer to the walkthrough's shape, and four lines of conduct: the forge's scripts before any tool, asking before a command of one's own, nothing changed that was not agreed, and every question that asks the principal to decide closed with the verdict line). The harness enforces what it can: deny rules keep Claude from sensitive paths and keep the other shell tool from git; a second hook holds the line between reading git and writing it (one sentence, link). A command that changes files the moment it runs starts on the principal's word and never on Claude's judgement: he invokes it by slash, or asks in words and Claude invokes the skill itself, never its steps replayed by hand; the guard is conduct, the step-by-step method and the wall on git, and no command carries a field of the harness that blocks the model from it, since that field did not make Claude wait for the word but made him mimic the command outside the skill where the principal could not see it. A subagent may take the session's copy of a file for the file on disk, so every isolated subagent reads its inputs from disk, and generated files are scanned mechanically. One model for the whole forge. The forge's behaviour never lives in the assistant's memory. The forge explains itself through one door, `/man`, a reader with no text of its own: it reads the definitions and the documentation in the run and never answers from memory, and a need said in free words gets the way the forge has for it; there is no second help command, because a second name for a question is one more thing to learn. One worked example, generic.
- inputs:
  CLAUDE.md#Prime directives
  CLAUDE.md#Working methods
  CLAUDE.md#Isolated reviewers
  .claude/settings.json
  scripts/hook-walkthrough.py
  scripts/hook-git.py
  projects/forge/10-intent.md#POS.0930
  projects/forge/10-intent.md#POS.0950
  projects/forge/10-intent.md#POS.1030
  projects/forge/10-intent.md#POS.1070
  projects/forge/10-intent.md#POS.1090
  projects/forge/10-intent.md#POS.1170
  projects/forge/10-intent.md#POS.1190
  projects/forge/10-intent.md#REJ.0500
  projects/forge/10-intent.md#POS.1200
  projects/forge/40-solution-design.md#The instruction layer
  projects/forge/40-solution-design.md#SOL.0110
- links:
  `docs/extend/what-it-is-made-of.md`: the files of the operating layer.
  `docs/about/persistence-in-git.md`: the hook that holds the line between reading and writing git.
  `docs/about/working-methods.md`: the step-by-step method the guard rests on.
  `docs/use/look-up-a-command.md`: the manual, `/man`, as you use it.
  `docs/reference/configuration.md`: the settings, exactly.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no claim that a hook or a deny rule guarantees behaviour; no incident story or date; no thread of the forge project; nothing of the hooks' docstrings beyond what the walkthrough hook prints and what the git hook answers; no list of the git hook's verbs; no list of the guarded commands beyond the criterion; no trial of the manual or count of trial questions; no span of dates the design gives for the dropped field; nothing of REJ.0500 beyond the help command it rejects.
- made: derived
- evidence: prime directive 10 and the Walkthrough method give the one-place rule and the hook with its four lines of conduct; CLAUDE.md, Isolated reviewers that every isolated subagent reads its inputs from disk because its copy of the core may be older; the settings the deny rules and the two hooks; the walkthrough hook's `LINES` what it prints; the git hook's header that it holds the line, in one sentence; the positions the reasons, POS.1090 the criterion of a guarded command, that the guard is conduct and the wall on git, and why the harness field was dropped; SOL.0110 that no command carries the field and every skill is model-invocable; POS.1190 the manual as a reader that answers a need from the documentation and the definitions read in the run; REJ.0500 why there is no second help command; the design's group how the core, the instance file, the hook and the walkthrough skill are realised.
- state: regenerate

### docs/about/languages.md
- title: Languages
- line: Which language does each kind of document carry, and why only one output language per project?
- kind: explanation
- reader: user, evaluator
- says: The forge dictates one output language per project: the artefacts in the language the project file declares, English when absent, and the documentation's pages with them, written in the project's language as its artefacts are; records, state, research and recipes always English, because they are read by Claude, the reviewers and the checks and never handed to the recipients, and one operating language lets them read every project the same way; English the notation throughout, ID prefixes, status words, front-matter keys and the fixed labels of a story among it; the verb of a requirement follows the language of the artefact, shall and shall not in English and the language's own verb of obligation elsewhere, the forge naming no word of another language; the briefs the one exception, kept in whatever language they are written in; a work specification follows the artefacts and its file the language its Making section says; a render in any language, or languages, its recipe declares, the first primary and the rest its translations, said in one sentence with a link; the README English only, a translation a render. The conversation language is an instance fact, never shown outward; the README and the other outward-facing renders state only the output-language rule. Translate on write. One worked example, generic.
- inputs:
  CLAUDE.md#Prime directives
  .claude/skills/docs-contract/SKILL.md#What must never reach a page or the map
  projects/forge/10-intent.md#POS.0060
  projects/forge/10-intent.md#POS.0250
  projects/forge/10-intent.md#POS.1450
  projects/forge/10-intent.md#POS.2010
- links:
  `docs/start/setup.md`: where the conversation language is set.
  `docs/about/renders-and-recipes.md`: a recipe in several languages.
  `docs/about/the-documentation.md`: the pages, generated in the project's language.
  `docs/about/the-assignment.md`: the obligation of a requirement and why its verb follows the artefact's language.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no language value of an instance; no example project; nothing of the prime directives but directive 6; nothing of POS.1450 but the language of the pages and of the README; nothing of the contract but the language of a page; nothing of POS.0250 beyond the verb following the artefact's language; nothing of POS.2010 beyond the labels of a story staying English; no language, project or date the positions cite as the case that changed a rule.
- made: derived
- evidence: prime directive 6 gives the rule, the project file as its source, the documentation in the project's language, the work specification, the briefs' exception and the languages of a render; the contract that a page is in the project's language; POS.0060 the reason for one operating language of the records, that the verb of a requirement follows the language of the artefact and that the conversation language is never presented outward; POS.0250 the obligation in the indicative with shall in English and the language's own verb elsewhere; POS.2010 the fixed English labels of a story; POS.1450 that the pages are written in the project's language and the README stays English. Where no input gives a reason, the page says the reason is not recorded.
- state: regenerate

### docs/about/where-it-is-going.md
- title: Where the forge is going
- line: In which direction is the forge developed, and what is deliberately not promised?
- kind: explanation
- reader: user, extender, evaluator
- says: Direction without destination: the chain is extended downward as far as the principal needs a thought taken; the BRD and the user stories exist, integration is intended, a strategy layer possible; nothing further approved for construction, the mechanics of a layer designed when it is taken up. A new kind of artefact is added by one command; a user is to be able to add one of his own at his own place, which is open. A model of another family is reached today for research; reviewers on that link, a challenger and a critic lens, are intended and not built. The forge's own project is to become a repository of its own beside the engine, so that a user clones the engine alone and a contributor clones the project beside it; today the engine still tracks it, and the order of the cut is decided. One principal per instance for now, and the chain never spans two principals. Developed at its owner's discretion and pace; feedback and ideas are wanted most.
- inputs:
  projects/forge/10-intent.md#POS.0700
  projects/forge/10-intent.md#POS.0780
  projects/forge/10-intent.md#POS.0800
  projects/forge/10-intent.md#POS.1430
  projects/forge/10-intent.md#POS.1440
  projects/forge/10-intent.md#POS.1980
  projects/forge/10-intent.md#POS.1990
- links:
  `docs/about/the-document-chain.md`: how a layer is added.
  `docs/about/another-model-family.md`: the link to another model family as it stands.
  `docs/about/projects-and-the-engine.md`: the engine and the projects as they are today.
  `docs/extend/how-a-change-is-made.md`: how a change reaches the forge.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no thread quoted; no date; no version; no company rollout; no name; no vendor, product or model family of the planned reviewers; no challenge number; no account or repository name beyond that the project is to be a repository of its own; no pull request or user the intent cites.
- made: derived
- evidence: positions only; POS.1980 gives the forge's own project as a repository of its own as a decided direction with its order, and that the engine still tracks it today; POS.1990 that the user stories exist. Where no input gives a reason, the page says the reason is not recorded.
- state: regenerate

### docs/about/the-tests.md
- title: The tests
- line: What do the engine's tests cover, what is the fixture they run on, and why are they in proportion rather than complete?
- kind: explanation
- reader: extender, evaluator
- says: A concept page. What it is: the engine's scripts have tests, in `tests/` at the engine root beside the scripts they test, run by pytest from the engine root; `/test` is the one door and `python -m pytest` the command it runs; pytest is the one thing a contributor installs beyond `python`, and a user of the engine never runs them and installs nothing for them. In proportion: enough to catch what a change of a script breaks, never a suite for its own sake, no coverage figure as a target. How it works: what is tested, in the order it was built, the deterministic cores first (the front-matter, the records of a history, the reader of the documentation map, the git hook's judgement over a command, the ledger made from the documents, the light check as a program), then the git scripts on the fixture (status, save, branch, pull, the step of a conflict standing and finished, a standing rebase refused, the derived file taken as ours with the registration and in conflict without it, a merge by hand pushed as it stands), while what calls pandoc, markitdown or the model is tested for its failure without the tool alone, naming the tool; not tested, the skills, the agents, the text of the core and the run of the screenplay script. The fixture, `tests/fixture`: a synthetic thought project of the current shape with a made-up subject, one of each kind of document the scripts read, marked as a fixture in its project file, never a copy of a real project and never under `projects/`; a test works on a copy of it in a temporary directory, as a repository with a bare origin beside it where it needs git, and the fixture itself is never changed; it conforms to the light check, so a template it no longer follows turns a test red, which is the signal wanted. What the tests share (a script loaded without its main, a script run as the forge runs it, the copy of the fixture, git with an empty global configuration, the copy as a repository and a second clone) lives in one file beside them. A script takes a project by its slug or by the path of its directory, so that a copy in a temporary directory is reached by a path, visible in the command. CI runs the same suite at every push and pull request, on Linux and Windows, Python 3.8 and the newest, macOS not until someone asks for it; the git tests run with an empty global configuration and no system one, the identity set in the throwaway repository alone, so that the user's guard, stanzas and registration change nothing and CI without them sees the same. A release of the engine runs the tests before anything else and a red test stops it; a save never runs them, every push running them in CI. Why: thousands of lines of Python and not one test is the first thing a contributor looks for and the first thing a change breaks; real content does not belong in the public engine and a fixture under the gitignored projects directory would reach neither a contributor nor CI; the portability rule becomes a run instead of a writing rule, and a test that depends on the machine it runs on tests the machine; a path is an argument everyone sees, where an environment variable or a branch in the scripts for a test project would be a setting hidden from the command. One worked example: a generic test over the copy of the fixture, in words.
- inputs:
  projects/forge/10-intent.md#POS.1930
  projects/forge/10-intent.md#POS.1940
  projects/forge/10-intent.md#POS.1950
  projects/forge/10-intent.md#POS.1960
  projects/forge/10-intent.md#REJ.0510
  projects/forge/10-intent.md#REJ.0520
  projects/forge/10-intent.md#REJ.0530
  projects/forge/40-solution-design.md#SOL.0900
  projects/forge/40-solution-design.md#SOL.0830
  pytest.ini
  .github/workflows/tests.yml
  templates/project.md
- links:
  `docs/use/run-the-tests.md`: running `/test`.
  `docs/extend/add-a-script.md`: changing a script with its test.
  `docs/about/persistence-in-git.md`: the portability rule the tests make a run.
  `docs/use/release-a-version.md`: the release that runs the tests first.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no count of tests or lines as a fact; no thread, brief, decision or date the positions and the design cite; no content of a test file; no real project or the fixture of the cutover named; no account or address of the CI; no slug from the scripts' examples.
- made: derived
- evidence: POS.1930 gives the tests, their place, the one door, the proportion, what is tested in which order and the reason; POS.1940 the fixture, how a test uses it and the reason; POS.1950 the slug or the path and the reason; POS.1960 the CI matrix, the empty git configuration and the reason; the three REJ what was weighed against the path and the fixture; SOL.0900 what the tests share, the files one per concern, the CI workflow and the release's step; SOL.0830 what the fixture holds and that a test never touches it; `pytest.ini` the test path and the import path; the workflow the matrix and the install; the project file skeleton the fixture flag. The order is the writer's, what, how, why.
- state: new

### docs/about/the-security-policy-and-the-code-of-conduct.md
- title: The security policy and the code of conduct
- line: What are the two fixed files of the root, what does the security policy promise, and why is neither a render?
- kind: explanation
- reader: user, extender, evaluator
- says: A concept page. What it is: beside the renders of the root stand two files that are no render and derive from nothing in the chain: `SECURITY.md`, the security policy, the principal's own text, and `CODE_OF_CONDUCT.md`, the code of conduct, the Contributor Covenant 3.0 word for word under its own licence, named in the README beside the engine's licence, its reporting sentence pointing at the private way the contributing file names, its suggested remedies kept. How it works, the policy by kind: a problem is reported through GitHub's private vulnerability reporting, a setting of the repository switched on before the file points at it, with the private way of the contributing file as the fallback and never a public issue; the forge promises an acknowledgement within seven days, a fix or a decision at the principal's pace told to the reporter first, credit in the advisory unless declined, and nothing else, no bounty, no safe harbour, no form; supported is the latest release on `main` only, a fix the next release; what the forge does on the machine is said by kind, instruction files, no server, the user's permissions, programs from PATH, nothing sent but what the user sends, data that may carry instructions, permissions a guard and not a sandbox, the specifics left to the documentation pages a release regenerates, so that the file stays true without a recipe; in scope is a script, a hook, a file of the engine or a piece of data making the forge write, run, send or publish what its rules do not say, out of scope Claude Code and the tools the scripts call, the user's permission mode and the content of his projects. Neither file is a render; neither has a companion, a row or a check, as holds for the principal's own files; a change to either is the principal's word. Why: a policy whose threat model is derived from the design stays true only when re-rendered, and a release re-renders the documentation, not a policy; a standard adopted is worth exactly its unchanged text. One worked example: the shape of a report a visitor would send, in words.
- inputs:
  projects/forge/10-intent.md#POS.1920
  CLAUDE.md#Repository layout
- links:
  `docs/extend/how-a-change-is-made.md`: the contributing file a visitor reads, which points at both.
  `docs/about/renders-and-recipes.md`: what a render is and what the principal's own files beside the forge's are.
  `docs/reference/repository-layout.md`: where the two files stand among the root's files.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no address, profile or account; no research or decision date the position cites; no text of either file quoted; no name of a person; no claim about the repository's settings beyond what the position says.
- made: derived
- evidence: POS.1920 gives both files, what the policy promises and holds by kind, what the code of conduct is, that neither is a render nor has a companion, a row or a check, and the reason; CLAUDE.md, Repository layout the two files among the root's files, each as no render. The example is the writer's shape from the policy's scope, taken from no report.
- state: new

## extend

### docs/extend/what-it-is-made-of.md
- title: What the forge is made of
- line: Which files make up the operating layer, what is each, and when is it loaded?
- kind: how-to
- reader: extender
- says: Opens with a table (path, what it is, loaded when): `CLAUDE.md`, the always-on core; `.claude/skills/<name>/SKILL.md`, one per command, with the `/forge` state files and the `/recipe` genre files as supporting files, and the skills that are not commands (the three reviewer contracts, the documentation contract, the walkthrough skill); `.claude/agents/`, one file per lens, persona and check, and the documentation's planner and writer; `.claude/settings.json`, the two hooks and the deny rules (the two sensitive paths and git in the other shell tool); `templates/`, the skeletons, the player page's skeleton among them; `scripts/`, Python with the shared modules beside them, the two hooks among the scripts; `tests/`, the engine's tests with their fixture, `pytest.ini` how they run, the CI workflow that runs them at every push; `.gitattributes`, the engine's own ways of merging its derived files; `.mailmap`, git's own mapping of the author's names in the history to one handle; `tmp/`, the engine's working folder, in git with its own README and ignore file, its contents never, no source of truth and read by no check, ledger or history, kept for inspection and emptied by hand; `projects/forge`, the forge's own project; `docs/`, the generated documentation, with `docs/videos/` the public folder of the videos, not the documentation's; at the root beside the renders the two fixed files, the security policy and the code of conduct, no render and the principal's word. Then one line of flow. Then the ideas that carry it. One worked example: one command traced through the layer.
- inputs:
  CLAUDE.md#Repository layout
  CLAUDE.md#Templates
  CLAUDE.md#Persistence (git)
  tmp/README.md
  projects/forge/10-intent.md#POS.1900
  projects/forge/10-intent.md#POS.1920
  projects/forge/40-solution-design.md#How the parts work together
  projects/forge/40-solution-design.md#The instruction layer
  projects/forge/40-solution-design.md#The commands
  projects/forge/40-solution-design.md#SOL.0300
  projects/forge/40-solution-design.md#SOL.0330
  projects/forge/40-solution-design.md#SOL.0900
  projects/forge/40-solution-design.md#Across the parts
  .claude/settings.json
- links:
  `docs/reference/repository-layout.md`: the layout block.
  `docs/reference/templates.md`: every skeleton.
  `docs/about/how-the-rules-are-held.md`: why the core is small and the rest on demand.
  `docs/about/the-tests.md`: what the tests cover and what the fixture is.
  `docs/about/the-security-policy-and-the-code-of-conduct.md`: the two fixed files of the root.
  `docs/extend/how-a-change-is-made.md`: changing any of it.
  `docs/about/the-documentation.md`: what `docs/` and the map are.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no listing of individual commands or agents; no file of an instance; no repository address; no count of pages, tests or date of a run; no thread named in the layout comments; no script, command or template the design names that does not exist on disk (a record driver, a merge command, a fixture script, ID reservations); no position the design's head lists as answered by no part; no file found in `tmp/` named; no name or e-mail of the mailmap's content.
- made: derived
- evidence: CLAUDE.md, Repository layout and Templates give the directories, the settings with the two hooks, `tmp/`, the tests, the CI workflow, the mailmap, the two fixed files and the `<type>-definition.md` rule; Persistence (Portability) the shared modules and the tests in CI; `tmp/README.md` and POS.1900 what the working folder holds and that nothing in it is a source of truth; POS.1920 the two fixed files as no render; `.claude/settings.json` the two deny rules on sensitive paths, the deny rule on git in the other shell tool and the two hooks; the design's head the ideas and its groups what each kind of file is and when the harness loads it; SOL.0300 and SOL.0330 the reviewer files; SOL.0900 the tests, the fixture, `pytest.ini` and the workflow. The table and the line of flow are the writer's join.
- state: regenerate

### docs/extend/how-a-change-is-made.md
- title: Make a change to the forge
- line: How is a change of the forge's behaviour made, proved, recorded and released?
- kind: how-to
- reader: extender
- says: A change of how the forge behaves goes through the chain before it is built: a position in the forge intent through `/forge intent forge`; the item of the solution design through `/forge solution-design forge`; then the operating layer. Where a change of the operating layer needs a test, the order is: the brief first, in the principal's words, then the build and its test, then the rounds of the intent and the design right after it, never across a release. A script is changed with its test in `tests/`, run by `/test` or `python -m pytest`. Proved by `/test` for a script, `/check engine` and, before a major or after a round on the operating layer, `/check single-source-of-truth`; recorded in the history companions; released by `/release forge`, which runs the tests first; a process change is complete only once the intent is updated and the README re-rendered. A change that alters no behaviour is made directly. The README, the release notes and CONTRIBUTING are renders: a change goes into their recipes; the README and the release notes are regenerated by every release, CONTRIBUTING on `/render contributing` and not by a release. A visitor's way to send feedback, an idea or a change is `CONTRIBUTING.md`, the channels by kind, a pull request carrying the position, the item, the change and one line on what was run, a script's test among it; everything that enters the forge's own project is English, a brief included; in a clone the user decides everything, what is merged into the public engine its author decides. One worked example: one invented change traced through.
- inputs:
  CLAUDE.md#The system's own project
  CLAUDE.md#Versioning & status
  projects/forge/10-intent.md#POS.0720
  projects/forge/10-intent.md#POS.0900
  projects/forge/10-intent.md#POS.1440
  projects/forge/10-intent.md#POS.1780
  projects/forge/10-intent.md#POS.1930
  .claude/agents/check-engine.md
  .claude/agents/check-single-source-of-truth.md
  .claude/skills/release/SKILL.md
  .claude/skills/test/SKILL.md
  projects/forge/recipes/contributing.md#Instructions
  projects/forge/40-solution-design.md#SOL.0450
  .claude/skills/render/SKILL.md
- links:
  `docs/use/forge-the-intent.md`: iterating an intent.
  `docs/use/check-conformance.md`: running the checks.
  `docs/use/run-the-tests.md`: running the tests.
  `docs/use/release-a-version.md`: the release.
  `docs/use/render-an-output.md`: regenerating a render such as CONTRIBUTING from its recipe.
  `docs/use/generate-the-documentation.md`: regenerating the pages.
  `docs/about/the-security-policy-and-the-code-of-conduct.md`: the two fixed files the contributing file points at.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no channel URL, account, profile or name; no pull-request mechanics beyond what the recipe gives; no claim that the release regenerates the documentation on its own; no brief, plan, fixture, release number or date of the forge project; no count of tests.
- made: derived
- evidence: CLAUDE.md gives the completeness rule and the `operating layer` subject; the positions intent-first, the open rule, POS.1780 the order of a change that needs a test and POS.1930 that a script is changed with its test and a pull request carries it; the contributing recipe's Instructions the line between the two kinds of change, who decides what, the channels by kind, the English of the forge's own project, the sentence on tests and the two fixed files pointed at; SOL.0450 that CONTRIBUTING is a render of its recipe made on `/render contributing` and not by a release; the two check agents what proves a change; the test skill and the release skill that the tests run by `/test` and first at a release; the release skill what a release re-renders; the render skill the command that regenerates a render.
- state: regenerate

### docs/extend/add-an-artefact.md
- title: Add an artefact
- line: How is a new kind of artefact added to the chain with `/new-artefact`?
- kind: how-to
- reader: extender
- says: An add page: `/new-artefact <name>` leads to everything a kind needs and decides nothing: a position in the forge intent first; the definition in the seven blocks from `templates/artefact-definition.md` and its template `templates/<name>.md`; the row of a new prefix; the reviewers; the item of the solution design. Where the kind needs a trial on real work before its position can hold, the order changes: the brief first, then the pair with its reviewers, the trial, then the position and the item of the design, the brief the authority until then. The rosters need nothing: `/forge`, `/man` and the README read the definitions from disk. Prove it: `/check engine`; the first artefact of the kind through `/forge <name>` on real work is the trial. Recorded and released as any change. One worked example with `<name>`.
- inputs:
  .claude/skills/new-artefact/SKILL.md
  templates/artefact-definition.md
- links:
  `docs/extend/how-a-change-is-made.md`: proving, recording and releasing the change.
  `docs/about/elicitation.md`: the seven blocks and the Map.
  `docs/about/where-it-is-going.md`: the layers the forge's owner intends to add.
  `docs/extend/add-a-challenger-persona.md`: the persona a kind may need.
  `docs/extend/add-a-check.md`: the check a kind may need.
  `docs/reference/templates.md`: the skeletons a definition and a persona start from.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no planned artefact named as if being added; no brief of the forge project; no kind of the forge named as the example of the trial order.
- made: mirrored
- state: regenerate

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
  .claude/agents/check-engine.md
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
  .claude/agents/check-engine.md
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
  .claude/agents/check-engine.md
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
- says: An add page: a genre is two files: `.claude/skills/recipe/genres/<genre>.md`, a definition with a one-line description, the skeleton and output, a role and a numbered elicitation checklist, and `templates/recipe-<genre>.md`, the skeleton that extends the base recipe shape, with a `## Format` section where the render has a file beside it and `languages:` where the genre allows translations. Every genre runs in the same frame: the checklist closes with the language question and the recipe is composed from the skeleton. The dispatcher never changes; bare `/recipe` scans the directory, and `/man recipe` prints each genre's description and its elicitation checklist in full. Prove it: a composition on a project through `/recipe <genre>`, then `/render <recipe>` of what it composed. Recorded and released as any change. One worked example with `<genre>`.
- inputs:
  .claude/skills/recipe/SKILL.md
  .claude/skills/recipe/genres/presentation.md
  templates/recipe.md
  templates/recipe-presentation.md
  .claude/skills/man/SKILL.md
- links:
  `docs/extend/how-a-change-is-made.md`: proving, recording and releasing the change.
  `docs/reference/recipe-genres.md`: the genres that exist.
  `docs/about/renders-and-recipes.md`: what a recipe is.
  `docs/use/compose-a-recipe.md`: the composition that proves a genre.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no checklist copied as content; no genre named as planned; no check named as the proof, since no check verifies a genre file.
- made: derived
- evidence: the `/recipe` skill says a genre is two files, that the dispatcher never changes and gives the shared frame with the language question and the offer of `/render` after a recipe is written; the presentation genre file and its skeleton are the model of the two shapes; `templates/recipe.md` owns the base shape, `languages:` among it; the `/man` skill's command page prints the roster a command dispatches over, for a genre its elicitation checklist in full. The proof is the writer's join of the skill's offer of `/render` with a composition; no check of the engine names the genre files.
- state: keep

### docs/extend/add-a-command.md
- title: Add a command
- line: How is a new command added as a skill, and how does a command that writes wait for the principal's word?
- kind: how-to
- reader: extender
- says: An add page: a command is a skill `.claude/skills/<name>/SKILL.md`: front-matter with `description` and a quoted `argument-hint`; a body that says what the command does and cites every mechanism of another by path; supporting files beside it where it dispatches over a roster. No command carries a field of the harness that blocks the model from it: every skill is model-invocable, and a command that writes, scaffolds, commits or regenerates starts only on the principal's word, invoked as a skill through the harness's Skill tool, never replayed from its definition by hand; the guard is conduct, the step-by-step method and the wall on git. A row in the Commands table of `CLAUDE.md`. Named so that it does not collide with a built-in of Claude Code. Prove it: `/check engine`; `/check single-source-of-truth`. Recorded and released as any change. One worked example with `<name>`.
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
  `docs/about/how-the-rules-are-held.md`: why the guard is conduct and not a field of the harness.
  `docs/reference/commands.md`: the commands that exist.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no skill body copied; no harness detail beyond what the solution design states; nothing of POS.1050 beyond the naming rule; no span of dates the design gives for the dropped field.
- made: derived
- evidence: SOL.0100 gives the skill shape and the quoted hint; SOL.0110 that no command carries the harness field, that every skill is model-invocable and that a guarded command starts on the principal's word through the Skill tool; POS.1090 the criterion of a guarded command, the guard as conduct and the wall on git, and why the field was dropped; POS.1070 citation over restatement; CLAUDE.md, Commands the table; the `ledger` and `end` skills the smallest models; the `check-engine` agent that the table is verified against the skills; POS.1050 and POS.1190 the naming rule.
- state: regenerate

### docs/extend/add-a-script.md
- title: Add a script
- line: How is a new script written so that it is portable, documented in its docstring, tested with its change and the one owner of its facts?
- kind: how-to
- reader: extender
- says: An add page: a script is Python 3.8 or newer, run as `python scripts/<name>.py`, with its help in its module docstring: synopsis, what it does, what it needs, options, where the output lands, examples; the docstring owns those facts and commands cite it. Rules: nothing Windows-only, `pathlib`, `subprocess` with argument lists, external tools resolved from PATH and never installed, colour only on a terminal, examples free of platform paths, no URL and no identity; a script that takes a project takes it by its slug or by the path of its directory through the one resolver of the shared module, so that a copy in a temporary directory is reached by a path. The scripts are written to run unchanged on Linux and macOS, and the tests run in CI on Linux and Windows at every push; nothing has run on macOS, so a new script is written to the rule. What several scripts share lives in one module beside them, five today: `forge_repos.py`, `forge_tools.py`, `forge_docs.py`, `docs_map.py`, `forge_check.py`, each with the scripts it serves in one clause. A script's working files go to the engine's working folder `tmp/`, never to the system's temporary directory. Named in the layout comment of `CLAUDE.md`. A script is changed with its test: one test file per concern in `tests/`, run by `/test`, using what the tests share (a script with a hyphen in its name loaded as a module without its main, a script run as the forge runs it, a copy of the fixture, git with an empty global configuration, the copy as a repository with a bare origin and a second clone); a script that calls an external tool is tested for its failure without the tool, naming the tool and how it is installed; never a test on a live repository. Prove it: `/test`; `/check engine`, which verifies that every file in `scripts/` is described in the layout comment and nothing described there is missing on disk. Recorded and released as any change, the release running the tests first. One worked example: a generic docstring and the test that goes with it, in words.
- inputs:
  CLAUDE.md#Persistence (git)
  CLAUDE.md#Repository layout
  scripts/forge-status.py
  scripts/forge_repos.py
  .claude/agents/check-engine.md
  .claude/skills/test/SKILL.md
  pytest.ini
  projects/forge/10-intent.md#POS.0830
  projects/forge/10-intent.md#POS.1900
  projects/forge/10-intent.md#POS.1930
  projects/forge/10-intent.md#POS.1950
  projects/forge/40-solution-design.md#SOL.0620
  projects/forge/40-solution-design.md#SOL.0890
  projects/forge/40-solution-design.md#SOL.0900
- links:
  `docs/extend/how-a-change-is-made.md`: proving, recording and releasing the change.
  `docs/use/run-the-tests.md`: running the tests.
  `docs/about/the-tests.md`: what the tests cover and what the fixture is.
  `docs/reference/scripts.md`: the scripts that exist.
  `docs/about/persistence-in-git.md`: why the scripts are the only door.
  `docs/extend/add-an-engine.md`: a row of the engine script, which needs no script of its own.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no claim of a run on macOS and none on Linux beyond what CLAUDE.md, Portability, and POS.0830 say; no issue, pull request or user the intent cites for the run on Linux; no instance path; no mention of PowerShell; no script body; nothing of SOL.0620 beyond how the scripts are written and what they share; no date; no count of tests or cases; no content of a test file beyond the names of what the tests share.
- made: derived
- evidence: CLAUDE.md, Persistence (Portability) gives the writing rules, the five shared modules and the tests in CI, Repository layout the layout comment and `tests/`; POS.0830 the reason and that nothing has run on macOS; SOL.0620 how the scripts are written, which scripts each module serves and the slug or the path through one resolver; POS.1950 the slug or the path with its reason; POS.1900 and SOL.0890 that `tmp/` is the one working folder and why it is chosen over the system's temporary directory; POS.1930 that a script is changed with its test, what is tested for a tool it calls and never a live repository; SOL.0900 what the tests share, one file per concern and the release's step; `pytest.ini` the test path and the import path; the test skill the command; `forge-status.py` the smallest model of a docstring, `forge_repos.py` of a shared module and the one resolver; the `check-engine` agent's clause that scripts on disk are verified against the layout comment of CLAUDE.md.
- state: regenerate

### docs/extend/add-an-engine.md
- title: Add an engine
- line: How is a model of another family added as one row of the engine table, and how is the row proved?
- kind: how-to
- reader: extender
- says: An add page. An engine is one row of the engine table of `scripts/forge-engine.py` and its pair in `COMMANDS`: one function that builds the engine's command line and one that reads its envelope. The row holds the engine's command-line tool in its one-shot, non-interactive shape (the prompt, the packet folder added as the workspace, the JSON envelope asked for, a time limit, and where it has them the model, the effort, a schema, the sandbox and the flag that approves every tool call); the fields of its envelope the script reads (a status that says success, a non-empty response, the usage) and whether the model is in it; a version floor where a bug is known. The script writes a per-run profile in the engine's own settings shape with the web allowed and the forge's tree, the shell and every write denied; the settings path of the profile is written for the first engine and moves into its row when a second engine comes. The forge names engines and tiers, never models or versions, so that a name always means the newest of its kind; it carries no key or account: the login is the user's, made once in the engine's own tool, and how the tool is installed and signed in is the tool's own documentation's. The row's name is what `/research --deep --engine <name>` takes. Prove it: a trial of the engine alone with `--no-profile` on a scratch packet under `tmp/research/`, which is a trial and never a research; then a run with the profile, `python scripts/forge-engine.py <name> --packet tmp/research/<run>/<card> --out tmp/research/<run>/<card>/<name>.md --allow-all --sandbox`, with a check that the profile's deny rules hold; then `/research --deep --engine <name> <topic>` on a real question. Recorded and released as any change. One worked example with `<name>`.
- inputs:
  scripts/forge-engine.py
  .claude/skills/research/SKILL.md
  projects/forge/10-intent.md#POS.1880
  projects/forge/40-solution-design.md#SOL.0870
- links:
  `docs/extend/how-a-change-is-made.md`: proving, recording and releasing the change.
  `docs/about/another-model-family.md`: what the link to another engine is and why it is a command-line tool.
  `docs/reference/scripts.md`: the engine script, its flags and exit codes.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no script body beyond the names the header and the design give (`ENGINES`, `COMMANDS`); no row invented beyond the one the header shows; no flag of another vendor's tool; no vendor, product or model family named beyond the row `antigravity` and its tool `agy`; no date or probe; no path of the user's settings file or of the profile; no packet path of the forge project's research; no check named as the proof, since no check verifies a row of the table.
- made: derived
- evidence: the script's header gives the table (one row each, a new engine a row and its pair in `COMMANDS`), the shape of the one row, the envelope's fields, the version floor, the profile and the flags with `--no-profile` as a trial; SOL.0870 that the pair is one function building the command and one reading the envelope, that the profile's settings path is written for the first engine and moves into its row with a second, and the price of one settings shape per engine; the research skill that `<name>` is a row of the table and that the forge names engines, never models; POS.1880 the login, no key and no configuration, the installation as the tool's own documentation's, the one-shot shape shared by the command-line tools, and that the forge names engines and tiers, never versions, with the reason. The order of the proof is the writer's join of the header's trial form and the skill's run form; no check of the engine names the table.
- state: regenerate

### docs/extend/change-a-documentation-page.md
- title: Change a documentation page
- line: How do you change what a page says, which pages exist, or what the check refuses, without editing a page?
- kind: how-to
- reader: extender
- says: A page is never edited by hand, because the next run of `/document` writes it again from its owners and the mend is gone; what is wrong is mended in the file that owns the matter and the page regenerated. Finding the owner: the page's front-matter lists its inputs. To change what a page says: change the owning file and run `/document`, which remakes only the pages whose inputs, entry or generating rule changed. To change the shape every page has, or what kind of content a page of each kind carries: the writer's definition and the documentation contract are hashed with the inputs, their whitespace normalised so that a re-wrap regenerates nothing. To change which pages exist or who reads it: the map is written by the planner from the target at every run, the readers and the outline are the planner's definition and a position of the forge intent. A fact a page needs and no file owns is reported under Unowned; the readme skeleton's "Pinned facts (not rendered)" is that home. What a run cannot place, an unowned fact, a disagreement of the map and an owner, a reason a page wants and no file records, is filed by the run as a check's report in `reviews/` and settled by walkthrough, the mend landing in the owner. What the check refuses. An agent's definition is loaded once per session. One worked example: one invented fix traced through.
- inputs:
  .claude/skills/document/SKILL.md
  .claude/skills/docs-contract/SKILL.md
  .claude/agents/docs-planner.md
  .claude/agents/docs-writer.md
  scripts/docs-state.py
  scripts/docs-check.py
  templates/recipe-readme.md#Pinned facts (not rendered)
  projects/forge/10-intent.md#POS.1450
- links:
  `docs/use/generate-the-documentation.md`: running the command.
  `docs/reference/documentation-map.md`: the fields of an entry and of a page's front-matter.
  `docs/extend/how-a-change-is-made.md`: the chain a change of the forge goes through.
  `docs/use/check-conformance.md`: how a report's findings are settled by walkthrough.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no model name; no agent text as an instruction to Claude; no address; no page named as an example that may not exist; no instance fact; nothing of the check script's `--file` mode; nothing of POS.1450 beyond why a page is never mended by hand and what the run files.
- made: derived
- evidence: the `/document` skill gives "mended in the file that owns the matter", the state computed from the inputs, the twice-failing page, the report of the run filed in `reviews/` and the harness note; the contract what must never reach a page and the kinds of a page; the writer the page's front-matter; the planner that the map is written from the target at every run and Unowned; the state script's docstring the parts and the generator hashed with its whitespace normalised; the check script's docstring what it looks for; the readme skeleton's comment the home of pinned facts; POS.1450 why a page is never mended by hand and that what a run cannot place is a finding of the run.
- state: regenerate

## reference

### docs/reference/commands.md
- title: Commands
- line: Every command with its signature, purpose and arguments.
- kind: reference
- reader: user, extender, evaluator
- says: A roster page: one overview table first (command, purpose, arguments, the skill file), then one entry per command in the order of the Commands table of `CLAUDE.md`: the row's signature and purpose, the skill's `description` and `argument-hint`; `/work`, `/research` with its two depths and `--engine`, `/release` with `--auto`, `/pull`, `/end`, `/history`, `/test` with its pytest arguments, `/migrate`, and `/man` and `/manual` with their three arguments (a command, a method, a question in free words) included. One line below the table: a command that writes starts on the principal's word, as every command's page says.
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
  .claude/skills/test/SKILL.md
  .claude/skills/save/SKILL.md
  .claude/skills/release/SKILL.md
  .claude/skills/pull/SKILL.md
  .claude/skills/end/SKILL.md
  .claude/skills/spinoff/SKILL.md
  .claude/skills/migrate/SKILL.md
  .claude/skills/man/SKILL.md
  .claude/skills/manual/SKILL.md
- links:
  `docs/use/look-up-a-command.md`: the same, printed in the session by `/man`, which also answers a need said in free words.
  `docs/extend/add-a-command.md`: adding a command of one's own, and how a command that writes waits for the principal's word.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no procedure of any command; no explanation; no column that no owner states, a guard field among them.
- made: mirrored
- state: regenerate

### docs/reference/artefacts.md
- title: Artefacts
- line: The artefacts of today's chain, one row per definition, with template, inputs, prefixes and command.
- kind: reference
- reader: user, extender, evaluator
- says: A roster page: one overview table first, then one row per definition in `.claude/skills/forge/states/` in the order of the file numbers (brief, intent, assignment, BRD, user stories, solution design): the artefact's file, its `description`, its template, its inputs (Target and Inputs blocks, the BRD's roster of areas as the definition names it, a library document of the instance cited by path; the stories' parent the BRD or, for a small change on the principal's word, the intent), the prefixes of its items, and the command that works it. One line below: a layer a project does not have is not missing.
- inputs:
  .claude/skills/forge/states/brief.md
  .claude/skills/forge/states/intent.md
  .claude/skills/forge/states/assignment.md
  .claude/skills/forge/states/brd.md
  .claude/skills/forge/states/user-stories.md
  .claude/skills/forge/states/solution-design.md
  CLAUDE.md#ID scheme
  CLAUDE.md#Ledger
- links:
  `docs/about/the-document-chain.md`: why the listing of that directory is the one list.
  `docs/about/the-brd.md`: what the BRD holds and why.
  `docs/about/the-user-stories.md`: what the stories hold and why.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no Aim, Partner, Map or Course text; no explanation; no library path or company of an instance; no thread number from a definition's Inputs.
- made: mirrored
- state: regenerate

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
- state: regenerate

### docs/reference/challenger-personas.md
- title: Challenger personas
- line: The challenger personas of today and what each hunts.
- kind: reference
- reader: user, extender
- says: A roster page: one overview table first (name, what it is for, when it fits, where it lives), then one entry per `.claude/agents/challenger-*.md` (`architect`, `business-analyst`, `cto`): the persona name, its `description`, and its Lens section, as `/man challenge` prints them.
- inputs:
  .claude/agents/challenger-cto.md
  .claude/agents/challenger-architect.md
  .claude/agents/challenger-business-analyst.md
- links:
  `docs/use/challenge-the-thinking.md`: running a persona.
  `docs/extend/add-a-challenger-persona.md`: adding a persona.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no contract text; no explanation.
- made: mirrored
- state: regenerate

### docs/reference/checks.md
- title: Checks
- line: The checks of today, what each verifies, its cost, and which a save and a release run.
- kind: reference
- reader: user, extender
- says: A roster page: one overview table first (name, what it is for, when it fits, where it lives), then one entry per `.claude/agents/check-*.md` (`brd`, `engine`, `history`, `light`, `project`, `single-source-of-truth`, `user-stories`): the check name, its `description`, and its Lens section (what it reads, what it verifies with the owner of each rule, its cost), as `/man check` prints them; one line on which a save and a release run, from the two skills.
- inputs:
  .claude/agents/check-light.md
  .claude/agents/check-project.md
  .claude/agents/check-engine.md
  .claude/agents/check-history.md
  .claude/agents/check-single-source-of-truth.md
  .claude/agents/check-brd.md
  .claude/agents/check-user-stories.md
  .claude/skills/save/SKILL.md
  .claude/skills/release/SKILL.md
- links:
  `docs/use/check-conformance.md`: running a check.
  `docs/extend/add-a-check.md`: adding a check.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no contract text; no explanation; nothing of the save and release skills beyond which checks each runs; no position or thread ID from a Lens.
- made: mirrored
- state: regenerate

### docs/reference/recipe-genres.md
- title: Recipe genres
- line: The genres of `/recipe` with their skeletons, outputs and checklists in full.
- kind: reference
- reader: user, extender
- says: A roster page: one overview table first (name, what it is for, when it fits, where it lives), then one entry per `.claude/skills/recipe/genres/*.md` (`presentation`, `readme`, `release-notes`, `screenplay`, `user-stories-export`): the genre, its `description`, its skeleton and output, and its elicitation checklist in full, as `/man recipe` prints them; the shared closing once.
- inputs:
  .claude/skills/recipe/genres/presentation.md
  .claude/skills/recipe/genres/readme.md
  .claude/skills/recipe/genres/release-notes.md
  .claude/skills/recipe/genres/screenplay.md
  .claude/skills/recipe/genres/user-stories-export.md
  .claude/skills/recipe/SKILL.md
- links:
  `docs/use/compose-a-recipe.md`: composing through a genre.
  `docs/use/make-a-video-from-a-recipe.md`: the screenplay genre from recipe to played file.
  `docs/use/write-user-stories.md`: the stories the export genre renders.
  `docs/extend/add-a-recipe-genre.md`: adding a genre.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no skeleton reproduced; no explanation; not the parenthesis of the release-notes genre that the forge's own recipe reads the intent alone; no product name of a wiki or a tracker; no source file of the forge project named.
- made: mirrored
- state: regenerate

### docs/reference/id-scheme.md
- title: ID scheme
- line: The format, the numbering rules and the prefix table, exactly.
- kind: reference
- reader: user, extender, evaluator
- says: The format `PREFIX.NNNN` with prefixes of two or three letters, the fifth digit beyond 9999 and the numeric sort, the rule that IDs are global and stable with its one exception (two items with one number, the younger renumbered with a record), the numbering rules, and the prefix table with meaning and where each lives (threads in `threads/`, one file per thread; BR, UC, DEP and NFR in the BRD; US in the user stories), as the ID scheme of `CLAUDE.md` has them.
- inputs:
  CLAUDE.md#ID scheme
- links:
  `docs/about/stable-ids.md`: why IDs are never renumbered, and how the one exception is settled.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no explanation; no example from a project; no position ID from the text (the bracketed IDs are left out).
- made: mirrored
- state: regenerate

### docs/reference/versioning-and-front-matter.md
- title: Versioning and front-matter
- line: The version scheme and the header fields of an artefact, a brief, a recipe, a work specification and an index, exactly.
- kind: reference
- reader: user, extender, evaluator
- says: The version scheme; the rule that a header carries nothing that changes with a round, the date and the last change computed from the history; the header fields of an artefact (`version`, `status`, `project`, `audience`; a BRD and the user stories add `parent:`), of a brief (`project`, `title`, `author`, `version`, `status`), of a recipe (`version` and no status, an integer only on the principal's word, optional `output:` and `languages:`), of a work specification (`file:`), of a resource index (`directory`); the status rule; the companion and archive file names, as `CLAUDE.md` and the templates have them.
- inputs:
  CLAUDE.md#Versioning & status
  templates/intent.md
  templates/brief.md
  templates/brd.md
  templates/user-stories.md
  templates/recipe.md
  templates/work.md
  templates/index.md
- links:
  `docs/reference/history-companion.md`: the record's shape.
  `docs/about/versioning-and-history.md`: why.
  `docs/reference/research-bundle.md`: the front-matter of a research note and plan, which carry no version.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no explanation; no example values from a project; no author value.
- made: mirrored
- state: regenerate

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
- title: Requirement style and Story style
- line: The rule set of the items of an assignment, the stricter one of a BRD, and the Story style of the user stories, exactly.
- kind: reference
- reader: user, extender
- says: The rule set as the Requirement style of the assignment's definition has it, the obligation in the indicative with shall and shall not in English and the language's own verb elsewhere among it; then the rules the BRD's definition makes stricter for its items, as that Requirement style has them; then the Story style of the user stories' definition, rule by rule, as it has them.
- inputs:
  .claude/skills/forge/states/assignment.md#Requirement style
  .claude/skills/forge/states/brd.md#Requirement style
  .claude/skills/forge/states/user-stories.md#Story style
- links:
  `docs/about/the-assignment.md`: why the items of an assignment are written so.
  `docs/about/the-brd.md`: why the items of a BRD are written so.
  `docs/about/the-user-stories.md`: why a story is shaped so.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no example item beyond the generic use-case step the BRD's style quotes and the generic criterion the Story style quotes; no explanation; no position ID from the text.
- made: mirrored
- state: regenerate

### docs/reference/document-kinds.md
- title: Document kinds
- line: The table of document kinds, verbatim, with the companion, library and wrapping rules and the files that have no kind.
- kind: reference
- reader: user, extender, evaluator
- says: The table of document kinds of `CLAUDE.md`, verbatim, six columns and every row, the ledger, the project file, the thread, the map, the work kind and the research with its bundle among them; one line each on the companion of every versioned kind, on a library's reduced set, on the three files that have no kind and are read as no document (a file of `tmp/`, the player page of `docs/videos/`, the principal's own file in `renders/` or `published/`), and on the wrapping rule.
- inputs:
  CLAUDE.md#Document kinds
- links:
  `docs/about/documents-and-records.md`: why the kinds exist.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no explanation; no position ID from the table's cells or the text (the bracketed IDs are left out).
- made: mirrored
- state: keep

### docs/reference/ledger.md
- title: Ledger
- line: The ledger's header, tables, columns, state words and reports, exactly, with where each column is read from.
- kind: reference
- reader: user, extender
- says: The ledger as `templates/ledger.md` owns it: the header (the slug and the day it was made, the kind and the language echoed from the project file); every table with its columns (Briefs, Documents, Renders, Published, Work, Sources, Dependencies, Research, Findings, Challenges) and, for each, which header, record, field or report its columns are read from, a research bundle read by its head; the state words of briefs, published files, work products, findings and challenges; the row of the documentation index in Renders; the rule of Waiting on principal; the Reports section with its three reports and the `unparsed:` header line; which tables a library keeps; `ledger.archive.md` read for items without a newer record. That it is made by `python scripts/forge-ledger.py <slug>`, or by the path of a project's directory, and never kept in git.
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
- state: regenerate

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
- state: regenerate

### docs/reference/research-bundle.md
- title: Research note and bundle
- line: The places, the front-matter and the sections of a research note, of a research bundle and of its plan, exactly.
- kind: reference
- reader: user, extender
- says: Where a research lands, as the research skill's Target has it: a bundle `research/YYYY-MM-DD-<topic>/` with `00-plan.md` at its head and one note per card per engine, `<card>.<engine>.md`, one entry in `research/00-INDEX.md` for the bundle; a research of one card on one engine a single note `research/YYYY-MM-DD-<topic>.md`; immutable from the filing of the synthesis; English. The plan's front-matter (`date`, `project`, `topic`, `status` draft then immutable, `engines`, `derived_from`) and its sections in order (Summary; Plan with Purpose, Perspectives, Assumptions, Left out, Cards, Agents, the second engine's review; Deviations from the plan; Synthesis with Completeness card by card, Answers side by side, Unexpected gathered, Not found gathered, Claude's view; Notes), and the six fields of a card. The note's front-matter (`date`, `project`, `topic`, `status`, `engine`, `model`, `usage`, `run`, `derived_from`) and its sections in order (In short, Question, Key findings with their epistemic status words, Unexpected, Not found, Options, Relevance to this project, Sources with the fields of a source, Opened and not used, Search record). The research entry of the resource index. The working files of a run under `tmp/research/<run>/`, which are no source of truth.
- inputs:
  .claude/skills/research/SKILL.md#Target
  templates/research-plan.md
  templates/research.md
  templates/index.md
- links:
  `docs/use/research-a-topic.md`: the command that makes them.
  `docs/about/the-research.md`: why a plan comes first and what the sections are for.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no explanation; no note, bundle or topic of a project; no skeleton reproduced whole; no position ID from the comments; no vendor or model family beyond the engine words the skeletons show.
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
- state: regenerate

### docs/reference/verdict-words.md
- title: Verdict words
- line: The words and letters the principal types in a walkthrough or at a step that needs his word, exactly.
- kind: reference
- reader: user
- says: The words and what each does, as the walkthrough skill owns them: the verdict line `(a)ccept / (m)odify / (q)uestion / (r)eject / (p)ark` and the single letters `a`, `m`, `q`, `r`, `p` as a whole message; that every step needing the principal's consent and every question of Claude's that asks him to decide closes with the same line, with Claude's recommendation as what `accept` means, a yes that carries a question being `question`, and only a question for information Claude lacks closing without it; `obsolete`; `write`; `??`; a closing word such as "done" for a thought sent in pieces; that no other word of the forge has a letter and every command is typed in full.
- inputs:
  .claude/skills/walkthrough/SKILL.md
  CLAUDE.md#Working methods
- links:
  `docs/use/walk-through-a-list.md`: the procedure the words belong to.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no explanation; no reason; nothing of the Working methods beyond `??`, `write`, the verdict line of Step by step and the closing word of In pieces; no date the skill carries.
- made: mirrored
- state: regenerate

### docs/reference/repository-layout.md
- title: Repository layout
- line: The layout of the engine root, a thought project and a library, file by file.
- kind: reference
- reader: user, extender, evaluator
- says: The layout block of `CLAUDE.md`, Repository layout, in full: the engine root with its renders, the two fixed files (the security policy, the code of conduct), the licence, `.gitattributes`, `.mailmap`, the scripts comment (the trial script `forge-check` with its module, `forge-engine` and `forge-cite` among them, and the five shared modules), `tests/` with its fixture, `pytest.ini`, the CI workflow, `tmp/` the working folder and `docs/videos/` as the comments have them; a thought project with its project file, `.gitattributes`, `.gitignore` from its template, `threads/`, `ledger.archive.md`, `renders/state.md`, the published companions, the principal's own files in `renders/` and `published/`, `work/`, the renders per language, and research as single notes or bundles with their plan; a library; each comment kept as a fact.
- inputs:
  CLAUDE.md#Repository layout
- links:
  `docs/about/projects-and-the-engine.md`: why projects are repositories of their own.
  `docs/about/the-security-policy-and-the-code-of-conduct.md`: the two fixed files of the root, explained.
  `docs/about/the-tests.md`: the tests and their fixture, explained.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no explanation; no value of an instance file; no name or e-mail of the mailmap's content; no position ID or thread number from the comments; no brief named from the comments.
- made: mirrored
- state: regenerate

### docs/reference/scripts.md
- title: Scripts
- line: Every script with its synopsis, options, forms, what it needs and the command that runs it.
- kind: reference
- reader: user, extender
- says: A roster page: one overview table first (script, what it is for, the command that runs it, what it needs), then one entry per file in `scripts/` from its module docstring: what it does, its synopsis and options, its forms, what it needs installed, where its output lands; that every script that takes a project takes it by its slug or by the path of its directory; for `forge-save.py` the rebase only where the histories diverged, a branch merely ahead pushed as it stands, the conflict left standing and the refusal of a standing rebase or merge; for `forge-status.py` the registration of the merge driver `ours`, a rebase or merge in progress, a repository-local identity reported as a fact and, with `--remote`, the state against the origin and the `github:` line of what waits on GitHub through `gh`, or the line saying it could not read and why; for `forge-clone.py` the facts it reports and the hint it prints where git resolves no identity; for `forge-config.py` its bare form, `--register` with `--zdiff3`, `--guard` with `--unset-identity`, `--identity` with `--replace`, and git 2.36 or newer; for `forge-check.py` the mechanical clauses of the light check run as a program, `light <slug>` with `--out`, its report in the check contract's shape with a section of what it leaves to reading, run by hand beside the check and by no command; for `forge-ledger.py` the ledger it writes and its `--out` form; for `forge-migrate.py` the dry run, `--apply` and `--undo`, the marks, the refusals and a project outside git; for `forge-report.py` the name it completes; for `forge-engine.py` the engine table with its one row, a new engine being a row and its pair in `COMMANDS`, the packet folder, the per-run profile, the verified read-only folder, the envelope, the flags (`--model`, `--effort`, `--timeout`, `--schema`, `--allow-all`, `--sandbox`, `--no-profile`, `--prompt`) and the exit codes, run by `/research`; for `forge-cite.py` the four states of a URL, `--out`, `--timeout`, `--independence` and the exit codes, run by `/research`; for `md2pptx.py` and `md2docx.py` the two engines; for `md2video.py` the two formats, the pace, `--frame`, the section and the name of a player file, where the file lands and that it renews the player page under `docs/videos/`; for `hook-walkthrough.py` and `hook-git.py` the hook each is and what it answers, the git hook's `--judge` form and that its cases are a test of the suite; for the three documentation scripts their place in the run of `/document`, `docs-state.py`'s `--previous` form and the generator hashed with its whitespace normalised, and `docs-check.py`'s one-file scan; the five shared modules (`forge_repos.py`, `forge_tools.py`, `forge_docs.py`, `docs_map.py`, `forge_check.py`) each in one line. Below, the portability rule in one line, with the tests in CI on Linux and Windows, which scripts are a writing rule, and that nothing has run on macOS.
- inputs:
  scripts/forge-save.py
  scripts/forge-pull.py
  scripts/forge-status.py
  scripts/forge-clone.py
  scripts/forge-branch.py
  scripts/forge-config.py
  scripts/forge-history.py
  scripts/forge-report.py
  scripts/forge-ledger.py
  scripts/forge-migrate.py
  scripts/forge-check.py
  scripts/forge_check.py
  scripts/forge-engine.py
  scripts/forge-cite.py
  scripts/forge_repos.py
  scripts/forge_docs.py
  scripts/doc2md.py
  scripts/md2pptx.py
  scripts/md2docx.py
  scripts/md2video.py
  scripts/forge_tools.py
  scripts/hook-walkthrough.py
  scripts/hook-git.py
  scripts/docs-state.py
  scripts/docs-index.py
  scripts/docs-check.py
  scripts/docs_map.py
  CLAUDE.md#Persistence (git)
  projects/forge/10-intent.md#POS.0830
- links:
  `docs/start/install.md`: installing what the scripts need.
  `docs/use/generate-the-documentation.md`: the run the documentation scripts serve.
  `docs/use/render-an-output.md`: the render that runs the conversions and the one-file scan.
  `docs/use/make-a-video-from-a-recipe.md`: the job `md2video.py` serves.
  `docs/use/read-the-history-of-an-item.md`: the command behind the history script.
  `docs/use/migrate-a-project.md`: the command behind the migration script.
  `docs/use/settle-a-conflict.md`: the step the save script leaves standing.
  `docs/use/research-a-topic.md`: the command behind the engine and the citation scripts.
  `docs/use/run-the-tests.md`: the tests the scripts are changed with.
  `docs/extend/add-a-script.md`: writing a script of one's own.
  `docs/extend/add-an-engine.md`: adding a row to the engine table.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: nothing below a docstring; no example path, slug, name or e-mail of the docstrings (they carry `platform-strategy`, `agentic-platform`, `acme`, `flow-ba`, `fixture`, a `lib-acme` path, a path into the forge project's renders and research, a forge report's name, a branch name, a person's name and an address in the configuration script's example, replaced by `<slug>`, `<path>`, `<branch>`, `<name>` and `<email>`; `forge`, `main`, `my-idea`, `github.com` as a host placeholder and `example.com` may stand); no date, probe, thread number, plan row, design, research or brief name from a docstring; no explanation; no version tag from an example; no vendor, product or model family beyond the row `antigravity`, its tool `agy` and the rows the header names as to be added; no issue, pull request or user the intent cites for the run on Linux; nothing of POS.0830 beyond the platforms; no count of tests or cases.
- made: mirrored
- state: regenerate

### docs/reference/templates.md
- title: Templates
- line: Every skeleton in `templates/`, what it is the skeleton of, and which procedure creates from it.
- kind: reference
- reader: extender
- says: A roster page: one overview table first (name, what it is for, when it fits, where it lives), then one entry per file in `templates/`: what it is the skeleton of, which command or procedure creates from it, and its fields or sections in one line; the `<type>-definition.md` naming rule; the project file's skeleton, what a project without the file is and the fixture flag it may carry; the thread's skeleton; the attributes template a project's `.gitattributes` is copied from, with the three root files anchored by a leading slash; the ignore template a project's `.gitignore` is copied from as it stands (the ledger, the lock files of an open Office document); the BRD's skeleton with its `parent:`; the user stories' skeleton with its `parent:` and the parts of a story; the export recipe's skeleton for the stories; the research note's and the research plan's skeletons; the map's skeleton; the work specification's skeleton; the screenplay recipe's skeleton; the player page's skeleton, from which the script writes the served page; the readme skeleton's "Pinned facts (not rendered)" section; the fields of a resource index entry and of a bundle index; the decision's Verdict line.
- inputs:
  templates/CLAUDE.local.md
  templates/project.md
  templates/gitattributes
  templates/gitignore
  templates/brief.md
  templates/intent.md
  templates/thread.md
  templates/assignment.md
  templates/brd.md
  templates/user-stories.md
  templates/solution-design.md
  templates/work.md
  templates/ledger.md
  templates/decisions.md
  templates/history.md
  templates/index.md
  templates/index-bundle.md
  templates/research.md
  templates/research-plan.md
  templates/recipe.md
  templates/recipe-readme.md
  templates/recipe-release-notes.md
  templates/recipe-presentation.md
  templates/recipe-screenplay.md
  templates/recipe-user-stories-export.md
  templates/html-player.html
  templates/docs-map.md
  templates/artefact-definition.md
  templates/critic-definition.md
  templates/challenger-definition.md
  templates/check-definition.md
  .claude/skills/new-project/SKILL.md
  CLAUDE.md#Templates
- links:
  `docs/extend/what-it-is-made-of.md`: where the templates sit in the whole.
  `docs/reference/documentation-map.md`: the map's fields in full.
  `docs/reference/research-bundle.md`: the research note and plan in full.
  `docs/about/the-work-product.md`: the kind the work skeleton serves.
  `docs/about/the-user-stories.md`: the kind the stories' skeleton and the export skeleton serve.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no skeleton reproduced whole; no explanation; not the readme skeleton's fixed closing sentence; nothing of the player page's styles or code beyond its head comment; no position, design or decision ID from the comments; no standard named in the BRD skeleton's comments beyond the public one it names; no pull request the attributes template cites.
- made: mirrored
- state: regenerate

### docs/reference/configuration.md
- title: Configuration
- line: The files that configure an instance and a project, and what each holds, field by field.
- kind: reference
- reader: user, extender
- says: `.claude/settings.json` (shared: `attribution` with an empty commit trailer and `sessionUrl` false; the deny rules for the two sensitive paths and for git in the other shell tool; the `UserPromptSubmit` hook running `scripts/hook-walkthrough.py` and the `PreToolUse` hook on the Bash tool running `scripts/hook-git.py`, both through `python`); `.claude/settings.local.json` (gitignored, the session model, created by `/setup`); `CLAUDE.local.md` (gitignored: the principal by role, the conversation language and the author handle); the `.gitignore` of the engine (the instance files, `projects/*` with `projects/forge` re-included, the forge project's ledger, the byte-code caches); the `.gitignore` of a project, copied from its template (the ledger, the lock files of an open Office document); the `.gitattributes` of the engine and the template a project's own is copied from (which files are taken as `ours` at a merge, the root files anchored with a leading slash, and which are binary); a project's file `project.md` (slug, kind, language, the fixture flag of a test fixture); `pytest.ini`, how the tests run (the test path, the scripts on the import path); the configuration outside the engine as `/setup` writes it through `scripts/forge-config.py`: the identity per host as two stanzas and an identity file beside the global file, the guard, and the registration of the merge driver `ours` with the git settings it needs, each key named.
- inputs:
  .claude/settings.json
  .gitignore
  .gitattributes
  templates/gitattributes
  templates/gitignore
  templates/project.md
  templates/CLAUDE.local.md
  pytest.ini
  .claude/skills/setup/SKILL.md
  scripts/forge-config.py
  CLAUDE.md#What this workspace is
- links:
  `docs/start/setup.md`: the command that fills the instance files.
  `docs/about/how-the-rules-are-held.md`: why the deny rules and the hooks exist.
  `docs/about/persistence-in-git.md`: what the merge driver `ours` and the git hook are for.
  `docs/about/working-together.md`: what the attributes do at a merge.
  `docs/about/the-tests.md`: what the test configuration serves.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no value of an instance; no host, name or e-mail but placeholders; no path of a machine's global git configuration file; no explanation beyond one clause per item; nothing of the `.gitignore`'s entry for a local launcher; no mention of PowerShell beyond the deny rule's shell name; no position, design or decision ID from the comments; no merge driver of the forge's own for record files, which the forge does not have; no pull request the attributes cite; nothing of the mailmap, which carries values.
- made: mirrored
- state: regenerate

### docs/reference/glossary.md
- title: Glossary
- line: Every term of the forge in one line, with the file that defines it.
- kind: reference
- reader: user, extender, evaluator
- says: The terms in one line each, with the file that defines each: principal, recipients, Claude as cognitive extension, Claude Code, session, harness, document, artefact, brief, intent, position, fact, thread, thread file, rejected direction, assignment, BRD, business requirement, use case, dependency, non-functional requirement, parent of an item, roster of areas, touched area, provenance map, user story, acceptance criterion, edge case, Reference of a story, Story style, the cut, the export of the stories, solution design, layer, definition, template, Map, elicitation, walkthrough, verdict, round, write, history companion, record, record of state, archive, ledger, made at read time, Waiting on principal, Reports, decision, Verdict line, source, bundle, growing bundle, extract, research, research note, research bundle, plan, card, perspective, disconfirming query, stop rule, quick and deep, synthesis, citation check, independence of engines, engine in its two senses (the forge's engine; another engine of a model family, a row of the engine table), engine and tier against model and version, second engine, packet, run folder, profile, envelope, working folder, resource index, Role, project file, kind, recipe, render, plain file, published file, published companion, the principal's own file, format file, genre, screenplay, player page, public folder, primary render, translation, provenance, stale, state render, work product, specification, critic, lens, challenger, persona, check, finding, challenge, the documentation run's report, contract, Lens section, subagent, isolated subagent, isolation, project, thought project, library, dependency, project outside git, instance, instance fact, session model, save, release, `--auto`, pull, migration, shape of a project, major, tag, branch, way of merging, derived file, merge driver `ours`, step of a conflict, the hook's ask, registration of the merge driver, integrator, contributor, what waits on GitHub, immutable, mined, documentation, documentation map, page, index, mirrored, derived, how-to, explanation, reference, pinned fact, Unowned, guarded command, manual, working method, prime directive, obligation in the indicative, prefix of two or three letters, test, fixture, CI, the security policy, the code of conduct, the fixed files of the root.
- inputs:
  CLAUDE.md
  projects/forge/10-intent.md#POS.0120
  projects/forge/10-intent.md#POS.0220
  projects/forge/10-intent.md#POS.0230
  projects/forge/10-intent.md#POS.0250
  projects/forge/10-intent.md#POS.0300
  projects/forge/10-intent.md#POS.0950
  projects/forge/10-intent.md#POS.1090
  projects/forge/10-intent.md#POS.1100
  projects/forge/10-intent.md#POS.1190
  projects/forge/10-intent.md#POS.1450
  projects/forge/10-intent.md#POS.1520
  projects/forge/10-intent.md#POS.1530
  projects/forge/10-intent.md#POS.1540
  projects/forge/10-intent.md#POS.1550
  projects/forge/10-intent.md#POS.1560
  projects/forge/10-intent.md#POS.1590
  projects/forge/10-intent.md#POS.1600
  projects/forge/10-intent.md#POS.1610
  projects/forge/10-intent.md#POS.1740
  projects/forge/10-intent.md#POS.1770
  projects/forge/10-intent.md#POS.1800
  projects/forge/10-intent.md#POS.1830
  projects/forge/10-intent.md#POS.1860
  projects/forge/10-intent.md#POS.1870
  projects/forge/10-intent.md#POS.1880
  projects/forge/10-intent.md#POS.1890
  projects/forge/10-intent.md#POS.1900
  projects/forge/10-intent.md#POS.1910
  projects/forge/10-intent.md#POS.1920
  projects/forge/10-intent.md#POS.1930
  projects/forge/10-intent.md#POS.1940
  projects/forge/10-intent.md#POS.1960
  projects/forge/10-intent.md#POS.1970
  projects/forge/10-intent.md#POS.1990
  projects/forge/10-intent.md#POS.2010
  projects/forge/10-intent.md#Elicitation
  .claude/skills/forge/states/brief.md
  .claude/skills/forge/states/intent.md
  .claude/skills/forge/states/assignment.md
  .claude/skills/forge/states/brd.md
  .claude/skills/forge/states/user-stories.md
  .claude/skills/forge/states/solution-design.md
  .claude/skills/walkthrough/SKILL.md
  .claude/skills/ingest/SKILL.md
  .claude/skills/research/SKILL.md
  .claude/skills/render/SKILL.md
  .claude/skills/publish/SKILL.md
  .claude/skills/document/SKILL.md
  .claude/skills/release/SKILL.md
  .claude/skills/pull/SKILL.md
  .claude/skills/work/SKILL.md
  .claude/skills/migrate/SKILL.md
  .claude/skills/man/SKILL.md
  .claude/skills/test/SKILL.md
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
  templates/brd.md
  templates/user-stories.md
  templates/research.md
  templates/research-plan.md
  templates/recipe-readme.md#Pinned facts (not rendered)
  scripts/forge-engine.py
  scripts/forge-cite.py
  scripts/forge-status.py
  tmp/README.md
- links:
  `docs/about/what-it-is-and-is-not.md`: the forge in prose.
- must-not: no term invented; no definition longer than a sentence; no name, handle or instance value; no address; no term of a mechanism the forge does not have (landing, `+` token, a merge driver of the forge's own for record files, `/merge`, worktree, ID blocks, a second help command); no vendor, product or model family beyond the row `antigravity`; no library path or company of an instance; no product name of a wiki or a tracker; no count of tests; no pull request, discussion or user the positions cite.
- made: derived
- evidence: each term is defined where a file first defines it: the roles, Claude Code, the document kinds and the files that have none, the chain, the reviewers and what holds for every isolated subagent, the ledger, persistence (the door, the hook's ask, the step of a conflict, the registration of the merge driver `ours`, a project outside git), the commands in CLAUDE.md (whole, since the terms span its sections); the artefacts in their definitions, the thread file in the intent's definition and its template; position, fact, thread, rejection in POS.0120 and POS.0230; the BRD, its four prefixes, the parent, the roster of areas, the touched areas and the provenance map in POS.1800, POS.1830, the BRD's definition and its skeleton; the user story, the acceptance criterion, the edge case, the Reference, the Story style, the cut and the export in POS.1990, POS.2010, the stories' definition and its skeleton; the obligation in the indicative in POS.0250 and the assignment's definition; the prefix of two or three letters in POS.0220; elicitation, Map, definition in the Elicitation group; walkthrough, verdict, round, write in the walkthrough skill; growing bundle in the ingest skill; research note, research bundle, plan, card, perspective, disconfirming query, stop rule, quick and deep, synthesis in the research skill, POS.1860 and the two research skeletons; citation check in POS.1890 and `forge-cite.py`'s header; independence, second engine, packet, run folder, profile, envelope in POS.1870, POS.1880 and `forge-engine.py`'s header, engine and tier against model and version in POS.1880; working folder in POS.1900 and `tmp/README.md`; render, provenance, stale, primary render, translation in the render skill and POS.1550; published companion in the publish skill; the principal's own file in POS.1910 and CLAUDE.md, Document chain (Renders); the work product and its specification in POS.1520 and the work skill; screenplay, format file, player page, public folder in POS.1530 and POS.1540; way of merging and derived file in POS.1560; integrator and contributor in POS.1770; what waits on GitHub in POS.1970 and `forge-status.py`'s header; the states against the origin in the pull skill; `--auto` and the order of a release in POS.1100 and the release skill; the migration and the shape of a project in the migrate skill, the project file skeleton and POS.1740; the project file, kind and the fixture flag in POS.1590 and its skeleton; made at read time, record of state, Waiting on principal, Reports and the archive in POS.1600, POS.1610 and the ledger and history skeletons; the Verdict line in the decisions skeleton; lens, persona, check, finding, challenge, contract, Lens section, isolation in the three contracts; the documentation run's report in the `/document` skill and POS.1450; session, harness, instance, subagent, how-to, explanation, reference, mirrored, derived in the docs contract; the ledger's state words in its template; engine, instance fact in POS.0950; major in POS.0300; guarded command in POS.1090; manual in POS.1190 and the `/man` skill; documentation, map, page, index in POS.1450, the `/document` skill and the two agents; pinned fact in the readme skeleton's section; test, fixture and CI in POS.1930, POS.1940, POS.1960 and the test skill; the security policy, the code of conduct and the fixed files of the root in POS.1920. A term no file defines is left out.
- state: regenerate

## Unowned

- How a merge request's branch is fetched onto the integrator's clone and the merge started there: CLAUDE.md, Persistence says the integrator merges on his own clone with git itself, outside the forge's scripts, and the hook's header that `git merge <branch>` typed by Claude runs on the principal's ask; no file says the command the integrator types to fetch the branch, and the owning project has parked the matter until the first merge request on a project of two people. Needed by `docs/about/working-together.md` and `docs/use/settle-a-conflict.md`, which say the merge is git's by hand and describe the step of a conflict that follows, and no more.
- A reason for the rule that a project records no engine version: POS.0940 and POS.0820 state the rule; no file gives its reason. Needed by `docs/about/upgrades-and-migration.md`, whose entry asks the page to say the reason is not recorded.

Brought to their owners' wording in this map, no longer Unowned: what `/document <slug>` reads for a project other than the engine (the planner's definition, What you read, its paragraph for a project, and REJ.0500 of the forge intent, which closes the thread that held it: the project's briefs, intent and threads, the layers below the intent, its ledger, the indexes of `sources/` and `research/`, its recipes and whatever those documents point to on disk, and nothing a project would set for itself; cited by `docs/use/generate-the-documentation.md` and `docs/about/the-documentation.md`); what the BRD's roster of areas holds and where it lies (the BRD definition's Inputs: a library document of the instance, cited by path, naming the areas of the enterprise a BRD must consider and which of them are mandatory, `Roster: none` where a project has no enterprise around it; POS.1800: the organisation's content lives in the instance's library and the engine carries a generic Map; cited by `docs/about/the-brd.md`, `docs/use/write-a-brd.md`, `docs/use/share-material-through-a-library.md` and `docs/reference/artefacts.md`; which library document an instance uses is that instance's to say and no page of the engine names one).

## Did not fit

- FND.3100 and FND.3160, the two Unowned findings of the last report that the task named: both have owners now and are cited above; neither is carried over as Unowned.
- The owning project's decisions park four findings of the last run against the map itself (an entry's order against its owner, claims no named input carries, input anchors the state script cannot isolate, roster columns no owner states) until this run, without naming the entries. The task did not list them, so their rule is applied to every entry: every claim of a `says` has an input that carries it, a part is named only where its heading, its ID or its bold label stands on disk, and no roster page asks for a column its owners do not state. The commands page loses the column "guarded or not": no command carries the harness field any more (SOL.0110, POS.1090), and whether a command starts on the principal's word is said in one line below the table and explained on `docs/about/how-the-rules-are-held.md`.
- Since the previous map the operating layer gained the user stories (a definition, a template, a check, a genre and its skeleton), the tests with their fixture, `pytest.ini`, the CI workflow and `/test`, the two fixed files of the root (POS.1920), the `.mailmap`, the line on what waits on GitHub (POS.1970), the rebase of a save narrowed to a diverged branch (POS.1690), prefixes of two or three letters (POS.0220), the requirement verb following the language of the artefact (POS.0250, REJ.0540), the guard of a command as conduct and no harness field (POS.1090, SOL.0110), and the decided direction that the forge's own project becomes a repository of its own (POS.1980). Five pages are new for them; the entries that touch them are brought to the owners' wording and keep their paths.
- POS.1980 decides that the forge's own project becomes a repository of its own and orders the cut; CLAUDE.md and the engine's `.gitignore` still say the engine tracks `projects/forge`, and the owning project's decision of 2026-11-08 keeps those sentences until the cut. The operating layer wins on `docs/about/projects-and-the-engine.md`, which describes today's shape and forbids the claim that the project is already a repository of its own; the decided direction stands on `docs/about/where-it-is-going.md` as intended, with its order and the fact that the engine still tracks the project. The `must-not` of every page that reads POS.1980 or POS.1990 forbids the pull request, the user and the clone the positions cite.
- The user stories' genre file cites a source of the forge project as the pattern of the export and names two tracker products; the pages that read it name neither, the export's shape being the skeleton's and the genre's own words. The `must-not` of those entries says so.
- The sum `/test` prints is given in the test skill with a real count; the pages take the shape of the line with placeholder numbers and forbid the count, since a count is a fact of one day. The same for the counts of tests, cases and lines of Python that POS.1930, SOL.0900 and the thread of the repository's reading carry.
- The hook `hook-git.py` no longer has a `--test` flag: its header says its cases are a test of the suite and its usage shows `--judge` alone; `docs/reference/scripts.md` says so, where the previous map named `--test`.
- The `.mailmap` carries a name and an e-mail. No entry names it as an input; `docs/extend/what-it-is-made-of.md` and `docs/reference/repository-layout.md` list it as the layout block does, "the author's names in the history mapped to one handle, git's own mechanism", and forbid its content; `docs/reference/configuration.md` leaves it out as a file of values.
- POS.1920 names GitHub's private vulnerability reporting as the way a problem is reported and "the profile CONTRIBUTING names" as the fallback; the contributing recipe carries that profile as an address. `docs/about/the-security-policy-and-the-code-of-conduct.md` names the mechanism as the position does and forbids the address; `SECURITY.md` and `CODE_OF_CONDUCT.md` themselves are the principal's own text and the covenant's, not among what the planner reads, and no entry names them as an input.
- `docs/use/run-the-tests.md` is a job of `use/` for the extender first: a user of the engine never runs the tests (POS.1930), and the command has a page because it is a command of the table. `docs/about/the-tests.md` carries the explanation and is on the extender's path in place of the templates page, which stays reachable from the pages that cite it.
- The release-notes recipe of the forge reads the design's history beside the intent's, where the genre file says the forge reads the intent alone; the pages leave the parenthesis out, as before.
- `docs/reference/requirement-style.md` takes the Story style as a third part under a widened title, since the style of a story is the rule set of its parts and a page of its own would be one list; its entry keeps the path.
- Eleven entries of the map before the previous one carried two inputs on one line; every input stands on a line of its own since the previous map and here.
- THR.0590 is closed (REJ.0500 carries what a project's planner reads); THR.0830, open, asks for a record of what was sent out of a project and is nothing a page says; THR.0790, open, holds the reading of the repository from GitHub and the matters still open there (the README made more human, the threads as issues, the two GitHub templates, the homepage field), none of which a page describes as built.
- FND.3070: the example of a state map on `see-where-a-project-stands` is asked to show a thread's line in words with no ID at all, not a placeholder ID, since the contract bars every chain ID on a page; the entry's `must-not` says so.
- FND.3060: the pinned facts' install lines of Claude Code carry the tool's own addresses; the install page's `must-not` allows them beside the engine's public home and the course page.
- FND.3050: the technical sentence of `what-it-is` rests on CLAUDE.md, What this workspace is, which names Claude Code as Anthropic's agent for the command line and the slash commands, skills, agents and hooks as the forge's mechanisms; the gloss has an owner.
- Of the "reason not recorded" findings of the last report, the owners record several: why reviewers run on the principal's word alone (POS.0400), why a source and a research note are immutable (POS.1040), why a recipe stays 0.x (POS.0710), why a page is never mended by hand (POS.1450), that nothing has run on macOS (POS.0830), why engines and tiers are named and never versions (POS.1880), why the verb of a requirement is an obligation in the indicative (POS.0250); the entries that read them ask for the reason. The rest stay unrecorded, parked by the owning project for a round of their own, and their entries ask the page to say so; no page is asked for a reason no owner records.
- CLAUDE.md, Persistence (git) stands as a heading of its own on disk, so `CLAUDE.md#Persistence (git)` is hashed as that section, to the heading `## Versioning & status`; the part takes the Portability and the Two doors paragraphs with it, which the entries that name it rely on.
- The scripts' module `docs_map.py` does not skip fenced code blocks when it cuts a part by its heading. `.claude/skills/critic-contract/SKILL.md#Output`, `.claude/skills/challenger-contract/SKILL.md#Output` and `.claude/skills/check-contract/SKILL.md#Output` therefore end at the first heading of the report template inside the fence, which is what the three use pages need, since they must not carry the report shape. The entries keep the parts.
- `projects/forge/recipes/release-notes.md#Template` would be cut at once by the level-one heading the Template carries, so the part would be empty for the hash and for the writer; `docs/use/upgrade-the-engine.md` cites the recipe's Instructions, which give the order of the groups with Action required first.
- The BRD's definition cites a thread in its Inputs block for the way a BRD from someone else's file enters the chain; the entries that read the block forbid the thread number. The user stories' definition and the stories' template name no thread.
- POS.1800 names a colleague's fork, the company's content and the group's standard; the definition names the roster and the standard as library documents of the instance, cited by path. Every entry that reads them forbids the company, the fork, the group's standard and any library path of an instance; the public standards POS.1800 names may stand on `docs/about/the-brd.md`.
- "Engine" has two senses on disk: the forge's engine (CLAUDE.md throughout) and another engine of a model family, a row of the table of `scripts/forge-engine.py`; `md2pptx.py` and `md2docx.py` use "engine" a third way, for pandoc and claude. The glossary gives the senses apart; `docs/about/another-model-family.md`, `docs/use/research-a-topic.md` and `docs/extend/add-an-engine.md` say "a second engine" or "another engine" at their first use.
- POS.0800 and POS.1880 name vendors and model families for the engines and the planned reviewers; the engine script's header names the profile's settings path, which carries a vendor's directory name. The pages name the row `antigravity` and its tool `agy` as the operating layer has them and forbid every other vendor, product, family and the profile's path.
- The headers of `scripts/forge-engine.py` and `scripts/forge-cite.py` carry dates, probes, counts of rewritten notes and paths into the forge project's research; the positions POS.1870 to POS.1890 cite a research and a brief of the forge project. The pages keep the mechanisms and forbid the rest.
- POS.0830 cites a user's issue and pull request as the evidence of the first runs on Linux, and POS.1690, POS.1970 and the save script's comments cite a pull request, a discussion and a contributor; the entries that read them take the facts as the operating layer says them and forbid the issue, the pull request, the discussion and the user.
- `use/` never names a subagent or a model; `docs/use/research-a-topic.md` and `docs/use/generate-the-documentation.md` say that Claude states the models and the number of runs before it dispatches, because the skills' steps and CLAUDE.md, Step by step say so; no agent type and no model name reaches the page. `docs/start/setup.md` names the session model the setup skill writes, since the setup is the one place the person meets it.
- The pinned facts list the videos of the course and short clips, with the page each video pairs with; the player page groups the videos by the section each file names. The pages say the videos are grouped by section and name neither the sections nor the order of the forge's own course.
- The setup skill, CLAUDE.md, Persistence and SOL.0150 speak of "the merge driver `ours`" in the singular; the entries say "the merge driver `ours` and the git settings it needs". The forge has no driver of its own for record files (REJ.0340), and the `must-not` fields that forbid it say "for record files".
- POS.1110 writes the branch command as `forge-branch <name>`; the script takes `<slug> [branch]`. The operating layer wins.
- CLAUDE.md, Repository layout names `forge-check` as "the trial of THR.0530"; no command runs the script, whose header gives it the form `light <slug>`. `docs/reference/scripts.md` lists it and its module as the docstrings describe them and says no command runs it; `docs/reference/repository-layout.md` keeps the comment without the thread number; `docs/about/the-check.md` does not present the program as a check.
- The walkthrough skill ends its paragraph on steps outside a walkthrough with a date in brackets; `docs/use/walk-through-a-list.md` and `docs/reference/verdict-words.md` forbid it.
- The solution design's head (How the parts work together) lists the positions no part answers; `docs/about/how-a-thought-travels.md` and `docs/extend/what-it-is-made-of.md` read the head and keep that list off the page. The design is a proposal not judged whole by the principal; the pages take its items as the owner of what is built and forbid the plan rows, the dates and the names of releases its items cite.
- Titled items of the intent carry the ID and a title in bold; `scripts/docs_map.py` matches the ID followed by `**` or a space, so the map cites titled items by ID. The bold labels of a definition (`**Inputs.**`, `**Requirement style.**`, `**Story style.**`, `**Target.**`, `**Course.**`) are cited by their label.
- The contract allows no address but the target's public home; the start pages carry the course page of the teaching videos and the install lines of Claude Code, which the pinned facts name. Kept on the start pages from the pinned facts and forbidden on every other page.
- `docs/start/what-it-is.md` is an explanation in a section the outline marks how-to; kept in `start/` with `kind: explanation`.
- The skeleton's heading `# Documentation map — <target>` carries a long dash; this map's heading carries a spaced hyphen.
- `docs/use/settle-a-conflict.md` names the hook because the finishing commands are put to the principal by it; no hook text reaches the page.
- CLAUDE.md, Isolated reviewers speaks of three contracts and opens with what holds for every isolated subagent, a renderer, a documentation agent and a research agent among them; the documentation agents share a fourth contract and are not reviewers. `docs/about/isolated-reviewers.md` says the shared rule in one sentence and keeps the documentation and research agents out of the reviewers.
- The owning project's recipes carry facts no page may carry: the readme recipe's author line with a name and an e-mail, the contributing recipe's channels as addresses and the author's profile; the pages that read either name the section they read and keep those off the page. The pitch recipes and the BA introduction own nothing a page needs.
- The scripts' docstrings carry example slugs, paths, a branch name, a person's name and an e-mail address, and the migration script's header names a brief of the forge project and "the first release"; the save, status, hook and configuration headers name plan rows, threads, pull requests and dates. The pages replace them by placeholders and say "a release that changes the shape of files".
- The intent's positions on merging (POS.1560, POS.1690, POS.1750, POS.1770, POS.1790) cite a real project's merges, the fixture, challenges, decisions, plan rows, tests and a hosting default; `docs/about/working-together.md` takes the rules and reasons and forbids the rest in `must-not`.
- The forge intent names its first principal by handle in POS.0005, POS.0990 names the licence holder; the briefs carry an `author` field, one of them a handle that is not the principal's; every page that reads the intent has "no name, no handle" in its `must-not` or reads no such item.
- POS.1910 cites the project and the decision at whose save the principal's own files came up; `docs/about/renders-and-recipes.md` forbids naming them.
- The `/man` skill reads the documentation's index `docs/README.md`, a derived file the planner does not read and no entry names as an input; `docs/use/look-up-a-command.md` and `docs/about/the-documentation.md` say that the manual reads the index, from the skill.
- `00-brief.md` says no brief exists for the forge; the other briefs were read for orientation, the briefs `tests` and `user-stories` among them, and the reasons of the `about/` pages come from the intent and the design, so no brief is an input. The threads, `decisions.md` and the research index were read for orientation and are the input of no page; the pull skill reads `RELEASE-NOTES.md`, a render, which the map never names as an input.
- `tmp/` holds working files of other projects and of earlier runs; none was read beyond `tmp/README.md`, which is the folder's own description, and the previous map, which the task named.
- The renders, the README, `CONTRIBUTING.md`, `RELEASE-NOTES.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `docs/`, `docs/videos/`, `tests/` and `LICENSE` of the target were not read, as the definition says or as they are outputs or the principal's own text; `CLAUDE.local.md` and `.claude/settings.local.json` were not read.

