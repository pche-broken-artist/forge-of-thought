---
generated: 2026-10-10
target: engine
owner: projects/forge
previous: tmp/docs-map.previous.md
---

# Documentation map - the engine

Paths under `inputs` are relative to the target's root, the engine
root. The fourth run, the first after the intent was approved as 5.0:
every page of the previous map still has material and is marked
`keep`; no page is `new` and none is `remove`. `regenerate` is the
script's to set from the hashes of the inputs; the planner never
writes it. What moved since the previous map and reaches the entries:
the render skill hands its subagent the provenance block and the
instance-fact rule in the prompt and scans the written file with
`scripts/docs-check.py --file`, so `docs/use/render-an-output.md` and
`docs/reference/scripts.md` say it; the documentation agents' shared
conduct is a skill of its own, `docs-contract`, and the map has a
skeleton, `templates/docs-map.md`, so the pages on the documentation
take them as inputs; the readme skeleton is the one owner of what a
README carries and of the optional "Pinned facts (not rendered)"
section, which the pinned facts of the forge's own readme recipe fill
and which now own the engine's public address (the solution design
names the recipe as the one place), so `docs/start/install.md` reads
the recipe and no longer the design; `templates/brief.md` carries
version, status and last_change; the help of `md2pptx.py` and
`md2docx.py` sends the reader to `forge_tools.py` for what the
conversions need, so the install page and the scripts page read it;
the intent gives two more working methods their positions (Plain
speech, Kind not count), a remark is not a yes under Step by step,
and says what a major approves and what its test attests; the
release-notes genre file still says the forge's recipe reads the
intent alone while the recipe reads the solution design's history
too, and the page that mirrors the genre leaves that parenthesis
out. The pages of `about/` take the operating layer's wording and the
intent's reason wherever the two differ. No page names a person, a
company, a host, an account or an e-mail; where an input carries one
(the forge intent names its first principal by handle, the readme
recipe carries an author line, the contributing recipe an author's
profile, the scripts' examples slugs of instance projects), the page
leaves it out, and every `must-not` below says so once more. The one
address a page carries is the engine's public home, which the
contract permits where the target's own documents name it as such,
on `docs/start/install.md` alone.

## start

### docs/start/what-it-is.md
- title: About what the forge is
- kind: explanation
- reader: user, evaluator
- says: One paragraph: Forge of Thought is a workshop where a thought is tempered and shaped into a versioned chain of documents under isolated adversarial review, run in Claude Code, with the person as principal who decides everything and Claude as a cognitive extension that proposes and keeps order. The chain starts at a brief, its trunk is the intent, and it ends where the project needs it to; what comes out is an artefact the principal stands behind, and audience-facing outputs are generated from it. One closing sentence says what it technically is (a git repository of slash commands, isolated agents, templates, scripts and conventions) and that the subject matter is unconstrained.
- inputs:
  CLAUDE.md
  projects/forge/10-intent.md
- links:
  `docs/start/install.md`: what must be on the machine and how it gets there.
  `docs/about/what-it-is-and-is-not.md`: the longer explanation of what the forge is, is not, and why.
- must-not: no commands, no file names, no conventions, no history of the project, no name of a person, no instance fact, no version number of the intent.
- made: derived
- evidence: the first two paragraphs of CLAUDE.md, "What this workspace is", give the identity sentence and "the chain ends where the project needs it to"; the intent's Essence and POS.0005, POS.0010, POS.0070, POS.0780 give the roles, the domain-agnosticism and the end of a forge run; POS.0600 and POS.0620 give the name and the subtitle sentence; the technical sentence is composed from CLAUDE.md, Repository layout (skills, agents, templates, scripts) and the intent's Essence ("runs in Claude Code"). The writer condenses; nothing is added.
- state: keep

### docs/start/install.md
- title: Install what the forge needs
- kind: how-to
- reader: user
- says: What must be on the machine before the forge runs and how each piece is installed, in the order a newcomer needs it: git; Python 3.8 or newer on PATH as `python`, because every script and the per-prompt hook are Python (a Linux or macOS system that has only `python3` gives it that name by an alias or a package); Claude Code with a paid subscription, installed by the commands the readme recipe pins; then the optional tools by function, each resolved from PATH and never installed by a script: markitdown through pip for converting documents at `/ingest`, pandoc for the plain Word and PowerPoint files of `/render`, the document-skills plugin installed once from an interactive Claude Code session for `/publish`, unless Claude Code already brings the docx and pptx skills. Then: clone the engine from its public home, the address the readme recipe's pinned facts give, the one address a page carries because it is a fact of the product and not of an instance; never copy it (the save script refuses an engine that is not a git repository); and always start `claude` from the engine root so that `CLAUDE.md` and `CLAUDE.local.md` load. The page closes by pointing at the first setup.
- inputs:
  CLAUDE.md
  .claude/settings.json
  scripts/hook-walkthrough.py
  scripts/forge-save.py
  scripts/forge_repos.py
  scripts/doc2md.py
  scripts/md2pptx.py
  scripts/md2docx.py
  scripts/forge_tools.py
  projects/forge/recipes/readme.md
- links:
  `docs/start/setup.md`: the first run, `/setup`, which fills the instance facts and sets the model.
  `docs/reference/scripts.md`: every script with what it needs and its options.
- must-not: no account, no author line, no e-mail, no address other than the engine's public home as the readme recipe's pinned facts give it; nothing of the readme recipe beyond its section "Pinned facts (not rendered)"; no platform-specific path; no claim that the scripts have been run on Linux or macOS (CLAUDE.md says portability is a writing rule); nothing on git identity (that is setup's); no mention of PowerShell.
- made: derived
- evidence: the readme recipe's section "Pinned facts (not rendered)" is the one owner of the prerequisites, the Claude Code install commands, the paid subscription, "clone, not copy", "start `claude` from the engine root", the script prerequisites and the public home of the engine ("the address a clone and a project's README point to"), and says it is their home; CLAUDE.md, Persistence (Portability) gives Python 3.8 or newer run as `python scripts/<name>.py`, `python` on PATH as the one prerequisite of the scripts, the `python3` remark and that the tools are resolved from PATH; `.claude/settings.json` starts `hook-walkthrough.py` through `python` at every prompt, and the hook's docstring says Python on PATH as `python` is all it needs, which is why Python is needed before anything else; the docstrings of `forge-save.py` (git on PATH) and `forge_repos.py` (the engine must be a clone) give git and the refusal of a copy; `doc2md.py` names the pip line for markitdown and says it installs nothing; `md2pptx.py` and `md2docx.py` say that `forge_tools.py` owns what pandoc and the claude engine need, and `forge_tools.py`'s docstring names pandoc with its install page and platform package lines, the `claude` CLI, and the plugin with its two `/plugin` commands and the two names of the skills. The order is the writer's, by when each piece is first needed.
- state: keep

### docs/start/setup.md
- title: Set up the forge
- kind: how-to
- reader: user
- says: The first run after cloning: `/setup`, run before any other work. What it does for the person, in its three steps: creates `CLAUDE.local.md` from its template by a short interview, the conversation language first and then who the principal is by role, gitignored and never committed; creates `.claude/settings.local.json` with the session model set to Fable, the strongest available model on which the whole forge including the blind reviewers runs, changeable at any time with `/model` or by editing the file; and closes with the git identity, which is git's own: it asks for the hosts the user pushes to with a name and an e-mail for each and offers to write, on his word, the per-host `includeIf` stanzas and the global guard `user.useConfigOnly = true` into the global git configuration file (named by the status script), never overwriting, or prints them for him to apply by hand. It never overwrites an existing file and runs no git operation; it ends by pointing at `/new-project` or `/import-project`.
- inputs:
  .claude/skills/setup/SKILL.md
  templates/CLAUDE.local.md
  CLAUDE.md
  scripts/forge-status.py
- links:
  `docs/start/first-result.md`: from a new project to a saved intent in one sitting.
  `docs/about/persistence-in-git.md`: why the identity is git's and the scripts are the only door.
  `docs/reference/configuration.md`: the instance files and settings, field by field.
- must-not: no example host, name or e-mail; no instance value; nothing of the skill copied as an instruction to Claude; no reason beyond the one sentence CLAUDE.md gives for the guard (fails aloud instead of taking a default).
- made: mirrored
- state: keep

### docs/start/first-result.md
- title: Get a first result
- kind: how-to
- reader: user
- says: One sitting from nothing to a saved intent: `/new-project <slug>` scaffolds the files (no git); paste or dictate the brief when asked, approve it when it is finished; `/forge intent` mines the brief into the first intent through an interview, one question per message, and writes once at the round's end on the word `write`; `/save` runs the light check and commits and pushes. Says in one line that a project is a repository of its own, that `git init` in its directory is the user's one-off act, and that "not under git" until then is a fact, not an error. The alternative door for an existing project: `/import-project <git-url>` then `/forge <slug>`.
- inputs:
  .claude/skills/new-project/SKILL.md
  .claude/skills/forge/states/brief.md
  .claude/skills/forge/states/intent.md
  .claude/skills/save/SKILL.md
  .claude/skills/import-project/SKILL.md
  CLAUDE.md
  projects/forge/recipes/readme.md
- links:
  `docs/use/start-a-project.md`: the full job of starting a project, thought or library.
  `docs/use/forge-the-intent.md`: the full job of iterating the intent.
  `docs/use/save-your-work.md`: what a save does and asks.
- must-not: no explanation of what a brief or an intent is beyond one clause each; no example slug that could be an instance project (use `my-idea`); no theory of elicitation; no repository address; nothing of the readme recipe beyond its Quickstart instruction (Section 3) and its Pinned facts.
- made: derived
- evidence: the sequence is the readme recipe's Quickstart instruction (pinned there: `/new-project my-idea`, `/forge intent`, `/save`; `/import-project <project url>`, `/forge <project-slug>`); what each step does for the person is read from the four skills and the two state files (new-project step 3 hands the brief to the brief procedure; the brief's Course approves a finished pasted text at once; the intent's Course consolidates the briefs into the first intent; save runs `light` then commits and pushes); the "not under git" sentence is CLAUDE.md, Persistence.
- state: keep

## use

### docs/use/start-a-project.md
- title: Start a project
- kind: how-to
- reader: user
- says: `/new-project <slug>`: a thought project (the chain) or a library (`lib-` prefix, material only), the kind and the language of the chain artefacts declared in the ledger header. What the command creates for each kind, files only, never git; the founding brief asked for at once and handed to `/forge brief`; the intent and lower layers not created until their first `/forge <state>`; `logo.png` optional. The one-off act that is the user's: `git -C projects/<slug> init -b main`, then a remote if wanted; the commit identity is git's.
- inputs:
  .claude/skills/new-project/SKILL.md
  CLAUDE.md
  templates/ledger.md
- links:
  `docs/use/write-a-brief.md`: composing the founding brief.
  `docs/use/share-material-through-a-library.md`: what a library is for and how it is used.
  `docs/about/projects-and-the-engine.md`: why a project is a repository of its own that the engine does not know.
- must-not: no instance slug; nothing of the brief procedure (it is the brief page's); no git beyond the one way in CLAUDE.md names.
- made: mirrored
- state: keep

### docs/use/bring-in-an-existing-project.md
- title: Bring in an existing project
- kind: how-to
- reader: user
- says: `/import-project <git-url>` clones the repository through `scripts/forge-clone.py` into `projects/<repository name>`, never overwriting, and relays the script's facts: the last commit, the origin, the identity git resolves for the clone (none resolved means the save script will report and commit nothing), and whether a ledger with a `kind:` header is present, its absence a fact. Nothing is written into the project. Work starts by selecting it, `/forge <slug>`, because the engine does not track projects and cannot guess the one meant.
- inputs:
  .claude/skills/import-project/SKILL.md
  scripts/forge-clone.py
  CLAUDE.md
- links:
  `docs/use/see-where-a-project-stands.md`: the `/forge` map that follows.
  `docs/use/upgrade-the-engine.md`: what to check when a project was written to older conventions.
- must-not: no example URL with a real host (use `<git-url>`; the script's examples use `example.com`, which may stand); no identity example.
- made: mirrored
- state: keep

### docs/use/see-where-a-project-stands.md
- title: See where a project stands
- kind: how-to
- reader: user
- says: Bare `/forge [slug]` reports the map of a project: its kind and whether it is under git, the artefacts with versions and status, the briefs with their mining state, which target states can be worked from here, which renders and published files are stale, which libraries it needs, what waits on the principal (the few live matters in words, the rest as a count), and a recommended next step, offering a walkthrough where more than one matter waits. A library's map stops after its material and the git line. `/ledger [slug]` is the same report read from the ledger only, for one project or all; reconciling the ledger with reality is the light check's.
- inputs:
  .claude/skills/forge/SKILL.md
  .claude/skills/ledger/SKILL.md
  CLAUDE.md
- links:
  `docs/use/walk-through-a-list.md`: how the matters waiting on the principal are worked one by one.
  `docs/reference/ledger.md`: the ledger's tables and state words.
- must-not: no description of `/forge <state>` (each state has its page); no staleness definition beyond a pointer.
- made: mirrored
- state: keep

### docs/use/write-a-brief.md
- title: Write a brief
- kind: how-to
- reader: user
- says: `/forge brief [name] [slug]` composes or finishes a brief, `00-brief.md` or `00-brief-<name>.md` for a later whole of thinking. The three ways the text arrives and what happens with each: pasted whole (stored verbatim, asked whether finished, approved at once if so); begun outside; born in the forge from a rough idea, Claude active at the opening with inspiration, verification, research and ingest proposed and run on the principal's word. What the person can ask for: a structure given to the text without a word changed; `??` for Claude's opinion. The brief is free form, no IDs, approved only on the principal's explicit word, and mined by `/forge intent` when he says so.
- inputs:
  .claude/skills/forge/states/brief.md
  templates/brief.md
  CLAUDE.md
- links:
  `docs/about/the-brief.md`: what a brief is and why it is rough on purpose.
  `docs/use/research-a-topic.md`: the research step the brief's finding uses.
  `docs/use/register-a-source.md`: the ingest step the brief's finding uses.
- must-not: no restatement of the Map's areas (the about page has them); nothing of the Partner block copied as instruction to Claude; no language rule beyond "kept in the language it is written in".
- made: mirrored
- state: keep

### docs/use/forge-the-intent.md
- title: Forge the intent
- kind: how-to
- reader: user
- says: `/forge intent [slug]` iterates `10-intent.md`: the briefs mined whole by whole, one at a time, briefs offered before threads; or a round starting from an open thread, a new word of the principal's or what the recipients sent back. One theme at a time, the reality check last; answers carried in the conversation and written once per round on `write`, Claude reflecting the round back first; resolved threads move into positions or rejections, the briefs' Mined column kept. The open threads live in `threads.md` beside the intent and are rewritten freely. The round ends by naming what changed and what stays open, and names the layers that can follow or offers the approval, a recommendation never a gate. `/challenge <persona> intent` is offered as the independent reality check, never run on Claude's own judgement.
- inputs:
  .claude/skills/forge/states/intent.md
  templates/intent.md
  templates/threads.md
  CLAUDE.md
- links:
  `docs/about/the-intent.md`: what the intent holds and why it is rewritten for coherence.
  `docs/about/working-methods.md`: the named ways the conversation runs, one write per round among them.
  `docs/use/challenge-the-thinking.md`: running the independent reality check.
- must-not: no ID scheme (reference); no restatement of the Map; no Partner text as instruction to Claude.
- made: mirrored
- state: keep

### docs/use/distil-an-assignment.md
- title: Distil an assignment
- kind: how-to
- reader: user
- says: `/forge assignment [slug]` derives `20-assignment.md` from the intent in a joint pass of three phases: questions up front, one per message, only what the intent does not answer; the recast, the whole draft from the intent with a provenance map (group, items, the positions they came from, what landed nowhere, what came from nowhere); the walkthrough by group, one verdict per group. A substance change asked for here goes to the intent first; a wording fix is made directly. After the pass `/critique essence` is offered as the independent test of drift, then the approval, a recommendation never a gate. The items are written in the Requirement style, shall and shall not, no priorities.
- inputs:
  .claude/skills/forge/states/assignment.md
  templates/assignment.md
  CLAUDE.md
- links:
  `docs/about/the-assignment.md`: what makes an assignment complete and where assigning ends.
  `docs/reference/requirement-style.md`: the rule set of the items.
  `docs/use/critique-the-documents.md`: running the essence lens.
- must-not: no restatement of the Requirement style rules (reference); no ID numbering rules.
- made: mirrored
- state: keep

### docs/use/design-the-solution.md
- title: Design the solution
- kind: how-to
- reader: user
- says: `/forge solution-design [slug]` iterates `40-solution-design.md`, how the things wanted are realised, derived from the lowest layer the project has above it. Whether one is worth writing is the principal's to say; the ways in: no design yet, a layer above that moved, the thing changed below, a wording fix. At every pass Claude makes the coverage map, the in-scope items of the layer above with no part and the parts that realise no item. What cannot be realised, or only at a price not worth paying, goes back to the intent as a thread. `/challenge <persona> solution-design` is offered once the design stands; the persona `architect` exists for it.
- inputs:
  .claude/skills/forge/states/solution-design.md
  templates/solution-design.md
  CLAUDE.md
- links:
  `docs/about/the-solution-design.md`: what a solution design holds and why it restates nothing above it.
  `docs/use/challenge-the-thinking.md`: the challenge of the design.
- must-not: no shape of a SOL item beyond one sentence (the about page has it); no theory of the intent/solution boundary.
- made: mirrored
- state: keep

### docs/use/register-a-source.md
- title: Register a source
- kind: how-to
- reader: user
- says: `/ingest [file] [slug]` stores, registers and catalogues external input in `sources/` and does nothing more: with a file, that document; with text pasted into the conversation, the text as `sources/<slug>.md`; bare, a sweep of `sources/` for unregistered files and a report of files changed since registration with a question what to do with each (a breach to settle in a thought project, ordinary maintenance in a library). Personal matter stops the command before storing. Every binary gets one question, convert to Markdown? Yes: `scripts/doc2md.py` makes the extract, which is then the source, the original not copied; no: the binary is the source as a functional thing. A set of related files is a bundle, one source with its own index. After registration Claude always asks what the source is for; the answer goes into the resource index as its Role. A document of a library is cited by path, not copied, and registered as a dependency. Registration is not intake: the principal alone directs how and when a source is used.
- inputs:
  .claude/skills/ingest/SKILL.md
  scripts/doc2md.py
  templates/index.md
  templates/index-bundle.md
  CLAUDE.md
- links:
  `docs/about/sources-and-research.md`: why sources are immutable and why registration is not intake.
  `docs/use/share-material-through-a-library.md`: citing a library's document from a project.
  `docs/reference/scripts.md`: `doc2md.py`, its formats and what it needs.
- must-not: no example file with a real name; no ledger column detail (reference); nothing of the skill copied as an instruction.
- made: mirrored
- state: keep

### docs/use/research-a-topic.md
- title: Research a topic
- kind: how-to
- reader: user
- says: `/research <topic> [slug]` looks up current best practice on one question with web sources, marks what is consensus, emerging or contested, and writes an immutable dated note into `research/` with the question, the findings with sources, options with trade-offs and a recommendation for this project; a topic that turns out to be several questions becomes several notes. The note is indexed in `research/00-INDEX.md` and registered in the ledger. The summary leads with the recommendation; a change to an artefact that follows from it is proposed through `/forge <state>`, never made silently.
- inputs:
  .claude/skills/research/SKILL.md
  templates/index.md
  CLAUDE.md
- links:
  `docs/about/sources-and-research.md`: what research is for and why it is immutable.
- must-not: no example topic from the forge project; no index field detail beyond naming the three fields.
- made: mirrored
- state: keep

### docs/use/compose-a-recipe.md
- title: Compose a recipe
- kind: how-to
- reader: user
- says: `/recipe [genre] [slug]`: bare, the roster of genres with the project's existing recipes; with a genre, a guided composition through that genre's checklist, closing with the language question, the recipe then composed from the genre's skeleton; with the name of an existing recipe, an iteration of it. A recipe outside any genre is composed conversationally from the base skeleton. A recipe is versioned 0.x for life with its history companion, written once per round on confirmation; `/render <recipe>` is offered as the next step. The three genres of today and what each produces, in one line each.
- inputs:
  .claude/skills/recipe/SKILL.md
  .claude/skills/recipe/genres/presentation.md
  .claude/skills/recipe/genres/readme.md
  .claude/skills/recipe/genres/release-notes.md
  templates/recipe.md
  CLAUDE.md
- links:
  `docs/about/renders-and-recipes.md`: why the recipe is iterated and the render never edited.
  `docs/reference/recipe-genres.md`: each genre's checklist in full.
  `docs/use/render-an-output.md`: generating the render.
- must-not: no checklist reproduced (reference); no Format section detail beyond its existence; not the parenthesis of the release-notes genre that the forge's own recipe reads the intent alone (that recipe reads the solution design's history too).
- made: mirrored
- state: keep

### docs/use/render-an-output.md
- title: Render an output
- kind: how-to
- reader: user
- says: `/render <recipe> [slug]` regenerates a render from its recipe: the inputs read at their current versions from disk, the Markdown generated in an isolated subagent that sees only the recipe and its inputs and is told in its prompt the provenance shape and that nothing of the people who run this forge is material, written to `renders/<recipe>.md` or the recipe's `output:` path, opening with provenance front-matter. Back in the session the written file is scanned mechanically for instance facts (`scripts/docs-check.py --file`): a hit is said aloud and the principal judges it, an instance fact is regenerated out and never edited by hand, a public fixed text of the recipe stands; then the file and its provenance are verified and the ledger's Renders table mirrors it. Where the recipe has a `## Format` section the plain `.docx` or `.pptx` is made beside the render through pandoc and said aloud when pandoc is missing; a published file of the same recipe is marked stale. A render is regenerated only on this command or by `/release`; Claude reports a stale render and offers. A missing recipe is offered through `/recipe`.
- inputs:
  .claude/skills/render/SKILL.md
  scripts/docs-check.py
  CLAUDE.md
- links:
  `docs/reference/render-provenance.md`: the front-matter block and the one definition of stale.
  `docs/use/publish-a-designed-file.md`: the designed file, made through a model.
  `docs/about/renders-and-recipes.md`: why a render is generated and never a source of truth.
- must-not: no subagent prompt text; no provenance block (reference); no script options beyond naming `--file`; nothing of the script's docstring beyond what the one-file scan looks for.
- made: mirrored
- state: keep

### docs/use/publish-a-designed-file.md
- title: Publish a designed file
- kind: how-to
- reader: user
- says: `/publish <recipe> [slug]` makes the designed `.pptx` or `.docx` from the render as it lies on disk, through a model and its document skills, into `published/`: started by the principal only, never by `/render`, `/release` or Claude's own judgement; expensive and minutes long, said in one line before it runs. It never renders: a stale render is named first and the word is the principal's. A recipe without a `## Format` section ends at the Markdown. The ledger's Published table gets a row with state `current`; every later `/render` of that recipe sets it `stale`. It makes a file and sends nothing anywhere.
- inputs:
  .claude/skills/publish/SKILL.md
  CLAUDE.md
- links:
  `docs/use/render-an-output.md`: the Markdown and the plain file that come first.
  `docs/reference/scripts.md`: `md2pptx.py` and `md2docx.py`, the `claude` engine and what it needs.
- must-not: no model name as a recommendation; no script options beyond naming `--engine claude`.
- made: mirrored
- state: keep

### docs/use/generate-the-documentation.md
- title: Generate the documentation
- kind: how-to
- reader: user, extender
- says: `/document [slug]` generates the documentation in one run that asks nothing: bare, the engine's, into `docs/` at the engine root with the map `docs-map.md` beside the ledger of `projects/forge`; with a slug, that project's, into `projects/<slug>/docs/` with the map beside its ledger. What happens, step by step, in the person's terms: a planner agent reads the target on disk and writes the map; a script computes the state of every page from the content of its inputs (new, regenerate, keep, remove) so that only what changed is remade, and writes one task file per page to make; pages that lost their entry are deleted; one writer agent per page is handed its task file by path, reads it first and makes the page from its entry and inputs alone, a mirrored page on a faster model and a derived page on the session model; a script derives the index `docs/README.md` from the map with the intent's version; a script checks every page (present and named by the map, every link resolving, no long dash, a front-matter, no instance fact), a failing page is regenerated once and a page that fails twice is left out and said. What the person gets at the end: the counts, the Unowned list (facts a page needs and no file owns, waiting for him to give them a home), what did not fit, what the writers left out, and a row for the index in the ledger's Renders table. A wrong page is mended in the file that owns the matter and regenerated, never by hand. A release never runs it: it reports the index's age against the intent's version and offers the command.
- inputs:
  .claude/skills/document/SKILL.md
  scripts/docs-state.py
  scripts/docs-index.py
  scripts/docs-check.py
- links:
  `docs/about/the-documentation.md`: what the documentation is, for whom, and why it is generated.
  `docs/extend/change-a-documentation-page.md`: how a page is changed through the file that owns its matter.
  `docs/reference/scripts.md`: the three documentation scripts with their options.
- must-not: no agent prompt or task text; no model name (say "a faster model" and "the session model"); no field of the map (reference); no page count or date of a run; no claim about a project's documentation beyond what the skill says of the places; nothing of the check script's `--file` mode (that is the render's).
- made: mirrored
- state: keep

### docs/use/critique-the-documents.md
- title: Critique the documents
- kind: how-to
- reader: user
- says: `/critique [lens] [artefact] [slug]`: bare, the roster of lenses with a recommended fit; with a lens, one isolated agent reads the project's documents and never the conversation, judges document quality through that lens, never substance, and writes a dated immutable report in `reviews/` with FND findings and ledger rows. The optional target narrows the run to one artefact named as `/forge` names it. What the person sees afterwards: the delta summary (new, verified resolved, still open, obsolete) and the offer of a walkthrough; `accept` means an iteration of the artefact through `/forge`. No lens runs at a save; a release offers `essence` once.
- inputs:
  .claude/skills/critique/SKILL.md
  .claude/skills/critic-contract/SKILL.md
  CLAUDE.md
- links:
  `docs/reference/critic-lenses.md`: the lenses of today and what each goes after.
  `docs/use/walk-through-a-list.md`: settling the findings one by one.
  `docs/about/the-critic.md`: what the critic judges and why it is blind.
- must-not: no report shape (the about and reference pages); no severity or category vocabulary beyond naming that they exist.
- made: mirrored
- state: keep

### docs/use/challenge-the-thinking.md
- title: Challenge the thinking
- kind: how-to
- reader: user
- says: `/challenge [persona] [artefact] [slug]`: bare, the roster of personas with a recommended fit; with a persona, one isolated agent attacks the substance of the thinking, never document quality, and writes a dated immutable report in `challenges/` with three to seven CHL challenges ordered by severity, each falsifiable and with its epistemic status, plus what is strong and the questions it cannot answer from the documents. Best run before the next layer is first derived from the target. What the person sees: the overall read, each challenge compressed, Claude's own disagreement marked as his, the questions answered where the conversation knows them, and the offer of a walkthrough; `accept` means the challenge is mended through `/forge` in the artefact it concerns. A rejected challenge is a healthy outcome.
- inputs:
  .claude/skills/challenge/SKILL.md
  .claude/skills/challenger-contract/SKILL.md
  CLAUDE.md
- links:
  `docs/reference/challenger-personas.md`: the personas of today and what each hunts.
  `docs/use/walk-through-a-list.md`: settling the challenges one by one.
  `docs/about/the-challenger.md`: what the challenger judges and why it may be wrong.
- must-not: no report shape; no persona text.
- made: mirrored
- state: keep

### docs/use/check-conformance.md
- title: Check conformance
- kind: how-to
- reader: user
- says: `/check [check] [slug]`: bare, the roster of checks, each saying when it fits; with a check, one read-only isolated agent verifies mechanical conformance of a project (by slug; the engine's own project is `forge`) or of the engine with the conventions, never substance or quality, and returns its report. The session files it in `reviews/` only when it has findings, gives each new finding its FND, presents the ranked findings, offers every "immediate fix" at once and a walkthrough of the rest; a rule worth changing goes to the intent. Nothing blocks: a release may proceed with a finding parked. Which checks a save and a release run is theirs.
- inputs:
  .claude/skills/check/SKILL.md
  .claude/skills/check-contract/SKILL.md
  CLAUDE.md
- links:
  `docs/reference/checks.md`: the checks of today and what each verifies.
  `docs/use/walk-through-a-list.md`: settling the findings.
  `docs/use/upgrade-the-engine.md`: the checks as the migration tool after an upgrade.
- must-not: no report shape; no Lens text.
- made: mirrored
- state: keep

### docs/use/walk-through-a-list.md
- title: Walk through a list
- kind: how-to
- reader: user
- says: How any list that needs the principal's decision is worked: one item per message, in order of weight; what an item carries (what it says and its evidence, what would change and for whom, the recommendation with the concrete text for accept); the proposition closing with `(a)ccept / (m)odify / (r)eject / (p)ark`, answered with a single letter or the word; `obsolete` as a fifth verdict; a question keeps the item open. The verdicts are carried in the conversation and written once at the round's end on `write`, Claude reflecting the whole round back first; what `reject`, `park` and `obsolete` record, and that `accept` writes what the producing command says. The elicitation interview runs the same way, one question per message.
- inputs:
  .claude/skills/walkthrough/SKILL.md
  CLAUDE.md
- links:
  `docs/reference/verdict-words.md`: the words and letters, exactly.
  `docs/about/working-methods.md`: why the one-item rule exists and how a hook holds it.
- must-not: no hook text; nothing addressed to Claude.
- made: mirrored
- state: keep

### docs/use/save-your-work.md
- title: Save your work
- kind: how-to
- reader: user
- says: `/save [slug] [-m "message"] [--tag name]`: the scope from the status script (the engine and every project repository, each with its branch; a project not under git named and left alone); the `light` check on every repository in scope, its findings settled through `/check`, a save never waiting on a finding the principal has not asked to fix; a one-line commit message drafted from the round's history records and confirmed, or `-m`; a tag only on the principal's word; then the save script, which commits and pushes on whatever branch is checked out, no render, and commits nothing where git resolves no identity. One message per repository when several have changes.
- inputs:
  .claude/skills/save/SKILL.md
  scripts/forge-save.py
  scripts/forge-status.py
  CLAUDE.md
- links:
  `docs/use/release-a-version.md`: the other door, from `main`, with the renders.
  `docs/about/persistence-in-git.md`: why there are two doors and two speeds.
- must-not: no git command; no example message from the forge project; no tag example with a real version; no slug of a project from the script's examples (use `<slug>`; `forge` may stand).
- made: mirrored
- state: keep

### docs/use/release-a-version.md
- title: Release a version
- kind: how-to
- reader: user
- says: `/release [slug] [-m "message"] [--tag name]` releases one repository from `main` only, refusing elsewhere and naming the branch, in the order of its steps: the checks (`light` and `project` for a project; `light`, `engine` and `project` for the engine) launched at once and settled by walkthrough, a finding may be parked; `critique essence` offered once and run only on the principal's word; then the README and the release notes regenerated unconditionally through `/render`, with a summary of what materially changed for the principal to rule on; then the age of the documentation reported, the version in the front-matter of the repository's `docs/README.md` against the intent's version (a repository without `docs/` has none, and that is no finding), and `/document` offered in one sentence, run before the save only on his word, never on its own; then `/save` with the message `release <intent version>: <one line>` and, when the intent's version is an integer, the tag `v<major>` proposed and taken on his word, Claude first naming what the forge's own intent asks a major to pass where the repository is the engine, a reminder and never a gate. The check is advisory: the principal may order the release regardless.
- inputs:
  .claude/skills/release/SKILL.md
  CLAUDE.md
- links:
  `docs/use/save-your-work.md`: the save the release ends with.
  `docs/use/check-conformance.md`: the checks and how their findings are settled.
  `docs/about/renders-and-recipes.md`: why the README and the release notes are renders.
  `docs/use/generate-the-documentation.md`: the command the release offers for the documentation.
  `docs/about/versioning-and-history.md`: what a major approves and what its test attests.
- must-not: no version number of the forge; no description of what a major must pass beyond the pointer the skill makes; no claim that the release regenerates the documentation on its own.
- made: mirrored
- state: keep

### docs/use/work-on-a-branch.md
- title: Work on a branch
- kind: how-to
- reader: user
- says: Branches are voluntary: whoever wants one gets it through `python scripts/forge-branch.py <slug> <branch>`, which switches the repository to the branch, creating it from the current state when it does not exist, `main` switching back; with the slug alone it reports the branch and lists the branches (`forge` means the engine). Unsaved changes stop a switch: save first. Merging, deleting and pushing branches stay with git by hand or by merge request; a new branch reaches the remote by the first save made on it; a release is made from `main` only. Whoever does not want branches works on `main` and never meets this.
- inputs:
  scripts/forge-branch.py
  CLAUDE.md
- links:
  `docs/use/save-your-work.md`: the save that carries a branch to the remote.
  `docs/about/persistence-in-git.md`: why merging is left to git.
- must-not: no git command other than through the script; no example branch name or slug from the script's examples other than `forge` and `main` (use `<slug>` and `<branch>`).
- made: mirrored
- state: keep

### docs/use/upgrade-the-engine.md
- title: Upgrade the engine
- kind: how-to
- reader: user
- says: Upgrading the engine is `python scripts/forge-pull.py`, a fast-forward from the remote (bare: the engine and every project with an origin; `forge` the engine alone; a repository with unsaved changes is skipped or refused, save first). Projects are untouched by it and record no engine version. Then read `RELEASE-NOTES.md`, the Action required lines first; then, project by project, `/check light <slug>` and `/check project <slug>` measure the project against the current conventions and report what no longer conforms; the findings are walked one at a time and Claude migrates on the user's word in the session. There is no migration tool. A project left as it is stays valid under the conventions it was written to.
- inputs:
  scripts/forge-pull.py
  CLAUDE.md
  projects/forge/10-intent.md
  projects/forge/recipes/release-notes.md
- links:
  `docs/use/check-conformance.md`: running a check and settling its findings.
  `docs/use/save-your-work.md`: saving before a pull.
- must-not: no version numbers; no history of past migrations; no repository address; no slug of a project from the script's examples (use `<slug>`; `forge` may stand); nothing of the release-notes recipe beyond its reader and that Action required stands first.
- made: derived
- evidence: `forge-pull.py`'s docstring gives the fast-forward, the bare and slug forms and the refusal on unsaved changes; CLAUDE.md, Persistence calls it the upgrade channel; POS.0940 of the intent states that a project records no engine version, that the migration path is `forge-pull`, then `/check light` and `/check project` per project, the release notes' Action required lines, and Claude migrating on the user's word with no tool; POS.0820 states that an artefact stays valid under the conventions it was written to; the release-notes recipe says the reader is the user who takes upgrades through `forge-pull` and that Action required stands first in every section. The page is the join of these.
- state: keep

### docs/use/spin-off-a-group.md
- title: Spin off a group
- kind: how-to
- reader: user
- says: `/spinoff <project> <group> <slug>` splits a requirement group of an assignment into a project of its own, only on the principal's explicit instruction: the items to move confirmed with him; the new project created by the `/new-project` procedure, files only; a short brief derived from the source intent, presented as a draft and approved on his word; mined into the new intent through `/forge intent`; the moved items marked superseded in the source assignment and replaced by one link item, recorded in its history and as a DEC; both ledgers updated. Claude may propose readiness, never run it.
- inputs:
  .claude/skills/spinoff/SKILL.md
  CLAUDE.md
- links:
  `docs/use/start-a-project.md`: what the new project is made of.
- must-not: no example group or slug from an instance project.
- made: mirrored
- state: keep

### docs/use/look-up-a-command.md
- title: Look up a command
- kind: how-to
- reader: user
- says: `/man [command | method]`, alias `/manual`, is the forge's manual, read at the moment of the call from the files that own it: bare, the commands with their arguments and one-line purposes and the working methods with their first sentences; with a command, its purpose, arguments, the roster it dispatches over with what each entry looks for, and the skill file for the whole procedure; with a method, its paragraph and the skill that holds its shape. It runs nothing and prints in the conversation language. The word `help` is Claude Code's own.
- inputs:
  .claude/skills/man/SKILL.md
  .claude/skills/manual/SKILL.md
  CLAUDE.md
- links:
  `docs/reference/commands.md`: the same table, as a page.
- must-not: no copy of the Commands table.
- made: mirrored
- state: keep

### docs/use/share-material-through-a-library.md
- title: Share material through a library
- kind: how-to
- reader: user
- says: A library is a project of kind `library`, slug prefix `lib-`, with no chain: a ledger, `sources/` and `research/` with their indexes, and a readme recipe whose render is a catalogue of what it holds. It is born by `/new-project lib-<name>`; documents enter by `/ingest` as everywhere, and a changed document is the owner's ordinary maintenance, not a breach. A project uses a library document by citing its path: `/ingest` adds an index entry and a Dependencies row, nothing is copied; a deck template or a Word reference document is named by path in a recipe's Format section. The `/forge` map says which libraries a project needs and whether each is cloned alongside; a missing one is brought in with `/import-project`. The library has its own repository and therefore its own visibility.
- inputs:
  .claude/skills/new-project/SKILL.md
  .claude/skills/ingest/SKILL.md
  .claude/skills/forge/SKILL.md
  .claude/agents/check-light.md
  CLAUDE.md
- links:
  `docs/about/projects-and-the-engine.md`: why a library is a kind of project and what a dependency means.
  `docs/use/register-a-source.md`: the ingest the library shares with every project.
- must-not: no library name of an instance (use `lib-<name>`); no template file name of a company.
- made: derived
- evidence: the library's file set and the `lib-` prefix are CLAUDE.md, Repository layout and Document chain (Renders); what `/new-project` creates for a library is its skill's Library paragraph; a changed library document as maintenance is `/ingest`'s sweep paragraph; citation by path with an index entry and a Dependencies row is `/ingest` step 5; the map's Dependencies line is `/forge` step 3; the missing-library finding with `/import-project` is the `light` check's Dependencies clause; naming a template by path is CLAUDE.md, Document chain, Renders. The page joins them into one procedure.
- state: keep

## about

### docs/about/what-it-is-and-is-not.md
- title: About what the forge is and is not
- kind: explanation
- reader: user, extender, evaluator
- says: What the forge is: a general engine for forging any thought, not bound to one person or one management relationship; the principal is whoever's thinking is forged, the recipients whoever receives the result; Claude is a cognitive extension, an amplifier never a substitute, who proposes and never decides. What it is not: not a program and nothing is implemented in it, the engine specifies; not a delivery tool, a forge run ends where its owner is satisfied, sponsorship and delivery outcomes outside its sight; not a chat, since state lives in files and nothing depends on a conversation's memory; not tied to one domain. Why the name, why "thought" and not "assignment", and why the chain ends where the project needs it to.
- inputs:
  CLAUDE.md
  projects/forge/10-intent.md
- links:
  `docs/about/how-a-thought-travels.md`: the course of one thought through the forge.
  `docs/about/the-principal-and-claude.md`: the two roles and the rule between them.
- must-not: no name of the first principal or author; no company; no history of the project's origin beyond "it began as one person's tool and that origin is an instance fact"; no commands.
- made: derived
- evidence: CLAUDE.md, "What this workspace is" and Roles give the identity and the two roles; the intent's Essence and POS.0005, POS.0010, POS.0070 give the general-engine framing and the amplifier; POS.0780 gives where a run ends and what is outside its sight; POS.0330 gives state in files; POS.0600, POS.0620 and REJ.0130 give the name, the subtitle and what was rejected; REJ.0125 gives the dropped founding framing. The page states each as the intent reasons it.
- state: keep

### docs/about/how-a-thought-travels.md
- title: About how a thought travels
- kind: explanation
- reader: user, extender, evaluator
- says: The course of one thought: it arrives as a brief, the principal's own text, rough on purpose; it is chiselled into the intent by elicitation, positions with their reasons, facts, threads, rejections, rewritten for coherence every round; below the intent the project takes the layers it needs, an assignment to hand over, a solution design of how it is realised, many ending at the intent; at every layer blind reviewers press on the documents and the thinking and every finding ends in a recorded verdict; outputs for every audience are generated from the artefacts through recipes and regenerated when the thinking moves, and the documentation of the project is generated from its documents the same way; everything is saved to git and released with a README and release notes. Sources and research arrive at any stage and are used only as the principal directs. The main courses of events, a round of work, a review, a render, a save and a release, in one sentence each.
- inputs:
  CLAUDE.md
  projects/forge/40-solution-design.md
  projects/forge/10-intent.md
- links:
  `docs/about/the-document-chain.md`: the chain as a star and why files are numbered in tens.
  `docs/about/isolated-reviewers.md`: why the reviewers never see the conversation.
  `docs/about/renders-and-recipes.md`: how an output is generated from the artefacts.
- must-not: no command syntax (commands named in passing only); no forge project detail; no version numbers.
- made: derived
- evidence: CLAUDE.md, Document chain gives the chain and its items, the documentation (item 5) among them; the solution design's "How the parts work together" gives the main courses of events (a round of work, a review, a render, persistence) in its own words; POS.0110, POS.0120, POS.0130, POS.1400, POS.0400, POS.0710, POS.1450, POS.0180 and POS.1100 of the intent give what each station is for. The page tells it in the order a thought meets it.
- state: keep

### docs/about/the-principal-and-claude.md
- title: About the principal and Claude
- kind: explanation
- reader: user, evaluator
- says: The two roles: the principal supplies ideas, answers and decisions and is the final authority on all content; Claude owns structure, order, process discipline and document hygiene, proposes and never decides. The prime directives that follow: when unsure, ask and elicit actively, raising what does not fit as a question and saying in words how sure a claim is; never introduce a convention unilaterally; many iterations are normal; research before inventing; advisory, never blocking; structure over prose; one write per round on confirmation and "written" means a file; one mechanism lives in one place. Why: nothing enters content because Claude proposed it, only because the principal took it up; the rules bind Claude, not the principal, whose recorded exception is the designed form. Authorship is the principal's whether an artefact is found together or handed over.
- inputs:
  CLAUDE.md
  projects/forge/10-intent.md
- links:
  `docs/about/working-methods.md`: the named ways the two work together.
  `docs/about/how-the-rules-are-held.md`: how the harness backs the principal's word.
- must-not: no name or role of an instance's principal; no handle; no directive quoted as an instruction to Claude beyond what it means for the person; no decision record of the forge project cited.
- made: derived
- evidence: CLAUDE.md, Roles and Prime directives give the rules; POS.0005, POS.0010, POS.0020, POS.0030, POS.0040, POS.0050, POS.0070, POS.0190, POS.0200, POS.1370 and POS.1410 give their reasons (POS.0200 the reason for structure over prose: an item with a stable ID can be cited, reviewed, traced and changed one at a time; POS.1370 that certainty is said in words). The page pairs each rule with its reason.
- state: keep

### docs/about/working-methods.md
- title: About the working methods
- kind: explanation
- reader: user, evaluator
- says: The forge's vocabulary of collaboration, none a command, each invoked in a word: Walkthrough, Propose never decide (and `??`), Step by step (a remark or a question in answer to "shall I change it?" is not a yes), Elicitation interview, In pieces, Draft early, Reflect back, One write per round (`write`), Intent-first, Handing over, Recommend do not push, Plain speech, Kind not count. For each, what it is in the operating layer's wording and why it exists in the intent's: the one-item rule because text loaded once dissolves in a long conversation, which is also why a hook repeats it at every prompt; one write per round because writing after every exchange buries the change; step by step because consent is given to a concrete operation and never to its description, a step hard to reverse being seen at the moment it happens and not in a plan read earlier; handing over because the principal's attention is the scarce thing; plain speech because the principal reads the first lines and carries no IDs in his head; kind not count because a numeric limit answers a problem of kind with a rule of amount. Every list that needs a decision ends by offering a walkthrough.
- inputs:
  CLAUDE.md
  .claude/skills/walkthrough/SKILL.md
  projects/forge/10-intent.md
- links:
  `docs/use/walk-through-a-list.md`: the walkthrough as a procedure.
  `docs/reference/verdict-words.md`: the words the principal types.
- must-not: no hook text; no run record or dates of incidents; no name of a project the methods were learnt on; nothing of the assistant's memory.
- made: derived
- evidence: CLAUDE.md, Working methods gives every method's name and wording, Plain speech and Kind not count included; the walkthrough skill gives the shape of an item and the verdicts; POS.0850 to POS.0910, POS.1160, POS.1170, POS.1210, POS.1410, POS.1460 (Step by step, with its reason and the rule that a remark is not a yes), POS.1470 (Plain speech) and POS.1480 (Kind not count) give the reasons. The page keeps CLAUDE.md's order and names.
- state: keep

### docs/about/elicitation.md
- title: About elicitation
- kind: explanation
- reader: user, extender, evaluator
- says: Elicitation is the process by which the principal and Claude find an artefact together and form the knowledge it holds: the conversation is the medium, the interview one instrument, research and sources others. Three things kept apart: the map of what must be found, the process by which it is walked, and the template where the result lands; the map stands before the template because a template can be filled and still miss what the artefact is for. Every kind of artefact has a definition in seven blocks, Target, Inputs, Aim, Partner, Map, Instruments, Course, paired with its template; a Map is a map of what must be found, not a questionnaire, walked at the moments the definition names, an area left empty when considered and found not to apply. What is not elicitation: composing a recipe, `/setup`, a walkthrough of findings. An artefact is found together or handed over; either way authorship is the principal's.
- inputs:
  projects/forge/10-intent.md
  templates/artefact-definition.md
  CLAUDE.md
- links:
  `docs/about/the-document-chain.md`: how the definitions make the chain a star.
  `docs/extend/add-an-artefact.md`: writing a definition of one's own.
- must-not: no block of a particular artefact's definition (each artefact has its page); no brief of the forge project cited by name.
- made: derived
- evidence: POS.1300, POS.1310, POS.1320 and POS.1410 of the intent state what elicitation is, the seven blocks and the Map, and POS.1300 the reason the map stands before the template; `templates/artefact-definition.md` shows the blocks as they stand on disk; CLAUDE.md, Document chain says every artefact has a definition paired with its template and that the definitions are the one list of artefacts. The page explains the shape from these three.
- state: keep

### docs/about/the-document-chain.md
- title: About the document chain
- kind: explanation
- reader: user, extender, evaluator
- says: The chain starts at a brief and its trunk is the intent; below the intent a project takes the layers it needs, none a condition of another, and a layer it does not have is not missing. The chain is a star, not a line: each artefact's definition declares its own inputs, so a layer branches from any artefact by adding one definition, and the dispatcher `/forge <state>` never changes; knowing the artefact's name is knowing the command. Files are numbered in tens so that layers can be added without renaming. Which artefacts exist is the listing of the definitions directory. Where a change goes: substance into the intent first, then down the chain; a change may come from below and then the intent changes first. The chain never spans two principals: an assignment handed to someone else is their own forge run's brief.
- inputs:
  CLAUDE.md
  .claude/skills/forge/SKILL.md
  projects/forge/10-intent.md
- links:
  `docs/about/the-brief.md`: the first artefact.
  `docs/about/the-intent.md`: the trunk.
  `docs/reference/artefacts.md`: the definitions of today, one row each.
- must-not: no list of planned layers as if they existed; no forge project history.
- made: derived
- evidence: CLAUDE.md, "What this workspace is" and Document chain give the trunk, the growth and the numbering; the `/forge` skill says the chain is a star and a layer is a file; POS.0100, POS.0140, POS.0580, POS.0700, POS.0900 and POS.1400 give the reasons. The page is their join.
- state: keep

### docs/about/the-brief.md
- title: About the brief
- kind: explanation
- reader: user, evaluator
- says: A brief is the principal's text of one whole of thinking: what he wants and why, with what he chose to take from the finding around it; free form, no required content, no IDs, a minimal header that carries the version and status like every artefact; rough on purpose because the chiselling is the intent's, and a brief polished until the intent has nothing to do has gone too far. It is not the record of the finding: what stays out lives in research and sources or nowhere. Nothing in it marks authorship; `(source: <path>)` and `(remark: …)` carry something other than authorship. Three origins are equally legitimate. A project may have more than one brief, each later whole born as `00-brief-<name>.md` and mined into the single intent when the principal says so; it is versioned like every artefact, approved on his word, never locked. Kept in whatever language it is written in.
- inputs:
  .claude/skills/forge/states/brief.md
  templates/brief.md
  projects/forge/10-intent.md
- links:
  `docs/use/write-a-brief.md`: composing one.
  `docs/about/the-intent.md`: where the brief is mined.
- must-not: no brief of the forge project named or quoted; no Course steps (the use page); no author field value.
- made: derived
- evidence: the brief's definition (Target, Aim, Partner, Map) gives the wording; `templates/brief.md` gives the header's fields; POS.0110 and POS.0920 give what a brief is, why it is free form and rough, why several briefs, and the marks; REJ.0040, REJ.0180, REJ.0220 give what was rejected; CLAUDE.md, prime directive 6 gives the language exception. The page explains with the intent's reasons.
- state: keep

### docs/about/the-intent.md
- title: About the intent
- kind: explanation
- reader: user, evaluator
- says: The intent is the working document: the consolidated current state of what the principal holds, rewritten for coherence every round, never an append-only log, because chat context dies and anything of value must live in a file. It holds positions with their reasons and provenance, facts on the principal's or a source's word, rejected directions with the reason, and in `threads.md` beside it what is being worked. What a position carries and what belongs in its history instead; why a fact has a prefix of its own; why a thread names the artefact it concerns; the optional staging area for what the layer below will need. An intent says what is wanted and why and does not solve: the test of a sentence is whether it would still hold if the thing were realised wholly differently. It is complete for now when no thread blocks the next layer, never finished.
- inputs:
  .claude/skills/forge/states/intent.md
  templates/intent.md
  templates/threads.md
  projects/forge/10-intent.md
- links:
  `docs/use/forge-the-intent.md`: iterating it.
  `docs/about/versioning-and-history.md`: the history companion a position's past lives in.
  `docs/about/the-solution-design.md`: where the solution goes instead.
- must-not: no position of the forge project quoted as an example; no ID numbering rules beyond naming the prefixes.
- made: derived
- evidence: the intent's definition (Aim, Threads and files) gives the wording; POS.0120 gives what the document is and what a position and a thread carry; POS.0230 gives why FCT and THR exist; POS.1340 and the template's last section give the staging area; POS.1390 gives the intent/solution test; REJ.0010 gives why a Q&A log was rejected. The page pairs each with its reason.
- state: keep

### docs/about/the-assignment.md
- title: About the assignment
- kind: explanation
- reader: user, evaluator
- says: The assignment carries the in-scope substance of the intent to the recipients, complete and precise, so that they can act without the principal in the room and act rightly where the plan no longer fits. Complete means nothing left to assumption: delegated or open on purpose is complete, silent is not; length is whatever fidelity requires. It assigns and does not solve, the boundary being the kind of content never its amount; any apparatus may appear where the principal judges it part of setting direction. Structured items with stable IDs and shall/shall not, no priorities, testability recommended not required, success criteria wanted not compulsory, a Terms section so it can be forwarded without oral tradition; why shall and not the softer verbs or MoSCoW. Why it is found in a joint pass of three phases and not item by item. Why the name "assignment".
- inputs:
  .claude/skills/forge/states/assignment.md
  templates/assignment.md
  projects/forge/10-intent.md
- links:
  `docs/use/distil-an-assignment.md`: the joint pass as a procedure.
  `docs/reference/requirement-style.md`: the rule set.
- must-not: no rule set reproduced; no example item from an instance project; no spin-off mechanics.
- made: derived
- evidence: the assignment's definition (Aim, Map, the joint pass with its two "why not") gives the wording; POS.0130, POS.0200 to POS.0290 and POS.1350 give the reasons (POS.0200 why structure over prose, POS.0250 why shall binds and the softer verbs and MoSCoW do not); REJ.0050, REJ.0060, REJ.0120 give what was rejected. The page states each as the intent reasons it.
- state: keep

### docs/about/the-solution-design.md
- title: About the solution design
- kind: explanation
- reader: user, extender, evaluator
- says: The solution design says how the things wanted are realised, as the solution stands today, kept current and read by whoever realises it without the principal in the room. It is derived from the lowest layer above it, the intent alone, the assignment or a BRD; worth writing where the way is not obvious, a choice has a price, or two hands would solve it differently; whether it is, the principal says. It holds what cannot be read off the thing itself, why, against what, at what price and how the parts fit; it cites the layer above by ID and names what realises a part by path, copying neither. The shape of a SOL item: what the part is and answers for, Realises, Choice, Where; a TBC with its owner, what would close it and whether it blocks. From the artefacts the thing must be buildable without the finished product; a technical specification is a layer below where the builder needs the detail.
- inputs:
  .claude/skills/forge/states/solution-design.md
  templates/solution-design.md
  projects/forge/10-intent.md
- links:
  `docs/use/design-the-solution.md`: iterating it.
  `docs/about/the-intent.md`: the layer whose "what" this answers.
- must-not: no item of the forge's own solution design quoted; no check named that does not exist.
- made: derived
- evidence: the solution design's definition (Aim, Partner, Map, the shape of an item) gives the wording; POS.1390, POS.1400, POS.1420 give the reasons and the place in the chain. The page explains from these.
- state: keep

### docs/about/documents-and-records.md
- title: About documents and records
- kind: explanation
- reader: user, extender, evaluator
- says: "Document" is every file of a project; "artefact" is reserved for the documents of the chain. Every document has one kind, in five groups: artefacts (versioned, rewritten freely), records (history and decisions append-only; reviews and challenges immutable), state (the ledger, the resource indexes and the documentation map, freely rewritten), rendering (recipes versioned and never approved, renders overwritten, the pages of the documentation overwritten by the documentation run), resources (sources and research, immutable). Why state lives in files and never in conversation: a session can end at any point without loss. The ledger as the single source of truth for state, kept current after every operation, citing and never copying. Why immutability is a process rule and not a git mechanism; why corrections happen downstream. Prose hard-wrapped at about 72 columns so that diffs stay legible.
- inputs:
  CLAUDE.md
  templates/ledger.md
  templates/decisions.md
  projects/forge/10-intent.md
- links:
  `docs/reference/document-kinds.md`: the table of kinds, verbatim.
  `docs/reference/ledger.md`: the ledger's tables and states.
  `docs/about/versioning-and-history.md`: the history companion of every versioned kind.
  `docs/about/the-documentation.md`: the map and the pages, the two generated kinds.
- must-not: no table reproduced (reference); no forge project ledger content.
- made: derived
- evidence: CLAUDE.md, Document kinds and Ledger give the groups, the kinds (map and page among them) and the ledger's role; the ledger and decisions templates show the shapes; POS.1080, POS.0160, POS.0320, POS.0330 and POS.0550 (why immutability is a process rule: git protects nothing from a commit that rewrites a file, the rule costs nothing, a mechanism would still not stop a hand edit) give the reasons. The page explains, the reference page mirrors.
- state: keep

### docs/about/versioning-and-history.md
- title: About versioning and history
- kind: explanation
- reader: user, extender, evaluator
- says: Integers denote signed-off versions, drafts 0.x, changes after approval 1.1 and on, the next approval 2.0; status must agree with the number; a recipe stays 0.x for life because it is never approved. What a major of an intent is: it closes a package the principal names, approves the intent as the record of what he holds at that date, signs nothing over (what is open stays open in its thread), and before its tag passes a test that attests the documents conform to the conventions and to each other and that the thinking has been challenged, nothing of how the model behaves. Every versioned document keeps its history in an append-only companion beside it, never in its body: the body is the current state, the companion the record, a log of one record per change with the reason, what the user must do (Action) and the wording that ceased to hold (Was), word for word. Why: the way to an item does not belong in the item; the log is the single primary from which commit messages and release notes derive; a history is searched, never loaded whole. A companion written before the log moves to an archive, immutable. The author of a record is the one who decided the change.
- inputs:
  CLAUDE.md
  templates/history.md
  projects/forge/10-intent.md
- links:
  `docs/reference/versioning-and-front-matter.md`: the fields and the scheme, exactly.
  `docs/reference/history-companion.md`: the record's shape.
  `docs/use/release-a-version.md`: where the tag of a major is proposed.
- must-not: no example record from the forge project; no research note cited; no version number of the forge; no list of the checks a major of the forge ran.
- made: derived
- evidence: CLAUDE.md, Versioning & status gives the scheme and the companion rule; `templates/history.md` gives the record; POS.0300 gives what a major closes, approves and attests and what its test does not attest; POS.0310 and POS.0730 give the reasons (the single primary, derivations, the archive); REJ.0110 gives the rejected scheme. The page pairs rule and reason.
- state: keep

### docs/about/stable-ids.md
- title: About stable IDs
- kind: explanation
- reader: user, extender, evaluator
- says: Every item carries an ID `PREFIX.NNNN`, three-letter prefix, numbered in tens with each group starting at the next hundred, global and stable, never renumbered; items move between groups without a change of ID; groups are plain headings with no ID and no lifecycle. Why structure over prose even at high abstraction: an item with a stable ID can be cited, reviewed, traced into the layer below and changed one at a time, where prose cannot be pointed at. Why a fact, a position and a thread have prefixes of their own; why a thread carries its origin. The prefix vocabulary is a house convention aligned with a BRD standard where one exists.
- inputs:
  CLAUDE.md
  projects/forge/10-intent.md
- links:
  `docs/reference/id-scheme.md`: the prefix table and the numbering rules, exactly.
- must-not: no table (reference); no example ID from an instance project; no group name of a company standard.
- made: derived
- evidence: CLAUDE.md, ID scheme gives the rules; POS.0200 (with its reason), POS.0220, POS.0230 give the reasons; REJ.0020 and REJ.0100 give what was rejected.
- state: keep

### docs/about/isolated-reviewers.md
- title: About the isolated reviewers
- kind: explanation
- reader: user, extender, evaluator
- says: Three kinds of reviewer of one shape: the critic (document quality, lenses, FND), the challenger (substance, personas, CHL), the check (mechanical conformance, checks, FND). All run as isolated subagents that see the project's documents and never the working conversation, on the session model; their blindness is the source of their value: they cannot be told what was meant. All are invoked by hand, settled by walkthrough, their reports immutable and dated; nothing blocks, every finding is fixed or rejected with a recorded reason. The shared behaviour of each kind is one contract, the agent file owns only its Lens; a lens narrows, never replaces. Isolation is not independence: the reviewers share the author's model family and their agreement is never validation. Instance facts never enter a report.
- inputs:
  CLAUDE.md
  projects/forge/10-intent.md
- links:
  `docs/about/the-critic.md`: what the critic judges.
  `docs/about/the-challenger.md`: what the challenger judges.
  `docs/about/the-check.md`: what a check verifies.
  `docs/use/walk-through-a-list.md`: how findings are settled.
- must-not: no roster (reference); no contract text; no planned challengers on another model family presented as built; the documentation agents are not reviewers and are not counted here.
- made: derived
- evidence: CLAUDE.md, Isolated reviewers gives the mechanism; POS.0400, POS.0430, POS.0440, POS.0450, POS.0540, POS.0790, POS.1120 give the reasons; REJ.0080 gives why review and challenge are two reviewers. The page explains from these.
- state: keep

### docs/about/the-critic.md
- title: About the critic
- kind: explanation
- reader: user, extender, evaluator
- says: The critic judges the quality of the artefacts as documents, read through a lens, never the substance of the thinking; two lenses because one critic hunted formalities and never guarded the chain: `clarity` reads each artefact on its own, `essence` distils every adjacent pair blind and compares, a finding being a difference of essences, not of texts. How it works: regression first on its own earlier findings, respect for rejected ones, sharp and few, each artefact judged against its own definition and the principal's deliberate omissions never reported as defects, testability a recommendation. What it produces: a dated report in `reviews/` with FND findings carrying severity and category, a delta summary and recommendations, and ledger rows. A target narrows a lens to one artefact or one pair.
- inputs:
  .claude/skills/critic-contract/SKILL.md
  CLAUDE.md
  projects/forge/10-intent.md
- links:
  `docs/use/critique-the-documents.md`: running a lens.
  `docs/reference/critic-lenses.md`: the lenses and their angles.
- must-not: no report template reproduced; no instruction to the agent copied as such; no finding of the forge project.
- made: derived
- evidence: the critic contract gives subject, way of working and output; CLAUDE.md, Isolated reviewers gives the critic's place; POS.0400, POS.0410 and POS.0270 give why two lenses and why testability is a recommendation. The page explains from these.
- state: keep

### docs/about/the-challenger.md
- title: About the challenger
- kind: explanation
- reader: user, extender, evaluator
- says: The challenger attacks the substance of the thinking through a persona with a register and blind spots of its own, as an equal with no stake in the principal being right, never document quality. How it works: reads for what is not there, grounds itself externally where a claim hinges on the world, never fabricates and flags what it reconstructs, three to seven challenges ordered by severity, each with what would change its mind and an epistemic status, never proposing document edits; it may be wrong and says what it assumes. What it produces: a dated report in `challenges/` with CHL challenges, what is strong and the questions it cannot answer from the documents, and ledger rows. Why it is best run before the next layer is derived; why a rejected challenge is healthy; why an accepted one is mended where it needs to be and goes above its layer only as a thread.
- inputs:
  .claude/skills/challenger-contract/SKILL.md
  CLAUDE.md
  projects/forge/10-intent.md
- links:
  `docs/use/challenge-the-thinking.md`: running a persona.
  `docs/reference/challenger-personas.md`: the personas and what each hunts.
- must-not: no report template; no challenge of the forge project; no persona text.
- made: derived
- evidence: the challenger contract gives subject, way of working and output; POS.0420, POS.0440, POS.0450, POS.0790 give the reasons; CLAUDE.md, Isolated reviewers gives the place. The page explains from these.
- state: keep

### docs/about/the-check.md
- title: About the check
- kind: explanation
- reader: user, extender, evaluator
- says: A check verifies mechanical conformance with the current conventions, never substance or quality, each check owning one concern and none another's; it reads the rules at their owners and never restates them. Read-only: it returns its report and the session files it, so that the IDs of a project's findings are given in one place and a check every save runs has no right to write into the project at every save. Findings only, precise to file and line, ranked by severity; what conforms is not reported; a fact the Lens names is reported once as a fact; a finding decided once by a DEC is not raised again; a known finding keeps its ID. Advisory: nothing blocks. Composition is the caller's: `/save` runs `light`, `/release` runs `light` and `project`, for the engine `engine` too; the rest on the principal's word. Why a check's findings are filed like a critic's and why a run that finds nothing files nothing.
- inputs:
  .claude/skills/check-contract/SKILL.md
  CLAUDE.md
  projects/forge/10-intent.md
- links:
  `docs/use/check-conformance.md`: running a check.
  `docs/reference/checks.md`: the checks and what each verifies.
- must-not: no report template; no Lens text; no finding of the forge project.
- made: derived
- evidence: the check contract gives subject, way of working and output; CLAUDE.md, Isolated reviewers and Persistence give the composition; POS.0540, POS.0570, POS.1140 give the reasons, POS.1140 among them why the session and not the agent files the report (the IDs given in one place; a check every save runs would otherwise write into the project at every save). The page explains from these.
- state: keep

### docs/about/renders-and-recipes.md
- title: About renders and recipes
- kind: explanation
- reader: user, extender, evaluator
- says: A render is an audience-specific output generated from the chain and never a source of truth; what is iterated is its recipe, inputs, audience, instructions and the literal output template in one versioned file; a render is never edited by hand. The boundary between chain and render is authorship: composed by the principal, a layer; generated from artefacts, a render. Every render opens with provenance and is stale when a cited version differs; a render is regenerated only on the principal's word or by a release, because regeneration is stochastic and an unreviewed regeneration is an unreviewed edit, which is why a recipe pins load-bearing wording, a release reports the delta and a written render is scanned for instance facts before it is kept. Everything is Markdown; an output is made in two steps divided by cost, the plain file with the render through pandoc, the designed file by `/publish` through a model. Every project's README and release notes are renders of its own recipes, regenerated at every release; what a README carries is the readme skeleton's, what the thing is, what one gets, how to start, where it stands and where the documentation is; recipes may be composed by genre. A render may be an input of another. A page of the documentation is not a render: no recipe stands behind it.
- inputs:
  CLAUDE.md
  templates/recipe.md
  templates/recipe-readme.md
  projects/forge/10-intent.md
- links:
  `docs/use/compose-a-recipe.md`: composing a recipe.
  `docs/use/render-an-output.md`: generating a render.
  `docs/use/publish-a-designed-file.md`: the designed file.
  `docs/reference/render-provenance.md`: the provenance block and the definition of stale.
  `docs/about/the-documentation.md`: the pages, generated without a recipe.
- must-not: no recipe of the forge project quoted; no author line; no pitch content; no script options; not the fixed closing sentence of the readme skeleton (it carries an address, which is the install page's alone).
- made: derived
- evidence: CLAUDE.md, Document chain (Renders) gives the mechanism and names the readme skeleton as the owner of what a README carries; the recipe skeleton gives the sections; the readme skeleton's Instructions say what a README carries; POS.0710, POS.0720, POS.0730, POS.0590, POS.0770, POS.0810, POS.0950 (the scan of generated files), POS.1000 give the reasons; REJ.0160 gives what was rejected; POS.1450 and REJ.0240 give why a page is not a render. The page explains from these.
- state: keep

### docs/about/the-documentation.md
- title: About the documentation
- kind: explanation
- reader: user, extender, evaluator
- says: The documentation of a project, the engine's among them, is a set of pages of one topic each in `docs/`, readable where the project is published and in a clone, with an index that lists every page and names each reader's path. Three readers in order of weight: the user who clones the thing and works with it, the extender who adds to it, the evaluator who never runs it and gets the concept pages and nothing made for him alone. Five sections by the reader's journey, the same for every project and filled only where the project has material: start, use, about, extend, reference; each page of one kind, how-to, explanation or reference, standing on its own. The documentation is generated and never composed by hand: a page either mirrors the files that own its topic or is derived from named evidence, and says which, so that a page cannot drift from what it mirrors; the map it is made from (kind `map`) lies beside the owning project's ledger and is never shown to the reader, the pages and the index (kind `page`) are what he reads. Two agents make it, a planner that writes the map and a writer per page, sharing one contract as the reviewers do: they see nothing of the conversation, read every input from disk, and keep every name, host, account, address but the public home, chain ID and long dash off a page. A run regenerates only pages whose inputs changed, decided from the content of the inputs, never by judgement; a release does not regenerate it but reports the index's age and offers the command. Why: the README was the whole documentation and poor as one, three things at once; why not a recipe per page, a site or a wiki, or a hand-kept file of the philosophy. The README is cut to what orients and points, its chapters the readme skeleton's.
- inputs:
  CLAUDE.md
  .claude/skills/document/SKILL.md
  .claude/skills/docs-contract/SKILL.md
  .claude/agents/docs-planner.md
  .claude/agents/docs-writer.md
  projects/forge/10-intent.md
  projects/forge/40-solution-design.md
- links:
  `docs/use/generate-the-documentation.md`: running `/document`.
  `docs/extend/change-a-documentation-page.md`: changing a page through its owners.
  `docs/reference/documentation-map.md`: the map's entry and the page's front-matter, field by field.
  `docs/about/renders-and-recipes.md`: the renders, which the pages are not.
- must-not: no count of pages or date of a run (the intent and the solution design carry both; the page carries neither); no model name; no entry of the map quoted; no instance fact; no name of a project other than `forge`; nothing of the contract copied as an instruction to Claude.
- made: derived
- evidence: CLAUDE.md, Document kinds (the rows `map` and `page`) and Document chain, item 5, give what the documentation is, where the map lies, that a release reports the index's age and that the readme skeleton owns what a README carries; the `/document` skill gives the one run and its places; the docs contract gives what the two agents share, isolation, inputs from disk and what must never reach a page; the planner agent gives the three readers, the outline and the mirrored/derived distinction in the words the documentation is planned by, the writer agent the page's shape and that a page stands alone; POS.1450 gives the position whole with its reason, POS.0930 why a mirrored page runs on a faster model, POS.0950 why no instance fact reaches a page and why generated files are scanned; REJ.0240, REJ.0250, REJ.0260 give what was rejected (a recipe per page, a site or a wiki, a hand-kept philosophy); SOL.0460 gives the choices and what each was chosen against (the index named `README.md`, the map beside the ledger, the pinned facts in the readme recipe) and says the whole is built and run with the contract and the map's skeleton. The page explains from these.
- state: keep

### docs/about/sources-and-research.md
- title: About sources and research
- kind: explanation
- reader: user, evaluator
- says: External inputs live in `sources/`, immutable once registered, one form each (text or a functional binary, an extract made by one script never by ad-hoc parsing), arriving at any stage; a related set is a bundle, one source with its own catalogue. Registration is not intake: what a source is for is the principal's word, recorded as its Role in the resource index, and source content enters the intent only by his explicit act with provenance; what someone said in a meeting is never silently his position. Research is a durable answer to one question, immutable and dated, because the principal does not want to reinvent what the world has solved. Every `sources/` and `research/` directory carries an index so that what exists is known without re-reading; the index tracks nothing and is an automatic input of no command, so a contradiction between the intent and a source is not a finding. Why personal matter stops an ingest before the store: a source is immutable from its registration and travels into git, so what has entered cannot be taken back.
- inputs:
  CLAUDE.md
  templates/index.md
  templates/index-bundle.md
  projects/forge/10-intent.md
- links:
  `docs/use/register-a-source.md`: the ingest procedure.
  `docs/use/research-a-topic.md`: the research procedure.
- must-not: no example source of the forge project; no index entry reproduced.
- made: derived
- evidence: CLAUDE.md, Document chain (External inputs, Resource indexes) gives the rules; the index skeletons give the fields; POS.0050, POS.0180, POS.0840, POS.1040 (with the reason personal matter stops the command before the store) give the reasons. The page explains from these.
- state: keep

### docs/about/projects-and-the-engine.md
- title: About projects and the engine
- kind: explanation
- reader: user, extender, evaluator
- says: The engine is one public repository, the core together with its own project `projects/forge`; every other project is a repository of its own under a gitignored `projects/`, which the engine does not know, recognised by the scripts through its `.git`; a project may have any remote and visibility, or none. Why: publication of the engine with nothing sensitive and no instance facts, access per project, seamless work inside. A project has a kind, thought or library, declared in its ledger header; a library is shared material with no chain, cited by path from other projects as a dependency taken knowingly. Instance facts live in `CLAUDE.local.md` at the engine root, never in the engine; the forge's behaviour lives in the engine, never in the assistant's memory. A project records no engine version: the upgrade is a fast-forward of the engine and the checks measure a project against the current conventions. The shapes rejected: submodules, subtree, a template repository, copying the engine into projects.
- inputs:
  CLAUDE.md
  projects/forge/10-intent.md
  projects/forge/40-solution-design.md
- links:
  `docs/use/share-material-through-a-library.md`: using a library.
  `docs/use/upgrade-the-engine.md`: the upgrade and the migration path.
  `docs/reference/repository-layout.md`: the layout, file by file.
- must-not: no host, no company, no name of a project other than `forge`; no repository address (the install page carries it); no history of the split as a story.
- made: derived
- evidence: CLAUDE.md, Repository layout and Persistence give the shape; POS.0760, POS.0940, POS.0950, POS.0960, POS.0970, POS.0980, POS.1020, POS.1030 give the reasons; REJ.0140, REJ.0150 give what was rejected; SOL.0500 gives the gitignore pattern and why it must be `projects/*`. The page explains from these.
- state: keep

### docs/about/persistence-in-git.md
- title: About persistence in git
- kind: explanation
- reader: user, extender, evaluator
- says: The scripts in `scripts/` are the only door to git, reading state included, for Claude a wall of the harness and not conduct alone; the principal's own git from the shell is his. Two doors, two speeds: `/save` with the light check, commit and push on any branch, seconds; `/release` from `main` only, with its checks, the README and release notes, the release message and the major's tag, because the renders cost minutes and a README on `main` is then current at every release and stale in between visibly. `main` is the released line, branches voluntary and left to git, merging never the forge's, because the principal does not want a wrapper of git. The commit identity is git's, resolved per host from the user's own configuration, the forge setting none, with a guard so that a missing identity fails aloud; a commit carries no attribution trailer. Immutability is a process rule, not a git mechanism: git protects nothing from a commit that rewrites a file, the rule costs nothing, and a mechanism would be one more layer that still would not stop a hand edit. The scripts are Python, `python` on PATH their one prerequisite, written to run unchanged on Linux and macOS as a writing rule, not yet a verified claim.
- inputs:
  CLAUDE.md
  projects/forge/10-intent.md
- links:
  `docs/use/save-your-work.md`: the save.
  `docs/use/release-a-version.md`: the release.
  `docs/use/work-on-a-branch.md`: branches.
  `docs/reference/scripts.md`: the scripts themselves.
- must-not: no host, no identity example, no incident story; no git command; no mention of PowerShell.
- made: derived
- evidence: CLAUDE.md, Persistence gives the rules, Portability among them; POS.0550 (with its reason why immutability stays a process rule), POS.0830, POS.0950, POS.1050, POS.1100, POS.1110, POS.1200 give the reasons; REJ.0160, REJ.0170 give what was rejected. The page explains from these.
- state: keep

### docs/about/how-the-rules-are-held.md
- title: About how the rules are held
- kind: explanation
- reader: extender, evaluator
- says: How the forge keeps its rules in force: one always-on core, `CLAUDE.md`, loaded into every session and subagent, carrying only what must hold everywhere; everything else a file read when its situation arises, a command, a definition, a contract, a template. One mechanism lives in one place and is cited by path everywhere else, because two copies drift. A rule that must hold through a long conversation is repeated at every prompt by a hook, since text loaded once dissolves; what the hook prints. The harness enforces what it can: deny rules keep Claude from raw git and sensitive paths, commands that write are guarded against being started on Claude's own judgement, maps and rosters stay his to propose. A subagent may take the session's copy of a file for the file on disk, so every agent that writes an outward-facing file reads its inputs from disk and says that instance facts are not material, and generated files, renders and pages alike, are scanned mechanically before they are kept. One model for the whole forge, chosen once as the session model. The forge's behaviour never lives in the assistant's memory. The forge explains itself from its own definitions through `/man`.
- inputs:
  CLAUDE.md
  .claude/settings.json
  scripts/hook-walkthrough.py
  projects/forge/10-intent.md
  projects/forge/40-solution-design.md
- links:
  `docs/extend/what-it-is-made-of.md`: the files of the operating layer.
  `docs/reference/configuration.md`: the settings, exactly.
- must-not: no claim that a hook or a deny rule guarantees behaviour (the intent says a hook is context, not enforcement); no incident story or date; no thread of the forge project; nothing of the hook's docstring beyond what it prints.
- made: derived
- evidence: CLAUDE.md, prime directive 10 and Working methods (Walkthrough) give the one-place rule and the hook; `.claude/settings.json` shows the deny rules and the hook started by `python`; the hook script's `LINES` show what it prints, its docstring that it runs at every prompt; POS.0930, POS.0950 (the subagent's copy, the scan of generated files), POS.1030, POS.1070, POS.1090, POS.1170, POS.1190, POS.1200 give the reasons; SOL.0010, SOL.0030, SOL.0110, SOL.0520, SOL.0600 say how each is realised. The page explains from these.
- state: keep

### docs/about/languages.md
- title: About languages
- kind: explanation
- reader: user, evaluator
- says: The forge dictates one output language per project: the artefacts of the chain are written in the language the ledger header declares, English when absent; records, state, research and recipes are always English because Claude, the reviewers and the checks read every project the same way; English is the notation throughout; the briefs are the one exception, kept as written; a render may be in any language its recipe declares, a translation being a render; the documentation is English only, a translation a render. The conversation language is an instance fact set in `CLAUDE.local.md`, never a property of the system and never shown outward. Translate on write.
- inputs:
  CLAUDE.md
  projects/forge/10-intent.md
- links:
  `docs/start/setup.md`: where the conversation language is set.
- must-not: no language value of an instance; no example project.
- made: derived
- evidence: CLAUDE.md, prime directive 6 gives the rule; POS.0060 gives the reason; POS.1450 gives the documentation's language. One topic, two sources.
- state: keep

### docs/about/where-it-is-going.md
- title: About where the forge is going
- kind: explanation
- reader: user, extender, evaluator
- says: The direction without a destination: the chain is to be extended downward as far as the principal needs a thought taken, a BRD layer certain, solution architecture and integration intended, a strategy layer possible; nothing is approved for construction and the mechanics of a layer are designed when it is taken up. A new kind of artefact is added by one command; a user is to be able to add one of his own kept at his own place, which is open. Independent challengers on a different model family are planned, the mechanics undecided. Multi-principal use is one principal per instance for now. The forge is developed at its owner's discretion and pace; direction is named, destinations and deadlines are not. Feedback and ideas from those who use it are wanted most.
- inputs:
  projects/forge/10-intent.md
- links:
  `docs/about/the-document-chain.md`: how a layer is added.
  `docs/extend/how-a-change-is-made.md`: how a change reaches the forge.
- must-not: no thread enumerated or quoted; no date; no version; no company rollout; no name.
- made: derived
- evidence: POS.0700, POS.0780, POS.0800, POS.1110 (one user per instance), POS.1430, POS.1440 of the intent; only positions, since threads change with every round. The page states direction as the positions state it.
- state: keep

## extend

### docs/extend/what-it-is-made-of.md
- title: About what the forge is made of
- kind: how-to
- reader: extender
- says: The operating layer, file by file and what each kind is for: `CLAUDE.md`, the always-on core; `.claude/skills/<name>/SKILL.md`, one per command, with the `/forge` state files and the `/recipe` genre files as supporting files, and the skills that are not commands, the three reviewer contracts, the contract of the documentation agents and the walkthrough skill; `.claude/agents/`, one file per lens, persona and check, front-matter and Lens only, and the two agents of the documentation, the planner and the writer; `.claude/settings.json`, the deny rules and the hook; `templates/`, the skeletons, among them one `<type>-definition.md` per type the forge is extended by and the skeleton of the documentation map; `scripts/`, the only platform-bound layer, Python, with the shared modules beside the scripts; `projects/forge`, the forge's own project where its intent, solution design, documentation map and the recipes of its README and release notes live; `docs/`, the generated documentation. The four ideas that carry it: one always-on core and the rest on demand, state in files, isolation by subagents, deterministic work in scripts. Where to read what a thing does: its own file, never a second description.
- inputs:
  CLAUDE.md
  projects/forge/40-solution-design.md
- links:
  `docs/reference/repository-layout.md`: the layout block.
  `docs/about/how-the-rules-are-held.md`: why the core is small and the rest on demand.
  `docs/extend/how-a-change-is-made.md`: changing any of it.
  `docs/about/the-documentation.md`: what `docs/` and the map are.
- must-not: no listing of individual commands or agents (reference); no file of an instance; no repository address; no count of pages or date of a run.
- made: derived
- evidence: CLAUDE.md, Repository layout and Templates give the directories, the scripts by name (the documentation scripts and `docs_map` among them), the contracts of the reviewers and of the documentation agents, `docs/` and the `<type>-definition.md` rule; CLAUDE.md, Persistence (Portability) gives the shared modules; the solution design's "How the parts work together" gives the four ideas and SOL.0010, SOL.0100, SOL.0120, SOL.0130, SOL.0300, SOL.0330, SOL.0460 (the contract `docs-contract` and the skeleton `templates/docs-map.md`), SOL.0500, SOL.0510, SOL.0610, SOL.0620 give what each kind of file is. The page joins them into one tour.
- state: keep

### docs/extend/how-a-change-is-made.md
- title: Make a change to the forge
- kind: how-to
- reader: extender
- says: A change of how the forge behaves goes through the chain before it is built: a position in the forge intent saying what is wanted and why, through `/forge intent forge`, with its history record; the item of the solution design where the change solves something, through `/forge solution-design forge`; then the operating layer, and where the operating layer and the intent differ that is a finding. It is proved by `/check engine`, which verifies the core against itself and against the intent, and before a major or after a round on the operating layer by `/check single-source-of-truth`, which verifies that every rule has one owner; recorded in the history companions (a change touching no item under the subject `operating layer`), released by `/release forge`, which re-renders the README and release notes and reports the age of the documentation's index, offering `/document`; the documentation is regenerated by `/document`, which remakes only the pages whose inputs changed; a process change is complete only once the intent is updated and the README re-rendered. A change that alters no behaviour, a wording or a broken path, is made directly. The README, the release notes and CONTRIBUTING are renders: a change goes into their recipes in `projects/forge/recipes/`. A visitor's way to send feedback, an idea or a change is `CONTRIBUTING.md` in the root, which names a discussion for feedback and an idea and an issue for a defect.
- inputs:
  CLAUDE.md
  projects/forge/10-intent.md
  .claude/agents/check-engine.md
  .claude/agents/check-single-source-of-truth.md
  .claude/skills/release/SKILL.md
  .claude/skills/document/SKILL.md
  projects/forge/recipes/contributing.md
- links:
  `docs/use/forge-the-intent.md`: iterating an intent.
  `docs/use/check-conformance.md`: running the checks.
  `docs/use/release-a-version.md`: the release.
  `docs/use/generate-the-documentation.md`: regenerating the pages.
- must-not: no channel URL, no account, no profile, no name (CONTRIBUTING.md is named as a file, the channels by kind only); no pull-request mechanics beyond what the recipe gives; no claim that the release regenerates the documentation on its own.
- made: derived
- evidence: CLAUDE.md, "The system's own project" gives the completeness rule; POS.0720, POS.0900, POS.1440 give intent-first for the forge and the open rule; the contributing recipe gives the line between the two kinds of change, the three channels by kind and what a pull request carries; the two check agents give what proves a change; the release skill gives what a release re-renders, that it reports the index's age and offers `/document` (its step 5), and that `single-source-of-truth` is not run by it; the `/document` skill and CLAUDE.md, Document chain, item 5 give that a run regenerates only what changed; CLAUDE.md, Versioning & status gives the `operating layer` subject (also POS.0310). The page joins them into the order of one change.
- state: keep

### docs/extend/add-an-artefact.md
- title: Add an artefact
- kind: how-to
- reader: extender
- says: A new kind of artefact is added by `/new-artefact <name>`, which leads to everything a kind needs and decides nothing: a position in the forge intent first; the definition `.claude/skills/forge/states/<name>.md` in the seven blocks from `templates/artefact-definition.md` and its template `templates/<name>.md`, which has no skeleton; the row of a new prefix in the ID scheme; the reviewers, a persona where decided and the calibration of the critic's contract; the item of the solution design; `/check engine` offered at the end. The Map of what is found: what the artefact is and for whom, where it stands and its number, its boundary, its items and prefixes, its reviewers, how it reaches a reader. The rosters need nothing: `/forge`, `/man` and the README read the definitions from disk. The first artefact of the kind is made through `/forge <name>` on real work; that is the trial. A kind that exists is changed through the intent.
- inputs:
  .claude/skills/new-artefact/SKILL.md
  templates/artefact-definition.md
  CLAUDE.md
  projects/forge/10-intent.md
- links:
  `docs/about/elicitation.md`: the seven blocks and the Map.
  `docs/extend/add-a-challenger-persona.md`: the persona a kind may need.
  `docs/extend/how-a-change-is-made.md`: proving and releasing the change.
- must-not: no planned artefact named as if being added; no brief of the forge project.
- made: mirrored
- state: keep

### docs/extend/add-a-critic-lens.md
- title: Add a critic lens
- kind: how-to
- reader: extender
- says: A lens is one agent file `.claude/agents/critic-<lens>.md` from `templates/critic-definition.md`: front-matter (name, description in one line saying what it reads and when it fits, tools, `model: inherit`, `skills: critic-contract`) and a Lens section with four parts, what it reads and how a target narrows it, what it goes after, its categories, its own report sections. Nothing the contract owns is restated; a lens may narrow or make a shared rule stricter, never rename, drop or duplicate one. The description is the roster line of bare `/critique` and `/man critique`. A description carrying a colon followed by a space is quoted whole or the agent does not register. Only by the principal's decision and only where what it finds genuinely differs. Proof: `/check engine` verifies the contract skill exists; a run on a project.
- inputs:
  templates/critic-definition.md
  .claude/skills/critic-contract/SKILL.md
  .claude/skills/critique/SKILL.md
  CLAUDE.md
- links:
  `docs/about/the-critic.md`: what the contract owns.
  `docs/reference/critic-lenses.md`: the lenses that exist, as models of the shape.
- must-not: no contract text copied; no existing lens's angles copied as content.
- made: mirrored
- state: keep

### docs/extend/add-a-challenger-persona.md
- title: Add a challenger persona
- kind: how-to
- reader: extender
- says: A persona is one agent file `.claude/agents/challenger-<persona>.md` from `templates/challenger-definition.md`: front-matter (name, description in one line saying who this is, tools including web search, `model: inherit`, `skills: challenger-contract`) and a Lens section in two parts, who the persona is, a role of its own reviewing as an equal with no stake in the principal being right, and what it goes after, the blind spots as concrete angles. Nothing of the contract restated. Only by the principal's decision and only where its blind spots genuinely differ: personas that would say the same in different words are noise. A persona costs one file and no edits: the roster is scanned. Proof: `/check engine`; a run on a target.
- inputs:
  templates/challenger-definition.md
  .claude/skills/challenger-contract/SKILL.md
  .claude/skills/challenge/SKILL.md
  CLAUDE.md
- links:
  `docs/about/the-challenger.md`: what the contract owns.
  `docs/reference/challenger-personas.md`: the personas that exist.
- must-not: no contract text copied; no existing persona's angles copied as content.
- made: mirrored
- state: keep

### docs/extend/add-a-check.md
- title: Add a check
- kind: how-to
- reader: extender
- says: A check is one agent file `.claude/agents/check-<name>.md` from `templates/check-definition.md`: front-matter (name, description saying what it verifies and when it fits, read-only tools, `model: inherit`, `skills: check-contract`) and a Lens section in three parts, what it reads and how the target narrows it, what it verifies with the owner of each rule cited and never restated and what is a fact rather than a finding, and its cost, honestly. One concern per check and none another's. It writes nothing: the `/check` procedure files its report. Whether a save or a release runs it is the caller's definition to say, not the check's. Proof: `/check engine`; a run on a project.
- inputs:
  templates/check-definition.md
  .claude/skills/check-contract/SKILL.md
  .claude/skills/check/SKILL.md
  CLAUDE.md
- links:
  `docs/about/the-check.md`: what the contract owns.
  `docs/reference/checks.md`: the checks that exist.
- must-not: no contract text copied; no existing check's clauses copied as content.
- made: mirrored
- state: keep

### docs/extend/add-a-recipe-genre.md
- title: Add a recipe genre
- kind: how-to
- reader: extender
- says: A genre is two files: `.claude/skills/recipe/genres/<genre>.md`, a definition with a one-line description, the genre name, its skeleton and output, a role and a numbered elicitation checklist, and `templates/recipe-<genre>.md`, the skeleton that extends the base recipe shape and never replaces it, with the same front-matter fields and sections and a `## Format` section where the render has a file beside it. Every genre runs in the same frame: the checklist closes with the language question and the recipe is composed from the skeleton. The dispatcher never changes; bare `/recipe` and `/man recipe` scan the directory. Proof: `/check engine`; a composition on a project.
- inputs:
  .claude/skills/recipe/SKILL.md
  .claude/skills/recipe/genres/presentation.md
  templates/recipe.md
  templates/recipe-presentation.md
  CLAUDE.md
- links:
  `docs/reference/recipe-genres.md`: the genres that exist.
  `docs/about/renders-and-recipes.md`: what a recipe is.
- must-not: no checklist copied as content; no genre named as planned.
- made: derived
- evidence: the `/recipe` skill says a genre is two files and that the dispatcher never changes, and gives the shared frame; the presentation genre file and its skeleton are the model of the two shapes; `templates/recipe.md` says the skeleton owns the shape and that a genre skeleton extends it (CLAUDE.md, Document chain, Renders and the `project` check say the same). The page derives the procedure from the model pair.
- state: keep

### docs/extend/add-a-command.md
- title: Add a command
- kind: how-to
- reader: extender
- says: A command is a skill, `.claude/skills/<name>/SKILL.md`: front-matter with `description` (one line, what the command does and what bare means), a quoted `argument-hint`, and `disable-model-invocation: true` where the command writes, scaffolds, commits or regenerates, so that Claude cannot start it on his own judgement; a body that says what the command does and cites every mechanism of another by path, never restating it; supporting files beside it where it dispatches over a roster, read by path. A row in the Commands table of `CLAUDE.md`, which `/man` and the README derive from. Named so that it does not collide with a built-in of Claude Code. Proof: `/check engine` verifies the table against the skills; `/check single-source-of-truth` verifies that nothing is restated. Recorded as any change of the forge.
- inputs:
  CLAUDE.md
  .claude/skills/ledger/SKILL.md
  .claude/skills/man/SKILL.md
  .claude/agents/check-engine.md
  projects/forge/10-intent.md
  projects/forge/40-solution-design.md
- links:
  `docs/extend/how-a-change-is-made.md`: the chain the change goes through.
  `docs/reference/commands.md`: the commands that exist.
- must-not: no skill body copied; no harness detail beyond what the solution design states.
- made: derived
- evidence: SOL.0100 and SOL.0110 of the solution design give the skill shape, the quoted hint and the guard; POS.1090 gives which commands are guarded and why; POS.1070 and prime directive 10 give citation over restatement; CLAUDE.md, Commands gives the table and that `/man` prints from the skill; the `ledger` skill is the smallest model of a command that cites another's mechanism; the `check-engine` agent says the table is verified against the skills; POS.1050 and POS.1190 give the naming rule against built-ins. The page derives the procedure from these.
- state: keep

### docs/extend/add-a-script.md
- title: Add a script
- kind: how-to
- reader: extender
- says: A script is Python 3.8 or newer, run as `python scripts/<name>.py`, and carries its help in its module docstring: a synopsis, what it does, what it needs installed, its options and where its output lands, examples each saying in a comment what it shows; the docstring is the owner of those facts, and commands and `CLAUDE.md` cite it and never restate it. Rules of every script: nothing Windows-only, paths through `pathlib`, processes through `subprocess` with argument lists and never a shell, external tools resolved from PATH and never installed by the script, colour only on a terminal, usage examples free of platform paths, no URL and no identity in the script. What several scripts share lives in one module beside them, imported by path, never twice: `forge_repos.py` for the git scripts, `forge_tools.py` for the conversions, `docs_map.py` for the documentation scripts. It is named in the layout comment of `CLAUDE.md`, and where a command uses it the command names it by path. Git is touched only by the scripts, which `.claude/settings.json` denies to Claude otherwise. Proof: `/check engine` verifies scripts on disk against `CLAUDE.md`.
- inputs:
  CLAUDE.md
  scripts/forge-status.py
  scripts/forge_repos.py
  .claude/agents/check-engine.md
  projects/forge/10-intent.md
  projects/forge/40-solution-design.md
- links:
  `docs/reference/scripts.md`: the scripts that exist.
  `docs/about/persistence-in-git.md`: why the scripts are the only door.
- must-not: no claim that the set has been run on Linux or macOS; no instance path; no mention of PowerShell beyond that the scripts were once in it, if at all; no script body.
- made: derived
- evidence: CLAUDE.md, Persistence (Portability) gives the writing rules, Python 3.8 or newer, `python scripts/<name>.py`, the docstring as the help and the shared modules; POS.0830 gives the reason and that portability is a writing rule until verified; SOL.0620 gives how the scripts are written (`pathlib`, `subprocess` with argument lists, colour on a terminal), what each shared module holds and the option spelling; `forge-status.py` is the smallest model of a docstring that owns its facts, `forge_repos.py` the model of a shared module ("Not a command"); the `check-engine` agent says scripts on disk are verified against CLAUDE.md's layout comment; CLAUDE.md, Document chain cites the headers for what each conversion needs. The page derives the procedure from these.
- state: keep

### docs/extend/change-a-documentation-page.md
- title: Change a documentation page
- kind: how-to
- reader: extender
- says: A page is never edited by hand; what is wrong on a page is mended in the file that owns the matter and the page is regenerated. How to find the owner: the page's front-matter lists its inputs and says whether it is mirrored or derived; a mirrored page restates its inputs, a derived page opens by saying which files it was put together from. To change what a page says, change the owning file (a skill, a definition, a template, an agent, a script's docstring; a reason comes from the forge intent) and run `/document`, which recomputes the state of every page from the content of its inputs and remakes only the pages whose inputs or entry changed, each writer handed its task as a file it reads first. To change which pages exist, what a page covers or who reads it: the map is written by the planner from the target on disk at every run, and the readers and the outline are the planner's definition and a position of the forge intent, so such a change goes through the chain like any change of the forge. What the two agents keep off every page by their shared contract: a name, a company, a host, an account, an e-mail, an address other than the public home, a document of another project, an ID of the chain, a long dash. A fact a page needs and no file owns is reported under Unowned in the planner's report and left out of the page until it gets a home; the readme skeleton gives every project an optional section "Pinned facts (not rendered)" for such facts, read by the planner as an owner and dropped the day a file owns the fact, and the readme recipe of `projects/forge` fills it with the install facts and the engine's public home today. What the check refuses on a page: a link that does not resolve, a long dash, a missing front-matter, an instance fact (a value of `CLAUDE.local.md`, an e-mail address, a path of a machine); a page that fails twice is left out and said, never mended by hand. An agent's definition is loaded once per session: a change to the planner or the writer reaches them in a new session.
- inputs:
  .claude/skills/document/SKILL.md
  .claude/skills/docs-contract/SKILL.md
  .claude/agents/docs-planner.md
  .claude/agents/docs-writer.md
  scripts/docs-check.py
  templates/recipe-readme.md
  projects/forge/recipes/readme.md
- links:
  `docs/use/generate-the-documentation.md`: running the command.
  `docs/reference/documentation-map.md`: the fields of an entry and of a page's front-matter.
  `docs/extend/how-a-change-is-made.md`: the chain a change of the forge goes through.
- must-not: no model name; no agent prompt text copied as an instruction to Claude; nothing of the readme recipe beyond its section "Pinned facts (not rendered)" (the recipe carries an author line and an address); not the address itself and not the readme skeleton's fixed closing sentence; no page named as an example that may not exist; no instance fact; nothing of the check script's `--file` mode (that is the render's).
- made: derived
- evidence: the `/document` skill gives "mended in the file that owns the matter, and the page is regenerated", the state computed from the inputs, the task file handed to a writer by path, the check's rules and the twice-failing page, the harness note on an agent's definition; the docs contract gives what must never reach a page; the writer agent gives the page's front-matter (`made`, `inputs`), that it reads its task first and that a derived page says in its opening what it was put together from; the planner agent gives that the map is written from the target on disk at every run, the readers, the outline and the Unowned section; `docs-check.py`'s docstring gives what the check looks for and that it mends nothing; the readme skeleton's "Pinned facts (not rendered)" comment gives the section as every project's home of facts no file owns, read by the planner and dropped when a file owns the fact; the readme recipe's section says it is the home of the forge's install facts and that the planner reads it as an owner. The page joins them into the order of one change to a page.
- state: keep

## reference

### docs/reference/commands.md
- title: Commands
- kind: reference
- reader: user, extender, evaluator
- says: The Commands table of `CLAUDE.md`, one row per command with its signature and purpose, each row followed by the skill's `description` and `argument-hint` and whether it is guarded against being started on Claude's own judgement (`disable-model-invocation`). Grouped as the table has them, `/document`, `/man` and `/manual` included.
- inputs:
  CLAUDE.md
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
  .claude/skills/check/SKILL.md
  .claude/skills/save/SKILL.md
  .claude/skills/release/SKILL.md
  .claude/skills/spinoff/SKILL.md
  .claude/skills/man/SKILL.md
  .claude/skills/manual/SKILL.md
- links:
  `docs/use/look-up-a-command.md`: the same, printed in the session by `/man`.
- must-not: no procedure of any command; no explanation.
- made: mirrored
- state: keep

### docs/reference/artefacts.md
- title: Artefacts
- kind: reference
- reader: user, extender, evaluator
- says: One row per definition in `.claude/skills/forge/states/`, in the order of the file numbers: the artefact's file, its `description`, its template, its inputs (the Target and Inputs blocks), the prefixes of its items from the ID scheme, and the command that works it. One line below: a layer a project does not have is not missing.
- inputs:
  .claude/skills/forge/states/brief.md
  .claude/skills/forge/states/intent.md
  .claude/skills/forge/states/assignment.md
  .claude/skills/forge/states/solution-design.md
  CLAUDE.md
- links:
  `docs/about/the-document-chain.md`: why the listing of that directory is the one list.
- must-not: no Aim, Partner, Map or Course text; no explanation.
- made: mirrored
- state: keep

### docs/reference/critic-lenses.md
- title: Critic lenses
- kind: reference
- reader: user, extender
- says: One entry per `.claude/agents/critic-*.md`: the lens name, its `description`, and its Lens section (what it reads, what it goes after, its categories, its own report sections), as `/man critique` prints them.
- inputs:
  .claude/agents/critic-clarity.md
  .claude/agents/critic-essence.md
- links:
  `docs/use/critique-the-documents.md`: running a lens.
- must-not: no contract text; no explanation.
- made: mirrored
- state: keep

### docs/reference/challenger-personas.md
- title: Challenger personas
- kind: reference
- reader: user, extender
- says: One entry per `.claude/agents/challenger-*.md`: the persona name, its `description`, and its Lens section (who it is, what it goes after), as `/man challenge` prints them.
- inputs:
  .claude/agents/challenger-cto.md
  .claude/agents/challenger-architect.md
- links:
  `docs/use/challenge-the-thinking.md`: running a persona.
- must-not: no contract text; no explanation.
- made: mirrored
- state: keep

### docs/reference/checks.md
- title: Checks
- kind: reference
- reader: user, extender
- says: One entry per `.claude/agents/check-*.md`: the check name, its `description` with when it fits, and its Lens section (what it reads, what it verifies with the owner of each rule, its cost), as `/man check` prints them; one line on which a save and a release run, from `CLAUDE.md`.
- inputs:
  .claude/agents/check-light.md
  .claude/agents/check-project.md
  .claude/agents/check-engine.md
  .claude/agents/check-history.md
  .claude/agents/check-single-source-of-truth.md
  CLAUDE.md
- links:
  `docs/use/check-conformance.md`: running a check.
- must-not: no contract text; no explanation.
- made: mirrored
- state: keep

### docs/reference/recipe-genres.md
- title: Recipe genres
- kind: reference
- reader: user, extender
- says: One entry per `.claude/skills/recipe/genres/*.md`: the genre, its `description`, its skeleton and output, and its elicitation checklist in full, as `/man recipe` prints them; the shared closing (the language question, composition from the skeleton) once.
- inputs:
  .claude/skills/recipe/genres/presentation.md
  .claude/skills/recipe/genres/readme.md
  .claude/skills/recipe/genres/release-notes.md
  .claude/skills/recipe/SKILL.md
- links:
  `docs/use/compose-a-recipe.md`: composing through a genre.
- must-not: no skeleton reproduced (templates); no explanation; not the parenthesis of the release-notes genre that the forge's own recipe reads the intent alone (that recipe reads the solution design's history too; the page says only that a project may narrow the companions).
- made: mirrored
- state: keep

### docs/reference/id-scheme.md
- title: ID scheme
- kind: reference
- reader: user, extender, evaluator
- says: The format `PREFIX.NNNN`, the numbering rules (tens, next hundred per group, overflow, groups as plain headings, depth two), and the prefix table with meaning and where each lives, as the ID scheme of `CLAUDE.md` has them.
- inputs:
  CLAUDE.md
- links:
  `docs/about/stable-ids.md`: why IDs are never renumbered.
- must-not: no explanation; no example from a project.
- made: mirrored
- state: keep

### docs/reference/versioning-and-front-matter.md
- title: Versioning and front-matter
- kind: reference
- reader: user, extender, evaluator
- says: The version scheme (0.x drafts, integers approved, x.y after approval), the front-matter fields of an artefact (`version`, `date`, `status` with its three words, `last_change`, `project`, `audience`; a brief carries `title` and `author` in place of `audience`) and of a recipe (`version`, `updated`, no status, optional `output:`), the status rule, the companion and archive file names, as `CLAUDE.md` and the templates have them.
- inputs:
  CLAUDE.md
  templates/intent.md
  templates/brief.md
  templates/recipe.md
- links:
  `docs/reference/history-companion.md`: the record's shape.
  `docs/about/versioning-and-history.md`: why.
- must-not: no explanation; no example values from a project; no author value.
- made: mirrored
- state: keep

### docs/reference/history-companion.md
- title: History companion
- kind: reference
- reader: user, extender
- says: The shape of `<file>.history.md` as `templates/history.md` owns it: the front-matter, the record line with its fields in order (date, version, author, subject, kind, reason, Action, Was), the five kinds, what the subject may be, when a field is left out, `Was` last with `<br>` between paragraphs, lines not wrapped, the two records at a document's birth, and the archive rule.
- inputs:
  templates/history.md
  CLAUDE.md
- links:
  `docs/reference/versioning-and-front-matter.md`: the fields the companion feeds.
- must-not: no example record from a project; no explanation.
- made: mirrored
- state: keep

### docs/reference/requirement-style.md
- title: Requirement style
- kind: reference
- reader: user, extender
- says: The rule set of the items of an assignment, as the Requirement style of the assignment's definition has it: shall and shall not, the banned words, no priorities and the *optional* note, one idea per item written once in full sentences, testability recommended not required, defined Terms capitalised, no dependence on an external link.
- inputs:
  .claude/skills/forge/states/assignment.md
  CLAUDE.md
- links:
  `docs/about/the-assignment.md`: why the items are written so.
- must-not: no example item; no explanation.
- made: mirrored
- state: keep

### docs/reference/document-kinds.md
- title: Document kinds
- kind: reference
- reader: user, extender, evaluator
- says: The table of document kinds of `CLAUDE.md`, Document kinds, verbatim, six columns and every row, the kinds `map` and `page` among them; one line each on the companion of every versioned kind, on a library's reduced set, and on the wrapping rule.
- inputs:
  CLAUDE.md
- links:
  `docs/about/documents-and-records.md`: why the kinds exist.
- must-not: no explanation.
- made: mirrored
- state: keep

### docs/reference/ledger.md
- title: Ledger
- kind: reference
- reader: user, extender
- says: The ledger as `templates/ledger.md` owns it: the header fields (`project`, `kind`, `language`, `updated`), every table with its columns (Briefs, Documents, Renders, Published, Sources, Dependencies, Research, Findings, Challenges) and Waiting on principal; the state words of briefs (mined), published files, findings and challenges with the reading of an older word; the row of the documentation index in Renders; which tables a library keeps.
- inputs:
  templates/ledger.md
  CLAUDE.md
- links:
  `docs/use/see-where-a-project-stands.md`: reading the ledger through `/ledger`.
- must-not: no row from a project; no explanation.
- made: mirrored
- state: keep

### docs/reference/render-provenance.md
- title: Render provenance
- kind: reference
- reader: user, extender
- says: The YAML front-matter every render opens with, verbatim as `/render` step 5 gives it (project, render, generated, recipe with version, inputs with versions; inputs without a version cited by path), and the one definition of a stale render; the two file places (`renders/<recipe>.md` or the recipe's `output:`), the plain file beside the render, and the `published/` place with its `current | stale` state.
- inputs:
  .claude/skills/render/SKILL.md
  .claude/skills/publish/SKILL.md
  CLAUDE.md
- links:
  `docs/use/render-an-output.md`: the command.
- must-not: no explanation; no example from a project; nothing of the scan a render passes (the use page's).
- made: mirrored
- state: keep

### docs/reference/documentation-map.md
- title: Documentation map
- kind: reference
- reader: extender
- says: The shape of the map `docs-map.md`, of a writer's task and of a page, as the map's skeleton, the planner's definition, the writer's definition, the contract and the scripts own them. The map: a front-matter of `generated`, `target` (`engine` or a project's slug), `owner`, `previous`; every path relative to the target's root; one section per section of the outline in its order, and in each one entry headed `### docs/<section>/<page>.md` with the fields in order: `title`, `kind` (how-to, explanation, reference), `reader` (user, extender, evaluator, one or more), `says`, `inputs` (whole files, one per line, no globs), `links` (a path and one sentence each), `must-not`, `made` (mirrored or derived), `evidence` (derived pages only), `state` (new, keep, regenerate, remove; which of them the planner writes and which the state script sets from the content of the inputs); then the sections Unowned and Did not fit. The task file the state script writes for a page to make: the engine root, the page's path, the date, the hash the page is to carry, the entry verbatim and the titles of the pages it links to; the writer reads it first. The page: a front-matter of `generated`, `made`, `inputs-hash` and `inputs`, then the title, one paragraph of what the page is for and for whom, the matter, and a See also of the linked pages cited by their titles; links into `docs/` only to the pages the entry lists, relative; what must never reach a page as the contract lists it (no name, company, host, account, e-mail or identifier of an instance, no address but the public home, no document of another project, nothing of a skill or an agent as an instruction, no ID of the chain, no long dash). The index `docs/README.md`: derived from the map, one line per page by section, with the version of the owning project's intent.
- inputs:
  templates/docs-map.md
  .claude/agents/docs-planner.md
  .claude/agents/docs-writer.md
  .claude/skills/docs-contract/SKILL.md
  scripts/docs_map.py
  scripts/docs-state.py
  scripts/docs-index.py
- links:
  `docs/about/the-documentation.md`: what the map and the pages are for.
  `docs/extend/change-a-documentation-page.md`: changing a page through its owners.
- must-not: no entry of the engine's map quoted; no explanation; no model name; nothing of the agents' conduct beyond the shapes and the contract's list.
- made: mirrored
- state: keep

### docs/reference/verdict-words.md
- title: Verdict words
- kind: reference
- reader: user
- says: The words the principal types and what each does, as the walkthrough skill and `CLAUDE.md` own them: the verdict line `(a)ccept / (m)odify / (r)eject / (p)ark` and the single letters `a`, `m`, `r`, `p` as a whole message; `obsolete`; `write`; `??`; a closing word such as "done" for a thought sent in pieces; that no other word of the forge has a letter and every command is typed in full.
- inputs:
  .claude/skills/walkthrough/SKILL.md
  CLAUDE.md
- links:
  `docs/use/walk-through-a-list.md`: the procedure the words belong to.
- must-not: no explanation; no reason.
- made: mirrored
- state: keep

### docs/reference/repository-layout.md
- title: Repository layout
- kind: reference
- reader: user, extender, evaluator
- says: The layout block of `CLAUDE.md`, Repository layout, in full: the engine root, a thought project, a library; each comment kept as a fact.
- inputs:
  CLAUDE.md
- links:
  `docs/about/projects-and-the-engine.md`: why projects are repositories of their own.
- must-not: no explanation; no instance file.
- made: mirrored
- state: keep

### docs/reference/scripts.md
- title: Scripts
- kind: reference
- reader: user, extender
- says: One entry per file in `scripts/`, from its module docstring: what it does, its synopsis and options in the Python spelling, its forms (bare, slug, `forge` for the engine), what it needs installed, where its output lands, and the command of the forge that runs it as `CLAUDE.md` says; for `md2pptx.py` and `md2docx.py` the two engines with their defaults and how a template or a reference document is named, and what the conversions need as `forge_tools.py`'s docstring owns it; for the three documentation scripts their place in the run of `/document`, and for `docs-check.py` its second form, the one-file scan of instance facts that `/render` runs on a render; the three shared modules (`forge_repos.py`, `forge_tools.py`, `docs_map.py`) each in one line as what the scripts beside them share, not commands. Below, the portability rule in one line: Python 3.8 or newer, run as `python scripts/<name>.py`.
- inputs:
  scripts/forge-save.py
  scripts/forge-pull.py
  scripts/forge-status.py
  scripts/forge-clone.py
  scripts/forge-branch.py
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
  CLAUDE.md
- links:
  `docs/start/install.md`: installing what the scripts need.
  `docs/use/generate-the-documentation.md`: the run the documentation scripts serve.
  `docs/use/render-an-output.md`: the render that runs the one-file scan.
- must-not: nothing below a docstring; no example path or slug of a project (the docstrings' examples carry the slugs `platform-strategy` and `agentic-platform`, a `lib-acme` path and a path into the forge project's renders, which are replaced by `<slug>` and `<path>`; `forge`, `main`, `my-idea` and `example.com` may stand); no date or thread number from the hook's docstring; no explanation.
- made: mirrored
- state: keep

### docs/reference/templates.md
- title: Templates
- kind: reference
- reader: extender
- says: One entry per file in `templates/`: what it is the skeleton of, which command or procedure creates from it, and its fields or sections in one line; the `<type>-definition.md` naming rule; the skeleton of the documentation map, written by the planner of `/document`; the readme skeleton's optional section "Pinned facts (not rendered)" and what it is for; the fields of a resource index entry (sources and research) and of a bundle index.
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
  CLAUDE.md
- links:
  `docs/extend/what-it-is-made-of.md`: where the templates sit in the whole.
  `docs/reference/documentation-map.md`: the map's fields in full.
- must-not: no skeleton reproduced whole; no explanation; not the fixed closing sentence of the readme skeleton (it carries an address, which is the install page's alone).
- made: mirrored
- state: keep

### docs/reference/configuration.md
- title: Configuration
- kind: reference
- reader: user, extender
- says: The files that configure an instance and what each holds: `.claude/settings.json` (shared: `attribution` empty and sessionUrl false, the deny rules for sensitive paths and raw git in both shells, the `UserPromptSubmit` hook running `scripts/hook-walkthrough.py` through `python` with the project-directory placeholder); `.claude/settings.local.json` (gitignored, the session model, created by `/setup`); `CLAUDE.local.md` (gitignored, the principal by role and the conversation language, from its template); the `.gitignore` of the engine (`projects/*` with `projects/forge` re-included, the two local files, the engine's `tmp/`, Python caches and office noise); the git identity outside the engine, per host, with the guard.
- inputs:
  .claude/settings.json
  .gitignore
  templates/CLAUDE.local.md
  .claude/skills/setup/SKILL.md
  CLAUDE.md
  projects/forge/40-solution-design.md
- links:
  `docs/start/setup.md`: the command that fills the instance files.
  `docs/about/how-the-rules-are-held.md`: why the deny rules and the hook exist.
- must-not: no value of an instance; no host; no explanation beyond one clause per item; nothing of the `.gitignore`'s entry for a local launcher (a file of one instance); no mention of PowerShell beyond the deny rule's shell name.
- made: mirrored
- state: keep

### docs/reference/glossary.md
- title: Glossary
- kind: reference
- reader: user, extender, evaluator
- says: The terms of the forge in one line each, with the file that defines each: principal, recipients, Claude as cognitive extension, document, artefact, brief, intent, position, fact, thread, rejected direction, assignment, solution design, layer, definition, template, Map, elicitation, walkthrough, round, write, history companion, archive, ledger, decision, source, bundle, extract, research, resource index, recipe, render, plain file, published file, genre, critic, lens, challenger, persona, check, finding, challenge, contract, project, thought project, library, dependency, engine, instance, instance fact, session model, save, release, major, tag, stale, immutable, mined, documentation, map, page, index, mirrored, derived, pinned fact.
- inputs:
  CLAUDE.md
  projects/forge/10-intent.md
  .claude/skills/forge/states/brief.md
  .claude/skills/forge/states/intent.md
  .claude/skills/forge/states/assignment.md
  .claude/skills/forge/states/solution-design.md
  .claude/skills/walkthrough/SKILL.md
  .claude/skills/render/SKILL.md
  .claude/skills/document/SKILL.md
  templates/ledger.md
  templates/recipe-readme.md
- links:
  `docs/about/what-it-is-and-is-not.md`: the forge in prose.
- must-not: no term invented; no definition longer than a sentence; no name, handle or instance value; not the readme skeleton's fixed closing sentence or its address.
- made: derived
- evidence: each term is defined where a file first defines it: the roles and the document kinds in CLAUDE.md (Roles, Document kinds, Document chain, Isolated reviewers, Ledger, Persistence); the artefacts in their definitions' Target and Aim; position, fact, thread, rejection in the ID scheme and POS.0120, POS.0230; elicitation, Map, definition in POS.1300 to POS.1320; walkthrough, round, write in the walkthrough skill and prime directive 9; stale and provenance in `/render` step 5; the ledger's state words in `templates/ledger.md`; engine, instance, instance fact in CLAUDE.md "What this workspace is" and POS.0950; major in POS.0300; documentation, map, page, index, mirrored and derived in CLAUDE.md, Document kinds and Document chain, item 5, POS.1450 and the `/document` skill; pinned fact in the readme skeleton's section comment. The writer takes each term from its owner and writes one sentence; a term no file defines is left out.
- state: keep

## Unowned

- Whether the forge runs on Linux and macOS as a verified fact, needed by `docs/start/install.md`, `docs/about/persistence-in-git.md` and `docs/extend/add-a-script.md`: CLAUDE.md and POS.0830 say it is a writing rule until verified, and SOL.0620 says the set has not been run on Linux. The pages state the rule and no claim.
- The name of the session model as a product fact ("Fable, the strongest available model"), stated in the body of `.claude/skills/setup/SKILL.md` and in POS.1050; no file says what happens when that model is not available to an instance. `docs/start/setup.md` mirrors the skill's body and says nothing more.
- Which faster model a mirrored page is written on: the `/document` skill names `sonnet` as the override; no file says why that one or what an instance without it does. The documentation pages say "a faster model" and name none.
- What `/document <slug>` reads for a project other than the engine beyond the planner's paragraph "For a project", and in which language a project's pages are written when its artefacts are not English: the forge intent (POS.1450) leaves both to THR.0590. `docs/use/generate-the-documentation.md` says only where the pages and the map of a project land, as the skill does; `docs/about/languages.md` says the engine's documentation is English.
- What `/forge <state>` does on a project of kind `library` beyond stopping the map: not needed by any page; recorded so that no page invents it.
- Settled since the previous map: the public address of the repository, which the readme recipe's section "Pinned facts (not rendered)" owns and SOL.0500 names as the one place the README and the documentation read it from; it reaches `docs/start/install.md` and no other page.

## Did not fit

- The skeleton's heading `# Documentation map — <target>` carries a long dash; the contract forbids one anywhere in what the agents write, so this map's heading carries a spaced hyphen. The scripts parse the entries, not the heading.
- `docs/start/what-it-is.md` is an explanation in a section the outline marks how-to. A page that says what the thing is in one paragraph cannot be a how-to; it is marked `kind: explanation` and kept in `start/` where the outline places it, so that the reader's journey begins there.
- The engine's public address: the previous map found the planner's and the writer's definitions banning "an address" without a distinction while the intent (POS.0990) and the solution design made the public face a fact of the product. Settled: the contract now permits "the public home of the target where the target's own documents name it as such", the readme recipe's pinned facts name it as such, and SOL.0500 names the recipe as the one place. The map keeps the earlier reading of where it belongs: `docs/start/install.md` alone, as the place a newcomer clones from; every other page keeps the ban whole, the readme skeleton's fixed closing sentence included.
- The pinned facts the owning project's recipes carry sit beside facts no page may carry. `projects/forge/recipes/readme.md` owns the prerequisites, the install lines and the public home in its section "Pinned facts (not rendered)", which names the planner as its reader; the same file carries an author line with a name and an e-mail. `projects/forge/recipes/contributing.md` carries the channels as addresses and the author's profile. The pages that take either as an input take only the section or the facts named in their entry, and their `must-not` says so. The three pitch recipes (`cto-pitch.md`, `ceo-pitch.md`, `executive-pitch.md`) carry the author's identity and contacts and own nothing a page needs; they are the input of no page.
- The release-notes genre file (`.claude/skills/recipe/genres/release-notes.md`) says in a parenthesis that the forge itself reads the intent alone, while the forge's release-notes recipe (0.13) reads the solution design's history as well. Both are operating layer; the recipe is the newer and the one that runs. The pages that mirror the genre (`docs/reference/recipe-genres.md`, `docs/use/compose-a-recipe.md`) leave the parenthesis out and say only that a project may narrow the companions; the owner of the genre file settles the sentence.
- `CLAUDE.md`, Isolated reviewers, and POS.1120 speak of three contracts, one per kind of reviewer; the layout comment of `CLAUDE.md` and SOL.0460 add a fourth contract skill, `docs-contract`, for the documentation agents, which are not reviewers. Not a contradiction: the pages keep the two apart. `docs/about/isolated-reviewers.md` counts three kinds of reviewer and says the documentation agents are not among them; `docs/about/the-documentation.md` says the two agents share a contract as the reviewers do.
- The scripts' docstrings carry example slugs (`platform-strategy` in `forge-save.py`, `forge-pull.py`, `forge-branch.py`; `agentic-platform`, a project of the first instance, in `md2pptx.py`), a path into the forge project's renders in `md2docx.py` and a `lib-acme` placeholder; the examples carry comments saying what each shows, which is a fact of the docstring's shape and reaches `docs/extend/add-a-script.md`. `docs/reference/scripts.md` and the use pages replace the slugs and paths by `<slug>` and `<path>`, and their `must-not` says so. The hook's docstring carries dates and a thread number; the pages take what it prints, not its history.
- The forge intent names its first principal by handle in POS.0005 and its Essence says the forge began as one CTO's tool; it names a programme name in POS.0610, and the briefs carry an `author` field; every page that reads the intent has "no name, no handle" in its `must-not`, and the origin is said only as "one person's tool, an instance fact".
- `md2pptx.py` defaults to the `claude` engine and `md2docx.py` to `pandoc`; both docstrings say so and `docs/reference/scripts.md` mirrors each. Both send the reader to `forge_tools.py` for what the conversions need; the install page and the scripts page read it as the owner of that text.
- The brief `00-brief.md` of the owning project says no brief exists for the forge; the reasons of the `about/` pages come from the intent, and from the briefs only through the positions mined from them (`00-brief-public-engine.md` through POS.0760, POS.0980; `00-brief-documentation.md` through POS.1450 and REJ.0240 to REJ.0260), so no brief is an input. `00-brief-next-gen.md` and `00-brief-elicitation.md` carry thoughts not yet positions or already mined and are the input of no page.
- `threads.md` of the owning project is the input of no page: it changes with every round and holds what is being worked, not what holds; `docs/about/where-it-is-going.md` reads positions only. `decisions.md` likewise: its records settle findings and challenges and name retired words and are the input of no page; the sentence of `docs/about/the-principal-and-claude.md` that the principal's recorded exception is the designed form is CLAUDE.md's (Roles, prime directive 5) and POS.0010's, not a decision record's.
- The solution design still opens by calling itself a proposal not judged whole by the principal; `docs/about/the-documentation.md`, `docs/about/how-a-thought-travels.md`, `docs/extend/what-it-is-made-of.md`, `docs/about/how-the-rules-are-held.md`, `docs/about/projects-and-the-engine.md`, `docs/extend/add-a-command.md`, `docs/extend/add-a-script.md` and `docs/reference/configuration.md` read items of it as evidence or facts, since every item says it records what the intent decided and the operating layer on disk agrees with what the pages take; where the design and a file differ, the page takes the file.
- Three reviewer kinds got one page each in `about/` beside the shared `isolated-reviewers.md`, on the reading that "one page per kind of artefact or part" covers a kind of reviewer; the rosters are three pages in `reference/` so that a new lens, persona or check regenerates one page. The two documentation agents are not reviewers and get no roster page: their shapes are `docs/reference/documentation-map.md`'s, their purpose `docs/about/the-documentation.md`'s.
- The research index was read for orientation only and is the input of no page; no research note is cited by a page.
- The README, the renders and `docs/` of the target were not read, as the definition says; `CONTRIBUTING.md` is named as a file by `docs/extend/how-a-change-is-made.md` on the strength of its recipe and CLAUDE.md's layout, not read. The ledger of the owning project was read for orientation and is the input of no page.
- Settled since the previous map and no longer noted: the public address had no owner among the engine's files (the readme recipe's pinned facts own it, SOL.0500 names the place, the contract permits it). Settled earlier and still no longer noted: the release skill lacked the step on the documentation's age; the solution design said the documentation was not yet built; the release skill offered `critique essence` against a thread's wish; CLAUDE.md said new scripts are Python while the scripts were PowerShell; `templates/intent.md` said IDs may be omitted; `.claude/agents/docs-planner.md` called itself a trial; the version of Python was unowned.
