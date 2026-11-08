---
generated: 2026-11-08
version: 7.0
made: derived
inputs-hash: f58136419fd60d06
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

The documentation of a project is a set of pages in `docs/`, each
page on one topic, with an index that lists every page and names
each reader's path through them. This page explains what the
documentation is, who it is for, how one run makes it, and why it is
generated from the project's files rather than written by hand. It
is for the user who reads the pages, for the extender who wants a
page to say something else, and for the evaluator who wants to know
how a documentation nobody writes stays true to what it describes.

## What it is

The documentation is kept with the project. It is readable where the
project is published and in a clone. Its pages lie in `docs/` at the
root of the project they document; for the engine of the forge that
is `docs/` at the engine root. Its index is `docs/README.md`.

### The readers

Three readers, in this order of weight:

1. The user, who clones the forge and forges his own thinking in it.
2. The extender, who adds an artefact, a lens, a persona, a genre, a
   check, a command or a script.
3. The evaluator, who never runs it and wants to understand what it
   is and how it works. He gets the concept pages and nothing made
   for him alone.

The reason for this order is not recorded. Each reader gets a path:
a few pages of the documentation in the order he reads them, printed
as links at the head of the index.

### The sections

Five sections by the reader's journey, each a directory under
`docs/`, the same for every project:

- `start/`: how-to pages for the user. What the thing is, what must
  be on the machine, the first setup, the first result.
- `use/`: how-to pages for the user. One page per job the thing has
  a command or a procedure for.
- `about/`: explanation for all three readers. One page per concept
  and per kind of artefact or part, the reasons included.
- `extend/`: how-to pages with the explanation they need, for the
  extender. What the thing is made of, how a change is made, proved
  and recorded, one page per kind of addition.
- `reference/`: derived fact for all. The commands, the rosters, the
  conventions, the layout, the scripts, the templates, a glossary.
  It mirrors its owners and never explains.

A section or a page with no material is left out, never left empty.
A project that is not installed has no install page, and that is no
gap.

### The kinds of a page

Each page has one topic and one kind. The kind says what kind of
content belongs on the page and what does not:

- a how-to carries steps, commands and what the person sees, never
  the reasons;
- an explanation carries what a thing is, how it works and why,
  never a procedure and never a listing;
- a reference states facts in the structure of what it mirrors,
  free of interpretation, and never explains.

Every page opens with what it is for and for whom, and stands on its
own. A reader who lands on it first understands it without another
page.

### One home page, every page reached

One rule of the forge has one home page: the page whose kind and
topic it is. Every other page that touches the rule says one
sentence and links to the home page. The same matter written on two
pages is a defect of the plan, not of the writer. Every page is
reached from another page: for every page at least one other page
names it under its links, chosen where a reader of that page would
ask for it. A page no other page would name is a page the
documentation does not need.

### Generated, never composed

The documentation is generated from the project's documents and
never composed or maintained by hand. A page either mirrors the files
that own its topic or is derived from named evidence in several
files, and its front-matter says which (`made: mirrored` or `made:
derived`). A mirrored page restates what its inputs say, in the
reader's words. A derived page puts together what no single file
says, by the reasoning its entry in the documentation map gives. A
page is never invented: what the inputs do not support is left out
and reported, never guessed. So a page cannot drift from what it
mirrors.

The documentation map is the plan the pages are made from: one entry
per page with everything a writer needs to make that page alone. It
is the file `docs-map.md` beside the owning project's ledger (the
ledger is the project's state file, made at read time). The map is
never in `docs/` and never shown to the reader. Its header carries
only its target (the engine, or the project's slug) and its owner.
The fields of an entry and of a page's front-matter are given field
by field in [Documentation map](../reference/documentation-map.md).

### What the documentation is not

A page is not a render: no recipe stands behind it, and `/render`
is untouched. What renders are is said in
[Renders and recipes](renders-and-recipes.md). The README of the
project is not a page either: it is a render, cut to what orients
and points, and it stays English, a translation being a render. The
folder `docs/videos/` of the engine is not the documentation's. It
is the public folder of the videos a project sends out, and the
planner, the index, the state and the check read `docs/` without it.
What it is for is said in
[The screenplay and its player](the-screenplay-and-its-player.md).

## How it works

### One run

One command makes the documentation, `/document [slug]`. Bare, the
target is the engine and the pages land in `docs/` at the engine
root. With a slug, the target is that project and the pages land in
`projects/<slug>/docs/`. The run asks nothing; the reason it asks
nothing is not recorded. How the command is used is said in
[Generate the documentation](../use/generate-the-documentation.md).
A run looks like this:

```
  /document [slug]            on main only, the repository up to
        |                     date with its origin
        v
+------------------------+    the previous map, taken from git
|  the planner           | <--------------------------------------
|  reads the target      |
|  writes the map        | ---> docs-map.md   (beside the ledger)
+------------------------+
        |
        v
+------------------------+    hashes each entry's inputs, a part
|  docs-state (script)   |    as that part, and the generator;
|                        |    sets new | regenerate | keep | remove;
|                        |    writes one task per page to make
+------------------------+
        |
        v
+------------------------+    one writer per page, each reading
|  the writers           |    its entry and its inputs from disk
|  one page each         | ---> docs/<section>/<page>.md
+------------------------+
        |
        v
+------------------------+
|  docs-index (script)   | ---> docs/README.md
|  docs-check (script)   |      a page that fails is made once more
+------------------------+
        |
        v
  the ledger remade; what the run could not place is filed in
  reviews/ as a check's report
```

### The agents and what they share

Two agents make the documentation, each a subagent: an isolated run
of Claude that sees nothing of the working conversation and reads
every input from disk in its own run. The planner reads the target
and writes the documentation map; it writes no page. The writer
makes one page from its entry in the map and the inputs the entry
names; it sees no other page and no map beyond its entry. The two
share one contract, as the reviewers of the forge do. The contract
owns their conduct and isolation, the kinds of a page, what must
never reach a page or the map, the one voice of the pages and the
shape of a sentence. What the pages say in that voice: Claude is
"it", the reader of a how-to is "you", and the principal (the person
whose thinking is forged) is named by role.

The planner runs on the session model, the model the working
conversation runs on. A writer runs on a faster model for a mirrored
page and on the session model for a derived page. The choice is made
by the entry's `made` field, mechanically, never per run.

### What the planner reads

For the engine, the planner reads the core file `CLAUDE.md`; every
file under `.claude/skills/`, the commands, the definitions of the
artefacts, the genre files, the contracts and the walkthrough skill
among them; every file under `.claude/agents/`; the settings file
`.claude/settings.json`; every file under `templates/`; the help
header of every script under `scripts/`; and, in the owning project,
the briefs, the intent, the threads, the solution design, the
decisions and the recipes. The recipes own pinned facts no other file
carries, such as the install lines and the public address of the
repository. The index of the project's research is read for
orientation only.

The owning project of the engine's documentation is the forge's own
project, `projects/forge`, a repository of its own cloned beside the
engine by whoever develops it. Because the planner reads that
project, the engine's documentation is made where the project is
cloned beside the engine, and the paths `projects/forge/...` the
pages cite are the paths of that clone. What the forge's own project
is, is said in [Projects and the engine](projects-and-the-engine.md).

For a project, the planner reads its briefs, its intent, its
threads, the layers below the intent, its ledger, the indexes of
`sources/` and `research/`, its recipes, and whatever those documents
point to on disk. What a project wants documented beyond that is not
a setting of its own.

Never read: the instance file `CLAUDE.local.md`, the local settings,
any memory directory, the renders and the README of the target, and
the bodies of the scripts below their help header. The renders and
the README are outputs, not owners.

### The previous map

The planner receives the map of the previous run, where one exists.
That map is taken from git, as last committed, since the map's
header carries no field that changes with a run. With it the planner
receives the open findings of the last documentation report that
concern the map. So the planner brings those entries to their
owners' wording instead of carrying the fault over. With a previous
map every page that still has material keeps its path. Without one
every page is new.

### What is regenerated

A run regenerates only the pages whose inputs changed. The state of
every page is computed by the script `scripts/docs-state.py`, never
judged. For every entry the script hashes the entry's text together
with the content of every input the entry names. An input is a file
or a named part of one: a section by its heading, or an item by its
ID, hashed as that part. So a change elsewhere in the file leaves
the page as it is. The generator is hashed with the inputs, that is
the writer's definition and the contract, with their whitespace
normalised. So a change of the rule a page is made by regenerates
every page made by the old rule, and a re-wrap of the rule
regenerates nothing. The page that exists at the entry's path
carries the hash it was made from in its front-matter,
`inputs-hash`. The two are compared:

- `new`: no page at the path;
- `regenerate`: a page exists and its hash differs, because an input
  or the entry changed;
- `keep`: a page exists with the same hash;
- `remove`: a page under `docs/` that no entry names, or the page of
  an entry the planner marked for removal.

For every new or regenerated entry the script writes one task file:
the page's path, the date, the version the page is made for (the
version of the owning project's intent), the hash the page is to
carry, the entry verbatim and the titles of the pages it links to.
That task is a writer's whole prompt. An input the map names and the
disk does not have is hashed as missing; the page is regenerated and
its writer reports the gap.

### Index and check

The script `scripts/docs-index.py` derives the index `docs/README.md`
from the map: the reader paths as links, one line per page (the
question the page answers), and the version of the owning project's
intent. The script `scripts/docs-check.py` scans the pages for
broken links, long dashes in prose and instance facts before they
are kept. A page that fails is regenerated once with the failure
named in its task. A page that fails twice is reported and left out
of the documentation, never mended by hand. The owning project's
ledger is then remade; its Renders table carries the index with the
map as its input, and nobody writes a row.

### What the run cannot place

What a run cannot place is a finding of the run: a fact a page needs
and no file owns, a matter the map and an owner disagree on, a claim
the map asked for and no input carried, a reason a page wants and no
file records. The command files these as the run's own report in
`reviews/`, in the shape a check's report has, one finding per
matter with a finding number of the owning project. The ledger reads
it as any check's report, and the findings are settled by
walkthrough: the one-item-at-a-time conversation in which the
principal gives a verdict on each. A mend lands in the owner, never
on a page. A run that leaves nothing files nothing. Nothing is
invented to fill a gap: a fact without an owner waits for the
principal to give it a home. What a check is and how its findings are
settled is said in [The check](the-check.md).

### Mending a page

A page is never mended by hand. The mend goes into the file that
owns the matter, and the page takes it at the next run. How to find
that file and change it is said in
[Change a documentation page](../extend/change-a-documentation-page.md).
A reason a page wants and no file records is not written on the
page: the page says that the reason is not recorded, the writer
reports the place, and the run lists every such place for the
principal. Where he wants the reason, it enters the intent in its
own round and reaches the page at the next run.

### A release and the documentation

A release never regenerates the documentation on its own judgement.
By hand it reports the age of the index against the intent's version
and offers `/document`. With `--auto` it asks once before anything
runs. So the pages pass under the principal's eyes as every
regenerated render does.

### The index as the manual's source

The index is also what the manual `/man` reads to answer a need said
in free words, since every page carries the one question it answers.
How to ask is said in
[Look up a command, or ask how to do something](../use/look-up-a-command.md).

### The language of the pages

The pages are written in the project's language, as its artefacts
are; the README stays English. Which language each kind of document
carries is said in [Languages](languages.md).

## Why

**Why generated at all.** The README was the whole documentation of
the engine and poor as one, three things at once. A page of one
topic can say a thing well. People inside the company and outside it
should understand the forge and use it in full.

**Why not a recipe per page, the pages as renders.** A documentation
of many pages would mean as many recipes to iterate by hand. A
recipe is a tool the principal shapes, while a page is to come from
the project's documents with no hand in between. The documentation
map replaces the recipes, one generated entry per page. The same
choice gives the documentation a command of its own: a page has no
recipe to iterate, and the map is generated.

**Why not a site or a wiki.** GitHub shows Markdown pages and the
README of a directory as they stand, so pages in the repository are
readable without a build, a host or a second place to keep current. A
site stays possible later over the same pages. For the same reason
the index is named `README.md` and not `index.md`: GitHub shows a
directory's README as its front page.

**Why not a hand-kept file of the philosophy.** The why lives in the
brief and the intent already, and a hand-kept copy would drift from
them. The About pages are derived from those two; the pitch stays a
render.

**Why a page is never mended by hand.** The next run writes it again
from its owners, and the mend is gone. Only a mend in the file that
owns the matter survives.

**Why the map lies beside the ledger and not in `docs/`.** A visitor
of the documentation would not understand it.

**Why an input is a named part of a file.** The alternative, hashing
a file's body without its front-matter, was rejected because the
body changes at every round too, and a page citing one position
would still be regenerated for every other. The cost is that a moved
heading or a renumbered ID loses the part and regenerates the page,
which is the safe side.

**Why the generator is hashed with the inputs.** The alternative was
a switch that forces a run. With the hash the state stays computed,
never judged. The cost is that a change of the writer's definition
or of the contract regenerates every page. The whitespace is
normalised so that a re-wrap regenerates nothing.

**Why one outline per kind and one line per page in the index.** An
audit of the documentation showed that headings and index lines left
to the writer's judgement did not converge: the how-to pages carried
many different headings, and the index lines ran long. So the
outlines are fixed per kind and the index takes one line.

**Why two models.** A mirrored page leaves the model no room, so a
mirrored page is written on a faster model. A trial showed the
session model more complete on derived pages and the faster model
sufficient on mirrored ones.

**Why the run is on `main` only, and refuses a repository behind or
diverged.** The pages are taken as `ours` at a merge, like every
file a release makes. That attribute turns round in the rebase a
save makes when the histories diverged: a fresh page would silently
lose to an older one. So everything that makes such files is made
only on `main`, on a repository up to date with its origin.

**Why the previous map comes from git.** The fields that changed
with each run left the map's header, because such fields are a
certain conflict when two people work on one project. With no
`previous` field in the header, the run takes the previous map as
last committed.

**Why the videos folder is kept apart.** The engine is the one
public place of an instance, served by GitHub Pages from `docs/`,
and a project may send a video's file there while the project
itself stays private. The engine carries the file only; its recipe,
its render and its history stay in the project. The folder is
therefore foreign to the documentation run and its checks, which
generate and verify the documentation around it.

**Why what the run cannot place is a check's report.** The
documentation finds what no other check does, and a check's report
already has a shape, a place in `reviews/`, a reading by the ledger
and a way of being settled.

**Why the manual reads the index.** The forge explains itself
through one door; a second name for a question would be one more
thing to learn. The index carries the one question every page
answers, so a need in free words finds its page there.

## A worked example

One entry of a documentation map, generic and taken from no project.
A planner would write it under the `about` section of the map; a
writer would receive it verbatim in its task and read the two inputs
named, and nothing else of those files:

```
### docs/about/the-weekly-review.md
- title: The weekly review
- line: What is the weekly review, and why does the project hold one?
- kind: explanation
- reader: user, evaluator
- says: The weekly review is the one meeting in which the open
  matters of the intent are read and a verdict is given on each.
  Who sits in it, what is read before it, what leaves it. The
  reason from the intent's objective.
- inputs:
  10-intent.md#Objective
  00-brief.md
- links:
  `docs/use/run-the-weekly-review.md`: running the review, step by
  step.
  `docs/reference/glossary.md`: every term of the project in one
  line.
- must-not: no name of a participant; no date of a past review.
- made: mirrored
- state: new
```

The entry's `inputs` name a section of the intent by its heading and
the brief whole. The state script hashes the section as that
section, so a change in another section of the intent leaves the
page as it is. The page made from this entry would carry `made:
mirrored` and the hash of these two inputs and the entry in its
front-matter, open with what the weekly review is and for whom, and
close with the two links under "See also".

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

Generated on 2026-11-08 for version 7.0 from the files the front-matter names; never edited by hand.
