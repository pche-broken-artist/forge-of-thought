---
generated: 2026-11-01
version: 6.8
made: derived
inputs-hash: d2c295b451a2779e
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
  - projects/forge/40-solution-design.md#SOL.0460
  - projects/forge/40-solution-design.md#SOL.0700
---

# The documentation

The documentation of a project is a set of pages of one topic each, kept in the project's `docs/` folder, with an index that names a path through the pages for each kind of reader. It is for the user, the extender and the evaluator, and this page explains what it is made of, how it is made and why it is generated rather than written. A term used here is glossed where it first appears. The principal is the person whose thinking is being forged.

## What it is

The documentation has three readers, in this order of weight:

1. The user, who clones the forge and works with it.
2. The extender, who adds to it.
3. The evaluator, who never runs it and wants to understand what it is and how it works. The evaluator gets the concept pages and nothing made for him alone.

The pages are cut into five sections by the reader's journey. A section or a page with no material is left out, never left empty.

- `start/`: what the thing is, what must be on the machine, the first setup and the first result.
- `use/`: one page per job that has a command or a procedure.
- `about/`: one page per concept and per kind of artefact or part, with the reasons.
- `extend/`: what the thing is made of, how a change is made, proved and recorded, and one page per kind of addition.
- `reference/`: the commands, the rosters, the conventions, the layout, the scripts, the templates and a glossary.

Each page is of one kind, and the kind says what content belongs on it:

- A how-to carries steps, commands and what the person sees. It never carries the reasons.
- An explanation carries what a thing is, how it works and why. It never carries a procedure and never a listing.
- A reference states facts in the structure of what it mirrors. It never explains.

Three rules bind the pages together:

- One rule has one home page, the page whose kind and topic it is. Every other page that touches the rule says one sentence and links.
- Every page opens with what it is for and for whom, and stands on its own.
- Every page is reached from another page. The index is not the only way in.

The index is the file `docs/README.md`. It lists every page with the one question the page answers and prints each reader's path. The manual command `/man` reads the same index to answer a need said in free words, which is why every page carries its one question. How to ask is on [Look up a command, or ask how to do something](../use/look-up-a-command.md).

The folder `docs/videos/` is not part of the documentation. It holds the public video files and the player page, and the planner, the index, the state script and the check all leave it alone. What it is: [The screenplay and its player](the-screenplay-and-its-player.md).

## How it works

The documentation is generated and never composed by hand. A page does one of two things: it mirrors the files that own its topic, or it is derived from evidence named in its entry, and it says which. A derived page puts together what no single file says, from several files and by a stated reasoning. Because a page restates its owners, it cannot drift from them.

### The map

The pages are made from a map, the documentation map. It has one entry per page. An entry holds the page's title, its one question, its kind, its reader, what it says, its inputs, the pages it links to with one sentence each, what it must not say, whether it is mirrored or derived, and its state. The entry's fields are listed on [Documentation map](../reference/documentation-map.md).

The map lies beside the owning project's ledger (the ledger is the state report made from the project's documents) and never in `docs/`, because a reader of the documentation would not understand it. Its header carries only its target and its owner. It carries no field that changes with a run, so the previous map is taken from git when a run needs it.

### The two agents

Two subagents make the documentation under one contract. A subagent is an agent that runs apart, sees nothing of the conversation and reads its inputs from disk. The contract owns what both share: their conduct, the kinds of a page, the voice and what must never reach a page.

- The planner reads the target and writes the map.
- A writer makes one page from its entry in the map and from the inputs the entry names, and sees no other page.

For the engine the planner reads these:

- the core file of the engine
- the skills
- the agents
- the settings
- the templates
- the help header of each script
- the owning project's briefs, intent, threads, solution design, decisions and recipes

For a project it reads these:

- its briefs, intent and threads
- the layers below the intent
- its ledger
- the indexes of its sources and research
- its recipes
- whatever those documents point to

It never reads the renders or the README of the target, since they are outputs of the documents and not their owners.

The pages are written in the project's language, as its artefacts are. The README stays English.

### One run

A run is made by `/document`, asks nothing, and goes in order:

```
previous map from git
        |
        v
   planner  --->  map (docs-map.md, beside the ledger)
        |
        v
   state script: hash every entry's inputs  --->  new / keep / regenerate / remove
        |
        v
   remove the pages marked remove
        |
        v
   one writer per new or regenerated page (one task file each)
        |
        v
   index script  --->  docs/README.md
        |
        v
   check script: broken links, long dashes, instance facts
        |
        v
   ledger remade; what the run could not place filed as a report
```

How to run it: [Generate the documentation](../use/generate-the-documentation.md).

### What is regenerated

A run regenerates only the pages whose inputs changed, and this is decided by hashes, never by judgement.

- Each input is hashed as the part of the file the entry names: a section by its heading or an item by its ID. A change elsewhere in the file leaves the page as it is.
- The rule the pages are made by is hashed with them: the writer's definition and the contract. Its whitespace is normalised first. A change of a sentence of the rule regenerates every page. A re-wrap of the rule regenerates nothing.
- A page that fails the check is regenerated once with the failure named. A page that fails twice is reported and left out of the documentation.

The mirrored pages are written by a faster model, because a mirrored page leaves a model no room. The derived pages are written by the model of the session, as the planner is. The model of the session is the one Claude is running on.

### Where and when it runs

A run is made on `main` only, and refuses a repository that is behind its origin or has diverged from it. The pages are taken as `ours` at a merge, and that rule turns round in the rebase of a save: a fresh page would silently lose to an older one.

A release by hand reports the age of the index against the intent's version and offers the command. A release with `--auto` asks once before anything runs. A release never regenerates the documentation on its own judgement, and the pages pass under the principal's eyes as every regenerated render does.

### A page is never mended by hand

The next run writes a page again from its owners, and a mend made on the page is gone. Only a mend in the file that owns the matter survives, and the page takes it at the next run. How a change is made: [Change a documentation page](../extend/change-a-documentation-page.md).

### What a run cannot place

Some things a run cannot place:

- a fact with no owner
- a matter on which the map and an owner disagree
- a reason that a page wants and no file records

Each is a finding of the run. The run files them in `reviews/` as a check's report and they are settled as a check's findings are, since the documentation finds what no other check does. A page does not carry a guess in their place: where a reason is not recorded, the page says so. The report shape and the settling are described on [The check](the-check.md). Nothing is invented to fill a gap, and a fact without an owner waits for the principal to give it a home.

## Why

- The README was once the whole documentation of the engine and was poor as one, because it was three things at once. A page of one topic can say a thing well, so that people inside the company and outside it can understand the forge and use it in full.
- A page comes from the project's documents with no hand in between. That is why the pages are not renders, and why there is no recipe per page: a recipe is a tool the principal shapes and iterates, and a page per recipe would mean as many recipes to iterate by hand as there are pages. The map replaces the recipes with one generated entry per page. What a render is: [Renders and recipes](renders-and-recipes.md).
- There is no site or wiki for now. The host shows Markdown pages and the README of a directory as they stand, so the pages are readable without a build, a host or a second place to keep current. A site stays possible later over the same pages.
- There is no hand-kept file of the philosophy in the project root. The why lives in the brief and the intent, and a hand-kept copy would drift from them. The pages about concepts are derived from those two.
- The previous map comes from git because the header of the map carries no field that changes with a run.
- The video folder is kept apart because it is public and the engine hosts it for projects that show a video there. The documentation is generated and checked around it.
- The language of the pages follows the project, as its artefacts do: [Languages](languages.md).
- The reason for the index carrying one question per page, beyond the manual reading it, is not recorded.

## A worked example

The shape of an entry of the map is plain and generic. This one is made up and belongs to no project.

```
### docs/use/<job>.md
- title: <the job, in the reader's words>
- line: <the one question the page answers>
- kind: how-to
- reader: user
- says: <what the page says, its one topic, the command spelled out>
- inputs:
  .claude/skills/<command>/SKILL.md
  CLAUDE.md#<Heading>
- links:
  `docs/reference/glossary.md`: every term of the forge in one line.
- must-not: <what the page must not say of its topic>
- made: mirrored
- state: new
```

On the next run the state script hashes the entry's text and the inputs it names, a part as that part, together with the rule the pages are made by. If the hash equals the one in the page's front-matter, the state is `keep` and nothing is written. If an input changed, the state is `regenerate` and one writer makes the page again.

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

Generated on 2026-11-01 for version 6.8 from the files the front-matter names; never edited by hand.
