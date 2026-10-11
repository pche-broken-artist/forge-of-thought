---
generated: 2026-10-11
version: 5.3
made: derived
inputs-hash: d760d0670f10623d
inputs:
  - CLAUDE.md#Document kinds
  - CLAUDE.md#Document chain
  - .claude/skills/document/SKILL.md
  - .claude/skills/docs-contract/SKILL.md
  - .claude/agents/docs-planner.md
  - .claude/agents/docs-writer.md
  - projects/forge/10-intent.md#POS.1450
  - projects/forge/10-intent.md#POS.0930
  - projects/forge/10-intent.md#REJ.0240
  - projects/forge/10-intent.md#REJ.0250
  - projects/forge/10-intent.md#REJ.0260
  - projects/forge/40-solution-design.md#Rendering and publishing
---

# The documentation

The documentation of a project is a set of pages of one topic each,
kept in `docs/` with the project, with an index that lists every
page and names a reading path for each kind of reader. This page
says what the documentation is, who it is written for, how it is
generated from the project's own files and why it is generated
rather than written by hand. It is for the user who reads the
documentation, for the extender who wants a page to change, and for
the evaluator who wants to understand the mechanism. The page in
front of the reader is itself one of these pages.

## What it is

Every project can carry a documentation. The engine's own
documentation is the documentation of the forge's own project,
`projects/forge`, and lands in `docs/` at the engine root. The
documentation of any other project lands in `projects/<slug>/docs/`.
The pages are Markdown files in the repository. They are readable
where the project is published and in a clone, with no build and no
host between. An index, `docs/README.md`, lists every page with one
line and prints each reader's path as links.

### The readers

Three readers, in this order of weight:

1. the user, who clones the forge and forges his own thinking in it;
2. the extender, who adds an artefact, a critic lens, a challenger
   persona, a recipe genre, a check, a command or a script;
3. the evaluator, who never runs it and wants to understand what it
   is and how it works. He gets the concept pages and nothing made
   for him alone.

Each reader gets a path: a short list of pages in the order he reads
them, printed in the index as links. The reason for the order of the
three readers is not recorded. The reason the evaluator gets no page
of his own is not recorded.

### The sections

Five sections by the reader's journey, each a directory under
`docs/`, the same for every project:

- `start/`: how-to pages for the user. What the thing is, what must
  be on the machine, the first setup, the first result.
- `use/`: how-to pages for the user. One page per job the thing has
  a command or a procedure for.
- `about/`: explanation pages for all three readers. One page per
  concept and per kind of artefact or part, the reasons included.
- `extend/`: how-to pages with the explanation they need, for the
  extender. What it is made of; how a change is made, proved and
  recorded; one page per kind of addition.
- `reference/`: pages of fact for all three readers. The commands,
  the rosters, the conventions, the layout, the scripts, the
  templates, the configuration, a glossary.

A section or a page with no material is left out, never left empty.
A project that is not installed has no install page, and that is no
gap.

### The pages

Each page is of one kind: how-to, explanation or reference. The kind
says what kind of content belongs on the page and what does not:

- a how-to carries steps, commands and what the person sees, never
  the reasons;
- an explanation carries what a thing is, how it works and why,
  never a procedure and never a listing;
- a reference mirrors its owner, never explains.

Every page opens with what it is for and for whom. Every page stands
on its own: a reader who lands on it first understands it without
another page. One rule of the forge has one home page, the page
whose kind and topic it is. Every other page that touches the rule
says one sentence and links to the home page. The same matter
written on two pages is a defect of the plan, not of the writer.
Every page is reached from at least one other page, chosen where a
reader of that page would ask for it; the index is not the only way
in. A page no other page would name is a page the documentation does
not need.

Each page is either mirrored or derived, and its front-matter says
which. A mirrored page restates what the files that own its topic
say, in the reader's words. A derived page puts together what no
single file says, from named evidence in several files: an install
procedure from what the scripts require and the skills install, or a
glossary from the terms the files use. Nothing on a page is
invented. What no file supports is left out and reported, never
guessed. An example that shows the shape a template or a convention
defines, plainly generic and taken from no project, counts as a
mirror of that owner. A diagram drawn from what the owners say
counts the same. The content of a real project never reaches a page.
No fact of the instance (that is, of one installation: a name, a
host, an account) reaches a page either. A reason the inputs do not
give is not written on the page: the page says that the reason is
not recorded.

The pages speak in one voice. Claude is "it". The reader of a how-to
is "you". The principal, that is the person whose thinking is
forged, is named by his role. The full rule of the voice and of the
sentence is held in the contract of the documentation agents,
`.claude/skills/docs-contract/SKILL.md`.

### Two kinds of document

The documentation is made of two kinds of document. The map, kind
`map`, is the file `docs-map.md`. It lies beside the ledger of the
owning project (the ledger is the single source of truth for a
project's state) and never in `docs/`. It carries one entry per
page with everything the page is made from. It is read by the
scripts and by the writers, never shown to the reader, and freely
rewritten by every run. The pages and the index, kind `page`, are
what the reader reads: generated, never a source of truth, and
overwritten by the documentation run. What the map's entry and the
page's front-matter hold, field by field, is on the page
[Documentation map](../reference/documentation-map.md).

A page is not a render. No recipe stands behind it, and `/render` is
untouched by the documentation; what a render is and how it differs
is on the page [Renders and recipes](renders-and-recipes.md).

## How it works

One command makes the documentation, `/document [slug]`, in one run
that asks nothing; how to run it is on the page
[Generate the documentation](../use/generate-the-documentation.md).
Bare, the target is the engine. With a slug, the target is that
project. The run is two agents and three scripts. The agents are
subagents (an agent Claude launches in isolation, which sees nothing
of the working conversation). The scripts are Python, run as
`python scripts/<name>.py`, and share one reader of the map,
`scripts/docs_map.py`.

```
  the files that own the target
  (CLAUDE.md, the skills, the agents, the templates, the help
  headers of the scripts; in the owning project the briefs, the
  intent, its threads, the solution design, the decisions, the
  recipes)
                      |
                      v
  [1] planner  (docs-planner, one subagent)
      reads the target on disk, writes the map
                      |
                      v
            docs-map.md   (beside the owning project's ledger)
                      |
                      v
  [2] state script  (scripts/docs-state.py)
      hashes each entry's inputs and the generator, compares
      with each page's front-matter
      -> new / regenerate / keep / remove, one task file per
         page to make
                      |
          +-----------+-----------+
          v           v           v
  [3] writer      writer      writer   (docs-writer, one
      page A      page B      page C    subagent per page)
      each reads its task file, then its inputs, from disk
          |           |           |
          +-----------+-----------+
                      v
            docs/<section>/<page>.md
                      |
                      v
  [4] index script  (scripts/docs-index.py)
      derives docs/README.md from the map
                      |
                      v
  [5] check script  (scripts/docs-check.py)
      broken links, long dashes in prose, instance facts
      -> a page that fails is regenerated once
                      |
                      v
      the ledger's Renders table: the index, made from the map
      the report to the principal
```

### The planner

The planner reads the target on disk and writes the map. For the
engine it reads `CLAUDE.md`, every file under `.claude/skills/` and
`.claude/agents/`, the settings, every template, the help header of
every script, and in the owning project the briefs, the intent, its
threads, the solution design, the decisions and the recipes. For a
project it reads the briefs, the intent, the threads, the layers
below the intent, the ledger, the indexes of `sources/` and
`research/`, the recipes, and whatever those documents point to on
disk. It never reads the renders or the README of the target,
because they are outputs and not owners. It never reads the instance
file or the body of a script below its help header.

The map it writes has a section of reader paths, then one entry per
page under the page's path. An entry carries the title, one line for
the index, the kind, the reader, what the page says, its exact
inputs, the pages it links to with the one sentence the writer will
know of each, what the page must not say, whether the page is
mirrored or derived with the evidence of a derived page, and a
state. An input is a file or a named part of a file: a section by
its heading, an item by its ID, a block by its bold label. With a
map of the previous run, the planner keeps every path that still has
material, so that the page names stay stable. The planner writes no
page. What it reads that no file supports goes into an Unowned list
of the map; what contradicts itself or the outline goes into a list
of what did not fit.

### The state script

The state script hashes the content of each entry's inputs, a part
hashed as that part, and hashes the generator with them: the
writer's definition and the contract. It compares the result with
the `inputs-hash` each page carries in its front-matter and sets the
state of every page: new, regenerate, keep or remove. For every page
to make it writes one task file. The state is computed, never a
judgement. A page marked `remove` is deleted.

### The writers

One writer makes one page. It reads its task file first, then
exactly the inputs its entry names, from disk, in this run. It sees
no other page, nothing of the map beyond its entry and nothing of
the working conversation. It writes the page in one fixed shape: a
front-matter with the date, the version the page was made for,
mirrored or derived, the `inputs-hash` and the inputs; the title;
one opening paragraph; the matter in the outline of the page's kind;
a See also list; and a fixed closing line. One outline exists per
kind of page: a how-to, an add page, an artefact page, a concept
page, a roster page, any other reference page. A mirrored page is
written on a faster model and a derived page on the session model
(the session is one working conversation of Claude; its model is
the one chosen for the instance). The choice is made by the entry's
`made` field, mechanically, never per run. Every writer reports what
its inputs did not support and it left out, and every place where a
reason was wanted and none is recorded.

Both agents share one contract, `.claude/skills/docs-contract/SKILL.md`,
in the same way the reviewers share theirs. The contract holds what
is common to the planner and the writer: that each sees nothing of
the conversation, reads every input from disk, asks no question and
decides aloud where something is unclear; what never reaches a page
or the map; the voice and the sentence of a page. What each agent
owns beyond it is its own file.

### The index and the check

The index script derives `docs/README.md` from the map: the reader
paths as links, one line per page, with the version of the owning
project's intent. The index is not planned as a page.

The check script scans the pages for broken links, long dashes in
prose and instance facts before they are kept. A page that fails is
regenerated once, with the failure named in its task. A page that
fails twice is reported and left out of the documentation, never
mended by hand.

### After a run

The ledger's Renders table of the owning project gets the index's
row, with the map as its input. Claude reports which pages are new,
regenerated, kept and removed; the Unowned list and what did not fit,
from the planner; what the writers left out; every place where a
writer wanted a reason and none is recorded, as one list; and the
check's result. Every fact in Unowned waits for the principal to give
it a home. A reason, where the principal wants one, enters the intent
in its own round and reaches the page at the next run.

What is wrong on a page is never mended on the page. It is mended in
the file that owns the matter, and the page is regenerated; how is on
the page
[Change a documentation page](../extend/change-a-documentation-page.md).

Facts no file of the chain owns, such as the install commands, the
prerequisites and the public address of the repository, have one
place in the project that both the README and the documentation
read: the section "Pinned facts (not rendered)" of the project's
readme recipe.

A release never regenerates the documentation. It reports the age of
the index against the version of the intent and offers `/document`.
The pages pass under the principal's eyes as every regenerated
render does.

## Why

The documentation is generated because the README was the whole
documentation of the engine, and poor as one: three things at once.
A page of one topic can say a thing well. People inside the
organisation that runs the forge and outside it should understand it
and use it in full. A page that mirrors the files that own its topic
cannot drift from them, because it is remade from them.

A recipe per page, with the documentation as renders of `/render`,
was rejected. Many pages would mean as many recipes to iterate by
hand. A recipe is a tool the principal shapes, while a page is to
come from the project's documents with no hand in between. The map
replaces the recipes: one generated entry per page. This is why the
documentation has a command of its own.

A site or a wiki was rejected for now. The repository host (GitHub)
shows Markdown pages and the README of a directory as they stand, so
pages in the repository are readable without a build, a host or a
second place to keep current. A site stays possible later over the
same pages. The index is named `README.md` and not `index.md` for
the same reason: the host shows a directory's README as its front
page.

A hand-kept file of the philosophy in the project root was rejected.
The why lives in the brief and the intent already, and a hand-kept
copy would drift from them. The About pages are derived from those
two; the pitch stays a render.

The map lies beside the ledger and not in `docs/`, because a visitor
of the documentation would not understand it.

A run regenerates only the pages whose inputs changed, decided
mechanically, so that a run is cheap and the page names stay stable.
An input is hashed as the named part of a file and not as the file's
body without its front-matter, because the body of the intent changes
at every round too, and a page citing one position would still be
regenerated for every other. The cost is that a moved heading or a
renumbered ID loses the part and regenerates the page: the safe side.

The generator, that is the writer's definition and the contract, is
hashed with the inputs rather than given a switch that forces a run,
so that the state stays computed and never judged. The cost is that a
change of the writer's definition or of the contract regenerates
every page.

The page has one fixed outline per kind and the index one line per
page, rather than trusting the writer's judgement, because left to
judgement the headings of the pages and the length of the index
entries do not converge.

A mirrored page is written on a faster model because it leaves the
model no room; a derived page, like the planner, runs on the session
model. Elsewhere the forge buys speed with context and never with a
weaker model, and this is the one case where a routine job is
mechanical enough.

The writers read every input from disk and see nothing of the
conversation, so that the session carries no page's material and a
page is made from the file as it is, not from an older copy.

The pinned facts stand in the readme recipe and not in a file of
their own, because a file would need a kind of its own, and the
recipe is read by both the README and the planner. The cost is that
a render's tool carries facts of the project.

## A worked example

One entry of the map, generic, for a made-up thought project
`<slug>`, in the shape the map's template gives. Nothing in it is
taken from a real project.

```
### docs/about/what-is-wanted.md
- title: What is wanted
- line: What does the project want, and what has it ruled out?
- kind: explanation
- reader: user, evaluator
- says: The aim of the project in plain words, the positions it holds and the directions it dropped, each with the reason the intent records; nothing of how it is realised.
- inputs:
  00-brief.md
  10-intent.md#Objective
  10-intent.md#Rejected directions
- links:
  `docs/about/how-it-is-realised.md`: the layer below the intent, where what is wanted is realised.
  `docs/reference/glossary.md`: every term of the project in one line.
- must-not: no ID of the chain; no name of a person; nothing of the threads still open.
- made: mirrored
- state: new
```

The writer of this page reads `00-brief.md` whole and two named
parts of `10-intent.md`, and nothing else. The state script hashes
exactly those three parts, with the generator; a change anywhere
else in `10-intent.md` leaves the page as it is. The two links are
the only links the page may carry, and the sentence beside each is
all the writer knows of the page it points to. The page the writer
makes opens with a front-matter of this shape:

```
---
generated: <date>
version: <the version of the project's intent>
made: mirrored
inputs-hash: <the hash of the three inputs and the generator>
inputs:
  - 00-brief.md
  - 10-intent.md#Objective
  - 10-intent.md#Rejected directions
---
```

The index then lists the page with its one line, and the path of the
evaluator may name it among the pages he reads in order.

## See also

- [Generate the documentation](../use/generate-the-documentation.md): running `/document`.
- [Change a documentation page](../extend/change-a-documentation-page.md): changing a page through its owners.
- [Documentation map](../reference/documentation-map.md): the map's entry and the page's front-matter, field by field.
- [Renders and recipes](renders-and-recipes.md): the renders, which the pages are not.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-11 for version 5.3 from the files the front-matter names; never edited by hand.
