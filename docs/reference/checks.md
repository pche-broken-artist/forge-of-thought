---
generated: 2026-11-08
version: 7.0
made: mirrored
inputs-hash: 314c188ab814dcb2
inputs:
  - .claude/agents/check-light.md
  - .claude/agents/check-project.md
  - .claude/agents/check-engine.md
  - .claude/agents/check-history.md
  - .claude/agents/check-single-source-of-truth.md
  - .claude/agents/check-brd.md
  - .claude/agents/check-user-stories.md
  - .claude/skills/save/SKILL.md
  - .claude/skills/release/SKILL.md
---

# Checks

This page lists the checks of the forge: the reviewers that verify mechanical conformance with the conventions, one concern each, never the substance or the quality of a document. You use it to pick the check that fits, whether you run one (see [Check conformance](../use/check-conformance.md)) or add one (see [Add a check](../extend/add-a-check.md)). Terms of the forge are one line each in the [Glossary](glossary.md).

A check runs as an isolated subagent, that is a helper of Claude that sees nothing of the conversation. Its findings are advisory: the principal, whose thinking is being forged, decides what to do with them. A run that finds nothing files nothing. Each check names a project by its slug, or the engine.

## Overview

| Name | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `light` | A project's bookkeeping: front-matter, history companions, the ledger's own reports, index entries, published companions, thread files | A save | `.claude/agents/check-light.md` |
| `project` | A project's structure, IDs, language, immutables, recipes and renders | A release, beside `light` | `.claude/agents/check-project.md` |
| `engine` | The core against itself and against the forge intent | A release | `.claude/agents/check-engine.md` |
| `history` | The division between a document and its history | When a document is cleaned, never at a save or a release | `.claude/agents/check-history.md` |
| `single-source-of-truth` | That every rule, procedure and file shape is written in one place | Before a major release or after a round on the operating layer, not at every release | `.claude/agents/check-single-source-of-truth.md` |
| `brd` | The mechanics of a BRD | After a pass of `/forge brd` | `.claude/agents/check-brd.md` |
| `user-stories` | The mechanics of user stories | After a pass of `/forge user-stories` | `.claude/agents/check-user-stories.md` |

## Which checks a save and a release run

- A save runs `light` on every repository in scope, unless it was given `--quick`. A save never waits on a finding the principal has not asked to fix.
- A release of a project runs `light` and `project` on it.
- A release of the engine runs `engine` on the engine root, and `light` and `project` on the forge's own project. The checks are launched at once and awaited together.
- The other four checks (`history`, `single-source-of-truth`, `brd`, `user-stories`) run neither at a save nor at a release.

## light

Description: Check "light" - verifies a project's bookkeeping: front-matter and the history companions against the templates, the ledger script's own reports, the index entries, the published companions and the thread files against the directories and the rules. Fit for a save. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.

What it reads: one project, by the path of the task (for the engine, the forge's own project). It is the check a save can afford: bookkeeping only. Everything else about a project belongs to `project`.

What it verifies, with the owner of each rule:

- Front-matter and history of every versioned document and its companion: the placement of the history and the form of its log. The owners are the section Versioning & status of `CLAUDE.md` and `templates/history.md`. Whether a text belongs in the document or in its history belongs to `history`.
- The ledger's own reports: each line of its Reports section and each `unparsed:` line of its header is a finding, with the file it names. The owner is `templates/ledger.md`. A ledger whose header says `shape: before the migration` is reported as `templates/project.md` says.
- Records and companions:
  - A published companion without its file is a finding. A file in `published/` without a companion is the principal's own and is never one.
  - Every specification in `work/` has its history companion.
  - A work file that cites an item by ID that is not among its specification's inputs is a finding.
  - Every thread file carries the header of `templates/thread.md`, and a closed one is unchanged since its closing.
  - A state word that a record or a verdict carries and the templates do not know is a finding. A review or decision record keeps the word it was written with.
- Dependencies: every path in the Dependencies table exists on disk. A missing library is an advisory finding.
- Resource indexes: `sources/00-INDEX.md` and `research/00-INDEX.md` exist and agree with their directories, bundle indexes included. A sources entry without its `Date` and `Form` fields is an immediate fix (owner: `templates/index.md`). A binary without an extract, or an extract without its original, is the normal case. A binary listed in `sources/.gitignore` is not an unregistered file. It never judges what the entries say.

Most of what it finds is pure bookkeeping, marked "immediate fix".

Cost: the ledger's header and Reports, the front-matter of every document, the newest records of the companions and the directory listings. Seconds, not minutes.

## project

Description: Check "project" - verifies a project's structure, IDs, language, immutables, recipes and renders against the conventions. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.

What it reads: one project by the path of the task, or, when the task names none, every project under `projects/` except the forge's own, each reported on its own. Run beside `light` at a release, it verifies everything but the bookkeeping.

What it verifies, with the owner of each rule:

- Kind: `project.md` declares `kind: thought | library` and `language`; `.gitattributes` exists; `threads/` exists in a thought project. Owners: `templates/project.md` and `templates/gitattributes`. A library needs no chain, and the absence of `logo.png` is never a finding.
- Structure: the files and folders of the section Repository layout of `CLAUDE.md` exist. A layer below the intent that the project does not have is not missing. The rules for `recipes/`, `renders/` and `published/` are the section Document chain, Renders of `CLAUDE.md`:
  - A render with provenance front-matter traces to a recipe.
  - A file in `published/` that a companion claims traces to a recipe with a `## Format` section.
  - Any other file in `renders/` or `published/` is the principal's own and is never a finding.
  - A recipe that still carries `## Build instructions` is a finding fixed at its next iteration (owner: `templates/recipe.md`).
  - The README and release-notes recipes exist.
  - A brief whose mining record says `mined` is cited somewhere in the intent.
- ID hygiene: every rule of the section ID scheme of `CLAUDE.md`, in every document that carries IDs.
- Language: prime directive 6 of `CLAUDE.md`, for every artefact and record. The briefs and renders are exempt.
- Immutables: the immutable documents named in Versioning & status of `CLAUDE.md` are never edited after creation. Signs of after-the-fact editing that the ledger or the history companions reveal are flagged. The `00-INDEX.md` catalogues are exempt.
- Recipes and renders, shape and freshness only: recipes conform to `templates/recipe.md` and its genre skeletons; every declared input exists; a declared `output:` points inside the repository. The staleness of a render is never a finding. Whether a recipe still matches the principal's thinking is substance, not conformance.

Cost: the project's files, read once; the conventions read from their owners.

## engine

Description: Check "engine" - verifies the core (CLAUDE.md, templates, skills, agents, scripts) against itself and against the forge intent: every position honoured, nothing withdrawn still advertised, every decision reflected. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.

What it reads: the engine root of the task (`CLAUDE.md`, `templates/`, `.claude/skills/`, `.claude/agents/`, `scripts/`) and the forge intent with its threads and its decisions record. The conformance of the forge's own project belongs to `project` and `light`. Whether a rule is stated in more than one place belongs to `single-source-of-truth`.

What it verifies, with the owner of each rule:

- Core internal consistency, against `CLAUDE.md`:
  - The commands table matches the skills on disk, the reviewers' contracts excepted.
  - The agents described match `.claude/agents/`.
  - Every skill an agent names in its front-matter exists.
  - Every file in `scripts/` is described in `CLAUDE.md`, and nothing described there is missing on disk.
  - The README agrees with `CLAUDE.md` on chain, conventions and command set. Currency is not checked, since the README and the release notes are regenerated at the release after this check.
  - The templates agree with the conventions as `CLAUDE.md` states them: front-matter fields, the history companion, prefixes, numbering and statuses.
- Core and forge intent:
  - Every position of the intent is honoured by the core documents.
  - Nothing withdrawn or rejected is still advertised in the core.
  - Decisions referenced from the intent exist in the decisions record, and every decision record is reflected in the intent where it applies.
- Rename and removal sweep: the old names recorded in decision records, and the terms the principal has dropped, appear only in historical records (history companions, decisions, rejected directions, reviews, challenges, research).

Cost: the core files once and the intent's positions once. Minutes at most, so that a release can afford it every time.

## history

Description: Check "history" - reads a document with its history and reports where the division between them does not hold, proposing each move in full. Fit when a document is cleaned, never at a save or a release. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.

What it reads: one project by the path of the task (for the engine, the forge's own project), and in it every versioned document with its history and its archive, or the one document the task names.

What it verifies: the division between a document and its history. The owners are the section Versioning & status of `CLAUDE.md` and the Threads and files section of `.claude/skills/forge/states/intent.md`.

- In the document, the way to an item (as Versioning & status lists it) is a finding. So is detail an item carries where the file that performs it exists.
- The other way round, an item that can no longer be understood because what makes it hold stands only in the history is a finding.
- Each finding proposes the move in full: the text that leaves, word for word, and the record it becomes.

The form of the log belongs to `light`.

Cost: whole documents with their histories. Minutes rather than seconds. It is never composed into a save or a release.

## single-source-of-truth

Description: Check "single-source-of-truth" - verifies that every rule, procedure and file shape is written in one place and cited everywhere else: no restatement across CLAUDE.md, skills, agents, templates and scripts, no direct operation where a mechanism exists. The honest sweep; expensive by design - fit before a major or after a round on the operating layer, not at every release. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.

What it reads: the whole operating layer of the engine, always the whole and never a changed subset: `CLAUDE.md`, every skill under `.claude/skills/` with its supporting files, every agent under `.claude/agents/`, every template under `templates/` and the help headers of `scripts/`. Named a project instead, it reads that project's recipes, resource indexes, ledger comments and its own `CLAUDE.md`, if any, against the owners in the engine.

What it verifies, with the owner of each rule: one mechanism lives in one place (the rule is stated in the section Prime directives of `CLAUDE.md`).

- One owner per rule. Every command, agent, contract and template describes only its own job. A procedure, rule set or file shape that another file owns is cited by path, never restated. A restatement is a finding, and the fix is a reference to the owner and the deletion of the copy. Where a shape has no owner, the finding proposes one.
- Reviewer files carry only their own. Every lens, persona and check file names its kind's contract skill and carries only its front-matter and its Lens section.
- No direct operation where a mechanism exists. No skill or agent performs directly what a script, command or agent exists for: git outside the scripts of `scripts/`, a conversion outside `doc2md.py`, a render outside `/render`, a review outside the reviewer agents, a check outside the check agents.

Cost: the whole layer, read and compared pairwise where the subjects overlap. Long by design. The first line of its report says how many files it read.

## brd

Description: Check "brd" - verifies a BRD's mechanics: every parent item carried, every cited ID existing, every item with a parent, the phasing present, every term defined, no link in an item. Fit after a pass of /forge brd. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.

What it reads: one project's `30-brd.md`, by the path of the task or the project's BRD, with its parent as the BRD's header declares it (`20-assignment.md` or `10-intent.md`). A BRD made from a source is a work product in `work/`, read when the task names it. A project without a BRD is not a finding. The bookkeeping of the file belongs to `light` and the ID scheme in general to `project`.

What it verifies, with the owner of each rule (`templates/brd.md` and the Requirement style section of `.claude/skills/forge/states/brd.md`):

- Traceability:
  - Every in-scope item of the parent is carried by at least one BR or UC, unless an OOS, a DEP or a TBC of the BRD names it.
  - Every parent cited by an item exists in the parent.
  - The appendix table matches the items.
  - Where the parent is a source, the citation is a path and a place; the path is verified and the place is read as a fact.
- Every item has a parent:
  - A BR and an NFR end with their parent. An NFR may end with its category instead.
  - A UC declares its parent in its `Carries` line.
  - Where the parent is a source with speakers, a BR whose every cited place is another party's turn is a finding.
- The sections that may not be silent:
  - Phasing is present and not empty, and every BR and UC stands in a phase or in the `not phased` row.
  - Every area of the roster the BRD cites is in the Touched areas table.
  - Every role the roster names as signing or reviewing is in the Stakeholders table or named as absent with a reason.
  - An ASM whose content answers what a TBC of the same BRD asks is a finding.
  - Every NFR category kept carries a value or a TBC with an owner.
  - Every TBC has an owner and says whether it blocks estimation.
- Terms and links: every capitalised term of an item is in the Terms table; no item depends on a link; no name of a person stands where the template asks for a role.
- Skeleton residue: no template comment, no `…`, no `<placeholder>`, no `NNNN` is left in the file. `owner: unassigned` is not residue.

Cost: the BRD and its parent, read once; the roster the BRD cites, read for its list of areas only.

## user-stories

Description: Check "user-stories" - verifies the mechanics of user stories: every parent item served or said not to be, every story with a Reference to an existing item, the fixed parts in their order and none left empty, questions with an owner, risks with a mitigation or consequences, notes with a link and what lies behind it, no vague word in a criterion. Fit after a pass of /forge user-stories. Verifies conformance with the conventions. Not a critic of the documents, not a challenger of the thinking.

What it reads: one project's `35-user-stories.md`, by the path of the task or the project's stories, with its parent as the header declares it (`30-brd.md` or `10-intent.md`). Stories made from a source are a work product in `work/`, read when the task names them. A project without stories is not a finding. The bookkeeping of the file belongs to `light` and the ID scheme in general to `project`.

What it verifies, against `.claude/skills/forge/states/user-stories.md` (its Aim and its Story style) and `templates/user-stories.md`:

- Coverage: every in-scope item of the parent is cited in the Reference of at least one story, unless the stories or the parent say why not. Coverage is counted, never judged.
- Reference: every story has a Reference; every ID it cites exists in the parent (or, for a DEP, in the BRD); a story citing only a position of the intent has `10-intent.md` as its parent. Where the parent is a source, the path is verified and the place is read as a fact.
- Shape: every story is a level-3 heading `US.NNNN — <name>`, then its sentence, then its acceptance criteria as bullets, then only the parts it has, in the template's order, under the fixed English labels. No part is present and empty, no other part appears, and no two stories share an ID.
- Parts: every question ends with `→ <owner>`; every risk has `→ <mitigation | consequences>`; every note carries a link and what lies behind it; every edge case is `situation → what happens`.
- Wording: no vague word in an acceptance criterion where a value is wanted. It reports the word and the place and never proposes the value. A criterion in the conditional mood is a finding.
- Skeleton residue: no template comment, no `…`, no `<placeholder>`, no `NNNN` is left in the file.

Cost: the stories and their parent, read once.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Add a check](../extend/add-a-check.md): adding a check.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
