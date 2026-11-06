---
date: 2026-11-01
project: forge
check: documentation
target: the engine (C:\pche\_dev\forge-of-thought), the documentation run of 2026-11-01
reviewer: the documentation run
---

# Check (documentation) — the engine — 2026-11-01

48 findings

What the documentation run of 2026-11-01 could not place: the planner's Unowned facts and the matters where the map and its owner disagree, the claims the map asked for and no input carried, and every place where a page wanted a reason and no file records one. Filed by the run itself, as POS.1450 has it from this day; the first report of its kind, gathered from the writers' hand-backs after the run. A mend lands in the owner, never on a page.

## Findings

### FND.3030 — medium — The language of the documentation's pages is ruled nowhere but in the documentation contract
- **Where:** .claude/skills/docs-contract/SKILL.md (the sentence "English, plain"); projects/forge/10-intent.md POS.1450 says only that the README is English. The map entry of `docs/about/languages.md` claimed "the documentation English only" on POS.1450, which does not say it.
- **Rule:** One mechanism lives in one place (CLAUDE.md, prime directive 10); a rule a page states must have an owner the page can cite.
- **Fix:** Decide the language of the pages in the intent and the core; bring the map entry to the owner's wording.

### FND.3040 — medium — Two map entries say a version given twice shows as a conflict in the header's `version:` line; POS.1790 says it is found by the conflict of the two history tails
- **Where:** projects/forge/docs-map.md, the `says` of `docs/use/settle-a-conflict.md` and of `docs/about/working-together.md`; projects/forge/10-intent.md POS.1790.
- **Rule:** A derived page claims nothing its inputs do not carry (the documentation contract); the planner's `says` follows the owner's present wording.
- **Fix:** Bring both entries to POS.1790: the header line merges silently when both sides wrote the same number, git finds the clash at the end of the history, and the ledger script reports a number taken twice. The writers followed the position; the pages are right, the map is not.

### FND.3050 — medium — The map's evidence for the technical sentence of the start page points at the wrong paragraph of the Essence
- **Where:** projects/forge/docs-map.md, entry of `docs/start/what-it-is.md`: the evidence names the Essence's last paragraph, which is about how complete an assignment must be and names no commands, agents, templates or scripts; the gloss "Anthropic's AI assistant for the command line" stands in the entry and in no input.
- **Rule:** A derived page names its evidence, and the evidence carries what the page says (POS.1450).
- **Fix:** Point the evidence at the paragraph that carries the parts, or carry the list in CLAUDE.md where the page can cite it; give the gloss an owner or drop it.

### FND.3060 — medium — The install page's entry asks for install lines that carry addresses the same entry forbids
- **Where:** projects/forge/docs-map.md, entry of `docs/start/install.md`: the pinned facts' Claude Code install lines carry `claude.ai` URLs; the entry allows only the engine's public home and the course page as addresses.
- **Rule:** An entry's `says` and its `must-not` cannot contradict each other (the planner's definition).
- **Fix:** Allow the install addresses in the entry, or point the reader to the tool's own documentation without the lines.

### FND.3070 — medium — The state-map page's entry asks for an ID in brackets in the worked example; the contract bars chain IDs on a page
- **Where:** projects/forge/docs-map.md, entry of `docs/use/see-where-a-project-stands.md`; the page carries a placeholder `THR.0010`.
- **Rule:** What never reaches a page (the documentation contract): a chain ID.
- **Fix:** Reword the entry so the example shows the shape of a thread's line without an ID, or rule in the contract that a template's placeholder ID is not a chain ID.

### FND.3080 — medium — Unowned: whether the forge runs on macOS, and whether the conversions and the two hooks run on Linux, as a verified fact
- **Where:** CLAUDE.md, Portability says "written to run" and names what has run on Linux; no file states a verified fact for macOS.
- **Rule:** A page cannot say what no owner says (POS.1450); the fact waits for its owner.
- **Fix:** Record in POS.0830 what has been verified and on what, or say plainly that macOS is unverified.

### FND.3090 — medium — Unowned: how the second engine's tool `agy` is installed and signed in
- **Where:** scripts/forge-engine.py names the tool and the login the user makes once; no file says how.
- **Rule:** A how-to page needs an owner for every step (POS.1450).
- **Fix:** Give the installation and login of an engine's tool a home, the script's header or the research skill, or state that it is the tool's own documentation's.

### FND.3100 — medium — Unowned: what `/document <slug>` reads for a project other than the engine
- **Where:** .claude/skills/document/SKILL.md says where the pages land; what the planner reads in a project is open in THR.0590.
- **Rule:** Trigger: the first `/document <slug>` on a project (THR.0590).
- **Fix:** Settle THR.0590 before the first run on a project; until then the page says the question is open.

### FND.3110 — medium — Unowned: what `/forge <state>` does on a library project
- **Where:** .claude/skills/forge/SKILL.md says the bare map stops after the git line for a library; nothing says what a target state does there.
- **Rule:** A how-to names what the person sees (POS.1450).
- **Fix:** One sentence in the forge skill: a library has no chain, so a target state reports that and stops.

### FND.3120 — medium — Unowned: what Claude Code is, beyond the intent's Essence
- **Where:** projects/forge/10-intent.md, Essence says "runs in Claude Code"; no file glosses it.
- **Rule:** A term a reader may not know is glossed where it first appears (the documentation contract).
- **Fix:** One sentence in the Essence or in CLAUDE.md, What this workspace is.

### FND.3130 — medium — Unowned: the document kind of the player page, of a file in `tmp/`, and of the principal's own file in `renders/` or `published/`
- **Where:** CLAUDE.md, Document kinds names none of the three; the layout and POS.1910 describe them.
- **Rule:** Every document has one kind (CLAUDE.md, Document kinds).
- **Fix:** Decide whether the three have a kind, or say in Document kinds that a file of `tmp/`, the player page and the principal's own file are outside the kinds.

### FND.3140 — medium — Unowned: how the tag taken before a migration is made
- **Where:** .claude/skills/migrate/SKILL.md names the tag; the save skill says a tag is the principal's request; no file says the step.
- **Rule:** A how-to names each step and what the person sees (POS.1450).
- **Fix:** One sentence in the migrate skill: the tag is taken through `/save --tag <name>` before `--apply`.

### FND.3150 — medium — Unowned: how the integrator starts a merge on his own clone
- **Where:** CLAUDE.md, Persistence says merging is git's, by hand or by merge request; no file says what the integrator types or where the step of a conflict begins.
- **Rule:** A how-to names each step (POS.1450).
- **Fix:** One sentence in Persistence or in the pull skill, or a decision that the merge is outside the forge's documentation.

### FND.3160 — medium — Unowned: what the BRD's roster of areas holds and where it lies, now that the definition names no path
- **Where:** .claude/skills/forge/states/brd.md, Inputs: "a library document of the instance, cited by path".
- **Rule:** The instance's roster is the library's (POS.1800); which library document, the instance's project must say.
- **Fix:** The instance names the roster in its own project, a library's index entry or the project's CLAUDE.md; the engine says only that it is a library document.

### FND.3170 — medium — Claims the map asked for and no input carried
- **Where:** `/check engine` as the proof on `docs/extend/add-a-recipe-genre.md`, `add-an-engine.md` and `add-a-script.md`; the step "save, then pull on the other clones" on `docs/use/upgrade-the-engine.md`; the command that regenerates CONTRIBUTING on `docs/extend/how-a-change-is-made.md`; a deck template named in a recipe's Format section on `docs/use/share-material-through-a-library.md`; what the deny rule covers on `docs/extend/what-it-is-made-of.md`; `/man recipe` scanning the genres on `add-a-recipe-genre.md`.
- **Rule:** A page claims nothing its inputs do not carry (the documentation contract).
- **Fix:** Add the carrying file to each entry's inputs where one exists, or cut the claim from the entry's `says`.

### FND.3180 — low — Reason not recorded: why a brief keeps its language
- **Where:** CLAUDE.md, prime directive 6 states the exception; `docs/about/the-brief.md` says the reason is not recorded.
- **Rule:** An explanation carries the why (POS.1450); a reason enters the intent, never a page.
- **Fix:** Record the reason in POS.0060 or say there is none worth writing.

### FND.3190 — low — Reason not recorded: why "Mandate" was rejected as the assignment's name, and why `shall`
- **Where:** `docs/about/the-assignment.md`; the intent says only that the principal rejected the name outright.
- **Rule:** As above.
- **Fix:** Record both in the assignment's positions or confirm no reason.

### FND.3200 — low — Reason not recorded: four rules of the languages page
- **Where:** `docs/about/languages.md`: why the briefs are exempt from the output language; why a work product's file takes the language its Making says; why the README is English only; why the conversation language never appears outward.
- **Rule:** As above.
- **Fix:** Record in POS.0060 and POS.1450, or confirm no reason.

### FND.3210 — low — Reason not recorded: why a rejected challenge is healthy, why no fabrication, why an accepted challenge is mended where needed
- **Where:** `docs/about/the-challenger.md`; the writer built the reasons from neighbouring rules and says so.
- **Rule:** As above.
- **Fix:** Record in POS.0400 or POS.0440, or confirm the neighbouring rules are the reason.

### FND.3220 — low — Reason not recorded: why a challenger may search the web, and why the reviewers run on the session model
- **Where:** `docs/about/isolated-reviewers.md`.
- **Rule:** As above.
- **Fix:** Record in POS.0400 or POS.0930.

### FND.3230 — low — Reason not recorded: why the projects live inside the engine's tree, and why a plugin as the only shape was rejected
- **Where:** `docs/about/projects-and-the-engine.md`; the rejection points to an open thread (THR.0190).
- **Rule:** As above.
- **Fix:** Record in POS.0940 or close THR.0190 with the reason.

### FND.3240 — low — Reason not recorded: why the listing of the definitions directory is the only list of artefacts, why substance goes into the intent first, why the chain never spans two principals
- **Where:** `docs/about/the-document-chain.md` and `docs/about/where-it-is-going.md`; POS.0140 and POS.0700 state the rules without their reasons.
- **Rule:** As above.
- **Fix:** Record in POS.0100, POS.0140 and POS.0700.

### FND.3250 — low — Reason not recorded: why the documentation is generated rather than written by hand
- **Where:** `docs/about/how-a-thought-travels.md`; CLAUDE.md, Document chain states the rule.
- **Rule:** As above.
- **Fix:** Record in POS.1450.

### FND.3260 — low — Reason not recorded: why the forge must not carry a key to another engine
- **Where:** `docs/about/another-model-family.md`; POS.1880 states the rule.
- **Rule:** As above.
- **Fix:** Record in POS.1880.

### FND.3270 — low — Reason not recorded: why the door to git binds the forge and not the principal's own shell
- **Where:** `docs/about/persistence-in-git.md`; CLAUDE.md, Persistence states it.
- **Rule:** As above.
- **Fix:** Record in POS.1200.

### FND.3280 — low — Reason not recorded: why a definition has exactly seven blocks, why shared mechanism stays outside the definitions, why the walk of a Map is said aloud and not recorded
- **Where:** `docs/about/elicitation.md`; POS.1310 and POS.1320.
- **Rule:** As above.
- **Fix:** Record in POS.1310 and POS.1320, or confirm no reason.

### FND.3290 — low — Reason not recorded: why `docs/videos/` is kept apart from the documentation, why the previous map is taken from git, why the run is on `main` only
- **Where:** `docs/about/the-documentation.md`; the owners are POS.1540 and SOL.0700, not among the page's inputs.
- **Rule:** As above.
- **Fix:** Add the owners to the entry's inputs; the reasons exist.

### FND.3300 — low — Reason not recorded: four rules of the check
- **Where:** `docs/about/the-check.md`: why a check reads each rule where it is defined; why it is read-only; why each check owns one concern; why every finding gives `file:line` and findings are ranked by severity.
- **Rule:** As above.
- **Fix:** Record in POS.0430 or the check contract's position.

### FND.3310 — low — Reason not recorded: why a source and a research note are immutable
- **Where:** `docs/about/sources-and-research.md` and `docs/about/documents-and-records.md`.
- **Rule:** As above.
- **Fix:** Record in POS.1040.

### FND.3320 — low — Reason not recorded: why regression comes first in the critic's lens, and why a lens returns its report rather than filing it
- **Where:** `docs/about/the-critic.md`; CLAUDE.md gives the second reason (no ID given twice) but is not an input of the page.
- **Rule:** As above.
- **Fix:** Add CLAUDE.md, Isolated reviewers to the entry's inputs; record the first in POS.0410.

### FND.3330 — low — Reason not recorded: why the reviewers run only on the principal's word
- **Where:** `docs/about/isolated-reviewers.md`; POS.0400.
- **Rule:** As above.
- **Fix:** Record in POS.0400.

### FND.3340 — low — Reason not recorded: why an assumption may never answer an open question of a BRD, and why the stakeholders' sign-off is not recorded as a rule
- **Where:** `docs/about/the-brd.md`; the only reason the inputs give is a trial the page may not cite.
- **Rule:** As above.
- **Fix:** Record in POS.1800 to POS.1850 without the trial.

### FND.3350 — low — Reason not recorded: why records are append-only, why reviews and challenges are immutable, why one project per session is the default
- **Where:** `docs/about/documents-and-records.md`.
- **Rule:** As above.
- **Fix:** Record in POS.0310, POS.0400 and the session position.

### FND.3360 — low — Reason not recorded: why the principal's own files get no companion, no row and no check, and why the line between chain and render is authorship rather than audience
- **Where:** `docs/about/renders-and-recipes.md`; POS.1910 and POS.0810.
- **Rule:** As above.
- **Fix:** Record in POS.1910 and POS.0810.

### FND.3370 — low — Reason not recorded: why the solution design cites the layer above by ID instead of restating it, and names what realises a part by path instead of copying it
- **Where:** `docs/about/the-solution-design.md`; the page's own question asks this.
- **Rule:** As above.
- **Fix:** Record in POS.1390.

### FND.3380 — low — Reason not recorded: five prime directives
- **Where:** `docs/about/the-principal-and-claude.md`: why never a convention alone; why many iterations are the normal mode; why research before inventing; why advisory, never blocking; why "written" must name a file.
- **Rule:** As above.
- **Fix:** Record in the positions behind directives 2, 3, 4, 5 and 9, or confirm no reason.

### FND.3390 — low — Reason not recorded: six rules of a research
- **Where:** `docs/about/the-research.md`: why an unanswered page counts as unverifiable and not a failure; why a card holds one kind of evidence; why every card carries a disconfirming query; why each agent sees nothing of the conversation; why the synthesis draws on the notes alone; why the unexpected finds are gathered before judgement.
- **Rule:** As above.
- **Fix:** Record in POS.1860 to POS.1900.

### FND.3400 — low — Reason not recorded: why no engine version is recorded, and why the shape of files is told by marks
- **Where:** `docs/about/upgrades-and-migration.md`; the entry gives "one more thing to keep", which no input states.
- **Rule:** As above.
- **Fix:** Record in POS.1740.

### FND.3410 — low — Reason not recorded: why a recipe stays 0.x
- **Where:** `docs/about/versioning-and-history.md`; POS.0810.
- **Rule:** As above.
- **Fix:** Record in POS.0810.

### FND.3420 — low — Reason not recorded: why a history written before the log is kept as it stands, and why a history is never loaded whole
- **Where:** `docs/about/versioning-and-history.md`; POS.0310 and the history skill.
- **Rule:** As above.
- **Fix:** Record in POS.0310.

### FND.3430 — low — Reason not recorded: why a skill's `description` is required beyond the harness listing it
- **Where:** `docs/extend/add-a-command.md`; SOL.0100.
- **Rule:** As above.
- **Fix:** Record in SOL.0100 or confirm the harness is the reason.

### FND.3440 — low — Reason not recorded: why a layer's mechanics are designed only when the layer is taken up, why no destination or deadline is promised, why feedback and ideas are wanted most
- **Where:** `docs/about/where-it-is-going.md`; POS.0700, POS.0780, POS.1440.
- **Rule:** As above.
- **Fix:** Record in those positions or confirm no reason.

### FND.3450 — low — Reason not recorded: why the names considered beside Forge of Thought were not chosen
- **Where:** `docs/about/what-it-is-and-is-not.md`; POS.0600.
- **Rule:** As above.
- **Fix:** Record in POS.0600 or confirm no reason.

### FND.3460 — low — Reason not recorded: why the pace and the look of a video stay out of the render, why video files stay out of the tree, why the public folder is kept out of the documentation
- **Where:** `docs/about/the-screenplay-and-its-player.md`; SOL.0420 and POS.1540 are not among the page's inputs.
- **Rule:** As above.
- **Fix:** Add the owners to the entry's inputs; record what they lack.

### FND.3470 — low — Reason not recorded: why a page is never mended by hand
- **Where:** `docs/extend/change-a-documentation-page.md`; POS.1450 states the rule.
- **Rule:** As above.
- **Fix:** Record in POS.1450.

### FND.3480 — low — Reason not recorded: why `ffmpeg failed.` happens, and why a screenplay has no designed file
- **Where:** `docs/use/make-a-video-from-a-recipe.md`; scripts/md2video.py and the render skill.
- **Rule:** As above.
- **Fix:** Record in the script's header and in POS.1540.

### FND.3490 — low — Reason not recorded: four working methods
- **Where:** `docs/about/working-methods.md`: why propose, never decide; why one write per round; why intent-first; why recommend, do not push. The owners of the second and third (POS.0190, POS.0140) are not among the page's inputs.
- **Rule:** As above.
- **Fix:** Add POS.0190 and POS.0140 to the entry's inputs; record the other two in POS.0850 to POS.0870.

### FND.3500 — low — Reason not recorded: why engines are named and never models
- **Where:** `docs/about/another-model-family.md` and `docs/extend/add-an-engine.md`; POS.1880.
- **Rule:** As above.
- **Fix:** Record in POS.1880.

## Facts
- The run remade all 101 pages: the re-wrap of the documentation contract at FND.3020 changed the generator's hash, wording unchanged.
- Six pages were refused by `scripts/docs-check.py` on the first pass (long dashes in quoted literals, broken relative links, a word naming the conversation language) and passed after one regeneration with the refusal in their task.
- The README was rendered before the run and read the documentation index at 6.1; it was rendered again after the run.
