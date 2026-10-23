---
generated: 2026-10-23
version: 5.33
made: derived
inputs-hash: 426de847270d2191
inputs:
  - CLAUDE.md#Document chain
  - .claude/skills/document/SKILL.md
  - .claude/skills/docs-contract/SKILL.md
  - .claude/agents/docs-planner.md
  - .claude/agents/docs-writer.md
  - templates/docs-map.md
  - projects/forge/10-intent.md#POS.1450
  - projects/forge/10-intent.md#POS.0930
  - projects/forge/10-intent.md#REJ.0240
  - projects/forge/10-intent.md#REJ.0250
  - projects/forge/10-intent.md#REJ.0260
  - projects/forge/40-solution-design.md#SOL.0460
---

# The documentation

The documentation of a project is a set of pages of one topic each,
kept in the project's `docs/` directory, with an index that names
each reader's path through them. This page explains what the
documentation is, who it is written for, how one run makes it and
why it is generated rather than written by hand. It is for anyone
who uses the forge, extends it or only wants to understand it.

## What it is

The documentation is a set of pages in `docs/`, at the engine root
for the engine itself and in `projects/<slug>/docs/` for a project.
Each page has one topic. The index is `docs/README.md`, and it
lists every page and names a path through the pages for each reader.

The pages are written for three readers, in this order of weight:

1. **The user**: the one who clones the forge and forges his own
   thinking in it.
2. **The extender**: the one who adds an artefact, a lens, a
   persona, a genre, a check, a command or a script.
3. **The evaluator**: the one who never runs it and wants to
   understand what it is and how it works. He gets the concept pages
   and nothing made for him alone.

Each reader's path is a short run of pages in the order he reads
them.

The pages fall into five sections, ordered by the reader's journey.
The sections are the same for every project:

- `start/`: what the thing is, what must be on the machine, the
  first setup and the first result.
- `use/`: one page per job the thing has a command or a procedure
  for.
- `about/`: one page per concept and per kind of artefact or part,
  the reasons included.
- `extend/`: what it is made of, how a change is made, proved and
  recorded, and one page per kind of addition.
- `reference/`: the commands, the rosters, the conventions, the
  layout, the scripts, the templates and a glossary.

A section or a page with no material is left out, never left empty.
A project that is not installed has no install page, and that is no
gap.

Each page is of one kind, and the kind says what content belongs on
it:

- **How-to**: what the reader does, step by step where there are
  steps, and what he sees; never the reasons.
- **Explanation**: what a thing is, how it works and why it is so;
  never a procedure and never a listing.
- **Reference**: facts in the structure of what it mirrors, a table
  where the owner has a table; it never explains.

One rule of the forge has one home page: the page whose kind and
topic it is. Every other page that touches the rule says one
sentence about it and links to the home page. The same matter
written on two pages is a defect of the plan, not of the page.
Every page is reached from at least one other page, so the index is
not the only way in.

The folder `docs/videos/` of the engine lies under `docs/` but is
not part of the documentation. It is the public folder of the video
players, described on
[The screenplay and its player](the-screenplay-and-its-player.md).
The documentation run never plans it, indexes it or checks it.

## How it works

The documentation is generated and never composed or maintained by
hand. Each page either mirrors the files that own its topic or is
derived from named evidence in several files, and its front-matter
says which:

- **Mirrored**: the page restates what its inputs say, in the
  reader's words.
- **Derived**: the page puts together what no single file says, from
  evidence the plan names and by the reasoning the plan gives.

A page is never invented. What its inputs do not support is left
out and reported. Where a page would want a reason that no input
gives, it says that the reason is not recorded. Every such place is
listed for the principal (the person whose thinking is forged and
who decides its content). Where he wants a reason, it enters the
intent in its own round and reaches the page at the next run. An
example that shows the shape a template or a convention defines,
plainly generic and taken from no project, counts as a mirror of
that owner. A diagram drawn from what the owners say counts the same
way. The content of a real project never reaches a page.

### The documentation map

Every page is made from its entry in the documentation map, the file
`docs-map.md`. The map lies beside the ledger (the file of a
project's state, made at read time) of the project that owns the
documentation: `projects/forge/` for the engine, the project's own
directory for a project. It is never in `docs/` and never shown to
the reader. Its header carries only two fields:

- `target`: `engine` or the project's slug.
- `owner`: the path of the owning project.

After the header come the reader paths, then one section per section
of the outline, each with one entry per page. Each field of an entry
is set out on [Documentation map](../reference/documentation-map.md).
The map of the previous run is not named in the header. It is taken
from git at the start of the next run. The reason the header was
reduced to these two fields is not recorded.

### Two agents under one contract

Two agents make the documentation. Each runs as a subagent: a
separate instance of Claude that sees nothing of the working
conversation and reads its inputs from disk.

- **The planner** reads the target on disk and writes the map. It
  writes no page.
- **The writer** makes one page from its entry alone. One writer
  runs per page, and it sees no other page and no other entry.

Both share one contract, `.claude/skills/docs-contract/SKILL.md`.
The contract holds what the two agents have in common: their
isolation, the kinds of a page, what must never reach a page, and
the voice and the sentence of a page. The writer's own definition,
`.claude/agents/docs-writer.md`, holds the fixed shape of a page and
one outline per kind of page.

The planner runs on the session model, the model the principal has
chosen for the whole forge. A derived page is written on the session
model too. A mirrored page is written on a faster model. A mirrored
page leaves the model no room, so the faster model is enough there.
The choice is made by the entry's `made` field, never per run.

### Only what changed

A run regenerates only the pages whose inputs changed. The decision
is mechanical, never a judgement. An input is a file or a named part
of one, such as a section by its heading or an item by its ID. A
named part is hashed as that part alone. A change elsewhere in the
same file therefore leaves the page as it is. The rules a page is
made by (the writer's definition and the contract) are hashed with
the inputs. A change to either of them regenerates every page.

### One documentation run

One command makes the documentation: `/document [slug]`. Bare, it
documents the engine; with a slug, that project. The run asks no
question. How to run it is on
[Generate the documentation](../use/generate-the-documentation.md).
The run goes as follows:

```
 previous map, taken from git
            |
            v
 +---------------------+
 | planner (agent)     |  reads the target on disk
 | writes docs-map.md  |
 +---------------------+
            |
            v
 +---------------------+
 | docs-state.py       |  hashes each entry's inputs and the
 | new / regenerate /  |  rules; writes one task file per page
 | keep / remove       |  to make
 +---------------------+
            |
            v
   pages marked remove are deleted
            |
            v
 +---------------------+
 | writers (agents)    |  one per page, each from its task file
 | one page each       |  and its inputs only
 +---------------------+
            |
            v
 +---------------------+
 | docs-index.py       |  derives docs/README.md from the map
 +---------------------+
            |
            v
 +---------------------+
 | docs-check.py       |  broken links, long dashes in prose,
 +---------------------+  instance facts
            |
            v
   ledger remade; report to the principal
```

The index carries each reader's path as links, one line per page,
and the version of the owning project's intent. A page that fails
the check is regenerated once, with the failure named. A page that
fails twice is left out of the documentation and reported. It is
never mended by hand. What is wrong on a page is mended in the file
that owns the matter, as
[Change a documentation page](../extend/change-a-documentation-page.md)
describes, and the page is then regenerated.

The run takes place on `main` only. It refuses a repository that is
behind or diverged from its remote. At a merge the pages are taken
as they stand on the receiving side (`ours`).

A release never regenerates the documentation. It reports how old
the index is against the version of the intent and offers
`/document`. The regenerated pages then pass under the principal's
eyes, as every regenerated render does.

## Why

The README of the engine was once its whole documentation, and it
was poor as one, because it did three things at once. A page of one
topic can say one thing well, so that people can understand the
forge and use it in full. The README is now cut to what orients and
points, and the pages carry the rest.

The pages are generated so that a page cannot drift from what it
mirrors. A page that mirrors its owner changes when the owner
changes, and only then.

Each kind of page has a fixed outline, and the index one line per
page. The reason is that the writer's own judgement of headings and
of index lines did not converge.

The map lies beside the ledger and not in `docs/`, because a visitor
of the documentation would not understand it. The index is named
`README.md` rather than `index.md`, because GitHub shows a
directory's README as its front page.

Inputs are named by part because the body of a file changes at every
round. A page citing one position would otherwise be regenerated for
every other. The cost is that a moved heading or a renumbered ID
loses the part and regenerates the page, which is the safe side.

The rules a page is made by are hashed with its inputs so that the
state of a run stays computed, never judged. The cost is that a
change of the writer's definition or of the contract regenerates
every page.

Three alternatives were rejected:

- **A recipe per page, the pages as renders.** A recipe is a tool
  the principal shapes by hand, while a page is to come from the
  project's documents with no hand in between. One recipe per page
  would mean as many recipes to iterate by hand as there are pages.
  The map replaces the recipes, with one generated entry per page.
  A page is therefore not a render, as
  [Renders and recipes](renders-and-recipes.md) explains.
- **A site or a wiki.** GitHub shows Markdown pages and the README of
  a directory as they stand. Pages in the repository are readable
  without a build, a host or a second place to keep current. A site
  stays possible later over the same pages.
- **A hand-kept file of the philosophy in the project root.** The
  reasons already live in the brief and the intent. A hand-kept copy
  would drift from them. The `about/` pages are derived from those
  two instead.

## A worked example

One entry of a documentation map, generic and taken from no project,
in the shape the map's template defines:

```
### docs/about/<concept>.md
- title: <The concept, named in the reader's words>
- line: What is <the concept>, and why does it work this way?
- kind: explanation
- reader: user, evaluator
- says: <the page's one topic, in a few sentences a writer can
  work from>
- inputs:
  CLAUDE.md#<Section>
  projects/<slug>/10-intent.md#<ID>
- links:
  `docs/reference/glossary.md`: every term in one line.
- must-not: <what the page must not say of its topic>
- made: derived
- evidence: <what the page is put together from, and by what
  reasoning>
- state: new
```

The writer of this page reads only the named section of `CLAUDE.md`
and the named item of the intent. A change to another section of
`CLAUDE.md` leaves the page as it is. A change to that item marks
the page `regenerate` at the next run.

## See also

- [Generate the documentation](../use/generate-the-documentation.md):
  running `/document`.
- [Change a documentation page](../extend/change-a-documentation-page.md):
  changing a page through its owners.
- [Documentation map](../reference/documentation-map.md): the map's
  entry and the page's front-matter, field by field.
- [Renders and recipes](renders-and-recipes.md): the renders, which
  the pages are not.
- [The screenplay and its player](the-screenplay-and-its-player.md):
  the videos folder under `docs/` that the documentation leaves
  alone.
- [Glossary](../reference/glossary.md): every term of the forge in
  one line.

Generated on 2026-10-23 for version 5.33 from the files the
front-matter names; never edited by hand.
