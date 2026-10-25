---
generated: 2026-10-25
version: 6.0
made: mirrored
inputs-hash: 965cc8424a1e4eda
inputs:
  - .claude/agents/check-light.md
  - .claude/agents/check-project.md
  - .claude/agents/check-engine.md
  - .claude/agents/check-history.md
  - .claude/agents/check-single-source-of-truth.md
  - .claude/agents/check-brd.md
  - .claude/skills/save/SKILL.md
  - .claude/skills/release/SKILL.md
---

# Checks

This page lists the checks of the forge: the reviewers that verify a project or the engine against the conventions (see the [Glossary](glossary.md) for the terms). It is for the user who chooses which check to run and for the extender who wants to see what the existing ones cover. Each check is a subagent, that is an isolated helper that does not see the conversation. A check verifies conformance only: it is not a critic of the documents and not a challenger of the thinking. To run one, see [Check conformance](../use/check-conformance.md). To add one, see [Add a check](../extend/add-a-check.md).

## Overview

| Check | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `brd` | The mechanics of a BRD: parents carried, cited IDs existing, phasing, terms | After a pass of `/forge brd` | `.claude/agents/check-brd.md` |
| `engine` | The core against itself and against the forge intent | Every release of the engine | `.claude/agents/check-engine.md` |
| `history` | The division between a document and its history | When a document is cleaned, never at a save or a release | `.claude/agents/check-history.md` |
| `light` | A project's bookkeeping | A save | `.claude/agents/check-light.md` |
| `project` | A project's structure, IDs, language, immutables, recipes and renders | A release | `.claude/agents/check-project.md` |
| `single-source-of-truth` | That every rule, procedure and file shape is written in one place | Before a major, or after a round on the operating layer | `.claude/agents/check-single-source-of-truth.md` |

## Which checks a save and a release run

A save runs `light` on every repository in scope, unless `--quick` is given. A release of a project runs `light` and `project` on it. A release of the engine runs `engine` on the engine root, and `light` and `project` on the forge's own project. The checks `brd`, `history` and `single-source-of-truth` are run by neither; the principal asks for them.

## brd

Description: verifies a BRD's mechanics: every parent item carried, every cited ID existing, every item with a parent, the phasing present, every term defined, no link in an item. Fit after a pass of `/forge brd`.

What it reads: one project's `30-brd.md` (the path the task names, or the project's BRD when the task names a project) with its parent as the BRD's header declares it, which is `20-assignment.md` or `10-intent.md`. A BRD made from a source is a work product in `work/`, read when the task names it, its parent being the source by path. A project without a BRD is not a finding.

What it verifies:

- Traceability: every in-scope item of the parent is carried by at least one BR or UC, unless an OOS, a DEP or a TBC of the BRD names it. Every parent an item cites exists in the parent. The appendix table matches the items. Where the parent is a source, the cited path exists.
- Every item has a parent: a BR and an NFR end with their parent, and an NFR may end with its category instead. A UC declares its parent in its `Carries` line. Where the parent is a source with speakers, a BR whose every cited place is another party's turn is a finding.
- The sections that may not be silent: Phasing is present, not empty, and every BR and UC stands in a phase or in the `not phased` row. Every area of the roster the BRD cites is in the Touched areas table, and every role the roster names as signing or reviewing is in the Stakeholders table or named as absent with a reason. An ASM whose content answers what a TBC of the same BRD asks is a finding. Every NFR category kept carries a value or a TBC with an owner. Every TBC has an owner (a role, or `unassigned`) and says whether it blocks estimation.
- Terms and links: every capitalised term of an item is in the Terms table, no item depends on a link, and no name of a person stands where the template asks for a role.
- Skeleton residue: no template comment, no `…`, no `<placeholder>`, no `NNNN` left in the file. `owner: unassigned` is not residue.

Owners of the rules: the BRD template `templates/brd.md` and the definition `.claude/skills/forge/states/brd.md` (Requirement style). The bookkeeping of the file belongs to the `light` check and the ID scheme in general to the `project` check.

Cost: the BRD and its parent, read once; the roster the BRD cites, read for its list of areas only.

## engine

Description: verifies the core (`CLAUDE.md`, templates, skills, agents, scripts) against itself and against the forge intent: every position honoured, nothing withdrawn still advertised, every decision reflected.

What it reads: the engine root the task names (`CLAUDE.md`, `templates/`, `.claude/skills/`, `.claude/agents/`, `scripts/`) and the forge intent, `projects/forge/10-intent.md`, with its threads and `projects/forge/decisions.md`.

What it verifies:

- Core internal consistency:
  - The commands table of `CLAUDE.md` agrees with the skills on disk (the reviewers' contracts excepted), the described agents agree with `.claude/agents/`, and every skill an agent names in its front-matter exists.
  - Every file in `scripts/` is described in `CLAUDE.md` and nothing described there is missing on disk.
  - The README agrees with `CLAUDE.md` on chain, conventions and command set. Currency is not checked: the README and the release notes are renders regenerated at the release, after this check.
  - The templates agree with the conventions that `CLAUDE.md` states (front-matter fields, the history companion, prefixes, numbering, statuses).
- Core against the forge intent: every position is honoured by the core documents, nothing withdrawn or rejected is still advertised in the core, decisions referenced from the intent exist in `decisions.md`, and every decision record is reflected in the intent where it applies.
- Rename and removal sweep: the old names recorded in decision records, and terms the principal has explicitly dropped, are searched for. Only historical records (history companions, decisions, rejected directions, reviews, challenges, research) may still contain them.

Owners of the rules: `CLAUDE.md` for the conventions, the forge intent for the positions and decisions. The conformance of the forge's own project belongs to the `project` and `light` checks, and whether a rule is stated in more than one place to the `single-source-of-truth` check.

Cost: the core files once and the intent's positions once; minutes at most, so that a release can afford it every time.

## history

Description: reads a document with its history and reports where the division between them does not hold, proposing each move in full. Fit when a document is cleaned, never at a save or a release.

What it reads: one project (for the engine, `projects/forge`), and in it every versioned document with its history and its archive, or the one document the task names.

What it verifies: the division between a document and its history. In the document, the way to an item (as Versioning & status lists it) is a finding, and so is detail an item carries where the file that performs it exists. The other way, an item that can no longer be understood because what makes it hold stands only in the history is a finding. Each finding proposes the move in full: the text that leaves, word for word, and the record it becomes.

Owners of the rules: `CLAUDE.md` (Versioning & status) and the intent's definition `.claude/skills/forge/states/intent.md` (Threads and files). The form of the log belongs to the `light` check.

Cost: whole documents with their histories; minutes rather than seconds. Never composed into a save or a release.

## light

Description: verifies a project's bookkeeping: front-matter and the history companions against the templates, the ledger script's own reports, the index entries, the published companions and the thread files against the directories and the rules. Fit for a save.

What it reads: one project, the path the task names (for the engine, `projects/forge`).

What it verifies:

- Front-matter and history: every rule of Versioning & status in `CLAUDE.md`, for every versioned document and its companion: the placement of the history and the form of its log as `templates/history.md` gives it. Whether a text belongs in the document or in its history belongs to the `history` check.
- The ledger's own reports: each line of its Reports section and each `unparsed:` line of its header is a finding, with the file it names. A project whose ledger header says `shape: before the migration` is reported as `templates/project.md` says.
- Records and companions:
  - The published companions and the files of `published/` agree.
  - Every specification in `work/` has its history companion.
  - A work file that cites an item by ID not named among its specification's Inputs is a finding.
  - Every thread file carries the header of `templates/thread.md`, and a closed one is unchanged since its closing.
  - A state word that a record or a verdict carries and the templates do not know is a finding. The review or decision record itself is never changed.
- Dependencies: every path in the Dependencies table exists on disk. A missing library is reported as advisory, with the command that brings it in.
- Resource indexes: `sources/00-INDEX.md` and `research/00-INDEX.md` exist and agree with their directories (a file or bundle without an entry, an entry without a file, a bundle entry whose inner index is missing, a file or entry inside a bundle without its counterpart). A sources entry without its `Date` and `Form` fields is an immediate fix. A binary without an extract, and an extract without its original, are the normal case. The check never judges what the entries say.

Most of what it finds is pure bookkeeping and is marked as an immediate fix.

Owners of the rules: `CLAUDE.md` (Versioning & status), `templates/history.md`, `templates/ledger.md` (Reports), `templates/thread.md`, `templates/index.md` and `templates/project.md`. Everything else about a project belongs to the `project` check.

Cost: the ledger's header and Reports, the front-matter of every document, the companions' newest records and the directory listings; seconds, not minutes.

## project

Description: verifies a project's structure, IDs, language, immutables, recipes and renders against the conventions.

What it reads: one project, the path the task names, or, when the task names none, every project under `projects/` except `forge`, each reported on its own. The bookkeeping that the `light` check owns is not read for findings.

What it verifies:

- Kind: the project file `project.md` declares `kind: thought | library` and `language`. `.gitattributes` exists, and `threads/` exists in a thought project. A library needs no chain: structure reduces to the library's file set, and ID hygiene does not apply. A missing `logo.png` is never a finding.
- Structure: the files and folders of the repository layout in `CLAUDE.md` exist. A layer below the intent that the project does not have is never a finding. Recipes and renders are paired, so that every render traces to a recipe and carries provenance front-matter. Every file in `published/` traces to a recipe that carries a `## Format` section, and a `.pptx` or `.docx` in `renders/` traces to a render beside it. A recipe still carrying `## Build instructions` is a finding. The README and release-notes recipes exist. A brief whose mining record says `mined` is cited somewhere in the intent.
- ID hygiene: every rule of the ID scheme in `CLAUDE.md`, in every document that carries IDs.
- Language: prime directive 6 of `CLAUDE.md`, for every artefact and record. The briefs and renders are exempt.
- Immutables: the immutable documents (reviews, challenges, sources, research) are never edited after creation; any sign of after-the-fact editing is flagged. The `00-INDEX.md` catalogues are exempt.
- Recipes and renders, shape and freshness only: recipes conform to `templates/recipe.md` in front-matter and sections, every declared input exists, and a declared `output:` path points inside the repository. The staleness of a render is never a finding. Whether a recipe's content still matches the principal's thinking is substance, not conformance.

Owners of the rules: `CLAUDE.md` (repository layout, ID scheme, Versioning & status, prime directive 6), `templates/project.md`, `templates/recipe.md` and `templates/gitattributes`.

Cost: the project's files, read once; the conventions read from their owners.

## single-source-of-truth

Description: verifies that every rule, procedure and file shape is written in one place and cited everywhere else: no restatement across `CLAUDE.md`, skills, agents, templates and scripts, no direct operation where a mechanism exists. The honest sweep, expensive by design: fit before a major or after a round on the operating layer, not at every release.

What it reads: the whole operating layer of the engine, always the whole and never a changed subset: `CLAUDE.md`, every skill under `.claude/skills/` (supporting files included), every agent under `.claude/agents/`, every template under `templates/` and the help headers of `scripts/`. Named a project instead, it reads that project's recipes, resource indexes, ledger comments and its own `CLAUDE.md`, if any, against the owners in the engine.

What it verifies:

- One owner per rule: every command, agent, contract and template describes only its own job. A procedure, rule set or file shape that another file owns is cited by path, never restated. A restatement is a finding whatever its wording, and the fix is a reference to the owner and the deletion of the copy. Where a shape has no owner at all, the finding proposes one.
- Reviewer files carry only their own: every lens, persona and check file names its kind's contract skill and carries only its front-matter and its Lens section.
- No direct operation where a mechanism exists: no skill or agent performs directly what a script, command or agent exists for. Git outside the scripts in `scripts/`, a conversion outside `doc2md.py`, a render outside `/render`, a review outside the reviewer agents and a check outside the check agents are findings.

Owners of the rules: `CLAUDE.md`, as the principle that one mechanism lives in one place, and the owner of each rule it compares.

Cost: the whole layer, read and compared pairwise where the subjects overlap. Long by design; the report's first line says how many files were read.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Add a check](../extend/add-a-check.md): adding a check.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-10-25 for version 6.0 from the files the front-matter names; never edited by hand.
