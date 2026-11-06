---
date: 2026-11-01
project: forge
check: documentation
target: the engine (C:\pche\_dev\forge-of-thought), the documentation run of 2026-11-01 at intent 6.8
reviewer: the documentation run
---

# Check (documentation) — the engine — 2026-11-01

23 findings

What the documentation run of 2026-11-01 at intent 6.8 could not place: the planner's Unowned list and the matters where the map and its owner, or two owners, disagree; the claims the map asked for and no named input carried; the facts the map asked a roster page to carry and no owner states; and every place where a page wanted a reason and no file records one. Filed by the run itself (POS.1450), from the planner's report and the writers' hand-backs; a mend lands in the owner, never on a page. The open findings of the report of 16:24 (FND.3180, FND.3190, FND.3200, FND.3210, FND.3230, FND.3240, FND.3250, FND.3260, FND.3270, FND.3280, FND.3300, FND.3340, FND.3350, FND.3360, FND.3370, FND.3380, FND.3390, FND.3400, FND.3440, FND.3480) were met again by the writers of this run, each page saying the reason is not recorded; they stand as they are and are not filed twice. FND.3100 and FND.3160 of that report are carried in the owners' wording by this map and are resolved by it.

## Findings

### FND.3580 — medium — Unowned: how a merge request's branch is fetched onto the integrator's clone and the merge started there
- **Where:** CLAUDE.md, Persistence (the integrator merges on his own clone with git itself, outside the forge's scripts); scripts/hook-git.py, the header (`git merge <branch>` typed by Claude runs on the ask); no file says how the branch gets onto the clone. Needed by docs/about/working-together.md and docs/use/settle-a-conflict.md, which say only what the owners say.
- **Rule:** A page states what an owner states (the documentation contract); a fact without an owner waits for the principal to give it a home (the document skill, step 7).
- **Fix:** Decide where the fetch is said: one sentence in CLAUDE.md, Persistence, or in the hook's header among the commands that run on the ask; then the map entries cite it.

### FND.3590 — medium — Two owners disagree on the published files at a merge: the way-2 list of the intent counts them among the files taken as `ours`, POS.1690 and the attributes template make them `binary`
- **Where:** projects/forge/10-intent.md:1751-1755 (way 2, derived: "... the state render and the published files, in git, made only on main, `ours` at a merge and made again"); projects/forge/10-intent.md POS.1690 (`merge=ours` on the renders, the documentation, the state render and the published companions, `binary` on the published files); templates/gitattributes (published/*.md merge=ours; published/*.pptx and *.docx binary). The page docs/about/working-together.md follows the template.
- **Rule:** One mechanism lives in one place (CLAUDE.md, prime directive 10); two statements of one rule that differ are a defect.
- **Fix:** Bring the way-2 list of the intent to POS.1690's wording: the published companions `ours`, the published files `binary`; a record in the intent's history.

### FND.3600 — medium — The map entry of docs/use/upgrade-the-engine.md names the checks before the migration; CLAUDE.md says the checks on an unmigrated project stop
- **Where:** projects/forge/docs-map.md, the entry of docs/use/upgrade-the-engine.md (`says`: the checks, then the migration); CLAUDE.md, Persistence ("Until a project is migrated nothing writes into it: the map, the checks and every writing command say what templates/project.md says and stop"). The writer put the migration first and said so on the page.
- **Rule:** The map carries the owner's order, never its own (the documentation contract; the planner's definition).
- **Fix:** The entry's `says` takes the owner's order: the migration, then the checks; the page then stands as written.

### FND.3610 — medium — Claims the map asked for and no named input carries, in seventeen entries
- **Where:** projects/forge/docs-map.md, the entries of: docs/about/the-check.md (`/save` runs `light` unless told otherwise: POS.1100; `/release` runs the `engine` check: the release skill); docs/about/the-assignment.md (who the recipients may be: CLAUDE.md, What this workspace is); docs/about/the-brief.md ("since the mining changes the intent and not the brief", stated as a reason by no file); docs/about/projects-and-the-engine.md ("seamless work inside" as a reason for the split, no file); docs/about/working-methods.md (the reason for Intent-first, "a lower layer that takes a change the intent does not carry drifts from it", no file); docs/about/renders-and-recipes.md (a work product is not a render: CLAUDE.md, Document kinds); docs/about/upgrades-and-migration.md ("which a hand migration cannot promise", no file); docs/extend/add-a-script.md ("options" and "where the output lands" as parts of the docstring: SOL.0620 names synopsis, what it does, what it needs, examples); docs/extend/add-a-recipe-genre.md (no check of the engine reads a genre file, no file); docs/start/what-it-is.md ("real sessions cut to a few minutes", no file; why the reviewers are blind: POS.0400, not the Essence); docs/start/first-result.md (one question per message and the word `write`: CLAUDE.md, Working methods); docs/use/work-on-a-branch.md (the documentation run and `/publish` from main only: CLAUDE.md, Persistence); docs/use/publish-a-designed-file.md (a screenplay has no published file: CLAUDE.md, Document chain, Renders); docs/about/how-a-thought-travels.md and docs/about/the-research.md (why a source and a note are immutable: POS.1040 holds the reason, the entries name POS.0180 and the research positions); docs/about/the-critic.md, docs/about/the-ledger.md and docs/about/isolated-reviewers.md (the state and severity words of a finding: templates/ledger.md and the check contract, not among the inputs). Each writer kept the claim as the `says` directs, or left it out and said so.
- **Rule:** A page states only what its named inputs carry, and the map names every input a page is made from (the documentation contract; the planner's definition, the map's inputs).
- **Fix:** For each entry either add the owner to its inputs where one exists, or cut the claim where no file states it; the pages take it at the next run.

### FND.3620 — medium — Input anchors the state script cannot isolate: a heading that does not exist, a heading hashed to the next heading, a part cut at a fence
- **Where:** projects/forge/docs-map.md: `.claude/skills/forge/states/brd.md#Inputs` (the entry of docs/use/share-material-through-a-library.md; the definition has a bold paragraph "**Inputs.**", no heading); `CLAUDE.md#Persistence (git)` (hashed to the next heading, the planner's Did not fit); the three contracts' `#Output` parts cut at the code fence; `recipes/release-notes.md#Template` unusable as a part. Carried forward from the previous map, not filed before.
- **Rule:** An input of an entry is a file or a part the state script can hash, so that a change in the owner regenerates the page (SOL.0460; the docs-state header).
- **Fix:** Name the whole file where the part has no heading, or give the owner the heading the map needs (the BRD definition's Inputs as a heading is the one-line form), on the principal's word.

### FND.3630 — medium — The roster pages carry columns no owner states: "When it fits", "Run by", the creating command, the meaning of a flag or a git key
- **Where:** docs/reference/artefacts.md, docs/reference/challenger-personas.md, docs/reference/checks.md and docs/reference/recipe-genres.md ("When it fits", the writers' reading of each description or Lens); docs/reference/scripts.md ("Run by" for forge-status.py, forge-branch.py, forge-check.py and md2video.py, whose docstrings name no command); docs/reference/templates.md (the creating command of ten skeletons, inferred); docs/reference/commands.md ("guarded" glossed as "runs only when the principal types it"; the semantics of `--engine`, `--bundle`, `--tag`, `--auto`, `--quick`, `--deep` from the hints only); docs/reference/configuration.md (what `merge.renormalize` does) and docs/start/setup.md (what `--zdiff3` does), both glosses from the key name. Each writer said so in its hand-back.
- **Rule:** Nothing is invented to fill a gap; a fact without an owner waits for the principal to give it a home (the document skill, step 7; the documentation contract).
- **Fix:** Decide per column: an owner gets the fact (a line on when it fits in each definition's description, a command in each script's docstring, a sentence in forge-config.py's header on the two git keys), or the map stops asking for the column.

### FND.3640 — medium — THR.0590 is open in the intent on what `/document <slug>` reads for a project, while the planner's definition and the document skill state it
- **Where:** projects/forge/threads/THR.0590.md (open); .claude/agents/docs-planner.md, What you read; .claude/skills/document/SKILL.md, Target and places. The map takes the operating layer's wording and cites no thread (the planner's Did not fit); FND.3100 is resolved by it.
- **Rule:** A thread is one open matter of the intent; a matter the operating layer has settled is either carried into a position and the thread closed, or the operating layer waits (the intent's definition, Threads and files).
- **Fix:** Close THR.0590 with its answer carried into POS.1450, or say in the thread what still stands open beyond what the operating layer does.

### FND.3650 — medium — The BRD definition's head points at the brief while POS.1800 exists, and POS.1800 names a fork and the company while the definition names library documents
- **Where:** .claude/skills/forge/states/brd.md, the head; projects/forge/10-intent.md POS.1800 (the planner's Did not fit, carried forward from the previous map, not filed before). The pages docs/about/the-brd.md and docs/use/write-a-brd.md take the definition's wording.
- **Rule:** A definition's head cites the position that owns it, and a position names no instance (POS.0950; the shape of a definition, POS.1310).
- **Fix:** Point the head at POS.1800 and bring POS.1800 to the definition's wording, library documents of the instance cited by path, with a record.

### FND.3660 — low — SOL.0830 still describes the fixture project deleted today
- **Where:** projects/forge/40-solution-design.md SOL.0830; DEC.0360 (the fixture deleted on 2026-11-01); templates/project.md:11 and the `fixture` field read by forge_repos.py, forge-migrate.py and forge-clone.py describe the kind, not the instance (the engine check of 19:20, Facts). No page names the fixture (the entries' must-not).
- **Rule:** The solution design is kept current: a part that describes what no longer exists is a part to change (the solution design's definition).
- **Fix:** Say in SOL.0830 that the fixture is a kind a project may declare and that no fixture project exists, or remove the part, on the principal's word.

### FND.3670 — low — The research skill names `antigravity` literally in step 3 while step 5 uses `<name>`
- **Where:** .claude/skills/research/SKILL.md:83 (`python scripts/forge-engine.py antigravity --packet ... plan-review/antigravity.md`) against :116 (`forge-engine.py <name> ... <card>.<name>.md`). Noted by the writer of docs/extend/add-an-engine.md: a second row of the engine table would make step 3 read as the first engine's only.
- **Rule:** The research skill names an engine by `--engine <name>`, a row of the engine table (the skill's own head).
- **Fix:** immediate fix: `<name>` in step 3 as in step 5, wording otherwise unchanged.

### FND.3680 — low — Owner wording the planner had to read around: the merge driver in the singular, `forge-branch <name>` in POS.1110, forge-check.py as the trial of THR.0530 with its new `light <slug>` form, the walkthrough skill's date, the design head's list of unanswered positions
- **Where:** CLAUDE.md, Persistence and POS.1690 (the driver `ours` named once where the registration carries several settings); projects/forge/10-intent.md POS.1110 (`forge-branch <name>` where the script takes a slug and a branch); scripts/forge-check.py, the header (the trial of THR.0530, now with `light <slug>`); .claude/skills/walkthrough/SKILL.md (a date in its head); projects/forge/40-solution-design.md, the head (a list of positions not yet answered). The planner's Did not fit, carried forward from the previous map, not filed before.
- **Rule:** A header carries nothing that changes with a round (POS.1570); a position names a mechanism as it is (CLAUDE.md, Working methods, Plain speech).
- **Fix:** Five small wordings, each on the principal's word: the registration named as the driver and its settings, POS.1110's example brought to the script's arguments, the forge-check header's trial sentence made current, the walkthrough skill's date dropped, the design head's list moved to its history or kept as a fact.

### FND.3690 — low — Reason not recorded: why items are numbered in tens and each group starts at the next hundred, and why at a clash the older item keeps its number
- **Where:** CLAUDE.md, ID scheme; projects/forge/10-intent.md POS.0220. docs/about/stable-ids.md says the reason is not recorded.
- **Rule:** A page gives the reason its owner records, or says it is not recorded (the documentation contract).
- **Fix:** One sentence of reason in POS.0220, or none; the page takes it at the next run.

### FND.3700 — low — Reason not recorded: why a bundle is catalogued in two levels and never deeper, and why a source carries a plain slug filename
- **Where:** CLAUDE.md, Document chain, External inputs; projects/forge/10-intent.md POS.0180. docs/about/sources-and-research.md.
- **Rule:** as FND.3690.
- **Fix:** A sentence of reason in POS.0180, or none.

### FND.3710 — low — Reason not recorded: why a position is dated once rather than carrying its earlier dates, and why the intent's audience is the principal and Claude only
- **Where:** .claude/skills/forge/states/intent.md; templates/intent.md (the audience in the header). docs/about/the-intent.md states both as rules without a reason.
- **Rule:** as FND.3690.
- **Fix:** A sentence of reason in the intent's definition, or none.

### FND.3720 — low — Reason not recorded: why the challenger has no stake in the principal being right, beyond "signal, not encouragement"
- **Where:** .claude/skills/challenger-contract/SKILL.md; projects/forge/10-intent.md, the reviewer positions. docs/about/the-challenger.md. Near FND.3210, which asks for the reasons of three other rules of the challenger.
- **Rule:** as FND.3690.
- **Fix:** A sentence of reason in the contract's owner position, or none.

### FND.3730 — low — Reason not recorded: why regression comes first in a critique, and why a report is written in English
- **Where:** .claude/skills/critic-contract/SKILL.md (regression first; the report in English). docs/about/the-critic.md says both are not recorded. The language of a report is CLAUDE.md, prime directive 6's (records are English, read by Claude and the checks), which was not an input of the entry.
- **Rule:** as FND.3690.
- **Fix:** The English of a report: add prime directive 6 to the entry's inputs; regression first: a sentence of reason in the contract's owner, or none.

### FND.3740 — low — Reason not recorded: Propose never decide, Intent-first and Recommend do not push
- **Where:** CLAUDE.md, Working methods; projects/forge/10-intent.md POS.0140 and the Working methods group. docs/about/working-methods.md says the reason of each is not recorded (POS.0010, POS.0070 and POS.0020, cited by the group, were not inputs of the entry).
- **Rule:** as FND.3690.
- **Fix:** Add the cited positions to the entry's inputs where they carry the reason; a sentence of reason in the group where none does.

### FND.3750 — low — Reason not recorded: why the way to an item goes into its record and not the item, and why the log is the single primary of the commit messages and the release notes
- **Where:** CLAUDE.md, Versioning & status; projects/forge/10-intent.md POS.0730. docs/about/versioning-and-history.md.
- **Rule:** as FND.3690.
- **Fix:** A sentence of reason in POS.0730, or none.

### FND.3760 — low — Reason not recorded: why the solution design is kept current and never finished rather than closed at approval
- **Where:** .claude/skills/forge/states/solution-design.md; the design positions of the intent. docs/about/the-solution-design.md. Beside FND.3370 (why it cites the layer above by ID).
- **Rule:** as FND.3690.
- **Fix:** A sentence of reason in the definition's Aim, or none.

### FND.3770 — low — Reason not recorded: why `.mp4` files never enter the tree, what the division of an output into two commands by cost was chosen against, and why a recipe's Format names one format, never both
- **Where:** projects/forge/10-intent.md, the screenplay and player positions (POS.1540 among them); projects/forge/40-solution-design.md (the two-command division, "not recorded" in the design itself); templates/recipe.md, the Format section. docs/about/the-screenplay-and-its-player.md.
- **Rule:** as FND.3690.
- **Fix:** A sentence of reason at each owner, or none.

### FND.3780 — low — Reason not recorded: why the documentation's index carries one question per page, beyond `/man` reading it
- **Where:** scripts/docs-index.py, the header; projects/forge/10-intent.md POS.1450. docs/about/the-documentation.md.
- **Rule:** as FND.3690.
- **Fix:** A sentence of reason in POS.1450, or none.

### FND.3790 — low — Reason not recorded: why the organisation's content lives in a library of the instance while the engine carries a generic Map
- **Where:** projects/forge/10-intent.md POS.1800. docs/about/the-brd.md. Beside FND.3340 (the stakeholders' sign-off).
- **Rule:** as FND.3690.
- **Fix:** A sentence of reason in POS.1800, or none; FND.3650 touches the same position.

### FND.3800 — low — Reason not recorded: why a rule of conduct was not enough and the door to git became a wall of the harness; why no alternative was weighed against one always-on core; why the principal owns every decision beyond "amplifier, never substitute"; why forge-config.py has a guard and why the hooks answer as they do; why the scripts run on Linux and macOS
- **Where:** projects/forge/10-intent.md POS.1200 and POS.1710 (the wall; docs/about/persistence-in-git.md, beside FND.3270); projects/forge/40-solution-design.md, the always-on core ("no real alternative, the intent records none"; docs/about/how-the-rules-are-held.md); POS.0070 (docs/about/what-it-is-and-is-not.md); scripts/forge-config.py and the two hooks' headers (docs/reference/scripts.md); POS.0830 (docs/extend/add-a-script.md).
- **Rule:** as FND.3690.
- **Fix:** A sentence of reason at each owner, or none; the pages state the rules and say where the reason is not recorded.

## Facts
- The run: 101 entries, all regenerated (the inputs of eleven entries were split from one line into their own lines, so their hashes changed; the intent moved from 6.4 to 6.8), none new, none removed; 53 mirrored pages on the faster model, 48 derived on the session model; six pages failed the check once (long dashes in quoted descriptions on four, an instance fact on two) and passed after one regeneration; the index derived at 6.8.
- The planner's choices that are not findings: "engine" in two senses plus the conversions' third is glossed per page; the course page and the install addresses are allowed on start pages only; docs/start/what-it-is.md is an explanation in `start/`; the documentation agents are not called reviewers; the recipes' author and channel facts stay off the pages; the docstrings' example slugs and names are replaced by placeholders; `/man` reads the index the planner never reads.
- Writers' readings beyond their inputs, said on the pages or in their hand-backs and not filed: the example `REQ.10000` in place of the owner's `POS.10000`; "whatever reads the intent" for POS.1680's driver; "a lens not on the roster does not run"; "nothing to pull" for a project not under git; the version checks as the sign a tool is on PATH.
