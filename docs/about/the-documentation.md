---
generated: 2026-10-25
version: 6.1
made: derived
inputs-hash: d7413555594447fd
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
kept in the project's `docs/` folder, with an index that names each
reader's path through them. This page explains what the documentation
is, who it is written for, how it is made and why it is generated
rather than written by hand. It is for anyone who uses the forge,
extends it or wants to judge it. Terms of the forge are defined in one
line each in the [Glossary](../reference/glossary.md).

## What it is

The documentation is generated from the project's own documents. It is
never composed or kept up by hand. Its pages live in `docs/` at the
root of the engine or of a project. The index is `docs/README.md`.

It is written for three readers, in this order of weight:

1. The user, who clones the forge and forges his own thinking in it.
2. The extender, who adds an artefact, a lens, a persona, a genre, a
   check, a command or a script.
3. The evaluator, who never runs the forge and wants to understand
   what it is and how it works. He gets the concept pages and nothing
   made for him alone.

Each reader has a path of three to five pages in reading order, and
the index prints these paths as links.

The pages fall into five sections, ordered by the reader's journey.
Each section is a folder under `docs/`:

- `start/`: what the thing is, what must be on the machine, the first
  setup, the first result.
- `use/`: one page per job the thing has a command or a procedure for.
- `about/`: one page per concept and per kind of artefact or part,
  the reasons included.
- `extend/`: what it is made of, how a change is made, proved and
  recorded, and one page per kind of addition.
- `reference/`: the commands, the rosters, the conventions, the
  layout, the scripts, the templates and a glossary.

A section or a page with no material is left out, never left empty. A
project that is not installed has no install page, and that is no gap.

Each page has one topic and one kind. The kind says what content
belongs on the page and what does not:

- A how-to: what the person does, step by step, and what he sees;
  never the reasons.
- An explanation: what a thing is, how it works and why; never a
  procedure and never a listing.
- A reference: facts in the structure of what it mirrors, a table
  where the owner has a table; never an explanation.

One rule of the forge has one home page, the page whose kind and topic
it is. Every other page that touches the rule says one sentence about
it and links to the home page. The same matter written on two pages is
a defect of the plan. Every page is reached from at least one other
page, so that the index is not the only way in.

A page is either mirrored or derived. A mirrored page restates what
the files that own its topic say, in the reader's words. A derived
page puts together what no single file says, from evidence named in
several. A page is never invented. Where a page would want a reason
and the project's documents give none, the page says that the reason
is not recorded.

The documentation is not a render (an audience-specific output made
from a recipe). No recipe stands behind a page, as
[Renders and recipes](../about/renders-and-recipes.md) explains for
the renders.

The engine's `docs/videos/` folder is not part of the documentation.
It is the public folder of the videos, described in
[The screenplay and its player](../about/the-screenplay-and-its-player.md).
The documentation run never maps it, and its scripts read `docs/`
without it.

## How it works

One command makes the documentation: `/document [slug]`. Bare, it
documents the engine; with a slug, it documents that project. How to
run it is on [Generate the documentation](../use/generate-the-documentation.md).
The run asks nothing. It runs on `main` only and refuses a repository
that is behind its remote or has diverged from it.

The run rests on the documentation map. This is a file named
`docs-map.md` with one entry per page, holding everything a page is
made from. It lies beside the ledger of the owning project (the ledger
is the file that holds the project's state), never in `docs/`. The
reader of the documentation never sees it. Its header carries only
the target and the owning project. Its fields are listed one by one on
[Documentation map](../reference/documentation-map.md).

Two agents make the documentation. Both run as subagents: isolated
helpers of Claude that never see the working conversation and read
their inputs from disk. They share their conduct through one contract,
which also owns the voice of a page, the shape of its sentences and
what must never reach a page.

- The planner reads the target on disk and writes the map. It writes
  no page.
- A writer makes one page from its entry in the map and the files the
  entry names. It sees no other page. There is one writer per page.

A mirrored page is written on a faster model. A derived page is
written on the session model (the model the principal's working
conversation runs on), like the planner. The principal is the person
whose thinking is forged. The entry's `made` field decides the
model, never a judgement per run.

Three scripts do the rest:

- `scripts/docs-state.py` computes which pages are stale.
- `scripts/docs-index.py` derives the index from the map.
- `scripts/docs-check.py` scans the pages for broken links, long
  dashes in prose and instance facts before they are kept.

A run regenerates only the pages whose inputs changed. The decision is
mechanical. Each input of an entry is a file or a named part of one: a
section by its heading or an item by its ID. A named part is hashed as
that part, so a change elsewhere in the file leaves the page as it is.
The rule the pages are made by (the writer's definition and the
contract) is hashed with the inputs. A change to that rule therefore
regenerates every page. The previous map is taken from git at the
start of a run, to compare against.

One documentation run goes like this:

```
/document [slug]   (on main only)
   |
   v
previous map taken from git
   |
   v
planner: reads the target on disk, writes docs-map.md
   |
   v
docs-state.py: hashes the inputs and the rule, marks each page
   new / regenerate / keep / remove, writes one task per page to write
   |
   v
pages marked remove are deleted
   |
   v
one writer per task: reads its entry and inputs, writes one page
   |
   v
docs-index.py: derives docs/README.md from the map
   |
   v
docs-check.py: a page that fails is regenerated once;
   a page that fails twice is left out and reported
   |
   v
the ledger is remade; the report lists what the inputs did not
support and every place where a reason is not recorded
```

What is wrong on a page is mended in the file that owns the matter,
and the page is regenerated. How that is done is on
[Change a documentation page](../extend/change-a-documentation-page.md).

A release never regenerates the documentation. It reports how old the
index is against the version of the intent and offers `/document`.

## Why

The README was once the whole documentation of the engine. It was
poor as one, because it tried to be three things at once. A page of
one topic can say a thing well. The aim is that people understand the
forge and use it in full.

Other choices, each with its reason:

- Generated, never written by hand. Because a page mirrors the files
  that own its topic or is derived from named evidence, it cannot
  drift from what it mirrors.
- A command of its own, not a recipe per page. A recipe is a tool the
  principal shapes by hand, and many pages would mean many recipes to
  iterate. A page is to come from the project's documents with no hand
  in between. The map replaces the recipes, one generated entry per
  page.
- Pages in the repository, not a site or a wiki for now. GitHub shows
  Markdown pages and the README of a folder as they stand. The pages
  are therefore readable without a build, a host or a second place to
  keep current. A site stays possible later over the same pages.
- No hand-kept file of the philosophy in the project root. The why
  already lives in the brief and the intent, and a hand-kept copy
  would drift from them. The About pages are derived from those two.
- The index named `README.md`, not `index.md`. GitHub shows a folder's
  README as its front page.
- The map beside the ledger, not in `docs/`. A visitor of the
  documentation would not understand it.
- Inputs by a named part, not by the whole file. The body of a file
  changes at every round, and a page citing one item would otherwise
  be regenerated for every change to the others. The cost is that a
  moved heading or a renumbered item loses the part and regenerates
  the page, which is the safe side.
- The rule hashed with the inputs, not a switch that forces a run. The
  state stays computed, never judged.
- Only changed pages regenerated. A run stays cheap, and the names of
  the pages stay stable.
- A fixed outline per kind of page and a one-line field for the index.
  A review of earlier pages showed that the writer's own judgement of
  headings and index lines did not converge.
- A faster model for a mirrored page. A mirrored page leaves the model
  no room.
- `main` only. At a merge the pages are taken as one side's whole
  (`ours`), not merged line by line.
- No regeneration at a release. The regenerated pages pass under the
  principal's eyes, as every regenerated render does.

## A worked example

One entry of a documentation map, for a generic project with the slug
`my-project`. Paths are relative to the target's root.

```
### docs/use/export-a-report.md
- title: Export a report
- line: How do I export a report?
- kind: how-to
- reader: user
- says: The command `/export <name>` writes the named report to a
  file. What the person types and what he sees, step by step.
- inputs:
  guide.md#Export
- links:
  `docs/reference/glossary.md`: every term in one line.
- must-not: no value of an instance.
- made: mirrored
- state: new
```

The writer of this page reads only this entry and the section
`Export` of `guide.md`. A change elsewhere in `guide.md` leaves the
page as it is. A change to the section `Export` marks the page
`regenerate` at the next run.

## See also

- [Generate the documentation](../use/generate-the-documentation.md):
  running `/document`.
- [Change a documentation page](../extend/change-a-documentation-page.md):
  changing a page through its owners.
- [Documentation map](../reference/documentation-map.md): the map's
  entry and the page's front-matter, field by field.
- [Renders and recipes](../about/renders-and-recipes.md): the renders,
  which the pages are not.
- [The screenplay and its player](../about/the-screenplay-and-its-player.md):
  the videos folder under `docs/` that the documentation leaves alone.
- [Glossary](../reference/glossary.md): every term of the forge in one
  line.

Generated on 2026-10-25 for version 6.1 from the files the
front-matter names; never edited by hand.
