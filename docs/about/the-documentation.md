---
generated: 2026-11-08
version: 6.21
made: derived
inputs-hash: 7081ba26bd4cdf5f
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
  - projects/forge/10-intent.md#REJ.0240
  - projects/forge/10-intent.md#REJ.0250
  - projects/forge/10-intent.md#REJ.0260
  - projects/forge/10-intent.md#REJ.0500
  - projects/forge/40-solution-design.md#SOL.0460
  - projects/forge/40-solution-design.md#SOL.0700
---

# The documentation

The documentation of a project is a set of pages of one topic each,
kept in `docs/` with an index that lists every page and names each
reader's path through them. This page explains what the documentation
is, who it is written for, how it is made and why it is generated
rather than written by hand. It is for the user who reads the pages,
the extender who wants a page to change, and the evaluator who wants
to understand how a forge documents itself.

## What it is

The pages lie in `docs/` of the engine root or of the project. They
are kept with the project and readable where it is published and in a
clone. The index, `docs/README.md`, lists every page with one line and
prints each reader's path as links.

The documentation has three readers, in this order of weight:

- the user, who clones the forge and forges his own thinking in it;
- the extender, who adds an artefact, a lens, a persona, a genre, a
  check, a command or a script;
- the evaluator, who never runs it and wants to understand what it is
  and how it works.

The evaluator gets the concept pages and nothing made for him alone.
Why the readers stand in this order is not recorded.

The pages are cut into five sections by the reader's journey, each a
directory under `docs/`:

- `start/`: what the thing is, what must be on the machine, the first
  setup and the first result;
- `use/`: one page per job the thing has a command or a procedure for;
- `about/`: one page per concept and per kind of artefact or part, the
  reasons included;
- `extend/`: what it is made of, how a change is made, proved and
  recorded, and one page per kind of addition;
- `reference/`: the commands, the rosters, the conventions, the
  layout, the scripts, the templates and a glossary.

A section is filled only where the project has material. A section or
a page with no material is left out, never left empty. A project that
is not installed has no install page, and that is no gap.

Every page is of one kind, and the kind says what kind of content
belongs on the page and what does not:

- a how-to carries steps, commands and what the person sees, never
  the reasons;
- an explanation carries what a thing is, how it works and why, never
  a procedure and never a listing;
- a reference mirrors its owner, in the structure of what it mirrors,
  and never explains.

Each page opens with what it is for and for whom, and stands on its
own. One rule of the forge has one home page, the page whose kind and
topic it is. Every other page that touches the rule says one sentence
and links to the home page. The same matter written on two pages is a
defect of the plan, not of the writer. Every page is reached from
another page: the index is not the only way in.

The documentation is generated from the project's documents and never
composed or maintained by hand. A page either mirrors the files that
own its topic, restating them in the reader's words, or is derived
from named evidence in several files, by a reasoning its entry in the
map gives. The page says which of the two it is in its front-matter.
A page cannot drift from what it mirrors. A page is never invented:
what no file supports is left out and reported, never guessed.

A page is not a render. No recipe stands behind it, and the render
command is untouched by it; what a render is and how its recipe is
iterated is on [Renders and recipes](renders-and-recipes.md). The
README is a render and stays what orients and points.

The public folder of the videos, `docs/videos/` of the engine, is not
the documentation's. The planner never maps it, and the index, the
state and the check read `docs/` without it. What that folder is for
is on [The screenplay and its player](the-screenplay-and-its-player.md).

## How it works

One command makes the documentation, `/document [slug]`, in one run
that asks nothing. Bare, the target is the engine and the pages land
in `docs/` at the engine root. With a slug, the target is that project
and the pages land in `projects/<slug>/docs/`. How the command is run
and what it prints is on
[Generate the documentation](../use/generate-the-documentation.md).

### The map

The run is made from a map, `docs-map.md`, the documentation map. It
lies beside the ledger of the owning project (the ledger is the
project's state file, made at read time), never in `docs/`, and it is
never shown to the reader. The map holds one entry per page: the
page's title, one line for the index, its kind, its reader, what it
says, its exact inputs, the pages it links to, what it must not say,
whether it is mirrored or derived, and its state. Its header carries
only the target and the owner. The fields of an entry and of a page's
front-matter are on [Documentation map](../reference/documentation-map.md).

The previous map, which the planner reads so that the page names stay
stable, is taken from git. The header of the map carries no field
that changes with a run. Because of that, two runs on two clones never
conflict on the header, and the last committed map is the previous one.

### Two agents under one contract

Two agents make the documentation. Both are subagents: each runs in
isolation, sees nothing of the working conversation, and reads every
input from disk in its own run.

The planner reads the target on disk and writes the map. It writes no
page. For the engine it reads the core (`CLAUDE.md`), the skills, the
agents, the settings, the templates, the help header of every script,
and in the owning project the briefs, the intent, the threads, the
solution design, the decisions and the recipes. The recipes own the
pinned facts no other file carries, such as the install lines and the
repository's public address: those facts have one place in the
project that both the README and the documentation read. For a
project other than the engine the planner reads its briefs, intent and
threads, the layers below the intent, its ledger, the indexes of
`sources/` and `research/`, its recipes, and whatever those documents
point to on disk. What a project wants documented beyond that is not
a setting of its own. The planner never reads the instance file, the
local settings, any memory directory, the renders and the README of
the target, or the bodies of scripts below their help header.
Because the renders and the README are outputs, not owners, they
cannot be a page's source.

The writer makes one page. It is given one task file that holds its
entry from the map verbatim, the path to write, the date, the version
the page is made for and the hash the page is to carry. It reads
exactly the inputs the entry names, and sees no other page and no map
beyond its entry. The page has a fixed shape with one outline per
kind of page. A mirrored page is written on a faster model and a
derived page on the session model (the model the conversation runs
on). The choice is made mechanically by the page's entry, never per
run.

What the two agents share is one contract: their conduct and
isolation, the kinds of a page, the voice and the sentence of a page,
and what must never reach a page. No instance fact reaches a page. No
content of a real project reaches a page. A plainly generic example
of the shape a template or a convention defines, and a diagram drawn
from what the owners say, are mirrors of their owner and belong on a
concept page and on a how-to.

The pages are written in the project's language, as its artefacts
are. The README stays English. Which language each kind of document
carries is on [Languages](languages.md).

### What a run regenerates

A run regenerates only the pages whose inputs changed. The state of
every page is computed by a script from the content of the inputs,
never by judgement. An input is a file or a named part of a file: a
section by its heading, an item by its ID. A part is hashed as that
part, so that a change elsewhere in the file leaves the page as it is.
The rule the pages are made by, the writer's definition and the
contract, is hashed with the inputs, its whitespace normalised. A
change of that rule regenerates every page made by the old one. A
re-wrap of the rule regenerates nothing.

Each entry gets one of four states:

- `new`: no page exists at the path;
- `regenerate`: a page exists and its hash differs, an input or the
  entry having changed;
- `keep`: a page exists with the same hash;
- `remove`: the page lost its material, or no entry names it.

Every page carries the hash it was made from in its front-matter. A
run writes one task file per new or stale page and launches one
writer per task. An index script derives `docs/README.md` from the
map. A check script scans the pages for broken links, long dashes in
prose and instance facts before they are kept. A page that fails the
check is regenerated once with the failure named in its task. A page
that fails twice is reported and left out, never mended by hand.
After the run the owning project's ledger is remade. Its Renders
table carries the index with the map as its input, and nobody writes
a row.

### On `main` only

A run is made on `main` only. A repository behind or diverged from
its origin is refused and a pull is offered. The reason: the pages are
taken as `ours` at a merge, and that turns round in the rebase of a
save. A fresh page would silently lose to an older one.

### What a release does

A release never regenerates the documentation on its own judgement.
By hand, it reports the age of the index against the intent's version
and offers the command. With `--auto`, it asks once before anything
runs. The pages pass under the eyes of the principal (the person whose
thinking is forged) as every regenerated render does.

### A page is never mended by hand

A page is never mended by hand. Because the next run writes it again
from its owners, the mend would be gone. Only a mend in the file that
owns the matter survives, and the page takes it at the next run. How
a page is changed through its owners is on
[Change a documentation page](../extend/change-a-documentation-page.md).

### What a run cannot place

Some of what a run meets has no home on a page:

- a fact a page needs that no file owns;
- a matter the map and an owner disagree on;
- a reason a page wants that no file records.

Such a matter is a finding of the run. The run files it in `reviews/`
as a check's report, in the shape every check's report has, with the
reviewer named as the documentation run. The ledger reads it as any
check's report, and the findings are settled by walkthrough (the
method of working a list one item per message, each closed with a
verdict). A mend lands in the owner, never on a page. A run that
leaves nothing files nothing. Where a page wants a reason and none is
recorded, the page says so in those words, and the reason, where the
principal wants one, enters the intent in its own round and reaches
the page at the next run. What a check is and how its findings are
settled is on [The check](the-check.md).

### The index and the manual

Every page carries the one question it answers: the `line` of its
entry, printed in the index. The manual reads the index to answer a
need said in free words: it chooses the pages whose question meets
the need, reads them, and shows the way the forge has. How that is
asked is on
[Look up a command, or ask how to do something](../use/look-up-a-command.md).

### One documentation run

```
 the target on disk                       docs-map.md (beside the ledger)
 (the core, the skills, the agents,  -->  planner  -->  one entry per page,
  the templates, the scripts' headers,                  the reader paths
  the owning project's documents)                        |
                                                         v
                                          the state script: every input
                                          hashed as the named part, the
                                          generator hashed with it
                                          new | regenerate | keep | remove
                                          one task file per page to make
                                                         |
                                                         v
                                   writer   writer   writer   (one per page,
                                      |        |        |      from its entry
                                      v        v        v      and its inputs)
                                          docs/<section>/<page>.md
                                                         |
                                     the index script    |    the check script
                                              |          |          |
                                              v          v          v
                                      docs/README.md   ledger    reviews/
                                                       remade    (what the run
                                                                 could not place)
```

## Why

The README was the whole documentation of the engine and poor as one:
three things at once. A page of one topic can say a thing well. People
inside a company and outside it should understand the forge and use it
in full.

A command of its own, not the render command: a page has no recipe to
iterate, and the map is generated. A recipe per page was considered
and dropped. A documentation of many pages would mean as many recipes
to iterate by hand. A recipe is a tool the principal shapes, while a
page is to come from the project's documents with no hand in between.
The map replaces the recipes, one generated entry per page.

A site or a wiki was considered and dropped for now. GitHub shows
Markdown pages and the README of a directory as they stand, so pages
in the repository are readable without a build, a host or a second
place to keep current. A site stays possible later over the same
pages. For the same reason the index is named `README.md` and not
`index.md`: GitHub shows a directory's README as its front page.

A hand-kept file of the philosophy in the project root was considered
and dropped. The why lives in the brief and the intent already, and a
hand-kept copy would drift from them. The About pages are derived from
those two, and the pitch stays a render.

The map lies beside the ledger and not in `docs/`, because a visitor
of the documentation would not understand it.

A run regenerates only what changed, so that a run is cheap and the
page names stay stable. An input is named as a part of a file rather
than hashed as the file's body: the body changes at every round too,
and a page citing one item would still be regenerated for every
other. The cost is that a moved heading or a renumbered ID loses the
part and regenerates the page, which is the safe side. The generator
is hashed with the inputs rather than forced by a switch, so that the
state stays computed, never judged. The cost is that a change of the
writer's definition or of the contract regenerates every page.

The outlines per kind and the one-line field of the index stand in
place of the writer's judgement, because an audit showed that the
judgement does not converge: the headings of the how-to pages differed
from page to page, and the index entries ran long.

A mirrored page is written on a faster model because it leaves the
model no room. A trial showed the faster model sufficient on mirrored
pages and the session model more complete on derived ones. The whole
forge otherwise runs on one model, and the documentation writer is a
named exception to that.

The fields that change with a run left the header of the map because
they were the certain conflict at a merge. The run takes the previous
map from git instead.

What a run cannot place is filed as a check's report, since the
documentation finds what no other check does.

The videos folder under `docs/` is kept apart because the engine,
public on GitHub and served by GitHub Pages from `docs/`, is the one
public place of an instance. The folder carries a project's public
file only; its recipe, its render and its history stay in the
project. The documentation is generated and verified around the
folder, and the folder is left alone.

Why the run asks nothing is not recorded.

## A worked example

One entry of the map, as the planner writes it for a how-to page of a
project `<slug>`, plainly generic:

```
### docs/use/<job>.md
- title: <The job, as the heading will carry it>
- line: How do I <do the job>?
- kind: how-to
- reader: user
- says: The command as it is typed, with one example on a placeholder
  slug; what the person sees at each step; what he has afterwards.
  Nothing of why: that is the concept page's matter, linked.
- inputs:
  .claude/skills/<command>/SKILL.md
  templates/<skeleton>.md#<Section>
- links:
  `docs/about/<concept>.md`: what the thing is and why it is so.
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: no value of an instance; no content of a real project.
- made: mirrored
- state: keep
```

From this entry the state script hashes the skill file whole and the
one section of the skeleton, together with the entry's text and the
generator. The page at `docs/use/<job>.md` carries the hash it was
made from. If the hashes agree, the state stays `keep` and no writer
runs. If the skill file changed, the state becomes `regenerate`, one
task file is written, and one writer makes the page again from the
entry and the two inputs, on the faster model, since the page is
mirrored. A change in any other section of the skeleton leaves the
page as it is.

## See also

- [Generate the documentation](../use/generate-the-documentation.md): running `/document`.
- [Change a documentation page](../extend/change-a-documentation-page.md): changing a page through its owners.
- [Documentation map](../reference/documentation-map.md): the map's entry and the page's front-matter, field by field.
- [Renders and recipes](renders-and-recipes.md): the renders, which the pages are not.
- [The check](the-check.md): the check, whose report shape and settling the documentation run borrows.
- [The screenplay and its player](the-screenplay-and-its-player.md): the videos folder under `docs/` that the documentation leaves alone.
- [Languages](languages.md): which language each kind of document carries, the pages among them.
- [Look up a command, or ask how to do something](../use/look-up-a-command.md): the manual that reads the index to answer a question.
- [Glossary](../reference/glossary.md): every term of the forge in one line.

Generated on 2026-11-08 for version 6.21 from the files the front-matter names; never edited by hand.
