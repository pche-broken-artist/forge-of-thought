---
generated: 2026-10-19
version: 5.26
made: mirrored
inputs-hash: 98922c24aee9d606
inputs:
  - .claude/agents/check-light.md
  - .claude/agents/check-project.md
  - .claude/agents/check-engine.md
  - .claude/agents/check-history.md
  - .claude/agents/check-single-source-of-truth.md
  - .claude/skills/save/SKILL.md
  - .claude/skills/release/SKILL.md
---

# Checks

This page lists the checks of the forge: what each one reads, what it verifies, which document owns each rule it verifies, and what it costs. It is for the person who runs a check and for the one who adds a check. A check verifies conformance with the conventions only. It is not a critic of the documents and not a challenger of the thinking. Each check is a subagent, that is an isolated helper that sees only the files it is sent to read, and it reports advisory findings to the principal, the person whose thinking is being forged.

## Overview

| Check | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `light` | A project's bookkeeping: front-matter, history companions, the ledger script's own reports, published companions, thread files, dependencies, resource indexes | A save | `.claude/agents/check-light.md` |
| `project` | A project's structure, IDs, language, immutables, recipes and renders | A release, beside `light` | `.claude/agents/check-project.md` |
| `engine` | The core (CLAUDE.md, templates, skills, agents, scripts) against itself and against the forge intent | A release of the engine | `.claude/agents/check-engine.md` |
| `history` | The division between a document and its history | When a document is cleaned; never at a save or a release | `.claude/agents/check-history.md` |
| `single-source-of-truth` | That every rule, procedure and file shape is written in one place and cited elsewhere | Before a major release or after a round on the operating layer; not at every release | `.claude/agents/check-single-source-of-truth.md` |

## What a save and a release run

A save runs `light` on every repository in scope, unless it is given `--quick`, which leaves the check out. A release of a project runs `light` and `project` on it. A release of the engine runs `engine` on the engine root, and `light` and `project` on `projects/forge`, the engine's own project. `history` and `single-source-of-truth` are run by hand and by neither.

Running a check is described on [Check conformance](../use/check-conformance.md), adding one on [Add a check](../extend/add-a-check.md), and the terms of the forge are in the [Glossary](glossary.md).

## light

Description: verifies a project's bookkeeping (front-matter and the history companions against the templates, the ledger script's own reports, the index entries, the published companions and the thread files against the directories and the rules). Fit for a save.

What it reads: one project, the path its task names. For the engine that is `projects/forge`. It is the check a save can afford: bookkeeping only, so that what lies in git between releases is at least consistent with itself. Everything else about a project belongs to `project`.

What it verifies, and the owner of each rule:

- Front-matter and history, for every versioned document and its companion: the placement of the history and the form of its log. Owners: CLAUDE.md, Versioning & status, and `templates/history.md`. Whether a text belongs in the document or in its history is the work of `history`.
- The ledger's own reports. The ledger (the single source of truth for state) is made at read time by `scripts/forge-ledger.py` from the records, so it is not compared with the files. Each line of its Reports section and each `unparsed:` line of its header is a finding, with the file it names. Owner: `templates/ledger.md`, Reports. A project whose ledger header says `shape: before the migration` is reported as `templates/project.md` says.
- Published companions: `published/<recipe>.md` and the files of `published/` agree. A companion without its file and a file without its companion are findings. The state current or stale is computed and is never a finding.
- Work products: every specification in `work/` has its history companion. A work file that cites an item by ID (DEC, SOL, POS, TBC, THR) not named among its specification's Inputs is a finding, because the file has moved past the way and the why.
- Thread files: every one carries the header of `templates/thread.md`, and a closed one is unchanged since its closing.
- State words: a state word a record or a verdict carries that the templates do not know is a finding. The check never changes a review or a decision record, which keep the word they were written with.
- Dependencies: every path in the Dependencies table exists on disk. A missing library is the advisory finding "library `<name>` not cloned alongside". The rows are the citations the script found, so there is nothing to add.
- Resource indexes: `sources/00-INDEX.md` and `research/00-INDEX.md` exist and agree with their directories. A file or bundle without an entry, an entry without a file, and a bundle entry whose inner `00-INDEX.md` is missing are findings. A sources entry without its `Date` and `Form` fields (owner: `templates/index.md`) is an immediate fix. A binary without an extract, and an extract without its original, are the normal case and never a finding. A binary listed in `sources/.gitignore` is not an unregistered file. The check never judges what the entries say.

Most of what it finds is pure bookkeeping and is marked "immediate fix".

Cost: the ledger's header and Reports, the front-matter of every document, the newest records of the companions and the directory listings. Seconds, not minutes.

## project

Description: verifies a project's structure, IDs, language, immutables, recipes and renders against the conventions.

What it reads: one project, the path its task names, or, when the task names none, every project under `projects/` except `forge`, each reported on its own. The bookkeeping of a project (front-matter, history companions, the ledger's reports, dependencies, resource indexes) belongs to `light`. Run beside it at a release, this check verifies everything else.

What it verifies, and the owner of each rule:

- Kind and repository. The project file `project.md` declares `kind: thought | library` and `language`; `templates/project.md` also says what a project without it is and how it is reported. `.gitattributes` exists (owner: `templates/gitattributes`). `threads/` exists in a thought project. `projects/<slug>/.git` exists, but a project that is not a repository is a fact and not a finding; it is reported with the one-line way in that CLAUDE.md, Persistence, names. A library needs no chain: its structure reduces to the library's file set (CLAUDE.md, Repository layout), ID hygiene does not apply, and its documents may be overwritten by their owner without an immutability breach. `logo.png` is optional everywhere and its absence is never a finding.
- Structure. The files and folders of CLAUDE.md, Repository layout, exist. A layer below the intent that the project does not have is not missing (CLAUDE.md, Ledger). `recipes/` and `renders/` are paired: every render traces to a recipe and carries provenance front-matter, and legacy pre-recipe editions with dated filenames are exempt. The ledger's Renders table is read from that provenance, so there is nothing to compare. Every file in `published/` traces to a recipe that carries a `## Format` section, and a `.pptx` or `.docx` in `renders/` traces to a render beside it (CLAUDE.md, Document chain, Renders). An older recipe still carrying `## Build instructions` is a finding fixed at its next iteration (owner: `templates/recipe.md`, Format). The README and release-notes recipes exist; the fix is to scaffold them from `templates/recipe-<genre>.md`. A brief whose mining record says `mined` is cited somewhere in the intent.
- ID hygiene, in every document that carries IDs. Owner: CLAUDE.md, ID scheme.
- Language, for every artefact and record. The briefs and renders are exempt. Owner: CLAUDE.md, prime directive 6.
- Immutables. The immutable documents (CLAUDE.md, Versioning & status) are never edited after creation. The check flags any sign of after-the-fact editing that the ledger or the history companions reveal. The `00-INDEX.md` catalogues are exempt because they are rewritten freely.
- Recipes and renders, shape and freshness, never content. Recipes conform to `templates/recipe.md` in front-matter and sections; the genre skeletons `templates/recipe-<genre>.md` extend that shape and never replace it. Every declared input exists on disk. The `output:` path, where declared, points inside the repository. The staleness of a render is never a finding, the README and the release notes included. Whether a recipe's content still matches the principal's thinking is substance, not conformance.

Cost: the project's files, read once, and the conventions read from their owners.

## engine

Description: verifies the core (CLAUDE.md, templates, skills, agents, scripts) against itself and against the forge intent: every position honoured, nothing withdrawn still advertised, every decision reflected.

What it reads: the engine, that is the root its task names (CLAUDE.md, `templates/`, `.claude/skills/`, `.claude/agents/`, `scripts/`), and the forge intent, `projects/forge/10-intent.md`, with its threads in `projects/forge/threads/` and `projects/forge/decisions.md`. The forge project's own conformance belongs to `project` and `light`, run beside it at a release. Whether a rule is stated in more than one place belongs to `single-source-of-truth`.

What it verifies:

- Core internal consistency:
  - The CLAUDE.md commands table agrees with the skills in `.claude/skills/*/SKILL.md` (the reviewers' contracts excepted). The agents described agree with `.claude/agents/`. Every skill an agent names in its front-matter exists as `.claude/skills/<name>/SKILL.md`, because Claude Code skips a missing one silently.
  - Every file in `scripts/` is described in CLAUDE.md (the layout comment and its governing rule), and nothing described there is missing on disk.
  - The README agrees with CLAUDE.md: same chain, same conventions, same command set, no contradictions. Currency is not checked, because the README and the release notes are renders regenerated at the release after this check. A claim in the README that CLAUDE.md or the intent no longer supports is a recipe defect, fixed in the recipe.
  - The templates agree with the conventions as CLAUDE.md, Versioning & status and ID scheme, state them: front-matter fields, the history companion, prefixes, numbering and statuses.
- Core and forge intent:
  - Every position (POS) is honoured by the core documents. Nothing withdrawn or rejected (REJ items, closed THR items) is still advertised anywhere in the core.
  - Decisions referenced from the intent exist in `decisions.md`, and every decision record is reflected in the intent where it applies.
- Rename and removal sweep: the old names recorded in decision records (for example a renamed command) and the terms the principal has explicitly dropped are searched for. Only historical records (history companions, decisions, rejected directions, reviews, challenges, research) may still contain them.

Cost: the core files once and the intent's positions once. Minutes at most, so that a release can afford it every time.

## history

Description: reads a document with its history and reports where the division between them does not hold, proposing each move in full. Fit when a document is cleaned, never at a save or a release.

What it reads: one project, the path its task names (for the engine `projects/forge`), and in it every versioned document with its history and its archive, or the one document its task names.

What it verifies: the division between a document and its history. Owners: CLAUDE.md, Versioning & status, and the intent's definition, `.claude/skills/forge/states/intent.md`, Threads and files.

- In the document, the way to an item, as Versioning & status lists it, is a finding. So is detail an item carries where the file that performs it exists.
- The other way round, an item that can no longer be understood because what makes it hold stands only in the history is a finding.
- Each finding proposes the move in full: the text that leaves, word for word, and the record it becomes.

The form of the log belongs to `light`.

Cost: whole documents with their histories, minutes rather than seconds. It is never composed into a save or a release.

## single-source-of-truth

Description: verifies that every rule, procedure and file shape is written in one place and cited everywhere else: no restatement across CLAUDE.md, skills, agents, templates and scripts, and no direct operation where a mechanism exists. It is the honest sweep and expensive by design. Fit before a major or after a round on the operating layer, not at every release.

What it reads: the whole operating layer of the engine, always the whole and never a changed subset. That is CLAUDE.md, every skill under `.claude/skills/` (supporting files included), every agent under `.claude/agents/`, every template under `templates/` and the help headers of `scripts/`. Named a project instead, it reads that project's recipes, resource indexes, ledger comments and its own CLAUDE.md, if any, against the owners in the engine.

What it verifies, with the rule that one mechanism lives in one place:

- One owner per rule. Every command, agent, contract and template describes only its own job. A procedure, rule set or file shape that another file owns is cited by path and not restated. A restatement, the same steps, rules or shape in two places in whatever wording, is a finding, and the fix is a reference to the owner and the deletion of the copy. Where a shape has no owner at all, the finding proposes one (a skeleton, a section of CLAUDE.md) and never a second description.
- Reviewer files carry only their own. Every lens, persona and check file (`.claude/agents/critic-*.md`, `challenger-*.md`, `check-*.md`) names its kind's contract skill and carries only its front-matter and its Lens section. Nothing the contract owns is restated in it.
- No direct operation where a mechanism exists. No skill or agent performs directly what a script, command or agent exists for: git outside the scripts in `scripts/`, a conversion outside `doc2md.py`, a render outside `/render`, a review outside the reviewer agents, a check outside the check agents.

Cost: the whole layer, read and compared pairwise where the subjects overlap. Long by design; its report says in its first line how many files it read.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Add a check](../extend/add-a-check.md): adding a check.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-19 for version 5.26 from the files the front-matter names; never edited by hand.
