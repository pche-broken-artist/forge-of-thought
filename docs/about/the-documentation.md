---
generated: 2026-10-14
version: 5.9
made: derived
inputs-hash: d78bc121da60ed55
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
  - projects/forge/40-solution-design.md#SOL.0460
---

# The documentation

The documentation of a project is a set of pages of one topic each,
kept in the project's `docs/` directory with an index, generated from
the project's own documents and never composed by hand. This page
says what the documentation is, who it is for, how one run makes it
and why it is made this way. It is for the user who reads it, the
extender who wants a page changed, and the evaluator who wants to
understand how a forge documents itself.

## What it is

The documentation is kept with the project. It is readable where the
project is published and in a clone. Its index lists every page and
names each reader's path through them.

### Three readers

The pages are written for three readers, in this order of weight:

1. The user, who clones the forge and forges his own thinking in it.
2. The extender, who adds an artefact, a lens, a persona, a genre, a
   check, a command or a script.
3. The evaluator, who never runs it and wants to understand what it
   is and how it works. He gets the concept pages and nothing made
   for him alone.

Each reader gets a path: three to five pages in the order he reads
them. The index prints the paths as links. The reason for this order
of weight is not recorded.

### Five sections

The pages are arranged in five sections by the reader's journey, each
a directory under `docs/`, the same for every project:

- `start/`: how-to pages for the user. What the thing is, what must
  be on the machine, the first setup, the first result.
- `use/`: how-to pages for the user. One page per job the thing has a
  command or a procedure for.
- `about/`: explanation pages for all three readers. One page per
  concept and per kind of artefact or part, the reasons included.
- `extend/`: how-to pages, with the explanation they need, for the
  extender. What the thing is made of, how a change is made, proved
  and recorded, and one page per kind of addition.
- `reference/`: fact for all three readers. The commands, the
  rosters, the conventions, the layout, the scripts, the templates,
  a glossary. A reference page mirrors its owners and never explains.

A section or a page with no material is left out, never left empty.
A project that is not installed has no install page, and that is no
gap.

### One kind per page

Each page is of one kind: how-to, explanation or reference. The kind
says what kind of content belongs on the page and what does not:

- A how-to carries steps, commands and what the person sees, never
  the reasons.
- An explanation carries what a thing is, how it works and why, never
  a procedure and never a listing.
- A reference mirrors its owner and never explains.

Every page opens with what it is for and for whom, and stands on its
own: a reader who lands on it first understands it without another
page.

### One home page per rule

One rule of the forge has one home page: the page whose kind and
topic it is. Every other page that touches the rule says one
sentence and links to the home page. The same matter written on two
pages is a defect of the plan, not of the writer.

Every page is reached from another page. The index is not the only
way in: at least one other page links to each page, where a reader
of that page would ask for it. A page no other page would name is a
page the documentation does not need.

### Mirrored or derived

A page either mirrors the files that own its topic or is derived from
named evidence, and says which in its front-matter. A mirrored page
restates what its inputs say, in the reader's words. A derived page
puts together what no single file says, from evidence in several:
an install procedure from what the scripts require and the skills
install, a glossary from the terms the files use. A page cannot drift
from what it mirrors.

Nothing on a page is invented. What the inputs do not support is
left out and reported, never guessed. An example that shows the
shape a template or a convention defines, plainly generic and taken
from no project, is a mirror of that owner and is welcome on a
concept page and on a how-to. A diagram drawn from what the owners
say is the same. The content of a real project never reaches a page,
and no fact of an instance (one installation of the forge) reaches
one either.

A reason the inputs do not give is not written on the page. The page
says that the reason is not recorded, and the run lists every such
place for the principal (the person whose thinking is being forged).
Where he wants the reason on the page, it enters the intent in its
own round and reaches the page at the next run.

### What it is not

A page is not a render. No recipe stands behind it, and the render
command is untouched by it; what a render is and how a recipe is
iterated is said in [Renders and recipes](renders-and-recipes.md).
In the table of document kinds a page has the kind `page`: generated,
never a source of truth, overwritten by the documentation run. The
map it is made from has the kind `map`: generated, freely rewritten
by the documentation run.

The README is not the documentation. It is cut to what orients and
points, and its chapters are owned by the readme skeleton. Facts no
file of the project owns, such as the install commands, the
prerequisites and the public address of the repository, have one
place in the project that both the README and the documentation
read: the section "Pinned facts (not rendered)" of the project's
readme recipe.

The public folder of the videos, `docs/videos/` of the engine, is not
the documentation's. The documentation run never maps it and its
scripts read `docs/` without it; what the folder is and what it
holds is said in
[The screenplay and its player](the-screenplay-and-its-player.md).

## How it works

### The map

The documentation is made from a map, the documentation map, one
file `docs-map.md` of the kind `map`. It lies beside the ledger of
the owning project (the ledger is the project's single source of
truth for state), never in `docs/`. For the engine the owning project
is `projects/forge` and the pages land in `docs/` at the engine root.
For any other project the owning project is the project itself and
the pages land in `projects/<slug>/docs/`.

The map is read by the scripts and by the writers, never shown to the
reader of the documentation. It holds a Paths section with three to
five pages per reader in reading order, then one entry per page
under the page's path. An entry carries everything a writer needs to
make that page alone: its title, one line for the index, its kind,
its reader, what the page says, its exact inputs, the pages it links
to with a title and a sentence each, what it must not say, whether it
is mirrored or derived with the evidence for a derived page, and its
state. The fields are given one by one in
[Documentation map](../reference/documentation-map.md).

An input is a file or a named part of a file, written after `#`: a
section by its heading, which runs to the next heading of the same
or a higher level, or an item by its ID, which runs to the next
item. A part is named wherever only the part matters. A file is
named whole only where the whole is the matter. A glob cannot be
named.

### One run

One command makes the documentation, `/document [slug]`, in one run
that asks nothing; how to run it is said in
[Generate the documentation](../use/generate-the-documentation.md).
Claude never runs it on its own judgement. Two agents and three
scripts take part, each an isolated subagent or a script that sees
nothing of the working conversation.

```
 the owning project's documents          the engine's rules
 (briefs, intent, threads, layers,       (CLAUDE.md, skills, agents,
  decisions, ledger, recipes)             templates, script headers)
                 \                              /
                  v                            v
   [1] plan      the planner reads the target on disk
                 and writes the map: docs-map.md, beside the ledger
                              |
   [2] state     docs-state.py hashes each entry's inputs and the
                 generator; reads docs/ as it stands (videos left out)
                 -> new / regenerate / keep / remove, one task per
                    page to make
                              |
   [3] remove    the pages marked remove are deleted
                              |
   [4] write     one writer per task, in parallel, each reading its
                 task file and its inputs from disk
                 -> docs/<section>/<page>.md
                              |
   [5] index     docs-index.py derives docs/README.md from the map
                              |
   [6] check     docs-check.py scans the pages; a page that fails is
                 regenerated once with the failure named in its task
                              |
   [7] record    the ledger's Renders table gets the index's row;
                 the report lists what was made and what is unowned
```

The steps in words:

1. The planner reads the target on disk and writes the map. It
   writes no page and changes no file of the target. With a previous
   map it keeps every path that still has material and marks what
   lost its material for removal.
2. A script computes the state of every page from the content of its
   inputs. Each input is hashed as the named part. The rule the pages
   are made by, that is the writer's definition and the contract, is
   hashed with the inputs. A page whose hash has not changed is kept;
   a page whose hash has changed is regenerated; a page without a
   previous entry is new. The state is the script's, never a
   judgement.
3. The pages marked for removal are deleted.
4. One writer is launched per page to make. Its prompt names a task
   file and nothing else. The task file holds the page's entry from
   the map, the path to write, the date, the version the page is made
   for and the hash of its inputs. The writer reads the task first,
   then exactly the inputs the entry names, from disk, and writes the
   page in the fixed page shape with the outline of its kind. It sees
   no other page and no map beyond its entry. A mirrored page is
   written on a faster model; a derived page, like the planner, on
   the session model (the model the working conversation runs on).
   The choice is made by the entry, never per run.
5. A script derives the index, `docs/README.md`, from the map: the
   reader paths as links and one line per page, with the version of
   the owning project's intent.
6. A script scans the pages for broken links, long dashes in prose
   and instance facts. A page that fails is regenerated once with the
   failure named in its task. A page that fails twice is reported and
   left out of the documentation, never mended by hand.
7. The ledger's Renders table of the owning project gets the index's
   row, with the map as its input. The run reports the pages new,
   regenerated, kept and removed; the facts no file owns; what the
   writers left out; every place where a writer wanted a reason and
   none is recorded; and the check's result.

A run never reads the renders or the README as owners of a topic.
They are outputs, not owners.

### The two agents and their contract

The planner owns the readers, the outline, what it reads and the
map. The writer owns the page and its shape: one fixed page shape,
with one outline per kind of page (a how-to, an add page, an artefact
page, a concept page, a roster page). What the two share is one
contract: their isolation, the reading of every input from disk, what
must never reach a page or the map, and the voice and the sentence
of a page. The contract holds one voice across all pages, one rule
per sentence, no image in place of a mechanism, and a literal copied
as its owner has it. It keeps off a page the content of a real
project, an unrecorded reason, a date of history and any sentence of
the generator about itself.

### What is wrong on a page

A page is never edited by hand. What is wrong on a page is mended in
the file that owns the matter, and the page is regenerated at the
next run; the way is said in
[Change a documentation page](../extend/change-a-documentation-page.md).

### What a release does

A release never regenerates the documentation. It reports the age of
the index against the intent's version and offers the command.

## Why

The README was the whole documentation of the engine and poor as one,
three things at once. A page of one topic can say a thing well. The
people who run the forge and the people outside should understand it
and use it in full.

The documentation is generated and never kept by hand so that a page
cannot drift from what it mirrors. The reasons live in the brief and
the intent already, and a hand-kept copy would drift from them; so a
hand-kept file of the philosophy in the project root was rejected.
The About pages are derived from those two, and the pitch stays a
render.

A recipe per page, with the documentation as renders, was rejected.
A documentation of many pages would mean as many recipes to iterate
by hand. A recipe is a tool the principal shapes, while a page is to
come from the project's documents with no hand in between. The map
replaces the recipes, one generated entry per page. For the same
reason the documentation has a command of its own: a page has no
recipe to iterate, and the map is generated.

A site or a wiki was rejected for now. GitHub shows Markdown pages
and the README of a directory as it stands, so pages in the
repository are readable without a build, a host or a second place to
keep current. A site stays possible later over the same pages. The
index is named `README.md` rather than `index.md` because GitHub
shows a directory's README as its front page.

The map lies beside the ledger rather than in `docs/` because a
visitor of the documentation would not understand it.

A run regenerates only the pages whose inputs changed, decided
mechanically from the inputs and never by judgement, so that a run
is cheap and the page names stay stable. An input is hashed as the
named part so that a change elsewhere in the file leaves the page as
it is. Hashing the body of a file without its front-matter was
rejected: the body changes at every round too, and a page citing one
position would still be regenerated for every other. The cost of the
named part is that a moved heading or a renumbered ID loses the part
and regenerates the page, which is the safe side. The generator is
hashed with the inputs rather than forced by a switch so that the
state stays computed, never judged. The cost is that a change of the
writer's definition or of the contract regenerates every page.

The writer follows one outline per kind and the index takes one line
per page because trusting the writer's judgement did not converge: a
documentation audit showed the headings of the how-to pages and the
length of the index lines varying from page to page.

A mirrored page is written on a faster model because it leaves the
model no room. A derived page is written on the session model, as
the planner is, since the whole forge otherwise runs on one model
and speed is bought with context, never with a weaker model where
judgement is needed. The choice stands in the entry so that it is
made mechanically, never per run.

The pinned facts stand in the readme recipe rather than in a file of
their own because a file would need a kind of its own, and the
recipe is read by both the README and the planner. The cost is that
a render's tool carries facts of the project.

A release reports the age of the index and offers the command rather
than regenerating the documentation, so that the pages pass under the
principal's eyes as every regenerated render does.

The reason why the public folder of the videos under `docs/` is left
alone by the documentation is not recorded among the inputs of this
page. The reason why the run asks no question is not recorded
either.

## A worked example: one entry of the map

The entry below is generic, for a page of an invented project
`<slug>`. It shows the shape of an entry, not an entry of any real
map. The writer that makes this page sees this entry, the inputs it
names and nothing else of the map.

```
### docs/about/the-weekly-review.md
- title: The weekly review
- line: What is the weekly review, who runs it, and why every week?
- kind: explanation
- reader: user, evaluator
- says: The weekly review is a meeting of one hour at which the
  open threads of the project are read in order of weight. Who
  attends, what is read, and what leaves the meeting as a decision.
  Why weekly and not on demand, from the intent.
- inputs:
  10-intent.md#<ID of the position on the review>
  20-assignment.md#Cadence
  recipes/readme.md#Pinned facts (not rendered)
- links:
  `docs/use/run-the-weekly-review.md`: running one review, step
  by step.
  `docs/reference/glossary.md`: every term of the project in one
  line.
- must-not: no name of an attendee; no date of a past review.
- made: derived
- evidence: the position gives what the review is and why it is
  weekly; the assignment's Cadence section the hour and the order;
  the pinned facts the room. Where no input gives a reason, the
  page says the reason is not recorded.
- state: keep
```

The page made from this entry opens with what the weekly review is,
carries the headings of a concept page, links only to the two pages
under `links`, cites each by the title the map gives it, and closes
with the fixed line every page ends with. Its front-matter names the
version it was made for, whether it is mirrored or derived, the hash
of its inputs and the inputs themselves, so that the next run can
tell whether it is still current.

## See also

- [Generate the documentation](../use/generate-the-documentation.md): running `/document`.
- [Change a documentation page](../extend/change-a-documentation-page.md): changing a page through its owners.
- [Documentation map](../reference/documentation-map.md): the map's entry and the page's front-matter, field by field.
- [Renders and recipes](renders-and-recipes.md): the renders, which the pages are not.
- [The screenplay and its player](the-screenplay-and-its-player.md): the videos folder under `docs/` that the documentation leaves alone.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-10-14 for version 5.9 from the files the front-matter names; never edited by hand.
