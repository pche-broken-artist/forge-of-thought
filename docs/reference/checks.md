---
generated: 2026-11-01
version: 6.4
made: mirrored
inputs-hash: b25460795412beba
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

This page lists the checks of the forge: what each one reads, what it verifies, what it costs and when it fits. It is for the user who wants to pick a check and for the extender who wants to see how the existing ones divide the work. A check verifies conformance with the conventions. It is neither a critic of the documents nor a challenger of the thinking. Terms of the forge are defined in the [Glossary](glossary.md).

Each check is an isolated subagent: a helper that runs on its own, sees nothing of the conversation and reads the files itself. It reports its findings to Claude, and the principal (the person whose thinking is forged) settles them. To run one, see [Check conformance](../use/check-conformance.md). To add one, see [Add a check](../extend/add-a-check.md).

| Check | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `light` | A project's bookkeeping: front-matter, history companions, the ledger's reports, records, dependencies, resource indexes | A save | `.claude/agents/check-light.md` |
| `project` | A project's structure, IDs, language, immutables, recipes and renders | A release, beside `light` | `.claude/agents/check-project.md` |
| `engine` | The core against itself and against the forge intent | A release of the engine | `.claude/agents/check-engine.md` |
| `history` | The division between a document and its history | When a document is cleaned, never at a save or a release | `.claude/agents/check-history.md` |
| `single-source-of-truth` | That every rule, procedure and file shape is written in one place | Before a major release or after a round on the operating layer | `.claude/agents/check-single-source-of-truth.md` |
| `brd` | The mechanics of a BRD | After a pass of `/forge brd` | `.claude/agents/check-brd.md` |

## Which checks a save and a release run

- A save runs `light` on every repository in scope, unless it is given `--quick`, which leaves the check out.
- A release of a project runs `light` and `project` on it.
- A release of the engine runs `engine` on the engine root, and `light` and `project` on `projects/forge`, the forge's own project.
- No other check runs at a save or a release.

## light

Description: verifies a project's bookkeeping: front-matter and the history companions against the templates, the ledger script's own reports, the index entries, the published companions and the thread files against the directories and the rules. Fit for a save.

What it reads: one project (for the engine, `projects/forge`).

What it verifies, and with what rule as the owner:

- Front-matter and history, for every versioned document and its companion: the placement of the history and the form of its log. The owner is the Versioning & status section of `CLAUDE.md`, and the log form is given by `templates/history.md`. Whether a text belongs in the document or in its history is the `history` check's.
- The ledger's own reports: each line of its Reports section and each `unparsed:` line of its header is a finding, with the file it names. The owner is `templates/ledger.md`. A project whose ledger header says `shape: before the migration` is reported as `templates/project.md` says.
- Records and companions:
  - A published companion `published/<recipe>.md` agrees with the files of `published/`. A companion without its file is a finding. A file without a companion is the principal's own and never a finding.
  - Every specification in `work/` has its history companion.
  - A work file that cites an item by ID that its specification's Inputs do not name is a finding.
  - Every thread file carries the header of `templates/thread.md`, and a closed one is unchanged since its closing.
  - A state word that a record or a Verdict carries and the templates do not know is a finding.
- Dependencies: every path in the ledger's Dependencies table exists on disk. A missing library is an advisory finding that tells you to import it.
- Resource indexes: `sources/00-INDEX.md` and `research/00-INDEX.md` exist and agree with their directories. The owner is `templates/index.md`. A binary without an extract and an extract without its original are normal and never a finding. It never judges what the entries say.

Cost: seconds, not minutes. It reads the ledger's header and Reports, the front-matter of every document, the newest records of the companions and the directory listings. Most of what it finds is marked "immediate fix".

## project

Description: verifies a project's structure, IDs, language, immutables, recipes and renders against the conventions.

What it reads: one project, or, when none is named, every project under `projects/` except `forge`, each reported on its own. The bookkeeping that `light` verifies is not repeated here.

What it verifies, and with what rule as the owner:

- Kind: `project.md` declares `kind` and `language` (owner: `templates/project.md`). `.gitattributes` exists (owner: `templates/gitattributes`). A thought project has `threads/`. A library needs no chain, and `logo.png` is optional everywhere.
- Structure: the files and folders of the Repository layout in `CLAUDE.md` exist. A layer below the intent that the project does not have is never missing. Every render with provenance front-matter traces to a recipe. A file in `published/` that a companion claims traces to a recipe with a `## Format` section. The README and release-notes recipes exist. A brief marked `mined` is cited somewhere in the intent. Any other file in `renders/` or `published/` is the principal's own and never a finding.
- ID hygiene: every rule of the ID scheme in `CLAUDE.md`, in every document that carries IDs.
- Language: prime directive 6 in `CLAUDE.md`, for every artefact and record. The briefs and renders are exempt.
- Immutables: the immutable documents named in Versioning & status of `CLAUDE.md` are never edited after creation. It flags signs of editing that the ledger or the history companions reveal. The `00-INDEX.md` catalogues are exempt.
- Recipes and renders, shape only: recipes conform to `templates/recipe.md` in front-matter and sections, every declared input exists, and an `output:` path points inside the repository. The staleness of a render is never a finding.

Cost: the project's files read once, and the conventions read from their owners.

## engine

Description: verifies the core (`CLAUDE.md`, templates, skills, agents, scripts) against itself and against the forge intent: every position honoured, nothing withdrawn still advertised, every decision reflected.

What it reads: the engine root (`CLAUDE.md`, `templates/`, `.claude/skills/`, `.claude/agents/`, `scripts/`) and the forge intent with its threads and decisions. The forge project's own conformance belongs to `project` and `light`. Whether a rule is stated in more than one place belongs to `single-source-of-truth`.

What it verifies:

- Core internal consistency:
  - The commands table of `CLAUDE.md` agrees with the skills in `.claude/skills/*/SKILL.md`.
  - The agents described agree with `.claude/agents/`.
  - Every skill an agent names in its front-matter exists.
  - Every file in `scripts/` is described in `CLAUDE.md`, and nothing described there is missing on disk.
  - The README agrees with `CLAUDE.md` on the chain, the conventions and the command set. Currency is not checked, because the README is regenerated at the release.
  - The templates agree with the conventions of `CLAUDE.md`: front-matter fields, the history companion, prefixes, numbering and statuses.
- Core against the forge intent: every position is honoured, and nothing withdrawn or rejected is still advertised in the core. Decisions that the intent cites exist in the decisions file, and every decision is reflected in the intent where it applies.
- Rename and removal sweep: old names and dropped terms are searched for. Only historical records may still contain them.

Cost: the core files once and the intent's positions once. Minutes at most, so that a release can afford it every time.

## history

Description: reads a document with its history and reports where the division between them does not hold, proposing each move in full. Fit when a document is cleaned, never at a save or a release.

What it reads: one project (for the engine, `projects/forge`), and in it every versioned document with its history and archive, or the one document the task names.

What it verifies, with the owners `CLAUDE.md` (Versioning & status) and the intent definition `.claude/skills/forge/states/intent.md` (Threads and files):

- In the document, the way to an item (as Versioning & status lists it) is a finding. So is detail that an item carries where the file that performs it exists.
- The other way round, an item that can no longer be understood because what makes it hold stands only in the history is a finding.
- Each finding proposes the move in full: the text that leaves, word for word, and the record it becomes.

The form of the log belongs to `light`.

Cost: whole documents with their histories, minutes rather than seconds.

## single-source-of-truth

Description: verifies that every rule, procedure and file shape is written in one place and cited everywhere else: no restatement across `CLAUDE.md`, skills, agents, templates and scripts, no direct operation where a mechanism exists. The honest sweep; expensive by design.

What it reads: the whole operating layer of the engine, never a changed subset: `CLAUDE.md`, every skill under `.claude/skills/` with its supporting files, every agent, every template and the help headers of `scripts/`. When a project is named instead, it reads that project's recipes, resource indexes, ledger comments and its own `CLAUDE.md`, if any, against the owners in the engine.

What it verifies:

- One owner per rule: a command, agent, contract or template describes only its own job. A procedure, rule set or file shape that another file owns is cited by path and not restated. A restatement is a finding, and the fix is a reference to the owner and the deletion of the copy. Where a shape has no owner, the finding proposes one.
- Reviewer files carry only their own: every lens, persona and check file names its kind's contract skill and carries only its front-matter and its Lens section.
- No direct operation where a mechanism exists: no skill or agent performs directly what a script, command or agent exists for. The examples are git outside the scripts, a conversion outside `doc2md.py`, a render outside `/render`, a review outside the reviewer agents and a check outside the check agents.

Cost: the whole layer, read and compared pairwise where subjects overlap. Long by design. The report's first line says how many files it read.

## brd

Description: verifies a BRD's mechanics: every parent item carried, every cited ID existing, every item with a parent, the phasing present, every term defined, no link in an item. Fit after a pass of `/forge brd`.

What it reads: one project's `30-brd.md` with its parent as the BRD's header declares it (`20-assignment.md` or `10-intent.md`). A BRD made from a source is a work product in `work/`, read when the task names it. A project without a BRD is not a finding. The bookkeeping of the file belongs to `light` and the ID scheme in general to `project`.

What it verifies, with the owners `templates/brd.md` and `.claude/skills/forge/states/brd.md`:

- Traceability: every in-scope item of the parent is carried by at least one BR or UC, unless an OOS, a DEP or a TBC of the BRD names it. Every parent that an item cites exists in the parent. The appendix table matches the items. Where the parent is a source, the cited path is verified to exist and the place is read as a fact.
- Every item has a parent: a BR and an NFR end with their parent or, for an NFR, its category. A UC declares its parent in its `Carries` line. Where the parent is a source with speakers, a BR whose every cited place is another party's turn is a finding.
- The sections that may not be silent:
  - Phasing is present and not empty, and every BR and UC stands in a phase or in the `not phased` row.
  - Every area of the roster that the BRD cites is in the Touched areas table.
  - Every role the roster names as signing or reviewing is in the Stakeholders table or named as absent with a reason.
  - An ASM whose content answers what a TBC of the same BRD asks is a finding.
  - Every NFR category kept carries a value or a TBC with an owner.
  - Every TBC has an owner and says whether it blocks estimation.
- Terms and links: every capitalised term of an item is in the Terms table, no item depends on a link, and no name of a person stands where the template asks for a role.
- Skeleton residue: no template comment, `…`, `<placeholder>` or `NNNN` is left in the file.

Cost: the BRD and its parent read once, and the roster the BRD cites read for its list of areas only.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Add a check](../extend/add-a-check.md): adding a check.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-01 for version 6.4 from the files the front-matter names; never edited by hand.
