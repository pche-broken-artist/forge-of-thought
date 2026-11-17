---
generated: 2026-11-17
version: 7.12
made: mirrored
inputs-hash: dcd4d88840d7ad4f
inputs:
  - .claude/agents/check-light.md
  - .claude/agents/check-project.md
  - .claude/agents/check-engine.md
  - .claude/agents/check-history.md
  - .claude/agents/check-boundary.md
  - .claude/agents/check-single-source-of-truth.md
  - .claude/agents/check-brd.md
  - .claude/agents/check-user-stories.md
  - .claude/skills/save/SKILL.md
  - .claude/skills/release/SKILL.md
---

# Checks

This page lists the eight checks of the forge: what each one verifies,
what it reads, what it costs and when it fits. It is for the one who
runs a check and for the one who adds another. Each check is a
reviewer that verifies conformance with the conventions. It is not a
critic of the documents and not a challenger of the thinking.

A check is advisory. Its findings are settled in a walkthrough, that
is, one item per message with the principal's verdict on each. The
principal is the person whose thinking is being forged.

| Name | What it is for | When it fits | Where it lives |
|---|---|---|---|
| `light` | A project's bookkeeping: front-matter, history companions, the ledger's reports, indexes, published companions, threads | A save | `.claude/agents/check-light.md` |
| `project` | A project's structure, IDs, language, immutables, recipes, renders and the shape of whole files | A release | `.claude/agents/check-project.md` |
| `engine` | The core against itself and against the forge intent | A release | `.claude/agents/check-engine.md` |
| `history` | The division between a document and its history | When a document is cleaned | `.claude/agents/check-history.md` |
| `boundary` | The division between an intent and its solution design | After a round on the intent, or before a major | `.claude/agents/check-boundary.md` |
| `single-source-of-truth` | That every rule, procedure and file shape is written in one place | Before a major, or after a round on the operating layer | `.claude/agents/check-single-source-of-truth.md` |
| `brd` | The mechanics of a BRD | After a pass of `/forge brd` | `.claude/agents/check-brd.md` |
| `user-stories` | The mechanics of user stories | After a pass of `/forge user-stories` | `.claude/agents/check-user-stories.md` |

## Which checks a save and a release run

A save runs `light` on every repository in scope, unless it is given
`--quick`, which leaves the check out. A release runs `light` and
`project` on a project. For the engine it runs `engine` on the engine
root, and `light` and `project` on the forge's own project. No other
check is run by either.

## light

**Description.** Verifies a project's bookkeeping: front-matter and
the history companions against the templates, the ledger script's own
reports, the index entries, the published companions and the thread
files against the directories and the rules. Fit for a save.

**Reads.** One project, the path the task names; for the engine, that
is `projects/forge`.

**Verifies.**

- Front-matter and history, against Versioning & status in
  `CLAUDE.md`, for every versioned document and its companion: where
  the history stands, and the form of its log as `templates/history.md`
  gives it. A Version History table in a document or its companion is
  a finding. It is settled by moving the table, untouched, to
  `<file>.history.archive.md`, on the principal's word, project by
  project.
- The ledger's own reports: each line of its Reports section and each
  `unparsed:` line of its header (`templates/ledger.md`) is a finding,
  with the file it names. The ledger is the state of a project, built
  from its documents at read time. A ledger whose header says `shape:
  before the migration` is reported as `templates/project.md` says.
- Records and companions: a published companion without its file is a
  finding; a published file without a companion is the principal's own
  and never one. Every specification in `work/` has its history
  companion. A work file that cites an item by ID not named among its
  specification's Inputs is a finding. Every thread file carries the
  header of `templates/thread.md`, and a closed one is unchanged since
  its closing. A state word that the templates do not know is a
  finding.
- Dependencies: every path in the Dependencies table exists on disk. A
  missing library is reported as an advisory finding.
- Resource indexes: `sources/00-INDEX.md` and `research/00-INDEX.md`
  exist and agree with their directories, bundles and the indexes
  inside them included. A sources entry without its `Date` and `Form`
  fields is an immediate fix. A binary without an extract, and an
  extract without its original, are the normal case. What the entries
  say is never judged.
- What a save added, against its template: of a file made from a
  template, it reads the newest of what the file holds (the header,
  the newest records of a history, the newest record of
  `decisions.md`). The whole of a file against its template is the
  `project` check's.

Most of what it finds is bookkeeping, marked "immediate fix".

**Cost.** The ledger's header and Reports, the front-matter of every
document, the companions' newest records and the directory listings:
seconds, not minutes.

## project

**Description.** Verifies a project's structure, IDs, language,
immutables, recipes and renders against the conventions.

**Reads.** One project, the path the task names, or, when the task
names none, every project under `projects/` except `forge`, each
reported on its own. The bookkeeping is the `light` check's. At a
release it runs beside `light` and verifies everything else.

**Verifies.**

0. Kind: `project.md` declares `kind: thought | library` and
   `language`; `.gitattributes` exists; `threads/` exists in a thought
   project. A library needs no chain, so its structure reduces to the
   library's file set and ID hygiene does not apply. `logo.png` is
   optional and its absence is never a finding.
1. Structure: the files and folders of the layout in `CLAUDE.md`
   exist. A layer below the intent that a project does not have is not
   missing. Every render with provenance front-matter traces to a
   recipe, and every published file that a companion claims traces to
   a recipe with a `## Format` section. Any other file in `renders/`
   or `published/` is the principal's own, never a finding. A recipe
   still carrying `## Build instructions` is a finding fixed at its
   next iteration. The README and release-notes recipes exist. A brief
   whose mining record says `mined` is cited somewhere in the intent.
2. ID hygiene: the ID scheme in `CLAUDE.md` and the table of prefixes
   in `.claude/reference/id-prefixes.md`, in every document that
   carries IDs.
3. Language: prime directive 6 of `CLAUDE.md`, for every artefact and
   record. A brief is exempt, a render is in the languages its recipe
   declares, and the file of a work product is in the language its
   specification's `## Making` says.
4. Immutables: the immutable documents of Versioning & status are
   never edited after creation. It flags signs of after-the-fact
   editing that the ledger or the history companions reveal. The
   `00-INDEX.md` catalogues are exempt.
5. Recipes and renders, shape and freshness, never content: a recipe
   extends `templates/recipe.md`; every declared input exists on disk;
   the `output:` path points inside the repository. The staleness of a
   render is never a finding.
6. Shape: every file made from a template is read whole against it,
   the artefacts of the chain included: the header, the fixed parts
   and fields in their order, the words the template gives. An
   optional part, a section left out because it was empty, and a
   comment still carried from a skeleton are never findings. A closed
   thread, an archive, a research and a source are not read for their
   shape.

**Cost.** The project's files, read once; the conventions read from
their owners.

## engine

**Description.** Verifies the core (`CLAUDE.md`, templates, skills,
agents, scripts) against itself and against the forge intent: every
position honoured, nothing withdrawn still advertised, every decision
reflected.

**Reads.** The engine root the task names: `CLAUDE.md`,
`.claude/reference/`, `templates/`, `.claude/skills/`,
`.claude/agents/`, `scripts/`, and the forge intent,
`projects/forge/10-intent.md`, with its threads and
`projects/forge/decisions.md`. Whether a rule is stated in more than
one place is the `single-source-of-truth` check's.

**Verifies.**

1. Core internal consistency:
   - The table of commands (`.claude/reference/commands.md`) agrees
     with the skills in `.claude/skills/*/SKILL.md`; the agents
     described agree with `.claude/agents/`; every skill an agent
     names in its front-matter exists.
   - Every file in `scripts/` is described in
     `.claude/reference/repository-layout.md`, with its governing rule
     in `CLAUDE.md` where it has one, and nothing described there is
     missing on disk.
   - The README agrees with `CLAUDE.md` and the table of commands:
     same chain, same conventions, same command set. Currency is not
     checked, because the README is a render regenerated at the
     release.
   - The templates agree with the conventions: front-matter fields,
     the history companion, prefixes, numbering, statuses.
2. Core against the forge intent: every position is honoured by the
   core documents; nothing withdrawn or rejected is still advertised
   in the core. Decisions referenced from the intent exist in
   `decisions.md`, and every decision record is reflected in the
   intent where it applies.
3. Rename and removal sweep: the old names recorded in decisions and
   the terms the principal has dropped appear only in historical
   records.

**Cost.** The core files once and the intent's positions once: minutes
at most, so that a release can afford it every time.

## history

**Description.** Reads a document with its history and reports where
the division between them does not hold, proposing each move in full.
Fit when a document is cleaned, never at a save or a release.

**Reads.** One project, the path the task names (for the engine,
`projects/forge`), and in it every versioned document with its history
and its archive, or the one document the task names.

**Verifies.** The division between a document and its history, by
Versioning & status in `CLAUDE.md` and the definition of the intent
(`.claude/skills/forge/states/intent.md`, Threads and files). The way
to an item found in the document is a finding. The other way, an item
that can no longer be understood because what makes it hold stands
only in the history, is a finding. Each finding proposes the move in
full: the text that leaves, word for word, and the record it becomes.
The form of the log is the `light` check's.

**Cost.** Whole documents with their histories: minutes rather than
seconds.

## boundary

**Description.** Reads an intent with its solution design and reports
where the division between them does not hold, proposing each move in
full. Fit after a round on the intent or before a major, never at a
save or a release.

**Reads.** One project, the path the task names (for the engine,
`projects/forge`): its intent and its solution design whole, or the
positions the task names. Of the files a design item names under
`Where:` it reads only what a finding needs. A project without a
solution design is a fact, said in one line, and nothing more is
read.

**Verifies.** The division between the intent and the solution design,
by the intent's definition
(`.claude/skills/forge/states/intent.md`) and the design's
(`.claude/skills/forge/states/solution-design.md`).

- A sentence in the intent that belongs to the solution is a finding.
- A design item that carries what is wanted or why, where no position
  holds it, is a finding.
- A position that no longer says what is wanted because it stands only
  in the design is a finding.

Each finding proposes the move in full: the position's new wording,
the text that leaves word for word, where it goes, and the record the
intent's history receives (`templates/history.md`). The way to an
item, its dates, trials and measurements, is the `history` check's.

**Cost.** The intent and the design whole, and the files the findings
reach into: minutes rather than seconds.

## single-source-of-truth

**Description.** Verifies that every rule, procedure and file shape is
written in one place and cited everywhere else: no restatement across
`CLAUDE.md`, skills, agents, templates and scripts, and no direct
operation where a mechanism exists. The honest sweep; expensive by
design. Fit before a major or after a round on the operating layer,
not at every release.

**Reads.** The whole operating layer of the engine: `CLAUDE.md`, every
skill under `.claude/skills/` with its supporting files, every agent
under `.claude/agents/`, every template under `templates/` and the
help headers of `scripts/`. It always reads the whole, never a changed
subset, and is run on the principal's word. Given a project instead,
it reads that project's recipes, resource indexes, ledger comments and
its own `CLAUDE.md`, if any, against the owners in the engine.

**Verifies.**

- One owner per rule: every command, agent, contract and template
  describes only its own job. A procedure, rule set or file shape that
  another file owns is cited by path, never restated. A restatement is
  a finding, fixed by a reference to the owner and the deletion of the
  copy. Where a shape has no owner, the finding proposes one.
- Reviewer files carry only their own: every lens, persona and check
  file names its kind's contract skill and carries only its
  front-matter and its Lens section.
- No direct operation where a mechanism exists: no skill or agent does
  directly what a script, command or agent exists for (git outside the
  scripts, a conversion outside `doc2md.py`, a render outside
  `/render`, a review outside the reviewer agents, a check outside the
  check agents).

**Cost.** The whole layer, read and compared pairwise where the
subjects overlap. Long by design; the report's first line says how
many files were read.

## brd

**Description.** Verifies a BRD's mechanics: every parent item
carried, every cited ID existing, every item with a parent, the
phasing present, every term defined, no link in an item. Fit after a
pass of `/forge brd`.

**Reads.** One project's `30-brd.md`, the path the task names or the
project's BRD, with its parent as the BRD's header declares it:
`20-assignment.md` or `10-intent.md`. A BRD made from a source is a
work product in `work/`, read when the task names it, its parent the
source by path. A project without a BRD is not a finding. The
bookkeeping of the file is the `light` check's, the ID scheme in
general and the shape of the file against its template the `project`
check's.

**Verifies**, against `.claude/skills/forge/states/brd.md` and
`templates/brd.md`:

1. Traceability: every in-scope item of the parent is carried by at
   least one BR or UC, unless an OOS, a DEP or a TBC of the BRD names
   it. Every parent an item cites exists. The appendix table matches
   the items. Where the parent is a source, the path is verified and
   the place is read as a fact.
2. Every BR, NFR and UC has its parent, and where the parent is a
   source, the place it cites is a turn of the right party.
3. The sections that may not be silent: Phasing is present and not
   empty, and every BR and UC stands in a phase or in the `not phased`
   row. Every area of the roster the BRD cites is in the Touched areas
   table, and every role the roster names as signing or reviewing is
   in the Stakeholders table or named as absent with a reason. No ASM
   answers what a TBC of the same BRD asks. Every NFR category kept
   has its value or its TBC, and every TBC its owner and its blocking.
4. Terms and links: every capitalised term of an item is in the Terms
   table, no item depends on a link, and no name of a person stands
   where the template asks for a role.
5. Skeleton residue: no template comment but the line that names the
   template, no `…`, no `<placeholder>`, no `NNNN` left in the file.
   `owner: unassigned` is not residue.

**Cost.** The BRD and its parent, read once; the roster the BRD cites,
read for its list of areas only.

## user-stories

**Description.** Verifies the mechanics of user stories: every parent
item served or said not to be, every story with a Reference to an
existing item, the fixed parts in their order and none left empty,
questions with an owner, risks with a mitigation or consequences,
notes with a link and what lies behind it, no vague word in a
criterion. Fit after a pass of `/forge user-stories`.

**Reads.** One project's `35-user-stories.md`, the path the task names
or the project's stories, with its parent as the header declares it:
`30-brd.md` or `10-intent.md`. Stories made from a source are a work
product in `work/`, read when the task names them, their parent the
source by path. A project without stories is not a finding. The
bookkeeping of the file is the `light` check's, the ID scheme in
general and the shape of the file against its template the `project`
check's.

**Verifies**, against `.claude/skills/forge/states/user-stories.md`
and `templates/user-stories.md`:

1. Coverage: every in-scope item of the parent is cited in the
   Reference of at least one story. An item served by none is a
   finding unless the stories or the parent say why. Coverage is
   counted, never judged.
2. Reference: every story has a Reference, and every ID it cites
   exists in the parent (or, for a DEP, in the BRD). A story citing
   only a POS has a parent `10-intent.md`. Where the parent is a
   source, the path is verified and the place is read as a fact.
3. Parts and wording: every story has its parts, their order, their
   labels and their wording as the Story style has them. For a vague
   word or a conditional in a criterion it reports the word and the
   place, never a value. No two stories carry one ID.
4. Skeleton residue: no template comment but the line that names the
   template, no `…`, no `<placeholder>`, no `NNNN` left in the file.

**Cost.** The stories and their parent, read once.

## See also

- [Check conformance](../use/check-conformance.md): running a check.
- [Add a check](../extend/add-a-check.md): adding a check.
- [Glossary](glossary.md): every term of the forge in one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
