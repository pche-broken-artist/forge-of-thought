---
generated: 2026-11-17
version: 7.12
made: derived
inputs-hash: 7d48184ffd82c513
inputs:
  - CLAUDE.md#Document chain
  - .claude/skills/document/SKILL.md
  - .claude/skills/docs-contract/SKILL.md
  - .claude/agents/docs-planner.md
  - .claude/agents/docs-writer.md
  - templates/docs-map.md
  - .claude/skills/man/SKILL.md
  - scripts/docs-state.py
  - projects/forge/10-intent.md#POS.1450
  - projects/forge/10-intent.md#POS.0930
  - projects/forge/10-intent.md#POS.1540
  - projects/forge/10-intent.md#POS.1690
  - projects/forge/10-intent.md#POS.1710
  - projects/forge/10-intent.md#POS.1980
  - projects/forge/10-intent.md#REJ.0240
  - projects/forge/10-intent.md#REJ.0250
  - projects/forge/10-intent.md#REJ.0260
  - projects/forge/10-intent.md#REJ.0500
  - projects/forge/40-solution-design.md#SOL.0460
  - projects/forge/40-solution-design.md#SOL.0700
---

# The documentation

The documentation of a project is a set of pages of one topic each in
`docs/`, with an index that names each reader's path through them.
This page explains what the documentation is, who reads it, how one
run makes it and why it is generated rather than written. It is for
all three readers of the documentation: the user, the extender and
the evaluator.

## What it is

### Pages, an index and three readers

Every page has one topic. The pages are kept with the project. They
are readable where the project is published and in a clone. The index
(`docs/README.md`) lists every page with one line: the question the
page answers. It also names a path for each reader: a few pages in
the order he reads them.

The documentation has three readers, in this order of weight:

1. **The user** clones the thing and works with it. For the engine
   (what the forge runs on: its core, skills, agents, templates and
   scripts), he clones the forge and forges his own thinking in it.
2. **The extender** adds to it. For the engine, he adds an artefact,
   a lens, a persona, a genre, a check, a command or a script. Each
   of these terms has its line in the
   [Glossary](../reference/glossary.md).
3. **The evaluator** never runs it and wants to understand what it is
   and how it works. He gets the concept pages and nothing made for
   him alone.

The reason for this order is not recorded.

### Five sections

The pages lie in five sections by the reader's journey, the same for
every project. Each section is a directory under `docs/`:

- `start/`: how-to pages on what the thing is, what must be on the
  machine, the first setup and the first result.
- `use/`: one page per job the thing has a command or a procedure
  for.
- `about/`: one page per concept and per kind of artefact or part,
  the reasons included.
- `extend/`: what the thing is made of, how a change is made, proved
  and recorded, and one page per kind of addition.
- `reference/`: the commands, the rosters, the conventions, the
  layout, the scripts, the templates and a glossary. This section
  mirrors its owners and never explains.

A section or a page with no material is left out, never left empty. A
project that is not installed has no install page, and that is no
gap.

### One kind per page

Each page is of one kind. The kind says what content belongs on the
page and what does not:

- A **how-to** carries what the reader does, step by step where there
  are steps, and what he sees. It never carries the reasons.
- An **explanation** carries what a thing is, how it works and why it
  is so. It is never a procedure and never a listing.
- A **reference** states facts in the structure of what it mirrors: a
  table where its input is a table. It never explains.

Each page opens with what it is for and for whom, and it stands on
its own.

Two rules hold across the sections:

- One rule of the forge has one home page: the page whose kind and
  topic it is. Every other page that touches the rule says one
  sentence and links. The same matter written on two pages is a
  defect of the plan, not of the writer.
- Every page is reached from another page. The index is not the only
  way in: at least one other page links to it, at a place where a
  reader of that other page would ask for it.

### Generated, never written by hand

The documentation is generated from the project's documents. It is
never composed or maintained by hand. Each page is made from its
owners: the files in which its topic is stated. A page is made in one
of two ways, and its front-matter says which:

- A **mirrored** page restates what its owners say, in the reader's
  words.
- A **derived** page puts together what no single file says, from
  named evidence in several files.

A page is never invented. What the files do not support is left out
and reported, never guessed. An example that shows the shape a
template or a convention defines, plainly generic and taken from no
project, counts as a mirror of that owner. A diagram drawn from what
the owners say counts the same.

A page is not a render. A render is an output for one audience,
generated from a recipe: a versioned file that says how the render is
made. No recipe stands behind a page, and the command `/render` has
no part in the documentation. See
[Renders and recipes](renders-and-recipes.md).

### The documentation map

The pages are made from the documentation map (`docs-map.md`). It
holds one entry per page, with everything a writer needs to make that
page alone. Three things hold for it:

- It lies beside the ledger of the owning project, never in `docs/`.
  The ledger is the file of a project's state, which a script makes
  at read time. The owning project is the project that owns the
  documentation: for the engine the forge's own project
  (`projects/forge`), for a project the project itself.
- Its header carries only its target (`engine` or the slug of the
  project) and its owner (the owning project).
- It is never shown to the reader. The scripts and the writers read
  it.

The entry of the documentation map and the front-matter of a page are
described field by field in
[Documentation map](../reference/documentation-map.md).

### The language of the pages

The pages are written in the project's language, as its artefacts
(the documents of its chain) are. The project file sets that
language. The README stays English. See [Languages](languages.md).

### What lies under `docs/` and is not the documentation

The folder `docs/videos/` of the engine does not belong to the
documentation. It is the engine's one public folder. A project's
recipe may send an output there by its `output:` path. The engine
carries the file only: its recipe, its render, its provenance and its
history stay in the project that made it. The planner never maps the
folder. The scripts of the index, of the state and of the check read
`docs/` without it. The documentation is generated and verified
around the folder and leaves it alone. See
[The screenplay and its player](the-screenplay-and-its-player.md).

## How it works

### One command, one run

One command makes the documentation: `/document [slug]`. Bare, its
target is the engine: the owning project is `projects/forge` and the
pages land in `docs/` at the engine root. With a slug, its target is
that project, and the pages land in `projects/<slug>/docs/`. The run
asks nothing. The reason it asks nothing is not recorded. Claude
never runs the command on its own judgement. Running it is the topic
of [Generate the documentation](../use/generate-the-documentation.md).

One documentation run:

```text
   the target on disk  +  the previous documentation map, from git
                                |
                                v
                 +------------------------------+
                 | planner                      |
                 | plans every page             |
                 +------------------------------+
                                |
                                v
       docs-map.md: one entry per page, beside the ledger
                                |
                                v
                 +------------------------------+
                 | scripts/docs-state.py        |
                 | hashes each entry, its       |
                 | inputs and the rule the      |
                 | pages are made by            |
                 +------------------------------+
                    |           |            |
                  keep       remove    new, regenerate
                    |           |            |
                the page    the page   one task file
                stays       is deleted per page
                                             |
                                             v
                 +------------------------------+
                 | writers, one per page        |
                 | each reads its task and the  |
                 | inputs its entry names       |
                 +------------------------------+
                                |
                                v
                 +------------------------------+
                 | scripts/docs-index.py        |
                 | derives docs/README.md from  |
                 | the documentation map        |
                 +------------------------------+
                                |
                                v
                 +------------------------------+
                 | scripts/docs-check.py        |
                 | scans the pages before they  |
                 | are kept                     |
                 +------------------------------+
                                |
                                v
       the ledger made again; the run's report; what the run
       could not place, filed in reviews/
```

The index script derives the index from the documentation map: the
reader paths as links and one line per page, with the version of the
owning project's intent. The intent is the trunk of a project's chain
of documents, which starts at a brief. The check script scans the
pages for broken links, for long dashes in prose and for instance
facts, that is facts of one installation. A page that fails the scan
is made again once. A page that fails twice is left out of the
documentation and reported. At the end the ledger is made again, and
the run reports the pages new, regenerated, kept and removed.

### Two agents under one contract

Two agents make the documentation: a planner, and a writer per page.
Each runs as an isolated subagent: a run of Claude of its own that
sees nothing of the conversation and reads every input from disk.

- The planner reads the target on disk and writes the documentation
  map. It writes no page and changes no file of the target.
- A writer makes one page from its entry of the documentation map and
  from the inputs the entry names. The entry reaches it as a task
  file. It sees no other page. It keeps a fixed page shape with one
  outline per kind of page.

Both work under one contract
(`.claude/skills/docs-contract/SKILL.md`). The contract holds what
the two share:

- the isolation;
- the kinds of a page;
- what must never reach a page or the documentation map;
- the voice and the sentence of a page.

The planner and the writer of a derived page run on the session model
(the model the conversation with Claude runs on). The writer of a
mirrored page runs on a faster model. The reason: a smaller model
drifts where its task leaves it room, and a mirrored page leaves it
none. The choice is made mechanically by the page's entry, never per
run.

### What the planner reads

For the engine, the planner reads:

- `CLAUDE.md` (the core);
- every file under `.claude/reference/` (the reference files, which
  are read on demand);
- every file under `.claude/skills/` (the skills);
- every file under `.claude/agents/` (the agents);
- `.claude/settings.json` (the settings);
- every file under `templates/` (the templates);
- the help header of every script under `scripts/`;
- in the owning project: the briefs, the intent, the threads, the
  solution design, the decisions and the recipes. The recipes are
  among them for the pinned facts they own and no other file carries,
  such as the install lines.

The owning project of the engine is the forge's own project. The
engine's documentation is therefore made where that project is cloned
beside the engine. The paths `projects/forge/...` that the pages cite
are the paths of that clone. See
[Projects and the engine](projects-and-the-engine.md).

For a project, the planner reads:

- its briefs, its intent and its threads;
- the layers below the intent;
- its ledger;
- the indexes of `sources/` and `research/`;
- its recipes;
- whatever those documents point to on disk.

What a project wants documented beyond that is not a setting of its
own. The reason is not recorded.

The planner never reads the renders or the README of the target: they
are outputs, not owners. It never reads the files of an instance, and
no instance fact reaches a page.

### Which pages a run writes

A run regenerates only the pages whose inputs changed. The decision
is mechanical, made from the inputs and never by judgement. The
purpose: a run stays cheap and the page names stay stable.

For every entry the state script (`scripts/docs-state.py`) computes
one hash from three things:

- the text of the entry;
- the content of every input the entry names;
- the rule the pages are made by, that is the writer's definition and
  the contract.

An input is a whole file or a named part of a file: a section by its
heading, or an item by its ID. A part is hashed as that part. A
change elsewhere in the file therefore leaves the page as it is.

The rule is hashed with its whitespace normalised. A change of the
rule regenerates every page made by the old one. A re-wrap of the
rule regenerates nothing.

Every page carries in its front-matter the hash it was made from
(`inputs-hash`). The script compares the two hashes and sets the
state of the entry:

- `new`: no page lies at the path.
- `regenerate`: a page exists and its hash differs. An input or the
  entry changed.
- `keep`: a page exists with the same hash.
- `remove`: no entry names the page, or the planner marked its entry
  for removal.

A writer is launched for the pages that are `new` or `regenerate`,
and for no other.

### The previous documentation map

The planner is given the documentation map of the previous run where
one exists. With it the planner keeps every path that still has
material. The run takes that previous map from git, as it was last
committed. The header of the documentation map carries no field that
changes with a run, and so none that points to a previous map. The
recorded reason for such a header: a field that changes with every
run is a certain conflict.

### Only on `main`

A run is made on the branch `main` only. It refuses a repository that
is behind its origin or has diverged from it. The reason lies in how
git merges the pages. At a merge a page is taken as `ours`: git keeps
one's own version of the page and merges no two generated texts. In
the rebase that a save makes, that choice turns round. A save is the
command `/save`, which commits and pushes the work. A freshly made
file would then silently lose to an older one. Two branches that both
make the documentation also conflict on the server, and such a
conflict is settled by making the documentation again.

### What a release does

A release (the command `/release`) never regenerates the
documentation on its own judgement. Run by hand, it reports the age
of the index against the version of the intent and offers
`/document`. Run with `--auto`, it asks once before anything runs.
The pages pass under the eyes of the principal (the person whose
thinking is forged), as every regenerated render does.

### A page is never mended by hand

A page is never mended by hand. The next run writes the page again
from its owners, and the mend is gone. Only a mend in the file that
owns the matter survives, and the page takes it at the next run. See
[Change a documentation page](../extend/change-a-documentation-page.md).

### What a run cannot place

A run meets three kinds of matter it cannot place:

- a fact a page needs and no file owns;
- a matter on which the documentation map and an owner disagree;
- a reason a page wants and no file records.

Each is a finding of the run. The run files its findings in
`reviews/` as a report of its own, in the shape of a check's report.
They are settled as a check's findings are: in a walkthrough, where
the principal decides them one by one. A mend lands in the owner,
never on a page. The reason for the report: the documentation finds
what no other check does. The report and its settling are explained
in [The check](the-check.md).

Nothing is invented to fill a gap. A fact without an owner waits for
the principal to give it a home. A page that wants a reason no file
records says that the reason is not recorded. Where the principal
wants the reason on the page, it enters the intent in a round of its
own and reaches the page at the next run.

### The index and the manual

The index has a second reader: the manual (`/man`). Every page
carries the one question it answers, and the index prints it. Asked a
need in free words, the manual reads the index and chooses the pages
whose question meets the need. See
[Look up a command, or ask how to do something](../use/look-up-a-command.md).

## Why

**Why pages of one topic.** The README was the whole documentation of
the engine and poor as one: it was three things at once. A page of
one topic can say a thing well. People inside the company and outside
it should understand the forge and use it in full. The README is cut
to what orients and points.

**Why generated.** A page that is generated from its owners cannot
drift from what it mirrors.

**What is rejected.** Three other directions are rejected:

- *A recipe per page, with the documentation as renders of
  `/render`.* A recipe for every page would be that many recipes to
  iterate by hand. A recipe is a tool the principal shapes. A page is
  to come from the project's documents with no hand in between. The
  documentation map replaces the recipes: one generated entry per
  page.
- *A site or a wiki for the documentation, for now.* The code host
  shows Markdown pages and the README of a directory as they stand.
  Pages in the repository are therefore readable without a build, a
  host or a second place to keep current. A site stays possible later
  over the same pages.
- *A hand-kept file of the philosophy in the project root.* The why
  lives in the brief and the intent already, and a hand-kept copy
  would drift from them. The pages of `about/` are derived from those
  two. The pitch stays a render.

**The choices of the build.** Each was made against an alternative:

- The index is named `README.md`, not `index.md`. The code host shows
  the README of a directory as its front page.
- The documentation map lies beside the ledger, not in `docs/`. A
  visitor of the documentation would not understand it.
- An input is hashed by its named part. The alternative was to hash a
  file's body without its front-matter. The body changes at every
  round of work too, and a page that cites one item would still be
  regenerated for every other. The cost: a moved heading or a
  renumbered ID loses the part and regenerates the page, which is the
  safe side.
- The rule the pages are made by is hashed with the inputs. The
  alternative was a switch that forces a run. With the hash the state
  stays computed, never judged. The cost: a change of the writer's
  definition or of the contract regenerates every page.
- Each kind of page has a fixed outline, and each entry has one line
  for the index. The alternative was to trust the writer's judgement,
  and that judgement does not converge.

## A worked example: one entry of the documentation map

The entry below is invented and belongs to no project. It shows the
shape the template `templates/docs-map.md` defines, for a project
with the placeholder slug `<slug>`. The paths of its inputs are
relative to the project's directory.

```text
### docs/about/the-weekly-report.md
- title: The weekly report
- line: What is the weekly report, and why has it three parts?
- kind: explanation
- reader: user, evaluator
- says: The weekly report is one page in three parts. What each part
  holds and why it is there. One worked example: an invented report.
- inputs:
  10-intent.md#The weekly report
  sources/00-INDEX.md
- links:
  `docs/reference/glossary.md`: every term of the project in one line.
- must-not: no name of a team; no figure of a real report.
- made: derived
- evidence: the section of the intent gives the three parts and the
  reason for each; the index of the sources names the form the report
  follows; the page puts the two together.
- state: new
```

What a run does with this entry:

- **The first run.** No page lies at `docs/about/the-weekly-report.md`,
  and the state is `new`. The state script writes one task file: the
  entry word for word, the path of the page, the date, the version
  the page is made for, the hash the page is to carry and the titles
  of the pages it links to. A writer reads the task, then the section
  "The weekly report" of the intent and the index of the sources, and
  nothing else. The entry says `derived`, and the writer runs on the
  session model. The page it writes carries `made: derived` and the
  hash in its front-matter.
- **A later run, after another section of `10-intent.md` changed.**
  The entry names one section of that file, and the section is hashed
  as that part. The hash is the same, the state is `keep`, and the
  page is not touched.
- **A later run, after the section "The weekly report" changed.** The
  hash differs, the state is `regenerate`, and a writer makes the
  page again.
- **A run after the project dropped the weekly report.** The planner
  finds no material for the page and marks the entry `remove`. The
  page is deleted.
- **A reason is missing.** Suppose the intent gives no reason for the
  third part. The page says that the reason is not recorded, the
  writer reports the place, and the run files it as a finding.

The page is reached from another page: at least one other entry of
the same documentation map names `docs/about/the-weekly-report.md`
under its `links`. Its `line` is what the index prints, and what the
manual reads to find the page.

## See also

- [Generate the documentation](../use/generate-the-documentation.md):
  running `/document`.
- [Change a documentation page](../extend/change-a-documentation-page.md):
  changing a page through its owners.
- [Documentation map](../reference/documentation-map.md): the map's
  entry and the page's front-matter, field by field.
- [Renders and recipes](renders-and-recipes.md): the renders, which
  the pages are not.
- [The check](the-check.md): the check, whose report shape and
  settling the documentation run borrows.
- [The screenplay and its player](the-screenplay-and-its-player.md):
  the videos folder under `docs/` that the documentation leaves
  alone.
- [Projects and the engine](projects-and-the-engine.md): the forge's
  own project, cloned beside the engine by whoever develops it.
- [Languages](languages.md): which language each kind of document
  carries, the pages among them.
- [Look up a command, or ask how to do something](../use/look-up-a-command.md):
  the manual that reads the index to answer a question.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-11-17 for version 7.12 from the files the front-matter names; never edited by hand.
