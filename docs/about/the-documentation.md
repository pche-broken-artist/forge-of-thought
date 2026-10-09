---
generated: 2026-10-09
made: derived
inputs-hash: 988928e88c127707
inputs:
  - CLAUDE.md
  - .claude/skills/document/SKILL.md
  - .claude/agents/docs-planner.md
  - .claude/agents/docs-writer.md
  - projects/forge/10-intent.md
  - projects/forge/40-solution-design.md
---

# About the documentation

This page explains what the documentation of a project is, who it is
written for, how it is made and why it is made that way. It is for
anyone who reads the documentation, adds to the forge or wants to
understand how the forge documents itself. It was put together from
`CLAUDE.md`, the `/document` skill, the two documentation agents and
the forge's own intent and solution design.

## What it is

The documentation of a project, the engine's among them, is a set of
pages of one topic each, kept with the project in `docs/` and readable
wherever the project is published and in a clone. An index,
`docs/README.md`, lists every page and names each reader's path
through them. The pages and the index are what the reader sees;
nothing else of the documentation is meant for him.

The pages you are reading now are the engine's own documentation,
made by the same mechanism from the forge's own project.

## Three readers

The documentation is written for three readers, in this order of
weight:

1. **The user**, who clones the forge and forges his own thinking in
   it.
2. **The extender**, who adds to it: an artefact, a critic lens, a
   challenger persona, a recipe genre, a check, a command or a script.
3. **The evaluator**, who never runs it and wants to understand what
   it is and how it works. He gets the concept pages and nothing made
   for him alone.

## Five sections, three kinds of page

The outline follows the reader's journey and is the same for every
project. Each section is a directory under `docs/`:

- **start**: what the thing is in one paragraph, what must be on the
  machine, the first setup, the first result in one sitting. How-to
  pages for the user.
- **use**: one page per job the thing has a command or a procedure
  for, titled by the job. How-to pages for the user.
- **about**: what it is and is not, and why; how one thing travels
  through it; one page per concept and per kind of artefact or part,
  with the reasons. Explanation pages for all three readers; the
  reasons come from the owning project's brief and intent.
- **extend**: what it is made of; how a change is made, proved and
  recorded; one page per kind of addition. How-to pages, with the
  explanation they need, for the extender.
- **reference**: the commands, the rosters, the conventions, the
  layout, the scripts, the templates, the configuration, a glossary.
  Reference pages for all readers; they mirror their owners and never
  explain.

A section or a page with no material is left out, never left empty:
a project that is not installed has no install page, and that is no
gap.

Each page is of one kind, how-to, explanation or reference, opens
with what it is for and for whom, and stands on its own: a reader who
lands on it first understands it without another page. A how-to page
says what the person does and what he sees. An explanation page says
what a thing is, how it works and why. A reference page states facts
in the structure of what it mirrors, free of interpretation.

## Generated, never composed by hand

The documentation is generated from the project's documents and is
never composed or maintained by hand. Every page is one of two
things, and its front-matter says which:

- A **mirrored** page restates what the files that own its topic say,
  in the reader's words.
- A **derived** page puts together what no single file says, from
  named evidence in several files, by a stated reasoning. It says in
  its opening that it was put together from those files.

Nothing on a page comes from anywhere but its inputs. What the inputs
do not support is left out and reported, never guessed. This is why a
page cannot drift from what it mirrors: when something on a page is
wrong, the file that owns the matter is mended and the page is
regenerated, and no one edits the page.

Two kinds of document carry the documentation, both generated, neither
a source of truth:

- The **map**, `docs-map.md`, lies beside the owning project's ledger
  and is never shown to the reader. It holds one entry per page with
  everything a page is made from: the title, the kind, the reader,
  what the page says, its inputs as whole files, the pages it links to
  with a sentence each, what it must not say, whether it is mirrored
  or derived, and its state. It is read by scripts and by the writers
  of the pages, not by the reader of the documentation.
- The **pages** and their index live in `docs/`, overwritten by every
  run of the documentation.

## How a run works

One command makes the documentation, `/document [slug]`: bare, the
engine's into `docs/` at the engine root, from the forge's own
project; with a slug, that project's into its own `docs/`. The run
asks nothing. In short:

1. A planner reads the target on disk and writes the map.
2. A script compares the content of each entry's inputs with what the
   existing page was made from and marks each page as new, to
   regenerate, to keep or to remove. The state is the script's, never
   a judgement.
3. One writer per page makes each page alone, from its entry and the
   files the entry names, read from disk, nothing else. A mirrored
   page leaves the model no room, so it is written on a faster model;
   a derived page, like the plan, on the session model. The choice is
   made by the page's entry, never per run.
4. A script derives the index from the map, with the version of the
   owning project's intent.
5. A script checks the pages: every page of the map present and none
   beside it, every link resolving, no long dash, a front-matter on
   every page and no instance fact.

A run regenerates only the pages whose inputs changed, decided
mechanically from the content of the inputs, so that a run is cheap
and the page names stay stable.

The command is guarded like every command that writes: it never runs
on Claude's own judgement. A release does not regenerate the
documentation either: it reports the age of the index against the
intent's version and offers the command, so that the pages pass under
the principal's eyes as every regenerated render does.

## What never reaches a page

No instance fact reaches a page: no name of a person, no company, no
host, no address, no account. The engine carries none of these in its
files, but an agent that writes a page sees the whole context of the
session, memory included, and may take it for the file on disk. So
every agent that writes an outward-facing file is told that instance
facts are not material and that an input is read from disk, and the
generated pages are scanned for them mechanically before they are
kept.

## Why it is so

The README was the whole documentation of the engine and poor as one:
three things at once. A page of one topic can say a thing well, and
people inside an organisation and outside it should understand the
forge and use it in full. So the README is cut to what the thing is,
what one gets, how to start and where the documentation is; it is
English only, and a translation is a render.

Three other shapes were considered and dropped:

- **A recipe per page**, the documentation as renders. Dropped because
  tens of pages would mean tens of recipes to iterate by hand, and a
  recipe is a tool the principal shapes, while a page is to come from
  the project's documents with no hand in between. The generated map
  replaces the recipes, one entry per page. A page is therefore not a
  render: no recipe stands behind it, and `/render` is untouched.
- **A site or a wiki**, for now. Dropped because the host that
  publishes the repository shows Markdown pages and a directory's
  README as they stand, so pages in the repository are readable
  without a build, a host or a second place to keep current. A site
  stays possible later over the same pages.
- **A hand-kept file of the philosophy** in the project root. Dropped
  because the why lives in the brief and the intent already, and a
  hand-kept copy would drift from them; the About pages are derived
  from those two, and the pitch stays a render.

Some smaller choices follow from the same reasoning:

- The index is named `README.md` rather than `index.md`, because the
  host shows a directory's README as its front page.
- The map lies beside the ledger rather than in `docs/`, because a
  visitor of the documentation would not understand it.
- Facts no file owns, such as the install commands, the prerequisites
  and the public address of the repository, have one place in the
  project that both the README and the documentation read: a section
  of pinned facts in the project's readme recipe. A file of their own
  would need a kind of its own; the cost is that a render's tool
  carries facts of the project.

## See also

- [Generate the documentation](../use/generate-the-documentation.md): running `/document`.
- [Change a documentation page](../extend/change-a-documentation-page.md): changing a page through its owners.
- [Documentation map](../reference/documentation-map.md): the map's entry and the page's front-matter, field by field.
- [About renders and recipes](renders-and-recipes.md): the renders, which the pages are not.
