---
date: 2026-10-09
project: forge
check: single-source-of-truth
target: engine (C:\pche\_dev\forge-of-thought)
reviewer: check single-source-of-truth (isolated context)
---

# Check (single-source-of-truth) - engine (C:\pche\_dev\forge-of-thought) - 2026-10-09

19 findings; 78 files of the operating layer read whole from disk (CLAUDE.md as it lies on disk, 31 skill files with the 4 states and 3 genres, 11 agents, 19 templates, the help headers of 15 scripts, .claude/settings.json), plus the Findings table of C:\pche\_dev\forge-of-thought\projects\forge\ledger.md, the two earlier reports of this check (2026-10-02, 2026-10-05) and the DEC headings of decisions.md with DEC.0170 and DEC.0180 in full. Of the seven findings the 2026-10-05 report left open or reopened, all seven still stand on disk and are named below under their IDs; FND.0710 (DEC.0170) and the caveat part of FND.0720 (DEC.0180) are rejected and not raised. Twelve findings are new, most of them in the documentation mechanism born since the last run.

## Findings

### FND.1060 - medium - The two documentation agents carry the same conduct and the same "what must not reach a page" rule set, word for word, with no owner
- **Where:** C:\pche\_dev\forge-of-thought\.claude\agents\docs-planner.md:18-22, 155-164 against C:\pche\_dev\forge-of-thought\.claude\agents\docs-writer.md:22-24, 83-96
- **Rule:** One owner per rule (CLAUDE.md, prime directive 10; POS.1070); shared behaviour of agents of one kind lives in one place (CLAUDE.md, Isolated reviewers, the contract pattern). The sentence "No name of a person, no company, no host, no address, no account, no email, no identifier of an instance: a placeholder slug replaces a real one in every example" stands verbatim in both; so do "Nothing of a skill copied as an instruction to Claude ...", "Where the operating layer (...) and the intent differ, ... the operating layer's wording and the intent's reason", and the opening "Whatever your context carries about the people who run this forge ... must not reach ..."; neither file cites the other, and the two have already begun to drift ("a skill" against "a skill or an agent", "hosts or addresses" against "hosts, addresses or preferences").
- **Fix:** Keep the rule set once in docs-writer.md (the page is where it bites) and cut docs-planner.md to one sentence citing that section by path, keeping in the planner only what the planner alone decides (the `must-not` of an entry).

### FND.1070 - medium - `/document` restates what its three scripts do, where the headers own it
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\document\SKILL.md:31-38 (step 2) against C:\pche\_dev\forge-of-thought\scripts\docs-state.py:9-33; SKILL.md:51-53 (step 5) against C:\pche\_dev\forge-of-thought\scripts\docs-index.py:8-18, 23-27; SKILL.md:54-61 (step 6) against C:\pche\_dev\forge-of-thought\scripts\docs-check.py:8-29
- **Rule:** A script is described in full by its own help header and the skill that runs it cites it (CLAUDE.md, Persistence: "each described in full by its own help header"; Document chain, External inputs: "how the conversion runs ... is the skill's and the script's header's"; POS.1070). Step 2 retells the hashing, the comparison with `inputs-hash`, the four states and the task files; step 6 retells the whole checklist of docs-check.py (every page present, no page beside the map, links, long dash, front-matter, instance facts with the three examples). `/ingest` step 3 shows the house style: the invocation and one clause.
- **Fix:** Cut steps 2, 5 and 6 to the invocation, the directories the command chooses and what the command does with the result (the `remove` list, a failed page), with "what it does is its header's" for the rest.

### FND.1080 - medium - What `/document` is and what a release does with it is said in CLAUDE.md, in the skill and in `/release`
- **Where:** the release rule: C:\pche\_dev\forge-of-thought\CLAUDE.md:326-328, C:\pche\_dev\forge-of-thought\.claude\skills\document\SKILL.md:72-74, C:\pche\_dev\forge-of-thought\.claude\skills\release\SKILL.md:58-66; the map's place: CLAUDE.md:321-323, 342-345, 374-375, document\SKILL.md:20-21, C:\pche\_dev\forge-of-thought\.claude\agents\docs-planner.md:85; "asks nothing": CLAUDE.md:324-325, document\SKILL.md:9-10 and 70
- **Rule:** POS.1070; CLAUDE.md:325-326 itself says "what it does in full is its skill's", and what a release runs is its own definition's (CLAUDE.md, Persistence). "A release does not run it: it reports the index's age against the intent's version and offers it" stands three times in nearly the same words; where the map lies is said five times; that a run asks nothing twice inside the skill.
- **Fix:** Let `/release` step 5 own what a release does with the documentation and cut CLAUDE.md:326-328 and document\SKILL.md:72-74 to a clause citing it; keep the map's place once in CLAUDE.md, Document chain 5, cited from the skill and the planner; say "asks nothing" once in the skill.

### FND.0980 - medium - What a missing `kind:` header means is said three times, the copies disagree, and the citation reaches no owner
- **Where:** C:\pche\_dev\forge-of-thought\.claude\agents\check-project.md:21-22; C:\pche\_dev\forge-of-thought\.claude\skills\import-project\SKILL.md:19-21; C:\pche\_dev\forge-of-thought\scripts\forge-clone.py:17-18
- **Rule:** One owner per rule, cited by path (CLAUDE.md, prime directive 10; POS.1070). The project check says a ledger without `kind:` is "a finding with the one-line fix"; `/import-project` and the clone script say "a fact, not a defect", the skill citing CLAUDE.md, Persistence, which speaks of a project not under git and not of the header. Unchanged since 2026-10-05 but for the script's extension.
- **Fix:** Give the rule one owner, a sentence in the header comment of `templates/ledger.md`, and cut the three places to a citation of it.
- **Known as:** FND.0980, still open

### FND.0990 - medium - `/spinoff` writes the source assignment by hand where `/forge assignment` and Intent-first are the mechanism
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\spinoff\SKILL.md:27-31
- **Rule:** No direct operation where a mechanism exists (CLAUDE.md, prime directive 10; Working methods, Intent-first; `.claude/skills/forge/states/assignment.md`, Course). Step 5 marks items superseded, writes the link item and the companion itself, without the source intent changing first. Unchanged since 2026-10-05.
- **Fix:** Record the spin-off in the source intent through the `/forge intent` procedure and derive the superseded group through the `/forge assignment` procedure, keeping in `/spinoff` only the DEC and the wording of the link item.
- **Known as:** FND.0990, still open

### FND.1090 - low - The documentation map is a kind of document with no skeleton; its shape is described in the planner and again in the map reader
- **Where:** C:\pche\_dev\forge-of-thought\.claude\agents\docs-planner.md:89-114 against C:\pche\_dev\forge-of-thought\scripts\docs_map.py:5-11; the kind: C:\pche\_dev\forge-of-thought\CLAUDE.md:180; C:\pche\_dev\forge-of-thought\templates\ has no `docs-map.md`
- **Rule:** A file shape has one owner, a skeleton under `templates/` (CLAUDE.md, Templates; POS.1070); where a shape has no owner the finding proposes one. The front-matter fields and the entry form (`### docs/<section>/<page>.md`, `- <field>: <value>`) stand in the planner and in the reader's docstring, which cites SOL.0460 and not the planner.
- **Fix:** Give the map a skeleton, `templates/docs-map.md`, owning the front-matter and the entry with its fields, and let docs-planner.md and docs_map.py cite it by path.

### FND.1100 - low - The Renders row of the documentation index has a shape the ledger skeleton does not own
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\document\SKILL.md:62-64 against C:\pche\_dev\forge-of-thought\templates\ledger.md:38-42
- **Rule:** The ledger's tables are `templates/ledger.md`'s (CLAUDE.md, Ledger; POS.1070). The skeleton says "one row per recipe in recipes/" with the columns Render, Audience, Recipe, Inputs, Generated; the command writes a row for a render that has no recipe, with "the intent's version" for which no column exists.
- **Fix:** Let the Renders comment of `templates/ledger.md` say how the documentation index is rowed (which column carries the map and the version) and cut step 7 to a citation of it.

### FND.1110 - low - That the Format section is never copied into the render is said in six places
- **Where:** C:\pche\_dev\forge-of-thought\CLAUDE.md:279, 292-294; C:\pche\_dev\forge-of-thought\.claude\skills\render\SKILL.md:35-37; C:\pche\_dev\forge-of-thought\templates\recipe.md:29-30; C:\pche\_dev\forge-of-thought\templates\recipe-presentation.md:57; C:\pche\_dev\forge-of-thought\.claude\skills\recipe\genres\presentation.md:11, 44-45
- **Rule:** POS.1070; CLAUDE.md:287-291 says how each step runs is its own definition's. "Content only" and "never copied into the render" stand in CLAUDE.md twice, in the render skill where the act happens, in two skeletons and in a genre checklist.
- **Fix:** Keep the rule in `/render` step 3, where it is acted on, let CLAUDE.md:292-294 cite it in a clause, and delete the sentence from the two skeletons and the genre file (the genre pair is also FND.0650's).

### FND.1120 - low - The two conversion scripts share the text on the claude engine and its installation, where a module beside them is the owner
- **Where:** C:\pche\_dev\forge-of-thought\scripts\md2pptx.py:36-47 against C:\pche\_dev\forge-of-thought\scripts\md2docx.py:56-69 (the skill under either of its names, "installs nothing", the two `/plugin` lines, pandoc from pandoc.org, "resolved from PATH"); C:\pche\_dev\forge-of-thought\scripts\forge_tools.py:1-8 claims "the headless Claude Code run"
- **Rule:** "What several scripts share lives in a module beside them (... `forge_tools.py` ...), never twice" (CLAUDE.md, Persistence, Portability; POS.0830). The two headers carry the same paragraph in slightly different words, and the pandoc install line differs between them already (one names winget and brew, the other does not).
- **Fix:** Let the docstring of `forge_tools.py` own what the claude engine and pandoc need and how each is installed, and cut each header's WHAT IT NEEDS to Python, the module beside it and a citation of that docstring.

### FND.1130 - low - What a README carries is said in CLAUDE.md and in the readme skeleton, and the two disagree
- **Where:** C:\pche\_dev\forge-of-thought\CLAUDE.md:328-329 against C:\pche\_dev\forge-of-thought\templates\recipe-readme.md:18-21, 50-77 and C:\pche\_dev\forge-of-thought\.claude\skills\recipe\genres\readme.md:28-31
- **Rule:** One owner per rule (POS.1070); the skeleton owns the shape of a genre's recipe (`.claude/skills/recipe/SKILL.md:6-12`). CLAUDE.md says "The README is cut to what the thing is, what one gets, how to start and where the documentation is"; the skeleton's Template carries Where it stands, Renders, Waiting on the principal and Layout, and the genre asks which ledger facts appear.
- **Fix:** Let the readme skeleton own what a README carries, brought in line with the cut where that is wanted, and reduce CLAUDE.md:328-329 to a citation of the skeleton.

### FND.1140 - low - The forge dispatcher restates where definitions live and how the chain grows, which Document chain owns
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\forge\SKILL.md:6-10 against C:\pche\_dev\forge-of-thought\CLAUDE.md:209-216
- **Rule:** POS.1070. "Definitions live in `.claude/skills/forge/states/<state>.md` - one file per target state, named after the artefact it produces. Adding a layer means adding a file" is CLAUDE.md, Document chain ("its state file ...; which artefacts the forge has is the listing of that directory, one definition each"), uncited.
- **Fix:** Cut the role paragraph to "the definitions and how the chain grows: CLAUDE.md, Document chain; this dispatcher never changes".

### FND.1150 - low - Reviewer files restate a rule beside the citation of its owner
- **Where:** C:\pche\_dev\forge-of-thought\.claude\agents\check-light.md:22-24 (the parenthesis "the fields in their order, the kinds, one line per record, `Was` last" beside `templates/history.md`); C:\pche\_dev\forge-of-thought\.claude\agents\critic-clarity.md:33-35 (the three Aim clauses beside "stated there and not here"); C:\pche\_dev\forge-of-thought\.claude\skills\critic-contract\SKILL.md:73-77 ("A solution design holds what cannot be read off the thing itself", `.claude/skills/forge/states/solution-design.md:26-27`, uncited where the sentence before cites the assignment's Aim)
- **Rule:** A Lens "names the owner of each rule and never restates it" (`.claude/skills/check-contract/SKILL.md:38-40`; CLAUDE.md, Isolated reviewers; POS.1120) - the rule FND.0690 settled, three new instances.
- **Fix:** Delete the restating clause in each place and leave the citation, adding the owner to the critic contract's sentence on the solution design.

### FND.1160 - low - One-line reminders echoed without naming their owner
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\save\SKILL.md:15-16 (not under git is a property; CLAUDE.md, Persistence); C:\pche\_dev\forge-of-thought\.claude\skills\spinoff\SKILL.md:7-8 (CLAUDE.md, Spin-off rule) and 13-14 (the repository and remote the principal's one-off act; CLAUDE.md, Persistence); C:\pche\_dev\forge-of-thought\.claude\skills\ingest\SKILL.md:38-39 (sources immutable from registration; CLAUDE.md, Versioning & status); C:\pche\_dev\forge-of-thought\.claude\agents\docs-planner.md:20-22 (the stale copy of CLAUDE.md; POS.0950, as the contracts and `/render` step 2 cite it); C:\pche\_dev\forge-of-thought\.claude\skills\new-project\SKILL.md:7-8 and 14 (the same sentence twice in one file)
- **Rule:** A one-line reminder at the point of action is not a restatement only where it names its owner (POS.1070; the rule FND.0700 settled).
- **Fix:** Add the owner in parentheses to each reminder and delete the second sentence of `/new-project`.

### FND.1170 - low - Two state files state one rule twice inside themselves
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\forge\states\intent.md:81-82 and 106-107 (the Mined column of every brief touched is kept); C:\pche\_dev\forge-of-thought\.claude\skills\forge\states\brief.md:49-50 and 154-156 (the Briefs table tracks the mining), 17 and 78 (no IDs enter a brief)
- **Rule:** One owner per rule, inside a file as across files (POS.1070; the pattern of FND.0620).
- **Fix:** Keep each rule in the block that acts on it (the Course for the write, the Target for the shape) and delete the other occurrence.

### FND.1000 - low - When a Renders row is born is said in three places that do not agree
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\recipe\SKILL.md:43-44; C:\pche\_dev\forge-of-thought\.claude\skills\render\SKILL.md:58-59; C:\pche\_dev\forge-of-thought\templates\ledger.md:39-40
- **Rule:** POS.1070. Unchanged since 2026-10-05: `/recipe` registers "when its first render exists", `/render` step 6 mirrors, the skeleton says "one row per recipe in recipes/" while the row "mirrors the render's front-matter provenance".
- **Fix:** Let the skeleton's comment own the moment ("one row per rendered recipe, written by `/render`"), cite it from `/render` step 6 and delete the sentence from `/recipe`.
- **Known as:** FND.1000, still open

### FND.1010 - low - Two script headers echo the commit-identity rule without naming its owner
- **Where:** C:\pche\_dev\forge-of-thought\scripts\forge-save.py:26-31; C:\pche\_dev\forge-of-thought\scripts\forge-clone.py:12-15
- **Rule:** POS.1070; the owner is CLAUDE.md, Persistence (431-439, 451), which `forge_repos.py:7-9` cites in the house style. The text survived the rewrite from PowerShell to Python unchanged.
- **Fix:** Cut each to one sentence ending "(CLAUDE.md, Persistence)".
- **Known as:** FND.1010, still open

### FND.0650 - low - Genre checklists repeat the rules their skeletons carry
- **Where:** C:\pche\_dev\forge-of-thought\.claude\skills\recipe\genres\presentation.md:7-11, 23-25, 33-34 against C:\pche\_dev\forge-of-thought\templates\recipe-presentation.md:13-17, 20-22, 26-28, 41-44; C:\pche\_dev\forge-of-thought\.claude\skills\recipe\genres\readme.md:5-6, 22-26 against C:\pche\_dev\forge-of-thought\templates\recipe-readme.md:8, 13-15, 18-21
- **Rule:** POS.1070; the genre file "carries the elicitation checklist and points at the canonical skeleton" (`.claude/skills/recipe/SKILL.md:6-9`). The picture-from-a-render clause, the Mermaid constraint, "source material, never the presentation itself", the input sets per kind and the README's output path stand in checklist and skeleton alike.
- **Fix:** Let each checklist item ask its question and leave the rule to the skeleton it points at.
- **Known as:** FND.0650, still open (parked)

### FND.0630 - low - Artefacts named by name in Isolated reviewers where Document chain says they are listed nowhere else
- **Where:** C:\pche\_dev\forge-of-thought\CLAUDE.md:590-592 against 214-216
- **Rule:** Rosters are the scan of their files and are named nowhere else (POS.1070; CLAUDE.md:215: "they are listed nowhere else"). The parenthesis "(`brief`, `brief-<name>`, `intent`, `assignment`, later layers)" stands unchanged, still without the solution design the directory holds.
- **Fix:** Cut the parenthesis to "an artefact named as `/forge` names it, by its state file".
- **Known as:** FND.0630, still open

### FND.0620 - low - Rules echoed inside CLAUDE.md, section to section
- **Where:** the layer a project does not have is not missing: C:\pche\_dev\forge-of-thought\CLAUDE.md:13-14, 217-219, 634-636 (the owner the others cite: Ledger); the authorship boundary between chain and render: CLAUDE.md:166-168 against 276-279
- **Rule:** One owner per rule, inside a file as across files (POS.1070). The first instance stands as on 2026-10-05; the second is new to this report: Document kinds says the artefacts are "the ones the principal composes ... and the renders are generated from", Document chain 4 says "a chain artefact is composed by the principal, a render is generated from artefacts".
- **Fix:** Keep the layer rule in Ledger with a clause in Document chain pointing to it, and keep the authorship boundary in Document chain 4 with Document kinds reduced to the label "the documents of the chain".
- **Known as:** FND.0620, still open
