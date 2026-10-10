---
generated: 2026-10-10
made: derived
inputs-hash: 2c473958f344d1c0
inputs:
  - CLAUDE.md
  - .claude/skills/document/SKILL.md
  - .claude/skills/docs-contract/SKILL.md
  - .claude/agents/docs-planner.md
  - .claude/agents/docs-writer.md
  - projects/forge/10-intent.md
  - projects/forge/40-solution-design.md
---

# About the documentation

This page explains what the documentation of a project is, who it is
written for, how it is made and why it is made that way. It is for
anyone who reads the documentation of the forge or of a project built
with it: the user who works with the thing, the extender who adds to
it, and the evaluator who only wants to understand it. It was put
together from `CLAUDE.md`, the `/document` skill, the contract and the
two agent definitions of the documentation, and the forge's own intent
and solution design.

## What the documentation is

The documentation of a project, the engine's among them, is a set of
pages in the directory `docs/`, one topic per page, kept with the
project. It is readable where the project is published and in a clone
alike: the pages are plain Markdown in the repository, so nothing has
to be built or hosted to read them. An index, `docs/README.md`, lists
every page and names each reader's path through them; it is derived
from the map by a script and carries the version of the project's
intent at the time of the run, so that a reader can tell how old the
documentation is.

The pages and the index are of one document kind, `page`: generated,
never a source of truth, overwritten by the documentation run. What
they are made from is the map, `docs-map.md`, of kind `map`: one entry
per page with everything that page is made from. The map lies beside
the ledger of the project that owns the documentation and is never
shown to the reader; it is read by the scripts and by the writers
only. For the engine the owning project is `forge`, and the pages land
in `docs/` at the engine root; for any other project the pages land in
that project's own `docs/`.

## The three readers

The documentation is written for three readers, in this order of
weight:

1. **The user**, who clones the thing and works with it.
2. **The extender**, who adds to it: an artefact, a lens, a persona, a
   genre, a check, a command or a script.
3. **The evaluator**, who never runs it and wants to understand what it
   is and how it works. He gets the concept pages and nothing made for
   him alone.

## The five sections

Every project's documentation has the same outline: five sections by
the reader's journey, each a directory under `docs/`. A section or a
page with no material is left out, never left empty: a project that is
not installed has no install page, and that is no gap.

- **Start** (how-to, for the user): what the thing is in one
  paragraph; what must be on the machine and how it is installed; the
  first setup; the first result in one sitting.
- **Use** (how-to, for the user): one page per job the thing has a
  command or a procedure for, titled by the job.
- **About** (explanation, for all three readers): what the thing is
  and is not, and why; how one thing travels through it; one page per
  concept; one page per kind of artefact or part. The reasons come
  from the owning project's brief and intent.
- **Extend** (how-to with the explanation it needs, for the extender):
  what the thing is made of; how a change is made, proved and
  recorded; one page per kind of addition.
- **Reference** (fact, for all): the commands, the rosters, the
  conventions, the layout, the scripts, the templates, the
  configuration, a glossary. It mirrors its owners and never explains.

## One topic, one kind, standing alone

Each page has one topic and is of one kind. A how-to page says what
the person does, step by step where there are steps, and what he sees.
An explanation page says what a thing is, how it works and why it is
so. A reference page states facts in the structure of what it
mirrors, free of interpretation. Every page opens with what it is for
and for whom, and stands on its own: a reader who lands on it first
understands it without another page. What is not of the page's topic
is a link to the page whose topic it is, and links go only to pages
of the same documentation.

## Generated, never composed by hand

No page is written or maintained by hand. A page is made in one of two
ways, and says which in its front-matter:

- A **mirrored** page restates what the files that own its topic say,
  in the reader's words.
- A **derived** page puts together what no single file says, from
  named evidence in several files: an install procedure from what the
  scripts require and the skills install, a glossary from the terms
  the files use. Its entry in the map says what it is derived from and
  by what reasoning, and the page says in its opening that it was put
  together from those files.

A page is never invented: what the inputs do not support is left out
and reported, never guessed. A fact that a page needs and no file owns
is listed in the map as unowned and waits for the owner of the
documentation to give it a home. This is why a page cannot drift from
what it mirrors: what is wrong on a page is mended in the file that
owns the matter, and the page is regenerated.

Facts that no file of the project would otherwise own, such as the
install commands, the prerequisites and the public address of the
repository, have one place in the project that both the README and
the documentation read: the pinned facts of the project's readme
recipe.

## How a run works

One command makes the documentation, `/document [slug]`: bare, it
documents the engine; with a slug, that project. It runs as one run
that asks nothing. Two agents and three scripts take part:

1. **The planner** reads the target on disk and writes the map: for
   the engine, `CLAUDE.md`, every skill, every agent, the settings,
   every template, the help header of every script, and the owning
   project's briefs, intent, threads, solution design, decisions and
   recipes. It never reads the renders or the README of the target,
   which are outputs, not owners. It writes no page.
2. **A script** computes the state of every page from the content of
   its inputs: which pages are new, which must be regenerated, which
   are kept and which are removed. Pages that lost their material are
   deleted.
3. **A writer per page** makes one page from its entry in the map and
   the files the entry names, read from disk, and nothing else. It
   sees no other page and no map beyond its entry; the one sentence
   beside each link is all it knows of the page it links to. A
   mirrored page leaves the model no room, so it is written on a
   faster model; a derived page, like the planner, is written on the
   session model. The choice is made by the page's entry, never per
   run.
4. **A script** derives the index from the map, and **a script**
   checks the pages: broken links, long dashes and instance facts.
   A page that fails the check is regenerated once with the failure
   named; a page that fails twice is left out of the documentation and
   reported, never mended by hand.

At the end the index gets a row in the ledger's Renders table of the
owning project, with the map as its input, and the run reports what it
made, what it left out and what the check found.

### One contract for both agents

The planner and the writer share their conduct through one contract,
as the forge's reviewers do. Neither sees anything of the conversation
that started it: its task is its whole brief. Every input is read from
disk in the run, because the copy of `CLAUDE.md` an agent carries in
its context is the session's and may be older than the file. Neither
asks a question: where something is unclear, it decides, says so in
what it writes, and moves on.

### What stays off a page

The contract also says what must never reach a page or the map: no
name of a person, no company, no host, no account, no e-mail, no
identifier of an instance; no address but the public home of the
project where its own documents name it as such; no document of any
project but the owning one; no instruction to the assistant copied
from a skill or an agent, since a page says what a command does for
the person, in the person's terms; no ID of the chain, since the
reason is given and its ID is not; and no long dash. The reason the
rule exists is that a subagent sees the session's whole context, the
assistant's memory included, and may take it for the file on disk; so
every agent that writes an outward-facing file is told that instance
facts are not material and that an input is read from disk, and the
generated files are scanned mechanically before they are kept.

## Only what changed is regenerated

A run regenerates only the pages whose inputs changed. The decision is
mechanical: every page carries a hash of the content of its inputs,
and a script compares it with the inputs on disk. Judgement plays no
part, so a run is cheap and the page names stay stable; a page's name
is the job or the topic, never a number.

A release never regenerates the documentation. It reports the age of
the index against the version of the intent and offers `/document`;
the pages then pass under the principal's eyes, as every regenerated
render does.

## Why it is so

The README was the whole documentation of the engine, and poor as one:
it was three things at once. A page of one topic can say a thing well,
and people both inside and outside the organisation that runs the
forge should be able to understand it and use it in full.

Three other ways were considered and dropped:

- **A recipe per page**, the documentation as renders of `/render`.
  Dozens of pages would mean dozens of recipes to iterate by hand, and
  a recipe is a tool the principal shapes, while a page is to come
  from the project's documents with no hand in between. The map
  replaces the recipes: one generated entry per page. A page is
  therefore not a render; no recipe stands behind it and `/render` is
  untouched.
- **A site or a wiki.** GitHub shows Markdown pages and the README of
  a directory as they stand, so pages in the repository are readable
  without a build, a host or a second place to keep current. A site
  stays possible later over the same pages.
- **A hand-kept file of the philosophy** in the project root. The why
  lives in the brief and the intent already, and a hand-kept copy
  would drift from them; the About pages are derived from those two,
  and the pitch stays a render.

Smaller choices follow the same reasoning. The documentation is a
command of its own rather than a use of `/render`, because a page has
no recipe to iterate and the map is generated. The index is named
`README.md` rather than `index.md`, because GitHub shows a directory's
README as its front page. The map lies beside the ledger rather than
in `docs/`, because a visitor of the documentation would not
understand it. The pinned facts live in the readme recipe rather than
in a file of their own, because a file would need a kind of its own
and the recipe is already read by both the README and the planner;
the cost is that a render's tool carries facts of the project.

## The README after the documentation

With the documentation in place, the README is cut to what orients and
points. Its chapters are the readme skeleton's,
`templates/recipe-readme.md`, the one owner of what a README carries.
The README is English only; a translation of it is a render.

## See also

- [Generate the documentation](../use/generate-the-documentation.md): running `/document`.
- [Change a documentation page](../extend/change-a-documentation-page.md): changing a page through its owners.
- [Documentation map](../reference/documentation-map.md): the map's entry and the page's front-matter, field by field.
- [About renders and recipes](renders-and-recipes.md): the renders, which the pages are not.
