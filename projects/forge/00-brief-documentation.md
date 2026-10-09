---
project: forge
title: Documentation — generated pages of one topic each, for the engine and for any project
date: 2026-10-09
author: PCHe
version: 0.1
status: draft
last_change: 0.1 (2026-10-09): draft begun; born from THR.0340 (the rounds of 2026-10-05 and 2026-10-07) and the principal's word of the day.
---

<!-- Only this header is fixed; the text below it is free-form. The
rules: its definition, `.claude/skills/forge/states/brief.md`; the
history companion:
templates/history.md. -->

## What I want

The forge's documentation as a set of pages, one topic each, in
`docs/`, readable on GitHub and in a clone, with an index. Three
readers in this order: the user who clones the forge and forges his
own thinking; the extender who adds an artefact, a lens, a persona,
a genre or a check; the evaluator who never runs it and wants to
understand what it is and how it works. The evaluator gets the
concept pages and nothing made for him alone.

The documentation is generated, as automatically as possible. It is
not an artefact I maintain by walkthrough. Its definition belongs
neither in the intent nor in the solution design: the intent
receives one position, the design one part.

The same mechanism serves any project, not only the engine. Readers
and the outline are general: every project needs the same kind of
documentation. The outline is a standard one we agree on, filled
only where the project has material: a project that is not
installed has no install page, and that is no gap.

The README is cut to what the forge is, what one gets, how to start
and where the documentation is. English only; a translation, if
ever wanted, is a render.

## Why

The README is today the whole documentation and is poor as
documentation: very long, three things at once. People inside the
company and outside it should understand the forge and use its
potential in full. A page of one topic can say a thing well; a
derived page cannot drift from what it mirrors.

## How, as far as the mechanism is part of the idea

A command of its own, two phases, no question asked. First a
mapper, an isolated agent on the session model, carries the whole
assignment, reads the project on disk and writes the map: one row
per page, and the row is the page's brief: path, reader, what the
page says, its exact inputs, the pages it links to with one
sentence about each, what it must not say, and whether the page
mirrors its owners or is derived from evidence, with the evidence
named. Install, for instance, is derived: walk the scripts and
skills, see what the forge needs, put the procedure together. Then
one page maker per page, on a faster model, from its row, its
inputs and a fixed page template. The state of a page, new /
regenerate / keep / remove, is computed by a script from the
content hashes of its inputs, never by judgement, so a run
regenerates only what changed. Page names are stable.

The map lives in the project that owns the documentation, beside
the ledger, never in `docs/`; the index `docs/README.md` is derived
from it by the script, one line per page. `docs/` holds pages and
the index, nothing else.

Philosophy and why are derived from the brief and the intent; the
pitch stays a render. Facts no file owns, such as the public
address of the repository, get one place that both the
documentation and the README read. No instance fact reaches a page.

## What I do not want

A recipe per page. A site or a wiki now. Pages composed by hand.
Everything regenerated at every release. A hand-kept file of the
philosophy in the project root. Waiting for the engine split: pages
of one topic move whole. The "what's new" piece beside the release
notes: a round of its own, it stays in the brief `next-gen`. A
tutorial with a worked example: after a public exemplar exists.

## The outline

Five sections by the reader's journey, the same for every project;
a section or a page with no material is left out, never left empty.
Each page is of one kind: how-to, explanation or reference.

- **Start** (how-to, for the user): what the thing is in one
  paragraph; what must be on the machine and how it is installed;
  the first setup; the first result in one sitting. Mostly derived.
- **Use** (how-to, for the user): one page per job the thing has a
  command or a procedure for, titled by the job.
- **About** (explanation, for all three readers): what it is and is
  not, and why; how one thing travels through it; one page per
  concept; one page per kind of artefact or part. Derived from the
  brief and the intent, the reasons included.
- **Extend** (how-to with the explanation it needs, for the
  extender): what it is made of; how a change is made, proved and
  recorded; one page per kind of addition.
- **Reference** (derived fact, for all): the commands, the rosters,
  the conventions, the layout, the scripts, the templates, the
  configuration, a glossary. Mirrors its owners; never explains.

The index `docs/README.md` lists every page in one line, grouped by
section, and names the path of each reader through it. It is named
`README.md` because GitHub shows it as the front page of the
directory. Every page opens with what it is for and for whom, then
its matter, then the few pages it points to. Later, when there is
material: a tutorial with a worked example, troubleshooting, the
news.

## Material

`research/2026-10-03-how-project-documentation-is-built.md` (one
page one topic, the README orients and points, no empty structure,
journey-ordered sections in the field).
`research/2026-10-03-the-threshold-of-entry-for-a-non-developer.md`
(what install must cover). The round of 2026-10-07, recorded in
THR.0340: the trial made a map of 65 pages and three pages that
read well, and left five lessons: instance facts reach a subagent,
pages mirror stale owners, inputs must be exact paths, a page maker
cannot see other pages, pinned text lives in recipes.
`proposal-documentation.md` of 2026-10-05: its page map and its
section 11 are material, the rest is superseded.

## Still open

The standard outline, as agreed above, against the research. What
the documentation of a project other than the engine reads: a
project may be self-contained like the forge, a strategy that
generates a heap of files, a budgeting exercise, or carry a link to
an implementation in another repository; to be worked out after
the first version. The name and exact shape of the map, and where
the per-project definition of the documentation lives. The place
of the pinned facts. Where the mapper and the page maker are
defined, in the engine's operating layer as agents and a command;
and whether the page maker may run on a faster model while the
forge runs on one. How the pages are kept free of instance facts
(a rule, a scan by the state script; THR.0580 widened to the whole
session context). A mechanical check of the links. What a release
does with the documentation: regenerates, or reports its age.
Whether stale owners are mended before the first run or the first
version ships with known faults.
