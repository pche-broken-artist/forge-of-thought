---
generated: 2026-11-08
version: 6.21
made: mirrored
inputs-hash: 8d93dd93475885d0
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

This page lists the checks of the forge: the reviewers that verify mechanical conformance of a project or of the engine with the conventions. It is for the user who picks a check to run and for the extender who needs to know what each one owns. A check is advisory: it reports findings, and only the principal (the person whose thinking is being forged) decides what is done with them. A check is neither a critic of the documents nor a challenger of the thinking.

## Overview

| Name | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `light` | A project's bookkeeping: front-matter, history companions, the ledger's own reports, records, dependencies, resource indexes. | A save. Also run at every release. | `.claude/agents/check-light.md` |
| `project` | A project's structure, IDs, language, immutables, recipes and renders. | A release, beside `light`. | `.claude/agents/check-project.md` |
| `engine` | The core against itself and against the forge intent. | A release of the engine. | `.claude/agents/check-engine.md` |
| `history` | The division between a document and its history. | When a document is cleaned; never at a save or a release. | `.claude/agents/check-history.md` |
| `single-source-of-truth` | That every rule, procedure and file shape is written in one place and cited elsewhere. | Before a major release or after a round on the operating layer; not at every release. | `.claude/agents/check-single-source-of-truth.md` |
| `brd` | The mechanics of a BRD. | After a pass of `/forge brd`. | `.claude/agents/check-brd.md` |
| `user-stories` | The mechanics of user stories. | After a pass of `/forge user-stories`. | `.claude/agents/check-user-stories.md` |

## Which checks a save and a release run

- A save runs `light` on every repository in scope, unless `--quick` leaves the check out.
- A release of a project runs `light` and `project` on it.
- A release of the engine runs `engine` on the engine root, and `light` and `project` on `projects/forge`, the forge's own project.
- The other checks run only when the principal asks for them.

## light

Description: verifies a project's bookkeeping: front-matter and the history companions against the templates, the ledger script's own reports, the index entries, the published companions and the thread files against the directories and the rules. Fit for a save.

Reads: one project; for the engine that is `projects/forge`.

Verifies:

- Front-matter and history: every rule of the versioning section of `CLAUDE.md` for every versioned document and its companion, the placement of the history and the form of its log as `templates/history.md` gives it. Whether a text belongs in the document or in its history belongs to the `history` check.
- The ledger's own reports: each line of the Reports section and each `unparsed:` line of the ledger header is a finding, with the file it names (owner: `templates/ledger.md`). A project whose ledger header says `shape: before the migration` is reported as `templates/project.md` says.
- Records and companions:
  - A published companion without its file is a finding; a file without a companion is the principal's own and never one.
  - Every specification in `work/` has its history companion.
  - A work file that cites an item by ID not named among its specification's Inputs is a finding.
  - Every thread file carries the header of `templates/thread.md`, and a closed one is unchanged since its closing.
  - A state word that a record or a verdict carries and the templates do not know is a finding.
- Dependencies: every path in the Dependencies table exists on disk. A missing library is an advisory finding.
- Resource indexes: `sources/00-INDEX.md` and `research/00-INDEX.md` exist and agree with their directories (owner: `templates/index.md`). A binary without an extract, and an extract without its original, is the normal case and never a finding. The check never judges what the entries say.

Cost: the ledger's header and Reports, the front-matter of every document, the newest records of the companions and the directory listings. Seconds, not minutes. Most of what it finds is pure bookkeeping, marked as an immediate fix.

## project

Description: verifies a project's structure, IDs, language, immutables, recipes and renders against the conventions.

Reads: one project, or, when no project is named, every project under `projects/` except `forge`, each reported on its own. The bookkeeping covered by `light` is not repeated here.

Verifies:

- Kind: `project.md` declares `kind` and `language` (owner: `templates/project.md`); `.gitattributes` exists (owner: `templates/gitattributes`); `threads/` exists in a thought project. A library needs no chain, and its documents may be overwritten by their owner. The absence of `logo.png` is never a finding.
- Structure: the files and folders of the repository layout in `CLAUDE.md` exist. A layer below the intent that the project does not have is never a finding. Renders with provenance trace to a recipe, and published files that a companion claims trace to a recipe with a `## Format` section. Other files in `renders/` and `published/` are the principal's own. The README and release-notes recipes exist. A brief whose mining record says `mined` is cited somewhere in the intent.
- ID hygiene: the ID scheme of `CLAUDE.md`, in every document that carries IDs.
- Language: the language rule of `CLAUDE.md` for every artefact and record; the briefs and renders are exempt.
- Immutables: the immutable documents are never edited after creation. The `00-INDEX.md` catalogues are exempt.
- Recipes and renders: recipes conform to `templates/recipe.md` in front-matter and sections; every declared input exists; an `output:` path points inside the repository. The staleness of a render is never a finding.

Cost: the project's files, read once, with the conventions read from their owners.

## engine

Description: verifies the core (`CLAUDE.md`, templates, skills, agents, scripts) against itself and against the forge intent: every position honoured, nothing withdrawn still advertised, every decision reflected.

Reads: the engine root, and the forge intent with its threads and decisions. The conformance of the forge project itself belongs to `project` and `light`; whether a rule is stated in more than one place belongs to `single-source-of-truth`.

Verifies:

- Core internal consistency:
  - The commands table of `CLAUDE.md` agrees with the skills on disk, the described agents with `.claude/agents/`, and every skill an agent names in its front-matter exists.
  - Every file in `scripts/` is described in `CLAUDE.md`, and nothing described there is missing on disk.
  - The README agrees with `CLAUDE.md` on chain, conventions and command set. Currency is not checked, because the README is regenerated at the release.
  - `templates/` agree with the conventions of `CLAUDE.md` (front-matter fields, history companion, prefixes, numbering, statuses).
- Core against the forge intent: every position is honoured by the core documents; nothing withdrawn or rejected is still advertised; decisions the intent cites exist and every decision is reflected where it applies.
- Rename and removal sweep: old names recorded in decisions, and terms the principal dropped, appear only in historical records.

Cost: the core files once and the intent's positions once. Minutes at most, so that a release can afford it every time.

## history

Description: reads a document with its history and reports where the division between them does not hold, proposing each move in full. Fit when a document is cleaned, never at a save or a release.

Reads: one project, and in it every versioned document with its history and archive, or the one document the task names.

Verifies (owners: the versioning section of `CLAUDE.md` and the intent's definition, `.claude/skills/forge/states/intent.md`):

- The way to an item, as the versioning section lists it, stands in the document: a finding.
- Detail an item carries where the file that performs it exists: a finding.
- An item that cannot be understood because what makes it hold stands only in the history: a finding.

Each finding proposes the move in full: the text that leaves, word for word, and the record it becomes. The form of the log belongs to `light`.

Cost: whole documents with their histories, minutes rather than seconds.

## single-source-of-truth

Description: verifies that every rule, procedure and file shape is written in one place and cited everywhere else: no restatement across `CLAUDE.md`, skills, agents, templates and scripts, no direct operation where a mechanism exists. The honest sweep; expensive by design.

Reads: the whole operating layer of the engine, never a changed subset: `CLAUDE.md`, every skill with its supporting files, every agent, every template and the help headers of `scripts/`. Named a project instead, it reads that project's recipes, resource indexes, ledger comments and its own `CLAUDE.md` against the owners in the engine.

Verifies:

- One owner per rule: a procedure, rule set or file shape that another file owns is cited by path, never restated. The fix is a reference to the owner and the deletion of the copy. Where a shape has no owner, the finding proposes one.
- Reviewer files carry only their own: every lens, persona and check file names its kind's contract skill and carries only its front-matter and its Lens section.
- No direct operation where a mechanism exists: no git outside the scripts, no conversion outside `doc2md.py`, no render outside `/render`, no review outside the reviewer agents, no check outside the check agents.

Cost: the whole layer, read and compared pairwise where the subjects overlap. Long by design; the report's first line says how many files were read.

## brd

Description: verifies a BRD's mechanics: every parent item carried, every cited ID existing, every item with a parent, the phasing present, every term defined, no link in an item. Fit after a pass of `/forge brd`.

Reads: one project's `30-brd.md` with its parent as the BRD's header declares it (`20-assignment.md` or `10-intent.md`); a BRD made from a source is a work product read when the task names it. A project without a BRD is not a finding. The bookkeeping belongs to `light` and the ID scheme in general to `project`.

Verifies (owners: `templates/brd.md` and `.claude/skills/forge/states/brd.md`):

- Traceability: every in-scope parent item is carried by at least one BR or UC, unless an OOS, a DEP or a TBC names it; every cited parent exists; the appendix table matches the items.
- Every item has a parent: a BR and an NFR end with their parent or, for an NFR, its category; a UC declares its parent in its `Carries` line.
- The sections that may not be silent: Phasing is present, not empty, and every BR and UC stands in a phase or in the `not phased` row; the areas of a cited roster are in the Touched areas table; roles that sign or review are in the Stakeholders table or named as absent with a reason; every kept NFR category carries a value or a TBC with an owner; every TBC has an owner and says whether it blocks estimation.
- Terms and links: every capitalised term of an item is in the Terms table; no item depends on a link; no name of a person stands where the template asks for a role.
- Skeleton residue: no template comment, `…`, `<placeholder>` or `NNNN` is left in the file.

Cost: the BRD and its parent, read once; the cited roster is read for its list of areas only.

## user-stories

Description: verifies the mechanics of user stories: every parent item served or said not to be, every story with a Reference to an existing item, the fixed parts in their order and none left empty, questions with an owner, risks with a mitigation or consequences, notes with a link and what lies behind it, no vague word in a criterion. Fit after a pass of `/forge user-stories`.

Reads: one project's `35-user-stories.md` with its parent as the header declares it (`30-brd.md` or `10-intent.md`); stories made from a source are a work product read when the task names them. A project without stories is not a finding. The bookkeeping belongs to `light` and the ID scheme in general to `project`. The rules it verifies against are `.claude/skills/forge/states/user-stories.md` and `templates/user-stories.md`.

Verifies:

- Coverage: every in-scope parent item is cited in the Reference of at least one story, unless the stories or the parent say why not. Coverage is counted, never judged.
- Reference: every story has a Reference; every ID it cites exists in the parent (a DEP in the BRD); a story citing only a POS has `10-intent.md` as parent.
- Shape: each story is a level-3 heading `US.NNNN — <name>`, then its sentence, its acceptance criteria as bullets, then only the parts it has in the template's order under the fixed English labels; no part present and empty; no other part; no two stories with one ID.
- Parts: every question ends with `→ <owner>`; every risk has `→ <mitigation | consequences>`; every note carries a link and what lies behind it; every edge case is `situation → what happens`.
- Wording: a vague word in an acceptance criterion where a value is wanted is reported with its word and place, without a proposed value; a criterion in the conditional mood is a finding.
- Skeleton residue: no template comment, `…`, `<placeholder>` or `NNNN` is left in the file.

Cost: the stories and their parent, read once.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Add a check](../extend/add-a-check.md): adding a check.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
