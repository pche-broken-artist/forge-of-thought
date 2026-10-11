# Documentation audit: Forge of Thought `docs/`, 2026-10-11

- **What this is:** a structured record of one audit of the generated documentation in `docs/` against the forge's own intent (`projects/forge/10-intent.md`, above all POS.1450, POS.1470, POS.0950). It records measurements, findings with evidence, where each finding should be mended, and what was not verified. It decides nothing and changes nothing.
- **Subject:** `github.com/pche-broken-artist/forge-of-thought` at commit `04e332a` (2026-10-11). The documentation was generated 2026-10-09/10 for intent 5.0; the intent at this commit is 5.1.
- **Written by:** Claude, 2026-10-11, in a session outside the forge, from a read-only clone. The intent was read in full by the main session. Every page of `docs/` was read in full by one of six isolated read-only agents, one per part (Start with the index and the root README; Use; About in two halves; Extend; Reference), each comparing its pages with the owner files they name. A mechanical pass measured the tree (section 2).
- **Status of a finding:** `verified` means the main session re-checked the quoted evidence against the files. `reported` means the evidence comes from one of the six agents and was not re-checked; line numbers and quotes are theirs. `measured` means the figure comes from a script. As a sample, 37 quoted phrases from `reported` findings were searched for in the files they are attributed to and all 37 were found; their line numbers were not re-checked.
- **Severity:** Critical = a reader of the kind the page is written for fails at his goal, or a core claim is false. High = a goal is reached only with outside help, or a central page is wrong. Medium = costs time or trust. Low = polish. Severity is the auditor's judgement.
- **Where a mend belongs:** the pages are generated and never edited by hand (POS.1450), so every remedy names the file to change: an owner (`CLAUDE.md`, a skill, a script, the readme recipe's pinned facts), the map (`projects/forge/docs-map.md`), the writer (`.claude/agents/docs-writer.md`), the planner (`.claude/agents/docs-planner.md`), the contract (`.claude/skills/docs-contract/SKILL.md`) or the intent.
- **Item numbering:** M = measurement, F = finding, C = contradiction inside the owners, W = what works. Numbers are stable within this record. Each finding also carries a `key`, a slug meant to stay the same across later audits so that a finding can be followed from one record to the next.
- **Limits:** no forge command was run and nothing was installed, so every statement about what a command or a script does at run time is read from its text. Rendering on GitHub was not looked at. Behaviour of Claude Code itself (hooks, skills, plugins) was not tested.

---

## 1. Verdict

The documentation keeps the form POS.1450 asks for: five sections, 83 pages of one topic each, every page opening with what it is for and for whom, all links resolving, no instance fact, no chain ID on a page. Where the owners have not moved since the run, mirrored pages follow them closely.

Three things carry most of the damage:

1. **It is behind the repository.** The commit that brought intent 5.1 added `/pull` and `/end`; neither occurs anywhere in `docs/`, and the forge's own state script marks 78 of 83 pages for regeneration.
2. **The newcomer's path in Start does not end in a saved result** if followed literally.
3. **About does not tell the evaluator in plain words what the thing is,** has no example and no picture in 33,000 words, and repeats itself.

Most findings have their cause in the generator (the writer's page shape, the contract's rules, the `must-not` lines of the map) or in an owner, not in a page.

Judgement by section (the auditor's, not measured):

| Section | Structure | Readability | Comprehensibility | Accuracy at `04e332a` |
|---|---|---|---|---|
| Index | weak | weak | n/a | says 5.0, intent is 5.1 |
| Start (4) | good | fair | weak: the user gets stuck | fair |
| Use (24) | fair: no shared skeleton | good | fair | `/pull`, `/end` missing; upgrade page superseded |
| About (25) | fair | weak | weak | fair: several unsupported or contradicting statements |
| Extend (10) | fair | weak to fair | fair | fair |
| Reference (20) | good | good | good | `commands.md` and `scripts.md` no longer hold |

---

## 2. Measurements

Taken with one read-only script over `docs/` (body text without front-matter; words counted without code blocks; a sentence is counted only in prose paragraphs, not in lists, tables or headings; duplication is the share of a page's 8-word sequences that also occur on another page, the closing "See also" list left out).

| # | Measure | Value |
|---|---|---|
| M.01 | Pages (without the index) | 83 |
| M.02 | Words on the pages | 78,555 (86,594 by `wc -w` over all 84 files, front-matter, code and index included) |
| M.03 | Index entries: number; median words; longest; entries of 40 words or more | 83; 50; 187; 56 |
| M.04 | Links in the body of pages; links in the closing "See also" lists | 8; 185 |
| M.05 | Broken relative links | 0 |
| M.06 | Pages no other page links to | 12: `about/languages.md`, `about/where-it-is-going.md`, `extend/add-a-check.md`, `extend/add-a-command.md`, `extend/add-a-critic-lens.md`, `extend/add-a-recipe-genre.md`, `extend/add-a-script.md`, `reference/glossary.md`, `reference/templates.md`, `start/what-it-is.md`, `use/bring-in-an-existing-project.md`, `use/spin-off-a-group.md` |
| M.07 | Links to the glossary from any page | 0 |
| M.08 | Duplication, all pages; About only | 7 %; 11 % |
| M.09 | Most duplicated pages | `about/the-principal-and-claude.md` 24 %, `about/the-solution-design.md` 19 %, `about/what-it-is-and-is-not.md` 17 %, `about/isolated-reviewers.md` 16 %, `about/the-document-chain.md` 16 %, `about/how-the-rules-are-held.md` 16 % |
| M.10 | Diagrams and images in `docs/` | 0 |
| M.11 | Pages marked `regenerate` by `scripts/docs-state.py` at `04e332a`; at the commit before (`8ad5714`) | 78 of 83; 16 of 83 |
| M.12 | Version in the index front-matter; version of the intent | 5.0; 5.1 |
| M.13 | Rows of the Commands table in `CLAUDE.md`; rows on `reference/commands.md`; occurrences of `/pull` or `/end` in `docs/` | 23; 21; 0 |
| M.14 | Pages naming all of `CLAUDE.md` as an input; all of the intent | 72 of 83; 32 of 83 |
| M.15 | `scripts/docs-check.py projects/forge/docs-map.md docs` | "84 files checked, no failure" |
| M.16 | Distinct H2 headings in `docs/use/`; of them on one page only | 106; 98 |
| M.17 | Pages `made: mirrored`; `made: derived` | 46; 37 |
| M.18 | Occurrences of the word "AI" in `docs/` | 1 (`extend/how-a-change-is-made.md`) |

By section:

| Section | Pages | Words | Code blocks | Pages with no code block | Tables | Mean words per sentence | Sentences of 30 words or more | Duplication | he / his / him | you / your |
|---|---|---|---|---|---|---|---|---|---|---|
| start | 4 | 2,696 | 4 | 2 | 0 | 19.6 | 15 % | 4 % | 6 | 58 |
| use | 24 | 14,218 | 15 | 15 | 2 | 15.6 | 7 % | 3 % | 17 | 266 |
| about | 25 | 33,159 | 0 | 25 | 2 | 21.8 | 22 % | 11 % | 120 | 2 |
| extend | 10 | 11,439 | 0 | 10 | 2 | 20.5 | 21 % | 7 % | 5 | 61 |
| reference | 20 | 17,043 | 20 | 16 | 61 | 15.5 | 8 % | 5 % | 7 | 4 |

Note on M.11: `docs-state.py` writes the computed state into the map. The run was made in a throwaway copy and the map of the clone was restored.

---

## 3. Findings

### Critical

#### F.01 `first-result-not-saved` (Critical, verified)
- **Where:** `docs/start/first-result.md`; the same gap in `README.md:176-180`.
- **Evidence:** line 17-18 promises "from nothing to a saved intent, in three commands and one short conversation"; the block at 28-32 shows `/new-project`, `/forge intent`, `/save`. The act that makes a save possible stands only in an aside after the save is described, lines 108-110: "If you want this first intent saved, do the one-off act before `/save`: `git -C projects/my-idea init -b main`, then a remote if you want one." The page does not say where to type it or that Claude cannot: `.claude/settings.json` denies `Bash(git *)` and `PowerShell(git *)`.
- **Second half, inferred from the files and not run:** the identity `/setup` offers is keyed to a remote URL (`.claude/skills/setup/SKILL.md:36`, `[includeIf "hasconfig:remote.*.url:https://<host>/**"]`) together with the guard `user.useConfigOnly = true`. A project without a remote, which the page presents as a choice, then resolves no identity, and `scripts/forge-save.py:50-53` prints "no commit identity - git resolves none for this host" and commits nothing. The page has no path for this outcome.
- **Fix in:** the map entry of the page (`says`), and the Quickstart of the readme recipe. Make the `git init` a numbered step before the save ("in your own terminal, at the engine root"), say that Claude is not allowed to run git, add "if `/save` saves nothing" with the two remedies the script itself names, and drop "three commands".

#### F.02 `no-plain-statement-of-what-it-is` (Critical, verified)
- **Where:** `docs/about/what-it-is-and-is-not.md`, `docs/about/how-a-thought-travels.md`, `docs/start/what-it-is.md`.
- **Evidence:** the word "AI" occurs once in all of `docs/` (M.18). `about/what-it-is-and-is-not.md:22-23` opens: "Forge of Thought is a place for forging thoughts: a workshop where thought is tempered and shaped." The first plain statement of what the thing physically is stands on another page, `about/how-a-thought-travels.md:34-35` ("It is a set of instructions that Claude Code reads"). The same page says at 28-29 "Two people are at work: the principal ... and Claude". Nobody is told that Claude is an AI model. Against POS.1470: "No metaphor and no invented word stands for a mechanism of the forge".
- **Fix in:** the map entries of the two entry pages. Open with three plain sentences: it is a set of instructions, agents and scripts for Claude Code (an AI coding assistant); one person works with it to write a numbered series of versioned Markdown documents; separate AI reviewer agents that never see the conversation criticise them. Replace "Two people" by "one person and an AI assistant".

### High

#### F.03 `stale-against-head` (High, verified)
- **Where:** all of `docs/`; worst on the pages below.
- **Evidence:** M.11, M.12, M.13. `/pull` and `/end` (`CLAUDE.md:681-682`, `.claude/skills/pull/SKILL.md`, `.claude/skills/end/SKILL.md`) occur nowhere in `docs/`.
  - `docs/reference/commands.md`: 21 rows against 23 (verified).
  - `docs/use/upgrade-the-engine.md:44-52` teaches `python scripts/forge-pull.py forge` and says "You see one line per repository: `up to date` in green when it went through"; `scripts/forge-pull.py:73-76` now prints `pulled <before> -> <after>` with the commits between, and `CLAUDE.md:488` makes `/pull` "the door inward" (verified).
  - `docs/reference/scripts.md:68` gives `python scripts/forge-status.py` without `[--remote]` (`scripts/forge-status.py:7`); the diverged refusal and the before/after report of `forge-pull.py` are missing (reported).
  - `docs/use/see-where-a-project-stands.md:24-25` does not mention the state against the origin that the map now shows (`.claude/skills/forge/SKILL.md:20-24`) (reported).
  - `docs/about/persistence-in-git.md:58` "Two doors, two speeds" knows only save and release (reported; that the page has no `/pull` is verified).
  - `docs/about/projects-and-the-engine.md:145-147` still carries the 5.0 wording of the upgrade, which the intent's history records as `Was` (reported).
  - The lists of guarded commands at `docs/extend/add-a-command.md:66-69` and `docs/about/how-the-rules-are-held.md:142-144` lack `/pull` (`projects/forge/10-intent.md:1335`) (reported).
- **Also:** only the index carries a version. A page says `generated: 2026-10-10` and nothing of what it was made for, so a reader landing on a page cannot see that it is behind.
- **Fix in:** two new map entries (pull, end), the two skills added to the inputs of `reference/commands.md`, then `/document`. For the visibility: a line "made for version X" on every page, in the writer's page shape.

#### F.04 `install-python-and-clone` (High, verified; the alias point is inferred)
- **Where:** `docs/start/install.md`; owner `projects/forge/recipes/readme.md:262` (pinned facts).
- **Evidence:** line 63-65 "give it the name `python`: by an alias, or by the `python-is-python3` package where your distribution offers it". The hook is started without a shell (`.claude/settings.json`: `"command": "python", "args": [...]`; `scripts/hook-walkthrough.py:20` "invokes this script in exec form"). A shell alias does not reach a process started that way; this is general operating system behaviour and was not run. macOS has no such package, so macOS is left with the alias. Cloning is "## 5." (line 129), after "## 4. Optional tools" which the page itself says is not needed to start, and line 136 says "Clone it with git" without a command.
- **Fix in:** the pinned fact first (a real `python` executable on PATH, one command per platform), then the map entry: order git, Python, Claude Code, clone, start, optional tools last, with the literal `git clone <address>` and `cd`.

#### F.05 `no-success-criteria-in-start` (High, reported; confirmed for `install.md` by reading)
- **Where:** all four Start pages.
- **Evidence:** `install.md:45-46` "check that `git` answers in a terminal" and :60 "Make sure the command `python` works" give no command and no expected output; 144-148 start `claude` and name no sign that the forge loaded. `setup.md:72-76` names the next command, not the two files that should now exist. `first-result.md` has no end state after `/save`.
- **Fix in:** the writer's shape for a how-to: every step closes with one line "you should now see ...".

#### F.06 `portability-claimed-as-fact` (High, verified)
- **Evidence:** `README.md:130-131` "the scripts are Python and run unchanged on Windows, Linux and macOS". Against `projects/forge/40-solution-design.md:746-747` "Portability is not verified: the set has not been run on Linux." and `projects/forge/10-intent.md:1202-1203` "until then it is a writing rule, not a claim". `docs/start/install.md:67` hedges ("written to run unchanged") but then concludes "nothing in them is bound to one platform".
- **Fix in:** the readme recipe and the map entry of `install.md`: "developed on Windows; written to be portable, not yet run on Linux or macOS".

#### F.07 `index-not-scannable` (High, measured)
- **Where:** `docs/README.md`; `scripts/docs-index.py`; the map's `says` field.
- **Evidence:** M.03. The brief `documentation` asks for an index that "lists every page in one line". The entries reproduce the map's `says`, the page's brief for its writer. `docs/README.md:52` (Release a version) is one sentence of 187 words; :28 (Install) has 137; :29 (Set up) has 16.
- **Fix in:** `templates/docs-map.md` and the planner: a separate short field per entry (one line, the question the page answers), which `docs-index.py` prints in place of `says`.

#### F.08 `reader-paths-not-paths` (High, verified)
- **Where:** `docs/README.md:21-23`.
- **Evidence:** "- **the user**: `start/`, then use/ for every job." / "- **the evaluator**: `about/`, the concept pages, nothing made for him alone." The paths are directory names, not links, with uneven code formatting. The evaluator's path is all of About: 25 pages and 33,159 words in no order. POS.1450 asks for an index that "names each reader's path through them".
- **Fix in:** `scripts/docs-index.py` and the map's header: each path as three to five linked pages in order.

#### F.09 `pages-do-not-stand-alone` (High, measured; term lists reported)
- **Where:** all sections. Cause: `.claude/agents/docs-writer.md:74` "Links go only to the pages the entry lists under `links`", and the shape that puts links only under "See also".
- **Evidence:** M.04, M.06, M.07. Terms of the forge are used before they are explained and are not linked. Samples of first uses with no definition and no link (reported): `start/first-result.md` "mines" (30), "light check" (31), "ledger", "history companions" (46-49), "round" (74), "reality check" (85); `about/how-a-thought-travels.md` "the finding" (44), "trunk" (58), "mined" (62), "subagent" (149); `about/isolated-reviewers.md` "lens", "persona", "FND", "CHL" (29-30), "session model" (62), "ledger" (84); `extend/*` "principal" on 8 pages, "operating layer", "harness", "roster", "bare".
- **Fix in:** the writer: allow a link at the first use of a term to its About page or to the glossary, and a half-sentence gloss for the few words every page needs (principal, ledger, walkthrough, subagent, harness).

#### F.10 `glossary-misses-core-terms` (High, verified for seven terms; the rest reported)
- **Where:** `docs/reference/glossary.md`; its map entry (`projects/forge/docs-map.md:1515` onward).
- **Evidence:** not terms of the glossary (verified): chain, slug, roster, provenance, operating layer, harness, hook. Reported as missing as well: kind, reviewer, skeleton, entry, front-matter, group, bare, writer, planner, verdict, Lens section, working method, guarded, "the only door", state map, trunk, light check, deny rule, mining, state file, Action required, prime directive, upgrade channel, handing over, house scheme, "whole" as a noun, extender, evaluator. "the chain" is used inside the glossary's own definitions.
- **Fix in:** the map entry: add the terms and, as inputs, the documentation contract, the walkthrough skill and the agent files.

#### F.11 `no-examples-no-pictures` (High, measured)
- **Where:** About and Extend above all. Cause: `must-not` lines of the map, for instance `projects/forge/docs-map.md:792` "no finding of the forge project", :809 "no challenge of the forge project", :958 "no example project"; and the writer's shape asks for none.
- **Evidence:** M.10 and the section table: About and Extend have no code block in 44,598 words; 17 of the 28 pages of Start and Use have none. No sample position, requirement, SOL item or history record appears anywhere (reported). `about/how-a-thought-travels.md:13` says "This page follows one thought through the forge" and follows none (reported). `about/the-document-chain.md:54-55` "the chain is a star, not a fixed line" has no picture (reported).
- **Fix in:** the contract and the map: allow an invented, plainly generic example; ask for one worked example on each concept page and each how-to, one diagram of the artefacts with their inputs, one of the engine and the projects, one of a documentation run.

#### F.12 `about-repeats-itself` (High, measured; pairs reported, one verified)
- **Evidence:** M.08, M.09. Copies already differ: `about/renders-and-recipes.md:213` "eighty pages would mean eighty recipes" against `about/the-documentation.md:205` "Dozens of pages would mean dozens of recipes" (verified). Reported pairs:
  - the Lens rule on four pages: `isolated-reviewers.md:119-122`, `the-critic.md:62-65`, `the-challenger.md:40-43`, `the-check.md:151-153`;
  - instance facts in a report on five: `isolated-reviewers.md:153-156`, `the-critic.md:151-153`, `the-challenger.md:127-129`, `the-check.md:88-90`, `how-the-rules-are-held.md:177-180`;
  - handing over told three times: `the-principal-and-claude.md:44-60`, `working-methods.md:175-196`, `elicitation.md:122-140`;
  - the intent/solution test: `the-intent.md:146-165` and `the-solution-design.md:53-65`;
  - the five git scripts: `projects-and-the-engine.md:49-56` and `persistence-in-git.md:37-53`;
  - "A layer ... is not missing" on four pages; `how-a-thought-travels.md:192-195` repeated on the same page at 216-218.
- **Fix in:** the planner: one home page per rule, elsewhere one sentence and a link. This needs F.09 mended first, since today a writer may not link from the body.

#### F.13 `isolation-claim-overstated` (High, verified)
- **Evidence:** `docs/about/isolated-reviewers.md:54-55` "It sees the project's documents and nothing else". Against `docs/about/how-the-rules-are-held.md:168-170` "A subagent sees the session's whole context: `CLAUDE.md` as the session read it, the assistant's memory and `CLAUDE.local.md` included", and the challenger's use of web search (`the-challenger.md:72`, reported). The owners say less than the page: `CLAUDE.md` "seeing the project's documents only, never the working conversation"; POS.0950 "everything there reaches every subagent, the isolated reviewers included".
- **Fix in:** the map entries of the four reviewer pages: one exact sentence on what a reviewer does not see (the conversation) and what it does see (the documents, the core file, the instance file, the web for a challenger). See also C.04.

#### F.14 `session-ends-without-loss` (High, verified)
- **Evidence:** `docs/about/what-it-is-and-is-not.md:69` and `docs/about/documents-and-records.md:90` "A session can be ended at any point without loss". Against the pages' own rule that what is agreed is carried in the conversation and written once at the round's end, against `CLAUDE.md` prime directive 9 ("Claude never says nothing is lost while anything lives only in the conversation") and against POS.1500. The intent carries both sentences: see C.01.
- **Fix in:** the intent first (C.01), then regenerate.

#### F.15 `unsupported-statements-on-derived-pages` (High, three verified, the rest reported)
- **Rule broken:** POS.1450 "what the inputs do not support is left out and reported, never guessed".
- **Verified:** `about/renders-and-recipes.md:125` "Three light defences follow from this" against the intent, line 694, "Two light defences"; `about/how-a-thought-travels.md:154` "Every run leaves an immutable, dated report" against `CLAUDE.md:631` "a run that finds nothing files nothing"; `about/persistence-in-git.md:29-30` "a sensitive project may be kept local, with or without a remote" where POS.0940 says "A project without a repository, or with a repository and no origin".
- **Reported:** `about/how-a-thought-travels.md:195-196` "The renders are made at the release only"; :189 "Every project is a git repository of its own"; `about/the-document-chain.md:26-28` "Every project has these two" (a library has no chain); `about/versioning-and-history.md:53-61` generalises to any intent what POS.0300 says of the forge intent; `about/documents-and-records.md:73-75` "changed in the recipe or the map". Reasons found in no input: `about/isolated-reviewers.md:64-65` "a cheaper model would read less sharply, not merely more slowly"; `about/the-document-chain.md:91-93`, :106-109; `about/documents-and-records.md:164-165`, :151-152; `about/versioning-and-history.md:124`, :146-148; `about/stable-ids.md:51-53`; `about/the-challenger.md:146-148`; `about/projects-and-the-engine.md:72-75`.
- **Fix in:** where a reason is wanted, write it into the intent first so that a page may carry it; otherwise the map's `must-not`. The writer's report already lists what the inputs did not support; the run could list what the writer added.

#### F.16 `add-pages-skip-the-record` (High, verified)
- **Where:** `docs/extend/add-a-critic-lens.md`, `add-a-challenger-persona.md`, `add-a-check.md`, `add-a-recipe-genre.md`, `add-a-script.md`.
- **Evidence:** none of the five links to `docs/extend/how-a-change-is-made.md` or mentions it (searched), and `add-a-challenger-persona.md:30` says "One file and no edits." The process page says a change of "what a reviewer looks for" goes through the intent first (`how-a-change-is-made.md:17-19`, reported), and the intent names its members (POS.0410 "The critic has two lenses"), which `/check engine` would then report (inference, reported).
- **Fix in:** the map entries of the five pages: the link to the process page and one clause "recorded and released as any change of the forge", as `add-a-command.md:153-158` has it.

#### F.17 `add-a-check-wrong-command` (High, verified)
- **Evidence:** `docs/extend/add-a-check.md:104` "Run `/check <name> engine`, or use the engine's own project slug if the check takes a slug". Against `.claude/skills/check/SKILL.md:25-26`: "`/check <name> [slug]` ... The target is a project by its slug (the engine's own project is `forge`) or the engine root". The map asked for "Proof: `/check engine`; a run on a project." (`projects/forge/docs-map.md:1077`, reported). `docs/extend/add-a-recipe-genre.md:149-150` has the same weakness: "Run a check on the engine (`/check`, with the engine as its target)" (reported).
- **Fix in:** the map entries: spell the commands out (`/check engine`, then `/check <name>` or `/check <name> forge`).

#### F.18 `who-decides-and-the-outside-contributor` (High, reported)
- **Evidence:** "the principal" is defined on no Extend page and stands for two people: `how-a-change-is-made.md:145` "only you publish" (the principal of the instance) and :219-220 "What enters the forge stays the principal's decision." (the author of the engine). `add-a-critic-lens.md:21` "A new lens is added only by the principal's decision" leaves open whether a reader may add one in his own clone. `how-a-change-is-made.md:211-212` says a pull request "carries the same things as the order above" and lists three, while the order above has seven steps, among them filed check reports, `/release forge` and `/document`. `CONTRIBUTING.md:79-84` lists the same three.
- **Fix in:** the contributing recipe and the map entry: one sentence separating "in your own clone you decide" from "what is merged into the public engine its author decides", and a short list of what a pull request contains and does not contain.

#### F.19 `how-tos-lack-example-and-failure` (High, reported)
- **Evidence:** `use/critique-the-documents.md:40` gives `/critique <lens> [artefact] [slug]` and names one lens on the whole page; `use/challenge-the-thinking.md:39` names no persona; `use/check-conformance.md:39` names no check; `use/research-a-topic.md:22` has no sample topic. No failure content on `challenge-the-thinking`, `critique-the-documents`, `forge-the-intent`, `research-a-topic`, `spin-off-a-group`, `write-a-brief`. Failure messages of scripts that are declared inputs are left out, for instance `scripts/forge-save.py:99` "Push failed in {name}." on the save page. Per page (Y / partial / N; precondition, example invocation, steps the user sees, result, failure cases):

| Page | Precond. | Example | Steps | Result | Failure |
|---|---|---|---|---|---|
| bring-in-an-existing-project | Y | Y | Y | Y | partial |
| challenge-the-thinking | Y | partial | Y | Y | N |
| check-conformance | partial | partial | Y | Y | partial |
| compose-a-recipe | Y | partial | Y | partial | partial |
| critique-the-documents | partial | partial | Y | Y | N |
| design-the-solution | Y | Y | partial | Y | partial |
| distil-an-assignment | Y | Y | Y | Y | partial |
| forge-the-intent | Y | Y | Y | Y | N |
| generate-the-documentation | partial | Y | partial | Y | Y |
| look-up-a-command | Y | Y | Y | Y | Y |
| publish-a-designed-file | Y | partial | Y | Y | Y |
| register-a-source | Y | partial | Y | Y | partial |
| release-a-version | Y | partial | Y | Y | Y |
| render-an-output | Y | partial | partial | Y | Y |
| research-a-topic | Y | partial | Y | Y | N |
| save-your-work | Y | partial | Y | Y | Y |
| see-where-a-project-stands | Y | Y | Y (stale) | Y | partial |
| share-material-through-a-library | Y | partial | Y | Y | Y |
| spin-off-a-group | Y | partial | Y | Y | N |
| start-a-project | partial | partial | Y | Y | partial |
| upgrade-the-engine | Y | Y (stale) | Y (stale) | Y | Y (stale) |
| walk-through-a-list | Y | Y | Y | Y | partial |
| work-on-a-branch | Y | Y | Y | Y | Y |
| write-a-brief | Y | Y | Y | Y | N |

- **Fix in:** the writer's shape for a how-to (see F.20): one line that can be typed as it stands, with a placeholder slug and a real roster entry, and a closing "If something goes wrong" filled from the owner's stop conditions and the script's messages. `save-your-work.md:54-70` is the model.

### Medium

#### F.20 `no-skeleton-per-kind` (Medium, verified for Use; Extend and About reported)
- **Evidence:** M.16. The command sits under "Run it", "Start", "The command", "What you type", "Run the command", "Steps", "What you do", "Ask for the map", or in the opening paragraph; the result under "What you see", "What you see afterwards", "What you have afterwards", "What you get at the end", "What you check afterwards". Extend: "Check that it works" (`add-a-critic-lens.md:82`), "See that it works" (`add-a-check.md:100`), "Step 3: prove it" (`add-a-recipe-genre.md:145`), "At the end" (`add-an-artefact.md:102`). About: the four artefact pages answer different questions; "How it is found" exists for the assignment and the solution design only. Cause: `.claude/agents/docs-writer.md:66` prescribes only "<The matter, under headings where the topic needs them.>".
- **Fix in:** the writer: one outline per kind. How-to: when to use, command with one example, what happens, what you have afterwards, if something goes wrong. Add page: before you start, files, steps, prove it, record and release. Artefact page: what it is, who writes and reads it, made from, holds, complete when, how found, why.

#### F.21 `dense-sentences-and-elliptical-possessives` (Medium, measured; examples reported)
- **Evidence:** section table: About 21.8 words per sentence with 22 % of sentences at 30 words or more, Extend 20.5 and 21 %, against 15.6 and 7 % in Use. Longest reported: `about/the-solution-design.md:147-157` (121 words), `about/the-documentation.md:168-175` (103), `extend/how-a-change-is-made.md:121-130` (95), `reference/checks.md:85-93` (85), `about/where-it-is-going.md:63-69` (81). The possessive without its noun: `extend/what-it-is-made-of.md:206-213` "what a command does is its skill's", "is its help header's", "is its contract's"; `about/the-brief.md:59-60` "The chiselling is the intent's"; `use/check-conformance.md:74-75` "is for those commands to say"; `about/stable-ids.md:19-20` "the rules are the former's, the reasons the latter's". The idiom is the owners' house style and is carried over.
- **Fix in:** the contract: one rule per sentence, enumerations as lists, and "is defined in X" or "belongs to X" in place of "is X's". Where the page says another page says it, state the fact and link.

#### F.22 `appositions-in-commas` (Medium, reported)
- **Evidence:** `about/projects-and-the-engine.md:123-124` "Git identities, names, e-mail addresses and hosts live in" where the intent has the apposition between long dashes; `about/the-challenger.md:127` "Instance facts, names, roles, addresses, hosts, never enter"; `about/how-the-rules-are-held.md:56-57`. Cause: `.claude/skills/docs-contract/SKILL.md:37-38` "No long dash anywhere: a colon, a full stop or a spaced hyphen where one would stand", and the writer chose commas, so an apposition reads as a list.
- **Fix in:** the contract: brackets, "such as" or "that is" for an apposition.

#### F.23 `metaphors-for-mechanisms` (Medium, reported)
- **Evidence:** one step, turning a brief into the intent, has four images, none explained where first used: "mined" (`about/how-a-thought-travels.md:62`), "chiselled" (:60), "sifted" (`about/the-brief.md:33-34`), "tempered" (`about/how-a-thought-travels.md:57`). "door" counts differently each time: `about/persistence-in-git.md:35` "One door: the scripts", :58 "Two doors, two speeds", `CLAUDE.md:488` "the door inward". Also "trunk", "a star, not a fixed line", "a wall of the harness", "fails aloud". Against POS.1470.
- **Fix in:** the contract: the mechanism in a plain clause at first use on each page; at most one image kept. The owners use the same images, so the rule has to tell the writer not to carry them over.

#### F.24 `one-word-several-meanings` (Medium, reported)
- **Evidence:** "map" is the elicitation Map (`about/elicitation.md:97`), the state map (`about/the-document-chain.md:69`), the documentation map (`about/documents-and-records.md:60`), the provenance map (`about/the-assignment.md:143`), the coverage map (`about/the-solution-design.md:159`). "finding" is the search around an idea (`about/the-brief.md:25-26`), a research result (:79) and a reviewer's result. "Lens" is a variant of the critic and also a section of every agent file. "slug" is the project and, one bullet later, a file name (`use/register-a-source.md:22-25`). Several words for one thing: definition, state file, state definitions; template, skeleton; instance, installation.
- **Fix in:** the owners where the double use lives; in the meantime the contract: every "map" qualified, one word per thing.

#### F.25 `pronouns` (Medium for consistency, measured)
- **Evidence:** section table: About has 120 he/his/him and 2 you/your; Use addresses "you" (266) and still has 17. Claude is "it" at `start/what-it-is.md:24-25` and "he" at `start/first-result.md:90`; "he" at `about/the-solution-design.md:138`, "it" at `about/the-principal-and-claude.md:97-98`; `about/the-intent.md:93` says "the forge's assistant". The intent is mixed in the same way.
- **Fix in:** the contract: "it" for Claude, "you" for the reader of a how-to, the role noun for the principal.

#### F.26 `names-of-the-actors-vary` (Medium, reported)
- **Evidence:** `about/persistence-in-git.md:27` "the user's one-off act" and :41 "the principal"; `about/where-it-is-going.md:29` "its owner's discretion"; `about/languages.md:84-85` "the person's". For the machine: "Claude's own judgement", "the forge's own judgement", "The session files it", "the harness".
- **Fix in:** the contract: one word per role; "session" and "harness" glossed once per page.

#### F.27 `dash-rule-alters-literals` (Medium, one verified, the rest reported)
- **Evidence:** `docs/reference/history-companion.md:32` "The heading below it is `# History - <file>`." against `templates/history.md:6` "# History — <file>" (verified). Reported: `reference/critic-lenses.md:115-117` against `.claude/agents/critic-essence.md:64-67`; 15 of 20 command descriptions on `reference/commands.md`; seven rows of `reference/id-scheme.md`; `extend/add-a-challenger-persona.md:44` quoting the skeleton.
- **Fix in:** the contract and `scripts/docs-check.py`: code spans and quoted literals are exempt from the dash rule; or the long dashes leave the owners, so that page and owner agree.

#### F.28 `layout-omits-claude-local` (Medium, verified)
- **Evidence:** `docs/reference/repository-layout.md` has no row for `CLAUDE.local.md`, which the layout block of `CLAUDE.md` lists at the engine root. Cause (reported): `projects/forge/docs-map.md:1428` "must-not: no explanation; no instance file."
- **Fix in:** the map entry: narrow the `must-not` to "no value of an instance".

#### F.29 `reference-pages-drifted-or-inferred` (Medium, reported)
- `reference/templates.md:55`, :78, :56: the "Created by" of `decisions.md`, `index.md` and `history.md` is inferred; `.claude/skills/new-project/SKILL.md:45-50` creates the first two and is not among the inputs.
- `reference/checks.md:38` prints a shortened description as "Description"; the critic and challenger pages print it in full.
- `reference/configuration.md:28` announces the list of what git leaves out and omits `.gitignore:22-23` (`/start-claude.ps1`).
- `reference/ledger.md:50` "One row per layer below the intent" although the skeleton's Documents table carries the intent (`templates/ledger.md:36`).
- `reference/scripts.md:106` and :144 show `--as-list` and `--model` in a synopsis and describe neither.
- **Fix in:** the map entries (inputs and `says`), then regenerate.

#### F.30 `reference-hard-to-scan` (Medium, reported)
- `reference/commands.md:71-217` is 147 lines of bullets where one table (command, argument hint, guarded, description) answers "which commands are guarded" at a glance; the page prints two signatures per command without saying which holds (:63 against :200).
- The five roster pages have four entry shapes; `checks.md`, `challenger-personas.md` and `recipe-genres.md` have no overview table.
- `reference/glossary.md` is ten thematic tables, not alphabetical, no anchor per term; "mined" sits under "Saving and releasing"; 12 of 65 "Defined in" cells cite the 1,794-line intent with no place in it; the rows for lens, persona, mined, project and definition are circular or inexact (:102, :104, :130, :114, :51).
- Only three links go from one reference page to another.
- **Fix in:** the map entries and one shared entry shape for rosters in the writer.

#### F.31 `coarse-inputs` (Medium, measured)
- **Evidence:** M.14 with M.11: a change of ten lines in `CLAUDE.md` and fifty in the intent moved 62 more pages to `regenerate`, though the sectional audits name a change of content on roughly a dozen (an estimate, counted from F.03). `scripts/docs-state.py` hashes each input file whole. POS.1450 wants a run to be cheap and to regenerate "only the pages whose inputs changed".
- **Fix in:** a design question for the map and `docs-state.py`: inputs by section of a file (a heading or an ID as anchor), hashed as that section.

#### F.32 `setup-page` (Medium, order and Fable verified, the rest reported)
- The page is `made: mirrored` and reorders its owner: page "Step 2: the session model", "Step 3: the git identity"; in `.claude/skills/setup/SKILL.md` the git identity closes item 1 (line 27) and the model is item 2 (line 50) (verified).
- It understates what is written outside the engine: page :56-57 "two things into the global git configuration file"; the owner also creates `.gitconfig-<host>` files and offers to remove an existing global `user.name` / `user.email` (`SKILL.md:40-46`, read). It does not say that with the guard a repository on a host without a stanza refuses to commit.
- `setup.md:45` "set to Fable, the strongest available model" has no fallback; the map records the gap itself (`projects/forge/docs-map.md:1542`) (verified).
- No example of "the principal by role" although `templates/CLAUDE.local.md:6` has one; no word on what the conversation language governs (reported).
- **Fix in:** the map entry; for the model, the setup skill.

#### F.33 `release-page` (Medium, verified)
- `docs/use/release-a-version.md:34-36` "for the engine, `light`, `engine` and `project`, the last two on the forge's own project" misreads `.claude/skills/release/SKILL.md:26-27` "the two project checks on `projects/forge`" (those are `light` and `project`). The owner's wording invites it.
- :39-40 "the release does not go on with an unsettled finding" against :79 "You may order the release at any moment regardless of findings." The owner has the same pair (`release/SKILL.md:31-32`, :84-85): see C.05.
- **Fix in:** the release skill, both points.

#### F.34 `internals-on-user-pages` (Medium, reported)
- **Evidence:** `use/render-an-output.md:37-38` "the copy a subagent carries in its context may be older than the file"; :42-43 "It is told the shape of the provenance block"; `use/generate-the-documentation.md:47-49` on which model writes which page; `use/start-a-project.md:57` "How a brief is composed is not repeated here."; `use/upgrade-the-engine.md:81-82` "`forge_repos.py` beside it". Against `.claude/skills/docs-contract/SKILL.md:30-32`.
- **Fix in:** the `must-not` of the Use entries: no subagent, prompt, model or helper module; "not repeated here" becomes a link.

#### F.35 `openings-carry-provenance` (Medium, verified on the pages read)
- **Evidence:** the first paragraph of most pages ends "It was put together from ..." with file names (`start/what-it-is.md:14-15`, `start/install.md:23-27`, `start/first-result.md:19-22`, `about/what-it-is-and-is-not.md:15-18`), repeating the front-matter. On concept pages half of the opening is provenance and none of it defines the concept (`about/persistence-in-git.md:12-18`, reported).
- **Fix in:** the writer's shape: the first sentence says what the thing is; provenance is one closing line or the front-matter alone.

#### F.36 `one-topic-doubtful` (Medium, reported)
- `about/renders-and-recipes.md` has nine topics as H2, `about/how-the-rules-are-held.md` eight, `about/documents-and-records.md` eight (down to "Prose at about 72 columns", :159). `about/the-documentation.md` (2,080 words) mixes the concept with run mechanics (:134-150). `about/persistence-in-git.md:147` "Portability" is not persistence. `about/where-it-is-going.md:59-83` describes `/new-artefact`, which exists today. `start/first-result.md:113-131` carries a second job ("The other door: an existing project"). `use/generate-the-documentation.md:14-16` addresses two readers.
- **Fix in:** the planner: pages cut by concept, not by the section of `CLAUDE.md` or of the intent they come from.

#### F.37 `process-page-contradicts-itself` (Medium, reported)
- `extend/how-a-change-is-made.md:36-38` "a slip, is made directly in the file where it stands, and nothing else is needed" against :184-185 "a page is never touched by hand" and :191-193 on renders. Step 7 "Regenerate the documentation" (:176) follows step 6 "Release it" (:147) although :165-166 says it runs "before the save, so that the release carries current pages".
- **Fix in:** the map entry.

#### F.38 `add-a-command-gaps` (Medium, reported)
- The guard criterion cannot be applied: `extend/add-a-command.md:62-63` "present on every command that writes, scaffolds, commits or regenerates", while `/research`, `/recipe`, `/forge` and `/critique` write and carry no guard. The page mirrors POS.1090.
- No word on how arguments reach the body (`$0`, `$ARGUMENTS`; `.claude/skills/ledger/SKILL.md:6`), no minimal skeleton, the model skill named without a path (:92).
- **Fix in:** the intent for the criterion (see C.06); the map entry for the rest.

#### F.39 `architecture-overview` (Medium, reported)
- `extend/what-it-is-made-of.md` is 231 lines of prose with no tree, table or diagram. :81-91 lists the walkthrough skill among the skills "preloaded into an agent", against `.claude/skills/walkthrough/SKILL.md:2`. :108-109 "the whole forge runs on one model" against POS.0930's two exceptions. Title "About ..." on a page whose kind is how-to.
- **Fix in:** the map entry: open with a table (path, what it is, loaded when) and one line of flow.

#### F.40 `use-page-slips` (Medium, reported)
- `use/see-where-a-project-stands.md` says which target states can be worked and neither shows `/forge <state>` nor links the four state pages (cause: its `must-not`, `projects/forge/docs-map.md:165-180`).
- `use/start-a-project.md:92-93` "The forge sets none and has nothing to propose." copies an instruction to the command; `/setup` does propose the identity.
- `use/compose-a-recipe.md` never says the recipe lands in `recipes/<recipe>.md`.
- `use/design-the-solution.md:75-76` "The persona `architect` exists for this." has no input behind it.
- `use/write-a-brief.md:97-99` names "the areas" and lists none; the owner lists five.
- **Fix in:** the map entries.

#### F.41 `start-pages-miss-their-prerequisites` (Medium, reported)
- `start/first-result.md:22-24` "how that is done is not this page's matter" and its See also links neither `install.md` nor `setup.md`; `start/setup.md:20` "Type `/setup` in the engine" does not say in a Claude Code session started at the engine root. `/forge intent` is shown without a slug (:82) though a new session needs it. No sample brief, no word on how a round ends or that the write may be ordered at any time.
- **Fix in:** the map entries: a "Before you start" line with two links, a five-line sample brief, the slug form.

#### F.42 `ideas-not-carried` (Medium, reported)
- `about/the-challenger.md` names no persona though POS.0420 defines `cto` and `architect`. `about/the-critic.md` never says what `essence` guards (the drift of the chain, POS.0400). `about/the-document-chain.md:88-89` answers "Which artefacts exist" with "the listing of the definitions directory" and lists none. No page says what problem the forge solves; `about/what-it-is-and-is-not.md:80-112` gives three "Why" headings to the name and to where a chain ends.
- **Fix in:** the map entries.

### Low

#### F.43 `titles` (Low, verified)
- All 25 About pages and two more are titled "About ...". Three are near-identical: "About what the forge is" (`start/what-it-is.md`), "About what the forge is and is not", "About what the forge is made of". The first sits in a how-to section.

#### F.44 `root-readme` (Low, lines 163-171 verified, the rest reported)
- The hand-off to the documentation is two comments inside a code block (`README.md:168-171`), so not clickable; git and Python are not named before the clone. Quickstart starts at line 163 after 70 lines of "What is new in 5.0". Lines 255-351 repeat every page title of the index. POS.1450: "The README is cut to what orients and points".

#### F.45 `history-and-generator-rules-on-pages` (Low, reported)
- `about/languages.md:43-44` "the boundary was narrowed to the artefacts on 2026-09-10"; `about/persistence-in-git.md:74-75` "a two-speed save had existed in practice for weeks"; `about/the-principal-and-claude.md:90-91`; `about/what-it-is-and-is-not.md:90-93` (the rejected names); `about/versioning-and-history.md:25` "aligned with the group BRD standard" (an unnamed organisation). Generator talking about itself: `about/the-check.md:19-21`, `about/versioning-and-history.md:57` "the inputs say precisely what it does".

#### F.46 `small-slips` (Low, reported)
- `about/the-assignment.md:104-105` against `.claude/skills/forge/states/assignment.md:129-130`; `about/elicitation.md:32-33` "over an assignment" where the intent has "over a BRD"; `about/working-methods.md:46` four verdicts where POS.0850 has five; `about/where-it-is-going.md:118-120` "A visitor is told how where the readers of a public repository look for it." (does not parse).
- `use/save-your-work.md:43-44` against `.claude/skills/save/SKILL.md:39` (`v<intent version>`); `use/bring-in-an-existing-project.md:53-54` against `scripts/forge-clone.py:65-67`; `use/share-material-through-a-library.md:26-27` "recognises it as one from the prefix" against the ledger header.
- `use/check-conformance.md:81` "the checks as the migration tool" against `use/upgrade-the-engine.md:115` "There is no migration tool, knowingly".
- `extend/add-an-artefact.md:28-29` "a whole chain, a reviewer and a genre each have their own way in" (the intent says only that they are not this command's).
- Line wrapping: twelve reference pages are wrapped at about 72 columns; `reference/scripts.md` has 56 prose lines over 100 characters.
- No page says what to read before or after it.

---

## 4. Contradictions inside the owners

Pages mirror these, so they have to be settled in the owner before a regeneration can mend the page.

| # | Status | The two sides |
|---|---|---|
| C.01 | verified | POS.0330 (`10-intent.md:953-955`) "A session can be ended at any point without loss" against POS.1500 (`/end` says what "would be lost") and POS.0190 ("Claude never says nothing is lost while anything lives only in the conversation"). |
| C.02 | reported | POS.1110 (`10-intent.md:1145`) "merge, rebase and conflicts stay git's" against POS.1490 (:1233-1234) "lets `/save` rebase his commits onto the remote". |
| C.03 | reported | POS.0970 (:727-728) "the version in the citation is a visible, unguarded pin" against POS.1020 (:1584) "No version is recorded" and `CLAUDE.md`, Ledger, "carries no version". |
| C.04 | verified | `CLAUDE.md`, Isolated reviewers: "seeing the project's documents only" against POS.0950: "everything there reaches every subagent, the isolated reviewers included". |
| C.05 | verified | `.claude/skills/release/SKILL.md:31-32` "never proceed with an unsettled finding" against :84-85 "at any moment regardless of findings". |
| C.06 | reported | POS.1090: the guard is for a command that "writes, scaffolds, commits or regenerates", while commands that write on the principal's word stay unguarded; the rule that separates them is not stated. |
| C.07 | reported | `scripts/forge_repos.py:2-4`: the docstring does not name the state against the origin, which the module now holds (`40-solution-design.md:633-635`). |

---

## 5. What works

- **W.01** The form of POS.1450 is kept: five sections, one topic per page in most cases, an opening that names the reader and the purpose on every page, a closing "See also" on every page.
- **W.02** The repository's own check passes (M.15): every link resolves, no long dash, no instance fact. No chain ID stands on a page except as an illustration of the format.
- **W.03** Provenance is machine-readable: every page carries `made`, `inputs` and `inputs-hash`, which is what made M.11 and this audit possible.
- **W.04** Reference is complete against the directories: 15 of 15 scripts, 20 of 20 templates, 5 of 5 checks, 2 of 2 lenses, 2 of 2 personas, 3 of 3 genres, 4 of 4 artefacts; the 21 command rows it has are identical to the owner's (reported).
- **W.05** Use and Reference read well by measure (15.6 and 15.5 words per sentence). `use/spin-off-a-group.md`, `use/publish-a-designed-file.md` and `use/save-your-work.md` are how-tos with precondition, steps and outcome.
- **W.06** Limits are stated honestly: "Isolation is not independence", "A hook is context, not enforcement", "It attests nothing of how the model behaves".
- **W.07** Model names and a vendor's product name in the intent are generalised on the pages ("the session model", "a faster model"), with the one exception of F.32.
- **W.08** `extend/change-a-documentation-page.md` is the strongest page of its section; `about/the-brief.md` and `about/the-assignment.md` have a clear arc and little repetition (6 % and 4 %, reported).

---

## 6. Not verified

- Nothing was executed: no `/setup`, `/save`, `/document`, no hook. F.01 (second half) and F.04 (the alias) rest on reading the files and on general behaviour of an operating system.
- Findings marked `reported` rest on one isolated agent each; their line numbers were not re-checked.
- "Not found in the inputs" (F.15) rests on phrase searches over the repository's Markdown files; a paraphrase elsewhere is possible.
- The pages were compared with the repository at `04e332a`, not with the state of 2026-10-10 they were generated from; what was already wrong on the day of the run and what became wrong a day later is separated only for F.03.
- How the pages render where the repository is published.
