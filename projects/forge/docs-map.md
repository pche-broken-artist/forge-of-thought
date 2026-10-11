---
generated: 2026-10-11
target: engine
owner: projects/forge
previous: tmp/docs-map.previous.md
---

# Documentation map - the engine

Paths under `inputs` are relative to the engine root. The seventh run, the third on the generator as the documentation audit redrew it, after the owners were brought current (solution design 0.13: the generator hashed with the inputs, every page reached from another page, the how-to naming its example heading, an enumeration with glosses as a list). Every entry carries a `line` for the index, the `## Paths` section stands first, inputs are named by part wherever only the part matters (`CLAUDE.md#<section>`, `10-intent.md#POS.NNNN`, a block of a definition by its bold label, a group of the intent or of the solution design by its heading where the page needs the group), and `CLAUDE.md` is an input only where no other file owns the matter. Every page keeps its path from the previous map and is `keep`; none is `new` and none is `remove`; `regenerate` is the script's. For every entry at least one other entry names it under `links`: the twelve pages the previous run reached from the index alone are now named where a reader would ask for them. Titles of `about/` name the concept. Every concept page and every how-to asks for one worked example; the three diagrams stand on `docs/about/the-document-chain.md`, `docs/about/projects-and-the-engine.md` and `docs/about/the-documentation.md`. No page names a person, a company, a host, an account or an e-mail; the one address a page carries is the engine's public home, on `docs/start/install.md` alone.

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
- says: One paragraph in plain words: Forge of Thought is a workshop in which a thought is tempered into a chain of versioned documents under review by agents that never saw the conversation; it runs in Claude Code, Anthropic's AI assistant for the command line, and the person who uses it is the principal, whose thinking is forged and who decides everything, while Claude proposes and keeps order. One person starts from a rough brief, works it into an intent by interview, takes the layers the project needs, has the thinking attacked by blind reviewers and gets outputs for every audience generated from the documents. One closing sentence says what it technically is: a git repository of slash commands, isolated agents, templates, scripts and conventions, bound to no domain.
- inputs:
  CLAUDE.md#What this workspace is
  CLAUDE.md#Roles
  projects/forge/10-intent.md#Essence
  projects/forge/10-intent.md#POS.0780
  projects/forge/10-intent.md#POS.0600
- links:
  `docs/start/install.md`: what must be on the machine and how it gets there.
  `docs/about/what-it-is-and-is-not.md`: the longer explanation of what the forge is, is not, and why.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no commands, no file names, no conventions, no history of the project, no name of a person, no instance fact, no version number.
- made: derived
- evidence: CLAUDE.md, What this workspace is, gives the identity sentence and where the chain ends; Roles gives the two roles; the Essence gives "runs in Claude Code", the reviewers and the domain; POS.0780 gives that a run ends where its owner is satisfied; POS.0600 the name. The technical sentence is composed from the Essence's last paragraph. That Claude Code is an AI assistant is said in the Essence's words ("the engine runs in Claude Code", "Claude acts as the principal's cognitive extension") and nothing more is claimed of it.
- state: keep

### docs/start/install.md
- title: Install what the forge needs
- line: What must be on your machine, and in what order, before the forge runs?
- kind: how-to
- reader: user
- says: Steps in the order a newcomer needs them, each with what you see when it worked: git; Python 3.8 or newer on PATH as a real executable named `python`, because the scripts and the per-prompt hook are Python and the hook is started without a shell, so an alias does not reach it (the package or symlink the pinned facts name for Linux and macOS); Claude Code with a paid subscription, installed by the commands the pinned facts give, signed in on first run; then clone the engine from its public home (the address the pinned facts give; never copy it, the save script refuses an engine that is not a git repository); always start `claude` from the engine root so that `CLAUDE.md` and `CLAUDE.local.md` load. The optional tools last, each resolved from PATH and installed by no script: markitdown through pip for `/ingest`'s conversions, pandoc for the plain Word and PowerPoint files of `/render`, the document-skills plugin for `/publish` unless Claude Code already brings the docx and pptx skills. Closes by pointing at the first setup. One worked example: the sequence as typed on one machine, with placeholders.
- inputs:
  projects/forge/recipes/readme.md#Pinned facts (not rendered)
  CLAUDE.md#Persistence (git)
  .claude/settings.json
  scripts/hook-walkthrough.py
  scripts/forge_repos.py
  scripts/doc2md.py
  scripts/forge_tools.py
- links:
  `docs/start/what-it-is.md`: what you are installing, in one paragraph.
  `docs/start/setup.md`: the first run, `/setup`, which fills the instance facts and sets the model.
  `docs/reference/scripts.md`: every script with what it needs and its options.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no account, no author line, no e-mail, no address other than the engine's public home as the pinned facts give it; nothing of the readme recipe beyond its pinned facts; no platform-specific path; no claim that the scripts have been run on Linux or macOS (CLAUDE.md says portability is a writing rule); nothing on git identity (setup's); no mention of PowerShell.
- made: derived
- evidence: the pinned facts are the one owner of the prerequisites, the real `python` executable with its Linux and macOS remedies, the Claude Code install lines, the subscription, "clone, not copy", "start claude from the engine root", the script prerequisites and the public home; CLAUDE.md, Persistence (Portability) gives Python 3.8 or newer, `python scripts/<name>.py` and the tools resolved from PATH; `.claude/settings.json` starts the hook through `python` in exec form and the hook's docstring says Python on PATH as `python` is all it needs; `forge_repos.py` refuses an engine that is not a clone; `doc2md.py` gives the pip line and installs nothing; `forge_tools.py` is the one owner of what pandoc and the claude engine need. The order is the writer's, by when each piece is first needed.
- state: keep

### docs/start/setup.md
- title: Set up the forge
- line: What does `/setup` ask and write on the first run after cloning?
- kind: how-to
- reader: user
- says: The first run, before any other work: `/setup`. Its three steps and what you see: `CLAUDE.local.md` created from its template by a short interview, the conversation language first and then who the principal is by role, gitignored and never committed; `.claude/settings.local.json` created with the session model set to Fable, the strongest model, on which the whole forge including the blind reviewers runs, or the strongest model the account lists when Fable is not offered, changeable at any time with `/model` or by editing the file; and the git identity, which is git's own: the hosts you push to with a name and an e-mail for each, and the offer to write, on your word, the per-host `includeIf` stanzas and the global guard `user.useConfigOnly = true` into the global git configuration file the status script names, never overwriting, or to print them for you to apply by hand. It never overwrites an existing file and runs no git operation; it ends by pointing at `/new-project` or `/import-project`. One worked example with placeholder values. Prerequisite: the install page.
- inputs:
  .claude/skills/setup/SKILL.md
  templates/CLAUDE.local.md
  scripts/forge-status.py
- links:
  `docs/start/install.md`: what must be on the machine first.
  `docs/start/first-result.md`: from a new project to a saved intent in one sitting.
  `docs/about/persistence-in-git.md`: why the identity is git's and the scripts are the only door.
  `docs/reference/configuration.md`: the instance files and settings, field by field.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no example host, name or e-mail that could be real (use `<host>`, `<name>`); no instance value; nothing of the skill copied as an instruction to Claude; no reason beyond the one sentence CLAUDE.md gives for the guard.
- made: mirrored
- state: keep

### docs/start/first-result.md
- title: Get a first result
- line: How do you go from nothing to a saved intent in one sitting?
- kind: how-to
- reader: user
- says: One sitting, every act outside Claude named as a step of its own: `/new-project my-idea` scaffolds the files; when asked, paste a brief (a five-line sample brief, generic and invented, is given on the page) and say it is finished, so it is approved; `/forge intent` mines the brief into the first intent through an interview, one question per message, written once at the round's end on the word `write`; in your own terminal at the engine root, `git -C projects/my-idea init -b main`, the one-off act Claude is not allowed to run, a remote optional; `/save`, which runs the light check and commits and pushes, and which names its cause when it commits nothing (no repository, or no git identity for the host). One line that "not under git" until then is a fact, not an error. The other door: `/import-project <git-url>` then `/forge <project-slug>`. Prerequisite: setup.
- inputs:
  projects/forge/recipes/readme.md#Instructions
  .claude/skills/new-project/SKILL.md
  .claude/skills/forge/states/brief.md#Course
  .claude/skills/forge/states/intent.md#Course
  .claude/skills/save/SKILL.md
  .claude/skills/import-project/SKILL.md
  CLAUDE.md#Persistence (git)
- links:
  `docs/start/setup.md`: the first run that comes before.
  `docs/use/start-a-project.md`: the full job of starting a project, thought or library.
  `docs/use/bring-in-an-existing-project.md`: the other door, a project you already have, cloned into `projects/`.
  `docs/use/forge-the-intent.md`: the full job of iterating the intent.
  `docs/use/save-your-work.md`: what a save does and asks.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no explanation of what a brief or an intent is beyond one clause each; no slug that could be an instance project (use `my-idea`); no theory of elicitation; no repository address; nothing of the readme recipe but its Quickstart instruction (Section 4).
- made: derived
- evidence: the sequence and the git step are the readme recipe's Quickstart instruction (Section 4: the two paths, the `git -C` line, what a save that commits nothing means); what each step does for the person is read from the skills and the two Courses (new-project step 3 hands the brief to the brief procedure, the brief's Course approves a finished pasted text at once, the intent's Course consolidates the briefs into the first intent, save runs `light` then commits and pushes); "not under git" is CLAUDE.md, Persistence. The sample brief is invented by the writer as a generic shape and names no project.
- state: keep

## use

### docs/use/start-a-project.md
- title: Start a project
- line: How do you scaffold a thought project or a library with `/new-project`?
- kind: how-to
- reader: user
- says: `/new-project <slug>`: a thought project (the chain) or a library (`lib-` prefix, material only), the kind and the language of the chain artefacts declared in the ledger header. What the command creates for each kind, files only, never git; the founding brief asked for at once and handed to the brief procedure; the intent and lower layers born at their first `/forge <state>`; `logo.png` optional. The one-off act that is yours: `git -C projects/<slug> init -b main`, then a remote if wanted; the commit identity is git's. One worked example with `<slug>`.
- inputs:
  .claude/skills/new-project/SKILL.md
  templates/ledger.md
  CLAUDE.md#Persistence (git)
- links:
  `docs/use/write-a-brief.md`: composing the founding brief.
  `docs/use/share-material-through-a-library.md`: what a library is for and how it is used.
  `docs/about/projects-and-the-engine.md`: why a project is a repository of its own that the engine does not know.
  `docs/about/languages.md`: why a project declares one output language and what each kind of document carries.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no instance slug; nothing of the brief procedure (the brief page's); no git beyond the one way in CLAUDE.md names.
- made: mirrored
- state: keep

### docs/use/bring-in-an-existing-project.md
- title: Bring in an existing project
- line: How do you clone a project you already have into `projects/` with `/import-project`?
- kind: how-to
- reader: user
- says: `/import-project <git-url>` clones the repository through the clone script into `projects/<repository name>`, never overwriting, and relays the script's facts: the last commit, the origin, the identity git resolves for the clone (none means the save script will report and commit nothing), and whether a ledger with a `kind:` header is present, its absence a fact. Nothing is written into the project. Work starts by selecting it, `/forge <slug>`, because the engine does not track projects. The script's messages under "If something goes wrong". One worked example with `<git-url>`.
- inputs:
  .claude/skills/import-project/SKILL.md
  scripts/forge-clone.py
- links:
  `docs/use/see-where-a-project-stands.md`: the `/forge` map that follows.
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
- says: Bare `/forge [slug]` reports the state map of a project: its kind and whether it is under git; for the engine and the project the state against the origin as a fact (up to date, behind, ahead, diverged, no origin) with that state's one offer, the map itself running none of it; the artefacts with versions and status, the briefs with their mining state; which target states can be worked from here; stale renders and published files; the libraries it needs; what waits on the principal, the few live matters in words and the rest as a count; a recommended next step and the offer of a walkthrough where more than one matter waits. A library's map stops after its material and the git line. `/ledger [slug]` is the same report read from the ledger only, one project or all; reconciling the ledger with reality is the light check's. One worked example of a map, generic.
- inputs:
  .claude/skills/forge/SKILL.md
  .claude/skills/ledger/SKILL.md
- links:
  `docs/use/pull-from-the-remote.md`: the offer the map makes when a repository is behind.
  `docs/use/walk-through-a-list.md`: how the matters waiting on the principal are worked one by one.
  `docs/reference/ledger.md`: the ledger's tables and state words.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no description of `/forge <state>` (each state has its page); no staleness definition beyond a pointer; no content of a real project in the example.
- made: mirrored
- state: keep

### docs/use/write-a-brief.md
- title: Write a brief
- line: How do you compose or finish a brief with `/forge brief`?
- kind: how-to
- reader: user
- says: `/forge brief [name] [slug]` composes or finishes `00-brief.md`, or `00-brief-<name>.md` for a later whole. The three ways the text arrives and what happens with each: pasted whole (stored verbatim, asked whether finished, approved at once if so); begun outside; born in the forge from a rough idea, Claude active at the opening with inspiration, verification, research and ingest proposed and run on your word. What you can ask for: a structure given to the text without a word changed; `??` for Claude's opinion. Free form, no IDs, approved only on your explicit word, mined by `/forge intent` when you say so. One worked example of the exchange, generic.
- inputs:
  .claude/skills/forge/states/brief.md
  templates/brief.md
- links:
  `docs/about/the-brief.md`: what a brief is and why it is rough on purpose.
  `docs/use/research-a-topic.md`: the research step the brief's finding uses.
  `docs/use/register-a-source.md`: the ingest step the brief's finding uses.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no restatement of the Map's areas (the about page's); nothing of the Partner block as instruction to Claude; no language rule beyond "kept in the language it is written in".
- made: mirrored
- state: keep

### docs/use/forge-the-intent.md
- title: Forge the intent
- line: How do you iterate the intent with `/forge intent`, round by round?
- kind: how-to
- reader: user
- says: `/forge intent [slug]` iterates `10-intent.md`: the briefs mined whole by whole, one at a time, briefs offered before threads; or a round from an open thread, a new word of yours or what the recipients sent back. One theme at a time, the reality check last; answers carried in the conversation and written once per round on `write`, Claude reflecting the round back first; resolved threads move into positions or rejections. The open threads live in `threads.md` beside the intent. The round ends by naming what changed and what stays open, naming the layers that can follow or offering the approval, a recommendation never a gate. `/challenge <persona> intent` is offered as the independent reality check. One worked example of a round, generic.
- inputs:
  .claude/skills/forge/states/intent.md
  templates/intent.md
  templates/threads.md
- links:
  `docs/about/the-intent.md`: what the intent holds and why it is rewritten for coherence.
  `docs/about/working-methods.md`: the named ways the conversation runs, one write per round among them.
  `docs/use/challenge-the-thinking.md`: running the independent reality check.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no ID scheme (reference); no restatement of the Map; no Partner text as instruction to Claude; no position of the forge project.
- made: mirrored
- state: keep

### docs/use/distil-an-assignment.md
- title: Distil an assignment
- line: How do you derive the assignment from the intent with `/forge assignment`?
- kind: how-to
- reader: user
- says: `/forge assignment [slug]` derives `20-assignment.md` from the intent in a joint pass of three phases: questions up front, one per message, only what the intent does not answer; the recast, the whole draft with a provenance map (group, items, the positions they came from, what landed nowhere, what came from nowhere); the walkthrough by group, one verdict per group. A substance change goes to the intent first; a wording fix is made directly. After the pass `/critique essence` is offered as the test of drift, then the approval. Items in the Requirement style, shall and shall not, no priorities. One worked example of a group's walkthrough item, generic.
- inputs:
  .claude/skills/forge/states/assignment.md
  templates/assignment.md
- links:
  `docs/about/the-assignment.md`: what makes an assignment complete and where assigning ends.
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
- says: `/forge solution-design [slug]` iterates `40-solution-design.md`, how the things wanted are realised, from the lowest layer above it. Whether one is worth writing is yours to say; the ways in: no design yet, a layer above that moved, the thing changed below, a wording fix. Every pass makes the coverage map: the in-scope items of the layer above with no part, and the parts that realise no item. What cannot be realised, or only at a price not worth paying, goes back to the intent as a thread. `/challenge <persona> solution-design` is offered once the design stands; the persona `architect` exists for it. One worked example, generic.
- inputs:
  .claude/skills/forge/states/solution-design.md
  templates/solution-design.md
- links:
  `docs/about/the-solution-design.md`: what a solution design holds and why it restates nothing above it.
  `docs/use/challenge-the-thinking.md`: the challenge of the design.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no shape of a SOL item beyond one sentence (the about page's); no theory of the intent/solution boundary; no item of the forge's own design.
- made: mirrored
- state: keep

### docs/use/register-a-source.md
- title: Register a source
- line: How do you store, register and catalogue external input with `/ingest`?
- kind: how-to
- reader: user
- says: `/ingest [file] [slug]`: with a file, that document; with text pasted into the conversation, the text as `sources/<slug>.md`; bare, a sweep for unregistered files and a report of files changed since registration with a question what to do with each (a breach to settle in a thought project, ordinary maintenance in a library). Personal matter stops the command before storing. Every binary gets one question, convert to Markdown? Yes: `scripts/doc2md.py` makes the extract, which is then the source; no: the binary is the source as a functional thing. A related set is a bundle with its own index. After registration Claude always asks what the source is for; the answer is its Role in the resource index. A library document is cited by path and registered as a dependency. Registration is not intake. One worked example, generic.
- inputs:
  .claude/skills/ingest/SKILL.md
  scripts/doc2md.py
  templates/index.md
  templates/index-bundle.md
- links:
  `docs/about/sources-and-research.md`: why sources are immutable and why registration is not intake.
  `docs/use/share-material-through-a-library.md`: citing a library's document from a project.
  `docs/reference/scripts.md`: `doc2md.py`, its formats and what it needs.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no example file with a real name; no ledger column detail; nothing of the skill as an instruction to Claude.
- made: mirrored
- state: keep

### docs/use/research-a-topic.md
- title: Research a topic
- line: How do you get a durable, indexed research note with `/research`?
- kind: how-to
- reader: user
- says: `/research <topic> [slug]` looks up current best practice on one question with web sources, marks consensus, emerging and contested, and writes an immutable dated note into `research/` with the question, findings with sources, options with trade-offs and a recommendation for this project; several questions become several notes. The note is indexed in `research/00-INDEX.md` and registered in the ledger. The summary leads with the recommendation; a change to an artefact is proposed through `/forge <state>`, never made silently. One worked example, generic.
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
- says: `/recipe [genre] [slug]`: bare, the roster of genres with the project's existing recipes; with a genre, a guided composition through its checklist, closing with the language question, the recipe composed from the genre's skeleton; with the name of an existing recipe, an iteration. A recipe outside any genre is composed from the base skeleton. Versioned 0.x for life with its history companion, written once per round on confirmation; `/render <recipe>` offered next. The three genres of today in one line each. One worked example, generic.
- inputs:
  .claude/skills/recipe/SKILL.md
  .claude/skills/recipe/genres/presentation.md
  .claude/skills/recipe/genres/readme.md
  .claude/skills/recipe/genres/release-notes.md
  templates/recipe.md
- links:
  `docs/about/renders-and-recipes.md`: why the recipe is iterated and the render never edited.
  `docs/reference/recipe-genres.md`: each genre's checklist in full.
  `docs/use/render-an-output.md`: generating the render.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no checklist reproduced; no Format section detail beyond its existence; not the parenthesis of the release-notes genre that the forge's own recipe reads the intent alone.
- made: mirrored
- state: keep

### docs/use/render-an-output.md
- title: Render an output
- line: How do you regenerate a render, and its plain file, with `/render`?
- kind: how-to
- reader: user
- says: `/render <recipe> [slug]` regenerates a render from its recipe: the inputs read from disk at their current versions, the Markdown generated in isolation from the recipe and its inputs alone, written to `renders/<recipe>.md` or the recipe's `output:` path, opening with provenance front-matter. Back in the session the file is scanned mechanically for instance facts (`python scripts/docs-check.py --file <render>`): a hit is said aloud and you judge it, an instance fact is regenerated out, never edited by hand; then the file and its provenance are verified and the ledger's Renders table mirrors it. Where the recipe has a `## Format` section the plain `.docx` or `.pptx` is made beside the render through pandoc, said aloud when pandoc is missing; a published file of the same recipe is marked stale. A render is regenerated only on this command or by `/release`. A missing recipe is offered through `/recipe`. One worked example, generic.
- inputs:
  .claude/skills/render/SKILL.md
  scripts/docs-check.py
- links:
  `docs/reference/render-provenance.md`: the front-matter block and the one definition of stale.
  `docs/use/publish-a-designed-file.md`: the designed file, made through a model.
  `docs/about/renders-and-recipes.md`: why a render is generated and never a source of truth.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no subagent prompt text; no provenance block (reference); no script options beyond `--file`; no render of the forge project named.
- made: mirrored
- state: keep

### docs/use/publish-a-designed-file.md
- title: Publish a designed file
- line: How do you make the designed Word or PowerPoint file with `/publish`?
- kind: how-to
- reader: user
- says: `/publish <recipe> [slug]` makes the designed `.pptx` or `.docx` from the render as it lies on disk, through a model and its document skills, into `published/`: started by you only, never by `/render`, `/release` or Claude's own judgement; expensive and minutes long, said in one line before it runs. It never renders: a stale render is named first and the word is yours. A recipe without a `## Format` section ends at the Markdown. The Published table gets a row `current`; every later `/render` of that recipe sets it `stale`. It makes a file and sends nothing anywhere. One worked example, generic.
- inputs:
  .claude/skills/publish/SKILL.md
- links:
  `docs/use/render-an-output.md`: the Markdown and the plain file that come first.
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
- says: `/document [slug]` generates the documentation in one run that asks nothing: bare, the engine's, into `docs/` at the engine root with the map beside the ledger of `projects/forge`; with a slug, that project's, into `projects/<slug>/docs/`. The steps in the person's terms: a planner reads the target on disk and writes the map; a script computes every page's state from the content of its inputs and of the rule the pages are made by (new, regenerate, keep, remove), so that a page is remade when an input changed or the rule changed, and writes one task per page to make; pages that lost their entry are deleted; one writer per page makes it from its entry and inputs alone, a mirrored page on a faster model and a derived page on the session model; a script derives the index `docs/README.md` with the intent's version; a script checks every page, a failing page is regenerated once and one that fails twice is left out and said. What you get: the counts, the Unowned list (facts a page needs and no file owns), what did not fit, what the writers left out, every place a writer wanted a reason and none is recorded, the check's result, and a row for the index in the ledger's Renders table. A wrong page is mended in the file that owns the matter and regenerated. A release never runs it: it reports the index's age and offers the command. One worked example of the closing report, generic.
- inputs:
  .claude/skills/document/SKILL.md
  scripts/docs-state.py
  scripts/docs-index.py
  scripts/docs-check.py
- links:
  `docs/about/the-documentation.md`: what the documentation is, for whom, and why it is generated.
  `docs/extend/change-a-documentation-page.md`: how a page is changed through the file that owns its matter.
  `docs/reference/scripts.md`: the three documentation scripts with their options.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no agent prompt or task text; no model name; no field of the map (reference); no page count or date of a run; nothing of the check script's `--file` mode (the render's).
- made: mirrored
- state: keep

### docs/use/critique-the-documents.md
- title: Critique the documents
- line: How do you run a critic lens on document quality with `/critique`?
- kind: how-to
- reader: user
- says: `/critique [lens] [artefact] [slug]`: bare, the roster of lenses with a recommended fit; with a lens, one isolated agent reads the project's documents and never the conversation, judges document quality through that lens, never substance, and writes a dated immutable report in `reviews/` with FND findings and ledger rows. The optional target narrows the run to one artefact named as `/forge` names it. What you see: the delta summary (new, verified resolved, still open, obsolete) and the offer of a walkthrough; `accept` means an iteration of the artefact through `/forge`. No lens runs at a save; a release offers `essence` once. One worked example, generic.
- inputs:
  .claude/skills/critique/SKILL.md
  .claude/skills/critic-contract/SKILL.md#Output
- links:
  `docs/reference/critic-lenses.md`: the lenses of today and what each goes after.
  `docs/use/walk-through-a-list.md`: settling the findings one by one.
  `docs/about/the-critic.md`: what the critic judges and why it is blind.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no report shape; no severity or category vocabulary beyond naming that they exist; no finding of the forge project.
- made: mirrored
- state: keep

### docs/use/challenge-the-thinking.md
- title: Challenge the thinking
- line: How do you have a persona attack the substance with `/challenge`?
- kind: how-to
- reader: user
- says: `/challenge [persona] [artefact] [slug]`: bare, the roster of personas with a recommended fit; with a persona, one isolated agent attacks the substance, never document quality, and writes a dated immutable report in `challenges/` with three to seven CHL challenges ordered by severity, each falsifiable and with its epistemic status, what is strong and the questions it cannot answer from the documents. Best run before the next layer is first derived from the target. What you see: the overall read, each challenge compressed, Claude's own disagreement marked as its own, the questions answered where the conversation knows them, the offer of a walkthrough; `accept` means the challenge is mended through `/forge` in the artefact it concerns. A rejected challenge is a healthy outcome. One worked example, generic.
- inputs:
  .claude/skills/challenge/SKILL.md
  .claude/skills/challenger-contract/SKILL.md#Output
- links:
  `docs/reference/challenger-personas.md`: the personas of today and what each hunts.
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
- says: `/check [check] [slug]`: bare, the roster of checks, each saying when it fits; with a check, one read-only isolated agent verifies mechanical conformance of a project (by slug; the engine's own project is `forge`, typed `/check light forge`) or of the engine (`/check engine`), never substance or quality, and returns its report. The session files it in `reviews/` only when it has findings, gives each new finding its FND, presents the ranked findings, offers every "immediate fix" at once and a walkthrough of the rest; a rule worth changing goes to the intent. Nothing blocks. Which checks a save and a release run is theirs. One worked example, generic.
- inputs:
  .claude/skills/check/SKILL.md
  .claude/skills/check-contract/SKILL.md#Output
- links:
  `docs/reference/checks.md`: the checks of today and what each verifies.
  `docs/use/walk-through-a-list.md`: settling the findings.
  `docs/use/upgrade-the-engine.md`: the checks as the migration tool after an upgrade.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no report shape; no Lens text; no finding of the forge project.
- made: mirrored
- state: keep

### docs/use/walk-through-a-list.md
- title: Walk through a list
- line: How is a list of findings, challenges or threads worked one item at a time?
- kind: how-to
- reader: user
- says: How any list that needs your decision is worked: one item per message, in order of weight; what an item carries (what it says and its evidence, what would change and for whom, the recommendation with the concrete text for accept); the proposition closing with `(a)ccept / (m)odify / (r)eject / (p)ark`, answered with a single letter or the word; `obsolete` as a fifth verdict; a question keeps the item open. The verdicts are carried and written once at the round's end on `write`, Claude reflecting the whole round back first; what `reject`, `park` and `obsolete` record, and that `accept` writes what the producing command says. The elicitation interview runs the same way. One worked example of one item, generic.
- inputs:
  .claude/skills/walkthrough/SKILL.md
- links:
  `docs/reference/verdict-words.md`: the words and letters, exactly.
  `docs/about/working-methods.md`: why the one-item rule exists and how a hook holds it.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no hook text; nothing addressed to Claude.
- made: mirrored
- state: keep

### docs/use/save-your-work.md
- title: Save your work
- line: What does `/save` check, ask and commit?
- kind: how-to
- reader: user
- says: `/save [slug] [-m "message"] [--tag name]`: the scope from the status script (the engine and every project repository, each with its branch; a project not under git named and left alone); the `light` check on every repository in scope, settled through `/check`, a save never waiting on a finding you have not asked to fix; a one-line commit message drafted from the round's history records and confirmed, or `-m`; a tag only on your word; then the save script, which commits, rebases your commits onto the remote and pushes on whatever branch is checked out, no render, and commits nothing where git resolves no identity, saying so. One message per repository when several have changes. One worked example, generic.
- inputs:
  .claude/skills/save/SKILL.md
  scripts/forge-save.py
  scripts/forge-status.py
- links:
  `docs/use/release-a-version.md`: the other door, from `main`, with the renders.
  `docs/use/end-a-session.md`: the end of a session, which names what is unsaved and offers the save.
  `docs/about/persistence-in-git.md`: why there are two doors and two speeds.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no git command; no example message from the forge project; no tag example with a real version; no slug from the script's examples (use `<slug>`; `forge` may stand).
- made: mirrored
- state: keep

### docs/use/release-a-version.md
- title: Release a version
- line: What does `/release` run, render and tag, in what order?
- kind: how-to
- reader: user
- says: `/release [slug] [-m "message"] [--tag name]` releases one repository from `main` only, refusing elsewhere, in the order of its steps: the checks (`light` and `project` for a project; `engine`, `light` and `project` for the engine) launched at once and settled by walkthrough, a finding may be parked; `critique essence` offered once; the README and the release notes regenerated unconditionally through `/render`, with a summary of what materially changed for you to rule on; the age of the documentation reported (the version in `docs/README.md` against the intent's; a repository without `docs/` has none, and that is no finding) and `/document` offered in one sentence, run before the save only on your word; then `/save` with the message `release <intent version>: <one line>` and, at an integer version, the tag `v<major>` proposed and taken on your word, Claude first naming what the forge's own intent asks a major to pass where the repository is the engine, a reminder never a gate. The check is advisory. One worked example, generic.
- inputs:
  .claude/skills/release/SKILL.md
- links:
  `docs/use/save-your-work.md`: the save the release ends with.
  `docs/use/check-conformance.md`: the checks and how their findings are settled.
  `docs/about/renders-and-recipes.md`: why the README and the release notes are renders.
  `docs/use/generate-the-documentation.md`: the command the release offers for the documentation.
  `docs/about/versioning-and-history.md`: what a major approves and what its test attests.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no version number of the forge; no description of what a major must pass beyond the pointer; no claim that the release regenerates the documentation on its own.
- made: mirrored
- state: keep

### docs/use/pull-from-the-remote.md
- title: Pull from the remote
- line: How does `/pull` look at the remote, and what does it pull and refuse?
- kind: how-to
- reader: user
- says: `/pull [slug]` (bare: the engine and every project with an origin; `forge`: the engine; a slug: that project). First the state of each repository against its origin, said as a fact: up to date, behind, ahead, diverged, no origin, not under git; a repository with unsaved changes or a diverged history stops with its one offer (`/save` first, or a merge by hand or by `/save`, which rebases your commits onto the remote), nothing pulled from it. For what is clean and behind the pull script fast-forwards and reports where each repository moved from and to and the subjects of the commits between. After a pull of the engine the Action required lines of the releases crossed are shown from `RELEASE-NOTES.md` and `/check light <slug>` and `/check project <slug>` are offered on each project, run only on your word. The forge never pulls or merges on its own. The scripts' refusals under "If something goes wrong". One worked example, generic.
- inputs:
  .claude/skills/pull/SKILL.md
  scripts/forge-pull.py
  scripts/forge-status.py
- links:
  `docs/use/upgrade-the-engine.md`: what to do after a pull of the engine, project by project.
  `docs/use/save-your-work.md`: the save that must come first on unsaved work.
  `docs/about/persistence-in-git.md`: why the forge looks at the remote and offers, never pulls on its own.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no git command; no slug from the script's examples (use `<slug>`; `forge` may stand); no version numbers.
- made: mirrored
- state: keep

### docs/use/upgrade-the-engine.md
- title: Upgrade the engine
- line: How do you take a new version of the engine and bring your projects to its conventions?
- kind: how-to
- reader: user
- says: The job after a pull of the engine (`/pull forge`, or bare `/pull`): read the Action required lines `/pull` showed, or `RELEASE-NOTES.md` yourself, Action required first in every section; then, project by project, `/check light <slug>` and `/check project <slug>` measure the project against the current conventions and report what no longer conforms; the findings are walked one at a time and Claude migrates on your word in the session. Projects record no engine version and are untouched by the pull; there is no migration tool; a project left as it is stays valid under the conventions it was written to. One worked example, generic.
- inputs:
  .claude/skills/pull/SKILL.md
  projects/forge/10-intent.md#POS.0940
  projects/forge/10-intent.md#POS.0820
  projects/forge/recipes/release-notes.md#Template
- links:
  `docs/use/pull-from-the-remote.md`: the pull itself, what it refuses and reports.
  `docs/use/check-conformance.md`: running a check and settling its findings.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no version numbers; no history of past migrations; no repository address; nothing of the release-notes recipe beyond its reader and that Action required stands first; no repetition of the pull page's states and refusals beyond one sentence.
- made: derived
- evidence: the pull skill's step 3 gives what follows a pull of the engine (the Action required lines, the two checks offered per project); POS.0940 states that a project records no engine version, the migration path through the two checks, the release notes' Action required lines and Claude migrating on the user's word with no tool; POS.0820 states that an artefact stays valid under the conventions it was written to; the release-notes recipe's Template says Action required stands first in every section and names the reader. The page is the join of these into one job.
- state: keep

### docs/use/end-a-session.md
- title: End a session
- line: How does `/end` tell you what a shutdown would lose?
- kind: how-to
- reader: user
- says: `/end` closes a session so that you know nothing is lost: it says what lives only in this conversation (a round not written, verdicts carried, anything promised and not done) and offers the write; runs the status script without the remote and names every repository with unsaved changes, offering `/save`; names stale renders as a fact from the ledger's Renders table, no offer; and closes with one sentence: nothing lives only in this conversation and shutting the command line loses nothing, or the list of what it would lose. It writes nothing and runs nothing but the status script. One worked example of the closing, generic.
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
- says: `/history <ID> [slug]` (a short form such as `pos580` is accepted; `forge` is the engine's own project) runs the history script and prints what it printed, unshortened: the item as it stands today, its timeline oldest first (archive rows, its own records, the records of other items that mention it, each with version and date) and every other citation in the project; `--full` prints every Was whole. Claude adds at most three sentences of its own, marked as such: what the item says today, how it moved, what hangs on it; nothing is derived from them and nothing written. An ID nothing in the project knows is said so, never guessed. Read-only. One worked example with a placeholder ID and generic lines.
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
- says: Branches are voluntary: `python scripts/forge-branch.py <slug> <branch>` switches the repository to the branch, creating it from the current state when it does not exist, `main` switching back; with the slug alone it reports the branch and lists the branches (`forge` means the engine). Unsaved changes stop a switch: save first. Merging, deleting and pushing branches stay with git; a new branch reaches the remote by the first save made on it; a release is made from `main` only. Whoever does not want branches works on `main` and never meets this. One worked example with `<slug>` and `<branch>`.
- inputs:
  scripts/forge-branch.py
- links:
  `docs/use/save-your-work.md`: the save that carries a branch to the remote.
  `docs/about/persistence-in-git.md`: why merging is left to git.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no git command other than through the script; no branch name or slug from the script's examples other than `forge` and `main`.
- made: mirrored
- state: keep

### docs/use/spin-off-a-group.md
- title: Spin off a group
- line: How does `/spinoff` make a requirement group a project of its own?
- kind: how-to
- reader: user
- says: `/spinoff <project> <group> <slug>` splits a requirement group of an assignment into a project of its own, only on your explicit instruction: the items to move confirmed; the new project created by the `/new-project` procedure, files only; a short brief derived from the source intent, presented as a draft and approved on your word; mined into the new intent through `/forge intent`; the moved items marked superseded in the source assignment and replaced by one link item, recorded as a DEC; both ledgers updated. Claude may propose readiness, never run it. One worked example, generic.
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
- says: `/man [command | method]`, alias `/manual`, is the forge's manual, read at the moment of the call from the files that own it: bare, the commands with their arguments and purposes and the working methods with their first sentences; with a command, its purpose, arguments, the roster it dispatches over with what each entry looks for, and the skill file for the whole procedure; with a method, its paragraph and the skill that holds its shape. It runs nothing and prints in the conversation language. The word `help` is Claude Code's own. One worked example, generic.
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
- says: A library is a project of kind `library`, prefix `lib-`, with no chain: a ledger, `sources/` and `research/` with their indexes, and a readme recipe whose render is a catalogue. Born by `/new-project lib-<name>`; documents enter by `/ingest`; a changed document is the owner's maintenance, not a breach. A project uses a library document by citing its path: `/ingest` adds an index entry and a Dependencies row, nothing copied; a deck template or a Word reference document is named by path in a recipe's Format section. The `/forge` map says which libraries a project needs and whether each is cloned alongside; a missing one is brought in with `/import-project`. The library has its own repository and visibility. One worked example with `lib-<name>`.
- inputs:
  .claude/skills/new-project/SKILL.md
  .claude/skills/ingest/SKILL.md
  .claude/skills/forge/SKILL.md
  .claude/agents/check-light.md
  CLAUDE.md#Repository layout
- links:
  `docs/about/projects-and-the-engine.md`: why a library is a kind of project and what a dependency means.
  `docs/use/register-a-source.md`: the ingest the library shares with every project.
  `docs/use/bring-in-an-existing-project.md`: cloning a library that is missing alongside.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no library name of an instance; no template file name of a company.
- made: derived
- evidence: the library's file set and the `lib-` prefix are CLAUDE.md, Repository layout; what `/new-project` creates for a library is its Library paragraph; a changed library document as maintenance is `/ingest`'s sweep paragraph; citation by path with an index entry and a Dependencies row is `/ingest` step 5; the map's Dependencies line is `/forge` step 3; the missing-library finding with `/import-project` is the light check's Dependencies clause. The page joins them into one procedure.
- state: keep

## about

### docs/about/what-it-is-and-is-not.md
- title: What the forge is and is not
- line: What is Forge of Thought, what is it not, and why?
- kind: explanation
- reader: user, extender, evaluator
- says: What the forge is: a general engine for forging any thought, bound to no person or management relationship; the principal is whoever's thinking is forged, the recipients whoever receives the result; Claude is a cognitive extension, an amplifier never a substitute, who proposes and never decides. What it is not: not a program, nothing is implemented in it; not a delivery tool, a run ends where its owner is satisfied; not a chat, state lives in files; not tied to one domain. Why the name, why "thought" and not "assignment", why the chain ends where the project needs it to. One worked example: one invented thought and where its run ends.
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
  `docs/about/where-it-is-going.md`: the direction the forge is developed in, and what is not promised.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no name of the first principal or author; no company; no origin story beyond "it began as one person's tool, an instance fact"; no commands.
- made: derived
- evidence: CLAUDE.md, What this workspace is, gives the identity; the Essence, POS.0005, POS.0010 and POS.0070 the general engine and the amplifier; POS.0780 where a run ends and what is outside its sight; POS.0330 state in files; POS.0600, POS.0620, REJ.0130 the name and what was rejected; REJ.0125 the dropped founding framing. The page states each as the intent reasons it.
- state: keep

### docs/about/how-a-thought-travels.md
- title: How a thought travels through the forge
- line: What happens to one idea from a rough brief to a saved release?
- kind: explanation
- reader: user, extender, evaluator
- says: One invented, generic thought followed through: it arrives as a brief, rough on purpose; is chiselled into the intent by elicitation, positions with reasons, facts, threads, rejections, rewritten for coherence every round; below the intent the project takes the layers it needs, an assignment to hand over, a solution design of how it is realised, many ending at the intent; at every layer blind reviewers press on the documents and the thinking and every finding ends in a recorded verdict; outputs for every audience are generated through recipes and regenerated when the thinking moves, the documentation the same way; everything saved to git and released with a README and release notes. Sources and research arrive at any stage and are used only as the principal directs. The main courses of events (a round, a review, a render, a save, a release) in one sentence each.
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
- links:
  `docs/about/the-document-chain.md`: the chain as a star and why files are numbered in tens.
  `docs/about/isolated-reviewers.md`: why the reviewers never see the conversation.
  `docs/about/renders-and-recipes.md`: how an output is generated from the artefacts.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no command syntax beyond names in passing; no forge project detail; no version numbers.
- made: derived
- evidence: CLAUDE.md, Document chain gives the chain and its items; the solution design's head gives the main courses of events in its own words; the positions give what each station is for. The page tells it in the order a thought meets it, on one invented thought.
- state: keep

### docs/about/the-principal-and-claude.md
- title: The principal and Claude
- line: Who decides, who proposes, and which rules bind Claude?
- kind: explanation
- reader: user, evaluator
- says: The two roles: the principal supplies ideas, answers and decisions and is the final authority on all content; Claude owns structure, order, process discipline and document hygiene, proposes and never decides. The prime directives that follow, each with its reason: when unsure ask and elicit, raising what does not fit as a question and saying in words how sure a claim is; never introduce a convention unilaterally; many iterations are normal; research before inventing; advisory never blocking; structure over prose; one write per round and "written" means a file; one mechanism in one place. Why: nothing enters content because Claude proposed it; the rules bind Claude, not the principal, whose recorded exception is the designed form. Authorship is the principal's whether an artefact is found together or handed over. One worked example of a question raised, generic.
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
- must-not: no name, role or handle of an instance's principal; no directive as an instruction to Claude beyond what it means for the person; no decision record cited.
- made: derived
- evidence: CLAUDE.md, Roles and Prime directives give the rules; the positions give their reasons (POS.0200 why structure over prose; POS.1370 that certainty is said in words; POS.1410 that authorship is the principal's either way). The page pairs each rule with its reason; a directive whose reason no position gives is said to have its reason not recorded.
- state: keep

### docs/about/working-methods.md
- title: The working methods
- line: What are the named ways a working conversation runs, and why each exists?
- kind: explanation
- reader: user, evaluator
- says: The forge's vocabulary of collaboration, none a command, each invoked in a word: Walkthrough, Propose never decide (and `??`), Step by step (a remark in answer to "shall I change it?" is not a yes), Elicitation interview, In pieces, Draft early, Reflect back, One write per round (`write`), Intent-first, Handing over, Recommend do not push, Plain speech, Kind not count. For each, what it is in the operating layer's wording and why in the intent's: the one-item rule because text loaded once dissolves in a long conversation, which is why a hook repeats it; one write per round because writing after every exchange buries the change; step by step because consent is given to a concrete operation, never to its description; handing over because the principal's attention is the scarce thing; plain speech because the principal reads the first lines and carries no IDs in his head; kind not count because a numeric limit answers a problem of kind with a rule of amount. Every list that needs a decision ends by offering a walkthrough. One worked example of a method invoked, generic.
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
- must-not: no hook text; no dates or incidents of the intent's reasons ("on 2026-10-03 ..."); no project the methods were learnt on; nothing of the assistant's memory.
- made: derived
- evidence: CLAUDE.md, Working methods gives every method's name and wording; the walkthrough skill the shape of an item and the verdicts; the intent's group Working methods (POS.0850 to POS.0910, POS.1160, POS.1170, POS.1210, POS.1460, POS.1470, POS.1480) and POS.1410 (handing over) give the reasons. The page keeps CLAUDE.md's order and names.
- state: keep

### docs/about/elicitation.md
- title: Elicitation
- line: How are the principal and Claude meant to find an artefact together, and what is a definition?
- kind: explanation
- reader: user, extender, evaluator
- says: Elicitation is the process by which the principal and Claude find an artefact together: the conversation is the medium, the interview one instrument, research and sources others. Three things kept apart: the map of what must be found, the process by which it is walked, the template where the result lands; the map stands before the template because a template can be filled and still miss what the artefact is for. Every kind of artefact has a definition in seven blocks, Target, Inputs, Aim, Partner, Map, Instruments, Course, paired with its template; a Map is a map of what must be found, not a questionnaire, walked at the moments the definition names, an area left empty when considered and found not to apply. What is not elicitation: composing a recipe, `/setup`, a walkthrough of findings. Found together or handed over, authorship is the principal's. One worked example: a Map walked for an invented artefact.
- inputs:
  projects/forge/10-intent.md#Elicitation
  templates/artefact-definition.md
  CLAUDE.md#Document chain
- links:
  `docs/about/the-document-chain.md`: how the definitions make the chain a star.
  `docs/extend/add-an-artefact.md`: writing a definition of one's own.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no block of a particular artefact's definition (each has its page); no brief of the forge project named; nothing of the Elicitation group's history (dates, briefs) beyond the reasons.
- made: derived
- evidence: the intent's group Elicitation (POS.1300, POS.1310, POS.1320, POS.1410) states what elicitation is, the seven blocks, the Map and the reason the map stands before the template; the skeleton shows the blocks as they stand on disk; CLAUDE.md, Document chain says every artefact has a definition paired with its template and that the definitions are the one list. The page explains the shape from these three.
- state: keep

### docs/about/the-document-chain.md
- title: The document chain
- line: Why is the chain a star of definitions, and how does it grow?
- kind: explanation
- reader: user, extender, evaluator
- says: The chain starts at a brief and its trunk is the intent; below the intent a project takes the layers it needs, none a condition of another, and a layer it does not have is not missing. The chain is a star, not a line: each artefact's definition declares its own inputs, so a layer branches from any artefact by adding one definition, and the dispatcher `/forge <state>` never changes; knowing the artefact's name is knowing the command. Files numbered in tens so that layers can be added without renaming. Which artefacts exist is the listing of the definitions directory. Substance changes go into the intent first, then down the chain; a change may come from below and then the intent changes first. The chain never spans two principals. The diagram: the artefacts of today's chain with their inputs as the definitions declare them (brief; intent from the briefs; assignment from the intent; solution design from the lowest layer above it), drawn from the Target and Inputs blocks. One worked example, generic.
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
  `docs/about/elicitation.md`: what a definition is and how an artefact is found by it.
  `docs/reference/artefacts.md`: the definitions of today, one row each.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no planned layer drawn as if it existed; no forge project history.
- made: derived
- evidence: CLAUDE.md, What this workspace is and Document chain give the trunk, the growth and the numbering; the `/forge` skill says the chain is a star and a layer is a file; the Inputs blocks of the four definitions give the arrows of the diagram; the positions give the reasons (POS.0700 the growth downward and that the chain never spans two principals; POS.0580 why work is invoked by target state). Where no input gives a reason (why the definitions directory is the one listing; why a change goes intent-first), the page says the reason is not recorded.
- state: keep

### docs/about/the-brief.md
- title: The brief
- line: What is a brief, who writes it, and why is it rough on purpose?
- kind: explanation
- reader: user, evaluator
- says: An artefact page: a brief is the principal's text of one whole of thinking, what he wants and why, with what he chose to take from the finding around it; free form, no IDs, a minimal header carrying version and status; rough on purpose because the chiselling is the intent's, and a brief polished until the intent has nothing to do has gone too far. Not the record of the finding: what stays out lives in research and sources or nowhere. Nothing marks authorship; `(source: <path>)` and `(remark: …)` carry something else. Three origins equally legitimate. A project may have more than one, each later whole as `00-brief-<name>.md`, mined into the single intent when the principal says so; versioned like every artefact, approved on his word, never locked. Kept in the language it is written in. Made from, what it holds, complete when, how it is found, why. One worked example: a generic five-line brief.
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
  `docs/about/languages.md`: why a brief keeps its language while the chain has one output language.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no brief of the forge project named or quoted; no Course steps (the use page's); no author field value; nothing of the prime directives but directive 6's language exception.
- made: derived
- evidence: the definition (Target, Aim, Partner, Map) gives the wording; the template the header; POS.0110 and POS.0920 what a brief is, why rough, why several, the marks; the three REJ what was rejected; prime directive 6 the language exception.
- state: keep

### docs/about/the-intent.md
- title: The intent
- line: What does the intent hold, why is it rewritten every round, and where does solving go instead?
- kind: explanation
- reader: user, evaluator
- says: An artefact page: the intent is the working document, the consolidated current state of what the principal holds, rewritten for coherence every round, never a log, because chat context dies and anything of value must live in a file. It holds positions with their reasons and provenance, facts on the principal's or a source's word, rejected directions with the reason, and in `threads.md` beside it what is being worked. What a position carries and what belongs in its history instead; why a fact has a prefix of its own; why a thread names the artefact it concerns; the optional staging area for the layer below. An intent says what is wanted and why and does not solve: the test of a sentence is whether it would still hold if the thing were realised wholly differently. Complete for now when no thread blocks the next layer, never finished. One worked example: a generic position with its reason.
- inputs:
  .claude/skills/forge/states/intent.md
  templates/intent.md
  templates/threads.md
  projects/forge/10-intent.md#POS.0120
  projects/forge/10-intent.md#POS.0230
  projects/forge/10-intent.md#POS.1390
  projects/forge/10-intent.md#REJ.0010
- links:
  `docs/use/forge-the-intent.md`: iterating it.
  `docs/about/elicitation.md`: how the intent is found, the Map walked at the round's end.
  `docs/about/versioning-and-history.md`: the history companion a position's past lives in.
  `docs/about/the-solution-design.md`: where the solution goes instead.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no position of the forge project quoted; no numbering rules beyond naming the prefixes.
- made: derived
- evidence: the definition (Aim, Threads and files) gives the wording; POS.0120 what the document is and what a position and a thread carry; POS.0230 why FCT and THR exist; the template's last section the staging area; POS.1390 the intent/solution test; REJ.0010 why a Q&A log was rejected. The page pairs each with its reason.
- state: keep

### docs/about/the-assignment.md
- title: The assignment
- line: What makes an assignment complete, and where does assigning end and solving begin?
- kind: explanation
- reader: user, evaluator
- says: An artefact page: the assignment carries the in-scope substance of the intent to the recipients, complete and precise, so that they can act without the principal in the room. Complete means nothing left to assumption: delegated or open on purpose is complete, silent is not; length is whatever fidelity requires. It assigns and does not solve, the boundary being the kind of content never its amount. Structured items with stable IDs and shall/shall not, no priorities, testability recommended, success criteria wanted not compulsory, a Terms section; why shall and not softer verbs or MoSCoW. Why a joint pass of three phases and not item by item. Why the name. One worked example: a generic requirement item.
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
  `docs/about/stable-ids.md`: why every item carries an ID that is never renumbered.
  `docs/reference/requirement-style.md`: the rule set.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no rule set reproduced; no item of an instance project; no spin-off mechanics.
- made: derived
- evidence: the definition (Aim, Map, the joint pass with its two "why not") gives the wording; POS.0130, the group Structure and style of an assignment (POS.0200 to POS.0290, POS.0200 and POS.0250 with their reasons) and POS.1350 give the reasons; the three REJ what was rejected.
- state: keep

### docs/about/the-solution-design.md
- title: The solution design
- line: What does a solution design hold, and why does it restate nothing above it?
- kind: explanation
- reader: user, extender, evaluator
- says: An artefact page: the solution design says how the things wanted are realised, as the solution stands today, kept current and read by whoever realises it without the principal in the room. Derived from the lowest layer above it; worth writing where the way is not obvious, a choice has a price, or two hands would solve it differently; whether it is, the principal says. It holds what cannot be read off the thing itself: why, against what, at what price, how the parts fit; it cites the layer above by ID and names what realises a part by path, copying neither. The shape of a SOL item: what the part is and answers for, Realises, Choice, Where; a TBC with its owner. From the artefacts the thing must be buildable without the finished product. One worked example: a generic SOL item.
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
- evidence: the definition (Aim, Partner, Map, the shape of an item) gives the wording; the three positions the reasons and the place in the chain.
- state: keep

### docs/about/documents-and-records.md
- title: Documents and records
- line: What kinds of document does a project hold, and why does state live in files?
- kind: explanation
- reader: user, extender, evaluator
- says: "Document" is every file of a project; "artefact" is reserved for the documents of the chain. Every document has one kind, in five groups: artefacts (versioned, rewritten freely), records (history and decisions append-only; reviews and challenges immutable), state (the ledger, the resource indexes, the documentation map, freely rewritten), rendering (recipes versioned and never approved, renders and pages overwritten), resources (sources and research, immutable). Why state lives in files and never in the conversation: what is in a file survives the session and what lives only in the conversation does not, so `/end` says what would be lost. The ledger as the single source of truth, kept current, citing and never copying. Why immutability is a process rule and not a git mechanism; why corrections happen downstream. Prose hard-wrapped at about 72 columns so that diffs stay legible. One worked example, generic.
- inputs:
  CLAUDE.md#Document kinds
  CLAUDE.md#Ledger
  templates/ledger.md
  templates/decisions.md
  projects/forge/10-intent.md#POS.1080
  projects/forge/10-intent.md#POS.0160
  projects/forge/10-intent.md#POS.0320
  projects/forge/10-intent.md#POS.0330
  projects/forge/10-intent.md#POS.0550
- links:
  `docs/reference/document-kinds.md`: the table of kinds, verbatim.
  `docs/reference/ledger.md`: the ledger's tables and states.
  `docs/use/end-a-session.md`: the command that says what lives only in the conversation.
  `docs/about/versioning-and-history.md`: the history companion of every versioned kind.
  `docs/about/the-documentation.md`: the map and the pages, the two generated kinds.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no table reproduced; no forge project ledger content.
- made: derived
- evidence: CLAUDE.md, Document kinds and Ledger give the groups, the kinds and the ledger's role; the two templates the shapes; the positions the reasons (POS.0550 why immutability stays a process rule; POS.0330 that what lives only in the conversation does not survive and `/end` says what that is). Where no input gives a reason (why the ledger cites and never copies; why corrections to an immutable document happen downstream), the page says the reason is not recorded.
- state: keep

### docs/about/versioning-and-history.md
- title: Versioning and history
- line: What does a version number mean, what is a major, and where does a document's history live?
- kind: explanation
- reader: user, extender, evaluator
- says: Integers denote signed-off versions, drafts 0.x, changes after approval 1.1 and on, the next approval 2.0; status agrees with the number; a recipe stays 0.x for life. What a major of an intent is: it closes a package the principal names, approves the intent as the record of what he holds at that date, signs nothing over, and before its tag passes a test that attests the documents conform to the conventions and to each other and that the thinking has been challenged, nothing of how the model behaves. Every versioned document keeps its history in an append-only companion beside it, a log of one record per change with the reason, Action and Was word for word. Why: the way to an item does not belong in the item; the log is the single primary from which commit messages and release notes derive; a history is searched by `/history`, never loaded whole, because the history of an item is scattered over the log, the archive and the records of other items. A companion written before the log moves to an archive. The author of a record is the one who decided the change. One worked example: a generic record.
- inputs:
  CLAUDE.md#Versioning & status
  templates/history.md
  projects/forge/10-intent.md#POS.0300
  projects/forge/10-intent.md#POS.0310
  projects/forge/10-intent.md#POS.0730
  projects/forge/10-intent.md#POS.1510
  projects/forge/10-intent.md#REJ.0110
- links:
  `docs/reference/versioning-and-front-matter.md`: the fields and the scheme, exactly.
  `docs/reference/history-companion.md`: the record's shape.
  `docs/use/read-the-history-of-an-item.md`: reading one item's history by command.
  `docs/use/release-a-version.md`: where the tag of a major is proposed.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no record of the forge project; no research note cited; no version number of the forge; no list of the checks a major of the forge ran.
- made: derived
- evidence: CLAUDE.md, Versioning & status gives the scheme and the companion rule; the template the record; POS.0300 what a major closes and attests; POS.0310 and POS.0730 the single primary and the derivations; POS.1510 why one command reads an item's history; REJ.0110 the rejected scheme.
- state: keep

### docs/about/stable-ids.md
- title: Stable IDs
- line: Why does every item carry an ID that is never renumbered?
- kind: explanation
- reader: user, extender, evaluator
- says: Every item carries `PREFIX.NNNN`, three-letter prefix, numbered in tens with each group at the next hundred, global and stable, never renumbered; items move between groups without a change of ID; groups are plain headings. Why structure over prose even at high abstraction: an item with a stable ID can be cited, reviewed, traced into the layer below and changed one at a time, where prose cannot be pointed at. Why a fact, a position and a thread have prefixes of their own; why a thread carries its origin. A house convention aligned with a BRD standard where one exists. One worked example, generic.
- inputs:
  CLAUDE.md#ID scheme
  projects/forge/10-intent.md#POS.0200
  projects/forge/10-intent.md#POS.0220
  projects/forge/10-intent.md#POS.0230
  projects/forge/10-intent.md#REJ.0020
  projects/forge/10-intent.md#REJ.0100
- links:
  `docs/reference/id-scheme.md`: the prefix table and the numbering rules, exactly.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no table (reference); no ID of an instance project; no group name of a company standard.
- made: derived
- evidence: CLAUDE.md, ID scheme gives the rules; the positions the reasons; the two REJ what was rejected. Where no input gives a reason (the numbering in tens and hundreds, the three-letter prefix), the page says the reason is not recorded.
- state: keep

### docs/about/isolated-reviewers.md
- title: The isolated reviewers
- line: Why do three kinds of reviewer never see the conversation, and what does their agreement mean?
- kind: explanation
- reader: user, extender, evaluator
- says: Three kinds of reviewer of one shape: the critic (document quality, lenses, FND), the challenger (substance, personas, CHL), the check (mechanical conformance, checks, FND). All run as isolated subagents that see the project's documents and never the working conversation, on the session model; their blindness is the source of their value. All invoked by hand, settled by walkthrough, reports immutable and dated; nothing blocks, every finding fixed or rejected with a recorded reason. The shared behaviour of each kind is one contract, the agent file owns only its Lens; a lens narrows, never replaces. Isolation is not independence: the reviewers share the author's model family, and their agreement is never validation. Instance facts never enter a report. One worked example, generic.
- inputs:
  CLAUDE.md#Isolated reviewers
  projects/forge/10-intent.md#POS.0400
  projects/forge/10-intent.md#POS.1120
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
- must-not: no roster (reference); no contract text; no planned challengers on another model family presented as built; the documentation agents are not reviewers and are not counted here.
- made: derived
- evidence: CLAUDE.md, Isolated reviewers gives the mechanism; the positions the reasons; REJ.0080 why review and challenge are two reviewers.
- state: keep

### docs/about/the-critic.md
- title: The critic
- line: What does a critic lens judge, and why two lenses?
- kind: explanation
- reader: user, extender, evaluator
- says: The critic judges the quality of the artefacts as documents through a lens, never the substance; two lenses because one critic hunted formalities and never guarded the chain: `clarity` reads each artefact on its own, `essence` distils every adjacent pair blind and compares, a finding being a difference of essences. How it works: regression first on its own earlier findings, respect for rejected ones, sharp and few, each artefact judged against its own definition, deliberate omissions never reported as defects, testability a recommendation. What it produces: a dated report in `reviews/` with FND findings carrying severity and category, a delta summary, recommendations, ledger rows. A target narrows a lens to one artefact or one pair. One worked example of a finding, generic.
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
- must-not: no report template reproduced; no instruction to the agent copied as such; no finding of the forge project.
- made: derived
- evidence: the contract gives subject, way of working and output; the positions why two lenses and why testability is a recommendation.
- state: keep

### docs/about/the-challenger.md
- title: The challenger
- line: What does a challenger persona attack, and why may it be wrong?
- kind: explanation
- reader: user, extender, evaluator
- says: The challenger attacks the substance of the thinking through a persona with a register and blind spots of its own, as an equal with no stake in the principal being right, never document quality. How it works: reads for what is not there, grounds itself externally where a claim hinges on the world, never fabricates, three to seven challenges ordered by severity, each with what would change its mind and an epistemic status, never proposing edits; it may be wrong and says what it assumes. What it produces: a dated report in `challenges/` with CHL challenges, what is strong and the questions it cannot answer, ledger rows. Why best run before the next layer is derived; why a rejected challenge is healthy; why an accepted one is mended where it needs to be and goes above its layer only as a thread. One worked example of a challenge, generic.
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
- evidence: the contract gives subject, way of working and output; the positions the reasons.
- state: keep

### docs/about/the-check.md
- title: The check
- line: What does a check verify, why is it read-only, and who files its report?
- kind: explanation
- reader: user, extender, evaluator
- says: A check verifies mechanical conformance with the current conventions, never substance or quality, each check owning one concern; it reads the rules at their owners and never restates them. Read-only: it returns its report and the session files it, so that the IDs of a project's findings are given in one place and a check every save runs has no right to write into the project at every save. Findings only, precise to file and line, ranked by severity; what conforms is not reported; a finding decided once by a DEC is not raised again; a known finding keeps its ID. Advisory. Composition is the caller's: `/save` runs `light`, `/release` runs `light` and `project`, for the engine `engine` too. Why a check's findings are filed like a critic's and why a run that finds nothing files nothing. One worked example, generic.
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
- must-not: no report template; no Lens text; no finding of the forge project.
- made: derived
- evidence: the contract gives subject, way of working and output; the positions the composition and the reasons, POS.1140 among them why the session files the report and why findings get an ID. Where no input gives a reason (why a run that finds nothing files nothing), the page says the reason is not recorded.
- state: keep

### docs/about/renders-and-recipes.md
- title: Renders and recipes
- line: Why is an output generated from a recipe and never edited by hand?
- kind: explanation
- reader: user, extender, evaluator
- says: A render is an audience-specific output generated from the chain, never a source of truth; what is iterated is its recipe, inputs, audience, instructions and the literal template in one versioned file; never edited by hand. The boundary between chain and render is authorship. Every render opens with provenance and is stale when a cited version differs; regenerated only on the principal's word or by a release, because regeneration is stochastic and an unreviewed regeneration is an unreviewed edit, which is why a recipe pins load-bearing wording, a release reports the delta and a written render is scanned for instance facts. An output is made in two steps divided by cost, the plain file with the render through pandoc, the designed file by `/publish` through a model. Every project's README and release notes are renders of its own recipes; what a README carries is the readme skeleton's; recipes may be composed by genre. A render may be an input of another. A page of the documentation is not a render. One worked example: a generic recipe's shape.
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
  projects/forge/10-intent.md#REJ.0160
  projects/forge/10-intent.md#REJ.0240
- links:
  `docs/use/compose-a-recipe.md`: composing a recipe.
  `docs/use/render-an-output.md`: generating a render.
  `docs/use/publish-a-designed-file.md`: the designed file.
  `docs/reference/render-provenance.md`: the provenance block and the definition of stale.
  `docs/about/the-documentation.md`: the pages, generated without a recipe.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no recipe of the forge project quoted; no author line; no pitch content; no script options; not the readme skeleton's fixed closing sentence (it carries an address).
- made: derived
- evidence: CLAUDE.md, Document chain (Renders) gives the mechanism; the recipe skeleton the sections; the readme skeleton's Instructions what a README carries; the positions the reasons; the two REJ what was rejected.
- state: keep

### docs/about/the-documentation.md
- title: The documentation
- line: What is the documentation, who reads it, and why is it generated rather than written?
- kind: explanation
- reader: user, extender, evaluator
- says: The documentation of a project, the engine's among them, is a set of pages of one topic each in `docs/`, readable where the project is published and in a clone, with an index that lists every page and names each reader's path. Three readers in order of weight: the user, the extender, the evaluator who gets the concept pages and nothing made for him alone. Five sections by the reader's journey, filled only where the project has material; each page of one kind, how-to, explanation or reference, and the kind says what belongs on it; one rule has one home page, every other page says a sentence and links; every page is reached from another page, not from the index alone. Generated and never composed by hand: a page mirrors the files that own its topic or is derived from named evidence, and says which; the map (kind `map`) lies beside the owning project's ledger and is never shown to the reader; the pages and the index (kind `page`) are what he reads. Two agents make it under one contract, a planner and a writer per page, reading every input from disk; a run regenerates only pages whose inputs changed, an input hashed as the named part of a file, and the rule the pages are made by is hashed with them so that a change of the rule regenerates every page; a release reports the index's age and offers the command. Why: the README was the whole documentation and poor as one; why not a recipe per page, a site, a hand-kept philosophy. The diagram: one documentation run (planner, map, state script, writers, index script, check script). One worked example: a generic entry of the map.
- inputs:
  CLAUDE.md#Document kinds
  CLAUDE.md#Document chain
  .claude/skills/document/SKILL.md
  .claude/skills/docs-contract/SKILL.md
  .claude/agents/docs-planner.md
  .claude/agents/docs-writer.md
  projects/forge/10-intent.md#POS.1450
  projects/forge/10-intent.md#POS.0930
  projects/forge/10-intent.md#REJ.0240
  projects/forge/10-intent.md#REJ.0250
  projects/forge/10-intent.md#REJ.0260
  projects/forge/40-solution-design.md#Rendering and publishing
- links:
  `docs/use/generate-the-documentation.md`: running `/document`.
  `docs/extend/change-a-documentation-page.md`: changing a page through its owners.
  `docs/reference/documentation-map.md`: the map's entry and the page's front-matter, field by field.
  `docs/about/renders-and-recipes.md`: the renders, which the pages are not.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no count of pages or date of a run; no model name; no entry of the engine's map quoted; no name of a project other than `forge`; nothing of the contract as an instruction to Claude; nothing of the solution design's group beyond SOL.0460.
- made: derived
- evidence: CLAUDE.md, Document kinds (the rows `map` and `page`) and Document chain item 5 give what the documentation is and where the map lies; the `/document` skill the one run; the contract what the two agents share; the planner the readers, the outline, mirrored/derived and that every page is reached from another page; the writer the page's shape; POS.1450 the position whole with its reason, POS.0930 why a mirrored page runs on a faster model; the three REJ what was rejected; SOL.0460 the choices and what each was chosen against, the generator hashed with the inputs among them, and the parts of a run the diagram draws. Where no input gives a reason (why the evaluator gets the concept pages and nothing of his own; the order of the three readers), the page says the reason is not recorded.
- state: keep

### docs/about/sources-and-research.md
- title: Sources and research
- line: Why are sources immutable, why is registration not intake, and what is a research note for?
- kind: explanation
- reader: user, evaluator
- says: External inputs live in `sources/`, immutable once registered, one form each, arriving at any stage; a related set is a bundle with its own catalogue. Registration is not intake: what a source is for is the principal's word, its Role in the resource index, and source content enters the intent only by his explicit act with provenance. Research is a durable answer to one question, immutable and dated, because the principal does not want to reinvent what the world has solved. Every `sources/` and `research/` directory carries an index so that what exists is known without re-reading; the index tracks nothing and is an automatic input of no command, so a contradiction between the intent and a source is not a finding. Why personal matter stops an ingest before the store. One worked example: a generic index entry.
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
- must-not: no source of the forge project; no index entry reproduced.
- made: derived
- evidence: CLAUDE.md, Document chain (External inputs, Resource indexes) gives the rules; the skeletons the fields; the positions the reasons (POS.1040 why personal matter stops the command before the store; POS.0050 why research). Where no input gives a reason (why a source is immutable at all), the page says the reason is not recorded.
- state: keep

### docs/about/projects-and-the-engine.md
- title: Projects and the engine
- line: Why is every project a repository of its own that the engine does not know?
- kind: explanation
- reader: user, extender, evaluator
- says: The engine is one public repository, the core together with its own project `projects/forge`; every other project is a repository of its own under a gitignored `projects/`, recognised by the scripts through its `.git`; a project may have any remote and visibility, or none. Why: publication of the engine with nothing sensitive, access per project, seamless work inside. A project has a kind, thought or library; a library is shared material with no chain, cited by path as a dependency taken knowingly. Instance facts live in `CLAUDE.local.md` at the engine root; the forge's behaviour lives in the engine, never in the assistant's memory. A project records no engine version. The shapes rejected. The diagram: the engine root with its own project and the nested project repositories, each with its own remote, the engine's remote the upgrade channel. One worked example, generic.
- inputs:
  CLAUDE.md#Repository layout
  CLAUDE.md#Persistence (git)
  projects/forge/10-intent.md#POS.0760
  projects/forge/10-intent.md#POS.0940
  projects/forge/10-intent.md#POS.0950
  projects/forge/10-intent.md#POS.0960
  projects/forge/10-intent.md#POS.0970
  projects/forge/10-intent.md#POS.1020
  projects/forge/10-intent.md#POS.1030
  projects/forge/10-intent.md#REJ.0140
  projects/forge/10-intent.md#REJ.0150
  projects/forge/40-solution-design.md#Persistence
- links:
  `docs/use/share-material-through-a-library.md`: using a library.
  `docs/use/upgrade-the-engine.md`: the upgrade and the migration path.
  `docs/reference/repository-layout.md`: the layout, file by file.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no host, company or project name other than `forge`; no repository address; no history of the split as a story; nothing of the design's group beyond SOL.0500.
- made: derived
- evidence: CLAUDE.md, Repository layout and Persistence give the shape; the positions the reasons; the two REJ what was rejected; SOL.0500 the gitignore pattern and why it must be `projects/*`, and the parts the diagram draws.
- state: keep

### docs/about/persistence-in-git.md
- title: Persistence in git
- line: Why are the scripts the only door to git, and why two doors, two speeds?
- kind: explanation
- reader: user, extender, evaluator
- says: The scripts in `scripts/` are the only door to git, reading state included, for Claude a wall of the harness; the principal's own git from the shell is his. Two doors, two speeds: `/save` with the light check, seconds, on any branch; `/release` from `main` only with its checks, the README and release notes, the release message and the major's tag, because the renders cost minutes and a README on `main` is then current at every release and stale in between visibly. `/pull` is the door inward: the forge looks at the remote and says the state as a fact, pulls only a clean repository that is behind, and never pulls or merges on its own, because a clone behind its origin is the normal case on more than one machine and a merge on Claude's judgement would be work without the principal's word. `main` is the released line, branches voluntary, merging git's, because the principal does not want a wrapper of git. The commit identity is git's, resolved per host, with a guard so that a missing identity fails aloud; a commit carries no attribution trailer. Immutability is a process rule, not a git mechanism. The scripts are Python, `python` on PATH their one prerequisite, written to run unchanged on Linux and macOS as a writing rule, not a verified claim. One worked example, generic.
- inputs:
  CLAUDE.md#Persistence (git)
  projects/forge/10-intent.md#POS.0550
  projects/forge/10-intent.md#POS.0830
  projects/forge/10-intent.md#POS.0950
  projects/forge/10-intent.md#POS.1100
  projects/forge/10-intent.md#POS.1110
  projects/forge/10-intent.md#POS.1200
  projects/forge/10-intent.md#POS.1490
  projects/forge/10-intent.md#REJ.0160
  projects/forge/10-intent.md#REJ.0170
- links:
  `docs/use/save-your-work.md`: the save.
  `docs/use/release-a-version.md`: the release.
  `docs/use/pull-from-the-remote.md`: the pull.
  `docs/use/work-on-a-branch.md`: branches.
  `docs/reference/scripts.md`: the scripts themselves.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no host, identity example or incident story; no git command; no mention of PowerShell.
- made: derived
- evidence: CLAUDE.md, Persistence gives the rules, Portability and the two doors among them; the positions the reasons (POS.0550 why immutability stays a process rule, POS.1100 why two commands, POS.1490 why the forge never pulls on its own); the two REJ what was rejected. Where no input gives a reason (why the scripts-only door is a wall of the harness and why a commit carries no attribution trailer, POS.1200 stating both as decided), the page says the reason is not recorded.
- state: keep

### docs/about/how-the-rules-are-held.md
- title: How the rules are held
- line: How does the forge keep its rules in force across a long conversation and inside a subagent?
- kind: explanation
- reader: extender, evaluator
- says: One always-on core, `CLAUDE.md`, loaded into every session and subagent, carrying only what must hold everywhere; everything else a file read when its situation arises. One mechanism lives in one place and is cited by path everywhere else, because two copies drift. A rule that must hold through a long conversation is repeated at every prompt by a hook, since text loaded once dissolves; what the hook prints. The harness enforces what it can: deny rules keep Claude from raw git and sensitive paths; a command that changes files the moment it runs is guarded against being started on Claude's own judgement, while maps, reports and rosters stay his to propose. A subagent may take the session's copy of a file for the file on disk, so every agent that writes an outward-facing file reads its inputs from disk and says that instance facts are not material, and generated files are scanned mechanically. One model for the whole forge. The forge's behaviour never lives in the assistant's memory. The forge explains itself through `/man`. One worked example, generic.
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
- evidence: prime directive 10 and the Walkthrough method give the one-place rule and the hook; `.claude/settings.json` the deny rules and the hook started by `python`; the hook's `LINES` what it prints; the positions the reasons (POS.1090 the criterion of a guarded command; POS.1170 the hook as context, not enforcement; POS.0950 why an agent reads from disk and the files are scanned; POS.1030 why the behaviour lives in the engine); SOL.0010, SOL.0020, SOL.0030 and SOL.0040 how the core, the instance file, the hook and the walkthrough skill are realised.
- state: keep

### docs/about/languages.md
- title: Languages
- line: Which language does each kind of document carry, and why only one output language per project?
- kind: explanation
- reader: user, evaluator
- says: The forge dictates one output language per project: the artefacts of the chain in the language the ledger header declares, English when absent; records, state, research and recipes always English because Claude, the reviewers and the checks read every project the same way; English the notation throughout; the briefs the one exception, kept as written; a render in any language its recipe declares, a translation being a render; the documentation English only. The conversation language is an instance fact set in `CLAUDE.local.md`, never shown outward. Translate on write. One worked example, generic.
- inputs:
  CLAUDE.md#Prime directives
  projects/forge/10-intent.md#POS.0060
  projects/forge/10-intent.md#POS.1450
- links:
  `docs/start/setup.md`: where the conversation language is set.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no language value of an instance; no example project; nothing of the prime directives but directive 6; nothing of POS.1450 but the documentation's language.
- made: derived
- evidence: prime directive 6 gives the rule; POS.0060 the reason; POS.1450 that the documentation is English only, a translation a render. Where no input gives a reason (why the briefs keep their language; why English is the notation), the page says the reason is not recorded.
- state: keep

### docs/about/where-it-is-going.md
- title: Where the forge is going
- line: In which direction is the forge developed, and what is deliberately not promised?
- kind: explanation
- reader: user, extender, evaluator
- says: Direction without destination: the chain is to be extended downward as far as the principal needs a thought taken, a BRD layer certain, integration intended, a strategy layer possible; nothing approved for construction, the mechanics of a layer designed when taken up. A new kind of artefact is added by one command; a user is to be able to add one of his own at his own place, which is open. Independent challengers on another model family are planned, mechanics undecided. One principal per instance for now. Developed at its owner's discretion and pace; direction named, destinations and deadlines not. Feedback and ideas are wanted most.
- inputs:
  projects/forge/10-intent.md#POS.0700
  projects/forge/10-intent.md#POS.0780
  projects/forge/10-intent.md#POS.0800
  projects/forge/10-intent.md#POS.1110
  projects/forge/10-intent.md#POS.1430
  projects/forge/10-intent.md#POS.1440
- links:
  `docs/about/the-document-chain.md`: how a layer is added.
  `docs/extend/how-a-change-is-made.md`: how a change reaches the forge.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no thread quoted; no date; no version; no company rollout; no name.
- made: derived
- evidence: positions only, since threads change with every round; the page states direction as the positions state it. Where no input gives a reason (why the mechanics of a layer are designed only when it is taken up; why one principal per instance), the page says the reason is not recorded.
- state: keep

## extend

### docs/extend/what-it-is-made-of.md
- title: What the forge is made of
- line: Which files make up the operating layer, what is each, and when is it loaded?
- kind: how-to
- reader: extender
- says: Opens with a table (path, what it is, loaded when): `CLAUDE.md`, the always-on core, every session and subagent; `.claude/skills/<name>/SKILL.md`, one per command, read when invoked, with the `/forge` state files and the `/recipe` genre files as supporting files read by path, and the skills that are not commands, the three reviewer contracts, the documentation contract and the walkthrough skill, preloaded or read when their situation arises; `.claude/agents/`, one file per lens, persona and check, front-matter and Lens only, and the documentation's planner and writer, loaded once per session when launched; `.claude/settings.json`, deny rules and the hook, at start; `templates/`, the skeletons, among them one `<type>-definition.md` per type the forge is extended by and the map's skeleton, read when a file is born; `scripts/`, Python with the shared modules beside them, run on demand; `projects/forge`, the forge's own project, where its intent, solution design, documentation map and the recipes of its README, release notes and CONTRIBUTING live; `docs/`, the generated documentation. Then one line of flow: a prompt arrives, the hook prints its lines, a command's skill is read, it reads definitions and templates by path, launches agents or runs scripts, and writes files of the project. Then the four ideas that carry it: one always-on core and the rest on demand, state in files, isolation by subagents, deterministic work in scripts. Where to read what a thing does: its own file. One worked example: one command traced through the layer.
- inputs:
  CLAUDE.md#Repository layout
  CLAUDE.md#Templates
  CLAUDE.md#Persistence (git)
  projects/forge/40-solution-design.md#How the parts work together
  projects/forge/40-solution-design.md#The instruction layer
  projects/forge/40-solution-design.md#The commands
  projects/forge/40-solution-design.md#The reviewers
  projects/forge/40-solution-design.md#Across the parts
- links:
  `docs/reference/repository-layout.md`: the layout block.
  `docs/reference/templates.md`: every skeleton, what it is the skeleton of and which procedure creates from it.
  `docs/about/how-the-rules-are-held.md`: why the core is small and the rest on demand.
  `docs/extend/how-a-change-is-made.md`: changing any of it.
  `docs/about/the-documentation.md`: what `docs/` and the map are.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no listing of individual commands or agents (reference); no file of an instance; no repository address; no count of pages or date of a run; no choice of the design restated beyond what each kind of file is.
- made: derived
- evidence: CLAUDE.md, Repository layout and Templates give the directories, the scripts by name, the contracts and the `<type>-definition.md` rule; Persistence (Portability) the shared modules; the design's head the four ideas and SOL.0010, SOL.0100, SOL.0120, SOL.0130, SOL.0300, SOL.0330, SOL.0620 what each kind of file is and when the harness loads it. The table and the line of flow are the writer's join of these.
- state: keep

### docs/extend/how-a-change-is-made.md
- title: Make a change to the forge
- line: How is a change of the forge's behaviour made, proved, recorded and released?
- kind: how-to
- reader: extender
- says: A change of how the forge behaves goes through the chain before it is built: a position in the forge intent, through `/forge intent forge`, with its history record; the item of the solution design where the change solves something, through `/forge solution-design forge`; then the operating layer, and where the two differ that is a finding. Proved by `/check engine`, which verifies the core against itself and the intent, and before a major or after a round on the operating layer by `/check single-source-of-truth`; recorded in the history companions (a change touching no item under the subject `operating layer`); released by `/release forge`, which re-renders the README and release notes and reports the age of the documentation, offering `/document`; a process change is complete only once the intent is updated and the README re-rendered. A change that alters no behaviour is made directly. The README, the release notes and CONTRIBUTING are renders: a change goes into their recipes. A visitor's way to send feedback, an idea or a change is `CONTRIBUTING.md`, a discussion for feedback and an idea, an issue for a defect, a pull request carrying the position, the item, the change and one line on what was run, and not a release or a regenerated render; in a clone the user decides everything, what is merged into the public engine its author decides. One worked example: one invented change traced through.
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
- must-not: no channel URL, account, profile or name (CONTRIBUTING.md named as a file, the channels by kind only); no pull-request mechanics beyond what the recipe gives; no claim that the release regenerates the documentation on its own.
- made: derived
- evidence: CLAUDE.md, The system's own project gives the completeness rule; Versioning & status the `operating layer` subject; the positions intent-first for the forge and the open rule; the contributing recipe's Instructions the line between the two kinds of change, who decides what, the channels by kind and what a pull request carries and does not; the two check agents what proves a change; the release skill what a release re-renders and that it offers `/document`.
- state: keep

### docs/extend/add-an-artefact.md
- title: Add an artefact
- line: How is a new kind of artefact added to the chain with `/new-artefact`?
- kind: how-to
- reader: extender
- says: An add page: `/new-artefact <name>` leads to everything a kind needs and decides nothing: a position in the forge intent first; the definition `.claude/skills/forge/states/<name>.md` in the seven blocks from `templates/artefact-definition.md` and its template `templates/<name>.md`, which has no skeleton; the row of a new prefix in the ID scheme; the reviewers, a persona where decided and the calibration of the critic's contract; the item of the solution design. The Map of what is found. The rosters need nothing: `/forge`, `/man` and the README read the definitions from disk. Prove it: `/check engine`; the first artefact of the kind through `/forge <name>` on real work is the trial. Recorded and released as any change. One worked example with `<name>`.
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
- says: An add page: a lens is one agent file `.claude/agents/critic-<lens>.md` from `templates/critic-definition.md`: front-matter (name, one-line description saying what it reads and when it fits, tools, `model: inherit`, `skills: critic-contract`) and a Lens section in four parts. Nothing the contract owns is restated; a lens may narrow or make a shared rule stricter, never rename, drop or duplicate one. The description is the roster line of bare `/critique` and `/man critique`; a description carrying a colon followed by a space is quoted whole or the agent does not register. Only by the principal's decision and only where what it finds genuinely differs. Prove it: `/check engine`; a run on a project. Recorded and released as any change. One worked example with `<lens>`.
- inputs:
  templates/critic-definition.md
  .claude/skills/critic-contract/SKILL.md
  .claude/skills/critique/SKILL.md
  CLAUDE.md#Isolated reviewers
- links:
  `docs/extend/how-a-change-is-made.md`: proving, recording and releasing the change.
  `docs/about/the-critic.md`: what the contract owns.
  `docs/reference/critic-lenses.md`: the lenses that exist, as models of the shape.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no contract text copied; no existing lens's angles copied as content.
- made: mirrored
- state: keep

### docs/extend/add-a-challenger-persona.md
- title: Add a challenger persona
- line: How is a new challenger persona added as one agent file?
- kind: how-to
- reader: extender
- says: An add page: a persona is one agent file `.claude/agents/challenger-<persona>.md` from `templates/challenger-definition.md`: front-matter (name, description saying who this is, tools including web search, `model: inherit`, `skills: challenger-contract`) and a Lens section in two parts, who the persona is and what it goes after. Nothing of the contract restated. Only by the principal's decision and only where its blind spots genuinely differ. A persona costs one file and no edits: the roster is scanned. Prove it: `/check engine`; a run on a target. Recorded and released as any change. One worked example with `<persona>`.
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
- says: An add page: a check is one agent file `.claude/agents/check-<name>.md` from `templates/check-definition.md`: front-matter (name, description saying what it verifies and when it fits, read-only tools, `model: inherit`, `skills: check-contract`) and a Lens section in three parts, what it reads, what it verifies with the owner of each rule cited and what is a fact rather than a finding, and its cost. One concern per check. It writes nothing: the `/check` procedure files its report. Whether a save or a release runs it is the caller's definition to say. Prove it: `/check engine`; a run on a project. Recorded and released as any change. One worked example with `<name>`.
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
- says: An add page: a genre is two files: `.claude/skills/recipe/genres/<genre>.md`, a definition with a one-line description, the genre name, its skeleton and output, a role and a numbered elicitation checklist, and `templates/recipe-<genre>.md`, the skeleton that extends the base recipe shape and never replaces it, with a `## Format` section where the render has a file beside it. Every genre runs in the same frame: the checklist closes with the language question and the recipe is composed from the skeleton. The dispatcher never changes; bare `/recipe` and `/man recipe` scan the directory. Prove it: `/check engine`; a composition on a project. Recorded and released as any change. One worked example with `<genre>`.
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
- evidence: the `/recipe` skill says a genre is two files, that the dispatcher never changes and gives the shared frame; the presentation genre file and its skeleton are the model of the two shapes; `templates/recipe.md` says the skeleton owns the shape and a genre skeleton extends it. The page derives the procedure from the model pair.
- state: keep

### docs/extend/add-a-command.md
- title: Add a command
- line: How is a new command added as a skill, and when is it guarded?
- kind: how-to
- reader: extender
- says: An add page: a command is a skill `.claude/skills/<name>/SKILL.md`: front-matter with `description` (one line, what the command does and what bare means), a quoted `argument-hint`, and `disable-model-invocation: true` where the command changes files the moment it runs (a write, a scaffold, a commit, a pull, a regeneration), so that Claude cannot start it on its own judgement, while a command that writes only at the end of a round on the principal's word, or files the record of a run he asked for, needs no guard; a body that says what the command does and cites every mechanism of another by path, never restating it; supporting files beside it where it dispatches over a roster. A row in the Commands table of `CLAUDE.md`, which `/man` and the README derive from. Named so that it does not collide with a built-in of Claude Code. Prove it: `/check engine` verifies the table against the skills; `/check single-source-of-truth` that nothing is restated. Recorded and released as any change. One worked example with `<name>`.
- inputs:
  CLAUDE.md#Commands
  .claude/skills/ledger/SKILL.md
  .claude/skills/end/SKILL.md
  .claude/agents/check-engine.md
  projects/forge/10-intent.md#POS.1090
  projects/forge/10-intent.md#POS.1070
  projects/forge/10-intent.md#POS.1050
  projects/forge/10-intent.md#POS.1190
  projects/forge/40-solution-design.md#The commands
- links:
  `docs/extend/how-a-change-is-made.md`: the chain the change goes through.
  `docs/reference/commands.md`: the commands that exist.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no skill body copied; no harness detail beyond what the solution design states; nothing of the design's group beyond SOL.0100, SOL.0110 and SOL.0180.
- made: derived
- evidence: SOL.0100 and SOL.0110 give the skill shape, the quoted hint and the guard; POS.1090 the criterion of a guarded command; POS.1070 citation over restatement; CLAUDE.md, Commands the table; the `ledger` skill the smallest model of a command that cites another's mechanism, the `end` skill the model of an unguarded report (SOL.0180); the `check-engine` agent that the table is verified against the skills; POS.1050 and POS.1190 the naming rule against built-ins.
- state: keep

### docs/extend/add-a-script.md
- title: Add a script
- line: How is a new script written so that it is portable, documented in its docstring and the one owner of its facts?
- kind: how-to
- reader: extender
- says: An add page: a script is Python 3.8 or newer, run as `python scripts/<name>.py`, with its help in its module docstring: synopsis, what it does, what it needs, options, where the output lands, examples each with a comment saying what it shows; the docstring owns those facts and commands cite it. Rules: nothing Windows-only, `pathlib` for paths, `subprocess` with argument lists and never a shell, external tools resolved from PATH and never installed, colour only on a terminal, examples free of platform paths, no URL and no identity. What several scripts share lives in one module beside them: `forge_repos.py` for the git scripts, `forge_tools.py` for the conversions, `docs_map.py` for the documentation scripts and the history script. It is named in the layout comment of `CLAUDE.md`, and a command that uses it names it by path. Prove it: `/check engine` verifies scripts on disk against `CLAUDE.md`. Recorded and released as any change. One worked example: a generic docstring.
- inputs:
  CLAUDE.md#Persistence (git)
  CLAUDE.md#Repository layout
  scripts/forge-status.py
  scripts/forge_repos.py
  .claude/agents/check-engine.md
  projects/forge/10-intent.md#POS.0830
  projects/forge/40-solution-design.md#Across the parts
- links:
  `docs/extend/how-a-change-is-made.md`: proving, recording and releasing the change.
  `docs/reference/scripts.md`: the scripts that exist.
  `docs/about/persistence-in-git.md`: why the scripts are the only door.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no claim that the set has been run on Linux or macOS; no instance path; no mention of PowerShell; no script body; nothing of the design's group beyond SOL.0620.
- made: derived
- evidence: CLAUDE.md, Persistence (Portability) gives the writing rules and the shared modules, Repository layout the comment a script is named in; POS.0830 the reason and that portability is a writing rule until verified; SOL.0620 how the scripts are written and what each shared module holds; `forge-status.py` the smallest model of a docstring, `forge_repos.py` the model of a shared module; the `check-engine` agent that scripts on disk are verified against the layout comment.
- state: keep

### docs/extend/change-a-documentation-page.md
- title: Change a documentation page
- line: How do you change what a page says, which pages exist, or what the check refuses, without editing a page?
- kind: how-to
- reader: extender
- says: A page is never edited by hand; what is wrong is mended in the file that owns the matter and the page regenerated. Finding the owner: the page's front-matter lists its inputs and says whether it is mirrored or derived. To change what a page says: change the owning file (a skill, a definition, a template, an agent, a script's docstring; a reason comes from the forge intent) and run `/document`, which remakes only the pages whose inputs, entry or generating rule changed. To change the shape every page has or what every page must keep off: the writer's definition and the contract are hashed with the inputs, so a change of either regenerates every page. To change which pages exist, what a page covers or who reads it: the map is written by the planner from the target at every run, and the readers and the outline are the planner's definition and a position of the forge intent, so such a change goes through the chain. What the contract keeps off every page. A fact a page needs and no file owns is reported under Unowned and left out until it gets a home; the readme skeleton's optional section "Pinned facts (not rendered)" is that home, read by the planner as an owner. What the check refuses: a link that does not resolve, a long dash in prose, a missing front-matter, an instance fact; a page that fails twice is left out and said. An agent's definition is loaded once per session: a change to the planner or the writer reaches them in a new session. One worked example: one invented fix traced through.
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
- evidence: the `/document` skill gives "mended in the file that owns the matter", the state computed from the inputs, the check's rules, the twice-failing page and the harness note; the contract what must never reach a page; the writer the page's front-matter and that it reads its task first; the planner that the map is written from the target at every run, the readers, the outline and Unowned; the state script's docstring that an input is hashed as its part and that the generator (the writer's definition and the contract) is hashed with the inputs; the check script's docstring what it looks for and that it mends nothing; the readme skeleton's pinned-facts comment the home of facts no file owns. The page joins them into the order of one change.
- state: keep

## reference

### docs/reference/commands.md
- title: Commands
- line: Every command with its signature, purpose, arguments and whether it is guarded.
- kind: reference
- reader: user, extender, evaluator
- says: A roster page: one overview table first (command, purpose, arguments, guarded or not), then one entry per command in the order of the Commands table of `CLAUDE.md`: the row's signature and purpose, the skill's `description` and `argument-hint`, and whether it carries `disable-model-invocation: true`; `/pull`, `/end`, `/history`, `/man` and `/manual` included.
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
- says: A roster page: one overview table first, then one row per definition in `.claude/skills/forge/states/` in the order of the file numbers: the artefact's file, its `description`, its template, its inputs (Target and Inputs blocks), the prefixes of its items from the ID scheme, and the command that works it. One line below: a layer a project does not have is not missing.
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
- says: A roster page: one overview table first (name, what it is for, when it fits, where it lives), then one entry per `.claude/agents/critic-*.md`: the lens name, its `description`, and its Lens section (what it reads, what it goes after, its categories, its own report sections), as `/man critique` prints them.
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
- says: A roster page: one overview table first, then one entry per `.claude/agents/challenger-*.md`: the persona name, its `description`, and its Lens section (who it is, what it goes after), as `/man challenge` prints them.
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
- says: A roster page: one overview table first, then one entry per `.claude/agents/check-*.md`: the check name, its `description` with when it fits, and its Lens section (what it reads, what it verifies with the owner of each rule, its cost), as `/man check` prints them; one line on which a save and a release run, from the two skills.
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
- says: A roster page: one overview table first, then one entry per `.claude/skills/recipe/genres/*.md`: the genre, its `description`, its skeleton and output, and its elicitation checklist in full, as `/man recipe` prints them; the shared closing (the language question, composition from the skeleton) once.
- inputs:
  .claude/skills/recipe/genres/presentation.md
  .claude/skills/recipe/genres/readme.md
  .claude/skills/recipe/genres/release-notes.md
  .claude/skills/recipe/SKILL.md
- links:
  `docs/use/compose-a-recipe.md`: composing through a genre.
  `docs/extend/add-a-recipe-genre.md`: adding a genre.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no skeleton reproduced; no explanation; not the parenthesis of the release-notes genre that the forge's own recipe reads the intent alone (the page says only that a project may narrow the companions).
- made: mirrored
- state: keep

### docs/reference/id-scheme.md
- title: ID scheme
- line: The format, the numbering rules and the prefix table, exactly.
- kind: reference
- reader: user, extender, evaluator
- says: The format `PREFIX.NNNN`, the numbering rules (tens, next hundred per group, overflow, groups as plain headings, depth two), and the prefix table with meaning and where each lives, as the ID scheme of `CLAUDE.md` has them.
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
- line: The version scheme and the front-matter fields of an artefact, a brief and a recipe, exactly.
- kind: reference
- reader: user, extender, evaluator
- says: The version scheme (0.x drafts, integers approved, x.y after approval), the front-matter fields of an artefact (`version`, `date`, `status` with its three words, `last_change`, `project`, `audience`; a brief carries `title` and `author` in place of `audience`) and of a recipe (`version`, `updated`, `last_change`, no status, optional `output:`), the status rule, the companion and archive file names, as `CLAUDE.md` and the templates have them.
- inputs:
  CLAUDE.md#Versioning & status
  templates/intent.md
  templates/brief.md
  templates/recipe.md
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
- says: The shape of `<file>.history.md` as `templates/history.md` owns it: the front-matter, the record line with its fields in order (date, version, author, subject, kind, reason, Action, Was), the five kinds, what the subject may be, when a field is left out, `Was` last with `<br>` between paragraphs, lines not wrapped, the two records at a document's birth, and the archive rule as `CLAUDE.md` has it.
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
- says: The rule set as the Requirement style of the assignment's definition has it: shall and shall not, the banned words, no priorities and the *optional* note, one idea per item in full sentences, testability recommended not required, defined Terms capitalised, no dependence on an external link.
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
- says: The table of document kinds of `CLAUDE.md`, verbatim, six columns and every row; one line each on the companion of every versioned kind, on a library's reduced set, and on the wrapping rule.
- inputs:
  CLAUDE.md#Document kinds
- links:
  `docs/about/documents-and-records.md`: why the kinds exist.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no explanation.
- made: mirrored
- state: keep

### docs/reference/ledger.md
- title: Ledger
- line: The ledger's header, tables, columns and state words, exactly.
- kind: reference
- reader: user, extender
- says: The ledger as `templates/ledger.md` owns it: the header fields (`project`, `kind`, `language`, `updated`), every table with its columns (Briefs, Documents, Renders, Published, Sources, Dependencies, Research, Findings, Challenges) and Waiting on principal; the state words of briefs, published files, findings and challenges with the reading of an older word; the row of the documentation index in Renders; which tables a library keeps; the rule that the ledger cites and never copies, as `CLAUDE.md` has it.
- inputs:
  templates/ledger.md
  CLAUDE.md#Ledger
- links:
  `docs/use/see-where-a-project-stands.md`: reading the ledger through `/ledger`.
  `docs/about/documents-and-records.md`: why the ledger is the single source of truth for state.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no row from a project; no explanation.
- made: mirrored
- state: keep

### docs/reference/render-provenance.md
- title: Render provenance
- line: The provenance block every render opens with, the definition of stale, and where the files land.
- kind: reference
- reader: user, extender
- says: The YAML front-matter every render opens with, verbatim as `/render` step 5 gives it, and the one definition of a stale render; the two file places (`renders/<recipe>.md` or the recipe's `output:`), the plain file beside the render, and the `published/` place with its `current | stale` state.
- inputs:
  .claude/skills/render/SKILL.md
  .claude/skills/publish/SKILL.md
- links:
  `docs/use/render-an-output.md`: the command.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no explanation; no example from a project; nothing of the scan a render passes.
- made: mirrored
- state: keep

### docs/reference/documentation-map.md
- title: Documentation map
- line: The fields of the map, of a writer's task, of a page's front-matter and of the index, exactly.
- kind: reference
- reader: extender
- says: The shape of the map `docs-map.md` as its skeleton, the planner, the writer, the contract and the scripts own it. The map: a front-matter of `generated`, `target`, `owner`, `previous`; every path relative to the target's root; the `## Paths` section, one line per reader; one section per section of the outline in its order, and in each one entry headed `### docs/<section>/<page>.md` with the fields in order: `title`, `line`, `kind`, `reader`, `says`, `inputs` (a file, or a part named after `#`: a section by its heading, an item by its ID, or a block by its bold label, hashed as that part), `links`, `must-not`, `made`, `evidence`, `state` (which of its values the planner writes and which the state script sets); then Unowned and Did not fit. The task file: the engine root, the page's path, the date, the version, the hash, the entry verbatim, the titles of the linked pages. The page: a front-matter of `generated`, `version`, `made`, `inputs-hash`, `inputs`, then the title, one paragraph, the matter in the outline of its kind, See also, the fixed closing line. The index: derived from the map, the reader paths as links, one line per page from the entry's `line`, with the intent's version.
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
- says: The words and what each does, as the walkthrough skill owns them: the verdict line `(a)ccept / (m)odify / (r)eject / (p)ark` and the single letters `a`, `m`, `r`, `p` as a whole message; `obsolete`; `write`; `??`; a closing word such as "done" for a thought sent in pieces; that no other word of the forge has a letter and every command is typed in full.
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
- says: The layout block of `CLAUDE.md`, Repository layout, in full: the engine root, a thought project, a library; each comment kept as a fact.
- inputs:
  CLAUDE.md#Repository layout
- links:
  `docs/about/projects-and-the-engine.md`: why projects are repositories of their own.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no explanation; no value of an instance file.
- made: mirrored
- state: keep

### docs/reference/scripts.md
- title: Scripts
- line: Every script with its synopsis, options, forms, what it needs and the command that runs it.
- kind: reference
- reader: user, extender
- says: A roster page: one overview table first (script, what it is for, the command that runs it, what it needs), then one entry per file in `scripts/` from its module docstring: what it does, its synopsis and options in the Python spelling, its forms (bare, slug, `forge` for the engine), what it needs installed, where its output lands; for `forge-status.py` the `--remote` flag and the states it reports; for `forge-history.py` what it gathers and `--full`; for `md2pptx.py` and `md2docx.py` the two engines with their defaults and how a template or a reference document is named, what the conversions need as `forge_tools.py` owns it; for the three documentation scripts their place in the run of `/document`, the state script's hashing of the generator with the inputs among it, and for `docs-check.py` its one-file scan of instance facts that `/render` runs; the three shared modules each in one line, not commands. Below, the portability rule in one line.
- inputs:
  scripts/forge-save.py
  scripts/forge-pull.py
  scripts/forge-status.py
  scripts/forge-clone.py
  scripts/forge-branch.py
  scripts/forge-history.py
  scripts/forge_repos.py
  scripts/doc2md.py
  scripts/md2pptx.py
  scripts/md2docx.py
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
  `docs/use/render-an-output.md`: the render that runs the one-file scan.
  `docs/use/read-the-history-of-an-item.md`: the command behind the history script.
  `docs/extend/add-a-script.md`: writing a script of one's own.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: nothing below a docstring; no example path or slug of a project (the docstrings carry `platform-strategy`, `agentic-platform`, a `lib-acme` path and a path into the forge project's renders, replaced by `<slug>` and `<path>`; `forge`, `main`, `my-idea` and `example.com` may stand); no date or thread number from the hook's docstring; no explanation.
- made: mirrored
- state: keep

### docs/reference/templates.md
- title: Templates
- line: Every skeleton in `templates/`, what it is the skeleton of, and which procedure creates from it.
- kind: reference
- reader: extender
- says: A roster page: one overview table first, then one entry per file in `templates/`: what it is the skeleton of, which command or procedure creates from it, and its fields or sections in one line; the `<type>-definition.md` naming rule; the map's skeleton, written by the planner of `/document`; the readme skeleton's optional section "Pinned facts (not rendered)" and what it is for; the fields of a resource index entry and of a bundle index.
- inputs:
  templates/CLAUDE.local.md
  templates/brief.md
  templates/intent.md
  templates/threads.md
  templates/assignment.md
  templates/solution-design.md
  templates/ledger.md
  templates/decisions.md
  templates/history.md
  templates/index.md
  templates/index-bundle.md
  templates/recipe.md
  templates/recipe-readme.md
  templates/recipe-release-notes.md
  templates/recipe-presentation.md
  templates/docs-map.md
  templates/artefact-definition.md
  templates/critic-definition.md
  templates/challenger-definition.md
  templates/check-definition.md
  CLAUDE.md#Templates
- links:
  `docs/extend/what-it-is-made-of.md`: where the templates sit in the whole.
  `docs/reference/documentation-map.md`: the map's fields in full.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no skeleton reproduced whole; no explanation; not the readme skeleton's fixed closing sentence (it carries an address).
- made: mirrored
- state: keep

### docs/reference/configuration.md
- title: Configuration
- line: The files that configure an instance and what each holds, field by field.
- kind: reference
- reader: user, extender
- says: `.claude/settings.json` (shared: `attribution` empty and sessionUrl false, the deny rules for sensitive paths and raw git in both shells, the `UserPromptSubmit` hook running `scripts/hook-walkthrough.py` through `python` with the project-directory placeholder); `.claude/settings.local.json` (gitignored, the session model, created by `/setup`); `CLAUDE.local.md` (gitignored, the principal by role and the conversation language, from its template); the `.gitignore` of the engine (`projects/*` with `projects/forge` re-included, the two local files, the engine's `tmp/`, Python caches and office noise); the git identity outside the engine, per host, with the guard, as `/setup` writes it.
- inputs:
  .claude/settings.json
  .gitignore
  templates/CLAUDE.local.md
  .claude/skills/setup/SKILL.md
  CLAUDE.md#What this workspace is
- links:
  `docs/start/setup.md`: the command that fills the instance files.
  `docs/about/how-the-rules-are-held.md`: why the deny rules and the hook exist.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no value of an instance; no host; no explanation beyond one clause per item; nothing of the `.gitignore`'s entry for a local launcher (a file of one instance); no mention of PowerShell beyond the deny rule's shell name.
- made: mirrored
- state: keep

### docs/reference/glossary.md
- title: Glossary
- line: Every term of the forge in one line, with the file that defines it.
- kind: reference
- reader: user, extender, evaluator
- says: The terms in one line each, with the file that defines each: principal, recipients, Claude as cognitive extension, session, harness, document, artefact, brief, intent, position, fact, thread, rejected direction, assignment, solution design, layer, definition, template, Map, elicitation, walkthrough, verdict, round, write, history companion, record, archive, ledger, decision, source, bundle, extract, research, resource index, Role, recipe, render, plain file, published file, genre, provenance, stale, critic, lens, challenger, persona, check, finding, challenge, contract, Lens section, subagent, isolation, project, thought project, library, dependency, engine, instance, instance fact, session model, save, release, pull, major, tag, branch, immutable, mined, documentation, documentation map, page, index, mirrored, derived, pinned fact, Unowned, guarded command, working method, prime directive.
- inputs:
  CLAUDE.md
  projects/forge/10-intent.md#POS.0120
  projects/forge/10-intent.md#POS.0230
  projects/forge/10-intent.md#POS.0300
  projects/forge/10-intent.md#POS.0950
  projects/forge/10-intent.md#POS.1090
  projects/forge/10-intent.md#POS.1450
  projects/forge/10-intent.md#Elicitation
  .claude/skills/forge/states/brief.md
  .claude/skills/forge/states/intent.md
  .claude/skills/forge/states/assignment.md
  .claude/skills/forge/states/solution-design.md
  .claude/skills/walkthrough/SKILL.md
  .claude/skills/render/SKILL.md
  .claude/skills/document/SKILL.md
  .claude/skills/pull/SKILL.md
  .claude/skills/critic-contract/SKILL.md
  .claude/skills/challenger-contract/SKILL.md
  .claude/skills/check-contract/SKILL.md
  .claude/skills/docs-contract/SKILL.md
  .claude/agents/docs-planner.md
  .claude/agents/docs-writer.md
  templates/ledger.md
  templates/recipe-readme.md#Pinned facts (not rendered)
- links:
  `docs/about/what-it-is-and-is-not.md`: the forge in prose.
- must-not: no term invented; no definition longer than a sentence; no name, handle or instance value; no address.
- made: derived
- evidence: each term is defined where a file first defines it: the roles, the document kinds, the chain, the reviewers, the ledger, persistence, the commands in CLAUDE.md (whole, since the terms span its sections); the artefacts in their definitions' Target and Aim; position, fact, thread, rejection in POS.0120 and POS.0230; elicitation, Map, definition in the Elicitation group; walkthrough, verdict, round, write in the walkthrough skill; render, provenance, stale in the render skill; the states against the origin in the pull skill; lens, persona, check, finding, challenge, contract, Lens section, isolation in the three contracts; session, harness, instance, subagent, voice in the docs contract; the ledger's state words in its template; engine, instance fact in POS.0950; major in POS.0300; guarded command in POS.1090; documentation, map, page, index, mirrored, derived in POS.1450, the `/document` skill and the two agents; pinned fact in the readme skeleton's section. The writer takes each term from its owner and writes one sentence; a term no file defines is left out.
- state: keep

## Unowned

- Whether the forge runs on Linux and macOS as a verified fact, needed by `docs/start/install.md`, `docs/about/persistence-in-git.md` and `docs/extend/add-a-script.md`: CLAUDE.md, POS.0830 and SOL.0620 say it is a writing rule until verified. The pages state the rule and no claim.
- Which faster model a mirrored page is written on and why that one: the `/document` skill names `sonnet` as the override, POS.0930 gives the reason for a faster model but not for which; `docs/use/generate-the-documentation.md` and `docs/about/the-documentation.md` say "a faster model" and name none.
- What `/document <slug>` reads for a project other than the engine beyond the planner's paragraph "For a project", and in which language a project's pages are written when its artefacts are not English: POS.1450 leaves both to THR.0590. `docs/use/generate-the-documentation.md` says only where a project's pages and map land; `docs/about/languages.md` says the documentation is English only, which is POS.1450's word for the engine.
- What `/forge <state>` does on a project of kind `library`: not needed by any page; recorded so that no page invents it.
- What Claude Code is beyond "the engine runs in Claude Code" and "Claude acts as the principal's cognitive extension": `docs/start/what-it-is.md` is asked to say in plain words that Claude is an AI assistant, and no file of the engine says more of Claude Code than that the forge runs in it, that it is Anthropic's and that `/help` and `/init` are its built-ins (POS.1050, POS.1190). The page says what the Essence says and nothing beyond it.

## Did not fit

- The skeleton's heading `# Documentation map — <target>` carries a long dash; the contract forbids one anywhere in what the agents write, so this map's heading carries a spaced hyphen. The scripts parse the entries, not the heading.
- `docs/start/what-it-is.md` is an explanation in a section the outline marks how-to; a page that says what the thing is in one paragraph cannot be a how-to. Marked `kind: explanation`, kept in `start/` where the outline places it.
- The reader of the map (`scripts/docs_map.py`) says in its docstring that an item is taken by the line that carries `**POS.1450**`; the positions of the groups Working methods and Elicitation and POS.1190 and POS.1200 carry a title inside the bold (`**POS.0850 Walkthrough.**`). The previous map cited POS.1200 and POS.1190 by ID, and this map does the same for a titled item where a page needs that item alone; where a page needs most of a group (the working methods, the Elicitation group), the group's heading is named and hashed as the group, and the entry's `evidence` narrows the writer to the items the page needs. A block of a definition is named by its bold label (`brief.md#Course`), which the reader supports. Should the state script report a titled item as missing, the group heading is the fallback.
- The outline says `use/` never names a subagent or a model; `docs/use/generate-the-documentation.md` says "a planner", "a writer", "a faster model" and "the session model" because the skill's steps are nothing without them and the person sees their reports; no agent file and no model name reaches the page.
- `/pull` is one command with two jobs on the pages: `docs/use/pull-from-the-remote.md` is the command's home (the states, what is pulled and refused, for the engine and the projects); `docs/use/upgrade-the-engine.md` is the job that follows a pull of the engine, the release notes and the checks per project (POS.0940). Each says one sentence of the other and links.
- The release-notes genre file says in a parenthesis that the forge itself reads the intent alone, while the forge's release-notes recipe (0.13) reads the solution design's history as well; the recipe is the newer and the one that runs. The pages that mirror the genre leave the parenthesis out and say only that a project may narrow the companions; the genre file's owner settles the sentence.
- POS.1110 of the intent writes the branch command as `forge-branch <name>` while the script takes `<slug> [branch]` and has no bare form; the operating layer wins and `docs/use/work-on-a-branch.md` reads the script alone.
- `CLAUDE.md`, Isolated reviewers and POS.1120 speak of three contracts, one per kind of reviewer; the layout comment and SOL.0460 add a fourth contract skill for the documentation agents, which are not reviewers. Not a contradiction: `docs/about/isolated-reviewers.md` counts three kinds and says the documentation agents are not among them; `docs/about/the-documentation.md` says the two agents share a contract as the reviewers do.
- The pinned facts the owning project's recipes carry sit beside facts no page may carry. `projects/forge/recipes/readme.md` owns the prerequisites, the install lines and the public home in its pinned facts and carries an author line with a name and an e-mail in its Instructions; `projects/forge/recipes/contributing.md` carries the channels as addresses and the author's profile. The pages that take either name the section they read (`#Pinned facts (not rendered)`, `#Instructions`) and their `must-not` keeps the author, the channels and the profile off the page; `docs/start/first-result.md` reads the readme Instructions for the Quickstart only. The three pitch recipes own nothing a page needs and are the input of no page.
- The scripts' docstrings carry example slugs (`platform-strategy`, `agentic-platform`), a `lib-acme` path and a path into the forge project's renders; the pages replace them by `<slug>` and `<path>` and their `must-not` says so. The hook's docstring carries dates and a thread number; the pages take what it prints.
- The forge intent names its first principal by handle in POS.0005, its Essence says the forge began as one CTO's tool, POS.0610 names a programme, POS.0990 names the licence holder as a fixed text of the readme recipe, and the briefs carry an `author` field; every page that reads the intent has "no name, no handle" in its `must-not`.
- `00-brief.md` of the owning project says no brief exists for the forge; the reasons of the `about/` pages come from the intent, and the briefs reach the pages only through the positions mined from them, so no brief is an input. `threads.md` and `decisions.md` are the input of no page: the threads hold what is being worked, the decisions settle findings and challenges of the forge project. The research index was read for orientation only; the documentation audit registered as a source bears on the generator and is an owner of nothing a page says. The ledger was read for orientation and is the input of no page.
- The thread on the documentation audit (THR.0630) lists reasons the writers wanted and found recorded nowhere, and names two as added in the previous run (why the evaluator gets the concept pages and nothing of his own with the order of the three readers; why the definitions directory is the one listing of the artefacts and why changes go intent-first). No position of the intent and no file of the operating layer carries them today: POS.1450 and the planner's definition state the readers and their order without a reason, and CLAUDE.md, Document chain and POS.0140 state the listing and intent-first without one. The entries of `docs/about/the-documentation.md` and `docs/about/the-document-chain.md` say in `evidence` that the page says the reason is not recorded; the same is said for the other reasons the thread lists where an entry's inputs give none, so that the writers report the places and none invents a reason.
- The solution design still opens by calling itself a proposal not judged whole by the principal; the pages that read its groups as evidence take what the operating layer on disk agrees with, and where the design and a file differ, the file.
- Three reviewer kinds got one page each in `about/` beside the shared one, on the reading that "one page per kind of artefact or part" covers a kind of reviewer; the rosters are three pages in `reference/` so that a new lens, persona or check regenerates one page. The documentation agents get no roster page.
- Every entry of `use/` and `about/` asks for a worked example, every one of `reference/` for an overview table where it is a roster; the writer's outline names the heading "A worked example" and the entries ask for one in those words. The three diagrams stand on the chain, the projects-and-engine and the documentation pages, each drawn from the Inputs blocks of the definitions, SOL.0500 with the layout, and SOL.0460 with the `/document` skill. A tutorial with a worked example and a troubleshooting page stay out of the outline until a public exemplar and material for them exist (THR.0200); no page is planned for either.
- The rule that every page is reached from another page (solution design 0.13) found twelve entries named under `links` by no other entry: `docs/start/what-it-is.md`, `docs/use/bring-in-an-existing-project.md`, `docs/use/end-a-session.md`, `docs/use/spin-off-a-group.md`, `docs/about/languages.md`, `docs/about/where-it-is-going.md`, `docs/extend/add-a-critic-lens.md`, `docs/extend/add-a-check.md`, `docs/extend/add-a-recipe-genre.md`, `docs/extend/add-a-command.md`, `docs/extend/add-a-script.md` and `docs/reference/templates.md`. Each got a link from the page where a reader would ask for it (the install page to what is installed, the first result and the library page to the import, the save and the documents page to the end of a session, the assignment how-to to the spin-off, the project how-to and the brief to the languages, what-it-is-and-is-not and the artefact add page to where the forge is going, each reviewer concept page and roster page to its add page, the commands and scripts rosters to theirs, what-it-is-made-of and the artefact add page to the templates), none to a page that has no use for it; `docs/extend/add-a-challenger-persona.md`, already reached from the artefact add page, gained the same links as the other two reviewer add pages so that the three are alike. The entries that gained a link are regenerated by the state script, since their text changed.
- The planner's rule that an entry agrees with itself was applied to every entry: where `says` named a fact of a file not among the inputs, the file or its part was added (the state script's docstring on `docs/extend/change-a-documentation-page.md` for the generator hashed with the inputs; POS.1370 on `docs/about/the-principal-and-claude.md` for certainty said in words, in place of the whole Elicitation group; POS.1170, POS.1190 and POS.1200 on `docs/about/how-the-rules-are-held.md` in place of the whole Working methods group); no `must-not` forbids what its `says` or the page shape requires.
- The renders, the README, `CONTRIBUTING.md` and `docs/` of the target were not read, as the definition says; `CONTRIBUTING.md` is named as a file on the strength of its recipe and the layout.
